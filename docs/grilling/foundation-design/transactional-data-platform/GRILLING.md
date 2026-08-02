# Transactional Data Platform Grilling

## Status

Active Foundation Design grill. This ledger does not authorize application
implementation, dependency installation, Neon configuration, Drizzle schema
creation, migration execution, deployment, or production-data handling.

## Owning Layer and Purpose

Owner: Foundation Design — Transactional Data Platform.

Define the durable Neon PostgreSQL and Drizzle foundations for validating,
accepting, relating, auditing, delivering, retaining, deleting, migrating, and
recovering Greek Essence's private Consultation Requests, Booking Requests, and
General Contact messages. Preserve accepted Product and Domain Truth and the
accepted upstream Foundation Design decisions without reopening the selected
technology stack.

## Components and Responsibilities

- **Next.js server orchestration** receives a submission, validates its public
  intent, performs any required live Sanity eligibility check, and asks the
  transactional layer to accept one complete Request.
- **Neon PostgreSQL** is the durable authority for accepted private Requests,
  immutable journey details, correction context, delivery work and outcomes,
  protected audit history, retention deadlines, and deletion-safe recovery
  state.
- **Drizzle ORM** will define and access the PostgreSQL schema and provide
  reproducible migrations. The latest suitable release candidate is verified
  and pinned only when implementation is authorized.
- **Drizzle's first-party Zod integration with Zod v4** will derive validation
  where database schema meaning is sufficient. Handwritten Zod remains available
  for cross-field, journey, privacy, and external-authority rules that cannot be
  expressed truthfully by table shape alone.
- **Nodemailer and the agency mail service** act only after durable Request
  acceptance. Mail handoff, failure, retry, and recovery never redefine whether
  the Request was accepted.

## Accepted Inputs

- A valid Request is accepted only after its complete private transactional
  record is durably committed in Neon. A persistence failure is not acceptance.
- Consultation Request, Booking Request, and General Contact form one Request
  family with one shared envelope and exactly one immutable typed journey detail.
  A wide nullable table, generic catch-all payload, and three unrelated Request
  models are excluded.
- The shared envelope owns identity, request type, durable acceptance time,
  normalized-email relationship value, opaque reference, correction intent and
  prior reference where applicable, audit and delivery boundaries, and retention
  deadline.
- Each Request preserves the contact values and journey information submitted for
  that Request. Later submissions and corrections append; they never rewrite an
  earlier accepted Request.
- A Booking Request is accepted only after current Sanity eligibility is
  established. It stores the immutable published Experience ID and bounded
  localized customer-visible snapshot without copying the editable catalogue.
- Every explicit correction is a complete new Request. It stores its submitted
  earlier opaque reference without a foreign key or correction-link entity, and
  every Request expires independently.
- Exact technical retries resolve idempotently to the same accepted Request,
  reference, and intended initial email work. Similar visitor content is not
  automatically a duplicate.
- Normalized email supports private exact grouping and correction validation. It
  is not an account or verified identity, and no separate contact entity or
  permanent customer directory exists.
- Agency notification and visitor acknowledgement are independent delivery
  purposes. Their attempts and recovery outcomes are append-only and cannot
  revoke Request acceptance.
- Each Request and its protected audit and delivery history expires twelve months
  after its own acceptance. Off-provider encrypted backups expire no later than
  thirty days after creation and must not resurrect expired or verified-deleted
  Requests during restore.
- Routine agency work remains in the business inbox. Production database access
  is restricted technical access, not a staff dashboard or customer-management
  workflow.

## Locked Technical Direction

Do not reopen Neon PostgreSQL, Drizzle ORM, the latest suitable implementation-
time Drizzle release candidate, Drizzle's first-party Zod integration, or the
latest suitable Zod v4. Exact versions, providers, regions, credentials,
connection strings, schedules, and production access remain implementation or
Launch Readiness work.

## Explicit Boundaries

This track may define:

- physical Request, typed-detail, delivery, audit, idempotency, and bounded
  recovery schemas;
- database constraints, indexes, transactions, and concurrency invariants;
- Drizzle-derived versus handwritten Zod validation responsibilities;
- normalized-email, opaque-reference, correction-lookup, and exact-retry
  representation;
- immutable delivery and audit transition storage;
- twelve-month deletion, independent correction expiry, and deletion-manifest
  representation;
- migration compatibility and Neon connection-handling foundations; and
- the transactional representation required by backup and deletion-safe restore.

This track must not choose visitor-facing wording, add customer or staff
interfaces, invent agency workflow states, select production owners or
credentials, configure providers, implement Route Handlers, choose application
module boundaries, or execute migrations and deployment.

## Locked Decisions

### D-001 — Commit the Complete Acceptance Aggregate and Delivery Intents

Accepted on 2026-08-02. Greek Essence treats a submission as an accepted Request
only after one Neon transaction durably commits the complete acceptance
aggregate:

- the shared Request envelope and exactly one typed journey detail;
- the immutable submitted contact and privacy snapshot;
- the bounded Experience identity and customer-visible snapshot for a Booking
  Request;
