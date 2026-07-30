import { describe, expect, it, vi } from "vitest"

import {
  classifyChangedPaths,
  packageScriptInvocation,
  parseNulPaths,
  resolvePrePushRanges,
} from "../../../scripts/change-gates.mjs"

const zero = "0".repeat(40)
const local = "a".repeat(40)
const remote = "b".repeat(40)

describe("Markdown-only change classification", () => {
  it("accepts non-empty Markdown and MDX path sets", () => {
    expect(
      classifyChangedPaths([
        "README.md",
        "docs/guide.MD",
        "content/example.mdx",
      ])
    ).toEqual({
      kind: "markdown-only",
      paths: ["README.md", "content/example.mdx", "docs/guide.MD"],
    })
  })

  it("uses full checks for mixed changes", () => {
    expect(classifyChangedPaths(["README.md", "package.json"]).kind).toBe(
      "full"
    )
  })

  it("uses full checks for an empty change set", () => {
    expect(classifyChangedPaths([])).toEqual({ kind: "full", paths: [] })
  })

  it("deduplicates paths from multiple pushed refs", () => {
    expect(classifyChangedPaths(["docs/a.md", "docs/a.md"]).paths).toEqual([
      "docs/a.md",
    ])
  })

  it("preserves whitespace in NUL-delimited Git paths", () => {
    expect(parseNulPaths(" docs/a.md\0docs/b .md\0")).toEqual([
      " docs/a.md",
      "docs/b .md",
    ])
  })
})

describe("pre-push range resolution", () => {
  it("compares an existing remote ref from its advertised SHA", () => {
    const mergeBase = vi.fn()

    expect(
      resolvePrePushRanges(
        `refs/heads/docs ${local} refs/heads/docs ${remote}\n`,
        "origin",
        mergeBase
      )
    ).toEqual([{ base: remote, head: local }])
    expect(mergeBase).not.toHaveBeenCalled()
  })

  it("compares a new branch from its merge base with remote main", () => {
    const mergeBase = vi.fn(() => remote)

    expect(
      resolvePrePushRanges(
        `refs/heads/docs ${local} refs/heads/docs ${zero}\n`,
        "origin",
        mergeBase
      )
    ).toEqual([{ base: remote, head: local }])
    expect(mergeBase).toHaveBeenCalledWith(local, "origin/main")
  })

  it("fails closed when a new branch merge base is unavailable", () => {
    expect(
      resolvePrePushRanges(
        `refs/heads/docs ${local} refs/heads/docs ${zero}\n`,
        "origin",
        () => undefined
      )
    ).toBeUndefined()
  })

  it("ignores deleted refs but fails closed when no pushed range remains", () => {
    expect(
      resolvePrePushRanges(
        `refs/heads/docs ${zero} refs/heads/docs ${remote}\n`,
        "origin",
        vi.fn()
      )
    ).toBeUndefined()
  })

  it("fails closed for malformed hook input", () => {
    expect(
      resolvePrePushRanges("not a valid ref update\n", "origin", vi.fn())
    ).toBeUndefined()
  })

  it("fails closed when hook SHAs are malformed", () => {
    expect(
      resolvePrePushRanges(
        "refs/heads/docs not-a-sha refs/heads/docs also-not-a-sha\n",
        "origin",
        vi.fn()
      )
    ).toBeUndefined()
  })
})

describe("package script execution", () => {
  it("uses the Windows command interpreter for standalone pnpm", () => {
    expect(packageScriptInvocation("win32", "check", "cmd.exe")).toEqual({
      command: "cmd.exe",
      args: ["/d", "/s", "/c", "pnpm check"],
    })
  })

  it("invokes pnpm directly on non-Windows platforms", () => {
    expect(packageScriptInvocation("linux", "check", "")).toEqual({
      command: "pnpm",
      args: ["check"],
    })
  })

  it("rejects unknown package scripts", () => {
    expect(() =>
      packageScriptInvocation("linux", "arbitrary-command", "")
    ).toThrow("Unsupported package script")
  })
})
