# Documentation Protocol

## Purpose

This file defines how humans and AI agents read, interpret, create, update,
and validate project documentation.

The documentation is a living knowledge system, not a collection of snapshots.

## Reading order

For any meaningful change, read in this order:

1. `docs/index.md`
2. Relevant current-state document
3. Relevant domain specification
4. Related ADRs
5. Active assumptions and open questions
6. Relevant development guide or runbook

Do not read the entire tree unless the task genuinely spans the whole system.

## Document authority

### Current-state documents

Folders: `architecture/`, `data/`, and most of `domain/`

They describe how the system is intended to work now.

### Domain specifications

They define intended business vocabulary, rules, states, and behavior.

### ADRs

Folder: `adr/`

They preserve why significant architectural decisions were made. ADRs are
historical records and do not automatically override newer current-state docs.

### Assumptions

Folder: `domain/assumptions/`

They record beliefs that are not fully verified. They are never authoritative
requirements until promoted into the relevant current-state or domain document.

### Runbooks

Folder: `runbooks/`

They provide operational procedures for known incidents or repeated tasks.

### Agent and development guides

Folder: `development/`

They define how changes should be implemented and validated.

## Update rules

### When business behavior changes

- Update the relevant domain specification.
- Update or add tests.
- Update affected current-state documents.
- Update related assumptions and open questions.

### When architecture changes

- Create a new ADR, or supersede an existing ADR.
- Update the current-state architecture document.
- Update indexes and cross-links.

### When an assumption is verified

- Change its status and add evidence.
- Move the verified rule into the authoritative domain or architecture document.
- Keep the assumption file as a record, or mark it obsolete.
- Do not leave the verified rule only in the assumption file.

### When an operational problem repeats

- Create or update a runbook.
- Link it from `runbooks/index.md`.

## ADR rules

- Accepted ADRs are not silently rewritten.
- Corrections may fix spelling or clarify wording without changing the decision.
- Changed decisions require a new ADR.
- Mark the previous ADR `Superseded by ADR-XXXX`.
- ADR filenames remain chronological and stable.

## Editing rules

- One document should own one decision, concept, or procedure.
- Prefer links over duplicated explanations.
- Update the owning document instead of creating overlapping guidance.
- Preserve uncertainty explicitly.
- Remove or mark obsolete guidance when replacing it.
- Update indexes when files are added, moved, renamed, or superseded.
- Keep documents concise enough to retrieve and review selectively.
- Do not encode an unverified assumption as confirmed business truth.

## Metadata

Use small frontmatter blocks only when useful:

```yaml
---
status: active
owner: engineering
related-adrs:
  - ADR-0001
---
```

Do not add review dates or owners that nobody will maintain.

## Completion checklist

Before considering a change complete:

- Did I read the authoritative documents?
- Did I identify relevant assumptions?
- Did behavior or architecture change?
- Is a new or superseding ADR required?
- Are current-state docs still accurate?
- Are indexes and links still valid?
- Are written rules enforced by tests or tooling where practical?
- Did I report remaining uncertainty honestly?

## Repository agent entry point

The repository-level `AGENTS.md` should include a short instruction such as:

```md
Before modifying architecture, domain behavior, persistence, or integrations,
read `docs/documentation-protocol.md` and follow its update rules.
```
