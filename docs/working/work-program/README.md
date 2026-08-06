# Work Program Map (Component B)

> Cold-start question this directory answers:
>
> **“It has been two weeks. I remember nothing. What must I do next, and what
> are the frontier tasks?”**

Read [`SEQUENCE.md`](SEQUENCE.md) first for the current answer. Read this file
when you need the rules, authority split, sync ritual, or an explanation of the
system.

## Purpose

Greek Essence tracks executable work as Trello Work Units. Trello is excellent
at one card’s contract and lifecycle. It is weak at an instant cross-program
map and a recommended “pull next” order after time away.

This directory is **Component B**: a thin repo-side navigation and selection
aid. It does not replace Trello, grilling decisions, or active work-item
handoffs.

| Component                    | Location                                                                 | Answers                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **A — Work Unit tracker**    | Trello board `Greek Essence` via `jz-trello-flow`                        | What is this unit? Who owns it? What state is it in? What hard prerequisites exist? Is it done?            |
| **B — Work program map**     | This directory                                                           | How do units relate? Which fronts are open? What should we choose next if free? What is parked on purpose? |
| Active multi-session handoff | Root [`NEXT.md`](../../../NEXT.md) + `docs/working/work-items/*/NEXT.md` | Continue one already-active repository work item                                                           |
| Unshaped ideas               | Root [`TODO.md`](../../../TODO.md)                                       | Remember work not yet promoted into Trello                                                                 |
| Product truth                | [`docs/grilling/`](../../grilling/)                                      | What the service is allowed to be and do                                                                   |

## Non-goals

- Not product authority and not implementation authorization by itself.
- Not a second backlog that duplicates every Work Unit field.
- Not a substitute for re-reading the selected Trello card before claim/design/delivery.
- Not a place for secrets, credentials, personal traveler data, raw logs, or long command transcripts.

## Authority split (single writer per fact)

| Fact                                 | Canonical writer    | May B show it?   | May B override it? |
| ------------------------------------ | ------------------- | ---------------- | ------------------ |
| WU identity, title, URL              | Trello (A)          | Yes (derived)    | No                 |
| Lifecycle status / list              | Trello (A)          | Yes (derived)    | No                 |
| Owner claim                          | Trello (A)          | Yes (derived)    | No                 |
| Hard prerequisites (`blocked_by`)    | Trello (A)          | Yes (draw DAG)   | No                 |
| Parent hierarchy                     | Trello (A)          | Yes (derived)    | No                 |
| Card `priority`, labels, type        | Trello (A)          | Yes (derived)    | No                 |
| Objective / AC / verification text   | Trello (A)          | Link only        | No                 |
| Recommended pull order               | **B annotations**   | n/a              | Yes                |
| Parked though Ready / do-not-pull    | **B annotations**   | n/a              | Yes                |
| Track narrative and planning notes   | **B annotations**   | n/a              | Yes                |
| One claimed unit’s next session step | work-item `NEXT.md` | Optional pointer | No                 |

**Conflict rule:** on hard task facts, Trello wins. Mark B dirty and refresh.
Soft order and parking live only in B unless the operator intentionally changes
a Trello field (for example clearing a stale blocker or lowering priority).

## Hard DAG vs soft sequence

### Hard DAG (Trello only)

An edge `WU-X → WU-Y` in `blocked_by` means: **Y cannot honestly start until X
is Done** (or X’s required outcome already exists).

Use hard edges only for real prerequisites. Do not encode preference as fake
blockers (example: do not block a small DX card on an unrelated product spike).

### Soft sequence (B only)

A ranked list of **eligible** work the operator prefers when capacity is free.

Eligible roughly means:

- status allows attention (commonly Ready; Inbox/In Design for design or agency intake),
- hard blockers are Done,
- not parked in B,
- not solely an external wait unless the action is “nudge / wait”,
- still wanted by the program.

B never marks a Work Unit Done.  
Trello never stores the full cross-track storyboard.

## Files

