# Application Architecture Decisions

Accepted by the operator on 2026-08-02 after Foundation Design grilling.
The operator amended the mail-provider dependency on 2026-08-04 through Runtime
and Production Foundations D-004; all other accepted application-architecture
meaning remains unchanged.

This document defines how the replacement Next.js application composes accepted
public content and Request workflows: capability ownership, dependency direction,
App Router delivery boundaries, server-only provider access, browser data
minimization, Booking render context, and proportional sharing among Request
journeys.

It does not authorize application implementation, dependency installation,
provider configuration, schema or migration execution, deployment,
production-data access, Runtime and Production Foundations, Launch Readiness, or
another work unit. Exact files, directories, imports, function names, result
types, dependency wiring, cache APIs, runtime placement, schedules, credentials,
monitoring, and production owners remain downstream work.

## Accepted Context

- Greek Essence uses one deployable Next.js application. It is not a microservice
  system and does not have a separately deployed application backend.
- Next.js App Router, Sanity, Neon PostgreSQL, Drizzle, Zod v4, the provider-
  neutral transactional-email interface with Resend primary and Brevo fallback,
  Vercel as the current hosting direction, and the conditional Netlify fallback
  are locked upstream and are not reopened here. Exact suitable versions are
  verified and pinned only during authorized implementation.
- Sanity is authoritative for editable public and catalogue content. Next.js owns
  public rendering, authenticated preview, published-content reads, localized
  search presentation, and secured cache revalidation.
- Public content uses complete bilingual records, authenticated draft preview,
  published-only cached reads, precise secured-webhook revalidation, localized
  published-only search, bounded fallback expiry, minimal withdrawn versions, and
  public verification of material changes.
- Neon PostgreSQL is authoritative for accepted private Requests. Drizzle owns
  PostgreSQL schema and access. Transactional-email provider calls begin only
  after durable Request acceptance.
- Consultation Request, Booking Request, and General Contact form one Request
  family with one shared envelope and exactly one typed journey detail. Each
  journey retains its own public fields, validation, data-minimization boundary,
  and truthful public outcome translation.
- A Booking Request is accepted only after a fresh Sanity authority check confirms
  that the Experience remains published and requestable. Neon preserves the
  immutable published Experience ID and bounded localized customer-visible
  snapshot, including its render-time source revision. Browser-editable values do
  not prove current eligibility or control the saved snapshot.
- Request acceptance atomically commits the complete Request aggregate,
  idempotency claim, acceptance audit event, and both initial delivery intents in
  Neon. Actual mail calls occur only after commit, and the submission path waits
  for required initial delivery work before returning its truthful outcome.
- Exact technical retries resolve to the same accepted Request. Corrections use
  the accepted private reference-and-normalized-email check and create a complete
  independent Request.
- Delivery recovery distinguishes confirmed, definitely failed, uncertain, and
  escalated outcomes. Uncertain mail handoff is never blindly resent. General
  logs, alerts, and delivery diagnostics exclude Request bodies, notes, messages,
  and full email addresses.
- Routine agency work remains in the business inbox. The Public Preview has no
  public account, Request history, staff dashboard, customer-management system,
  generic queue, or supplier automation.
- Server Components are the default. Client Components exist only for behavior
  that requires browser state or browser APIs, and they receive only minimized,
  serializable, public values.
- The architecture borrows the operator-provided external reference's
  domain-centered modular-monolith method, dependency direction, vertical-slice
  delivery, and testing seams. It imports none of that reference's Customers,
  Travelers, Quotes, confirmed Bookings, Payments, lifecycle rules, or commercial
  workflows. The reference's documentation protocol remains informative rather
  than part of this architecture decision.

## D-001 — Domain-Centered Feature-First Modular Monolith with Vertical Slices

Greek Essence uses one deployable Next.js application organized primarily by
accepted business capability. Work is delivered through complete vertical slices
rather than global technical layers or speculative modelling of the wider travel
industry.

Within a capability, thin App Router presentation adapters call capability-owned
application workflows. Those workflows coordinate the complete accepted use case
and use framework-independent domain behavior and contracts only where a real
business rule or testing seam justifies them. Narrow server-only infrastructure
adapters provide Sanity, Drizzle and Neon, and mail behavior without exposing
provider SDKs, credentials, environment secrets, raw provider records, or private
persistence shapes outside the trusted server boundary.

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

