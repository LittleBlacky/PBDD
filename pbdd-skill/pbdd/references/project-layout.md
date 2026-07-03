# Project Layout Reference

## Required Files

```text
project/
  pbdd.yaml
  AGENTS.md
  brain/
  artifacts/
```

## Recommended Brain Layout

```text
brain/
  project.md
  feature/
  task/
  risk/
  decision/
  knowledge/
  timeline/
  health/
```

## Recommended Artifact Layout

```text
artifacts/
  spec/
  adr/
  task/
  review/
  release/
  test/
```

## Initialization Rules

When initializing PBDD in an existing project:

1. Prefer `scripts/initialize_project.py <project-root>`.
2. Preserve existing files.
3. Add only missing required directories and files.
4. Create `AGENTS.md` so future agents know to use the PBDD Skill.
5. Avoid moving user source code.
6. Record assumptions in `brain/decision/` when initialization requires non-obvious choices.

## Repair Rules

When a PBDD project is partially initialized:

1. Preserve existing files.
2. Add only missing required directories and files.
3. Record assumptions in `brain/decision/`.
4. Avoid moving user project source code.
