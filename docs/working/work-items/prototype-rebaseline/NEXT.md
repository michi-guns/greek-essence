# Prototype Rebaseline

## Status

Active

## Ownership and Scope

Owner: Hermes Agent (`greek-essence`)

Scope: prototype archive verification, curated reference material, active-tree
retention and removal planning, expanded client-requirements intake,
architecture rebaseline, and promotion of settled documentation.

## Current State

- The prototype archive, active-tree retention boundary, expanded-requirements
  intake, first source batch, and public production-facing preview status remain
  verified and documented. The archived showcase is historical only.
- The operator accepted the project-level Public Preview Release grill on
  2026-07-29. Durable outcomes are distilled in
  `docs/grilling/DECISIONS.md`.
- The operator approved removal of the raw project ledger on 2026-07-29.
  `docs/grilling/GRILLING.md` is removed, Git history retains it, and
  `docs/grilling/DECISIONS.md` is now the sole project-level grilling authority.
- The accepted product provides destination and Experience discovery, catalogue
  search and filters, consultation requests, non-confirming booking requests,
  and general contact. The agency follows up manually through its existing
  email and telephone process.
- The selected platform direction is Sanity, Neon PostgreSQL, Drizzle, Vercel,
  and Nodemailer through the agency mail service. Netlify is only the accepted
  fallback direction if Vercel fails a mandatory commercial or technical gate.
- The operator clarified that the Public Preview is commercially a
  market-validation experiment: target zero new recurring platform spend, use
  compliant free quotas until traffic proves demand, and require explicit client
  approval for a later paid upgrade. Visitor-driven quota pressure is a positive
  validation signal; unrelated CI or operational exhaustion is not. Neither
  case authorizes silent enquiry loss, unsafe data handling, or misleading
  failure behavior.
- Example-led client validation is required. Prepare realistic drafts,
  templates, and mockups, but do not publish unapproved legal text, prices,
  claims, testimonials, media rights, response promises, or other client facts.
- Customer accounts, payments, paid consultation, questionnaires, scheduling,
  live availability, confirmed online booking, cancellation/refund handling,
  staff dashboards, customer-management systems, and supplier automation are
  deferred. Newsletter is excluded entirely.
