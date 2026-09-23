---
name: design-directions
description: Find and build a visual direction for a website the way a strong freelance designer-engineer would - silent intake, a short discovery round, three contrasting live demos with one recommendation, then build the chosen one section by section with a screenshot loop. Use for a new site, a redesign, a first fold or hero, a landing page, or any "make this look great" request, and whenever a visual direction has not been locked yet. If a direction is already locked, start at step 4.
---

# design-directions

## Purpose

A description of a design wins nobody. A page they can open does. This skill gets from a vague
brief to a direction the owner has chosen by looking at it, then builds that direction without
losing the quality floor.

The owner is whoever approves the direction. The goal is the moment they open the demo and say
"yes, that one."

**Direction already locked?** Skip steps 1-3 and start at step 4. Never pitch new directions
for work whose direction has been chosen.

## Precedence

1. The owner's own words. A change to an approved decision gets recorded where that decision
   lives.
2. The project's decisions, design system and stack (see _In this repo_ below). Approved rules
   there are not reopened by this skill. If the best result needs one reopened, say so and stop.
3. This skill.

## Step 1 - Silent intake

Read everything before asking anything: the brief, decisions, design-system doc, existing
tokens and fonts, brand assets, reference research, `package.json`. Never ask what you can
infer. Write down the assumptions you made.

## Step 2 - Discovery (skip what step 1 answered)

At most six questions, in one round, each with a recommended default so the owner can just
accept. Follow the owner's rules for how to ask (some owners want to be asked before a
questions tool opens). Pick the highest-impact ones:

- **Feeling:** which three words should a visitor feel in five seconds? Offer contrasting trios.
- **Single job:** the one action a visitor must take.
- **Audience:** who, and what they compare this site against.
- **References:** one to three sites they love, one they dislike. None? You will bring some.
- **Boldness:** safe and elegant / confident / experimental.
- **Real assets:** logo, photos, colours, copy - or placeholders for now.

Then play back a three-line brief ("Here is what I heard") and move on.

## Step 3 - Three live directions

- Build **three deliberately contrasting** directions as runnable demos: the first fold plus one
  key section each, **the same content** in all three. Same content is what makes them
  comparable.
- Content is drafted copy that fits the subject, never lorem. Facts - prices, dates, names,
  figures - stay labelled placeholders.
- Directions differ only in what the project has left open. Anything already decided (palette,
  fonts, motion) stays shared; then they differ in layout, image treatment and hierarchy.
- Each gets a name, a one-line idea, what makes it different, and its one signature moment.
- One local index page links all three. Screenshot each at desktop and phone width and show the
  screenshots with the links.
