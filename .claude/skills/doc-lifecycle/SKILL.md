---
name: doc-lifecycle
description: Audit and maintain a repository's markdown documents so they do not accumulate and go stale - update what drifted, merge what overlaps, delete what has outlived its purpose. Use at the end of a task, phase or feature and before reporting work done; when a plan, handoff, brief, notes or README has been superseded by the work that just landed; when two documents disagree; or when the user asks to clean up, consolidate, audit or prune documentation.
---

# doc-lifecycle

## Purpose

Work finishes, the agent stops, and nobody asks whether the documents that described the work
still make sense. Plans outlive their implementation. Handoffs outlive the session that read
them. Two files end up describing the same thing and one of them is wrong. This skill is the
stop-and-look step, plus the procedure for doing it safely.

**A document is not free.** Every stale file costs the next reader time and can actively
mislead an agent into doing the wrong thing. Fewer, truer files beat more files.

## When this runs

Run it when any of these is true:

- A task, phase or feature is complete and you are about to report it done.
- The work that just landed implements, supersedes or contradicts a document.
- You created a plan, handoff, brief or notes file earlier in the work.
- Two documents disagree and you noticed.
- The user asks to clean up, consolidate, audit or prune documentation.

If none is true, say so in one line and stop. Do not audit documentation because a commit was
large.

## Step 1 — Decide the scope

In scope: markdown and text documents that describe the project to a human or an agent.
READMEs, plans, handoffs, briefs, conventions, architecture notes, runbooks, agent guides.

**Never touch these:**

- **Task-tracker files managed by a CLI** (for example a `backlog/` directory). Editing them
  by hand corrupts metadata and history. Use the tool's own commands or leave them alone.
- **Decision registers and changelogs.** They are append-only history. A decision that is no
  longer true is superseded, not deleted, and superseding one is a decision the owner makes.
- **Anything git-ignored.** Local evidence, scratch directories and personal preference files
  are not the repository's business.
- **Licences, codes of conduct, and files the project did not author.**

## Step 2 — Classify every in-scope document by lifespan

This is the judgement the whole skill turns on. Two kinds:

- **Timeless** (durable). It stays true after the work lands. Conventions, architecture, the
  index, rules for editing. These get _updated_.
- **Work-scoped.** It exists to get a piece of work done and dies with it. Plans, handoffs,
  build briefs, migration notes, TODO lists. These get _deleted_ when the work lands.

A document can be a mix. That is the normal case, and it is why step 3 exists rather than a
straight delete.

## Step 3 — Act

**Update** a timeless document that drifted. Correct it in the same pass, without asking. Say
what changed in the commit body.

**Merge** when two documents overlap. The bigger or more current one absorbs the other. Route
each piece of unique content by _lifespan_, not by convenience: timeless content goes to the
timeless document even if you are merging into a work-scoped one, or it dies a second time when
that file is deleted.

**Delete** a work-scoped document whose work has landed, and remove every pointer to it in the
same commit.

## Step 4 — The deletion safety rule

**Before deleting or merging away any file, read all of it, then write an accounting: for each
piece of content unique to that file, state where it moved or why it dies with the file. If
you cannot write that accounting, the file is not ready to be removed.**

This is not ceremony. A file being deleted is exactly the file nobody will read again, and the
one line that matters is usually not in its summary or its headings. Skim-then-delete is how
a real instruction gets lost.

Put the accounting in the commit body. It is the record of what was decided and the only
practical way for the owner to spot a mistake.

## Step 5 — When to stop and ask

Do the ordinary work yourself. Stop and ask the owner only when:

- Two documents disagree and you cannot tell which is current.
- The correction would reopen an accepted decision.
- The "stale" content may be deliberate.
- A file is work-scoped but you cannot confirm the work actually landed.

State the conflict and stop. Do not guess.

## Step 6 — Report

Report in the reply, not only in the commit:

- What you updated, and what was wrong with it.
- What you merged, and where each unique piece went.
- What you deleted, and why its work is done.
- What you stopped on, if anything.

"Documentation checked" is not a report.

## Writing a work-scoped document so it can die

When you create a plan, handoff or brief, make its disposal automatic rather than someone
else's judgement call later:

- Open the file with a header saying it is temporary, why it exists, and the condition under
  which it gets deleted.
- Put the same instruction in the index or README entry that points at it.
- Put it in the commit body too.

Three copies, because the file will be read by someone who opens only one of them.

## Anti-patterns

- Deleting a file because its title sounds obsolete. Read it.
- Merging two documents by concatenating them. That creates one stale document instead of two.
- "Improving" prose that was fine. This skill removes and corrects; it does not restyle.
- Hand-editing CLI-managed task files.
- Running the audit to satisfy a gate, cheaply, under time pressure. That is when things get
  deleted that should not have been.
