#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
6次元スコアリング実装 - Batch 020
医院のガチャガチャ導入意欲を複合的に評価
"""

import csv
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any

class DentalClinicScorer:
    """歯科医院の6次元スコアリングエンジン"""

    def __init__(self):
        """スコアリングパラメータの初期化"""
        self.six_dimensions = {
            '子ども対応力': {
                'weight': 20,
                'description': '子ども患者への対応施設・サービス'
            },
            'デジタル活動': {
                'weight': 20,
                'description': 'Web・SNS・ブログなどのデジタル展開'
            },
            '医院規模': {
                'weight': 15,
                'description': '医院の施設規模と診療能力'
            },
            'ブランド価値': {
                'weight': 15,
                'description': 'Googleレビュー評価と認知度'
            },
            '営業積極性': {
                'weight': 15,
                'description': '営業展開・マーケティング活動'
            },
            '患者基盤': {
                'weight': 15,
                'description': '来院患者数と患者定着率'
            }
        }

    def calculate_kids_care_score(self, row: Dict[str, str]) -> Tuple[float, Dict[str, Any]]:
        """
        子ども対応力スコア（0-20点）

        指標:
        - 子ども対応力フラグ（0-30）: 医院が子ども対応を謳っているか
        - 診療科目タグに「dentist」含有: +5点
        """
        score = 0
        details = {}

        # 子ども対応力フラグ（0-30のスケールを0-10点に正規化）
        kids_flag = float(row.get('子ども対応力', 0) or 0)
        kids_flag_score = min(10, (kids_flag / 30) * 10)
        score += kids_flag_score
        details['子ども対応力フラグ'] = kids_flag_score

        # 診療科目タグに「dentist」含有で+5点
        tags = row.get('診療科目タグ', '').lower()
        if 'dentist' in tags:
            score += 5
            details['診療科目(歯科医)'] = 5

        # 写真枚数で加点（子ども対応医院は通常、施設写真が充実）
        photo_count = int(row.get('写真枚数', 0) or 0)
        if photo_count >= 5:
            photo_score = min(5, photo_count / 2)
            score += photo_score
            details['写真枚数'] = photo_score

        # 営業時間が「月-土」で+3点（休日診療で子ども対応強化）
        hours = row.get('営業時間', '')
        if '月-土' in hours:
            score += 3
            details['営業時間(平日)'] = 3

        details['合計'] = min(20, score)
        return min(20, score), details

    def calculate_digital_activity_score(self, row: Dict[str, str]) -> Tuple[float, Dict[str, Any]]:
        """
        デジタル活動スコア（0-20点）

        指標:
        - Webサイト有無: +8点
        - ブログ更新日（過去6ヶ月以内）: +6点
        - SNS連携（複数プラットフォーム）: +3点/プラットフォーム
        - Google Maps URL: +3点
        """
        score = 0
        details = {}

        # Webサイト有無
        website_url = row.get('WebサイトURL', '').strip()
        if website_url:
            score += 8
            details['Webサイト'] = 8

        # ブログ更新日（過去6ヶ月以内で加点）
        blog_date = row.get('ブログ更新日', '').strip()
        if blog_date:
            try:
                # ISO形式またはYYYY-MM-DD形式を想定
                blog_datetime = datetime.fromisoformat(blog_date.replace('/', '-'))
                days_since = (datetime.now() - blog_datetime).days
                if days_since <= 180:  # 6ヶ月以内
                    blog_score = max(2, 6 - (days_since / 30))  # 最低2点
                    score += blog_score
                    details['ブログ活動'] = blog_score
            except:
                pass

        # SNS連携（複数プラットフォーム）
        sns_count = 0
        sns_score = 0
        for sns_type in ['Instagram', 'Facebook', 'Twitter', 'LINE']:
            sns_col = f'SNS_{sns_type}' if f'SNS_{sns_type}' in row else None
            # 列が存在しない場合、SNS連携列をチェック
            if sns_col is None and 'SNS連携' in row:
                if sns_type.lower() in row.get('SNS連携', '').lower():
                    sns_count += 1

        sns_score = min(12, sns_count * 3)  # 最大4プラットフォーム = 12点
        if sns_score > 0:
            score += sns_score
            details['SNS連携'] = sns_score

        # Google Maps URL
        maps_url = row.get('Google Maps URL', '').strip()
        if maps_url:
            score += 3
            details['Google Maps'] = 3

        details['合計'] = min(20, score)
        return min(20, score), details

    def calculate_clinic_size_score(self, row: Dict[str, str]) -> Tuple[float, Dict[str, Any]]:
        """
        医院規模スコア（0-15点）

        指標:
        - 医院規模フラグ（0-30）: 施設規模を反映
        - 診療科目タグの複雑性: 専門分野が多いほど高点
        - 営業時間の充実度: 診療時間が長いほど高点
        """
        score = 0
        details = {}

        # 医院規模フラグ（0-30のスケールを0-10点に正規化）
        size_flag = float(row.get('医院規模', 0) or 0)
        size_flag_score = min(8, (size_flag / 30) * 8)
        score += size_flag_score
        details['医院規模フラグ'] = size_flag_score

        # 診療科目タグの複雑性（タグ数が多いほど加点）
        tags = row.get('診療科目タグ', '').split(',')
        tag_score = min(4, len(tags) * 0.5)
        score += tag_score
        details['診療科目の多様性'] = tag_score

        # 営業時間の充実度（18:00以降営業で加点）
        hours = row.get('営業時間', '')
        if '19:00' in hours or '20:00' in hours or '21:00' in hours:
            score += 3
            details['営業時間(夜間)'] = 3

        details['合計'] = min(15, score)
        return min(15, score), details

    def calculate_brand_value_score(self, row: Dict[str, str]) -> Tuple[float, Dict[str, Any]]:
        """
        ブランド価値スコア（0-15点）

        指標:
        - Google評価（1-5段階）: 0-10点
        - レビュー件数: 0-3点
        - Googleマップ登録済み: +2点
        """
        score = 0
        details = {}

        # Google評価（1-5段階を0-10点に変換）
        try:
            rating = float(row.get('評価', 0) or 0)
            rating_score = (rating / 5) * 10  # 5段階 → 10点
            score += rating_score
            details['Google評価'] = rating_score
        except:
            pass

        # レビュー件数（100件以上で満点3点）
        try:
            review_count = int(row.get('レビュー件数', 0) or 0)
            review_score = min(3, review_count / 50)  # 50件で1点、最大3点
            score += review_score
            details['レビュー件数'] = review_score
        except:
            pass

        # Googleマップ登録済み
        maps_url = row.get('Google Maps URL', '').strip()
        if maps_url:
            score += 2
            details['Googleマップ登録'] = 2

        details['合計'] = min(15, score)
        return min(15, score), details

    def calculate_business_aggressiveness_score(self, row: Dict[str, str]) -> Tuple[float, Dict[str, Any]]:
        """
        営業積極性スコア（0-15点）

        指標:
        - Web積極性フラグ（0-30）: マーケティング展開度
        - ブログ活動フラグ（0-30）: コンテンツマーケティング
        - Webサイト有無: +3点
        """
        score = 0
        details = {}

        # Web積極性フラグ（0-30のスケールを0-10点に正規化）
        web_flag = float(row.get('Web積極性', 0) or 0)
        web_flag_score = min(8, (web_flag / 30) * 8)
        score += web_flag_score
        details['Web積極性フラグ'] = web_flag_score

        # ブログ活動フラグ（0-30のスケールを0-5点に正規化）
        blog_flag = float(row.get('ブログ活動', 0) or 0)
        blog_flag_score = min(5, (blog_flag / 30) * 5)
        score += blog_flag_score
        details['ブログ活動'] = blog_flag_score

        # Webサイト有無
        website_url = row.get('WebサイトURL', '').strip()
        if website_url:
            score += 2
            details['Webサイト'] = 2

        details['合計'] = min(15, score)
        return min(15, score), details

    def calculate_patient_base_score(self, row: Dict[str, str]) -> Tuple[float, Dict[str, Any]]:
        """
        患者基盤スコア（0-15点）

        指標:
        - 来院患者数（0-30）: 患者数の多さ
        - 基礎評価（0-30）: 基本的な医院評価
        """
        score = 0
        details = {}

        # 来院患者数（0-30のスケールを0-8点に正規化）
        visitors = float(row.get('来院患者数', 0) or 0)
        visitors_score = min(8, (visitors / 30) * 8)
        score += visitors_score
        details['来院患者数'] = visitors_score

        # 基礎評価（0-30のスケールを0-7点に正規化）
        base_eval = float(row.get('基礎評価', 0) or 0)
        base_eval_score = min(7, (base_eval / 30) * 7)
        score += base_eval_score
        details['基礎評価'] = base_eval_score

        details['合計'] = min(15, score)
        return min(15, score), details

    def calculate_total_score(self, six_dimension_scores: Dict[str, float]) -> float:
        """
        6次元スコアを加重平均で統合（100点満点）

        各次元の重み:
        - 子ども対応力: 20%
        - デジタル活動: 20%
        - 医院規模: 15%
        - ブランド価値: 15%
        - 営業積極性: 15%
        - 患者基盤: 15%
        """
        weighted_sum = 0
        total_weight = 0

        weights = {
            '子ども対応力': 20,
            'デジタル活動': 20,
            '医院規模': 15,
            'ブランド価値': 15,
            '営業積極性': 15,
            '患者基盤': 15
        }

        for dimension, score in six_dimension_scores.items():
            weight = weights.get(dimension, 0)
            weighted_sum += (score / 20) * weight if dimension in ['子ども対応力', 'デジタル活動'] else (score / 15) * weight
            total_weight += weight

        # より簡潔な計算：各次元を正規化してから重み付け
        normalized_scores = {
            '子ども対応力': (six_dimension_scores.get('子ども対応力', 0) / 20) * 100,
            'デジタル活動': (six_dimension_scores.get('デジタル活動', 0) / 20) * 100,
            '医院規模': (six_dimension_scores.get('医院規模', 0) / 15) * 100,
            'ブランド価値': (six_dimension_scores.get('ブランド価値', 0) / 15) * 100,
            '営業積極性': (six_dimension_scores.get('営業積極性', 0) / 15) * 100,
            '患者基盤': (six_dimension_scores.get('患者基盤', 0) / 15) * 100
        }

        total = sum(normalized_scores.values()) / len(normalized_scores)
        return round(total, 2)

    def score_clinic(self, row: Dict[str, str]) -> Dict[str, Any]:
        """
        単一医院の6次元スコアリング実行
        """
        results = {
            'clinic_name': row.get('医院名', 'Unknown'),
            'phone': row.get('電話番号', ''),
            'address': row.get('住所', ''),
            'website': row.get('WebサイトURL', ''),
            'scores': {},
            'details': {},
            'total_score': 0
        }

        # 6次元スコアを計算
        scores = {}
        details = {}

        score, detail = self.calculate_kids_care_score(row)
        scores['子ども対応力'] = score
        details['子ども対応力'] = detail

        score, detail = self.calculate_digital_activity_score(row)
        scores['デジタル活動'] = score
        details['デジタル活動'] = detail

        score, detail = self.calculate_clinic_size_score(row)
        scores['医院規模'] = score
        details['医院規模'] = detail

        score, detail = self.calculate_brand_value_score(row)
        scores['ブランド価値'] = score
        details['ブランド価値'] = detail

        score, detail = self.calculate_business_aggressiveness_score(row)
        scores['営業積極性'] = score
        details['営業積極性'] = detail

        score, detail = self.calculate_patient_base_score(row)
        scores['患者基盤'] = score
        details['患者基盤'] = detail

        results['scores'] = scores
        results['details'] = details
        results['total_score'] = self.calculate_total_score(scores)

        return results


def main():
    """メイン処理"""

    # ファイルパスの設定
    csv_file = Path('/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads/scoring_batches/batch_020_to_score.csv')
    output_dir = Path('/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads')
    output_file = output_dir / 'scoring_results_batch_020.json'

    if not csv_file.exists():
        print(f"❌ エラー: ファイルが見つかりません: {csv_file}")
        return 1

    # スコアラーの初期化
    scorer = DentalClinicScorer()

    # CSVファイルを読み込み
    print(f"📖 読み込み中: {csv_file}")
    clinics = []
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        clinics = list(reader)

    print(f"📊 総件数: {len(clinics)}件")

    # スコアリング実行
    print(f"\n🔄 スコアリング実行中...\n")
    results = {
        'metadata': {
            'timestamp': datetime.now().isoformat(),
            'source_file': str(csv_file.name),
            'total_clinics': len(clinics),
            'scoring_method': '6次元複合評価（100点満点）',
            'dimensions': list(scorer.six_dimensions.keys())
        },
        'clinics': []
    }

    # 医院ごとにスコアリング
    for i, clinic in enumerate(clinics, 1):
        clinic_name = clinic.get('医院名', 'Unknown')
        clinic_result = scorer.score_clinic(clinic)
        results['clinics'].append(clinic_result)

        # 進捗表示（50件ごと）
        if i % 50 == 0:
            print(f"  ✓ {i}/{len(clinics)} 件処理済み")

    # スコア統計の計算
    all_scores = [c['total_score'] for c in results['clinics']]
    results['metadata']['statistics'] = {
        'average_score': round(sum(all_scores) / len(all_scores), 2),
        'max_score': max(all_scores),
        'min_score': min(all_scores),
        'median_score': round(sorted(all_scores)[len(all_scores)//2], 2),
        'high_potential_count': len([s for s in all_scores if s >= 70]),
        'medium_potential_count': len([s for s in all_scores if 50 <= s < 70]),
        'low_potential_count': len([s for s in all_scores if s < 50])
    }

    # JSON出力
    print(f"\n💾 JSON出力中: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # 統計情報の表示
    print(f"\n✅ スコアリング完了\n")
    print(f"📊 統計情報:")
    print(f"   平均スコア: {results['metadata']['statistics']['average_score']:.2f}点")
    print(f"   最高スコア: {results['metadata']['statistics']['max_score']:.2f}点")
    print(f"   最低スコア: {results['metadata']['statistics']['min_score']:.2f}点")
    print(f"   中央値: {results['metadata']['statistics']['median_score']:.2f}点")
    print(f"\n🎯 ガチャガチャ導入意欲別:")
    print(f"   🔥 高い（70点以上）: {results['metadata']['statistics']['high_potential_count']}件")
    print(f"   ⭐ 中程度（50-69点）: {results['metadata']['statistics']['medium_potential_count']}件")
    print(f"   💤 低い（50点未満）: {results['metadata']['statistics']['low_potential_count']}件")

    # トップ10医院の表示
    print(f"\n🏆 スコアTOP 10医院:")
    sorted_clinics = sorted(results['clinics'], key=lambda x: x['total_score'], reverse=True)
    for rank, clinic in enumerate(sorted_clinics[:10], 1):
        print(f"   {rank}. {clinic['clinic_name']}: {clinic['total_score']:.2f}点")

    print(f"\n📂 出力ファイル: {output_file}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
