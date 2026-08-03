---
name: trello-work-deliver
description: Claim and deliver Ready, In Progress, Blocked, or Review Trello Work Units through Done. Use for ownership, implementation handoff, progress evidence, blocking or resuming, review disposition, and justified completion.
---

# Trello Work Deliver

## Overview

Own the normal delivery lifecycle from Ready through read-back-confirmed Done. This skill coordinates durable Trello state and concise evidence; Superpowers or equivalent harness practice owns software design, implementation, TDD, debugging, review, and verification methodology.

The normative contract is [`packages/trello-work-cli/assets/agent-workflow-protocol.md`](references/agent-workflow-protocol.md). Use installed `jz-trello-flow` docs for exact command syntax and effective configured transitions.

## When to use

Use this skill for:

- Claiming a Ready Work Unit.
- Resuming confirmed owned In Progress work.
- Recording material progress/evidence.
- Moving a genuine blocker to Blocked.
- Resuming or releasing a resolved Blocked Work Unit.
- Submitting In Progress work to Review.
- Returning Review work to In Progress.
- Completing accepted Review work as Done.

Do not use it for:

- Inbox, draft, or In Design clarification; use `trello-work-design`.
- Read-only selection/status routing; use `trello-work-orchestrator`.
- Ambiguous, partial, stale, replayed, conflicting, or drifted mutation outcomes; use `trello-work-recover`.
- Claiming atomic locking, migrating production boards, or archiving cards.

## Required inputs

- Explicit board ID or exact board name.
- Current Work Unit/card reference and latest read.
- Stable owner identity for claim/resume.
- Repository instructions, acceptance criteria, approval state, and applicable engineering-practice capabilities.
- Durable repository links for detailed evidence.

## Universal mutation discipline

For every mutation:

1. Select the board explicitly and prefer JSON output.
2. Read immediately before mutation.
3. Use the latest observed version.
4. Use a durable unique operation ID for the intended operation.
5. Reuse that ID only to recover the same intent.
6. Make the minimum required mutation.
7. Read back and verify the exact postcondition.
8. Route uncertainty to `trello-work-recover`; never retry blindly.

`--if-version` is a best-effort stale-read check, not a lock or transaction.

Before writing a description or metadata, inspect the exact final-payload preflight. `DESCRIPTION_BUDGET_EXCEEDED` is a confirmed no-write result: preserve the operation ID and content, shorten deliberately, and never delete recovery markers or retry blindly. A dry-run wrapper/rendering error does not imply a mutation; read back before classifying any uncertain result.

## Claim Ready work

Claiming has two required postconditions: expected stable owner and `in_progress` status. Current Trello operations do not make these atomic.

1. **Read Ready.** Stop if status changed, a blocker exists, or a conflicting owner/claim is present. Completion: the task is still safely claimable.
2. **Choose claim identity.** Select stable owner and one durable claim identity; derive distinct operation IDs for owner update and transition while retaining common local recovery context. Completion: retries cannot be confused with new intent.
3. **Update owner.** Apply the guarded metadata update with latest version. Completion: read-back confirms expected owner.
4. **Read again.** Obtain the new latest version and check for conflict. Completion: transition intent remains valid.
5. **Transition Ready → In Progress.** Use a distinct operation ID for this step. Completion: final read-back confirms both expected owner and `in_progress` status/list.
6. **Begin engineering work only now.** Before both postconditions exist, a claim is partial—not acquired.

This reduces duplicate work but is not an atomic or globally exclusive lock. Stronger allocation requires another approved mechanism.

## Execute and update

After a confirmed claim:

1. Load applicable Superpowers capabilities when installed; otherwise use equivalent repository engineering practice.
2. Follow repository design, plan, testing, review, and approval rules.
3. Keep detailed designs, source, logs, and CI evidence in their authoritative systems.
4. Update Trello only when scope/acceptance, owner/resumability, blockers, implementation frontier, review frontier, or recovery-relevant state materially changes.
5. Record concise summaries and repository links; do not duplicate full logs.

Completion: the current Work Unit and repository evidence let another actor resume safely without turning the card into a journal.

## Block and resume

Use `In Progress → Blocked` only when useful progress cannot continue.

Before or with blocking, record what is blocked, why, who/what can unblock it, safest next action, and useful evidence/recovery identity. Read back Blocked.

After resolution:

- `Blocked → In Progress` when the existing owner remains valid.
- `Blocked → Ready` when ownership is released and a fresh claim is required.

Read back before resuming. Clarification still possible during normal work is not automatically a blocker.

## Submit to Review

Before `In Progress → Review`, confirm:

- Acceptance criteria appear satisfied.
- Applicable implementation verification passed.
- No known blocker prevents review.
- Repository artifacts and Git/CI references are current.
- The card has a concise evidence summary sufficient to evaluate or resume.

Apply the guarded transition and read back `review`/Review. No specific Superpowers artifact, independent reviewer, PR, or CI system is mandatory unless repository instructions or the Work Unit require it.

## Review disposition

- Material changes or failed acceptance → record concise findings, transition `Review → In Progress`, read back, and resume engineering practice.
- Accepted completion → apply the Done gate below.
- Ambiguous review mutation → `trello-work-recover`.

## Done gate

Transition `Review → Done` only when all are true:

1. Current acceptance criteria are satisfied.
2. Applicable verification passed.
3. No known blocking issue remains.
4. Concise supporting evidence and durable links are present.
5. Any dangerous-deletion approval or hard-prerequisite clearance required by the current Work Unit exists.

Agent judgment cannot override failing criteria, required failing checks, known
blockers, a dangerous-deletion approval gate, or an unavailable hard
prerequisite. Read back `done` and the Done list.

Done terminates agent lifecycle mutation. Report that a human may perform final portfolio review and manually archive the card. Never archive, delete, reopen for cleanup, or close Done as a substitute.

## Routes

- Inbox/In Design → `trello-work-design`.
- Ambiguous/partial/stale/replay/conflict/drift → `trello-work-recover`.
- Normal Ready/In Progress/Blocked/Review → continue this skill.
- Done → stop; human review/manual archival only.

## Common pitfalls

- Starting implementation after only the owner update or only the transition.
- Calling the claim atomic or lock-protected.
- Reimplementing Superpowers methodology inside lifecycle instructions.
- Recording every command in Trello instead of proportionate evidence.
- Blocking work that is merely incomplete.
- Completing despite failed acceptance or verification.
- Automatically archiving Done cards.

## Verification checklist

- [ ] Explicit board and latest read guarded each action.
- [ ] Every mutation used current version, durable operation ID, and read-back.
- [ ] Work began only after owner and In Progress were both confirmed.
- [ ] Detailed evidence stayed in repository/Git/CI; Trello remained concise.
- [ ] Review and Done gates are satisfied.
- [ ] Exceptional uncertainty routed to recovery.
- [ ] Done ended agent mutation and no archival occurred.
