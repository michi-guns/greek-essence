---
id: doc-001
title: Visual research - annotated references
type: specification
created_date: '2026-09-23 09:17'
updated_date: '2026-09-23 09:28'
---
# Visual research — annotated references (GE-003.01)

Captured 2026-09-23. Ten references and three counter-examples from boutique hotels, a hospitality
group and travel/design editorial. No travel-agency templates. The distilled rules live in
[`docs/v1/02-DESIGN-SYSTEM.md` §4](../../docs/v1/02-DESIGN-SYSTEM.md); this file is the evidence
behind them.

**How the numbers were taken.** Each site was loaded in Chrome at 1440×900 and 390×844. Fonts, sizes,
weights, tracking and colours are computed styles read from the live DOM, not guesses. Two numbers
come from the pixels of the desktop full-page capture, below the first fold:

- **Bare ground** — the share of pixels within a small distance of the page's dominant background
  colour. It is the whitespace ratio: how much of the page is empty ground.
- **Saturated** — the share of pixels with HSV saturation above 0.35 (value above 0.2). It is the
  colour-restraint number, and it includes the photographs.

A number is not a verdict: every screenshot was looked at, and the notes say what was seen.
Screenshots and `facts.json` are local only, in `.local/evidence/2026-09-23-visual-research/`.

| | Reference | Kind | Display / text faces | Ground | Bare ground | Saturated |
|---|---|---|---|---|---|---|
| 1 | Le Sirenuse, Positano | Hotel | Epicene Display, one family | `#f8f8f8` | n/a¹ | n/a¹ |
| 2 | Aman | Hotel group | Lyon Text + Whitney | `#f3eee7` | 34% | 16% |
| 3 | Masseria Moroseta, Puglia | Boutique hotel | Fira Mono + Tinos | `#ffffff` | 62% | 7% |
| 4 | Dexamenes, Peloponnese | Boutique hotel (GR) | Helvetica Neue Light | `#ffffff` | ≤ 66%² | 8% |
| 5 | The Newt in Somerset | Hotel + estate | Adobe Caslon + Avenir Next | `#ffffff` | 54% | 18% |
| 6 | Kinsterna, Monemvasia | Boutique hotel (GR) | corporate-a + Open Sans | `#e5e5e5` | 56% | 16% |
| 7 | Kinfolk | Magazine | Kinfolk Serif + Kinfolk Sans | `#ffffff` | ≤ 44%² | 27% |
| 8 | Cereal | Travel magazine | Adobe Text + Neue Haas Unica | `#f7f6ef` | 70% | 7% |
| 9 | Openhouse | Design magazine | EB Garamond + Sneak | `#ffffff` | 45% | 8% |
| 10 | Monocle — Travel | Magazine | Plantin + Helvetica Neue | `#ffffff` | 57% | 10% |
| ✕ | Perivolas, Santorini | Hotel (GR) — counter | Montserrat only | `#1c1c1c` | 52% | 19% |
| ✕ | Casa Cook | Hotel group — counter | Oswald + Courier Prime | `#f8f6f2` | 50% | 8% |
| ✕ | Xenodocheio Milos, Athens | Hotel (GR) — counter | PF Regal Display + Averta | `#ffffff` | 62% | 11% |

¹ Le Sirenuse's full-page capture is broken: its content below the video appears on scroll and
did not render in the capture (the DOM records a heading at y=2340 that the image shows as empty
ground). Both pixel numbers would measure the capture, not the design, so they are left out. Its
type and colour values come from the DOM and stand.

² One section on each of these pages reveals on scroll and shows as a blank band in the capture,
so the bare-ground number is an upper bound.

Corners: **square everywhere.** The script measured one call-to-action per site; all nine sites
that have one return `border-radius: 0` (Cereal has no buttons), and every photograph in the
captures is square-cornered. None puts a shadow on a card.

---

## 1. Le Sirenuse — https://www.sirenuse.it

**Seen:** wordmark centred, `MENU` left and `BOOK` right in small caps, nothing else in the header.
A three-word headline, *"A world apart."*, in a light display serif, then a full-width video. On
mobile the intro paragraph is set in the display face at ~30px, centred.

- **Type:** one family does everything. Headline 60.5px, light weight, tracking −0.5px. Section
  heads 40px. Nav 18px uppercase in the same serif.
- **Colour:** *every* piece of text is one green, `#11695d`, on near-white `#f8f8f8`. There is no
  second UI colour. The brand colour is the ink, not a fill.
- **Image:** full-bleed video directly under the headline; the headline never sits on the photo.
- **Steal:** brand colour as the text colour — for us, deep Aegean blue as ink on ivory. The
  three-item header.
