---
status: active
owner: engineering
---

# Module Structure

Business capabilities own their code.

Example:

```text
modules/bookings/
├── domain/
├── application/
├── infrastructure/
└── presentation/
```

## Domain

Entities, value objects, invariants, domain errors, and repository contracts.

## Application

Use cases, commands, queries, application ports, and result DTOs.

## Infrastructure

Drizzle repositories, Sanity adapters, external providers, mappers, and
technical configuration owned by the module.

## Presentation

Server Actions, route handlers, components, input schemas, and view models.

## Rule

Do not create empty architectural folders in advance. Add a folder when it
contains real code.

Keep `shared/` small. Business concepts should remain in their owning module.
