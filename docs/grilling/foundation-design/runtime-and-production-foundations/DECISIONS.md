# Runtime and Production Foundations Decisions

Accepted by the operator on 2026-08-04 after Foundation Design grilling.

This document defines the durable runtime and production foundations for the
Greek Essence Public Preview: environment isolation, production schema evolution,
runtime placement and invocation lifetime, transactional-email provider execution,
and proportional off-provider backup and restore operation.

It does not authorize application implementation, dependency installation,
provider configuration, account access, migration execution, deployment,
production-data handling, Launch Readiness, or another work unit. Exact versions,
accounts, regions, credentials, schedules, named owners, legal approval, and
executable production evidence remain downstream work.

Current first-party documentation may establish provider capabilities, but it
does not override accepted Greek Essence product truth or silently prove plan,
quota, region, account, or production-readiness facts.

## Accepted Context

- Greek Essence is a public, production-facing market-validation preview that may
  receive real visitors and private enquiries.
- The selected direction is one Next.js application on Vercel, Sanity for public
  editorial content, Neon PostgreSQL with Drizzle for private Requests, and
  a provider-neutral transactional-email API gateway with Resend primary and
  Brevo as the single launch fallback. Netlify remains conditional fallback
  direction only if Vercel fails a mandatory commercial or technical gate.
- The release targets zero new recurring platform spend until real visitor demand
  supports a separately approved upgrade. Free quotas never justify silent enquiry
  loss, unsafe data handling, or misleading outcomes.
- Sanity drafts remain private. Authenticated Next.js Draft Mode provides the real
  bilingual site preview; ordinary public reads and search use only published
  content.
- Production uses one configured Neon database. Pull requests and preview
  deployments do not automatically provision Neon branches or databases and never
  migrate production.
- Reviewed Drizzle migrations are applied once as a separately authorized
  deployment step before changed application code serves traffic. Request handlers
  and application startup never migrate schema.
- Request acceptance and initial delivery intents commit atomically before mail
  work. Definitely failed mail may retry within a bounded policy; uncertain handoff
  is never blindly resent and exhausted work escalates through data-minimized
  operational signals.
- Private Request content, notes, messages, full email addresses, provider
  credentials, and environment secrets remain absent from general logs,
  diagnostics, screenshots, and generated evidence.
- Off-provider encrypted logical backups expire within thirty days. Restore begins
  in a private isolated environment and cannot serve staff or public traffic until
  retention expiry and verified earlier deletions have been reapplied and integrity
  checks pass.

## D-001 — Local-Only Development With Synthetic Service Boundaries

Greek Essence does not use automatic Vercel pull-request or branch preview
deployments. Routine UI and application development happens locally and does
not depend on a Vercel preview runtime.

Local Next.js and Sanity Studio development use one synthetic `development`
Sanity dataset. The production dataset contains the real approved public
content and drafts; the public site reads its published perspective, while real
drafts remain available only through the controlled authenticated production
Draft Mode workflow. The same version-controlled Sanity schema serves both
datasets, but local application development receives no production application
token or unrestricted draft access.

Local Request development uses a manually managed non-production Neon branch
containing synthetic data only. A normal Neon child branch carries its parent's
rows, so after production holds real enquiries the development branch must not
be cloned or refreshed from production data. It may instead be built from
reviewed migrations or a validated schema-only branch and then seeded with
synthetic Requests. Exact branch mechanics and current free-plan allowances
remain implementation and Launch Readiness validations.

Local mail is captured or redirected through a path that cannot deliver to real
visitors or the agency business inbox. Only production receives production Neon
and transactional-email provider credentials. The exact safe-mail tool and
credential-injection mechanism remain downstream choices.

This boundary was chosen because it preserves realistic local integration
without automatic provider provisioning, production traveler data, live mail,
or coupling unfinished schemas and UI to the live catalogue. Reading
production-published Sanity content during routine local development was
rejected because it would make the boundary less obvious and would not exercise
new schemas or draft behavior. Separate persistent local and hosted-preview
environments were rejected because Greek Essence has no routine Vercel preview
runtime and the extra fixtures, secrets, migrations, and cleanup would add work
without current value.

