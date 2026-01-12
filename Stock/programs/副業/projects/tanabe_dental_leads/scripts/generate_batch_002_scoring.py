#!/usr/bin/env python3
"""
バッチ002スコアリング結果生成

WebFetch分析結果を基に、500件の歯科医院をスコアリングしてJSON出力。
"""

import csv
import json
from datetime import datetime
from pathlib import Path

# WebFetch分析結果（4医院）
WEBFETCH_RESULTS = {
    "https://www.mamoru-shika.com/?utm_source=google&utm_medium=maps": {
        "sns_instagram": True,
        "sns_facebook": False,
        "sns_line": True,
        "sns_twitter": False,
        "blog_updated": "2025-12-27",
        "kids_content": True,
        "waiting_room_photo": True,
        "operating_hours": "月火木金土日祝 9:30-13:00, 14:30-18:30（水曜休診）",
        "director_name": "金俊介"
    },
    "http://www.matsuo-dc.info/": {
        "sns_instagram": True,
        "sns_facebook": True,
        "sns_line": True,
        "sns_twitter": False,
        "blog_updated": None,
        "kids_content": True,
        "waiting_room_photo": True,
        "operating_hours": "平日9:00-12:30, 14:00-17:30（木曜休診）",
        "director_name": "松尾紘吾"
    },
    "https://tonandc.com/": {
        "sns_instagram": True,
        "sns_facebook": True,
        "sns_line": False,
        "sns_twitter": False,
        "blog_updated": None,
        "kids_content": True,
        "waiting_room_photo": False,
        "operating_hours": "月火水木金土 9:00-12:30 / 13:30-17:30",
        "director_name": "山田優貴"
    },
    "https://www.n-yoshida.jp/": {
        "sns_instagram": True,
        "sns_facebook": False,
        "sns_line": True,
        "sns_twitter": False,
        "blog_updated": "2025-12-11",
        "kids_content": True,
        "waiting_room_photo": False,
        "operating_hours": "月～土 9:00～17:00",
        "director_name": "吉田洋一"
    }
}


def calculate_score_dimension_1(rating: float) -> int:
    """基礎評価スコア（20点満点）"""
    return min(int(rating * 4), 20)


def calculate_score_dimension_2(review_count: int) -> int:
    """来院患者数スコア（20点満点）"""
    if review_count >= 100:
        return 20
    elif review_count >= 50:
        return 15
    elif review_count >= 20:
        return 10
    elif review_count >= 10:
        return 5
    else:
        return 0


def calculate_score_dimension_3(clinic_name: str, website_data: dict) -> int:
    """子ども対応力スコア（30点満点）"""
    score = 0

    # kids_content (15点)
    if website_data.get('kids_content', False):
        score += 15

    # 医院名に子ども関連キーワード (10点)
    keywords = ['小児', 'こども', '子ども', 'キッズ', '矯正']
    if any(kw in clinic_name for kw in keywords):
        score += 10

    # waiting_room_photo (5点)
    if website_data.get('waiting_room_photo', False):
        score += 5

    return min(score, 30)


def calculate_score_dimension_4(website_data: dict) -> int:
    """Web積極性スコア（15点満点）"""
    sns_count = 0
    if website_data.get('sns_instagram', False):
        sns_count += 1
    if website_data.get('sns_facebook', False):
        sns_count += 1
    if website_data.get('sns_line', False):
        sns_count += 1
    if website_data.get('sns_twitter', False):
        sns_count += 1

    return min(sns_count * 5, 15)


def calculate_score_dimension_5(operating_hours: str, photo_count: int) -> int:
    """医院規模スコア（10点満点）"""
    score = 0

    # 営業時間記載 (5点)
    if operating_hours:
        score += 5

    # 写真10枚以上 (5点)
    if photo_count >= 10:
        score += 5

    return score


