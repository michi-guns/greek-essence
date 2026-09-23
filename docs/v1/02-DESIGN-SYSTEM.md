# Greek Essence v1 — Design System

You called UI/UX the hardest part. It is, but not for the reason it usually is. The risk here
is not *"can we make it look good"* — it's *"can we make 9 templates feel like one product
without spending three weeks building a component library we don't need."*

**The rule for v1: build a design *language*, not a design *system*.** Tokens, a type scale,
a spacing rhythm, 8 components, 4 section patterns. Stop there.

---

## 1. Salvage what already exists

`app/globals.css` on the old `main` already contains a complete, considered token set:

- **Neutrals:** ivory / limestone / sand — warm, Mediterranean, not the default grey
- **Primary:** deep Aegean blue (`#17475f` → `#0b2433`)
- **Accent:** teal (`#34767a`)
- **Support:** olive, slate, plus semantic success/warning/error/info pairs
- Semantic aliases already mapped (`--color-primary-hover`, `--color-surface-subtle`, …)

This is genuinely good work and it is the single highest-value thing to carry across the
repo reset. **Copy it verbatim into the new tree, then validate it rather than redesign it.**

Validation (do this once, in Phase 1.1, ~1 hour):
- Contrast-check every foreground/background pair against WCAG AA. `--ge-slate-500` on
  `--ge-limestone-100` is the one to watch.
- Decide dark mode: **recommendation — no dark mode in v1.** A warm ivory travel brand does
  not need it, and it doubles every visual review.

---

## 2. What the design language consists of

### Tokens (`app/globals.css`)
Colour (above) · type scale · spacing scale · radii · shadows · motion durations.

```
Type   — provisional; §4.1 governs the comps, GE-004.01 (T-01.5) sets the final scale
         display 3.5–5rem · h1 2.5rem · h2 2rem · h3 1.5rem · lede 1.375–1.75rem (serif)
         body-lg 1.125rem · body 1rem · small 0.875rem · caption 0.75rem
         Heading font: Fraunces · Body font: Inter (S-005). Two families, no more.
         How to set them: §4.1
Space  — 4 8 12 16 24 32 48 64 96 128   (Tailwind default is fine; just don't freestyle)
Radius — 0 on images, cards and buttons (§4.5) · xs 4 for inputs · full for pills
Shadow — none on cards (§4.5); one elevation for overlays. That's it.
Motion — 220ms hover · 700ms image · 800ms reveal. Rules in DS-006 (§6). Reduced motion = none
```

### Components (8, built on shadcn + Base UI)
`Button` (solid/outline/link — DS-002, 3 sizes) · `Card` (image + eyebrow + title + meta + body) ·
`Badge` (package type, destination) · `Input` + `Select` (filters only — the forms are on Google) ·
`Breadcrumb` · `Dialog` (mobile filter sheet) · `Gallery` (lightbox) · `Prose` (Portable Text renderer).

### Section patterns (4)
`Hero` (full-bleed image + scrim + headline) · `CardGrid` (1/2/3 col responsive — DS-003) ·
`SplitFeature` (image one side, copy the other, alternating) · `CtaBand` (full-width, single action).

Every one of the 9 templates is a composition of these four. If a page needs a fifth pattern,
that's a decision, not an improvisation.

---

## 3. The sequence that de-risks it

This is the part that matters more than the token list.

1. **Direction before components.** Produce **2 static page comps** — Home and a Package
   detail — as real code at production quality. Nothing else. Then show the client.
2. **Get a single explicit "yes, this is the look."** In writing. This is the one client
   approval gate that cannot be skipped, because every later template inherits it.
3. **Only then extract** the tokens and components from those two pages. Components that
   come out of real pages fit; components designed in the abstract don't.
4. **Build the remaining 7 templates** against the extracted system. They should now be
   assembly, not design.

Doing 1–3 before 4 is what stops week 4 turning into "the client doesn't like it."

