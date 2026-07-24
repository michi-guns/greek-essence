# Issue Review 01: Explore the bilingual Paros and Antiparos editorial journey

Date: 2026-07-25
Reviewer: fresh independent `jzgreekrev` code-review agent
Issue: `02-explore-paros-editorial`
Verdict: `FAIL`
Route: `red`

## Scope

Reviewed the issue-2 implementation at fixed point `0a3d7a4224b6d0f648edc39abfc5b5e14314efd8` on `feat/jz-ralph-workflow` plus the live dirty-worktree snapshot. The reviewed production/content/test/config scope was:

- `app/[locale]/destinations/paros-antiparos/page.tsx`
- `app/[locale]/page.tsx`
- `app/globals.css`
- `components/layout/language-switcher.tsx`
- `components/layout/site-footer.tsx`
- `components/layout/site-header.tsx`
- `components/sections/home-sections.tsx`
- `components/sections/paros-sections.tsx`
- `components/sections/showcase-media.tsx`
- `content/en/showcase.json`
- `content/el/showcase.json`
- `content/schemas/showcase.ts`
- `lib/content.ts`
- `lib/routes.ts`
- `scripts/validate-content.mjs`
- `tests/unit/content/showcase-content.test.ts`
- `tests/unit/routes/showcase-routes.test.ts`
- `tests/e2e/localization-and-quality.spec.ts`
- `tests/e2e/accessibility.spec.ts`
- `unlighthouse.config.ts`

Also inspected the unchanged authority/fixed-boundary neighbours `content/shared/media.json`, `i18n/navigation.ts`, `i18n/routing.ts`, `next.config.ts`, and `package.json`. Read root `AGENTS.md` and `NEXT.md`; feature `AGENTS.md`, `PRD.md`, and the complete approved `SPEC.md`; issue 2 `issue.md` and `change-contract.md`; `implementation-attempt-02.md`; all `jz-implement-contract` references; immutable issue-1 review 05; and Ralph/JZ operator-exception evidence where relevant. Resolved depth is Tier 2 — Prototype by direct operator instruction, consistent with SPEC front matter and the project default.

The unrelated Ralph rebuild, plan, generated `.playwright-cli`, workflow/signal, issue-1, and other dirty-worktree changes were preserved and excluded. No source, test, contract, lifecycle, signal, visual-review, Git-history, remote, or deployment mutation was performed. This review does not provide visual certification.

## Standards Verdict

`FAIL`. The current destination routes build statically, render bilingual six-section pages, retain route-aware navigation and metadata, use the established token foundation, keep pending media behind a neutral fallback, and pass the focused lint/type/content/unit/build/browser/axe checks rerun below. No credential, PII, dynamic content boundary, successor form implementation, broader catalogue, or unsupported operational claim was found in the reviewed slice.

However, required Tier-2 contract behavior is not fully protected at the agreed public seams. Locale parity validation permits value-level drift in stable IDs/routes/media, the approved-media rendering boundary is not complete, and the issue-specific browser matrix does not exercise several explicitly required destination journeys and realistic responsive boundaries. These are accepted-behavior and focused-test gaps, not requests for speculative production breadth.

The inherited quality failures remain failures: global formatting exits 1 on the same eight preserved unrelated files; Unlighthouse remains technically RED from inherited Home failures, including the latest reported `/en` performance score `0.89` and LCP `2693.751ms`; and `check:all` exits 1 at the inherited global format check. Destination Unlighthouse scores were reported as `0.91`, with other destination scores `1.0`. None is reclassified as green.

## Spec And Contract Verdict

`FAIL`. Live content and route inspection confirms the intended six-section order, complete EN/EL fixtures, culture/gastronomy coverage, fixed destination paths, localized canonical/alternate/noindex metadata, current destination nav state, literal `destination=paros-antiparos` query in the live CTA, static generation, pending-media fallback, and no obvious privacy/claims breach. The following blocking gaps violate FR-003/013 and the issue/change-contract acceptance matrix.

## Blocking Findings

### F-01: Build-time locale parity validates shapes but not stable IDs, media references, or route values

