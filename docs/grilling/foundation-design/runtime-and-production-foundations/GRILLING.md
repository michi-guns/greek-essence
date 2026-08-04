# Runtime and Production Foundations Grilling

## Status

Active.

Started on 2026-08-02 after explicit operator authorization.

## Layer and Scope

Layer: Foundation Design.

This subject defines the costly-to-reverse runtime boundaries needed before Greek
Essence can safely implement and operate its public production-facing preview:
environment isolation, secret scope, deployment and migration ordering, rollback,
mail recovery execution, observability, quota behavior, backup automation,
deletion-safe restore, and the accepted hosting fallback boundary.

It does not authorize application implementation, dependency installation,
provider configuration, account access, migration execution, deployment,
production-data handling, or launch. Named owners, provider-plan evidence,
regions, account control, exact credentials, legal approval, and executable
production proof remain Launch Readiness work.

## Authority

This ledger is constrained by:

- [`../../DECISIONS.md`](../../DECISIONS.md);
- [`../../CLASSIFICATION.md`](../../CLASSIFICATION.md);
- [`../system-boundaries-and-domain-representation/DECISIONS.md`](../system-boundaries-and-domain-representation/DECISIONS.md);
- [`../editorial-content-platform/DECISIONS.md`](../editorial-content-platform/DECISIONS.md);
- [`../transactional-data-platform/DECISIONS.md`](../transactional-data-platform/DECISIONS.md);
- [`../application-architecture/DECISIONS.md`](../application-architecture/DECISIONS.md);
- [`../../request-processing-and-communications/DECISIONS.md`](../../request-processing-and-communications/DECISIONS.md); and
- [`../../protocol.md`](../../protocol.md).

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

## Locked Decisions

### D-001 — Local-Only Development With Synthetic Service Boundaries

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
credential injection
mechanism remain downstream choices.

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

### D-002 — Backward-Compatible Staged Schema Evolution

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

### D-003 — One Node.js Runtime With Invocation-Bounded Work

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

### D-004 — Provider-Neutral API Delivery With One Safe Fallback

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

## Open Questions

- D-005 — off-provider backup execution and freshness monitoring.

## Next Question

### Runtime and Production Foundations D-005 — Off-Provider Backup Execution

**State:** Pending.

The accepted privacy and recovery boundary requires encrypted logical copies of
Request data outside Neon, with each copy expiring no later than thirty days.
Restore must begin in an isolated private environment and reapply Request expiry
and verified earlier deletions before any restored data could return to
production. Provider-managed Neon recovery alone is insufficient.

The remaining foundation choice is where the small recurring backup job runs.
Neon's current guidance documents `pg_dump` automation through a scheduled GitHub
Actions workflow. Greek Essence's repository is public, and GitHub documents that
scheduled workflows run from the default branch, may be delayed, and are
automatically disabled after sixty days without repository activity. The backup
therefore also needs a freshness signal that cannot silently disappear with the
schedule.

1. **(recommended): Scheduled and manually triggerable GitHub Actions backup.**
   A focused workflow uses encrypted Actions secrets for a narrowly scoped backup
   connection and private object-storage write credential, runs the logical dump,
   encrypts it before upload, and relies on storage lifecycle rules to remove every
   copy within thirty days. No Request content or credentials enter repository
   files or logs. A separate freshness check alerts the named owner when no recent
   successful copy exists, covering job failure and public-repository schedule
   disablement. Restore remains a separately authorized manual drill into an
   isolated Neon environment. Exact schedule, storage provider, encryption tool,
   and alert route remain implementation and Launch Readiness evidence.
2. **Run backup export inside the production Next.js application.**
   A daily Vercel cron invokes a protected Node.js Route Handler that exports,
   encrypts, and uploads the database. This avoids GitHub's inactivity rule but
   places dump tooling and backup credentials inside the visitor-facing deployment,
   couples recovery to the application host, and must fit function duration,
   memory, and temporary-storage limits.

Current capability references:

- <https://neon.com/docs/manage/backup-pg-dump-automate>
- <https://docs.github.com/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule>
- <https://vercel.com/docs/cron-jobs/usage-and-pricing>

These references establish current scheduling and backup capabilities, not a
permanent free allowance or proof that any account, storage provider, encryption
configuration, or restoration procedure is launch-ready.

Which backup-execution model should Greek Essence adopt for Runtime and Production
Foundations D-005?

After the answer: lock the backup runner and credential boundary, retain exact
providers, schedule, encryption, freshness alert, restore commands, and named
owner for implementation or Launch Readiness, and store the next highest-value
unresolved runtime decision.