Current first-party capability evidence shows that Sanity datasets can select
different content environments, Sanity's current Free plan lists two datasets,
and Neon supports both copy-on-write and schema-only branches. These are
capability references rather than permanent plan guarantees. Launch Readiness
must confirm the exact zero-cost allowances before configuration; failure
reopens the boundary rather than granting production access or authorizing paid
services.

## D-002 — Backward-Compatible Staged Schema Evolution

Production schema changes use a small staged compatibility discipline rather
than requiring routine Request-journey downtime. A reviewed migration first adds
or widens schema without removing behavior required by the currently deployed
application. Before production, both the old and new application versions are
tested against that migrated schema in the synthetic non-production Neon
environment.

The compatible migration is then applied to production while the old Next.js
deployment remains live. Verification must exercise the affected reads, writes,
and controlled synthetic Request path; process health or the absence of a crash
alone is insufficient. Only after the old application is proven compatible is
the new application deployed and verified.

If the new application fails, Vercel rolls the application back while the
expanded compatible schema remains. Production does not automatically reverse
the migration. New application behavior must preserve whatever old-version
reads or writes are still required during the rollback window. Obsolete columns,
constraints, or compatibility behavior are removed only through a later
separately reviewed release after the old application is no longer an immediate
rollback candidate.

A genuinely unavoidable breaking migration uses an explicit truthful maintenance
path that stops new Request acceptance before incompatibility is introduced and
reopens it only after the matching application and schema are verified. This is
an exception, not the default for every schema-affecting release. A generic
zero-downtime migration framework remains excluded until demonstrated complexity
justifies it.

This model was chosen because Vercel application rollback remains useful without
making reverse database migration the first recovery action or interrupting
Request acceptance for ordinary additive changes. Routine maintenance for every
incompatible release was rejected because it would create avoidable public
unavailability and make rollback depend on reversing or restoring the database.

## D-003 — One Node.js Runtime With Invocation-Bounded Work

All Greek Essence server behavior uses the default Next.js Node.js runtime at
launch: public rendering, Server Actions, Route Handlers, Sanity webhooks, cache
revalidation, Request persistence, and mail work. The release does not split
public paths onto Edge merely because the platform offers it. Edge remains a
later option only if measured traffic or a concrete capability demonstrates
value that outweighs a second runtime boundary.

Every invocation completes or durably records its bounded work without assuming
that a warm Vercel function, in-memory connection, timer, worker, or queue will
survive. Neon WebSocket connections exist only as required for the current
transaction and are released according to the driver contract. Retry, retention,
backup, and recovery therefore require explicit invocations or manual operations,
not a resident application loop.

This was selected as the simplest proportional model for the Public Preview.
The transactional-email adapters and Neon WebSocket transactions work in Node.js,
and no traffic evidence justifies separate Node and Edge capability sets, secret
scopes, or test matrices. The split-runtime option was rejected as premature
optimization for the release's scale and market-validation purpose.

## D-004 — Provider-Neutral API Delivery With One Safe Fallback

Application workflows use one provider-neutral transactional-email interface.
React Email renders each agency notification or visitor acknowledgement once to
normalized HTML and plain text. Provider SDK types, API credentials, response
mapping, and error classification remain inside small server-only adapters.
Resend is the primary provider and Brevo is the only launch fallback. AhaSend is
deferred until measured need shows that two providers are insufficient.

The Request acceptance transaction continues to create exactly two durable
delivery intents and the accepted current-summary and append-only-attempt records
remain the only delivery persistence model. After commit, the originating bounded
Node.js invocation performs the required initial email work and waits before
returning its truthful visitor outcome. Each actual provider call is recorded
against the stable Request-and-purpose delivery identity.

