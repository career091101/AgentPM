#!/usr/bin/env python3
"""
スコア根拠付き分析スクリプト

CSVとWebサイト分析結果を統合し、スコアの内訳を出力します。
"""

import csv
import json
from datetime import datetime

def calculate_advanced_score(clinic_data, website_analysis=None, return_breakdown=False):
    """
    Phase C: 精緻スコアリング（最大200点）

    配点:
    - 基礎評価: 80点（評価★ × 16点）
    - 来院患者数: 20点（レビュー件数ボーナス）
    - 子ども対応力: 50点（キッズコンテンツ20 + 待合室写真15 + 診療科目15）
    - Web積極性: 20点（SNS連携 各5点 × 4種類）
    - 医院規模: 20点（営業時間10 + 写真枚数10）
    - ブログ活動: 10点（更新頻度）

    合計: 200点
    """
    score = 0
    breakdown = {
        "base_evaluation": {"score": 0, "max": 80, "rating": 0},
        "patient_volume": {"score": 0, "max": 20, "reviews": 0},
        "children_friendliness": {"score": 0, "max": 50, "kids_content": 0, "waiting_room_photo": 0, "specialty_tag": 0},
        "web_activity": {"score": 0, "max": 20, "instagram": 0, "facebook": 0, "line": 0, "twitter": 0},
        "clinic_scale": {"score": 0, "max": 20, "weekend_hours": 0, "evening_hours": 0, "photo_count_bonus": 0},
        "blog_activity": {"score": 0, "max": 10, "last_updated": None, "days_ago": None}
    }

    # 1. 基礎評価（最大80点）
    rating = float(clinic_data.get('評価', 0))
    base_score = rating * 16
    score += base_score
    breakdown["base_evaluation"]["score"] = round(base_score, 1)
    breakdown["base_evaluation"]["rating"] = rating

    # 2. 来院患者数（最大20点）
    reviews = int(clinic_data.get('レビュー件数', 0))
    patient_score = 0
    if reviews >= 100:
        patient_score = 20
    elif reviews >= 50:
        patient_score = 15
    elif reviews >= 20:
        patient_score = 10
    elif reviews >= 10:
        patient_score = 5

    score += patient_score
    breakdown["patient_volume"]["score"] = patient_score
    breakdown["patient_volume"]["reviews"] = reviews

    # Webサイト分析がない場合は簡易版
    if not website_analysis:
        if clinic_data.get('WebサイトURL'):
            score += 10
            breakdown["web_activity"]["score"] = 10

        photo_count = int(clinic_data.get('写真枚数', 0))
        photo_bonus = 0
        if photo_count >= 20:
            photo_bonus = 10
        elif photo_count >= 10:
            photo_bonus = 7
        elif photo_count >= 5:
            photo_bonus = 4

        score += photo_bonus
        breakdown["clinic_scale"]["score"] = photo_bonus
        breakdown["clinic_scale"]["photo_count_bonus"] = photo_bonus

        tags = clinic_data.get('診療科目タグ', '')
        specialty_score = 0
        if '小児対応' in tags:
            specialty_score = 15
        elif '矯正歯科' in tags:
            specialty_score = 8

        score += specialty_score
        breakdown["children_friendliness"]["score"] = specialty_score
        breakdown["children_friendliness"]["specialty_tag"] = specialty_score

        final_score = round(score, 1)
        breakdown["total_score"] = final_score

        if return_breakdown:
            return final_score, breakdown
        return final_score

    # --- Webサイト分析あり（フルスコアリング） ---

    # 3. 子ども対応力（最大50点）
    kids_score = 0

    if website_analysis.get('kids_content'):
        kids_score += 20
        breakdown["children_friendliness"]["kids_content"] = 20

    if website_analysis.get('waiting_room_photo'):
        kids_score += 15
        breakdown["children_friendliness"]["waiting_room_photo"] = 15

    tags = clinic_data.get('診療科目タグ', '')
    specialty_tag_score = 0
    if '小児対応' in tags:
        specialty_tag_score = 15
    elif '矯正歯科' in tags:
        specialty_tag_score = 8

    kids_score += specialty_tag_score
    breakdown["children_friendliness"]["specialty_tag"] = specialty_tag_score
    breakdown["children_friendliness"]["score"] = kids_score
    score += kids_score

    # 4. Web積極性（最大20点）
    web_score = 0

    if website_analysis.get('sns_instagram'):
        web_score += 5
        breakdown["web_activity"]["instagram"] = 5
    if website_analysis.get('sns_facebook'):
        web_score += 5
        breakdown["web_activity"]["facebook"] = 5
    if website_analysis.get('sns_line'):
        web_score += 5
        breakdown["web_activity"]["line"] = 5
    if website_analysis.get('sns_twitter'):
        web_score += 5
        breakdown["web_activity"]["twitter"] = 5

    breakdown["web_activity"]["score"] = web_score
    score += web_score

    # 5. 医院規模（最大20点）
    scale_score = 0

    operating_hours = website_analysis.get('operating_hours', '')
    if operating_hours:
        if '土' in operating_hours or '日' in operating_hours:
            scale_score += 5
            breakdown["clinic_scale"]["weekend_hours"] = 5
        if '19:00' in operating_hours or '20:00' in operating_hours or '21:00' in operating_hours:
            scale_score += 5
            breakdown["clinic_scale"]["evening_hours"] = 5

    photo_count = int(clinic_data.get('写真枚数', 0))
    photo_bonus = 0
    if photo_count >= 20:
        photo_bonus = 10
    elif photo_count >= 10:
        photo_bonus = 5

    scale_score += photo_bonus
    breakdown["clinic_scale"]["photo_count_bonus"] = photo_bonus
    breakdown["clinic_scale"]["score"] = scale_score
    score += scale_score

    # 6. ブログ活動（最大10点）
    blog_score = 0
    blog_updated = website_analysis.get('blog_updated')
    if blog_updated:
        try:
            last_update = datetime.strptime(blog_updated, '%Y-%m-%d')
            days_ago = (datetime.now() - last_update).days

            if days_ago <= 30:
                blog_score = 10
            elif days_ago <= 90:
                blog_score = 5

            breakdown["blog_activity"]["last_updated"] = blog_updated
            breakdown["blog_activity"]["days_ago"] = days_ago
        except:
            pass

    breakdown["blog_activity"]["score"] = blog_score
    score += blog_score

    final_score = round(score, 1)
    breakdown["total_score"] = final_score

    if return_breakdown:
        return final_score, breakdown
    return final_score

