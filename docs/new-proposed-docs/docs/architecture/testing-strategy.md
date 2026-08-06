---
status: active
owner: engineering
---

# Testing Strategy

## Domain tests

Test invariants, calculations, and state transitions with fast unit tests.

## Application tests

Test orchestration with fake or in-memory ports.

## Infrastructure tests

Test Drizzle mappings, database constraints, Sanity parsing, and external
adapter behavior.

## End-to-end tests

Cover a small number of critical workflows:

```text
Customer
→ Quote
→ Offering snapshot
→ Acceptance
→ Booking
→ Payment
→ Confirmation
```

## Principle

Written rules should be executable where practical.

Examples:

- Dependency rules → lint or architecture tests
- Domain behavior → unit tests
- Stored integrity → database constraints
- Documentation structure → link and naming checks
