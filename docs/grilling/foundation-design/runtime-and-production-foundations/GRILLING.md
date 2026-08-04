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

## Open Questions

- D-002 — production schema, application deployment, and rollback compatibility.

## Next Question

### Runtime and Production Foundations D-002 — Schema, Deployment, and Rollback Compatibility

**State:** Pending.

A reviewed Drizzle migration must run before changed application code serves
traffic, but the existing production deployment remains live while that
migration runs. If the new deployment then fails, Vercel can point production
back to the previous application deployment; that rollback is safe only if the
database schema still supports the previous code.

The foundation choice is how Greek Essence handles schema changes that would
otherwise make the old and new application versions incompatible during the
release or after an application rollback.

1. **(recommended): Backward-compatible staged schema evolution.**
   Add or widen schema first without removing behavior required by the current
   application, apply that reviewed migration, manually deploy and verify the new
   application, and remove obsolete schema only in a later separately reviewed
   release after the previous application can no longer be restored against it.
   If the new application fails, Vercel can roll back the application while the
   compatible schema remains. A genuinely unavoidable breaking migration uses an
   explicit truthful maintenance path rather than pretending the ordinary release
   is safe. This is a release discipline, not a generic zero-downtime migration
   framework.
2. **Maintenance boundary for every incompatible schema release.**
   Before migration, the public Request journeys stop accepting submissions and
   show a truthful temporary-unavailability outcome. Apply the migration, deploy
   the matching application, verify both together, and reopen acceptance. This
   permits direct breaking migrations but creates an avoidable interruption and
   makes rollback depend on a reviewed reverse migration or compatible database
   restore rather than Vercel application rollback alone.

Current capability references:

- <https://vercel.com/docs/cli/deploy>
- <https://vercel.com/docs/instant-rollback>
- <https://orm.drizzle.team/docs/drizzle-kit-migrate>

These references establish available deployment, application-rollback, and
migration capabilities. They do not prove that a particular Greek Essence schema
change is backward compatible or authorize migration or deployment. Exact release
commands, readiness evidence, and the rare breaking-change procedure remain later
work.

Which release-compatibility model should Greek Essence adopt for Runtime and
Production Foundations D-002?

After the answer: lock the schema/application compatibility and rollback boundary,
retain exact deployment commands and evidence for later work, and store the next
highest-value unresolved runtime decision.
