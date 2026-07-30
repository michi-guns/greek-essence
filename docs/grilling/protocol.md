# Grilling Protocol

## Purpose

Use this protocol to run stateful project and feature design interviews before
implementation planning. A new agent must be able to resume from repository
state without relying on chat history.

This repository adapts the practical mechanics of `jz-feature-grilling` to the
project-owned `docs/grilling/` workspace. It does not use `.scratch/features/`,
`features-cli`, `GRILL_SESSION.md`, or engineering-depth tiers.

## Authority and Routing

- Current operator instructions override stored grilling state.
- Root [`NEXT.md`](../../NEXT.md) identifies the active multi-session work item.
- This file owns the grilling process.
- Root `GRILLING.md` or `DECISIONS.md` owns project-level product decisions.
- A feature's `GRILLING.md` or `DECISIONS.md` owns that feature's decisions.
- Authoritative PRD and technical documents are updated only after accepted
  grilling decisions are promoted through the active work item.
- A grill does not authorize implementation, dependency installation, schema
  migration, deployment, or destructive path changes.

## Workspace Shape

While project-level grilling is active:

```text
docs/grilling/
  README.md
  protocol.md
  GRILLING.md
  GLOSSARY.md              # only when project terms need clarification
```

For each confirmed feature:

```text
docs/grilling/<feature-slug>/
  GRILLING.md              # active design ledger
  GLOSSARY.md              # optional, feature terms only
  contracts/               # optional, normative contracts
  examples/                # optional, illustrative examples
```

After a grill is accepted, `DECISIONS.md` replaces `GRILLING.md` at the same
level. Do not keep both as competing sources of truth. Because replacement
removes a file, the acceptance review must name the exact `GRILLING.md` path.
The operator may approve acceptance, that path's later removal, and automated
GitHub delivery in one combined answer. If they do not choose that combined
option, obtain separate path-level approval before deletion. Git history must
preserve the final accepted raw ledger.

Use kebab-case feature directory names based on accepted business capabilities.
Do not create feature directories from speculative architecture or technical
categories.

## Read Order

For a project-level session:

1. Root `NEXT.md` and its linked active work-item `NEXT.md`.
2. `docs/grilling/protocol.md`.
3. `docs/grilling/GLOSSARY.md` when present.
4. `docs/grilling/GRILLING.md`, continuing from `## Next Question`.

For a feature session:

1. The project-level `DECISIONS.md`, or active root `GRILLING.md` if the
   high-level grill is not complete.
2. `docs/grilling/protocol.md`.
3. The feature's `GLOSSARY.md` when present.
4. The feature's `GRILLING.md`, continuing from `## Next Question`.

Inspect relevant repository code and documentation before asking anything that
can be answered locally.

## Product-Management and Travel-Agency Coaching

The operator has explicitly stated that both the operator and client are still
developing their requirements-writing and product-management practice. Treat
that as a reason to provide respectful support, not as permission to dismiss,
replace, or invent their business decisions.

In addition to software-engineering analysis, approach each grill as a senior
product manager with practical knowledge of tourism and travel-agency
operations. When a request appears incomplete, internally inconsistent,
solution-led, operationally risky, or likely to create a hidden future problem:

1. pause that decision instead of silently filling the gap;
2. state the concern in plain, nonjudgmental language;
3. give a short traveler or agency example;
4. explain the likely product or operational consequence;
5. recommend the smallest workable clarification or alternative; and
6. ask one focused decision question, then persist the answer normally.

Pay particular attention to the difference between inspiration, enquiry,
offer, reservation, and confirmed booking; pricing and availability claims;
deposits, cancellation, refunds, taxes, and fees; traveler data and consent;
supplier and manual handoffs; time zones; workflow states and ownership;
notifications and recovery; localization; media rights; and trust or legal
claims.

Do not assume generic industry practice describes this agency's actual
operation. Label inferences, let the operator make the product decision, and
flag areas that require validation by the client or an appropriate legal, tax,
privacy, security, or travel-industry professional.

## Question Protocol

- Ask exactly one decision question at a time.
- Use the next decision ID stored in the applicable `GRILLING.md`.
- Offer two to four reasonable numbered options.
- Prefix the recommended option exactly with `(recommended):`.
- Explain why the decision matters when the tradeoff is not obvious.
- Keep the recommendation pragmatic for a small team and the agreed release.
- Avoid rare edge cases unless they protect data correctness, privacy,
  security, payments, fiscal integrity, or unrecoverable operations.
