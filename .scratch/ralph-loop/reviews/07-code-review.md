# Ralph/JZ Controller Repair — Final Bounded Independent Code Review 07

**Verdict:** FAIL  
**Resolved engineering depth:** Tier 2 — Prototype (direct operator instruction; consistent with root `AGENTS.md` and approved feature `SPEC.md` `implementation_depth: 2`)  
**Review type:** Final bounded independent review of only the current seven-path unstaged Ralph snapshot relative to the index  
**Reviewed unstaged binary diff SHA-256:** `4eb50746647c96b39902506d8da066786fcf82dc034d759a02abf29d1812df74`

## Exact scope and reviewed diff

Only the unstaged delta relative to the index on these seven paths was reviewed:

1. `.scratch/ralph-loop/tools/ralph_loop.py`
2. `.scratch/ralph-loop/tests/test_ralph_loop.py`
3. `.scratch/ralph-loop/tests/test_ralph_acceptance.py`
4. `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`
5. `.agents/skills/ralph-loop-manager/scripts/preflight.py`
6. `.scratch/ralph-loop/RALPH_LOOP.md`
7. `.agents/skills/ralph-loop-manager/SKILL.md`

The scoped binary diff is 76,395 bytes and contains 780 insertions and 65 deletions across exactly seven paths. The pre-existing cached binary diff SHA-256 remained `e8c67dff2c6768a26f7a7eae66cf043fa35f6285deb2ec4da8a491f66f9473c3`.

I read root `AGENTS.md`, `NEXT.md`, documentation/bootstrap entry points, the rebuild plan and implementation report, approved feature `SPEC.md`, immutable reviews 04–06, both controller documents, controller, preflight, and all three scoped test files. I read the recommended live `jz-code-review-super-fast` skill; its status-mutation requirement was overridden by this direct read-only brief. I independently inspected the installed stable `features-cli` 0.3.0 `progress-state.ts`, its source-identical AI Arsenal copy, and `features-state.ts` feature-directory identity contract.

No implementation, test, documentation, signal, frontier, status, profile, email, staging, commit, push, deployment, remote, visual-certification, Ralph, or Hermes action was performed. This immutable review artifact is the sole repository write.

## Finding

### 1. HIGH — Feature identity is not validated, so missing/mismatched stable identities and an invalid optional-field value create evidence and launch under the wrong feature owner

