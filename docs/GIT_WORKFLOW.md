# Git Workflow

Greek Essence uses GitHub Flow with one branch and pull request for each
**coherent, independently reviewable unit of work**.

## Core Rules

- `main` must always be deployable.
- Never commit or push directly to `main`.
- A pull request represents one coherent outcome, not one chat turn, answer,
  commit, file, or work session.
- Related changes accumulate on the same short-lived branch and pull request.
- Open an early draft pull request for ongoing or multi-session work. Continue
  updating that draft instead of opening a new pull request for each increment.
- A small change completed in one session may open directly as ready for review.
- Do not combine unrelated outcomes merely to reduce the pull-request count.
- A review approval is not required, but the logical unit must be complete and
  required checks must pass before merge.
- Start every newly authorized coherent unit on its own short-lived branch in a
  dedicated isolated worktree. Do not repurpose the original checkout or an
  unrelated worktree for the new unit.
- Place Greek Essence task worktrees under the sibling
  `../greek-essence.worktrees/<short-name>` directory.
- Create and remove task worktrees with `git worktree add` and
  `git worktree remove`. Do not copy a repository directory to create one or
  manually delete a registered worktree directory.
- Squash-merge the pull request, then delete its short-lived branch and isolated
  worktree after GitHub verifies the merge.

## Isolated Worktree Lifecycle

Before creating durable state, fetch current `origin/main` and search existing
worktrees, local and remote branches, repository work-item routing, and GitHub
pull requests. Recover matching same-intent state instead of creating a duplicate.

From the original `greek-essence/` checkout, create a new task branch and
isolated worktree without switching branches or modifying checked-out files.
Create the sibling `greek-essence.worktrees/` container first if it does not yet
exist; the task directory itself must be created by Git:

```bash
git fetch --prune origin
git worktree list --porcelain
git worktree add \
  -b <type>/<short-description> \
  ../greek-essence.worktrees/<short-name> \
  origin/main
git -C ../greek-essence.worktrees/<short-name> status --short --branch
```

Use the task worktree for all changes, checks, commits, pushes, and pull-request
updates for that coherent unit. Keep the original checkout and every unrelated
worktree untouched.

After GitHub reports the pull request merged and the task worktree is clean,
perform cleanup from the original `greek-essence/` checkout, using the actual
registered path for any older worktree that predates this convention:

```bash
git fetch --prune origin
git worktree list --porcelain
git push origin --delete <type>/<short-description>
git worktree remove ../greek-essence.worktrees/<short-name>
git branch -D <type>/<short-description>
git worktree prune
git worktree list --porcelain
```

Skip the remote-branch deletion command only when fresh inspection proves the
remote branch is already absent. The forceful local branch deletion is permitted
only after fresh GitHub read-back proves the pull request merged; squash merge
does not make the task commit an ancestor of `main`, so `git branch -d` may reject
the already-delivered branch.
Never use `git worktree remove --force` to bypass uncommitted or untracked files.
Treat refusal to remove the worktree as a cleanup blocker, inspect and preserve
the state, and resolve it without discarding work. Verify the task worktree,
local branch, and remote branch are absent while unrelated worktrees remain.

## Trello Work Unit Lifecycle

For work selected from the Greek Essence Trello board, Trello owns Work Unit
identity, owner, lifecycle, and concise evidence. Git owns branch and commit
state; GitHub owns pull-request, review, check, and merge state; repository
artifacts own detailed design and verification.

| Trello state | Git and pull-request meaning                                                                    | Evidence required to advance                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Inbox        | Unselected intake. No task branch or pull request.                                              | The original card remains available for same-card Work Unit design.                                                     |
| In Design    | Contract clarification. No implementation branch or pull request.                               | Objective, boundaries, acceptance, dependencies, and verification are being resolved.                                   |
| Ready        | Complete and claimable. No implementation has started.                                          | No material pending question or blocker remains.                                                                        |
| In Progress  | One confirmed owner; one branch and linked draft PR exist, or same-intent recovery is underway. | Owner and status read-back, current-main branch point, repository work-item registration, draft PR, and Trello PR link. |
| Blocked      | The existing branch and PR are retained.                                                        | The blocker, responsible unblocker, safe resume action, and durable recovery references are recorded.                   |
| Review       | The PR is non-draft and ready for disposition.                                                  | Acceptance is satisfied, required verification passes, and no known blocker remains.                                    |
| Done         | Delivery and local cleanup are verified; the card remains unarchived.                           | Squash merge, short-lived branch cleanup, and clean synchronized local `main`.                                          |

### Guarded claim and bootstrap

1. Re-read the Ready Work Unit. Stop for a conflicting owner, blocker, status,
   or repository authority.
2. Apply the stable owner update and read it back.
3. Re-read, transition `Ready → In Progress`, and confirm both expected owner
   and status. Trello does not make these two operations atomic.
4. Fetch current `origin/main`. Search local and remote branches, repository
   work-item routing, and GitHub PRs by intended head/base before creating
   anything.
5. Follow the isolated-worktree lifecycle above to create one worktree under
   `../greek-essence.worktrees/` and one
   `<type>/wu-<number>-<short-description>` branch from current `origin/main`.
6. Add the work-item directory and preserved root-router link as the first
   meaningful commit. Push the branch and open one early draft pull request.
7. Put the Work Unit's direct Trello URL in the PR and the verified PR URL in
   the Work Unit.

### Cross-system recovery

Durable creation order is branch → work-item registration → push → draft PR →
Trello link-back. After an interruption or failed step:

1. Re-read Trello, local Git, the remote branch, root work-item routing, and
   GitHub head/base PR state.
