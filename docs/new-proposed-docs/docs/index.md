# Project Documentation

> [!CAUTION]
> This index belongs to a non-authoritative documentation-architecture proposal.
> Follow the repository-root `docs/README.md` for current documentation and
> authority.

This directory is the knowledge system for the travel agency application.

## Start here

- [System in five minutes](./handbook/system-in-five-minutes.md)
- [Documentation protocol](./documentation-protocol.md)
- [Architecture overview](./architecture/overview.md)
- [Data ownership](./data/ownership.md)
- [Current assumptions](./domain/assumptions/index.md)

## Build or change a feature

1. Read the relevant current-state documents.
2. Read the related domain specification.
3. Read linked ADRs.
4. Check active assumptions and open questions.
5. Follow the [implementation workflow](./development/implementation-workflow.md).
6. Apply the [quality gates](./development/quality-gates.md).

## Document map

- `handbook/`: fast human orientation
- `architecture/`: how the system currently works
- `domain/`: business concepts, rules, lifecycles, and uncertainty
- `data/`: ownership and consistency rules
- `development/`: implementation and agent guidance
- `adr/`: historical architectural decisions
- `runbooks/`: operational recovery procedures

## Authority

When documents disagree, follow the authority rules in
[documentation-protocol.md](./documentation-protocol.md). Do not guess.
