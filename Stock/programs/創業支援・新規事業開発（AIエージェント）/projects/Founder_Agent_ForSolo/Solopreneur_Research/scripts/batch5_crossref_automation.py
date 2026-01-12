#!/usr/bin/env python3
"""
Batch 5 SNS Cross-Reference Automation
B/C-grade後半34件のcross_reference実装（Priority 3-B）
"""

import os
import re
import csv
from pathlib import Path
from typing import Dict, List, Tuple

# Base paths
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research")
SNS_DIR = BASE_DIR / "documents/03_SNS"
NEWSLETTER_DIR = BASE_DIR / "documents/02_Newsletter"
APP_DIR = BASE_DIR / "documents/01_App"
OUTPUT_CSV = BASE_DIR / "analysis/quality_scores/improvement_batch5_sns_crossref_part2.csv"

# 対象34件（B/C-grade後半）
TARGET_FILES = [
    "case_studies/blake_anderson/sns_analysis.md",
    "case_studies/brock/sns_analysis.md",
    "case_studies/catnose99/sns_analysis.md",
    "case_studies/chase_jarvis/sns_analysis.md",
    "case_studies/chris_do/sns_analysis.md",
    "case_studies/chris_williamson/sns_analysis.md",
    "case_studies/codie_sanchez/sns_analysis.md",
    "case_studies/connor/sns_analysis.md",
    "case_studies/courtland_allen/sns_analysis.md",
    "case_studies/dagobert_renouf/sns_analysis.md",
    "case_studies/damon_chen/sns_analysis.md",
    "case_studies/dan_koe/sns_analysis.md",
    "case_studies/daniel_bitton/sns_analysis.md",
    "case_studies/daniel_nguyen/sns_analysis.md",
    "case_studies/daniel_vassallo/sns_analysis.md",
    "case_studies/danny_postma/sns_analysis.md",
    "case_studies/david_perell/sns_analysis.md",
    "case_studies/des_traynor/sns_analysis.md",
    "case_studies/desmond/sns_analysis.md",
    "case_studies/dharmesh_shah/sns_analysis.md",
    "case_studies/dhh/sns_analysis.md",
    "case_studies/dickie_bush/sns_analysis.md",
    "case_studies/diego_roshardt/sns_analysis.md",
    "case_studies/elise_darma/sns_analysis.md",
    "case_studies/florin_pop/sns_analysis.md",
    "case_studies/gary_vaynerchuk/sns_analysis.md",
    "case_studies/gil_hildebrand/sns_analysis.md",
    "case_studies/graham_stephan/sns_analysis.md",
    "case_studies/grant_mcconnaughey/sns_analysis.md",
    "case_studies/greg_isenberg/sns_analysis.md",
    "case_studies/hahnbee_lee/sns_analysis.md",
    "case_studies/harry_dry/sns_analysis.md",
    "case_studies/hassan_el_mghari/sns_analysis.md",
    "case_studies/ikehaya/sns_analysis.md"
]

def extract_person_info(filepath: Path) -> Tuple[str, str, str]:
    """SNSファイルから人物情報を抽出"""
    content = filepath.read_text(encoding='utf-8')

    # 名前を抽出
    name_match = re.search(r'\*\*名前\*\*:\s*(.+)', content)
    name = name_match.group(1).strip() if name_match else filepath.parent.name.replace('_', ' ')

    # IDを抽出
    id_match = re.search(r'\*\*ID\*\*:\s*(\d+)', content)
    person_id = id_match.group(1) if id_match else "unknown"

    # 主要プロダクトを抽出
    products = []
    in_products_section = False
    for line in content.split('\n'):
        if '**主要プロダクト**' in line or '**プロダクト**' in line:
            in_products_section = True
            continue
        if in_products_section:
            if line.strip().startswith('- **'):
                product = re.search(r'\*\*(.+?)\*\*', line)
                if product:
                    products.append(product.group(1))
            elif line.strip().startswith('##'):
                break

    return name, person_id, ', '.join(products) if products else ""

