---
name: greek-essence-work-program
description: Use when cold-starting, asking what next, frontier tasks, or prioritizing WUs across Trello and the repo work-program map.
---

# Greek Essence work program (A + B)

## Overview

Help the operator choose the best course of action after time away, or when many Work Units compete.

Two components:

| Component                 | Where                                             | Owns                                                                                           |
| ------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **A — Work Unit tracker** | Trello board `Greek Essence` via `jz-trello-flow` | Identity, lifecycle, owner, hard `blocked_by`, card priority/labels, objective/AC, transitions |
| **B — Work program map**  | `docs/working/work-program/`                      | Instant map, frontier, soft pull order, parking, external waits, drift notes                   |

Canonical rules: [`docs/working/work-program/README.md`](../../../docs/working/work-program/README.md)  
Live answer sheet: [`docs/working/work-program/SEQUENCE.md`](../../../docs/working/work-program/SEQUENCE.md)

This skill calibrates selection and explanation. It does **not** replace Trello lifecycle skills.

## When to use

Use when the operator:

- cold-starts (“two weeks away”, “I remember nothing”)
- asks what to do next, what the frontier is, or how to prioritize WUs
- wants the relationship map across programs/tracks
- asks how Component A/B planning works
- needs a refresh of the work-program sequence from Trello

Do **not** use this skill as a substitute for:

- single-card design → `trello-work-design`
- claim/deliver/review/complete → `trello-work-deliver`
- ambiguous Trello mutation recovery → `trello-work-recover`
- pure single-WU status routing after a target is already chosen → `trello-work-orchestrator`
- product grilling truth → `docs/grilling/`

## Authority order for selection

1. Current operator instructions
2. Hard task facts from live Trello (A)
3. Soft order / parking / track intent from `SEQUENCE.md` (B annotations)
4. Root `NEXT.md` and active work-item handoffs for already-active multi-session work
5. `TODO.md` only as unshaped ideas (never an execution queue)

Conflict on status, owner, or `blocked_by`: **Trello wins**. Mark B dirty and refresh.

## Hard DAG vs soft sequence

- **Hard:** Trello `blocked_by` / `parent` only. Real prerequisite edges.
- **Soft:** B pull order among eligible work. Preference, not a gate.
- **Parked:** May be Ready on Trello and still do-not-pull in B (example pattern: early platform work).
- Never encode soft preference as fake `blocked_by`.

## Workflow

1. **Orient.** Read `docs/working/work-program/SEQUENCE.md` (and `README.md` if rules are unclear). Note `Last refreshed` and `Drift`.  
   Done when: cold-start sections are known.

2. **Refresh when needed.** Refresh B derived sections if SEQUENCE is missing, drift is dirty, refresh is older than the planning need, or the operator asks for a current map.  
   Command:
   `jz-trello-flow list --board "Greek Essence" --output json`  
   Rebuild only **Derived from Trello** tables/DAG/frontier inputs; preserve operator annotations unless intent changes. Update `Last refreshed` and `Drift`.  
   Done when: derived facts match this session’s Trello read or drift is explicitly reported.

3. **Build the decision picture.** From A+B, separate:
   - do-next recommendation (one primary)
   - frontier now
   - hard-blocked
   - parked
   - external wait / nudge
   - active handoffs in root `NEXT.md`
   - hygiene repairs on Trello (stale Done blockers, closeout candidates)  
     Done when: every active WU is classified; no silent drops.

4. **Verify top candidates on Trello.** Before recommending claim/design/start on a specific WU, re-read it:
   `jz-trello-flow get WU-N --board "Greek Essence" --output json`  
   Confirm status, owner, blockers, open questions.  
   Done when: recommendation cites live card facts, not SEQUENCE alone.

5. **Recommend, do not auto-start.** Present options; prefer one best next action. Ask one focused decision question when needed.  
   Done when: operator can choose without reading the whole board.

6. **Route after the operator chooses.**
   - program still unclear → stay in this skill / refresh B
   - design/clarify card → `trello-work-design`
   - ready to claim or resume delivery → `trello-work-deliver` (via orchestrator if helpful)
   - Trello state dirty/ambiguous → `trello-work-recover`  
     Done when: exactly one next route or a clear stop for operator input.

## Required report shape

Use this structure (omit empty sections only with a one-line reason):

```text
Do next: <one primary action + WU if any>
Why: <hard facts + soft intent>
Frontier: <bullets>
Parked / waiting: <bullets>
Blocked: <bullets>
Drift / hygiene: <none or bullets>
Active repo handoffs (NEXT.md): <none or bullets>
Need from you: <one question or "none — say go on <WU>">
```

## Hard stops

- Do not implement, claim, transition, or design-start solely because a WU is #1 in soft order.
- Do not treat Trello Ready as an automatic queue when B parks it.
- Do not dual-write lifecycle status into SEQUENCE as a second Done/In Progress authority.
- Do not invent WU IDs, board defaults, or hard edges.
- Always pass `--board "Greek Essence"` explicitly.
- Never archive Trello cards (human-only).
- No secrets, personal traveler data, or raw logs in SEQUENCE/README.

## Refresh ritual (short)

```text
A (Trello) --list/get--> derived sections in SEQUENCE.md
SEQUENCE annotations --selection advice--> operator/agent
Annotations never override live blockers/status
Intentional Trello fixes (clear stale blocker, close WU) are normal guarded mutations — not automatic sync
```

Planning-fresh is enough; continuous identical sync is not required.

## Common pitfalls

1. Answering “what next?” from chat memory without SEQUENCE + Trello.
2. Serializing unrelated tracks into one fake total order.
3. Pulling parked Ready cards (for example early Drizzle) because priority is high.
4. Ignoring root `NEXT.md` active handoffs while only reading Trello Inbox.
5. Duplicating the live board into this skill body — keep state in SEQUENCE/Trello only.
6. Mutating Trello during a read-only planning pass without operator authorization.

## Verification checklist

- [ ] SEQUENCE read; refresh performed or drift explicitly reported
- [ ] Board selector explicit: `Greek Essence`
- [ ] Hard blockers taken from live Trello for recommended WUs
- [ ] Parking and external waits respected
- [ ] One primary recommendation + clear alternatives
- [ ] No claim/implement/transition performed from soft order alone
- [ ] Next lifecycle skill named only after operator direction or explicit authorization to proceed
