# Coding Rules

- Use strict TypeScript.
- Keep domain code free of framework imports.
- Prefer behavior-rich domain methods over public mutation.
- Represent money without floating-point arithmetic.
- Use explicit domain, application, persistence, CMS, and UI types.
- Do not return Drizzle rows or Sanity documents from use cases.
- Create interfaces only when they protect real boundaries.
- Keep `shared/` small.
- Add domain events only for concrete workflows.
- Preserve historical transaction data.
- Favor small changes over broad rewrites.
- Follow existing repository conventions unless an approved decision changes them.
