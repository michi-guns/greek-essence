# Agent Tooling Policy

## Purpose and Authority

This guide owns the repository's approved agent skills, browser interface, and
tool-specific documentation requirements. Guidance supplements and never
replaces executable checks from [`QUALITY_GATES.md`](QUALITY_GATES.md).

Do not use a repository-local skill that is not authorized here unless the
operator explicitly approves it.

## Baseline Approved Skills

| Skill                                | Use                                          |
| ------------------------------------ | -------------------------------------------- |
| Google Chrome Modern Web Guidance    | Modern-web implementation decisions          |
| Vercel `vercel-react-best-practices` | React and Next.js implementation and review  |
| Official Playwright CLI Agent Skill  | Browser inspection and interaction           |
| `greek-essence-quality-review`       | Structured Greek Essence quality reviews     |
| `trello-work-orchestrator`           | Read-only Trello Work Unit routing           |
| `trello-work-design`                 | Trello Work Unit design and clarification    |
| `trello-work-deliver`                | Trello Work Unit delivery lifecycle          |
| `trello-work-recover`                | Trello Work Unit recovery and reconciliation |

The archived agent-tooling documents are provenance only. Do not install or use
the retired `next-best-practices` skill.

For Next.js-specific work, consult the documentation bundled with the installed
Next.js version under `next/dist/docs/` and its approved generated agent rules.

## Browser Boundary

Playwright CLI is the only approved interactive browser interface. Do not
install, configure, or use Playwright MCP, `agent-browser`, Browser Use, Browser
Use CLI, or another overlapping browser-agent tool.
