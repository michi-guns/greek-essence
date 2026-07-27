# GitHub Organization Migration

This checklist tracks the pending transfer of `jimzord12/greek-essence` to an
organization-owned repository. Replace `<organization>` with the approved
GitHub organization slug before executing commands or changing integrations.

Do not record credentials, secret values, personal data, runtime identifiers,
or raw service logs in this file.

## Before the transfer

- [ ] Confirm the target repository will be
      `<organization>/greek-essence` and confirm its visibility.
- [ ] Confirm both maintainers belong to the organization with the required
      repository roles.
- [ ] Confirm the operator performing the transfer can create repositories in
      the organization.
- [ ] Agree on a short transfer window and avoid concurrent pushes while the
      repository moves.
- [ ] Record the intended organization teams and ownership rules without
      copying credentials or secret values.
- [ ] Review repository rulesets, branch protection, Actions permissions,
      environments, variable names, secret names, webhooks, deploy keys, and
      installed GitHub Apps that must be verified after transfer.
- [ ] Confirm the default branch and working tree are in the intended state.

## Transfer

- [ ] In GitHub, open **Settings → General → Danger Zone → Transfer**.
- [ ] Transfer `jimzord12/greek-essence` to `<organization>` without renaming
      it unless a separate naming decision has been approved.
- [ ] Confirm the repository resolves at
      `https://github.com/<organization>/greek-essence`.
- [ ] Confirm GitHub redirects the former personal-account URL as expected.

## Repository access and policy

- [ ] Assign the approved organization teams and individual repository roles.
- [ ] Verify the default branch, rulesets, branch protection, required checks,
      merge settings, and Actions workflow permissions.
- [ ] Verify GitHub environments, variables, and secret names; restore missing
      values through GitHub's secret UI rather than through Git or this file.
- [ ] Verify Dependabot alerts and the dependency graph are enabled under the
      organization's security policy.
- [ ] Review audit and security settings available under the organization plan.

## Local checkouts and worktrees

- [ ] Update each local checkout after the transfer using the commands below.

```powershell
git remote set-url origin https://github.com/<organization>/greek-essence.git
git remote -v
git fetch origin
```

- [ ] Update the remote for every active worktree or clone used by either
      maintainer.
- [ ] Verify fetch and push authorization for the intended organization account.

## GitHub Apps and external integrations

- [ ] Install the free hosted Renovate GitHub App for only
      `<organization>/greek-essence`.
- [ ] Verify Renovate reads `renovate.json`, creates its Dependency Dashboard,
      preserves exact pins, groups non-major updates, and waits for dashboard
      approval before opening major-update pull requests.
- [ ] Verify the GitHub Actions `CI` workflow runs successfully in the
      organization-owned repository.
- [ ] Reconnect or reauthorize the Vercel Git integration and verify preview and
      production project links, domains, and environment configuration.
- [ ] Review any remaining webhooks or GitHub Apps individually; do not assume
      personal-account installation grants transfer to the organization.

## Documentation and references

- [ ] Search tracked files for the former repository URL and update links,
      badges, ownership references, and clone instructions where necessary.
- [ ] Update any external bookmarks, deployment settings, or service links that
      do not follow GitHub's repository redirect.
- [ ] Confirm `README.md`, `AGENTS.md`, and project documentation do not imply
      the personal account remains the repository owner.

## Verification and closure

- [ ] Run `pnpm install --frozen-lockfile` from a clean checkout.
- [ ] Run `pnpm check`, `pnpm build`, and the required Playwright and
      accessibility checks.
- [ ] Confirm the CI workflow and a Renovate dry onboarding/update run complete
      without unapproved lockfile or `allowBuilds` changes.
- [ ] Confirm both maintainers can clone, fetch, and push according to the new
      organization rules.
- [ ] Record the completed transfer date and remove resolved checklist items or
      archive this file in durable project history.
