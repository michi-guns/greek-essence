import { describe, expect, it, vi } from "vitest"

import {
  classifyChangedPaths,
  collectRangeChanges,
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

describe("pushed-tree Markdown collection", () => {
  it("does not read blobs after a mixed range selects full checks", () => {
    const git = vi.fn((args: string[]) => {
      if (args[0] === "diff") return "README.md\0public/image.jpg\0"
      throw new Error("mixed ranges must not read blobs")
    })

    expect(collectRangeChanges([{ base: "base", head: "head" }], git)).toEqual({
      paths: ["README.md", "public/image.jpg"],
      files: [],
    })
    expect(git).toHaveBeenCalledTimes(1)
  })

  it("reads surviving files from the pushed commit and excludes deletions", () => {
    const hash = "c".repeat(40)
    const git = vi.fn((args: string[]) => {
      if (args[0] === "diff") return "docs/old.md\0docs/new.md\0"
      if (args[0] === "ls-tree" && args.at(-1) === ":(literal)docs/old.md")
        return ""
      if (args[0] === "ls-tree") return `100644 blob ${hash}\tdocs/new.md\0`
      if (args[0] === "cat-file")
        throw new Error("blob contents must not be captured in memory")
      return undefined
    })

    expect(collectRangeChanges([{ base: "base", head: "head" }], git)).toEqual({
      paths: ["docs/old.md", "docs/new.md"],
      files: [
        {
          head: "head",
          path: "docs/new.md",
          blob: hash,
        },
      ],
    })
  })

  it("keeps a pure Markdown deletion on the fast path without a file to format", () => {
    const git = vi.fn((args: string[]) =>
      args[0] === "diff" ? "docs/removed.md\0" : ""
    )

    const changes = collectRangeChanges([{ base: "base", head: "head" }], git)

    expect(changes).toEqual({ paths: ["docs/removed.md"], files: [] })
    expect(classifyChangedPaths(changes?.paths ?? []).kind).toBe(
      "markdown-only"
    )
  })

  it("fails closed when a surviving tree entry is not a blob", () => {
    const git = vi.fn((args: string[]) => {
      if (args[0] === "diff") return "docs/file.md\0"
      if (args[0] === "ls-tree") return "040000 tree invalid\tdocs/file.md\0"
      return undefined
    })

    expect(
      collectRangeChanges([{ base: "base", head: "head" }], git)
    ).toBeUndefined()
  })
})
