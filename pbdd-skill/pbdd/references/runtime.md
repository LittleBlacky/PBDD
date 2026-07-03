# Runtime Reference

## Responsibilities

A PBDD runtime:

1. Reads the project manifest.
2. Loads brain state.
3. Interprets user intent as events.
4. Applies valid workflow transitions.
5. Updates brain state.
6. Creates or updates artifacts.
7. Reports evidence and remaining risks.

## Non-Responsibilities

A PBDD runtime must not:

- Redefine lifecycle states that already exist in the spec.
- Treat prompts as protocol.
- Store implementation-only metadata in brain files.
- Delete project history without an explicit superseding event.

## Protocol References

For full iteration behavior, read these files as needed:

- `iteration-protocol.md` for the end-to-end loop.
- `event-handling.md` for request classification.
- `workflow-execution.md` for lifecycle transitions.
- `brain-maintenance.md` for brain updates.
- `artifact-maintenance.md` for engineering outputs.
- `done-criteria.md` before marking work complete.

## Event Handling

When a user asks for a change, map it to the smallest useful PBDD event.

Examples:

- "Plan coupon support" -> `feature.proposed`
- "Start Task-23" -> `task.started`
- "This is blocked by auth" -> `task.blocked`
- "Record why we chose SQLite" -> `decision.recorded`

## Transition Handling

Before editing:

1. Identify the subject kind and current state.
2. Locate the matching workflow file.
3. Confirm the target state is reachable from the current state.
4. Identify required artifacts or evidence.

If a transition is invalid, explain the missing state or evidence and propose the nearest valid transition.

## Mutation Order

Use this order for file updates:

1. Artifacts that provide required evidence.
2. Brain entity files.
3. Timeline entries.
4. Health summary.

This keeps state explainable if a run is interrupted.