### Client review mechanics
The v0 decisions are right that this client needs **example-led** approval — he can react to
a concrete thing, not specify from blank. So: deploy every phase to a Netlify deploy preview URL and
send *links*, never descriptions. Ask closed questions ("keep this hero or the alternative?"),
never "what do you think?".

---

## 4. Art-direction brief (for whoever/whatever generates the comps)

> Quiet premium. Editorial, not e-commerce. The photography carries the emotion; the interface
> gets out of its way. Generous whitespace, large type, few borders, restrained colour — deep
> blue and teal used as punctuation, not as fields. Warm off-white ground, never pure white,
> never grey. No gradients, no glassmorphism, no card shadows competing with photos. Feels like
> a well-made printed travel journal that happens to be a website. The visitor should believe a
> real person in Greece is behind this, and that they take care with things.

The rules below turn that paragraph into decisions. Each one comes from ten boutique-hotel and
travel-editorial sites measured in Chrome (GE-003.01). The evidence — screenshots described,
fonts, sizes and colours read from each live page — is in
[`backlog/docs/doc-001`](../../backlog/docs/doc-001%20-%20Visual-research-annotated-references.md).
Reference names in parentheses point there.

**Comps: set this brief in your own CSS.** GE-003.03 (T-01.3) runs before the P1.2 token work,
and today's `app/globals.css` contradicts §4 (headings at weight 600, `h1` up to 6.8rem, 8px
buttons, cards with border, fill and shadow — full list in §4.5 — and `--font-display` /
`--font-inter` defined nowhere). Until P1.2 lands, each comp sets its own:
`font-family: 'Fraunces Variable'` and `'Inter Variable'`, display weight ≤ 500, radius 0, no card
border, fill or shadow. The §4.5 handoff to the token audit does not cover the comps.

### 4.1 Type

- **Load the whole family first.** `app/layout.tsx` imports `@fontsource-variable/fraunces`, which
  is the weight axis only, upright only: `opsz`, `SOFT` and `WONK` are missing and an italic would
  be a fake, browser-slanted one. The comps need `@fontsource-variable/fraunces/full.css` and
  `full-italic.css` (GE-004.02 (T-01.6) owns the final import). Fraunces has **no Greek
  glyphs** — no Greek-script display text in the comps (GE-022).
- **Fraunces is set like a book serif, not a novelty face.** Weight 300–400 for display, never
  above 500. `opsz` follows the size (automatic once `full.css` is loaded). `SOFT` 0–50, `WONK` 0.
  The references set their display serifs at weight 500 or lighter, mostly regular, light or thin
  — Lyon (Aman), Caslon (The Newt), Garamond (Openhouse), Epicene (Le Sirenuse, weight 100).
  Nobody uses bold.
- **Display sizes are large and few.** 56–80px on desktop for the one headline per page (Le Sirenuse
  and The Newt set 60px, Openhouse 75px), tracking about −0.01em. Section heads 28–40px. Headlines are
  sentence case — uppercase serif reads as a magazine cover, not a sentence (Kinfolk).
- **One italic moment.** A headline may pair a roman line with an italic line — the place, then
  what it feels like: *"Paros & Antiparos / Slow days between two harbours"* (Openhouse; The Newt
  sets its whole hero headline in italic).
  Fraunces has true italics, once `full-italic.css` is loaded.
- **The lede is serif.** The intro paragraph under a page headline is Fraunces at 22–28px
  (Kinsterna sets 23.5px; Le Sirenuse goes as far as 40px). Everything after it is Inter.
- **Inter is the working voice.** Body 16–18px, line-height 1.5–1.6, **60–72 characters per line**
  (Aman 62, Dexamenes 70). Left-aligned, never justified.
- **Labels are tracked caps.** Eyebrows, captions and nav: Inter 12–13px, uppercase, tracking
  0.1–0.2em (Aman's *AMANJENA, MOROCCO*, The Newt's nav at 0.2em). This is where the place names
  live: *CYCLADES · 8 DAYS*.

### 4.2 Colour

