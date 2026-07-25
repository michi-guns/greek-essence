# Ralph Loop Knowledge

Record only durable, non-obvious discoveries needed by future Ralph contexts. Current workflow state belongs in [HANDOFF.md](HANDOFF.md); `features-cli` remains the workflow ledger.

## K-001 — Hermes harness avoids the Codex Windows automation sandbox

- Observation: Windows `workspace-write` with the unelevated restricted-token backend rejects `apply_patch` when the runtime supplies split writable roots. The elevated backend requires interactive UAC setup and cannot run unattended here.
- Working configuration: Ralph invokes non-interactive, fresh Hermes profile sessions with `--yolo`; Hermes uses native file and terminal tools rather than the Codex CLI sandbox.
- Consequence: Repository safety instructions, task scope, deterministic checks, and the no-push/no-deploy/no-history-rewrite boundaries remain the safety layer.

## K-002 — Windows owned-tree cleanup must fail closed when ambiguous

- Observation: A controller can terminate abruptly while its owned Hermes root and descendants remain alive.
- Consequence: Treat a dead lock owner with a live recorded root as `AMBIGUOUS_SURVIVING_ROOT_PROCESS`; never launch a concurrent controller or automatically kill an unverified process tree.
- Controller relevance: On timeout or controlled cleanup, terminate only the verified owned root tree, verify its exit, and return a failure rather than guessing when ownership or cleanup cannot be proven.
