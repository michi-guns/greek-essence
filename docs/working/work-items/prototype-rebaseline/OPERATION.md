# Prototype Rebaseline

## Goal

Preserve the existing Greek Essence prototype as recoverable reference, remove
its friction from active development, capture the client's materially expanded
requirements, and establish a clean foundation for the expanded product.

This is a temporary operation document. Settled decisions belong in durable,
focused documentation; this file may be removed when the operation is complete.

## Boundaries

- Prototype material is reference and inspiration, not current authority.
- Do not implement new product features during this operation.
- Do not migrate old code merely to preserve it.
- Do not copy prototype source into the active documentation tree.
- Do not delete or overwrite files without explicit path-level user approval.
- Do not select future product architecture without confirmed product needs.
- Do not install candidate platform dependencies or model persistent data before
  their responsibilities and risks are approved.

## Current State

- The remote-tracking archive ref `origin/archive/showcase-prototype-v0` exists at
  `3a29ce9615f20b4b41089543c972a3115f79672f`.
- The operator archived the former protocol, product, prototype, technical,
  design, tooling, and reference documentation under
  [`../../../archive/showcase-prototype-v0/`](../../../archive/showcase-prototype-v0/README.md).
- The archive is explicitly non-authoritative; current authority routes through
  `AGENTS.md`, the active work item, accepted grilling decisions, and future
  promoted canonical documentation.
- The structural migration principles are in
  [`../../NEXTJS_LAYER_2_MIGRATION.md`](../../NEXTJS_LAYER_2_MIGRATION.md).
- The current-code inventory and provisional move map are in
  [`../../NEXTJS_LAYER_2_INVENTORY.md`](../../NEXTJS_LAYER_2_INVENTORY.md).
- The active-tree classification is in [`RETENTION_PLAN.md`](RETENTION_PLAN.md).
- The earlier capability proposal is retained as withdrawn in
  [`ARCHITECTURE_PROPOSAL.md`](ARCHITECTURE_PROPOSAL.md).
- Expanded requirements are routed through
  [`REQUIREMENTS_INTAKE.md`](REQUIREMENTS_INTAKE.md), with architecture choices
  tracked in [`DECISION_REGISTER.md`](DECISION_REGISTER.md).
- The first operator-authored, agent-assisted working-draft batch is preserved under
  [`sources/`](sources/) and normalized in
  [`REQUIREMENTS_BATCH_01.md`](REQUIREMENTS_BATCH_01.md).
- The preview release is confirmed as public and production-facing; its client
  questions and launch-quality gate are in
  [`PREVIEW_RELEASE_VALIDATION.md`](PREVIEW_RELEASE_VALIDATION.md).
- Stateful project and feature design now routes through
  [`../../../grilling/GRILLING.md`](../../../grilling/GRILLING.md), beginning
  with the high-level public-preview product boundary.
- The grilling protocol now requires product-management and travel-agency
  operations coaching when requirements hide ambiguity or operational risk.
- The closed showcase execution records were removed from `.scratch/` with
  exact user approval; the archive branch retains them.
- No application files have been moved or removed.

## Workstreams

| Workstream | Status | Outcome |
| --- | --- | --- |
| Verify archive | Complete | Confirmed the recovery point contains the expected prototype code and assets |
| Curate reference | Complete | Selected useful screenshots, patterns, and cautions without duplicating source |
| Archive former documentation | Complete | Preserved the old baseline under one explicitly non-authoritative boundary |
| Plan retention and removal | Complete | Classified active paths and removed only the explicitly approved closed execution records |
| Capture expanded requirements | In progress | Batch 01 is a provisional internal baseline; grill preview scope, ingest remaining material, and isolate client-validation needs |
| Grill product and features | In progress | Lock the high-level preview promise, derive real feature boundaries, then grill each feature statefully |
| Establish new architecture | Pending | Select CMS, data, backend, runtime, security, and module boundaries from approved requirements |
| Promote durable decisions | Pending | Write focused architecture documents and a concise documentation router |

## Approval Gates

User approval is required before:

- copying selected visual artifacts into the curated reference;
- deleting, moving, or replacing active prototype files; or
- adopting the final feature names and module boundaries.

## Completion Criteria

- The full prototype remains recoverable outside the active source tree.
- Curated reference material is clearly non-authoritative and useful.
- All active-path removals were explicitly approved and verified.
- The new architecture reflects confirmed product boundaries rather than the
  prototype structure.
- Durable documentation contains the settled outcomes.
- No operation-specific instruction remains in `AGENTS.md` or `docs/working/`.
