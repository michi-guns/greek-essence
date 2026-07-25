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