- **Don't copy:** long paragraphs set in the display face at 40px — striking once on a home page,
  tiring on a package page.

## 2. Aman — https://www.aman.com

**Seen:** warm limestone ground, the hero video inset by a 25px margin rather than bleeding. Each
story is an eyebrow in tracked caps (*AMANJENA, MOROCCO*), a serif title, and an underlined
"Discover more". Images pair up as two-thirds plus one-third. On mobile a single full-width
`Reserve` bar is pinned to the bottom.

- **Type:** Lyon Text 31px regular for titles, tracking +0.5px; Whitney 14px for UI. Body 14px,
  line length ≈ 62 characters.
- **Colour:** ground `#f3eee7`, text `#313131`, and one solid dark button (`#313131`, radius 0,
  10×15px padding). The only colour on the page comes from the photographs.
- **Image:** inset, generous, consistently warm and desaturated grade; no text on images.
- **Steal:** the eyebrow → title → text-link card; one solid button per screen; the pinned
  single action on mobile.
- **Don't copy:** its density (34% bare ground) — Aman can afford it with a vast photo library;
  we cannot.

## 3. Masseria Moroseta — https://www.masseriamoroseta.it

**Seen:** the closest subject match — whitewashed walls, a doorway framing a courtyard, hard
Mediterranean light. Below it, a two-column grid of photographs with a centred monospace title and
two lines of serif text under each.

- **Type:** Fira Mono 28px, tracking +1px, for headings and nav; Tinos 16px/25 for body in grey
  `#727272`. A monospace display is an unusual, memorable choice.
- **Colour:** white ground, grey text, 7% saturated pixels — the photographs carry all the colour
  and even they are mostly white and ochre.
- **Image:** architecture and detail, not panoramas. A bowl of tomatoes shot from above, olive
  trees at sunset, a boat on turquoise water — each image one idea.
- **Steal:** the photographic brief itself (see §4 of 02-DESIGN-SYSTEM). The image grid with the
  caption *under* the picture, never over it.
- **Don't copy:** the partner-logo strip and the mid-page newsletter form.

## 4. Dexamenes — https://www.dexamenes.com

**Seen:** a Greek hotel in a converted winery. A dark, slow video hero with only a thin wordmark and
a hairline "Book Now" outline button. Below, the layout breaks symmetry: a text column on the left,
an offset cluster of four photographs on the right, small caps captions under each
(*BEACHFRONT WINETANK SUITES*).

- **Type:** Helvetica Neue Light throughout; headings 21–24px, body 16px/23, ≈ 70 characters per
  line. Almost no size contrast — the photographs are the headline.
- **Colour:** white ground, `#1d1c1a` text, 8% saturated. Photo grade is dusty, olive and
  concrete.
- **Image:** asymmetric clusters, varied sizes, generous gutters; up to 66% of the page is bare
  ground (one section did not render in the capture).
- **Steal:** the offset image cluster with captions; the outline button on the hero.
- **Don't copy:** text that small and light as the only type.

## 5. The Newt in Somerset — https://thenewtinsomerset.com

**Seen:** inset hero (60px margins) with an italic serif headline, *"Dreaming in Colour"*. Then
alternating 50/50 rows: photograph edge-to-edge on one side, text centred in the other half,
flipping side each row. Links are uppercase, tracked, underlined text.

- **Type:** Adobe Caslon 60px regular italic for the hero, 32px for section titles; Avenir Next
  16px/24 body. Nav 16px uppercase, tracking 3.2px (0.2em), dark olive.
- **Colour:** white ground, black text, olive for nav; 18% saturated because the food and autumn
  photography is rich.
- **Image:** the alternating split is exactly our `SplitFeature` pattern, done well.
- **Steal:** the split rhythm; the italic display headline; tracked-caps text links instead of
  buttons.
- **Don't copy:** the frosted "We're open" pill with a weather widget.

## 6. Kinsterna — https://www.kinsternahotel.gr

**Seen:** a Greek hotel in Monemvasia. An aerial golden-hour video of stone buildings, cypresses and
bougainvillea. The logo is Greek handwriting. A long serif intro paragraph (23.5px) sets the tone
before any photograph grid.

- **Type:** corporate-a serif for display and the intro lede; Open Sans for UI.
- **Colour:** grey ground `#e5e5e5` — which cools the warm stone photography; a crimson accent on
  the intro screen.
- **Image:** stone, water, olive, golden hour. This is the Greek register we want.
- **Steal:** the photographic mood; the lede paragraph set in the display face.
- **Don't copy:** the "2026" splash that delays the page, lace ornaments in the margins, the
  *Why Book Direct* checklist, and the testimonial carousel.