- Eight feature-grilling workspaces exist in accepted order. Public Brand Pages
  is the accepted first feature. D-001 establishes that
  Home will lead with useful Greece discovery and make personal agency help
  available without implying live availability or confirmed booking. D-002
  permits only client-approved, verifiable trust evidence; unsupported social
  proof is omitted rather than published provisionally. D-003 makes About the
  deeper explanation of who the agency is, how its human help works, and why it
  is credible. D-004 establishes two shared travel-planning paths: catalogue
  browsing and consultation, while keeping general contact secondary and
  booking requests Experience-specific. D-005 preserves separately stored
  English and Greek content, permits AI-assisted drafting, and requires complete
  human-reviewed language experiences with named client ownership. The five
  decisions were accepted by the operator on 2026-07-29 and distilled into
  `docs/grilling/public-brand-pages/DECISIONS.md`. The operator separately
  approved removal of the raw feature ledger on 2026-07-29; Git history retains
  it. Catalogue Discovery D-001 now establishes explicit per-Experience
  requestability: publishing alone does not enable a booking request, and
  requestability never means availability or confirmation. D-002 establishes
  Tour, Activity, and Travel package as the three launch Experience types;
  Cruise and Transfer are deferred, while real content and package terminology
  still require client validation. D-003 establishes localized title-and-summary
  search across Destinations and Experiences, with destination and type filters
  for Experiences; Interest is conditional on an approved bilingual taxonomy,
  while price, duration, and difficulty filters are deferred. D-004 permits only
  structurally complete, client-approved indicative “from” prices with explicit
  confirmation wording, and prohibits availability claims. D-005 blocks
  incomplete publication, removes withdrawn Experiences from discovery and new
  requests, provides a generic recovery page at their former URLs, and preserves
  historical request intelligibility as a downstream contract. The operator
  accepted the five decisions on 2026-07-29, and they are distilled into
  `docs/grilling/catalogue-discovery/DECISIONS.md`. The operator separately
  approved removal of the raw feature ledger on 2026-07-29; Git history retains
  it. Consultation Request D-001 establishes a short structured initial trip
  brief that gives the agency useful context without recreating the deferred
  detailed questionnaire or collecting sensitive planning data too early.
  D-002 makes email the sole acknowledgement and follow-up channel for the
  consultation journey, with no response-time promise until the client confirms
  one the agency can reliably meet. D-003 requires name, email, party size, at
  least one destination or interest, and privacy acknowledgement; timing,
  budget guidance, and notes are optional, while unnecessary sensitive details
  are excluded. D-004 requires a just-in-time privacy summary, full-notice link,
  and read-only acknowledgement without mislabeling it as consent; actual legal
  facts and wording require client and qualified review. D-005 establishes
  distinct validation, saved, email-failure, and unsaved outcomes with an opaque
  request reference and no false receipt or resubmission claim. D-006 retains
  the optional notes field with the nine-word persistent warning “Please don’t
  include passport, payment, or medical information here”; notes are excluded
  from notification emails, and downstream handling requires privacy review.
  D-007 rejects a special age gate, age data, or child-specific workflow unless
  later concrete client or qualified-review evidence requires one. The operator
  accepted the seven decisions on 2026-07-29, and they are distilled into
  `docs/grilling/consultation-request/DECISIONS.md`. The operator separately
  approved removal of the raw feature ledger on 2026-07-29; Git history retains
  it. Booking Request D-001 establishes that the selected Experience is carried
  automatically and the visitor provides preferred and optionally alternative
  or flexible dates, party size, contact details, preferred contact method,
  optional notes, and privacy acknowledgement. Booking Request D-002 requires
  concise non-confirming wording near the form introduction, beside submission,
  in the saved-request acknowledgement, and in the customer verification or
  acknowledgement email. Booking Request D-003 requires one preferred date, an
  optional alternative date or flexible-date indication, adult and conditional
  child counts, and an optional bounded accessibility or practical-needs field
  that warns against medical, passport, or payment information. Booking Request
  D-004 blocks new submissions after an Experience is disabled but preserves
  already-saved requests, a bounded historical Experience snapshot, and manual
  agency follow-up without automatic cancellation or deletion. Booking Request
  D-005 distinguishes validation failure, safely saved acknowledgement,
  saved-with-customer-email-failure, and unsaved persistence failure without
  false confirmation or duplicate-producing resubmission advice. The operator accepted
  all five Booking Request decisions on 2026-07-29; they are distilled into
  `docs/grilling/booking-request/DECISIONS.md`, and the operator explicitly
  approved removal of the raw feature ledger and feature-branch cleanup after
  successful merge.
  Grill one feature at a time.
- The architecture register now records Sanity, Neon, Drizzle, Vercel with
  optional Netlify, and Nodemailer as accepted directions with remaining
  feature-level and launch validation.
- No application implementation, dependency installation, schema migration,
  or active application path change is authorized by these decisions.
- General Contact D-001 establishes that Contact accepts ordinary questions
  outside the dedicated Consultation Request and Booking Request journeys and
  provides prominent routes to those journeys instead of accepting incomplete
  travel requests through a catch-all form.
- General Contact D-002 requires name, email, subject, message, and privacy
  acknowledgement; email is the sole acknowledgement and follow-up channel,
  with no telephone field or reply preference.
- General Contact D-003 uses a short pre-form intent choice: trip planning routes
  to Consultation Request, specific-Experience interest routes through the
  catalogue to an eligible Booking Request, and another question reveals the
  General Contact form, with visible fallback links.
- General Contact D-004 requires the shared just-in-time privacy explanation,
  read-only acknowledgement, and persistent warning against passport, payment,
  or medical information; it excludes blanket and marketing consent.
