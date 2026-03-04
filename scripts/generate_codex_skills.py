#!/usr/bin/env python3
"""Generate Codex-compatible skills from The Agency agent markdown files."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.S)
KEY_VALUE_RE = re.compile(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None

    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        kv = KEY_VALUE_RE.match(line.strip())
        if not kv:
            continue
        key, value = kv.group(1), kv.group(2).strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        frontmatter[key] = value

    body = text[match.end() :]
    return frontmatter, body.lstrip("\n")


def skill_slug(path: Path) -> str:
    slug = path.stem.lower()
    slug = re.sub(r"[^a-z0-9-]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def generate(root: Path, out_dir: Path) -> list[tuple[str, str, str]]:
    records: list[tuple[str, str, str]] = []

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for md in sorted(root.rglob("*.md")):
        if md.is_relative_to(out_dir):
            continue
        if md.parts[0] in {".git", "docs"}:
            continue

        parsed = parse_frontmatter(md.read_text(encoding="utf-8"))
        if not parsed:
            continue

        meta, body = parsed
        if "name" not in meta or "description" not in meta:
            continue

        slug = skill_slug(md)
        skill_dir = out_dir / slug
        skill_dir.mkdir(parents=True, exist_ok=True)

        skill_md = skill_dir / "SKILL.md"
        source_rel = md.relative_to(root).as_posix()
        content = (
            "---\n"
            f"name: {slug}\n"
            f"description: {meta['description']}\n"
            "---\n\n"
            f"# {meta['name']}\n\n"
            "This skill is adapted from The Agency and is intended for Codex skill workflows.\n"
            f"Source: `{source_rel}`\n\n"
            "## Agent Instructions\n\n"
            f"{body.rstrip()}\n"
        )
        skill_md.write_text(content, encoding="utf-8")
        records.append((slug, meta["name"], source_rel))

    index = out_dir / "README.md"
    lines = [
        "# Codex Skills for The Agency",
        "",
        "Generated skills compatible with Codex `SKILL.md` format.",
        "",
        "## Skills",
        "",
    ]
    for slug, name, source in records:
        lines.append(f"- `{slug}` -> **{name}** (`{source}`)")

    lines.extend(
        [
            "",
            "## Regenerate",
            "",
            "```bash",
            "python3 scripts/generate_codex_skills.py",
            "```",
            "",
        ]
    )
    index.write_text("\n".join(lines), encoding="utf-8")

    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Repository root",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("codex-skills"),
        help="Output directory relative to root",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    out_dir = (root / args.out_dir).resolve()
    records = generate(root, out_dir)
    print(f"Generated {len(records)} skills in {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
