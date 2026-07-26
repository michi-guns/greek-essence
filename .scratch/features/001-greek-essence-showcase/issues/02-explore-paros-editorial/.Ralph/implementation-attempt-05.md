# Issue 02 Implementation Repair — Attempt 05

Date: 2026-07-25
Issue: `02-explore-paros-editorial`
Method: `tdd-solo`
Resolved depth: Tier 2 — Prototype
Scope: immutable review 03 F-01 only. No lifecycle, review, visual-review, signal, Git, remote, deployment, successor-surface, or unrelated-worktree mutation was made.

## RED → GREEN chronology

### F-01 — `pnpm validate:content` shares Paros final-CTA semantics

1. Added a command-level regression test at the existing content seam in `tests/unit/content/showcase-content.test.ts`. It temporarily writes equal English/Greek fixture copies, invokes `node scripts/validate-content.mjs`, and restores the exact original fixture bytes in `finally`. It covers both invalid final-CTA pairings:
   - `routeId: "plan-my-trip"` with `destinationContext: null`;
   - non-Plan `routeId: "home"` with `destinationContext: "paros-antiparos"`.
2. RED command: `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose`
3. RED result: `FAIL`, exit 1; 1 test failed / 20 passed (21 total). The `plan-my-trip` with null context case observed validation-script exit 0 and failed at `expected +0 not to be +0`. The non-Plan/context case already failed through the general CTA schema. This proves the missing command-boundary invariant rather than test setup or syntax failure.
4. GREEN repair: extracted the exact positional Paros final-CTA invariant into `validateParosFinalCta` in `content/schemas/showcase.ts`. Both `validateShowcaseContentPair` and `scripts/validate-content.mjs` call that function after schema parsing. General context-free CTAs, including valid Home CTAs, remain accepted by the general CTA schema; route APIs and successor behavior were not changed.
5. GREEN command: `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose && pnpm validate:content`
6. GREEN result: `PASS`, exit 0; focused content suite 1 file / 21 tests passed, then content validation printed `Showcase content validation passed for en/el with media approval checks`.

## Files changed in this attempt

### Production

- `content/schemas/showcase.ts` — exports the shared positional Paros final-CTA invariant.
- `lib/content.ts` — uses the shared invariant in `validateShowcaseContentPair`.
- `scripts/validate-content.mjs` — uses the same shared invariant for the dedicated `pnpm validate:content` boundary.

### Tests

- `tests/unit/content/showcase-content.test.ts` — command-level equal-EN/EL invalid-CTA regression coverage with fixture restoration.

### Supporting evidence

- `.scratch/features/001-greek-essence-showcase/issues/02-explore-paros-editorial/.Ralph/implementation-attempt-05.md`

## Verification

- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose` — RED `FAIL`, exit 1; 1 failed / 20 passed (21 tests). The missing behavior was `plan-my-trip` with null destination context exiting 0 from the dedicated validator.
- `pnpm exec vitest run tests/unit/content/showcase-content.test.ts --reporter=verbose && pnpm validate:content` — `PASS`, exit 0; 1 file / 21 tests, then content validation passed.
- `pnpm test:unit` — `PASS`, exit 0; 9 files / 44 tests.
- `pnpm lint` — `PASS`, exit 0.
- `pnpm typecheck` — `PASS`, exit 0.
- `pnpm build` — `PASS`, exit 0; 10 static pages generated, including both localized Paros routes as SSG; no new dynamic application boundary.
- `pnpm exec prettier --check content/schemas/showcase.ts lib/content.ts scripts/validate-content.mjs tests/unit/content/showcase-content.test.ts` — `PASS`, exit 0.
- `git diff --check -- content/schemas/showcase.ts lib/content.ts scripts/validate-content.mjs tests/unit/content/showcase-content.test.ts` — `PASS`, exit 0. These issue-owned source/test files are intentionally untracked in the inherited dirty worktree, so Git produced no diff output; no whitespace error was reported.
- `pnpm format:check` — `FAIL`, exit 1; preserved unrelated formatting failures only: `.hermes/plans/2026-07-24_174920-rebuild-ralph-for-jz-workflow.md` and seven generated `.playwright-cli/*.yml` files. No issue-owned changed path failed focused Prettier, and none of the eight unrelated files was edited.
- `pnpm quality:unlighthouse` — not rerun: this validation-only shared invariant/test change does not materially affect rendered performance. Immutable review 03 remains the fresh performance evidence: `FAIL`, exit 1, because `/en` LCP was `2565.43ms > 2500ms` despite all four route score budgets passing. That inherited exception remains technically RED and is not called a pass.
- `pnpm check:all` — not rerun: it deterministically stops at the known unrelated initial `pnpm format:check` failure, as review 03 recorded. Repeating it would not execute later chained gates or add issue-owned evidence.
- Browser/a11y suites — not rerun: this repair changes only build-time validation and a unit command seam; review 03 independently passed the unchanged focused browser/a11y behavior (`34 passed / 2 expected wide compact-menu skips`, full E2E `50 passed / 4 expected skips`, a11y `18 passed`).

## Privacy and scope assurance

- The command-level test uses only existing static/provisional showcase fixtures and restores their exact original bytes; no visitor, client, recipient, credential, or other PII was introduced or retained.
- No media approval state, assets, rendered route, form, draft, submission, API, email, confirmation, route interface, or broader catalogue behavior changed.
- The repair remains inside the change-contract content/schema/script/test soft scope. The intentionally dirty worktree and immutable reviews 01–03 were preserved.

## Handoff

Review 03 F-01 is repaired at the required dedicated `pnpm validate:content` boundary with one shared invariant. The issue remains `in-progress`, Phase `red`, awaiting a fresh independent code review; this implementer did not self-review or transition status.
