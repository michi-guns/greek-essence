# Issue Review 05: Explore the bilingual Paros and Antiparos editorial journey

Date: 2026-07-25
Reviewer: fresh independent `jzgreekrev` code-review agent
Issue: `02-explore-paros-editorial`
Verdict: `PASS`
Route: `PASS`

## Scope

Reviewed issue 2 at fixed point `0a3d7a4224b6d0f648edc39abfc5b5e14314efd8` on `feat/jz-ralph-workflow` plus the complete live dirty-worktree issue-owned fixed point after `tdd-solo` repair attempt 06. Resolved depth is Tier 2 — Prototype by direct operator instruction, consistent with SPEC front matter `implementation_depth: 2` and the repository default.

Because much of the implementation is untracked, the reviewed diff is the tracked diff plus the complete current contents of these 22 issue-owned production/content/test/config paths:

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

The tracked portion is five files with 916 insertions and 139 deletions; the other 17 reviewed implementation paths are untracked and were reviewed as complete files. Also inspected fixed-boundary neighbours `content/shared/media.json`, `i18n/navigation.ts`, `i18n/routing.ts`, `next.config.ts`, `app/[locale]/layout.tsx`, `tests/e2e/browser-guards.ts`, `playwright.config.ts`, `vitest.config.mts`, and `package.json`.

Read root `AGENTS.md` and `NEXT.md`; feature `AGENTS.md`, `PRD.md`, and the complete approved `SPEC.md`; issue `issue.md` and `change-contract.md`; immutable reviews 01 through 04; `.Ralph/implementation-attempt-04.md`, `implementation-attempt-05.md`, and `implementation-attempt-06.md`; the live `jz-implement-contract` skill and all five required references; the repository-approved `greek-essence-quality-review` skill and all five checklists; the approved tooling baseline; and relevant routing, responsive, accessibility, SEO, media, and testing documentation. No final issue-2 `implementation-report.md` exists yet; that is expected because the orchestrator owns finalization only after the required review gates pass.

`features-cli docs current --feature greek-essence-showcase` and `features-cli progress --feature greek-essence-showcase --json` independently confirmed frontier `review-issue`, issue 2 `in-review`, before and after review work.

The unrelated Ralph/JZ rebuild, plan, generated `.playwright-cli`, workflow/signal, issue-1, and other dirty-worktree changes were preserved and excluded. No production, test, contract, lifecycle, signal, implementation-report, visual-review, Git-history, remote, deployment, credential, or unrelated mutation was performed. The sole new artifact is this immutable review. This is code review only and does not provide visual certification.

## Standards Verdict

`PASS`. Review 04 F-01 is repaired at the required bounded command seam. `scripts/validate-content.mjs` now has one optional `--content-root <path>` input; omitting it still resolves the authoritative repository `content/` directory. The regression helper creates a fresh OS temporary directory with `mkdtempSync` for every case, copies the content fixtures there, changes only temporary EN/EL JSON, invokes the same validator script against that temporary root, and removes only that root. It never writes either authoritative locale fixture.

The focused command cases prove both equal-locale invalid Paros final-CTA pairings fail: `home` with `paros-antiparos`, and `plan-my-trip` with `null`. The same command seam proves a valid pair with a context-free Home `plan-my-trip` CTA passes. `validateParosFinalCta` remains the single shared exact Paros positional invariant called by both `validateShowcaseContentPair` and the dedicated script, while the general CTA schema continues to allow context-free Home CTAs.

Two repeated focused Vitest runs used default Vitest behavior, with file parallelism not disabled, and both passed 22/22 tests. The full default-parallel unit suite passed 45/45 tests across nine files. Independent before/after SHA-256 and nanosecond-mtime snapshots remained byte-for-byte identical across all runs:

- EN SHA-256 `6c826cc7a6bd782f0fa4322ee71f9dcddd2357e281ba2fbe1b0e6b250fea8e9e`, mtime ns `1784931645044935200`.
- EL SHA-256 `f9bc86ece8f5813a75d73d2ea8865b18ce2feff275ab01af92aaafa435ab5b5b`, mtime ns `1784931645044935200`.

Reviews 01–03 F-01/F-02/F-03 repairs remain intact. Stable locale IDs/media/routes are compared; Paros CTA semantics are enforced centrally at loader and command boundaries; `getCtaPathname` permits only the allow-listed Plan My Trip query; approved media fails closed on incomplete metadata or absent files; emitted media variants remain tied to tested hero/card geometry; and all live destination media remains the intended pending-approval fallback. The unchanged guarded destination matrix still covers both localized Home-to-Paros journeys, both locale-switch directions, both contextual CTA hrefs, all five security headers, current navigation, reduced motion, 320 px and exact 195 px no-overflow boundaries, compact Escape/outside close with focus return, browser guards, and axe coverage.

