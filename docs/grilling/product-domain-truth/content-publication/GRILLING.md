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

## Open Questions

- D-002: What happens when a Destination or other non-Experience public content
  is withdrawn?

## Next Question

ID: D-002

Layer:
Product and Domain Truth.

Topic:
Withdrawal behavior for Destinations and other non-Experience public content.

Prompt:
What should visitors see, and what should happen to related public content,
when Greek Essence withdraws a Destination or another non-Experience page?

Options:

1. (recommended): **Use relationship-aware withdrawal with a generic recovery
   path.** Withdrawn optional content disappears from navigation, listings, and
   search, and its former URL shows a generic localized message with relevant
   routes back to discovery or consultation instead of stale claims. Before a
   Destination is withdrawn, each affected published Experience must retain
   another valid published Destination relationship or be withdrawn through the
   already accepted Experience process. A required service, request, privacy, or
   legal page must be replaced, redirected, or have its dependent journey
   honestly disabled; it cannot simply disappear while that journey remains
   public.
2. **Treat every withdrawal as ordinary removal.** Remove the content from
   discovery and let its former URL use the normal not-found page, without
   relationship-specific recovery. This is simple, but bookmarked visitors lose
   useful guidance and linked Experiences or required journeys can become
   inconsistent unless handled separately.
3. **Keep withdrawn content publicly visible as an archive.** Remove it from
   normal discovery but retain the former page with an archived or unavailable
   label. This preserves context, but risks continuing to expose stale claims,
   media, contact details, or service information after approval has been
   withdrawn.

Why this matters:
The answer determines whether withdrawal can leave broken catalogue
relationships, dead-end visitor journeys, or stale public claims, and which
lifecycle and reference rules Foundation Design must preserve.

After answer:

- Lock the visitor-visible withdrawal rule and the treatment of related public
  content.
- Check D-001 and D-002 for internal consistency, then present the complete
  two-decision set for combined acceptance under the grilling protocol.
