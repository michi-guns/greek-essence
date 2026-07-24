# Hermes Ralph/JZ Profiles

These source-controlled SOUL templates are the reviewable role contracts for the Ralph/JZ rebuild in the isolated worktree `C:/Users/jimzord12/Documents/GitHub/greek-essence-jz-ralph`. Live profile configuration, credentials, memories, and sessions remain outside Git under `%LOCALAPPDATA%/hermes/profiles/<name>/`.

| Role | Live profile | Source contract | Installed state |
|---|---|---|---|
| One-action workflow orchestrator | `jzgreekorch` | [jzgreekorch-SOUL.md](jzgreekorch-SOUL.md) | Installed; profile-owned configuration |
| TDD implementer for RED and/or GREEN | `jzgreekimpl` | [jzgreekimpl-SOUL.md](jzgreekimpl-SOUL.md) | Installed; profile-owned configuration |
| Independent code reviewer | `jzgreekrev` | [jzgreekrev-SOUL.md](jzgreekrev-SOUL.md) | Installed; profile-owned configuration |
| Independent rendered visual reviewer | `jzgreekvisualrev` | [jzgreekvisualrev-SOUL.md](jzgreekvisualrev-SOUL.md) | Installed; profile-owned configuration |

All four profiles are installed, have `terminal.cwd` set to this isolated worktree, and their live `SOUL.md` files match the source templates. The controller names only `jzgreekorch`; it does not override the profile-owned model, provider, or reasoning configuration. The orchestrator creates fresh standalone child sessions and never resumes a prior role session.

## Reproducibility and role boundary

- The four templates above are the only retained source-controlled role contracts for this workflow. Obsolete legacy source templates are not runtime dependencies.
- Do not copy runtime configuration, credentials, memories, or sessions into this directory.
- The live recommended JZ skill comes from `features-cli docs current`; role contracts must load that skill and its required references rather than pin remembered workflow behavior.
- Child briefs must state the one assigned action, authority paths, resolved engineering depth, gates, evidence path, and prohibited side effects.
- Code and visual reviews create new immutable evidence files; implementation agents never edit them.

## Read-only installed-profile checks

```bash
hermes profile show jzgreekorch
hermes profile show jzgreekimpl
hermes profile show jzgreekrev
hermes profile show jzgreekvisualrev

hermes -p jzgreekorch config show
hermes -p jzgreekimpl config show
hermes -p jzgreekrev config show
hermes -p jzgreekvisualrev config show
```

These commands inspect configuration only. They do not authorize a profile launch, feature transition, signal mutation, legacy-profile retirement, staging, commit, push, or deployment.