- **Ground:** `--ge-ivory-100 #faf6ed`. It already sits where the best references do — Aman
  `#f3eee7`, Cereal `#f7f6ef`. `--ge-limestone-100` for a secondary band, at most one per page.
- **Ink is blue.** Headlines in `--ge-blue-900` (12.2:1 on ivory), body in `--ge-slate-950`
  (15.2:1). Le Sirenuse sets *every* word in its one brand green and has no other UI colour; the
  equivalent here is Aegean blue as ink, not as a filled band.
- **Punctuation, not fields:** links keep the existing `--color-link` (`--ge-blue-800`, 9.3:1).
  `--ge-teal-700` is the focus ring (`--color-ring`) and the occasional accent — 4.85:1 on ivory,
  4.47:1 on limestone, so no small teal text on limestone. The one solid button per view (§4.5)
  is `--ge-blue-800`. No full-width coloured bands except, at most, one `CtaBand`.
- **Never as text:** `--ge-slate-500` (3.99:1) and `--ge-sand-500` (3.60:1) — lines and rules only.
  The one exception is disabled text (`--color-disabled-fg`), which WCAG exempts.
- **Target: under ~12% saturated pixels per page, photographs included.** The nine references
  that could be measured range 7–27% (median 10%); the calmest — Moroseta, Cereal, Dexamenes,
  Openhouse — sit at 7–8%, and Kinfolk tops the range only because its content is colourful
  magazine covers. The colour a visitor sees should come from the photographs.

### 4.3 Photography

This is the brief for image curation (M6), and it matters more than any rule above: the most
expensive-looking references are the ones whose photographs share one grade (Cereal, Aman).

- **One grade across the site:** natural light, warm, slightly muted. Late afternoon over midday.
  No HDR, no boosted turquoise, no sunset-orange skies. Where a stock image is too saturated,
  leave it out rather than use it.
- **Architecture, texture, food and detail, with landscape as the wide shot:** a whitewashed
  doorway, a plate from above, an olive grove, stone steps (Masseria Moroseta, Kinsterna). Each
  image carries one idea; wall-to-wall postcard panoramas are the exception, not the rule. People
  appear from behind or at a distance — which D-034 already asks for, for licence reasons.
- **Text goes beside or under a photograph, not on it**, except the one `Hero`. Captions sit
  below the image as tracked caps (Dexamenes, Moroseta).
- **Heroes are inset or full-bleed, never a carousel.** Inset means a 24–64px margin of ground
  around the image (Aman, The Newt); full-bleed means edge to edge (Dexamenes, Moroseta). A hero
  scrim is allowed only as far as the headline needs to pass contrast. The inset form is a
  variant of the `Hero` pattern in §2, not a fifth pattern; the direction pick decides which one
  ships.

### 4.4 Space and layout

- **55–70% of the page below the fold is bare ground.** Measured: Cereal 70%, Moroseta 62%,
  Monocle 57%; The Newt sits just under at 54%, and Dexamenes' 66% is an upper bound (one section
  did not render in the capture). Aman, at 34%, shows what dense looks like — it can afford it; a small catalogue cannot.
- **Asymmetry is allowed and useful:** two-thirds plus one-third image pairs (Aman), an offset
  cluster of three or four photographs beside a text column (Dexamenes), or alternating 50/50
  rows with the photograph running to the viewport edge (The Newt, which is our `SplitFeature`).
- **Header: three things.** Menu, wordmark centred, one action (*Plan your trip*) — Le Sirenuse and
  Dexamenes do exactly this; Aman adds only search and a language switch. On mobile the one
  action may pin to the bottom as a full-width bar (Aman).

### 4.5 Components in this voice

- **Corners are square.** The three references with boxed buttons (Aman, Dexamenes, Kinsterna)
  all use `border-radius: 0`; the others use plain text links. Every photograph in the captures is
  square-cornered. 4px (`--radius-xs`) only on form inputs; `full` only on pills.
