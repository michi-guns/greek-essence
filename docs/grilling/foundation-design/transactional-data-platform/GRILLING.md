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

### D-004 — Separate Purpose-Specific Identities and Compare Exact Retries Directly

Accepted on 2026-08-02. Greek Essence keeps four purpose-specific values rather
than making one identifier carry unrelated meaning:

- a random internal Request ID relates protected database rows and is never
  public;
- a separate high-entropy, human-safe opaque reference is uniquely indexed,
  shown to the visitor, included in Request emails, and grants no history access
  by itself;
- each immutable Request preserves the submitted email and a separately indexed
  normalized email for private grouping and correction validation; and
- a separate random idempotency token identifies one intentional submission,
  persists through its exact technical retries, and is uniquely bound to the
  accepted Request for that Request's retention period through a one-way stored
  representation.

Email normalization trims surrounding whitespace and canonicalizes the domain
while preserving the local part. It does not apply provider-specific dot
removal, plus-address stripping, approximate matching, or another transformation
that could merge distinct mailboxes. A later intentional Request receives a new
idempotency token; the token is not a person, account, public reference, or
content-similarity fingerprint.

When an existing idempotency token is encountered, the server compares the new
canonical validated visitor-controlled fields directly with the retained
immutable Request. An exact match resolves to the same Request and public
reference without another Request or intentional email dispatch. Materially
different input produces one generic conflict and neither rewrites the original
nor creates a new Request under that token.

A separate payload digest is not stored. The Request is already loaded to return
its reference, its payload is small, and direct comparison avoids an additional
canonical serialization and secret lifecycle. A fast unkeyed digest was rejected
because visitor content includes personal and potentially sensitive data and the
digest would add no necessary lookup capability. If later measured behavior
demonstrates a real need, a private server-computed keyed digest would require a
separate technical and security decision and must never become general log data.

Reusing one random value as the database ID, public reference, and idempotency
identity was rejected because it couples public, relational, and retry
lifecycles. Content- or time-derived duplicate identity was rejected because
similar intentional Requests are not technical retries. Exact random algorithms,
human-safe alphabets, lengths, hashing, token issuance and rotation, canonical
field comparison, and index names remain bounded technical design.

### D-005 — Simple Private Correction Check Without a Lock or Foreign Key

Accepted on 2026-08-02. Immediately before correction acceptance, the server
performs one indexed private check using the submitted earlier public reference
and normalized submitted email and requires the earlier Request to be retained
at check time. Every failed check returns the same generic result whether the
reference is unknown, expired, deleted, or belongs to another email. Public
behavior never reveals which value matched or whether prior activity exists.

On a match, the D-001 transaction stores a complete independent correction with
its correction intent and submitted earlier reference. It stores no internal
target ID, foreign key, copied earlier content, or relationship entity. While the
earlier Request remains retained, authorized processing may resolve the prior
reference. After deletion, the correction remains understandable from its own
snapshot and reports only that the target is no longer retained; deletion does
not mutate it or extend either Request's retention.

The check uses no row lock. A theoretical deletion immediately after validation
has no material Public Preview consequence because the correction is already a
complete independent Request and no customer-visible history, booking promise,
or mutable staff workflow depends on the live relationship. Lock orchestration
was rejected as disproportionate for this low-volume small-agency release. A
nullable foreign key was rejected because deletion would mutate the later
correction and recreate the relationship lifecycle excluded upstream.

Exact query composition and generic bilingual error copy remain bounded
technical and content design.

### D-006 — Current Delivery Summary With Append-Only Attempts and Audit

Accepted on 2026-08-02. Each accepted Request owns exactly two small current
delivery rows created atomically by D-001: one agency-notification purpose and
one visitor-acknowledgement purpose. A unique Request-and-purpose constraint
prevents a second current row for the same intentional delivery.

