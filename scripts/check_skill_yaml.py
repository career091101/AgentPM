#!/usr/bin/env python3
import os
import re
from pathlib import Path

skills_dir = Path("/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup")

missing_fields = []

for skill_dir in sorted(skills_dir.iterdir()):
    if not skill_dir.is_dir():
        continue

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        continue

    content = skill_file.read_text()

    # Extract YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        print(f"{skill_dir.name}: NO YAML FRONTMATTER")
        continue

    yaml_content = yaml_match.group(1)

    # Check for required fields
    has_trigger = 'trigger_keywords:' in yaml_content
    has_stage = 'stage:' in yaml_content
    has_deps = 'dependencies:' in yaml_content
    has_output = 'output_file:' in yaml_content

    if not all([has_trigger, has_stage, has_deps, has_output]):
        missing = []
        if not has_trigger: missing.append('trigger_keywords')
        if not has_stage: missing.append('stage')
        if not has_deps: missing.append('dependencies')
        if not has_output: missing.append('output_file')

        missing_fields.append({
            'skill': skill_dir.name,
            'missing': missing
        })

print("\nSkills missing YAML fields:")
print("=" * 60)
for item in missing_fields:
    print(f"{item['skill']}: Missing {', '.join(item['missing'])}")

print(f"\nTotal skills with missing fields: {len(missing_fields)}/{len(list(skills_dir.iterdir()))}")
