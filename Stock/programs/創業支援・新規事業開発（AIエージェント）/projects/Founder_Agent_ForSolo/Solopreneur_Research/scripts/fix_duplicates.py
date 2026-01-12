#!/usr/bin/env python3
"""
Fix duplicate quality sections in files
"""

import re
from pathlib import Path

BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research")
SNS_DIR = BASE_DIR / "documents/03_SNS"

# Files that were marked as "no" in the CSV (newly added quality sections)
files_to_check = [
    "case_studies/dharmesh_shah/sns_analysis.md",
    "case_studies/dhh/sns_analysis.md",
    "case_studies/dickie_bush/sns_analysis.md",
    "case_studies/elise_darma/sns_analysis.md",
    "case_studies/florin_pop/sns_analysis.md",
    "case_studies/gil_hildebrand/sns_analysis.md"
]

def remove_duplicate_quality(content):
    """Remove duplicate quality sections, keeping the first one"""
    lines = content.split('\n')
    quality_count = 0
    new_lines = []
    skip_mode = False
    skip_count = 0

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check if this is a quality section start
        if line.strip() == 'quality:':
            quality_count += 1

            if quality_count == 1:
                # Keep the first quality section
                new_lines.append(line)
                skip_mode = False
            else:
                # Skip subsequent quality sections
                skip_mode = True
                skip_count = 0
                # Skip until we find a non-indented line or empty line followed by ##
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    # If line starts with ## or is a markdown header, we're done skipping
                    if next_line.strip().startswith('##') or (not next_line.strip().startswith(' ') and not next_line.strip().startswith('-') and next_line.strip() and not next_line.strip().startswith('quality')):
                        break
                    i += 1
                i -= 1  # Back up one because we'll increment at the end of the loop
                skip_mode = False
        else:
            if not skip_mode:
                new_lines.append(line)

        i += 1

    return '\n'.join(new_lines)

def main():
    print("Fixing duplicate quality sections...")
    print("=" * 60)

    for file_path in files_to_check:
        full_path = SNS_DIR / file_path
        print(f"Checking: {file_path}")

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Count quality sections
            quality_count = content.count('\nquality:') + (1 if content.startswith('quality:') else 0)

            if quality_count > 1:
                print(f"  Found {quality_count} quality sections - fixing...")
                new_content = remove_duplicate_quality(content)

                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f"  ✓ Fixed!")
            else:
                print(f"  ✓ OK (only 1 quality section)")

        except Exception as e:
            print(f"  ✗ Error: {e}")

    print("=" * 60)
    print("Done!")

if __name__ == "__main__":
    main()
