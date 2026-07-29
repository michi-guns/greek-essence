# Catalogue Discovery Decisions

## Status and Authority

Accepted by the operator on 2026-07-29 after feature grilling.

This document defines the Public Preview Release boundary for destination and
Experience discovery, requestable catalogue entries, launch Experience types,
search and filters, indicative pricing, availability language, publication
completeness, and withdrawn Experience behavior.

It does not authorize application implementation, dependency installation,
schema migration, deployment, or destructive path changes. Those require later
promoted canonical documentation and explicit bounded implementation contracts.

Use the terms in [GLOSSARY.md](GLOSSARY.md) and the project terms in
[../GLOSSARY.md](../GLOSSARY.md). The accepted project boundary remains in
[../DECISIONS.md](../DECISIONS.md).

## Catalogue Boundary

Visitors can browse published Destination and Experience lists and detail pages
in English and Greek. Catalogue discovery supports localized text search and a
small trustworthy filter set. A published Experience may be useful inspiration
without accepting a Booking Request.

Articles, Accommodation pages, and Attraction pages remain deferred unless
client validation proves a specific launch need. Live supplier availability,
confirmed online booking, and public claims derived from unapproved or
incomplete content remain outside this feature.

## D-001 — Requestability Is Controlled per Experience

An authorized editor explicitly marks each eligible published Experience as
requestable. Publishing does not automatically enable a Booking Request, and
Experience type does not determine eligibility.

A published Experience that is not requestable remains available for discovery
without a booking-request action. A requestable Experience shows a clearly
non-confirming action. Requestability means only that the agency is willing to
receive an expression of interest; it does not claim supplier availability,
create a reservation, or confirm a booking.

Dependencies:

- Content Operations must provide a clear per-Experience requestability control.
- The catalogue exposes a booking-request action only for a published,
  explicitly requestable Experience.
- The Booking Request feature must preserve the selected Experience and the
  non-confirming meaning through submission and acknowledgement.

## D-002 — Launch Experience Types

The launch catalogue supports exactly these Experience classifications:

- Tour
- Activity
- Travel package

Cruise and Transfer are deferred. Unsupported free-form type variants are not
part of the launch catalogue, and empty types must not be presented as populated
services.

This classification does not approve any particular Experience, package claim,
price, inclusion, supplier relationship, or availability statement. Before
public launch, the client must validate representative content for all three
types, approve the English and Greek public labels, and confirm that “Travel
package” accurately describes services Greek Essence offers. Appropriate
travel-industry or legal review remains required if that term creates regulated
consumer, pricing, inclusion, or agency-responsibility obligations.

## D-003 — Localized Search and Focused Filters

Launch search covers the published, localized titles and summaries of
Destinations and Experiences. Search operates within the visitor's selected
language and must not expose drafts or text from the other locale.

Experience results have two required filters:

- Destination
- Experience type: Tour, Activity, or Travel package

Every published Experience therefore requires a valid published Destination
relationship and one accepted launch type.

Interest is a conditional launch filter. It is included only if, before scope
freeze, the client approves a small bilingual Interest taxonomy and the launch
Experiences apply it consistently. Otherwise, Interest filtering is omitted.

Price, duration, and difficulty filters are deferred because their structured
data and consistent meanings have not been accepted for the preview release.

## D-004 — Conditional Indicative Prices and No Availability Claims

An Experience may show a client-approved indicative “from” price only when the
content maintains all of the following:

- currency;
- charging basis, such as per person or per group;
- key inclusions;
- review date; and
- an explicit warning that the price is subject to confirmation.

If those conditions are not met, the Experience shows no price and invites the
visitor to request current details. Stale or structurally incomplete prices are
omitted rather than displayed without their qualifications.

The catalogue never describes an Experience or requested date as available. It
explains that requested dates, final price, and applicable terms are checked
after enquiry. Requestability remains separate from availability.

The client owns price approval and review dates and must approve the precise
English and Greek charging-basis, inclusion, and confirmation wording. Taxes,
fees, exclusions, cancellation terms, and other legally material offer
information require client confirmation and appropriate professional review;
this decision does not invent or approve them.

## D-005 — Publication Gate and Withdrawn Experience Recovery

An Experience cannot be published until its required catalogue content is
complete and approved for both public languages. At minimum, publication
requires:

- usable localized titles, summaries, and detail content;
- one accepted Experience type;
- a valid published Destination relationship;
- approved public claims and media;
- an explicit requestability choice; and
- every D-004 qualification when an indicative price is shown.

Content Operations owns the exact validation and approval workflow without
weakening this catalogue boundary. Drafts, partial translations, and entries
with unresolved required relationships or approvals remain private.

When an Experience is unpublished, it disappears from catalogue listings,
search results, filters, and booking-request actions. Its former public URL shows
a generic localized message that the Experience is no longer listed, without
retaining stale detail claims, prices, or media. That page offers paths back to
the catalogue and to consultation without implying current supplier
availability. An unrelated unknown URL continues to use the normal not-found
behavior.

Already accepted Booking Request records remain available to the agency after
the referenced Experience changes or is unpublished. The Booking Request and
Request Processing features must define the immutable identifier and historical
snapshot needed for each record to remain intelligible; historical requests
must not depend solely on the current public CMS document.

## Explicit Exclusions and Deferrals

- Publishing does not automatically enable Booking Requests.
- Experience type does not determine requestability.
- Cruise and Transfer are not launch Experience types.
- Interest is not a launch commitment without the required client validation.
- Price, duration, and difficulty filters are deferred.
- Fixed current pricing and live availability claims are not supported.
- Incomplete, mixed-language, unapproved, or withdrawn detail content is not
  publicly discoverable.
- This feature does not define Booking Request form fields, submission
  processing, transactional snapshots, customer communications, or staff
  workflow; the later dependent feature grills own those decisions.

## Dependencies and Unresolved External Validations

- **Client:** approve representative Destinations and Experiences, the three
  type labels in English and Greek, the meaning of Travel package, public claims,
  media rights, price content, price-review ownership, and any Interest taxonomy.
- **Content Operations feature:** define roles, exact required fields,
  validation, bilingual approval, preview, publishing, unpublishing, revision,
  and recovery while preserving these gates.
- **Booking Request feature:** preserve Experience-specific, non-confirming
  intent and define behavior when an Experience changes or is withdrawn.
- **Request Processing and Communications feature:** define the immutable
  Experience identifier and historical snapshot stored with an accepted request.
- **Production Operations feature:** ensure public content freshness, monitoring,
  and recovery support the accepted catalogue behavior.
- **Qualified reviewers where applicable:** validate package, pricing, tax, fee,
  cancellation, consumer, and other legal or travel-industry claims.

These validations may refine approved content and operational ownership. They
must not silently expand the launch types, weaken the publication gate, imply
live availability, or turn a Booking Request into a reservation or confirmation.
