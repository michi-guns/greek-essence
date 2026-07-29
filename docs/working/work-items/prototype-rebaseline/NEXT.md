# Prototype Rebaseline

## Status

Active

## Ownership and Scope

Owner: Codex (`/root`)

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
  and Nodemailer through the agency mail service. Netlify remains an optional
  later replacement for Vercel.
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
  it. Consultation Request D-001 is ready. Grill one feature at a time.
- The architecture register now records Sanity, Neon, Drizzle, Vercel with
  optional Netlify, and Nodemailer as accepted directions with remaining
  feature-level and launch validation.
- No application implementation, dependency installation, schema migration,
  or active application path change is authorized by these decisions.
- A separate explicit operator instruction corrected the retained prototype's
  media path: `assets/imgs/` moved to `public/images/`, the approval-gated
  `content/shared/media.json` was removed, and direct localized image records
  now render on Home and Paros in English and Greek. This is a prototype
  correction, not replacement-product architecture authority.
- The operator set the prototype's custom bilingual Home LCP ceiling to 3000
  ms while retaining the Unlighthouse score budgets. Final measured LCP was
  2646.837 ms for `/en` and 2621.026 ms for `/el`.
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

## Next Recommended Action

Begin the Consultation Request feature grill at
`docs/grilling/consultation-request/GRILLING.md` D-001 and decide how much trip
information belongs in the initial request. Persist the operator's answer,
consequences, dependencies, rejected alternatives, and next question before
continuing.

Completion condition: the operator accepts the Consultation Request decisions,
they are distilled into that feature's `DECISIONS.md`, and the raw feature
`GRILLING.md` is removed only after separate path-specific approval.

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
- Vercel's public commercial plan or a validated Netlify replacement remains a
  production-operations decision before public launch.
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
- [Next feature grill: Consultation Request](../../../grilling/consultation-request/GRILLING.md)
- [Feature grilling router](../../../grilling/README.md)
- [Grilling protocol](../../../grilling/protocol.md)
