#!/usr/bin/env python3
"""
データ品質検証スクリプト

【検証項目】
1. 重複率チェック（閾値: 10%）
2. データ完全性チェック（必須フィールド）
3. スコア分布の妥当性
4. 医院長名抽出率

【使用タイミング】
- データ収集後
- バッチ分割前
- 最終統合前
"""

import csv
import sys
from pathlib import Path
from typing import Dict, List, Set
from collections import Counter

class DataQualityValidator:
    """データ品質検証クラス"""

    def __init__(self, csv_file: str, max_duplicate_rate: float = 10.0):
        """
        Args:
            csv_file: 検証対象CSVファイル
            max_duplicate_rate: 許容する最大重複率（%）
        """
        self.csv_file = Path(csv_file)
        self.max_duplicate_rate = max_duplicate_rate
        self.rows: List[Dict] = []
        self.clinic_names: List[str] = []

        # 検証結果
        self.validation_passed = True
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def load_data(self):
        """CSVデータを読み込み"""
        print(f"📂 データ読み込み: {self.csv_file}")

        if not self.csv_file.exists():
            self.errors.append(f"ファイルが見つかりません: {self.csv_file}")
            self.validation_passed = False
            return

        with open(self.csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            self.rows = list(reader)
            self.clinic_names = [row.get('医院名', '') for row in self.rows]

        print(f"✓ 読み込み完了: {len(self.rows)}件")

    def check_duplicates(self):
        """重複率チェック"""
        print(f"\n🔍 重複率チェック（閾値: {self.max_duplicate_rate}%）")

        total = len(self.clinic_names)
        unique = len(set(self.clinic_names))
        duplicate_count = total - unique
        duplicate_rate = (duplicate_count / total * 100) if total > 0 else 0

        print(f"   総件数: {total}件")
        print(f"   ユニーク: {unique}件")
        print(f"   重複: {duplicate_count}件")
        print(f"   重複率: {duplicate_rate:.1f}%")

        if duplicate_rate > self.max_duplicate_rate:
            error_msg = f"❌ 重複率が高すぎます: {duplicate_rate:.1f}% > {self.max_duplicate_rate}%"
            self.errors.append(error_msg)
            self.validation_passed = False
            print(f"   {error_msg}")

            # 最も重複している医院を表示
            clinic_counts = Counter(self.clinic_names)
            top_duplicates = clinic_counts.most_common(5)

            print(f"\n   上位5件の重複医院:")
            for name, count in top_duplicates:
                print(f"      {name}: {count}回出現")

        else:
            print(f"   ✓ 重複率OK: {duplicate_rate:.1f}%")

    def check_completeness(self):
        """データ完全性チェック"""
        print(f"\n🔍 データ完全性チェック")

        required_fields = ['医院名', 'WebサイトURL', 'Google評価', 'レビュー件数']
        missing_counts = {field: 0 for field in required_fields}

        for row in self.rows:
            for field in required_fields:
                if not row.get(field) or row.get(field).strip() == '':
                    missing_counts[field] += 1

        for field, count in missing_counts.items():
            missing_rate = (count / len(self.rows) * 100) if len(self.rows) > 0 else 0

            if missing_rate > 10:
                warning_msg = f"⚠️ {field}の欠損率が高い: {missing_rate:.1f}%（{count}件）"
                self.warnings.append(warning_msg)
                print(f"   {warning_msg}")
            else:
                print(f"   ✓ {field}: 欠損率{missing_rate:.1f}%")

    def check_score_distribution(self):
        """スコア分布の妥当性チェック"""
        print(f"\n🔍 スコア分布チェック")

        if 'スコア' not in self.rows[0]:
            self.warnings.append("⚠️ スコア列が存在しません")
            return

        scores = [int(row.get('スコア', 0)) for row in self.rows if row.get('スコア', '').isdigit()]

        if not scores:
            self.warnings.append("⚠️ 有効なスコアデータがありません")
            return

        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)

        # スコア帯別集計
        high = sum(1 for s in scores if s >= 70)
        mid = sum(1 for s in scores if 40 <= s < 70)
        low = sum(1 for s in scores if s < 40)

        print(f"   平均スコア: {avg_score:.1f}点")
        print(f"   最高スコア: {max_score}点")
        print(f"   最低スコア: {min_score}点")
        print(f"\n   スコア帯別分布:")
        print(f"      70点以上: {high}件 ({high/len(scores)*100:.1f}%)")
        print(f"      40-69点: {mid}件 ({mid/len(scores)*100:.1f}%)")
        print(f"      40点未満: {low}件 ({low/len(scores)*100:.1f}%)")

        # 分布の妥当性チェック
        if high / len(scores) > 0.5:
            self.warnings.append("⚠️ 高スコア医院が50%以上（分布が偏っている可能性）")
        if low / len(scores) > 0.8:
            self.warnings.append("⚠️ 低スコア医院が80%以上（基準が厳しすぎる可能性）")

    def check_director_name_extraction(self):
        """医院長名抽出率チェック"""
        print(f"\n🔍 医院長名抽出率チェック")

        if '医院長名' not in self.rows[0]:
            self.warnings.append("⚠️ 医院長名列が存在しません")
            return

        extracted = sum(1 for row in self.rows if row.get('医院長名', '').strip())
        extraction_rate = (extracted / len(self.rows) * 100) if len(self.rows) > 0 else 0

        print(f"   医院長名抽出数: {extracted}件")
        print(f"   抽出率: {extraction_rate:.1f}%")

        if extraction_rate < 50:
            warning_msg = f"⚠️ 医院長名抽出率が低い: {extraction_rate:.1f}% < 50%"
            self.warnings.append(warning_msg)
            print(f"   {warning_msg}")
        else:
            print(f"   ✓ 抽出率OK: {extraction_rate:.1f}%")

    def validate(self) -> bool:
        """全検証を実行"""
        print(f"=" * 60)
        print(f"データ品質検証開始")
        print(f"=" * 60)

        self.load_data()

        if not self.validation_passed:
            return False

        self.check_duplicates()
        self.check_completeness()
        self.check_score_distribution()
        self.check_director_name_extraction()

        # 結果サマリー
        print(f"\n" + "=" * 60)
        print(f"検証結果サマリー")
        print(f"=" * 60)

        if self.errors:
            print(f"❌ エラー: {len(self.errors)}件")
            for error in self.errors:
                print(f"   - {error}")

        if self.warnings:
            print(f"⚠️  警告: {len(self.warnings)}件")
            for warning in self.warnings:
                print(f"   - {warning}")

        if self.validation_passed and not self.errors:
            print(f"✅ 検証合格: データ品質OK")
        else:
            print(f"❌ 検証不合格: 上記の問題を修正してください")

        print(f"=" * 60)

        return self.validation_passed and len(self.errors) == 0


# ========================================
# 使用例
# ========================================

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("使用方法: python validate_data_quality.py <csv_file> [max_duplicate_rate]")
        print("例: python validate_data_quality.py dental_leads.csv 10.0")
        sys.exit(1)

    csv_file = sys.argv[1]
    max_dup_rate = float(sys.argv[2]) if len(sys.argv) > 2 else 10.0

    validator = DataQualityValidator(csv_file, max_duplicate_rate=max_dup_rate)
    is_valid = validator.validate()

    sys.exit(0 if is_valid else 1)
