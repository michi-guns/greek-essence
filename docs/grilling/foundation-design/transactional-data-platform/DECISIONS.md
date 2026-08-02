# Transactional Data Platform Decisions

Accepted by the operator on 2026-08-02 after Foundation Design grilling.

This document defines the durable Neon PostgreSQL and Drizzle foundations for
validating, accepting, relating, auditing, delivering, retaining, deleting,
migrating, and recovering Greek Essence's private Consultation Requests,
Booking Requests, and General Contact messages.

It does not authorize application implementation, dependency installation,
Neon or mail-provider configuration, schema creation, migration execution,
deployment, production-data access, or commencement of Application Architecture,
Runtime and Production Foundations, Launch Readiness, or another work unit.
Exact package versions, table and column names, provider accounts, regions,
credentials, schedules, named owners, monitoring, and launch evidence remain
downstream work.

## Accepted Context

- Next.js server orchestration receives a submission, validates its public
  intent, performs any required live Sanity eligibility check, and asks the
  transactional layer to accept one complete Request.
- Neon PostgreSQL is the durable authority for accepted private Requests,
  immutable journey details, correction context, delivery work and outcomes,
  protected audit history, retention deadlines, and deletion-safe recovery
  state.
- Drizzle ORM defines and accesses the PostgreSQL schema and provides
  reproducible migrations. The latest suitable release candidate is verified
  and pinned only when implementation is authorized.
- Drizzle's first-party Zod integration with Zod v4 derives validation where
  database schema meaning is sufficient. Handwritten Zod remains responsible
  for cross-field, journey, privacy, and external-authority rules that table
  shape cannot express truthfully.
- Nodemailer and the agency mail service act only after durable Request
  acceptance. Mail handoff, failure, retry, and recovery never redefine whether
  the Request was accepted.
- Consultation Request, Booking Request, and General Contact form one Request
  family with one shared envelope and exactly one immutable typed journey
  detail. A wide nullable table, generic catch-all payload, and three unrelated
  Request models are excluded.
- The shared envelope owns identity, Request type, durable acceptance time,
  normalized-email relationship value, opaque reference, correction intent and
  prior reference where applicable, audit and delivery boundaries, and
  retention deadline.
- Each Request preserves the submitted contact values and journey information.
  Later submissions and corrections append; they never rewrite an earlier
  accepted Request.
- A Booking Request is accepted only after current Sanity eligibility is
  established. It stores the immutable published Experience ID and bounded
  localized customer-visible snapshot without copying the editable catalogue.
  Submission-time live eligibility and render-time snapshot provenance are
  separate responsibilities and may concern different Sanity revisions. The
  system independently verifies current eligibility while preserving the
  trustworthy context actually rendered to the visitor; it neither replaces
  that context silently with newer content nor trusts editable browser fields as
  its proof.
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
- Each Request and its protected audit and delivery history expires twelve
  months after its own acceptance. Off-provider encrypted backups expire no
  later than thirty days after creation and must not resurrect expired or
  verified-deleted Requests during restore.
- Routine agency work remains in the business inbox. Production database access
  is restricted technical access, not a staff dashboard or customer-management
  workflow.
- Corresponding agency notification and follow-up inbox copies follow the same
  twelve-month deletion rule under a named agency owner and evidenced deletion
  practice selected during Launch Readiness.

## D-001 — Commit the Complete Acceptance Aggregate and Delivery Intents

A submission becomes an accepted Request only after one Neon transaction
durably commits the complete acceptance aggregate:

- the shared Request envelope and exactly one typed journey detail;
- the immutable submitted contact and privacy snapshot;
- the bounded Experience identity and customer-visible snapshot, including its
  source Sanity revision, for a Booking Request;
- correction context when applicable;
- the bounded idempotency claim for the technical submission;
- the acceptance audit event; and
- one pending delivery record for each required purpose: agency notification and
  visitor acknowledgement.

The successful commit is the acceptance event. Actual mail-service network calls
start only afterward and remain outside the database transaction. A slow,
failed, or uncertain mail handoff cannot hold open, roll back, or redefine
Request acceptance. If the process stops immediately after commit, the database
still proves acceptance and exposes both pending delivery purposes for safe
recovery.

