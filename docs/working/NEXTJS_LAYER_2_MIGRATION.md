# Documentation Architecture and Migration Strategy Review

**Review status:** completed 2026-08-02. This is an investigation and planning
artifact. It does not promote candidate documents, replace accepted grilling
decisions, authorize source moves, or authorize implementation.

The companion current-code inventory is
[`NEXTJS_LAYER_2_INVENTORY.md`](NEXTJS_LAYER_2_INVENTORY.md).

## 1. Executive recommendation

Adopt the candidate documentation system's _operating ideas_, not its document
set unchanged. Its thin index, explicit authority categories, ADR discipline,
assumption register, documentation-update rules, and focused runbook pattern
are good fits for a small AI-heavy team. They must be revised to preserve the
repository's already accepted grilling authority and to remove unsupported
customer/quote/booking/payment assumptions.

Choose **Option C — merge the migrations**:

- finish this active evaluation safely (this report), but do not execute the
  old `features/showcase` source migration;
- retain its compatible code-placement and dependency rules as inputs to the
  accepted Application Architecture; and
- transition documentation incrementally after the operator approves the
  revised authority model, using accepted grilling decisions as source material.

The single most important next action is to obtain an operator decision
recording Option C, with the explicit rule that the old Layer 2 move map is
superseded before any application paths move. That decision should then route
the first documentation-transition slice; it must not start implementation.

## 2. Current-state findings

### Application architecture

The runtime is a root-level Next.js App Router prototype, not the candidate
modular monolith:

- [`../../app/[locale]/layout.tsx`](../../app/[locale]/layout.tsx) statically
  provides `en` and `el`, initializes `next-intl`, and supplies global metadata.
  [`../../proxy.ts`](../../proxy.ts) redirects `/` to `/en` and applies locale
  middleware.
- [`../../app/[locale]/page.tsx`](../../app/[locale]/page.tsx) and
  [`../../app/[locale]/destinations/paros-antiparos/page.tsx`](../../app/[locale]/destinations/paros-antiparos/page.tsx)
  are async Server Components that compose content-backed sections and localized
  metadata. [`../../app/[locale]/quality-lab/page.tsx`](../../app/[locale]/quality-lab/page.tsx)
  is an internal quality fixture.
- Root `components/` holds a branded header/footer, Home and Paros page
  sections, a shared CTA/media component, and one Base UI button primitive.
  [`../../components/layout/site-header.tsx`](../../components/layout/site-header.tsx)
  is a Client Component for the menu; the quality fixture also has isolated
  client components. Everything else is server-rendered by default.
- [`../../lib/content.ts`](../../lib/content.ts) imports local JSON, validates it
  with the Zod schema in [`../../content/schemas/showcase.ts`](../../content/schemas/showcase.ts),
  and checks bilingual parity at module load. [`../../lib/routes.ts`](../../lib/routes.ts)
  is a client-safe prototype route/CTA contract; [`../../lib/utils.ts`](../../lib/utils.ts)
  is the `cn` utility.
- There are no Server Actions, Route Handlers, database code, Drizzle migrations,
  Sanity integration, form-processing code, mail delivery, or dynamic business
  APIs. `package.json` confirms that those dependencies are absent.

The only current cross-route dependency is showcase presentation and content;
there is no demonstrated domain module. `app/[locale]/quality-lab` and its
toggle are a testing aid, not product architecture.

### Product and migration reality

Current authority says the replacement is a public preview with editable
catalogue content, private request records, consultation/booking-request/general
contact journeys, manual agency follow-up, and deliberately non-confirming
booking-request language. It expressly excludes customer accounts, confirmed
bookings, payments, supplier workflows, a private dashboard, live availability,
and online cancellation/refunds for launch
([`../grilling/DECISIONS.md`](../grilling/DECISIONS.md),
[`../grilling/booking-request/DECISIONS.md`](../grilling/booking-request/DECISIONS.md)).

Sanity, Neon PostgreSQL, Drizzle, Next.js, Vercel-direction hosting, and agency
SMTP are locked Foundation inputs. The accepted System Boundaries decision
requires Sanity to verify current Experience eligibility and Neon to retain a
stable Sanity root ID plus a bounded request-time snapshot; accepted editorial
decisions define bilingual content, secure preview, publication, withdrawal,
and cache revalidation. They do **not** authorize installation or source work
([`../grilling/foundation-design/system-boundaries-and-domain-representation/DECISIONS.md`](../grilling/foundation-design/system-boundaries-and-domain-representation/DECISIONS.md),
[`../grilling/foundation-design/editorial-content-platform/DECISIONS.md`](../grilling/foundation-design/editorial-content-platform/DECISIONS.md)).

