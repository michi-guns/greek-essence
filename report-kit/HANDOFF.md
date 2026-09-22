# report-kit — build brief

**For the agent picking this up.** Everything here is decided. Where a decision is recorded,
it is not an invitation to redesign — if you think one is wrong, say so and stop, don't
quietly do something else (`AGENTS.md` → Posture).

---

## 1. What you are building

`report-kit` is a tiny component library plus a build step that produces **internal project
documents** — reports that go between the developer and Giorgos, the agency owner. It is
**totally isolated from the Greek Essence website**: different audience, different job, its own
palette. Do not import from, or align to, `app/globals.css` or `docs/v1/02-DESIGN-SYSTEM.md`.

The first and currently only document is the client brief, already finished and published.
**Your job is to decompose it into components without changing a single rendered pixel.**

## 2. Ground truth

| | |
|---|---|
| Current output | `report-kit/dist/greek-essence-brief.html` — one self-contained file, ~219KB |
| Published at | claude.ai artifact, version 12 — the file above is byte-identical to it |
| Assets | `report-kit/assets/logos/*.svg` (8), `report-kit/assets/brand/greek-essence-logo.png` |
| Rules you must follow | `report-kit/CONVENTIONS.md` — **read this first, all of it** |

The published file is the acceptance baseline. It is correct. It has been through three
adversarial visual review rounds and the client has signed off on how it looks.

## 3. Non-negotiable constraints

1. **Output is one self-contained HTML file.** Artifact pages block every external origin
   except `fonts.googleapis.com`. CSS, JS and images are inlined at build time.
2. **Output is plain, parsable, light-DOM HTML.** The client pastes this into an AI to check
   whether 141.5 hours is honest. No Shadow DOM, no client-side rendering of content.
3. **Zero runtime framework.** Preact renders to a string at build time and ships nothing.
   The only JS in the output is the existing ~40 lines for tabs, reveal-on-scroll and particles.
4. **Pixel-identical to the baseline.** See §8.

## 4. Decisions already made

| Decision | Choice |
|---|---|
| Location | `report-kit/` at repo root. Self-contained — no imports reaching into the parent — so `git subtree split` can lift it out later. Not a submodule. |
| Renderer | **Preact + `preact-render-to-string`**, transpiled by **esbuild**. Chosen over Astro (wants routing and split assets), 11ty (SSG machinery for one page), and raw template literals (loses escaping, typing and editor support). |
| Language | **TypeScript.** Typed props on the data-driven components are where an arithmetic error gets caught at compile time instead of by a reviewer. |
| Styling | Plain CSS, **light DOM**, every class prefixed `ge-`. No `@scope` yet — see CONVENTIONS. |
| Content | **Hybrid.** Repeating structures (67 tasks, 11 asks, 8 logos, stat tiles) live in typed data files. Prose stays inline in the component that renders it, where it reads in context. |
| Decomposition depth | **Componentise everything, including single-use blocks.** |
| Single-use rule | A single-use component takes **no props.** Content inline, zero API. Inventing a props API for one caller is how the library rots. When a second caller appears, *that* tells you the real API. |
| Dev loop | `npm run build` and a watch flag. No dev server. |
| Palette | Unchanged. Isolated from the website by decision, not drift. |

## 5. Target structure

```
report-kit/
  package.json
  tsconfig.json
  build.ts              # esbuild transpile → renderToString → inline CSS + base64 assets → dist/
  tokens.css            # palette, type scale, radii, shadows, spacing rhythm
  components/           # one .tsx + one .css per component
  documents/
    greek-essence-brief/
      index.tsx         # the document root — reads as an outline
      data/             # tasks.ts, asks.ts, logos.ts, stats.ts
  assets/
  dist/
  README.md  HANDOFF.md  CONVENTIONS.md
```

The document root should end up readable as an outline:
`<Page><Hero/><TechStrip/><WhatWeBuild/><WhereTimeGoes/>…</Page>`

