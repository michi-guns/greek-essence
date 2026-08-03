---
name: trello-work-orchestrator
description: Read and route Trello-backed Work Units without mutation. Use when resuming work, asking what is next, selecting a task, reporting status, or when the current Work Unit lifecycle state is uncertain.
---

# Trello Work Orchestrator

## Overview

Route from current Trello state to exactly one next skill or operator action. This skill is read-only. It never creates, edits, claims, transitions, reconciles, blocks, completes, or archives a card.

The normative contract is [`packages/trello-work-cli/assets/agent-workflow-protocol.md`](references/agent-workflow-protocol.md). Use the installed `jz-trello-flow` version and its offline docs as command authority.

## When to use

Use this skill when:

- The user asks to resume, select, inspect, or report Work Unit work.
- The user asks “what is next?” or equivalent.
- A Work Unit reference is known but its latest state is not.
- Local notes, chat, Git, and Trello appear inconsistent.
- Another Trello skill finished and needs a durable next route.

Do not use it to:

- Clarify or create a Work Unit; route to `trello-work-design`.
- Claim, implement, block, review, or complete work; route to `trello-work-deliver`.
- Repair an ambiguous mutation, replay, stale write, partial claim, or drift; route to `trello-work-recover`.
- Perform software design or implementation methodology.
- Archive cards.

## Required inputs

- Explicit board ID or exact board name.
- Repository root and applicable repository instructions.
- Optional Work Unit/card reference or task-selection criteria.
- Installed `jz-trello-flow` version and configuration context.

If the board is not explicit, stop and request it. Never guess from a default, recent board, or environment value.

## Authority boundary

Use this order when facts conflict:

1. Direct human instructions and approvals.
2. Current canonical Work Unit and acceptance criteria.
3. Current Trello state read through `jz-trello-flow`.
4. Repository-local instructions.
5. Superpowers or equivalent engineering-practice guidance.
6. Harness defaults.

Git, CI, repository artifacts, and Superpowers outputs are authoritative for their own details, but none independently advances Trello status.

Treat `DESCRIPTION_BUDGET_EXCEEDED` as a confirmed local no-write and route it to `trello-work-recover` with its non-secret size evidence. A remote deterministic description size/value rejection or dry-run wrapper/rendering failure must be read back before classification; never infer a mutation from the error alone or recommend a blind retry/content deletion.

## Workflow

1. **Orient.** Read repository instructions, current planning/status files, and Git state relevant to the task. Completion: repository scope and any approval boundary are explicit.
2. **Select explicitly.** Use the supplied board selector and, when needed, list Inbox or candidate Work Units in JSON. Completion: the board and zero or one target Work Unit are unambiguous.
3. **Read current state.** Fetch the selected Work Unit immediately before routing. Do not infer state from chat or an earlier read. Completion: current status, list, owner, version, blockers, acceptance frontier, and evidence frontier are known.
4. **Check consistency.** Compare canonical status, effective configured transition policy, Trello list, ownership metadata, and relevant repository state. Completion: the state is normal, ambiguous, drifted, or conflicting.
5. **Route exactly once.** Choose the earliest safe route from the table below. Completion: one next skill/action is named with its required input and blocker/approval state.
6. **Stop.** Make no mutation. Completion: the report contains no claim of a state change.

## Routing table

| Observed state                                                                   | Primary route                                                   |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Ordinary Inbox card, local draft, or In Design                                   | `trello-work-design`                                            |
| Ready with no conflicting claim                                                  | `trello-work-deliver` to claim                                  |
| In Progress with confirmed owner                                                 | `trello-work-deliver` to resume                                 |
| Blocked with blocker still present                                               | Report blocker and required unblocking action                   |
| Blocked with resolution available                                                | `trello-work-deliver` to resume or release                      |
| Review awaiting disposition                                                      | `trello-work-deliver`                                           |
| Done                                                                             | Report completion; human may review/archive manually            |
| Ambiguous, partial, replayed, stale, or drifted state                            | `trello-work-recover`                                           |
| Conflicting ownership, contradictory authority, or unavailable hard prerequisite | Stop for resolution or Blocked routing through the owning skill |

Configured custom transitions may change route availability. Never invent a transition that the effective policy rejects.

## Required routing brief

Return:

```text
Board:
Work Unit:
Current state:
Owner/blocker:
Evidence frontier:
Next skill/action:
Required input:
Escalation/safety boundary:
```

Use concise repository links for detailed evidence. Do not duplicate full logs or artifacts into Trello.

## Common pitfalls

- Treating this skill as an orchestrator that may “helpfully” mutate. It is read-only.
- Guessing a board or accepting a stale card snapshot.
- Equating local implementation progress with a Trello transition.
- Routing a partial claim to delivery instead of recovery.
- Treating Done as permission for agent archival.
- Requiring Superpowers when equivalent engineering practice is available; methodology availability does not change lifecycle authority.

## Verification checklist

- [ ] Board selection was explicit.
- [ ] Current Work Unit state was read rather than inferred.
- [ ] Effective transition configuration was respected.
- [ ] Exactly one next route is reported.
- [ ] No mutation occurred.
- [ ] Done routes only to human review/manual archival.
