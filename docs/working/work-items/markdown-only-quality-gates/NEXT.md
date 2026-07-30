# Markdown-Only Quality Gates

## Status

Complete

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

## Outcome

- A tested classifier now selects Gitleaks and scoped Prettier for non-empty
  `.md`/`.mdx`-only ranges and fails closed to the existing full checks.
- Pre-commit now formats staged Markdown under `docs/` instead of silently
  honoring the repository-wide documentation exclusion.
- Local pre-push classifies all pushed refs. A synthetic Markdown-only push
  range ran Gitleaks and scoped Prettier; a mixed historical range ran
  `pnpm check`.
- GitHub preserves the required `Lightweight quality gates` context, uses the
  licensed official Gitleaks Action, and runs change-appropriate checks.
- `pnpm check:push` exited `0`: Gitleaks found no leaks; the configured audit
  gate passed while reporting three known findings; 54 unit tests passed with
  coverage; build passed; and Playwright completed with 53 passing and 4
  intentionally skipped tests.
- GitHub Actions run `30561310912` exited successfully after the licensed
  Gitleaks Action and full mixed-change path both passed.

No further action is required for this work item.

## Constraints

- Preserve the exact required GitHub check name.
- Do not use workflow-level path exclusions that can leave branch protection
  waiting for a skipped status.
- Do not weaken or bypass Gitleaks.
- Do not globally expose the historical documentation archive to formatting
  churn.
- Preserve unrelated changes in the original worktree.
