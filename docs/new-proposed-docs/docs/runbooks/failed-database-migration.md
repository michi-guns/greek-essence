# Runbook: Failed Database Migration

## Trigger

A Drizzle/PostgreSQL migration fails or leaves the deployment unable to start.

## Impact

The application may be partially unavailable or running against an unexpected
schema version.

## Procedure

1. Stop further deployments.
2. Capture the migration error and current schema version.
3. Determine whether the migration was transactional.
4. Compare the actual schema with the expected migration state.
5. Restore from backup or apply a reviewed corrective migration.
6. Run database and application verification checks.
7. Resume deployment only after schema compatibility is confirmed.

## Safety

Do not manually delete production data or edit migration history without
review, backup, and a documented recovery plan.

## Note

Replace this placeholder with exact hosting, backup, and deployment commands
after infrastructure is chosen.
