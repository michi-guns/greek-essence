# Ralph/JZ Controller Repair — Independent Code Review 06

**Verdict:** FAIL  
**Resolved engineering depth:** Tier 2 — Prototype (direct operator instruction; consistent with root `AGENTS.md` and approved feature `SPEC.md` `implementation_depth: 2`)  
**Review type:** Fresh independent final review attempt of the current seven-path unstaged snapshot relative to the index  
**Reviewed unstaged binary diff SHA-256:** `45d7110448f4773f416de44d77e62bc236ae3eb49e1099c552814a65bd331c99`

## Exact scope and reviewed diff

Only the unstaged delta relative to the index on these seven paths was reviewed:

1. `.scratch/ralph-loop/tools/ralph_loop.py`
2. `.scratch/ralph-loop/tests/test_ralph_loop.py`
3. `.scratch/ralph-loop/tests/test_ralph_acceptance.py`
4. `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py`
5. `.agents/skills/ralph-loop-manager/scripts/preflight.py`
6. `.scratch/ralph-loop/RALPH_LOOP.md`
7. `.agents/skills/ralph-loop-manager/SKILL.md`

The scoped binary diff is 68,356 bytes and contains 650 insertions and 65 deletions across exactly seven paths. The pre-existing cached binary diff SHA-256 remained `e8c67dff2c6768a26f7a7eae66cf043fa35f6285deb2ec4da8a491f66f9473c3`.

I read root `AGENTS.md`, `NEXT.md`, `docs/README.md`, the bootstrap entry point, feature `AGENTS.md`, approved feature `SPEC.md`, the Ralph/JZ rebuild plan, implementation report, immutable reviews 04 and 05, both controller documents, controller, preflight, and all three scoped test files. I also read the recommended live `jz-code-review-super-fast` skill and inspected the installed stable `features-cli` 0.3.0 `FrontierKind` type and every frontier construction branch in `packages/features-cli/src/progress-state.ts`. The skill's status-mutation instructions were overridden by the direct read-only review brief.

No implementation, test, documentation, signal, frontier, status, profile, email, staging, commit, push, deployment, remote, visual-certification, Ralph, or Hermes action was performed. This new immutable review artifact is the sole repository write.

## Review-05 finding verification

| Review-05 required behavior | Result | Independent evidence |
|---|---|---|
| Same-owner iteration 2 reuses only the current invocation's run directory | **PASS** | Complete two-iteration probe returned `LIMIT_REACHED`, called `Popen` twice, created one run directory, and retained independently readable `iteration-0001.log`=`one` and `iteration-0002.log`=`two`. Focused test passed. |
| Cross-invocation no-clobber remains strict | **PASS** | Independent two-invocation probe created two distinct parent run directories with separately readable `first` and `second` logs. Forced UUID collision raised `FrontierRouteError` before `Popen` and left only the pre-existing directory. |
| Changed-owner routing works | **PASS** | Complete two-iteration probe called `Popen` twice and created exactly one same-ID run directory under each of two issue owners. |
| Artifact/owner/`.Ralph`/`runs` junction or reparse components cannot redirect creation | **PASS** | Windows `mklink /J` probes for artifact, `.Ralph`, and `runs` components each raised `FrontierRouteError`; no outside run directory was created. The Windows junction regression test ran and passed (it was not skipped). |
| Missing/unknown/inconsistent/duplicate frontier routing fields fail before creation or launch | **PASS for the malformed cases required by review 05** | Independent missing-kind, unknown-kind, issue-without-ID, non-issue-with-ID, and duplicate-kind matrix produced `FrontierRouteError`, zero `Popen`, and no `.Ralph`. Focused controller and preflight tests passed. |
| Dry-run and preflight do not create the live owner's `.Ralph` | **PASS** | Live owner `.Ralph` was absent before dry-run, after dry-run, and after preflight. Dry-run exited 0; preflight exited 2 only for the existing completion-true launch incompatibility. |

All three review-05 findings are closed as originally stated. The separate finding below is a concrete compatibility/usability regression exposed by comparing the new closed schema with the actual stable CLI payload contract; it does not reopen review-03's excluded stale-handoff prose finding.

## Finding

### 1. HIGH — The allowlisted routing schema rejects legitimate stable `features-cli` frontiers that omit optional `artifactPath`, so a normal overnight campaign stops at review and other real transitions

**Location:** `.scratch/ralph-loop/tools/ralph_loop.py:344-360`; `.agents/skills/ralph-loop-manager/scripts/preflight.py:127-164`; contract mismatch in `.scratch/ralph-loop/RALPH_LOOP.md:30` and `.agents/skills/ralph-loop-manager/SKILL.md:65`; missing real-shape coverage near `.scratch/ralph-loop/tests/test_ralph_loop.py:625-641` and `.scratch/ralph-loop/tests/test_ralph_manager_preflight.py:58-70`.

