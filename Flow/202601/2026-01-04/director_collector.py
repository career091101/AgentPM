#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
歯科医院リストから院長名を収集するスクリプト
機能:
  1. 公式ウェブサイトがあればWebFetchで取得
  2. ウェブサイトから院長名を抽出（院長、理事長、Dr.等のキーワード）
  3. 見つからない場合はWebSearchで「医院名 院長」を検索
  4. 結果をCSV形式で保存
"""

import csv
import json
import time
import sys
import re
from pathlib import Path
from typing import Optional, List, Dict, Tuple
import subprocess

# CSV入力ファイルパス
INPUT_CSV = "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/歯科医院リスト - nationwide_45prefectures_split_address_20260102_233408.csv.csv"
OUTPUT_CSV = "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_1.csv"
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04")

# 出力ディレクトリ作成
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

class DirectorCollector:
    def __init__(self):
        self.results = []
        self.processed_count = 0
        self.webfetch_success = 0
        self.websearch_success = 0
        self.unknown_count = 0
        self.webfetch_error_count = 0

    def extract_director_from_text(self, text: str, clinic_name: str) -> Optional[str]:
        """テキストから院長名を抽出"""
        if not text:
            return None

        # キーワードリスト（優先順）
        keywords = [
            r'院長\s*[:：]\s*([^\s、。\n]+)',
            r'院長\s+([^\s、。\n]+)',
            r'理事長\s*[:：]\s*([^\s、。\n]+)',
            r'理事長\s+([^\s、。\n]+)',
            r'Dr\.\s*([^\s、。\n]+)',
            r'医師\s+([^\s、。\n]+)',
            r'代表\s*[:：]\s*([^\s、。\n]+)',
        ]

        for pattern in keywords:
            match = re.search(pattern, text)
            if match:
                name = match.group(1).strip()
                # 敬称を除去
                name = re.sub(r'[先生等医師Dr\.の]*$', '', name).strip()
                # 名前の妥当性チェック（3文字以上30文字以下）
                if 1 < len(name) <= 30:
                    return name

        return None

    def call_claude_webfetch(self, website_url: str, clinic_name: str) -> Optional[str]:
        """Claude CodeのWebFetch toolを使用してウェブサイトから院長名を取得"""
        prompt = f"""
以下の歯科医院のウェブサイトから院長名を抽出してください。

医院名: {clinic_name}
URL: {website_url}

抽出ルール:
- 「院長」「理事長」「Dr.」などのキーワードから院長名を探す
- 複数候補ある場合は最初の1名のみ
- 敬称（先生、Dr.等）は除外して氏名のみ出力
- 見つからない場合は「見つかりません」と返答