- General Contact D-005 distinguishes validation failure, safely saved success,
  customer-email failure after saving, agency-notification failure after saving,
  and persistence failure without false receipt or duplicate-producing advice.
- The operator accepted all five General Contact decisions on 2026-07-29. They
  are distilled into `docs/grilling/general-contact/DECISIONS.md`. The operator
  separately approved removal of the raw feature ledger on 2026-07-29; Git
  history retains it.
- Request Processing and Communications D-001 establishes that a valid request
  is accepted after its private record is durably committed in Neon. Agency and
  visitor email outcomes are recorded and recovered separately; email failure
  cannot revoke acceptance, prompt resubmission, or be ignored. The shared
  acceptance and delivery-state boundary is recorded in the feature contract.
- Request Processing and Communications D-002 uses normalized submitted email
  to group an internal customer-contact relationship while preserving the
  immutable contact snapshot on every request. Email is not proof of a unique
  person; public forms do not expose or prefill prior details, and approximate
  identity merging is prohibited. D-003 owns whether a later submission is a
  new request, an explicit correction, or an accidental duplicate.
- Request Processing and Communications D-003 preserves an immutable
  chronological history of accepted requests under the email-based contact
  relationship. New requests are the default; an explicit correction requires
  the earlier opaque reference and creates a linked record without overwriting
  history. Exact technical retries resolve idempotently to the same request,
  and no public account or request-history surface is introduced.
- Request Processing and Communications D-004 limits the website to truthful
  system-owned acceptance, correction, notification, and acknowledgement
  states with append-only transition history. Staff handling remains in the
  agency inbox; unsupported lifecycle fields and direct database maintenance
  are excluded, and general logs must not copy private request content.
- Request Processing and Communications D-005 applies bounded automatic retry
  only to definitely failed email sends. Confirmed handoffs are not retried;
  uncertain or exhausted delivery escalates through a separately monitored,
  data-minimized alert to a named recovery owner. Attempts and recovery outcomes
  are audited, and the owner, alert route, timing, and procedure are launch
  validations before real enquiries.
- Request Processing and Communications D-006 sets one proportional rule:
  website enquiry records, protected audit history, and corresponding agency
  email copies are retained for twelve months from acceptance and then deleted.
  One named agency owner is responsible; backups expire through the provider's
  documented cycle; database access is restricted; and private request content
  remains excluded from general logs. Client approval and accurate privacy
  wording remain launch validations rather than a custom privacy system.
- The operator accepted all six Request Processing and Communications decisions
  on 2026-07-30. The final accepted raw ledger must first remain durable on
  `main`; distillation and any later raw-ledger removal follow separately so a
  squash merge cannot discard the accepted source history.
- The operator approved raw-ledger removal after a draft distillation, but final
  consistency review found that D-003 corrections could outlive their original
  request under D-006 per-request deletion. Removal stopped before commit, the
  draft was preserved outside the repository, and D-007 reopened only this
  interaction.
- Request Processing and Communications D-007 requires every correction to store
  a complete corrected request. Each original and correction still expires
  twelve months after its own acceptance; a surviving correction may keep the
  submitted prior opaque reference and an expired-target marker but cannot
  retrieve or reconstruct the deleted request.
- Request Processing and Communications D-008 keeps routine prior-request
  context in the agency business inbox through the current request reference,
  submitted reply email, ordinary search or threading, and the prior reference
  for explicit corrections. Database grouping is not a routine staff view, and
  different-email relationships cannot be manually merged at launch.
- Request Processing and Communications D-009 uses encrypted off-provider
  request-data backups within zero-cost quotas, each expiring no later than
  thirty days after creation. Restores are isolated and reapply expired and
  verified-deleted records before production use; quota pressure alerts the
  owner and triggers client review rather than an automatic paid upgrade.
- On 2026-07-30, the operator accepted Request Processing and Communications
  D-001 through D-009 and authorized verified distillation, removal of the exact
  feature `GRILLING.md` path, automated pull-request delivery, squash merge, and
  merged-branch deletion. The final accepted raw state was preserved on `main`
  before the separately merged distillation/removal change; the durable feature
  authority is now
  `docs/grilling/request-processing-and-communications/DECISIONS.md`.
