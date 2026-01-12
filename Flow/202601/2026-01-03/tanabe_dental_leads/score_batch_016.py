#!/usr/bin/env python3
"""
6次元スコアリング実行スクリプト - batch_016
田辺玩具向け歯科医院営業リスト

6つのスコアリング次元 (100点満点):
1. Web積極性 (0-20点): Webサイト有無、SNS連携数
2. 子ども対応力 (0-20点): 子ども対応、小児・矯正特化
3. コンテンツ活動 (0-20点): ブログ更新、写真枚数、営業時間充実
4. 信頼性 (0-20点): Google評価、レビュー件数
5. 医院規模 (0-10点): 医院規模データから推定
6. 営業時間対応力 (0-10点): 営業時間の充実度、土日対応
"""

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import re

class DentalScoringEngine:
    """6次元スコアリングエンジン"""

    def __init__(self):
        self.results = []
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def score_web_presence(self, clinic: Dict) -> float:
        """
        Web積極性スコア (0-20点)
        - Webサイト有無: 0-10点
        - SNS連携数: 0-10点
        """
        score = 0

        # Webサイト有無
        website_url = clinic.get('WebサイトURL', '').strip()
        if website_url and website_url != 'http://':
            score += 10

        # SNS連携数
        sns_fields = ['SNS連携']  # CSV内のSNS連携フィールド
        sns_count = 0

        # SNS連携フィールドから連携数を推定
        sns_value = clinic.get('SNS連携', '').strip()
        if sns_value and sns_value != '':
            # カンマ区切りやスペース区切りのSNS情報があれば数える
            sns_count = len([x for x in re.split(r'[,、]', sns_value) if x.strip()])

        if sns_count > 0:
            score += min(10, sns_count * 2)  # 最大10点

        return score

    def score_kids_friendliness(self, clinic: Dict) -> float:
        """
        子ども対応力スコア (0-20点)
        - 子ども対応力フィールド: 0-20点
        """
        score = 0

        # 子ども対応力スコアが直接ある場合
        kids_score_str = clinic.get('子ども対応力スコア', '').strip()
        if kids_score_str:
            try:
                kids_score = float(kids_score_str)
                # スケーリング: CSV値を20点満点に変換
                score = min(20, (kids_score / 30) * 20) if kids_score <= 30 else 20
            except ValueError:
                pass

        # 診療科目タグから小児・矯正を検出
        diagnosis_tags = clinic.get('診療科目タグ', '').lower()
        if 'pediatric' in diagnosis_tags or '小児' in diagnosis_tags:
            score = min(20, score + 10)
        if 'orthod' in diagnosis_tags or '矯正' in diagnosis_tags:
            score = min(20, score + 5)

        return score

    def score_content_activity(self, clinic: Dict) -> float:
        """
        コンテンツ活動スコア (0-20点)
        - ブログ更新日: 0-10点
        - 写真枚数: 0-10点
        """
        score = 0

        # ブログ更新日
        blog_date = clinic.get('ブログ更新日', '').strip()
        if blog_date:
            try:
                # 日付が最近かどうきか判定
                blog_datetime = datetime.strptime(blog_date, '%Y-%m-%d')
                days_ago = (datetime.now() - blog_datetime).days

                if days_ago <= 30:  # 30日以内なら満点
                    score += 10
                elif days_ago <= 90:  # 90日以内なら8点
                    score += 8
                elif days_ago <= 180:  # 180日以内なら5点
                    score += 5
                elif days_ago <= 365:  # 1年以内なら2点
                    score += 2
            except (ValueError, TypeError):
                pass

        # 写真枚数
        photo_count_str = clinic.get('写真枚数', '').strip()
        if photo_count_str:
            try:
                photo_count = int(photo_count_str)
                if photo_count >= 20:
                    score += 10
                elif photo_count >= 10:
                    score += 8
                elif photo_count >= 5:
                    score += 5
                elif photo_count > 0:
                    score += 2
            except ValueError:
                pass

        return score

    def score_trustworthiness(self, clinic: Dict) -> float:
        """
        信頼性スコア (0-20点)
        - Google評価: 0-10点
        - レビュー件数: 0-10点
        """
        score = 0

        # Google評価 (★)
        rating_str = clinic.get('評価', '').strip()
        if rating_str:
            try:
                rating = float(rating_str)
                # 評価の線形スケーリング (3.0-5.0 → 0-10点)
                if rating >= 4.5:
                    score += 10
                elif rating >= 4.0:
                    score += 8
                elif rating >= 3.5:
                    score += 6
                elif rating >= 3.0:
                    score += 3
            except ValueError:
                pass

        # レビュー件数
        review_count_str = clinic.get('レビュー件数', '').strip()
        if review_count_str:
            try:
                review_count = int(review_count_str)
                if review_count >= 100:
                    score += 10
                elif review_count >= 50:
                    score += 8
                elif review_count >= 20:
                    score += 6
                elif review_count >= 10:
                    score += 4
                elif review_count >= 5:
                    score += 2
            except ValueError:
                pass

        return score

    def score_clinic_scale(self, clinic: Dict) -> float:
        """
        医院規模スコア (0-10点)
        - 医院規模フィールドから推定
        """
        score = 0

        clinic_scale_str = clinic.get('医院規模', '').strip()
        if clinic_scale_str:
            try:
                clinic_scale = int(clinic_scale_str)
                # 規模が大きいほど高スコア
                if clinic_scale >= 30:
                    score = 10
                elif clinic_scale >= 20:
                    score = 8
                elif clinic_scale >= 10:
                    score = 6
                elif clinic_scale >= 5:
                    score = 4
                else:
                    score = 2
            except ValueError:
                score = 5  # デフォルト
        else:
            score = 5  # 不明の場合は中程度

        return score

    def score_availability(self, clinic: Dict) -> float:
        """
        営業時間対応力スコア (0-10点)
        - 営業時間の充実度から推定
        """
        score = 5  # デフォルト

        operating_hours = clinic.get('営業時間', '').strip().lower()

        if operating_hours and operating_hours != '':
            # 土日対応をチェック
            has_weekend = '土' in operating_hours or '日' in operating_hours

            # 夜間営業をチェック
            has_evening = any(hour in operating_hours for hour in ['18:', '19:', '20:', '21:'])

            # 朝早い営業をチェック
            has_early = '9:' in operating_hours or '8:' in operating_hours

            bonus = 0
            if has_weekend:
                bonus += 3
            if has_evening:
                bonus += 2
            if has_early:
                bonus += 2

            score = min(10, 5 + bonus)

        return score

    def calculate_total_score(self, clinic: Dict) -> Dict:
        """
        6次元全体スコアを計算
        """
        scores = {
            'web_presence': self.score_web_presence(clinic),
            'kids_friendliness': self.score_kids_friendliness(clinic),
            'content_activity': self.score_content_activity(clinic),
            'trustworthiness': self.score_trustworthiness(clinic),
            'clinic_scale': self.score_clinic_scale(clinic),
            'availability': self.score_availability(clinic)
        }

        total_score = sum(scores.values())

        return {
            'dimensions': scores,
            'total_score': total_score,
            'percentage': round((total_score / 100) * 100, 1)
        }

    def process_batch(self, csv_path: str) -> List[Dict]:
        """
        バッチCSVファイルを処理
        """
        clinics_scored = []

        try:
            with open(csv_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)

                for i, clinic in enumerate(reader, 1):
                    # スコア計算
                    scoring_result = self.calculate_total_score(clinic)

                    # 結果を構築
                    result = {
                        'rank': i,
                        'clinic_name': clinic.get('医院名', ''),
                        'clinic_director': clinic.get('医院長名', ''),
                        'phone': clinic.get('電話番号', ''),
                        'address': clinic.get('住所', ''),
                        'website_url': clinic.get('WebサイトURL', ''),
                        'google_maps_url': clinic.get('Google Maps URL', ''),
                        'rating': clinic.get('評価', ''),
                        'review_count': clinic.get('レビュー件数', ''),
                        'scoring': {
                            'web_presence': round(scoring_result['dimensions']['web_presence'], 1),
                            'kids_friendliness': round(scoring_result['dimensions']['kids_friendliness'], 1),
                            'content_activity': round(scoring_result['dimensions']['content_activity'], 1),
                            'trustworthiness': round(scoring_result['dimensions']['trustworthiness'], 1),
                            'clinic_scale': round(scoring_result['dimensions']['clinic_scale'], 1),
                            'availability': round(scoring_result['dimensions']['availability'], 1)
                        },
                        'total_score': round(scoring_result['total_score'], 1),
                        'percentage': scoring_result['percentage']
                    }

                    clinics_scored.append(result)

                    if i % 50 == 0:
                        print(f"  処理済: {i}件")

        except FileNotFoundError:
            print(f"エラー: ファイルが見つかりません: {csv_path}")
            return []

        return clinics_scored

    def generate_summary(self, results: List[Dict]) -> Dict:
        """
        スコアリング結果のサマリーを生成
        """
        if not results:
            return {}

        scores = [r['total_score'] for r in results]

        return {
            'total_clinics': len(results),
            'average_score': round(sum(scores) / len(scores), 1),
            'median_score': sorted(scores)[len(scores) // 2],
            'max_score': max(scores),
            'min_score': min(scores),
            'score_distribution': {
                'high': len([s for s in scores if s >= 70]),  # 高スコア (70+)
                'medium': len([s for s in scores if 40 <= s < 70]),  # 中スコア (40-69)
                'low': len([s for s in scores if s < 40])  # 低スコア (-39)
            }
        }

    def save_results(self, results: List[Dict], output_path: Optional[str] = None) -> str:
        """
        結果をJSONファイルに保存
        """
        if output_path is None:
            output_path = f"scoring_results_batch_016.json"

        summary = self.generate_summary(results)

        output_data = {
            'metadata': {
                'timestamp': self.timestamp,
                'batch_number': 16,
                'batch_file': 'batch_016_to_score.csv',
                'scoring_version': '6-dimensional',
                'total_points': 100
            },
            'summary': summary,
            'results': results
        }

        output_file = Path(output_path)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"✅ 結果を保存しました: {output_file}")
        return str(output_file)