The submission handler still waits for the required initial delivery work before
returning the visitor-visible outcome. Waiting for post-commit work does not
move email inside the transaction or make delivery success an acceptance
condition.

Committing the Request first and creating audit and delivery records afterward
was rejected because a failure could leave an accepted Request without durable
notification work. A generic outbox with asynchronously derived projections was
rejected because it adds an event-processing boundary without proportional
Public Preview value.

## D-002 — Shared Request Envelope with Three Typed Detail Tables

Neon uses one shared Request table and three one-to-one typed detail tables for
Consultation Request, Booking Request, and General Contact. Each detail row uses
its Request ID as its primary and foreign key. A fixed detail type and composite
relationship to the Request ID and discriminator prevent a detail from attaching
to an envelope of the wrong journey type.

The one supported server-side acceptance writer derives the typed table from the
validated journey type and inserts exactly one matching detail within the D-001
transaction. Ordinary PostgreSQL primary-key, foreign-key, unique, check, and
composite constraints reject duplicate details in one typed table, orphaned
details, and envelope/detail type mismatch. Focused integration tests verify the
remaining aggregate invariant that every accepted Request has exactly one row
across the three sibling detail tables.

A custom deferred PostgreSQL trigger that counts across all typed tables was
rejected as disproportionate for a system with one supported writer and no
routine database editing. An intermediate generic detail-container table was
rejected because it adds a table and join without eliminating the application
logic or trigger needed to guarantee one subtype.

Arbitrary privileged SQL could bypass the final cross-table invariant, but such
writes are outside supported agency and application operation. Production
access remains restricted to authorized technical recovery, security, or
privacy work.

## D-003 — Layer Public, Authority, Persistence, and Database Validation

Greek Essence uses four validation layers with different responsibilities:

1. Handwritten Zod journey schemas validate untrusted public Consultation,
   Booking, and Contact input, including accepted cross-field rules and data-
   minimization boundaries.
2. Server orchestration performs authority checks that schema shape cannot
   prove, including current published Sanity requestability and private
   correction-reference and normalized-email matching.
3. Drizzle-generated Zod insert and select schemas validate internal persistence
   shapes derived from Drizzle table definitions.
4. PostgreSQL constraints provide the final durable guard for relational and
   storage invariants such as required columns, accepted values, uniqueness,
   foreign keys, and bounded numeric values.

Public schemas do not expose internal IDs, timestamps, normalized values,
idempotency records, audit states, delivery fields, or other server-managed
columns. Public and persistence boundaries may intentionally repeat a small
amount of primitive validation so a storage migration cannot silently alter
accepted visitor behavior.

Using refined Drizzle-generated insert schemas directly as public form and Route
Handler contracts was rejected because it would couple visitor input to database
columns, defaults, and migrations. Fully handwritten public and persistence
schemas were rejected because they would duplicate the complete table shape and
underuse the selected Drizzle–Zod integration.

First-party capability reference: <https://orm.drizzle.team/docs/zod>.

## D-004 — Separate Purpose-Specific Identities and Compare Exact Retries Directly

Greek Essence keeps four purpose-specific values:

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
while preserving the local part. It does not remove dots, strip plus-address
labels, apply provider-specific rules, or otherwise merge distinct mailboxes. A
later intentional Request receives a new idempotency token; the token is not a
person, account, public reference, or content-similarity fingerprint.

When an existing idempotency token is encountered, the server compares the new
canonical validated visitor-controlled fields directly with the retained
immutable Request. An exact match resolves to the same Request and public
reference without another Request or intentional email dispatch. Materially
different input produces one generic conflict and neither rewrites the original
nor creates a new Request under that token.

No payload digest is stored. Direct comparison is sufficient for the small
Request payload and avoids another canonical serialization and secret
lifecycle. A fast unkeyed digest was rejected because the content contains
personal and potentially sensitive data and the digest adds no necessary lookup
capability. Any later private keyed digest would require separate technical and
security justification and must never become general log data.

Reusing one value as database ID, public reference, and idempotency identity was
rejected because those purposes have different public, relational, and retry
lifecycles. Content- or time-derived duplicate identity was rejected because
similar intentional Requests are not technical retries.

