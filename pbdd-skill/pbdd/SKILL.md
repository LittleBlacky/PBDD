---
name: pbdd
description: Maintain projects that use the PBDD specification. Use when Codex needs to inspect or create a PBDD project, read pbdd.yaml, load or update brain state, run a PBDD workflow transition, create or update artifacts such as specs, ADRs, tasks, reviews, releases, or keep an AI-assisted project aligned with the PBDD protocol.
---

# PBDD Runtime

## Overview

Use this skill as a PBDD Runtime. PBDD is a specification; this skill is only an implementation that reads the spec, interprets project state, and maintains brain and artifact files.

## Runtime Rule

Do not invent local protocol rules when a PBDD spec file exists. Treat the nearest available `pbdd-spec/` project as the source of truth. If the spec is missing, continue conservatively and record assumptions in a decision artifact.

## Project Detection

1. Locate `pbdd.yaml` in the workspace root or current project root.
2. Read `pbdd.yaml` and identify:
   - `pbdd.spec_version`
   - `brain.path`
   - `artifacts.path`
3. Locate the PBDD specification:
   - Prefer a sibling `pbdd-spec/` directory in this workspace.
   - Otherwise use the spec path declared by the project, if present.
   - Otherwise use the runtime references in this skill as fallback guidance.
4. Validate that the project has a brain directory and an artifacts directory.

## Workflow

For any project change:

1. Interpret the user request as a PBDD event.
2. Read the relevant brain files before editing.
3. Select the matching workflow definition from the spec.
4. Check whether the requested state transition is valid.
5. Update brain state.
6. Create or update required artifacts.
7. Record important decisions, risks, knowledge, or timeline entries.
8. Report the changed brain and artifact files.

## Brain Maintenance

Treat `brain/` as project state, not as documentation. Keep entries short, structured, and current. Preserve existing user-authored content unless the request clearly supersedes it.

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

Read `references/runtime.md` when implementing or changing runtime behavior. Read `references/project-layout.md` when bootstrapping or repairing a project.

## Scripts

Use `scripts/inspect_project.py` to summarize a PBDD project layout and identify missing required directories. Patch scripts here instead of rewriting repeated inspection logic in answers.
