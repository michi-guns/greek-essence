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

None yet.

## Open Questions

- D-001 — environment isolation across local development, Vercel previews, and
  production.

## Next Question

### Runtime and Production Foundations D-001 — Environment Isolation

**State:** Pending.

A developer opens a pull request and Vercel creates a live preview URL. That
preview must exercise realistic Sanity reads, Request persistence, and mail
outcomes without receiving production Neon or SMTP credentials, writing test
Requests into the real database, exposing private drafts, or sending messages to
real visitors or the agency business inbox.

The accepted Transactional Data Platform already rejects automatic per-preview
Neon databases. The remaining foundation choice is therefore which stable
non-production services local development and preview deployments may share, and
whether they may read production-published Sanity content.

1. **(recommended): One shared synthetic non-production environment for local and preview use.**
   Local development and Vercel previews use one non-production Sanity dataset,
   one shared non-production Neon database, and a mail path that cannot deliver to
   real visitors or the agency business inbox. Only the production deployment
   receives production Sanity, Neon, and SMTP credentials. Actual private Sanity
   drafts are previewed through controlled authenticated production Draft Mode,
   not generic pull-request previews. This gives one clear safety boundary without
   per-PR provider provisioning.
2. **Separate persistent development and preview environments.**
   Local development and Vercel previews each receive their own non-production
   Sanity, Neon, and safe-mail configuration. This reduces interference between a
   developer's local work and shared preview demonstrations, but doubles fixture,
   secret, migration, and cleanup work before traffic has justified it.
3. **Read production-published Sanity content from non-production runtimes.**
   Local and preview deployments may query only the public published Sanity
   perspective, while still using shared non-production Neon and safe mail. This
   avoids maintaining synthetic editorial content, but couples unfinished code to
   the live catalogue, does not test schema changes or draft behavior, and makes
   the environment boundary less obvious.

Current capability references:

- <https://vercel.com/docs/deployments/environments>
- <https://www.sanity.io/docs/content-lake/datasets>
- <https://neon.com/docs/guides/neon-managed-vercel-integration>

These references confirm that Vercel environment scopes, separate Sanity datasets,
and Neon preview branching exist. They do not override the accepted decision that
Greek Essence will not automatically provision per-preview Neon databases.
Whichever option is selected still requires later evidence that its exact provider
configuration fits compliant zero-cost allowances. Failed validation reopens the
boundary or hosting direction; it never silently grants production credentials or
authorizes a paid upgrade.

Which environment-isolation model should Greek Essence adopt for Runtime and
Production Foundations D-001?

After the answer: lock the chosen environment and secret boundary, retain exact
provider setup and account evidence for later work, and store the next highest-
value unresolved runtime decision.
