import { describe, expect, it, vi } from "vitest"

import {
  parseDeployHookUrl,
  requestVercelDeployment,
  runDeployCli,
} from "../../../scripts/deploy-vercel.mjs"

const hookUrl =
  "https://api.vercel.com/v1/integrations/deploy/project-id/hook-secret"

function jsonResponse(body: unknown, status = 200, statusText = "OK") {
  return {
    ok: status >= 200 && status < 300,
    status,
    statusText,
    json: vi.fn().mockResolvedValue(body),
  }
}

describe("Vercel Deploy Hook validation", () => {
  it("accepts the documented Vercel Deploy Hook shape", () => {
    const parsed = parseDeployHookUrl(hookUrl)

    expect(parsed.hostname).toBe("api.vercel.com")
    expect(parsed.pathname).toBe(
      "/v1/integrations/deploy/project-id/hook-secret"
    )
  })

  it.each([
    undefined,
    "not-a-url",
    "http://api.vercel.com/v1/integrations/deploy/project-id/hook-secret",
    "https://example.com/v1/integrations/deploy/project-id/hook-secret",
    "https://api.vercel.com/not-a-deploy-hook",
    `${hookUrl}?leak=true`,
  ])("rejects unsafe configuration before a request: %s", async (value) => {
    const fetchImpl = vi.fn()

    await expect(
      requestVercelDeployment({ deployHookUrl: value, fetchImpl })
    ).rejects.toThrow()
    expect(fetchImpl).not.toHaveBeenCalled()
  })
})

describe("Vercel deployment request", () => {
  it("sends one POST and returns non-secret job evidence", async () => {
    const fetchImpl = vi
      .fn()
      .mockResolvedValue(
        jsonResponse({ job: { id: "job-123", state: "PENDING" } })
      )

    await expect(
      requestVercelDeployment({ deployHookUrl: hookUrl, fetchImpl })
    ).resolves.toEqual({ jobId: "job-123", state: "PENDING" })
    expect(fetchImpl).toHaveBeenCalledTimes(1)
    expect(fetchImpl).toHaveBeenCalledWith(
      new URL(hookUrl),
      expect.objectContaining({
        method: "POST",
        headers: { accept: "application/json" },
        signal: expect.any(AbortSignal),
      })
    )
  })

  it("reports network failure without exposing the hook URL", async () => {
    const fetchImpl = vi.fn().mockRejectedValue(new Error(`failed ${hookUrl}`))

    await expect(
      requestVercelDeployment({ deployHookUrl: hookUrl, fetchImpl })
    ).rejects.toThrow("Unable to reach Vercel")
  })

  it("reports a rejected response without echoing its body", async () => {
    const response = jsonResponse(
      { message: `do not print ${hookUrl}` },
      429,
      "Too Many Requests"
    )
    const fetchImpl = vi.fn().mockResolvedValue(response)

    await expect(
      requestVercelDeployment({ deployHookUrl: hookUrl, fetchImpl })
    ).rejects.toThrow(
      "Vercel rejected the deployment request (429 Too Many Requests)"
    )
    expect(response.json).not.toHaveBeenCalled()
  })

  it.each([
    { body: {}, label: "missing job" },
    { body: { job: { id: "" } }, label: "empty job ID" },
  ])("rejects an invalid success response: $label", async ({ body }) => {
    const fetchImpl = vi.fn().mockResolvedValue(jsonResponse(body))

    await expect(
      requestVercelDeployment({ deployHookUrl: hookUrl, fetchImpl })
    ).rejects.toThrow("Vercel returned an invalid deployment response")
  })

  it("rejects non-JSON success responses", async () => {
    const response = jsonResponse({})
    response.json.mockRejectedValue(new SyntaxError("invalid JSON"))
    const fetchImpl = vi.fn().mockResolvedValue(response)

    await expect(
      requestVercelDeployment({ deployHookUrl: hookUrl, fetchImpl })
    ).rejects.toThrow("Vercel returned an invalid deployment response")
  })
})

describe("deployment command", () => {
  it("prints only non-secret success evidence", async () => {
    const writeOutput = vi.fn()
    const writeError = vi.fn()

    await expect(
      runDeployCli({
        env: { VERCEL_DEPLOY_HOOK_URL: hookUrl },
        fetchImpl: vi
          .fn()
          .mockResolvedValue(
            jsonResponse({ job: { id: "job-123", state: "PENDING" } })
          ),
        writeOutput,
        writeError,
      })
    ).resolves.toBe(0)
    expect(writeOutput).toHaveBeenCalledWith(
      "Vercel deployment accepted: job job-123 (PENDING)."
    )
    expect(JSON.stringify(writeOutput.mock.calls)).not.toContain(hookUrl)
    expect(writeError).not.toHaveBeenCalled()
  })

  it("returns nonzero with a useful missing-configuration error", async () => {
    const fetchImpl = vi.fn()
    const writeError = vi.fn()

    await expect(
      runDeployCli({ env: {}, fetchImpl, writeError, writeOutput: vi.fn() })
    ).resolves.toBe(1)
    expect(fetchImpl).not.toHaveBeenCalled()
    expect(writeError).toHaveBeenCalledWith(
      "Deployment failed: Missing VERCEL_DEPLOY_HOOK_URL. Add it to .env.local before deploying."
    )
  })
})
