# ADR-0003: Use PostgreSQL for Transactional Truth

## Status

Accepted

## Context

Quotes, bookings, payments, availability, supplier operations, and historical
records require transactions, relational constraints, and reliable history.

## Decision

Use PostgreSQL as the source of transactional business truth and Drizzle as the
persistence library.

## Consequences

### Positive

- Strong relational and transactional guarantees.
- Explicit schema migrations and constraints.
- Suitable foundation for reporting and audit history.

### Negative

- Domain and persistence models require mapping.
- Schema evolution requires migration discipline.

## Related Documents

- [PostgreSQL](../data/postgresql.md)
- [Data ownership](../data/ownership.md)