The earlier Layer 2 migration is not partially implemented. Its only artifacts
are the general brief and old inventory in this directory, plus a longer source
brief under `work-items/prototype-rebaseline/sources/`. No code has moved, so
no migration work needs to be unwound and no intermediate architecture needs to
be maintained.

### Current documentation system

Useful, authoritative material to preserve:

- [`../README.md`](../README.md) correctly explains archive, working-state, and
  authority boundaries.
- [`../PRODUCT_COLLABORATION.md`](../PRODUCT_COLLABORATION.md),
  [`../PROJECT_ACTORS.md`](../PROJECT_ACTORS.md),
  [`../DEVELOPMENT_STANDARDS.md`](../DEVELOPMENT_STANDARDS.md),
  [`../QUALITY_GATES.md`](../QUALITY_GATES.md), [`../AGENT_TOOLING.md`](../AGENT_TOOLING.md),
  and [`../GIT_WORKFLOW.md`](../GIT_WORKFLOW.md) are concise owner documents
  with strong operational guardrails.
- The `grilling/` router, protocol, classification, accepted `DECISIONS.md`
  files, and request-processing contracts distinguish settled product truth,
  Foundation Design, and launch evidence well. This is stronger than the
  candidate's generic “current-state/domain/ADR” split for this project.
- `docs/working/` accurately marks temporary operational documents and
  evaluation artifacts; `docs/archive/showcase-prototype-v0/` preserves useful
  prototype history without letting it become replacement authority.

Weaknesses to address, without losing history:

- Orientation is fragmented: a new agent must traverse root `AGENTS.md`,
  `docs/README.md`, `NEXT.md`, an active work-item handoff, the grilling
  protocol, classification, and several decisions before it can tell present
  fact from intended state.
- Current state, approved foundation truth, working drafts, withdrawn proposals,
  and prototype archive are well labelled but spread across several roots.
- The two Layer 2 migration briefs duplicate placement rules and differ in
  details such as required feature barrels. Their `showcase` mapping describes
  an intended structural future, rather than current replacement architecture.
- The existing system does not yet have a concise replacement-product
  “current architecture” page, data-ownership map, or assumption/open-question
  register. Accepted Foundation decisions now provide the source material, but
  promotion into canonical summaries remains a separately authorized gap.
- The historical prototype tree is intentionally very large and granular. It
  should remain archived, not be deleted or silently treated as active reading.

## 3. Proposed-documentation assessment

### Strengths worth preserving

The proposal is readable and easy for both humans and agents to traverse:

- `docs/index.md` provides a small start path and a meaningful document map.
- `documentation-protocol.md` offers useful ownership, update, link, and
  duplication-control rules. Its instruction to preserve uncertainty explicitly
  is particularly valuable for AI-assisted work.
- ADR templates and the “do not silently rewrite accepted ADRs” rule are sound.
- Assumption templates and `open-questions.md` provide a lightweight place for
  unverified decisions, which complements the current grilling process.
- The presentation/application/domain/infrastructure vocabulary, focused module
  folders, strict input-validation boundary, and explicit Sanity/PostgreSQL
  ownership are pragmatic principles when real business behavior exists.
- The runbook template appropriately postpones exact operations until a real
  owner and provider configuration exist.

### Weaknesses and conflicts

- Candidate ADRs `0001`–`0004` are labelled **Accepted**, and architecture/data
  pages say `status: active`, although the proposal root correctly says it is
  non-authoritative. That dual signal is unsafe and directly conflicts with
  current authority rules.
- `handbook/system-in-five-minutes.md`, `domain/modules.md`, lifecycle pages,
  data ownership, testing strategy, and implementation workflow normalize a
  customer → quote → booking → payment system. That scope is deferred by the
  accepted Public Preview Release rather than merely unknown.
- `architecture/overview.md` asserts a `src/modules/{catalog,customers,...}`
  tree that does not exist, conflicts with accepted capability boundaries, and
  hard-codes exact source structure that Application Architecture deliberately
  leaves to bounded implementation design.
- The generic data documents blur current preview truth with later commercial
  operations. For example, current accepted data modeling is a private immutable
  Request envelope and bounded Experience snapshot, not customers, travelers,
  quote items, supplier obligations, payments, capacity, or reservation holds.