def search_newsletter_references(person_name: str, products: str) -> List[str]:
    """Newsletterディレクトリから関連ファイルを検索"""
    references = []

    # 検索キーワードを準備
    search_terms = [person_name]
    if products:
        search_terms.extend([p.strip() for p in products.split(',')])

    # Newsletter配下を全検索
    for md_file in NEWSLETTER_DIR.rglob("*.md"):
        if md_file.name in ['index.md', 'orchestration_report_20251226.md']:
            continue

        try:
            content = md_file.read_text(encoding='utf-8')

            # キーワードマッチング
            for term in search_terms:
                if term and term.lower() in content.lower():
                    relative_path = md_file.relative_to(BASE_DIR / "documents")
                    references.append(f"../{relative_path}")
                    break
        except Exception:
            continue

    return references

def search_app_references(person_name: str, products: str) -> List[str]:
    """Appディレクトリから関連ファイルを検索"""
    references = []

    # App配下のケーススタディを検索
    case_studies_dir = APP_DIR / "case_studies"
    if not case_studies_dir.exists():
        return references

    search_terms = [person_name]
    if products:
        search_terms.extend([p.strip() for p in products.split(',')])

    for md_file in case_studies_dir.rglob("*.md"):
        try:
            content = md_file.read_text(encoding='utf-8')

            for term in search_terms:
                if term and term.lower() in content.lower():
                    relative_path = md_file.relative_to(BASE_DIR / "documents")
                    references.append(f"../{relative_path}")
                    break
        except Exception:
            continue

    return references

def update_cross_reference(filepath: Path, references: List[str]) -> bool:
    """cross_referenceセクションを更新"""
    if not references:
        return False

    content = filepath.read_text(encoding='utf-8')

    # 既存のcross_referenceセクションを検索
    crossref_pattern = r'(## \d+\. cross_reference.*?)(?=\n## |\Z)'
    match = re.search(crossref_pattern, content, re.DOTALL)

    # 新しいcross_referenceセクションを生成
    new_section = "## 8. cross_reference\n\n"
    new_section += "### Related Case Studies\n\n"

    for ref in sorted(set(references)):
        # ファイル名から説明を生成
        filename = Path(ref).stem
        new_section += f"- [{filename}]({ref})\n"

    new_section += "\n"

    if match:
        # 既存セクションを置換
        new_content = content[:match.start()] + new_section + content[match.end():]
    else:
        # ファイル末尾に追加
        new_content = content.rstrip() + "\n\n" + new_section

    filepath.write_text(new_content, encoding='utf-8')
    return True

def main():
    """メイン処理"""
    results = []

    print(f"Processing {len(TARGET_FILES)} SNS files...")

    for idx, target_file in enumerate(TARGET_FILES, 1):
        filepath = SNS_DIR / target_file

        if not filepath.exists():
            print(f"[{idx}/{len(TARGET_FILES)}] SKIP: {target_file} (not found)")
            results.append({
                'file': target_file,
                'status': 'NOT_FOUND',
                'references_added': 0,
                'references': ''
            })
            continue

        # 人物情報を抽出
        name, person_id, products = extract_person_info(filepath)
        print(f"[{idx}/{len(TARGET_FILES)}] Processing: {name} (ID: {person_id})")

        # Newsletter/Appから関連ファイルを検索
        newsletter_refs = search_newsletter_references(name, products)
        app_refs = search_app_references(name, products)

        all_refs = newsletter_refs + app_refs

        if all_refs:
            # cross_referenceを更新
            updated = update_cross_reference(filepath, all_refs)
            status = 'UPDATED' if updated else 'FAILED'
            print(f"  → Found {len(all_refs)} references: {status}")
        else:
            status = 'NO_REFS'
            print(f"  → No references found")

        results.append({
            'file': target_file,
            'name': name,
            'id': person_id,
            'status': status,
            'references_added': len(all_refs),
            'references': '; '.join(all_refs)
        })

    # CSV出力
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['file', 'name', 'id', 'status', 'references_added', 'references'])
        writer.writeheader()
        writer.writerows(results)

    # サマリー
    total = len(results)
    updated = sum(1 for r in results if r['status'] == 'UPDATED')
    no_refs = sum(1 for r in results if r['status'] == 'NO_REFS')

    print(f"\n=== Summary ===")
    print(f"Total: {total}")
    print(f"Updated: {updated}")
    print(f"No References: {no_refs}")
    print(f"CSV: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
