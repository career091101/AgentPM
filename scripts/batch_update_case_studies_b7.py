#!/usr/bin/env python3
"""
B7バッチ（051-060番台）のケーススタディファイルをv4.0テンプレート準拠に更新
"""

import os
import re

# ベースディレクトリ
BASE_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies"

# 更新対象ファイル（残り）
FILES_TO_UPDATE = [
    "051_dominic_zijlstra.md",
    "051_julien_nahum.md",
    "052_grant_mcconnaughey.md",
    "053_mac_martine.md",
    "054_sorin_alupoaie.md",
    "055_daniel_nguyen.md",
    "055_yasser_elsaid.md",
    "056_romain_torres.md",
    "057_david_attias.md",
    "057_saeed_ezzati.md",
    "058_simon_hoiberg.md",
    "058_timo_tzschetzsch.md",
    "059_nikita_evgeniy.md",
    "059_sumit_kumar.md",
]

# YAML Front Matter とコメントのテンプレート（ファイル内容から抽出した情報で埋める）
YAML_TEMPLATE = """---
id: "{id}"
title: "{title}"
revenue:
  mrr_usd: {mrr}
  arr_usd: {arr}
  note: "{revenue_note}"
  mrr_tier: "{mrr_tier}"
main_product:
  name: "{product_name}"
  url: "{product_url}"
  category: "{category}"
  description: "{description}"
tags:
  growth_strategy: {growth_strategy}
  niche: {niche}
  marketing_channel: {marketing_channel}
  tech_stack: {tech_stack}
  business_model: {business_model}
  target_market: {target_market}
founder:
  name: "{founder_name}"
  nationality: "{nationality}"
  age: {age}
  background: "{background}"
timeline_start: "{timeline_start}"
launch_date: "{launch_date}"
japan_score:
  total: {japan_score}
  rating: "{japan_rating}"
  product_similarity: {jp_product}
  market_need: {jp_market}
  competition: {jp_competition}
  localization: {jp_localization}
  reproducibility: {jp_reproducibility}
  comment: "{jp_comment}"
quality:
  fact_check: "pass"
  sources: {sources}
  last_updated: "2025-12-28"
---
"""

def extract_file_number(filename):
    """ファイル名から番号を抽出"""
    match = re.match(r'(\d+)_', filename)
    return match.group(1) if match else "000"

def check_has_yaml_frontmatter(filepath):
    """YAMLFront Matterがあるか確認"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        return content.startswith('---\n')

def add_analyst_comment_if_missing(filepath):
    """分析者コメントがない場合、末尾に追加"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 既にコメントがあるかチェック
    if '## 分析者コメント' in content:
        print(f"  ✓ {os.path.basename(filepath)}: 分析者コメント既存")
        return

    # ファイル末尾に追加
    comment = "\n\n---\n\n## 分析者コメント\n\n（このケーススタディの分析者コメントは後ほど追加予定）\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content + comment)

    print(f"  ✓ {os.path.basename(filepath)}: 分析者コメント追加")

def main():
    print("=== B7バッチ ケーススタディ v4.0更新処理 ===\n")

    updated_count = 0
    skipped_count = 0

    for filename in FILES_TO_UPDATE:
        filepath = os.path.join(BASE_DIR, filename)

        if not os.path.exists(filepath):
            print(f"✗ {filename}: ファイルが存在しません")
            continue

        # YAML Front Matter確認
        has_yaml = check_has_yaml_frontmatter(filepath)

        if has_yaml:
            print(f"→ {filename}: YAML Front Matter既存、スキップ")
            skipped_count += 1
            # 分析者コメントのみ確認・追加
            add_analyst_comment_if_missing(filepath)
        else:
            print(f"→ {filename}: YAML Front Matter未実装（手動更新必要）")
            # とりあえず分析者コメント枠だけ追加
            add_analyst_comment_if_missing(filepath)
            updated_count += 1

    print(f"\n=== 処理完了 ===")
    print(f"更新: {updated_count}件")
    print(f"スキップ: {skipped_count}件")
    print(f"\n※ YAML Front Matter未実装ファイルは手動で更新が必要です")

if __name__ == "__main__":
    main()
