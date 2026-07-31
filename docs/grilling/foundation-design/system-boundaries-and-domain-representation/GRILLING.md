# System Boundaries and Domain Representation Grilling

## Status

Active Foundation Design interview. No decision is accepted until the operator
selects or formulates an option and that answer is persisted here.

This grill does not authorize application implementation, dependency
installation, schema migration, deployment, or production-data handling. Use
[`../../protocol.md`](../../protocol.md), the accepted
[classification](../../CLASSIFICATION.md), and the
[Foundation Design layer](../../layers/foundation-design.md).

## Owning Layer and Scope

Owning layer: **Foundation Design**.

This topic defines the durable system boundaries and conceptual domain
representation that the later Editorial Content Platform, Transactional Data
Platform, Application Architecture, and Runtime and Production Foundations
tracks must preserve. It owns:

- responsibility boundaries among Next.js, Sanity, Neon, and the mail service;
- launch entities and value objects;
- relationships and cardinalities;
- stable identities and cross-service references;
- lifecycle invariants; and
- immutable snapshots needed when editable source content later changes or is
  withdrawn.

It does not choose exact Sanity fields, Drizzle tables, indexes, migrations,
Route Handlers, deployment configuration, named production owners, or launch
evidence. Those belong to dependent Foundation Design tracks, bounded
implementation contracts, or Launch Readiness.

## Locked Inputs

The following accepted inputs are not reopened here:

- Next.js owns the public application and server-side orchestration.
- Sanity owns editable public and catalogue content, including Destinations and
  Experiences. Private customer or request data never enters Sanity.
- Neon PostgreSQL owns private customer, request, correction, delivery, and audit
  records.
- Drizzle, its first-party Zod integration, and Zod v4 are locked implementation
  inputs for the transactional boundary.
- Nodemailer uses the agency mail service for agency notifications and visitor
  acknowledgements; email outcomes never determine whether a request was
  accepted.
- Every accepted submission is durably saved before receipt is claimed and
  remains an immutable chronological record during its own retention period.
- Consultation Request, Booking Request, and General Contact remain distinct
  visitor journeys with their own accepted fields and wording; shared
  foundations must not collapse them into one generic form.
- Normalized submitted email groups an internal contact relationship without
  proving identity or exposing prior activity.
- A Booking Request preserves an authoritative Experience identifier and the
  smallest useful immutable historical snapshot; it must remain intelligible if
  the live Experience changes or is withdrawn.
- Destination and Experience publication lifecycles remain independent, while
  every published Experience requires at least one valid published Destination
  relationship.
- Customer accounts, public or routine staff request-history interfaces, a CRM,
  and website-owned staff workflow states remain deferred.

## Locked Decisions

### D-001 — Sanity Verifies Live Eligibility; Neon Preserves Accepted Meaning

Sanity remains authoritative for whether an Experience is currently published
and explicitly requestable. On every Booking Request submission, the Next.js
server checks the current published Sanity record rather than trusting the
browser's older page state. Only after eligibility is established does the
server commit the private Booking Request, a stable Experience reference, and a
bounded immutable acceptance snapshot to Neon.

After that commit, Neon is authoritative for what the visitor requested. Later
Sanity edits, disabled requestability, or withdrawal cannot rewrite, detach, or
delete the accepted record. The exact stable identifier and bounded snapshot
contents remain later decisions in this track.

Submission outcomes preserve distinct truths:

- a published but non-requestable Experience produces no accepted request and
  explains that this Experience is not currently accepting Booking Requests;
- a withdrawn or unpublished Experience produces no accepted request and
  explains that it is no longer listed without repeating stale claims;
- inability to reach Sanity or otherwise establish current eligibility produces
  a temporary verification failure, not a false withdrawal or accepted request;
  and
- the interface preserves entered information for a safe retry where feasible
  without claiming receipt.

The catalogue and Consultation Request journey are safe onward paths. Any public
email, telephone, WhatsApp, or other direct-contact fallback must be separately
approved and validated in Launch Readiness. It must be described as a separate
conversation, not as an accepted website Booking Request, because it bypasses
the structured request, privacy acknowledgement, opaque reference, duplicate
protection, and Neon acceptance boundary.

A synchronized Experience-eligibility projection in Neon was rejected for
launch because it adds stale-state, reconciliation, monitoring, and recovery
work before the market-validation release needs it. Copying the complete public
Experience into Neon was rejected because it duplicates mutable catalogue
content and expands retention, backup, migration, and stale-claim complexity
without improving historical request meaning.

### D-002 — Published Sanity Document ID Is the Shared Experience Identity

The immutable published Sanity document `_id` is the shared Experience identity
across Sanity and Neon. It is generated once as an opaque, non-semantic value
when the Experience is created. Draft and release-version prefixes resolve to
that published root ID before it crosses the service boundary.

Neon stores the published root ID with every accepted Booking Request snapshot.
Localized titles, slugs, and public URLs remain editable attributes and never
become identity. Renaming or translating an Experience therefore cannot detach
an accepted request or make the same Experience appear to be a new one.

