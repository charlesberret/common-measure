#!/usr/bin/env python3
"""Scan text files for patterns that should not appear in the public docs tree."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = REPO_ROOT / "tests" / "fixtures"

SKIP_DIR_NAMES = {".git", "__pycache__", ".venv", "node_modules"}
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".yml",
    ".yaml",
    ".json",
    ".cff",
    ".toml",
    ".html",
    ".css",
    ".sh",
}


@dataclass(frozen=True)
class Pattern:
    name: str
    regex: re.Pattern[str]


PATTERNS: tuple[Pattern, ...] = (
    Pattern(
        "warehouse_identifier",
        re.compile(
            r"\b(?=[a-z0-9_.]*_)"
            r"[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*\b",
        ),
    ),
    Pattern(
        "dollar_amount",
        re.compile(r"\$\d[\d,]*(?:\.\d{1,2})?\b"),
    ),
    Pattern(
        "long_digit_count",
        re.compile(r"\b\d{7,}\b"),
    ),
    Pattern(
        "absolute_home_path",
        re.compile(
            r"(?:^|(?<=\s))"
            r"(?:/(?:Users|home)/[a-zA-Z0-9._~/-]+|~(?:/[a-zA-Z0-9._-]+)+)"
        ),
    ),
    Pattern(
        "linear_issue_id",
        re.compile(r"\b(?!SHA-)[A-Z]{2,10}-\d{3,}\b"),
    ),
)


def under_fixtures(path: Path) -> bool:
    try:
        path.resolve().relative_to(FIXTURES_DIR.resolve())
        return True
    except ValueError:
        return False


def iter_files(root: Path, *, include_fixtures: bool) -> list[Path]:
    if root.is_file():
        if include_fixtures or not under_fixtures(root):
            return [root]
        return []

    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if not include_fixtures and under_fixtures(path):
            continue
        if path.suffix and path.suffix not in TEXT_SUFFIXES:
            if path.suffix not in {".cff"} and path.name not in {
                "LICENSE",
                "NOTICE",
                ".gitignore",
            }:
                continue
        files.append(path)
    return files


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    hits: list[tuple[int, str, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern in PATTERNS:
            for match in pattern.regex.finditer(line):
                text = match.group(0)
                if pattern.name == "absolute_home_path":
                    text = text.rstrip(".,;)")
                hits.append((lineno, pattern.name, text))
    return hits


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) > 1:
        print("usage: check_public.py [path]", file=sys.stderr)
        return 2

    if argv:
        root = Path(argv[0]).resolve()
        include_fixtures = under_fixtures(root) or root == FIXTURES_DIR.resolve()
    else:
        root = REPO_ROOT
        include_fixtures = False

    if not root.exists():
        print(f"error: path does not exist: {root}", file=sys.stderr)
        return 2

    all_hits: list[tuple[Path, int, str, str]] = []
    for file_path in iter_files(root, include_fixtures=include_fixtures):
        for lineno, kind, matched in scan_file(file_path):
            display = file_path
            try:
                display = file_path.resolve().relative_to(REPO_ROOT)
            except ValueError:
                pass
            all_hits.append((display, lineno, kind, matched))

    if not all_hits:
        return 0

    for path, lineno, kind, matched in all_hits:
        print(f"{path}:{lineno}: {kind}: {matched}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
