# Iteration Protocol

Use this reference when the user asks for a feature, bug fix, refactor,
research task, release, or any change that should move the project forward.

## Iteration Loop

1. Boot the project.
2. Classify the request as an event.
3. Load the relevant brain state.
4. Select the workflow.
5. Plan the artifact and code changes.
6. Update or create the required artifacts.
7. Implement the code change.
8. Run the appropriate checks.
9. Update brain state.
10. Report what changed, evidence, risks, and next steps.

## Boot Before Work

Before changing files:

1. Read `pbdd.yaml`.
2. Read `brain/project.md`.
3. Read `brain/health/status.md`.
4. Inspect related files under `brain/feature/`, `brain/task/`,
   `brain/risk/`, `brain/decision/`, and `brain/knowledge/`.
5. Inspect relevant artifacts.

If PBDD is missing and the user asked to use PBDD, initialize it first.

## Request Handling

Never treat a non-trivial request as "just code". First decide what kind of
project event it is.

Common mappings:

- New capability -> Feature event
- Broken behavior -> Bug event
- Structure improvement -> Refactor event
- Investigation -> Research event
- Shipping work -> Release event
- Architectural choice -> Decision event
- Newly learned project fact -> Knowledge event

## Work Order

Use this order unless the user explicitly asks for a narrower action:

1. Create or update the spec/task/review artifact needed for the work.
2. Update brain entries that describe planned state.
3. Change source code and tests.
4. Run checks.
5. Update brain entries with actual state and evidence.
6. Update timeline and health.

## Pause Conditions

Ask the user before continuing when:

- The request changes product scope in a way the project brain cannot infer.
- A destructive migration is required.
- A workflow transition is blocked by missing required evidence.
- Several valid product decisions exist and none is implied by existing brain
  state.

Do not ask when the missing detail can be safely inferred from local code,
tests, or existing PBDD state.