## D-005 — Simple Private Correction Check Without a Lock or Foreign Key

Immediately before correction acceptance, the server performs one indexed
private check using the submitted earlier public reference and normalized
submitted email and requires the earlier Request to be retained at check time.
Every failure returns the same generic result whether the reference is unknown,
expired, deleted, or belongs to another email. Public behavior never reveals
which value matched or whether prior activity exists.

On a match, the D-001 transaction stores a complete independent correction with
its correction intent and submitted earlier reference. It stores no internal
target ID, foreign key, copied earlier content, or relationship entity. While
the earlier Request remains retained, authorized processing may resolve the
prior reference. After deletion, the correction remains understandable from its
own snapshot and reports only that the target is no longer retained; deletion
does not mutate it or extend either Request's retention.

The check uses no row lock. A theoretical deletion immediately after validation
has no material Public Preview consequence because the correction is a complete
independent Request and no customer-visible history, booking promise, or mutable
staff workflow depends on the live relationship. Lock orchestration was
rejected as disproportionate. A nullable foreign key was rejected because
deletion would mutate the later correction and recreate an excluded relationship
lifecycle.

## D-006 — Current Delivery Summary With Append-Only Attempts and Audit

Each accepted Request owns exactly two small current delivery rows created
atomically by D-001: one agency-notification purpose and one visitor-
acknowledgement purpose. A unique Request-and-purpose constraint prevents a
second current row for the same intentional delivery.

The current row contains only the minimum recoverable summary required to find
work and communicate truth, including whether the purpose is pending,
attempting, confirmed handed off, definitely failed, uncertain, or escalated,
plus bounded scheduling and attempt metadata. It is not a general queue, staff
case state, or proof that a recipient received or read an email.

Every actual mail call receives an append-only attempt row. A guarded database
change claims an eligible purpose and records that the attempt started before
the network call, protecting realistic overlap between initial delivery and
recovery. Each attempt preserves its minimum time, outcome, and bounded
diagnostic context. The known result then appends its outcome and updates the
current summary together. If processing stops after the attempt starts but
before the result is known, the unresolved attempt is uncertain and is not
blindly retried.

A definitely failed delivery receives bounded safe retry. An uncertain handoff
never receives blind redispatch. Exhausted retry or uncertainty enters a
separately monitored escalation route whose alert payload is minimized and
contains no Request body, notes, message, or full email address. Exact retry
counts, timing, scheduler, provider mechanism, and named recovery owner remain
downstream decisions; the retry, uncertainty, escalation, and minimization
behaviors are mandatory.

Acceptance, delivery transitions, recovery, escalation, and authorized manual
actions append the audit evidence required upstream. The current summary may
advance, but later success does not erase an earlier failure or uncertainty.
Delivery diagnostics retain only minimum provider and failure context and never
Request bodies, notes, messages, or full email addresses.

An append-only-only event model was rejected because ordinary recovery would
require event folding or projections. A mutable latest-status row without
attempt history was rejected because it would erase investigation evidence.
Exact state names, guarded SQL, retry policy, scheduling, escalation route, and
named owner remain downstream responsibilities.

## D-007 — Hard-Delete the Request Root With Database Cascades

Every Request stores its exact `expires_at` time. A simple scheduled cleanup
hard-deletes due Request roots in modest batches. The same aggregate-deletion
operation runs after the separate authorization and identity verification
required for an earlier deletion.

PostgreSQL ownership and cascade constraints remove the Request's typed detail,
immutable contact and privacy snapshot, idempotency identity, two current
delivery rows, delivery attempts, and audit events in the same transaction. This
makes deletion all-or-nothing and automatically covers declared owned
relationships without repeating table ownership in application deletion code.

Live Request tables retain no soft-deleted row or tombstone. A later correction
is not an owned child and has no foreign key to the earlier Request, so it is
neither deleted nor mutated. Its complete snapshot and submitted prior reference
remain independently understandable until its own expiry.

