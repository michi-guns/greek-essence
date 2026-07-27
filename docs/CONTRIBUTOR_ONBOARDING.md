# Contributor onboarding

This guide takes a new Greek Essence contributor from a clean machine to a verified local development environment. Run commands from the repository root unless a step says otherwise.

## 1. Install the required tools

Use the instructions for your operating system. All three paths install Git, the exact Node.js version recorded in [`.node-version`](../.node-version), standalone pnpm from [`package.json`](../package.json), and Gitleaks. Do not substitute npm, Yarn, Corepack, or another package manager for pnpm.

### Windows 11 with PowerShell

Install Git, [fnm](https://github.com/Schniz/fnm), and Gitleaks through Windows Package Manager:

```powershell
winget install --id Git.Git --exact
winget install --id Schniz.fnm --exact
winget install --id Gitleaks.Gitleaks --exact
```

Open a new PowerShell terminal. Add the following line to your PowerShell profile so fnm selects the repository's Node version when you enter its directory:

```powershell
fnm env --use-on-cd --shell powershell | Out-String | Invoke-Expression
```

Run that line in the current terminal as well, then install the pinned Node.js release:

```powershell
fnm install 24.18.0
fnm use 24.18.0
```

Install standalone pnpm with its official PowerShell installer, then open one more refreshed terminal:

```powershell
$env:PNPM_VERSION = "11.17.0"
irm https://get.pnpm.io/install.ps1 | iex
```

### macOS with zsh

Install [Homebrew](https://brew.sh/) if it is not already available:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow Homebrew's printed PATH instructions, then install Git, fnm, and Gitleaks:

```bash
brew install git fnm gitleaks
```

Add this line to `~/.zshrc`, and run it once in the current terminal:

```bash
eval "$(fnm env --use-on-cd --shell zsh)"
```

Install the pinned Node.js and standalone pnpm versions:

```bash
fnm install 24.18.0
fnm use 24.18.0
curl -fsSL https://get.pnpm.io/install.sh | env PNPM_VERSION=11.17.0 sh -
```

Open a refreshed terminal before continuing.

### Ubuntu or Debian with bash

Install the base packages from the operating-system repository:

```bash
sudo apt update
sudo apt install --yes ca-certificates curl git tar unzip
```

Install fnm with its official script. The installer adds the fnm loader to your shell configuration:

```bash
curl -fsSL https://fnm.vercel.app/install | bash
```

Open a refreshed terminal, or load fnm in the current Bash session, then install Node.js:

```bash
eval "$(fnm env --use-on-cd --shell bash)"
fnm install 24.18.0
fnm use 24.18.0
```

Install standalone pnpm:

```bash
curl -fsSL https://get.pnpm.io/install.sh | env PNPM_VERSION=11.17.0 sh -
```

Gitleaks does not provide an official apt repository. Download the pinned official release for the machine architecture and verify it against the published checksums before installing it:

```bash
gitleaks_version="8.30.1"
case "$(uname -m)" in
  x86_64) gitleaks_arch="x64" ;;
  aarch64|arm64) gitleaks_arch="arm64" ;;
  *) echo "Unsupported architecture: $(uname -m)" >&2; exit 1 ;;
esac
gitleaks_archive="gitleaks_${gitleaks_version}_linux_${gitleaks_arch}.tar.gz"
gitleaks_tmp="$(mktemp -d)"
curl -fL "https://github.com/gitleaks/gitleaks/releases/download/v${gitleaks_version}/${gitleaks_archive}" -o "${gitleaks_tmp}/${gitleaks_archive}"
curl -fL "https://github.com/gitleaks/gitleaks/releases/download/v${gitleaks_version}/gitleaks_${gitleaks_version}_checksums.txt" -o "${gitleaks_tmp}/checksums.txt"
(cd "${gitleaks_tmp}" && sha256sum --check --ignore-missing checksums.txt)
tar -xzf "${gitleaks_tmp}/${gitleaks_archive}" -C "${gitleaks_tmp}" gitleaks
sudo install -m 0755 "${gitleaks_tmp}/gitleaks" /usr/local/bin/gitleaks
```

Open a refreshed terminal after pnpm finishes installing.

### Verify the toolchain

On every operating system, these commands must succeed before cloning or installing the project:

```bash
git --version
node --version
pnpm --version
gitleaks version
```

`node --version` must report `v24.18.0`, `pnpm --version` must report `11.17.0`, and Gitleaks must report `8.30.1` or newer.

## 2. Clone the organization repository

Choose a workspace directory and clone the canonical repository:

```bash
git clone https://github.com/michi-guns/greek-essence.git
cd greek-essence
```

The repository is public, but pushing requires access to the `michi-guns` organization and GitHub authentication through your preferred credential manager.

## 3. Install project dependencies

Install exactly what is recorded in the lockfile:

```bash
pnpm install --frozen-lockfile
```

The install runs the Husky `prepare` script and configures the repository's Git hooks. pnpm's approved and denied dependency build scripts are declared in [`pnpm-workspace.yaml`](../pnpm-workspace.yaml) under `allowBuilds`. Review any proposed change to that list; do not approve an unfamiliar install script globally or interactively just to make installation pass.

## 4. Install the Playwright browser

The end-to-end and accessibility suites use Chromium at three responsive viewport sizes. Install only that required browser:

```bash
pnpm exec playwright install chromium
```

On Linux, install the required operating-system libraries as well when needed:

```bash
pnpm exec playwright install --with-deps chromium
```

Re-run the browser installation after a Playwright upgrade if the test runner requests a newer browser binary.

## 5. Configure the local environment

No secrets are required for local prototype development. The application has safe development defaults, so creating an environment file is optional. To make the configuration explicit, copy the example:

Windows PowerShell:

```powershell
Copy-Item .env.example .env.local
```

macOS or Linux:

```bash
cp .env.example .env.local
```

Available variables:

| Variable | Local value | Purpose |
|---|---|---|
| `NEXT_PUBLIC_SITE_URL` | `http://localhost:3000` | Base URL used for canonical metadata. Set the deployed HTTPS origin in production. |
| `NEXT_PUBLIC_DEFAULT_LOCALE` | `en` | Documents the default locale; explicit English and Greek routes remain authoritative. |

All `.env*` files except `.env.example` are ignored by Git. Never commit credentials, client information, or production secrets.

## 6. Diagnose the setup

Run the repository doctor after installation or whenever the toolchain behaves unexpectedly:

```bash
pnpm run doctor
```

The doctor checks the Git checkout, Git, the exact Node.js and pnpm versions, Gitleaks, dependencies, Husky hooks, optional local environment configuration, and the Playwright Chromium executable. `[FAIL]` entries must be corrected. `[WARN]` entries explain optional configuration and do not make the command fail.

## 7. Start the application

```bash
pnpm dev
```

Open [http://localhost:3000/en](http://localhost:3000/en) for English or [http://localhost:3000/el](http://localhost:3000/el) for Greek. Stop the server with `Ctrl+C`.

## 8. Understand the development checks

| Command | Purpose |
|---|---|
| `pnpm run doctor` | Diagnose workstation and repository setup. (`pnpm doctor` without `run` invokes pnpm's own diagnostic instead.) |
| `pnpm check` | Run formatting, linting, unused-code analysis, type checking, content validation, and unit tests. This is the lightweight GitHub Actions gate. |
| `pnpm check:push` | Run secret scanning, dependency auditing, static checks, coverage, the production build, and Playwright tests. Husky runs this before every push. |
| `pnpm check:all` | Run the push gate plus the built-site Unlighthouse quality check. |
| `pnpm test:unit:watch` | Run Vitest interactively while developing. |
| `pnpm test:a11y` | Run the focused automated accessibility suite. |
| `pnpm format` | Apply Prettier formatting. |
| `pnpm lint:fix` | Apply safe ESLint fixes. |

The local Git hooks provide three layers of feedback:

- `pre-commit` runs lint-staged against staged files.
- `commit-msg` enforces Conventional Commit messages through commitlint.
- `pre-push` runs `pnpm check:push`, including the heavier local quality gates.

Hooks can technically be bypassed, but a bypass should be exceptional and agreed by the team. Never bypass a secret-scanning or security failure.

## 9. First-day verification checklist

Before beginning feature work, confirm all of the following:

1. `pnpm run doctor` exits successfully.
2. `pnpm check` passes.
3. `pnpm dev` serves both `/en` and `/el` without console errors.
4. Your GitHub credentials can fetch the repository and, if authorized, push a branch.
5. You have read the [documentation entry point](README.md), the repository [`AGENTS.md`](../AGENTS.md), and the product or technical documents relevant to your task.

For the complete architecture and quality requirements, continue from the [Greek Essence documentation map](README.md).
