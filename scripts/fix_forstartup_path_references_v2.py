#!/usr/bin/env python3
"""
ForStartup Skills Path Reference Correction Script V2

Enhanced version to fix ALL path reference patterns, including:
- @skill-name/SKILL.md (without Japanese bracket)
- @FAILURE_XXX.md references
- @.claude/skills/_shared/ references
"""

import re
from pathlib import Path

# Project root
PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0")
SKILLS_DIR = PROJECT_ROOT / ".claude" / "skills" / "for_startup"
SHARED_DIR = PROJECT_ROOT / ".claude" / "skills" / "_shared"
FOUNDER_RESEARCH_DIR = PROJECT_ROOT / "Stock" / "programs" / "創業支援・新規事業開発（AIエージェント）" / "projects" / "Founder_Research"


def fix_all_patterns(content: str) -> tuple[str, dict]:
    """Fix all path reference patterns in content."""

    stats = {
        'skill_cross_ref': 0,
        'failure_ref': 0,
        'shared_ref': 0,
        'founder_research': 0
    }

    # Pattern 1: @skill-name/SKILL.md (both with and without Japanese bracket）
    def replace_skill_ref(match):
        skill_name = match.group(1)
        stats['skill_cross_ref'] += 1
        return str(SKILLS_DIR / skill_name / "SKILL.md")

    content = re.sub(r'@([a-z-]+)/SKILL\.md[）)]?', replace_skill_ref, content)

    # Pattern 2: @FAILURE_XXX.md references
    def replace_failure_ref(match):
        failure_file = match.group(1)
        stats['failure_ref'] += 1
        return str(FOUNDER_RESEARCH_DIR / "documents" / "07_Failure_Study" / failure_file)

    content = re.sub(r'@(FAILURE_\d+_\w+\.md)', replace_failure_ref, content)

    # Pattern 3: @.claude/skills/_shared/xxx.md references (already relative, make absolute)
    def replace_shared_ref(match):
        shared_file = match.group(1)
        stats['shared_ref'] += 1
        return str(SHARED_DIR / shared_file)

    # Don't replace if already absolute path
    content = re.sub(r'@\.claude/skills/_shared/([^\s#]+)(?=[^/])', replace_shared_ref, content)

    # Pattern 4: @Founder_Research/documents/ (already handled by previous script, but double-check)
    founder_research_count = content.count('@Founder_Research/documents/')
    if founder_research_count > 0:
        content = content.replace('@Founder_Research/documents/', f'{FOUNDER_RESEARCH_DIR}/documents/')
        stats['founder_research'] += founder_research_count

    return content, stats


def main():
    """Main execution function."""

    print("=" * 80)
    print("ForStartup Skills Path Reference Correction V2")
    print("=" * 80)
    print()

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    print(f"Found {len(skill_files)} SKILL.md files\n")

    total_stats = {
        'files_processed': 0,
        'skill_cross_ref': 0,
        'failure_ref': 0,
        'shared_ref': 0,
        'founder_research': 0
    }

    file_breakdown = []

    for skill_file in skill_files:
        original_content = skill_file.read_text(encoding='utf-8')
        new_content, stats = fix_all_patterns(original_content)

        total_replacements = sum(stats.values())

        if new_content != original_content:
            skill_file.write_text(new_content, encoding='utf-8')
            total_stats['files_processed'] += 1

            for key in stats:
                total_stats[key] += stats[key]

            if total_replacements > 0:
                file_breakdown.append({
                    'name': skill_file.parent.name,
                    'replacements': total_replacements,
                    'stats': stats
                })

                print(f"✓ {skill_file.parent.name:<30} {total_replacements:>3} replacements")

    print()
    print("=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"Files processed: {total_stats['files_processed']}/{len(skill_files)}")
    print(f"Total replacements: {sum(total_stats[k] for k in total_stats if k != 'files_processed')}")
    print()
    print("Replacement Statistics:")
    print(f"  Skill cross-references:     {total_stats['skill_cross_ref']:>4}")
    print(f"  Failure study references:   {total_stats['failure_ref']:>4}")
    print(f"  Shared skill references:    {total_stats['shared_ref']:>4}")
    print(f"  Founder_Research paths:     {total_stats['founder_research']:>4}")
    print()

    # Validation
    print("=" * 80)
    print("Validation")
    print("=" * 80)

    remaining_patterns = {
        'skill_refs': 0,
        'failure_refs': 0,
        'at_symbols': 0
    }

    for skill_file in skill_files:
        content = skill_file.read_text(encoding='utf-8')

        # Check for @skill-name/SKILL.md pattern
        if re.search(r'@[a-z-]+/SKILL\.md', content):
            remaining_patterns['skill_refs'] += 1
            print(f"⚠️  {skill_file.parent.name} has @skill-name/SKILL.md pattern")

        # Check for @FAILURE_XXX.md pattern
        if re.search(r'@FAILURE_\d+', content):
            remaining_patterns['failure_refs'] += 1
            print(f"⚠️  {skill_file.parent.name} has @FAILURE_XXX.md pattern")

        # Count all remaining @ symbols (excluding email addresses and anchors)
        at_count = len(re.findall(r'@(?![a-zA-Z0-9._%+-]+@|#)', content))
        remaining_patterns['at_symbols'] += at_count

    total_remaining = sum(remaining_patterns.values())

    if total_remaining == 0:
        print("✅ All path reference patterns fixed!")
    else:
        print(f"⚠️  {total_remaining} potential issues remain:")
        print(f"    - Skill refs: {remaining_patterns['skill_refs']}")
        print(f"    - Failure refs: {remaining_patterns['failure_refs']}")
        print(f"    - Other @ symbols: {remaining_patterns['at_symbols']}")

    print()


if __name__ == "__main__":
    main()