**Severity:** HIGH / blocking at Tier 2.

**Requirement:** Ralph must remain usable for a normal bounded overnight campaign, launch one fresh orchestrator for each real `features-cli` frontier action, and route logs safely without inventing a second workflow ledger. The stable CLI is the sole ledger. A closed per-kind schema must reject genuinely malformed or inconsistent fields, but it must accept every legitimate payload shape produced by the pinned stable CLI for a routable frontier. `RALPH_LOOP.md:30` and manager `SKILL.md:65` claim the allowlisted kinds are routable.

**Evidence / reproduction:** The installed/source stable CLI 0.3.0 declares `artifactPath?: string` in `packages/features-cli/src/progress-state.ts:49-55`. Its actual branches intentionally omit `artifactPath` for realistic states, including:

- `review-issue` for an `in-review` issue (`progress-state.ts:513-526`), carrying `kind`, `summary`, and `issueId` only;
- resumed `implement-issue` for an `in-progress` issue (`progress-state.ts:528-541`), carrying `kind`, `summary`, and `issueId` only;
- `design-ready` (`421-429`), `feature-review` (`596-605`), `blocked` (`608-617`), and `archived` (`369-375`), carrying no artifact path.

The new controller nevertheless requires a non-empty `artifactPath` for every allowlisted kind at `ralph_loop.py:358-360`, and preflight does the same at `preflight.py:155-157`. An independent probe passed exact payload shapes from those source branches through complete `run_loop`. Every one raised:

```text
FrontierRouteError: frontier artifactPath must be a non-empty relative POSIX path
```

Each safely made zero `Popen` calls and created no `.Ralph`, but the safety behavior is unusably fail-closed for valid data. A second independent probe showed `validate_progress` rejects legitimate `review-issue`, `feature-review`, and `blocked` payloads with `frontier artifactPath is missing or invalid`.

This is reachable immediately in ordinary overnight use: after an implementation action moves an issue to `in-review`, the next controller iteration receives the legitimate artifact-less `review-issue` shape and stops before launching the reviewer-owning orchestrator. Existing tests use invented `review-issue`/`implement-issue` shapes with `artifactPath`, so all 63 tests pass while missing this real stable-CLI boundary.

**Required correction:** Make the closed routing schema match the pinned stable CLI's actual per-kind contract. Preserve strict duplicate rejection, the complete known-kind allowlist, positive `issueId` requirements for issue kinds, issue-directory identity checks, containment/reparse safety, and pre-creation/pre-`Popen` rejection of genuinely malformed combinations. For legitimate kinds whose stable shape omits `artifactPath`, derive a deterministic contained owner mechanically from validated feature/issue identity (or first change and repin the stable CLI so its documented output supplies a safe route for every kind). Keep semantic workflow interpretation out of Python.

**Required verification:** Add tests based on the actual `progress-state.ts` payload shapes, not invented supersets. At minimum prove complete consecutive controller iterations can cross into artifact-less `review-issue` and resumed `implement-issue` while routing to the correct issue owner; prove valid artifact-less `design-ready`, `feature-review`, and `blocked` dry-run/preflight routes behave deterministically; retain strict rejection of missing fields that are required for that specific kind; retain the review-05 no-creation/no-`Popen` malformed matrix, collision refusal, junction protections, and review-04 ownership suite. Then obtain a fresh immutable review.

## Review-04 ownership/PID safety

Review-04 safety remains intact. The independent order/cleanup probe observed durable `starting` before `Popen`, exact PID `54321`, 25 `running` writes, 24 waits of 250 ms, and one PID-scoped cleanup call. Verified cleanup exited the child and removed the idle record; ambiguous cleanup preserved exact-PID `cleanup_ambiguous` evidence. The focused ownership/preflight regressions and full suite passed, and the added-line scan found no name-based or bulk-kill path.

## Commands and exact results

