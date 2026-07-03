# Concepts

## Core Belief

AI shouldn't remember conversations. AI should remember projects.

PBDD makes project memory explicit, versionable, portable, and inspectable. The project stores its own identity, plans, tasks, decisions, risks, knowledge, timeline, and health so any conforming runtime can continue work without depending on private conversation history.

## Specification

The specification defines the rules. It is independent of runtime
implementations.

## Runtime

A runtime implements the specification for a specific agent environment.

## Brain

The brain is project state. Markdown, YAML, JSON, or a database can store it,
but the semantics are state, not prose.

## Workflow

A workflow is a state transition system.

## Artifact

An artifact is a durable engineering output created or maintained by a
workflow.

