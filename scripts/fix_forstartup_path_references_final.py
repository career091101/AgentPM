#!/usr/bin/env python3
"""
ForStartup Skills Path Reference Correction - Final Cleanup

Fixes remaining @startup_science/ and @for_startup/ references.
"""

import re
from pathlib import Path

# Project root
PROJECT_ROOT = Path("/Users/yuichi/AIPM/aipm_v0")
SKILLS_DIR = PROJECT_ROOT / ".claude" / "skills" / "for_startup"
SHARED_DIR = PROJECT_ROOT / ".claude" / "skills" / "_shared"
STARTUP_SCIENCE_DIR = PROJECT_ROOT / "Stock" / "programs" / "創業支援・新規事業開発（AIエージェント）" / "startup_science"


def fix_remaining_patterns(content: str) -> tuple[str, dict]:
    """Fix remaining @ patterns."""

    stats = {
        'startup_science': 0,
        'for_startup_analysis': 0,
        'removed_nonexistent': 0
    }

    # Pattern 1: @startup_science/ references (framework documentation)
    startup_science_count = content.count('@startup_science/')
    if startup_science_count > 0:
        # Note: These are documentation references, keep as relative for portability
        # But we can convert to full path if needed
        stats['startup_science'] += startup_science_count

    # Pattern 2: @for_startup/_analysis/ references (non-existent paths)
    # These files don't exist, so we'll remove or comment out these references
    def remove_nonexistent_line(match):
        stats['removed_nonexistent'] += 1
        return ""  # Remove the line entirely

    # Remove lines with non-existent @for_startup/_analysis/ references
    content = re.sub(r'^- @for_startup/_analysis/[^\n]+\n', remove_nonexistent_line, content, flags=re.MULTILINE)

    return content, stats


def main():
    """Main execution function."""

    print("=" * 80)
    print("ForStartup Skills Path Reference Correction - Final Cleanup")
    print("=" * 80)
    print()

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    print(f"Found {len(skill_files)} SKILL.md files\n")

    total_stats = {
        'files_processed': 0,
        'startup_science': 0,
        'for_startup_analysis': 0,
        'removed_nonexistent': 0
    }

    for skill_file in skill_files:
        original_content = skill_file.read_text(encoding='utf-8')
        new_content, stats = fix_remaining_patterns(original_content)

        total_changes = stats['removed_nonexistent']

        if new_content != original_content:
            skill_file.write_text(new_content, encoding='utf-8')
            total_stats['files_processed'] += 1

            for key in stats:
                total_stats[key] += stats[key]

            if total_changes > 0:
                print(f"✓ {skill_file.parent.name:<30} {total_changes:>3} non-existent refs removed")

    print()
    print("=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"Files processed: {total_stats['files_processed']}/{len(skill_files)}")
    print(f"Non-existent references removed: {total_stats['removed_nonexistent']}")
    print(f"startup_science refs (kept as-is): {total_stats['startup_science']}")
    print()

    # Final validation
    print("=" * 80)
    print("Final Validation")
    print("=" * 80)

    for skill_file in skill_files:
        content = skill_file.read_text(encoding='utf-8')

        # Check for non-existent @for_startup/_analysis/ references
        if '@for_startup/_analysis/' in content:
            print(f"⚠️  {skill_file.parent.name} still has @for_startup/_analysis/ reference")

    print("✅ Final cleanup complete!")


if __name__ == "__main__":
    main()
