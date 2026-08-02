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

None yet.

## Open Questions

- D-001: What must the atomic Neon acceptance transaction commit before a Request
  may be called received?
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

ID: D-001

Owning layer: Foundation Design.

Topic:
Atomic Request acceptance transaction.

Prompt:
What must Neon commit atomically before Greek Essence may treat a submission as
an accepted Request and start email delivery?

Options:

1. (recommended): **Commit the complete acceptance aggregate and durable delivery
   intents in one transaction.** The transaction stores the shared Request
   envelope, exactly one typed journey detail, immutable submitted contact and
   privacy snapshot, any Booking Request Experience snapshot, correction context
   when applicable, the bounded idempotency claim, the acceptance audit event,
   and one pending delivery record for each required email purpose. Only after
   that transaction commits is the Request accepted; actual email sending starts
   afterward.
2. **Commit the Request and idempotency state first, then create audit and
   delivery records immediately afterward.** This shortens the acceptance
   transaction, but a process failure between the steps can leave an accepted
   Request with no durable agency-notification or visitor-acknowledgement work,
   requiring a separate reconciliation mechanism to discover it.
3. **Commit the Request plus generic outbox events, then derive delivery and audit
   records asynchronously.** This closes the process-failure gap, but makes
   delivery truth and audit history dependent on a second projection step and
   introduces a generic event-processing boundary that the preview does not
   otherwise require.

Why this matters:

Consider a visitor submitting a Consultation Request. Neon commits the visitor's
brief, then the server process stops before contacting the mail service. Greek
Essence must still be able to prove that the Request was accepted and discover
that both required emails remain pending. If the durable commit contains only
form data, the website can truthfully claim receipt but the agency notification
may have no recoverable work record. If the commit includes the two pending
email purposes and acceptance audit event, recovery can resume safely without
creating another Request or guessing whether email work existed.

A representative relational shape for option 1 is a `requests` row, one matching
journey-detail row, one acceptance audit row, and two `request_deliveries` rows
for `agency_notification` and `visitor_acknowledgement`, all committed together.
The exact table and column names remain downstream schema design. Email network
calls stay outside the database transaction so a slow or failed mail service
cannot hold or roll back Request acceptance.

The recommendation creates one unambiguous durable acceptance boundary and
avoids an orphaned accepted Request or a generic event framework. Its tradeoff is
that the acceptance transaction writes several tightly related rows, which is
appropriate because all are required to recover the accepted workflow.

After answer:

- Lock the atomic acceptance transaction boundary and post-commit email boundary.
- Preserve exact tables, columns, transaction API, and retry scheduling for their
  owning later decisions or bounded technical design.
- Store D-002 as the next question.
