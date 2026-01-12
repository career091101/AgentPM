#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dental Clinic Scoring System
CSVファイルから医院スコアを読み込み、6次元のスコアリング検証を実施してJSON出力
"""

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class DentalClinicScorer:
    """歯科医院スコアリングシステム"""

    def __init__(self, csv_file: str):
        self.csv_file = Path(csv_file)
        self.clinics = []
        self.scoring_results = []
        self.errors = []

    def load_csv(self) -> None:
        """CSVファイルを読み込む"""
        if not self.csv_file.exists():
            raise FileNotFoundError(f"CSVファイルが見つかりません: {self.csv_file}")

        try:
            with open(self.csv_file, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                self.clinics = list(reader)
            print(f"✓ CSV読み込み完了: {len(self.clinics)}件")
        except Exception as e:
            raise ValueError(f"CSV読み込みエラー: {e}")

    def parse_score(self, value: str) -> Optional[int]:
        """スコア値をパース（エラーハンドリング付き）"""
        if not value or value.strip() == '':
            return None
        try:
            return int(value)
        except ValueError:
            return None

    def parse_rating(self, value: str) -> Optional[float]:
        """評価値をパース（浮動小数点数）"""
        if not value or value.strip() == '':
            return None
        try:
            return float(value)
        except ValueError:
            return None

    def parse_review_count(self, value: str) -> int:
        """レビュー件数をパース"""
        if not value or value.strip() == '':
            return 0
        try:
            return int(value)
        except ValueError:
            return 0

    def parse_sns_list(self, value: str) -> Dict[str, bool]:
        """SNS連携情報をパース（カンマ区切り）"""
        sns_map = {
            'Instagram': 'sns_instagram',
            'Facebook': 'sns_facebook',
            'LINE': 'sns_line',
            'Twitter': 'sns_twitter',
            'X': 'sns_twitter'  # X（旧Twitter）
        }

        result = {
            'sns_instagram': False,
            'sns_facebook': False,
            'sns_line': False,
            'sns_twitter': False
        }

        if not value or value.strip() == '':
            return result

        platforms = [p.strip() for p in value.split(',')]
        for platform in platforms:
            key = sns_map.get(platform)
            if key:
                result[key] = True

        return result

    def parse_blog_date(self, value: str) -> Optional[str]:
        """ブログ更新日をパース（YYYY-MM-DD形式）"""
        if not value or value.strip() == '':
            return None
        return value.strip()

    def calculate_scores(self, clinic_data: Dict) -> Dict:
        """6次元のスコアリング計算"""
        scores = {
            '基礎評価': 0,
            '来院患者数': 0,
            '子ども対応力': 0,
            'Web積極性': 0,
            '医院規模': 0,
            'ブログ活動': 0
        }

        # 1. 基礎評価 (20点) - Google評価ベース
        rating = self.parse_rating(clinic_data.get('評価', ''))
        if rating:
            # 4.5評価 → 18点の計算式
            scores['基礎評価'] = min(int(rating * 4), 20)
        else:
            scores['基礎評価'] = 0

        # 2. 来院患者数 (20点) - レビュー件数ベース
        review_count = self.parse_review_count(clinic_data.get('レビュー件数', ''))
        if review_count >= 100:
            scores['来院患者数'] = 20
        elif review_count >= 50:
            scores['来院患者数'] = 15
        elif review_count >= 20:
            scores['来院患者数'] = 10
        elif review_count >= 10:
            scores['来院患者数'] = 5
        else:
            scores['来院患者数'] = 0

        # 3. 子ども対応力 (30点)
        # CSVから既に計算済みの値を使用
        kids_score = self.parse_score(clinic_data.get('子ども対応力スコア', ''))
        if kids_score is not None:
            scores['子ども対応力'] = min(kids_score, 30)
        else:
            # 医院名から判定
            clinic_name = clinic_data.get('医院名', '')
            kids_keywords = ['小児', 'こども', '子ども', 'キッズ', '矯正']
            if any(keyword in clinic_name for keyword in kids_keywords):
                scores['子ども対応力'] = 25
            else:
                scores['子ども対応力'] = 0

        # 4. Web積極性 (15点) - SNS連携
        sns_data = self.parse_sns_list(clinic_data.get('SNS連携', ''))
        sns_count = sum(1 for v in sns_data.values() if v)
        scores['Web積極性'] = min(sns_count * 5, 15)

        # 5. 医院規模 (10点)
        has_operating_hours = bool(clinic_data.get('営業時間', '').strip())
        photo_count = self.parse_review_count(clinic_data.get('写真枚数', ''))

        size_score = 0
        if has_operating_hours:
            size_score += 5
        if photo_count >= 10:
            size_score += 5
        scores['医院規模'] = min(size_score, 10)

        # 6. ブログ活動 (5点) - ブログ更新日ベース
        blog_date = self.parse_blog_date(clinic_data.get('ブログ更新日', ''))
        if blog_date:
            try:
                from datetime import date, timedelta
                blog_update = datetime.strptime(blog_date, '%Y-%m-%d').date()
                today = date.today()
                days_diff = (today - blog_update).days

                if days_diff <= 30:
                    scores['ブログ活動'] = 5
                elif days_diff <= 60:
                    scores['ブログ活動'] = 4
                elif days_diff <= 90:
                    scores['ブログ活動'] = 3
                elif days_diff <= 180:
                    scores['ブログ活動'] = 2
                elif days_diff <= 365:
                    scores['ブログ活動'] = 1
                else:
                    scores['ブログ活動'] = 0
            except ValueError:
                scores['ブログ活動'] = 0
        else:
            scores['ブログ活動'] = 0

        return scores

    def process_clinics(self) -> None:
        """全医院をスコアリング"""
        print(f"\n📊 スコアリング処理開始...")

        for idx, clinic_data in enumerate(self.clinics, 1):
            try:
                clinic_name = clinic_data.get('医院名', 'Unknown')

                # スコア計算
                calculated_scores = self.calculate_scores(clinic_data)
                total_score = sum(calculated_scores.values())

                # SNS連携情報を抽出
                sns_data = self.parse_sns_list(clinic_data.get('SNS連携', ''))

                # 結果を記録
                result = {
                    'clinic_name': clinic_name,
                    'director_name': clinic_data.get('医院長名') or None,
                    'total_score': total_score,
                    'scores': calculated_scores,
                    'website_analysis': {
                        'sns_instagram': sns_data['sns_instagram'],
                        'sns_facebook': sns_data['sns_facebook'],
                        'sns_line': sns_data['sns_line'],
                        'sns_twitter': sns_data['sns_twitter'],
                        'operating_hours': clinic_data.get('営業時間') or None,
                        'blog_updated': clinic_data.get('ブログ更新日') or None,
                    },
                    'raw_data': {
                        'rating': self.parse_rating(clinic_data.get('評価')),
                        'user_ratings_total': self.parse_review_count(clinic_data.get('レビュー件数')),
                        'formatted_address': clinic_data.get('住所') or None,
                        'formatted_phone_number': clinic_data.get('電話番号') or None,
                        'website': clinic_data.get('WebサイトURL') or None,
                    }
                }

                self.scoring_results.append(result)

                # 進捗表示（50件ごと）
                if idx % 50 == 0:
                    print(f"   処理中: {idx}/{len(self.clinics)}件")

            except Exception as e:
                print(f"   ✗ エラー（{idx}）: {clinic_data.get('医院名', 'Unknown')} - {e}")
                self.errors.append({
                    'clinic_name': clinic_data.get('医院名', 'Unknown'),
                    'error': str(e),
                    'index': idx
                })

        print(f"✓ スコアリング完了: {len(self.scoring_results)}件")
        if self.errors:
            print(f"✗ エラー: {len(self.errors)}件")

    def save_json(self, output_path: Optional[str] = None) -> str:
        """JSON形式で出力"""
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f'scoring_results_batch_001_{timestamp}.json'

        output_data = {
            'metadata': {
                'batch_file': self.csv_file.name,
                'total_clinics': len(self.clinics),
                'processed_clinics': len(self.scoring_results),
                'errors': len(self.errors),
                'timestamp': datetime.now().isoformat(),
                'scoring_version': '1.0.0'
            },
            'results': self.scoring_results,
            'errors': self.errors if self.errors else []
        }

        output_file = Path(output_path)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"\n✓ JSON出力完了: {output_file}")
        print(f"   ファイルサイズ: {output_file.stat().st_size:,} bytes")

        return str(output_file)

    def print_statistics(self) -> None:
        """スコアリング統計を表示"""
        if not self.scoring_results:
            print("スコアリング結果がありません")
            return

        total_scores = [r['total_score'] for r in self.scoring_results]

        print(f"\n📈 スコアリング統計:")
        print(f"   平均スコア: {sum(total_scores) / len(total_scores):.1f}/100")
        print(f"   最高スコア: {max(total_scores)}/100")
        print(f"   最低スコア: {min(total_scores)}/100")

        # スコア分布
        score_ranges = {
            '90-100': 0,
            '80-89': 0,
            '70-79': 0,
            '60-69': 0,
            '50-59': 0,
            '0-49': 0
        }

        for score in total_scores:
            if score >= 90:
                score_ranges['90-100'] += 1
            elif score >= 80:
                score_ranges['80-89'] += 1
            elif score >= 70:
                score_ranges['70-79'] += 1
            elif score >= 60:
                score_ranges['60-69'] += 1
            elif score >= 50:
                score_ranges['50-59'] += 1
            else:
                score_ranges['0-49'] += 1

        print(f"\n   スコア分布:")
        for range_key, count in score_ranges.items():
            percentage = count / len(total_scores) * 100
            print(f"   {range_key}: {count}件 ({percentage:.1f}%)")


def main():
    """メイン処理"""
    # CSVファイルパス
    csv_file = 'scoring_batches/batch_001_to_score.csv'

    # スコアリング実行
    scorer = DentalClinicScorer(csv_file)
    scorer.load_csv()
    scorer.process_clinics()
    scorer.print_statistics()

    # JSON出力
    output_file = scorer.save_json()

    print(f"\n✅ 処理完了!")
    print(f"   出力ファイル: {output_file}")


if __name__ == '__main__':
    main()
