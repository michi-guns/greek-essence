# report-kit — conventions

Rules learned by building the Greek Essence client brief. Every one of these cost a review
round or a client-visible defect. Read before editing anything that renders.

## Naming

**Prefix every class `ge-`.** The v1 document has 221 distinct classes, many of them one or
two characters (`n`, `t`, `c`, `e`, `u`, `l`, `v`, `k`, `s`, `p`, `h`). That is how `.lg` — the
legend row — was silently overwritten by a new `.lg` logo class. Both rules stayed in the file
and cross-applied: legend rows inherited background sizing, and every logo inherited the
legend's `display:grid` and `border-bottom`. It looked plausible on screen and took a user
report to find.

Do **not** reach for CSS `@scope` yet. It is the right mechanism and it is Baseline _Newly
Available_ (Firefox 146, January 2026), but an unsupporting browser drops the whole block —
the styles vanish rather than degrade. A prefix convention costs nothing and cannot fail.
Revisit when `@scope` reaches Widely Available.

## Greek text

**`lang="el"` on the wrapper is load-bearing.** CSS `text-transform:uppercase` applied to Greek
keeps the tonos unless the element is in a Greek language context — you get `ΠΛΑΊΣΙΟ` instead
of `ΠΛΑΙΣΙΟ`, which is an orthographic error a Greek reader sees immediately. Verified in
Chromium: with `lang="el"` the accents are stripped correctly, without it they are not. Never
remove that attribute, and never assume it is inherited into a shadow root or an iframe.

## Layout

**A `%`-based mask or gradient ramp collapses at small widths.** The logo marquee faded its
edges with `linear-gradient(90deg,transparent,#000 6%,...)`. At 380px that 6% is 22px, narrower
than the tile's own 18px padding — so the first tile's text rendered at nearly full opacity
right at the strip edge and read as clipped, broken text. Use fixed lengths:
`linear-gradient(90deg,transparent 0,#000 64px,#000 calc(100% - 64px),transparent 100%)`.

**Overlap needs geometry _and_ paint order.** The tech strip is pulled 12px up under the hero
card. Correct geometry, but `position:relative; z-index:0` on the strip creates a stacking
context, and as a later sibling it painted _in front_ of the hero — its square top corner sat
on top of the hero's rounded corner. Pixel-sampling columns will not catch this; it tells you
which pixels are there, not which element drew them. Zoom in and look. Fix was `z-index` on
the hero, above the strip.

## Numbers

- `font-variant-numeric: tabular-nums` on every figure. Non-tabular digits make columns of
  numbers jitter and undermine a document whose whole argument is arithmetic.
- **Durations display as `2ω 15λ` and carry raw minutes in `data-m` and `title`.** The display
  form is for the client; the raw form is for the AI auditor he will paste this into.
- **Every number must reconcile, in every view.** 67 rows, seven phase subtotals, and the
  grand totals 4560 / 8490 / 17280 minutes = 76.0 / 141.5 / 288.0 hours. Change one estimate
  and all three views plus the hero move. A wrong arithmetic _operator_ shipped once — `5 × 495`
  where the truth was `5 tasks totalling 495` — inside the exact paragraph written for the
  auditor. Re-verify totals after any content edit.

## Colour

Floor is WCAG AA 4.5:1 for text under 18px. `--c3-solid: #B4520F` exists for exactly one
reason: white on `--c3` (`#C65C14`) measures 4.25:1, just under. It is used by the orange
stacked-bar segment and its matching legend dot, and nowhere else. `--c3` itself is unchanged.

The data colours are validated for protanopia and deuteranopia — separation is carried by
lightness and the blue/warm axis, which survives both. Do not substitute a colour into a chart
role without re-running the check.

## Motion

`prefers-reduced-motion` must produce a **static fallback that still works**, not merely a
stopped animation. The marquee's fallback is a centred 4+4 grid with the dividers suppressed
and `max-width:500px` forcing the break — a bare `animation:none` leaves one sequence
overflowing off-screen.

Marquee seamlessness = two identical sequences in the rail, animating `translateX(0 → -50%)`.
Any asymmetry between the two sequences shows as a visible jump once per cycle.

## Publishing (Artifact pages)

- The only external origin allowed is `fonts.googleapis.com`. Everything else — CSS, JS,
  images — must be inline or a `data:` URI. This is a _publish_ constraint, not an authoring
  one: author in separate files, inline at build time.
- **No Shadow DOM.** The client feeds this document to an AI to sanity-check the hours.
  Shadow content is harder to parse and complicates find-in-page and print. Light DOM only.
- Page size ceiling is 16MB. The current document is ~219KB, of which ~40KB is base64 assets.

## Component architecture

Decided before the library was built. These rules outlive any one document.

- **Componentise everything, including single-use blocks.** A block that appears once still
  gets its own file. The document root then reads as an outline.
- **A single-use component takes no props.** Content inline, zero API. Inventing a props API
  for one caller is how the library rots. When a second caller appears, _that_ tells you the
  real API.
- **Content is hybrid.** Repeating structures — task rows, ask panels, logo tiles, stat tiles
  — live in typed data files. Prose stays inline in the component that renders it, where it
  reads in context.
- **TypeScript, always.** Typed props on the data-driven components are where an arithmetic
  error is caught at compile time instead of by a reviewer.
- **Plain CSS in the light DOM.** No CSS-in-JS, no Shadow DOM, no `@scope` yet — see Naming.
- **Zero runtime framework.** Preact renders to a string at build time and ships nothing. The
  only JavaScript in the output is the document's own inline script.

## Deliberate oddities — do not "fix" these

Each looks like a defect and is not. All were flagged to the owner and kept on purpose.

- **`assets/logos/google-forms.svg` is not the Google Forms logo.** It is the four-colour
  Google Developers chevron. The real Forms mark could not be sourced, the strip scrolls, and
  the tile is decorative. Leave it.
- **The Sanity tile's label is in the markup but hidden by CSS**, while the other seven tiles
  show theirs. Its wordmark already says the name. Keep the label in the DOM — the rail's
  accessible name is built from it.
- **`--c3-solid` exists for exactly one bar segment and one legend dot.** See Colour.
- **The palette does not match the website's.** Deliberate isolation (D-052, D-053).
- **The hero's call-to-action link carries a `data-go` attribute that nothing binds.**
  Pre-existing and harmless. Giving it the handler class would change its appearance.

## Review

Visual work is verified by **looking at screenshots**, not by reading CSS or measuring the DOM.
Both defects that reached the user — the nested `<div class="hero">` that made every card look
like one continuous surface, and the strip painting in front of the hero — passed
measurement-based checks and failed instantly on inspection. Render, crop, and look.
