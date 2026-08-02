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

## Open Questions

- D-002: Which Next.js mutation entry points should carry website-owned visitor
  forms and independent machine callers into the accepted application workflows?

## Next Question

ID: D-002

Topic:
Visitor and machine mutation entry points.

Context:
Next.js offers two relevant mutation adapters. A **Server Action** is a server
function invoked through React's form or action mechanisms. It receives untrusted
input through a framework-managed POST, can return a bounded result to
`useActionState`, and supports progressive form enhancement and a single response
containing both the result and refreshed UI. It is still publicly reachable and
must perform the same input and authority checks as any public endpoint. Its
build-generated action identity may become stale when an already-open page
submits after a new deployment, so the UI needs a safe refresh-and-retry path
that preserves entered values and the accepted idempotency identity.

A **Route Handler** is a stable URL and HTTP contract using `Request` and
`Response`. It is the natural boundary for callers that are not participating in
the React page interaction, such as the secured Sanity publication webhook and
later protected delivery-recovery or retention entry points. Route Handlers are
also publicly reachable and must authenticate or verify machine callers, validate
their bounded input, and translate only safe outcomes.

D-001 now keeps both adapters thin: neither owns business rules, provider access,
or Request orchestration. The open choice is whether website-owned Consultation,
Booking Request, and General Contact forms should use React's Server Action path
or the same explicit HTTP endpoints required by independent machine callers.

Prompt:
Which Next.js entry-point split should invoke Greek Essence's accepted mutation
workflows?

Options:

1. (recommended): **Use Server Actions for the three website-owned visitor forms
   and Route Handlers only for callers that require an explicit HTTP endpoint.**
   Each form action is a thin public presentation adapter that validates and maps
   its untrusted form payload, invokes the owning application workflow, and
   returns only the bounded public outcome needed by that form. Secured Sanity
   webhooks and later protected operational callers use thin Route Handlers that
   invoke their own application workflows. Both adapters share inner contracts
   where behavior is genuinely shared; neither calls the other. This follows the
   installed Next.js 16 form path, retains progressive enhancement and
   `useActionState`, avoids creating a public Request API with no external
   consumer, and still provides stable HTTP contracts where machines require
   them. The form experience must handle a stale action after deployment through
   a truthful refresh-and-safe-retry path without claiming receipt or discarding
   entered information.
2. **Use Route Handlers for all mutations, including visitor forms.** Each form
   submits to a stable journey-specific HTTP endpoint through browser code or a
   native form POST, and the presentation layer maps HTTP responses back into
   field and outcome state. This creates explicit stable transport contracts and
   avoids build-generated Server Action identity, but Greek Essence must own more
   browser request, progressive-enhancement, response, and form-state plumbing
   for three website-only submission journeys.
3. **Expose both Server Actions and parallel Route Handlers for every visitor
   Request journey.** The website uses Server Actions while a first-class public
   HTTP API exposes the same Consultation, Booking Request, and General Contact
   submissions. Both adapters call the same application workflows, but the
   release must maintain and protect two public mutation surfaces despite having
   no accepted external Request client. This preserves future API flexibility at
   the cost of duplicate contracts, tests, abuse controls, and deployment surface
   now.

Recommendation rationale:
Option 1 assigns each framework mechanism to the caller it naturally serves. A
visitor submitting the Booking Request form receives the progressive,
UI-integrated Server Action path, while Sanity receives a stable signed webhook
URL and operational automation later receives separately protected endpoints.
The accepted application workflows remain reusable and testable below both
adapters. The one additional Server Action deployment failure mode is real but
bounded: no Request has been accepted when the action cannot be found, and the
form can preserve the visitor's data and idempotency identity through a refresh
and safe retry rather than creating a second API surface for every form.

Why this matters:
Server Actions and Route Handlers are both public mutation boundaries, not
trusted shortcuts. Choosing their responsibilities now sets the browser form
contract, progressive-enhancement behavior, stable machine endpoints, and the
number of externally reachable adapters that must remain consistent and tested.

Deferred from D-002:

- exact action names, Route Handler URLs, directories, files, and exports;
- exact public form payloads, `FormData` mapping, result-union names, status codes,
  and field-error representation;
- exact Sanity webhook signature and operational authorization mechanisms;
- exact stale-action detection copy and implementation;
- abuse controls, rate thresholds, and production deployment configuration;
- Node versus Edge runtime placement and WebSocket lifetime;
- recovery schedules, escalation transport, and named ownership; and
- detailed implementation and test mechanics.

Installed Next.js 16.2.12 references:

- <https://nextjs.org/docs/app/getting-started/mutating-data>
- <https://nextjs.org/docs/app/guides/forms>
- <https://nextjs.org/docs/app/guides/server-actions>
- <https://nextjs.org/docs/app/getting-started/route-handlers>
- <https://nextjs.org/docs/app/guides/backend-for-frontend>
- <https://nextjs.org/docs/app/guides/data-security>

After answer:

- Lock the visitor-form and machine-caller entry-point responsibilities.
- Store D-003 as the next question without answering it.
