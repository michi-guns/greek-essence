---
id: doc-002
title: 'Motion research: hover, reveal, scroll'
type: other
created_date: '2026-09-23 10:40'
updated_date: '2026-09-23 10:48'
---
# Motion research — hover, reveal, scroll

Evidence for DS-006 (docs/v1/02-DESIGN-SYSTEM.md §6). GE-003.02, 2026-09-23.

## Method

The ten GE-003.01 references (doc-001), the three counter-examples, and The Hoxton as an extra,
opened in real Chrome at 1440×900 after cookie banners were dismissed (Le Sirenuse headed, past
its bot wall). Aesop was tried and dropped: a region pop-up covers the page. Method adapted from
SkillUI's "ultra" extractors, with three changes: real Chrome instead of headless Chromium, the
timings read from the browser's own animation records instead of stylesheets (so JavaScript-driven
motion counts too), and every hidden element sampled frame by frame as it enters the viewport.

For each site:

- **Hover.** Up to five elements — a nav link, the main call to action, a link in body text, an
  image card, a button. Styles on the element, its `::before` / `::after` and its image are
  compared before and one second after the pointer arrives; running transitions are read 30ms
  after it arrives, which gives duration and easing.
- **Scroll reveal.** Every element below the first screen that starts hidden (opacity near 0,
  `visibility: hidden`, shifted or scaled) is watched as the page is scrolled with the mouse
  wheel. Recorded: delay after it enters, how long it moves, the largest vertical travel.
- **Header.** Position and styles at the top, after one screen of scrolling down, and after
  scrolling back up.
- **Page.** Animation and smooth-scroll libraries present, `prefers-reduced-motion` rules, and
  whether the first screen holds a video or a carousel.
- Seven screenshots at 0–100% scroll depth and a scroll recording per site (local evidence only).

Limits: desktop only. Hover does not exist on phones; reveals on phones were not measured. Elements whose
travel is expressed as a percentage are reported in pixels at 1440px. Load-time animation of the
first screen was not measured.

## Results

| Site | Scroll reveal | Hover (text) | Hover (image) | Header on scroll | Smooth-scroll library |
|---|---|---|---|---|---|
| Le Sirenuse | 3 · fade + 50px · 1.9s | fade · 250ms | fade · 250ms | sticky, changes height | Locomotive |
| Aman | none | fill · 400ms | none | hides | — |
| Masseria Moroseta | none | colour + fade · 300ms | overlay fade · 200ms | scrolls away | — |
| Dexamenes | 21 · fade + its own height · 1.25s, 210ms stagger | colour | — | sticky | — |
| The Newt | none | 150ms | underline | sticky | — |
| Kinsterna | 31 · fade + 100px · 1.5s, 270ms stagger | colour + fill · 150ms | zoom ×1.20 · 2s | sticky | — |
| Kinfolk | 13 · fade, rise 0–58px · 1.1s, 60ms stagger | fade · 500ms | dim + overlay · 1.2s | sticky | Lenis |
| Cereal | none | none | — | sticky | — |
| Openhouse | 8 · fade + 60px · 0.8s | underline · 300ms | dim · 700ms | sticky | — |
| Monocle | none | underline | — | sticky | — |
| ✕ Perivolas | 3 · fade · 2s | colour · 200ms | colour | sticky, changes height | — |
| ✕ Casa Cook | 9 · fade + 50px · 0.5s | 300–400ms | — | sticky | Lenis |
| ✕ Xenodocheio Milos | none | 200ms | underline + dim · 300ms | scrolls away | — |
| The Hoxton | none | 600ms | zoom ×1.07 · 600ms | sticky | — |

"—" means no element of that kind was found or it did not change.

## What the numbers say

1. **The calmest references move least.** Aman, Cereal, Monocle, Moroseta and The Newt use no
   scroll reveal. Five of the ten references do.
2. **Where they reveal, it is always a fade,** over 0.8–1.9s. Le Sirenuse, Openhouse and Kinsterna rise 50–100px; Kinfolk barely moves (0–58px).
   Openhouse is the quickest (0.8s, 60px). Dexamenes moves each block by its own height — median
   about 450px, up to about 900px — the far end, not a model.
3. **Text hovers change colour, opacity or underline, never position.** 100–500ms, median about
   300ms. Plain `ease` is the most common curve.
4. **Image hovers are slow, or absent.** The Hoxton scales 1.07 in 600ms; Kinsterna's
   1.20 over 2s is the most dramatic measured.
5. **Headers stay put.** Nine of 14 are sticky and unchanged; two change height, one hides, two scroll
   away.
6. **Smooth-scroll libraries** appear on three sites (Le Sirenuse, Kinfolk, Casa Cook). They change
   how the mouse wheel feels on every page.
7. **Focus is neglected.** Five of 14 sites draw no outline or ring on any element tested
   (Moroseta, Dexamenes, Openhouse, Casa Cook, The Hoxton).
8. **Carousels and hero video are common** (carousel library on 11 sites, video in the first screen on
   six) — and already ruled out by the brief (§4.3, §4.7).
