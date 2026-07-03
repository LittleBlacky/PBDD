# Task Lifecycle

Task states:

```text
Todo
  -> Doing
  -> Done
```

## Optional States

- `Blocked`
- `Canceled`

## Invariants

- A blocked task must include a blocker reason.
- A done task must include completion evidence.

