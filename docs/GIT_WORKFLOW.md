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
- Squash-merge the pull request, then delete its short-lived branch.

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

1. Start from the latest `main`:

   ```bash
   git switch main
   git pull --ff-only origin main
   ```

2. Define the coherent unit and create one short-lived branch:

   ```bash
   git switch -c <type>/<short-description>
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

7. Squash-merge the pull request and delete the branch:

   ```bash
   gh pr merge --squash --delete-branch
   git switch main
   git pull --ff-only origin main
   ```

8. Confirm local `main` is clean and synchronized with `origin/main`.

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
  operator's acceptance and exact authorized ledger path in the pull-request
  description so the authorization remains reviewable after squash merge.
- If the discussion exposes a genuinely independent topic, record the dependency
  and give that topic its own coherent pull-request unit rather than mixing it
  into the current one.

Per-answer persistence protects continuity; it does not define pull-request
granularity.

## Safety

- Inspect the complete logical diff before staging, before marking a draft ready,
  and before merge.
- Preserve unrelated and concurrent edits.
- Do not discard local changes to make the worktree clean.
- Do not force-push, rewrite history, or delete unmerged work without explicit
  operator approval.
- Use a separate worktree when concurrent work would otherwise overlap.
- Do not merge an incomplete draft merely to preserve intermediate state; the
  pushed branch and draft pull request already provide that continuity.
