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

### D-001 — Domain-Centered Feature-First Modular Monolith with Vertical Slices

Greek Essence will use one deployable Next.js application organized primarily
by accepted business capability. Work will be delivered through complete
vertical slices rather than global technical layers or speculative modelling of
the wider travel industry.

Within a capability, thin App Router presentation adapters call capability-owned
application workflows. Those workflows coordinate the complete accepted use case
and use framework-independent domain behavior and contracts where a real business
rule or testing seam justifies them. Narrow server-only infrastructure adapters
provide Sanity, Drizzle/Neon, and mail behavior without exposing provider SDKs,
credentials, environment secrets, raw provider records, or private persistence
shapes outside the trusted server boundary.

The source dependency direction remains inward:

- presentation depends on application behavior;
- application depends on domain rules or narrow contracts where needed, not on
  Next.js presentation types or raw provider SDKs; and
- infrastructure implements the narrow capability contracts it needs and is
  wired to the application at the server composition boundary.

Server Components call internal feature read workflows directly rather than the
application's own HTTP endpoints. Pages receive bounded public view models, and
Client Components receive only minimized, serializable, public values. A mutation
adapter invokes one journey workflow that owns the accepted validation and
orchestration sequence instead of reproducing it in a route file.

Cross-feature code is limited to genuinely shared concepts such as Request,
locale, public outcome, and shared validation rules. A generic `utils` layer or
broad global services must not become an alternative ownership model.

The architecture remains proportional. `domain`, `application`,
`infrastructure`, and `presentation` folders appear only when they contain real
code. Greek Essence will not create an entity, repository, interface,
dependency-injection container, or empty architectural scaffold merely to match
a methodology. Exact capability names, directories, aliases, contract syntax,
and composition mechanics remain bounded implementation design.

This decision adapts the architecture from the operator-provided domain-centered
vertical-slice reference, but imports none of that reference's conflicting
Customers, Travelers, Quotes, confirmed Bookings, Payments, lifecycle rules, or
commercial workflows. Greek Essence's accepted Product and Domain Truth remains
authoritative. The reference's documentation protocol remains informative rather
than becoming part of this architecture decision.

Route-centric orchestration was rejected because validation, transaction order,
data minimization, and truthful failure handling could drift across Request and
recovery entry points. Global horizontal services and repositories were rejected
because capability changes would spread through premature abstractions. An
internal HTTP boundary for every provider operation was rejected because
same-application Server Components do not need an extra transport hop or public
transport contract.

### D-002 — Server Actions for Visitor Forms and Route Handlers for Machine Callers

The website-owned Consultation Request, Booking Request, and General Contact
forms use thin Server Actions. Each action treats its `FormData` as untrusted,
validates and maps only the owning journey's accepted public fields, invokes that
capability's application workflow, and returns only the bounded public result
needed by the form. The action owns React and form translation, not business
rules, provider calls, Request persistence, or delivery orchestration.

Callers that require an explicit HTTP contract use thin Route Handlers. This
includes the secured Sanity publication webhook and any later authorized machine
caller accepted for delivery recovery, retention, or another operational purpose.
Each handler verifies its caller as required, validates a bounded request, invokes
the owning application workflow directly, and translates only a safe HTTP result.
A Server Action and Route Handler do not call each other.

Both mechanisms remain externally reachable mutation boundaries and receive no
implicit trust from running on the server. Their workflows repeat all accepted
authority, validation, privacy, and persistence checks below the presentation
boundary. Inner behavior may be shared where it is genuinely common, but Greek
Essence does not expose a parallel public Request API without an accepted external
consumer.

An already-open form can hold a build-specific Server Action identity after a new
deployment. If that action cannot run, no Request has been accepted. The form must
not claim receipt or ask for a blind second submission; it provides a truthful
refresh-and-safe-retry path that preserves entered information where feasible and
reuses the same idempotency identity for the same intentional submission. Exact
copy and implementation remain bounded design.

Using Route Handlers for all visitor forms was rejected because three
website-owned journeys would need additional browser request,
progressive-enhancement, response-mapping, and form-state plumbing without an
external API requirement. Publishing both Server Actions and parallel Route
Handlers for every Request journey was rejected because it would create two
public mutation surfaces, duplicate contracts, and additional abuse and testing
responsibilities for hypothetical future consumers.