- **Severity:** High / blocking.
- **Location:** `lib/content.ts:30-40,54-72`; `content/schemas/showcase.ts:3-21,59-86`; `scripts/validate-content.mjs:23-50`; weak coverage at `tests/unit/content/showcase-content.test.ts:44-50,79-99`.
- **Requirement:** SPEC §7.3 lines 718-720 requires both locale files to have identical structure and referenced stable IDs. Change contract lines 74-77 requires identical structural keys and collection IDs and rejection of mismatched EN/GR collection shape, unknown route IDs, and media defects; issue acceptance line 15 requires build-time locale-structure, message-parity, stable-media-ID, and approval-metadata rules.
- **Evidence / reproduction:** `shape()` converts every scalar to only its JavaScript type. The pair check therefore cannot distinguish different non-empty collection IDs, different known media IDs, or different valid route IDs. A read-only inline Node probe changed the Greek signature-experience ID, changed its media ID to another known manifest ID, and changed the final CTA route from `plan-my-trip` to valid enum member `home`; it exited 0 and reported `{"shapeEqual":true,"allChangedMediaKnown":true,...}`. Each changed value also satisfies the current Zod schemas. The existing “complete six-part” unit test only checks that `paros` exists, and no controlled value-parity drift case exists.
- **Impact:** A locale can silently point a section at different approved media, use a different collection identity, or route its CTA differently while `getShowcaseContent`, `pnpm validate:content`, and current tests remain green. That breaks the fixed bilingual route/content/media identity boundary and can create mixed or behaviorally non-equivalent locales.
- **Required correction:** First add RED tests at `validateShowcaseContentPair`/`pnpm validate:content` proving rejection of mismatched destination collection IDs, referenced media IDs, and CTA route/context semantics. Then make the public build-time validator compare the required stable values across locales while still allowing translated prose.
- **Verification:** Show the controlled drift tests fail before the correction and pass afterward; rerun the focused content tests, `pnpm validate:content`, `pnpm test:unit`, `pnpm typecheck`, and `pnpm build`.

### F-02: The approved-media path is not a complete fail-closed rendering boundary

- **Severity:** High / blocking.
- **Location:** `lib/content.ts:103-108,119-150,153-155`; `components/sections/showcase-media.tsx:19-32`; `app/globals.css:470-493`; coverage at `tests/unit/content/showcase-content.test.ts:116-163`.
- **Requirement:** SPEC §7.3 lines 705-720 and change contract lines 53, 79-83 require approved media to render only with an existing file, complete localized approval metadata, intrinsic geometry, focal position, and a stable component presentation; removal of any required approval field/file must fail closed. Issue acceptance lines 16 and 19 require a safe fallback and stable responsive media behavior.
- **Evidence / reproduction:** The live `resolveMedia()` calls `resolveMediaFromManifest()` without an existence predicate, whose default is `() => true`; the public loader therefore does not itself verify the physical file before returning `kind: "approved"`. The standalone validation script checks files only when separately invoked. The unit suite injects only a successful file predicate and has no missing-file case. Separately, `ShowcaseMedia` emits approved images with class `showcase-media`, but the complete stylesheet has no `.showcase-media` rule; destination CSS defines geometry only for `.media-fallback`. In the hero, only `.media-fallback` receives the absolute overlay treatment, and media cards likewise style only fallback media.
- **Impact:** A manifest promoted to approved can pass through the public resolver despite a missing file if the standalone validator is skipped, and an approved image does not share the fallback's required hero/card crop and layout contract. QUE-003 makes fallback the current live state, but the controlled approved state is an explicit, realistic contract boundary and is already represented as supported by the public union.
- **Required correction:** Add RED seam/component tests for a missing approved file and approved hero/card rendering geometry. Make the public build-time media resolution fail closed on actual file existence and give approved images responsive width/aspect/crop positioning equivalent to their intended hero/card slots without changing the pending fallback.
- **Verification:** Prove missing files and incomplete approval remain rejected, controlled approved records render localized alt/intrinsic/focal data in stable hero/card containers, all three live destination IDs still resolve to `pending-approval`, and rerun content/unit/build/compact/wide/axe checks.

### F-03: Destination-specific browser coverage does not exercise the required integrated and responsive matrix

- **Severity:** Medium / blocking focused-test gap.
- **Location:** `tests/e2e/localization-and-quality.spec.ts:209-242,282-340`; `tests/e2e/accessibility.spec.ts:10-55`.
- **Requirement:** Change contract lines 97-107 and 113-118 requires Home → Paros in both locales, destination locale switching in both directions, contextual CTA parity, destination security headers/browser guards, compact-menu behavior, reduced motion, 200% zoom, and no-overflow checks at required compact/wide surfaces. Issue acceptance lines 20-21 explicitly requires focused automated proof and the integrated Home-to-Paros compact/wide journey.
- **Evidence / reproduction:** The destination journey test starts directly at the English destination route, checks only the English final CTA query, then switches only EN → EL. It never activates a Home destination link, never covers EL → EN destination switching, never checks the Greek contextual CTA, and never verifies all destination headings/order beyond a section count and H1. The security-header test loops only over `/en` and `/el`. The reduced-motion/195px overflow/focus test navigates only the two Home routes. Axe covers the destination routes, but it does not replace those behavior assertions. The compact/wide rerun passes because the named gaps are not exercised.
- **Impact:** Regressions in Home-to-destination wiring, reverse locale identity, Greek CTA context, destination header policy, or destination-specific compact/zoom/overflow/reduced-motion behavior can ship while every current browser test stays green.
- **Required correction:** Add the missing issue-specific RED browser assertions using the existing guarded seams, without expanding into form behavior or visual certification. Cover Home → Paros from EN and EL, both switch directions, both localized CTA hrefs with only the allow-listed query, destination current nav/security headers, and destination no-overflow/focus/reduced-motion/zoom behavior at the contract's realistic compact/wide boundaries.
- **Verification:** Demonstrate the new assertions fail for the removed/mutated behavior before repair, then pass under both `chromium-compact` and `chromium-wide`; rerun the full focused localization/axe files and browser guards.

