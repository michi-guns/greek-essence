# Application Architecture Grilling

## Status

Active Foundation Design grill, authorized by the operator on 2026-08-02. This
ledger does not authorize application implementation, dependency installation,
Sanity, Neon, Drizzle, or mail-provider configuration, schema or migration
execution, deployment, production-data access, Runtime and Production
Foundations, Launch Readiness, or another work unit.

## Owning Layer and Purpose

Owner: Foundation Design — Application Architecture.

Define how the replacement Next.js application composes the accepted public
content and Request workflows: App Router entry points, feature and shared
server-only modules, provider access, Route Handler orchestration, dependency
direction, data passed into browser code, and proportional Server/Client
Component boundaries. Preserve accepted Product and Domain Truth and the three
accepted upstream Foundation Design tracks without reopening the selected
technology stack.

## Concrete Public Preview Workflow

1. A visitor opens a localized public page. A Next.js App Router route obtains
   approved published Sanity content, applies the accepted publication and
   fallback rules, and renders the page without exposing draft content or
   provider credentials.
2. Most page composition runs as Server Components. Small Client Component
   islands add only interaction that requires browser state or browser APIs,
   such as interactive search controls or form feedback.
3. A Consultation Request, Booking Request, or General Contact submission enters
   through a server mutation boundary. Untrusted public input is validated before
   server-managed values or provider operations are allowed.
4. Booking Request orchestration independently verifies current Sanity
   requestability while preserving the bounded customer-visible snapshot and
   source revision actually rendered to the visitor.
5. Server-only orchestration asks the transactional layer to commit the complete
   Request aggregate, idempotency claim, audit event, and both delivery intents
   atomically in Neon through Drizzle.
6. Only after commit does server-only delivery orchestration call the agency mail
   service through Nodemailer. The visitor receives the truthful accepted,
   delivery-failure, or unsaved outcome already defined upstream.
7. Separate protected runtime entry points later recover eligible delivery work,
   retention deletion, and other operational tasks without creating a staff
   dashboard or exposing private Request data to public routes.

## Accepted Inputs

- Next.js is the application framework. Sanity is the authority for editable
  public and catalogue content; Neon PostgreSQL is the authority for accepted
  private Requests; Drizzle owns PostgreSQL schema and access; Nodemailer uses
  the agency mail service after durable acceptance.
- Public content uses one bilingual Sanity document per item, explicit repeatable
  types and controlled singletons, authenticated draft preview, minimal
  withdrawn versions, cached published reads, precise secured-webhook
  revalidation, localized published-only search, bounded fallback expiry, and
  public verification of material changes.
- Current Booking Request eligibility is a live Sanity authority check. Neon
  preserves the immutable published Experience ID and bounded localized
  customer-visible snapshot, including its render-time source revision. Editable
  browser fields do not prove current eligibility or control the saved snapshot.
- Consultation Request, Booking Request, and General Contact share one Request
  envelope with exactly one typed journey detail. Public validation, external
  authority validation, persistence validation, and database constraints remain
  separate responsibilities.
- Request acceptance is one atomic Neon transaction. Actual mail calls happen
  only after commit, and the submission path still waits for required initial
  delivery work before returning its truthful outcome.
- Exact technical retries resolve idempotently to the same accepted Request.
  Corrections use one private reference-and-normalized-email check and create a
  complete independent Request.
- Delivery recovery distinguishes confirmed, definitely failed, uncertain, and
  escalated outcomes. Uncertainty is never blindly resent. General logs and
  alerts exclude Request bodies, notes, messages, and full email addresses.
- Routine agency work remains in the business inbox. There is no public account,
  request-history surface, staff dashboard, customer-management system, generic
  queue, or supplier automation in the Public Preview.
- Server Components are the repository default. Client Components exist only
  where browser interaction requires them, and values passed to browser code
  must be serializable, public, and minimized.

## Locked Technical Direction

Do not reopen Next.js App Router, Sanity, Neon PostgreSQL, Drizzle, Zod v4,
Nodemailer through the agency mail service, Vercel as the current hosting
direction, or the conditional Netlify fallback. Exact package versions are
verified and pinned only during authorized implementation. Provider accounts,
regions, credentials, secrets, schedules, deployment topology, and named
production owners remain Runtime and Production Foundations, Launch Readiness,
or bounded implementation work.

