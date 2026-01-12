#!/usr/bin/env python3
"""
ForStartup Skills Path Reference Correction Script

This script fixes 629 broken path references in all 30 ForStartup SKILL.md files.

Root Cause:
- Current: @validate-pmf/SKILL.md） (incorrect relative path with Japanese bracket)
- Correct: /Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/validate-pmf/SKILL.md (absolute path)
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

# Project root
PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0")
SKILLS_DIR = PROJECT_ROOT / ".claude" / "skills" / "for_startup"
SHARED_DIR = PROJECT_ROOT / ".claude" / "skills" / "_shared"
FOUNDER_RESEARCH_DIR = PROJECT_ROOT / "Stock" / "programs" / "創業支援・新規事業開発（AIエージェント）" / "projects" / "Founder_Research"

# Replacement patterns
REPLACEMENT_PATTERNS = [
    # Pattern 1: Skill cross-references with Japanese bracket
    (
        r'@([a-z-]+)/SKILL\.md[）)]',
        lambda m: f'{SKILLS_DIR / m.group(1) / "SKILL.md"}'
    ),
    # Pattern 2: Knowledge base references (relative to absolute)
    (
        r'@\.claude/skills/_shared/knowledge_base\.md',
        str(SHARED_DIR / "knowledge_base.md")
    ),
    # Pattern 3: Case reference for startup
    (
        r'@\.claude/skills/_shared/case_reference_for_startup\.md',
        str(SHARED_DIR / "case_reference_for_startup.md")
    ),
    # Pattern 4: Founder_Research documents (relative to absolute)
    (
        r'@Founder_Research/documents/',
        f'{FOUNDER_RESEARCH_DIR}/documents/'
    ),
]

# Non-existent files to remove (these don't exist in the project)
NONEXISTENT_PATTERNS = [
    r'@\.claude/skills/_shared/research_knowledge\.md',
    r'@\.claude/skills/_shared/domain_requirements\.md',
    r'@\.claude/skills/_shared/skill_templates\.md',
]


def fix_skill_file(skill_path: Path) -> Dict[str, int]:
    """Fix path references in a single SKILL.md file."""

    content = skill_path.read_text(encoding='utf-8')
    original_content = content

    stats = {
        'skill_cross_ref': 0,
        'knowledge_base': 0,
        'case_reference': 0,
        'founder_research': 0,
        'nonexistent_removed': 0
    }

    # Apply replacement patterns
    for pattern, replacement in REPLACEMENT_PATTERNS:
        if callable(replacement):
            # Pattern with lambda function
            matches = list(re.finditer(pattern, content))
            for match in reversed(matches):  # Reverse to preserve positions
                old_text = match.group(0)
                new_text = replacement(match)
                content = content[:match.start()] + new_text + content[match.end():]

                if 'SKILL.md' in old_text:
                    stats['skill_cross_ref'] += 1
        else:
            # Simple string replacement
            count = content.count(pattern)
            content = content.replace(pattern, replacement)

            if 'knowledge_base' in pattern:
                stats['knowledge_base'] += count
            elif 'case_reference' in pattern:
                stats['case_reference'] += count
            elif 'Founder_Research' in pattern:
                stats['founder_research'] += count

    # Remove non-existent file references
    for pattern in NONEXISTENT_PATTERNS:
        matches = list(re.finditer(pattern, content))
        for match in reversed(matches):
            # Remove the entire line containing the non-existent reference
            line_start = content.rfind('\n', 0, match.start()) + 1
            line_end = content.find('\n', match.end())
            if line_end == -1:
                line_end = len(content)

            content = content[:line_start] + content[line_end+1:]
            stats['nonexistent_removed'] += 1

    # Write back if changed
    if content != original_content:
        skill_path.write_text(content, encoding='utf-8')

    return stats


def main():
    """Main execution function."""

    print("=" * 80)
    print("ForStartup Skills Path Reference Correction")
    print("=" * 80)
    print()

    # Find all SKILL.md files
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))

    if not skill_files:
        print("❌ No SKILL.md files found in", SKILLS_DIR)
        return

    print(f"Found {len(skill_files)} SKILL.md files\n")

    # Process each file
    total_stats = {
        'files_processed': 0,
        'skill_cross_ref': 0,
        'knowledge_base': 0,
        'case_reference': 0,
        'founder_research': 0,
        'nonexistent_removed': 0
    }

    file_breakdown = []

    for skill_file in skill_files:
        stats = fix_skill_file(skill_file)
        total_replacements = sum(stats.values())

        if total_replacements > 0:
            total_stats['files_processed'] += 1
            for key in stats:
                total_stats[key] += stats[key]

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
    print(f"  Knowledge base paths:       {total_stats['knowledge_base']:>4}")
    print(f"  Case reference paths:       {total_stats['case_reference']:>4}")
    print(f"  Founder_Research paths:     {total_stats['founder_research']:>4}")
    print(f"  Non-existent files removed: {total_stats['nonexistent_removed']:>4}")
    print()

    # Validation
    print("=" * 80)
    print("Validation")
    print("=" * 80)

    # Check for remaining broken patterns
    remaining_broken = 0
    for skill_file in skill_files:
        content = skill_file.read_text(encoding='utf-8')

        # Check for Japanese bracket pattern
        if re.search(r'@[a-z-]+/SKILL\.md[）)]', content):
            remaining_broken += 1
            print(f"⚠️  {skill_file.parent.name} still has broken patterns")

    if remaining_broken == 0:
        print("✅ All broken path patterns fixed!")
    else:
        print(f"❌ {remaining_broken} files still have broken patterns")

    print()
    print("=" * 80)
    print("File-by-File Breakdown")
    print("=" * 80)

    for item in file_breakdown:
        print(f"\n{item['name']}:")
        print(f"  Total: {item['replacements']}")
        if item['stats']['skill_cross_ref'] > 0:
            print(f"  - Skill cross-refs: {item['stats']['skill_cross_ref']}")
        if item['stats']['knowledge_base'] > 0:
            print(f"  - Knowledge base: {item['stats']['knowledge_base']}")
        if item['stats']['case_reference'] > 0:
            print(f"  - Case reference: {item['stats']['case_reference']}")
        if item['stats']['founder_research'] > 0:
            print(f"  - Founder_Research: {item['stats']['founder_research']}")
        if item['stats']['nonexistent_removed'] > 0:
            print(f"  - Non-existent removed: {item['stats']['nonexistent_removed']}")


if __name__ == "__main__":
    main()
