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
