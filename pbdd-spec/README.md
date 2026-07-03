# PBDD Specification

PBDD is an open specification for maintaining project state, workflows, and
engineering artifacts across AI agents.

PBDD is not a code framework. It defines a protocol, project conventions, state
schemas, workflow state machines, and artifact contracts.

## Scope

This project defines:

- Project manifest: `pbdd.yaml`
- Event protocol
- Brain data model
- Workflow lifecycle definitions
- Artifact contracts
- Conformance rules

This project does not define:

- Agent prompts
- IDE integrations
- Runtime implementation details
- Business application code

## Layout

```text
pbdd-spec/
  protocol/
    events/
    lifecycle/
    workflow/
    artifact/
  schemas/
  workflow/
  templates/
  examples/
  docs/
```

## Draft Version

Current draft: `0.1.0`.

The schema files are the normative source. Markdown documents explain intent,
terms, and usage.

