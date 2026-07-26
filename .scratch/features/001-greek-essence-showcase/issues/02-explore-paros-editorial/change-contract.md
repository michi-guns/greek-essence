# Change Contract — Explore the bilingual Paros and Antiparos editorial journey

Issue: `02-explore-paros-editorial` · Method: `tdd-solo` · Milestone: `explore-bilingual-showcase`

## Goal / postcondition

After this slice, a visitor can move from the completed Home to a static six-section Paros & Antiparos editorial page at `/en/destinations/paros-antiparos` or `/el/destinations/paros-antiparos`, switch language while preserving destination route identity, and follow a contextual planning CTA whose only query value is the allow-listed public `paros-antiparos` identifier. Both locales expose complete natural editorial content and localized metadata, all pending destination media renders through the established neutral fallback, and the integrated journey remains responsive, accessible, private, performant, and browser-clean. Because this is user-visible work, completion also requires fresh independent code review followed by the feature-local visual-review gate for both locales and both required viewport sizes; those reviews occur during implementation, not during this contract action.

## Traces

FR-002, FR-003, FR-013, FR-015, FR-016; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-002, DEC-008, DEC-010, DEC-011, DEC-012, DEC-013, SUBDEC-004.

## Soft scope — edit freely

| Path | Create / edit | Reason & pattern to match |
| --- | --- | --- |
| `app/[locale]/destinations/paros-antiparos/page.tsx` | create | Add the static localized destination route; mirror `app/[locale]/page.tsx` for `setRequestLocale`, typed local content, shared shell, media resolution, and localized canonical/alternate/noindex metadata. The existing route directories are under `app/[locale]`; create the contained destination directories as needed. |
| `app/[locale]/page.tsx` | edit | Pass explicit Home route identity to the shared header after its public props become route-aware; preserve the completed six-section Home and metadata behavior. |
| `components/layout/site-header.tsx` | edit | Accept `{locale, routeId}` and mark only the actual current route while preserving the existing accessible compact-menu close/focus behavior and locale-aware `Link` pattern. |
| `components/layout/language-switcher.tsx` | create | Isolate equivalent-route locale switching using the established `i18n/navigation.ts` helper and `ShowcaseRouteId`; preserve destination identity without raw pathname replacement. The `components/layout` directory and sibling shell patterns exist. |
| `components/layout/site-footer.tsx` | edit only if needed | Reuse the bounded bilingual footer unchanged where possible; a destination-specific localized return link is allowed only if it preserves the no-invented-contact/legal boundary. |
| `components/sections/home-sections.tsx` | edit | Reuse its public CTA/media patterns and make CTA query construction honor only a non-null allow-listed `destinationContext`; existing Home CTAs remain behaviorally unchanged because their context is null. |
| `components/sections/paros-sections.tsx` | create | Render exactly the destination hero, defining-character introduction, traveler-fit block, signature experiences including culture/gastronomy, combinations block, and contextual final CTA using explicit content props and established semantic classes. Mirror `home-sections.tsx`; no filesystem reads or client boundary. |
| `components/sections/showcase-media.tsx` | create if needed | Extract the existing approved-image versus neutral-fallback presentation only when sharing it avoids duplication between Home and Paros; preserve `next/image`, intrinsic geometry, focal position, and adjacent-copy meaning. |
| `content/en/showcase.json` | edit | Add complete English `paros` editorial content with the exact SPEC structure and stable destination/editorial media IDs. |
| `content/el/showcase.json` | edit | Add structurally identical, natural Greek `paros` content with comparable hierarchy and no copied-English fallback. |
| `content/schemas/showcase.ts` | edit | Extend the strict public content schema with the SPEC's exact `paros` shape, including non-empty traveler-fit, signature-experience, and combination collections. |
| `content/shared/media.json` | reuse; edit only after explicit asset approval | Existing stable IDs and pending approval metadata are authoritative. This slice consumes the records but defaults to fallback and may not invent or promote approval fields. |
| `lib/content.ts` | edit | Extend the sole public build-time loader/validator to include all destination media references while retaining locale-shape parity and fail-closed media resolution. |
| `lib/routes.ts` | edit if needed | Preserve the fixed `showcaseRoutes` and `getLocalizedHref(routeId, locale)` interface; add only a small typed helper for an allow-listed destination-context query if shared CTA construction needs one. |
| `messages/en.json` | edit only if needed | Add only destination/shared-shell interface labels consumed outside editorial JSON, preserving all existing keys. |
| `messages/el.json` | edit only if needed | Keep exact message-key parity and natural Greek for any corresponding interface labels. |
| `scripts/validate-content.mjs` | edit | Extend the existing content-validation command's referenced-media checks from Home to the destination structure; retain fail-closed approval validation. |
| `app/globals.css` | edit | Add only destination-consumed responsive section/card/media states using the established CSS-only light semantic foundation; do not duplicate or redesign the completed token inventory. |
| `tests/unit/content/showcase-content.test.ts` | edit | Extend the public content/media seams with exact EN/GR destination structure, Greek prose, distinct media references, and invalid fixture cases. |
| `tests/unit/routes/showcase-routes.test.ts` | edit | Preserve fixed route mappings and cover any public allow-listed contextual-CTA helper without testing string-building internals. |
| `tests/unit/messages/parity.test.ts` | edit only if destination interface keys are added | Reuse the existing recursive message-parity seam; do not create another translation mechanism. |
| `tests/e2e/localization-and-quality.spec.ts` | edit | Extend the existing guarded metadata, locale-switch, security-header, focus, reduced-motion, zoom, and no-overflow matrix to Home → Paros and both destination routes. |
| `tests/e2e/accessibility.spec.ts` | edit | Add both localized destination routes to the existing axe WCAG 2.2 A/AA guarded matrix. |
| `tests/e2e/browser-guards.ts` | edit only if required | Preserve zero unexpected console, page, request, and HTTP failures; adjust only for a demonstrated legitimate destination behavior. |
| `playwright.config.ts` | edit only if required | Preserve compact `390 × 844`, medium `834 × 1112`, and wide `1440 × 1024` projects and retained failure artifacts. |
| `unlighthouse.config.ts` | edit | Add representative English/Greek destination URLs while retaining all existing score budgets and the accepted Windows throttling evidence. |

