# Development Standards

## Purpose and Authority

This guide owns stable implementation defaults for Greek Essence. Accepted
product and Foundation Design decisions determine what must be built; explicit
task contracts define bounded implementation scope; this guide defines how to
implement that scope responsibly.

Do not use these defaults to override an accepted decision or fill an unresolved
product, operational, or architectural gap. Follow
[`PRODUCT_COLLABORATION.md`](PRODUCT_COLLABORATION.md) when clarification is
required.

## Repository and Architecture Defaults

- Use the package manager and version declared by the repository's
  `packageManager` field. Do not substitute another package manager.
- Keep TypeScript strict.
- Preserve the current application and its checks while it remains in the
  active tree unless an explicitly approved replacement task changes them.
- Prefer simple, maintainable, battle-tested solutions.
- Keep Server Components as the default for Next.js work. Add Client Components
  only for necessary interaction unless a later accepted technical design
  establishes a different boundary.

The replacement product architecture is being rebaselined through
[`grilling/`](grilling/). Do not inherit the archived static-first architecture
or mechanically reorganize the current prototype as the new foundation.

Accepted Foundation Design inputs do not by themselves authorize dependency
installation, configuration, modeling, schema migration, or implementation.
That work requires promotion into an explicit bounded task contract.

For Next.js-specific work, consult the documentation bundled with the installed
Next.js version under `next/dist/docs/` and its approved generated agent rules.

## Proportional Implementation

Implement the smallest complete solution that satisfies the task contract and
acceptance criteria. Produce modern, maintainable code, but keep effort
proportional to explicit requirements, realistic risks, and the agreed release
scope.

- Prefer one clear code path over speculative flexibility.
- Reuse existing architecture, dependencies, and conventions before
  introducing new abstractions.
- Do not add unsolicited abstraction layers, generalized frameworks,
  compatibility shims, fallback systems, migration machinery, production
  infrastructure, or handling for hypothetical future requirements.
- Do not broaden a task merely because a more enterprise-grade solution is
  possible.
- Treat an edge case as in scope only when the task or authoritative
  documentation names it, supported user behavior can reasonably reach it,
  security or data integrity requires it, or it reproduces an observed failure.

## Testing Scope and Stop Condition

- Test the requested behavior, important realistic boundaries, and identified
  regressions.
- Do not create exhaustive or combinatorial tests for implausible edge cases
  unless the task, a documented requirement, or an observed defect requires
  them.
- When acceptance criteria and required verification pass, stop. Do not
  continue refactoring, polishing, documenting, or expanding adjacent
  functionality without a concrete task requirement.
- Report material out-of-scope concerns briefly; do not implement them
  automatically.

Correctness, accessibility, security, privacy, and the repository gates in
[`QUALITY_GATES.md`](QUALITY_GATES.md) remain mandatory. Proportionality must
not be used to bypass them.