- **Recommend one and say why in one line.** Never hand over a menu without a pick.
- Ask one question: "Which one, or what should I take from each?" Offer mixes ("A's type with
  C's image treatment").

## Step 4 - Converge and build

- Record the chosen direction's tokens (colour, type scale, spacing, radius, motion) where the
  project already keeps them, not in a new file.
- Build the first fold first, until it is right. Then the rest, one section at a time. Never
  one-shot the whole site.
- Run the screenshot loop after every section. Show the owner milestones only.

## Screenshot loop (every section)

1. Screenshot at the project's own check widths; if it has none, 1440 and 375.
2. Compare with the plan or the reference. Name concrete differences with numbers: "headline
   48px reads weak, target 80px", not "headline could be bigger".
3. Fix. Re-screenshot. At most three loops per section, then move on.

This loop is the builder checking its own work. It does not replace the independent visual
review before the work is called done.

## Step 5 - The finishing pass

- Ask: would someone screenshot this and send it to a friend? If not, strengthen the one
  signature moment - inside the project's motion and stack rules, not around them.
- Add the details that separate designed from templated: hover states with intent, a
  considered easing curve, optical spacing, icons aligned to the text, real photography.
- **Remove one decorative thing before shipping.**

## Quality floor (non-negotiable, never the excuse for a dull page)

- Works at every check width, down to 320. No horizontal scroll, no two-line buttons, no headline
  overflowing its box.
- A `prefers-reduced-motion` fallback for every animation. Visible keyboard focus. Body text at
  4.5:1 contrast or better.
- Explicit image dimensions, lazy-loaded heavy media, a poster frame for any video or canvas.

## References

- From the owner's references, take structure, rhythm, type scale and palette. Remix, never
  copy. Combining two references usually gives something new.
- No references? Find four to six that fit the feeling and show them before step 3.

## Honesty and assets

- Never invent facts, figures, prices, testimonials, reviews or client logos. Use placeholders
  that are plainly labelled as placeholders.
- Real client assets beat generated ones. Collect them first.
- Generating images or video costs money: ask first and state the estimate.

## Signature moment - pick one, at most two supporting

Kinetic or oversized type · a clip-path or mask reveal · a pinned storytelling section · an
interactive tool (planner, map, calculator) · real textured photography · view transitions ·
a scroll-scrubbed image sequence · one 3D object · a subtle shader background · a short muted
video loop.

Each option must pass the project's motion and stack decisions before it is offered. Many
projects rule out the heavier ones - that is a decision, not an obstacle.

## Looks to avoid (the most common machine-made designs)

Unless the owner asks, or the project's approved rules already chose it:

- Purple-to-blue gradients, gradient text, mesh blobs.
- Inter, Roboto or a system font as the display face.
- Three identical icon cards in a row; cards inside cards; one radius and one shadow on
  everything.
- An uppercase eyebrow label above every heading; decorative "01 / 02 / 03" numbering.
- Hero stat strips, logo clouds, fake dashboards drawn from divs.
- Fade-up on every section; bounce easing.
- Cream + serif + terracotta; near-black + one acid accent.

## How to talk to the owner

- Screenshots and links first, explanation after.
- One line of "why" per decision.
- End every milestone with exactly one question or next step.
- If a request will hurt the result, say so briefly, offer the better option, then do what the
  owner chooses.

## In this repo (Greek Essence)

Replace this section when reusing the skill in another project.

- **Who is who:** the owner is the operator. The client is Giorgos; nothing reaches him
  except through the operator (AGENTS.md, Roles). He sees demos as Netlify preview links
  (`docs/v1/02-DESIGN-SYSTEM.md` §3).
- **Steps 1-2 are answered** by 02 §4, the art-direction brief. `backlog/docs/doc-001` (visual
  research) and `doc-002` (motion) are the evidence behind it.
- **Step 3 is fixed by 02 §4.6:** type-led, image-led and editorial grid, same content and same
  tokens. Palette (§4.2), fonts (Fraunces + Inter, S-005) and motion (DS-006) are shared; the
  directions differ in layout and image treatment.
- **Motion:** read DS-006 in 02 §6, including its "Ruled out" list, before offering any
  signature moment. DS-006 and S-006 (no motion library; view transitions only as a plain
  cross-fade) remove most of the menu above: no scroll-scrubbing, 3D, shader, video, loops,
  clip-path reveals or cursor effects.
- **Exempt from "Looks to avoid":** ivory with a serif (the approved brand, §4.2); tracked-caps
  eyebrows (§4.1, §4.5); fade-and-rise reveals below the fold (DS-006); the numbered package
  index of the editorial grid (§4.6).
- **Check widths:** 390, 768, 1024 and 1440 (DS-003, A-007 walks).
- **Content:** copy is drafted by agents (D-035); photos are free stock, each logged (D-034).
  No prices (D-006).
- **Where the work lives:** the three directions are real code in the repo, as T-01.3 and
  GE-003.03 require. The side-by-side page and screenshots go in
  `.local/design-exploration/<date>-<slug>/` (git-ignored). Hand the operator a local HTML page,
  not an artifact link.
- **Independent review:** the `visual-reviewer` agent (`docs/v1/09-REVIEW.md` §8.1).
- **Step to task map:**

  | Step | Task |
  |---|---|
  | 3, three directions | GE-003.03 |
  | Owner picks | GE-003.04 |
  | 4, tokens | GE-004.01, into `app/globals.css` |
  | 4, build | GE-005.01 to GE-005.04 |
  | Client sign-off | GE-005.05 |
