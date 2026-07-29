# Requirements Batch 01 Synthesis

## Status

Normalized from three operator-authored, agent-assisted working drafts on
2026-07-29. The drafting agent had repository context, but the client has not
read or approved the documents. Requirements are **reported** and architecture
choices are **candidates**. They form a provisional internal planning baseline,
especially for the preview release, while the operator resolves conflicts and
selectively validates material product decisions with the client.

## Sources

- [`sources/07_PROJECT_ROADMAP.md`](sources/07_PROJECT_ROADMAP.md)
- [`sources/06_DOMAIN_ARCHITECTURE.md`](sources/06_DOMAIN_ARCHITECTURE.md)
- [`sources/NEXTJS_LAYER_2_MIGRATION.md`](sources/NEXTJS_LAYER_2_MIGRATION.md)

The files are byte-for-byte copies of the provided source material. They are
preserved as evidence and are not implementation authority by location alone.

## Reported Requirements

| ID | Outcome or constraint | Release | Source | Status |
| --- | --- | --- | --- | --- |
| REQ-001 | Deliver a polished public Phase 1 release by the end of August for real visitors and enquiries | Phase 1 | Roadmap §§1, Phase 1; SRC-005 | Operator-confirmed |
| REQ-002 | Use Sanity as the owner of public editorial and catalogue content | Phase 1 | Roadmap §2; Domain §2 | Reported |
| REQ-003 | Use Supabase as the owner of transactional and operational data | Phase 1 | Roadmap §2; Domain §2 | Reported |
| REQ-004 | Use Drizzle for transactional schema access and reproducible migrations | Phase 1 | Roadmap M1 | Reported |
| REQ-005 | Organize cross-route business code into features, route-local code under `app/`, and domain-neutral code under `shared/` | Foundation | Layer 2 brief | Reported |
| REQ-006 | Keep Phase 1 customer interactions unauthenticated | Phase 1 | Roadmap §2 | Reported |
| REQ-007 | Prefer Route Handlers for business operations and reserve Server Actions for UI-oriented interactions | All | Roadmap §2; Domain §9 | Reported |
| REQ-008 | Protect public operations with appropriate validation, rate limiting, idempotency, and security controls | All | Roadmap §2; Domain §9 | Reported |
| REQ-009 | Model Marketing, Catalogue, Consultation, Booking, and CRM as distinct business contexts | All | Domain §3 | Reported |
| REQ-010 | Manage homepage, destinations, experiences, accommodation, attractions, interests, articles, FAQ, testimonials, navigation, footer, settings, and SEO through Sanity | Phase 1 | Roadmap M2/M4; Domain §4 | Reported |
| REQ-011 | Support Sanity draft preview, essential-content validation, relationships, and reusable query modules | Phase 1 | Roadmap M4 | Reported |
| REQ-012 | Publish Home, About, Contact, destination catalogue/detail, experience catalogue/detail, consultation, launch legal pages, and optional articles | Phase 1 | Roadmap M5 | Reported |
| REQ-013 | Search catalogue text and filter by destination, experience type, and interest where ready | Phase 1 | Roadmap M5 | Reported |
| REQ-014 | Create or reuse a Customer and persist a Consultation from an unauthenticated request | Phase 1 | Roadmap M6; Domain §§5–8 | Reported |
| REQ-015 | Capture consultation identity, contact, locale, travel timing, party, budget, interests, notes, and consent without exposing personal data in logs or URLs | Phase 1 | Roadmap M6 | Reported |
| REQ-016 | Handle duplicate consultation submissions safely and notify both agency and customer | Phase 1 | Roadmap M6 | Reported |
| REQ-017 | Create or reuse a Customer and persist a Booking Request referencing the correct Sanity Experience | Phase 1 | Roadmap M7; Domain §§5–8 | Reported |
| REQ-018 | Present a Booking Request as an expression of intent, never a confirmed booking | Phase 1 | Roadmap M7; Domain §§5, 11 | Reported |
| REQ-019 | Notify agency and customer after a valid booking request and continue the workflow manually | Phase 1 | Roadmap M7 | Reported |
| REQ-020 | Keep Sanity content and Supabase business data non-duplicative while allowing safe external content references | All | Roadmap M2; Domain §§1–2, 11 | Reported |
| REQ-021 | Provide CI, preview deployments, production deployment, reproducible migrations, tests, security, accessibility, performance, monitoring, documentation, and launch checks | Phase 1 | Roadmap M1/M8 | Reported |
| REQ-022 | Add paid consultation, questionnaire, scheduling, and full booking confirmation only after Phase 1 | Full MVP | Roadmap M9–M12 | Reported |
| REQ-023 | Make payment handling provider-independent, verified, idempotent, auditable, and refund-aware | Full MVP | Roadmap M9; Domain §§5–7, 11 | Reported |
| REQ-024 | Keep questionnaire access secure without requiring an account and prevent cross-customer access | Full MVP | Roadmap M10 | Reported |
| REQ-025 | Prevent scheduling before successful payment and prevent double booking with correct time-zone behavior | Full MVP | Roadmap M11; Domain §§7, 11 | Reported |
| REQ-026 | Keep Booking Request and confirmed Booking distinct, with traceable state, pricing, terms, communications, and payment association | Full MVP | Roadmap M12 | Reported |
| REQ-027 | Preserve explicit workflow state, diagnostics, audit information, manual recovery, and duplicate-event protection for critical operations | Full MVP | Roadmap M13/M14 | Reported |

