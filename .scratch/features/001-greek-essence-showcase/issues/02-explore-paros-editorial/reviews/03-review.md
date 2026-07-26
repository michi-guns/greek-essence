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
