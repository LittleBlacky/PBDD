#!/usr/bin/env python3
"""Inspect a PBDD project layout."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_BRAIN_DIRS = [
    "feature",
    "task",
    "risk",
    "decision",
    "knowledge",
    "timeline",
    "health",
]

REQUIRED_ARTIFACT_DIRS = [
    "spec",
    "adr",
    "task",
    "review",
    "release",
    "test",
]


def exists_label(path: Path) -> str:
    return "ok" if path.exists() else "missing"


def inspect(root: Path) -> int:
    manifest = root / "pbdd.yaml"
    brain = root / "brain"
    artifacts = root / "artifacts"

    print(f"root: {root}")
    print(f"manifest: {exists_label(manifest)} pbdd.yaml")
    print(f"brain: {exists_label(brain)} brain/")
    print(f"artifacts: {exists_label(artifacts)} artifacts/")

    if brain.exists():
        print("brain_dirs:")
        for name in REQUIRED_BRAIN_DIRS:
            print(f"  {exists_label(brain / name)} {name}/")

    if artifacts.exists():
        print("artifact_dirs:")
        for name in REQUIRED_ARTIFACT_DIRS:
            print(f"  {exists_label(artifacts / name)} {name}/")

    missing = [
        path
        for path in [manifest, brain, artifacts]
        if not path.exists()
    ]
    return 1 if missing else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a PBDD project.")
    parser.add_argument("root", nargs="?", default=".", help="Project root")
    args = parser.parse_args()
    return inspect(Path(args.root).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
