# Event Handling

Use this reference to convert user intent into PBDD events.

## Event Rule

Every meaningful project change starts as an event. The event is the runtime's
explanation of what kind of change the user requested.

## Event Shape

Use this conceptual shape when recording or reasoning about events:

```text
id: <event-id>
type: <kind.action>
source: user | agent | system | ci
subject:
  kind: feature | task | bug | decision | knowledge | release | project
  id: <subject-id>
payload:
  summary: <short summary>
```

## Classification

Classify requests by intent:

- "Add", "support", "enable", "build" -> `feature.proposed`
- "Fix", "broken", "regression", "error" -> `bug.reported`
- "Refactor", "simplify", "restructure" -> `refactor.proposed`
- "Research", "investigate", "compare" -> `research.started`
- "Release", "ship", "publish" -> `release.prepared`
- "Decide", "record why", "choose" -> `decision.recorded`
- "Remember", "note", "document this" -> `knowledge.added`
- "Start task" -> `task.started`
- "Mark done" -> `task.completed`
- "Blocked by" -> `task.blocked`

## Event Granularity

Choose the smallest event that can drive useful engineering work.

If one user request contains several independent changes, split it into several
events and create tasks for each.

## Event Output

When starting an iteration, report the inferred event in plain language:

```text
Interpreted as: feature.proposed for refund support.
```

If the event creates durable state, record it in the relevant brain file or
timeline entry.

## Ambiguity Handling

If the user request is ambiguous:

1. Check existing brain state.
2. Check related specs and code.
3. Make a conservative assumption if the blast radius is low.
4. Ask the user only if the choice affects product behavior, data, security, or
   irreversible work.