- It duplicates parts of current policies: quality gates, coding rules, agent
  guidance, security direction, technical stack choices, terminology, and
  operational procedures. Two competing agent entry points would reduce rather
  than improve AI reliability.
- It assumes React Hook Form, TanStack Query, general “ports/adapters,” and a
  full layered module shape before actual need. These are reasonable optional
  tools, but are unnecessary ceremony for a first public-content or request
  slice.
- The two included runbooks are premature placeholders. They should not be
  promoted until Runtime and Production Foundations supplies exact access,
  backup, monitoring, and recovery facts.

### Recommended treatment of candidate concepts

| Candidate files/concepts                                                               | Treatment                        | Reason                                                                                                                             |
| -------------------------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `docs/index.md`, `documentation-protocol.md`                                           | **Rewrite and merge**            | Use their navigability/update discipline, but retain the current authority order and grilling-to-canonical promotion rule.         |
| ADR index/template/rules                                                               | **Keep, then adapt**             | Adopt only after deciding how ADRs coexist with accepted `DECISIONS.md`; do not duplicate existing decisions as new accepted ADRs. |
| Assumption template/index and open-question concept                                    | **Keep, then adapt**             | Add a small cross-cutting register after defining its hand-off to grilling ledgers and accepted decisions.                         |
| `architecture/dependency-rules.md` and `nextjs-boundaries.md`                          | **Merge**                        | Preserve as future technical design constraints; make Server Actions conditional and retain route-handler use for webhooks.        |
| `architecture/overview.md`, `module-structure.md`, testing strategy                    | **Rewrite/delay**                | Replace the speculative modules and end-to-end journey with the accepted preview capability map and actual test scripts.           |
| Sanity/PostgreSQL/cross-system/snapshot documents                                      | **Merge and rewrite**            | Source them from accepted Foundation decisions; describe Requests and Experience snapshots now, not quotes/payments.               |
| Customer, traveler, quote, booking, payment, supplier, document modules and lifecycles | **Archive as future hypotheses** | They require a later product decision; do not promote or implement them for the preview.                                           |
| Availability document                                                                  | **Delay**                        | The preview explicitly makes no live availability claim. Retain as later-domain guidance only.                                     |
| Form-library guidance                                                                  | **Merge minimally**              | Keep native-form-first and runtime validation; defer library choice until an authorized form slice requires it.                    |
| Candidate runbooks                                                                     | **Delay**                        | Add actual procedures only after provider/runtime evidence and named owners exist.                                                 |

## 4. Architecture-fit assessment

A domain-centered, feature-first modular monolith delivered through vertical
slices is now the accepted replacement architecture, not the current runtime
shape or permission to implement it. One Next.js deployable is appropriate for
the team and avoids microservice operational cost. Compatible dependency rules
are valuable for keeping Sanity, Neon, mail, and Next.js details away from
business rules where real behavior or testing seams justify them.

For the Public Preview, use vertical slices by accepted capability rather than
by speculative enterprise entity:

| Practical first modules/slices                           | Why they fit                                                                                                           | Initial layering needed                                                                                           |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Public content/catalogue discovery                       | Sanity owns bilingual editable content and publication.                                                                | Server-side query/validation/mapping boundary plus route presentation; a separate rich domain layer is optional.  |
| Request processing and communications                    | It has accepted invariants for immutability, exact retry, opaque references, email delivery, retention, and snapshots. | Small domain/application core, Drizzle/SMTP adapters, and route/action presentation boundary are justified.       |
| Consultation request / booking request / general contact | They have distinct visitor scope but share accepted request processing.                                                | Thin form/presentation slices that call shared request-processing use cases; do not create a generic form domain. |

Do **not** pre-create `customers`, `travelers`, `quotes`, `bookings`,
`payments`, `suppliers`, or `documents` modules. The preview's accepted contact
relationship is derived from retained immutable Requests, expressly without a
separate customer entity or public account. Confirmed booking and payment
lifecycles are deferred.

Sanity/PostgreSQL ownership is compatible after revision: Sanity is the
editable public/categorical source, Neon is the private transactional source,
and accepted requests retain only a stable Experience ID and bounded immutable
visitor-visible snapshot. What is not yet practical is forcing every display
component through domain/application/infrastructure folders; a server-only
content adapter beside a public-content module and thin route composition is
enough initially.

