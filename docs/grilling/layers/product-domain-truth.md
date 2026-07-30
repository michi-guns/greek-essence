# Product and Domain Truth Layer

## Purpose

Define the product and business meaning that development must preserve before
architecture is selected. This layer answers **what Greek Essence is building**,
not how the system will implement it or who will operate it on a particular day.

## Belongs Here

- product promise, release scope, and supported user journeys;
- distinctions such as inspiration, enquiry, Booking Request, and Booking;
- domain concepts, vocabulary, business ownership, and durable invariants;
- user-visible lifecycle meaning and business relationships;
- information the service must collect, preserve, expose, or deliberately avoid;
- privacy, money, supplier, and truthful-service constraints that change product
  behavior or the information architecture must support.

A question belongs here when materially different answers would change the
service offered, the meaning of a domain concept, or the business behavior the
software must preserve.

## Does Not Belong Here

- framework, provider, package, deployment, module, or persistence choices;
- database tables or CMS schema mechanics;
- named reviewers, incident contacts, routine cadence, or launch-day assignments;
- implementation details that can be decided responsibly from accepted product
  truth without another client-facing choice.

## Outputs and Handoff

Accepted outcomes live in `DECISIONS.md`, with a glossary, contract, or example
only when needed to preserve domain meaning. The Foundation Design layer receives
settled capabilities, concepts, relationships, lifecycles, data sensitivity,
and business invariants as architectural inputs.

Existing project and feature decision files under `docs/grilling/` retain their
current authority. Their later classification requires an explicit review; this
layer definition does not reclassify them automatically.
