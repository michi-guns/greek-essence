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
- The original Trello attachment `vercel-deploy-hook-script.js.txt` is retained
  as implementation input, not authority.
- The active Prototype rebaseline and WU-20 integration work remain separate;
  their files and primary checkout changes are untouched.

## Next Recommended Action

Commit this registration, push the branch, open one draft pull request against
`main`, and record its verified URL on WU-27. Then inspect the attached script
and implement the smallest tested solution matching the approved Work Unit.

Completion condition: the remote branch, draft pull request, and Trello link
are verified as one matching durable chain with no duplicate state.

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