def main():
    print("=" * 60)
    print("スコア根拠付き分析")
    print("=" * 60)

    # CSVファイル読み込み
    csv_file = 'test_dental_leads_10_20260103_215311.csv'
    print(f"\nCSV読み込み: {csv_file}")

    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        clinics = list(reader)

    # Webサイト分析結果読み込み
    analysis_file = 'website_analysis_test_20260103_223000.json'
    print(f"Webサイト分析結果読み込み: {analysis_file}")

    with open(analysis_file, 'r', encoding='utf-8') as f:
        analysis_data = json.load(f)
        website_analysis = analysis_data['results']

    # スコア根拠付き分析
    results = []
    all_breakdowns = {}

    for clinic in clinics:
        clinic_name = clinic['医院名']
        analysis = website_analysis.get(clinic_name)

        # スコアと内訳を取得
        score, breakdown = calculate_advanced_score(
            clinic,
            website_analysis=analysis,
            return_breakdown=True
        )

        # CSVデータ更新
        clinic['スコア'] = score

        # 内訳をCSVに追加
        clinic['基礎評価'] = breakdown['base_evaluation']['score']
        clinic['来院患者数'] = breakdown['patient_volume']['score']
        clinic['子ども対応力'] = breakdown['children_friendliness']['score']
        clinic['Web積極性'] = breakdown['web_activity']['score']
        clinic['医院規模'] = breakdown['clinic_scale']['score']
        clinic['ブログ活動'] = breakdown['blog_activity']['score']

        # SNS連携情報
        if analysis:
            sns_list = []
            if analysis.get('sns_instagram'):
                sns_list.append('Instagram')
            if analysis.get('sns_facebook'):
                sns_list.append('Facebook')
            if analysis.get('sns_line'):
                sns_list.append('LINE')
            if analysis.get('sns_twitter'):
                sns_list.append('Twitter')

            clinic['SNS連携'] = '+'.join(sns_list) if sns_list else 'なし'
        else:
            clinic['SNS連携'] = 'なし'

        clinic['子ども対応力スコア'] = breakdown['children_friendliness']['score']

        results.append(clinic)
        all_breakdowns[clinic_name] = breakdown

    # スコア順にソート
    results_sorted = sorted(results, key=lambda x: float(x['スコア']), reverse=True)

    # CSV出力
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_output = f'test_dental_leads_with_breakdown_{timestamp}.csv'

    fieldnames = [
        'スコア',
        '医院名',
        '基礎評価',
        '来院患者数',
        '子ども対応力',
        'Web積極性',
        '医院規模',
        'ブログ活動',
        '郵便番号',
        '住所',
        '電話番号',
        'WebサイトURL',
        '評価',
        'レビュー件数',
        '診療科目タグ',
        '写真枚数',
        'SNS連携',
        '子ども対応力スコア',
        'Google Maps URL'
    ]

    with open(csv_output, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results_sorted)

    print(f"\n✓ CSV出力完了: {csv_output}")

    # JSON出力（詳細な内訳）
    json_output = f'test_dental_leads_breakdown_detail_{timestamp}.json'

    output_data = {
        "metadata": {
            "total_clinics": len(results),
            "timestamp": datetime.now().isoformat(),
            "source_csv": csv_file,
            "source_analysis": analysis_file
        },
        "scoring_criteria": {
            "base_evaluation": {"max": 80, "description": "評価★ × 16点"},
            "patient_volume": {"max": 20, "description": "レビュー件数ボーナス"},
            "children_friendliness": {"max": 50, "description": "キッズコンテンツ20 + 待合室写真15 + 診療科目15"},
            "web_activity": {"max": 20, "description": "SNS連携 各5点 × 4種類"},
            "clinic_scale": {"max": 20, "description": "営業時間10 + 写真枚数10"},
            "blog_activity": {"max": 10, "description": "更新頻度"}
        },
        "clinics": []
    }

    for clinic in results_sorted:
        clinic_name = clinic['医院名']
        breakdown = all_breakdowns[clinic_name]

        clinic_detail = {
            "name": clinic_name,
            "total_score": float(clinic['スコア']),
            "rank": results_sorted.index(clinic) + 1,
            "breakdown": breakdown,
            "basic_info": {
                "postal_code": clinic['郵便番号'],
                "address": clinic['住所'],
                "phone": clinic['電話番号'],
                "website": clinic['WebサイトURL'],
                "rating": float(clinic['評価']),
                "reviews": int(clinic['レビュー件数']),
                "tags": clinic['診療科目タグ'],
                "photos": int(clinic['写真枚数'])
            },
            "sns": clinic['SNS連携']
        }

        output_data["clinics"].append(clinic_detail)

    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"✓ JSON出力完了: {json_output}")

    # 統計情報
    print(f"\n--- 統計情報 ---")
    print(f"総件数: {len(results)}件")

    avg_score = sum(float(c['スコア']) for c in results) / len(results)
    print(f"平均スコア: {avg_score:.1f}点")

    high_score_count = sum(1 for c in results if float(c['スコア']) >= 150)
    print(f"高スコア（150点以上）: {high_score_count}件")

    # 各カテゴリの平均スコア
    print(f"\n--- カテゴリ別平均スコア ---")
    for category in ['基礎評価', '来院患者数', '子ども対応力', 'Web積極性', '医院規模', 'ブログ活動']:
        avg = sum(float(c[category]) for c in results) / len(results)
        max_score = 80 if category == '基礎評価' else (20 if category in ['来院患者数', 'Web積極性', '医院規模'] else (50 if category == '子ども対応力' else 10))
        print(f"{category}: {avg:.1f}点 / {max_score}点 ({avg/max_score*100:.1f}%)")

    # Top 3医院の詳細
    print(f"\n--- Top 3医院の詳細 ---")
    for i, clinic in enumerate(results_sorted[:3], 1):
        print(f"\n{i}. {clinic['医院名']}: {clinic['スコア']}点")
        print(f"   基礎評価: {clinic['基礎評価']}点 (評価★{clinic['評価']})")
        print(f"   来院患者数: {clinic['来院患者数']}点 (レビュー{clinic['レビュー件数']}件)")
        print(f"   子ども対応力: {clinic['子ども対応力']}点")
        print(f"   Web積極性: {clinic['Web積極性']}点 (SNS: {clinic['SNS連携']})")
        print(f"   医院規模: {clinic['医院規模']}点")
        print(f"   ブログ活動: {clinic['ブログ活動']}点")

    print(f"\n✓ 処理完了")

if __name__ == '__main__':
    main()