The current row contains only the minimum recoverable summary required to find
work and communicate truth, including whether the purpose is pending,
attempting, confirmed handed off, definitely failed, uncertain, or escalated,
plus bounded scheduling and attempt metadata. It is not a general queue, staff
case state, or proof that a recipient received or read an email.

Every actual mail call receives an append-only attempt row. A guarded database
change claims an eligible purpose and records that the attempt started before
the network call, protecting the realistic overlap between initial delivery and
recovery. The known result then appends its outcome and updates the current
summary together. If processing stops after the attempt starts but before the
result is known, the unresolved attempt is uncertain and is not blindly retried.

Acceptance, delivery transitions, recovery, escalation, and authorized manual
actions append the audit evidence required upstream. The current summary may
advance, but later success does not erase an earlier failure or uncertainty.
Delivery diagnostics retain only minimum provider and failure context and never
Request bodies, notes, messages, or full email addresses.

An append-only-only event model was rejected because it would require event
folding or projections for ordinary recovery queries. A mutable latest-status
row without attempt history was rejected because it would erase investigation
evidence. Exact state names, conditional SQL, retry count and timing, scheduler,
escalation route, and named owner remain bounded technical design, Runtime
Foundations, or Launch Readiness work.

## Open Questions

- D-007: How should twelve-month expiry, earlier verified deletion, cascading
  deletion, and minimum deletion-manifest state interact?
- D-008: What migration and Neon connection-handling contract should preserve
  safe deploys and transactions within the accepted free-quota boundary?
- D-009: What transactional backup and restore representation is required to
  reapply expiry and verified deletions without making backups an active history
  surface?

## Next Question

ID: D-007

Owning layer: Foundation Design.

Topic:
Hard deletion of expired or verified Request aggregates.

Prompt:
How should the platform remove a complete Request aggregate at twelve-month
expiry or after an authorized earlier-deletion decision without retaining a live
tombstone or risking partial deletion?

Options:

1. (recommended): **Hard-delete the Request root and let database cascades remove
   its owned aggregate in one transaction.** Store `expires_at` on the Request;
   run one simple scheduled deletion query in small batches; and use the same
   aggregate-deletion operation after an authorized earlier-deletion decision.
   Keep no tombstone in the live Request tables.
2. **Soft-delete or anonymize the Request and retain its relationships and audit
   rows.** This makes accidental restoration less likely and preserves counts,
   but retains a private record beyond the accepted deletion event and requires
   difficult proof that every personal field was irreversibly anonymized.
3. **Delete each owned table explicitly in application code.** This avoids
   database cascades, but duplicates aggregate ownership in deletion code and
   creates more opportunities for a newly added child table or interrupted
   operation to leave private remnants.

Why this matters:

The Request root owns its typed details, immutable contact and privacy snapshot,
idempotency identity, current delivery rows, delivery attempts, and audit events.
Database-owned cascade rules make removal all-or-nothing and automatically cover
those declared relationships. A correction's submitted earlier reference is
plain snapshot data rather than a relationship, so deleting the earlier Request
does not delete or mutate the later correction.

A daily scheduled cleanup is sufficient for a small-agency Public Preview;
sub-minute deletion timing and a separate deletion platform are unnecessary.
Each run can delete a modest batch of rows whose `expires_at` has passed and
repeat until none remain. Earlier verified deletion uses the same operation after
the separate authorization and identity-verification contract is satisfied.

Deletion removes any pending delivery work owned by the Request. A mail handoff
already confirmed before deletion cannot be recalled from an external mail
service or recipient mailbox. D-009 separately decides the minimum backup-restore
representation needed to prevent a restore from reviving data that should remain
deleted; D-007 does not add that machinery pre-emptively.

After answer:

- Lock aggregate hard deletion, cascade ownership, and proportional scheduling.
- Preserve exact batch size, schedule, earlier-deletion authorization, and
  backup-restore behavior for downstream decisions and owners.
- Store D-008 as the next question.