出力形式: 院長名のみ（例: 山田太郎）
"""
        try:
            # Claude Codeの呼び出し（claude --eval で実装可能な場合）
            # ここではシミュレーション: actual使用時はClaude Code内で実行
            # 実装: WebFetchツールの直接呼び出しが必要
            print(f"WebFetch対象: {clinic_name}")
            print(f"URL: {website_url}")
            print(f"prompt: {prompt}")
            return None  # 実装時にはWebFetch結果を処理
        except Exception as e:
            print(f"WebFetch エラー ({clinic_name}): {e}")
            self.webfetch_error_count += 1
            return None

    def call_claude_websearch(self, clinic_name: str) -> Optional[str]:
        """Claude CodeのWebSearch toolを使用して院長名を検索"""
        search_query = f"{clinic_name} 院長"
        print(f"[WebSearch実行] {search_query}")

        try:
            # WebSearchツール使用例（claude --eval内で実装）
            # 実装時にはWebSearchの結果をパース
            return None  # 実装時にはWebSearch結果を処理
        except Exception as e:
            print(f"WebSearch エラー ({clinic_name}): {e}")
            return None

    def read_csv_data(self) -> List[Dict[str, str]]:
        """CSVファイルから医院データを読み込み（行1-107）"""
        clinics = []
        try:
            with open(INPUT_CSV, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for idx, row in enumerate(reader, start=2):  # ヘッダー行のため start=2
                    if idx <= 107:  # 行1-107（ヘッダー除外）
                        clinics.append(row)
                    else:
                        break
            print(f"✓ {len(clinics)}件の医院データを読み込みました")
            return clinics
        except FileNotFoundError:
            print(f"❌ ファイルが見つかりません: {INPUT_CSV}")
            return []
        except Exception as e:
            print(f"❌ CSVファイル読み込みエラー: {e}")
            return []

    def process_clinics(self, clinics: List[Dict[str, str]]):
        """医院リストを処理して院長名を収集"""
        total = len(clinics)

        for idx, clinic in enumerate(clinics, start=1):
            clinic_name = clinic.get('医院名', '').strip()
            website_url = clinic.get('公式ウェブサイト', '').strip()

            if not clinic_name:
                continue

            print(f"\n[{idx}/{total}] {clinic_name}")
            director_name = "不明"
            source = "unknown"

            # Step 1: 公式ウェブサイトがあればWebFetchで取得
            if website_url:
                print(f"  → WebFetch対象: {website_url}")
                director_name = self.call_claude_webfetch(website_url, clinic_name)
                if director_name and director_name != "見つかりません":
                    source = "webfetch"
                    self.webfetch_success += 1
                    print(f"  ✓ 院長名: {director_name}")

            # Step 2: WebFetchで見つからない場合はWebSearch
            if director_name is None or director_name == "見つかりません":
                print(f"  → WebSearch実行: {clinic_name} 院長")
                director_name = self.call_claude_websearch(clinic_name)
                if director_name:
                    source = "websearch"
                    self.websearch_success += 1
                    print(f"  ✓ 院長名: {director_name}")

            # Step 3: 見つからない場合は「不明」
            if not director_name:
                director_name = "不明"
                source = "not_found"
                self.unknown_count += 1
                print(f"  × 院長名: 不明")

            # 結果を記録
            self.results.append({
                "医院名": clinic_name,
                "院長名": director_name,
                "ソース": source,
                "ウェブサイト": website_url
            })

            self.processed_count += 1

            # レート制限対策: 2秒ごとにインターバル
            if idx < total:
                time.sleep(2)

    def save_results(self):
        """結果をCSV形式で保存"""
        try:
            with open(OUTPUT_CSV, 'w', encoding='utf-8', newline='') as f:
                fieldnames = ["医院名", "院長名"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for result in self.results:
                    writer.writerow({
                        "医院名": result["医院名"],
                        "院長名": result["院長名"]
                    })

            print(f"\n✓ 結果を保存しました: {OUTPUT_CSV}")
            return True
        except Exception as e:
            print(f"❌ CSVファイル保存エラー: {e}")
            return False

    def print_summary(self):
        """処理結果のサマリーを表示"""
        print("\n" + "="*60)
        print("処理完了サマリー")
        print("="*60)
        print(f"処理済み医院数: {self.processed_count}")
        print(f"  - WebFetch成功: {self.webfetch_success}")
        print(f"  - WebSearch成功: {self.websearch_success}")
        print(f"  - 不明: {self.unknown_count}")
        print(f"  - WebFetchエラー: {self.webfetch_error_count}")
        print(f"\n成功率: {(self.processed_count - self.unknown_count) / self.processed_count * 100:.1f}%")
        print(f"出力ファイル: {OUTPUT_CSV}")
        print("="*60)

def main():
    print("歯科医院院長名収集スクリプト")
    print("="*60)
    print(f"入力ファイル: {INPUT_CSV}")
    print(f"出力ファイル: {OUTPUT_CSV}")
    print("="*60)

    collector = DirectorCollector()

    # Step 1: CSVデータを読み込み
    clinics = collector.read_csv_data()
    if not clinics:
        print("❌ 医院データの読み込みに失敗しました")
        return False

    # Step 2: 医院を処理（実装時はClaude CodeのWebFetch/WebSearchツールと連携）
    print("\n医院データを処理中...\n")
    # 本スクリプトはテンプレート。実装時にはClaude Code内で実行
    collector.process_clinics(clinics)

    # Step 3: 結果をCSV保存
    collector.save_results()

    # Step 4: サマリー表示
    collector.print_summary()

    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n中断されました")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 予期しないエラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
