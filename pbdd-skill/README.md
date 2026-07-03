# PBDD Skill

This project contains the PBDD Runtime for AI agents.

The runtime reads the PBDD specification, loads a project's `pbdd.yaml`, updates the project brain, executes workflow transitions, and maintains artifacts.

## Layout

```text
pbdd-skill/
  pbdd/
    SKILL.md
    agents/
    references/
    scripts/
    assets/
```

The `pbdd/` directory is the installable Codex skill package.

## Boundary

This project implements PBDD. It must not redefine PBDD.

Normative rules belong in `../pbdd-spec/`. Runtime-specific guidance, adapter behavior, prompts, scripts, and tests belong here.
