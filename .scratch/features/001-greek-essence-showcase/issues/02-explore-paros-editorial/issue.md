Status: done
Method: tdd-solo
Complexity: 3
BlockedBy: 1
Milestone: explore-bilingual-showcase
Phase: red
Reopens: 4

# Explore the bilingual Paros and Antiparos editorial journey

Extend the consumed showcase foundation into the destination discovery slice: a visitor can move from Home to a complete Paros & Antiparos editorial page in either locale, switch language without losing route identity, and follow the contextual planning call to action while unapproved media remains a safe neutral fallback.

## Acceptance criteria

- [ ] English and Greek destination routes render the exact six-section Paros & Antiparos composition and shared shell, covering character, traveler fit, signature experiences including culture/gastronomy, combinations, and the final planning CTA without broader catalogue sections (FR-002, DEC-002).
- [ ] Home-to-destination navigation and locale switching preserve the equivalent destination route, and the final CTA carries only the allow-listed public `paros-antiparos` context into the localized Plan My Trip URL (FR-003, DEC-010).
- [ ] Destination editorial content passes the shared build-time locale-structure, message-parity, stable-media-ID, and approval-metadata rules with complete natural English/Greek coverage (FR-013, DEC-008, SUBDEC-004, NFR-007).
- [ ] Pending QUE-003 destination media uses the designed neutral fallback without losing editorial meaning, broken-image UI, or invented approval metadata.
- [ ] Destination URLs, metadata, fixtures, screenshots, console output, and browser artifacts contain no PII; the public destination context remains an allow-listed non-PII identifier (NFR-004).
- [ ] Both localized destination routes emit non-empty localized metadata, self-canonical URLs, `en`/`el`/`x-default` alternates, and `noindex,nofollow` (FR-015).
- [ ] The page consumes the established semantic token foundation and only accepted showcase component variants; it remains static-first, shallow, responsive, accessible, performant, and free of unnecessary client code or unsafe runtime content boundaries (FR-016, NFR-001, NFR-002, NFR-003, NFR-005, NFR-008, DEC-011, DEC-013).
- [ ] Focused automated checks prove both locale routes, section/heading structure, localized CTA paths and context, locale switching, metadata, content validation, and safe fallback rendering.
- [ ] The integrated Home-to-Paros journey is exercised at the required compact and wide Playwright viewports with browser guards, axe checks, responsive/zoom spot checks, and preserved Unlighthouse plus documented transfer, image, JavaScript, CSS, LCP, INP, and CLS budgets; failures are fixed in this slice without weakening gates (DEC-012).

Traces: FR-002, FR-003, FR-013, FR-015, FR-016; NFR-001, NFR-002, NFR-003, NFR-004, NFR-005, NFR-007, NFR-008; DEC-002, DEC-008, DEC-010, DEC-011, DEC-012, DEC-013, SUBDEC-004.

## Reopen History

### 2026-07-24 — review failed → restart at red (tests)
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

### 2026-07-24 — review failed → restart at red (tests)
# Issue Review 02: Explore the bilingual Paros and Antiparos editorial journey

Date: 2026-07-25
Reviewer: fresh independent `jzgreekrev` code-review agent
Issue: `02-explore-paros-editorial`
Verdict: `FAIL`
Route: `red`

## Scope

Reviewed issue 2 at fixed point `0a3d7a4224b6d0f648edc39abfc5b5e14314efd8` on `feat/jz-ralph-workflow` plus the final dirty-worktree snapshot. Because the implementation is partly untracked, the reviewed diff is the complete live issue-owned file content and tracked diff for:

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
- `tests/unit/components/showcase-media.test.tsx`
- `tests/unit/content/showcase-content.test.ts`
- `tests/unit/routes/showcase-routes.test.ts`
- `tests/e2e/localization-and-quality.spec.ts`
- `tests/e2e/accessibility.spec.ts`
- `unlighthouse.config.ts`

Also inspected fixed-boundary neighbours `content/shared/media.json`, `i18n/navigation.ts`, `i18n/routing.ts`, `next.config.ts`, `app/[locale]/layout.tsx`, `tests/e2e/browser-guards.ts`, `tests/unit/design/showcase-token-contract.test.ts`, and `package.json`.

Read root `AGENTS.md` and `NEXT.md`; feature `AGENTS.md`, `PRD.md`, and complete approved `SPEC.md`; issue `issue.md` and `change-contract.md`; live `jz-implement-contract` `SKILL.md` and all five required references; implementation attempts 02 and 03; immutable review 01; the project quality-review skill/checklists; and the inherited Home operator-exception evidence. `features-cli docs current` and `features-cli progress --feature greek-essence-showcase --json` independently confirmed frontier `review-issue`, issue 2 `in-review`. Resolved depth is Tier 2 — Prototype by direct operator instruction, consistent with SPEC `implementation_depth: 2` and project default.

The unrelated Ralph/JZ rebuild, feature workflow/status, issue-1 evidence, generated `.playwright-cli`, plan, signals, and other dirty changes were preserved and excluded. No source, test, contract, lifecycle, signal, visual-review, Git-history, remote, deployment, or unrelated mutation was performed. This report is code review only and does not provide visual certification.

## Standards Verdict

`FAIL`. The live destination implementation remains static-first, shallow, bilingual, schema-backed, metadata-complete, private-prototype-safe, and free of observed PII, credentials, unsafe runtime content, successor form implementation, broader catalogue scope, or unsupported operational claims. Both localized routes render exactly six destination sections, preserve route identity, expose the literal allow-listed destination context, use the established CSS token foundation, retain pending-media neutral fallbacks, build as SSG, and pass the independently rerun lint/type/content/unit/build/browser/axe gates below.

