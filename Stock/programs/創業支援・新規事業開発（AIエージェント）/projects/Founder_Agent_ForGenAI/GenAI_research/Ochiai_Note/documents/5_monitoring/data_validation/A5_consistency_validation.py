#!/usr/bin/env python3
"""
A5 Consistency Validation Agent
JSON-Markdown-画像の対応関係と整合性の検証
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set
import yaml

# Base paths
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note/full_run")
ARTICLES_DIR = BASE_DIR / "articles"
IMAGES_DIR = BASE_DIR / "images"
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31")


def load_json_files() -> Dict[str, dict]:
    """Load all JSON files and return a dict keyed by file_stem"""
    json_data = {}
    json_files = list(ARTICLES_DIR.glob("*.json"))
    print(f"Found {len(json_files)} JSON files")

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                file_stem = data.get('file_stem', json_file.stem)
                json_data[file_stem] = {
                    'path': str(json_file),
                    'image_paths': data.get('image_paths', []),
                    'data': data
                }
        except Exception as e:
            print(f"Error reading JSON {json_file}: {e}")

    return json_data


def load_markdown_files() -> Dict[str, dict]:
    """Load all Markdown files and return a dict keyed by file_stem"""
    md_data = {}
    md_files = list(ARTICLES_DIR.glob("*.md"))
    print(f"Found {len(md_files)} Markdown files")

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Count image links in markdown: ![...](...) pattern
                image_links = re.findall(r'!\[.*?\]\((.*?)\)', content)
                md_data[md_file.stem] = {
                    'path': str(md_file),
                    'image_count': len(image_links),
                    'image_links': image_links
                }
        except Exception as e:
            print(f"Error reading Markdown {md_file}: {e}")

    return md_data


def get_image_directories() -> Dict[str, dict]:
    """Get all image directories and count files in each"""
    img_dirs = {}

    if not IMAGES_DIR.exists():
        print(f"Warning: Images directory not found: {IMAGES_DIR}")
        return img_dirs

    for img_dir in IMAGES_DIR.iterdir():
        if img_dir.is_dir():
            # Count image files (jpg, png, gif, webp, etc.)
            image_files = []
            for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.webp', '*.svg']:
                image_files.extend(list(img_dir.glob(ext)))

            img_dirs[img_dir.name] = {
                'path': str(img_dir),
                'count': len(image_files),
                'files': [f.name for f in sorted(image_files)]
            }

    print(f"Found {len(img_dirs)} image directories")
    return img_dirs


def validate_consistency(json_data: Dict, md_data: Dict, img_dirs: Dict) -> Dict:
    """Validate consistency between JSON, Markdown, and images"""

    # Get all unique file_stems
    all_stems = set(json_data.keys()) | set(md_data.keys()) | set(img_dirs.keys())

    results = {
        'agent': 'A5_Consistency_Validation',
        'total_articles': len(all_stems),
        'consistent_articles': 0,
        'inconsistencies': {
            'missing_markdown': [],
            'missing_json': [],
            'missing_images': [],
            'image_count_mismatch': [],
            'orphaned_json': [],
            'orphaned_markdown': [],
            'orphaned_images': []
        }
    }

    for stem in sorted(all_stems):
        has_json = stem in json_data
        has_md = stem in md_data
        has_img_dir = stem in img_dirs

        json_image_count = len(json_data[stem]['image_paths']) if has_json else 0
        md_image_count = md_data[stem]['image_count'] if has_md else 0
        actual_image_count = img_dirs[stem]['count'] if has_img_dir else 0

        is_consistent = True

        # Case 1: JSON exists but Markdown missing
        if has_json and not has_md:
            is_consistent = False
            results['inconsistencies']['missing_markdown'].append({
                'file_stem': stem,
                'json_exists': True,
                'markdown_exists': False,
                'image_dir_exists': has_img_dir,
                'json_image_count': json_image_count,
                'actual_image_count': actual_image_count
            })

        # Case 2: Markdown exists but JSON missing
        if has_md and not has_json:
            is_consistent = False
            results['inconsistencies']['missing_json'].append({
                'file_stem': stem,
                'json_exists': False,
                'markdown_exists': True,
                'image_dir_exists': has_img_dir,
                'markdown_image_count': md_image_count,
                'actual_image_count': actual_image_count
            })

        # Case 3: JSON or Markdown exists but image directory missing
        if (has_json or has_md) and not has_img_dir and (json_image_count > 0 or md_image_count > 0):
            is_consistent = False
            results['inconsistencies']['missing_images'].append({
                'file_stem': stem,
                'json_exists': has_json,
                'markdown_exists': has_md,
                'image_dir_exists': False,
                'json_image_count': json_image_count,
                'markdown_image_count': md_image_count,
                'actual_image_count': 0
            })

        # Case 4: Image count mismatch
        if has_json and has_img_dir:
            if json_image_count != actual_image_count:
                is_consistent = False
                # Find missing images
                json_image_names = [Path(p).name for p in json_data[stem]['image_paths']]
                actual_image_names = img_dirs[stem]['files']
                missing_in_dir = [img for img in json_image_names if img not in actual_image_names]
                extra_in_dir = [img for img in actual_image_names if img not in json_image_names]

                results['inconsistencies']['image_count_mismatch'].append({
                    'file_stem': stem,
                    'json_image_count': json_image_count,
                    'actual_image_count': actual_image_count,
                    'difference': actual_image_count - json_image_count,
                    'missing_in_directory': missing_in_dir,
                    'extra_in_directory': extra_in_dir
                })

        # Case 5: Orphaned JSON (JSON exists but no MD and no images)
        if has_json and not has_md and not has_img_dir:
            is_consistent = False
            results['inconsistencies']['orphaned_json'].append({
                'file_stem': stem,
                'json_exists': True,
                'markdown_exists': False,
                'image_dir_exists': False,
                'json_image_count': json_image_count
            })

        # Case 6: Orphaned Markdown (MD exists but no JSON and no images)
        if has_md and not has_json and not has_img_dir:
            is_consistent = False
            results['inconsistencies']['orphaned_markdown'].append({
                'file_stem': stem,
                'json_exists': False,
                'markdown_exists': True,
                'image_dir_exists': False,
                'markdown_image_count': md_image_count
            })

        # Case 7: Orphaned images (images exist but no JSON and no MD)
        if has_img_dir and not has_json and not has_md:
            is_consistent = False
            results['inconsistencies']['orphaned_images'].append({
                'file_stem': stem,
                'json_exists': False,
                'markdown_exists': False,
                'image_dir_exists': True,
                'actual_image_count': actual_image_count
            })

        if is_consistent:
            results['consistent_articles'] += 1

    # Calculate summary statistics
    results['consistency_rate'] = f"{(results['consistent_articles'] / results['total_articles'] * 100):.2f}%" if results['total_articles'] > 0 else "0%"
    results['total_inconsistencies'] = sum(len(v) for v in results['inconsistencies'].values())

    # Add detailed counts
    results['inconsistency_counts'] = {
        'missing_markdown': len(results['inconsistencies']['missing_markdown']),
        'missing_json': len(results['inconsistencies']['missing_json']),
        'missing_images': len(results['inconsistencies']['missing_images']),
        'image_count_mismatch': len(results['inconsistencies']['image_count_mismatch']),
        'orphaned_json': len(results['inconsistencies']['orphaned_json']),
        'orphaned_markdown': len(results['inconsistencies']['orphaned_markdown']),
        'orphaned_images': len(results['inconsistencies']['orphaned_images'])
    }

    return results


def main():
    """Main execution"""
    print("=" * 80)
    print("A5 Consistency Validation Agent")
    print("JSON-Markdown-画像の対応関係と整合性の検証")
    print("=" * 80)
    print()

    # Load data
    print("Step 1: Loading JSON files...")
    json_data = load_json_files()

    print("\nStep 2: Loading Markdown files...")
    md_data = load_markdown_files()

    print("\nStep 3: Scanning image directories...")
    img_dirs = get_image_directories()

    # Validate consistency
    print("\nStep 4: Validating consistency...")
    results = validate_consistency(json_data, md_data, img_dirs)

    # Save results
    output_file = OUTPUT_DIR / "A5_consistency_validation_result.yaml"
    print(f"\nStep 5: Saving results to {output_file}")

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(results, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    # Print summary
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print(f"Total articles: {results['total_articles']}")
    print(f"Consistent articles: {results['consistent_articles']}")
    print(f"Consistency rate: {results['consistency_rate']}")
    print(f"Total inconsistencies: {results['total_inconsistencies']}")
    print()
    print("Inconsistency breakdown:")
    for key, count in results['inconsistency_counts'].items():
        if count > 0:
            print(f"  - {key}: {count}")
    print("=" * 80)
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