## Explicit Boundaries

This track may define:

- dependency direction among App Router routes, feature modules, shared contracts,
  server-only orchestration, and provider-specific access modules;
- public page and layout composition, Route Handler responsibilities, and
  protected operational entry-point boundaries;
- journey-specific versus shared Request application services;
- public validation, Sanity authority-check, persistence, post-commit delivery,
  retry, correction, and truthful-outcome orchestration;
- data-transfer boundaries from server modules to Client Components;
- Server/Client Component placement and browser-state ownership;
- localized routing, error, loading, and not-found composition where architectural
  consistency is costly to reverse; and
- proportional testing seams for application orchestration and provider access.

This track must not invent visitor fields or copy, agency workflow states,
commercial promises, legal facts, production owners, credentials, monitoring
mechanisms, retry schedules, backup commands, hosting topology, exact Drizzle
schema, or deployment procedures. It must not install dependencies, configure
providers, implement routes or application modules, execute migrations, handle
production data, or begin Runtime and Production Foundations.

## Locked Decisions

None yet.

## Open Questions

- D-001: What server-only application boundary and dependency direction should
  connect App Router entry points to Sanity, Neon, and mail delivery?

## Next Question

ID: D-001

Topic:
Server-only application boundary and dependency direction.

Context:
In Next.js, pages and layouts are Server Components by default and may technically
query APIs or databases directly. Route Handlers provide HTTP mutation entry
points. Client Components and everything they import form a browser bundle, so
provider clients, credentials, private Request records, and server orchestration
must never cross that boundary.

A concrete Greek Essence journey touches several authorities. An Experience page
reads published Sanity content; a Booking Request separately verifies live
Sanity eligibility, atomically writes private Request state to Neon, then calls
the mail service after commit. The application needs one clear dependency rule
so route files do not each recreate that sequence or accidentally expose private
provider data.

Prompt:
How should App Router pages and Route Handlers reach Sanity, Neon, and mail
delivery for the replacement Public Preview?

Options:

1. (recommended): **Use thin App Router entry points over feature-oriented,
   server-only application modules and narrow provider modules.** A page or
   layout asks a feature read service for the minimal public view model it needs;
   a Route Handler translates the HTTP request and response while a journey
   application service owns validation and the accepted orchestration sequence.
   Only narrow server-only modules import Sanity, Drizzle/Neon, Nodemailer,
   environment secrets, or private persistence shapes. Shared domain rules and
   public contracts do not import Next.js or provider SDKs. This adds a small
   explicit boundary, but keeps the multi-provider workflow in one testable place
   without a generic framework or an interface for every function.
2. **Let each page and Route Handler call provider libraries directly, with
   shared helper functions where duplication appears.** This begins with fewer
   modules and Next.js permits server-side data access in Server Components, but
   content mapping, validation, transaction orchestration, data minimization,
   and failure translation can spread across route files as the three Request
   journeys grow.
3. **Put every provider operation behind internal HTTP Route Handlers and make
   both Server and Client Components call that internal API.** This creates one
   uniform API boundary, but same-application Server Components would incur an
   unnecessary HTTP hop and the application would need to maintain transport
   contracts for internal reads that do not require a separately deployable API.

Recommendation rationale:
Option 1 gives this small real-data application one auditable server boundary
without enterprise layering. For example, the Booking page receives only an
approved localized Experience view model, while the Booking submission service
alone coordinates the live Sanity check, Neon acceptance, and post-commit mail
work. Provider credentials and private rows cannot become Client Component props
by convenience, and focused tests can exercise the accepted sequence without
rendering a route or making every provider call over HTTP.

Why this matters:
If route files directly own provider access and orchestration, later changes to
validation, idempotency, eligibility, or truthful failure handling must be found
and coordinated across multiple pages and handlers. If the boundary is too
heavy, a solo developer instead maintains abstractions and internal network
calls that add no Public Preview value. This decision sets the dependency
direction before exact folders and handlers make it expensive to change.

First-party Next.js references:

- <https://nextjs.org/docs/app/getting-started/server-and-client-components>
- <https://nextjs.org/docs/app/getting-started/route-handlers>
- <https://nextjs.org/docs/app/guides/data-security>

After answer:

- Lock the selected server-only application boundary and dependency direction.
- Store D-002 as the next question without answering it.
