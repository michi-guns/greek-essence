# Greek Essence v1 — Delivery Workflow

Authority: [00-DECISIONS.md](00-DECISIONS.md) D-020 … D-025.
Design goal: **zero friction.** Agents ship without asking permission for routine work.

---

## 1. Repo reset procedure

Run once, before any v1 work. Copy the salvage set out first.

```bash
cd greek-essence

# 0. Salvage — outside the repo
mkdir -p ../ge-salvage
cp -r docs/v1 ../ge-salvage/
cp -r backlog  ../ge-salvage/          # config.yml only; no tasks seeded yet
cp app/globals.css ../ge-salvage/
cp .editorconfig .prettierrc .gitattributes .node-version ../ge-salvage/

# 1. Archive the current main, permanently
git checkout main && git pull
git branch archive/v0-preview
git tag  archive/v0-preview-final
git push origin archive/v0-preview --tags

# 2. New history, no parent
git checkout --orphan v1
git rm -rf .                      # clears the index, not the archive branch
# ...scaffold the new project here (Phase 0.1)...
git add -A
git commit -m "chore: initialise v1"

# 3. Make it main
git branch -M main-old-ref main 2>/dev/null || true
git push origin v1:main --force-with-lease
git checkout main && git reset --hard origin/main
```

Then in GitHub: keep `main` as default, **remove branch protection that requires PRs**
(D-023 gives agents merge authority), and delete the stale `docs/*` and `chore/*` remote
branches once confirmed merged or abandoned.

**Do not delete `archive/v0-preview`. Ever.** The grilling decisions in it are the only
record of why several v1 rules exist.

---

## 2. Branch flow

```
main                         always deployable, always the source of truth for backlog/
 │
 ├─ phase/03-public-site     one open at a time · max 7 days · rebase from main daily
 │   ├─ task/03.1-home       branched from the phase · merged back on completion
 │   ├─ task/03.2-destinations
 │   └─ task/03.3-packages
 │   └── merge phase → main when the phase's tasks are all merged and checks are green
 │
 └─ backlog/** travels on the same branch as the work it describes.
    Backlog.md reconciles task state across active branches itself (§3).
```

### Standing agent authority (no approval needed)
create branches · commit · push · merge task→phase · merge phase→main once checks pass ·
delete branches proven merged · rebase a phase branch onto `main` · create and update tasks
through the `backlog` CLI.

### Always requires the operator
force-push · history rewrite · deleting an unmerged branch · deleting `main` or any
`archive/*` ref · anything that discards uncommitted work in another worktree · adding a paid
service · sending real email to a real customer address.

### Non-happy paths
Agent judgement. Hotfix straight off `main` into `fix/<slug>` and merge back is fine, and so is
abandoning a task branch. Say what you did in the merge commit body. These rules are
conventions to keep the history legible — they are not a permission system.

### Commit messages
Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `style:`, `refactor:`, `test:`).
Scope optional. Keep commitlint; drop everything else from the old husky chain except
lint-staged formatting.

---

## 3. Backlog.md conventions

