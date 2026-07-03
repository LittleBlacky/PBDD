# Bug Lifecycle

Bug states:

```text
Reported
  -> Triaging
  -> Fixing
  -> Verifying
  -> Resolved
```

## Optional States

- `Duplicate`
- `Won't Fix`

## Invariants

- A bug in `Fixing` must reference reproduction notes.
- A bug in `Resolved` must reference verification evidence.

