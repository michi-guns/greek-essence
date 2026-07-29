# Prototype Rebaseline

## Status

Active

## Ownership and Scope

Owner: Codex (`/root`)

Scope: prototype archive verification, curated reference material, active-tree
retention and removal planning, expanded client-requirements intake,
architecture rebaseline, and promotion of settled documentation.

## Current State

- The operation and its boundaries are documented.
- The prototype archive ref and its Git object connectivity are verified.
- The operator moved the former protocol, PRD, prototype specification,
  technical design, design system, tooling documentation, and prototype
  references under `docs/archive/showcase-prototype-v0/`.
- The archive has an explicit non-authoritative notice; current authority now
  routes through `AGENTS.md`, the active work item, accepted grilling decisions,
  and future promoted canonical documents.
- The Layer 2 brief, current-code inventory, and active-tree retention plan
  exist.
- The approved closed showcase execution records are absent from the active
  tree; `pnpm check` and `pnpm build` pass afterward.
- The earlier capability proposal is withdrawn because materially expanded
  client requirements invalidate its static-first assumptions.
- A structured requirements intake and architecture decision register now
  capture CMS, Supabase, Drizzle, data, authorization, runtime, migration, and
  operational questions without selecting solutions prematurely.
- The first client-document batch is preserved under `sources/` and normalized
  into 27 reported requirements, candidate domain ownership, scope changes, and
  15 explicit conflicts or clarification needs.
- The batch is confirmed as an operator-authored, agent-assisted working draft
  that had repository context but has not been read or approved by the client.
- The end-of-August preview is operator-confirmed as a public,
  production-facing release expected to receive real visitors and enquiries.
- A minimal client-validation checklist and production-facing Phase 1 gate are
  documented separately from internally owned technical decisions.
- The stateful grilling workflow is active at `docs/grilling/GRILLING.md`; it
  starts with the public preview's product promise and will create feature
  directories only after high-level feature boundaries are accepted.
- `AGENTS.md` and the grilling protocol require senior product-management and
  travel-agency operations coaching when requirements are unclear, inconsistent,
  solution-led, or conceal likely operational problems.
- The documentation rebaseline passes `pnpm format:check` and
  `git diff --check`.
- No application files have been moved or removed.

## Next Recommended Action

Continue the project-level session from `docs/grilling/GRILLING.md` D-001,
persisting each answer before moving to the next question. Use the accepted
high-level decisions to create and sequence feature-specific grills.

## Done When

The preview-release requirements are internally coherent, material client
questions are isolated, and the remaining evidence is sufficient to evaluate
CMS, Supabase, Drizzle, data, security, runtime, and migration boundaries
without relying on prototype assumptions.

## Constraints

- Do not remove or reorganize the runnable prototype before its replacement
  architecture and coordinated path changes are approved.
- Do not treat prototype material as current product or architecture authority.
- Do not treat anything under `docs/archive/showcase-prototype-v0/` as current
  authority, even when an archived document describes itself as approved or
  authoritative.
- Do not install or configure a CMS, Supabase, Drizzle, or another backend
  dependency before its responsibility boundary is approved.
- Obtain user approval before changing active paths.

## Related Documents

- [Operation](OPERATION.md)
- [Layer 2 migration principles](../../NEXTJS_LAYER_2_MIGRATION.md)
- [Layer 2 inventory](../../NEXTJS_LAYER_2_INVENTORY.md)
- [Archived prototype baseline](../../../archive/showcase-prototype-v0/README.md)
- [Retention plan](RETENTION_PLAN.md)
- [Architecture proposal](ARCHITECTURE_PROPOSAL.md)
- [Expanded requirements intake](REQUIREMENTS_INTAKE.md)
- [Decision register](DECISION_REGISTER.md)
- [Requirements Batch 01 synthesis](REQUIREMENTS_BATCH_01.md)
- [Public preview release validation](PREVIEW_RELEASE_VALIDATION.md)
- [Active project grilling](../../../grilling/GRILLING.md)
- [Grilling protocol](../../../grilling/protocol.md)