## Non-Blocking Findings

- `git diff --check` over the whole dirty worktree exited 2 on `.scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/issue.md:24` for a new blank line at EOF. A source/content/test/config-scoped `git diff --check` exited 0, and focused Prettier passed. This is a separate issue-directory workflow-metadata whitespace observation, not an issue-2 implementation blocker and not one of the eight global Prettier failures; the reviewer did not alter lifecycle metadata.
- The localized final CTA labels (`Plan Paros & Antiparos` / `Σχεδιάστε Πάρο & Αντίπαρο`) are understandable but slightly compressed editorial phrasing. A later copy pass could make both more idiomatic; this does not block the provisional Tier-2 content slice.

## Verification Considered

- `pnpm typecheck` — `PASS`, exit 0.
- `pnpm lint` — `PASS`, exit 0.
- `pnpm validate:content` — `PASS`, exit 0; reported EN/EL validation with media approval checks, subject to F-01/F-02.
- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/routes/showcase-routes.test.ts` — `PASS`, exit 0; 2 files / 20 tests.
- `pnpm test:unit` — `PASS`, exit 0; 7 files / 30 tests.
- `pnpm build` — `PASS`, exit 0; 10 static pages generated, including both localized Paros routes as SSG, with no new dynamic application route.
- Focused `pnpm exec prettier --check` over 19 issue-owned production/content/test/config paths — `PASS`, exit 0; all matched files use Prettier style.
- `pnpm format:check` — `FAIL`, exit 1; exactly eight preserved unrelated files failed (one `.hermes/plans` file and seven generated `.playwright-cli/*.yml` files). This is not called green.
- `pnpm exec playwright test --project=chromium-compact --project=chromium-wide tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` — `PASS`, exit 0; 29 passed / 1 expected wide-project compact-interaction skip, subject to F-03's missing acceptance coverage.
- `git diff --check` over the full dirty worktree — `FAIL`, exit 2; issue workflow metadata had a new blank line at EOF. The same command scoped to reviewed production/content/test/config paths — `PASS`, exit 0.
- Read-only parity probe mutating only in-memory JSON values — `FAIL` against the contract, command exit 0: current parity logic reported `shapeEqual:true` and all changed media known despite changed Greek collection ID, media ID, and valid CTA route ID. This reproduces F-01.
- Read-only `getCtaPathname` probe — command exit 0; it can append the destination query to Home and Paros route IDs (`/?destination=paros-antiparos` and `/destinations/paros-antiparos?destination=paros-antiparos`), reinforcing the absence of tested CTA route/context semantics in F-01.
- Implementation evidence records `pnpm test:e2e` as `PASS`, exit 0, 43 passed / 2 skipped and `pnpm test:a11y` as `PASS`, exit 0, 18 passed.
- Implementation evidence records `pnpm quality:unlighthouse` as `FAIL`, exit 1. Latest destination performance scores were `0.91` and other destination scores `1.0`; inherited Home remained technically RED, including `/en` performance `0.89` and LCP `2693.751ms`. Historical immutable issue-1 evidence remains EN LCP `2547.223ms > 2500ms` under direct operator exception. No performance threshold was lowered, and this review does not call the command green.
- Implementation evidence records `pnpm check:all` as `FAIL`, exit 1 at inherited `format:check`; later chained subcommands did not run in that invocation. This review does not call the aggregate green.
- TDD evidence considered: the retained missing-`paros` content RED and destination-404/H1 RED are valid missing-behavior failures, followed by passing GREEN commands. They do not cover F-01 through F-03 and therefore do not satisfy the full contract acceptance matrix.

## Required Route

`red`. Preserve this immutable report and reopen issue 2 at the RED phase. Add focused failing tests for F-01 through F-03 at the contract's existing content/media/browser seams before repairing implementation. Do not patch findings while the issue remains in review, do not self-convert this failure to approval, and require a fresh independent code-review attempt after the RED → GREEN repair. The mandatory visual review remains downstream of a passing code review.
