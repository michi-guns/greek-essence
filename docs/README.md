# Greek Essence Documentation

This directory is the entry point for current Greek Essence discovery,
requirements grilling, working state, repository guidance, and archived
documentation.

## Rebaseline Notice

Greek Essence is being redefined from an archived private prototype into a
public, production-facing preview release expected to receive real visitors and
real enquiries. Product scope, business workflows, feature boundaries, content
ownership, transactional data, and platform responsibilities are currently
being grilled and are not yet complete implementation authority.

The former documentation tree has moved to
[`archive/showcase-prototype-v0/`](archive/showcase-prototype-v0/). That entire
tree—including its project protocol, PRD, prototype specification, technical
design, design system, agent-tooling baseline, and prototype reference—is
historical reference only. Its internal approval and authority statements apply
only to the archived prototype and have no current authority.

## Documentation map

| Area | Role | Start here |
| --- | --- | --- |
| Active product grilling | Stateful project and feature decisions before implementation planning | [`grilling/README.md`](grilling/README.md) |
| Active work routing | Current multi-session work and immediate continuation | [`../NEXT.md`](../NEXT.md) |
| Working evidence | Temporary rebaseline operations, requirements intake, draft sources, and decision registers | [`working/work-items/prototype-rebaseline/NEXT.md`](working/work-items/prototype-rebaseline/NEXT.md) |
| Contributor onboarding | Current workstation setup and local verification | [`CONTRIBUTOR_ONBOARDING.md`](CONTRIBUTOR_ONBOARDING.md) |
| Git workflow | Current branch, pull-request, checks, merge, and cleanup strategy | [`GIT_WORKFLOW.md`](GIT_WORKFLOW.md) |
| Archived prototype documentation | Non-authoritative former protocol, product, UX, technical, design, tooling, and reference material | [`archive/showcase-prototype-v0/README.md`](archive/showcase-prototype-v0/README.md) |

## Authority and conflict resolution

During the rebaseline, use this order:

1. Current operator instructions.
2. Root [`AGENTS.md`](../AGENTS.md) and the selected active work-item `NEXT.md`
   for workflow and continuation.
3. Accepted `DECISIONS.md` files under `grilling/`.
4. New canonical product, domain, UX, technical, and design documents after
   accepted decisions are promoted.
5. Explicit task contracts for bounded implementation.

An active `GRILLING.md` preserves in-progress decisions and the next question;
it does not authorize implementation. `working/` contains temporary state and
evidence. `archive/` is never current authority. Existing code behavior is also
not a substitute for accepted replacement-product requirements.

## Recommended reading paths

### Resume current discovery

1. Read root [`NEXT.md`](../NEXT.md).
2. Read its linked work-item `NEXT.md`.
3. Read the accepted project [`grilling/DECISIONS.md`](grilling/DECISIONS.md).
4. Read [`grilling/protocol.md`](grilling/protocol.md).
5. Continue the applicable feature `GRILLING.md` from its stored next question.

### Historical research

Use [`archive/showcase-prototype-v0/`](archive/showcase-prototype-v0/) only when
a current task benefits from prototype lessons, language, visual reference, or
decision history. Label all extracted material as historical until it is
revalidated through grilling.

### Implementation work

Implementation of replacement-product features must wait for accepted grilling
decisions, new canonical documentation where required, and an explicit bounded
task contract. Before committing or publishing any authorized change, follow
[`GIT_WORKFLOW.md`](GIT_WORKFLOW.md).

## Current status

| Document area | Status |
| --- | --- |
| Project-level grilling | Accepted and distilled into DECISIONS.md |
| Feature grilling | Public Brand Pages accepted; Catalogue Discovery D-001 ready |
| New canonical PRD | Not yet created |
| New domain and roadmap documents | Working drafts only |
| New UX specification | Not yet created |
| New technical design | Not yet created |
| New design system | Not yet created |
| Former documentation baseline | Archived and non-authoritative |
| Current application | Preserved prototype implementation; not the replacement-product contract |

## Development package manager

Use standalone pnpm `11.17.0` directly:

```bash
pnpm install --frozen-lockfile
pnpm dev
```

On Windows, install the repository-pinned version with the official PowerShell installer, then open a refreshed terminal:

```powershell
$env:PNPM_VERSION = "11.17.0"
irm https://get.pnpm.io/install.ps1 | iex
```

## Contributor rules

- Preserve one source of truth for each concern.
- Assume requirements may be incomplete or use informal terminology; follow the
  product-and-requirements collaboration rules in root `AGENTS.md`.
- Do not introduce implementation details into the PRD.
- Do not change product or UX requirements through implementation choices.
- Do not invent unresolved business, operational, legal, trust, pricing, or content facts.
- Treat provisional content and assets as provisional in code, reviews, and demonstrations.
- Record approved changes in the document that owns the decision and update affected traceability references.
- Do not revive archived decisions merely because they are detailed or already
  implemented.