Small neighbouring files under these same destination/content/layout/testing concerns may be added without approval when they preserve these patterns and do not introduce form, submission, or broader-catalogue work.

## Hard walls — STOP if hit

- **Explicit locale-routing interface** — `routing.locales` remains exactly `en`/`el`, locale prefixes remain mandatory, `/` continues to resolve to `/en`, unsupported locales remain 404, and static locale generation with `dynamicParams = false` remains unchanged (DEC-010; SPEC §§4.3, 5.3, 12.5).
- **Fixed route and metadata identity** — the destination pair remains exactly `/en/destinations/paros-antiparos` and `/el/destinations/paros-antiparos`; `showcaseRoutes` and `getLocalizedHref(routeId, locale)` keep their stable signatures, and each page keeps self-canonical, `en`/`el`/`x-default`, and `noindex,nofollow` semantics (FR-003/015; SPEC §§5.3, 12.5).
- **Static-first boundary** — this issue may not add a Route Handler, Server Action, runtime content fetch, database, CMS, or other dynamic boundary; the destination page and editorial content remain build-time/static, and only the existing necessary compact-menu client island is reused (DEC-010; NFR-008; SPEC §§0, 5.1, 10).
- **Exact destination composition** — shared header, destination hero, defining-character introduction, traveler-fit block, signature experiences including culture/gastronomy, one combinations block, contextual final CTA, and footer are the complete slice. Accommodation, sample journeys, a gallery, broader catalogue sections/routes, or generalized page-builder components require a new contract (DEC-002; SPEC §§2.5, 5.4, 12.3).
- **Context allow-list and privacy boundary** — the CTA may carry only `destination=paros-antiparos`; no free-form or user-derived value, unknown query key, PII, credentials, analytics, logs, metadata, fixture, screenshot, or artifact data may be introduced. The target form itself is successor work (NFR-004/005; SPEC §§6.2, 9).
- **Stable media-ID and approval boundary** — editorial JSON references IDs from `content/shared/media.json`, never physical paths. Pending records resolve to the existing neutral fallback; an image may render only with complete localized alt, approved source/rights/status, non-provisional state, focal coordinates, positive geometry, and an existing file. QUE-003 is not reopened (FR-013; SPEC §§2.3, 6.3, 7.3).
- **Bilingual parity and claims boundary** — every destination section, shell label, CTA, metadata value, route state, fallback, focus state, and compact-menu state has complete natural EN/GR coverage with comparable hierarchy and no mixed-language fallback. Content may not invent price, availability, booking guarantees, response times, awards, partners, reviews, credentials, or operational facts (DEC-008/SUBDEC-004; NFR-004/007; SPEC §7.3).
- **Established visual foundation** — consume the completed light-only CSS/Tailwind semantic token source and accepted showcase variants. Do not add dark mode, a TypeScript theme object, a partial parallel palette, a new design system, speculative variants, or changes that regress completed Home behavior (DEC-011/013; FR-016; SPEC §§2.1, 7.1).
- **Quality budgets and viewport interfaces** — do not lower Playwright dimensions, axe expectations, Unlighthouse scores (performance ≥90, accessibility 100, best practices ≥95, SEO ≥95), or documented transfer/image/JS/CSS/LCP/INP/CLS budgets to obtain green checks (DEC-012; NFR-003; SPEC §§3.3, 13–14).
- **Successor milestone surfaces** — do not implement the Plan My Trip page/form/draft, confirmation, submission API, Resend transport, or emails. A contextual link to the fixed Plan My Trip URL is the only successor-facing behavior authorized here (SPEC milestone coverage and §12.3).
- **Feature-local review completion gates** — implementation cannot mark this user-visible issue `done` until a fresh independent code review passes and then a fresh independent visual review reports `PASS` for both localized destination routes at `390 × 844` and `1440 × 1024`, including pending-media fallback, Home-to-destination navigation, route-preserving locale switch, contextual CTA, current navigation state, focus, and reduced motion. Evidence is sanitized and immutable (`.scratch/features/001-greek-essence-showcase/AGENTS.md`).

