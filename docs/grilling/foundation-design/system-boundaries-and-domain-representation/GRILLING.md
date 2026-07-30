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

None yet.

## Open Questions

- D-001: Which system authoritatively verifies Booking Request eligibility, and
  what Experience information crosses the Sanity–Neon boundary at acceptance?
- Later: How should the three accepted submission journeys form one domain model
  without erasing their different meanings and fields?
- Later: What stable identities and relationship rules should Destinations and
  Experiences use across editorial revisions and withdrawal?
- Later: What exact bounded Experience snapshot should a Booking Request
  preserve?
- Later: How should contact relationships, corrections, and independently
  expiring records remain linked without reconstructing deleted data?
- Later: Which lifecycle invariants cross service boundaries, and which remain
  owned by one downstream platform track?

## Next Question

ID: D-001

Topic:
Authoritative Booking Request eligibility and the Sanity–Neon Experience
boundary.

Prompt:
When a visitor submits a Booking Request, which system should authoritatively
confirm that the selected Experience is still published and requestable, and
what should cross from editable Sanity content into the immutable Neon request
record?

Options:

1. (recommended): **Validate against live published Sanity content, then commit
   a stable Experience reference and bounded acceptance snapshot to Neon.** The
   Next.js server asks Sanity whether the Experience is currently published and
   explicitly requestable. Only then does it save the private Booking Request,
   the stable source identity, and the smallest customer-visible snapshot needed
   to preserve historical meaning. Exact snapshot fields remain a later
   decision. If current eligibility cannot be established, the request is not
   accepted.
2. **Maintain a synchronized Experience eligibility projection in Neon and
   validate against that copy.** Sanity remains the editorial source, but each
   publication or requestability change updates a small Neon catalogue registry.
   Booking Request acceptance reads the registry and stores a bounded snapshot.
   This reduces a live Sanity dependency during submission, but creates
   synchronization, stale-state, recovery, and monitoring work before any real
   enquiry can be accepted.
3. **Validate against live Sanity content and copy the complete public
   Experience record into Neon.** This keeps Sanity authoritative at submission
   and makes the accepted request independent afterward, but duplicates far more
   mutable catalogue content than staff need. It increases private-data backup,
   retention, migration, and stale-claim complexity without improving the
   visitor's request meaning.

Why this matters:

Giorgos or an authorized delegate may publish an Experience in Sanity and later
turn off its requestability or withdraw it. A visitor can still have an older
page open when they submit. The browser therefore cannot be trusted to tell the
server that the Experience is eligible. At the same time, an accepted Booking
Request in Neon must remain understandable after Sanity content changes or is
withdrawn; it cannot depend only on the current CMS document.

The decision establishes the first major service boundary: whether submission
requires a current authoritative Sanity read or a separately synchronized Neon
projection, and whether Neon stores only a bounded historical snapshot or a
full catalogue copy. It constrains later identifiers, schemas, failure behavior,
and integration contracts without choosing exact fields or implementation code.

After answer:

- Lock the authoritative eligibility and cross-service persistence boundary
  without choosing exact Sanity fields, Neon tables, or snapshot contents.
- Reconcile the remaining question order against that boundary.
- Store the next highest-value System Boundaries and Domain Representation
  question.
