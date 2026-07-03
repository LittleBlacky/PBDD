# Feature Lifecycle

Feature states:

```text
Draft
  -> Planning
  -> Implementing
  -> Testing
  -> Done
```

## Terminal States

- `Done`
- `Canceled`

## Invariants

- A feature in `Implementing` must have at least one task.
- A feature in `Testing` must reference a test artifact or test plan.
- A feature in `Done` must reference completion evidence.

