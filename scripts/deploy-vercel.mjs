import { resolve } from "node:path"
import { fileURLToPath } from "node:url"

const VARIABLE_NAME = "VERCEL_DEPLOY_HOOK_URL"
const VERCEL_HOST = "api.vercel.com"
const DEPLOY_HOOK_PATH = /^\/v1\/integrations\/deploy\/[^/]+\/[^/]+\/?$/
const REQUEST_TIMEOUT_MS = 30_000

export function parseDeployHookUrl(value) {
  if (!value) {
    throw new Error(
      `Missing ${VARIABLE_NAME}. Add it to .env.local before deploying.`
    )
  }

  let url

  try {
    url = new URL(value)
  } catch {
    throw new Error(`${VARIABLE_NAME} is not a valid URL.`)
  }

  if (
    url.protocol !== "https:" ||
    url.hostname !== VERCEL_HOST ||
    url.port ||
    url.username ||
    url.password ||
    url.search ||
    url.hash ||
    !DEPLOY_HOOK_PATH.test(url.pathname)
  ) {
    throw new Error(`${VARIABLE_NAME} is not a valid Vercel Deploy Hook URL.`)
  }

  return url
}

export async function requestVercelDeployment({
  deployHookUrl,
  fetchImpl = globalThis.fetch,
}) {
  const url = parseDeployHookUrl(deployHookUrl)
  let response

  try {
    response = await fetchImpl(url, {
      method: "POST",
      headers: { accept: "application/json" },
      signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
    })
  } catch {
    throw new Error("Unable to reach Vercel.")
  }

  if (!response.ok) {
    const status = [response.status, response.statusText]
      .filter(Boolean)
      .join(" ")
    throw new Error(`Vercel rejected the deployment request (${status}).`)
  }

  let responseBody

  try {
    responseBody = await response.json()
  } catch {
    throw new Error("Vercel returned an invalid deployment response.")
  }

  const jobId = responseBody?.job?.id
  const state = responseBody?.job?.state

  if (typeof jobId !== "string" || !jobId) {
    throw new Error("Vercel returned an invalid deployment response.")
  }

  return {
    jobId,
    state: typeof state === "string" && state ? state : "UNKNOWN",
  }
}

export async function runDeployCli({
  env = process.env,
  fetchImpl = globalThis.fetch,
  writeOutput = console.log,
  writeError = console.error,
} = {}) {
  try {
    const result = await requestVercelDeployment({
      deployHookUrl: env[VARIABLE_NAME],
      fetchImpl,
    })

    writeOutput(
      `Vercel deployment accepted: job ${result.jobId} (${result.state}).`
    )
    return 0
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown error."
    writeError(`Deployment failed: ${message}`)
    return 1
  }
}

const isMain =
  process.argv[1] &&
  resolve(process.argv[1]) === resolve(fileURLToPath(import.meta.url))

if (isMain) {
  process.exitCode = await runDeployCli()
}