`domain`, `application`, `infrastructure`, and `presentation` describe
responsibilities, not mandatory directories. Greek Essence does not create an
entity, repository, interface, dependency-injection container, or empty
architectural scaffold merely to match a methodology. Exact capability names,
directories, aliases, contract syntax, and composition mechanics remain bounded
implementation design.

Route-centric orchestration was rejected because validation, transaction order,
data minimization, and truthful failure handling could drift across Request and
recovery entry points. Global horizontal services and repositories were rejected
because capability changes would spread through premature abstractions. An
internal HTTP boundary for every provider operation was rejected because
same-application Server Components do not need another transport hop or public
transport contract.

## D-002 — Server Actions for Visitor Forms and Route Handlers for Machine Callers

The website-owned Consultation Request, Booking Request, and General Contact forms
use thin Server Actions. Each action treats its `FormData` as untrusted, validates
and maps only the owning journey's accepted public fields, invokes that
capability's application workflow, and returns only the bounded public result
needed by the form. The action owns React and form translation, not business
rules, provider calls, Request persistence, or delivery orchestration.

Callers that require an explicit HTTP contract use thin Route Handlers. This
includes the secured Sanity publication webhook and any later authorized machine
caller accepted for delivery recovery, retention, or another operational purpose.
Each handler verifies its caller as required, validates a bounded request, invokes
the owning application workflow directly, and translates only a safe HTTP result.
Server Actions and Route Handlers do not call each other.

Both mechanisms remain externally reachable mutation boundaries and receive no
implicit trust from running on the server. Their workflows repeat all accepted
authority, validation, privacy, and persistence checks below the presentation
boundary. Inner behavior may be shared where it is genuinely common, but Greek
Essence does not expose a parallel public Request API without an accepted external
consumer.

An already-open form can hold a build-specific Server Action identity after a new
deployment. If that action cannot run, no Request has been accepted. The form must
not claim receipt or ask for a blind second submission. It provides a truthful
refresh-and-safe-retry path that preserves entered information where feasible and
reuses the same idempotency identity for the same intentional submission. Exact
copy and implementation remain bounded design.

Using Route Handlers for all visitor forms was rejected because the three
website-owned journeys would need additional browser request,
progressive-enhancement, response-mapping, and form-state plumbing without an
external API requirement. Publishing both Server Actions and parallel Route
Handlers for every Request journey was rejected because it would create two public
mutation surfaces, duplicate contracts, and additional abuse and testing
responsibilities for hypothetical consumers.

## D-003 — Bounded Booking Render Context in the Server Action Closure

When Next.js produces an Experience page containing the Booking form, the server
constructs the accepted bounded Request snapshot from the same validated published
Sanity result already needed to render the page. This is an in-memory selection of
fields, not another provider read, a Neon write, a provisional Request, or a new
staff record. A cached page version may reuse that rendered output rather than
performing the work separately for every visitor.

The thin Booking Server Action captures that server-created render context in its
encrypted build-specific closure. The closure contains only the published root ID,
source revision, visitor locale, and already-accepted bounded public Experience
snapshot. It excludes provider documents, drafts, credentials, media, unrelated
editorial fields, and private data.

On submission, the action validates the decrypted internal context and validates
visitor-authored `FormData` separately. The Booking application workflow preserves
the captured context as the immutable accepted Request snapshot and independently
reads current Sanity authority using the published root ID before any new
acceptance. Current content determines whether a new Request remains allowed; it
does not overwrite the proposition captured from the rendered page.

This is deliberately the smallest implementation compatible with accepted System
Boundaries D-003. Greek Essence does not add a custom signed-token format,
provisional snapshot storage, historical-revision retrieval, automated price
comparison, discrepancy alerts, a customer dispute workflow, or extra evidentiary
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

## D-004 — Explicit Journey Workflows with Narrow Earned Sharing

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

The shared exact-retry resolver returns the same Request only when the retained
canonical visitor-controlled fields match. Materially different input under the
same idempotency identity returns one generic conflict and creates neither a new
Request nor another intentional email dispatch. The shared correction verifier
returns one generic failure for every failed earlier-reference and normalized-email
check; it reveals neither which value matched nor whether prior activity exists.

Shared agency-notification construction includes the current opaque Request
reference and submitted reply address; a correction additionally includes its
submitted earlier reference. It does not automatically repeat or summarize prior
Request content. This keeps the accepted inbox-only agency workflow usable without
creating a dashboard or exposing private history publicly.

Some duplicate sequencing lines are acceptable and can be clearer than an early
abstraction. Abstraction must earn its place through demonstrated repeated
complexity, not mathematical symmetry. The operator's magnitude example is five
or more workflows sharing roughly three hundred or more lines. This records the
intended scale, not a fixed numeric gate that forbids a smaller extraction when a
concrete correctness or maintenance problem justifies it.

