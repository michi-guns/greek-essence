# Ralph Loop Glossary

## Ralph Campaign

The process of taking a defined list of one or more tasks and implementing them through the Ralph Loop. A campaign may contain a single task, particularly during testing, or multiple related tasks that together deliver a bounded outcome.

A campaign begins when its campaign identity is established and work starts on its first task. It ends when every task in its defined list is completed, the campaign is explicitly abandoned, or Ralph reaches a terminal blocked outcome requiring operator action.

## Task

A bounded unit of work within a Ralph Campaign. A task has its own identity, scope, acceptance criteria, verification requirements, and completion state.

## Step

A meaningful stage of work within a task, such as implementation, independent review, correction, verification, or closure. Steps provide the primary task-level breakdown for analytics when their boundaries can be observed reliably.

## Ralph Iteration

One fresh root-orchestrator session launched by the Ralph controller. A task may require multiple iterations, and one iteration may coordinate multiple task steps without changing the task or campaign identity.

## Root Orchestrator

The fresh `greekroot` Sol session launched for a Ralph Iteration. It selects or resumes authorized work, delegates substantial implementation and independent review, verifies repository evidence, and updates the handoff.

## Implementer

A fresh `greekimpl` Luna session responsible for substantial implementation within one scoped task. It does not independently approve its own work.

## Reviewer

A fresh `greekreview` Terra session responsible for independent review or read-only health and timeout assessment, depending on how it is invoked.
