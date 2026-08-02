# Implementation Workflow

For each business capability:

1. Read the relevant documentation.
2. Define or update the domain specification.
3. Identify assumptions and open questions.
4. Implement the smallest useful domain behavior.
5. Add domain tests.
6. Define application ports and use cases.
7. Add application tests with fakes.
8. Implement infrastructure adapters.
9. Add Next.js presentation entry points.
10. Add integration or end-to-end coverage where valuable.
11. Update current-state docs and ADRs.
12. Run quality gates.

## First vertical slice

```text
Customer
→ Travelers
→ Quote
→ Sanity offering
→ Snapshot
→ Acceptance
→ Booking
→ Payment
→ Confirmation
```

Do not model the entire travel industry before completing a real workflow.
