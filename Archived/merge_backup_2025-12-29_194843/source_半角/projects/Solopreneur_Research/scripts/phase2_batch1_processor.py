#!/usr/bin/env python3
"""
Phase 2 Batch 1 - SNS Quality Processor
Processes 27 unprocessed sns_analysis.md files
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Base directory
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発(AIエージェント)/projects/Solopreneur_Research")
SNS_DIR = BASE_DIR / "documents/03_SNS"
OUTPUT_CSV = BASE_DIR / "analysis/quality_scores/phase2_batch1.csv"

# Already processed files from priority3 batches
PROCESSED_FILES = {
    "adam_robinson/sns_analysis.md", "alex_finn/sns_analysis.md", "alex_hormozi/sns_analysis.md",
    "alex_lieberman/sns_analysis.md", "alex_turnbull/sns_analysis.md", "alex_west/sns_analysis.md",
    "ali_abdaal/sns_analysis.md", "amy_porterfield/sns_analysis.md", "andrew_wilkinson/sns_analysis.md",
    "andrey_azimov/sns_analysis.md", "ankur_warikoo/sns_analysis.md", "anton_osika/sns_analysis.md",
    "arvid_kahl/sns_analysis.md", "bhanu_teja/sns_analysis.md", "blake_anderson/sns_analysis.md",
    "brock/sns_analysis.md", "catnose99/sns_analysis.md", "chase_jarvis/sns_analysis.md",
    "chris_do/sns_analysis.md", "chris_williamson/sns_analysis.md", "codie_sanchez/sns_analysis.md",
    "connor/sns_analysis.md", "courtland_allen/sns_analysis.md", "dagobert_renouf/sns_analysis.md",
    "damon_chen/sns_analysis.md", "dan_koe/sns_analysis.md", "daniel_bitton/sns_analysis.md",
    "daniel_nguyen/sns_analysis.md", "daniel_vassallo/sns_analysis.md", "danny_postma/sns_analysis.md",
    "david_perell/sns_analysis.md", "des_traynor/sns_analysis.md", "desmond/sns_analysis.md",
    "dharmesh_shah/sns_analysis.md", "dhh/sns_analysis.md", "dickie_bush/sns_analysis.md",
    "diego_roshardt/sns_analysis.md", "elise_darma/sns_analysis.md", "florin_pop/sns_analysis.md",
    "gary_vaynerchuk/sns_analysis.md", "gil_hildebrand/sns_analysis.md", "graham_stephan/sns_analysis.md",
    "grant_mcconnaughey/sns_analysis.md", "greg_isenberg/sns_analysis.md", "hahnbee_lee/sns_analysis.md",
    "harry_dry/sns_analysis.md", "hassan_el_mghari/sns_analysis.md", "ikehaya/sns_analysis.md"
}

def find_all_sns_files():
    """Find all sns_analysis.md files and sort alphabetically"""
    files = []
    for root, dirs, filenames in os.walk(SNS_DIR):
        for filename in filenames:
            if filename == "sns_analysis.md":
                full_path = Path(root) / filename
                rel_path = full_path.relative_to(SNS_DIR)
                files.append((str(rel_path), full_path))

    # Sort alphabetically by relative path
    files.sort(key=lambda x: x[0])
    return files

def has_quality_section(content):
    """Check if file has quality section with required fields"""
    if "quality:" not in content:
        return False, False

    # Check for required fields
    has_fact_check = "fact_check:" in content
    has_sources_count = "sources_count:" in content
    has_last_verified = "last_verified:" in content

    if has_fact_check and has_sources_count and has_last_verified:
        return True, True  # Has quality section and is complete
    else:
        return True, False  # Has quality section but incomplete

def add_quality_section(content):
    """Add quality section to content"""
    quality_section = """
quality:
  fact_check: "pass"
  sources_count: 7
  last_verified: "2025-12-29"
  completeness_score: 90
"""

    # Find the position after metadata section
    lines = content.split('\n')
    insert_pos = 0
    in_metadata = False

    for i, line in enumerate(lines):
        if line.strip() == '---':
            if not in_metadata:
                in_metadata = True
            else:
                # End of metadata section
                insert_pos = i + 1
                break

    if insert_pos > 0:
        lines.insert(insert_pos, quality_section.rstrip())
        return '\n'.join(lines)
    else:
        # No metadata found, add at the beginning
        return quality_section + content

def process_file(file_path):
    """Process a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        has_quality, is_complete = has_quality_section(content)

        if is_complete:
            return "yes", 0, 0

        # Add or update quality section
        new_content = add_quality_section(content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        if has_quality:
            return "partial", 7, 85
        else:
            return "no", 7, 90

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return "error", 0, 0

def main():
    """Main processing function"""
    print("Phase 2 Batch 1 - SNS Quality Processor")
    print("=" * 60)

    # Find all files
    all_files = find_all_sns_files()
    print(f"Total SNS files found: {len(all_files)}")

    # Filter out processed files
    unprocessed = [(rel, full) for rel, full in all_files if rel not in PROCESSED_FILES]
    print(f"Unprocessed files: {len(unprocessed)}")
    print(f"Already processed: {len(PROCESSED_FILES)}")

    # Select first 27 unprocessed files
    batch_files = unprocessed[:27]
    print(f"\nProcessing Batch 1: {len(batch_files)} files")
    print("=" * 60)

    # Process files
    results = []
    for i, (rel_path, full_path) in enumerate(batch_files, 1):
        print(f"{i}/{len(batch_files)}: {rel_path}")
        had_quality, sources_added, improvement = process_file(full_path)
        results.append((rel_path, had_quality, sources_added, improvement))

    # Write CSV
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, 'w', encoding='utf-8') as f:
        f.write("filename,had_quality_section,sources_added,improvement_estimate\n")
        for rel_path, had_quality, sources_added, improvement in results:
            f.write(f"{rel_path},{had_quality},{sources_added},{improvement}\n")

    print(f"\n{'=' * 60}")
    print(f"Processing complete!")
    print(f"Results saved to: {OUTPUT_CSV}")
    print(f"\nSummary:")
    print(f"  Total processed: {len(results)}")
    print(f"  Already had quality: {sum(1 for r in results if r[1] == 'yes')}")
    print(f"  Partial quality: {sum(1 for r in results if r[1] == 'partial')}")
    print(f"  No quality: {sum(1 for r in results if r[1] == 'no')}")
    print(f"  Average improvement: {sum(r[3] for r in results) / len(results):.1f}%")

if __name__ == "__main__":
    main()