- **Handed to the token audit (GE-004.01 (T-01.5)):** today `app/globals.css` still rounds with
  `--radius-sm` (8px) and up, and `.editorial-card` and the showcase card carry a border, a
  `--surface` fill and `--shadow-soft`. All of it changes to match this section.
- **A card is an image and a caption on the ground** — eyebrow, title, one line, a text link. No
  border, no fill, no shadow (Aman, Moroseta, Kinfolk).
- **Links do most of the work.** Secondary actions are underlined text — *Discover the itinerary*
  — not buttons (Aman, The Newt, Openhouse). One solid button per view; an outline button only on
  a photograph (Dexamenes).
- **Rules, not boxes.** Where structure is needed, a 1px `--color-border` hairline (Monocle), not
  a bordered container.

### 4.6 The three directions for GE-003.03 (T-01.3)

Same content, same tokens, deliberately different. Each takes its lead from references here.

| | Type-led | Image-led | Editorial grid |
|---|---|---|---|
| **After** | Le Sirenuse, Kinfolk, Openhouse | Dexamenes, Moroseta, Aman | Cereal, Monocle, The Newt |
| **First fold** | Headline in Fraunces at 72–80px, blue ink on ivory, italic second line. Photograph starts below it, inset. | Full-bleed photograph, wordmark and one outline button on it; headline small, bottom-left. | Headline + dek left, one tall photograph right, hairline rule under the header; packages begin inside the fold. |
| **Below** | Lede paragraph in the serif, then one image at a time. | Offset photo clusters with captions, very little text. | Numbered package index — *(01) Cyclades · 8 days* — in a 3-column grid. |
| **Risk** | Needs very good copy; weak headlines show. | Lives or dies on photography we do not yet have (§5). | Can read as a magazine rather than a service. |

### 4.7 What is ruled out

From the counter-examples in the evidence file:

- **Booking-engine chrome** — date pickers, "who / where / when" bars, price badges, "best rate
  guaranteed", urgency counters, star ratings (Casa Cook, Xenodocheio Milos, Hoshino). We have no
  availability to search (D-001, D-032c) and must not look as if we do.
- **The default Greek-hotel template** — one geometric sans for everything, justified body at 150+
  characters per line, a 12-link nav with a phone bar, saturated postcard colour (Perivolas).
- **Two brand colours as fields** — gold and navy boxed buttons, bordered slogan boxes, icon tiles
  (Xenodocheio Milos).
- **"Why book with us" checklists, testimonial carousels, splash intros** (Kinsterna).
- **Carried over:** stock-photo collage heroes, icon grids of abstract benefits, carousel heroes.

### 4.8 Checking a comp against this brief

Measurable, so a reviewer can check without taste arguments: display weight ≤ 500 · body line
length 60–72 characters · every radius on images and buttons is 0 · one solid button per viewport ·
bare ground 55–70% below the fold · saturated pixels under ~12%. The evidence file describes how
each number is taken. **The numbers support a visual
review; they do not replace one** (09-REVIEW §8.1).

---

## 5. Content dependency — the real schedule risk

A design system cannot be validated against lorem ipsum, and this design in particular lives
or dies on photography. **Photography is the highest-probability cause of a slipped launch.**

Mitigation, starting week 1:
- Ask the client for his image library *now*, before any design work.
- Agree a minimum set: 1 hero + 4 gallery per destination, 1 hero + 4 gallery per package.
- If he can't supply them, decide early between licensed stock (budget + who pays) or a
  design direction that leans on type and colour rather than full-bleed photography.
- Build with a clearly-labelled placeholder set so the pipeline is done and only the assets swap.

---

## 6. Design decisions record

How the design language in §2 and §4 is built in code. Written in GE-003.02 (T-01.2), before the
comps, so the comps (GE-003.03) and the P1.2 foundations build the same way. Numbered `DS-nnn`
alongside `D-` (00), `S-` (05) and `A-` (06).

### DS-001 Three component layers

