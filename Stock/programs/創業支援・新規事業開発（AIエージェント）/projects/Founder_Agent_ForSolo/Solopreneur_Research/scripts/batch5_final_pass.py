#!/usr/bin/env python3
"""
Batch 5 Final Pass - 残り8件の最終確認
戦略文書、索引、成功パターンなど広範囲検索
"""

import re
from pathlib import Path
from typing import List

BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research")
SNS_DIR = BASE_DIR / "documents/03_SNS"
DOCS_DIR = BASE_DIR / "documents"

# 残り8件（NO_REFS）
FINAL_TARGETS = [
    ("case_studies/chase_jarvis/sns_analysis.md", ["chase", "jarvis", "creative live", "photography"]),
    ("case_studies/chris_williamson/sns_analysis.md", ["williamson", "modern wisdom", "podcast"]),
    ("case_studies/dan_koe/sns_analysis.md", ["dan koe", "digital economics", "solopreneur"]),
    ("case_studies/florin_pop/sns_analysis.md", ["florin", "100 days", "100 projects"]),
    ("case_studies/gary_vaynerchuk/sns_analysis.md", ["gary vee", "vayner", "entrepreneur"]),
    ("case_studies/greg_isenberg/sns_analysis.md", ["isenberg", "late checkout", "community"]),
    ("case_studies/hahnbee_lee/sns_analysis.md", ["hahnbee", "korean", "creator"]),
    ("case_studies/hassan_el_mghari/sns_analysis.md", ["hassan", "page flows", "ui"]),
]

def deep_search(search_terms: List[str]) -> List[str]:
    """ドキュメント全体から深い検索"""
    references = []

    # 除外パターン
    exclude_patterns = ['index.md', 'progress', 'roadmap', 'orchestration', 'completion']

    for md_file in DOCS_DIR.rglob("*.md"):
        # SNS自身のファイルは除外
        if '/03_SNS/' in str(md_file):
            continue

        # 除外パターン
        if any(pattern in md_file.name for pattern in exclude_patterns):
            continue

        try:
            content = md_file.read_text(encoding='utf-8').lower()

            # 複数のキーワードが同時に含まれているかチェック（AND検索）
            matches = 0
            for term in search_terms:
                if term.lower() in content:
                    matches += 1

            # 2つ以上のキーワードがマッチしたら関連ドキュメントとみなす
            if matches >= 2 or (len(search_terms) <= 2 and matches >= 1):
                relative_path = md_file.relative_to(DOCS_DIR)
                references.append(f"../{relative_path}")

        except Exception:
            continue

    return list(set(references))

def add_strategic_crossref(filepath: Path, references: List[str]) -> bool:
    """戦略的cross_referenceを追加"""
    if not references:
        # 参照が見つからない場合、一般的な戦略文書へのリンクを追加
        references = [
            "../02_Newsletter/strategies/NL_STRATEGY_020_comment_engagement.md",
            "../02_Newsletter/strategies/NL_STRATEGY_024_sns_marketing_nl.md"
        ]

    content = filepath.read_text(encoding='utf-8')

    # 既存のcross_referenceセクションを検索
    crossref_pattern = r'## \d+\. cross_reference.*?(?=\n## |\Z)'
    match = re.search(crossref_pattern, content, re.DOTALL | re.IGNORECASE)

    if match:
        # 既に存在する場合はスキップ（手動追加済み）
        return False

    # 新しいcross_referenceセクションを生成
    new_section = "\n## 8. cross_reference\n\n"

    if len(references) > 2:
        new_section += "### Related Case Studies\n\n"
        for ref in sorted(references):
            filename = Path(ref).stem
            new_section += f"- [{filename}]({ref})\n"
    else:
        new_section += "### Related Strategies\n\n"
        new_section += "この人物に直接関連するケーススタディは見つかりませんでしたが、以下の戦略が応用可能です：\n\n"
        for ref in references:
            filename = Path(ref).stem
            new_section += f"- [{filename}]({ref})\n"

    new_section += "\n"

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
    print(f"Final pass for {len(FINAL_TARGETS)} remaining NO_REFS files...")

    results = []

    for idx, (target_file, search_terms) in enumerate(FINAL_TARGETS, 1):
        filepath = SNS_DIR / target_file

        if not filepath.exists():
            print(f"[{idx}/{len(FINAL_TARGETS)}] SKIP: {target_file} (not found)")
            continue

        print(f"[{idx}/{len(FINAL_TARGETS)}] Processing: {search_terms[0]}")

        # 深い検索
        references = deep_search(search_terms)

        if references:
            print(f"  → Found {len(references)} references via deep search")
        else:
            print(f"  → No specific references, adding strategic links")

        updated = add_strategic_crossref(filepath, references)
        results.append((target_file, len(references), 'ADDED' if updated else 'SKIP'))

    # サマリー
    total = len(results)
    added = sum(1 for _, _, status in results if status == 'ADDED')

    print(f"\n=== Final Summary ===")
    print(f"Total: {total}")
    print(f"Added: {added}")

    print(f"\n=== Details ===")
    for file, count, status in results:
        print(f"{status:10} {count:2}件 - {file}")

if __name__ == "__main__":
    main()
