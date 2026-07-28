# Git Workflow

Greek Essence uses a simple GitHub Flow strategy.

## Rules

- `main` must always be deployable.
- Never commit or push directly to `main`.
- Create a short-lived branch for every change.
- Push the branch and open a pull request into `main`.
- A review approval is not required.
- Required checks must pass before the pull request is merged.
- Merge the pull request into `main`, then delete the short-lived branch.

## Workflow

1. Start from the latest `main`:

   ```bash
   git switch main
   git pull --ff-only origin main
   ```

2. Create a short-lived branch:

   ```bash
   git switch -c <type>/<short-description>
   ```

   Common prefixes are `feat/`, `fix/`, `docs/`, `test/`, `refactor/`, and
   `chore/`.

3. Make the change, run the applicable checks, and commit it:

   ```bash
   git add <paths>
   git commit -m "<type>(<scope>): <summary>"
   ```

4. Push the branch:

   ```bash
   git push -u origin HEAD
   ```

5. Open a pull request targeting `main`.

6. When required checks pass, merge the pull request. No review approval is
   required.

7. Confirm `main` contains the merged change, then delete the merged branch.

## Safety

- Inspect the diff before staging and committing.
- Do not include unrelated work in a pull request.
- Do not discard local changes to make the worktree clean.
- Do not force-push, rewrite history, or delete unmerged work without explicit
  operator approval.
- Use a separate worktree when concurrent work would otherwise overlap.
