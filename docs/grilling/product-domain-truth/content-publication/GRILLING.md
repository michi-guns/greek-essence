# Content Publication Truth Grilling

## Status

Active Product and Domain Truth gap review before Foundation Design.

This grill does not authorize implementation, dependency installation, schema
migration, deployment, or destructive path changes. Use
[`../../DECISIONS.md`](../../DECISIONS.md),
[`../../CLASSIFICATION.md`](../../CLASSIFICATION.md), and
[`../../protocol.md`](../../protocol.md).

## Scope

Resolve only the two approved upstream gaps needed before the Editorial Content
Platform foundation:

1. minimum publishable completeness for a Destination;
2. withdrawal behavior for Destinations and other non-Experience public content.

Do not reopen accepted Experience publication/withdrawal behavior, the bilingual
parity requirement, public claims and media approval, or the selected Sanity
direction.

## Imported Locked Context

- Each public language must be complete, separately represented, human-approved,
  and meaning-equivalent before publication.
- An Experience already has an accepted type-specific publication gate and
  withdrawal recovery behavior.
- Public claims, prices, and media must satisfy their accepted approval and
  evidence boundaries.
- Sanity owns editable public and catalogue content; private request/customer data
  never enters Sanity.
- Exact Sanity fields and validation mechanics belong to Foundation Design after
  the product meaning is settled.

## Locked Decisions

### D-001 — Useful standalone Destinations may publish independently

A Destination may be published without a published Experience when it is a
useful standalone discovery page. Publication requires approved English and
Greek titles and summaries, useful orientation or detail content, applicable
claims and media approval, and clear paths to continue browsing or request a
consultation.

When a published Destination currently has no published Experiences, its page
omits the Experience section rather than showing empty catalogue scaffolding.
It must not imply that an Experience, supplier availability, reservation, or
confirmed booking exists.

This keeps the Destination and Experience publication lifecycles independent
and preserves destination-first inspiration. It does not weaken the accepted
rule that every published Experience requires a valid published Destination
relationship.

Requiring at least one published Experience was rejected because it would make
useful destination-first content dependent on a separate content lifecycle.
Allowing title-and-summary-only Destinations was rejected because those thin
pages would not fulfil the accepted discovery promise.

### D-002 — Relationship-aware withdrawal preserves truthful public journeys

When Greek Essence withdraws optional public content, it disappears from
navigation, listings, filters, and search. Its former URL shows a generic
bilingual recovery message with appropriate paths back to discovery or
consultation, without retaining stale claims, prices, or media.

Before withdrawing a Destination, every affected published Experience must
retain another genuinely valid and approved published Destination relationship
or also be withdrawn through the accepted Experience-withdrawal process. An
Experience must not be assigned an unrelated Destination merely to keep it
public.

Required service, request, privacy, or legal pages cannot disappear while their
dependent public journey remains active. The page must be replaced or
redirected, or the dependent journey must be disabled honestly.

This defines the visitor-visible behavior and relationship invariants that
Foundation Design must later enforce. It does not choose Sanity schemas,
validation, permissions, revalidation, redirects, or rendering mechanics.

Ordinary removal was rejected because it would provide poor recovery for old
links and leave relationship and required-journey consistency dependent on
manual memory. A public archive was rejected because it could continue exposing
outdated claims, expired media rights, or misleading service information.

## Open Questions

None. D-001 and D-002 form the complete Content Publication Truth decision set
and await combined acceptance.

## Acceptance Review

The operator must now review D-001 and D-002 together for internal consistency.
The acceptance question must name draft pull request #42 and the exact raw-ledger
path:

`docs/grilling/product-domain-truth/content-publication/GRILLING.md`

Acceptance does not authorize application implementation, dependency
installation, schema migration, or deployment.