Review 01 F-02's production behavior is now present: `resolveMediaFromManifest` defaults to real `existsSync`, incomplete or absent approved files fail closed, and approved hero/card classes are connected to explicit width/aspect/object-fit/positioning CSS while all three live destination IDs remain pending fallbacks. However, its geometry regression test is not strong enough to prove those CSS rules remain present or correct.

Review 01 F-01 and F-03 are only partially repaired. The locale validator now compares stable values between locales, but still accepts an equally wrong route/context pairing in both locales. The new browser test exercises both Home-to-Paros directions and several destination boundaries, but it omits contract-named destination-only zoom, complete security-header, and compact-menu close/focus-return coverage. These are named accepted behavior and focused regression seams, not optional higher-tier hardening.

Global formatting remains `FAIL`, exit 1, on exactly eight preserved unrelated files. `check:all` remains `FAIL`, exit 1, at that initial formatting step. Unlighthouse was not rerun after repair and is not called green. The inherited Home performance/LCP gate remains technically RED under the direct operator Home exception. The present repair changes no live approved media and only adds marginal CSS/build-time validation work, so the documented exception and current direct marginal-metric practicality instruction are sufficient not to create a separate performance blocker; they do not waive the destination defects below or convert any failed/skipped command to PASS.

## Spec And Contract Verdict

`FAIL`. Direct source/content inspection and executable checks prove the original six-section composition, natural EN/EL content, culture/gastronomy coverage, stable live IDs, pending fallback, fixed localized route pair, current navigation, localized metadata/canonicals/alternates/noindex, static generation, guarded browser cleanliness, axe results, and literal contextual CTA in the actual fixtures. TDD evidence for F-01/F-02 includes valid behavior-level RED failures after setup corrections followed by GREEN. F-03's temporary bounded mutation is acceptable sensitivity evidence for the current-nav assertion because the pre-existing production behavior was already correct; it does not prove the matrix cases that were never asserted.

The remaining failures are at the contract's existing content and browser seams and require no scope expansion.

## Blocking Findings

### F-01: Stable parity still does not validate CTA route/context semantics

- **Severity:** High / blocking correctness and focused-test gap.
- **Location:** `content/schemas/showcase.ts:3-8`; `lib/content.ts:44-62,76-98`; `lib/routes.ts:24-35`; `tests/unit/content/showcase-content.test.ts:102-136`; `tests/unit/routes/showcase-routes.test.ts:1-18`.
- **Requirement:** Review 01 F-01 required RED coverage and enforcement for CTA route/context semantics, not only cross-locale equality. Change contract lines 52, 62-65, 85-90 require the destination context to be carried only into the localized Plan My Trip URL and Home links to carry no query. SPEC §6.2 lines 441-448 and §7.3 lines 663-720 fix that semantic relationship.
- **Evidence / reproduction:** `ctaSchema` independently permits every route ID with either `null` or `"paros-antiparos"`. `stableValues` only proves EN and EL contain equal values. If both in-memory locale fixtures change the Paros final CTA to `{routeId:"home", destinationContext:"paros-antiparos"}`, schema parsing, known-media checks, and stable-value comparison all still pass. `getCtaPathname` then emits `/?destination=paros-antiparos`. The repair test mutates only one locale at a time, so it proves parity drift rejection but not semantic validity; the route unit file never exercises `getCtaPathname`.
- **Impact:** A synchronized bilingual content edit can redirect the accepted destination planning CTA to Home, Paros, or confirmation while carrying the query, and all current build-time and unit gates remain green. Actual live fixtures are correct, but the named public content seam remains fail-open to a realistic editorial/config regression.
- **Required correction:** Add a RED test using equal EN/EL controlled fixtures that pairs `destinationContext:"paros-antiparos"` with a non-`plan-my-trip` route, plus the inverse invalid destination CTA context case if represented at the same seam. Enforce the accepted CTA relationship in the public schema/validator or a comparably central typed boundary. Add public `getCtaPathname` coverage proving contextual output is only the Plan My Trip path and context-free Home/destination links remain query-free. Do not broaden the route API or implement the form.
- **Verification:** Show the controlled equal-locale semantic fixture fails before correction and passes afterward; rerun focused content/route tests, `pnpm validate:content`, `pnpm test:unit`, `pnpm typecheck`, and `pnpm build`.

### F-02: Approved-media geometry regression test proves class names, not geometry

- **Severity:** Medium / blocking focused-test gap.
- **Location:** `tests/unit/components/showcase-media.test.tsx:21-31`; production rules at `app/globals.css` under `.hero .showcase-media--hero`, `.split .showcase-media--card`, and `.media-card .showcase-media--card`.
- **Requirement:** Review 01 F-02 required a RED seam/component test for approved hero/card rendering geometry and verification in stable hero/card containers. Change contract lines 53, 79-83, 103-108 and SPEC §7.3 lines 705-720 require approved media to retain intrinsic/focal data and stable responsive presentation equivalent to the intended fallback slots.
- **Evidence / reproduction:** The new two-case unit test asserts only that the image has `showcase-media` and `showcase-media--hero|card`. It remains green if every corresponding CSS rule is deleted, or if `object-fit`, absolute hero fill, card width/aspect ratio, or height behavior regresses. Current destination E2E cannot cover this state because the authoritative manifest intentionally keeps every live destination asset pending. Direct source inspection confirms the CSS is currently present, so this finding is test protection rather than a claim that current fallback geometry is visually broken.
- **Impact:** The exact approved-state regression identified in review 01 can return while content, component, build, compact/wide, full E2E, and axe checks all pass. This is a named realistic boundary, not a speculative media matrix.
- **Required correction:** Strengthen the focused approved-state test at the established seam so it proves the required hero fill/crop and card width/aspect/crop declarations, for example with a bounded static CSS contract assertion tied to the emitted variant classes or a controlled approved-state browser fixture that does not promote live media. Preserve current pending fallback and do not perform visual certification in code review.
- **Verification:** Demonstrate the strengthened test fails when one required hero/card geometry declaration is removed or mutated and passes with the final rules; rerun the component/content tests, focused Prettier, lint, typecheck, build, and compact/wide destination suites.

