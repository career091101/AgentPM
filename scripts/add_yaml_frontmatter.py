#!/usr/bin/env python3
"""
Add YAML Front Matter to case study files
"""
import os
import re
from pathlib import Path

# 処理対象ファイル
FILES_TO_PROCESS = [
    "075_rox.md",
    "076_andrey_azimov.md",
    "077_yong_soo_chung.md",
    "079_arvid_kahl.md",
    "080_bhanu_teja.md",
    "083_pieter_levels_ai.md",
    "084_dmytro_krasun.md",
    "085_marc_lou_shipfast.md"
]

BASE_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies"

def extract_basic_info(content):
    """Extract basic information from markdown content"""
    info = {}

    # Extract title from first H1
    title_match = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
    if title_match:
        info['title'] = title_match.group(1).replace('Case Study: ', '').strip()

    # Extract revenue
    revenue_patterns = [
        r'[\$¥]([0-9,]+)[kKmM]?[/\/](?:月|month|mo)',
        r'月商.*?[\$¥]([0-9,]+)[kKmM]?',
        r'MRR.*?[\$¥]([0-9,]+)[kKmM]?',
    ]
    for pattern in revenue_patterns:
        revenue_match = re.search(pattern, content)
        if revenue_match:
            rev_str = revenue_match.group(1).replace(',', '')
            try:
                revenue = int(rev_str)
                if 'k' in revenue_match.group(0).lower() or 'K' in revenue_match.group(0):
                    revenue *= 1000
                if 'm' in revenue_match.group(0).lower() or 'M' in revenue_match.group(0):
                    revenue *= 1000000
                info['mrr_usd'] = revenue
                break
            except:
                pass

    # Extract product name
    product_patterns = [
        r'\*\*代表プロダクト\*\*[:\s]+(.+?)(?:\n|\|)',
        r'\*\*プロダクト名\*\*[:\s]+(.+?)(?:\n|\|)',
    ]
    for pattern in product_patterns:
        product_match = re.search(pattern, content)
        if product_match:
            info['main_product'] = product_match.group(1).strip()
            break

    # Extract founder name
    founder_patterns = [
        r'\*\*人物名\*\*[:\s]+(.+?)(?:\n|\|)',
        r'#\s+Case Study:\s+(.+?)(?:\(|$)',
    ]
    for pattern in founder_patterns:
        founder_match = re.search(pattern, content)
        if founder_match:
            info['founder'] = founder_match.group(1).strip()
            break

    return info

def generate_yaml_frontmatter(file_num, info):
    """Generate YAML Front Matter based on extracted info"""
    yaml = f"""---
id: "APP_{file_num}"
title: "{info.get('title', 'Unknown')}"
revenue:
  mrr_usd: {info.get('mrr_usd', 0)}
  arr_usd: {info.get('mrr_usd', 0) * 12 if 'mrr_usd' in info else 0}
  note: "要確認"
  mrr_tier: "要確認"
main_product:
  name: "{info.get('main_product', '要確認')}"
  url: "要確認"
  category: "要確認"
  description: "要確認"
tags:
  growth_strategy: []
  niche: []
  marketing_channel: []
  tech_stack: []
  business_model: []
  target_market: []
founder:
  name: "{info.get('founder', '要確認')}"
  nationality: "要確認"
  background: "要確認"
timeline_start: "要確認"
launch_date: "要確認"
japan_score:
  total: 0.0
  rating: "not_assessed"
  product_similarity: 0
  market_need: 0
  competition: 0
  localization: 0
  reproducibility: 0
  comment: "要確認"
quality:
  fact_check: "pending"
  sources: 0
  last_updated: "2025-12-28"
---

"""
    return yaml

def process_file(filename):
    """Process a single file"""
    filepath = os.path.join(BASE_DIR, filename)

    print(f"Processing: {filename}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already has YAML
        if content.startswith('---'):
            print(f"  ✓ Already has YAML Front Matter")
            return True

        # Extract file number
        file_num = filename.split('_')[0]

        # Extract basic info
        info = extract_basic_info(content)

        # Generate YAML
        yaml = generate_yaml_frontmatter(file_num, info)

        # Add YAML to content
        new_content = yaml + content

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✓ Added YAML Front Matter")
        print(f"    - Title: {info.get('title', 'N/A')}")
        print(f"    - Founder: {info.get('founder', 'N/A')}")
        print(f"    - MRR: ${info.get('mrr_usd', 'N/A')}")

        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("Adding YAML Front Matter to Case Study Files")
    print("=" * 60)
    print()

    success_count = 0
    for filename in FILES_TO_PROCESS:
        if process_file(filename):
            success_count += 1
        print()

    print("=" * 60)
    print(f"Completed: {success_count}/{len(FILES_TO_PROCESS)} files processed successfully")
    print("=" * 60)

if __name__ == "__main__":
    main()
