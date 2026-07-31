# System Boundaries and Domain Representation Decisions

Accepted by the operator on 2026-07-31 after Foundation Design grilling.

This document defines the Public Preview Release boundary among Sanity, Next.js,
Neon PostgreSQL, and the agency mail service; the conceptual representation of
catalogue and request data; the stable identities and relationships that cross
those boundaries; and the immutable history required when editable catalogue
content changes or disappears.

It does not authorize application implementation, dependency installation,
schema migration, deployment, or production-data handling. Exact Sanity fields,
Drizzle tables, indexes, migrations, Route Handlers, runtime configuration,
named production owners, and launch evidence remain downstream work.

## Accepted Context

- Next.js owns the public application and server-side orchestration.
- Sanity owns editable public and catalogue content, including Destinations and
  Experiences. Private customer and request data never enters Sanity.
- Neon owns private Request, correction, delivery, and audit records.
- Nodemailer uses the agency mail service for agency notifications and visitor
  acknowledgements. Email delivery never determines whether a Request was
  accepted.
- Consultation Request, Booking Request, and General Contact remain distinct
  visitor journeys with their own fields and meaning.
- Every accepted Request is durably saved before receipt is claimed, remains
  immutable during its own retention period, and expires independently under the
  accepted twelve-month rule.
- Corresponding agency notification and follow-up email copies follow the same
  twelve-month deletion rule in the agency inbox.
- Customer accounts, a CRM, public or routine staff request-history interfaces,
  and website-owned staff workflow states remain deferred.

## D-001 — Sanity Verifies Live Eligibility; Neon Preserves Accepted Meaning

Sanity is authoritative for whether an Experience is currently published and
explicitly requestable. On every Booking Request submission, the Next.js server
checks the current published Sanity record rather than trusting the browser's
older page state. Only after eligibility is established may the server commit the
private Booking Request, stable Experience identity, and bounded immutable
acceptance snapshot to Neon.

After that commit, Neon is authoritative for what the visitor requested. Later
Sanity edits, disabled requestability, or withdrawal cannot rewrite, detach, or
delete the accepted record. The system does not maintain a synchronized
Experience-eligibility projection or a complete duplicate catalogue in Neon.

Submission outcomes preserve distinct truths:

- a published but non-requestable Experience produces no accepted Request and is
  explained as not currently accepting Booking Requests;
- a withdrawn or unpublished Experience produces no accepted Request and is
  explained as no longer listed without repeating stale claims;
- inability to reach Sanity or otherwise establish current eligibility produces
  a temporary verification failure, not false withdrawal or acceptance; and
- entered information is preserved for safe retry where feasible without
  claiming receipt.

The catalogue and Consultation Request journey are safe onward paths. Any public
email, telephone, WhatsApp, or other direct-contact fallback requires separate
Launch Readiness approval. It must be described as a separate conversation, not
an accepted website Booking Request, because it bypasses structured submission,
privacy acknowledgement, opaque-reference, duplicate-protection, and durable
acceptance safeguards.

## D-002 — Published Sanity Document ID Is the Shared Experience Identity

The immutable published Sanity document `_id` is the shared Experience identity
across Sanity and Neon. It is generated once as an opaque, non-semantic value
when the Experience is created. Draft and release-version identifiers resolve to
that published root ID before crossing the service boundary.

Neon stores the published root ID with every accepted Booking Request snapshot.
Localized titles, slugs, and public URLs remain editable attributes and never
become identity. A separate Greek Essence domain-ID field is unnecessary at
launch, and slugs or URLs must not identify immutable request relationships.

## D-003 — Preserve a Bounded Customer-Visible Experience Snapshot

Every accepted Booking Request stores a bounded immutable request-context
snapshot alongside the published Sanity Experience ID. The snapshot preserves:

- the source Sanity revision;
- the visitor's locale;
- the localized title and summary shown in that locale;
- the Experience type;
- associated Destination labels;
- the public URL shown at acceptance; and
- when an indicative price was displayed, its amount or “from” value, currency,
  charging basis, key inclusions, review date, and confirmation warning.

The snapshot excludes long detail copy, media, search metadata, other-language
variants, and unrelated editorial fields. It belongs to the private Request,
follows that Request's retention and deletion boundary, and cannot be rewritten
by later Sanity changes.

