# Greek Essence Grilling Workspace

This is the thin router for Greek Essence decision grilling. It establishes the
layer sequence and points to the rules for each layer. It does not track active
work, completion, or the next question; root [`NEXT.md`](../../NEXT.md) and the
selected work-item handoff own that state.

## Sequence

1. [Product and Domain Truth](layers/product-domain-truth.md) — define what the
   service means, which capabilities exist, and the business concepts and
   invariants that later architecture must preserve.
2. [Foundation Design](layers/foundation-design.md) — choose the technology,
   service boundaries, architecture, domain representation, integrations, and
   other durable development foundations.
3. [Launch Readiness](layers/launch-readiness.md) — verify the owners, approved
   inputs, provider facts, operating procedures, and evidence required to launch
   the accepted product and foundation safely.

The sequence is dependency-driven, not an irreversible waterfall. A downstream
layer may expose a missing upstream decision, but it must route that issue back
to the owning layer instead of silently redefining it.

## Permanent Guidance

- [Grilling protocol](protocol.md)
- [Project glossary](GLOSSARY.md)
- [Approved classification](CLASSIFICATION.md)
- [Foundation Design track map](foundation-design/README.md)

## Artifact Rule

Active `GRILLING.md` ledgers and accepted `DECISIONS.md` files remain the sources
for their recorded decisions. Existing artifacts stay at their current paths.
The approved [classification](CLASSIFICATION.md) determines whether their
material is retained, promoted, moved, reopened, or dropped; this router does
not track that work and is not implementation authorization.