### F-03: The guarded destination browser matrix still omits named contract cases

- **Severity:** Medium / blocking focused-test gap.
- **Location:** `tests/e2e/localization-and-quality.spec.ts:244-314,354-412`.
- **Requirement:** Review 01 F-03 and change contract lines 93-107 and 113-118 require complete destination response headers, destination compact-menu close/focus behavior, reduced motion, 200% zoom, and no-overflow checks alongside both localized Home-to-Paros and switch directions. Issue acceptance lines 22-23 require focused proof of the integrated compact/wide destination journey.
- **Evidence / reproduction:** The new destination test correctly covers EN and EL Home navigation, both switch directions, localized CTA hrefs, current state, CSP, `nosniff`, `DENY`, 320px overflow, reduced-motion transition duration, and a generic wide focus. It checks only three of the five required destination headers; `Referrer-Policy` and `Permissions-Policy` remain asserted only by the Home-only header test at lines 354-369. It never sets a destination route to the existing 195px 200%-zoom equivalent; the 195px helper is used only after `page.goto("/el")` and `page.goto("/en")` at lines 389-412. Escape/outside close and trigger focus return are likewise exercised only from `/en` Home at lines 371-387, not on either destination route. Browser guards do run, but they do not supply these missing behavior assertions.
- **Impact:** A destination-specific regression in the complete header policy, zoom overflow, or compact-menu close/focus behavior can ship while the newly named destination matrix and all rerun E2E/axe commands remain green.
- **Required correction:** Add the missing assertions to the existing guarded destination matrix without duplicating the whole site suite: check all five required headers on both destination responses; exercise the established compact menu's Escape/outside close and trigger focus return on a destination route; and run the exact 195px equivalent no-overflow probe for EN and EL destination routes. Keep the existing 390/1440 project coverage, 320 realistic boundary, reduced-motion assertion, and browser guards.
- **Verification:** Show bounded temporary mutations/removals make each new assertion fail, restore production, then rerun the focused test under `chromium-compact` and `chromium-wide`, the complete localization/accessibility files, `pnpm test:e2e`, and `pnpm test:a11y`.

## Non-Blocking Findings

- The actual English/Greek final CTA labels remain understandable provisional copy. A later editorial pass could improve idiomatic phrasing, but this is not a Tier-2 blocker.
- Object-key ordering in `stableValues` follows source insertion order rather than sorting like `shape`. Current schema-parsed fixtures have aligned key order and no observed defect; normal JSON edits should preserve it. Sorting could make the validator less order-sensitive later, but no speculative refactor is required for this issue.

## Verification Considered

- `features-cli docs current --feature greek-essence-showcase` — `PASS`, exit 0; frontier `review-issue`, issue 2.
- `features-cli progress --feature greek-essence-showcase --json` — `PASS`, exit 0; issue 2 is the sole `in-review` issue and resumable issue.
- `pnpm lint` — `PASS`, exit 0; full ESLint completed with no findings.
- `pnpm typecheck` — `PASS`, exit 0.
- `pnpm validate:content` — `PASS`, exit 0; reported EN/EL validation with media approval checks, subject to F-01.
- `pnpm test:unit` — `PASS`, exit 0; 8 files / 37 tests, subject to F-01 and F-02 test gaps.
- `pnpm build` — `PASS`, exit 0; 10 static pages generated, including both localized destination routes as SSG; no application dynamic boundary was added.
- Focused `pnpm exec prettier --check` over the 21 reviewed issue-owned production/content/test/config files — `PASS`, exit 0; all matched files use Prettier style.
- Issue-scoped `git diff --check -- <21 reviewed paths>` — `PASS`, exit 0.
- `pnpm format:check` — `FAIL`, exit 1; exactly eight preserved unrelated files failed: one `.hermes/plans` Markdown file and seven generated `.playwright-cli/*.yml` files. No issue-owned file failed focused Prettier.
- `pnpm exec playwright test --project=chromium-compact --project=chromium-wide tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` — `PASS`, exit 0; 31 passed / 1 expected wide-project compact-menu skip, subject to F-03's missing matrix assertions.
- `pnpm test:e2e` — `PASS`, exit 0; 46 passed / 2 expected non-compact menu skips across compact, medium, and wide.
- `pnpm test:a11y` — `PASS`, exit 0; 18 passed across compact, medium, and wide, including both destination locales.
- `pnpm check:all` — `FAIL`, exit 1 at the initial global `format:check`; build/E2E/a11y/Unlighthouse did not run inside this chained invocation. Their separate results are reported independently.
- `pnpm quality:unlighthouse` — `NOT RERUN` after repair by direct operator instruction. Immutable prior evidence remains technically `FAIL`, exit 1: destination performance scores were `0.91` with other destination categories `1.0`; inherited Home included `/en` performance `0.89` and LCP `2693.751ms`, while historical operator-exception evidence records EN LCP `2547.223ms > 2500ms`. None is called green.
- TDD evidence — F-01 and F-02 behavior-level RED failures are valid after documented setup corrections, followed by targeted GREEN. F-03's temporary current-nav mutation validly proves that one assertion's sensitivity, but does not cover F-03's omitted destination matrix cases. No evidence of test deletion, threshold lowering, axe weakening, viewport reduction, or browser-guard relaxation was found.