def calculate_score_dimension_6(blog_updated: str) -> int:
    """ブログ活動スコア（5点満点）"""
    if not blog_updated:
        return 0

    try:
        from datetime import datetime
        blog_date = datetime.strptime(blog_updated, "%Y-%m-%d")
        now = datetime.now()
        days_diff = (now - blog_date).days

        if days_diff <= 30:
            return 5
        elif days_diff <= 60:
            return 4
        elif days_diff <= 90:
            return 3
        elif days_diff <= 180:
            return 2
        elif days_diff <= 365:
            return 1
        else:
            return 0
    except:
        return 0


def main():
    csv_path = "scoring_batches/batch_002_to_score.csv"
    output_path = "scoring_results_batch_002_retry_20260104.json"

    print("=" * 80)
    print("バッチ002スコアリング結果生成")
    print("=" * 80)

    # CSV読み込み
    clinics = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clinics.append(row)

    print(f"\n✓ 総件数: {len(clinics)}件")

    # スコアリング実行
    results = []
    director_names_found = 0

    for clinic in clinics:
        clinic_name = clinic.get('医院名', 'Unknown')
        website_url = clinic.get('WebサイトURL', '').strip()

        # WebFetch結果を取得
        website_data = WEBFETCH_RESULTS.get(website_url, {})

        if not website_data:
            print(f"⚠️  {clinic_name}: WebFetch結果なし")
            continue

        # 生データ抽出
        rating = float(clinic.get('評価', '0') or '0')
        review_count = int(clinic.get('レビュー件数', '0') or '0')
        photo_count = int(clinic.get('写真枚数', '0') or '0')

        # スコアリング
        scores = {
            "基礎評価": calculate_score_dimension_1(rating),
            "来院患者数": calculate_score_dimension_2(review_count),
            "子ども対応力": calculate_score_dimension_3(clinic_name, website_data),
            "Web積極性": calculate_score_dimension_4(website_data),
            "医院規模": calculate_score_dimension_5(website_data.get('operating_hours', ''), photo_count),
            "ブログ活動": calculate_score_dimension_6(website_data.get('blog_updated'))
        }

        total_score = sum(scores.values())

        result = {
            "clinic_name": clinic_name,
            "total_score": total_score,
            "scores": scores,
            "website_analysis": {
                "sns_instagram": website_data.get('sns_instagram', False),
                "sns_facebook": website_data.get('sns_facebook', False),
                "sns_line": website_data.get('sns_line', False),
                "sns_twitter": website_data.get('sns_twitter', False),
                "blog_updated": website_data.get('blog_updated'),
                "kids_content": website_data.get('kids_content', False),
                "waiting_room_photo": website_data.get('waiting_room_photo', False),
                "operating_hours": website_data.get('operating_hours'),
                "director_name": website_data.get('director_name')
            },
            "raw_data": {
                "rating": rating,
                "user_ratings_total": review_count,
                "formatted_address": clinic.get('住所', ''),
                "formatted_phone_number": clinic.get('電話番号', ''),
                "website": website_url,
                "photos_count": photo_count
            }
        }

        results.append(result)

        if website_data.get('director_name'):
            director_names_found += 1

    # 統計情報
    extraction_rate = (director_names_found / len(results) * 100) if results else 0

    print(f"✓ 分析完了: {len(results)}件")
    print(f"✓ 医院長名取得: {director_names_found}件 ({extraction_rate:.1f}%)")

    # JSON出力
    output_data = {
        "metadata": {
            "batch_file": "batch_002_to_score.csv",
            "total_clinics": len(results),
            "timestamp": datetime.now().isoformat(),
            "retry_execution": True,
            "webfetch_forced": True,
            "director_names_found": director_names_found,
            "director_extraction_rate": f"{extraction_rate:.1f}%",
            "unique_clinics": 4,
            "note": "Batch 002 contains 4 unique clinics repeated 125 times each"
        },
        "results": results
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ JSON出力完了: {output_path}")
    print(f"✓ 医院長名抽出率: {director_names_found}/{len(results)} ({extraction_rate:.1f}%)")
    print(f"✓ ユニーク医院数: 4")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
