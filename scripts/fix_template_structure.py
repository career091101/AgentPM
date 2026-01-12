#!/usr/bin/env python3
"""
テンプレートv4.0統一スクリプト
H2 `## 📋 調査項目` を削除し、H3セクションをH2に昇格
"""

import re
from pathlib import Path

# 対象ファイル
files = [
    "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/082_samuel_rondot.md",
    "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/081_tony_dinh_ai.md",
    "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/085_marc_lou_shipfast.md",
    "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/083_pieter_levels_ai.md",
    "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/084_dmytro_krasun.md",
    "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/076_andrey_azimov.md",
    "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/077_yong_soo_chung.md",
    "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents/01_App/case_studies/080_bhanu_teja.md",
]


def fix_template(content: str) -> str:
    """
    テンプレート構造を修正

    1. `## 📋 調査項目` とその直後の空行を削除
    2. `### [数字]. [タイトル]` → `## 📋 [数字]. [タイトル]` に変換
    3. `### 📚 参考リンク` → `## 📚 参考リンク` に変換
    """
    lines = content.split('\n')
    result = []
    skip_next_empty = False

    for i, line in enumerate(lines):
        # パターン1: ## 📋 調査項目 を削除
        if re.match(r'^##\s+📋\s*調査項目\s*$', line):
            skip_next_empty = True
            continue

        # 直後の空行をスキップ
        if skip_next_empty and line.strip() == '':
            skip_next_empty = False
            continue

        skip_next_empty = False

        # パターン2: ### 数字. セクション名 → ## 📋 数字. セクション名
        match = re.match(r'^###\s+(\d+)\.\s+(.+)$', line)
        if match:
            number, title = match.groups()
            result.append(f'## 📋 {number}. {title}')
            continue

        # パターン3: ### 📚 参考リンク → ## 📚 参考リンク
        if re.match(r'^###\s+📚\s+参考リンク\s*$', line):
            result.append('## 📚 参考リンク')
            continue

        # その他の行はそのまま
        result.append(line)

    return '\n'.join(result)


def main():
    """メイン処理"""
    for file_path in files:
        path = Path(file_path)
        if not path.exists():
            print(f"⚠️  File not found: {path.name}")
            continue

        print(f"Processing: {path.name}")

        # ファイル読み込み
        content = path.read_text(encoding='utf-8')

        # 修正
        fixed_content = fix_template(content)

        # 書き戻し
        path.write_text(fixed_content, encoding='utf-8')

        print(f"✅ Fixed: {path.name}")

    print("\n✅ All files processed!")


if __name__ == "__main__":
    main()