## 7. Kinfolk — https://www.kinfolk.com

**Seen:** a centred headline, one object (the issue cover) floating in white space, and two text
links, *Buy | Read*. Then a horizontal strip of story cards, each an image with a two-line caption.

- **Type:** Kinfolk Serif Deck 50–60px uppercase, tracking −0.5px; Kinfolk Serif Text 15px for
  body; a sans for labels.
- **Colour:** white ground, black text; 27% saturated because the magazine's own imagery is
  colourful.
- **Image:** single objects in space rather than full-bleed; a big full-bleed image appears only
  once, near the end.
- **Steal:** headline → one object → two quiet links. Restraint in how many things compete.
- **Don't copy:** uppercase serif headlines — they read well as covers and badly as sentences.

## 8. Cereal — https://readcereal.com

**Seen:** an archive of photographs in a six-column grid on a warm off-white. Every caption is an
issue number in brackets and a title: *(032-15) Modern Living*. Image heights vary; the grid's
top edges step.

- **Type:** Adobe Text Pro 12px for nearly everything (Neue Haas Unica for a few links). Hierarchy comes from position and space, not
  size. The wordmark is widely letterspaced caps.
- **Colour:** ground `#f7f6ef`, ink `#363531`, 7% saturated. The ground is within a few units of
  our `--ge-ivory-100 #faf6ed`.
- **Image:** one consistent grade across ~60 photographs from different shoots — muted, warm,
  natural light. That consistency is most of why it looks expensive.
- **Steal:** a numbered caption system (for us: day counts, island names); the colour grade
  discipline; 70% bare ground.
- **Don't copy:** 12px body text — our readers are planning a trip, not browsing an archive.

## 9. Openhouse — https://openhouse-magazine.com

**Seen:** full-bleed dark photograph, a small category label, and a two-line headline in which the
first line is roman and the second italic: *"Blasco / The heritage in every piece"* in the
capture (the hero rotates between stories; an earlier load showed *"Ca's Xorc / A Place to Return
To"* in the same form). One underlined
"Read more".

- **Type:** EB Garamond 75px roman + italic; Sneak (a grotesque) for nav. Intro text 35px serif.
- **Colour:** photograph does the work; white text; ground white below.
- **Steal:** roman + italic in one headline — a place name, then what it feels like. Fraunces has
  true italics, once its italic files are loaded (02-DESIGN-SYSTEM §4.1).
- **Don't copy:** the cookie and advertising chrome; the heavy darkening of every hero image.

## 10. Monocle — Travel — https://monocle.com/travel/

**Seen:** a newspaper structure: hairline rules above and below the section nav, a black bar
naming the section, then headline + dek (the one-line summary under a headline) + photograph pairs.

- **Type:** Plantin 32px headlines, Plantin 18px/26 body at ≈ 76 characters; Helvetica Neue 13px
  bold uppercase for nav.
- **Colour:** white ground, black ink; the one yellow is the subscribe button.
- **Image:** documentary photographs, often black-and-white, always paired with a headline.
- **Steal:** rules as structure (a hairline instead of a box); headline + dek as the unit of a
  package card.
- **Don't copy:** the advertising slot and the density — Monocle is a newspaper.

---

## Counter-examples — what the brief rules out

### ✕ Perivolas, Santorini — https://www.perivolas.gr

A beautiful property on a generic template. Montserrat for everything; body 15px light with +1px
tracking **justified across 155 characters per line** in white on `#1c1c1c`; a 12-link nav plus a
phone-number bar; magenta cushions and turquoise pools at full saturation (19%). It is what a Greek
hotel site looks like by default, and the thing we are designing away from.

### ✕ Casa Cook — https://www.casacook.com

A strong brand whose home page is taken over by a booking bar pinned under the hero:
*Where · Select your dates · Who · Do you have a code? · BOOK NOW*. That is booking-engine chrome —
we have no availability to search (D-001, D-032c) and must not pretend to.

### ✕ Xenodocheio Milos, Athens — https://www.xenodocheiomilos.com

Two ideas worth one look — a 270px ghost word behind an image, and a warm cream section ground —
buried under gold (≈ `#cba977`) and navy (≈ `#042444`, a measured colour bucket, not an exact
hex) boxed buttons, a date-picker availability bar, a
bordered centred box around a slogan, and a row of icon tiles. Two brand colours used as fields
rather than punctuation is the specific failure.

### Dropped during the research

Hoshino Resorts (price and "Best Rate Guaranteed" in the header), Design Hotels (bot wall), Kalesma,
Parilio and Mèlisses (the domains tried did not serve the hotels), The Wild (the domain tried does not
resolve).
