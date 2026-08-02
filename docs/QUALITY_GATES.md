# Quality Gates

## Purpose and Authority

This guide owns change classification, required verification, evidence
reporting, and the repository-wide definition of done. A task contract may add
focused checks but may not silently weaken applicable repository gates.

Run the required checks against the complete intended change range. Record the
exact commands, exit codes, and results. Never claim a check that did not run.

## Change Classification

| Change range                                          | Applicable automated gates                                       |
| ----------------------------------------------------- | ---------------------------------------------------------------- |
| Non-empty range containing only `.md` or `.mdx` files | Gitleaks and Prettier against the changed Markdown files         |
| Mixed, empty, malformed, or unresolved range          | Full applicable gates                                            |
| Task contract with additional verification            | Contract checks plus the applicable range-based repository gates |

For Markdown-only changes, do not run application lint, unused-code analysis,
type checking, content-data validation, unit tests, coverage, build, browser,
accessibility, metadata, or visual quality gates unless the task contract
separately requires them.

## Full Repository Gates

While the current runtime remains, full applicable verification includes:

- redacted Gitleaks scanning;
- dependency security audit;
- Prettier formatting verification;
- ESLint;
- unused-code analysis;
- strict TypeScript checking;
- content-data validation;
- unit tests and required coverage;
- a production build;
- required Playwright end-to-end, accessibility, and metadata checks; and
- required project visual quality checks.

Use the repository's current `package.json` scripts as the executable source of
truth. Current aggregate commands include `pnpm check:push` and, when the task
requires the extended quality suite, `pnpm check:all`. Future accepted
architecture work must explicitly replace obsolete gates rather than silently
dropping them.

## Evidence Rules

- Report the exact command and exit code for every executed check.
- Distinguish passing, failing, skipped, and not-applicable checks.
- Do not infer a pass from a partial command or an earlier change range.
- Resolve unexpected console errors and failed critical network requests when
  browser verification applies.
- Protect personal and client data from Git, logs, screenshots, previews, and
  analytics throughout verification.

## Definition of Done

A change is done only when all applicable conditions are satisfied:

- It meets current accepted decisions and its explicit task contract.
- It preserves applicable product, data, locale, security, and privacy
  boundaries.
- Focused required checks pass and their exact results are recorded.
- No console errors or failed critical network requests remain when browser
  verification applies.
- Personal and client data are protected from Git, logs, screenshots,
  previews, and analytics.
- Only approved visible claims and assets are used.
- Known production gaps are recorded.
- Required review approval is received.