## Required Route

`red`. Preserve reviews 01 and 02 unchanged. Reopen issue 2 at RED and add focused failing tests for F-01 through F-03 at the existing public content/media/browser seams before repairing or strengthening implementation. Do not self-convert this failure to approval or patch findings while the issue remains in review. Require a fresh independent code-review attempt after the next RED → GREEN repair. The mandatory visual review remains downstream of a passing code review.

### 2026-07-24 — review failed → restart at red (tests)
# Issue Review 03: Explore the bilingual Paros and Antiparos editorial journey

Date: 2026-07-25
Reviewer: fresh independent `jzgreekrev` code-review agent
Issue: `02-explore-paros-editorial`
Verdict: `FAIL`
Route: `red`

## Scope

Reviewed issue 2 at fixed point `0a3d7a4224b6d0f648edc39abfc5b5e14314efd8` on `feat/jz-ralph-workflow` plus the complete live dirty-worktree issue-owned fixed point. Because many source files are untracked, the reviewed diff is the tracked diff plus the complete current contents of:

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
- `tests/unit/components/showcase-media.test.tsx`
- `tests/unit/content/showcase-content.test.ts`
- `tests/unit/design/showcase-media-geometry-contract.test.ts`
- `tests/unit/routes/showcase-routes.test.ts`
- `tests/e2e/localization-and-quality.spec.ts`
- `tests/e2e/accessibility.spec.ts`
- `unlighthouse.config.ts`

Also inspected the fixed-boundary neighbours `content/shared/media.json`, `i18n/navigation.ts`, `i18n/routing.ts`, `next.config.ts`, `app/[locale]/layout.tsx`, `tests/e2e/browser-guards.ts`, `playwright.config.ts`, `package.json`, and the established token/component tests.

Read root `AGENTS.md` and `NEXT.md`; feature `AGENTS.md`, `PRD.md`, and the complete approved `SPEC.md`; issue `issue.md` and `change-contract.md`; immutable reviews 01 and 02; `.Ralph/implementation-attempt-03.md` and `.Ralph/implementation-attempt-04.md`; the live `jz-implement-contract` skill and all five references; the repository-approved `greek-essence-quality-review` skill and all five checklists; the approved tooling baseline; and relevant testing/quality documentation. `features-cli docs current --feature greek-essence-showcase` and `features-cli progress --feature greek-essence-showcase --json` independently confirmed frontier `review-issue`, issue 2 `in-review`. Resolved depth is Tier 2 — Prototype by direct operator instruction, consistent with SPEC `implementation_depth: 2` and the project default.

The unrelated Ralph/JZ rebuild, plan, generated `.playwright-cli`, signal/workflow, issue-1, and other dirty-worktree changes were preserved and excluded. No production, test, contract, lifecycle, signal, implementation-report, visual-review, Git-history, remote, deployment, credential, or unrelated mutation was performed. This report is code review only and does not provide visual certification.

## Standards Verdict

`FAIL`. The live destination implementation remains static-first, shallow, bilingual, metadata-complete, private-prototype-safe, responsive at the exercised boundaries, and free of observed PII, credentials, unsafe runtime content, successor form implementation, broader catalogue scope, or unsupported operational claims. Both localized routes build as SSG, render the exact six destination sections, preserve route identity, use the established semantic token foundation, retain pending-media neutral fallbacks, and pass the independently rerun lint, type, live-content, unit, build, focused browser, full E2E, and axe checks recorded below.

Review 02 F-02 and F-03 are repaired at their named seams. The public approved-media resolver defaults to real `existsSync`, controlled incomplete or absent approved files fail closed, approved hero/card variant classes connect to a static CSS geometry contract, and all live destination media remains pending fallback. The guarded destination matrix now checks all five required headers on both locales, exact 195 px zoom-equivalent no-overflow in both locales, both Home-to-Paros and locale-switch directions, reduced motion, current state, and compact destination Escape/outside close with trigger focus return.

Review 02 F-01 is repaired in `validateShowcaseContentPair` and `getCtaPathname`, but the repository's separately implemented `pnpm validate:content` boundary still accepts the same equal-locale invalid Paros final-CTA pairing. That is a named required gate and central-validation maintainability defect, so standards approval is withheld.

Global `pnpm format:check` remains `FAIL`, exit 1, on exactly the same eight preserved unrelated files. `pnpm check:all` remains `FAIL`, exit 1, at that initial formatting step. `pnpm quality:unlighthouse` remains technically `FAIL`, exit 1: all four scanned Home/destination routes met score budgets, but `/en` LCP was `2565.43ms` against the unchanged `<=2500ms` assertion. The inherited Home exception permits completion consideration but does not turn that command or metric green. None of these inherited failures is reclassified as a pass or used to waive the blocking issue-owned finding below.

## Spec And Contract Verdict

`FAIL`. Direct source/content inspection and executable checks prove the required six-section composition, EN/EL editorial coverage, culture/gastronomy content, stable live IDs, pending fallbacks, localized metadata/canonicals/alternates/noindex, static generation, guarded browser cleanliness, axe results, literal allow-listed contextual CTA output, and no observed privacy, security, localization, claims, scope, or threshold breach.

