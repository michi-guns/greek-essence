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

## Open Questions

- D-004: How should the three accepted submission journeys form one domain model
  without erasing their different meanings and fields?
- Later: What relationship rules should Destinations and Experiences use across
  editorial revisions and withdrawal?
- Later: What exact bounded Experience snapshot should a Booking Request
  preserve?
- Later: How should contact relationships, corrections, and independently
  expiring records remain linked without reconstructing deleted data?
- Later: Which lifecycle invariants cross service boundaries, and which remain
  owned by one downstream platform track?

## Next Question

ID: D-004

Topic:
Shared request family and journey-specific meaning.

Prompt:
How should Consultation Requests, Booking Requests, and General Contact messages
share acceptance, references, contact grouping, audit, retention, and email
recovery while preserving their different business meanings and fields?

Options:

1. (recommended): **Use one shared Request envelope with exactly one typed,
   immutable journey detail.** Every accepted submission shares its core
   identity, acceptance time, contact relationship, opaque reference, audit and
   delivery boundaries, and retention rule. Its detail is exactly one
   Consultation Request, Booking Request, or General Contact snapshot with that
   journey's own required fields and meaning. Later tracks may choose the
   physical table layout but must preserve this domain split.
2. **Use three independent request entities that reuse shared processing
   services.** Each journey owns its complete identity and lifecycle model;
   common services implement contact matching, audit, retention, and email. This
   gives strong isolation, but repeats shared invariants and makes one contact's
   private cross-journey chronology and recovery behavior harder to keep
   consistent.
3. **Use one generic Request entity with a flexible journey payload.** A type
   label selects conditional validation over a flexible data object. This
   minimizes the initial domain model, but weakens structural guarantees, permits
   more invalid field combinations, and makes migrations and privacy review
   harder for real enquiries.

Why this matters:

A Consultation Request may contain timing and budget guidance. A Booking Request
contains dates, party composition, and the D-003 Experience snapshot. General
Contact contains a subject and message. After any one is accepted, however, it
uses the same kind of opaque reference, belongs to the appropriate email-based
contact relationship, records independent agency and visitor email outcomes,
and follows the same twelve-month rule.

This decision determines whether later domain contracts and transactional design
start from one typed request family or three unrelated records. It does not
choose exact Neon tables, Drizzle schemas, or application modules.

After answer:

- Lock the conceptual request-family boundary without choosing exact Neon tables,
  Drizzle schemas, or application modules.
- Reconcile the remaining question order against that boundary.
- Store the next highest-value System Boundaries and Domain Representation
  question.
