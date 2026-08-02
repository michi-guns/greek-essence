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
Server-side composition and dependency direction.

Context:
In Next.js, an **App Router entry point** is a framework-facing page, Server
Action, or Route Handler. Pages and layouts are Server Components by default and
may technically query APIs or databases directly. A **server-only module** may
hold credentials, query Sanity or Neon, and perform trusted orchestration; a
browser import must fail. A **feature application workflow** coordinates a
complete use case such as rendering an Experience page or submitting a Booking
Request. A **provider gateway** is the narrow module through which a workflow
uses Sanity, Neon/Drizzle, or mail; it does not require dependency injection,
generic repositories, or a separate deployed service.

The operator also supplied a non-authoritative travel-application architecture
reference for this question. Its conflicting product entities, lifecycle rules,
and commercial workflows are excluded. Its relevant architectural pattern is a
**domain-centered modular monolith delivered through vertical feature slices**:
one deployable Next.js application organized first by business capability, with
presentation, application, domain, and infrastructure responsibilities separated
inside a capability only when real code needs them. The pattern keeps Next.js
and provider SDKs outside domain behavior, keeps shared code small, and forbids
empty folder scaffolding or abstractions created only to resemble a methodology.
The operator expects Greek Essence will probably adopt this pattern, but has not
yet selected a D-001 option.

Client Components and everything they import form a browser bundle, so provider
clients, credentials, private Request records, and server orchestration must
never cross that boundary.

A concrete Greek Essence journey touches several authorities. An Experience page
reads published Sanity content; a Booking Request separately verifies live
Sanity eligibility, atomically writes private Request state to Neon, then calls
the mail service after commit. The application needs one clear dependency rule
so route files do not each recreate that sequence or accidentally expose private
provider data.

Prompt:
Which durable application boundary should App Router entry points use to reach
Greek Essence's trusted content, Request, and delivery behavior?

Options:

1. (recommended): **Use one domain-centered, feature-first Next.js modular
   monolith delivered through vertical slices.** Thin App Router presentation
   adapters call capability-owned application workflows; those workflows use
   framework-independent domain behavior and contracts where the accepted rules
   justify them, plus narrow server-only infrastructure adapters for Sanity,
   Drizzle/Neon, and mail. The source dependency direction is inward:
   presentation depends on application behavior, application depends on domain
   rules or contracts where needed, and provider infrastructure implements the
   narrow contracts required by the capability. A page asks a feature read
   workflow for the minimal public view model it needs; a mutation adapter invokes
   one journey workflow that owns validation and the accepted orchestration
   sequence. Only server-only infrastructure modules import provider SDKs,
   environment secrets, or private persistence shapes. Server Components call
   internal read workflows directly rather than the application's own HTTP
   endpoints. Cross-feature code holds only genuinely shared Request, locale,
   outcome, and validation concepts—not a generic `utils` dumping ground. Exact
   folders emerge with real code: no empty `domain`, `application`,
   `infrastructure`, or `presentation` scaffolding, and no entity, repository,
   interface, or dependency-injection abstraction without a concrete rule or
   testing boundary that needs it.
2. **Use route-centric slices with orchestration colocated in each App Router
   segment.** Each page and mutation entry point directly imports the required
   Sanity, Drizzle, and mail modules; shared helpers appear only after duplication
   is observed. This starts with fewer files, but framework entry points become
   the application layer. Validation, transaction ordering, data minimization,
   and truthful failure handling can drift across the three Request journeys,
   retries, and later recovery entry points, while complete workflow tests become
   framework-aware.
3. **Use global horizontal layers shared by every feature.** All App Router entry
   points call common application services, which call domain, repository, and
   provider layers—for example, a global `RequestService`, `ContentService`,
   `RequestRepository`, and `MailService`. Provider access is explicit and
   centralized, but Consultation, Booking, and Contact changes can spread across
   broad shared services. It also encourages generic repositories and interfaces
   before this one-application, one-writer Public Preview has multiple
   implementations that justify them.
4. **Put every provider operation behind internal HTTP Route Handlers and make
   both Server and Client Components call that internal API.** This creates one
   uniform API boundary, but same-application Server Components would incur an
   unnecessary HTTP hop and the application would need to maintain transport
   contracts for internal reads that do not require a separately deployable API.

Recommendation rationale:
Option 1 adapts the useful part of the operator-provided domain-centered
vertical-slice reference to Greek Essence's already accepted domain instead of
importing that reference's Customers, Quotes, confirmed Bookings, Payments, or
other conflicting scope. It is the smallest architecture that protects the
accepted cross-provider and privacy boundaries without introducing a separate
backend or generic enterprise framework. For example, the Booking Request page
receives only an approved localized Experience view model, while the Booking
Request submission workflow alone coordinates the live Sanity check, Neon
acceptance, and post-commit mail work. Provider credentials and private rows
cannot become Client Component props by convenience, and focused tests can
exercise the accepted sequence without rendering a route or making every
provider call over HTTP. Vertical delivery can complete one real Greek Essence
workflow at a time without modelling every future travel-agency capability.

Why this matters:
If route files directly own provider access and orchestration, later changes to
validation, idempotency, eligibility, or truthful failure handling must be found
and coordinated across multiple pages and handlers. If the boundary is too
heavy, a solo developer instead maintains abstractions and internal network
calls that add no Public Preview value. This decision sets the dependency
direction before exact folders and handlers make it expensive to change.

Deferred from D-001:

- Server Actions versus Route Handlers for visitor form submission;
- exact directories, filenames, aliases, interface syntax, and data-transfer
  field names;
- exact cache APIs, tags, webhook signatures, and fallback intervals;
- exact outcome-union names and HTTP status mapping;
- Node versus Edge runtime placement and WebSocket lifetime;
- retry scheduling, escalation transport, and production ownership; and
- detailed test doubles, package versions, and implementation tasks.

First-party Next.js references:

- <https://nextjs.org/docs/app/getting-started/server-and-client-components>
- <https://nextjs.org/docs/app/getting-started/route-handlers>
- <https://nextjs.org/docs/app/guides/data-security>

After answer:

- Lock the selected server-only application boundary and dependency direction.
- Store D-002 as the next question without answering it.
