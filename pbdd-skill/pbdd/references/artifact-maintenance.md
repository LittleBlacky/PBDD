# Artifact Maintenance

Use this reference whenever modifying `artifacts/`.

## Artifact Rule

Artifacts are durable engineering outputs. The brain indexes state; artifacts
carry the reasoning, plan, evidence, or deliverable.

## Spec

Use `artifacts/spec/<feature>.md` when defining behavior.

Include:

- Problem
- Goals
- Non-goals
- Proposal
- Impact
- Acceptance criteria

## ADR

Use `artifacts/adr/<decision>.md` for architectural or product decisions.

Include:

- Context
- Decision
- Consequences
- Alternatives

## Task

Use `artifacts/task/<task-id>.md` when a task needs more detail than the brain
summary.

Include:

- Scope
- Dependencies
- Implementation notes
- Completion evidence

## Review

Use `artifacts/review/<subject>.md` for code, design, or spec reviews.

Include findings first:

- Severity
- Location or artifact
- Risk
- Recommendation

## Test Evidence

Use `artifacts/test/<subject>.md` to record checks that matter for future
agents.

Include:

- Commands run
- Result
- Relevant output summary
- Untested areas

## Release

Use `artifacts/release/<version>.md` for shipping records.

Include:

- Scope
- Validation
- Risks
- Notes

## Linking Rule

Every artifact should be linked from the relevant brain entry. Every brain entry
that depends on evidence should link to an artifact, code change, test command,
or user decision.

