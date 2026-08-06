# Next.js and Documentation Architecture Inventory

**Review status:** completed 2026-08-02. This is an evidence-based snapshot,
not implementation authority. No application files were moved or changed for
this review.

## Scope and sources

This inventory compares the checked-out runtime with current repository
authority and the evaluation-only candidate in
[`../new-proposed-docs/`](../new-proposed-docs/README.md).

Read sources included the documentation entry point and active-work router
([`../README.md`](../README.md), [`../../NEXT.md`](../../NEXT.md)); project,
feature, and Foundation Design decisions under [`../grilling/`](../grilling/);
the existing Layer 2 material; the full candidate documentation tree; and the
application, configuration, scripts, and tests listed below. Documents under
`../archive/showcase-prototype-v0/` were inspected only through their archive
router because `docs/README.md` explicitly designates that tree as historical
reference, not current authority.

## Executive current-state statement

The running application is a small bilingual, static showcase prototype. It is
not yet the Public Preview Release described by the accepted product decisions.
It has no Sanity client or Studio, database, Drizzle schema or migrations,
Neon connection, request persistence, email integration, Server Action, Route
Handler, public form submission, or dynamic business backend.

The source reorganization described by the previous Layer 2 migration has not
started: `git status --short` was empty before this report, and the inventory's
own status correctly says that no application files had moved. Consequently,
the feature name `showcase` and its detailed move map remain a plan for an
archived prototype, not a reusable target architecture.

## Runtime and source structure

| Area               | Verified current state                                                                                                                                                                                         | Evidence                                                                                                                                                                                                                                                                                             |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Framework          | Next.js 16.2.12 App Router, React 19.2.4, strict TypeScript, pnpm 11.17.0.                                                                                                                                     | [`../../package.json`](../../package.json), [`../../tsconfig.json`](../../tsconfig.json)                                                                                                                                                                                                             |
| Routes             | `app/[locale]` supplies `/en`, `/el`, and `/[locale]/destinations/paros-antiparos`; `/[locale]/quality-lab` is a test/quality fixture. `app/robots.ts` is the only metadata-route file.                        | [`../../app/[locale]/layout.tsx`](../../app/[locale]/layout.tsx), [`../../app/[locale]/page.tsx`](../../app/[locale]/page.tsx), [`../../app/[locale]/destinations/paros-antiparos/page.tsx`](../../app/[locale]/destinations/paros-antiparos/page.tsx), [`../../app/robots.ts`](../../app/robots.ts) |
| Rendering          | Locale params are statically enumerated, Server Components are the default, and pages calculate localized metadata from local content. No `revalidate`, dynamic data fetch, or Draft Mode is present.          | [`../../app/[locale]/layout.tsx`](../../app/[locale]/layout.tsx), route `page.tsx` files                                                                                                                                                                                                             |
| Localization       | `next-intl` owns the `en`/`el` routing and request configuration. `proxy.ts` redirects `/` to `/en` and applies locale middleware.                                                                             | [`../../i18n/routing.ts`](../../i18n/routing.ts), [`../../i18n/request.ts`](../../i18n/request.ts), [`../../proxy.ts`](../../proxy.ts)                                                                                                                                                               |
| Presentation       | Home and Paros pages compose shared header/footer and page-section components from root `components/`. The header is the main interactive client boundary; the quality lab dynamically loads a test toggle.    | [`../../components/layout/site-header.tsx`](../../components/layout/site-header.tsx), [`../../components/sections/`](../../components/sections), [`../../components/quality-lab-toggle.tsx`](../../components/quality-lab-toggle.tsx)                                                                |
| Content            | English and Greek JSON files are imported and validated at module load by Zod. The schema also enforces structural parity and selected stable values across locales.                                           | [`../../content/en/showcase.json`](../../content/en/showcase.json), [`../../content/el/showcase.json`](../../content/el/showcase.json), [`../../content/schemas/showcase.ts`](../../content/schemas/showcase.ts), [`../../lib/content.ts`](../../lib/content.ts)                                     |
| Navigation         | `lib/routes.ts` supplies a prototype-specific route-ID union and CTA mapping. It refers to planned but absent Plan My Trip and confirmation paths; existing header/CTA links can therefore lead to route gaps. | [`../../lib/routes.ts`](../../lib/routes.ts), [`../../components/sections/showcase-media.tsx`](../../components/sections/showcase-media.tsx)                                                                                                                                                         |
| Shared utilities   | `lib/utils.ts` contains `cn`; `components/ui/button.tsx` is a reusable Base UI/CVA primitive but is consumed only by the quality fixture.                                                                      | [`../../lib/utils.ts`](../../lib/utils.ts), [`../../components/ui/button.tsx`](../../components/ui/button.tsx)                                                                                                                                                                                       |
| Styling and assets | Global CSS, local public images, `next/image`, fixed quality settings, and Google fonts support the showcase.                                                                                                  | [`../../app/globals.css`](../../app/globals.css), [`../../public/images/`](../../public/images), [`../../next.config.ts`](../../next.config.ts)                                                                                                                                                      |

### Server and data boundaries

- A repository-wide source search found no `"use server"`, Server Action,
  `app/**/route.ts`, or API handler.