Per S-004 (hand-written against Base UI) and 06-ARCHITECTURE §3–4 (folders, import direction).

| Layer | What goes in it | Props | Examples |
|---|---|---|---|
| `components/ui/` | One styled element. Wraps a Base UI primitive **only** when it needs behaviour — focus trap, dismiss, keyboard | element props + `variant` / `size` + `className` | `Button`, `Badge`, `Dialog` |
| `components/patterns/` | A repeatable composition around one domain DTO | a DTO | `PackageCard`, `Gallery` |
| `components/sections/` | A full-width page block. Owns vertical rhythm and the grid | DTOs or arrays of them | `Hero`, `CardGrid` |

- **Base UI where there is behaviour, plain HTML everywhere else.** v1 needs it for the mobile
  filter sheet (`Dialog`), `MobileNav` and the `Gallery` lightbox. The catalogue filter `Select`
  is a native `<select>`. A link styled as a button is an `<a>`, not a primitive.
- **`'use client'` stays on those wrappers,** never on a section. A section passes server-rendered
  children into them. 06 §6 owns the list of client components; this record adds none.
- **Every `ui/` component takes `className`, merged last with `cn()`.** A component never sets its
  own outer margin; spacing between things belongs to the caller or the section.

### DS-002 Utility, CVA variant, or new component

| Situation | Do | Example |
|---|---|---|
| Placement at one call site — margin, width, grid position | Utility classes through `className` | `<Button className="mt-8">` |
| A look that repeats and has a name | A CVA variant | `Button` `variant: solid \| outline \| link` — `outline` only on a photograph (§4.5) |
| Different markup, slots or meaning | A new component — after the second caller (06 §4) | `PackageCard` vs `DestinationCard` |
| A look used once | Nothing. It means the design is drifting; raise it | — |

- At most two variant axes per component (`variant`, `size`). No boolean style props
  (`isLarge`); compound variants only for a combination that really ships.
- Tokens only, no arbitrary values (06 §9). No per-component CSS files and no global component
  classes: the old `.editorial-card`, `.nav-links` and `.split` rules in `app/globals.css` are
  deleted in P1.2 as the components that replace them land.

### DS-003 Breakpoints

Tailwind 4 defaults, mobile-first. `md` and `lg` shape layout; `xl` only caps width:

| Name | From | Layout |
|---|---|---|
| base | 0 | One column. Designed at 390px |
| `md` | 48rem · 768px | Two-column splits, two-column card grid |
| `lg` | 64rem · 1024px | Full desktop: three-column grid, asymmetric pairs (§4.4). Designed at 1440px |
| `xl` | 80rem · 1280px | No layout change. The page container stops growing at `--container` (the existing token in `app/globals.css`) |

`sm` and `2xl` are not used for layout. **Cards answer to their container, not the viewport:**
`CardGrid` cells are `@container`, and a card changes shape at `@sm` / `@md`, because the same
`PackageCard` sits in a three-column grid and in a one-column related list. A-007 walks check
390, 768, 1024 and 1440.

### DS-004 Fluid type with `clamp()`

- **Fluid:** display, h1–h3, the lede and the pull quote. **Fixed on every device:** body 16px,
  body-lg 18px, labels, captions — small text that changes size between devices only reads as
  inconsistent.
- **The middle value is `rem + vw`, never `vw` alone.** A pure `vw` size ignores browser zoom, which
  fails WCAG 1.4.4. Today's `--text-*` tokens are `vw`-only (`clamp(3rem, 6vw, 4.75rem)`); handed
  to GE-004.01.
- **Interpolate from 390px to 1440px** (24.375rem to 90rem): `slope = (max − min) / 65.625`, middle
  value `(min − slope × 24.375)rem + (slope × 100)vw`.
- **Max no more than 2.5 × min.** With a `rem` term in the middle value, that ratio is what lets
  browser zoom reach 200% text size (WCAG 1.4.4) at any viewport width.
- Example — display 40px on a phone to 80px at 1440: `clamp(2.5rem, 1.571rem + 3.81vw, 5rem)`.

