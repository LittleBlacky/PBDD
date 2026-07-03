# Event

An event is a request to change project state.

## Contract

An event must be immutable once recorded. If an event is incorrect, another
event should correct or supersede it.

## Event Types

- `project.created`
- `feature.proposed`
- `feature.planned`
- `feature.started`
- `feature.tested`
- `feature.completed`
- `task.created`
- `task.started`
- `task.blocked`
- `task.completed`
- `risk.raised`
- `decision.recorded`
- `knowledge.added`

