#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
歯科医院院長名検索スクリプト（バッチ処理版）
WebFetch/WebSearchを使用して院長名を取得

使用方法:
  claude < director_search_batch.py

このスクリプトはClaude Code内で直接実行することを想定しています。
Claude CodeのWebFetch/WebSearchツールを使用して院長名を検索します。
"""

import json
import time
import re
from pathlib import Path

# ファイルパス定義
CLINICS_JSON = "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/clinics_for_director_search.json"
OUTPUT_CSV = "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_1.csv"

def load_clinics():
    """JSON形式の医院リストを読み込む"""
    with open(CLINICS_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_director_name(name):
    """院長名をクリーニング（敬称除外など）"""
    if not name:
        return None

    name = name.strip()

    # 敬称を除外
    name = re.sub(r'[先生等医師Dr\.の]*$', '', name).strip()
    name = re.sub(r'^Dr\.\s*', '', name).strip()

    # 妥当性チェック
    if not name or len(name) > 30:
        return None

    return name

def format_output_csv(results):
    """結果をCSV形式でフォーマット"""
    lines = ["医院名,院長名"]

    for result in results:
        clinic_name = result['clinic_name'].replace(',', '、')  # CSVの区切り文字を避ける
        director_name = result['director_name'] or '不明'
        lines.append(f"{clinic_name},{director_name}")

    return '\n'.join(lines)

def main():
    # 医院リストを読み込み
    clinics = load_clinics()

    # 最初の20医院に限定
    sample_clinics = clinics[:20]

    print(f"院長名検索を開始します")
    print(f"処理対象: {len(sample_clinics)}医院")
    print("="*80)

    results = []

    for idx, clinic in enumerate(sample_clinics, 1):
        clinic_id = clinic['clinic_id']
        clinic_name = clinic['clinic_name']
        website = clinic['website']

        print(f"\n[{idx}/{len(sample_clinics)}] {clinic_name}")

        director_name = None
        source = "not_found"

        # Step 1: WebFetchでウェブサイトから院長名を抽出
        print(f"  → WebFetch: {website}")

        # 実装: Claude Code内でWebFetchツールを使用
        # 以下は擬似コード（実際のClaude Code実行時に置き換え）
        webfetch_prompt = f"""
以下の歯科医院のウェブサイトから院長名を抽出してください。

医院名: {clinic_name}
URL: {website}

抽出ルール:
- 「院長」「理事長」「Dr.」などのキーワードから院長名を探す
- 複数候補がある場合は最初の1名のみ
- 敬称（先生、Dr.等）は除外して氏名のみ出力
- 見つからない場合は「見つかりません」と返答

出力形式: 院長名のみ（例: 山田太郎）
"""

        # Claude Code内のWebFetchツール呼び出し
        # webfetch_result = await webfetch(url=website, prompt=webfetch_prompt)
        # director_name = clean_director_name(webfetch_result)

        # テンプレートでは None を設定（実装時に置き換え）
        if director_name is None:
            # Step 2: WebSearchで検索
            print(f"  → WebSearch: {clinic_name} 院長")

            websearch_prompt = f"{clinic_name} 院長"

            # Claude Code内のWebSearchツール呼び出し
            # websearch_result = await websearch(query=websearch_prompt)
            # director_name = clean_director_name(extract_from_websearch(websearch_result))
            # source = "websearch"
        else:
            source = "webfetch"

        if director_name:
            print(f"  ✓ 院長名: {director_name} (source: {source})")
        else:
            director_name = None
            print(f"  × 院長名: 不明")

        results.append({
            'clinic_id': clinic_id,
            'clinic_name': clinic_name,
            'director_name': director_name,
            'source': source,
            'website': website
        })

        # レート制限対策: 2秒待機
        if idx < len(sample_clinics):
            time.sleep(2)

    print("\n" + "="*80)

    # 結果をCSVで保存
    csv_content = format_output_csv(results)

    with open(OUTPUT_CSV, 'w', encoding='utf-8') as f:
        f.write(csv_content)

    # サマリー出力
    found = sum(1 for r in results if r['director_name'])
    not_found = len(results) - found

    print(f"\n処理完了")
    print(f"  - 院長名取得: {found}医院")
    print(f"  - 不明: {not_found}医院")
    print(f"  - 成功率: {found/len(results)*100:.1f}%")
    print(f"\n出力ファイル: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