### DS-005 Icons

`lucide-react` (S-006).

- **Functional only:** menu, close, arrows, chevrons, plus / minus, and `ArrowUpRight` for a link
  that leaves the site (the Google Form handoff). No icon grids, no icons as decoration (§4.7).
- **Size follows the text:** 16px beside body text, 20px beside larger text, 24px only for a
  standalone icon button. `strokeWidth={1.5}` — lucide's default 2 is heavier than light Fraunces
  and Inter 400.
- **Colour is `currentColor`.** Never a filled or tinted icon tile.
- **Accessibility:** lucide 1.47 adds `aria-hidden` unless the icon gets `aria-label` or `title`
  (checked in `node_modules`). An icon-only button puts `aria-label` on the button, and its hit
  area is at least 44 × 44px.
- Named imports only (`import { ArrowRight } from 'lucide-react'`), so the bundle carries only
  the icons used.

### DS-006 🟡 Motion policy

Measured on 14 sites in Chrome — hover timings, scroll reveals and header behaviour read from
the live pages (evidence: [`backlog/docs/doc-002`](../../backlog/docs/doc-002%20-%20Motion-research-hover-reveal-scroll.md)).
The calmest references move least: Aman, Cereal, Monocle, Moroseta and The Newt have no scroll
reveals at all. Five of the ten references reveal on scroll, taking 0.8–1.9s: Le Sirenuse,
Openhouse and Kinsterna rise 50–100px, Kinfolk barely moves (0–58px), and Dexamenes moves each
block its own height (median ~450px, up to ~900px). **This policy keeps the reveal, but shorter
and closer.** 🟡 because motion is a design call, and it refines S-006 (below).

| Where | What moves | Timing | Evidence |
|---|---|---|---|
| Links, buttons | Colour or underline only. No movement, no scale | `--motion-base` 220ms, `--ease-standard` | References 100–500ms, median 300ms |
| Image in a card | Scale to 1.03 inside a fixed frame; the caption link underlines | 700ms, `--ease-emphasized` | The Hoxton 1.07 at 600ms; Kinsterna's 1.20 at 2s is the ceiling not to reach |
| Content below the fold | Fade from 0 and rise 24px, once, as it enters the viewport. Up to three siblings stagger 100ms apart | 800ms, `--ease-emphasized` | Openhouse 800ms / 60px, the quickest reference; Dexamenes moves a block its own height |
| The `Hero` on load | Photograph settles from scale 1.04 to 1; the italic headline line fades up 150ms after the roman line, which is at rest from the first paint | 1600ms photo, 800ms text | Judgement, not measured. Neither the photo nor the first headline line fades, so the largest paint is not delayed |
| Header | Sticky, and it does not change. Over a full-bleed photograph it takes the ivory ground once the hero has passed | 220ms colour fade | 9 of 14 sticky and unchanged |
| Focus ring | Appears at once, teal, 2px, offset 2px. Never animated | 0ms | 5 of 14 sites draw no outline or ring on any element tested — the one place to beat them |

**Ruled out:** smooth-scroll libraries that take over the wheel (Lenis, Locomotive — Kinfolk,
Casa Cook, Le Sirenuse); parallax; carousels (§4.3); hero video; page-transition libraries;
anything that moves after the page has loaded without the visitor scrolling, hovering or
clicking, and anything that loops; cursor effects. S-006's View Transitions stay: a plain
cross-fade between pages, no library.

**How it is built** (S-006 stays "no motion library"; 06 §6's client-component count is
unchanged):

- Hover, focus and the hero settle are CSS.
- Reveals and the header's colour change need one small script, not CSS alone. CSS scroll-driven
  animations were considered: they scrub with the scroll and play backwards on the way up, which
  is not how any reference feels.
