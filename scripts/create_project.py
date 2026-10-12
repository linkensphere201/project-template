#!/usr/bin/env python3
"""Render a pinned template without copying repository metadata."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import date
from pathlib import Path

TOKEN = re.compile(r"\{\{([A-Z_]+)\}\}")
DOCUMENT_DIRS = ("context", "tasks", "prompts", "logs")


def slugify(value: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9-]", "-", value.lower())).strip("-")


def titleize(slug: str) -> str:
    return " ".join(p.upper() if p in {"ai", "api", "llm", "ui", "ux"} else p.capitalize()
                    for p in slug.split("-"))


def source_files(template: Path) -> dict[str, Path]:
    files = {"README.md": template / "PROJECT.md", "AGENTS.md": template / "AGENTS.md"}
    for directory in DOCUMENT_DIRS:
        folder = template / directory
        if not folder.is_dir() or folder.is_symlink():
            raise ValueError(f"Missing or linked template directory: {folder}")
        for source in folder.rglob("*.md"):
            if any(part.startswith(".") for part in source.relative_to(template).parts):
                continue
            if source.is_symlink() or not source.resolve().is_relative_to(template):
                raise ValueError(f"Template document must not escape its checkout: {source}")
            files[source.relative_to(template).as_posix()] = source
    for source in files.values():
        if not source.is_file() or source.is_symlink():
            raise ValueError(f"Missing or linked template document: {source}")
    return files


def render(text: str, values: dict[str, str]) -> str:
    def substitute(match):
        key = match.group(1)
        if key not in values:
            raise ValueError(f"Unknown template placeholder: {key}")
        return values[key]
    return TOKEN.sub(substitute, text).rstrip() + "\n"


def provenance(template: Path) -> dict:
    result = {"version": (template / "VERSION").read_text(encoding="utf-8").strip(),
              "commit": None, "dirty": None}
    # An exported ZIP must not inherit the enclosing workspace's Git identity.
    if not (template / ".git").exists():
        return result
    try:
        result["commit"] = subprocess.check_output(
            ["git", "-C", str(template), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
        result["dirty"] = bool(subprocess.check_output(
            ["git", "-C", str(template), "status", "--porcelain"], text=True, stderr=subprocess.DEVNULL).strip())
    except (OSError, subprocess.CalledProcessError):
        pass
    return result


def index_text(text: str, marker: str, entry: str) -> str:
    if entry in text.splitlines():
        return text
    lines = text.splitlines()
    index = next((i for i, line in enumerate(lines) if marker in line), len(lines))
    lines.insert(index, entry)
    return "\n".join(lines) + "\n"


def create_project(template: Path, root: Path, name: str, description: str,
                   goal: str | None, owner: str, day: str, update_indexes: bool = True) -> Path:
    template, root = template.resolve(), root.resolve()
    date.fromisoformat(day)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
        raise ValueError("Date must use YYYY-MM-DD")
    slug = slugify(name)
    if not slug:
        raise ValueError("Project name must contain ASCII letters or digits")
    if root == template or root.is_relative_to(template):
        raise ValueError("Output root must be outside the template checkout")
    directory = f"{day}-{slug}"
    target = root / directory
    if target.exists():
        raise ValueError(f"Refusing to overwrite existing project: {target}")
    values = dict(PROJECT_TITLE=titleize(slug), PROJECT_DIRECTORY=directory,
                  DESCRIPTION=description.strip() or "TODO", OWNER=owner, START_DATE=day,
                  ACTIVE_GOAL=goal or f"Define the minimum viable plan for {titleize(slug)}")
    rendered = {relative: render(path.read_text(encoding="utf-8-sig"), values)
                for relative, path in source_files(template).items()}
    rendered[".template-source.json"] = json.dumps(provenance(template), indent=2) + "\n"
    indexes = {}
    if update_indexes:
        for filename, marker, entry in [
            ("README.md", "`project-template/`", f"- `{directory}/`: {values['DESCRIPTION']}"),
            ("WORKSPACE-STRUCTURE.md", "| `project-template/` |", f"| `{directory}/` | {values['DESCRIPTION']} |"),
        ]:
            path = root / filename
            if path.is_symlink():
                raise ValueError(f"Refusing to update linked workspace index: {path}")
            if path.exists():
                indexes[path] = index_text(path.read_text(encoding="utf-8-sig"), marker, entry)
    root.mkdir(parents=True, exist_ok=True)
    target.mkdir(exist_ok=False)
    for relative, content in rendered.items():
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
    for path, content in indexes.items():
        path.write_text(content, encoding="utf-8", newline="\n")
    return target


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_name")
    parser.add_argument("--project-root", "--output-root", default=".")
    parser.add_argument("--template-dir", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--description", default="TODO")
    parser.add_argument("--goal")
    parser.add_argument("--owner", default="Project owner + AI assistant")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--no-index", action="store_true")
    args = parser.parse_args(argv)
    try:
        target = create_project(Path(args.template_dir), Path(args.project_root), args.project_name,
                                args.description, args.goal, args.owner, args.date, not args.no_index)
    except (ValueError, OSError) as error:
        parser.exit(2, f"error: {error}\n")
    print(f"created: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