Adopt immediately: a one-deployable application, narrow module ownership,
route composition, Server Components by default, explicit server-only
boundaries, runtime validation, minimal `shared/`, and no framework types in
business rules. Delay: complete Clean/Hexagonal folder quadrants, generic ports,
domain events, query cache, RHF, availability/locking, financial types, and
future commercial modules.

## 5. Migration strategy comparison

| Option                                                   | Benefits                                                                                                                                         | Costs and risks                                                                                                                                                                                          | Evidence-based assessment                                                                                |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| A. Complete the current Layer 2 migration first          | Would tidy the prototype and exercise route/feature/shared rules.                                                                                | Creates `features/showcase` immediately before replacing the prototype; consumes verification time; yields paths that future modules will not use.                                                       | Low value. No source move has occurred, so there is no sunk implementation cost to recover.              |
| B. Stop after active work is safe, then replace it       | Avoids a prototype-only source move and enables a clean new design.                                                                              | Throws away good generic rules; a wholesale docs replacement risks losing accepted decision provenance and creates a large review surface.                                                               | Safer than A for code, but unnecessarily discontinuous for documentation.                                |
| C. Preserve compatible work and redirect unfinished work | Keeps narrow placement, incremental validation, and server/client boundaries; avoids a double source migration; preserves all authority/history. | Requires a clearly documented transition so old and new language cannot both be active.                                                                                                                  | **Recommended.** The reusable part is guidance, not code. No data migration or rollback is needed today. |
| D. Full rewrite now                                      | Could create a clean tree quickly.                                                                                                               | High risk of copying unsupported future assumptions into “current” docs, losing traceability, and replacing accepted Transactional Data and Application Architecture boundaries with speculative detail. | Not justified.                                                                                           |

Current test coverage and code stability support this choice: the static
prototype is well guarded, but it cannot validate a future source reorganization
or unimplemented integrations. The absence of data means there is no data
migration risk today; the material risk is documentation authority drift, not
technical rollback.

## 6. Recommended migration path

### Phase 0 — Ratify and freeze the transition boundary

- **Goal:** make Option C and the authority model explicit before another agent
  interprets candidate material as active truth.
- **Scope:** documentation decision only; no application files.
- **Affected paths:** active evaluation work-item, this review, and a future
  documentation-transition decision artifact selected by the operator.
- **Reusable work:** current `docs/README.md` authority map, grilling protocol,
  and generic Layer 2 placement/dependency principles.
- **Quality gates:** Markdown-only Prettier and Gitleaks; link audit.
- **Complete when:** the operator has approved Option C and named the owner and
  first transition slice.
- **Main risk:** silently treating candidate ADR status or frontmatter as
  accepted authority.

### Phase 1 — Establish a thin canonical documentation front door

- **Goal:** reduce initial navigation while preserving the established authority
  hierarchy and all accepted decisions.
- **Scope:** add/revise only routers and protocol language; link to existing
  decision documents instead of duplicating them.
- **Affected paths:** future canonical `docs/index.md` or an explicit rename of
  `docs/README.md`; root `AGENTS.md` only if separately authorized; current
  routers and candidate index/protocol as source material.
- **Reusable work:** candidate index, protocol, ADR and assumption templates.
- **Quality gates:** Markdown-only checks and a repository link-target audit.
- **Complete when:** a new agent can identify (a) current runtime, (b) accepted
  product/Foundation decisions, (c) working state, (d) archive, and (e) open
  questions without reading non-authoritative candidate files.
- **Main risk:** creating a second authority hierarchy. Mitigate by retaining
  current precedence and explicitly linking the grilling promotion rule.

### Phase 2 — Promote only settled current-state summaries

- **Goal:** create concise current-state pages for public content, request
  processing, data ownership, and technical boundaries.
- **Scope:** summarize accepted decisions exactly once and link back to their
  authoritative `DECISIONS.md`/contracts. Do not copy candidate commercial
  workflows.
- **Affected paths:** future canonical architecture/data/domain pages; accepted
  grilling records remain unchanged.
- **Reusable work:** candidate architecture/data document shapes; accepted
  System Boundaries, Editorial Content Platform, Transactional Data Platform,
  Application Architecture, Catalogue Discovery, Booking Request, and Request
  Processing decisions.
- **Quality gates:** Markdown-only checks; semantic review against each linked
  accepted decision; link audit.
- **Complete when:** the public-preview state and its deferred scope are
  accurately discoverable, with each summary having one source of authority.
