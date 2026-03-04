# Codex Adaptation Guide

This repository is adapted for Codex by adding generated skills under `codex-skills/`.

## What Was Added

- `scripts/generate_codex_skills.py`: converts agent markdown files into Codex skills.
- `codex-skills/<skill-name>/SKILL.md`: Codex-compatible skills (55 generated).
- `codex-skills/README.md`: generated list of all available Codex skills.

## Regenerate Skills

Run from repo root:

```bash
python3 scripts/generate_codex_skills.py
```

## Install Skills Into Codex

Install one skill from upstream:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo msitarzewski/agency-agents \
  --path codex-skills/engineering-frontend-developer
```

Install multiple skills:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo msitarzewski/agency-agents \
  --path codex-skills/engineering-frontend-developer \
         codex-skills/testing-api-tester \
         codex-skills/marketing-growth-hacker
```

After installing skills, restart Codex so the new skills are detected.

## Install From Local Clone (No GitHub)

```bash
cp -R codex-skills/engineering-frontend-developer ~/.codex/skills/
```

For multiple skills, repeat `cp -R` for each directory under `codex-skills/`.

## Notes

- Skill directory names use file stem slugs (for example `engineering-frontend-developer`).
- The generated `SKILL.md` preserves the original agent instructions and source path.
- Re-running the generator replaces the full `codex-skills/` folder.