- Request Processing and Communications distillation verification on 2026-07-30:
  D-001 through D-009 appear exactly once and in order; all feature-contract and
  authority links resolve; formatting and diff checks pass; and independent
  semantic review found no material conflict blocking raw-ledger deletion. Its
  three non-blocking fidelity omissions—initial email-work completion,
  non-confirming Booking Request acknowledgement, and owning-journey persistence
  failure behavior—were added before deletion.
- Content Operations D-001 establishes that the client supplies and explicitly
  approves public content, while a named operator or developer performs the
  technical preview and publication in Sanity. The technical publisher does not
  become responsible for approving business claims. Client approval ownership,
  the technical publisher, and their handoff are Launch Readiness items rather
  than another foundation decision.
- Content Publication Truth D-001 establishes that a useful standalone
  Destination may publish without a published Experience when its approved
  bilingual orientation/detail content and onward paths fulfil the discovery
  promise. A Destination with no published Experiences omits the empty section
  and makes no availability implication. Destination and Experience publication
  lifecycles are independent, while every published Experience still requires a
  valid published Destination relationship.
- Content Publication Truth D-002 establishes relationship-aware withdrawal.
  Withdrawn optional content leaves discovery and its former URL provides a
  generic bilingual recovery path without stale content. Each affected published
  Experience must retain another genuinely valid and approved published
  Destination relationship or also be withdrawn. Required service, request,
  privacy, or legal pages must be replaced or redirected, or their dependent
  journey must be disabled honestly.
- On 2026-07-30, the operator accepted Content Publication Truth D-001 and D-002
  together and selected automatic finalization. The exact raw-ledger removal,
  verified distillation, required-check monitoring, squash merge, and
  merged-branch deletion are authorized through draft pull request #42. This
  does not authorize implementation or automatic commencement of Foundation
  Design.
- Content Publication Truth is distilled into
  `docs/grilling/product-domain-truth/content-publication/DECISIONS.md`. D-001
  and D-002 occur exactly once and in order, preserve the accepted rationale and
  rejected alternatives, align with accepted Catalogue Discovery and Public
  Brand Pages behavior, and retain product invariants without choosing Sanity
  mechanics or technical relationship cardinality. The exact authorized raw
  `GRILLING.md` path is removed, while its final accepted contents and removal
  authorization remain preserved in pull request #42.
- The operator accepted the three-layer classification and dependency sequence.
  `docs/grilling/CLASSIFICATION.md` now carries accepted product/domain truth,
  locked foundation inputs, Launch Readiness items, deferrals, and promotion
  rules without reopening accepted decisions. The former mixed Content
  Operations and Production Operations ledgers are paused and preserved at their
  existing paths rather than deleted.
- Foundation Design has five accepted tracks in dependency order: System
  Boundaries and Domain Representation, Editorial Content Platform,
  Transactional Data Platform, Application Architecture, and Runtime and
  Production Foundations. Before technology-dependent questions, explain the
  relevant components and a concrete project workflow without assuming CMS,
  Sanity, or Neon experience.
- Locked stack inputs now include Next.js, Sanity, Neon PostgreSQL, the latest
  Drizzle release candidate available when implementation begins, Drizzle's
  first-party Zod integration with the latest Zod v4, Nodemailer through the
  agency mail service, and the current Vercel direction with conditional Netlify
  fallback. Exact versions are pinned and verified during later authorized
  implementation rather than reopened in grilling.
