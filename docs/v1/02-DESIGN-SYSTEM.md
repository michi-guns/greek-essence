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
         Heading font: a serif with character (Fraunces / Newsreader / Cormorant)
         Body font: Inter or Geist. Two families, no more.
Space  — 4 8 12 16 24 32 48 64 96 128   (Tailwind default is fine; just don't freestyle)
Radius — sm 4 · md 8 · lg 16 · full
Shadow — one elevation for cards, one for overlays. That's it.
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

## 4. Visual direction brief (for whoever/whatever generates the comps)

> Quiet premium. Editorial, not e-commerce. The photography carries the emotion; the interface
> gets out of its way. Generous whitespace, large type, few borders, restrained colour — deep
> blue and teal used as punctuation, not as fields. Warm off-white ground, never pure white,
> never grey. No gradients, no glassmorphism, no card shadows competing with photos. Feels like
> a well-made printed travel journal that happens to be a website. The visitor should believe a
> real person in Greece is behind this, and that they take care with things.

Anti-patterns to avoid: booking-engine chrome (price badges, urgency counters, star ratings),
stock-photo collage heroes, icon grids of abstract benefits, carousel heroes.

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
