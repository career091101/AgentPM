#!/usr/bin/env python3
"""
Fix duplicate quality sections in files - Version 2
"""

import re
from pathlib import Path

BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Solopreneur_Research")
SNS_DIR = BASE_DIR / "documents/03_SNS"

# Files that were marked as "no" in the CSV (newly added quality sections)
files_to_check = [
    "case_studies/dharmesh_shah/sns_analysis.md",
    "case_studies/dhh/sns_analysis.md",
]

def clean_quality_sections(content):
    """Clean up quality sections - remove any loose quality fields and duplicates"""
    lines = content.split('\n')
    new_lines = []
    in_quality_block = False
    quality_found = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Start of quality block
        if line.strip() == 'quality:':
            if not quality_found:
                # Keep the first quality block
                quality_found = True
                in_quality_block = True
                new_lines.append(line)
            else:
                # Skip duplicate quality blocks
                in_quality_block = True
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    # Stop when we hit a non-indented line that isn't empty
                    if next_line and not next_line.startswith('  ') and not next_line.startswith('\t') and next_line.strip():
                        if not next_line.strip().startswith('---'):
                            i -= 1  # Back up to process this line normally
                        break
                    i += 1
                in_quality_block = False
        # Check for loose quality fields (not in a block)
        elif line.strip().startswith(('fact_check:', 'sources_count:', 'last_verified:', 'completeness_score:')):
            if not in_quality_block:
                # Skip loose quality fields
                pass
            else:
                # Keep fields that are part of the quality block
                new_lines.append(line)
        else:
            # End of quality block if we see a non-indented line
            if in_quality_block and line and not line.startswith('  ') and not line.startswith('\t'):
                in_quality_block = False

            new_lines.append(line)

        i += 1

    return '\n'.join(new_lines)

def main():
    print("Fixing duplicate quality sections - V2...")
    print("=" * 60)

    for file_path in files_to_check:
        full_path = SNS_DIR / file_path
        print(f"Processing: {file_path}")

        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = clean_quality_sections(content)

            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  ✓ Cleaned!")

        except Exception as e:
            print(f"  ✗ Error: {e}")

    print("=" * 60)
    print("Done!")

if __name__ == "__main__":
    main()
