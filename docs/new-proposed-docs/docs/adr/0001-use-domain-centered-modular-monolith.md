# ADR-0001: Use a Domain-Centered Modular Monolith

## Status

Accepted

## Context

The application is built by a small team and heavily assisted by AI agents. It
needs clear business boundaries without the operational cost of microservices.

## Decision

Use one deployable Next.js application organized by business modules. Within
each module, separate domain, application, infrastructure, and presentation
responsibilities where useful.

## Consequences

### Positive

- Business capabilities remain cohesive.
- Deployment and operations remain simple.
- AI agents can retrieve focused context.
- Domain behavior remains independent from frameworks.

### Negative

- Module boundaries require discipline.
- In-process coupling can grow if dependency rules are ignored.

## Related Documents

- [Architecture overview](../architecture/overview.md)
- [Dependency rules](../architecture/dependency-rules.md)
