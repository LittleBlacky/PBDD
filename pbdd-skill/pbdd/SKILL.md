---
name: pbdd
description: Maintain and initialize projects that use the PBDD specification. Use when Codex needs to initialize PBDD in an existing project, inspect or create pbdd.yaml, load or update brain state, run a PBDD workflow transition, create or update artifacts such as specs, ADRs, tasks, reviews, releases, or keep an AI-assisted project aligned with the PBDD protocol.
---

# PBDD Runtime

## Overview

Use this skill as a PBDD Runtime. PBDD is a specification; this skill is the implementation entry point that initializes project state, reads the spec, interprets user intent, and maintains brain and artifact files.

## User Model

Users do not maintain PBDD manually and do not need to copy the starter by hand.

A user enables this skill in an agent environment, opens an existing project, and asks the agent to initialize or boot PBDD. This skill then creates or reads the PBDD structure and teaches the agent how to maintain it.

## Initialize PBDD

When the user asks to initialize PBDD in a project:

1. Read `references/project-layout.md`.
2. Run `scripts/initialize_project.py <project-root>` or create the same structure manually if the script is unavailable.
3. Preserve existing files. Never overwrite an existing `pbdd.yaml`, `AGENTS.md`, `brain/`, or `artifacts/` file without explicit user approval.
4. Inspect the project source tree and update `brain/project.md` only with facts that can be inferred from local files.
5. Report what was created and what still needs user input.

## Boot PBDD

When the user asks to boot or continue a PBDD project:

1. Locate and read `pbdd.yaml`.
2. Read `brain/project.md` and `brain/health/status.md`.
3. Inspect active feature, task, risk, decision, knowledge, and timeline entries.
4. Inspect relevant artifacts.
5. Summarize the current project state before changing code.

If `pbdd.yaml` is missing and the user asked to use PBDD, initialize PBDD first.

## Runtime Rule

Do not invent local protocol rules when a PBDD spec file exists. Treat the nearest available `pbdd-spec/` project as the source of truth. If the spec is missing, continue conservatively and record assumptions in a decision artifact.

## Iteration Workflow

For any non-trivial project change:

1. Read `references/iteration-protocol.md`.
2. Read `references/event-handling.md` to classify the user request.
3. Read `references/workflow-execution.md` to choose and validate the lifecycle transition.
4. Read `references/brain-maintenance.md` before editing `brain/`.
5. Read `references/artifact-maintenance.md` before editing `artifacts/`.
6. Change source code and tests only after the relevant state and artifact plan is clear.
7. Read `references/done-criteria.md` before marking work done or sending the final iteration summary.

## Brain Maintenance

Treat `brain/` as project state, not as documentation. Keep entries short, structured, current, and linked to artifacts or evidence. Preserve existing user-authored content unless the request clearly supersedes it.

Expected brain areas:

- `project.md`
- `feature/`
- `task/`
- `risk/`
- `decision/`
- `knowledge/`
- `timeline/`
- `health/`

## Artifact Maintenance

Treat `artifacts/` as durable engineering output. Use templates from the spec when available.

Expected artifact areas:

- `spec/`
- `adr/`
- `task/`
- `review/`
- `release/`
- `test/`

## References

Use references by task:

- `references/project-layout.md`: initialize or repair PBDD structure.
- `references/runtime.md`: understand runtime responsibilities and boundaries.
- `references/iteration-protocol.md`: run a complete project iteration.
- `references/event-handling.md`: classify user intent as PBDD events.
- `references/workflow-execution.md`: apply lifecycle transitions.
- `references/brain-maintenance.md`: update project brain state.
- `references/artifact-maintenance.md`: create or update engineering artifacts.
- `references/done-criteria.md`: decide whether work is truly complete.

## Scripts

Use `scripts/initialize_project.py` to initialize PBDD in an existing project. Use `scripts/inspect_project.py` to summarize a PBDD project layout and identify missing required directories. Patch scripts here instead of rewriting repeated initialization or inspection logic in answers.
