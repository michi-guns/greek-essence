# Greek Essence Agent Operating Guide

> [!IMPORTANT]
> This file contains stable repository guardrails and routing instructions. The
> linked documents own detailed product, workflow, development, quality, and
> tooling policy.

## Start Here

Before beginning project work:

1. Read [`docs/README.md`](docs/README.md), the documentation entry point.
2. Read [`NEXT.md`](NEXT.md), the router for active multi-session work.
3. If a work item is assigned, read its linked `NEXT.md` completely before
   acting.
4. For program-level “what next?”, frontier tasks, or cold-start prioritization
   across many Trello Work Units, read
   [`docs/working/work-program/SEQUENCE.md`](docs/working/work-program/SEQUENCE.md)
   and follow the `greek-essence-work-program` skill. Trello remains Work Unit
   authority; the sequence is navigation and selection only.

If no work item is assigned, present the available work items and the work
program frontier, then ask the operator which one to continue. Do not select or
begin one autonomously. Current operator instructions always take precedence
over handoff content.

## Authority

Resolve instructions and requirements in this order:

1. Current operator instructions.
2. This `AGENTS.md` and the selected active work item's `NEXT.md` for repository
   workflow and immediate continuation.
3. Accepted `DECISIONS.md` files under `docs/grilling/`.
4. Accepted [`docs/grilling/CLASSIFICATION.md`](docs/grilling/CLASSIFICATION.md)
   for routing locked inputs and existing outcomes without changing an accepted
   decision's meaning.
5. New canonical product, domain, UX, technical, and design documents after
   accepted decisions are promoted into them.
6. Explicit task contracts for bounded implementation work.

An active `GRILLING.md` is an in-progress decision ledger, not permission to
implement. `docs/working/` contains temporary operational state and evidence,
not durable product authority. Everything under
`docs/archive/showcase-prototype-v0/` is historical reference only. Existing
application behavior does not define the replacement product. Record and
escalate conflicts instead of silently choosing an old or convenient
interpretation.

## Work-Item Guardrails

- Each work item has one primary owner. Claim it in its `NEXT.md` before
  changing its scope.
- Do not act on an item claimed by another owner without explicit coordination.
- Only the primary owner updates that work item's `NEXT.md`; subagents report
  results unless explicitly given ownership.
- Inspect other active work items and coordinate overlapping paths or
  responsibilities before creating or claiming work.
- Verify handoff claims against the live repository. Reconcile or escalate stale
  state before continuing.
- Create a work-item directory and its root-router link in the same change. At
  completion, mark the work item complete and remove its root-router link in the
  same change.
- Before handing off materially advanced work, update the work item's `NEXT.md`
  as the final documentation action with one next action, its completion
  condition, and immediate constraints.

Root `NEXT.md` contains links only; it never owns task details or a global next
action.

[`TODO.md`](TODO.md) is an operator-managed backlog, not an execution queue,
task contract, status ledger, or handoff. Agents may add clearly attributable
pending work or clarify an entry without changing its intent. Do not implement,
delegate, schedule, or promote an entry unless the operator or an authorized
planning task selects it. Before execution, move selected work into its
authorized plan, issue, task contract, or active work item. Remove completed
entries after reconciling their outcomes into durable project history. Never
store secrets, credentials, runtime state, process identifiers, raw logs, or
detailed execution evidence there.

## Hard Delivery Boundaries

- Follow [`docs/GIT_WORKFLOW.md`](docs/GIT_WORKFLOW.md) for every coherent,
  independently reviewable unit of work.
- Keep `main` deployable; never commit or push directly to `main`.
- Use one short-lived branch and one pull request for each coherent unit; do not
  split incremental edits or combine unrelated outcomes.
- Preserve unrelated and concurrent work. Never discard or overwrite it without
  explicit authorization.
- Do not create an implementation branch or pull request for a Trello Work Unit
  in Inbox or In Design.
- Before creating durable Trello, Git, or GitHub state, search for matching
  existing state and reuse it after verified recovery.
- Re-read Trello and GitHub and obtain fresh, explicit operator confirmation
  immediately before an agent merge. Detect an operator-performed merge and
  never attempt a second merge.
- Trello card archival remains human-only.

## Task Routing

Read the applicable owner completely before acting:

| When work involves                                                                                                       | Authoritative route                                                                        |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Project roles or responsibility                                                                                          | [`docs/PROJECT_ACTORS.md`](docs/PROJECT_ACTORS.md)                                         |
| Product discovery, requirements, traveler experience, agency workflow, public claims, personal data, money, or suppliers | [`docs/PRODUCT_COLLABORATION.md`](docs/PRODUCT_COLLABORATION.md)                           |
| Grilling or decision persistence                                                                                         | [`docs/grilling/protocol.md`](docs/grilling/protocol.md) and the selected layer and ledger |
| Git, GitHub, Trello, branches, pull requests, merge, or cleanup                                                          | [`docs/GIT_WORKFLOW.md`](docs/GIT_WORKFLOW.md)                                             |
| Implementation, coding defaults, testing scope, or proportionality                                                       | [`docs/DEVELOPMENT_STANDARDS.md`](docs/DEVELOPMENT_STANDARDS.md)                           |
| Checks, verification evidence, or completion claims                                                                      | [`docs/QUALITY_GATES.md`](docs/QUALITY_GATES.md)                                           |
| Skills, browser automation, or agent tooling                                                                             | [`docs/AGENT_TOOLING.md`](docs/AGENT_TOOLING.md)                                           |

When a product or workflow proposal appears incomplete, inconsistent,
misleading, operationally risky, or likely to affect trust, workload, data,
privacy, money, suppliers, or customer communication, stop before encoding the
assumption and follow `docs/PRODUCT_COLLABORATION.md`.

## Stable Development Defaults

- Use the package manager and version declared by the repository's
  `packageManager` field. Do not substitute another package manager.
- Keep TypeScript strict.
- Use only skills and browser tooling authorized by `docs/AGENT_TOOLING.md`.
- Run the task-required and range-applicable checks in
  `docs/QUALITY_GATES.md`. Record exact commands, exit codes, and results; never
  claim a check that did not run.