Identification-only storage is insufficient because it would not preserve the
customer-visible proposition or indicative price. Copying the complete
Experience is excluded because it would create a second catalogue and expand
retention, backup, migration, and stale-content responsibilities.

## D-004 — Shared Request Envelope with One Typed Journey Detail

Consultation Requests, Booking Requests, and General Contact messages form one
conceptual Request family. Every accepted submission has one shared envelope
that owns its identity, request type, durable acceptance time, normalized-email
relationship value, opaque reference, correction intent and prior reference when
applicable, audit and delivery boundaries, and retention deadline.

Each Request has exactly one immutable typed detail: Consultation Request,
Booking Request, or General Contact. The detail owns only that journey's accepted
fields and meaning. Shared processing must not erase the journeys' different
validation and privacy boundaries.

A representative relational mapping is one common `requests` table plus exactly
one typed detail in `consultation_request_details`,
`booking_request_details`, or `general_contact_details`; delivery attempts and
audit transitions may be related records. Exact physical layout remains a
Transactional Data Platform decision.

One wide table containing every journey field with type-dependent nullable
columns is excluded. A generic catch-all payload is also excluded. Three
unrelated Request models are excluded because they would repeat shared
acceptance, chronology, retention, audit, and delivery invariants.

## D-005 — Derive Contact Relationships from Retained Requests

The private customer-contact relationship is derived from the normalized email
stored on each retained immutable Request. Greek Essence does not create a
separate contact entity or permanent customer directory at launch.

Each Request preserves both the contact values submitted with that Request and
the normalized email used for exact grouping and correction validation. While
related Requests remain within retention, authorized processing can group them
by the stored normalized value. Each Request expires independently; deleting a
Request removes its normalized value from the active transactional record. After
the final related Request is deleted, no derived contact relationship or separate
customer record remains in the active transactional model. Separately governed
inbox copies, protected backup expiry, and any minimal deletion-safe restore
manifest retain their already accepted lifecycles and do not become customer
records.

Email grouping is not an account, login, verified person identity, or proof that
all grouped Requests came from one person. Shared, reassigned, mistyped, and
changed addresses must not create unsupported identity claims. Names, telephone
numbers, approximate matching, and provider-specific mailbox transformations
must not merge relationships automatically.

A representative implementation is a normalized-email value and index on the
common Request record. Exact normalization, columns, indexes, and query contracts
remain Transactional Data Platform decisions.

## D-006 — Destination Relationships Are Equal

An Experience has one or more equally valid published Destination relationships.
There is no required primary Destination and no role taxonomy such as starts in,
visits, or ends in. The Experience appears in discovery for every related
Destination and remains publishable while at least one genuinely valid published
Destination relationship remains.

The Experience's canonical identity and public URL do not depend on a single
Destination. Before a Destination is withdrawn, every affected published
Experience must remove that relationship and retain another genuinely valid and
approved published Destination relationship, or the Experience must also be
withdrawn under the accepted publication process. Withdrawal does not
automatically assign another Destination or rewrite an Experience relationship.

A representative Sanity mapping is an array of Destination references on the
Experience. Exact fields, validation, and queries remain Editorial Content
Platform decisions. A primary relationship is excluded because a
multi-destination Experience may have no truthful main place. Role-labelled
relationships are excluded because they would introduce an unapproved bilingual
itinerary taxonomy and validation burden.

## D-007 — Reference-Only Correction Relationship

An explicit correction is a complete new immutable Request. Before accepting it,
the server privately confirms that the supplied earlier opaque reference exists
among retained Requests and that its normalized email matches the correction's
normalized submitted email. Failure returns one generic result that does not
reveal whether the reference or email exists.

The correction stores its `correction` intent and submitted earlier opaque
reference, but no internal foreign key or separate correction-link entity. The
reference is the durable logical relationship. While the earlier Request exists,
authorized technical processing can derive that state by reference lookup. After
the earlier Request expires independently, the reference no longer resolves; no
deletion-time relationship update, reconstruction, or retained target content is
required. The correction's complete snapshot remains independently understandable
until its own expiry.

Agency and visitor emails clearly identify the submission as a correction and
include the submitted earlier reference. Routine staff context remains in the
agency inbox through ordinary search or threading. Every agency notification
also includes the current opaque Request reference and submitted reply email;
corrections additionally include the earlier submitted reference. Notifications
do not automatically repeat or summarize prior Request content.

