# Next.js Layer 2 Inventory

Status: proposed migration map; no application files have moved.

## Recommendation

The migration is worthwhile but small. Keep the root-level `app/` layout and
create root-level `features/` and `shared/`; introducing `src/` would add a
second source root without a current benefit.

The code has three demonstrated ownership zones:

- route-local Home, Paros, and quality-lab composition;
- a cross-route showcase domain for navigation, content, routes, media, and
  CTAs; and
- domain-neutral UI utilities.

Keep `i18n/`, `messages/`, and raw `content/` data in place. They are established
framework and data boundaries, not uncertain shared code.

## Current Boundaries

- `app/[locale]/layout.tsx` statically enumerates `en` and `el`; locale pages use
  `setRequestLocale` and localized metadata.
- Pages and section components are Server Components by default.
- `site-header`, `quality-lab-toggle`, and `fixture-toggle` are the only explicit
  Client Component entry points.
- `lib/content.ts` performs build/server-side JSON validation and filesystem
  checks. It must not share an entry point with client-safe modules.
- `lib/routes.ts` is client-safe and is consumed by pages, navigation, and CTAs.
- `app/globals.css` combines tokens, base styles, UI primitives, and showcase
  selectors. Splitting it is a separate visual-risk refactor and is not part of
  this migration.

## Proposed Moves

| Current path | Current consumers | Proposed target | Reason |
| --- | --- | --- | --- |
| `components/ui/button.tsx` | Quality lab; design contract test | `shared/ui/button.tsx` | Domain-neutral UI primitive |
| `lib/utils.ts` | Button | `shared/lib/cn.ts` | Domain-neutral class composition |
| `components/quality-lab-toggle.tsx` | Quality-lab route | `app/[locale]/quality-lab/_components/quality-lab-toggle.tsx` | Route-local client boundary |
| `components/fixture-toggle.tsx` | Quality-lab toggle and unit test | `app/[locale]/quality-lab/_components/fixture-toggle.tsx` | Route-local interaction |
| `components/sections/home-sections.tsx` | Home route | `app/[locale]/_components/home-sections.tsx` | Home-only composition |
| `components/sections/paros-sections.tsx` | Paros route | `app/[locale]/destinations/paros-antiparos/_components/paros-sections.tsx` | Destination-route composition |
| `components/layout/site-header.tsx` | Home and Paros routes | `features/showcase/components/site-header.tsx` | Cross-route, branded showcase navigation |
| `components/layout/language-switcher.tsx` | Site header | `features/showcase/components/language-switcher.tsx` | Internal navigation collaborator |
| `components/layout/site-footer.tsx` | Home and Paros routes | `features/showcase/components/site-footer.tsx` | Cross-route, branded showcase shell |
| `components/sections/showcase-media.tsx` | Home and Paros compositions | `features/showcase/components/showcase-media.tsx` | Cross-route showcase media and CTA behavior |
| `lib/routes.ts` | Pages, header, switcher, CTA, unit test | `features/showcase/routes.ts` | Client-safe showcase route contract |
| `lib/content.ts` | Home, Paros, and content tests | `features/showcase/server/content.ts` | Server/build-only showcase content boundary |
| `content/schemas/showcase.ts` | Loader, sections, validator, and tests | `features/showcase/content/schema.ts` | Showcase-owned content contract |

`features/showcase` is a provisional name grounded in the current code and
content vocabulary. Confirm it before implementation; renaming it to
`marketing`, `destinations`, or another future capability would be speculative
until the expanded product boundaries are defined.

No feature-wide `index.ts` is proposed. Consumers should use narrow,
statically-analyzable module paths so server-only content code cannot enter a
Client Component graph.

## Intentionally Retained

- Next.js files and route entry points under `app/`
- `app/globals.css` and `app/favicon.ico`
- `i18n/`, `messages/`, `proxy.ts`, and the next-intl plugin configuration
- localized JSON and media data under `content/`
- central `tests/` and `scripts/` organization
- the root `@/*` alias

Tests, scripts, and configuration stay in place but their imports and exact-path
contracts must follow moved source files. This includes `components.json`,
`vitest.config.mts`, `scripts/validate-content.mjs`, and the affected unit tests.
Historical references in `docs/` and `.scratch/` are records, not live imports,
and should not be rewritten as part of this structural migration.

## Migration Slices

1. Move the generic button and `cn` helper; update shadcn aliases and the design
   contract path.
2. Colocate the quality-lab client graph; update its test and coverage paths.
3. Establish the showcase routes, schema, and server content modules; update
   pages, validation, tests, and coverage paths.
4. Move the cross-route showcase shell and media components.
5. Colocate the Home and Paros compositions.
6. Search live source, tests, scripts, and configuration for stale imports;
   remove superseded paths only after explicit approval.

Each slice should pass focused tests and `pnpm typecheck`. The completed
migration should pass `pnpm format:check`, `pnpm lint`, `pnpm knip`,
`pnpm typecheck`, `pnpm validate:content`, `pnpm test:unit`, `pnpm build`, and
the applicable Playwright and accessibility checks on a verified free port.

## Approval Gate

Before implementation, confirm the provisional `showcase` feature name and the
path map above. Approval of this inventory must explicitly include removal of
the listed old source paths after their moved replacements and references have
been verified.
