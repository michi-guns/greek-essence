# Docs Management and Next.js Architecture Plan

## Status

In Progress

## Ownership and Scope

Owner: Hermes Agent (`greek-essence`)

Work Unit: [Plan docs management and Next.js architecture (grilling-locked) (WU-44)](https://trello.com/c/mz7FD4rm)

Parent: [Bootstrap Public Preview platform foundations (WU-43)](https://trello.com/c/bk57rL7w)

Scope: author and land the grilling-locked working plan for documentation management and Next.js source architecture. Does not install Neon, Drizzle, or Sanity.

## Current State

- WU-44 claimed `in_progress` by `hermes-greek-essence`.
- Branch: `docs/wu-44-docs-nextjs-plan`
- Plan artifact: `docs/working/DOCS_AND_NEXTJS_ARCHITECTURE_PLAN.md`
- Inspiration: PR #50 / `docs/migration-v4` (non-authoritative)
- Authority: `docs/grilling/**` accepted decisions

## Next Recommended Action

Obtain operator accept/correct/reject on the plan. On accept: mark acceptance in plan §8, open/update PR, run docs-range gates, move WU-44 through Review → Done after merge and cleanup. Then pull WU-45 or WU-46 per plan phase 2/3.

## Done When

WU-44 acceptance criteria are met on Trello, plan is on `main`, operator acceptance is recorded, and task branch/worktree cleanup is complete.

## Constraints

- Do not promote `docs/new-proposed-docs/` wholesale.
- Do not install platform packages on this branch.
- Do not reopen accepted grilling decisions.
