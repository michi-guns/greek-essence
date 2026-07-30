# Markdown-Only Quality Gates

## Status

Active

## Ownership and Scope

Owner: Hermes Agent (`greek-essence`)

Scope: classify pushed and pull-request changes, retain secret scanning and
actual Markdown formatting for Markdown-only changes, skip application checks
that those changes cannot affect, and preserve the existing full-check path for
mixed or uncertain changes.

This work item may change Git hooks, CI configuration, check scripts and focused
tests, package scripts, and contributor or agent workflow documentation. It
does not change product decisions, prototype behavior, or the active
prototype-rebaseline work item's grilling documents.

## Current State

- Local `pre-commit` runs `lint-staged`, but `.prettierignore` excludes `docs/`,
  so explicitly staged project documentation can be reported as formatted
  without actually being parsed.
- Local `pre-push` always runs `pnpm check:push`.
- GitHub's required `Lightweight quality gates` job always runs `pnpm check`.
- Branch protection strictly requires the exact `Lightweight quality gates`
  context.

## Next Recommended Action

Implement a fail-closed, tested Markdown-only classifier and wire it into local
pre-push and the existing required CI job.

Completion condition: Markdown-only ranges run Gitleaks and scoped Prettier;
mixed, empty, or unresolved ranges retain the full existing checks; the full
local gates and both route tests pass; and the real required GitHub check is
verified.

## Constraints

- Preserve the exact required GitHub check name.
- Do not use workflow-level path exclusions that can leave branch protection
  waiting for a skipped status.
- Do not weaken or bypass Gitleaks.
- Do not globally expose the historical documentation archive to formatting
  churn.
- Preserve unrelated changes in the original worktree.
