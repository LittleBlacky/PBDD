# Project Layout Reference

## Required Files

```text
project/
  pbdd.yaml
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

## Bootstrap Rules

When creating a new PBDD project:

1. Create `pbdd.yaml`.
2. Create required brain and artifact directories.
3. Add a project identity file.
4. Add a health file with initial unknown or draft status.
5. Avoid adding implementation-specific prompt files.

## Repair Rules

When a PBDD project is partially initialized:

1. Preserve existing files.
2. Add only missing required directories and files.
3. Record assumptions in `brain/decision/`.
4. Avoid moving user project source code.
