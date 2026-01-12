#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch 021 - 6次元スコアリング実行スクリプト
歯科医院WebサイトをCSVから読み込み、以下の6次元で100点満点評価を実行
"""

import csv
import json
from pathlib import Path
from datetime import datetime
import sys

# スコアリング基準の定義
SCORING_CRITERIA = {
    "1_web_presence": {
        "name": "Web存在感",
        "description": "WebサイトURL、Google Maps登録、SNS連携の充実度",
        "weight": 20,
        "max_score": 100
    },
    "2_sns_engagement": {
        "name": "SNS連携度",
        "description": "Instagram、Facebook、LINE、Twitterなどの連携数と更新頻度",
        "weight": 15,
        "max_score": 100
    },
    "3_content_quality": {
        "name": "コンテンツ品質",
        "description": "ブログ活動、写真掲載数、医院紹介の充実度",
        "weight": 20,
        "max_score": 100
    },
    "4_kids_orientation": {
        "name": "子ども向け対応",
        "description": "子ども対応力、子ども向けコンテンツ、設備写真",
        "weight": 15,
        "max_score": 100
    },
    "5_online_reputation": {
        "name": "オンライン評判",
        "description": "Google評価スコア、レビュー件数、診療科目の多様性",
        "weight": 15,
        "max_score": 100
    },
    "6_operational_info": {
        "name": "営業情報充実度",
        "description": "営業時間掲載、医院長名、基本情報の完全性",
        "weight": 15,
        "max_score": 100
    }
}

def safe_float(value):
    """文字列を安全にfloatに変換"""
    if value is None or value == "" or value == "nan":
        return 0.0
    try:
        return float(str(value).strip())
    except (ValueError, TypeError):
        return 0.0

def safe_int(value):
    """文字列を安全にintに変換"""
    if value is None or value == "":
        return 0
    try:
        return int(float(str(value).strip()))
    except (ValueError, TypeError):
        return 0

def score_web_presence(row):
    """
    1. Web存在感（20点満点）
    - WebサイトURL有無: 0-30点
    - Google Maps登録: 0-35点
    - SNS連携数: 0-35点
    """
    score = 0
    max_score = 100

    # WebサイトURL（0-30点）
    website_url = str(row.get('WebサイトURL', '')).strip()
    if website_url and website_url != '':
        score += 30

    # Google Maps URL（0-35点）
    maps_url = str(row.get('Google Maps URL', '')).strip()
    if maps_url and maps_url != '' and 'maps.google.com' in maps_url:
        score += 35

    # SNS連携数（0-35点）
    sns_count = 0
    if row.get('SNS連携') == '1' or row.get('SNS連携') == 1:
        sns_count = 1
    # Instagram、Facebook、LINE、Twitterの個別チェック（基本情報から推測）
    # CSV形式から直接判定が難しい場合、SNS連携フラグで判定
    sns_score = min(35, sns_count * 35)
    score += sns_score

    return min(score, max_score)

def score_sns_engagement(row):
    """
    2. SNS連携度（15点満点）
    - SNS連携フラグ: 0-50点
    - ブログ更新日の新しさ: 0-50点
    """
    score = 0
    max_score = 100

    # SNS連携フラグ（0-50点）
    sns_engagement = row.get('SNS連携', 0)
    if sns_engagement == '1' or sns_engagement == 1:
        score += 50

    # ブログ更新日の新しさ（0-50点）
    blog_date = str(row.get('ブログ更新日', '')).strip()
    if blog_date and blog_date != '' and blog_date != '0':
        try:
            # YYYY-MM-DD形式と想定
            blog_date_obj = datetime.strptime(blog_date, '%Y-%m-%d')
            today = datetime.now()
            days_old = (today - blog_date_obj).days

            if days_old <= 7:  # 1週間以内
                score += 50
            elif days_old <= 30:  # 1ヶ月以内
                score += 40
            elif days_old <= 90:  # 3ヶ月以内
                score += 30
            elif days_old <= 180:  # 6ヶ月以内
                score += 20
            else:  # 6ヶ月以上前
                score += 5
        except:
            pass

    return min(score, max_score)

def score_content_quality(row):
    """
    3. コンテンツ品質（20点満点）
    - ブログ活動: 0-40点
    - 写真枚数: 0-30点
    - 診療科目タグの多様性: 0-30点
    """
    score = 0
    max_score = 100

    # ブログ活動（0-40点）
    blog_activity = safe_float(row.get('ブログ活動', 0))
    if blog_activity > 0:
        score += min(40, blog_activity * 4)  # 10件以上で40点

    # 写真枚数（0-30点）
    photo_count = safe_int(row.get('写真枚数', 0))
    if photo_count > 0:
        score += min(30, photo_count * 3)  # 10枚以上で30点

    # 診療科目タグの多様性（0-30点）
    tags = str(row.get('診療科目タグ', '')).strip()
    if tags:
        tag_count = len(tags.split(','))
        score += min(30, tag_count * 5)  # 6個以上で30点

    return min(score, max_score)

def score_kids_orientation(row):
    """
    4. 子ども向け対応（15点満点）
    - 子ども対応力スコア: 0-40点
    - 子ども対応力フラグ: 0-30点
    - 待合室写真の有無: 0-30点
    """
    score = 0
    max_score = 100

    # 子ども対応力スコア（0-40点）
    kids_score = safe_float(row.get('子ども対応力スコア', 0))
    if kids_score > 0:
        score += min(40, kids_score * 0.4)  # 100で40点

    # 子ども対応力フラグ（0-30点）
    kids_capability = safe_int(row.get('子ども対応力', 0))
    if kids_capability > 0:
        score += 30

    # 待合室写真の有無（0-30点）
    # CSV内に直接の待合室写真フラグがない場合、写真枚数で推測
    photo_count = safe_int(row.get('写真枚数', 0))
    if photo_count > 5:
        score += 30

    return min(score, max_score)

def score_online_reputation(row):
    """
    5. オンライン評判（15点満点）
    - Google評価: 0-40点
    - レビュー件数: 0-30点
    - 診療科目の多様性: 0-30点
    """
    score = 0
    max_score = 100

    # Google評価（0-40点）
    rating = safe_float(row.get('評価', 0))
    if rating > 0:
        score += min(40, rating * 8)  # 5.0で40点

    # レビュー件数（0-30点）
    review_count = safe_int(row.get('レビュー件数', 0))
    if review_count > 0:
        score += min(30, review_count)  # 30件以上で30点

    # 診療科目の多様性（0-30点）
    tags = str(row.get('診療科目タグ', '')).strip()
    if tags:
        tag_count = len(tags.split(','))
        score += min(30, tag_count * 5)  # 6個以上で30点

    return min(score, max_score)

def score_operational_info(row):
    """
    6. 営業情報充実度（15点満点）
    - 営業時間掲載: 0-35点
    - 医院長名の有無: 0-35点
    - 基本情報の完全性: 0-30点
    """
    score = 0
    max_score = 100

    # 営業時間掲載（0-35点）
    operating_hours = str(row.get('営業時間', '')).strip()
    if operating_hours and operating_hours != '':
        score += 35

    # 医院長名の有無（0-35点）
    director_name = str(row.get('医院長名', '')).strip()
    if director_name and director_name != '':
        score += 35

    # 基本情報の完全性（0-30点）
    # 郵便番号、住所、電話番号が揃っているかチェック
    zipcode = str(row.get('郵便番号', '')).strip()
    address = str(row.get('住所', '')).strip()
    phone = str(row.get('電話番号', '')).strip()

    filled_count = sum([1 for x in [zipcode, address, phone] if x and x != ''])
    score += int((filled_count / 3) * 30)

    return min(score, max_score)

def calculate_overall_score(dimension_scores):
    """
    総合スコア計算（100点満点）
    各次元のスコアに重みを付けて計算
    """
    weighted_score = 0
    total_weight = 0

    dimension_names = [
        "1_web_presence",
        "2_sns_engagement",
        "3_content_quality",
        "4_kids_orientation",
        "5_online_reputation",
        "6_operational_info"
    ]

    for dim_key in dimension_names:
        criteria = SCORING_CRITERIA[dim_key]
        weight = criteria['weight']
        score = dimension_scores[dim_key]

        # 20点満点 → 100点満点に正規化
        normalized_score = (score / 20) * 100 if dim_key in dimension_scores else 0

        weighted_score += normalized_score * weight
        total_weight += weight

    # 加重平均を計算
    overall = weighted_score / total_weight if total_weight > 0 else 0
    return round(overall, 1)

def score_clinic(row):
    """
    クリニック全体のスコアリング
    6次元すべてを計算し、総合スコアを算出
    """
    # 各次元のスコアを計算（20点満点）
    dimensions = {
        "1_web_presence": score_web_presence(row) / 5,  # 100→20点
        "2_sns_engagement": score_sns_engagement(row) / 5,
        "3_content_quality": score_content_quality(row) / 5,
        "4_kids_orientation": score_kids_orientation(row) / 5,
        "5_online_reputation": score_online_reputation(row) / 5,
        "6_operational_info": score_operational_info(row) / 5
    }

    # 総合スコア計算（100点満点）
    overall_score = calculate_overall_score(dimensions)

    return {
        "dimensions": dimensions,
        "overall_score": overall_score
    }

def main():
    # ファイルパス
    csv_path = Path("scoring_batches/batch_021_to_score.csv")
    output_path = Path("scoring_results_batch_021.json")

    if not csv_path.exists():
        print(f"エラー: {csv_path} が見つかりません")
        sys.exit(1)

    # CSVを読み込み
    results = []
    errors = []

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        clinics = list(reader)

    print(f"📊 Batch 021 スコアリング開始")
    print(f"   対象: {len(clinics)}件の歯科医院")
    print("")

    # 各クリニックをスコアリング
    for idx, clinic in enumerate(clinics, 1):
        try:
            clinic_name = clinic.get('医院名', 'Unknown')
            director_name = clinic.get('医院長名', '')

            # スコアリング実行
            score_result = score_clinic(clinic)

            # 結果を構築
            result_entry = {
                "clinic_name": clinic_name,
                "director_name": director_name,
                "scores": {
                    "web_presence": round(score_result["dimensions"]["1_web_presence"], 1),
                    "sns_engagement": round(score_result["dimensions"]["2_sns_engagement"], 1),
                    "content_quality": round(score_result["dimensions"]["3_content_quality"], 1),
                    "kids_orientation": round(score_result["dimensions"]["4_kids_orientation"], 1),
                    "online_reputation": round(score_result["dimensions"]["5_online_reputation"], 1),
                    "operational_info": round(score_result["dimensions"]["6_operational_info"], 1)
                },
                "overall_score": score_result["overall_score"],
                "source_data": {
                    "website_url": clinic.get('WebサイトURL', ''),
                    "google_rating": safe_float(clinic.get('評価', 0)),
                    "review_count": safe_int(clinic.get('レビュー件数', 0)),
                    "photo_count": safe_int(clinic.get('写真枚数', 0)),
                    "blog_activity": safe_int(clinic.get('ブログ活動', 0)),
                    "sns_linked": clinic.get('SNS連携', '0'),
                    "kids_capability": safe_int(clinic.get('子ども対応力', 0))
                }
            }

            results.append(result_entry)

            # 進捗表示
            if idx % 50 == 0 or idx == len(clinics):
                print(f"✓ 処理中: {idx}/{len(clinics)} ({idx/len(clinics)*100:.1f}%)")

        except Exception as e:
            error_entry = {
                "clinic_name": clinic.get('医院名', 'Unknown'),
                "error": str(e),
                "row_number": idx
            }
            errors.append(error_entry)
            print(f"✗ エラー行 {idx}: {clinic.get('医院名', 'Unknown')} - {str(e)}")

    # 統計情報を計算
    scores_list = [r["overall_score"] for r in results]
    avg_score = sum(scores_list) / len(scores_list) if scores_list else 0
    max_score = max(scores_list) if scores_list else 0
    min_score = min(scores_list) if scores_list else 0

    # スコア分布
    score_distribution = {
        "90_100": sum(1 for s in scores_list if s >= 90),
        "80_89": sum(1 for s in scores_list if 80 <= s < 90),
        "70_79": sum(1 for s in scores_list if 70 <= s < 80),
        "60_69": sum(1 for s in scores_list if 60 <= s < 70),
        "50_59": sum(1 for s in scores_list if 50 <= s < 60),
        "below_50": sum(1 for s in scores_list if s < 50)
    }

    # JSON出力
    output_data = {
        "metadata": {
            "batch_name": "batch_021",
            "total_clinics": len(clinics),
            "successfully_scored": len(results),
            "errors": len(errors),
            "timestamp": datetime.now().isoformat(),
            "scoring_criteria": list(SCORING_CRITERIA.keys())
        },
        "statistics": {
            "average_score": round(avg_score, 1),
            "max_score": max_score,
            "min_score": min_score,
            "score_distribution": score_distribution
        },
        "results": results,
        "errors": errors
    }

    # ファイルに保存
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    # 完了メッセージ
    print("")
    print("="*60)
    print("✓ スコアリング完了")
    print("="*60)
    print(f"📊 処理統計:")
    print(f"   対象医院数: {len(clinics)}件")
    print(f"   スコア済み: {len(results)}件")
    print(f"   エラー: {len(errors)}件")
    print("")
    print(f"📈 スコア統計:")
    print(f"   平均スコア: {avg_score:.1f}/100")
    print(f"   最高スコア: {max_score}/100")
    print(f"   最低スコア: {min_score}/100")
    print("")
    print(f"📊 スコア分布:")
    print(f"   90-100点: {score_distribution['90_100']}件 ({score_distribution['90_100']/len(results)*100:.1f}%)")
    print(f"   80-89点:  {score_distribution['80_89']}件 ({score_distribution['80_89']/len(results)*100:.1f}%)")
    print(f"   70-79点:  {score_distribution['70_79']}件 ({score_distribution['70_79']/len(results)*100:.1f}%)")
    print(f"   60-69点:  {score_distribution['60_69']}件 ({score_distribution['60_69']/len(results)*100:.1f}%)")
    print(f"   50-59点:  {score_distribution['50_59']}件 ({score_distribution['50_59']/len(results)*100:.1f}%)")
    print(f"   0-49点:   {score_distribution['below_50']}件 ({score_distribution['below_50']/len(results)*100:.1f}%)")
    print("")
    print(f"💾 出力ファイル: {output_path}")
    print("")

if __name__ == "__main__":
    main()