### D-003 — Bounded Booking Render Context in the Server Action Closure

When Next.js produces an Experience page containing the Booking form, the server
constructs the accepted bounded Request snapshot from the same validated published
Sanity result already needed to render the page. This is an in-memory selection of
fields, not another provider read, a Neon write, a provisional Request, or a new
staff record. A cached page version may reuse that rendered output rather than
performing the work separately for every visitor.

The thin Booking Server Action captures that server-created render context in its
encrypted build-specific closure. The closure contains only the published root
ID, source revision, visitor locale, and already-accepted bounded public
Experience snapshot. It excludes provider documents, drafts, credentials, media,
unrelated editorial fields, and private data.

On submission, the action validates the decrypted internal context and validates
visitor-authored `FormData` separately. The Booking application workflow preserves
the captured context as the immutable accepted Request snapshot and independently
reads current Sanity authority using the published root ID before any new
acceptance. Current content determines whether a new Request remains allowed; it
does not overwrite the proposition captured from the rendered page.

This is deliberately the smallest implementation compatible with accepted System
Boundaries D-003. Greek Essence will not add a custom signed-token format,
provisional snapshot storage, historical-revision retrieval, automated price
comparison, discrepancy alerts, customer dispute workflow, or extra evidentiary
records around it. Ordinary questions about an indicative-price or content change
remain part of normal agency communication. If the built-in closure proves
materially disproportionate during implementation, the accepted snapshot
requirement must be reopened explicitly rather than surrounded with fallback
systems.

A stale build-specific action follows D-002: no Request has been accepted, the
website makes no receipt claim, and the visitor receives the smallest truthful
refresh-and-safe-retry path. Exact state preservation remains best effort and must
not grow into a general browser recovery system.

Custom signing was rejected because it adds serialization, key lifecycle, and
versioning for one framework-owned form. Temporary server storage was rejected
because page views would create provisional state and cleanup. Submission-time
historical Sanity reconstruction was rejected because it adds provider work and
depends on old-revision availability even though rendering already had the needed
bounded values.

### D-004 — Explicit Journey Workflows with Narrow Earned Sharing

Consultation Request, Booking Request, and General Contact each use one explicit,
named, journey-owned application workflow. Their Server Actions validate and map
their own public commands before invoking those workflows. Each workflow remains
short enough for a solo developer to read from entry to outcome without tracing a
generic execution framework.

The workflows share only narrow operations whose behavior is already common and
whose consistency protects accepted invariants: exact-retry resolution, the
private correction check when requested, the one transactional Request acceptance
writer, and post-commit delivery processing. Booking alone owns its captured
Experience context and current Sanity authority preparation. Each journey retains
its own public fields, validation, data minimization, and outcome translation.

Some duplicate sequencing lines are acceptable and can be clearer than an early
abstraction. Abstraction must earn its place through demonstrated repeated
complexity, not mathematical symmetry. The operator's magnitude example is five
or more workflows sharing roughly three hundred or more lines; this records the
intended scale, not a fixed numeric gate that forbids a smaller extraction when a
concrete correctness or maintenance problem justifies it.

A shared typed coordinator with preparation hooks was rejected because three
small workflows do not yet justify a callback or strategy pipeline. One central
`submitRequest` workflow was rejected because it would collect unrelated journey
fields and Booking-only Sanity behavior in a growing conditional module. If real
implementation later demonstrates substantial common orchestration, a bounded
refactor may extract that proven shape without reopening the architectural
ownership decision.

## Open Questions

- None.

## Next Question

None. An authority and scope audit found no remaining unresolved question that
would materially change Application Architecture service ownership, module
boundaries, browser/server contracts, or dependency direction. Exact files,
types, cache APIs, dependency wiring, test seams, and small helper extractions are
bounded implementation choices. Runtime placement, deployment topology,
encryption-key configuration, recovery schedules, production ownership, and
operational controls belong to Runtime and Production Foundations.

The Application Architecture grill is ready for operator acceptance review and
verified distillation; it does not authorize implementation.
