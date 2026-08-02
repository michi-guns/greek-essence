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

### D-002 — Shared Request Envelope with Three Typed Detail Tables

Accepted on 2026-08-02. Neon uses one shared Request table and three one-to-one
typed detail tables for Consultation Request, Booking Request, and General
Contact. Each detail row uses its Request ID as its primary and foreign key. A
fixed detail type and composite relationship to the Request ID and discriminator
prevent a detail from attaching to an envelope of the wrong journey type.

The one supported server-side acceptance writer derives the typed table from the
validated journey type and inserts exactly one matching detail within the D-001
transaction. Ordinary PostgreSQL primary-key, foreign-key, unique, check, and
composite constraints reject duplicate details in one typed table, orphaned
details, and envelope/detail type mismatch. Focused integration tests verify the
remaining aggregate invariant that every accepted Request has one and only one
row across the three sibling detail tables.

A custom deferred PostgreSQL trigger that counts across all typed tables was
rejected as disproportionate. It would protect against arbitrary privileged SQL
but add custom trigger and raw-migration behavior to a system with one supported
writer and no routine database editing. An intermediate generic detail-container
table was rejected because it adds a table and join without eliminating the need
for application logic or a trigger to guarantee one subtype.

This choice accepts the bounded tradeoff that arbitrary privileged SQL could
bypass the final cross-table invariant. Such writes are outside supported agency
and application operation; production database access remains restricted to
authorized technical recovery, security, or privacy work. Exact names and
journey columns remain bounded schema design.

## Open Questions

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

ID: D-003

Owning layer: Foundation Design.

Topic:
Database, generated-schema, and journey-validation responsibilities.

Prompt:
How should Greek Essence divide validation among PostgreSQL constraints,
Drizzle-generated Zod schemas, handwritten journey schemas, and server-side
authority checks?

Options:

1. (recommended): **Use four explicit validation layers with different
   responsibilities.** PostgreSQL constraints protect durable relational
   invariants. Drizzle-generated Zod insert and select schemas validate the
   internal persistence shape. Handwritten Zod schemas validate each public
   journey's untrusted form input and cross-field rules before mapping it to the
   internal aggregate. Server orchestration separately performs authority checks
   that schemas cannot prove, such as current Sanity requestability and private
   correction-reference matching.
2. **Use refined Drizzle-generated insert schemas directly as the public form and
   Route Handler schemas.** This minimizes repeated primitive field definitions,
   but couples the visitor contract to database columns, nullability, defaults,
   and migrations. Server-owned fields must continually be omitted, and a storage
   refactor could unintentionally change accepted form behavior.
3. **Use fully handwritten Zod schemas for both public input and internal
   persistence, with PostgreSQL constraints as the final guard.** This keeps
   visitor and storage contracts explicit, but duplicates the table shape in a
   second handwritten schema and underuses the selected first-party Drizzle–Zod
   integration.

Why this matters:

Validation answers different questions at different boundaries:

- **PostgreSQL** can guarantee durable facts such as non-null required columns,
  accepted enum or check values, unique opaque references and idempotency
  identities, valid foreign keys, and bounded numeric ranges. It cannot establish
  that a Sanity Experience is currently requestable.
- **Drizzle-generated Zod schemas** mirror the selected table shape at runtime.
  Current first-party Drizzle guidance supports generated select, insert, and
  update schemas and field refinement through `drizzle-orm/zod` with Zod v4.
- **Handwritten journey schemas** can express the visitor contract without
  exposing server-managed fields. For example, Booking Request validation can
  require one preferred date, allow either an alternative date or flexible-date
  indication, bound adult and child counts, and keep a short optional practical-
  needs field.
- **Server authority checks** query other trusted state. A browser-provided
  Experience ID may be structurally valid but is not eligible until the server
  verifies the current published Sanity record. A correction reference and email
  may be well formed but are accepted only after private Neon matching.

The recommendation intentionally repeats a small amount of primitive validation,
such as string lengths or email shape, at the public and persistence boundaries.
That duplication prevents a database migration from silently changing what the
public form accepts and keeps internal IDs, timestamps, normalized values, audit
states, and delivery fields outside visitor-controlled input.

First-party reference consulted for current capability, not exact implementation
authorization: <https://orm.drizzle.team/docs/zod>.

After answer:

- Lock validation ownership across the public, orchestration, persistence, and
  database boundaries.
- Preserve exact schema composition, error mapping, and field limits for bounded
  technical design and accepted journey contracts.
- Store D-004 as the next question.
