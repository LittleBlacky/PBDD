# Workflow Execution

Use this reference after classifying an event.

## Workflow Rule

Do not move project state arbitrarily. Move it through the lifecycle defined by
the PBDD spec or the project's declared workflow.

## Feature Workflow

```text
Draft -> Planning -> Implementing -> Testing -> Done
```

Required behavior:

- Draft: capture intent and rough scope.
- Planning: create or update spec, impact notes, and tasks.
- Implementing: change code and tests.
- Testing: run checks and collect evidence.
- Done: record evidence and final state.

## Bug Workflow

```text
Reported -> Triaging -> Fixing -> Verifying -> Resolved
```

Required behavior:

- Reported: capture symptom.
- Triaging: identify reproduction or likely cause.
- Fixing: patch code and tests.
- Verifying: run focused checks.
- Resolved: record verification evidence.

## Research Workflow

```text
Question -> Investigating -> Synthesizing -> Knowledge
```

Required behavior:

- Question: state the unknown.
- Investigating: collect evidence.
- Synthesizing: summarize implications.
- Knowledge: write durable knowledge into the brain or artifacts.

## Release Workflow

```text
Preparing -> Validating -> Releasing -> Released
```

Required behavior:

- Preparing: define scope.
- Validating: run checks and review risks.
- Releasing: update release artifacts.
- Released: record published state.

## Transition Check

Before updating state:

1. Identify current state.
2. Identify target state.
3. Check required artifacts or evidence.
4. Update artifacts first when they provide required evidence.
5. Update brain state after evidence exists.

## Invalid Transition

If the requested transition is invalid, do not fake state. Report:

- Current state
- Requested state
- Missing evidence or intermediate state
- Nearest valid next transition