## Candidate Domain Ownership

| Owner | Candidate responsibility |
| --- | --- |
| Sanity / Marketing | Pages, branding, SEO, articles, homepage, navigation, settings |
| Sanity / Catalogue | Experiences, destinations, accommodation, attractions, interests, FAQ, media relationships |
| Supabase / CRM | Customer, Contact Message, optional Newsletter Subscriber |
| Supabase / Consultation | Consultation, Payment, Meeting, Questionnaire |
| Supabase / Booking | Booking Request in Phase 1; confirmed Booking in the Full MVP |

## Conflicts and Clarifications Required

1. **Phase 1 consultation state:** Phase 1 explicitly excludes payment,
   questionnaire, and scheduling, while the domain state machine begins at
   `Pending Payment`. Define a Phase 1-compatible request state and its later
   transition into the paid workflow.
2. **Booking Request terminal state:** The domain state machine uses
   `Confirmed`, but the roadmap and invariant say a Booking Request is not a
   confirmed Booking. Prefer an unambiguous state such as `accepted` or
   `converted`, with a separate Booking entity in the Full MVP.
3. **Payment cardinality:** “Consultation has one Payment” does not explain
   retries, failed attempts, replacement sessions, partial refunds, or multiple
   provider events. Confirm whether the domain needs one logical payment with
   many attempts/events or multiple payment records.
4. **Customer reuse:** Define matching, normalization, concurrency, consent
   history, and whether email alone is sufficient to reuse a Customer.
5. **Sanity reference durability:** Define behavior when a referenced
   Experience is edited, unpublished, renamed, or deleted after a Booking
   Request is stored. Decide which immutable identifiers and snapshots are
   required transactionally.
6. **Experience scope:** The domain document lists Cruise and Transfer, while
   the Phase 1 roadmap limits initial types to Tour, Activity, and Travel
   package. Confirm Cruise and Transfer as deferred or included.
7. **Search filters:** The domain document adds accommodation, duration,
   difficulty, and price filters beyond the Phase 1 search contract. Clarify
   release ownership and where price data lives without duplicating
   transactional pricing.
8. **Public catalogue scope:** Sanity includes Accommodation and Attraction,
   but the Phase 1 public-route list does not clearly include their listing or
   detail pages. Confirm whether they are supporting content only.
9. **Newsletter scope:** Newsletter Subscriber is conditional in the roadmap
   but present in the CRM domain. Confirm inclusion, consent model, and delivery
   provider.
10. **Authentication:** Phase 1 is unauthenticated and future authentication is
    mentioned, but agency/editor authentication and operational interfaces are
    not defined. Clarify Sanity Studio access and any Supabase-backed staff UI.
11. **Layer 2 location:** The provided migration brief prefers `src/features/`
    and `src/shared/` when `app/` is root-level, while the repository's earlier
    working proposal chose root `features/` and `shared/`. Choose one source-root
    strategy before moving code.
12. **Feature public APIs:** The provided migration brief mandates an `index.ts`
    for every feature; the repository's earlier proposal rejected feature-wide
    barrels to protect server/client boundaries. Define separate, narrow public
    entry points if one barrel cannot safely serve both environments.
13. **CMS details:** Editorial roles, localization ownership, revision policy,
    preview authorization, media pipeline, content environments, and recovery
    are not yet specified.
14. **Platform topology:** Confirm Vercel/Sanity/Supabase environment mapping,
    regions, connection method, pooling, migration runner, backups, monitoring,
    and secrets ownership.
15. **Notification providers and recovery:** Agency/customer delivery channels,
    provider choice, retry behavior, idempotency boundary, and manual recovery
    are not specified.

## Scope Classification Against the Former Prototype

| Classification | Change |
| --- | --- |
| Replacement | Local JSON as public-content authority → Sanity |
| Replacement | Email-only, no-storage enquiry boundary → Supabase transactional persistence |
| Replacement | Prototype `showcase` structure → business-context feature architecture |
| Additional scope | Customer, Consultation, Booking Request, Contact Message, optional Newsletter Subscriber |
| Additional scope | Catalogue search and filtering |
| Additional scope | CMS Studio, preview, validation, and editorial operations |
| Additional scope | Phase 1 public production deployment and operational monitoring |
| Future enhancement | Payments, questionnaire, scheduling, confirmed Booking, customer authentication |

## Batch Completion Condition

This batch is fully reconciled when the operator resolves or delegates the 15
conflicts above, identifies the subset requiring client validation, and supplies
any remaining material that affects preview-release scope or platform
boundaries.
