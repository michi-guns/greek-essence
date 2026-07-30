# Manual Vercel Re-deploy

## Status

In Progress

## Ownership and Scope

Owner: Codex (`jimzord Stam`)

Trello Work Unit: [WU-27 — Configure Vercel - manual Re-deploy](https://trello.com/c/16L5cZe0)

Scope: disable every Git-triggered Vercel deployment and provide
`pnpm deploy:vercel` as the only supported Greek Essence production
re-deployment workflow. Keep the Deploy Hook secret local, expose no secret in
output, add focused tests, and verify the real post-merge workflow once with
explicit operator authorization.

This work item owns `vercel.json`, the bounded deployment script and tests,
the `deploy:vercel` package command, the credential-free `.env.example`
placeholder, focused usage guidance, and its own routing document. Vercel
account administration remains operator-owned.

## Current State

- WU-27 completed same-card design, is read-back-confirmed In Progress, and is
  owned by `jimzord Stam`.
- GitHub `main` protection is strict and requires only
  `Lightweight quality gates`; Vercel statuses are not required and no
  repository ruleset adds another check.
- Branch `task/wu-27-vercel-manual-redeploy` was created in a separate worktree
  from current `origin/main` at
  `9d5ebf7427d2c874edb0188af37afefd26d5eeb3`.
- Recovery preflight found no matching local branch, remote branch, worktree,
  or head/base pull request before bootstrap.
- Draft pull request
  [#46](https://github.com/michi-guns/greek-essence/pull/46) is linked from
  Trello and targets `main` from the verified branch.
- Implementation commit `90f72cc` adds `git.deploymentEnabled: false`, the
  dependency-free `pnpm deploy:vercel` command, strict Vercel-hook validation,
  one bounded POST with timeout, non-secret output, focused tests, environment
  guidance, and the empty `.env.example` placeholder.
- The attached reference script was inspected and executed once with explicit
  authorization. Vercel accepted job `DFkugYrVSy5tJne42VF0` for the hook's
  configured `main` branch; the hook URL was never printed. This proves the
  existing hook, not the still-unmerged repository command.
- Focused verification passes 15 deployment tests. The full `pnpm check:push`
  gate passes secret scanning, audit policy, formatting, linting, Knip, strict
  type checking, content validation, 73 unit tests with coverage, production
  build, and 53 Playwright tests with 4 intentional skips.
- The active Prototype rebaseline and WU-20 integration work remain separate;
  their files and primary checkout changes are untouched.

## Next Recommended Action

Push the verified implementation and handoff commits, update draft PR #46 with
the final scope and evidence, then wait for the required
`Lightweight quality gates` result. Review the complete diff before marking the
PR ready and moving WU-27 to Review.

Completion condition: local and remote heads match, PR #46 represents the
complete implementation, required CI passes, and no material review finding
remains.

## Done When

- `vercel.json` disables Git-triggered deployments for every branch.
- `pnpm deploy:vercel` loads the ignored hook URL and triggers exactly one
  deployment request without adding a runtime dependency or exposing secrets.
- Focused success and realistic failure tests pass.
- Required repository and GitHub checks pass without requiring Vercel status.
- After merge, no Git-triggered deployment occurs and one explicitly authorized
  command deploys latest `main`.
- Squash merge, branch cleanup, and clean synchronized local `main` are verified
  before WU-27 moves to Done; Trello archival remains human-only.

## Constraints

- Never commit or print `VERCEL_DEPLOY_HOOK_URL`.
- Vercel account, hook creation/rotation, and dashboard actions remain the
  operator's responsibility.
- Automatic PR previews are intentionally disabled with all other Git-triggered
  deployments.
- Preserve unrelated files and concurrent work items.
- Obtain fresh explicit operator confirmation immediately before an agent
  merge. The operator may merge personally.