- A repository-wide source and dependency search found no installed or imported
  Sanity, Drizzle, PostgreSQL, Neon, React Hook Form, or TanStack Query
  integration. Incidental TanStack packages in the lockfile are transitive and
  are not application dependencies.
- The only application environment value in use is the public site URL for
  metadata. [`../../.env.example`](../../.env.example) has no CMS, database,
  mail, or webhook configuration.
- `next.config.ts` sets security headers and permits local image optimization;
  it is not an authorization, persistence, or integration boundary.

## Cross-feature dependencies and migration implications

The code has only three real reuse clusters:

1. Locale framework code: `i18n/`, `messages/`, `proxy.ts`, and the locale
   layout.
2. Prototype showcase code: JSON schema/loading, route IDs, header/footer,
   CTA/media, Home/Paros sections, and their tests.
3. Quality-fixture primitives: `components/ui/button.tsx`, the fixture toggle,
   and `quality-lab` tests.

The old inventory's route-local placement and small `shared/` principle remain
sound. Its proposed `features/showcase` does not: it would classify a
short-lived prototype representation as a business capability just before the
new product replaces it. The accepted future capability boundaries are instead
public brand pages, catalogue discovery, three distinct request journeys, and
request processing; those are documented in
[`../grilling/DECISIONS.md`](../grilling/DECISIONS.md) and are not implemented
yet.

## Tests and quality controls

The existing quality system is unusually strong for the current prototype:

- Vitest covers localized content parity, route utilities, component behavior,
  design-token/media contracts, and scripts under [`../../tests/unit/`](../../tests/unit/).
- Playwright covers localization, metadata, and accessibility under
  [`../../tests/e2e/`](../../tests/e2e/).
- `package.json` defines Prettier, ESLint, Knip, strict type checking, content
  validation, coverage, build, Playwright, secret scanning, dependency audit,
  and Unlighthouse commands; `pnpm check:push` is the full push gate.
- [`../QUALITY_GATES.md`](../QUALITY_GATES.md) correctly makes Markdown-only
  changes proportionate, while retaining full gates for runtime work.

The tests validate prototype behavior, not the unimplemented public-preview
workflows or a future domain layer. There are no database, Sanity adapter,
request-processing, mail-delivery, or migration tests because those systems do
not exist in the checkout.

## Documentation accuracy and drift

| Documentation claim or area                                                                                                                                              | Assessment against code                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`NEXTJS_LAYER_2_INVENTORY.md`](NEXTJS_LAYER_2_INVENTORY.md) says no files moved and describes the prototype's three reuse zones.                                        | Accurate at the time of review; the file's detailed move map is now strategically stale because its `showcase` destination conflicts with accepted replacement-product boundaries. |
| [`NEXTJS_LAYER_2_MIGRATION.md`](NEXTJS_LAYER_2_MIGRATION.md) establishes narrow placement, dependency direction, Server/Client separation, and incremental verification. | Useful generic migration guidance; it does not describe current source paths or a settled future module design.                                                                    |
| [`work-items/prototype-rebaseline/ARCHITECTURE_PROPOSAL.md`](work-items/prototype-rebaseline/ARCHITECTURE_PROPOSAL.md) labels itself withdrawn.                          | Accurate as history; its proposed `discovery`/`trip-request` folders are not yet authoritative or implemented.                                                                     |
| [`../README.md`](../README.md), [`../grilling/README.md`](../grilling/README.md), and accepted decisions.                                                                | Accurate about authority and the fact that the runnable prototype is not the replacement contract. Their number and cross-links make initial orientation slower than necessary.    |
| Candidate `new-proposed-docs/docs/architecture/*` and `data/*`.                                                                                                          | Not current state: no `src/`, `modules/`, `db/`, `sanity/`, domain/application/infrastructure/presentation folders, or adapters exist.                                             |
| Candidate customer/quote/booking/payment documentation.                                                                                                                  | Conflicts with accepted Public Preview scope, which defers accounts, confirmed bookings, payments, suppliers, dashboard work, and live availability.                               |

## Current migration progress

The previous migration is documentation-only and **0% implemented in source**.
It has produced reusable governance, not reusable runtime structure:

- reusable: the narrowest-owner rule, dependency direction, route colocation,
  Server/Client separation, staged verification, and no-speculative-directory
  guard in [`NEXTJS_LAYER_2_MIGRATION.md`](NEXTJS_LAYER_2_MIGRATION.md);
- not reusable as a target: the `features/showcase` namespace, its file moves,
  and its assumption that the preserved prototype should become the future
  foundation;
- data-migration risk today: none, because no production data store or schema
  exists;
- code-discard risk today: none, because no source migration occurred.

The repository now has accepted System Boundaries, Editorial Content Platform,
Transactional Data Platform, and Application Architecture decisions. Runtime and
Production Foundations remains the next separately authorized Foundation Design
subject; see
[`../grilling/foundation-design/README.md`](../grilling/foundation-design/README.md).

## Inventory conclusion

Do not execute the old Layer 2 file-move map. Preserve its generic principles as
inputs to the accepted Application Architecture, then introduce only the module
boundaries demanded by an explicitly authorized public-preview vertical slice.
This avoids creating an intermediate `showcase` architecture that the replacement
product would immediately abandon.
