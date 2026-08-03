---
name: trello-work-design
description: Create and clarify canonical Trello Work Units through Ready. Use for ordinary Inbox selection, local Draft Work Unit intake, same-card In Design work, unresolved questions, or readiness assessment before claiming.
---

# Trello Work Design

## Overview

Own durable Work Unit intake and clarification from an ordinary Inbox card or validated local draft through read-back-confirmed Ready. This skill coordinates Trello state; it does not replace software-design methodology.

The normative contract is [`packages/trello-work-cli/assets/agent-workflow-protocol.md`](references/agent-workflow-protocol.md). Use the installed `jz-trello-flow` offline guide for version-matched command syntax.

## When to use

Use this skill for:

- Selecting an ordinary Inbox card for design while preserving its identity.
- Validating and creating an agent-prepared Draft Work Unit.
- Resuming a Work Unit already in In Design.
- Clarifying scope, non-goals, acceptance criteria, dependencies, or verification.
- Deciding whether an In Design Work Unit is complete enough for Ready.

Do not use it to:

- Claim Ready work or perform implementation; use `trello-work-deliver`.
- Repair uncertain, stale, partial, replayed, or conflicting mutation outcomes; use `trello-work-recover`.
- Reimplement brainstorming, architecture design, planning, TDD, debugging, review, or verification methodology.
- Move work beyond Ready, migrate a board, or archive a card.

## Required inputs

- Explicit board ID or exact board name.
- Exactly one ordinary Inbox card, one validated local draft, or one In Design Work Unit.
- Human intent and applicable repository instructions.
- Current CLI version/configuration and the latest Work Unit read.

Stop when target identity or board selection is ambiguous. Never create a replacement card merely because an existing card is incomplete.

## Responsibility boundary

Trello and `jz-trello-flow` own durable identity, canonical Work Unit content, lifecycle status, version/operation identity, read-back, and recovery diagnostics.

When installed, Superpowers owns engineering design exploration and planning. Otherwise use equivalent repository-compatible practice. Summarize durable conclusions in the Work Unit and link repository artifacts; do not copy methodology internals or full documents into Trello.

## Universal mutation discipline

For every mutation:

1. Select the board explicitly.
2. Prefer JSON output for automation.
3. Read the target immediately before mutation.
4. Pass the latest observed version.
5. Use a durable operation ID unique to that intent.
6. Execute the minimum mutation.
7. Read back the card and verify identity, content, status, list, and version.
8. Route uncertainty to `trello-work-recover`; never retry blindly.

Use a dry run when target, policy, operation, or consequences are not already established. Do not add duplicate ceremony to understood routine changes.

Before writing a description, inspect the exact final-payload preflight. `DESCRIPTION_BUDGET_EXCEEDED` is a confirmed no-write result: preserve the operation ID and content, shorten deliberately, and never delete recovery markers or retry blindly. A dry-run wrapper/rendering error does not imply a mutation; read back before classifying any uncertain result.

## Workflow A — ordinary Inbox card

1. **Read the card.** Confirm explicit board, Inbox state, identity, attachments/comments, and latest version. Completion: the same-card target is unambiguous.
2. **Clarify materially.** Use human input, repository evidence, and Superpowers brainstorming/planning when applicable. Mark unresolved material content as `Pending:` or Open Questions. Completion: current known intent and uncertainty are explicit.
3. **Start design on the same card.** Use the CLI design-start operation with current version and durable operation ID. Completion: read-back confirms unchanged card identity, canonical Work Unit content, `in_design` status, and expected list.
4. **Continue clarification.** Update only canonical sections/metadata needed for resumability. Completion: another actor can distinguish resolved facts from pending decisions.

Never create a new Draft Work Unit to replace the selected Inbox card.

## Workflow B — agent-prepared draft

1. **Prepare locally.** Draft the canonical Work Unit without Trello mutation. Completion: the draft has required sections and no secret values.
2. **Validate offline.** Use version-matched CLI validation. Completion: validation succeeds or defects are corrected locally.
3. **Inspect creation.** Use dry run when board or creation intent is not already established. A dry run cannot allocate the final Work Unit ID. Completion: target board and planned creation are understood.
4. **Create once.** Use explicit board and durable operation ID. Completion: read-back accepts the server-assigned identity and confirms the new canonical Work Unit is in Inbox.
5. **Start design on the created card.** Read the new Inbox Work Unit, then use the same-card design-start operation with the latest version, a new operation ID for that intent, and the canonical In Design content. Completion: read-back confirms the server-assigned identity is unchanged and status/list are In Design.
6. **Continue clarification.** Resolve material questions before readiness.

Never recreate a card after a lost response; route ambiguity to recovery.

## Readiness gate — In Design to Ready

Before transition, confirm:

- Required canonical sections exist.
- Material `Pending:` entries are resolved.
- Material Open Questions are resolved. The section may be omitted or contain only `None`, `N/A`, or `No open questions` (optionally as one bullet and with a terminal period); the Ready transition removes that resolved optional section. Any other content remains unresolved.
- Objective, scope, non-goals, acceptance criteria, and verification expectations are observable and claimable.
- Dependencies and blockers are explicit and use Work Unit IDs where applicable.
- Routine scoped decisions are resolved from Work Unit and repository authority;
  only dangerous deletion/data loss or a hard blocker requires escalation.
- Useful repository artifacts are linked concisely.

Then read again, apply the guarded transition with latest version and durable operation ID, and read back. Completion: status is `ready`, list is Ready, identity is unchanged, and no unresolved material question remains.

If work is not ready, leave it in In Design and report the smallest unresolved decision. Do not block merely because clarification is ongoing.

## Routes

- In Design with pending material questions → resolve autonomously from current
  authority; escalate only contradictory authority or an unavailable hard
  prerequisite.
- Ready → `trello-work-deliver` for claim.
- Ambiguous/partial/stale/conflicting mutation → `trello-work-recover`.
- Out-of-contract change → revise the bounded Work Unit autonomously when
  authority is clear; otherwise route a genuine contradiction/hard blocker.

## Common pitfalls

- Duplicating software-design practice instead of delegating it.
- Converting an Inbox card by creating a second card.
- Moving to Ready with unresolved material `Pending:` entries.
- Guessing IDs after draft dry run.
- Blindly retrying creation or transition after a timeout.
- Claiming, implementing, completing, or archiving from this skill.

## Verification checklist

- [ ] Board and target identity were explicit.
- [ ] Latest read/version and durable operation ID guarded each mutation.
- [ ] Ordinary Inbox intake preserved the same card.
- [ ] Material questions are explicit or resolved.
- [ ] Ready criteria are complete and read back.
- [ ] Engineering methodology remained outside this skill.
- [ ] No claim, post-Ready transition, production migration, or archival occurred.
