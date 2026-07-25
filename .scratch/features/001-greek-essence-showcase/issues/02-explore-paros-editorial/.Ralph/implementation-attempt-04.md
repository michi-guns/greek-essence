# Issue 02 Implementation Repair — Attempt 04

Date: 2026-07-25
Issue: `02-explore-paros-editorial`
Method: `tdd-solo`
Resolved depth: Tier 2 — Prototype
Scope: immutable review 02 findings F-01 through F-03 only. No lifecycle, review, visual-review, signal, Git, remote, deployment, successor-surface, or unrelated-worktree mutation was made.

## RED → GREEN chronology

### F-01 — equal-locale destination CTA route/context semantics

1. RED test added at the existing public `validateShowcaseContentPair` seam: an equal EN/EL Paros final CTA using `routeId: "plan-my-trip"` and `destinationContext: null` must be rejected. The existing paired case for a non-plan route with destination context remains covered. The existing public `getCtaPathname` unit test proves contextual output is only `/plan-my-trip?destination=paros-antiparos` and Home/Paros context-free output is query-free.
2. RED command: `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose`
3. RED result: exit 1; `rejects an equally invalid bilingual destination CTA pairing: Plan My Trip route without destination context` failed with `expected [Function] to throw an error`. This was a behavior failure, not a setup or syntax error.
4. GREEN repair: `lib/content.ts` now centrally validates that each parsed `paros.finalCta` is exactly `routeId: "plan-my-trip"` plus `destinationContext: "paros-antiparos"`, before accepted content is returned by the public paired validator. General context-free CTAs remain allowed for other content positions.
5. GREEN command: `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/components/showcase-media.test.tsx tests/unit/routes/showcase-routes.test.ts --reporter=verbose`
6. GREEN result: exit 0; 3 files / 31 tests passed.

### F-02 — approved media geometry regression protection

1. The resumed live issue-owned worktree already contained the review-02-required static CSS contract at `tests/unit/design/showcase-media-geometry-contract.test.ts`. It proves the emitted approved-media variants retain required hero fill/crop declarations and card width/aspect/height/crop declarations. The existing component seam continues to prove the `hero`/`card` variant classes are emitted; live destination IDs remain pending fallbacks.
2. No additional production repair was needed in this attempt: current `app/globals.css`, `ShowcaseMedia`, and the static contract already cover the review-02 requirement without promoting pending media or changing fallback behavior.
3. Verification command: `pnpm test:unit`
4. GREEN result: exit 0; 9 files / 43 tests, including `showcase-media-geometry-contract.test.ts` (2 tests) and `showcase-media.test.tsx` (3 tests).

### F-03 — guarded destination browser matrix

1. The resumed live issue-owned worktree already contained the review-02-required guarded browser assertions in `tests/e2e/localization-and-quality.spec.ts`: all five headers on both destination routes; exact 195px zoom-equivalent no-overflow on EN/EL; and compact destination Escape/outside closure with trigger focus return.
2. No additional production repair was needed in this attempt. Existing assertions preserve browser guards, compact/wide projects, 320px/reduced-motion boundaries, and both locale Home-to-Paros / route-switch coverage.
3. Focused command: `pnpm exec playwright test --project=chromium-compact --project=chromium-wide tests/e2e/localization-and-quality.spec.ts --grep 'protects destination headers|closes compact destination menus'`
4. GREEN result: exit 0; 3 passed / 1 expected wide-project compact-interaction skip.

## Files changed in this attempt

### Production

- `lib/content.ts` — central destination-final-CTA semantic validation.

### Tests

- `tests/unit/content/showcase-content.test.ts` — equal-EN/EL invalid destination CTA context test.

### Existing issue-owned repair seams reverified

- `tests/unit/routes/showcase-routes.test.ts`
- `tests/unit/components/showcase-media.test.tsx`
- `tests/unit/design/showcase-media-geometry-contract.test.ts`
- `tests/e2e/localization-and-quality.spec.ts`
- `app/globals.css`
- `components/sections/showcase-media.tsx`

### Supporting evidence

- `.scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/.Ralph/implementation-attempt-04.md`

## Verification

- `pnpm exec prettier --check lib/content.ts tests/unit/content/showcase-content.test.ts tests/unit/components/showcase-media.test.tsx tests/unit/design/showcase-media-geometry-contract.test.ts` — PASS, exit 0.
- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/components/showcase-media.test.tsx tests/unit/routes/showcase-routes.test.ts --reporter=verbose` — PASS, exit 0; 3 files / 31 tests.
- `pnpm lint` — PASS, exit 0.
- `pnpm typecheck` — PASS, exit 0.
- `pnpm validate:content` — PASS, exit 0; English/Greek content validation with media approval checks.
- `pnpm test:unit` — PASS, exit 0; 9 files / 43 tests.
- `pnpm build` — PASS, exit 0; 10 pages, including both localized Paros routes as SSG and no new dynamic application route.
- `pnpm exec playwright test --project=chromium-compact tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` — PASS, exit 0; 18 passed.
- `pnpm exec playwright test --project=chromium-wide tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts` — PASS, exit 0; 16 passed / 2 expected compact-only skips.
- `pnpm test:e2e` — PASS, exit 0; 50 passed / 4 expected compact-only skips.
- `pnpm test:a11y` — PASS, exit 0; 18 passed.
- `git diff --check -- lib/content.ts tests/unit/content/showcase-content.test.ts tests/unit/routes/showcase-routes.test.ts tests/unit/components/showcase-media.test.tsx tests/unit/design/showcase-media-geometry-contract.test.ts tests/e2e/localization-and-quality.spec.ts app/globals.css components/sections/showcase-media.tsx` — PASS, exit 0.
- `pnpm format:check` — FAIL, exit 1; exactly eight preserved unrelated files: `.hermes/plans/2026-07-24_174920-rebuild-ralph-for-jz-workflow.md` and seven generated `.playwright-cli/*.yml` files. No issue-owned path failed focused Prettier.
- `pnpm quality:unlighthouse` — FAIL, exit 1; Unlighthouse score budgets passed, but inherited `/en` LCP was `2502.126ms` against the strict `<=2500ms` assertion. This remains technically RED under the existing direct operator exception; no threshold was changed.
- `pnpm check:all` — FAIL, exit 1 at inherited global `format:check`; chained build/E2E/a11y/Unlighthouse steps did not execute in that aggregate invocation.

## Privacy and scope assurance

- Tests, browser output, and evidence use only static synthetic/provisional showcase content; no visitor, client, recipient, credential, or other PII was introduced.
- Pending media remains the intentional neutral `pending-approval` fallback. No media approval metadata, asset status, form, submission, email, confirmation, or other successor work was changed.
- The intentionally dirty worktree and all immutable reviews were preserved. No lifecycle state was transitioned.

## Handoff

F-01 is newly repaired and F-02/F-03’s already-present issue-owned repairs were reverified against review 02. Issue remains `in-progress`, Phase `red`, pending a fresh independent code review; this implementer did not self-review or transition status.
