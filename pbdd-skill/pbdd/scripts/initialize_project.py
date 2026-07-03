#!/usr/bin/env python3
"""Initialize PBDD structure in an existing project."""

from __future__ import annotations

import argparse
from pathlib import Path


BRAIN_DIRS = [
    "feature",
    "task",
    "risk",
    "decision",
    "knowledge",
    "timeline",
    "health",
]

ARTIFACT_DIRS = [
    "spec",
    "adr",
    "task",
    "review",
    "release",
    "test",
]


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    return True


def touch_keep(path: Path) -> bool:
    path.mkdir(parents=True, exist_ok=True)
    keep = path / ".gitkeep"
    if keep.exists():
        return False
    keep.write_text("\n", encoding="utf-8")
    return True


def initialize(root: Path, name: str) -> list[str]:
    created: list[str] = []
    root.mkdir(parents=True, exist_ok=True)

    manifest = f"""pbdd:
  spec_version: 0.1.0
  runtime: pbdd-skill
  profile: initialized
project:
  name: {name}
  kind: application
  description: A project initialized with PBDD.
brain:
  path: brain
artifacts:
  path: artifacts
conventions:
  feature_id_prefix: FEAT
  task_id_prefix: TASK
  decision_id_prefix: ADR
"""
    if write_if_missing(root / "pbdd.yaml", manifest):
        created.append("pbdd.yaml")

    agents = """# Agent Instructions

This is a PBDD project.

Use the PBDD Skill as the runtime entry point for maintaining this project.

## Boot

1. Read `pbdd.yaml`.
2. Load `brain/project.md` and `brain/health/status.md`.
3. Inspect current features, tasks, risks, decisions, knowledge, and timeline.
4. Inspect relevant artifacts.
5. Summarize current project state before changing code.

## Maintenance

1. Interpret user requests as PBDD events.
2. Update the Project Brain.
3. Run the appropriate workflow.
4. Create or update required artifacts.
5. Implement and test code changes when needed.
6. Record decisions, risks, progress, and completion evidence.
"""
    if write_if_missing(root / "AGENTS.md", agents):
        created.append("AGENTS.md")

    project = f"""# Project

## Identity

Name: {name}

Kind: application

Status: Initialized

## Purpose

Not recorded yet.

## Current Focus

No active focus has been recorded.
"""
    if write_if_missing(root / "brain" / "project.md", project):
        created.append("brain/project.md")

    health = """# Health

## Status

Initialized

## Signals

- No features recorded.
- No active tasks recorded.
- No risks recorded.

## Last Updated

Not recorded.
"""
    if write_if_missing(root / "brain" / "health" / "status.md", health):
        created.append("brain/health/status.md")

    timeline = """# Timeline

Record project events here when they matter for future reasoning.
"""
    if write_if_missing(root / "brain" / "timeline" / "README.md", timeline):
        created.append("brain/timeline/README.md")

    for directory in BRAIN_DIRS:
        if touch_keep(root / "brain" / directory):
            created.append(f"brain/{directory}/.gitkeep")

    for directory in ARTIFACT_DIRS:
        if touch_keep(root / "artifacts" / directory):
            created.append(f"artifacts/{directory}/.gitkeep")

    return created


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize PBDD in a project.")
    parser.add_argument("root", nargs="?", default=".", help="Project root")
    parser.add_argument("--name", help="Project name; defaults to folder name")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    name = args.name or root.name
    created = initialize(root, name)

    print(f"root: {root}")
    if created:
        print("created:")
        for path in created:
            print(f"  {path}")
    else:
        print("created: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