Deletion also removes pending delivery work owned by the Request. Email already
handed to an external mail service or recipient mailbox cannot be recalled. Soft
deletion or field-by-field anonymization was rejected because it would retain a
private Request after the accepted deletion event. Explicit application deletion
of each child table was rejected because it duplicates database ownership and
can omit later-added private rows.

## D-008 — Neon WebSocket Runtime and Separately Applied Reviewed Migrations

Runtime database work uses Drizzle's Neon serverless WebSocket driver so the
D-001 acceptance path can perform conditional work and dependent writes inside
one interactive PostgreSQL transaction. The Public Preview keeps one runtime
database path and does not also introduce the HTTP driver without a measured
need.

Drizzle Kit generates SQL migrations and metadata into the repository for
review and testing. An authorized deployment step applies each pending migration
once before the changed application serves traffic. Migration failure stops that
deployment. Public request handlers and application startup never create, push,
or migrate production schema.

The application uses one configured production Neon database within the
accepted free-quota boundary. Pull requests and preview deployments do not
automatically provision Neon branches or databases and never run migrations
against production. Connection URLs are environment secrets and do not enter
source, migration files, logs, screenshots, or generated evidence.

Redesigning D-001 around HTTP-only non-interactive batching was rejected because
it adds complexity to accommodate a transport limitation. Production schema
push and application-startup migration were rejected because they bypass
reviewed durable SQL or allow serverless instances to race while serving
requests. Future destructive or data-transforming changes require their own
bounded migration and rollback contract; the initial preview does not add a
generic zero-downtime framework.

First-party capability references:

- <https://orm.drizzle.team/docs/get-started/neon-new>
- <https://neon.com/docs/connect/choose-connection>
- <https://orm.drizzle.team/docs/kit-overview>

## D-009 — Encrypted Logical Snapshot With a Short-Lived Deletion Manifest

Each off-provider recovery copy is one encrypted logical snapshot of the private
PostgreSQL transactional schema and expires automatically no later than thirty
days after creation. It follows the schema and migration history owned by
Drizzle rather than creating a parallel per-Request serialization. Backups are
not history or reporting surfaces and are available only to named technical
recovery roles. Launch operation must remain within the accepted zero-new-
recurring-spend boundary; it does not add a self-hosted backup VPS or paid backup
service without separately approved demand and cost.

Routine twelve-month expiry needs no manifest entry because every restored
Request retains its `expires_at` value and the cutoff is reapplied before
production use. An earlier verified deletion receives one minimal protected
manifest entry before deletion is reported complete. The entry contains only
the random internal Request ID and the time when the last eligible backup that
could contain it will have expired. It stores no public reference, email,
Request content, or deletion reason and is removed when no eligible backup can
revive the Request.

A restore first enters an isolated, access-restricted environment. It restores a
compatible schema, removes every now-expired Request, applies every still-
relevant manifest ID through the D-007 cascade deletion, and runs focused
integrity checks. No restored database serves staff or public traffic before
those steps succeed.

Per-Request JSON exports were rejected because they would create a second schema
and serialization path that could omit typed details, delivery history, audit
rows, or later migrations. Neon-managed recovery alone was rejected because it
does not satisfy the accepted off-provider copy or carry the latest earlier-
deletion state when restoring an older snapshot.

The manifest is temporary restore-safety state, not a permanent deletion ledger,
customer history, or privacy-management platform. Exact provider, schedule,
archive and manifest layout, encryption and key custody, monitoring, write
order, expiry automation, and restore commands remain Runtime and Production
Foundations or Launch Readiness work.

## Cross-Cutting Invariants

- The durable Request, typed detail, idempotency claim, acceptance audit event,
  and both initial delivery purposes commit atomically before acceptance is
  claimed.
- Email network calls occur only after commit and never redefine acceptance.
- Untrusted visitor input, current external authority, internal persistence
  shape, and durable relational invariants remain separate validation concerns.
- Public reference, internal identity, normalized contact relationship, and
  retry identity remain separate values with separate disclosure and lifecycle
  boundaries.
- Every correction is complete and independently retained; its earlier reference
  is not a foreign-key ownership relationship.
- Current delivery state supports bounded recovery without erasing append-only
  attempt and audit evidence.