## 6. Component inventory

Taken from the live file. 30 top-level blocks across three views; 221 distinct classes, 135
used more than once, 86 used exactly once.

**View 1 — Σύνοψη (9 blocks):** `Hero` (brand, dateline, logo, headline, 9-vs-141 ratio,
timeline chips, thesis, CTA) · `TechStrip` (logo marquee) · `WhatWeBuild` (4 tiles) ·
`WhereTimeGoes` (stacked bar + legend) · `AiComparison` (two bars + saved figure) ·
`Progress` (bar + reconciliation) · `Stats` (4 tiles) · `NextNav` · `Sig`

**View 2 — Τι χρειαζόμαστε (13 blocks):** an intro panel, then **11 near-identical ask
panels** (A1–A11: code, title, why, what it blocks, cost of delay, fallback + quality cost,
worked example), then `NextNav`. **This is the highest-value extraction in the whole job** —
one `AskPanel` component driven by an array of 11 typed records replaces eleven hand-written
panels.

**View 3 — Τεχνικά (8 blocks):** task table intro · estimate assumptions · stack rationale ·
hours distribution · how-to-audit-this-table · **the 67-row task table** (the second big data
extraction) · `NextNav` · `Sig`

**Shared shell:** `Page`, `TabNav`, `Panel`, `PanelHead` (eyebrow + h2 + intro), `WaveBg`,
`DustBg`, `Reveal`.

Expect roughly 25–35 components under the everything-is-a-component rule. Most take no props.

**Delete on sight — 34 classes with CSS but no markup**, left over from sections cut during
iteration: `all, ask, ask-top, asks, cx, cxw, first, metrics, mins, mk, mu, mv, org, segs,
special, starthead, step, step-top, steps, tbar, tbox, tint, tkey, tline, totals, totchip,
ubar, unlock, us, uu, uv, you`. Leave `js` and `js-anim` — they are toggled from script.

## 7. Suggested order

1. Scaffold: `package.json`, `tsconfig`, `build.ts`, and get the **current HTML rendering
   through Preact unchanged** as one giant component. Prove the pipeline before decomposing.
2. Extract `tokens.css`. Confirm nothing moved.
3. Extract the shared shell (`Page`, `Panel`, `PanelHead`, `TabNav`, `NextNav`, backgrounds).
4. Extract View 2's `AskPanel` + `asks.ts`. Biggest win, and the clearest data shape.
5. Extract View 3's task table + `tasks.ts`.
6. Extract View 1 block by block.
7. Delete the 34 dead classes. Re-verify.
8. Write `README.md` as the component index, and add one line to root `AGENTS.md` pointing at
   it — the owner wants agents to find this without a skill.

Verify after **every** step, not at the end.

## 8. Verification — this is the acceptance test

Render the baseline and your build, and diff them as images:

```bash
# playwright + chromium are available; deviceScaleFactor 2
# capture both files at 1120, 900, 660, 380 and at reducedMotion:'reduce'
# compare pixel-by-pixel; the animated marquee and particles need a
# frozen frame (set animation-play-state:paused) before comparing
```

**Zero pixel difference is the bar**, other than the marquee/particle frames. If output moves,
the extraction is wrong — do not "improve" the design while refactoring. Design changes are a
separate task with the owner's sign-off.

Also assert, in the build:
- totals still reconcile: 4560 / 8490 / 17280 minutes across 67 rows and 7 phase subtotals
- every duration cell carries a `data-m` matching its display string
- no external `src`/`href` in the output except `fonts.googleapis.com`
- output is a single file under 16MB

## 9. Out of scope

- Any visual change, including ones you believe are improvements.
- Converging with the website's palette or tokens. Decided against; see `00-DECISIONS.md`.
- Shadow DOM, `@scope`, a dev server, a second document, a published npm package.
- Generalising components for hypothetical future documents.
