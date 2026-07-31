# Trello and GitHub Flow Integration

## Status

In Progress

## Ownership and Scope

Owner: Codex (`jimzord Stam`)

Trello Work Unit: [WU-20 — Trello Workflow & CLI](https://trello.com/c/IC2bdbjQ)

Scope: define and prove the repository contract joining Trello Work Unit states
to Greek Essence GitHub Flow. Add one default pull-request template, preserve a
deployable protected `main`, create one short-lived branch and early draft pull
request for each claimed implementation unit, recover existing durable state
instead of duplicating it, and require fresh operator confirmation before an
agent merges.

This work item owns `AGENTS.md`, `docs/GIT_WORKFLOW.md`, the default pull-request
template, and its own routing documents only. It preserves the active Prototype
rebaseline route and does not modify that work item's directory or product
decisions.

## Current State

- WU-20 is read-back-confirmed In Progress and owned by `jimzord Stam`.
- Branch `docs/wu-20-trello-github-flow` was created from current
  `origin/main` at `ec9fa47980b32ceee038c2ca6f895bf685970ac0` in a separate
  worktree.
- No matching remote branch or pull request existed before bootstrap.
- Pull request [#44](https://github.com/michi-guns/greek-essence/pull/44) is
  non-draft for the verified head/base pair and its URL is recorded on WU-20.
- `AGENTS.md` and `docs/GIT_WORKFLOW.md` now define the seven-state lifecycle,
  guarded claim, durable creation order, cross-system recovery, Review gate,
  fresh merge confirmation, operator-performed merge handling, cleanup, Done,
  and human-only archival boundaries.
- `.github/pull_request_template.md` captures Work Unit identity, outcome,
  boundaries, acceptance, verification, risks, recovery, and completion state.
- Final head `1810f007879015103f5c004e95689afb7341484c` is pushed. GitHub
  `Lightweight quality gates` run `30572523370`, the Vercel deployment status,
  and Vercel Preview Comments pass.
- Focused semantic review found no unresolved contract inconsistency. The
  repository's visual quality-review skill is not applicable to this
  workflow-only Markdown change.
- Inbox card
  [#27 — Configure Vercel - manual Re-deploy](https://trello.com/c/16L5cZe0)
  is the selected tracer after this integration contract is established.
- `FLOW-001` records that WU-20 cannot remain in Review before card #27 proves
  its final acceptance criterion. PR #44 is a complete foundational
  sub-delivery whose merge enables that tracer; WU-20 is therefore
  read-back-confirmed In Progress until the independent tracer completes.
- The unrelated Prototype rebaseline remains owned by Hermes Agent in its own
  work item. The primary checkout's untracked Hermes files remain untouched.

## Next Recommended Action

Re-read PR #44 and WU-20, then obtain fresh explicit operator confirmation
before an agent squash-merges this foundational PR, or detect and accept an
operator-performed merge. After verified merge and branch cleanup, synchronize
local `main` and begin same-card design of tracer card #27 through the newly
merged workflow.

Completion condition: PR #44's merge and cleanup are verified without a second
merge attempt, and card #27 begins the independent tracer lifecycle while
WU-20 remains In Progress.

## Done When

- All seven Trello states have explicit Git and pull-request meanings and
  transition evidence.
- Claim and cross-system recovery ordering are documented without representing
  Trello ownership as atomic.
- The default pull-request template captures Work Unit identity, intended
  outcome, boundaries, acceptance, verification, risks, and completion state.
- Review, merge authorization, operator-performed merge detection, cleanup, and
  Done gates are explicit.
- WU-20's branch, draft pull request, Trello link, checks, review evidence, and
  final lifecycle state are verified.
- Card #27 completes the resulting workflow as the independent tracer unit
  before this integration is treated as proven.

## Constraints

- Never push directly to `main`, bypass protection or checks, force-push, or
  rewrite history.
- An agent must obtain fresh explicit operator confirmation immediately before
  merging. The operator may merge personally; detect that state and do not
  attempt a second merge.
- Reuse a verified matching branch, work item, or pull request after partial
  failure. A failed Trello link-back never authorizes duplicate GitHub state.
- Keep Trello evidence concise; repository, Git, GitHub, and CI remain
  authoritative for their detailed state.
- Trello card archival remains human-only.
- Preserve unrelated files and the active Prototype rebaseline work item.