- Request-root deletion removes every owned private row in one transaction but
  never cascades to an independent later correction.
- Production schema change is a reviewed deployment operation, not request-time
  or startup behavior.
- Backup restore remains private and isolated until retention and earlier-
  deletion cleanup and focused integrity checks succeed.
- No Request content, notes, messages, or full email addresses enter general
  logs or delivery diagnostics.

## Explicit Exclusions

The Public Preview does not include:

- a wide nullable Request table, catch-all payload, or three unrelated Request
  families;
- a custom cross-table detail-count trigger or generic detail-container layer;
- database-derived public form contracts or visitor control of persistence
  fields;
- one identifier reused for internal, public, contact, and retry purposes;
- provider-specific mailbox merging, similarity-based deduplication, or a payload
  digest;
- a correction foreign key, correction-link entity, retention extension, or row
  lock for the theoretical deletion race;
- a general queue, outbox-projection platform, event-sourcing system, or staff
  case-management state;
- soft-deleted Requests, live Request tombstones, or application-maintained
  child-by-child deletion;
- automatic per-preview Neon databases, production schema push, application-
  startup migration, or request-time migration;
- a generic zero-downtime migration framework without a demonstrated need;
- per-Request JSON backup exports, permanent deletion history, or routine backup
  access; or
- Neon-managed recovery as the sole accepted recovery copy.

## Downstream Dependencies

### Bounded Schema and Application Design

Define exact Drizzle tables, columns, types, constraints, indexes, generated and
handwritten Zod schemas, field limits, coercion and mapping, canonical field
comparison, opaque-reference and token alphabets, lengths, hashing, issuance and
rotation, transaction functions, guarded delivery claims, exact correction-query
composition, test-database boundaries, and focused integration tests without
weakening these decisions.

### Application Architecture

Define server-only module boundaries and Route Handler orchestration for public
validation, Sanity authority checks, atomic persistence, idempotent retry,
correction validation, post-commit mail calls, truthful outcomes, and recovery
entry points. Browser-supplied data must not assert current Sanity eligibility or
control server-managed persistence values.

Agency-notification construction must make the inbox-only workflow usable. Every
agency notification includes the current opaque Request reference and submitted
reply address; a correction additionally includes its submitted earlier
reference. It does not automatically repeat or summarize prior Request content.

### Content Operations

Provide natural, semantically equivalent English and Greek generic correction-
failure copy without revealing whether the earlier reference, email, retained
Request, or another private condition matched.

### Runtime and Production Foundations

Define environment separation, secret injection, WebSocket connection lifetime,
deployment and migration ordering, rollback compatibility, cleanup cadence and
batch size, delivery retry and escalation mechanics, monitoring, backup and
manifest storage, encryption and key custody, expiry automation, restore
commands, provider quota behavior, backup-creation failure alerting, and the
truthful temporary failure required if a free provider limit prevents durable
Request acceptance. Backup-creation failure must reach the named technical
recovery owner selected during Launch Readiness.

### Launch Readiness

Verify actual provider plan and region facts, account control, migration and
rollback evidence, SMTP authorization, delivery recovery, restricted database
and backup access, twelve-month cleanup, authorized earlier deletion, backup
expiry, deletion-safe restoration, and named technical and agency roles. Name the
agency owner responsible for inbox-copy retention and evidence the twelve-month
inbox deletion practice.
Confirm the privacy explanation discloses that protected backup residue may
remain for up to thirty days after active deletion. Qualified privacy, security,
or legal review remains appropriate where actual processing, retention,
deletion, and recovery procedures require it.

## Material Risks and Validation Boundaries

- Sanity unavailability intentionally blocks a Booking Request when current
  requestability cannot be established.
- Mail handoff can be definitely failed or uncertain after durable acceptance;
  recovery must preserve that distinction without blind redispatch.
- Normalized email is weak private relationship evidence and must never become
  an account or identity claim.
- An earlier verified deletion must be durably represented outside any older
  backup that could otherwise revive the Request.
- WebSocket transaction support, selected Drizzle release-candidate compatibility,
  free provider quotas, encrypted off-provider storage, key custody, and actual
  restore behavior require implementation-time or Launch Readiness evidence.