Neon remains authoritative for acceptance when either agency or visitor email
fails. Delivery purposes retain independent append-only audit histories.
Definitely failed delivery receives bounded safe retry; uncertain mail-service
handoff stops blind redispatch; and exhausted or uncertain delivery uses the
accepted separately monitored escalation boundary. Retry counts, timing,
scheduling, provider mechanics, and named recovery ownership remain downstream
Foundation Design or Launch Readiness work.

A representative Request mapping uses an intent and optional prior opaque
reference beside the complete typed snapshot. Exact lookup constraints,
normalization, columns, and indexes remain Transactional Data Platform decisions.
A foreign key with target-expiry mutation, separate correction-link entity, and
retention extension of earlier Requests are excluded.

## Cross-Service Lifecycle Invariants

- Sanity changes or withdrawal never cascade into accepted Neon records.
- Neon Request expiry never mutates Sanity catalogue content.
- The server must establish live Experience eligibility before accepting a
  Booking Request; source unavailability fails safely without acceptance.
- The Experience ID and bounded snapshot are the only accepted catalogue-to-
  transaction historical boundary defined by this track.
- Mail is a downstream operational surface. Delivery success, failure, or
  uncertainty never changes durable Request acceptance.
- Every private Request, correction, delivery history, and audit history follows
  its accepted retention boundary without being extended by a related record.
- Routine agency personnel use authorized business-inbox copies rather than the
  production database. Production database access is restricted to named
  technical roles for authorized recovery, security, or privacy work; exact
  people, permissions, and evidence remain Launch Readiness responsibilities.

## Explicit Exclusions

The Public Preview does not include:

- a synchronized Sanity eligibility projection or full catalogue copy in Neon;
- mutable slug or URL identity;
- a wide nullable or generic Request model;
- a separate contact entity, permanent customer directory, CRM, or customer
  account;
- public or routine staff Request-history browsing;
- automatic or manual cross-email identity merging;
- primary or role-labelled Destination relationships;
- a correction-chain entity, foreign-key lifecycle, or retention extension; or
- website-owned staff lifecycle states such as in progress, resolved, or closed.

## Downstream Dependencies

### Editorial Content Platform

Define the exact Sanity Destination and Experience documents, references,
English/Greek representation, root-ID handling, revision capture, publication and
requestability validation, preview, withdrawal, rendering, caching, revalidation,
search, and freshness behavior.

### Transactional Data Platform

Define the exact Neon and Drizzle schemas, typed-detail constraints, normalized
email implementation, opaque-reference lookup, correction validation,
transactions, idempotency, audit, delivery state, independent retention and
deletion, indexes, migrations, and backup representation.

### Application Architecture

Define the Next.js server-only orchestration and module boundaries that read
Sanity, validate eligibility, persist Neon records, distinguish truthful failure
states, and dispatch mail only after durable acceptance. It must preserve the
exact bounded context rendered to the visitor without allowing browser-supplied
fields to assert current eligibility; the render-time snapshot provenance and
the submission-time live Sanity eligibility check are distinct responsibilities.

### Runtime and Production Foundations

Define mail retry and recovery, observability without request-body leakage,
provider failure behavior, secrets, deployment and migration ordering, backup and
restore behavior, and deletion-safe operations.

### Launch Readiness

Approve any direct email, telephone, WhatsApp, or other fallback channel and its
truthful wording. Name and evidence production owners, mail recipients, recovery
routes, retention and inbox-deletion practice, provider configuration, privacy
explanation, and other launch validations. Qualified privacy or legal review
remains appropriate where required.

## Material Risks to Preserve

- Sanity unavailability intentionally blocks new Booking Request acceptance
  because current eligibility cannot be established.
- Email grouping is deliberately weak identity evidence and must remain private.
- The agency inbox is the only routine staff context surface; its availability,
  retention, and recovery practice are therefore launch dependencies.
- Accepted Booking Request meaning depends on complete, consistent snapshot
  capture at acceptance.
- Live eligibility and historical display context may come from different Sanity
  revisions when a visitor submits an older open page. Downstream design must
  verify current eligibility while preserving trustworthy render-time context
  rather than silently replacing it with newer content or trusting editable
  browser fields.
- Later customer accounts, CRM capabilities, Destination roles, or staff history
  would require new decisions rather than reinterpretation of these launch
  foundations.