- **Where the script lives:** `app/layout.tsx`, not a React component.
  1. A one-line inline script in `<head>` adds `js` to `<html>` before the first paint, so there
     is no flash of visible-then-hidden content.
  2. One `IntersectionObserver`, loaded with `next/script`, sets `data-inview` on each
     `[data-reveal]` element as it enters and stops watching it.
  3. The same observer watches the `Hero` and sets `data-past-hero` on the header once the hero
     leaves the viewport.
- **The hidden state exists only when both hold** — the script has run, and the visitor has not
  asked for reduced motion:
  `@media (prefers-reduced-motion: no-preference) { .js [data-reveal]:not([data-inview]) { … } }`.
  A failed script, a crawler or a reduced-motion visitor never sees an empty section — the
  problem that made three GE-003.01 captures unreadable. The existing reduced-motion rule at the
  end of `app/globals.css` keeps zeroing every duration.
- **A-007 walks run with reduced motion,** so full-page screenshots show every section at rest.
  The task that builds the reveal sets `use: { contextOptions: { reducedMotion: 'reduce' } }` in
  `playwright.config.ts`, and checks the reveal itself once in a normal-motion walk.
- Tokens handed to GE-004.01 (T-01.5): keep `--motion-base` 220ms, `--ease-standard` and
  `--ease-emphasized`; `--motion-image` becomes 700ms; add `--motion-reveal` 800ms and
  `--motion-stagger` 100ms.

### DS-007 Image aspect ratios

Four shapes, no others:

| Ratio | Where |
|---|---|
| 4:5 portrait | `PackageCard`, `DestinationCard`; the full-bleed `Hero` below `md` |
| 3:2 landscape | `SplitFeature`, `Gallery` thumbnails, images inside Portable Text, the inset `Hero`; the full-bleed `Hero` from `md` to `lg` |
| Full-bleed `Hero` from `lg` | Viewport-bound: full width, height `--hero-h` = `min(100svh − --header-h, 56rem)`. Both tokens are added by GE-004.01 (T-01.5), since arbitrary values are not allowed (06 §9) |
| Original | The `Gallery` lightbox only — the photograph uncropped |

Two card-and-feature ratios keep a page calm the way one photographic grade does (§4.3), and an
editor uploads each photograph once.

### DS-008 Sanity hotspot and crop

- **Every image field** has `options: { hotspot: true }` and a required `alt` (06 §13).
- **The crop rectangle is applied on Sanity's CDN,** because it is the editor's decision about
  what is in the photograph. `lib/sanity/map.ts` writes `rect=` into the DTO's `url`; the loader
  in `lib/sanity/image.ts` keeps it, since it only adds parameters to `new URL(src)`. The DTO's
  `width` and `height` are the cropped dimensions.
- **The hotspot becomes CSS:** `object-fit: cover` plus `object-position: x% y%` inside a
  fixed-ratio box, while the CDN serves `fit=max` widths. One set of URLs then works for every
  ratio in DS-007 and every breakpoint, including the `Hero` that is 4:5 on a phone and wide on
  desktop.
- **Why not crop per ratio on the CDN** (`fit=crop&crop=focalpoint`): a `next/image` loader only
  receives a width, so each ratio would need its own loader, and a box that changes ratio at a
  breakpoint would load the wrong crop. (A per-image `loader` prop is no way out either: it is a
  function, so it cannot be passed from a Server Component.)
- **The cost is real, so `sizes` must account for it.** When the photograph is wider than its box,
  `cover` renders it wider than the box: a 3:2 photograph in a 4:5 box is 1.875 × the box width,
  so the browser downloads about 88% more pixels than it shows. Set `sizes` to the box width ×
  `max(1, photoRatio ÷ boxRatio)`, from the DTO's `width` / `height` — otherwise the phone `Hero`
  loads a file too small for its rendered width and the largest image on the page looks soft.
- `lib/sanity/map.ts` converts the hotspot into percentages relative to the crop, not the
  original image, and adds `focus: { x, y }` to the `Img` DTO in 06 §5, which keeps its `lqip`.
- The Studio field description tells the editor what the circle means: *put it on what must
  never be cut off.*