- **Main risk:** summaries weakening exclusions or presenting bounded technical
  mechanics as accepted product or architecture decisions.

### Phase 3 — Finish Runtime and Production Foundations before source restructuring

- **Goal:** resolve Runtime and Production Foundations through the current
  grilling process without reopening the accepted upstream Foundation subjects.
- **Scope:** decision work only until explicit implementation contracts exist.
- **Affected paths:** `docs/grilling/foundation-design/` and its work-item
  routing; no source moves as a side effect.
- **Reusable work:** Layer 2 constraints and revised architecture pages.
- **Quality gates:** the applicable documentation checks and required semantic
  reviews specified by the grilling protocol.
- **Complete when:** runtime placement, deployment topology, migration and
  recovery operations, secrets, scheduling, observability, rollback, and hosting
  fallback responsibilities are accepted enough to bound later implementation.
- **Main risk:** encoding unverified vendor or operational facts. Route such
  gaps to Launch Readiness rather than filling them with generic documentation.

### Phase 4 — Implement one reversible vertical slice

- **Goal:** introduce only the foundation needed for one real preview workflow,
  likely published catalogue access or one request journey, as selected by an
  explicit task contract.
- **Scope:** a coherent module plus thin route composition, not a project-wide
  move from `components/` to `modules/`.
- **Affected paths:** determined by the authorized Application Architecture
  decision; likely a module-specific server boundary, app route composition,
  tests, and configuration. Existing prototype paths remain until a contracted
  replacement makes them obsolete.
- **Reusable work:** strict TypeScript, i18n boundaries, content validation,
  test infrastructure, security headers, and generic Layer 2 dependency rules.
- **Quality gates:** full task/range-applicable gates in
  [`../QUALITY_GATES.md`](../QUALITY_GATES.md), including focused integration
  tests and provider-specific checks where applicable.
- **Complete when:** the slice meets accepted invariants, has clear ownership,
  passes repository gates, and documents its live state and remaining
  assumptions.
- **Main risk:** coupling current editable content to immutable Requests or
  treating a saved request as a confirmed booking.

### Phase 5 — Retire superseded planning material deliberately

- **Goal:** leave one discoverable documentation system after multiple promoted
  slices prove its maintenance cost.
- **Scope:** reclassify duplicate proposals and working briefs only after their
  content and inbound links have been reconciled.
- **Affected paths:** `docs/new-proposed-docs/`, working Layer 2 artifacts, and
  work-item source records—not accepted decisions or prototype history.
- **Reusable work:** approved candidate templates and revised canonical pages.
- **Quality gates:** Markdown-only checks, link audit, and a provenance review.
- **Complete when:** every retired file is either archived with rationale or
  removed under explicit path-level approval, and no active route links to it.
- **Main risk:** deleting useful context or accidental authority loss. Default to
  archive until an operator authorizes a named deletion.

## 7. Documentation transition plan

The classifications below are transition recommendations, not file operations.
“Move” means relocate only after the replacement destination and links are
approved. “Delete” is intentionally empty because the repository requires
explicit path-level approval and no current evidence justifies loss of history.