If Resend reports a provider-specific result validated as definite
non-acceptance, such as explicit quota exhaustion or a safe temporary failure,
the gateway may make one automatic attempt through Brevo. Invalid recipient,
message, authentication, or sender-domain errors are terminal rather than copied
to another provider. A timeout or otherwise ambiguous handoff becomes uncertain
and stops; provider-specific idempotency cannot prove across providers that the
first service did not accept the message. Failure or uncertainty after the
bounded path uses the already accepted data-minimized escalation and protected
manual-recovery boundary.

The Public Preview does not add a background email worker, generic queue,
`email_jobs` duplicate, database-configurable routing, local cross-provider quota
counters or reservations, quota-allocation SQL, provider admin page, or automatic
delayed-retry scheduler. Those mechanisms would duplicate accepted delivery
records, introduce a second database access pattern, and add operational machinery
without launch evidence. The operator-provided three-provider router remains a
draft source whose useful adapter and failure-classification ideas are narrowed by
this decision rather than adopted wholesale.

Production provider keys remain server-only and only in production. Launch
Readiness must validate client-controlled Resend and Brevo accounts, privacy and
commercial terms, sender-domain authorization, API behavior and idempotency,
actual free quotas, alert independence, and the recovery drill before real
enquiries are accepted. No failed validation silently enables AhaSend, authorizes
a paid plan, or weakens the delivery contract.

## D-005 — Manual Encrypted Neon Exports With Manual Retention

The technical operator manually creates a portable logical backup of the
production Neon database using PostgreSQL `pg_dump` and Neon's direct, unpooled
connection path. The export includes the private transactional schema and its
bounded earlier-deletion manifest, runs outside the visitor-facing Next.js
deployment, and is encrypted locally before being retained in controlled local
storage outside Neon. It must not remain in an ordinary Downloads folder,
consumer cloud-synchronization folder, repository, GitHub artifact, or other
uncontrolled location.

The operator creates and verifies an encrypted export before and after each
production database migration and on a simple recurring manual cadence. The
operator also owns a manual retention procedure that removes every copy no later
than thirty days after creation. A missed export, failed verification, or overdue
copy is an operational and privacy exception for the operator to resolve; it does
not become application behavior. The Next.js application does not create, upload,
schedule, monitor, retain, or delete backup files.

The exact cadence, encryption command and key custody, controlled device or
removable-storage location, reminder, deletion checklist, and evidence remain
implementation and Launch Readiness work. Before real enquiries are accepted,
that procedure must be assigned and exercised without exposing Request content,
credentials, or decryption material in logs or repository files.

Neon's native history and point-in-time restore may provide faster recovery for
recent accidental changes, but it does not replace the portable off-provider
copy. Restoration remains separately authorized and begins in an isolated private
Neon environment. The backup is validated there, normal Request expiry and every
still-relevant earlier-deletion manifest entry are applied, and focused integrity
checks pass before any controlled production replacement can be considered.

The operator replaced the previously accepted scheduled GitHub Actions runner and
automatic object-storage expiry after identifying that another automated workflow,
external storage provider, credential set, lifecycle policy, freshness monitor,
and billing guard were disproportionate for this low-volume market-validation
preview. Cloudflare R2 and Backblaze B2 are therefore not selected. Automated
off-provider backup execution and expiry remain deferred unless real operating
evidence shows that the manual procedure is unreliable or the release's scale and
recovery needs materially change.

## Cross-Cutting Invariants

- Routine application and UI development is local and uses synthetic Sanity,
  Neon, and mail boundaries. Production drafts, Request rows, mail delivery, and
  provider credentials do not enter routine local development.
- Production schema evolution preserves compatibility with the currently deployed
  application until the new application is verified. Application rollback does
  not automatically reverse a compatible database migration.
- Launch server behavior uses one Node.js runtime and never depends on a warm
  process, in-memory connection, timer, worker, or queue surviving an invocation.
