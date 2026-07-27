# Greek Essence

Greek Essence is a public source repository for a bilingual client-review prototype of a Greece-focused travel-planning service.

## Getting started

New contributors should follow the complete [contributor onboarding guide](docs/CONTRIBUTOR_ONBOARDING.md). It covers the required Node.js, pnpm, Git, Gitleaks, and Playwright installations; repository cloning; pnpm build-script approvals; environment configuration; Git hooks; and verification commands.

After installing the documented prerequisites:

```bash
pnpm install --frozen-lockfile
pnpm exec playwright install chromium
pnpm run doctor
pnpm dev
```

Local environment overrides are optional. Copy [`.env.example`](.env.example) to `.env.local` when you want to make the development defaults explicit.

## Documentation

- [Documentation entry point](docs/README.md)
- [Contributor onboarding](docs/CONTRIBUTOR_ONBOARDING.md)
- [Bootstrap workspace](.scratch/bootstrap/README.md)

Bootstrap tooling and the bilingual fixture scaffold are complete, and prototype implementation is in progress. This repository does not implement booking, payments, accounts, analytics, or production operations.

## Development

Use standalone pnpm `11.17.0` directly:

```bash
pnpm install --frozen-lockfile
pnpm dev
```

On Windows, install the repository-pinned version with the official PowerShell installer, then open a refreshed terminal:

```powershell
$env:PNPM_VERSION = "11.17.0"
irm https://get.pnpm.io/install.ps1 | iex
```

### Secret scanning

Install Gitleaks `8.30.1` or newer before the first push. On Windows, install the
official package with Windows Package Manager, then open a refreshed terminal:

```powershell
winget install --id Gitleaks.Gitleaks --exact
gitleaks version
```

On macOS, use `brew install gitleaks`. On Linux, install the appropriate binary
from the [official Gitleaks releases](https://github.com/gitleaks/gitleaks/releases).

Run `pnpm secrets:scan` to scan committed Git history manually. Husky also runs
the redacted scan as the first part of `pnpm check:push`, so a detected secret
blocks the push without printing its value. Treat a real finding as compromised:
revoke or rotate it, remove it from the proposed commits, and rerun the scan.
Only suppress a verified false positive after review; do not ignore a real or
unexplained finding.

### Dependency auditing

Run `pnpm security:audit` to query the registry for high- and critical-severity
advisories affecting the installed dependency graph. Husky runs this strict
audit during `pnpm check:push`; registry errors and security findings both block
the push. Review and update the affected dependency deliberately. Do not run
`pnpm audit --fix` without inspecting the proposed lockfile or override changes.

### Unit-test coverage

Run `pnpm test:unit:coverage` to generate a terminal summary and an ignored HTML
report under `coverage/`. The coverage gate requires at least 80% statements,
branches, functions, and lines across the unit-testable source files selected in
`vitest.config.mts`. Husky runs coverage during `pnpm check:push` instead of
repeating the normal unit-test command. Adjust the thresholds deliberately as
the supported logic grows; coverage indicates execution, not assertion quality.
