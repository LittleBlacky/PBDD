# PBDD

[中文](README.md) | English

**PBDD (Project Brain Driven Development) is an open specification for helping AI agents maintain project state, execute engineering workflows, and produce durable engineering artifacts through a shared protocol.**

PBDD is not a code framework. It is closer to Kubernetes, Dockerfile, OpenAPI, or MCP: it defines protocols, states, conventions, and artifact boundaries that different runtimes and agents can implement.

## Positioning

PBDD consists of four core parts:

```text
PBDD
  ├── Protocol   # Events, lifecycles, workflows, artifact contracts
  ├── Brain      # Project state database
  ├── Workflow   # Engineering process and state transitions
  └── Artifacts  # Specs, ADRs, tasks, reviews, releases, and more
```

In short:

```text
Event -> Brain -> Workflow -> Artifacts
```

A user expresses intent. A runtime interprets it as an event. The event drives workflow transitions. The Brain records project state. Artifacts hold durable engineering output.

## Why It Is Not a Framework

Traditional frameworks usually bind application structure, runtime dependencies, and extension points together. PBDD does not.

PBDD defines:

- Project manifest: `pbdd.yaml`
- Project state model: Brain
- Event protocol
- Lifecycle protocol
- Workflow state machines
- Engineering artifact contracts
- Project directory conventions

PBDD does not define:

- Agent prompts
- IDE plugin behavior
- Business application structure
- A specific programming language or framework
- Vendor-specific AI platform features

## Repository Layout

This workspace is split into three independently maintainable projects:

```text
PBDD/
  ├── pbdd-spec/      # Specification: source of truth
  ├── pbdd-skill/     # Runtime: agent implementation
  └── pbdd-starter/   # Starter: project template
```

### `pbdd-spec/`

The source of truth for the PBDD specification.

It defines:

- Event types
- Brain data model
- Workflow lifecycles
- Artifact schemas
- Project manifest: `pbdd.yaml`
- Conformance rules

The specification should be machine-readable first. `schemas/` and `workflow/` are normative. Markdown documents explain intent and usage.

### `pbdd-skill/`

The PBDD Agent Runtime implementation.

It is responsible for:

- Reading `pbdd.yaml`
- Loading the PBDD Spec
- Reading and maintaining the Brain
- Executing Workflow state transitions
- Creating or updating Artifacts
- Providing adapters for different agents or IDEs

A runtime may contain prompts, scripts, adapters, and tests, but it must not redefine the specification.

### `pbdd-starter/`

A PBDD project template.

It contains the minimal structure a real project needs:

```text
project/
  pbdd.yaml
  brain/
  artifacts/
  src/
  tests/
```

The starter is a consumer of the specification. It must not contain protocol or workflow definitions.

## Dependency Direction

```text
pbdd-spec
  -> pbdd-skill
  -> pbdd-starter
  -> user project
```

The dependency direction must not be reversed.

- The Spec does not depend on the Skill.
- The Skill implements the Spec.
- The Starter consumes the Spec and Skill.
- User projects copy the Starter and grow their own Brain and Artifacts.

## What Is the Brain?

The Brain is project state, not ordinary documentation.

Recommended layout:

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

Example:

```text
Feature: Coupon
Status: Implementing
Owner: Agent
Progress: 60%
Tasks: TASK-22, TASK-23
```

Markdown is only the current storage format. Semantically, the Brain is the Project Database.

## What Is a Workflow?

A Workflow is a state transition system, not a prompt.

Example Feature lifecycle:

```text
Draft -> Planning -> Implementing -> Testing -> Done
```

All agents should follow the same state machine. A runtime reads workflow definitions and applies valid transitions.

## What Are Artifacts?

Artifacts are engineering outputs, not Brain state.

Common artifacts include:

- Spec
- ADR
- Task
- Review
- Release note
- Knowledge note
- Test evidence
- Code

The Brain records current state and indexes. Artifacts preserve reviewable, deliverable, and traceable engineering content.

## Quick Start

Copy the starter:

```powershell
Copy-Item -Recurse pbdd-starter my-project
```

Enter the project:

```powershell
Set-Location my-project
```

Edit:

```text
pbdd.yaml
brain/project.md
```

Then ask a PBDD-capable agent runtime to read the project:

```text
Use PBDD to inspect the project manifest, update brain state, run the appropriate workflow, and maintain engineering artifacts.
```

## Current Version

Current specification draft:

```text
0.1.0
```

Current status:

- `pbdd-spec/`: initial specification draft
- `pbdd-skill/`: initial Codex Skill runtime
- `pbdd-starter/`: minimal project template

## Commit Convention

This repository uses Conventional Commits.

Common types:

- `feat`: new capability
- `fix`: bug fix
- `docs`: documentation update
- `refactor`: behavior-preserving restructure
- `chore`: repository maintenance, configuration, housekeeping
- `test`: test changes
- `ci`: automation and CI configuration

See [docs/commit-convention.md](docs/commit-convention.md) for details.

## Design Principles

- The Spec is the source of truth, the Runtime is the implementation, and the Project is the consumer.
- Machine-readable rules come first; Markdown explains them.
- The Brain maintains state; Artifacts hold deliverables.
- Prompts are not part of the core protocol.
- PBDD is not bound to any agent, IDE, language, or platform.

## License

No license has been declared yet.