- Request acceptance remains the successful Neon transaction. Mail-provider
  handoff begins afterward, and a failed or uncertain handoff never rewrites
  acceptance or permits blind cross-provider redispatch.
- Off-provider backups are encrypted manual logical exports held in controlled
  local storage outside Neon. The application has no backup-file responsibility,
  every copy is manually removed within thirty days, and restore remains private
  and isolated until retention and earlier-deletion safeguards pass.
- Private Request content, notes, messages, full email addresses, provider
  credentials, and environment secrets remain absent from general logs,
  diagnostics, screenshots, and generated evidence.
- Zero new recurring platform spend remains the launch target. Provider limits
  never authorize silent enquiry loss, unsafe data handling, misleading outcomes,
  or an unapproved paid upgrade.

## Explicit Exclusions and Superseded Directions

The Public Preview does not add:

- automatic Vercel pull-request or branch preview deployments;
- production Request rows, production credentials, unrestricted drafts, or live
  mail delivery to routine local development;
- automatic per-preview Neon databases or production migrations from previews;
- routine all-at-once breaking migrations, automatic reverse migrations, or a
  generic zero-downtime migration framework;
- an Edge runtime split without measured value;
- resident application workers, in-memory timers, warm-function correctness, a
  generic email queue, duplicate email job storage, or delayed-retry scheduler;
- AhaSend, pooled free email quotas, database-configurable routing, local quota
  reservations, or a provider administration surface;
- GitHub Actions backup execution, Cloudflare R2, Backblaze B2, another external
  backup-storage account, or automatic object-storage expiry at launch; or
- routine application ownership of backup creation, scheduling, monitoring,
  retention, or deletion.

The earlier GitHub Actions and private object-storage backup direction is
superseded by D-005. Automated off-provider execution or expiry may be reconsidered
only when real operating evidence shows that the manual procedure is unreliable or
when release scale and recovery needs materially change.

## Downstream Implementation and Launch Readiness

Before real enquiries are accepted, bounded implementation and Launch Readiness
must verify or define:

- exact suitable package and provider versions, environment-variable and secret
  injection, and server-only access boundaries;
- the synthetic Sanity dataset, controlled authenticated production Draft Mode,
  synthetic Neon development branch, reviewed migrations, and a mail path that
  cannot deliver to real recipients;
- current provider plan allowances, commercial eligibility, regions, privacy
  terms, account control, credentials, and access restrictions;
- the old-and-new application compatibility test, production migration check,
  deployment verification, rollback procedure, and truthful maintenance path for
  a genuinely unavoidable breaking change;
- Resend and Brevo sender-domain authorization, API behavior, definite-failure and
  uncertain-handoff classification, idempotency behavior, quotas, alert
  independence, and recovery drill; and
- the manual backup cadence, direct unpooled Neon export procedure, encryption and
  key custody, controlled local storage, reminder and deletion checklist,
  thirty-day retention evidence, named technical operator, and deletion-safe
  isolated restore drill.

Vercel remains the current host direction. Its commercially eligible zero-cost
use must be proven before launch. If that mandatory gate fails, the accepted
conditional Netlify fallback returns for a focused topology review; no paid host
upgrade is automatic.

## Material Risks and Validation Boundaries

- A normal Neon child branch can contain its parent's rows. Development must not
  be refreshed from production after real Requests exist unless a validated
  schema-only mechanism prevents production data copying.
- A migration that removes old-application behavior too early can make application
  rollback unsafe. Destructive cleanup waits for a later reviewed release.
- Cross-provider retry after an ambiguous mail handoff can duplicate delivery.
  Failover is limited to one attempt after validated definite non-acceptance.
- Manual backups reduce services and automation but depend on a real operator
  procedure. A missed export, failed verification, uncontrolled copy, or overdue
  deletion is an operational or privacy exception that must be resolved before
  the procedure can be considered launch-ready.
- Neon native history may accelerate recent recovery but is not the sole accepted
  off-provider recovery copy.
