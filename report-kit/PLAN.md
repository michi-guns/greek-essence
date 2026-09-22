# ⚠️ TEMPORARY FILE — DELETE ON COMPLETION

**This file is not documentation. It is a parked implementation plan.**

The work described below — decomposing the published client brief into a Preact component
library with a build step — is **approved but not started**. It was deferred because the
owner's weekly model-usage budget was exhausted, not for any technical reason.

**When this plan has been implemented and the work is merged, delete this file.** It is the
only instruction in it that outlives the work. The repository should not carry a plan for
something that already exists; `README.md` and `CONVENTIONS.md` are the durable documents
here. Remove the pointer to this file from `README.md` in the same commit.

This file absorbed `HANDOFF.md`, the earlier build brief, which was then deleted. Its durable
rules — component architecture, and the list of deliberate oddities not to "fix" — moved into
`CONVENTIONS.md`, where they survive this file.

Written 2026-09-22.

---

# The plan: turn the published brief into a document builder

## Context

Greek Essence is a static marketing site for a boutique Greece travel agency. Alongside the
website, the project produces **internal documents** that pass between the developer and
Giorgos, the agency owner: the M7 client brief, and the phase reports meant to follow it.

That second product already has a home and accepted decisions:

- **D-052** — internal reports are a separate product. `report-kit/` at the repo root, own
  palette, own components, no imports in either direction, self-contained so `git subtree
split` can lift it out later.
- **D-053** — the brief's palette stays. Convergence with the site tokens was tested and
  rejected on coupling grounds.
- **D-054** — documents are built with Preact plus `preact-render-to-string` and esbuild, in
  TypeScript, emitting inert light-DOM HTML with zero runtime framework.

What exists today is the **finished brief as one hand-written 2000-line HTML file** at
`report-kit/dist/greek-essence-brief.html`, published to the client and signed off, plus
`CONVENTIONS.md` and the source assets. There is no package, no build script and no component
in the folder.

**Outcome:** a working build step and a component library that reproduce the published
document exactly. That converts a one-off artifact into a tool.

**Scope.** Decompose the one existing document. A second document is the natural follow-up and
is deliberately out of scope, per the owner's sequencing: set up the stack, decompose,
reproduce pixel-perfect, then wait for a real second document to force the API out.

---

## Findings about the baseline

Six things exploration and design turned up. Each contradicted the original build brief, and
each is load-bearing — they are recorded here so nobody has to re-derive them.

1. **The baseline is an HTML fragment.** No doctype, no html, head or body element. The CSS
   styles `body` anyway and the browser auto-wraps. The build must emit the same fragment
   shape, and the screenshot harness must wrap it in a real document or the page gutter rules
   never apply.
2. **The inline script is 173 lines, not about 40**, with five concerns: tab switching, a
   print-everything mode, reveal-on-scroll, a particle canvas, and **a runtime arithmetic
   self-check** that re-sums every duration in front of the reader and prints a tick or a
   warning. That check is a free regression test.
3. **22 classes are dead, not 34.** Nine names in the handoff's list never had a CSS rule. One,
   `all`, is alive: the script toggles it, and it is what makes the show-everything button
   work. Deleting it would break that silently, and the default-state screenshot would not
   catch it.
4. **Full-page screenshots are not reproducible at this page height.** Two captures of the
   unmodified baseline, with animations stopped and nothing changed, produce three different
   images. The page is over 20,000 pixels tall. Scroll-and-shoot viewport tiles are stable, and
   were proven stable across all eight width and motion combinations.
5. **Google Fonts is a live network dependency inside the test.** With the font race left open,
   all 41 tiles at the narrow width differed between two runs of the same file. The harness
   must wait for and assert the webfont.
6. **`pnpm check` is already red on `main`.** Prettier fails on six files, four of them the
   report-kit docs committed last night. Pre-existing, not ours, but it has to be cleared
   before branching or every run is red for unrelated reasons.

---

## One decision that needs your word

**Do not rename the 221 CSS classes to the `ge-` prefix.** `CONVENTIONS.md` says prefix every
class, so this contradicts something already written down and `AGENTS.md` says stop and ask
rather than quietly choose.

