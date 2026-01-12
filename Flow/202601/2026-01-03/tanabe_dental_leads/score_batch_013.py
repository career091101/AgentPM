#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Batch 013 - 6次元スコアリング実行スクリプト
目的: CSV データを読み込み、6次元評価を実施して JSON 出力

評価軸（100点満点）:
1. Web積極性（15点）- WebサイトURL, SNS連携（Instagram/Facebook/LINE/Twitter）, ブログ更新
2. 子ども対応力（20点）- 子ども向けコンテンツ, 子ども向け装飾
3. 信頼度指標（20点）- Googleレビュー評価, レビュー件数
4. 医院基盤（20点）- 来院患者数, 医院規模
5. デジタル成熟度（15点）- ブログ活動, 写真掲載, Google Maps登録
6. ガチャガチャ親和性（10点）- 子ども対応+親の満足度（評価+患者数）

合計: 100点
"""

import csv
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Tuple


class DentalScoringEngine:
    """6次元スコアリングエンジン"""

    def __init__(self):
        self.results = {}
        self.errors = []
        self.stats = {
            'total': 0,
            'scored': 0,
            'errors': 0,
            'average_score': 0.0,
            'score_distribution': {}
        }

    def score_web_activity(self, row: Dict[str, str]) -> Tuple[int, Dict]:
        """1. Web積極性（15点）"""
        score = 0
        details = {}

        # WebサイトURL有無（5点）
        website_url = row.get('WebサイトURL', '').strip()
        details['has_website'] = bool(website_url)
        if website_url:
            score += 5

        # SNS連携（8点：各2点）
        sns_score = 0
        sns_details = {}

        for platform in ['Instagram', 'Facebook', 'Line', 'Twitter']:
            key = f'SNS_{platform.lower()}'
            has_sns = row.get(key, '').lower() in ['yes', 'true', '1', 'o', '◎']
            sns_details[platform.lower()] = has_sns
            if has_sns:
                sns_score += 2

        details['sns'] = sns_details
        details['sns_score'] = min(8, sns_score)
        score += details['sns_score']

        # ブログ活動（2点）
        blog_activity = row.get('ブログ活動', '').strip().lower()
        details['blog_active'] = blog_activity in ['yes', 'true', '1', 'o', '◎']
        if details['blog_active']:
            score += 2

        details['total'] = score
        return min(15, score), details

    def score_kids_capability(self, row: Dict[str, str]) -> Tuple[int, Dict]:
        """2. 子ども対応力（20点）"""
        score = 0
        details = {}

        # CSV の「子ども対応力」列（最大15点）
        kids_score_str = row.get('子ども対応力', '0').strip()
        try:
            csv_kids_score = int(kids_score_str) if kids_score_str else 0
            csv_kids_score = min(30, max(0, csv_kids_score))  # 0-30 にクリップ
        except ValueError:
            csv_kids_score = 0

        # CSV スコアから 20 点満点に正規化
        details['csv_score'] = csv_kids_score
        details['normalized_score'] = int((csv_kids_score / 30) * 20) if csv_kids_score > 0 else 0
        score += details['normalized_score']

        # 診療科目タグから「小児」「矯正」などを検出（加点5点まで）
        tags = row.get('診療科目タグ', '').lower()
        kids_keywords = ['pediatric', 'children', 'child', 'ortho', '小児', '矯正', 'キッズ']
        kids_tag_match = any(kw in tags for kw in kids_keywords)

        details['kids_tags'] = kids_tag_match
        if kids_tag_match and score < 20:
            tag_bonus = 5
            details['tag_bonus'] = tag_bonus
            score = min(20, score + tag_bonus)
        else:
            details['tag_bonus'] = 0

        details['total'] = score
        return min(20, score), details

    def score_trust_indicators(self, row: Dict[str, str]) -> Tuple[int, Dict]:
        """3. 信頼度指標（20点）"""
        score = 0
        details = {}

        # Google Maps 評価（最大12点）
        try:
            rating = float(row.get('評価', '0').strip() or '0')
            rating = min(5.0, max(0.0, rating))
        except ValueError:
            rating = 0.0

        details['google_rating'] = rating
        rating_score = int((rating / 5.0) * 12)
        details['rating_score'] = rating_score
        score += rating_score

        # レビュー件数（最大8点）
        try:
            review_count = int(row.get('レビュー件数', '0').strip() or '0')
        except ValueError:
            review_count = 0

        details['review_count'] = review_count
        if review_count >= 500:
            review_score = 8
        elif review_count >= 200:
            review_score = 6
        elif review_count >= 100:
            review_score = 4
        elif review_count >= 20:
            review_score = 2
        else:
            review_score = 0

        details['review_score'] = review_score
        score += review_score

        details['total'] = score
        return min(20, score), details

    def score_clinic_foundation(self, row: Dict[str, str]) -> Tuple[int, Dict]:
        """4. 医院基盤（20点）"""
        score = 0
        details = {}

        # 来院患者数（最大12点）
        try:
            patient_count = int(row.get('来院患者数', '0').strip() or '0')
        except ValueError:
            patient_count = 0

        details['patient_count'] = patient_count
        if patient_count >= 30:
            patient_score = 12
        elif patient_count >= 20:
            patient_score = 9
        elif patient_count >= 15:
            patient_score = 6
        elif patient_count >= 5:
            patient_score = 3
        else:
            patient_score = 0

        details['patient_score'] = patient_score
        score += patient_score

        # 医院規模（最大8点）
        try:
            clinic_size = int(row.get('医院規模', '0').strip() or '0')
        except ValueError:
            clinic_size = 0

        details['clinic_size'] = clinic_size
        if clinic_size >= 20:
            size_score = 8
        elif clinic_size >= 10:
            size_score = 6
        elif clinic_size >= 5:
            size_score = 3
        else:
            size_score = 0

        details['size_score'] = size_score
        score += size_score

        details['total'] = score
        return min(20, score), details

    def score_digital_maturity(self, row: Dict[str, str]) -> Tuple[int, Dict]:
        """5. デジタル成熟度（15点）"""
        score = 0
        details = {}

        # ブログ更新（最大7点）
        blog_activity = row.get('ブログ活動', '').strip().lower()
        details['blog_active'] = blog_activity in ['yes', 'true', '1', 'o', '◎']
        blog_score = 0

        if details['blog_active']:
            # ブログ更新日を判定
            blog_date_str = row.get('ブログ更新日', '').strip()
            if blog_date_str:
                # 直近 7 日以内なら 7点、30日以内なら 5点、それ以外は 3点
                try:
                    # 簡易判定（日付情報がない場合は 3 点）
                    blog_score = 3
                except:
                    blog_score = 0
            else:
                blog_score = 3

        details['blog_score'] = blog_score
        score += blog_score

        # 写真掲載（最大5点）
        try:
            photo_count = int(row.get('写真枚数', '0').strip() or '0')
        except ValueError:
            photo_count = 0

        details['photo_count'] = photo_count
        if photo_count >= 50:
            photo_score = 5
        elif photo_count >= 20:
            photo_score = 4
        elif photo_count >= 10:
            photo_score = 3
        elif photo_count > 0:
            photo_score = 1
        else:
            photo_score = 0

        details['photo_score'] = photo_score
        score += photo_score

        # Google Maps 登録（最大3点）
        google_maps = row.get('Google Maps URL', '').strip()
        details['google_maps_registered'] = bool(google_maps)
        google_score = 3 if google_maps else 0

        details['google_score'] = google_score
        score += google_score

        details['total'] = score
        return min(15, score), details

    def score_gacha_affinity(self, kids_score: int, trust_score: int,
                             patient_count: int, review_count: int) -> Tuple[int, Dict]:
        """6. ガチャガチャ親和性（10点）
        = 子ども対応力の高さ × 親の信頼度（評価+患者数）
        """
        score = 0
        details = {}

        # 子ども対応力ウェイト（最大6点）
        kids_weight = min(6, int((kids_score / 20) * 6))
        details['kids_weight'] = kids_weight
        score += kids_weight

        # 親の信頼度（最大4点）
        # = Google評価 + 患者数（正規化）
        trust_weight = min(4, int((trust_score / 20) * 2) + int(min(2, patient_count / 30)))
        details['trust_weight'] = trust_weight
        score += trust_weight

        details['total'] = score
        return min(10, score), details

    def score_clinic(self, row: Dict[str, str]) -> Dict[str, Any]:
        """医院を 6 次元評価"""

        clinic_name = row.get('医院名', 'Unknown')

        # 6次元スコアリング
        web_score, web_details = self.score_web_activity(row)
        kids_score, kids_details = self.score_kids_capability(row)
        trust_score, trust_details = self.score_trust_indicators(row)
        foundation_score, foundation_details = self.score_clinic_foundation(row)
        maturity_score, maturity_details = self.score_digital_maturity(row)
        gacha_score, gacha_details = self.score_gacha_affinity(
            kids_score, trust_score,
            trust_details.get('review_count', 0),  # patient_count の代わりに review_count
            trust_details.get('review_count', 0)
        )

        # 総合スコア（100点満点）
        total_score = (web_score + kids_score + trust_score +
                      foundation_score + maturity_score + gacha_score)

        return {
            'clinic_name': clinic_name,
            'postal_code': row.get('郵便番号', ''),
            'address': row.get('住所', ''),
            'phone': row.get('電話番号', ''),
            'website_url': row.get('WebサイトURL', ''),
            'director_name': row.get('医院長名', ''),
            'scores': {
                'web_activity': {
                    'score': web_score,
                    'details': web_details,
                    'max': 15
                },
                'kids_capability': {
                    'score': kids_score,
                    'details': kids_details,
                    'max': 20
                },
                'trust_indicators': {
                    'score': trust_score,
                    'details': trust_details,
                    'max': 20
                },
                'clinic_foundation': {
                    'score': foundation_score,
                    'details': foundation_details,
                    'max': 20
                },
                'digital_maturity': {
                    'score': maturity_score,
                    'details': maturity_details,
                    'max': 15
                },
                'gacha_affinity': {
                    'score': gacha_score,
                    'details': gacha_details,
                    'max': 10
                }
            },
            'total_score': total_score,
            'percentage': f"{(total_score / 100) * 100:.1f}%",
            'grade': self._calculate_grade(total_score)
        }

    def _calculate_grade(self, score: int) -> str:
        """スコアを等級に変換"""
        if score >= 90:
            return 'S'
        elif score >= 80:
            return 'A'
        elif score >= 70:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'F'

    def process_csv(self, csv_path: str):
        """CSVファイルを処理"""
        csv_file = Path(csv_path)

        if not csv_file.exists():
            raise FileNotFoundError(f"CSVファイルが見つかりません: {csv_path}")

        print(f"📖 CSVファイル読み込み中: {csv_path}")

        try:
            with open(csv_file, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
        except Exception as e:
            raise Exception(f"CSV読み込みエラー: {e}")

        self.stats['total'] = len(rows)
        print(f"📊 総件数: {self.stats['total']}件")

        # スコアリング実行
        print(f"\n⏳ スコアリング実行中...")
        for i, row in enumerate(rows, 1):
            try:
                clinic_result = self.score_clinic(row)
                clinic_name = clinic_result['clinic_name']
                self.results[clinic_name] = clinic_result
                self.stats['scored'] += 1

                # 進捗表示
                if i % 50 == 0:
                    print(f"  {i}/{self.stats['total']} 完了")

            except Exception as e:
                self.stats['errors'] += 1
                error_entry = {
                    'row_number': i,
                    'clinic_name': row.get('医院名', 'Unknown'),
                    'error': str(e)
                }
                self.errors.append(error_entry)
                print(f"  ✗ エラー: {error_entry['clinic_name']} - {e}")

        print(f"\n✅ スコアリング完了: {self.stats['scored']}件")
        print(f"❌ エラー: {self.stats['errors']}件")

        # 統計情報を計算
        if self.results:
            scores = [r['total_score'] for r in self.results.values()]
            self.stats['average_score'] = sum(scores) / len(scores)

            # スコア分布
            for score in scores:
                grade = self._calculate_grade(score)
                self.stats['score_distribution'][grade] = \
                    self.stats['score_distribution'].get(grade, 0) + 1

    def save_json(self, output_path: str = None):
        """JSONファイルに保存"""
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f'scoring_results_batch_013.json'

        output_file = Path(output_path)

        output_data = {
            'metadata': {
                'batch_number': 13,
                'source_file': 'scoring_batches/batch_013_to_score.csv',
                'timestamp': datetime.now().isoformat(),
                'total_clinics': self.stats['total'],
                'scored_clinics': self.stats['scored'],
                'error_count': self.stats['errors'],
                'average_score': round(self.stats['average_score'], 1),
                'score_distribution': self.stats['score_distribution']
            },
            'scoring_dimensions': {
                '1_web_activity': {'max_score': 15, 'description': 'Web積極性'},
                '2_kids_capability': {'max_score': 20, 'description': '子ども対応力'},
                '3_trust_indicators': {'max_score': 20, 'description': '信頼度指標'},
                '4_clinic_foundation': {'max_score': 20, 'description': '医院基盤'},
                '5_digital_maturity': {'max_score': 15, 'description': 'デジタル成熟度'},
                '6_gacha_affinity': {'max_score': 10, 'description': 'ガチャガチャ親和性'}
            },
            'results': self.results,
            'errors': self.errors
        }

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, ensure_ascii=False, indent=2)

            print(f"\n✅ JSON保存完了: {output_file}")
            return str(output_file)

        except Exception as e:
            raise Exception(f"JSON保存エラー: {e}")

    def print_summary(self):
        """サマリーを表示"""
        print("\n" + "="*80)
        print("📊 スコアリング結果サマリー")
        print("="*80)

        print(f"\n📈 統計情報:")
        print(f"  総件数: {self.stats['total']}")
        print(f"  スコア対象: {self.stats['scored']}")
        print(f"  エラー: {self.stats['errors']}")
        print(f"  平均スコア: {self.stats['average_score']:.1f}/100")

        print(f"\n📊 等級分布:")
        for grade in ['S', 'A', 'B', 'C', 'D', 'F']:
            count = self.stats['score_distribution'].get(grade, 0)
            percentage = (count / self.stats['scored'] * 100) if self.stats['scored'] > 0 else 0
            bar = '█' * int(percentage / 2)
            print(f"  {grade}: {count:3d}件 ({percentage:5.1f}%) {bar}")

        # Top 10 を表示
        print(f"\n🏆 スコア Top 10:")
        sorted_results = sorted(
            self.results.values(),
            key=lambda x: x['total_score'],
            reverse=True
        )[:10]

        for rank, result in enumerate(sorted_results, 1):
            print(f"  {rank:2d}. {result['clinic_name']:30s} {result['total_score']:3d}点 ({result['grade']})")

        print("\n" + "="*80)


def main():
    """メイン処理"""
    import sys

    csv_file = 'scoring_batches/batch_013_to_score.csv'

    if len(sys.argv) > 1:
        csv_file = sys.argv[1]

    try:
        # エンジン初期化
        engine = DentalScoringEngine()

        # CSV処理
        engine.process_csv(csv_file)

        # JSON保存
        output_file = engine.save_json()

        # サマリー表示
        engine.print_summary()

        print(f"\n✅ 処理完了: {output_file}")
        return 0

    except Exception as e:
        print(f"❌ エラー: {e}")
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main())
