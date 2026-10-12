# Project Agents Guide

## Purpose

This directory contains the working documents for one project only.

The goal is to keep project context, tasks, and decisions organized so that future work can continue smoothly.

## Scope

- This file applies to the current project directory and its subdirectories
- Keep all project-specific content inside this directory
- Do not mix content from other projects into this folder

## Read First

Before doing substantial work, read files in this order:

1. `README.md`
2. `context/project-overview.md`
3. `context/research-notes.md` for exploratory projects
4. `tasks/active.md`
5. `tasks/decisions.md`
6. `context/architecture.md` if technical context is needed

## Directory Rules

- `context/` stores stable background knowledge
- `context/research-notes.md` stores exploratory notes, open questions, and interim findings
- `tasks/` stores active work, backlog, and decisions
- `prompts/` stores prompts worth reusing
- `logs/` stores chronological work notes
- Prefer updating an existing document over creating a duplicate one

## Working Rules

- Use English for AI-maintained project documents unless the user explicitly asks for another language
- Use Chinese for conversation by default unless the user requests another language
- Prefer small, clear, reversible changes
- Briefly explain intended edits before changing files
- Use existing project docs to infer context before asking questions
- If assumptions are made, state them clearly
- Stay within the current task scope unless the user asks for broader changes
- For exploratory work, prefer fact gathering, concept clarification, and question framing before solutioning
- Distinguish clearly between facts, assumptions, open questions, and recommendations
- If normal file editing is blocked by the environment but the user has clearly requested the change, escalation may be used to complete the requested write safely

## Documentation Rules

- Put stable knowledge in `context/`
- Put exploratory background learning and research notes in `context/research-notes.md`
- Put current execution status in `tasks/`
- Record important decisions in `tasks/decisions.md`
- Add reusable prompts only when they are likely to help again
- Update docs after meaningful work so the next collaborator can continue quickly

## Numbered Design And Change Points

- Assign a stable, individually referenceable ID to every design point and change point before implementation, including proposals, review findings and problems discovered during testing.
- Reuse the project's existing hierarchical `M<n>.<s>.<t>` task IDs rather than creating a competing numbering system. If a task contains multiple independently discussable design or change points, give them distinct numbered child entries using the existing optional fourth level.
- Use these IDs in design discussions, approval requests, implementation summaries, validation evidence and follow-up references; a broad milestone ID alone is insufficient for several distinct points.
- Never renumber or reuse a published ID. Retain rejected, deferred and superseded points with their status and links to replacements.

## Reuse And Design Change Approval

- Before changing an existing system, inspect its approved design, relevant code and existing components. Prefer extending or reusing them; identify the concrete reuse path in the numbered proposal.
- Do not silently introduce a parallel mechanism, new abstraction, framework, state model or alternative source of truth. Explain why existing designs/components are insufficient, the proposed alternative, affected interfaces, complexity and validation impact; obtain explicit user approval before implementing it.
- Approval of a goal or earlier design is not blanket permission to invent a different mechanism later. Update the numbered design decision and its approval record before proceeding with a material design change.
- During testing, surface newly discovered problems as numbered findings. If solving one requires a new mechanism/abstraction or departs from the approved design, pause the affected implementation, present the evidence and options, and discuss the design with the user before applying the solution. Testing is not an exception to this gate.
- Narrow implementation corrections that preserve the approved design may proceed under existing authorization, but still need numbered reporting and relevant verification. When unsure whether a fix changes the design, ask first.
- Continue independent, already-approved work where possible; do not hide unresolved design questions inside a workaround, refactor or test-only helper.

## Task Management

- Read `tasks/milestones.md` before planning or implementation.
- Classify the project as simple or complex.
- For a complex project, define and approve the known milestone sequence `M1` through `Mn` before implementation begins.
- Use `M<n>` for milestones, `M<n>.<s>` for subgoals, and `M<n>.<s>.<t>` for executable tasks.
- Add a fourth numeric level only when an executable task requires further decomposition.
- Assign IDs sequentially within their parent; never renumber or reuse an ID after progress reporting or implementation begins.
- Keep cancelled or superseded IDs and mark their final state.
- Reference the most specific applicable ID in active status, backlog, decisions, implementation notes, tests, and work-log entries.
- Add new requests or ideas to `tasks/backlog.md`
- Track in-progress work in `tasks/active.md`
- Move major conclusions or tradeoffs into `tasks/decisions.md`
- Record notable progress in `logs/worklog.md`

## Naming Rules

- Use `YYYY-MM-DD` for dates
- Prefer short and descriptive file names
- Keep files in Markdown or plain text unless another format is necessary

## Safety

- Do not delete files unless explicitly requested
- Confirm dangerous commands before running them
- Preserve user-authored content unless edits are requested
- Avoid broad rewrites when a targeted update is sufficient

## Output Style

- Be concise, practical, and easy to scan
- Surface assumptions, risks, and next steps when useful
- Favor actionable summaries over long restatements
