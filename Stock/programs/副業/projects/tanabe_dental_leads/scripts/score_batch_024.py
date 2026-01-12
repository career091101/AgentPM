#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6次元スコアリングシステム（100点満点）
Batch 024用スコアリング処理
"""

import csv
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple


class DentalWebsiteScorer:
    """歯科医院ウェブサイト総合スコアリング"""

    def __init__(self):
        self.scoring_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def normalize_score(self, value: int, max_val: int = 100) -> float:
        """スコアを0-20点に正規化"""
        if max_val == 0:
            return 0
        normalized = (value / max_val) * 20
        return min(20, normalized)

    def calculate_dimension_1_credibility(self, row: Dict[str, str]) -> float:
        """
        次元1: 信頼性（20点）
        - Google評価（0-5★） → 0-10点
        - レビュー件数（0+） → 0-5点
        - 医院長名記載 → 0-5点
        """
        score = 0

        # Google評価: 4.5★以上で10点、3.5★以上で7点、3★以上で5点
        try:
            rating = float(row.get('評価', '0').replace('★', ''))
            if rating >= 4.5:
                score += 10
            elif rating >= 3.5:
                score += 7
            elif rating >= 3.0:
                score += 5
            else:
                score += 2
        except:
            score += 0

        # レビュー件数: 20件以上で5点、10件以上で3点、1件以上で1点
        try:
            reviews = int(row.get('レビュー件数', '0'))
            if reviews >= 20:
                score += 5
            elif reviews >= 10:
                score += 3
            elif reviews > 0:
                score += 1
        except:
            pass

        # 医院長名記載
        if row.get('医院長名', '').strip():
            score += 5

        return min(20, score)

    def calculate_dimension_2_web_presence(self, row: Dict[str, str]) -> float:
        """
        次元2: Web存在度（20点）
        - WebサイトURL → 0-8点
        - ブログ活動 → 0-6点
        - SNS連携 → 0-6点
        """
        score = 0

        # WebサイトURL
        url = row.get('WebサイトURL', '').strip()
        if url and len(url) > 10:
            score += 8
        elif url:
            score += 4

        # ブログ活動
        try:
            blog_score = int(row.get('ブログ活動', '0'))
            if blog_score > 0:
                score += min(6, blog_score * 2)
        except:
            pass

        # SNS連携
        sns = row.get('SNS連携', '').strip()
        if sns and sns != '0':
            score += 6

        return min(20, score)

    def calculate_dimension_3_children_service(self, row: Dict[str, str]) -> float:
        """
        次元3: 子ども対応力（20点）
        - 子ども対応力スコア → 0-10点
        - 来院患者数 → 0-5点
        - 診療科目に小児歯科含む → 0-5点
        """
        score = 0

        # 子ども対応力スコア
        try:
            children_score = int(row.get('子ども対応力スコア', '0'))
            if children_score > 0:
                score += min(10, children_score)
        except:
            pass

        # 来院患者数
        try:
            patients = int(row.get('来院患者数', '0'))
            if patients >= 5:
                score += 5
            elif patients >= 3:
                score += 3
            elif patients > 0:
                score += 1
        except:
            pass

        # 診療科目に小児歯科含むか
        tags = row.get('診療科目タグ', '').lower()
        if 'pediatric' in tags or '小児' in tags or 'children' in tags.lower():
            score += 5

        return min(20, score)

    def calculate_dimension_4_facility_quality(self, row: Dict[str, str]) -> float:
        """
        次元4: 設備・規模（20点）
        - 医院規模スコア → 0-10点
        - 写真枚数 → 0-10点
        """
        score = 0

        # 医院規模スコア
        try:
            scale = int(row.get('医院規模', '0'))
            score += min(10, int(scale / 2))
        except:
            pass

        # 写真枚数: 多いほど信頼度UP
        try:
            photos = int(row.get('写真枚数', '0'))
            if photos >= 10:
                score += 10
            elif photos >= 5:
                score += 7
            elif photos >= 1:
                score += 4
        except:
            pass

        return min(20, score)

    def calculate_dimension_5_active_engagement(self, row: Dict[str, str]) -> float:
        """
        次元5: アクティブさ（20点）
        - ブログ更新日（新しいほど加点） → 0-10点
        - Web積極性スコア → 0-10点
        """
        score = 0

        # ブログ更新日（新しいほど加点）
        blog_date = row.get('ブログ更新日', '').strip()
        if blog_date:
            try:
                # 更新日が記載されている = 積極的
                score += 10
            except:
                pass

        # Web積極性スコア
        try:
            web_activity = int(row.get('Web積極性', '0'))
            score += min(10, web_activity * 2)
        except:
            pass

        return min(20, score)

    def calculate_dimension_6_basic_quality(self, row: Dict[str, str]) -> float:
        """
        次元6: 基本品質（20点）
        - 基礎評価スコア → 0-10点
        - 住所・電話の完全性 → 0-10点
        """
        score = 0

        # 基礎評価スコア
        try:
            basic = int(row.get('基礎評価', '0'))
            score += min(10, basic)
        except:
            pass

        # 住所・電話・医院名の完全性
        completeness = 0
        if row.get('住所', '').strip():
            completeness += 1
        if row.get('電話番号', '').strip():
            completeness += 1
        if row.get('医院名', '').strip():
            completeness += 1
        if row.get('郵便番号', '').strip():
            completeness += 1

        score += completeness * 2.5  # 4/4で10点

        return min(20, score)

    def score_clinic(self, row: Dict[str, str]) -> Dict[str, Any]:
        """歯科医院全体をスコアリング"""

        # 6次元スコア計算
        d1_credibility = self.calculate_dimension_1_credibility(row)
        d2_web_presence = self.calculate_dimension_2_web_presence(row)
        d3_children = self.calculate_dimension_3_children_service(row)
        d4_facility = self.calculate_dimension_4_facility_quality(row)
        d5_engagement = self.calculate_dimension_5_active_engagement(row)
        d6_quality = self.calculate_dimension_6_basic_quality(row)

        # 総合スコア（100点満点）
        total_score = d1_credibility + d2_web_presence + d3_children + \
                      d4_facility + d5_engagement + d6_quality

        return {
            "clinic_name": row.get('医院名', '').strip(),
            "location": row.get('住所', '').strip(),
            "phone": row.get('電話番号', '').strip(),
            "website_url": row.get('WebサイトURL', '').strip(),
            "google_maps_url": row.get('Google Maps URL', '').strip(),
            "scores": {
                "dimension_1_credibility": round(d1_credibility, 1),
                "dimension_2_web_presence": round(d2_web_presence, 1),
                "dimension_3_children_service": round(d3_children, 1),
                "dimension_4_facility_quality": round(d4_facility, 1),
                "dimension_5_active_engagement": round(d5_engagement, 1),
                "dimension_6_basic_quality": round(d6_quality, 1)
            },
            "total_score": round(total_score, 1),
            "score_details": {
                "google_rating": row.get('評価', ''),
                "review_count": row.get('レビュー件数', ''),
                "clinic_director": row.get('医院長名', ''),
                "photos": row.get('写真枚数', ''),
                "blog_update": row.get('ブログ更新日', '')
            }
        }


def main():
    """メイン処理"""

    # パス設定
    base_dir = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads")
    input_csv = base_dir / "scoring_batches" / "batch_024_to_score.csv"
    output_json = base_dir / "scoring_results_batch_024.json"

    print(f"Starting batch 024 scoring...")
    print(f"Input: {input_csv}")
    print(f"Output: {output_json}")

    # スコアラー初期化
    scorer = DentalWebsiteScorer()

    # CSVを読み込みしてスコアリング
    results = {
        "batch": "024",
        "timestamp": scorer.scoring_date,
        "total_clinics": 0,
        "scoring_method": "6-dimensional assessment (100-point scale)",
        "dimension_definitions": {
            "1_credibility": "Google rating, review count, director info (20pts)",
            "2_web_presence": "Website URL, blog activity, SNS integration (20pts)",
            "3_children_service": "Children service score, patient diversity (20pts)",
            "4_facility_quality": "Facility scale, photos (20pts)",
            "5_active_engagement": "Blog updates, web activity (20pts)",
            "6_basic_quality": "Basic evaluation, completeness (20pts)"
        },
        "clinics": []
    }

    # CSV読み込み
    try:
        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0

            for row in reader:
                # スコアリング
                clinic_score = scorer.score_clinic(row)
                results["clinics"].append(clinic_score)

                count += 1
                if count % 50 == 0:
                    print(f"  Processed {count} clinics...")

        results["total_clinics"] = count

        # JSON出力
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        # サマリー統計
        if results["clinics"]:
            scores = [c["total_score"] for c in results["clinics"]]
            avg_score = sum(scores) / len(scores)
            max_score = max(scores)
            min_score = min(scores)

            print(f"\nScoring completed successfully!")
            print(f"Total clinics: {count}")
            print(f"Average score: {avg_score:.1f}/100")
            print(f"Max score: {max_score:.1f}/100")
            print(f"Min score: {min_score:.1f}/100")
            print(f"Output saved: {output_json}")

            # Top 10をリスト表示
            print(f"\nTop 10 clinics (by score):")
            sorted_clinics = sorted(results["clinics"],
                                  key=lambda x: x["total_score"],
                                  reverse=True)[:10]
            for i, clinic in enumerate(sorted_clinics, 1):
                print(f"  {i}. {clinic['clinic_name']}: {clinic['total_score']:.1f}/100")

    except Exception as e:
        print(f"Error processing CSV: {e}")
        raise


if __name__ == "__main__":
    main()
