import { spawnSync } from "node:child_process"
import { existsSync, readFileSync } from "node:fs"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..")
const packageJson = JSON.parse(
  readFileSync(resolve(root, "package.json"), "utf8")
)
const expectedNode = readFileSync(resolve(root, ".node-version"), "utf8").trim()
const expectedPnpm = packageJson.packageManager.replace(/^pnpm@/, "")
const minimumGitleaks = "8.30.1"
const results = []

function result(status, name, detail) {
  results.push({ status, name, detail })
}

function run(command, args) {
  const execution = spawnSync(command, args, {
    cwd: root,
    encoding: "utf8",
    windowsHide: true,
  })

  return {
    ok: execution.status === 0,
    output: `${execution.stdout ?? ""}\n${execution.stderr ?? ""}`.trim(),
  }
}

function versionFrom(value) {
  const match = value.match(/v?(\d+)\.(\d+)\.(\d+)/)
  return match ? match.slice(1, 4).map(Number) : undefined
}

function compareVersions(left, right) {
  const leftParts = versionFrom(left)
  const rightParts = versionFrom(right)
  if (!leftParts || !rightParts) return undefined

  for (let index = 0; index < leftParts.length; index += 1) {
    if (leftParts[index] !== rightParts[index])
      return leftParts[index] - rightParts[index]
  }
  return 0
}

function checkCommand(name, command, args, validate, remediation) {
  const execution = run(command, args)
  if (!execution.ok) {
    result("FAIL", name, remediation)
    return
  }

  const validation = validate(execution.output)
  result(validation.ok ? "PASS" : "FAIL", name, validation.detail)
}

console.log("Greek Essence doctor\n")

result(
  existsSync(resolve(root, ".git")) ? "PASS" : "FAIL",
  "Git checkout",
  existsSync(resolve(root, ".git"))
    ? root
    : "Clone the repository with Git; source archives do not configure hooks."
)

checkCommand(
  "Git",
  "git",
  ["--version"],
  (output) => ({ ok: true, detail: output }),
  "Install Git and open a new terminal."
)

const actualNode = process.versions.node
result(
  actualNode === expectedNode ? "PASS" : "FAIL",
  "Node.js",
  actualNode === expectedNode
    ? `v${actualNode}`
    : `Expected v${expectedNode}; found v${actualNode}. Follow .node-version.`
)

const actualPnpm = process.env.npm_config_user_agent?.match(
  /\bpnpm\/(\d+\.\d+\.\d+)/
)?.[1]
result(
  actualPnpm === expectedPnpm ? "PASS" : "FAIL",
  "pnpm",
  actualPnpm === expectedPnpm
    ? actualPnpm
    : actualPnpm
      ? `Expected ${expectedPnpm}; found ${actualPnpm}.`
      : `Run the doctor through standalone pnpm ${expectedPnpm}: pnpm run doctor.`
)

checkCommand(
  "Gitleaks",
  "gitleaks",
  ["version"],
  (output) => {
    const comparison = compareVersions(output, minimumGitleaks)
    return {
      ok: comparison !== undefined && comparison >= 0,
      detail:
        comparison !== undefined && comparison >= 0
          ? output
          : `Expected ${minimumGitleaks} or newer; found ${output || "an unknown version"}.`,
    }
  },
  `Install Gitleaks ${minimumGitleaks} or newer and open a new terminal.`
)

const dependenciesInstalled = existsSync(
  resolve(root, "node_modules", ".modules.yaml")
)
result(
  dependenciesInstalled ? "PASS" : "FAIL",
  "Dependencies",
  dependenciesInstalled
    ? "node_modules is present."
    : "Run pnpm install --frozen-lockfile."
)

const hooksPath = run("git", ["config", "--get", "core.hooksPath"])
const normalizedHooksPath = hooksPath.output.replaceAll("\\", "/")
result(
  hooksPath.ok && normalizedHooksPath === ".husky/_" ? "PASS" : "FAIL",
  "Husky hooks",
  hooksPath.ok && normalizedHooksPath === ".husky/_"
    ? normalizedHooksPath
    : "Run pnpm install --frozen-lockfile to configure the repository hooks."
)

const environmentConfigured = [".env.local", ".env.development.local"].some(
  (file) => existsSync(resolve(root, file))
)
result(
  environmentConfigured ? "PASS" : "WARN",
  "Local environment",
  environmentConfigured
    ? "A local environment file is present."
    : "No local override found; documented development defaults will be used."
)

if (!dependenciesInstalled) {
  result(
    "FAIL",
    "Playwright Chromium",
    "Install dependencies, then run pnpm exec playwright install chromium."
  )
} else {
  try {
    const { chromium } = await import("playwright-core")
    const executablePath = chromium.executablePath()
    result(
      existsSync(executablePath) ? "PASS" : "FAIL",
      "Playwright Chromium",
      existsSync(executablePath)
        ? executablePath
        : "Run pnpm exec playwright install chromium."
    )
  } catch {
    result(
      "FAIL",
      "Playwright Chromium",
      "Could not load Playwright. Run pnpm install --frozen-lockfile."
    )
  }
}

for (const { status, name, detail } of results)
  console.log(`[${status}] ${name}: ${detail}`)

const failures = results.filter(({ status }) => status === "FAIL").length
const warnings = results.filter(({ status }) => status === "WARN").length

console.log(
  `\nDoctor completed with ${failures} failure${failures === 1 ? "" : "s"} and ${warnings} warning${warnings === 1 ? "" : "s"}.`
)

if (failures > 0) process.exitCode = 1
