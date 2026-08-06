# Quality Gates

Before a change is complete, run the repository's relevant checks:

- Type checking
- Linting
- Unit tests
- Integration tests
- Production build
- Migration validation when persistence changes
- Documentation link checks when docs change

Review for:

- Domain imports from infrastructure
- Missing authorization
- Missing runtime validation
- Floating-point money
- Drizzle or Sanity types leaking across boundaries
- Data-loss migrations
- Historical records coupled to current CMS content
- Unverified assumptions encoded as facts
- Documentation that no longer matches current behavior

Do not report success when a relevant check failed or was skipped.
