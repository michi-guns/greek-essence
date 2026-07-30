# Greek Essence

Greek Essence is a public source repository for a bilingual client-review prototype of a Greece-focused travel-planning service.

## Getting started

New contributors should follow the complete [contributor onboarding guide](docs/CONTRIBUTOR_ONBOARDING.md). It provides dedicated Windows, macOS, and Ubuntu/Debian setup paths covering the required Node.js, pnpm, Git, Gitleaks, and Playwright installations; repository cloning; pnpm build-script approvals; environment configuration; Git hooks; and verification commands.

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

Bootstrap tooling and the bilingual fixture scaffold are complete, and prototype implementation is in progress. This repository does not implement booking, payments, accounts, or analytics.

## Development

Use standalone pnpm `11.17.0` directly:

```bash
pnpm install --frozen-lockfile
pnpm dev
```

### Manual production deployment

Git pushes do not deploy this project to Vercel. The supported production
deployment workflow always builds the latest commit on the `main` branch linked
to the Vercel Deploy Hook, regardless of the caller's local branch.

Add the operator-provided hook to ignored `.env.local`:

```dotenv
VERCEL_DEPLOY_HOOK_URL=https://api.vercel.com/v1/integrations/deploy/...
```

Then deliberately trigger one deployment:

```bash
pnpm deploy:vercel
```

The command prints the accepted Vercel job ID and state but never the hook URL.
Vercel account access, hook creation, and hook rotation remain operator
responsibilities.

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

Run `pnpm secrets:scan` to scan committed Git history manually. Husky runs the
redacted scan for every push: directly for Markdown-only changes and through
`pnpm check:push` for all other changes. GitHub Actions also scans proposed
changes. A detected secret blocks delivery without printing its value. Treat a
real finding as compromised: revoke or rotate it, remove it from the proposed
commits, and rerun the scan. Only suppress a verified false positive after
review; do not ignore a real or unexplained finding.

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