def main():
    """メイン処理"""
    import sys

    # ファイルパス
    csv_file = "scoring_batches/batch_016_to_score.csv"
    output_file = "scoring_results_batch_016.json"

    # 実行
    print("=" * 60)
    print("6次元スコアリング実行 - Batch 016")
    print("=" * 60)

    engine = DentalScoringEngine()

    print(f"\n📂 入力ファイル: {csv_file}")
    print("📊 スコアリング次元:")
    print("  1. Web積極性 (0-20点)")
    print("  2. 子ども対応力 (0-20点)")
    print("  3. コンテンツ活動 (0-20点)")
    print("  4. 信頼性 (0-20点)")
    print("  5. 医院規模 (0-10点)")
    print("  6. 営業時間対応力 (0-10点)")
    print("  合計: 100点満点\n")

    # バッチ処理
    print("⏳ スコアリング実行中...\n")
    results = engine.process_batch(csv_file)

    if results:
        print(f"\n✅ {len(results)}件のスコアリング完了\n")

        # 結果保存
        saved_path = engine.save_results(results, output_file)

        # サマリー表示
        summary = engine.generate_summary(results)
        print("\n" + "=" * 60)
        print("📊 スコアリングサマリー")
        print("=" * 60)
        print(f"総件数: {summary['total_clinics']}件")
        print(f"平均スコア: {summary['average_score']}点")
        print(f"中央値: {summary['median_score']}点")
        print(f"最高スコア: {summary['max_score']}点")
        print(f"最低スコア: {summary['min_score']}点")
        print("\nスコア分布:")
        print(f"  高スコア (70点以上): {summary['score_distribution']['high']}件 ({round(summary['score_distribution']['high']/summary['total_clinics']*100, 1)}%)")
        print(f"  中スコア (40-69点): {summary['score_distribution']['medium']}件 ({round(summary['score_distribution']['medium']/summary['total_clinics']*100, 1)}%)")
        print(f"  低スコア (39点以下): {summary['score_distribution']['low']}件 ({round(summary['score_distribution']['low']/summary['total_clinics']*100, 1)}%)")
        print("\n" + "=" * 60)

        # トップ5表示
        print("\n🏆 スコアトップ5:")
        for i, result in enumerate(sorted(results, key=lambda x: x['total_score'], reverse=True)[:5], 1):
            print(f"\n{i}. {result['clinic_name']}")
            print(f"   スコア: {result['total_score']}点")
            print(f"   評価: ★{result['rating']} | レビュー: {result['review_count']}件")
    else:
        print("❌ スコアリング処理に失敗しました")
        sys.exit(1)


if __name__ == '__main__':
    main()
