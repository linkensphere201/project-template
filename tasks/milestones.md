# Milestone Register

## Complexity

- Classification: Pending
- Planning gate: Pending

Complex projects must define the complete known milestone sequence `M1` through `Mn` and approve milestone-level acceptance targets before implementation begins.

## Numbering Contract

- `M<n>`: milestone.
- `M<n>.<s>`: stable subgoal or work package.
- `M<n>.<s>.<t>`: executable task.
- `M<n>.<s>.<t>.<u>`: optional final decomposition level when required.
- Assign IDs sequentially within their parent.
- Never renumber or reuse an ID after progress reporting or implementation begins.
- Keep cancelled or superseded IDs and mark their final state.
- Reference at least one ID in every active-status, decision, implementation, test, and work-log entry.

## Milestones

| ID | Name | Goal | Acceptance target | Status |
|---|---|---|---|---|
| `M1` | Define milestone | Define the first independently acceptable delivery. | Define measurable milestone acceptance. | Planning |

## Decomposition

### M1

- [ ] `M1.1` Define the first stable subgoal.
  - [ ] `M1.1.1` Define the first executable task.