A separate Greek Essence domain-ID field was rejected because it would add a
second required unique value that every creation, import, duplication, and
validation path must preserve without a current need to decouple from Sanity.
Slug or URL identity was rejected because editorial and localization changes
must not rewrite historical relationships.

### D-003 — Preserve a Bounded Customer-Visible Experience Snapshot

Every accepted Booking Request stores a bounded immutable request-context
snapshot alongside the published Sanity Experience ID. The snapshot preserves:

- the source Sanity revision;
- the visitor's locale;
- the localized title and summary shown in that locale;
- the Experience type;
- associated Destination labels;
- the public URL shown at acceptance; and
- when an indicative price was displayed, its complete accepted context: amount
  or “from” value, currency, charging basis, key inclusions, review date, and
  confirmation warning.

The snapshot excludes long detail copy, media, search metadata, other-language
variants, and unrelated editorial fields. It is part of the private accepted
request record, follows that request's twelve-month retention and deletion
boundary, and cannot be rewritten by later Sanity edits or withdrawal.

Identification-only storage was rejected because the immutable ID and title
would not preserve the proposition or indicative price the visitor saw. Copying
the complete published Experience was rejected because it would create an
unnecessary second catalogue in Neon and expand retention, backup, migration,
and stale-content handling.

### D-004 — Shared Request Envelope with One Typed Journey Detail

Consultation Requests, Booking Requests, and General Contact messages form one
conceptual Request family. Every accepted submission has one shared envelope
that owns its core identity, request type, durable acceptance time, contact
relationship, opaque reference, correction relationship where applicable,
audit and delivery boundaries, and retention deadline.

Each Request has exactly one immutable typed detail: Consultation Request,
Booking Request, or General Contact. The typed detail owns only that journey's
accepted fields and meaning. A Booking Request therefore cannot also carry
Consultation or General Contact detail, and shared processing cannot erase the
journeys' different validation and privacy boundaries.

An illustrative relational implementation is one common `requests` table plus
exactly one row in `consultation_request_details`, `booking_request_details`, or
`general_contact_details`. Delivery attempts and audit transitions may use
their own related tables. This example explains the domain boundary but does not
lock the later Transactional Data Platform track to exact table names, columns,
or physical layout.

One wide table containing every journey field with type-dependent nullable
columns is excluded. A generic catch-all payload is also excluded. Both would
make invalid field combinations easier and move important domain and privacy
rules out of the structural model. Three unrelated request models were rejected
because they would repeat shared acceptance, chronology, retention, audit, and
delivery invariants.

## Open Questions

- D-005: Should the normalized-email contact relationship be a separate retained
  entity or be derived only from retained immutable requests?
- Later: What relationship rules should Destinations and Experiences use across
  editorial revisions and withdrawal?
- Later: How should contact relationships, corrections, and independently
  expiring records remain linked without reconstructing deleted data?
- Later: Which lifecycle invariants cross service boundaries, and which remain
  owned by one downstream platform track?

## Next Question

ID: D-005

Topic:
Contact-relationship representation and expiry.

Prompt:
How should the normalized-email relationship that groups retained requests be
represented without creating an indefinite customer directory or weakening
correction validation?

Options:

1. (recommended): **Derive the relationship from normalized email stored on each
   retained Request; do not create a separate contact entity at launch.** Each
   immutable Request keeps both its submitted contact snapshot and the normalized
   email used for exact grouping and correction validation. An indexed lookup can
   find retained related requests. When requests expire independently, their
   values disappear with them; after the last one is deleted, no separate contact
   record remains.
2. **Create a separate contact entity with a generated ID and normalized email.**
   Requests point to that entity while preserving their own submitted snapshots.
   The contact record is deleted when no retained Request refers to it. This makes
   the relationship explicit and avoids repeating the normalized value, but adds
   creation, concurrency, orphan cleanup, and deletion rules for a relationship
   that has no launch account or staff interface.
3. **Keep a separate contact entity indefinitely as a customer directory.** This
   gives future enquiries a permanent relationship anchor, but silently creates
   the deferred customer-management system and retains personal data beyond the
   accepted request lifecycle. It conflicts with the launch boundary.

Why this matters:

Suppose one email address submits a Consultation Request in January and a Booking
Request in June. While both records remain, the system must recognize their
private relationship for integrity and correction checks without exposing it to
the visitor or routine agency staff. The January record still expires on its own
schedule; the June request must not extend it. After the final retained request
expires, keeping an otherwise empty contact record would preserve personal data
without an accepted launch purpose.

Technically, option 1 could use a normalized-email column and index on the common
`requests` table. Option 2 could use a `customer_contacts` table referenced by
`requests`. This decision chooses the domain representation and lifecycle, not
the exact column names, normalization algorithm, indexes, or deletion job.

After answer:

- Lock the contact-relationship representation and expiry boundary without
  choosing exact columns, indexes, normalization code, or deletion jobs.
- Reconcile the remaining question order against that boundary.
- Store the next highest-value System Boundaries and Domain Representation
  question.
