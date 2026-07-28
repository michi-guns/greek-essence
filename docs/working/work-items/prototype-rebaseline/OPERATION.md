# Prototype Rebaseline

## Goal

Preserve the existing Greek Essence prototype as recoverable reference, remove
its friction from active development, and establish a clean foundation for the
expanded product.

This is a temporary operation document. Settled decisions belong in durable,
focused documentation; this file may be removed when the operation is complete.

## Boundaries

- Prototype material is reference and inspiration, not current authority.
- Do not implement new product features during this operation.
- Do not migrate old code merely to preserve it.
- Do not copy prototype source into the active documentation tree.
- Do not delete or overwrite files without explicit path-level user approval.
- Do not select future product architecture without confirmed product needs.

## Current State

- The remote-tracking archive ref `origin/archive/showcase-prototype-v0` exists at
  `3a29ce9615f20b4b41089543c972a3115f79672f`.
- The curated reference boundary exists at
  [`../../../reference/showcase-prototype-v0/index.md`](../../../reference/showcase-prototype-v0/index.md).
- The structural migration principles are in
  [`../../NEXTJS_LAYER_2_MIGRATION.md`](../../NEXTJS_LAYER_2_MIGRATION.md).
- The current-code inventory and provisional move map are in
  [`../../NEXTJS_LAYER_2_INVENTORY.md`](../../NEXTJS_LAYER_2_INVENTORY.md).
- No application files have been moved or removed.

## Workstreams

| Workstream | Status | Outcome |
| --- | --- | --- |
| Verify archive | Next | Confirm the recovery point contains the expected prototype code and assets |
| Curate reference | Pending | Select useful screenshots, patterns, and cautions without duplicating source |
| Plan retention and removal | Pending | Classify active paths and obtain exact deletion approval |
| Establish new architecture | Pending | Build the approved structure directly from confirmed product needs |
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
