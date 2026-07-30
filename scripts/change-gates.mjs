import { spawnSync } from "node:child_process"
import { readFileSync } from "node:fs"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..")
const allowedPackageScripts = new Set(["check", "check:push", "secrets:scan"])
const shaPattern = /^[0-9a-f]{40,64}$/i
const zeroShaPattern = /^0{40,64}$/

export function classifyChangedPaths(paths) {
  const uniquePaths = [...new Set(paths)].sort()
  const markdownOnly =
    uniquePaths.length > 0 && uniquePaths.every((path) => /\.mdx?$/i.test(path))

  return {
    kind: markdownOnly ? "markdown-only" : "full",
    paths: uniquePaths,
  }
}

export function parseNulPaths(output) {
  return output.split("\0").filter(Boolean)
}

export function resolvePrePushRanges(input, remoteName, mergeBase) {
  const ranges = []
  const lines = input.split(/\r?\n/).filter(Boolean)

  for (const line of lines) {
    const fields = line.trim().split(/\s+/)
    if (fields.length !== 4) return undefined

    const [, localSha, , remoteSha] = fields
    if (!shaPattern.test(localSha) || !shaPattern.test(remoteSha))
      return undefined
    if (zeroShaPattern.test(localSha)) continue

    if (!zeroShaPattern.test(remoteSha)) {
      ranges.push({ base: remoteSha, head: localSha })
      continue
    }

    const base = mergeBase(localSha, `${remoteName}/main`)
    if (!base) return undefined
    ranges.push({ base, head: localSha })
  }

  return ranges.length > 0 ? ranges : undefined
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: root,
    encoding: "utf8",
    stdio: options.capture ? "pipe" : "inherit",
    windowsHide: true,
  })

  if (result.error || result.status !== 0) return undefined
  return options.capture ? result.stdout : ""
}

function gitOutput(args) {
  return run("git", args, { capture: true })
}

function changedPathsForRanges(ranges) {
  if (!ranges) return undefined

  const paths = []
  for (const { base, head } of ranges) {
    const output = gitOutput([
      "diff",
      "--no-renames",
      "--name-only",
      "-z",
      base,
      head,
      "--",
    ])
    if (output === undefined) return undefined
    paths.push(...parseNulPaths(output))
  }
  return paths
}

export function packageScriptInvocation(platform, script, commandInterpreter) {
  if (!allowedPackageScripts.has(script)) {
    throw new Error(`Unsupported package script: ${script}`)
  }

  return platform === "win32"
    ? {
        command: commandInterpreter || "cmd.exe",
        args: ["/d", "/s", "/c", `pnpm ${script}`],
      }
    : { command: "pnpm", args: [script] }
}

function runPackageScript(script) {
  const invocation = packageScriptInvocation(
    process.platform,
    script,
    process.env.ComSpec
  )
  return run(invocation.command, invocation.args) !== undefined
}

function runPrettier(paths) {
  return (
    run(process.execPath, [
      resolve(root, "node_modules/prettier/bin/prettier.cjs"),
      "--check",
      "--ignore-path",
      ".gitignore",
      "--",
      ...paths,
    ]) !== undefined
  )
}

function runSelectedGates(paths, fullScript, scanSecrets) {
  const classification = classifyChangedPaths(paths ?? [])

  if (classification.kind === "markdown-only") {
    console.log(
      `Markdown-only change detected (${classification.paths.length} file${classification.paths.length === 1 ? "" : "s"}).`
    )
    if (scanSecrets && !runPackageScript("secrets:scan")) return 1
    return runPrettier(classification.paths) ? 0 : 1
  }

  console.log("Mixed or uncertain change scope; running full checks.")
  try {
    return runPackageScript(fullScript) ? 0 : 1
  } catch (error) {
    console.error(error.message)
    return 1
  }
}

function mergeBase(left, right) {
  return gitOutput(["merge-base", left, right])?.trim() || undefined
}

function runCli() {
  const [, , mode, ...args] = process.argv

  if (mode === "range") {
    const [base, head, fullScript = "check"] = args
    const ranges = base && head ? [{ base, head }] : undefined
    return runSelectedGates(
      changedPathsForRanges(ranges),
      fullScript,
      args.includes("--secrets")
    )
  }

  if (mode === "pre-push") {
    const [remoteName] = args
    const input = readFileSync(0, "utf8")
    const ranges = remoteName
      ? resolvePrePushRanges(input, remoteName, mergeBase)
      : undefined
    return runSelectedGates(changedPathsForRanges(ranges), "check:push", true)
  }

  console.error("Usage: change-gates.mjs range|pre-push ...")
  return 1
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  process.exitCode = runCli()
}