The reasoning: the prefix would not have prevented the collision it is credited with, because
that collision was between two classes in the same file, and a blanket prefix would have
renamed both to the same thing. What actually prevents it is one stylesheet per component,
which this decomposition delivers. Against that, renaming touches stylesheets, markup and the
script in one change, so a regression cannot be attributed to any of the three. Several class
names are a single character, which makes a mechanical rename unsafe. And it doubles the diff
on a branch whose acceptance test is looking at screenshots.

If you want it anyway, it lands as its own commit after everything else is green, driven by a
reviewed rename map and a parser-based codemod, never a find and replace. Identifiers stay
untouched in either case, since the client may already hold links containing them.

Two related things that do **not** need a decision, now that the design pass resolved them:

- **Assets regenerate byte-identically.** The brand logo on disk is larger than the published
  copy, but the image data is identical and the difference is one metadata chunk. Stripping it
  reproduces the published bytes exactly. The eight logos are percent-encoded rather than
  base64, and the exact encoding was recovered and verified against all eight. So assets are
  generated from source, not frozen as literals, and the published bytes still match.
- **The component count is about 45, not 25 to 35.** The extra twenty are the twelve worked
  examples inside the ask panels, which are genuinely different layouts, plus the ledger's
  table parts. Hitting 35 would mean pasting about 600 lines of markup into a data file.

---

## The acceptance bar, restated

The handoff asks for zero pixel difference. That holds, but it is only the last of five layers,
and the cheaper layers are what will actually drive the work day to day.

| Layer          | Bar                                                           | How                   |
| -------------- | ------------------------------------------------------------- | --------------------- |
| Stylesheet     | Byte-identical to the published block                         | Build assertion       |
| Inline script  | Byte-identical                                                | Build assertion       |
| Inlined images | Byte-identical                                                | Proven encoders       |
| Markup         | Same tags, attributes and normalised text, element by element | Parse both, walk both |
| Rendering      | Zero differing pixels, tile by tile                           | Playwright            |

Byte-identity of the whole file is not achievable, because the renderer will not reproduce hand
formatting of 140KB of markup. Byte-identity of everything except the markup is achievable, and
it removes the entire cascade-ordering risk from the pixel test.

Six gates run on every commit. Five are parsing checks that finish in milliseconds. Only the
pixel diff needs a browser.

| Gate             | Proves                                                                                                         |
| ---------------- | -------------------------------------------------------------------------------------------------------------- |
| Stylesheet order | The split files concatenate to the published bytes                                                             |
| Markup           | Element-by-element equality. **This is what catches a dropped space**                                          |
| Geometry         | Every element's box at four widths, so a failure reads as "this moved 1.4px", not "3,200 pixels differ"        |
| Arithmetic       | 67 rows, three grand totals, seven subtotals, seven hour labels, every cell's display matching its raw minutes |
| Contract         | Every element and selector the shipped script depends on still exists                                          |
| Publish          | One file, under 16MB, no external reference but Google Fonts                                                   |

**The harness is built first and proved green comparing the baseline with itself, before a
single component is extracted.** A gate that has never passed is not a gate.

---

## The whitespace question, settled

The two design passes disagreed here, and both were right about different things.

Whitespace **between block-level siblings is provably harmless**. Removing all 922
whitespace-only text nodes inside the page wrapper moved zero of 2,147 elements at four widths,
and produced a byte-identical screenshot. Every multi-child container in this document is flex
or grid, where whitespace-only nodes generate no boxes.

Whitespace **inside a prose paragraph is not harmless**. Every paragraph containing an inline
bold run is written on one physical line in the published file. Reflowing it across lines in
JSX deletes the newline and the space vanishes on screen. There are 47 paragraphs and 107 bold
runs in the asks view alone, and Prettier at a 100-character width would do this silently on
save.

So: keep each paragraph on one physical line, ignore the whole folder in Prettier, and let the
markup gate catch it mechanically if it ever slips.

---

## Target structure

