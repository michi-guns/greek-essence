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

None yet. Decision IDs begin at D-001.

## Open Questions

- D-001: When is a Destination useful and complete enough to publish, including
  when it has no published Experiences yet?
- D-002: What happens when a Destination or other non-Experience public content
  is withdrawn?

## Next Question

ID: D-001

Layer:
Product and Domain Truth.

Topic:
Destination publication completeness and its relationship to Experiences.

Prompt:
When should Greek Essence consider a Destination useful and complete enough to
publish, especially if it has no published Experiences yet?

Options:

1. (recommended): **A useful standalone Destination may publish without a
   published Experience.** It requires approved English and Greek title,
   summary, useful orientation/detail content, applicable claims/media approval,
   and clear browse/consultation paths. If it currently has no Experiences, the
   page omits an empty Experience section and makes no availability implication.
2. **Require at least one published Experience.** A Destination remains private
   until visitors can continue into an Experience. This prevents empty catalogue
   branches but blocks destination-first inspiration and ties Destination
   publication to another content lifecycle.
3. **Allow a minimal title-and-summary Destination.** The record may publish as
   soon as localized search text exists, even without useful detail or an
   Experience. This is fastest to populate but risks thin pages that do not
   fulfil the accepted discovery promise.

Why this matters:
The answer controls whether Destination and Experience publication lifecycles
are independent, what a visitor receives from destination-first discovery, and
which completeness and relationship rules Foundation Design must enforce.

After answer:

- Lock the Destination completeness and Experience-dependency rule.
- Preserve D-002 as the next unresolved product/domain gap.
