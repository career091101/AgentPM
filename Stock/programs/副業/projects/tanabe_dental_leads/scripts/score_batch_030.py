#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6-Dimensional Dental Clinic Scoring System
Batch 030 Analysis: 100-point scale scoring for dental lead qualification
"""

import csv
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional


class DentalClinicScorer:
    """6-dimensional scoring system for dental clinics"""

    # 6 Dimensions with weights (total = 100%)
    DIMENSIONS = {
        "web_quality": {
            "weight": 20,
            "name": "Web技術力 (0-20点)",
            "description": "ウェブサイト品質・SNS連携・ブログ活動"
        },
        "market_presence": {
            "weight": 20,
            "name": "市場認知度 (0-20点)",
            "description": "Googleレビュー・医院長名・診療科目の充実"
        },
        "kids_services": {
            "weight": 15,
            "name": "子ども対応力 (0-15点)",
            "description": "子ども向けコンテンツ・待合室環境・対応スコア"
        },
        "clinic_scale": {
            "weight": 20,
            "name": "医院規模 (0-20点)",
            "description": "従業員数・診療科目数・営業時間"
        },
        "lead_quality": {
            "weight": 15,
            "name": "リード品質 (0-15点)",
            "description": "来院患者数・基礎評価・電話番号保有"
        },
        "location_opportunity": {
            "weight": 10,
            "name": "立地機会 (0-10点)",
            "description": "都市規模・競争環境・郵便番号"
        }
    }

    def __init__(self):
        self.results = []
        self.stats = {
            "total_clinics": 0,
            "high_score_clinics": 0,  # >= 75点
            "medium_score_clinics": 0,  # 50-74点
            "low_score_clinics": 0,     # < 50点
            "average_score": 0.0,
            "dimension_averages": {}
        }

    def score_web_quality(self, row: Dict[str, Any]) -> int:
        """
        Web技術力 (0-20点)
        ウェブサイト品質・SNS連携・ブログ活動
        """
        score = 0

        # Webサイト存在 (5点)
        if row.get("WebサイトURL") and row["WebサイトURL"].strip():
            score += 5

        # SNS連携 (各2点 = 最大8点)
        sns_count = 0
        sns_fields = ["SNS連携"]  # From CSV
        if row.get("SNS連携"):
            sns_val = row.get("SNS連携", 0)
            if isinstance(sns_val, str):
                try:
                    sns_val = int(sns_val)
                except:
                    sns_val = 0
            if sns_val > 0:
                sns_count = min(sns_val, 4)
                score += min(sns_count * 2, 8)

        # ブログ活動 (4点)
        blog_activity = row.get("ブログ活動", 0)
        if isinstance(blog_activity, str):
            try:
                blog_activity = int(blog_activity)
            except:
                blog_activity = 0
        if blog_activity and blog_activity > 0:
            score += 4

        # ブログ更新日 (3点)
        if row.get("ブログ更新日") and row.get("ブログ更新日").strip():
            score += 3

        return min(score, 20)

    def score_market_presence(self, row: Dict[str, Any]) -> int:
        """
        市場認知度 (0-20点)
        Googleレビュー・医院長名・診療科目の充実
        """
        score = 0

        # Googleレビュー件数 (10点満点)
        review_count = row.get("レビュー件数", 0)
        if isinstance(review_count, str):
            try:
                review_count = int(review_count)
            except:
                review_count = 0

        if review_count >= 50:
            score += 10
        elif review_count >= 30:
            score += 8
        elif review_count >= 10:
            score += 6
        elif review_count > 0:
            score += 3

        # 医院長名 (5点)
        if row.get("医院長名") and row["医院長名"].strip():
            score += 5

        # 診療科目数 (5点)
        diagnosis_tags = row.get("診療科目タグ", "")
        if diagnosis_tags:
            tag_count = len([t for t in str(diagnosis_tags).split(",") if t.strip()])
            if tag_count >= 5:
                score += 5
            elif tag_count >= 3:
                score += 3
            else:
                score += 1

        return min(score, 20)

    def score_kids_services(self, row: Dict[str, Any]) -> int:
        """
        子ども対応力 (0-15点)
        子ども向けコンテンツ・待合室環境・対応スコア
        """
        score = 0

        # 子ども対応力スコア (7点)
        kids_score = row.get("子ども対応力スコア", 0)
        if isinstance(kids_score, str):
            try:
                kids_score = int(kids_score)
            except:
                kids_score = 0

        if kids_score >= 30:
            score += 7
        elif kids_score >= 20:
            score += 5
        elif kids_score > 0:
            score += 3

        # 子ども対応力スコア (4点) - CSV値
        kids_content = row.get("子ども対応力", 0)
        if isinstance(kids_content, str):
            try:
                kids_content = int(kids_content)
            except:
                kids_content = 0

        if kids_content >= 20:
            score += 4
        elif kids_content >= 10:
            score += 2

        # 待合室写真 (4点)
        photos = row.get("写真枚数", 0)
        if isinstance(photos, str):
            try:
                photos = int(photos)
            except:
                photos = 0

        if photos >= 10:
            score += 4
        elif photos >= 5:
            score += 2
        elif photos > 0:
            score += 1

        return min(score, 15)

    def score_clinic_scale(self, row: Dict[str, Any]) -> int:
        """
        医院規模 (0-20点)
        従業員数・診療科目数・営業時間
        """
        score = 0

        # 医院規模スコア (10点)
        clinic_scale = row.get("医院規模", 0)
        if isinstance(clinic_scale, str):
            try:
                clinic_scale = int(clinic_scale)
            except:
                clinic_scale = 0

        if clinic_scale >= 20:
            score += 10
        elif clinic_scale >= 15:
            score += 7
        elif clinic_scale >= 10:
            score += 5
        elif clinic_scale > 0:
            score += 2

        # 営業時間 (7点)
        operating_hours = row.get("営業時間", "")
        if operating_hours and "18:00" in str(operating_hours) or "19:00" in str(operating_hours):
            score += 7
        elif operating_hours and "17:00" in str(operating_hours):
            score += 4
        elif operating_hours:
            score += 2

        # 診療科目タグ (3点)
        diagnosis_tags = row.get("診療科目タグ", "")
        if diagnosis_tags:
            tag_count = len([t for t in str(diagnosis_tags).split(",") if t.strip()])
            if tag_count >= 5:
                score += 3
            elif tag_count >= 3:
                score += 2
            else:
                score += 1

        return min(score, 20)

    def score_lead_quality(self, row: Dict[str, Any]) -> int:
        """
        リード品質 (0-15点)
        来院患者数・基礎評価・電話番号保有
        """
        score = 0

        # 来院患者数 (5点)
        patients = row.get("来院患者数", 0)
        if isinstance(patients, str):
            try:
                patients = int(patients)
            except:
                patients = 0

        if patients >= 10:
            score += 5
        elif patients >= 5:
            score += 3
        elif patients > 0:
            score += 1

        # 基礎評価 (7点)
        basic_eval = row.get("基礎評価", 0)
        if isinstance(basic_eval, str):
            try:
                basic_eval = int(basic_eval)
            except:
                basic_eval = 0

        if basic_eval >= 10:
            score += 7
        elif basic_eval >= 5:
            score += 4
        elif basic_eval > 0:
            score += 2

        # 電話番号保有 (3点)
        phone = row.get("電話番号", "")
        if phone and str(phone).strip():
            score += 3

        return min(score, 15)

    def score_location_opportunity(self, row: Dict[str, Any]) -> int:
        """
        立地機会 (0-10点)
        都市規模・競争環境・郵便番号
        """
        score = 0

        # Google Maps スコア (5点)
        google_rating = row.get("評価", 0)
        if isinstance(google_rating, str):
            try:
                google_rating = float(google_rating)
            except:
                google_rating = 0

        if google_rating >= 4.5:
            score += 5
        elif google_rating >= 4.0:
            score += 4
        elif google_rating >= 3.5:
            score += 3
        elif google_rating > 0:
            score += 1

        # 郵便番号 (3点)
        postal_code = row.get("郵便番号", "")
        if postal_code and str(postal_code).strip():
            score += 3

        # 住所（都市規模判定） (2点)
        address = row.get("住所", "")
        major_cities = ["東京", "大阪", "名古屋", "福岡", "札幌", "京都", "神戸", "横浜", "川崎", "さいたま"]
        if any(city in str(address) for city in major_cities):
            score += 2

        return min(score, 10)

    def calculate_total_score(self, row: Dict[str, Any]) -> tuple[int, Dict[str, int]]:
        """Calculate total score and dimension breakdown"""

        scores = {
            "web_quality": self.score_web_quality(row),
            "market_presence": self.score_market_presence(row),
            "kids_services": self.score_kids_services(row),
            "clinic_scale": self.score_clinic_scale(row),
            "lead_quality": self.score_lead_quality(row),
            "location_opportunity": self.score_location_opportunity(row)
        }

        # Calculate weighted total
        total = sum(
            scores[dim] * (self.DIMENSIONS[dim]["weight"] / 100)
            for dim in scores
        )

        return round(total), scores

    def process_csv(self, csv_path: str) -> List[Dict[str, Any]]:
        """Process CSV file and calculate scores for all clinics"""

        results = []

        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)

            for row_num, row in enumerate(reader, start=2):
                clinic_name = row.get("医院名", "不明")
                total_score, dimension_scores = self.calculate_total_score(row)

                result = {
                    "row_number": row_num,
                    "clinic_name": clinic_name,
                    "phone": row.get("電話番号", ""),
                    "address": row.get("住所", ""),
                    "website_url": row.get("WebサイトURL", ""),
                    "director_name": row.get("医院長名", ""),
                    "total_score": total_score,
                    "dimension_scores": {
                        dim: {
                            "score": score,
                            "weight": self.DIMENSIONS[dim]["weight"],
                            "weighted_value": round(score * (self.DIMENSIONS[dim]["weight"] / 100), 2),
                            "description": self.DIMENSIONS[dim]["description"]
                        }
                        for dim, score in dimension_scores.items()
                    },
                    "raw_data": {
                        "basic_evaluation": row.get("基礎評価", ""),
                        "incoming_patients": row.get("来院患者数", ""),
                        "kids_capability": row.get("子ども対応力", ""),
                        "web_proactivity": row.get("Web積極性", ""),
                        "clinic_scale": row.get("医院規模", ""),
                        "blog_activity": row.get("ブログ活動", ""),
                        "google_rating": row.get("評価", ""),
                        "review_count": row.get("レビュー件数", ""),
                        "diagnosis_tags": row.get("診療科目タグ", ""),
                        "photo_count": row.get("写真枚数", ""),
                        "sns_integration": row.get("SNS連携", ""),
                        "kids_capability_score": row.get("子ども対応力スコア", "")
                    }
                }

                results.append(result)

                # Update statistics
                self.stats["total_clinics"] += 1
                if total_score >= 75:
                    self.stats["high_score_clinics"] += 1
                elif total_score >= 50:
                    self.stats["medium_score_clinics"] += 1
                else:
                    self.stats["low_score_clinics"] += 1

        return results

    def calculate_statistics(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate overall statistics"""

        if not results:
            return {}

        # Average total score
        total_scores = [r["total_score"] for r in results]
        avg_score = sum(total_scores) / len(total_scores)

        # Average dimension scores
        dimension_averages = {}
        for dim in self.DIMENSIONS.keys():
            dim_scores = [r["dimension_scores"][dim]["score"] for r in results]
            dimension_averages[dim] = {
                "average": round(sum(dim_scores) / len(dim_scores), 2),
                "name": self.DIMENSIONS[dim]["name"],
                "weight": self.DIMENSIONS[dim]["weight"]
            }

        # Score distribution
        score_dist = {
            "90-100": len([s for s in total_scores if s >= 90]),
            "80-89": len([s for s in total_scores if 80 <= s < 90]),
            "70-79": len([s for s in total_scores if 70 <= s < 80]),
            "60-69": len([s for s in total_scores if 60 <= s < 70]),
            "50-59": len([s for s in total_scores if 50 <= s < 60]),
            "40-49": len([s for s in total_scores if 40 <= s < 50]),
            "0-39": len([s for s in total_scores if s < 40])
        }

        return {
            "total_clinics": len(results),
            "average_score": round(avg_score, 2),
            "max_score": max(total_scores),
            "min_score": min(total_scores),
            "median_score": sorted(total_scores)[len(total_scores) // 2],
            "dimension_averages": dimension_averages,
            "score_distribution": score_dist,
            "high_score_clinics": self.stats["high_score_clinics"],
            "medium_score_clinics": self.stats["medium_score_clinics"],
            "low_score_clinics": self.stats["low_score_clinics"]
        }

    def generate_output(self, results: List[Dict[str, Any]], csv_path: str) -> Dict[str, Any]:
        """Generate JSON output"""

        stats = self.calculate_statistics(results)

        output = {
            "metadata": {
                "batch": "030",
                "timestamp": datetime.now().isoformat(),
                "source_csv": os.path.basename(csv_path),
                "scoring_system": "6-Dimensional (100-point scale)",
                "dimensions": self.DIMENSIONS
            },
            "statistics": stats,
            "results": results
        }

        return output


def main():
    # File paths
    current_dir = Path(__file__).parent
    csv_path = current_dir / "scoring_batches" / "batch_030_to_score.csv"
    output_path = current_dir / "scoring_batches" / "scoring_results_batch_030.json"

    print(f"📊 Processing: {csv_path}")
    print(f"🎯 Output: {output_path}")
    print()

    # Process scoring
    scorer = DentalClinicScorer()
    results = scorer.process_csv(str(csv_path))

    # Generate output
    output = scorer.generate_output(results, str(csv_path))

    # Save JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Print summary
    print("✅ Scoring Complete!")
    print(f"   Total Clinics: {output['statistics']['total_clinics']}")
    print(f"   Average Score: {output['statistics']['average_score']:.2f}/100")
    print(f"   High Score (≥75): {output['statistics']['high_score_clinics']} clinics")
    print(f"   Medium Score (50-74): {output['statistics']['medium_score_clinics']} clinics")
    print(f"   Low Score (<50): {output['statistics']['low_score_clinics']} clinics")
    print()
    print("📊 Dimension Averages:")
    for dim, data in output['statistics']['dimension_averages'].items():
        print(f"   {data['name']}: {data['average']}/20 (weight: {data['weight']}%)")
    print()
    print(f"✅ JSON saved: {output_path}")
    print(f"✅ Total records: {len(results)}")


if __name__ == "__main__":
    main()
