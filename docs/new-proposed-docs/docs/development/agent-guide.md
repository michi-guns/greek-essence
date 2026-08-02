# AI Coding Agent Guide

## Mission

Evolve the travel agency application without breaking domain, data ownership,
or documentation boundaries.

## Before coding

1. Read `docs/index.md`.
2. Read `docs/documentation-protocol.md`.
3. Read the relevant current-state and domain documents.
4. Read linked ADRs.
5. Check active assumptions and open questions.
6. Inspect existing repository conventions.

## During implementation

- Prefer small, reviewable vertical slices.
- Keep domain code framework-independent.
- Validate untrusted input with Zod.
- Keep Drizzle and Sanity inside infrastructure adapters.
- Snapshot commercial data entering quotes and bookings.
- Record new uncertainty as assumptions.
- Do not rewrite accepted ADR history.

## Before completion

- Run relevant type checks, linting, tests, builds, and migration checks.
- Update current-state docs when behavior changes.
- Create or supersede an ADR when architecture changes.
- Update indexes and links.
- Report skipped or failed checks honestly.