- On 2026-07-30, the operator explicitly authorized the first Foundation Design
  track. The accepted System Boundaries and Domain Representation authority is
  `docs/grilling/foundation-design/system-boundaries-and-domain-representation/DECISIONS.md`.
  Related work is finalized through pull request #45.
  D-001 is accepted: Sanity authoritatively verifies current Booking Request
  eligibility, while Neon preserves the stable Experience reference and bounded
  acceptance snapshot. Distinct disabled, withdrawn, and temporary-verification
  failures never claim receipt; exact approved direct-contact fallbacks remain
  Launch Readiness work. D-002 is accepted: the immutable published Sanity
  document ID is the shared Experience identity across Sanity and Neon; titles,
  slugs, and URLs remain editable attributes. D-003 is accepted: each Booking
  Request freezes the bounded localized Experience context and any complete
  indicative-price context shown to the visitor, while excluding the full
  catalogue document. D-004 is accepted: one shared Request envelope has exactly
  one strongly typed journey detail; a wide nullable table and generic catch-all
  payload are excluded. D-005 is accepted: the normalized-email contact
  relationship is derived only from retained immutable Requests, with no
  separate contact entity or indefinite customer directory. D-006 is accepted:
  all valid Destination relationships are equal; there is no primary or role
  taxonomy. D-007 is accepted: a correction stores its intent and submitted prior
  opaque reference after private reference-and-email validation, without a
  foreign key or correction-link entity; routine staff context remains in email.
  No material question remains in this track. On 2026-07-31 the operator accepted
  D-001 through D-007 and authorized verified distillation, exact raw-ledger
  removal, checks, squash merge, feature-branch deletion, and isolated-worktree
  cleanup on PR #45. The final accepted raw ledger and exact deletion
  authorization are preserved in the pull-request record. Independent semantic
  review initially found four editorial fidelity omissions concerning deletion
  residue, inbox notification context, production database access, and delivery
  recovery. After correction, the completed rerun passed with no remaining
  semantic conflicts, weakened obligations, or unresolved fidelity findings. The
  authorized raw `GRILLING.md` path is removed; `DECISIONS.md` is the sole
  accepted authority at this level.
- A separate explicit operator instruction corrected the retained prototype's
  media path: `assets/imgs/` moved to `public/images/`, the approval-gated
  `content/shared/media.json` was removed, and direct localized image records
  now render on Home and Paros in English and Greek. This is a prototype
  correction, not replacement-product architecture authority.
- The operator set the prototype's custom bilingual Home LCP ceiling to 3000
  ms while retaining the Unlighthouse score budgets. Final measured LCP was
  2646.837 ms for `/en` and 2621.026 ms for `/el`.
- On 2026-07-31, the operator accepted Editorial Content Platform D-001 through
  D-006 and selected automatic verified finalization through pull request #48.
  [`docs/grilling/foundation-design/editorial-content-platform/DECISIONS.md`](../../../grilling/foundation-design/editorial-content-platform/DECISIONS.md)
  is the sole accepted authority. It establishes one bilingual Sanity document
  per public content item; explicit repeatable types, controlled singletons, and
  embedded objects; structural validation plus meaning-based agency approval;
  compact item-level evidence metadata; authenticated draft preview and minimal
  withdrawn versions; and cached published content with precise secured-webhook
  revalidation, localized published-only search, bounded fallback expiry, and
  public verification of material changes. The final accepted raw ledger is
  preserved in pull request #48, and the operator authorized removal of the
  exact repository path
  `docs/grilling/foundation-design/editorial-content-platform/GRILLING.md` after
  verified distillation. Acceptance does not authorize Sanity installation,
  configuration, schemas, migration, or application implementation.
- Editorial Content Platform finalization verification on 2026-07-31: pull
  request #48 was read back after its description preserved the exact final
  accepted raw ledger and finalization authorization; the staged structural
  check confirmed one accepted `DECISIONS.md` with D-001 through D-006 exactly
  once and the authorized raw path absent; `git diff --cached --check`, focused
  Prettier, and staged Gitleaks checks passed. `pnpm check:push` then exited `0`:
  the full Gitleaks scan found no leaks; the configured audit gate passed while
  reporting three known findings; formatting, lint, Knip, typecheck, and content
  validation passed; 73 unit tests passed with coverage; the production build
  passed; and Playwright completed with 53 passing and 4 intentionally skipped
  tests. Independent semantic review then identified four fidelity omissions in
  the first distillation; the accepted standalone-Destination and equal-
  relationship inputs, shared-site singleton scope, mandatory publisher preview
  and technical-readiness check, and ordinary-copy evidence exclusion were
  restored. A fresh independent comparison of the corrected `DECISIONS.md`
  against the final accepted raw ledger returned `PASS`.