## Seams to test

- **`getShowcaseContent(locale)` and `pnpm validate:content`** — the public build-time boundary exposes exact typed EN/GR destination data and rejects structural, parity, empty-copy, or referenced-media defects.
- **`resolveMedia(id, locale)`** — the public media boundary returns a fully approved localized record or the intentional pending-approval fallback for each destination media ID; components never infer approval.
- **`showcaseRoutes` / `getLocalizedHref(routeId, locale)` and contextual CTA href** — the public route boundary preserves fixed destination identity by locale and emits only the allow-listed planning context.
- **Rendered destination route (`GET /en/destinations/paros-antiparos`, `GET /el/destinations/paros-antiparos`)** — browser-observable composition, locale purity, metadata, shell/current state, fallback rendering, links, headers, and static behavior.
- **Home-to-destination and destination locale-switch journey** — browser navigation preserves destination route identity in both directions without raw pathname replacement or mixed locale content.
- **User-visible responsive/accessibility surface** — destination hierarchy, cards, fallback media, navigation, focus, reduced motion, zoom, and overflow at required compact/wide surfaces and realistic spot checks.
- **Repository quality gates** — focused content/route tests plus formatting, lint, type, content validation, unit, build, compact/wide Playwright, axe, full E2E, Unlighthouse, and aggregate commands remain truthful and threshold-preserving.

## Triangulating acceptance cases

**Seam: `getShowcaseContent(locale)` and `pnpm validate:content`**

- [ ] Locale `en` → `paros` contains exactly metadata, hero, introduction, traveler fit, signature experiences, combinations, and final CTA; each required collection is non-empty and culture/gastronomy is explicitly represented in the English signature-experience content (FR-002; SPEC §§5.4, 6.3).
- [ ] Locale `el` → the identical structural keys and collection IDs are present with Greek-script prose, comparable section depth, and no copied English except the Greek Essence brand (DEC-008/SUBDEC-004; SPEC §7.3).
- [ ] A controlled fixture with a missing `paros` key, empty heading, mismatched EN/GR collection shape, unknown route ID, or unknown destination media ID → schema/validation fails instead of dropping the field or falling back to another locale (FR-013; SPEC §7.3).
- [ ] Static editorial inspection of the actual EN/GR destination fixtures → rejects any price, availability/booking guarantee, response-time promise, award, partner, review, or credential claim; deterministic validation remains limited to structural and allow-listable rules (NFR-004/007; SPEC §7.3).

