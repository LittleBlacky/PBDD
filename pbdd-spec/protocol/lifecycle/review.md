# Review Lifecycle

Review states:

```text
Requested
  -> Reviewing
  -> Addressing
  -> Approved
```

## Optional States

- `Changes Requested`
- `Canceled`

## Invariants

- A review with requested changes must list actionable findings.
- An approved review must reference the reviewed artifact or code revision.