- On 2026-08-02, the operator accepted Transactional Data Platform D-001 through
  D-009 and authorized verified automatic finalization through pull request #49.
  [`docs/grilling/foundation-design/transactional-data-platform/DECISIONS.md`](../../../grilling/foundation-design/transactional-data-platform/DECISIONS.md)
  is the sole accepted authority. It establishes atomic Request acceptance and
  delivery intents; one shared envelope with three typed detail tables; layered
  public, authority, persistence, and database validation; purpose-specific
  internal, public, contact, and retry identities; a simple private correction
  check without a lock or foreign key; bounded current delivery state with
  append-only attempts and audit; hard Request-root deletion through database
  cascades; Neon WebSocket transactions and separately applied reviewed Drizzle
  migrations; and encrypted logical backups with a short-lived earlier-deletion
  manifest and isolated restore cleanup. The final accepted raw ledger and exact
  authorization to remove
  `docs/grilling/foundation-design/transactional-data-platform/GRILLING.md` are
  preserved in pull request #49. This authority does not permit Neon or Drizzle
  installation, configuration, schema creation, migration execution,
  application implementation, deployment, production-data handling, or
  automatic commencement of Application Architecture.
- During Transactional Data Platform finalization, the operator explicitly
  authorized the small related workflow clarification in
  [`docs/GIT_WORKFLOW.md`](../../../GIT_WORKFLOW.md). Every newly authorized
  coherent unit now defaults to its own isolated worktree under the sibling
  `greek-essence.worktrees/` directory. Git must create and remove the registered
  worktree, the original checkout and unrelated worktrees remain untouched, and
  verified post-merge cleanup removes the remote branch, worktree, local branch,
  and stale worktree metadata.
- Transactional Data Platform finalization verification on 2026-08-02 confirmed
  `DECISIONS.md` contains D-001 through D-009 exactly once and the authorized raw
  path is absent. The pull-request description's embedded raw ledger exactly
  matches the final committed source. A final independent comparison of the
  corrected distillation against that raw source and accepted upstream authority
  returned `PASS`. `docs/grilling/CLASSIFICATION.md` and both Foundation routing
  documents remain structurally correct and require no status edit. Focused
  Prettier, `gitleaks dir --redact --no-banner docs`, and `git diff --check`
  exited `0` before staging; the committed Markdown-only range still requires
  the repository range gate and GitHub read-back before readiness.
- Pull request #49 was subsequently squash-merged and its remote branch,
  deregistered worktree residue, local branch, and stale metadata were removed.
  Local `main` was synchronized with `origin/main`; unrelated worktrees and the
  original checkout's pre-existing changes remained untouched.
- On 2026-08-02, the operator explicitly authorized the Application Architecture
  Foundation Design subject. Work is isolated on branch
  `docs/application-architecture` in the Git-managed sibling worktree
  `../greek-essence.worktrees/application-architecture`. The active source ledger
  is
  [`docs/grilling/foundation-design/application-architecture/GRILLING.md`](../../../grilling/foundation-design/application-architecture/GRILLING.md).
  Independent authority review confirmed D-001 as the first costly-to-reverse
  unresolved seam and found no upstream conflict. Draft pull request #52 is open
  from the task branch. The authorization permits decision grilling and this
  early draft pull request, not implementation, provider configuration,
  migration, deployment, production-data handling, Runtime and Production
  Foundations, Launch Readiness, or another work unit.