1. `git status --short --branch; git diff --name-status/stat/numstat -- <seven paths>; git diff --binary -- <seven paths> | sha256sum; ... | wc -c; git diff --check -- <seven paths>; git diff --cached --binary | sha256sum` — exit 0; exactly seven unstaged scoped paths; 650 insertions, 65 deletions; 68,356 bytes; scoped hash `45d7110448f4773f416de44d77e62bc236ae3eb49e1099c552814a65bd331c99`; zero scoped whitespace errors; cached hash `e8c67dff2c6768a26f7a7eae66cf043fa35f6285deb2ec4da8a491f66f9473c3`.
2. Complete file reads plus file-split `git diff --unified=... -- <seven paths>` — exit 0; full live files and exact unstaged changes inspected.
3. `features-cli docs current --feature greek-essence-showcase && features-cli progress --feature greek-essence-showcase --json` — exit 0; live frontier `contract-issue`, issue 02, warnings `[]`; read-only.
4. `features-cli docs execution` — exit 0; review owner `jz-code-review-super-fast`; its live source skill was read.
5. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_loop.py' -v` — exit 0; 35/35 passed; Windows junction test ran and passed.
6. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_acceptance.py' -v` — exit 0; 2/2 passed.
7. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_ralph_manager_preflight.py' -v` — exit 0; 13 tests run, 12 passed, 1 skipped (`file symlinks unavailable`).
8. `python -B -m unittest discover -s .scratch/ralph-loop/tests -p 'test_*.py' -v` — exit 0; 63 tests run, 62 passed, 1 skipped, 0 failed/errors.
9. `pnpm exec prettier --check <seven paths>` — exit 0; all seven scoped paths matched style.
10. `pnpm format:check` — exit 1; preserved exact failure: Prettier reported the rebuild plan and seven pre-existing/out-of-scope `.playwright-cli/*.yml` files (8 files total). This failed full command is not claimed as passing and is not a seven-path finding.
11. `pnpm lint` — exit 0. `pnpm typecheck` — exit 0.
12. `pnpm test:unit` — exit 0; 7 files and 29 tests passed.
13. `pnpm build` — exit 0; compiled and typechecked successfully; generated 8/8 static pages.
14. `pnpm validate:content` — exit 0; EN/EL showcase content and media approval checks passed.
15. `python -B .scratch/ralph-loop/tools/ralph_loop.py --dry-run` — exit 0; live issue-02 owner/run/log route reported, completion true, pause false, 100 iterations, 10,800-second timeout, `launch_performed:false`.
16. `python -B .agents/skills/ralph-loop-manager/scripts/preflight.py --repo . --target greek-essence-showcase` — exit 2; expected hard stop `COMPLETION_NOT_LAUNCH_COMPATIBLE`, one dirty-worktree warning, all other checks passed, `launch_performed:false`.
17. Live owner no-creation check around dry-run and preflight — exit 0; `.Ralph` absent before dry-run, after dry-run, and after preflight; dry-run exit 0 and preflight exit 2.
18. Independent combined routing probe — exit 0; same-owner: `LIMIT_REACHED`, 2 `Popen`, 1 run directory, two readable iteration logs; changed-owner: 2 `Popen`, one run directory under each owner; two invocations: two distinct run parents and independent contents; collision: `FrontierRouteError`, 0 `Popen`, only pre-existing evidence remained; malformed schema matrix: all five cases `FrontierRouteError`, 0 `Popen`, no `.Ralph`.
19. Independent Windows junction probe using `cmd /c mklink /J` — exit 0; artifact, `.Ralph`, and `runs` junction cases all raised `FrontierRouteError`; zero outside run creation.
20. Independent review-04 event-order probe — exit 0; both outcomes recorded `starting` before `Popen`; exact PID `54321`; 25 running writes; 24 × 0.25-second waits; one PID cleanup. Successful cleanup verified exit 0 and no record; ambiguous cleanup retained exact-PID `cleanup_ambiguous`.
21. Added-line static scan over the exact seven-path diff — exit 0; 650 added lines; no hardcoded-secret assignment, shell injection, dangerous eval/exec, unsafe pickle, or name-based/bulk-kill match.
22. Stable CLI source inspection of `FrontierKind`, `FeatureProgress.frontier`, and all construction branches — exit 0/read success; proved `artifactPath` is optional and the legitimate shapes cited in finding 1 omit it.
23. Independent legitimate stable-shape controller probe — exit 0; `review-issue`, resumed `implement-issue`, `design-ready`, `feature-review`, `blocked`, and `archived` all reproduced `FrontierRouteError: frontier artifactPath must be a non-empty relative POSIX path`, with 0 `Popen` and no `.Ralph`.
24. Independent legitimate stable-shape preflight-helper probe — exit 0; valid `review-issue`, `feature-review`, and `blocked` shapes each returned `(False, 'frontier artifactPath is missing or invalid')`.

## Required route

Preserve reviews 01–06 unchanged. Return finding 1 to `jzgreekorch` for a separate Tier-2 implementation session, rerun affected/full gates, and obtain a fresh immutable code-review attempt. Do not reopen review-03's stale-handoff prose finding. Do not launch Ralph, run operational acceptance, mutate signals/frontier/status, email, stage, commit, push, deploy, or touch unrelated work.
