# Manual Vercel Re-deploy

## Status

Complete

## Ownership and Scope

Owner: Codex (`jimzord Stam`)

Trello Work Unit: [WU-27 — Configure Vercel - manual Re-deploy](https://trello.com/c/16L5cZe0) — **Done**

Scope was: disable Git-triggered Vercel deployments and provide
`pnpm deploy:vercel` as the supported production re-deploy command.

## Final outcome

- Implementation merged via https://github.com/michi-guns/greek-essence/pull/46
  (`75968647a92096b80d3c1f19cb429aa4183b652a`).
- Post-merge: merge did not auto-deploy; authorized `pnpm deploy:vercel`
  deployed latest `main`.
- Trello WU-27 is Done; this handoff is closed.

## Constraints (historical)

- Deploy Hook stays in ignored `.env.local`; never print secrets.
- Vercel account administration remains operator-owned.