- Application Architecture D-001 is accepted. Greek Essence will use one
  domain-centered, feature-first Next.js modular monolith delivered through
  vertical slices, with thin App Router presentation adapters, capability-owned
  application workflows, framework-independent domain behavior where justified,
  narrow server-only infrastructure adapters, and inward source dependencies.
  Shared code remains small; empty layer scaffolding and speculative entities,
  repositories, interfaces, or dependency injection are excluded. This adapts
  the operator-provided reference architecture without importing its conflicting
  travel-domain choices; its documentation protocol remains informative rather
  than part of D-001.
- Application Architecture D-002 is accepted. The three website-owned visitor
  forms use thin Server Actions; Sanity webhooks and later authorized callers
  that require explicit HTTP contracts use thin Route Handlers. Both are public,
  untrusted presentation adapters that invoke application workflows directly and
  never call each other. Greek Essence will not publish a parallel Request API
  without an accepted external consumer. A stale build-specific Server Action
  must claim no receipt and offer a truthful refresh and safe retry that preserves
  entered information where feasible and reuses the same idempotency identity.
- Application Architecture D-003 is accepted with an explicit proportionality
  constraint. The Booking Server Action captures the bounded server-created
  Experience render context in its encrypted closure, validates visitor input
  separately, and invokes a workflow that independently checks current Sanity
  authority before new acceptance. This uses the same Sanity read already needed
  for rendering and creates no provisional record. It does not authorize custom
  signing, historical-revision recovery, temporary snapshot storage, automated
  discrepancy handling, or extra evidentiary machinery; ordinary questions remain
  part of manual agency communication.
- Application Architecture D-004 is accepted. Consultation, Booking, and Contact
  keep explicit journey-owned workflows and share only narrow operations whose
  identical behavior protects accepted invariants. Readable duplicate sequencing
  is preferred over a generic coordinator or central `submitRequest` service until
  abstraction earns its place through demonstrated repeated complexity. The
  operator's magnitude example is five or more workflows sharing roughly three
  hundred or more lines, not a fixed numeric gate. A completed authority and scope
  audit found no further costly-to-reverse Application Architecture seam; exact
  files, types, wiring, tests, and small helper extractions remain implementation
  choices, while runtime and operational concerns stay routed to Runtime and
  Production Foundations. The subject is ready for acceptance review.
- Verification on 2026-07-29: `pnpm format:check` exited `0`; `git diff
--check` exited `0`; all eight expected feature `GRILLING.md` files exist and
  each has one stored next-question section.
- Post-deletion verification on 2026-07-29: `pnpm format:check` and `git diff
--check` both exited `0`; the raw project ledger is absent. Its two remaining
  path mentions are intentional: the reusable protocol names the standard
  project-ledger location, and this handoff records its approved removal.
- Prototype-media verification on 2026-07-29: `pnpm check` exited `0` with 40
  unit tests passing; `pnpm build` exited `0`; the final `pnpm test:e2e` rerun
  exited `0` with 53 passing and 4 intentionally skipped tests; and `pnpm
quality:unlighthouse` exited `0`. Playwright CLI inspection found all
  referenced images decoded, image requests returned `200`, localized alt text
  was present, and representative 320, 390, 834, and 1440 layouts had no
  horizontal overflow.
- Public Brand Pages acceptance verification on 2026-07-29: `pnpm
format:check` and `git diff --check` exited `0` before the approved raw-ledger
  removal. After removal and routing updates, `pnpm check:push` exited `0`: the
  secrets scan found no leaks; the configured audit gate passed while reporting
  three known dependency findings; formatting, lint, Knip, typecheck, and
  content validation passed; 40 unit tests passed with coverage; the production
  build passed; and Playwright completed with 53 passing and 4 intentionally
  skipped tests.
- Catalogue Discovery acceptance verification on 2026-07-29: `pnpm check:push`
  exited `0`. Gitleaks found no leaks; the configured audit gate passed while
  reporting three known dependency findings; formatting, lint, Knip, typecheck,
  and content validation passed; 40 unit tests passed with coverage; the
  production build passed; and Playwright completed with 53 passing and 4
  intentionally skipped tests. `git diff --check` also exited `0` after the
  accepted distillation and approved raw-ledger removal.