**Severity:** HIGH / blocking at Tier 2.  
**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:350-364,395-429`; `.agents/skills/ralph-loop-manager/scripts/preflight.py:130-170`; incomplete “actual shape” fixtures at `.scratch/ralph-loop/tests/test_ralph_loop.py:625-703` and `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py:72-81`.

**Requirement:** The direct review brief requires actual artifact-less stable payloads to derive deterministic contained issue/feature `.Ralph` owners, while invalid or ambiguous identities must fail before filesystem creation or `Popen`. The pinned stable `FeatureProgress` identity always includes `feature.id` and `feature.slug` (`progress-state.ts:41-55`). Its canonical directory function is exactly `.scratch/features/${String(id).padStart(3, "0")}-${slug}` (`features-state.ts:71-77`). Optional `artifactPath?: string` permits omission or a string, not explicit JSON `null`.

**Evidence / reproduction:** `_frontier_artifact_owner` reads only `feature.slug`; `_contained_feature_owner` then globs `*-greek-essence-showcase` and ignores `feature.id`. `validate_progress` likewise ignores `feature.id`. The tests labeled as actual stable shapes construct only `feature.slug`, so they omit the identity field that the stable CLI always emits.

A temporary complete-`run_loop` probe used otherwise full stable-shaped `review-issue` payloads against a repository containing only `.scratch/features/001-greek-essence-showcase/issues/02-owner`:

1. `feature.id: 999` with the valid slug was accepted, returned without error, called `Popen` once, and created `.Ralph` under feature 001; preflight returned `(True, "review-issue")`.
2. Missing `feature.id` was accepted with the same one-launch/creation result; preflight returned true.
3. Explicit `artifactPath: null`, which is outside the pinned `artifactPath?: string` contract, was treated as omission and also launched once after creating `.Ralph`; preflight returned true.

This is fail-open behavior at the exact pre-creation/pre-launch identity boundary. Containment alone does not make a mismatched stable identity valid: the controller can attribute evidence and launch based on a feature directory that does not match the payload's declared feature ID.

**Required correction:** Strictly require a positive integer `feature.id` and the expected slug, derive the feature owner from the exact canonical `${id.padStart(3)}-${slug}` identity, and reject missing, mismatched, zero/multiple, unsafe, or reparsed owners before creation or `Popen`. Distinguish an omitted optional `artifactPath` from a present non-string value; explicit `null` must be rejected. Apply the same minimum stable schema validation in preflight. Keep the correction mechanical and narrow; do not add semantic workflow interpretation or optional hardening.

**Required verification:** Use complete payload fixtures copied from the pinned stable shape, including `feature.id`, `slug`, `status`, `phase`, and `focusPath`. Prove all six valid artifact-less kinds still route and run consecutively as appropriate. Add complete `run_loop` and preflight regressions proving missing/non-positive/mismatched `feature.id` and present `artifactPath: null` fail before `.Ralph` creation and before `Popen`. Retain the review-05 same-owner/no-clobber/junction/frontier suite and review-04 exact-PID ownership suite.

## Required behavior observations

Subject to the blocking finding:

- Full-shape valid artifact-less `review-issue` then resumed `implement-issue` completed two normal iterations, called fake `Popen` twice, used one issue-owned run directory, and preserved two readable logs.
- Full-shape valid artifact-less `design-ready`, `feature-review`, `blocked`, and `archived` completed four normal iterations, called fake `Popen` four times, used one feature-owned run directory, and preserved four readable logs.
- Review-05 same-owner reuse, cross-invocation no-clobber collision refusal, Windows artifact/owner/`.Ralph`/`runs` junction rejection, malformed frontier rejection, and changed-owner behavior passed.
- Review-04 PID ownership remains intact. The direct event-order probe observed `starting` before `Popen`, exact PID `54321`, 25 `running` writes, 24 waits of 0.25 seconds, one PID-scoped cleanup, verified child exit 0, and final `idle`/null-root evidence. Focused ambiguity/preflight tests also passed.
- Dry-run performed no launch or creation. Live preflight exited 2 only for the expected existing `COMPLETION_NOT_LAUNCH_COMPATIBLE` hard stop and reported `launch_performed: false`.

These passing observations do not override the invalid-identity finding.

## Commands and exact results

1. Initial status/scope inspection (`git status --short`; `git diff --name-only/stat`; `git diff --cached --name-only`) — exit 0; confirmed the intentionally dirty worktree, the requested seven unstaged Ralph paths among unrelated preserved changes, and the populated index.
2. Scoped hash/stat/check command over the seven exact paths — exit 0; hash `4eb50746647c96b39902506d8da066786fcf82dc034d759a02abf29d1812df74`; 76,395 bytes; 780 insertions, 65 deletions; zero scoped whitespace errors; cached hash `e8c67dff2c6768a26f7a7eae66cf043fa35f6285deb2ec4da8a491f66f9473c3`.
3. Full live file reads and file-split `git diff` inspection — exit 0; all seven current files and their unstaged delta were inspected.
4. `features-cli docs execution` — exit 0; recommended review owner `jz-code-review-super-fast`; its live skill was read without performing its overridden workflow mutation.
5. Installed/source `progress-state.ts` comparison — exit 0; installed version 0.3.0; both files 17,000 bytes; both SHA-256 `d55176336d721079d8d690ec015f3414b7aa6926e517deb79187343ef9543cf5`; byte-identical.
6. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_loop.py' -v` — exit 0; 38/38 passed, including the Windows junction test.
7. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_acceptance.py' -v` — exit 0; 2/2 passed.
8. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_manager_preflight.py' -v` — exit 0; 14 tests run, 13 passed, 1 skipped (`file symlinks unavailable`).
9. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_*.py' -v` — exit 0; 67 tests run, 66 passed, 1 skipped, 0 failed/errors.
10. Exact six-test review-04/review-05 regression command — exit 0; 6/6 passed: same-owner reuse, collision refusal, live Windows junction rejection, ambiguous ownership preservation, verified cleanup, and preflight ambiguity refusal.
11. `pnpm exec prettier --check <seven exact paths>` — exit 0; all seven scoped paths matched style.
12. `pnpm format:check` — exit 1; preserved exact failure: Prettier reported the rebuild plan plus seven pre-existing/out-of-scope `.playwright-cli/*.yml` files (8 files total). This failed full command is not claimed as passing and is not the scoped finding.
13. `pnpm lint` — exit 0.
14. `pnpm typecheck` — exit 0.
15. `pnpm test:unit` — exit 0; 7 test files and 29 tests passed.
16. `pnpm build` — exit 0; production build compiled/typechecked and generated 8/8 static pages.
17. `pnpm validate:content` — exit 0; English/Greek showcase content and media approval checks passed.
18. `python -B .scratch/ralph-loop/tools/ralph_loop.py --dry-run` — exit 0; resolved the live issue-02 route, completion true, pause false, max iterations 100, timeout 10,800, and `launch_performed:false`; no Ralph/Hermes launch.
19. `python -B .agents/skills/ralph-loop-manager/scripts/preflight.py --repo . --target greek-essence-showcase` — exit 2; expected `HARD_STOP` with sole hard stop `COMPLETION_NOT_LAUNCH_COMPATIBLE`, one dirty-worktree warning, all other checks passed, and `launch_performed:false`.
20. First direct real-shape probe attempt — exit 1 with preserved `SyntaxError: unterminated string literal (detected at line 38)`; it executed no probe and is not claimed as passing.
21. Corrected direct real-shape/invalid-identity probe — exit 0; valid issue sequence produced `LIMIT_REACHED`, 2 `Popen`, 2 readable issue logs; valid feature sequence produced `LIMIT_REACHED`, 4 `Popen`, 4 readable feature logs. Mismatched feature ID, missing feature ID, and explicit-null artifact path each produced no controller error, 1 `Popen`, `.Ralph` creation, and preflight acceptance, reproducing finding 1.
22. Direct review-04 event-order/exact-PID probe — exit 0; `starting` preceded `Popen`; PID `54321`; 25 running writes; 24 waits all `0.25`; one PID-scoped cleanup; verified exit 0; final record `idle` with null root; expected propagated `LockConflict` after exhausted persistence.
23. Initial installed-package metadata probe — exit 1 after `pnpm list` succeeded because a guessed non-virtual-store package path produced Node `MODULE_NOT_FOUND`; not claimed as passing. A later pipe-based command resolved the actual installed path and produced the successful byte-identity evidence in command 5.
24. Initial Python subprocess package-hash probe — exit 1 with `FileNotFoundError [WinError 2]` because native Python could not execute the pnpm shell shim directly; not claimed as passing. The shell-piped replacement succeeded as command 5.
25. Added-line static scan over the exact seven-path diff — exit 0; no hardcoded-secret assignment, shell injection, dangerous eval/exec, unsafe pickle, or name-based/bulk-kill match.
26. Final pre-artifact scope/hash/status check — exit 0; review 07 was absent; scoped hash remained `4eb50746647c96b39902506d8da066786fcf82dc034d759a02abf29d1812df74`; 76,395 bytes and 780/65 remained unchanged; exactly the seven requested scoped paths were listed.

## Required route

Preserve reviews 01–07 unchanged. Return this FAIL and finding 1 to `jzgreekorch`; do not self-repair or self-convert it to approval. Do not reopen stale handoff findings, broaden the Tier-2 task, launch Ralph, run operational acceptance, mutate signals/frontier/status, email, stage, commit, push, deploy, or touch unrelated work.
