# Foundation Design Layer

## Purpose

Turn accepted product and domain truth into the durable technical foundations
of Greek Essence. This layer answers **how the system will be shaped and how its
major services will divide responsibility** before bounded implementation work
begins.

## Belongs Here

- technology stack and provider selection where still unresolved;
- what Sanity, Neon, Drizzle, Next.js, hosting, and mail services each own;
- architectural boundaries, modules, dependency direction, and runtime topology;
- content and transactional entities as represented in their owning systems;
- relationships, cardinalities, identifiers, snapshots, and cross-service links;
- localization, rendering, caching, revalidation, preview, and search architecture;
- authentication, authorization, validation, migration, and data-access boundaries;
- security, privacy, recovery, observability, and failure-handling mechanisms that
  materially shape the architecture;
- environments, deployment, rollback, and provider-limit behavior where those
  choices constrain implementation.

A question belongs here when materially different answers would change schemas,
service ownership, integration contracts, module boundaries, runtime behavior,
or another costly-to-reverse development foundation.

## Does Not Belong Here

- unresolved product meaning that should be returned upstream;
- named staff, reviewers, recipients, or account contacts;
- final copy, media approval, legal sign-off, or provider evidence;
- low-level implementation choices that a bounded task can make safely within the
  accepted architecture.

## Inputs and Outputs

Inputs are accepted Product and Domain Truth decisions plus verified provider and
repository constraints. Outputs are accepted foundation decisions and normative
contracts suitable for promotion into canonical domain and technical design
documentation.

If architecture work exposes missing or contradictory product truth, stop and
route one focused question back to the Product and Domain Truth layer. Do not
resolve it through a convenient schema or provider assumption.

Use the dependency-ordered
[`Foundation Design track map`](../foundation-design/README.md) after its
upstream Product and Domain Truth gaps are resolved.
