# report-kit

Component library and build step for **internal project documents** — reports that pass
between the developer and the agency owner. Deliberately isolated from the Greek Essence
website: different audience, different job, its own palette. Nothing here imports from `app/`,
and nothing in `app/` should import from here.

| File | What it owns |
|---|---|
| [HANDOFF.md](HANDOFF.md) | The build brief: decisions, target structure, component inventory, acceptance test. Start here if you are implementing. |
| [CONVENTIONS.md](CONVENTIONS.md) | Rules that must not be broken when editing anything that renders. Read before touching CSS or markup. |
| `dist/` | Built output. One self-contained HTML file per document. |
| `assets/` | Source logos and brand marks, inlined at build time. |

## Documents

| Document | Status | Output |
|---|---|---|
| Greek Essence client brief (M7) | Published, signed off | `dist/greek-essence-brief.html` |

**Published at** `https://claude.ai/artifact/AxtuR89rsCcEUpx58uyfh5` — version 12, private to
the owner until shared. `dist/greek-essence-brief.html` is that exact version. To publish an
update, republish the same file to that URL rather than creating a new artifact, or the link
already given to the client goes stale.

## Status

**Built, not yet decomposed.** `dist/greek-essence-brief.html` is the finished, published
document as a single hand-written file. The Preact component extraction described in
`HANDOFF.md` has not been done yet. Until it is, edit the dist file directly and re-publish —
and re-read `CONVENTIONS.md` first.
