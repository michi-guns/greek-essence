# Content Publication Truth Decisions

## Status and Authority

Accepted by the operator on 2026-07-30 after Product and Domain Truth grilling.

This document defines the minimum publishable completeness and withdrawal
behavior for Destinations and other non-Experience public content in the Greek
Essence Public Preview Release. It is Product and Domain Truth authority for
later canonical documentation and Foundation Design.

It does not authorize application implementation, dependency installation,
schema migration, deployment, or automatic commencement of Foundation Design.
Use the accepted project context in [`../../DECISIONS.md`](../../DECISIONS.md),
the actor responsibilities in
[`../../../PROJECT_ACTORS.md`](../../../PROJECT_ACTORS.md), and the accepted
Catalogue Discovery decisions in
[`../../catalogue-discovery/DECISIONS.md`](../../catalogue-discovery/DECISIONS.md).

## Imported Boundaries

- Each public language must be complete, separately represented,
  human-approved, and meaning-equivalent before publication.
- Public claims, prices, and media must satisfy their accepted approval and
  evidence boundaries.
- Every published Experience requires a valid published Destination
  relationship and retains its accepted type-specific publication and
  withdrawal behavior.
- Sanity owns editable public and catalogue content. Private customer and
  request data never enters Sanity.
- Greek Essence, acting through Giorgos or an authorized agency delegate,
  approves public business content. Dimitri's expected role as technical
  publisher does not make him responsible for approving agency facts, claims,
  prices, media rights, or other business meaning.

## D-001 — Useful Standalone Destinations May Publish Independently

A Destination may be published without a published Experience when it is a
useful standalone discovery page. Publication requires approved English and
Greek titles and summaries, useful orientation or detail content, applicable
claims and media approval, and clear paths to continue browsing or request a
consultation.

When a published Destination currently has no published Experiences, its page
omits the Experience section rather than showing empty catalogue scaffolding.
It must not imply that an Experience, supplier availability, reservation, or
confirmed booking exists.

This keeps Destination and Experience publication lifecycles independent and
preserves destination-first inspiration. It does not weaken the accepted rule
that every published Experience requires a valid published Destination
relationship.

Requiring at least one published Experience was rejected because it would make
useful destination-first content dependent on a separate content lifecycle.
Allowing title-and-summary-only Destinations was rejected because those thin
pages would not fulfil the accepted discovery promise.

## D-002 — Relationship-Aware Withdrawal Preserves Truthful Public Journeys

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

Ordinary removal was rejected because it would provide poor recovery for old
links and leave relationship and required-journey consistency dependent on
manual memory. A public archive was rejected because it could continue exposing
outdated claims, expired media rights, or misleading service information.

## Foundation Design Handoff

Foundation Design must preserve:

- the independent Destination and Experience publication lifecycles;
- the minimum useful bilingual Destination publication boundary;
- the requirement that every published Experience retains a valid published
  Destination relationship;
- removal of withdrawn optional content from public discovery;
- generic bilingual recovery at former URLs without stale public content;
- relationship-aware Destination withdrawal; and
- continuity between required public pages and their dependent journeys.

Exact Sanity document types, fields, references, validation, permissions,
preview, revisions, withdrawal mechanics, redirects, rendering, caching,
revalidation, and search-index updates remain Foundation Design decisions. This
document does not determine technical relationship cardinality beyond the
accepted publication and withdrawal invariants.

## Dependencies and External Validation

Before public release, Giorgos or an authorized agency delegate must approve the
actual bilingual Destination content, claims, prices where applicable, media
rights, and required legal or privacy wording. Launch Readiness must confirm the
responsible content approver, technical publisher, language reviewers,
production access, and publication handoff.

Editorial Content Platform Foundation Design must define enforceable publication
and withdrawal mechanisms without weakening these product rules. Catalogue
Discovery retains authority for Experience-specific publication, withdrawal,
requestability, and historical request meaning.

Qualified legal, privacy, or travel-industry review remains required where the
content or public journey creates an applicable professional-review dependency.
These validations may approve or correct actual public material; they must not
silently weaken the accepted completeness, truthful-withdrawal, relationship,
or bilingual-parity boundaries.
