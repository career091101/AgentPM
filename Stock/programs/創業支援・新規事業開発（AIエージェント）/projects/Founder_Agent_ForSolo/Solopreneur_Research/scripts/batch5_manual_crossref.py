#!/usr/bin/env python3
"""
Batch 5 Manual Cross-Reference Enhancement
NO_REFSの16件を再検索し、より広範な検索で参照を発見
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research")
SNS_DIR = BASE_DIR / "documents/03_SNS"
NEWSLETTER_DIR = BASE_DIR / "documents/02_Newsletter"
APP_DIR = BASE_DIR / "documents/01_App"

# NO_REFSの16件
NO_REFS_TARGETS = [
    ("case_studies/catnose99/sns_analysis.md", ["catnose99", "catnose", "Zenn"]),
    ("case_studies/chase_jarvis/sns_analysis.md", ["chase jarvis", "CreativeLive"]),
    ("case_studies/chris_do/sns_analysis.md", ["chris do", "The Futur"]),
    ("case_studies/chris_williamson/sns_analysis.md", ["chris williamson", "Modern Wisdom"]),
    ("case_studies/dan_koe/sns_analysis.md", ["dan koe", "Digital Economics"]),
    ("case_studies/des_traynor/sns_analysis.md", ["des traynor", "Intercom"]),
    ("case_studies/dharmesh_shah/sns_analysis.md", ["dharmesh shah", "HubSpot"]),
    ("case_studies/dhh/sns_analysis.md", ["dhh", "david heinemeier hansson", "basecamp", "hey", "37signals"]),
    ("case_studies/elise_darma/sns_analysis.md", ["elise darma", "Instagram"]),
    ("case_studies/florin_pop/sns_analysis.md", ["florin pop", "100 days 100 projects"]),
    ("case_studies/gary_vaynerchuk/sns_analysis.md", ["gary vaynerchuk", "gary vee", "VaynerMedia"]),
    ("case_studies/graham_stephan/sns_analysis.md", ["graham stephan", "Real Estate"]),
    ("case_studies/greg_isenberg/sns_analysis.md", ["greg isenberg", "Late Checkout"]),
    ("case_studies/hahnbee_lee/sns_analysis.md", ["hahnbee lee", "hahnbee"]),
    ("case_studies/hassan_el_mghari/sns_analysis.md", ["hassan el mghari", "hassan", "Page Flows"]),
    ("case_studies/ikehaya/sns_analysis.md", ["ikehaya", "イケハヤ", "イケダハヤト"])
]

def search_in_all_files(search_terms: List[str], directories: List[Path]) -> List[str]:
    """複数ディレクトリを横断的に検索"""
    references = []

    for directory in directories:
        if not directory.exists():
            continue

        for md_file in directory.rglob("*.md"):
            # 除外ファイル
            if any(skip in str(md_file) for skip in ['index.md', 'orchestration', 'progress', 'roadmap']):
                continue

            try:
                content = md_file.read_text(encoding='utf-8').lower()

                # いずれかのキーワードにマッチすればOK
                for term in search_terms:
                    if term.lower() in content:
                        relative_path = md_file.relative_to(BASE_DIR / "documents")
                        references.append(f"../{relative_path}")
                        break
            except Exception:
                continue

    return list(set(references))

def add_manual_crossref(filepath: Path, references: List[str]) -> bool:
    """cross_referenceセクションを手動追加"""
    if not references:
        return False

    content = filepath.read_text(encoding='utf-8')

    # 既存のcross_referenceセクションを検索
    crossref_pattern = r'## \d+\. cross_reference.*?(?=\n## |\Z)'
    match = re.search(crossref_pattern, content, re.DOTALL | re.IGNORECASE)

    # 新しいcross_referenceセクションを生成
    new_section = "\n## 8. cross_reference\n\n"
    new_section += "### Related Case Studies\n\n"

    for ref in sorted(references):
        filename = Path(ref).stem
        new_section += f"- [{filename}]({ref})\n"

    new_section += "\n"

    if match:
        # 既存セクションを置換
        new_content = content[:match.start()] + new_section + content[match.end():]
    else:
        # ファイル末尾に追加
        # 参考リンクセクションの前に挿入
        refs_pattern = r'(## 参考リンク|## 修正履歴)'
        refs_match = re.search(refs_pattern, content)

        if refs_match:
            new_content = content[:refs_match.start()] + new_section + content[refs_match.start():]
        else:
            new_content = content.rstrip() + "\n\n" + new_section

    filepath.write_text(new_content, encoding='utf-8')
    return True

def main():
    """メイン処理"""
    print(f"Processing {len(NO_REFS_TARGETS)} NO_REFS SNS files with enhanced search...")

    search_dirs = [NEWSLETTER_DIR, APP_DIR]
    results = []

    for idx, (target_file, search_terms) in enumerate(NO_REFS_TARGETS, 1):
        filepath = SNS_DIR / target_file

        if not filepath.exists():
            print(f"[{idx}/{len(NO_REFS_TARGETS)}] SKIP: {target_file} (not found)")
            continue

        print(f"[{idx}/{len(NO_REFS_TARGETS)}] Processing: {search_terms[0]}")

        # 全ディレクトリから検索
        references = search_in_all_files(search_terms, search_dirs)

        if references:
            updated = add_manual_crossref(filepath, references)
            print(f"  → Found {len(references)} references: {'UPDATED' if updated else 'FAILED'}")
            results.append((target_file, len(references), 'UPDATED' if updated else 'FAILED'))
        else:
            print(f"  → Still no references found")
            results.append((target_file, 0, 'NO_REFS'))

    # サマリー
    total = len(results)
    updated = sum(1 for _, _, status in results if status == 'UPDATED')
    no_refs = sum(1 for _, _, status in results if status == 'NO_REFS')

    print(f"\n=== Summary ===")
    print(f"Total: {total}")
    print(f"Updated: {updated}")
    print(f"Still No References: {no_refs}")

    # 詳細レポート
    print(f"\n=== Details ===")
    for file, count, status in results:
        print(f"{status:10} {count:2}件 - {file}")

if __name__ == "__main__":
    main()
