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
