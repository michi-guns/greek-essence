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

## Open Questions

- D-003: Which bounded customer-visible Experience facts should be frozen with
  each accepted Booking Request?
- Later: How should the three accepted submission journeys form one domain model
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

ID: D-003

Topic:
Bounded historical Experience snapshot.

Prompt:
Which customer-visible Experience facts should Neon freeze with an accepted
Booking Request so the agency can understand what the visitor saw without
copying the complete mutable Sanity document?

Options:

1. (recommended): **Store a bounded request-context snapshot.** Preserve the
   published Sanity ID and source revision, visitor locale, localized title and
   summary, Experience type, associated Destination labels, and public URL shown
   at acceptance. If an indicative price was displayed, preserve its complete
   accepted price context: amount or “from” value, currency, charging basis, key
   inclusions, review date, and confirmation warning. Exclude long detail copy,
   media, search metadata, and other editorial fields.
2. **Store identification only.** Preserve the Sanity ID, visitor locale,
   localized title, Experience type, and Destination labels, but no summary,
   historical URL, revision, or displayed-price context. This minimizes Neon
   data, but after withdrawal or a material edit the agency may know which
   Experience was selected without knowing the proposition or indicative price
   the visitor actually saw.
3. **Store the complete published Experience document.** Preserve all localized
   text, price content, relationships, metadata, and media references as they
   existed at acceptance. This maximizes historical detail, but copies far more
   catalogue data than the manual enquiry workflow needs and expands retention,
   backup, migration, and stale-content handling.

Why this matters:

Suppose a visitor requests “Paros Sunset Sailing” after seeing an indicative
“from €120 per person” price. Six months later, the Experience is renamed, its
summary changes, and that price disappears. The immutable Sanity ID proves which
Experience was selected, but it does not by itself tell agency staff what
customer-visible proposition influenced the request.

The snapshot should preserve enough context for honest follow-up and historical
intelligibility while remaining smaller than a second catalogue. This decision
sets that information boundary; the Transactional Data Platform track will later
choose exact columns, value-object representation, and constraints.

After answer:

- Lock the bounded Experience snapshot contents without choosing exact Neon
  columns or Drizzle schema layout.
- Reconcile the remaining question order against that boundary.
- Store the next highest-value System Boundaries and Domain Representation
  question.