```
report-kit/
  package.json  tsconfig.json  pnpm-workspace.yaml
  build.ts              # esbuild transpile -> renderToString -> inline CSS and assets -> dist/
  src/
    styles/             # tokens, base, one file per component, media tail last
    runtime/brief.js    # the document's inline script, copied verbatim, never transpiled
    components/         # one .tsx + one .css per component
    document/greek-essence-brief/
      render.tsx        # the document root — reads as an outline
      data/             # tasks, asks, logos, stats, stack, build tiles, time split
  assets/  dist/  tests/{baseline,visual}/
  README.md  CONVENTIONS.md
```

The root should read as an outline: page, backgrounds, tab nav, then three views each holding
a list of named blocks.

## Inventory, for orientation

30 top-level blocks across three views. 221 distinct classes, 135 used more than once.

- **Summary view, 9 blocks:** hero, tech strip, what-we-build tiles, where-time-goes stacked
  bar with legend, the comparison, progress, stat tiles, footer nav, signature.
- **Asks view, 13 blocks:** an intro panel, eleven near-identical ask panels, footer nav.
  **This is the highest-value extraction in the job** — one component driven by eleven typed
  records replaces eleven hand-written panels. Note there is no signature here, deliberately.
- **Technical view, 8 blocks:** table intro, estimate assumptions, stack rationale, hours
  distribution, how-to-audit, the 67-row ledger, footer nav, signature.

## Out of scope

- Any visual change, including ones you believe are improvements.
- Converging with the website's palette or tokens. Decided against; see D-052 and D-053.
- Shadow DOM, `@scope`, a dev server, a second document, a published package.
- Generalising components for hypothetical future documents.

---

## Phase 0 — clear the ground

Two commits on `main`, before branching.

**Isolation.** `report-kit/` gets its own package and its own install, but three root tools
reach into the folder and must be told not to.

| File                | Edit                                                                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `tsconfig.json`     | add `"report-kit"` to `exclude` — `include` is unanchored, so typecheck breaks on the first Preact file                             |
| `eslint.config.mjs` | add `'report-kit/**'` to the global ignores — 113 rules resolve there, 60 of them errors, and the commit hook would rewrite sources |
| `.prettierignore`   | add `report-kit/` wholesale, not just `dist/`                                                                                       |
| `.gitignore`        | add `report-kit/node_modules/`, `.tmp/`, `.artifacts/` — the existing entries are anchored to the root                              |
| `.gitattributes`    | pin the built and baseline HTML to line-feed endings                                                                                |

**Then format the two remaining files** so `pnpm check` is green. Separate commit, pure
whitespace, and it must come after the ignore so the report-kit docs are already invisible.

**Verify the workspace assumption before anything else.** pnpm searches upward for the
workspace file and will find the root one. A two-line workspace file inside `report-kit`
scoped to itself stops that. Confirm the root still reports exactly one project and a frozen
install stays green. Do not proceed until it does.

---

## Phase 1 — harness before components

Freeze the published file as a permanent committed baseline under `report-kit/tests/baseline/`.
It is never regenerated. It is the contract that a fresh build still renders like the artifact
the client signed off, and it is what keeps the test meaningful after the decomposition lands.

Build the six gates and prove all six green **baseline against baseline**.

The pixel harness specifics that were measured, not guessed: viewport tiles at 900px steps,
never full-page; four widths at double scale, each with and without reduced motion, plus one
run in the default single-view state; animations killed outright rather than paused, because
pausing pins a phase and the phase is not equal across two loads; the particle canvas hidden;
the font awaited and asserted; no retries, because a retry on a pixel test hides the
nondeterminism you are trying to remove. Both documents load from the filesystem, since the
output has exactly one external reference.

On a mismatch the harness writes expected, actual and difference images and reports the tile,
the page offset and the first differing pixel.

---

## Phase 2 — prove the pipeline before decomposing

One giant component. The entire markup pasted as a single JSX blob, the stylesheet verbatim as
one file, the script copied byte-for-byte and never transpiled.

The mechanism: esbuild bundles the component entry to a temporary module, Node imports it by
file URL and calls the renderer, and the build assembles title, font link, stylesheet,
background layers, markup and script into the fragment. Every file read normalises line
endings on the way in, so a carriage return can never reach the output.

All six gates green before moving on. This step surfaces every conversion trap at once. Do not
proceed on a close-enough diff.

