# Issue 02 Implementation Repair — Attempt 06

Date: 2026-07-25
Issue: `02-explore-paros-editorial`
Method: `tdd-solo` RED → GREEN
Resolved depth: Tier 2 — Prototype
Scope: immutable review 04 F-01 only. No lifecycle, review, visual-review, signal, Git, remote, deployment, successor-surface, or unrelated-worktree mutation was made.

## Repair

Replaced the unsafe command-level regression that rewrote `content/en/showcase.json` and `content/el/showcase.json` with an isolated-fixture seam.

- `scripts/validate-content.mjs` now accepts one bounded optional `--content-root <path>` input. With no argument, `pnpm validate:content` keeps its existing authoritative `content/` behavior.
- The command reads EN, EL, and `shared/media.json` from that supplied content root while preserving the existing shared `validateParosFinalCta` invariant.
- The focused test copies the complete `content/` directory to a unique OS temporary directory, mutates only temporary EN/EL JSON, and invokes the same script with `--content-root`.
- The regression proves both equal-locale invalid Paros final-CTA pairings fail, and a valid pair with a context-free Home CTA passes. It snapshots real EN/EL fixture SHA-256 bytes and mtimes before every command invocation and asserts they are identical afterward.

No test writes `content/en/showcase.json` or `content/el/showcase.json`.

## RED → GREEN evidence

### RED — missing isolated script seam

Test-first change: replaced the live-fixture rewrite helper with the temporary-fixture safety/seam test before changing production script behavior.

Command:

```text
pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose
```

Result: `FAIL`, exit 1; 1 file, 2 failed / 20 passed / 22 tests total.

Expected failures:

```text
validates isolated fixtures without changing authoritative source fixtures: home route with destination context
validates isolated fixtures without changing authoritative source fixtures: Plan My Trip route without destination context

AssertionError: expected true to be false // Object.is equality
```

The validator exited 0 for both invalid temporary inputs because it still consumed the authoritative repository content root and ignored `--content-root`. The context-free Home CTA case passed. This is the intended missing-seam behavior, not a test setup or syntax error.

### GREEN — bounded caller-supplied content root

Implementation: added the optional `--content-root` path handling in `scripts/validate-content.mjs`, routing EN/EL fixture and shared-media reads through that root. The existing default command behavior and shared `validateParosFinalCta` invariant remain unchanged.

Repeated focused command with Vitest default file parallelism (no `--no-file-parallelism` option):

```text
pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose && pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose
```

Result: `PASS`, exit 0; each run 1 file / 22 passed tests.

The three isolated command cases were green on each run:

1. Equal EN/EL `home` + `paros-antiparos` Paros final CTA fails.
2. Equal EN/EL `plan-my-trip` + `null` Paros final CTA fails.
3. Valid EN/EL Paros final CTA plus a context-free Home `plan-my-trip` CTA passes.

## Source-fixture preservation evidence

The isolated test snapshots real fixture SHA-256 values and mtimes before invoking each temporary-root command and asserts exact equality after it returns. This assertion ran during the RED run, two repeated focused GREEN runs, the four-file focused run, and both final full-unit runs.

Final read-only source fixture state:

```text
content/en/showcase.json SHA-256 6c826cc7a6bd782f0fa4322ee71f9dcddd2357e281ba2fbe1b0e6b250fea8e9e
content/el/showcase.json SHA-256 f9bc86ece8f5813a75d73d2ea8865b18ce2feff275ab01af92aaafa435ab5b5b
content/en/showcase.json mtime 2026-07-25 01:20:45.044935200 +0300
content/el/showcase.json mtime 2026-07-25 01:20:45.044935200 +0300
```

No real fixture content or mtime changed during the repair verification.

## Changed files

- `scripts/validate-content.mjs` — bounded optional content-root seam; default `pnpm validate:content` behavior retained.
- `tests/unit/content/showcase-content.test.ts` — temporary EN/EL/media fixture copies, isolated command regression cases, and authoritative source byte/hash/mtime preservation assertions.
- `.scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/.Ralph/implementation-attempt-06.md` — this immutable implementation evidence.

## Verification

- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose` — RED `FAIL`, exit 1; 1 file / 2 failed / 20 passed / 22 tests. Intended ignored-temporary-root behavior.
- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose && pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose` — GREEN `PASS`, exit 0; both runs 1 file / 22 passed tests, with Vitest default file parallelism.
- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts tests/unit/routes/showcase-routes.test.ts tests/unit/components/showcase-media.test.tsx tests/unit/design/showcase-media-geometry-contract.test.ts --reporter=verbose` — `PASS`, exit 0; 4 files / 35 passed tests.
- `pnpm validate:content` — `PASS`, exit 0; `Showcase content validation passed for en/el with media approval checks`.
- `pnpm lint` — `PASS`, exit 0.
- `pnpm typecheck` — `PASS`, exit 0.
- `pnpm build` — `PASS`, exit 0; 10 static pages generated, including EN/EL Paros SSG routes; no dynamic application boundary added.
- `pnpm test:unit` — `PASS`, exit 0; 9 files / 45 passed tests. (Run once before and once after formatting; final result listed.)
- Focused `pnpm exec prettier --check` across the 22 issue-owned production/content/test/config paths — `PASS`, exit 0; all matched files use Prettier style.
- Focused `git diff --check -- scripts/validate-content.mjs tests/unit/content/showcase-content.test.ts` plus the established content/route/media focused paths — `PASS`, exit 0. The changed issue-owned files are inherited untracked files, so Git emitted no diff while reporting no whitespace error.
- `pnpm format:check` — `FAIL`, exit 1, truthfully unchanged: exactly eight unrelated files failed (`.hermes/plans/2026-07-24_174920-rebuild-ralph-for-jz-workflow.md` and seven generated `.playwright-cli/*.yml` files). No issue-owned focused path failed Prettier; none of those eight files was edited.

Not rerun by direct operator instruction because this repair changes only content-validation script/test behavior, not rendering, route output, or performance code:

- Browser/a11y: fresh immutable review 03/04 evidence remains `PASS` for focused compact/wide localization plus accessibility files (34 passed / 2 expected wide compact-interaction skips), full E2E (50 passed / 4 expected compact-only skips), and a11y (18 passed).
- Unlighthouse: fresh immutable review 03/04 evidence remains technically `FAIL`, exit 1, because `/en` LCP was `2565.43ms > 2500ms`; score budgets passed but the inherited direct operator exception does not make this green.
- `pnpm check:all`: fresh immutable review 03/04 evidence remains `FAIL`, exit 1, at the same initial eight-file global format failure; chained later steps do not execute in that command.

## Privacy, scope, and worktree assurance

- Temporary test inputs contain only copied static provisional showcase content. No visitor, client, recipient, credential, or other PII was introduced in source, artifacts, output, or evidence.
- The repair stays inside the contract soft scope: content schema/script/test seams. It retains static-first behavior, route interfaces, media approval behavior, bilingual validation, and the shared CTA invariant.
- No generalized harness, lock, dependency, new framework, form/API/email successor implementation, lifecycle change, review mutation, staging, commit, push, deploy, reset, stash, or history rewrite occurred.
- The intentionally dirty worktree was preserved.

## Next handoff

Review 04 F-01 has a bounded RED → GREEN repair with isolated command inputs and source-fixture preservation evidence. Issue remains `in-progress`, Phase `red`; a fresh independent code review is required next. This implementation owner did not self-review or transition workflow state.