However, change-contract lines 62 and 72-77/111-118 name both `getShowcaseContent(locale)` and `pnpm validate:content` as the public build-time content seam and require controlled invalid route/context pairings to fail. The live validator command does not share or reproduce the repaired positional Paros final-CTA invariant. Required focused validation is therefore incomplete even though the current fixtures are valid and `pnpm build` catches the invalid state through `lib/content.ts`.

## Blocking Findings

### F-01: `pnpm validate:content` still accepts an equal-locale invalid Paros final CTA

- **Severity:** High / blocking required-gate correctness and maintainability defect.
- **Location:** `scripts/validate-content.mjs:4-17,23-69`; repaired but disconnected central boundary at `lib/content.ts:76-109`; positional schema context at `content/schemas/showcase.ts:3-16,67-94`; missing command-level regression coverage at `tests/unit/content/showcase-content.test.ts:142-166`.
- **Requirement:** Review 02 F-01 requires exact Paros final-CTA route/context semantics for equal EN/EL fixtures. Change contract lines 62, 72-77, 85-90, and 111-118 require both the public loader and `pnpm validate:content` to reject controlled route/context defects. SPEC §6.2 fixes the contextual planning destination, and §7.3 requires the content validator to reject invalid route semantics. NFR-008 requires one maintainable content boundary rather than divergent validation behavior.
- **Evidence / reproduction:** `validateShowcaseContentPair` now correctly calls `validateDestinationCta` for each locale and the focused equal-locale unit cases pass. `getCtaPathname` also rejects destination context on non-Plan routes and emits only `/plan-my-trip?destination=paros-antiparos`. But `scripts/validate-content.mjs` independently parses `showcaseContentSchema`, compares shape/stable-value parity, checks Greek presence, and checks known media; it never applies `validateDestinationCta` or an equivalent positional rule. The general CTA schema intentionally permits a context-free `plan-my-trip` CTA for Home. A read-only in-memory probe changed both locale fixtures' `paros.finalCta` to `{routeId:"plan-my-trip", destinationContext:null}` and ran every relevant script predicate. It exited 0 and reported `{"schemaAccepted":true,"shapeEqual":true,"stableValuesEqual":true,"greekPresent":true,...}`. Therefore `pnpm validate:content` would print success for this equal-locale invalid destination final CTA, while `pnpm build` would fail later only because it imports the separate loader.
- **Impact:** The repository's dedicated content gate can produce a false green for the exact synchronized route/context regression identified by the prior immutable review. The duplicated validator has already drifted from the central public content boundary, so editors or future focused runs can trust a passing command that has not enforced the contract.
- **Required correction:** First add a RED command-level or script-seam test proving `pnpm validate:content` rejects the equal-EN/EL `plan-my-trip`/`null` Paros final CTA (and preserves the non-Plan/context rejection). Then make the command use the central paired validator or otherwise share the exact invariant without weakening the general context-free Home CTA behavior. Do not broaden the route API or implement successor form behavior.
- **Verification:** Demonstrate the new command/script assertion fails before correction and passes afterward; rerun the focused content/route tests, `pnpm validate:content`, `pnpm test:unit`, `pnpm lint`, `pnpm typecheck`, and `pnpm build`, followed by a fresh independent review.

## Non-Blocking Findings

- `.Ralph/implementation-attempt-04.md` overstates current unit counts: it records 3 focused files / 31 tests and 9 files / 43 tests, while this fresh fixed-point run observed the corresponding four-file focused set as 32 tests, the three-file subset as 30 by current file counts, and the full suite as 9 files / 42 tests. This does not invalidate real passing behavior, but the eventual implementation report must use fresh actual counts rather than copying the attempt summary.
- The actual EN/EL final CTA labels remain understandable provisional copy. A later editorial pass could improve idiomatic phrasing, but this is not a Tier-2 blocker.

## Verification Considered

