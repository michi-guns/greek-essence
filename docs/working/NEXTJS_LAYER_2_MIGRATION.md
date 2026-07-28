# Next.js Feature Architecture Migration

## Goal

Reorganize the application around clear ownership without changing its routes,
behavior, rendered output, or public contracts.

This migration introduces feature-based structure only. It does not authorize
product changes, behavioral refactors, new infrastructure, a monorepo, or a new
data or state-management architecture.

## Placement Rule

Place code at the narrowest location justified by its current consumers. Move
it outward only when demonstrated reuse requires it.

1. Keep Next.js route conventions and route-specific code under `app/`.
2. Put code shared by routes in one business domain under
   `features/<feature-name>/`.
3. Put proven domain-neutral code used across unrelated domains under `shared/`.
4. If ownership is unclear, leave the code in its current narrowest valid
   location until usage provides evidence.

Do not create empty directories or generic dumping grounds. Name features after
business capabilities, not technical categories.

```text
app/routes  ->  features  ->  shared
     +--------------------------^
```

## Dependency Boundaries

- `shared/` must not import from `features/` or `app/`.
- Features must not import from `app/`.
- Route-local code must not be imported by another route subtree.
- Feature-to-feature dependencies must reflect real domain composition, remain
  one-way, and avoid cycles.
- Keep domain-owned types and rules with their feature.
- Add a feature public entry point only when external consumers need one. Keep
  exports narrow and statically analyzable; avoid broad barrel files.
- Keep server-only and client-safe exports separate so an import cannot
  accidentally cross the Server/Client Component boundary.

## Next.js and Project Constraints

- Follow the documentation bundled with the installed Next.js version for
  framework behavior and file conventions.
- Prefer Server Components. Add Client Components only where interaction
  requires them, and keep their dependency surface small.
- Preserve English and Greek route and content boundaries.
- Preserve existing static, build-time, and request-time behavior. This
  structural migration must not redesign data flow or dynamic boundaries.
- Keep content, schemas, metadata, assets, styles, tests, fixtures, and mocks
  with their established owners unless current consumers justify moving them.
- Preserve the existing `@/*` alias unless a change is required for the chosen
  structure.

## Migration Loop

Work in small, independently verifiable slices:

1. Inventory a candidate and find all of its consumers.
2. Choose the narrowest justified owner: route, feature, or shared.
3. Move one coherent slice and update its imports without changing behavior.
4. Run focused tests and type checking before continuing.
5. Search for stale paths and unintended boundary crossings.
6. Stop and ask when evidence does not support a clear ownership decision.

Use temporary working notes for the consumer map. Do not turn the migration
brief into a file-by-file ledger.

Before deleting obsolete files or directories, present the exact paths and
obtain explicit user approval. Confirm that source, tests, configuration,
documentation, and dynamic imports no longer reference them.

## Completion Criteria

The migration is complete when:

- existing routes, behavior, rendering, and public contracts are preserved;
- every moved file has a clear route, feature, or shared owner;
- Server/Client, locale, and static/dynamic boundaries remain intact;
- no stale imports, duplicate implementations, or dependency cycles remain;
- applicable formatting, lint, type-check, test, content-validation, and build
  commands pass; and
- the final report records boundary decisions, validation results, approved
  deletions, and unresolved risks.