A shared typed coordinator with preparation hooks was rejected because three small
workflows do not yet justify a callback or strategy pipeline. One central
`submitRequest` workflow was rejected because it would collect unrelated journey
fields and Booking-only Sanity behavior in a growing conditional module. If real
implementation later demonstrates substantial common orchestration, a bounded
refactor may extract that proven shape without reopening the architectural
ownership decision.

## Cross-Cutting Invariants

- Next.js delivery adapters remain thin, untrusted boundaries; accepted authority,
  privacy, transactional, and truthful-outcome checks remain in capability-owned
  server workflows.
- Browser code never receives provider credentials, drafts, raw provider records,
  private persistence shapes, or unnecessary server-managed values.
- Server Components call application reads directly. Same-application code does
  not call its own Route Handlers merely to cross an artificial HTTP boundary.
- Sanity, Neon and Drizzle, transactional-email provider adapters and credentials,
  environment access, SQL or GROQ, and trusted orchestration remain server-only.
- A Request is not reported accepted unless its complete accepted Neon transaction
  committed. Mail work begins only after commit and cannot redefine acceptance.
- Current Booking eligibility and historical rendered Experience context remain
  distinct responsibilities.
- Shared code represents stable shared meaning or protects an accepted common
  invariant. Similar shape or a modest line-count reduction alone is insufficient.
- Delivery proceeds in small, testable end-to-end slices. Architectural boundary
  tests or lint rules may enforce costly dependency constraints where practical,
  but enforcement remains proportional.

## Explicit Exclusions

The Public Preview does not include:

- microservices or a separately deployed application backend;
- route-owned provider orchestration or global horizontal ownership of business
  workflows;
- an internal HTTP API for same-application Server Component reads;
- a duplicate public Request API without an accepted external consumer;
- Server Action-to-Route Handler or Route Handler-to-Server Action calls;
- provider SDKs, credentials, private Request records, raw SQL or GROQ, or mail
  operations in browser code;
- empty layer scaffolding, a generic repository or service for every capability,
  speculative interfaces, or a dependency-injection framework for symmetry;
- a universal Request coordinator, callback pipeline, or central conditional
  `submitRequest` service for the three launch journeys;
- custom render-context signing, provisional page-view persistence, historical
  revision reconstruction, discrepancy alerts, or automated dispute handling;
- exhaustive stale-page recovery or perfect historical evidence for ordinary
  editorial discrepancies; or
- external reference entities, lifecycle states, payment flows, or travel-agency
  assumptions that conflict with Greek Essence authority.

## Downstream Dependencies

### Bounded Implementation Design

Define exact capability directories, imports, aliases, public command and result
types, Zod schemas, server composition, provider adapter contracts, view models,
Client Component islands, cache access, idempotency reuse, form-state preservation,
and focused tests without weakening these decisions. Begin with the smallest
complete vertical slice and do not create empty architecture in advance.

Where a dependency rule is costly to violate, a focused test or lint rule may
protect it. Do not build a generic architecture-enforcement system for boundaries
that ordinary code review and tests can keep obvious.

### Runtime and Production Foundations

Define Node or Edge placement, WebSocket connection lifetime, protected operational
caller authentication, deployment and migration ordering, secrets, delivery and
retention schedules, recovery and escalation execution, observability, provider
quotas, backup and deletion-safe restore, rollback compatibility, and hosting
fallback implications.

### Launch Readiness

Verify production environment separation, credentials and account control,
webhook authentication, deployed stale-action behavior, current Sanity authority
checks, truthful form outcomes, transactional acceptance, post-commit mail
behavior, restricted private-data access, accessibility, and the named technical
and agency operating responsibilities.

## Material Risks and Validation Boundaries

- Next.js build-specific Server Action and encrypted-closure behavior must be
  verified against the implemented framework version. A failure must preserve the
  truthful non-acceptance and safe-retry boundary.
- Sanity unavailability intentionally blocks a new Booking Request when current
  requestability cannot be established.
- Provider calls or private persistence accidentally entering browser bundles
  would violate the accepted data and credential boundary.
- Premature shared orchestration can obscure journey behavior and create more
  maintenance work than duplication. Extraction requires demonstrated value.
- Runtime entry-point authentication, scheduling, production ownership, quotas,
  recovery, and monitoring remain unresolved by this architecture document and
  must be completed by their named downstream tracks.