2. Reuse state whose identity and intent match the Work Unit.
3. Create only the earliest missing artifact. Never create a second branch,
   work item, or PR merely because a response or Trello link-back was lost.
4. Preserve conflicts and stop instead of overwriting a different owner or
   incompatible durable state.

An unsuccessful Trello PR-link update leaves the GitHub PR authoritative for
its own existence. Recover the link; do not create another PR.

### Review, merge, and completion

- Before moving to Review, update the same PR to represent the complete unit,
  run applicable final checks, resolve material findings, and mark it
  non-draft. The Work Unit must contain concise current evidence.
- Immediately before an agent merge, re-read the Work Unit and PR and obtain
  fresh explicit operator confirmation. Earlier design approval, approval to
  begin work, or a standing autonomy rule is not merge confirmation.
- The operator may merge the PR personally. If GitHub already reports it
  merged, do not issue another merge call; continue verification and cleanup.
- Use squash merge and delete the short-lived branch. Synchronize local `main`
  with `origin/main` and verify it is clean before moving the Work Unit to Done.
- Done ends agent lifecycle mutation. A human may later review and archive the
  Trello card manually.

## Coherent Pull-Request Units

A coherent unit has one outcome that a reviewer can understand, verify, accept,
or revert independently. Typical units are:

- one feature or bounded feature slice;
- one bug fix with its regression evidence;
- one accepted product or foundation decision set;
- one architectural foundation or independently reviewable subtopic;
- one focused refactor, documentation change, or process change.

A unit may contain multiple related decisions, commits, files, and work sessions.
For example, five decisions that together define one feature normally belong in
one pull request. A broad Foundation Design track may use several pull requests
when each covers a complete, independently useful subtopic.

Split work when a discovered concern has a different outcome, risk, review
boundary, or rollback boundary. Do not split merely because another answer was
recorded or another commit was made.

## Draft Pull-Request Lifecycle

1. Fetch the latest remote state and inspect existing same-intent state:

   ```bash
   git fetch --prune origin
   git worktree list --porcelain
   ```

2. Define the coherent unit and create one short-lived branch in its own
   isolated worktree:

   ```bash
   git worktree add \
     -b <type>/<short-description> \
     ../greek-essence.worktrees/<short-name> \
     origin/main
   ```

   Common prefixes are `feat/`, `fix/`, `docs/`, `test/`, `refactor/`, and
   `chore/`.

3. Make the first meaningful bounded change, run the applicable focused checks,
   and commit it:

   ```bash
   git add <paths>
   git commit -m "<type>(<scope>): <summary>"
   ```

4. Push the branch and open one draft pull request when the unit will continue
   across more decisions, commits, or sessions:

   ```bash
   git push -u origin HEAD
   gh pr create --draft --base main --title "<title>" --body-file <body-file>
   ```

   If the coherent unit is already complete, open it as ready instead.

5. Keep related work on that branch and update the same pull request. Keep its
   title, description, scope, and verification evidence representative of the
   complete unit. Do not create another pull request for an incremental answer or
   commit.

6. When the unit is complete and any required operator acceptance exists:

   - run the applicable final repository gates against the stable result;
   - resolve material review findings;
   - mark the draft ready for review; and
   - wait for required GitHub checks.

7. Squash-merge the pull request:

   ```bash
   gh pr merge --squash
   ```

8. After fresh GitHub read-back proves the merge, leave the task worktree, remove
   the remote branch, remove the task worktree with `git worktree remove`, delete
   the merged local branch, prune worktree metadata, and verify cleanup as
   defined in the isolated-worktree lifecycle.
   Fast-forward a clean local `main` checkout to `origin/main` when one exists;
   never switch, overwrite, or clean an unrelated worktree to do so.

## Grilling and Design Work

A feature grill, bounded Product and Domain Truth topic, or coherent Foundation
Design subtopic normally forms one pull-request unit.

- Persist each operator answer in the same working ledger and draft pull request.
- Do not open or merge a pull request for each decision ID.
- Keep the draft open while the related decision set is incomplete.
- At final approval, use the same pull request for accepted decision
  distillation, explicitly authorized raw-ledger deletion, handoff updates,
  verification, and merge.
- Before deleting an approved raw ledger in that pull request, record the
  operator's acceptance, exact authorized ledger path, and final accepted raw
  ledger in the pull-request description so the evidence remains reviewable
  after squash merge. The distilled decision document remains the repository
  authority.
- If the discussion exposes a genuinely independent topic, record the dependency
  and give that topic its own coherent pull-request unit rather than mixing it
  into the current one.

Per-answer persistence protects continuity; it does not define pull-request
granularity.

## Change-Appropriate Checks

Before claiming that a change is ready for review or completion, read and
follow [`QUALITY_GATES.md`](QUALITY_GATES.md). That document owns change
classification, required verification, evidence reporting, and the definition
of done.

Local pre-push and the required GitHub job classify the complete pushed or
pull-request range, not the working tree. Any mixed, empty, malformed, or
unresolved range fails closed to the full gates defined there. The GitHub
workflow always reports the required `Lightweight quality gates` context; do
not replace this behavior with workflow-level path exclusions.

## Safety

- Inspect the complete logical diff before staging, before marking a draft ready,
  and before merge.
- Preserve unrelated and concurrent edits.
- Do not discard local changes to make the worktree clean.
- Do not force-push, rewrite history, or delete unmerged work without explicit
  operator approval.
- Use one dedicated isolated worktree for every newly authorized coherent unit,
  even when no concurrent work is currently visible.
- Create, inspect, remove, and prune worktrees through Git. Never manually move,
  copy, or delete a registered worktree directory.
- Do not merge an incomplete draft merely to preserve intermediate state; the
  pushed branch and draft pull request already provide that continuity.
