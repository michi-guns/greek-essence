# Public Brand Pages Decisions

## Status and Authority

Accepted by the operator on 2026-07-29 after feature grilling.

This document defines the product promise, trust standard, page roles, action
hierarchy, and language-publication boundary for the Public Preview Release's
Home and About pages. It is feature-level product and design authority for later
canonical documentation and bounded implementation planning.

It does not authorize application implementation, dependency installation,
schema migration, deployment, or active-path removal. Use the accepted project
context in [../DECISIONS.md](../DECISIONS.md). Detailed catalogue, request,
content-management, and visual-system decisions belong to their later grills.

## Home Promise

Home will first promise **useful Greece discovery with personal agency help
available**. Visitors can explore destinations and Experiences, understand that
Greek Essence can help them plan, and choose whether to keep browsing or request
a consultation.

The page must preserve the distinction between inspiration and an
agency-managed request. It must not imply live prices, live availability,
instant confirmation, a reservation, or a confirmed booking.

Consequences:

- Opening content establishes discovery value before asking for a request.
- Browsing and consultation are both visible paths; neither is incidental.
- Draft public copy requires client validation.

Catalogue-first and consultation-first positioning were rejected because each
would obscure either the human agency role or the release's discovery value.

## Trust Evidence

Home and About will use only **client-approved, verifiable evidence**. Before
richer proof is approved, trust comes from clear agency identity, usable contact
routes, an honest request-process explanation, and approved factual statements.

Credentials, experience claims, testimonials, ratings, memberships, partner or
supplier logos, awards, and local-expertise claims require evidence and client
permission for the exact public use. Third-party marks, quotations, ratings, and
relationship claims also require applicable third-party permission.

Missing proof results in omission or neutral factual wording. Draft examples
must be marked unapproved and must not reach the public release by default.
Content operations must later define approval-state and evidence-ownership
handling. Qualified legal or industry review may be needed for regulated,
contractual, or materially misleading claims.

Provisional social proof and an aspiration-only trust approach were rejected:
the former risks deception and unauthorized use, while the latter gives
travelers too little evidence that they are dealing with a real agency.

## About Role

About will explain **who the agency is, how its human help works, and why the
agency is credible**. Home owns the concise discovery promise; About provides
the deeper approved context a cautious visitor may want before sharing travel
intent or personal details.

Subject to the trust-evidence standard, About may cover agency identity,
relevant people or ownership, its approach to helping travelers, the boundary
between a request and a confirmed booking, and verified trust evidence. It ends
with relevant paths to browse or request help.

Personal or founder material may support the agency explanation when approved,
but cannot replace clear business identity and service responsibility. About
must not imply unapproved response times, supplier access, expertise, or service
outcomes. Detailed request steps remain owned by later request-feature grills.

A founder biography as the primary purpose and a longer Home-style sales page
were rejected because neither adequately answers the visitor's agency and
service trust questions.

## Shared Action Hierarchy

Home and About will consistently offer **two clear travel-planning paths**:
browse the catalogue or request planning help through the consultation journey.
Their relative prominence may adapt to the surrounding content, but both choices
must remain understandable.

General contact remains available through navigation or a contextual link for
questions outside the travel journeys. Booking requests belong only to a
specific Experience and must not appear as a generic brand-page action.

The pages use consistent visitor language for the two journeys in English and
Greek. Exact labels and detailed journey behavior belong to the relevant later
grills and client content approval. A consultation-only hierarchy and three
equally prominent actions were rejected because they would respectively weaken
discovery or blur planning help with general contact.

## Languages and Served Markets

Every published language will be a **complete, separately approved visitor
experience**. The replacement product preserves the prototype's sound basic
mechanism of storing English and Greek content separately while adding the
ownership and approval required for a real public service.

AI or a translation service may assist drafting. Before publication, the client
must name the served markets and responsible English and Greek content owners or
reviewers. A responsible human approves each language's Home and About copy,
action labels, agency facts, contact details, trust evidence, and
market-sensitive claims.

Requirements:

- Mixed-language, machine-only, or silent fallback content is not finished
  public copy.
- Translation may preserve meaning without being word-for-word, but languages
  must communicate the same service boundaries.
- A language-specific claim requires explicit market-specific approval.
- A language is not offered publicly until its complete launch content and
  ongoing owner are ready.

English-authoritative partial translation and Greek-authoritative generic
English were rejected because either could omit material information or present
an unfinished visitor experience.

## Dependencies and External Validation

- Catalogue Discovery owns catalogue content and browse-journey detail.
- Consultation Request owns the planning-help journey.
- Booking Request owns Experience-specific booking interest and its
  non-confirming wording.
- General Contact owns questions outside the two travel-request journeys.
- Content Operations owns editorial workflow, approval states, evidence
  ownership, preview, and publishing.
- The future design-system work owns visual hierarchy and component treatment.

Before public release, the client must validate the served markets, language
owners, Home and About copy, agency identity and contact details, all public
claims and evidence, third-party permissions, and the exact English and Greek
action labels. These are external validation gates, not permission to invent
missing facts.
