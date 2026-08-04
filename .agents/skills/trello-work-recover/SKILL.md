---
name: trello-work-recover
description: Recover exceptional Trello Work Unit mutations safely. Use after an ambiguous, partial, timed-out, stale-version, replayed, colliding, conflicting, or drifted operation—not for routine lifecycle work.
---

# Trello Work Recover

## Overview

Restore a known intended postcondition or stop safely after an exceptional Trello outcome. Recovery is minimal and evidence-driven: read first, recognize success, retry unchanged state once with the same operation identity, and never overwrite conflict blindly.

The normative contract is [`packages/trello-work-cli/assets/agent-workflow-protocol.md`](references/agent-workflow-protocol.md). Use installed `jz-trello-flow` safety/workflow docs for exact recovery data and reconciliation syntax.

## When to use

Use this skill after:

- Timeout, interruption, or lost response.
- Partial multi-step claim or other partial mutation.
- Stale-version rejection.
- Idempotency replay or operation-ID collision signal.
- Current state that conflicts with the intended postcondition.
- Suspected canonical status/list drift.
- A retry whose result is still ambiguous.

Do not use it for:

- Routine reads/status; use `trello-work-orchestrator`.
- Normal Inbox/In Design work; use `trello-work-design`.
- Normal claim, implementation, blocking, review, or completion; use `trello-work-deliver`.
- New scope, changed intent, destructive cleanup, production migration, or archival.

## Required recovery context

Preserve before acting:

- Explicit board ID or exact board name.
- Work Unit/card and affected resource IDs.
- Original intended postcondition.
- Original durable operation ID and operation type.
- Latest known version and timestamp, if available.
- Stable expected owner for claim recovery.
- CLI non-secret recovery data and observed error/result.
- Repository/human authority for any proposed repair.

If intended postcondition or operation identity is unknown, do not invent it. Read and report uncertainty; request human input or route to Blocked through an authorized lifecycle operation.

## Minimal recovery algorithm

1. **Read current state.** Use explicit board and fetch the affected Work Unit/resources before any retry. Completion: current status, list, owner, version, and relevant idempotency/drift evidence are known.
2. **Classify.** Choose exactly one branch: already satisfied, unchanged, conflicting, drifted, or still ambiguous. Completion: evidence supports the branch.
3. **Already satisfied.** If the intended postcondition exists and belongs to the same intent, treat the operation as recovered. Do not replay. Completion: read-back proves the postcondition and normal owning skill is identified.
4. **Unchanged.** If state is unchanged, retry once using the same operation ID and newly read latest version. Completion: read-back proves success or the outcome is reclassified; no second blind retry occurs.
5. **Conflicting.** Do not overwrite. Preserve both intended and observed states. Use reconciliation dry-run where applicable, then perform only a repair authorized by the current Work Unit/repository plan or route to Blocked with concise explanation. Do not add a redundant permission prompt when scoped authority already exists. Completion: conflict is safely resolved or durably exposed.
6. **Drifted.** Run reconciliation dry-run, inspect configured source-of-truth policy and proposed direction, and execute only when understood and authorized. Use current version and durable operation ID, then read back. Completion: canonical description/status and list agree under configured policy.
7. **Still ambiguous.** Stop mutation. Preserve non-secret recovery data and the safest next action for another actor. Completion: no speculative write follows uncertainty.
8. **Route back.** Return to `trello-work-design` or `trello-work-deliver` only after current state is read-back-confirmed. Done routes to human review/manual archival only.

## Partial claim recovery

A claim requires both expected owner and `in_progress` status.

| Observed state                             | Safe response                                                                                              |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Expected owner and In Progress             | Claim recovered; route to delivery                                                                         |
| Neither owner nor status changed           | Retry the failed original step once with same operation ID/latest version                                  |
| Expected owner but still Ready             | Re-read for conflict; recover the transition with its original operation ID only when unchanged/authorized |
| In Progress but owner missing or different | Do not begin work; preserve conflict and reconcile or Block                                                |
| Different owner or incompatible status     | Do not overwrite; stop for conflict resolution                                                             |

Never generate a new claim operation identity merely to bypass replay/collision detection. Never begin engineering work on a partial claim.

## Replay and collision

- Same operation ID plus same intent: read current state and recognize already-applied success or retry unchanged state once.
- Same operation ID plus different intent: stop. Generate no mutation under that ID.
- Lost creation response: read/list using available recovery identity; never create a replacement card merely because the response was lost.
- Version stale: re-read. A newer version authorizes no overwrite by itself; re-evaluate intent against current state.

## Reconciliation boundary

Reconciliation repairs authorized status/list drift under configured source-of-truth policy. It does not:

- Invent which side is authoritative.
- Approve scope or acceptance changes.
- Resolve ownership conflict by force.
- Delete or recreate cards.
- Migrate a production board.
- Archive Done cards.

Always inspect `reconcile --dry-run` before a write when reconciliation is applicable.

For `DESCRIPTION_BUDGET_EXCEEDED`, record the non-secret current/proposed character and byte counts, marker contribution, operation kind, and documented limit. It is a confirmed local no-write. For a remote deterministic description size/value rejection or a dry-run wrapper/rendering failure, read back first; never blind-retry, change the operation ID, discard card content, or remove legacy/compact recovery markers merely to fit. Retry unchanged state at most once only when the exact payload now preflights and the ordinary unchanged-state rule authorizes it.

## Evidence

Record recovery evidence only when state changed, uncertainty remains, or another actor needs it. Keep it concise:

- Intended versus observed postcondition.
- Original operation ID/type.
- Read-back outcome.
- Authorized repair or Blocked route.
- Repository link for detailed logs when useful.

A successfully recognized routine replay needs no extra recovery ceremony.

## Routes

- Recovered In Design/Ready → `trello-work-design` or `trello-work-deliver` according to status.
- Recovered In Progress/Blocked/Review → `trello-work-deliver`.
- Done → stop; human review/manual archival.
- Unresolved conflict/uncertainty → preserve evidence and request authority or route to Blocked through `trello-work-deliver` when safe.

## Common pitfalls

- Retrying before reading.
- Changing operation ID to force a second mutation.
- Retrying more than once after unchanged state.
- Treating latest version as permission to overwrite conflict.
- Starting work on a partial claim.
- Choosing reconciliation direction without inspecting policy.
- Turning routine success into a recovery journal.
- Archiving or destructive cleanup during recovery.

## Verification checklist

- [ ] Board, resource IDs, intent, and original operation identity are explicit.
- [ ] Current state was read before mutation.
- [ ] Exactly one recovery branch was selected from evidence.
- [ ] Unchanged state retried at most once with the same operation ID/latest version.
- [ ] Conflict was not overwritten blindly.
- [ ] Reconciliation direction was inspected and authorized.
- [ ] Final postcondition was read back or mutation stopped safely.
- [ ] No new scope, destructive cleanup, production migration, or archival occurred.
