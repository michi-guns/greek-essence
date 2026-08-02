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

### D-003 — Layer Public, Authority, Persistence, and Database Validation

Accepted on 2026-08-02. Greek Essence uses four explicit validation layers with
different responsibilities:

1. Handwritten Zod journey schemas validate untrusted public Consultation,
   Booking, and Contact form input, including accepted cross-field rules and
   data-minimization boundaries.
2. Server orchestration performs authority checks that schema shape cannot
   prove, including current published Sanity requestability and private
   correction-reference and normalized-email matching.
3. Drizzle-generated Zod insert and select schemas validate internal persistence
   shapes derived from the Drizzle table definitions.
4. PostgreSQL constraints provide the final durable guard for relational and
   storage invariants such as required columns, accepted values, uniqueness,
   foreign keys, and bounded numeric values.

Public schemas do not expose internal IDs, timestamps, normalized values,
idempotency records, audit states, delivery fields, or other server-managed
columns. The public and persistence boundaries may intentionally repeat a small
amount of primitive validation, such as string length or email shape, so a
storage migration cannot silently alter accepted visitor behavior.

Using refined Drizzle-generated insert schemas directly as public form and Route
Handler contracts was rejected because it would couple visitor input to database
columns, defaults, and migrations and require continual omission of server-owned
fields. Fully handwritten public and persistence schemas were rejected because
they would duplicate the complete table shape and underuse the selected
first-party Drizzle–Zod integration.

Exact schema composition, error localization, field limits, coercion, and
mapping functions remain bounded technical design and must preserve the accepted
journey contracts. First-party capability reference:
<https://orm.drizzle.team/docs/zod>.

## Open Questions

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

ID: D-004

Owning layer: Foundation Design.

Topic:
Purpose-specific Request, reference, contact, and retry identities.

Prompt:
How should Greek Essence represent and index internal Request identity, the
visitor-visible opaque reference, normalized email grouping, and the bounded
idempotency identity without merging their different responsibilities?

Options:

1. (recommended): **Use separate purpose-specific values and indexes.** Give each
   Request an internal random database ID that is never public; generate a
   separate high-entropy, human-safe public reference with a unique index; store
   the submitted email snapshot plus a separately indexed normalized value; and
   use a different random idempotency token for one intentional submission,
   retained through its exact technical retries and bound uniquely to the
   accepted Request.
2. **Reuse one random value as the database ID, public reference, and idempotency
   identity.** This reduces columns and generation steps, but exposes the
   internal relationship key publicly, makes a pre-acceptance retry key become a
   permanent customer reference, and couples unrelated lookup, presentation, and
   duplicate-protection lifecycles.
3. **Derive duplicate identity from normalized email, submitted content, and a
   time window.** This needs no explicit retry token, but similar intentional
   Requests could be misclassified as technical duplicates. It also creates
   personal-data-derived fingerprints and contradicts the accepted rule that
   content similarity and close timing do not prove duplication.

Why this matters:

These values answer different questions:

- The **internal Request ID** relates protected database rows efficiently. It is
  not shown to visitors and does not need to be comfortable to type.
- The **opaque public reference** is copied into the success page and emails and
  may later be typed with a correction. It contains no personal information or
  sequential private-record detail and grants no history access by itself.
- The **normalized email** groups retained Requests and privately checks a
  correction. Greek Essence keeps the original submitted email in each immutable
  snapshot. Normalization trims surrounding whitespace and canonicalizes the
  domain while preserving the local part; it does not apply provider-specific
  Gmail-style dot removal, plus-address stripping, or approximate matching that
  could merge distinct mailboxes.
- The **idempotency token** identifies one intentional submission transport, not
  a person or similar content. It is random, non-sensitive, preserved across
  technical retries, and replaced for a later intentional Request. The database
  stores a one-way representation with a unique index and binds it to the
  accepted Request for that Request's retention period. Reuse with materially
  different input is a generic conflict rather than a new or silently rewritten
  Request.

The recommendation uses a few small indexed values to keep public references,
private relationships, and duplicate protection from silently inheriting one
another's meaning. Exact random algorithms, alphabets, lengths, token issuance,
hashing, and index names remain bounded technical design and security review.

After answer:

- Lock the separation, normalization boundary, idempotency conflict behavior, and
  indexing responsibilities of the four identity values.
- Preserve exact generation, hashing, and token-rotation mechanics for bounded
  technical design.
- Store D-005 as the next question.
