# Next.js Layer 2 Migration Brief

Use this file as the implementation brief for migrating a standard
`create-next-app` project to the feature-based architecture described in
[How to Build Reusable Architecture for Large Next.js Applications](https://www.freecodecamp.org/news/reusable-architecture-for-large-nextjs-applications/).

This migration stops at **Layer 2: Feature-Based Folder Structure**. Do not
introduce Turborepo, workspace packages, or other later layers unless separately
requested.

## Objective

Organize application code by business domain while preserving Next.js App
Router colocation:

- Route-specific code stays close to its route.
- Cross-route domain code lives in `features/<feature-name>/`.
- Truly generic, domain-agnostic code lives in `shared/`.
- Each feature exposes an intentional public API through `index.ts`.
- Existing behavior, routes, rendered output, and public contracts remain
  unchanged unless a change is explicitly requested.

## Target Structure

Keep the project's existing choice of either a root-level `app/` directory or a
`src/app/` directory. Do not move `app/` merely to make the tree match this
example.

```text
src/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── dashboard/
│       ├── page.tsx
│       ├── loading.tsx
│       ├── error.tsx
│       ├── components/        # Used only by this route subtree
│       └── lib/               # Used only by this route subtree
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── lib/
│   │   ├── types.ts
│   │   └── index.ts           # Intentional public API
│   └── billing/
│       ├── components/
│       ├── hooks/
│       ├── lib/
│       ├── types.ts
│       └── index.ts
└── shared/
    ├── components/
    ├── hooks/
    ├── lib/
    └── ui/                    # Optional design-system primitives
```

If the project uses a root-level `app/`, create `src/features/` and
`src/shared/` unless an established project convention clearly requires
otherwise. Preserve the configured `@/*` alias and update it only if needed to
resolve the chosen structure consistently.

Do not create empty directories just to reproduce this tree. Add a directory
only when a real file belongs there.

## Placement Decision

For every file being moved or created, apply these rules in order:

1. **Next.js route convention:** `page.tsx`, `layout.tsx`, `loading.tsx`,
   `error.tsx`, `not-found.tsx`, route handlers, and route-segment configuration
   stay under `app/`.
2. **One route subtree:** code used only by one route or route subtree stays
   colocated inside that route, normally in its local `components/`, `hooks/`,
   `lib/`, or `actions/` directory.
3. **One business domain across routes:** code with a clear domain owner, such
   as authentication, billing, orders, or notifications, belongs in
   `features/<domain>/`.
4. **Generic across domains:** code that has no knowledge of routes or business
   domains belongs in `shared/`.
5. **Unclear ownership:** keep the file at its current narrowest valid location
   until real usage proves where it belongs. Do not put it in a generic
   `utils/`, `helpers/`, or global `components/` dumping ground.

Promote code only as far as its current consumers require:

```text
one component/route -> nearest route folder
multiple routes in one domain -> feature
multiple unrelated domains -> shared, only if genuinely generic
```

## Dependency Rules for Coding Agents

Treat these as mandatory invariants for all new and modified code.

### Allowed dependency direction

```text
app/routes  ->  features  ->  shared
     |              |
     +--------------+      (routes may also import shared directly)
```

- `shared/` must never import from `features/` or `app/`.
- A feature must never import from `app/`.
- Route-local code must not be imported by a different route subtree. Move the
  reusable code to its owning feature or to `shared/`.
- Prefer no feature-to-feature imports. When a real domain dependency makes one
  necessary, import only from the other feature's public API, keep the
  dependency one-way, and do not create a cycle.

### Feature boundaries

- Every feature must have an `index.ts` public API.
- Code outside a feature must import from `@/features/<feature>`, never from a
  feature's internal path.
- A feature's own files may use relative imports to its internals.
- Export only symbols required by external consumers. Do not use blanket
  `export *` statements and do not expose internal storage, validation, query,
  or implementation helpers without a real external contract.
- Keep types owned by the domain inside the feature. Put a type in `shared/`
  only when it is genuinely domain-neutral.

Example:

```ts
// src/features/auth/index.ts
export { LoginForm } from "./components/LoginForm";
export { useAuth } from "./hooks/useAuth";
export type { AuthState, AuthUser } from "./types";

// Deliberately private:
// ./lib/tokenStorage
// ./lib/validators
```

External consumers:

```ts
import { LoginForm, type AuthUser } from "@/features/auth";
```

Forbidden external deep import:

```ts
import { readToken } from "@/features/auth/lib/tokenStorage";
```

### Naming and file hygiene

- Name features after business capabilities, not technical categories:
  `auth`, `billing`, and `orders`, not `hooks`, `forms`, or `api`.
- Use the project's existing naming conventions. Do not perform unrelated
  renames or formatting rewrites during the migration.
- Keep tests next to the code they verify when the existing test tooling allows
  it.
- Avoid duplicate sources of truth. Move an implementation and update its
  imports; do not copy it into the new structure and leave both versions active.
- Delete an old directory only after confirming that no source, test, config,
  story, or documentation file still imports from it.
- Do not turn a feature barrel into an application-wide service locator. Public
  APIs should stay small and intentional.

## Migration Procedure

Perform the migration in small, verifiable slices.

### 1. Inventory before editing

- Inspect `app/` or `src/app/`, existing top-level `components/`, `hooks/`,
  `lib/`, `utils/`, services, stores, types, tests, and path aliases.
- Build a consumer map for each candidate file using repository-wide import
  searches.
- Identify business domains from existing behavior and terminology. Do not
  invent speculative features.
- Record the project's current validation commands from `package.json`.

### 2. Classify files

Create a temporary migration table in the agent's working notes:

| Current path | Consumers | Owner | Target path | Reason |
| --- | --- | --- | --- | --- |
| `...` | `...` | route / feature / shared | `...` | `...` |

Resolve ambiguous ownership from actual consumers and behavior. If a choice
would materially alter module boundaries and evidence is insufficient, ask
before moving that file.

### 3. Establish directories and aliases

- Add only the feature and shared directories required by the inventory.
- Confirm `@/features/...` and `@/shared/...` resolve through `tsconfig.json` or
  `jsconfig.json`.
- Do not add a new alias scheme when the existing `@/*` alias already works.

### 4. Migrate one domain at a time

For each domain:

1. Move its components, hooks, domain utilities, services, and types into one
   feature folder.
2. Add a minimal `index.ts` containing only the exports needed outside the
   feature.
3. Replace external deep imports with imports from the feature public API.
4. Keep route-only code in the route instead of forcing it into the feature.
5. Run focused tests and type checking before starting the next domain.

Use file moves that preserve history where practical. Do not mix this
structural migration with behavioral refactors.

### 5. Migrate genuinely shared code

- Move only domain-neutral UI primitives, hooks, and utilities to `shared/`.
- Verify each shared file has zero imports from `features/` and `app/`.
- If a supposedly shared component contains domain language, domain-specific
  types, permissions, or business rules, keep it in its owning feature.

### 6. Remove obsolete locations

- Search the whole repository for old import paths and deep feature imports.
- Remove superseded files and now-empty dumping-ground directories.
- Check tests, Storybook files, mocks, dynamic imports, and configuration—not
  only production TypeScript files.

### 7. Validate the completed migration

Run the repository's existing:

- formatter or formatting check;
- linter;
- TypeScript type check;
- unit/integration tests;
- production build.

If the project lacks one of these scripts, report that fact. Do not silently add
a new toolchain outside the migration scope.

## Definition of Done

The migration is complete only when all applicable statements are true:

- All existing application routes and behavior are preserved.
- Cross-route domain code is grouped under clearly named features.
- Route-only code remains colocated with its route.
- Generic code in `shared/` has no feature or route knowledge.
- Every feature has a small, intentional `index.ts` public API.
- No external code deep-imports feature internals.
- No feature imports from `app/`.
- No circular feature dependencies were introduced.
- Old duplicate implementations and obsolete directories are gone.
- Repository-wide searches find no stale import paths.
- Existing lint, type-check, test, and production-build commands pass.
- The final agent report lists moved files, boundary decisions, validation
  commands, and any unresolved risks.

## Scope Guard

This is an architectural reorganization, not permission to:

- change product behavior or UI;
- rewrite working modules;
- introduce global state, a new data-fetching library, or a new design system;
- add Turborepo or convert the repository into a monorepo;
- move code to `shared/` because it might be reused someday;
- expose feature internals merely to make an import convenient.

When uncertain, choose the narrowest location justified by current usage and
the smallest migration that leaves the codebase in a valid, tested state.