**Seam: `resolveMedia(id, locale)`**

- [ ] Live `destination-paros-antiparos-primary-01` with pending manifest defaults → `{kind:"fallback", id:"destination-paros-antiparos-primary-01", reason:"pending-approval"}` (QUE-003; live manifest).
- [ ] Live `paros-antiparos-editorial-culture-food-01` and `paros-antiparos-editorial-local-moment-01` under the same pending defaults → distinct fallback results retaining each requested ID, proving destination fallback is not hardcoded to the hero (live manifest; SPEC §7.3).
- [ ] A controlled fully approved destination record with existing file, positive dimensions, supported role, localized EN/GR alt, approved source/rights/status, non-provisional state, and focal coordinates in 0–100 → `kind:"approved"` with the requested locale's alt and manifest geometry; removing any required approval field makes validation/resolution fail closed (FR-013; SPEC §7.3).

**Seam: route identity and contextual CTA href**

- [ ] `paros` + `en` → `/en/destinations/paros-antiparos`; `paros` + `el` → `/el/destinations/paros-antiparos` (ASM-001; SPEC §5.3).
- [ ] English destination final CTA → `/en/plan-my-trip?destination=paros-antiparos`; Greek destination final CTA → `/el/plan-my-trip?destination=paros-antiparos` (SPEC §6.2).
- [ ] Home destination links carry no destination query, while the destination planning CTA drops unknown query keys and never serializes arbitrary values or PII; only the literal `paros-antiparos` context is accepted (NFR-004/005; SPEC §§6.2, 9).

**Seam: rendered destination route**