| Classification | Documents / groups                                                                                                                                                                                                                                                 | Transition treatment                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Keep**       | `docs/README.md`; `PROJECT_ACTORS.md`; `PRODUCT_COLLABORATION.md`; `DEVELOPMENT_STANDARDS.md`; `QUALITY_GATES.md`; `AGENT_TOOLING.md`; `GIT_WORKFLOW.md`; `grilling/README.md`, `protocol.md`, `CLASSIFICATION.md`, accepted `DECISIONS.md`, and request contracts | Retain as the current authority and link to it from any new index. These own policy or accepted decisions.                                                                                  |
| **Keep**       | `docs/archive/showcase-prototype-v0/`                                                                                                                                                                                                                              | Keep as an explicitly historical archive. Do not merge its detailed prototype requirements into current docs.                                                                               |
| **Keep**       | Active work-item `NEXT.md` files and `docs/working/work-items/prototype-rebaseline/`                                                                                                                                                                               | Keep as temporary routing/evidence until each work item is completed under its own rules.                                                                                                   |
| **Move**       | Candidate ADR and assumption templates; candidate index/protocol concepts                                                                                                                                                                                          | After approval, move/adapt the reusable templates into canonical paths. Do not move candidate “Accepted” ADR instances as accepted records.                                                 |
| **Merge**      | Candidate `architecture/dependency-rules.md`, `nextjs-boundaries.md`, `validation-and-forms.md`, and `security-baseline.md`                                                                                                                                        | Merge their compatible principles into current development/technical documents after relevant Foundation tracks accept exact rules.                                                         |
| **Merge**      | Candidate Sanity/PostgreSQL/ownership/snapshot/cross-system files                                                                                                                                                                                                  | Merge only their structure with accepted preview facts: Sanity content, Neon private Requests, stable Experience identity, bounded snapshots, bilingual publication, and truthful failures. |
| **Rewrite**    | Candidate `docs/index.md`, `documentation-protocol.md`, `handbook/system-in-five-minutes.md`, `architecture/overview.md`, `module-structure.md`, testing strategy, and development workflow                                                                        | Remove false present-tense claims, retain the active authority hierarchy, and make the first public-preview slice—not quotes/payments—the example workflow.                                 |
| **Rewrite**    | `docs/working/NEXTJS_LAYER_2_INVENTORY.md` and `NEXTJS_LAYER_2_MIGRATION.md`                                                                                                                                                                                       | This review rewrites their purpose from a prototype move plan into evidence and strategy. Future approved technical design should supersede them rather than reusing `showcase` paths.      |
| **Archive**    | Candidate customer/traveler/quote/booking/payment/supplier/document module and lifecycle files; availability guidance; draft runbooks                                                                                                                              | Preserve as clearly labelled post-preview hypotheses only if the operator wants them; otherwise retain them in the evaluation artifact until final documentation cleanup.                   |
| **Archive**    | `work-items/prototype-rebaseline/sources/` and withdrawn `ARCHITECTURE_PROPOSAL.md` at work-item closure                                                                                                                                                           | Preserve source provenance and withdrawn reasoning; do not let it remain in a primary reading path.                                                                                         |
| **Delete**     | None now                                                                                                                                                                                                                                                           | No deletion is recommended before an approved replacement, link reconciliation, historical-retention decision, and explicit path-level authorization.                                       |
| **Unclear**    | `docs/DAIRY.md`, older operational working records, and whether candidate proposal files remain as a review fixture after adoption                                                                                                                                 | Decide during Phase 5 based on audit/history needs and whether the merged pull request supplies durable evidence.                                                                           |

Missing project-specific documents to add only when their inputs are settled:

- a compact **Public Preview current-state** page that distinguishes the running
  prototype from the accepted replacement;
- an **authority/promotion map** from grill → accepted decision/contract →
  canonical summary → bounded task contract;
- a **request-processing data and lifecycle** page grounded in accepted
  immutability, retry, retention, and email rules;
- a **Sanity–Next.js–Neon boundary** page grounded in accepted identity,
  snapshots, preview, withdrawal, cache, and webhook rules;
- a **runtime/operations index** only after named providers, access, recovery,
  monitoring, and launch evidence are known.

## 8. Open questions and assumptions

The following cannot be concluded from the repository and must not be guessed:

1. Which canonical documentation root/name the operator prefers (`docs/index.md`
   versus retaining `docs/README.md` as the front door), and who owns updates.
2. Whether the operator wants candidate long-horizon commercial material kept as
   an archive or discarded after its useful principles are extracted.
3. The first authorized implementation slice and therefore the first real
   module name; current evidence supports public content/catalogue and request
   processing, but does not select their delivery order.
4. Exact implementation schema, table, index, query, migration, and test-fixture
   design within the accepted Transactional Data Platform boundaries.
5. Exact source directories, import aliases, capability contracts, composition
   mechanics, and proportional dependency-rule enforcement within the accepted
   Application Architecture boundaries.
6. Exact Sanity schema, Studio/preview/webhook configuration, cache APIs/tags,
   fallback expiry, and production ownership. The accepted editorial outcomes
   deliberately leave these as bounded technical design work.
7. Agency and qualified-reviewer facts: public content, English/Greek approval,
   privacy/legal wording, SMTP readiness, provider account ownership, data
   region, backups, recovery ownership, and commercially eligible zero-cost
   hosting.
8. Any later quote, payment, confirmed booking, supplier, traveler, dashboard,
   or availability workflow. These are not “missing implementation details” of
   the preview; they require new product decisions.

## Verification record

This review was based on direct repository inspection. Before this report was
written, `git status --short` returned no changes on `docs/migration-v4`. The
runtime was not modified. The Markdown-only verification for the two report
files is recorded with its exact command and exit status in the delivery
report.
