# Agent Guidance Decomposition

## Status

Complete

## Ownership and Scope

Owner: Codex

Scope: reduce root `AGENTS.md` to stable safety, authority, and task-routing
instructions; move detailed product-collaboration, development, quality, and
agent-tooling policy into documents with one clear owner; and update the
documentation entry point and existing workflow protocols to preserve complete
navigation without duplicating policy.

The operator explicitly coordinated this bounded overlap with the active
Trello and GitHub Flow work item on 2026-08-02. That work item continues to own
the meaning of the Git, GitHub, and Trello lifecycle. This item may route to and
clarify the location of those rules but must not change their meaning.

## Current State

- Branch `docs/agent-guidance-decomposition` starts at current `origin/main`
  commit `978136091639aa473b8b384b6b9ee8382da040c3`.
- Root `AGENTS.md` contains the operator-approved structural rewrite.
- The clean `docs/wu-20-trello-github-flow` worktree has no concurrent edits to
  the files in this change.
- The proposal branch and discarded Superpowers installation remain outside
  this item's ownership.
- `AGENTS.md` is reduced to startup, authority, ownership, hard delivery,
  routing, stable defaults, and Superpowers activation rules.
- `docs/PRODUCT_COLLABORATION.md`, `docs/DEVELOPMENT_STANDARDS.md`,
  `docs/QUALITY_GATES.md`, and `docs/AGENT_TOOLING.md` now own the detailed
  policies extracted from `AGENTS.md`.
- `docs/README.md` exposes the new owners, `docs/GIT_WORKFLOW.md` delegates
  verification policy to `docs/QUALITY_GATES.md`, and
  `docs/grilling/protocol.md` delegates general product coaching to
  `docs/PRODUCT_COLLABORATION.md`.
- Accepted stack and Foundation Design choices remain in `docs/grilling/`; no
  product or architecture authority was moved or rewritten.
- Superpowers activation and skill policy are excluded because the
  repository-local skills are not installed on `main`; their later installation
  must add its matching activation policy in the same coherent unit.
- A local Markdown-link audit found that every local target in the changed
  files exists.
- Preliminary Markdown-only verification passed: Prettier reported all ten
  owned Markdown files formatted, and redacted Gitleaks scans reported no leaks
  in each file.
- Commit `95e75ae` is pushed to
  `origin/docs/agent-guidance-decomposition`.
- Pull request [#51](https://github.com/michi-guns/greek-essence/pull/51) is
  non-draft and targets `main` from the verified branch.
- Commit and pre-push hooks classified the change as Markdown-only; Prettier and
  the repository Gitleaks history scan passed.
- GitHub `Lightweight quality gates` run
  [30750511156](https://github.com/michi-guns/greek-essence/actions/runs/30750511156)
  passed on the non-draft pull request.

## Next Recommended Action

Re-read pull request #51 and obtain fresh operator confirmation immediately
before squash merge. After merge, verify remote branch deletion and a clean
local `main` synchronized with `origin/main`.

Completion condition: delivery cleanup is verified without including proposal
or Superpowers installation changes.

## Done When

- `AGENTS.md` contains stable startup, authority, ownership, safety, routing,
  default-behavior, and Superpowers activation instructions only.
- Product collaboration, development standards, quality gates, and agent
  tooling each have one explicit documentation owner.
- `docs/README.md`, `docs/GIT_WORKFLOW.md`, and `docs/grilling/protocol.md`
  route to those owners without duplicating their detailed policy.
- A semantic comparison finds no omitted guardrail or changed product,
  architecture, workflow, or quality decision.
- Gitleaks and Prettier pass for the changed Markdown range.

## Constraints

- Preserve the Trello and GitHub lifecycle established by WU-20.
- Do not include the documentation-architecture proposal or Superpowers
  installation in this work.
- Do not modify accepted product or Foundation Design decisions.
- Obtain fresh explicit operator confirmation immediately before merge.
