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
  Nodemailer through the agency mail service. Netlify remains conditional fallback
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
and SMTP credentials. The exact safe-mail tool and credential injection
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
Nodemailer already needs Node.js, Neon WebSocket transactions work there, and no
traffic evidence justifies separate Node and Edge capability sets, adapters,
secret scopes, or test matrices. The split-runtime option was rejected as
premature optimization for the release's scale and market-validation purpose.

## Open Questions

- D-004 — bounded mail retry execution without a durable background queue.

## Next Question

### Runtime and Production Foundations D-004 — Mail Retry Execution

**State:** Pending.

Every accepted Request creates separate visitor-acknowledgement and agency-
notification delivery work. The first send happens only after the Request commits.
A definitely failed send must receive bounded automatic retry; an uncertain send
must never be resent blindly, and exhausted work must create a data-minimized
escalation without asking the visitor to submit again.

The release now needs a proportional execution model. Vercel Hobby cron currently
runs at most once per day. That cadence is suitable for slow housekeeping but
would leave a recoverable visitor acknowledgement or agency notification waiting
for up to a day. A more frequent external scheduler would add another production
service, secret, failure mode, and monitoring dependency.

1. **(recommended): Retry within the originating invocation, then escalate for manual recovery.**
   After commit, a definitely failed send receives a small bounded number of safe
   retries while the invocation can still complete truthfully. If they fail, the
   delivery is recorded as exhausted and a separately monitored, data-minimized
   alert requests human recovery through a protected operation. Uncertain handoff
   is recorded and escalated without redispatch. There is no background mail queue
   or frequent scheduler at launch; exact retry count and short timing remain
   implementation settings within provider and function limits.
2. **Persist delayed retries for a scheduled recovery invocation.**
   Definitely failed deliveries store a future retry time and a protected
   scheduled caller claims them later. This handles longer transient outages
   automatically, but useful mail timing requires a dependable scheduler more
   frequent than the current zero-cost Vercel cadence, plus its own credentials,
   monitoring, overlap protection, and failure recovery.

Current capability references:

- <https://vercel.com/docs/cron-jobs/usage-and-pricing>
- <https://nodemailer.com/usage/>

These references establish the current scheduling and mail capabilities, not the
exact retry count, function duration, alert route, or recovery owner. Launch
Readiness must prove that the selected alert path is monitored and independent
enough to report an SMTP failure without copying private Request content.

Which mail-retry execution model should Greek Essence adopt for Runtime and
Production Foundations D-004?

After the answer: lock the automatic-retry and escalation execution boundary,
retain exact retry values, alert recipient, and protected recovery procedure for
later work, and store the next highest-value unresolved runtime decision.
