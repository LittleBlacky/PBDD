# Event Protocol

Events are the inputs to a PBDD runtime.

An event records intent. It does not directly mutate files. A runtime must map
the event to a valid workflow transition, then update brain state and artifacts.

## Required Event Fields

- `id`
- `type`
- `source`
- `occurred_at`
- `subject`
- `payload`

## Event Flow

```text
Event
  -> Workflow transition
  -> Brain mutation
  -> Artifact update
```

