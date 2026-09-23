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
- Contrast-check every foreground/background pair against WCAG AA. `--color-slate-500` on
  `--color-limestone-100` is the one to watch.
- Decide dark mode: **recommendation — no dark mode in v1.** A warm ivory travel brand does
  not need it, and it doubles every visual review.

---

## 2. What the design language consists of

### Tokens (`app/globals.css`)
Colour (above) · type scale · spacing scale · radii · shadows · motion durations.

```
Type   — display 3.5rem/3rem/2.25rem · h1 2.5rem · h2 2rem · h3 1.5rem
         body-lg 1.125rem · body 1rem · small 0.875rem · caption 0.75rem
         Heading font: Fraunces · Body font: Inter (S-005). Two families, no more.
         How to set them: §4.1
Space  — 4 8 12 16 24 32 48 64 96 128   (Tailwind default is fine; just don't freestyle)
Radius — 0 on images, cards and buttons (§4.5) · xs 4 for inputs · full for pills
Shadow — none on cards (§4.5); one elevation for overlays. That's it.
Motion — 150ms ease-out (micro) · 300ms ease-out (transitions). Respect prefers-reduced-motion
```

### Components (8, built on shadcn + Base UI)
`Button` (primary/secondary/ghost, 3 sizes) · `Card` (image + eyebrow + title + meta + body) ·
`Badge` (package type, destination) · `Input` + `Select` (filters only — the forms are on Google) ·
`Breadcrumb` · `Dialog` (mobile filter sheet) · `Gallery` (lightbox) · `Prose` (Portable Text renderer).

### Section patterns (4)
`Hero` (full-bleed image + scrim + headline) · `CardGrid` (2/3/4 col responsive) ·
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

### 4.1 Type

- **Load the whole family first.** `app/layout.tsx` imports `@fontsource-variable/fraunces`, which
  is the weight axis only, upright only: `opsz`, `SOFT` and `WONK` are missing and an italic would
  be a fake, browser-slanted one. The comps need `@fontsource-variable/fraunces/full.css` and
  `full-italic.css` (T-01.6 / GE-004.02 owns the final import).
- **Fraunces is set like a book serif, not a novelty face.** Weight 300–400 for display, never
  above 500. `opsz` follows the size (automatic once `full.css` is loaded). `SOFT` 0–50, `WONK` 0.
  The references set their display serifs at weight 500 or lighter, mostly regular or light —
  Lyon (Aman), Caslon (The Newt), Garamond (Openhouse), Epicene (Le Sirenuse). Nobody uses bold.
- **Display sizes are large and few.** 56–80px on desktop for the one headline per page (Le Sirenuse
  and The Newt set 60px, Openhouse 75px), tracking about −0.01em. Section heads 28–40px. Headlines are
  sentence case — uppercase serif reads as a magazine cover, not a sentence (Kinfolk).
- **One italic moment.** A headline may pair a roman line with an italic line — the place, then
  what it feels like: *"Paros & Antiparos / Slow days between two harbours"* (Openhouse, The Newt).
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
  4.47:1 on limestone, so no small teal text on limestone. One solid `--ge-blue-800` button per
  view. No full-width coloured bands except, at most, one `CtaBand`.
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
  Monocle 57%, The Newt 54% (Dexamenes' 66% is an upper bound — one section did not render in the
  capture). Aman, at 34%, shows what dense looks like — it can afford it; a small catalogue cannot.
- **Asymmetry is allowed and useful:** two-thirds plus one-third image pairs (Aman), an offset
  cluster of three or four photographs beside a text column (Dexamenes), or alternating 50/50
  rows with the photograph running to the viewport edge (The Newt, which is our `SplitFeature`).
- **Header: three things.** Menu, wordmark centred, one action (*Plan your trip*) — Le Sirenuse and
  Dexamenes do exactly this; Aman adds only search and a language switch. On mobile the one
  action may pin to the bottom as a full-width bar (Aman).

### 4.5 Components in this voice

- **Corners are square.** Every call-to-action measured has `border-radius: 0` (nine of the ten
  references; Cereal has no buttons), and every photograph in the captures is square-cornered.
  4px (`--radius-xs`) only on form inputs; `full` only on pills.
- **Handed to the token audit (T-01.5 / GE-004.01):** today `app/globals.css` still rounds with
  `--radius-sm` (8px) and up, and `.editorial-card` and the showcase card carry `--shadow-soft`.
  Both change to match this section.
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
