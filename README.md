# PBDD Workspace

This workspace contains three independently maintained PBDD projects.

## Projects

- `pbdd-spec/`: the open specification. It defines protocols, schemas,
  workflows, artifact contracts, and project conventions.
- `pbdd-skill/`: the agent runtime implementation. It loads the spec,
  interprets project state, performs workflow transitions, and updates brain
  and artifact files.
- `pbdd-starter/`: the project template. It is a minimal application skeleton
  that consumes the PBDD specification through `pbdd.yaml`, `brain/`, and
  `artifacts/`.

## Maintenance Boundaries

`pbdd-spec` is the source of truth. It must stay independent of any specific
agent, IDE, prompt format, or implementation language.

`pbdd-skill` is an implementation. It may contain prompts, adapters, runtime
logic, commands, and tests, but it must not redefine the specification.

`pbdd-starter` is a consumer. It should remain small, copyable, and practical.
It should not contain protocol definitions or runtime internals.

## Dependency Direction

```text
pbdd-spec
  -> pbdd-skill
  -> pbdd-starter
  -> user project
```

The dependency direction should never be reversed.

