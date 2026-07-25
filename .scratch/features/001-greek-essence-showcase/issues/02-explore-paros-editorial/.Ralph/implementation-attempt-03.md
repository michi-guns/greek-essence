# Issue 02 Implementation Repair — Attempt 03

Date: 2026-07-25
Issue: `02-explore-paros-editorial`
Method: `tdd-solo`
Resolved depth: Tier 2 — Prototype
Scope: repair only immutable review 01 findings F-01 through F-03. No lifecycle, review, visual-review, signal, Git, remote, deployment, successor-surface, or unrelated-worktree mutation was made.

## RED → GREEN chronology

### F-01 — stable EN/EL parity

1. RED tests were added to `tests/unit/content/showcase-content.test.ts` for controlled Greek Paros drift in a collection ID, a known destination media ID, final CTA route, and final CTA context.
2. RED command: `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose`
3. RED result: exit 1; the collection-ID, known-media-ID, and valid CTA-route fixtures did not throw, proving the former type-only structure check allowed value drift. The initial fixture list lacked Home IDs and was corrected before the recorded RED; after correction, the four expected parity assertions failed for the missing stable-value behavior rather than setup.
4. GREEN implementation: `lib/content.ts` now validates schema/structure, validates referenced manifest IDs, then compares only stable identity values (`id`, `mediaId`, `routeId`, `destinationContext`) across locales. Translated prose remains unrestricted. `scripts/validate-content.mjs` performs the same stable-value build validation.
5. GREEN command: `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose`
6. GREEN result: exit 0; 1 file / 16 tests passed.

### F-02 — fail-closed approved media and stable presentation

1. RED seam/component tests were added:
   - `tests/unit/content/showcase-content.test.ts`: a fully approved controlled record whose physical file is absent must throw.
   - `tests/unit/components/showcase-media.test.tsx`: approved hero/card media must render their stable layout class.
2. RED command: `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/components/showcase-media.test.tsx`
3. RED result: exit 1; absent approved file was returned as approved, and both approved hero/card class assertions failed. An initial component import failure and unsupported matcher were test-setup failures and were repaired before the behavioral RED was recorded.
4. GREEN implementation: the public `resolveMediaFromManifest` now defaults to real `node:fs` `existsSync`; controlled injected predicates remain supported for unit seams. `ShowcaseMedia` has explicit hero/card variants, section callers select the appropriate variant, and `app/globals.css` gives approved hero/card media the same stable geometry/crop contract as their fallback slots. Pending fallback behavior was unchanged.
5. GREEN command: `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/components/showcase-media.test.tsx`
6. GREEN result: exit 0; 2 files / 19 tests passed. Live pending destination IDs continue through their existing fallback assertions.

### F-03 — destination browser matrix

1. RED browser coverage was added in `tests/e2e/localization-and-quality.spec.ts` for EN and EL Home → Paros navigation, both locale-switch directions, localized allow-listed CTA hrefs, current destination navigation, destination CSP/nosniff/frame headers, compact/wide no-overflow, focus, and reduced-motion boundaries.
2. The first run exposed compact-menu test setup (destination link was correctly hidden); the test was corrected to open the existing compact menu before activation/current-nav checks.
3. The new assertion passed against the intact implementation, so a bounded temporary test-only mutation removed the Paros `aria-current` implementation. RED command: `pnpm exec playwright test --project=chromium-compact tests/e2e/localization-and-quality.spec.ts --grep 'protects both localized'`.
4. RED result: exit 1; the EN destination current-nav assertion received no `aria-current="page"`. The exact existing implementation was restored immediately.
5. GREEN command: `pnpm exec playwright test --project=chromium-compact --project=chromium-wide tests/e2e/localization-and-quality.spec.ts --grep 'protects both localized'`
6. GREEN result: exit 0; 2 passed.

## Files changed

- `lib/content.ts` — stable bilingual value parity plus real approved-file existence predicate.
- `scripts/validate-content.mjs` — equivalent stable-value parity at the public content command.
- `components/sections/showcase-media.tsx` — explicit approved hero/card variant classes.
- `components/sections/home-sections.tsx`, `components/sections/paros-sections.tsx` — select stable hero/card media variants.
- `app/globals.css` — approved hero/card geometry/crop styling matching fallback slots.
- `tests/unit/content/showcase-content.test.ts` — F-01 and F-02 seams.
- `tests/unit/components/showcase-media.test.tsx` — approved hero/card component seam.
- `tests/e2e/localization-and-quality.spec.ts` — F-03 destination journey/responsive/security coverage.

## Verification

- `pnpm exec prettier --write ...issue-owned paths... && pnpm exec prettier --check ...same paths... && pnpm lint && pnpm typecheck && pnpm validate:content && pnpm test:unit && pnpm build` — PASS, exit 0. Focused Prettier passed; lint/typecheck/content passed; unit: 8 files / 37 tests; build generated 10 static pages including both localized Paros SSG routes.
- `pnpm exec playwright test --project=chromium-compact --project=chromium-wide tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` — PASS, exit 0; 31 passed / 1 expected compact-only wide skip.
- `pnpm test:e2e` — PASS, exit 0; 46 passed / 2 expected compact-only skips.
- `pnpm test:a11y` — PASS, exit 0; 18 passed.
- `git diff --check -- <issue-owned source/test paths>` — PASS, exit 0.
- `pnpm format:check` — FAIL, exit 1; exactly the preserved eight unrelated files remain: one `.hermes/plans` Markdown file and seven generated `.playwright-cli/*.yml` files. No issue-owned path failed focused Prettier.
- `pnpm check:all` — FAIL, exit 1 at the inherited global `format:check`; chained later aggregate steps did not run.

## Performance

`pnpm quality:unlighthouse` was not rerun in this repair. The repair does not enable live approved media (all destination records remain pending fallback), and immutable review 01/attempt 02 already records inherited strict Home performance failures, including historical EN LCP `2547.223ms > 2500ms` and the later `/en` `2693.751ms`. Per operator direction, the inherited expensive Home failure was not repeatedly rerun to chase a non-contract marginal metric; it remains technically RED and is not called green.

## Finding resolution and handoff

- F-01 resolved with stable ID/media/CTA semantic parity at loader and public validation seams.
- F-02 resolved with public actual-file fail-closed resolution and explicit approved hero/card geometry; pending fallback remains intact.
- F-03 resolved with both localized destination journeys and guarded compact/wide responsive/security assertions.

Issue implementation remains in progress and requires the next fresh independent code review. This implementer did not review, transition workflow state, create/modify review artifacts, or start any successor work.