- correction context when applicable;
- the bounded idempotency claim for the technical submission;
- the acceptance audit event; and
- one pending delivery record for each required purpose: agency notification and
  visitor acknowledgement.

The successful commit is the acceptance event. Actual mail-service network calls
start only afterward and remain outside the database transaction. A slow,
failed, or uncertain mail handoff therefore cannot hold open, roll back, or
redefine Request acceptance. If the server process stops immediately after the
commit, the database still proves acceptance and exposes both pending delivery
purposes for safe recovery without another Request or guessed reconstruction.

This decision carries forward the accepted requirement that the submission
handler waits for the required initial delivery work before returning the
visitor-visible outcome. Waiting for that post-commit work does not move mail
delivery inside the acceptance transaction or make delivery success an
acceptance condition.

Committing the Request first and creating audit and delivery records afterward
was rejected because a process failure could leave an accepted Request without
durable notification work and require a reconciliation mechanism. A generic
outbox followed by asynchronously derived delivery and audit projections was
rejected because it adds an event-processing boundary without proportional
Public Preview value.

Exact tables, columns, transaction APIs, retry timing, and mail scheduling remain
downstream schema, Application Architecture, Runtime Foundations, or bounded
technical-design responsibilities.

## Open Questions

- D-002: How should the shared Request envelope and exactly one typed journey
  detail be represented and constrained relationally?
- D-003: Which validation belongs to PostgreSQL and Drizzle-derived Zod, and which
  remains handwritten journey validation?
- D-004: How should opaque references, normalized email, and bounded idempotency
  identities be represented and indexed?
- D-005: How should explicit correction lookup preserve privacy and independent
  expiry without a foreign-key relationship?
- D-006: How should delivery work, attempts, uncertainty, escalation, and
  append-only audit transitions be represented safely under concurrency?
- D-007: How should twelve-month expiry, earlier verified deletion, cascading
  deletion, and minimum deletion-manifest state interact?
- D-008: What migration and Neon connection-handling contract should preserve
  safe deploys and transactions within the accepted free-quota boundary?
- D-009: What transactional backup and restore representation is required to
  reapply expiry and verified deletions without making backups an active history
  surface?

## Next Question

ID: D-002

Owning layer: Foundation Design.

Topic:
Relational Request envelope and typed-detail enforcement.

Prompt:
How should Neon and Drizzle represent one shared Request envelope with exactly
one correctly typed journey detail without introducing a wide nullable table or
generic payload?

Options:

1. (recommended): **Use one shared `requests` table and three one-to-one typed
   detail tables, with ordinary relational constraints and one trusted
   transactional writer.** Each detail row uses its Request ID as its primary and
   foreign key. A fixed detail type plus a composite foreign key to the Request's
   ID and discriminator prevents a Consultation detail from belonging to a
   Booking or Contact envelope. The acceptance transaction chooses the one typed
   table from the server-validated journey type and inserts exactly one detail.
   Focused integration tests verify that every accepted aggregate has one and
   only one matching detail.
2. **Use the same shared and typed tables, plus a custom deferred PostgreSQL
   constraint trigger that counts across all three detail tables at commit.**
   This makes the database reject a Request with zero, multiple, or mismatched
   typed details regardless of the writer. It provides stronger defence against
   arbitrary direct SQL, but adds custom trigger code, raw migration SQL, and
   more complex insert, deletion, and migration behavior for a system with one
   supported application writer and no routine database editing.
3. **Add an intermediate one-to-one `request_details` record before the three
   typed subtype tables.** The intermediate row guarantees one detail container
   per Request, while each subtype stores its journey fields. It adds another
   table and join but still needs application logic or a trigger to guarantee
   exactly one subtype, so it does not remove the central enforcement problem.

Why this matters:

The **envelope** contains facts common to every Request, such as identity,
reference, journey type, submitted contact snapshot, acceptance and expiry
times, correction intent, and normalized email. A **typed detail** contains only
the fields belonging to one journey: trip-planning information, one specific
Experience request, or a general message. Keeping those details in distinct
tables prevents a Booking Request from silently acquiring Consultation fields
and avoids dozens of irrelevant nullable columns.

For option 1, a Booking detail can carry a fixed `booking` discriminator and
reference only a `requests` row whose discriminator is also `booking`. The
database therefore rejects the wrong detail type and duplicate detail rows in
the same table. The D-001 acceptance transaction and its integration tests
enforce the remaining cross-table rule that exactly one of the three typed
tables receives a row.

PostgreSQL does not provide a simple ordinary foreign-key or check constraint
that counts children across three sibling tables. Enforcing that last rule
inside the database therefore requires custom trigger logic. The recommendation
avoids that machinery because Greek Essence has one supported server-side writer,
atomic acceptance, no routine direct database editing, and focused tests as a
practical enforcement boundary. The tradeoff is that arbitrary privileged SQL
could bypass the aggregate writer; such SQL is already outside normal agency and
application operation.

After answer:

- Lock the Request envelope, typed-detail table shape, and exact-one enforcement
  boundary.
- Preserve exact field names and journey columns for bounded schema design.
- Store D-003 as the next question.
