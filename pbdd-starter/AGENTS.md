# Agent Instructions

This is a PBDD project.

Use the PBDD Skill as the runtime entry point for maintaining this project.

## Boot

When asked to boot or continue this project:

1. Read `pbdd.yaml`.
2. Load `brain/project.md` and `brain/health/status.md`.
3. Inspect current features, tasks, risks, decisions, knowledge, and timeline.
4. Inspect relevant artifacts.
5. Summarize current project state before changing code.

## Maintenance

For user requests:

1. Interpret the request as a PBDD event.
2. Update the Project Brain.
3. Run the appropriate workflow.
4. Create or update required artifacts.
5. Implement and test code changes when needed.
6. Record decisions, risks, progress, and completion evidence.

Users should state intent. The PBDD Skill should guide project maintenance.
