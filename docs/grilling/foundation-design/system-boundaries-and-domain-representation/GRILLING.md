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

## Open Questions

- D-002: Which stable Experience identity should cross from Sanity into Neon and
  remain separate from editable URLs and titles?
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

ID: D-002

Topic:
Stable cross-service Experience identity.

Prompt:
Which immutable identifier should represent the same Experience across Sanity
and an accepted Neon Booking Request while titles, localized URLs, drafts, and
published content can change?

Options:

1. (recommended): **Use the immutable published Sanity document ID as the shared
   Experience identity.** Generate it once as an opaque, non-semantic value when
   the Experience is created. Sanity drafts and release versions resolve to that
   published root ID; Neon stores the same ID with the accepted snapshot. Titles,
   slugs, and localized URLs remain editable and never become identity. This uses
   Sanity's existing immutable identity without adding a second identifier.
2. **Add a separate immutable domain ID field shared by Sanity and Neon.** Sanity
   keeps its internal document ID, while a second opaque identifier represents
   the Experience across systems. This reduces coupling to Sanity identity and
   may simplify a future CMS migration, but creates another required unique value
   that every creation, import, duplication, and validation path must preserve.
3. **Use the public slug or URL key as the shared identity.** This is readable and
   initially simple, but a title correction, localization change, or URL rename
   can make the same Experience look like a new one or force historical records
   to follow mutable editorial naming. This is not recommended for immutable
   requests.

Why this matters:

Suppose an Experience begins as `/en/experiences/paros-sailing`, receives a
Booking Request, and is later renamed or given a corrected Greek URL. The
accepted request must still point to the same Experience without freezing its
old URL as identity. Sanity already assigns every document an immutable `_id`
and uses prefixes to associate drafts and versions with the published root ID.
The choice is whether that existing identity crosses the service boundary or
whether Greek Essence maintains a second domain identifier.

This decision constrains Sanity creation and duplication, Neon references,
snapshot provenance, imports, and later relationship contracts. It does not
choose public URL structure, exact schema fields, or snapshot contents.

After answer:

- Lock the stable cross-service Experience identity without choosing public URL
  structure, exact Sanity schemas, or Neon table layout.
- Reconcile the remaining question order against that boundary.
- Store the next highest-value System Boundaries and Domain Representation
  question.