We use the real [Backlog.md](https://github.com/MrLesk/Backlog.md) CLI, and we adapt to it
rather than the other way round. It is more capable than a folder of markdown files, and
several rules in an earlier draft of this document were solving problems it already solves.

### Init

```bash
backlog init --task-prefix GE
```

This creates `backlog/` and `backlog/config.yml`, and generates an `AGENTS.md` /`CLAUDE.md`
stanza telling agents to run `backlog instructions overview`.

### `backlog/config.yml` for this project

Verified against **backlog.md v1.52.0**. Note the file stores **snake_case**; the CLI reads and
writes **camelCase** (`backlog config set autoCommit true` → `auto_commit: true` in the file).

```yaml
project_name: "Greek Essence"
task_prefix: "GE"            # read-only after init
default_status: "To Do"
statuses: ["To Do", "In Progress", "In Review", "Blocked", "Done"]
zero_padded_ids: 3           # a DIGIT COUNT, not a boolean -> GE-001
auto_commit: true            # commits task changes automatically
remote_operations: true
check_active_branches: true
active_branch_days: 14       # our phase branches live <= 7 days; 30 is wider than needed
bypass_git_hooks: false
auto_open_browser: false
default_port: 6420
definition_of_done:
  - "Acceptance criteria met"
  - "typecheck, lint and unit tests pass"
  - "Verified in a browser on the preview URL"
  - "Task branch merged into its phase branch"
```

**List-valued keys cannot be set from the CLI.** `backlog config set statuses ...` is refused
with "cannot be set directly". `statuses`, `definition_of_done`, `priorities`, `types`,
`labels`, `projects` and `milestones` are edited in `config.yml` directly, through the
interactive `backlog config` wizard, or in the Web UI. This is not an exception to the
never-hand-edit rule below — that rule covers task/draft/doc/decision/milestone markdown,
not the config file.

### Use the CLI, never edit the files

Backlog.md's own agent instructions are explicit about this, and we adopt it verbatim:

> Do not edit Backlog task, draft, document, decision or milestone markdown files directly.
> Use the `backlog` CLI so metadata, relationships and history stay consistent.

So: `backlog task create`, `backlog task edit`, `backlog task list`, `backlog task view`,
`backlog board`, `backlog search`. An agent that hand-writes a task file has made a mistake.

### Structure mapping

| Our concept | Backlog.md mechanism |
|---|---|
| Milestone (M0…M5) | Native milestone — `backlog milestone add "M3 Public Site"` |
| Phase (P3.1…) | A label on the task, e.g. `phase:P3.1` |
| Task | A task. **The CLI assigns the ID** (`GE-1`, `GE-2`, …) |
| Planning ref (`T-03.4`) | First line of the task description — a pointer back to `04-ROADMAP.md`, not an ID |
| Estimate (min/avg/max) | There is no native estimate field. Put `est: 90/180/360 min` in the description |
| Dependencies | Native dependency links |
| Decision records | `backlog decision` is available. We are **not** using it for v1 — `00-DECISIONS.md` is a narrative register, and splitting it into per-decision files would fragment the one document agents need to read whole |

### Cross-branch state — the rule this replaces

An earlier draft of this document invented a rule: *"commit `backlog/**` straight to `main`,
bypassing the branch flow, so everyone sees current task state."*

**Drop it.** `check_active_branches: true` (on by default) reconciles task state across every
branch active within `active_branch_days`, which is exactly what that rule was solving — and it
does it without a special-cased hole in the branch flow. Backlog files travel on the same branch
as the work they describe.

### The push gap — verified, and how we close it

`auto_commit: true` **commits but does not push.** Confirmed by experiment: creating and editing
a task produced `Create task GE-002` and `Update task GE-002` commits, and nothing was pushed.

An earlier draft of this document proposed `onStatusChange: git push`. **That key does not exist
in v1.52.0** — it appears in the project's ADVANCED-CONFIG.md but not in `backlog config list`.
It was an unverified inference and it is withdrawn.

Close the gap with a `post-commit` hook that pushes only backlog-only commits, so code pushes
stay deliberate:

```sh
# .husky/post-commit  — set up in T-00.10, after the repo reset
changed=$(git diff-tree --no-commit-id --name-only -r HEAD)
case "$changed" in
  backlog/*) git push --quiet || true ;;
esac
```

Zero discipline required, and it keeps the "every agent sees the claim within seconds" property.

**Git identity must be configured** or `auto_commit` fails with
`unable to auto-detect email address` and the task operation aborts half-done. Check it in
T-00.10 preflight.

### Verified behaviours worth knowing

| Behaviour | Detail |
|---|---|
| Task ID / filename | `GE-001` → `backlog/tasks/ge-001 - Title-slugified.md` |
| Real frontmatter | `id, title, status, assignee[], created_date, labels[], dependencies[], priority, ordinal` |
| Body format | Sectioned with HTML markers: `SECTION:DESCRIPTION`, `AC:BEGIN/END`, `DOD:BEGIN/END` |
| `--ac` | **Does not split on commas** — repeat the flag per criterion. `-l` and `-a` *do* accept comma-separated |
| Native task types | `bug, feature, enhancement, task, chore, docs, spike` via `--type` |
| Subtasks | `-p/--parent <taskId>` exists — an alternative to `phase:` labels if we want phases as parent tasks |
| Agent-readable output | `--plain` and `--json` on `task list` / `task view` |
| Deletion | **There is none.** Only `archive`, `complete`, `demote`. Backlog.md is append-only; `milestone remove` archives too |
| DoD defaults | Auto-attached to every new task from config; `--no-dod-defaults` opts out |

### CLI, not MCP — decided

Backlog.md ships an MCP server (`backlog mcp start`). **We are not using it.** CLI only.

The reasoning, because this reverses an earlier recommendation in this document:

- **MCP tool definitions are resident context.** They load at session start and stay loaded
  whether or not the session ever touches the backlog. Reported costs for a full-featured
  server run to ~55k tokens before a single question is asked; one practitioner measured
  ~145k tokens via MCP vs ~4.2k for the same job via CLI. Backlog.md's server is far smaller
  than the GitHub server those numbers come from, so treat the magnitude as directional —
  but the *shape* of the cost is the same, and the CLI's baseline is zero.
- **The published decision framework puts this case squarely on the CLI side.** MCP earns its
  overhead for remote/multi-tenant SaaS, OAuth, dynamic discovery, and services with no CLI.
  Backlog.md is a local binary operating on local files in our own repo, with no auth. That is
  the textbook CLI case.
- **Models already know CLI syntax.** `backlog task list -s "To Do"` needs no schema
  interpretation; it looks like every CLI in the training data. An MCP tool surface is a novel
  abstraction the model has to reason about.
- **The tool is already designed for lazy loading, and we measured it.** `backlog instructions
  overview` is 416 words (~550 tokens); the three detailed guides are 925 / 639 / 397 words.
  An agent pulls only what the current step needs, and a session that never touches the backlog
  pays nothing. `backlog init --integration-mode` defaults to `cli` and its own help text says
  "cli instructions are recommended".
- **Its own `AGENTS.md` leads with the CLI.** We follow the tool author's primary contract.

*Partial mitigation worth knowing:* Claude Code defers MCP tool schemas and loads them on
demand via tool search, which blunts the resident-context cost. It does not remove it, and it
does not apply to every harness the agents might run in.

**Reversal condition:** if agents repeatedly fail at CLI invocation or output parsing — wrong
flags, mangled quoting, misread board output — that is evidence the typed surface is worth its
cost. Turn the MCP on then. It is one command and a config line; this is not a one-way door.

Human interface stays the same either way: `backlog board` for the TUI, `backlog browser` for
the web UI on port 6420.

### The built-in three-checkpoint workflow

Backlog.md has an opinionated review flow: **review the spec → review the plan → review the
code**. For v1, use checkpoint 1 and 3 and skip checkpoint 2 on tasks under ~2 hours. A 9-page
marketing site does not need a plan review for "build the footer".

## 4. `AGENTS.md` — what goes in it

One file, target < 200 lines, `CLAUDE.md` is a one-liner pointing at it. Sections:

0. **The Backlog.md stanza** — generated by `backlog init`. Leave it at the top, don't rewrite it.
1. **What this project is** — 5 lines. Static marketing site, no backend, Google Forms intake.
2. **Read before working** — run `backlog instructions overview` (Backlog.md's own generated
   stanza does this for you), then `docs/v1/00-DECISIONS.md`, then your task via
   `backlog task view <id>`. That's the whole reading list.
3. **Stack and versions** — with the note that Next 16 / Tailwind 4 / Zod 4 differ from
   training data; read `node_modules/next/dist/docs/` before writing routing or config code.
   *(This is the single most valuable line in the reference repo's AGENTS.md.)*
4. **Conventions** — file layout, naming, where components live, design tokens are the only
   source of colour/spacing (no arbitrary Tailwind values).
5. **Git** — section 2 above, compressed.
6. **Checks** — the commands and when to run them.
7. **Posture** — "balanced commercial engineering: deliver the behaviour, handle realistic
   failures, stop when the checks pass. Don't build abstractions for one caller."
8. **Standing authorisations and the `.local/` pointer** — §5.
9. **The standing deviation clause** — conventions are direction; deviate when needed and say so.

### Borrow from `nextjs-todo-list-example`, don't copy
Worth lifting: the Next-16-isn't-what-you-know warning · the engineering-posture paragraph ·
the standing browser/dashboard permission grant · the independent-reviewer-subagent rule
(use it for **phase** closeouts only, not every task — it's too heavy for a 9-page site).

Leave behind: AgentForge, the `.dwf/` framework, the 43-skill directory, the Trello skills,
the multi-stage planning protocol. That machinery is priced for a long-lived platform.
v1 is five weeks long.

**Skills worth installing (4, not 43):** `frontend-ui-engineering`, `web-design-guidelines`,
`next-dev-loop`, `playwright-cli`.

---

## 5. Agentic posture — standing permissions and local preferences

**The operating principle: agents should be able to do the work.** Friction is the tax we are
trying not to pay, and an approval prompt for `pnpm test` is not a safety control — it is a
habit that trains everyone to click "allow" without reading, which is how the prompt that
*should* have stopped something gets waved through too.

So: pre-authorise the routine surface broadly, deny the genuinely destructive specifics, and
keep the number of prompts small enough that each one still means something.

### `.claude/settings.json` — committed, shared by both developers

This is the real mechanism for the permissions file. Two files exist and the distinction matters:

- **`.claude/settings.json`** — committed. Project-wide standing permissions, so the operator and
  the junior get the same behaviour without either configuring anything.
- **`.claude/settings.local.json`** — gitignored. Personal overrides only.

Shape (finalised in T-00.5):

```jsonc
{
  "permissions": {
    "allow": [
      "Bash(pnpm *)",                  // install, dev, build, test, lint, typecheck
      "Bash(npx sanity *)",            // typegen, schema deploy, dataset ops (A-006)
      "Bash(netlify *)",               // deploy, logs, env, status (A-005)
      "Bash(backlog *)",               // task management (D-021b)
      "Bash(npx skills *)",            // agent skill installs
      "Bash(git *)", "Bash(gh *)",     // the D-023 branch flow
      "WebFetch", "WebSearch"
    ],
    "deny": [
      "Bash(git push --force*)",
      "Bash(git reset --hard*)",
      "Bash(git clean *)",
      "Bash(rm -rf *)",
      "Bash(npx sanity dataset delete*)",
      "Bash(netlify sites:delete*)"
    ]
  }
}
```

The deny list is the whole safety story, and it is short on purpose: history destruction, file
destruction, and deleting the client's dataset or site. Everything else an agent might do to
this project is recoverable from Git.

### Standing authorisations — prose in `AGENTS.md`

Some authorisations are not tool permissions, they are statements of intent. Borrowed in shape
from `nextjs-todo-list-example`:

> The owner grants standing permission to use the Netlify, Sanity, Google and Resend dashboards
> through the personal Chrome extension or Computer Use, for tasks already authorised — including
> inspecting settings and applying routine configuration such as environment variables, webhooks
> and integrations. Check the intended account and project before writing. No additional
> permission is needed to reach the browser or save those changes.
>
> This does **not** waive: the deny list above, a production deployment (A-003 — deploys are
> deliberate and budgeted), sending real email to a real customer address, deleting anything of
> the client's, or any paid commitment.

### `.local/` — untracked, personal

Gitignored directory, matching the convention already used in `marine-engineer-cv` and
`agentic-wave`:

```
.local/
  preferences/user-profile.md    how the owner wants to be talked to — read before replying
  evidence/<date>-<slug>/        screenshots, logs, run output from verification
  README.md                      what lives here and why it is untracked
```

`AGENTS.md` carries a short pointer and nothing more:

> If `.local/preferences/user-profile.md` exists, read it before replying. It holds local
> preferences; keep it untracked and never copy its contents into shared documentation.

Two rules: **`.local/` is never committed**, and **nothing in it is authoritative for the
product** — decisions live in `docs/v1/`, tasks live in `backlog/`. It holds preferences and
evidence, not truth.

## 6. Quality gates

Deliberately thinner than v0. Three tiers:

| Tier | When | What |
|---|---|---|
| **pre-commit** | every commit | lint-staged: eslint --fix + prettier |
| **pre-push** | every push | `typecheck` + `lint` + `test:unit` + gitleaks |
| **phase merge → main** | phase close | the above + `build` + Playwright smoke + Lighthouse on the changed templates + an independent reviewer subagent |

Dropped from v0: knip, the 80% coverage gate, `pnpm audit --audit-level=high` on every push
(move to a weekly Renovate/Dependabot pass), unlighthouse on every push, the content validator.

*Why:* v0's `check:push` ran secrets scan + audit + format + lint + knip + typecheck +
coverage + build + full e2e on every single push. That is a multi-minute tax on every commit,
paid hundreds of times, to catch problems that a phase-close gate catches just as well.
