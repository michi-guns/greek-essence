---
status: active
owner: engineering
related-adrs:
  - ADR-0001
---

# Dependency Rules

Allowed direction:

```text
Presentation → Application → Domain
Infrastructure → Application and Domain contracts
```

## Domain restrictions

The domain must not import:

- Next.js
- React
- Drizzle
- Sanity clients or GROQ helpers
- HTTP request or response types
- Browser APIs

## Application restrictions

Application use cases must not:

- Execute SQL directly
- Execute GROQ directly
- Render JSX
- Depend on Drizzle row types
- Return raw Sanity documents

## Presentation restrictions

Presentation code must not:

- Contain core business rules
- Import database tables directly
- Treat hidden UI controls as authorization

## Infrastructure restrictions

Infrastructure implementations may depend on external libraries, but their
types must not leak into domain APIs.

Where practical, enforce these rules through linting, architecture tests, and
module boundaries.