- [ ] `/en/destinations/paros-antiparos` → `<html lang="en">`, exactly six destination sections in DEC-002 order, English shell/editorial/CTA text, destination navigation marked current, self-canonical English URL, alternates to EN/EL plus English x-default, and `noindex,nofollow` (FR-002/015; SPEC §§3.2, 5.4).
- [ ] `/el/destinations/paros-antiparos` → `<html lang="el">`, the same hierarchy and IDs with natural Greek presentation, Greek self-canonical URL, equivalent alternates, and no English editorial fallback (DEC-008; FR-015).
- [ ] Both destination responses retain the existing CSP, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy: camera=(), microphone=(), geolocation=()`, and `X-Frame-Options: DENY`; browser guards observe no unexpected console/page/request/HTTP failure (NFR-005; existing guarded route pattern).

**Seam: Home-to-destination and destination locale-switch journey**

- [ ] Start `/en`, activate “Explore Paros & Antiparos” or “Discover the islands” → English destination route and English destination heading; switch via “Ελληνικά” → Greek destination route and Greek destination heading (FR-003; existing Home CTA and switcher patterns).
- [ ] Start `/el`, activate the equivalent Greek Home destination link → Greek destination; switch via “English” → English destination, preserving `paros` route identity rather than returning Home (FR-003; SPEC §5.3).
- [ ] Compact menu navigation, outside/Escape close, and route navigation keep the established focus-return/current-state behavior; destination identity changes only through locale-aware navigation (NFR-002; SPEC §7.1).

**Seam: user-visible responsive/accessibility surface**

- [ ] EN and EL destination routes at `390 × 844` → one-column six-section journey, operable compact menu, readable fallback aspect ratios and Greek copy, 44 × 44 practical targets, visible focus, and no clipping/horizontal overflow (NFR-001/002/007; feature visual gate).
- [ ] EN and EL destination routes at `1440 × 1024` → wide navigation and intentional selective multi-column editorial/card compositions preserve hierarchy, spacing, CTA prominence, and comparable locale depth (DEC-011/012; feature visual gate).
- [ ] At 320 px, intermediate/landscape width, and 200% zoom, plus `prefers-reduced-motion: reduce`, content and controls remain usable without horizontal overflow and no motion delays an action; axe reports zero selected WCAG 2.2 A/AA violations on both locale routes (NFR-001/002; SPEC §§7.1, 13.3).
- [ ] Pending hero/editorial media at both required widths/locales → intentional neutral surfaces show no broken-image icon or decorative replacement text, and adjacent headings/body preserve all editorial meaning (QUE-003; SPEC §§7.1, 7.3).
- [ ] After implementation and code review, a fresh independent visual reviewer inspects the final live application/screenshots for both locales and required widths and records immutable `reviews/<NN>-visual-review.md` with `PASS`; automated capture alone does not satisfy completion (feature `AGENTS.md`).

**Seam: repository quality gates**

- [ ] Focused route/content/message tests and `pnpm validate:content` → exit 0 for complete EN/GR destination data and fail the controlled structural/media defects above (FR-003/013/015).
- [ ] Compact and wide Playwright/axe runs → Home → Paros, both locale routes, metadata, locale switching, contextual CTA, browser guards, focus, reduced motion, zoom/no-overflow, and zero selected WCAG A/AA violations pass at `390 × 844` and `1440 × 1024` (DEC-012; SPEC §§13–14).
- [ ] `pnpm build` → exit 0 with both localized destination routes statically generated and no new dynamic server boundary (DEC-010; SPEC §14).
- [ ] Global `pnpm format:check` is run and reported exactly; focused Prettier verification over every issue-2-owned file exits 0. Existing unrelated Ralph/plan/generated Playwright formatting failures are preserved rather than edited or misreported, and any new issue-2 formatting failure is repaired (root `AGENTS.md`; immutable issue-1 review 05 lines 46–59).
- [ ] `pnpm quality:unlighthouse` is run with performance ≥90, accessibility 100, best practices ≥95, SEO ≥95 and unchanged transfer/image/JavaScript/CSS/LCP/INP/CLS budgets. The inherited issue-1 English Home LCP measurement of `2547.223ms` against the strict `≤2500ms` assertion remains technically RED under its direct operator-authorized exception and is never called a pass; issue 2 must introduce no new or worsened failure (immutable issue-1 review 05 lines 17–21 and 46–59; NFR-003; SPEC §§3.3, 13.4).
- [ ] The full applicable sequence in SPEC §14, including `pnpm check:all`, is run and each component result is preserved truthfully. The aggregate is not called green while inherited global formatting or strict LCP remains nonzero. Any new or worsened failure is repaired or requires a new direct operator decision; the implementation/review agents may not self-waive it.

## Method / risk

`tdd-solo` — the destination logic is routine and its public seams are clear, but exact bilingual structure, route/context allow-listing, fail-closed media approval, metadata, responsive accessibility, and preservation of completed Home behavior can regress silently; one fresh implementation agent must preserve exact RED and GREEN evidence across the seam-driven loop.

## Escalation — what forces a ScopeExpansionRequest

- A correct solution requires implementing or editing a concern outside the destination/content/layout/test soft scope, including the form/draft, API/email, confirmation, broader catalogue, deployment, credentials, remote Git state, or unrelated dirty work.
- A required change would cross a hard wall: explicit locale/static routing, fixed route/metadata signatures, exact six-section destination scope, context/privacy allow-list, stable media approval, bilingual claims parity, established CSS-only foundation, quality thresholds, successor ownership, or mandatory independent reviews.
- The implementation needs an architectural change not anticipated here, such as runtime content fetching, a CMS/database, generalized page builder/component system, new global client state, dark mode, or parallel theme representation.
- A RED test or later code/visual review implies behavior different from the issue or approved SPEC, including a missing locale/state/surface or a fix that requires crossing a wall.
- Required sanitized compact/wide EN/GR review evidence cannot be produced inside the accepted user-visible surfaces and states.

Small in-scope neighbour additions under the same destination/content/layout/testing concerns do **not** need a request.

## ScopeExpansionRequest (fill only if a hard wall is hit)

- **What was discovered:** <the file/interface/invariant the plan didn't anticipate>
- **Why the current contract is insufficient:** <what can't be done inside it>
- **Proposed change:** <files to add to soft scope, or wall to renegotiate>
- **Risk if ignored:** <low | medium | high>
