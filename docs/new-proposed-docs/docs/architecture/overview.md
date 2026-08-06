---
status: active
owner: engineering
related-adrs:
  - ADR-0001
---

# Architecture Overview

The application is a **domain-centered modular monolith with vertical slices**.

It is one deployable system organized by business capability.

```text
src/
├── app/
├── modules/
│   ├── catalog/
│   ├── customers/
│   ├── travelers/
│   ├── quotes/
│   ├── bookings/
│   ├── payments/
│   ├── suppliers/
│   └── documents/
├── shared/
├── sanity/
└── db/
```

Each module may contain:

```text
domain/
application/
infrastructure/
presentation/
```

The architecture borrows useful dependency rules from Clean Architecture,
Onion Architecture, Hexagonal Architecture, and Domain-Driven Design without
requiring every pattern from those approaches.

## Design goal

Keep business behavior understandable and testable even when frameworks,
databases, CMSs, or external providers change.