| File                         | Role                                                   |
| ---------------------------- | ------------------------------------------------------ |
| [`README.md`](README.md)     | Durable rules for humans and agents (this file)        |
| [`SEQUENCE.md`](SEQUENCE.md) | Current map, frontier, soft pull order, parking, drift |

Optional later: `tracks/*.md` only if a single track needs lasting notes.
Prefer keeping `SEQUENCE.md` thin.

## SEQUENCE.md structure

`SEQUENCE.md` has two layers:

1. **Derived projection** — rebuilt from a live Trello read. Replaceable.
2. **Operator annotations** — hand-maintained intent preserved across refresh:
   pull order, parking reasons, track goals, external waits.

Also record:

- board name,
- last refreshed timestamp (UTC date is enough),
- drift status: `clean` or `dirty` with bullets.

## Sync ritual (how A and B stay aligned)

Default model: **pull-based reconciliation**.

```text
Trello (A)  --refresh derived facts-->  SEQUENCE.md (B)
SEQUENCE.md (B) --selection advice-->  human / agent
SEQUENCE.md (B) --intentional task-fact fixes only-->  Trello (A)
```

### When to refresh B

- Start of a planning session after time away
- After a batch of Trello status/dependency/priority changes
- Before answering “what is next?”
- After closing a meaningful Work Unit

### When refresh is not required

- Mid-implementation of one already claimed unit (use that WU + its work-item `NEXT.md`)
- Every minor checklist tick on a single card

### Refresh steps

1. Read Work Units:
   `jz-trello-flow list --board "Greek Essence" --output json`
2. Rebuild the **Derived from Trello** sections in `SEQUENCE.md`.
3. Preserve **Operator annotations** unless the operator is changing intent.
4. Recompute helpers:
   - unblocked / frontier candidates
   - soft-order items whose WU is missing or Done
   - Ready-but-parked callouts
   - stale hard edges (child still lists a Done blocker)
5. Set `last_refreshed` and `drift`.
6. Do not invent new WU IDs or change Trello status from a refresh alone.

### Intentional A writes suggested by B

Examples: clear a Done id from `blocked_by`, close a finished parent WU, add a
`parked` label if agents keep auto-pulling Ready cards. Those are ordinary
guarded Trello mutations with operator authorization — not automatic sync.

## Cold-start procedure (humans and agents)

After two weeks away:

1. Read [`SEQUENCE.md`](SEQUENCE.md) top sections: **Do next**, **Frontier**, drift.
2. Skim track map and soft pull order.
3. Re-read the chosen Work Unit from Trello (`jz-trello-flow get WU-N --board "Greek Essence"`).
4. If B and A disagree on status/blockers/owner: **A wins**; refresh B.
5. Only then design, claim, or continue delivery under `docs/GIT_WORKFLOW.md` and the managed Trello skills.
6. Root [`NEXT.md`](../../../NEXT.md) still lists active multi-session repo work items; it is not the global program map.

## Agent rules

Agents MUST:

- Treat B as selection aid and explanation source for this process.
- Re-read Trello before claim, design start, transition, or implementation.
- Keep hard dependency edits on Trello; keep soft order/parking edits in B.
- Explain the system from this README when the operator asks how planning works.

Agents MUST NOT:

- Implement solely because a WU is first in soft pull order.
- Treat Ready on Trello as an automatic execution queue when B parks it.
- Dual-write status or acceptance completion into B as a second source of truth.
- Put secrets, personal data, or raw logs in this directory.
- Archive Trello cards (human-only).

## Related repository pointers

- Trello ↔ Git lifecycle: [`docs/GIT_WORKFLOW.md`](../../GIT_WORKFLOW.md)
- Docs entry map: [`docs/README.md`](../../README.md)
- Active work-item router: [`NEXT.md`](../../../NEXT.md)
- Operator idea inbox: [`TODO.md`](../../../TODO.md)
- Board selection: always pass `--board "Greek Essence"` explicitly

## Proportionality

v1 is two Markdown files and a manual/agent refresh ritual. Add scripts or CI
drift checks only if repeated planning pain appears. With roughly a dozen
active Work Units, planning-fresh reconciliation is enough.
