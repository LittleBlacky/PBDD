# Brain Maintenance

Use this reference whenever modifying `brain/`.

## Brain Rule

The brain is project state. Keep it short, structured, current, and evidence
linked.

## Project

`brain/project.md` stores durable identity:

- Name
- Purpose
- Current focus
- Architecture summary
- Active constraints

Only write facts that can be inferred from the user, code, artifacts, or
existing brain state.

## Features

Use `brain/feature/<feature-id>.md` for feature state.

Recommended shape:

```text
# Feature: <title>

Status: Draft | Planning | Implementing | Testing | Done | Canceled
Owner: Agent | Human | Mixed
Progress: 0-100

## Intent
...

## Tasks
- TASK-...

## Artifacts
- artifacts/spec/...

## Evidence
- ...
```

## Tasks

Use `brain/task/<task-id>.md` for actionable work.

Recommended shape:

```text
# Task: <title>

Status: Todo | Doing | Blocked | Done | Canceled
Feature: <feature-id>
Blocked: false

## Work
...

## Completion Evidence
- ...
```

## Decisions

Use `brain/decision/<decision-id>.md` for choices that affect future work.

Record:

- Context
- Decision
- Consequences
- Alternatives considered

## Risks

Use `brain/risk/<risk-id>.md` when uncertainty may affect delivery, security,
data, user behavior, or maintainability.

Record:

- Risk
- Impact
- Mitigation
- Owner
- Status

## Knowledge

Use `brain/knowledge/<topic>.md` for durable project facts an agent should not
rediscover.

Examples:

- Domain concepts
- Architecture conventions
- API contracts
- Testing strategy
- Deployment notes

## Timeline

Use `brain/timeline/` for notable project events, not every minor file change.

Record:

- Date or timestamp when available
- Event
- Linked feature/task/artifact
- Evidence

## Health

Update `brain/health/status.md` at the end of meaningful iterations.

Include:

- Current status
- Active work
- Known risks
- Test status
- Next recommended action

