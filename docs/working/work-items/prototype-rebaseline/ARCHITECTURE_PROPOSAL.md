# Expanded Product Architecture Proposal

## Decision Status

Withdrawn on 2026-07-28 after the operator reported materially expanded client
requirements involving CMS, persistent data, ORM, backend, and additional
unknown capabilities. Do not implement this proposal.

The remainder is retained only to show which assumptions were considered and
why they are no longer sufficient. The active architecture process is routed
through `REQUIREMENTS_INTAKE.md` and `DECISION_REGISTER.md`.

The archived product documents once described two substantial cross-route
capabilities:

1. travel discovery across destinations, experiences, journeys, and their
   editorial relationships; and
2. trip-request qualification, draft state, validation, submission, and
   acknowledgement.

About, FAQ, legal, and simple contact pages were routes in that baseline, but
the withdrawn proposal cannot establish their current scope or ownership.

## Authority Conflict to Resolve

The archived technical design prescribed a shallow `components/`, `lib/`, and
root `emails/` structure. The provisional Layer 2 working documents instead
proposed `features/` and `shared/`, initially under the prototype-specific name
`showcase`. Neither is current architecture authority.

Do not implement either interpretation. This proposal is withdrawn; any future
capability structure must follow accepted grilling decisions and new canonical
technical documentation before runtime paths move.

## Recommended Boundaries

```text
app/
  [locale]/
    _components/             # branded site shell for the locale route tree
    destinations/            # thin route composition
    experiences/             # thin route composition
    journeys/                # thin route composition
    about/ faq/ contact/      # route-local until reuse is demonstrated
    plan-my-trip/             # route composition for the trip-request feature
    privacy/ cookies/ terms/
  api/trip-request/route.ts   # sole dynamic server boundary

features/
  discovery/
    components/              # cross-route destination/experience/journey UI
    destinations/            # destination-specific types and rules
    experiences/             # experience-specific types and rules
    journeys/                # journey-specific types and rules
    server/                   # build/server-only content access
  trip-request/
    components/              # interactive form and confirmation UI
    client/                   # draft persistence and browser-only state
    schema/                   # shared client/server request contract
    server/                   # delivery and email composition

shared/
  ui/                         # proven domain-neutral UI primitives
  lib/                        # proven domain-neutral utilities only

content/{en,el,shared}/       # local product facts and relationships
i18n/                         # locale routing/request/navigation boundary
messages/{en.json,el.json}    # small interface translations only
public/                       # approved delivery-ready media
```

## Boundary Rules

- `app/` owns routing, metadata, locale parameters, page composition, and the
  same-origin route handler. It does not own large cross-route implementations.
- `features/discovery/` is a business capability, not a replacement name for
  the prototype. It owns only behavior reused across destination, experience,
  and journey surfaces.
- `features/trip-request/` owns qualification and submission end to end while
  keeping browser-safe and server-only imports separate.
- Branded header, footer, navigation, and language controls remain colocated
  under the locale route tree. They are neither domain-neutral `shared` code nor
  an invented business feature.
- About, FAQ, legal, and simple contact pages stay route-local until real reuse
  demonstrates a broader owner.
- `shared/` cannot import from `features/` or `app/`; features cannot import from
  `app/`; route-local private folders cannot be imported by sibling routes.
- Server Components remain the default. Client boundaries are limited to
  navigation interaction and the trip-request experience.
- Local JSON content remains a build-time boundary. The trip-request route
  handler remains the only dynamic server-side business boundary.
- No broad feature barrel is required. Use narrow import paths and explicit
  server-only entry points.

## Why These Names

- `discovery` follows the product language in FR-003, FR-004, FR-005, and FR-016
  and covers the demonstrated relationships among the three content domains.
- `trip-request` follows the primary conversion language in FR-007 through
  FR-012 and keeps personal-data handling in one explicit boundary.
- `showcase` is rejected because it describes the archived demonstration, not
  the expanded product capability.
- `marketing` is rejected because it is too broad and would blur discovery,
  trust, contact, legal, and conversion ownership.

## Explicit Non-Decisions

This proposal does not choose a CMS, database, CRM, analytics provider,
scheduler, payment system, account system, or broader production integration.
It does not settle unresolved business, legal, lead-operation, content, asset,
or commercial decisions in the PRD.

## Historical Approval Questions

These questions were never approved and must be reconsidered rather than
answered from this withdrawn proposal:

- the capability names `discovery` and `trip-request`;
- branded shell colocation under `app/[locale]/_components/`;
- neutral primitives under `shared/`; and
- creation of new canonical technical architecture before runtime migration.
