# Showcase Prototype v0 Lessons and Cautions

This note distills useful observations from the archived prototype. It does not
promote prototype behavior, code, content, naming, or visual treatments into
current requirements.

## Useful Patterns

- Preserve explicit English and Greek routes and equivalent-route language
  switching. Review both locales as parallel experiences rather than treating
  Greek as a final translation pass.
- Let editorial sections recompose by viewport while preserving their semantic
  order, content hierarchy, and primary action.
- Treat compact navigation as an interaction system: expose current location,
  keep focus visible, close on Escape and outside activation, and return focus
  to the trigger.
- Test narrow reflow with long Greek copy. The prototype needed explicit
  wrapping and shrink behavior to avoid horizontal overflow at its supported
  200%-zoom-equivalent width.
- Keep media records structured and fail closed when approval, provenance,
  localized alternative text, focal data, or geometry is incomplete. Stable
  placeholders are preferable to broken or unapproved imagery.
- Prefer static locale generation and Server Components for editorial pages;
  isolate client JavaScript to interactions that require it.

## Cautions

- The archived `showcase` modules and file layout are historical implementation,
  not approved boundaries for the expanded product.
- The screenshots contain neutral media placeholders. They are useful for
  studying composition and fallback geometry, not final art direction.
- The archived image masters are large PNG files and some asset records remain
  provisional. Do not reuse them without separate provenance, licensing,
  relevance, crop, and performance review.
- Home-page LCP remained technically above the prototype's strict 2.5-second
  assertion in final evidence despite passing category score budgets. Do not
  inherit the exception as a new baseline.
- Greek display typography appeared heavier than English in the reviewed
  fallback configuration. Reassess font coverage and weight parity when the
  active visual direction is settled.
- Only the bilingual Home and Paros and Antiparos editorial slice was complete.
  The trip-request flow, submission boundary, and later product surfaces were
  not implemented by this prototype.
- The archived `.scratch` material is execution evidence, not durable product or
  architecture documentation.

## Curated Screenshot Intent

| Screenshot | What it preserves |
| --- | --- |
| `screenshots/home-wide-en.png` | Wide Home hierarchy, pacing, section rhythm, and CTA balance |
| `screenshots/home-compact-el.png` | Greek expansion and compact single-column composition |
| `screenshots/paros-wide-en.png` | Wide destination editorial composition and card geometry |
| `screenshots/paros-compact-el.png` | Greek destination hierarchy and compact reflow |
| `screenshots/navigation-compact-el.png` | Localized compact menu, current state, and action hierarchy |
| `screenshots/focus-state-en.png` | Visible keyboard focus on the contextual primary action |