No credential, PII, unsafe runtime content boundary, unsupported claim, arbitrary query value, analytics, successor form/API/email implementation, broader catalogue, dynamic route, threshold reduction, accessibility weakening, or scope/hard-wall breach was found. The issue remains static-first, shallow, bilingual, metadata-complete, and Tier-2 proportionate.

Global formatting remains `FAIL`, exit 1, on exactly the same eight preserved unrelated files. `check:all` remains `FAIL`, exit 1, because it stops at that initial global formatting failure; later chained commands did not execute in that invocation. Unlighthouse was appropriately reused rather than rerun because attempt 06 changes only the validation script and test fixture seam, not rendering, route output, CSS, media, browser behavior, or performance code. The latest immutable performance result remains technically `FAIL`, exit 1: all four Home/destination score budgets passed, but `/en` LCP was `2565.43ms > 2500ms`. The inherited direct operator exception permits routing this issue onward but does not convert formatting, `check:all`, Unlighthouse, or the LCP metric to green.

## Spec And Contract Verdict

`PASS`. Direct inspection and executable checks prove the accepted six-section EN/EL destination composition, natural bilingual editorial content including culture/gastronomy, stable collection and media IDs, pending-media fallback, fixed localized destination identity, localized metadata/canonicals/alternates/noindex, route-aware shell/current state, exact allow-listed contextual planning CTA, static generation, and focused regression coverage.

The review-04 safety requirement is now satisfied without a generalized harness or lock layer: every command-level fixture case has a unique temporary root, the default validator remains authoritative, both invalid equal-locale Paros CTA pairings fail, the valid context-free Home CTA passes, and authoritative EN/EL bytes and mtimes survive repeated focused runs and the full default-parallel unit suite unchanged.

All issue acceptance criteria and contract hard walls are met at Tier 2. Rendering, browser, accessibility, and performance evidence is reusable because the attempt-06 fixed point changes only `scripts/validate-content.mjs` and `tests/unit/content/showcase-content.test.ts`. A fresh visual review remains mandatory downstream and is not certified here.

## Blocking Findings

None.

## Non-Blocking Findings

None.

## Verification Considered

