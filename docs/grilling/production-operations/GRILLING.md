# Production Operations Grilling

## Status

Paused and preserved as a mixed-layer classification source. Do not begin from
the stored D-001 question. Its approved disposition is recorded in
[`../CLASSIFICATION.md`](../CLASSIFICATION.md): durable mechanisms move to
Foundation Design, named owners and executable evidence move to Launch
Readiness, and locked provider/cost directions are not reopened by default.

This grill does not authorize implementation. Use [../DECISIONS.md](../DECISIONS.md)
and [../protocol.md](../protocol.md).

## Locked Project Context

- The preview is public, commercial, and accepts real enquiries.
- Commercially, launch is a market-validation experiment targeting zero new
  recurring platform spend. Use compliant free quotas until traffic provides
  evidence for an explicitly client-approved paid upgrade.
- The current direction is Vercel, Sanity, Neon, and the agency mail service.
  Netlify is only the accepted fallback direction if Vercel fails a mandatory
  commercial or technical gate.
- Production accounts and data must be client-controlled.
- Monitoring, backup, restore, incidents, rollback, and recovery need named
  owners and executable launch evidence.

## Scope

Define account ownership and access, environments, regions, secrets,
deployments, migrations, monitoring, backup and restore, provider limits,
incidents, rollback, costs, launch readiness, and operational handoff.

## Locked Decisions

None yet. Feature decision IDs begin at D-001.

## Open Questions

- D-001: Who owns production accounts and responds to failures?
- D-002: Does public launch use Vercel or a validated Netlify replacement?
- D-003: How are development, preview, and production separated?
- D-004: How are Neon backup and restore proven?
- D-005: What monitoring and notification failures require action?
- D-006: Who may deploy, migrate, rotate secrets, and roll back?
- D-007: How are free quotas monitored, and what evidence triggers a separately
  approved paid upgrade?

## Next Question

ID: D-001

Topic:
Production account and incident ownership.

Prompt:
Who should own the live service accounts and who is responsible when the site,
database, content platform, or email delivery fails?

Options:

1. (recommended): **Client-owned accounts with named technical administrators.**
   The client owns the domain and production services; the operator and approved
   developer receive separate removable access. Name one business incident
   contact and one technical responder, with a clear handover path.
2. **Operator-owned accounts transferred later.** The operator owns production
   initially and plans a later client transfer. This may launch faster but makes
   billing, data control, continuity, and offboarding harder.
3. **Shared credentials.** The client and developers use the same logins. This
   is simple initially but weakens security, auditability, revocation, and
   recovery and should not be used for real personal data.

Why this matters:
The person who owns an account controls billing, data, recovery, and access. A
public service should not become unavailable because the agency cannot reach a
former developer's personal account.

After answer:

- Lock account and incident ownership.
- Store D-002 as the next question.