- The operator may answer with an option, combine options, reject all options,
  or provide a new direction.

Decision IDs begin at `D-001` independently in the root grill and in each
feature grill. Setup facts, protocol rules, imported evidence, and already-made
operator instructions do not consume decision IDs. They belong under context,
preferences, or constraints.

## Persistence Loop

After every operator answer and before asking another question:

1. Add or update the accepted item under `## Locked Decisions` using the stored
   decision ID.
2. Record why it was chosen, its scope, and material consequences.
3. Record rejected or deferred alternatives when that history prevents future
   ambiguity.
4. Remove the answered item from `## Open Questions`.
5. Update `GLOSSARY.md` when a domain term is introduced, renamed,
   disambiguated, or rejected.
6. Create a decision-linked contract only when the answer defines a normative
   data, API, validation, storage, wording, or module-boundary contract.
7. Create a decision-linked example only when an illustration materially
   reduces ambiguity; label examples non-normative.
8. Store the next highest-value question under `## Next Question`.
9. Update the active work-item `NEXT.md` when the durable continuation changes.

Do not batch several unanswered questions into one user message. Do not advance
the stored next question until the current answer is persisted.

## Root-to-Feature Transition

The root grill should establish enough shared context to identify:

- the release's primary product promise;
- included and deferred user journeys;
- agency operational needs;
- accepted feature boundaries and dependencies;
- candidate platform mandates versus technical choices;
- client-validation needs; and
- cross-feature quality, privacy, security, and launch constraints.

Only then create feature directories. Record the agreed feature list and
recommended grilling order before beginning feature sessions.

Grill one feature at a time unless the operator explicitly chooses otherwise.
When a question belongs to another feature, record the dependency and defer the
detail to that feature's session.

## Completion and Distillation

A grill is ready for acceptance when:

- no unresolved question can materially change user value, scope, data,
  workflow, ownership, security/privacy, external contracts, or implementation
  boundaries;
- accepted decisions are internally consistent;
- rejected and deferred scope is explicit;
- necessary glossary terms and contracts are present; and
- remaining unknowns have named owners or validation actions.

At acceptance, present one numbered approval question that names the exact raw
ledger path and offers at least these materially distinct outcomes:

1. **Accept and finalize automatically** — accept the decisions; authorize the
   named `GRILLING.md` path's removal after verified distillation; and authorize
   commits, pushes, pull requests, required-check monitoring, squash merge, and
   merged-branch deletion without another routine approval request.
2. **Accept but retain the raw ledger** — record acceptance, but do not delete
   the ledger or automate final distillation delivery.
3. **Correct a material decision first** — keep the grill active and name the
   correction.

After combined acceptance-and-finalization authorization:

1. Persist the operator's acceptance and exact-path authorization in the raw
   ledger.
2. If squash merge and branch deletion would otherwise discard that final
   accepted raw state, first merge it to `main` in its own pull request. The one
   authorization covers this preservation PR and the later distillation PR.
3. Write a self-contained `DECISIONS.md` containing only durable context,
   accepted decisions, explicit exclusions, dependencies, risks, and unresolved
   external validations.
4. Verify it structurally and semantically against the accepted raw ledger,
   every normative contract, higher-level authority, and adjacent accepted
   feature decisions. Do not delete the raw ledger while a material review
   finding remains unresolved.
5. Remove the approved `GRILLING.md` path, leaving `DECISIONS.md` as the sole
   accepted design authority at that level. Update `README.md` and the active
   work-item continuation.
6. Commit and push the finalization branch, open its pull request, and use
   `gh pr merge --auto --squash --delete-branch` when repository support permits.
   If auto-merge is unavailable, wait for required checks and run
   `gh pr merge --squash --delete-branch` without requesting another routine
   approval. Confirm the merged result on updated local `main`.

Combined authorization does not override failed checks, merge protection,
unrelated concurrent edits, or a new material product conflict. If semantic
review changes accepted product truth, stop, preserve the raw ledger, and ask
one corrected decision; the earlier finalization authorization no longer covers
the changed grill. It also never authorizes implementation, dependency
installation, migration, or deployment.

Implementation specifications and tasks are a later workflow. Do not turn
`DECISIONS.md` into code-level implementation instructions unless a decision
requires a normative contract.