- `features-cli docs current --feature greek-essence-showcase` — `PASS`, exit 0; frontier `review-issue`, issue 2.
- `features-cli progress --feature greek-essence-showcase --json` — `PASS`, exit 0; issue 2 is the sole `in-review` issue and resumable issue.
- `git status --short` plus issue-scoped tracked diff/stat inspection — `PASS`, exit 0; confirmed the intentionally dirty fixed point and partially untracked issue-owned source. No worktree mutation was made.
- `test ! -e .scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/reviews/03-review.md` before writing — `PASS`, exit 0; the immutable attempt path was available.
- `pnpm lint` — `PASS`, exit 0; full ESLint completed with no findings.
- `pnpm typecheck` — `PASS`, exit 0.
- `pnpm validate:content` — `PASS`, exit 0 for the actual EN/EL fixtures; reported media approval checks, subject to blocking F-01's controlled equal-locale false-green case.
- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/components/showcase-media.test.tsx tests/unit/design/showcase-media-geometry-contract.test.ts tests/unit/routes/showcase-routes.test.ts --reporter=verbose` — `PASS`, exit 0; 4 files / 32 tests, including both equal-locale CTA cases, public `getCtaPathname`, missing approved file, emitted variants, and static hero/card geometry.
- `pnpm test:unit` — `PASS`, exit 0; 9 files / 42 tests.
- `pnpm build` — `PASS`, exit 0; 10 static pages generated, including both localized Paros routes as SSG, with no new application dynamic boundary.
- Focused `pnpm exec prettier --check` over all 22 reviewed issue-owned production/content/test/config paths — `PASS`, exit 0.
- Issue-scoped `git diff --check -- <22 reviewed paths>` — `PASS`, exit 0.
- `pnpm format:check` — `FAIL`, exit 1; exactly eight preserved unrelated files failed: one `.hermes/plans` Markdown file and seven generated `.playwright-cli/*.yml` files. No issue-owned path failed focused Prettier.
- `pnpm exec playwright test --project=chromium-compact --project=chromium-wide tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` — `PASS`, exit 0; 34 passed / 2 expected wide-project compact-interaction skips.
- `pnpm test:e2e` — `PASS`, exit 0; 50 passed / 4 expected medium/wide compact-interaction skips across compact, medium, and wide.
- `pnpm test:a11y` — `PASS`, exit 0; 18 passed across compact, medium, and wide, including both destination locales.
- Read-only scan of the 22 reviewed paths for credential/dangerous-code/debug/conflict-marker patterns — command exit 0; one expected `console.log` was the content-validator success output, with no credential, unsafe-eval, raw-HTML, conflict-marker, or debug-code finding.
- Read-only equal-locale validator probe using the actual schema and `scripts/validate-content.mjs` predicates — command exit 0; reported `schemaAccepted:true`, `shapeEqual:true`, `stableValuesEqual:true`, and `greekPresent:true` for the invalid `paros.finalCta` `plan-my-trip`/`null` pairing, reproducing F-01.
- `pnpm quality:unlighthouse` — `FAIL`, exit 1; Unlighthouse score assertions passed for 4 routes: `/el` performance `0.92`, `/el/destinations/paros-antiparos` `0.91`, `/en` `0.91`, `/en/destinations/paros-antiparos` `0.92`, with accessibility/best-practices/SEO all `1.0`. The unchanged strict assertion then failed at `/en` LCP `2565.43ms > 2500ms`. This remains technically RED under the inherited direct operator exception and is not called a pass.
- `pnpm check:all` — `FAIL`, exit 1 at the inherited global `format:check`; later chained build/E2E/a11y/Unlighthouse commands did not run inside that aggregate invocation. Their separate outcomes are reported independently.
- TDD evidence — attempt 04 records a valid behavior-level RED for the central `validateShowcaseContentPair` equal-locale `plan-my-trip`/`null` case and subsequent GREEN. The current focused tests confirm F-02/F-03 repair behavior. No command/script-level RED exists for F-01's still-divergent `pnpm validate:content` seam.

## Required Route

`red`. Preserve reviews 01, 02, and this review 03 unchanged. Reopen issue 2 at RED and add a focused failing test at the existing `pnpm validate:content`/script seam before repairing the divergent validator. Do not patch this finding while the issue remains in review, do not self-convert this failure to approval, and require a fresh independent code-review attempt after RED → GREEN repair. The mandatory visual review remains downstream of a passing code review.

### 2026-07-24 — review failed → restart at red (tests)
# Issue Review 04: Explore the bilingual Paros and Antiparos editorial journey

Date: 2026-07-25
Reviewer: fresh independent `jzgreekrev` code-review agent
Issue: `02-explore-paros-editorial`
Verdict: `FAIL`
Route: `red`

## Scope

Reviewed issue 2 at fixed point `0a3d7a4224b6d0f648edc39abfc5b5e14314efd8` on `feat/jz-ralph-workflow` plus the complete live dirty-worktree issue-owned fixed point after repair attempt 05. Because much of the implementation is untracked, the reviewed diff is the tracked diff plus the complete current contents of:

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
- `tests/unit/components/showcase-media.test.tsx`
- `tests/unit/content/showcase-content.test.ts`
- `tests/unit/design/showcase-media-geometry-contract.test.ts`
- `tests/unit/routes/showcase-routes.test.ts`
- `tests/e2e/localization-and-quality.spec.ts`
- `tests/e2e/accessibility.spec.ts`
- `unlighthouse.config.ts`

The tracked portion is five files with 916 insertions and 139 deletions; the remaining 17 issue-owned files are untracked and were reviewed as complete file contents. Also inspected the fixed-boundary neighbours `content/shared/media.json`, `i18n/navigation.ts`, `i18n/routing.ts`, `next.config.ts`, `app/[locale]/layout.tsx`, `tests/e2e/browser-guards.ts`, `playwright.config.ts`, `vitest.config.mts`, `package.json`, `tsconfig.json`, and the relevant token/component tests.

Read root `AGENTS.md` and `NEXT.md`; feature `AGENTS.md`, `PRD.md`, and approved `SPEC.md`; issue `issue.md` and `change-contract.md`; immutable reviews 01, 02, and 03; `.Ralph/implementation-attempt-04.md` and `.Ralph/implementation-attempt-05.md`; the live `jz-implement-contract` skill and all five references; the repository-approved `greek-essence-quality-review` skill and all five checklists; the approved tooling baseline; and relevant routing, responsive, accessibility, SEO, media, and testing documentation. `features-cli docs current --feature greek-essence-showcase` and `features-cli progress --feature greek-essence-showcase --json` independently confirmed frontier `review-issue`, issue 2 `in-review`. Resolved depth is Tier 2 — Prototype by direct operator instruction, consistent with SPEC `implementation_depth: 2` and the project default.

The unrelated Ralph/JZ rebuild, plan, generated `.playwright-cli`, signal/workflow, issue-1, and other dirty-worktree changes were preserved and excluded. No production, test, contract, lifecycle, signal, implementation-report, visual-review, Git-history, remote, deployment, credential, or unrelated mutation was performed. The sole new artifact is this immutable review. This is code review only and does not provide visual certification.

## Standards Verdict

`FAIL`. Review 03 F-01 is functionally repaired at both required validation boundaries. `validateParosFinalCta` is one shared exact positional invariant; both `validateShowcaseContentPair` and `scripts/validate-content.mjs` call it after schema parsing. The live fixtures retain valid context-free Home CTAs, and the dedicated `pnpm validate:content` command exits 0. Focused tests reject both equal-locale invalid Paros final-CTA pairings: a non-Plan route carrying `paros-antiparos`, and `plan-my-trip` without that context. Public route coverage still proves context-free Home/Paros output is query-free and only the Plan My Trip CTA emits the allow-listed query.

Review 03's accepted F-02 and F-03 repairs remain intact. The approved-media resolver still defaults to real file existence, controlled incomplete/missing approved media fails closed, emitted hero/card classes remain tied to the static geometry contract, and live destination media stays pending fallback. The unchanged guarded destination matrix still contains all five response-header assertions, both locale Home-to-Paros and switch directions, exact 195 px zoom-equivalent overflow checks, reduced-motion coverage, current state, and destination compact-menu Escape/outside close with trigger focus return. Attempt 05 changed no rendering source, so review 03's browser and axe evidence is reusable rather than repeated.

The new command regression is not acceptable as a repository test, however. It writes invalid JSON directly over both live authoritative content fixtures, runs a child command while those source files are invalid, and relies on an in-process `finally` to write the originals back. This creates a realistic race and worktree-corruption boundary under the repository's normal parallel test tooling and ordinary interruption behavior. A focused test required by the contract may not obtain coverage by making the source tree transiently invalid.

No contract hard-wall, quality threshold, bilingual/static/privacy/accessibility/security boundary, rendering scope, or unsupported-claim regression was otherwise found. Global formatting remains `FAIL`, exit 1, on exactly the same eight preserved unrelated files. The latest Unlighthouse evidence remains technically `FAIL`, exit 1: review 03 recorded all four Home/destination score budgets passing but `/en` LCP at `2565.43ms > 2500ms`; the inherited direct operator exception does not turn that command or metric green. `check:all` remains historically `FAIL`, exit 1, at its initial global formatting step and was not repeated because the operator explicitly excluded that expensive deterministic rerun.

## Spec And Contract Verdict

`FAIL`. Direct source/content inspection and executable checks prove the six-section EN/EL destination composition, natural bilingual editorial content, culture/gastronomy coverage, stable IDs, pending-media fallback, fixed localized route identity, localized metadata/canonicals/alternates/noindex, static generation, exact allow-listed contextual CTA, and one shared Paros final-CTA invariant. The actual fixtures and dedicated content command are correct.

The remaining defect is in the required command-level regression itself. Change-contract lines 62, 72–77, and 111–118 require focused validation at `getShowcaseContent(locale)` and `pnpm validate:content`; NFR-008 requires a maintainable shallow boundary; root `AGENTS.md` requires realistic-boundary correctness and worktree preservation. Tier 2 does not require a generalized harness, lock service, or production infrastructure, but it does require a small isolated script seam because the current test can realistically race another Vitest worker, build/content command, editor, watcher, or interrupted test process.

## Blocking Findings

### F-01: The command-level regression rewrites authoritative live fixtures and can race or corrupt the worktree

- **Severity:** High / blocking test-safety, determinism, and maintainability defect.
- **Location:** `tests/unit/content/showcase-content.test.ts:1-3,19-52,181-194`; parallel test configuration at `vitest.config.mts:13-17`; command seam at `scripts/validate-content.mjs:9-23`.
- **Requirement:** Review 03 F-01 requires a reliable command/script-level regression for both equal-locale invalid Paros CTA pairings while preserving valid context-free Home CTA behavior. Change contract lines 62, 72-77, 85-90, and 111-118 require trustworthy focused content-command evidence. Root `AGENTS.md` lines 21-33 and 85-91 require maintainable Tier-2 tests, required gates, and worktree preservation; NFR-008 requires a shallow maintainable content boundary.
- **Evidence / reproduction:** `runContentValidationWithInvalidParosCtas` reads the real `content/en/showcase.json` and `content/el/showcase.json`, then overwrites them one after the other at lines 33-42. It leaves the source tree in a mixed or fully invalid state while `spawnSync` runs the validator at lines 43-46, then restores each source file one after the other in `finally` at lines 47-50. The live Vitest CLI reports `--fileParallelism` defaults to `true`, and `vitest.config.mts` does not disable it. Therefore another worker or independently invoked `pnpm validate:content`/`pnpm build` can observe one or both invalid fixtures. `finally` covers ordinary JavaScript exceptions but cannot restore after abrupt process termination such as forced stop, process kill, runtime crash, or machine interruption. A stop between either pair of writes can leave one or both authoritative untracked fixtures invalid. Both fresh successful test runs restored identical bytes—the EN SHA-256 stayed `6c826cc7a6bd782f0fa4322ee71f9dcddd2357e281ba2fbe1b0e6b250fea8e9e` and EL stayed `f9bc86ece8f5813a75d73d2ea8865b18ce2feff275ab01af92aaafa435ab5b5b`—but that proves only the normal path, not crash safety or concurrency safety.
- **Impact:** A normal parallel or interrupted unit run can make unrelated content tests, a build, or the dedicated content command fail nondeterministically; can trigger watchers against invalid source; and can leave the user's intentionally dirty, untracked authoritative fixtures corrupted. Because the files are untracked, ordinary Git restoration is not guaranteed. This is a realistic local/CI integrity risk, not speculative higher-tier hardening.
- **Required correction:** Keep the shared `validateParosFinalCta` invariant, but move the command regression to isolated inputs. Add the smallest script seam needed to validate a caller-supplied fixture root/paths or exported validation function, copy/write controlled EN/EL fixtures under a temporary directory, and invoke the same command logic there. Do not write `content/en/showcase.json` or `content/el/showcase.json` during tests. Prove both invalid equal-locale pairings fail and a valid pair with context-free Home CTAs passes. Avoid a generalized framework or locking layer; one bounded injectable fixture-root/function seam is sufficient at Tier 2.
- **Verification:** Add a RED safety/seam test before correction; then run the isolated command regression repeatedly with Vitest file parallelism enabled, verify source fixture hashes and mtimes remain unchanged, and rerun the four focused content/route/media/geometry files, `pnpm validate:content`, `pnpm test:unit`, `pnpm lint`, `pnpm typecheck`, `pnpm build`, focused Prettier, and focused diff check. Require a fresh independent code review afterward.

## Non-Blocking Findings

- The actual EN/EL final CTA labels remain understandable provisional copy. A later editorial pass could improve idiomatic phrasing, but this is not a Tier-2 blocker.

## Verification Considered

- `features-cli docs current --feature greek-essence-showcase` — `PASS`, exit 0; frontier `review-issue`, issue 2.
- `features-cli progress --feature greek-essence-showcase --json` — `PASS`, exit 0; issue 2 is the sole `in-review` and resumable issue.
- `test ! -e .scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/reviews/04-review.md` before writing — `PASS`, exit 0; immutable attempt path was available.
- `git status --short --untracked-files=all` plus issue-scoped tracked diff/stat and complete untracked-file inspection — `PASS`, exit 0; fixed point remained intentionally dirty and excluded unrelated work.
- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/components/showcase-media.test.tsx tests/unit/design/showcase-media-geometry-contract.test.ts tests/unit/routes/showcase-routes.test.ts --reporter=verbose` — `PASS`, exit 0; 4 files / 34 tests, including both loader and command-level equal-locale CTA cases, valid route output, pending/approved media boundaries, emitted variants, and static hero/card geometry. Subject to blocking F-01 because two tests transiently rewrote live source fixtures.
- SHA-256 before and after the focused run — command exit 0; EN remained `6c826cc7a6bd782f0fa4322ee71f9dcddd2357e281ba2fbe1b0e6b250fea8e9e`, EL remained `f9bc86ece8f5813a75d73d2ea8865b18ce2feff275ab01af92aaafa435ab5b5b`.
- `pnpm validate:content` — `PASS`, exit 0; printed `Showcase content validation passed for en/el with media approval checks` for the actual valid fixtures.
- `pnpm test:unit` — `PASS`, exit 0; 9 files / 44 tests. Subject to F-01's parallel/crash-safety defect. Fixture SHA-256 values were identical before and after this successful run.
- `pnpm lint` — `PASS`, exit 0; full ESLint completed with no findings.
- `pnpm typecheck` — `PASS`, exit 0.
- `pnpm build` — `PASS`, exit 0; 10 static pages generated, including both localized Paros routes as SSG, with no new dynamic application boundary.
- Focused `pnpm exec prettier --check` over all 22 reviewed issue-owned production/content/test/config paths — `PASS`, exit 0; all matched files use Prettier style.
- Issue-scoped `git diff --check -- <22 reviewed paths>` — `PASS`, exit 0; no tracked whitespace error. Seventeen reviewed paths are untracked, so focused Prettier is the substantive style check for those files.
- `pnpm format:check` — `FAIL`, exit 1; exactly eight preserved unrelated paths failed: `.hermes/plans/2026-07-24_174920-rebuild-ralph-for-jz-workflow.md` and seven generated `.playwright-cli/*.yml` files. No issue-owned path failed focused Prettier.
- Read-only dangerous-code/credential/conflict-marker scan over 22 issue-owned paths — command exit 0; no match was reported.
- `pnpm exec vitest --help --expand-help` — command exit 0; reported `--fileParallelism` default `true`, grounding F-01's normal parallel-run risk.
- Review 03 reusable rendering evidence: focused compact/wide localization plus accessibility files `PASS`, exit 0, 34 passed / 2 expected wide compact-interaction skips; full E2E `PASS`, exit 0, 50 passed / 4 expected medium/wide compact-interaction skips; a11y `PASS`, exit 0, 18 passed. Attempt 05 did not change rendering source or those tests.
- Review 03 latest Unlighthouse evidence — `FAIL`, exit 1; all four Home/destination score budgets passed, but `/en` LCP was `2565.43ms > 2500ms`. It remains technically RED under the inherited direct operator exception and is not called a pass.
- Review 03 latest `pnpm check:all` evidence — `FAIL`, exit 1 at the initial inherited global `format:check`; later chained commands did not run in that invocation. It was not repeated because it deterministically stops at the same eight unrelated paths and the operator excluded unnecessary expensive reruns.
- Worktree preservation after verification — command exit 0; final scoped status matched the reviewed tracked/untracked set, and both source fixture hashes matched their pre-test values.

## Required Route

`red`. Preserve reviews 01 through 04 unchanged. Reopen issue 2 at RED and replace the live-fixture rewrite with a bounded isolated command/script seam and focused safety regression. This is missing/unsafe test coverage at the required command seam, so the correct route is `red`, not `green` and not `ScopeExpansionRequest`. Do not patch the finding while the issue remains in review, do not self-convert this failure to approval, and require a fresh independent code-review attempt after RED → GREEN repair. The mandatory visual review remains downstream of a passing code review.
