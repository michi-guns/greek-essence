# Prototype Rebaseline Retention Plan

## Purpose

Classify the active tree without treating archived prototype structure as the
future architecture. No path in this document is approved for deletion merely
because it is listed here.

## Retain

Retain these as current project infrastructure, routing, or active working
state:

- `AGENTS.md`, `NEXT.md`, and `TODO.md`
- `docs/README.md`, `docs/CONTRIBUTOR_ONBOARDING.md`, and
  `docs/GIT_WORKFLOW.md`
- `docs/grilling/` while product and feature decisions are being established
- `docs/working/work-items/prototype-rebaseline/` while this operation is active
- `docs/archive/showcase-prototype-v0/` as non-authoritative historical
  reference only
- `.agents/`, `.codex/`, `.github/`, `.husky/`, and repository policy files
- package-manager, TypeScript, formatting, linting, Git-hook, and dependency
configuration until replacements are justified and verified

## Archived by the Operator

The former `docs/00_project_protocol/` through `docs/05_agent_skills/` and
`docs/reference/` trees now live under
`docs/archive/showcase-prototype-v0/`. Preserve them as historical evidence,
but do not treat their internal authority, approval, architecture, scope, or
tooling statements as current.

## Removed With Explicit Approval

The following closed prototype execution records were removed after exact user
approval. They had no live source or documentation consumers, and the complete
versions remain available at `archive/showcase-prototype-v0`:

- `.scratch/features-status.json`
- `.scratch/features/001-greek-essence-showcase/`

The removal deleted 76 tracked files and approximately 12.7 MB from the active
tree. It did not remove them from Git history or the archive branch. Afterward,
`pnpm check` and `pnpm build` both passed.

The operator later approved one coordinated correction inside the retained
prototype: move `assets/imgs/` to Next.js's served `public/images/` path, remove
`content/shared/media.json`, and replace its approval-gated media IDs with
direct localized content records. This preserves the complete image library in
the active tree, makes the referenced images render, and keeps the former
manifest recoverable from Git history and `archive/showcase-prototype-v0`.

## Hold for Coordinated Architecture Replacement

Do not remove or reorganize these paths independently. Together they form the
currently runnable prototype and its executable checks:

- `app/`
- `public/images/`
- `components/`
- `content/`
- `i18n/`
- `lib/`
- `messages/`
- `tests/`
- `scripts/assert-unlighthouse-lcp.mjs`
- `scripts/validate-content.mjs`
- `scripts/validate-prototype-asset-prompts.mjs`
- prototype-specific commands and paths in `package.json`, `knip.config.ts`,
  `playwright.config.ts`, `unlighthouse.config.ts`, and `vitest.config.mts`

Removing only part of this set would leave stale imports, scripts, content
references, or broken quality gates. Classify individual files only after the
expanded product boundaries and the replacement application foundation are
approved. Keep `main` deployable by replacing obsolete runtime paths in the
same verified change that removes them.

## Review Later

- `MIGRATION.md` may be superseded by the settled architecture documentation.
- `docs/working/NEXTJS_LAYER_2_MIGRATION.md` and
  `docs/working/NEXTJS_LAYER_2_INVENTORY.md` are provisional working documents;
  promote useful rules and remove these files when the operation completes.
- `.hermes/plans/2026-07-24_103303-client-demo-vertical-slice-12h.md` is
  historical planning material. Review its durable value separately rather
  than bundling it into prototype-source deletion.