- Consultation Request acceptance verification on 2026-07-29: the first `pnpm
check:push` run reached Playwright after all preceding gates passed, then
  exited `1` when one compact-browser navigation case timed out with 52 passing
  and 4 intentionally skipped tests. The exact failed case immediately passed
  alone, and the complete `pnpm test:e2e` rerun exited `0` with 53 passing and 4
  intentionally skipped tests. The final `pnpm check:push` rerun exited `0`:
  Gitleaks found no leaks; the configured audit gate passed while reporting
  three known dependency findings; formatting, lint, Knip, typecheck, and
  content validation passed; 40 unit tests passed with coverage; the production
  build passed; and Playwright completed with 53 passing and 4 intentionally
  skipped tests.

## Next Recommended Action

Present the streamlined two-option Application Architecture completion question
for the exact raw ledger path and existing draft pull request #52: finalize the
grilling subject, or make changes first. The operator does not need to restate the
finalization mechanics.

Completion condition: the operator explicitly selects one of the two outcomes. If
finalization is authorized, follow the grilling protocol's verified distillation,
exact-path deletion, pull-request completion, merge, synchronization, and cleanup
sequence without treating it as implementation or successor-subject authorization.
After completion, recommend the next dependency-ordered subject and wait for
explicit approval before creating its branch, worktree, ledger, or draft PR.

## Done When

The preview-release requirements and all confirmed feature grills are accepted,
material client questions are isolated, replacement architecture is promoted
into canonical technical authority, approved implementation work has replaced
the prototype without relying on archived assumptions, and temporary rebaseline
state has been reconciled or removed.

## Constraints

- Do not further remove or reorganize the runnable prototype before its
  replacement architecture and coordinated path changes are approved.
- Do not treat prototype material as current product or architecture authority.
- Do not treat anything under `docs/archive/showcase-prototype-v0/` as current
  authority, even when an archived document describes itself as approved or
  authoritative.
- Do not install or configure Sanity, Neon, Drizzle, Nodemailer, or another
  backend dependency until a later explicit implementation task authorizes it.
- Obtain user approval before changing active paths.
- Vercel's commercially eligible zero-cost launch use must be proven in Launch
  Readiness. Failure of that mandatory gate routes an explicit Foundation Design
  topology review using the accepted Netlify fallback direction. Any paid host
  upgrade requires visitor-demand evidence and explicit client approval.
- The operator's personal Gmail may receive only synthetic controlled test
  enquiries; it must not receive real public visitor data.

## Related Documents

- [Operation](OPERATION.md)
- [Layer 2 migration principles](../../NEXTJS_LAYER_2_MIGRATION.md)
- [Layer 2 inventory](../../NEXTJS_LAYER_2_INVENTORY.md)
- [Archived prototype baseline](../../../archive/showcase-prototype-v0/README.md)
- [Retention plan](RETENTION_PLAN.md)
- [Architecture proposal](ARCHITECTURE_PROPOSAL.md)
- [Expanded requirements intake](REQUIREMENTS_INTAKE.md)
- [Decision register](DECISION_REGISTER.md)
- [Requirements Batch 01 synthesis](REQUIREMENTS_BATCH_01.md)
- [Public preview release validation](PREVIEW_RELEASE_VALIDATION.md)
- [Accepted project decisions](../../../grilling/DECISIONS.md)
- [Accepted Public Brand Pages decisions](../../../grilling/public-brand-pages/DECISIONS.md)
- [Accepted Catalogue Discovery decisions](../../../grilling/catalogue-discovery/DECISIONS.md)
- [Accepted Consultation Request decisions](../../../grilling/consultation-request/DECISIONS.md)
- [Accepted Booking Request decisions](../../../grilling/booking-request/DECISIONS.md)
- [Accepted Request Processing and Communications decisions](../../../grilling/request-processing-and-communications/DECISIONS.md)
- [Feature grilling router](../../../grilling/README.md)
- [Grilling protocol](../../../grilling/protocol.md)