---

## Phases 3 to 9 — extract, one gate at a time

Each phase ends with the gates green. The order is chosen so that a failure can only have one
cause.

| Phase | What comes out                                                                                | The gate that matters                                      |
| ----- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 3     | The stylesheet splits into component files, markup untouched                                  | Stylesheet order. A failure here can only be a split error |
| 4     | The shell: page, backgrounds, tab nav, view, panel, heading, footer nav, signature, reveal    | Markup and contract                                        |
| 5     | The ledger and the 67 tasks                                                                   | Arithmetic, including the hour labels                      |
| 6     | The rest of the technical view                                                                | Contract: the audit line and the show-all button survive   |
| 7     | The ask panel and the eleven records, then the twelve worked examples lift out as a pure move | Markup, exact. A pure move must be a zero diff             |
| 8     | The summary view, one block per commit                                                        | Markup and pixels after each                               |
| 9     | Delete the 22 dead classes, rule by rule                                                      | Stylesheet order with the dead set subtracted              |

Two details that will bite if they are skipped.

**Subtotals are derived, not stored.** The document already re-sums every duration in front of
the reader whose whole purpose is auditing the hours. A stored subtotal that disagreed would
make the document contradict itself on screen. Build-time assertions against the published
values provide the safety instead.

**The hour labels round half to even.** The first milestone is 13.25 hours and the document
prints 13,2. Ordinary one-decimal rounding gives 13,3. Two milestones land exactly on the half
and round in opposite directions. This affects 21 visible strings.

**Dead-class deletion is rule by rule, never a line range.** Live rules sit inside the dead
cluster.

---

## Phase 10 — close it out

Write the component index into `README.md`. Add one line to the root agent guide so agents
find this without a skill. Record the class-prefix decision and the two asset encoders in
`CONVENTIONS.md`. **Then delete this file and its pointer in `README.md`.**

Add a separate continuous-integration workflow for report-kit, filtered to its own paths so the
website's checks keep running untouched on every change. It typechecks, builds, asserts that the
committed output equals a fresh build, then runs the pixel suite. That last check is worth its
five minutes: the committed-output check catches someone forgetting to rebuild, but only the
frozen baseline catches a rebuild whose rendering has moved.

---

## Process

**No backlog task, deliberately.** This corrects an earlier draft of this plan, which said to
create one. `report-kit/` is internal tooling, not client scope. The roadmap's 67 estimated
tasks and the hour totals reconcile against each other, and the client has already been shown
those numbers in the published brief. Adding tasks here would corrupt them. Track progress in
the branch and the pull-request body instead.

**Branch.** One branch off `main`, `chore/report-kit-decomposition`, rather than the phase and
task branches the website work uses — there are no backlog tasks to name them after.

**The merge to `main` is pre-authorised once the checks are green** (D-023: agents may merge
phase into `main` once checks pass). This corrects an earlier draft of this plan, which said
the merge waits for the owner. It does not. What still needs the owner is a force-push, a
history rewrite, or deleting an unmerged branch.

**Before starting,** confirm headless Chromium runs. The pixel diff is not optional; a refactor
verified by eye is not verified. If it cannot run, say so and stop.

**Review.** Every phase from 2 onward is a non-trivial change, so each goes through the
independent review loop before it is called done: a fresh reviewer with no session context,
given the diff and the settled decisions, fixing blocking and material findings and re-running
the gates until a pass verdict or five rounds.

**Evidence.** Screenshots and gate output land in `.local/evidence/` per the repo's walk rule.

**Notification.** This is long unattended work, so it ends with a single phone notification:
done on completion, escalate if something needs you.

---

## Verification you can check yourself

When it is finished, the proof is three things you can run or look at in under a minute:

```bash
cd report-kit && pnpm test
```

That typechecks, builds, and runs the full gate suite including the pixel diff against the
frozen published baseline.

```bash
git diff --exit-code -- report-kit/dist
```

Silence means the committed document is exactly what a fresh build produces.

And the document itself, opened in a browser: the audit line at the bottom of the technical
view must read with a tick and 67 tasks. The document audits its own arithmetic, so if that
line is right, the entire duration surface survived the refactor.