- `features-cli docs current --feature greek-essence-showcase` — `PASS`, exit 0; frontier `review-issue`, issue 2.
- `features-cli progress --feature greek-essence-showcase --json` — `PASS`, exit 0; issue 2 is the sole `in-review` issue and resumable issue.
- `test ! -e .scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/reviews/05-review.md` — `PASS`, exit 0 before writing; the immutable attempt path was available.
- `git rev-parse HEAD && git branch --show-current` plus scoped `git diff --stat` and `git status --short --untracked-files=all` — `PASS`, exit 0; fixed point `0a3d7a4224b6d0f648edc39abfc5b5e14314efd8`, branch `feat/jz-ralph-workflow`, five tracked reviewed files with 916 insertions/139 deletions, and 17 untracked reviewed implementation files.
- `snapshot() { python -c 'import hashlib,json,os; ps=["content/en/showcase.json","content/el/showcase.json"]; print(json.dumps([{"path":p,"sha256":hashlib.sha256(open(p,"rb").read()).hexdigest(),"mtime_ns":os.stat(p).st_mtime_ns} for p in ps],sort_keys=True))'; }; before="$(snapshot)"; printf 'BEFORE=%s\n' "$before"; pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose; first=$?; pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose; second=$?; after="$(snapshot)"; printf 'AFTER=%s\n' "$after"; if [ "$before" = "$after" ]; then printf 'FIXTURE_PRESERVATION=PASS\n'; preserve=0; else printf 'FIXTURE_PRESERVATION=FAIL\n'; preserve=1; fi; printf 'RUN1_EXIT=%s RUN2_EXIT=%s PRESERVATION_EXIT=%s\n' "$first" "$second" "$preserve"; test "$first" -eq 0 -a "$second" -eq 0 -a "$preserve" -eq 0` — `PASS`, exit 0; both default-configuration runs passed 1 file / 22 tests, including both isolated invalid equal-locale CTA cases and the valid context-free Home CTA case. EN/EL SHA-256 values and mtime ns values were exactly unchanged before and after.
- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/routes/showcase-routes.test.ts tests/unit/components/showcase-media.test.tsx tests/unit/design/showcase-media-geometry-contract.test.ts --reporter=verbose` — `PASS`, exit 0; 4 files / 35 tests.
- `pnpm validate:content` — `PASS`, exit 0; default authoritative content validation printed `Showcase content validation passed for en/el with media approval checks`.
- `pnpm test:unit` with independent source-fixture snapshots — `PASS`, exit 0; 9 files / 45 tests under default parallel behavior; both authoritative fixture hashes and mtimes remained exactly unchanged.
- `pnpm lint` — `PASS`, exit 0; full ESLint completed with no findings.
- `pnpm typecheck` — `PASS`, exit 0.
- `pnpm build` — `PASS`, exit 0; 10 static pages generated, including both localized Paros routes as SSG, with no new dynamic application boundary.
- `pnpm exec prettier --check app/'[locale]'/destinations/paros-antiparos/page.tsx app/'[locale]'/page.tsx app/globals.css components/layout/language-switcher.tsx components/layout/site-footer.tsx components/layout/site-header.tsx components/sections/home-sections.tsx components/sections/paros-sections.tsx components/sections/showcase-media.tsx content/en/showcase.json content/el/showcase.json content/schemas/showcase.ts lib/content.ts lib/routes.ts scripts/validate-content.mjs tests/unit/components/showcase-media.test.tsx tests/unit/content/showcase-content.test.ts tests/unit/design/showcase-media-geometry-contract.test.ts tests/unit/routes/showcase-routes.test.ts tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts unlighthouse.config.ts` — `PASS`, exit 0; all 22 reviewed paths use Prettier style.
- `git diff --check -- app/'[locale]'/destinations/paros-antiparos/page.tsx app/'[locale]'/page.tsx app/globals.css components/layout/language-switcher.tsx components/layout/site-footer.tsx components/layout/site-header.tsx components/sections/home-sections.tsx components/sections/paros-sections.tsx components/sections/showcase-media.tsx content/en/showcase.json content/el/showcase.json content/schemas/showcase.ts lib/content.ts lib/routes.ts scripts/validate-content.mjs tests/unit/components/showcase-media.test.tsx tests/unit/content/showcase-content.test.ts tests/unit/design/showcase-media-geometry-contract.test.ts tests/unit/routes/showcase-routes.test.ts tests/e2e/localization-and-quality.spec.ts tests/e2e/accessibility.spec.ts unlighthouse.config.ts` — `PASS`, exit 0; no tracked whitespace error. Seventeen reviewed implementation paths are untracked, so focused Prettier is the substantive style check for those files.
- Read-only credential/dangerous-code/debug/conflict-marker scan over the 22 reviewed paths — `PASS`, exit 0; no match. A separate prohibited-claim term scan found only the ordinary verb “Review” in Home planning copy, not a customer-review, credential, price, availability, guarantee, award, partner, or response-time claim.
- `pnpm format:check` — `FAIL`, exit 1; exactly eight preserved unrelated paths failed: `.hermes/plans/2026-07-24_174920-rebuild-ralph-for-jz-workflow.md` and seven generated `.playwright-cli/*.yml` files. No issue-owned path failed focused Prettier, and none of the eight files was edited.
- `pnpm check:all` — `FAIL`, exit 1 at the same initial global `format:check`; its later chained build/E2E/a11y/Unlighthouse commands did not execute in that invocation. Separate focused/full results are reported independently.
- Reused immutable rendering evidence from reviews 03/04 because attempt 06 did not change rendering source or browser tests: compact/wide localization plus accessibility files `PASS`, exit 0, 34 passed / 2 expected wide compact-interaction skips; full E2E `PASS`, exit 0, 50 passed / 4 expected medium/wide compact-interaction skips; a11y `PASS`, exit 0, 18 passed.
- Reused immutable performance evidence from review 03/04 because attempt 06 did not affect rendering or performance: `pnpm quality:unlighthouse` — `FAIL`, exit 1; four Home/destination score-budget assertions passed, while strict `/en` LCP failed at `2565.43ms > 2500ms`. This remains technically RED under the inherited direct operator exception and is not called a pass.
- TDD evidence from attempt 06 — `PASS` as process evidence: the isolated-fixture tests first failed 2/22 because the script ignored `--content-root`, then passed 22/22 after the bounded seam was implemented. No live fixture was written during RED or GREEN.
- Final read-only fixture state and scoped worktree status — command exit 0; EN/EL hashes and mtimes matched the pre-verification values, and the issue-owned tracked/untracked fixed point remained unchanged before this report was added.

## Required Route

`PASS`. Preserve reviews 01 through 05 unchanged. No blocking defect remains in the issue-2 code-review scope, and the inherited unrelated formatting/LCP failures remain accurately classified under the existing operator authority rather than converted to passes. Return this verdict to the orchestrator for the required fresh independent visual review. Do not mark the issue `done`, finalize the implementation report, transition lifecycle, or begin a successor until the feature-local visual-review gate passes and the orchestrator completes its separate artifact/lifecycle duties.
