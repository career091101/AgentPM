#!/usr/bin/env python3
"""
歯科医院リストから院長名を収集するスクリプト（バッチ4: 行322-428）
"""

import csv
import json
import time
import os
import re
from datetime import datetime
from pathlib import Path

# 設定
CSV_INPUT_PATH = "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/歯科医院リスト - nationwide_45prefectures_split_address_20260102_233408.csv.csv"
OUTPUT_DIR = "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04"
OUTPUT_FILE = f"{OUTPUT_DIR}/director_names_batch_4.csv"

# 出力ディレクトリ作成
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def read_csv_lines(file_path: str, start_line: int = 322, end_line: int = 428) -> list:
    """CSVファイルから指定行を読み込む"""
    clinics = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader, 1):
                if start_line <= idx <= end_line:
                    if len(row) > 0:
                        # 最初の列（医院名）を取得
                        clinic_name = row[0].strip()
                        # ウェブサイトURL（8番目の列）を取得
                        website = row[7].strip() if len(row) > 7 else ""
                        clinics.append({
                            'line_number': idx,
                            'clinic_name': clinic_name,
                            'website': website,
                            'director_name': '',
                            'method': '',
                            'status': ''
                        })
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

    return clinics

def collect_director_names():
    """院長名を収集"""
    print("医院リスト読み込み中...")
    clinics = read_csv_lines(CSV_INPUT_PATH)

    if not clinics:
        print("ERROR: CSVファイルを読み込めませんでした")
        return

    print(f"対象医院数: {len(clinics)} 件（行322-428）")
    print("\nWebSearchとWebFetchを使用して院長名を検索します。")
    print("-" * 80)

    # 院長名を検索（WebSearchを使用する場合は、別の方法で実装）
    # 注: 本スクリプトはマニュアル検索用のテンプレートです
    # Claude CodeのWebSearch/WebFetchツールを使用する場合は、
    # このスクリプトは出力ファイルのみ生成します

    print("\nこのスクリプトは以下の処理を実行します：")
    print("1. CSVファイルから医院情報を読み込み")
    print("2. Claude Codeで WebSearch/WebFetch を使用して院長名を検索")
    print("3. 結果をCSVファイルに保存")
    print("\nManual Mode: 以下のコマンドを実行して院長名を検索してください：")
    print("")
    print("このスクリプトの代わりに、Claude Code内で直接以下を実行:")
    print('- /WebSearch "医院名 院長"')
    print('- /WebFetch "公式ウェブサイトURL" "院長名を探す"')

    # CSVに保存（スケルトン）
    print("\n" + "-" * 80)
    print(f"結果テンプレートをCSVに保存中: {OUTPUT_FILE}")

    try:
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['行番号', '医院名', '公式ウェブサイト', '院長名'])

            for clinic in clinics:
                # デフォルトは「検索待ち」
                director_name = "検索待ち"
                writer.writerow([
                    clinic['line_number'],
                    clinic['clinic_name'],
                    clinic['website'],
                    director_name
                ])

        print(f"✓ テンプレート保存完了: {OUTPUT_FILE}")
        print(f"\n次のステップ:")
        print(f"1. {OUTPUT_FILE} を開く")
        print(f"2. Claude CodeでWebSearchまたはWebFetchを使用して各医院の院長名を検索")
        print(f"3. 「院長名」列に検索結果を記入")
        print(f"4. 見つからない場合は「不明」と記入")

    except Exception as e:
        print(f"ERROR: ファイル保存に失敗しました: {e}")

if __name__ == "__main__":
    collect_director_names()
