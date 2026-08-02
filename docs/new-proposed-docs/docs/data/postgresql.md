---
status: active
owner: engineering
related-adrs:
  - ADR-0003
---

# PostgreSQL

PostgreSQL is the transactional source of truth.

Drizzle defines and queries the relational persistence model.

## Responsibilities

- Relational integrity
- Transactions
- Historical records
- Concurrency-sensitive state
- Reporting-ready business data
- Audit information

## Persistence rules

- Use migrations committed to source control.
- Use foreign keys, unique constraints, checks, nullability, and indexes.
- Map persistence rows explicitly to domain models.
- Do not use Drizzle row types as domain entities.
- Prefer business states over deleting commercially relevant history.
- Treat sensitive traveler data deliberately.
