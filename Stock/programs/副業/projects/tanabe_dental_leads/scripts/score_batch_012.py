#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6-Dimensional Scoring System for Dental Clinics (Batch 012)
Scoring Dimensions:
1. Web Presence & Technology (25 points) - Website, Online Reviews, Digital Engagement
2. Clinical Reputation & Patient Reviews (20 points) - Google Review Rating, Number of Reviews
3. Patient-Focused Services (20 points) - Child-Friendly, Operating Hours, Accessibility
4. Content & Information Availability (15 points) - Photos, Blog Updates, Service Information
5. Digital Marketing & Social Presence (15 points) - SNS Integration, Blog Activity
6. Business Fundamentals (5 points) - Basic Information Completeness
Total: 100 points
"""

import json
import csv
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class DentalClinicScorer:
    def __init__(self):
        self.batch_name = "batch_012"
        self.results = {}
        self.metadata = {
            "batch": self.batch_name,
            "timestamp": datetime.now().isoformat(),
            "scoring_method": "6-dimensional framework",
            "total_clinics": 0,
            "analyzed_clinics": 0,
            "errors": 0
        }

    def calculate_web_presence_score(self, row: Dict) -> int:
        """
        Dimension 1: Web Presence & Technology (25 points max)
        - Website existence: 10 points
        - Google Maps presence: 8 points
        - Online rating presence: 7 points
        """
        score = 0

        # Website presence
        website_url = row.get('WebサイトURL', '')
        if website_url and isinstance(website_url, str) and website_url.strip() and website_url != '':
            score += 10
        else:
            score += 0

        # Google Maps presence
        maps_url = row.get('Google Maps URL', '')
        if maps_url and isinstance(maps_url, str) and maps_url.strip():
            score += 8
        else:
            score += 4  # Partial credit for Google presence

        # Online rating (Google Review Rating)
        try:
            rating = float(row.get('評価', 0))
            if rating >= 4.5:
                score += 7
            elif rating >= 4.0:
                score += 5
            elif rating >= 3.5:
                score += 3
            elif rating > 0:
                score += 1
        except (ValueError, TypeError):
            score += 0

        return min(score, 25)

    def calculate_reputation_score(self, row: Dict) -> int:
        """
        Dimension 2: Clinical Reputation & Patient Reviews (20 points max)
        - Google Review Count: 0-20 points
        """
        score = 0

        try:
            review_count = int(row.get('レビュー件数', 0))
            rating = float(row.get('評価', 0))

            # Review count scoring
            if review_count >= 300:
                review_score = 15
            elif review_count >= 200:
                review_score = 12
            elif review_count >= 100:
                review_score = 10
            elif review_count >= 50:
                review_score = 7
            elif review_count >= 20:
                review_score = 5
            elif review_count >= 10:
                review_score = 3
            else:
                review_score = 1 if review_count > 0 else 0

            # Rating bonus
            rating_bonus = 0
            if rating >= 4.7:
                rating_bonus = 5
            elif rating >= 4.5:
                rating_bonus = 3
            elif rating >= 4.0:
                rating_bonus = 1

            score = min(review_score + rating_bonus, 20)
        except (ValueError, TypeError):
            score = 0

        return score

    def calculate_patient_services_score(self, row: Dict) -> int:
        """
        Dimension 3: Patient-Focused Services (20 points max)
        - Child-friendly services: 10 points
        - Good operating hours: 5 points
        - Accessibility indicators: 5 points
        """
        score = 0

        # Child-friendly services
        kids_content = row.get('子ども対応力', 0)
        try:
            kids_score = int(kids_content)
            if kids_score >= 30:
                score += 10
            elif kids_score >= 15:
                score += 7
            elif kids_score > 0:
                score += 4
        except (ValueError, TypeError):
            pass

        # Operating hours (月-土 indicates business day coverage)
        operating_hours = row.get('営業時間', '')
        if operating_hours and isinstance(operating_hours, str):
            if '土' in operating_hours:  # Includes Saturday
                score += 5
            else:
                score += 3

        # Accessibility (location provided)
        address = row.get('住所', '')
        if address and isinstance(address, str) and address.strip():
            score += 5

        return min(score, 20)

    def calculate_content_availability_score(self, row: Dict) -> int:
        """
        Dimension 4: Content & Information Availability (15 points max)
        - Website photos: 8 points
        - Blog updates: 7 points
        """
        score = 0

        # Photo availability
        photo_count = row.get('写真枚数', 0)
        try:
            photos = int(photo_count)
            if photos >= 20:
                score += 8
            elif photos >= 10:
                score += 6
            elif photos >= 5:
                score += 4
            elif photos > 0:
                score += 2
        except (ValueError, TypeError):
            pass

        # Blog updates
        blog_update = row.get('ブログ更新日', '')
        if blog_update and isinstance(blog_update, str) and blog_update.strip():
            score += 7
        else:
            # Check blog activity score
            try:
                blog_activity = int(row.get('ブログ活動', 0))
                if blog_activity > 0:
                    score += 3
            except (ValueError, TypeError):
                pass

        return min(score, 15)

    def calculate_digital_marketing_score(self, row: Dict) -> int:
        """
        Dimension 5: Digital Marketing & Social Presence (15 points max)
        - SNS integration: 10 points
        - Blog activity: 5 points
        """
        score = 0

        # SNS integration (Instagram, Facebook, LINE, Twitter)
        sns_count = 0
        sns_integrations = ['sns_instagram', 'sns_facebook', 'sns_line', 'sns_twitter']

        # Check SNS integration column
        sns_col = row.get('SNS連携', '')
        if sns_col and isinstance(sns_col, str) and sns_col.strip():
            # Count comma-separated SNS platforms
            sns_count = len([x for x in sns_col.split(',') if x.strip()])

        if sns_count >= 3:
            score += 10
        elif sns_count == 2:
            score += 7
        elif sns_count == 1:
            score += 4
        elif sns_count == 0:
            score += 0

        # Blog activity
        try:
            blog_activity = int(row.get('ブログ活動', 0))
            if blog_activity >= 30:
                score += 5
            elif blog_activity >= 15:
                score += 3
            elif blog_activity > 0:
                score += 1
        except (ValueError, TypeError):
            pass

        return min(score, 15)

    def calculate_business_fundamentals_score(self, row: Dict) -> int:
        """
        Dimension 6: Business Fundamentals (5 points max)
        - Essential info completeness: 5 points
        """
        score = 5  # Start with full points

        # Deduct for missing essential information
        essential_fields = ['医院名', '住所', '電話番号']
        missing = 0

        for field in essential_fields:
            value = row.get(field, '')
            if not value or (isinstance(value, str) and not value.strip()):
                missing += 1

        deduction = missing * 2  # 2 points per missing field
        score = max(0, score - deduction)

        return score

    def calculate_total_score(self, row: Dict) -> Dict[str, int]:
        """Calculate total score across all 6 dimensions"""
        scores = {
            "web_presence": self.calculate_web_presence_score(row),
            "reputation": self.calculate_reputation_score(row),
            "patient_services": self.calculate_patient_services_score(row),
            "content_availability": self.calculate_content_availability_score(row),
            "digital_marketing": self.calculate_digital_marketing_score(row),
            "business_fundamentals": self.calculate_business_fundamentals_score(row)
        }

        scores["total"] = sum(scores.values())

        return scores

    def score_clinic(self, clinic_name: str, row: Dict) -> Dict[str, Any]:
        """Score a single clinic"""
        scores = self.calculate_total_score(row)

        result = {
            "clinic_name": clinic_name,
            "scores": scores,
            "breakdown": {
                "1_web_presence": {
                    "dimension": "Web Presence & Technology",
                    "points": scores["web_presence"],
                    "max": 25,
                    "percentage": round((scores["web_presence"] / 25) * 100, 1) if scores["web_presence"] > 0 else 0
                },
                "2_reputation": {
                    "dimension": "Clinical Reputation & Patient Reviews",
                    "points": scores["reputation"],
                    "max": 20,
                    "percentage": round((scores["reputation"] / 20) * 100, 1) if scores["reputation"] > 0 else 0
                },
                "3_patient_services": {
                    "dimension": "Patient-Focused Services",
                    "points": scores["patient_services"],
                    "max": 20,
                    "percentage": round((scores["patient_services"] / 20) * 100, 1) if scores["patient_services"] > 0 else 0
                },
                "4_content": {
                    "dimension": "Content & Information Availability",
                    "points": scores["content_availability"],
                    "max": 15,
                    "percentage": round((scores["content_availability"] / 15) * 100, 1) if scores["content_availability"] > 0 else 0
                },
                "5_digital_marketing": {
                    "dimension": "Digital Marketing & Social Presence",
                    "points": scores["digital_marketing"],
                    "max": 15,
                    "percentage": round((scores["digital_marketing"] / 15) * 100, 1) if scores["digital_marketing"] > 0 else 0
                },
                "6_fundamentals": {
                    "dimension": "Business Fundamentals",
                    "points": scores["business_fundamentals"],
                    "max": 5,
                    "percentage": round((scores["business_fundamentals"] / 5) * 100, 1) if scores["business_fundamentals"] > 0 else 0
                }
            },
            "summary": {
                "total_score": scores["total"],
                "max_score": 100,
                "percentage": round((scores["total"] / 100) * 100, 1),
                "grade": self.assign_grade(scores["total"])
            },
            "raw_data": {
                "website_url": row.get('WebサイトURL', ''),
                "google_maps_url": row.get('Google Maps URL', ''),
                "review_count": row.get('レビュー件数', 0),
                "rating": row.get('評価', 0),
                "photos": row.get('写真枚数', 0),
                "phone": row.get('電話番号', '')
            }
        }

        return result

    def assign_grade(self, score: int) -> str:
        """Assign letter grade based on total score"""
        if score >= 85:
            return "A (Excellent)"
        elif score >= 75:
            return "B (Very Good)"
        elif score >= 65:
            return "C (Good)"
        elif score >= 55:
            return "D (Fair)"
        elif score >= 45:
            return "E (Poor)"
        else:
            return "F (Very Poor)"

    def process_csv(self, csv_path: str) -> None:
        """Process CSV file and score all clinics"""
        self.metadata["source_csv"] = csv_path

        try:
            with open(csv_path, 'r', encoding='utf-8-sig') as f:
                # Detect BOM and skip
                reader = csv.DictReader(f)

                for idx, row in enumerate(reader, 1):
                    try:
                        clinic_name = row.get('医院名', f'Clinic_{idx}')

                        # Skip empty rows
                        if not clinic_name or not clinic_name.strip():
                            continue

                        self.metadata["total_clinics"] += 1

                        # Score the clinic
                        clinic_score = self.score_clinic(clinic_name, row)
                        self.results[clinic_name] = clinic_score
                        self.metadata["analyzed_clinics"] += 1

                    except Exception as e:
                        self.metadata["errors"] += 1
                        print(f"Error processing clinic at row {idx}: {str(e)}")
                        continue

        except Exception as e:
            print(f"Error reading CSV: {str(e)}")
            self.metadata["errors"] += 1

    def export_to_json(self, output_path: str) -> None:
        """Export results to JSON file"""
        output_data = {
            "metadata": self.metadata,
            "results": self.results
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"Results exported to: {output_path}")
        print(f"Total clinics analyzed: {self.metadata['analyzed_clinics']}")
        print(f"Errors: {self.metadata['errors']}")


def main():
    # Initialize scorer
    scorer = DentalClinicScorer()

    # Define paths
    base_path = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads")
    csv_file = base_path / "scoring_batches" / "batch_012_to_score.csv"
    output_file = base_path / "scoring_results_batch_012.json"

    print(f"Processing: {csv_file}")
    print("=" * 80)

    # Process CSV
    scorer.process_csv(str(csv_file))

    # Export results
    scorer.export_to_json(str(output_file))

    # Print summary
    print("\n" + "=" * 80)
    print("BATCH 012 SCORING COMPLETE")
    print("=" * 80)
    print(f"Total clinics in batch: {scorer.metadata['total_clinics']}")
    print(f"Successfully analyzed: {scorer.metadata['analyzed_clinics']}")
    print(f"Errors: {scorer.metadata['errors']}")
    print(f"Output file: {output_file}")

    # Sample output
    if scorer.results:
        first_clinic = next(iter(scorer.results.items()))
        print(f"\nSample Result - {first_clinic[0]}:")
        print(f"  Total Score: {first_clinic[1]['summary']['total_score']}/100")
        print(f"  Grade: {first_clinic[1]['summary']['grade']}")
        print(f"  Dimensions breakdown:")
        for dim_key, dim_data in first_clinic[1]['breakdown'].items():
            print(f"    - {dim_data['dimension']}: {dim_data['points']}/{dim_data['max']} points")


if __name__ == "__main__":
    main()
