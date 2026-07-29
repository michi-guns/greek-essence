# Project TODO

`TODO.md` is the operator-managed backlog and idea inbox for work that must be remembered but is not currently active.

It is not an execution queue, task contract, project-status ledger, or agent handoff. [`NEXT.md`](NEXT.md) remains the single source for the immediate project continuation. An item appearing here does not authorize an agent to implement it.

## Workflow

```text
New idea or pending work
        ↓
TODO.md — Inbox
        ↓
Clarified and prioritized
        ↓
Formal plan or task contract
        ↓
NEXT.md when it becomes active
        ↓
Completed and removed or reconciled into durable project history
```

## Rules

- The operator controls priority and promotion into active work.
- Agents may add a clearly attributable item when new pending work emerges, clarify an existing item without changing its intent, or mark an item blocked when supported by evidence.
- Agents must not implement, delegate, schedule, or start an item merely because it appears here.
- Before implementation, promote the item into the appropriate plan, issue, or task contract. Put only the immediate continuation in `NEXT.md`.
- Keep entries concise: desired outcome, useful source/reference, and any known decision or blocker.
- Do not store runtime state, process IDs, session IDs, raw logs, secrets, credentials, or detailed execution evidence here.
- Remove completed items once their outcome is reconciled into Git history, task records, or another durable source of truth. This file is not a changelog.

## Inbox

- [ ] Re-establish performance budgets after the new architecture, route set,
      rendering model, and third-party integrations are approved.
  - **Desired outcome:** Replace prototype-specific measurements with budgets
    and routes that represent the expanded product without weakening
    accessibility, best-practice, or SEO expectations.

<!-- New unprioritized items go here before entering the planned dependency graph. -->

## Planned

No non-active work is currently planned. Requirements rebaseline and
architecture discovery are active through `NEXT.md`; implementation planning
must wait for their approved outcomes.

<!-- Agreed and prioritized work that is not active yet. Link its plan/task when available. -->

## Blocked / awaiting decision

<!-- Items that require operator input or an external dependency before planning. -->

## Later / ideas

- [ ] Adopt Trello as the durable task and work-coordination system.
  - **Available tooling:** An existing Trello CLI allows agents to perform CRUD operations on the operator's boards.
  - **Current position:** The repository-local work-item and per-item `NEXT.md` system is intentionally ephemeral.
  - **Future direction:** Define how agents use Trello for assignment, ownership, status, and handoff before replacing the file-based system.

<!-- Uncommitted possibilities that should remain visible but need clarification. -->
