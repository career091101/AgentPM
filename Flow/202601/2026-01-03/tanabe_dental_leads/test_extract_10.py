#!/usr/bin/env python3
"""
田辺玩具向け歯科医院営業リスト抽出（テスト版：10件）

取得情報:
- 医院名
- 郵便番号
- 住所
- 電話番号
- WebサイトURL
- 評価
- レビュー件数
"""

import googlemaps
import csv
import os
from datetime import datetime
import time
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

# API設定
API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
if not API_KEY:
    raise ValueError("環境変数 GOOGLE_MAPS_API_KEY が設定されていません")

# Google Maps クライアント初期化
gmaps = googlemaps.Client(key=API_KEY)

def extract_postal_code(address_components):
    """住所コンポーネントから郵便番号を抽出"""
    for component in address_components:
        if 'postal_code' in component['types']:
            return component['long_name']
    return ''

def extract_types_tags(types_list):
    """
    types から診療科目タグを抽出

    Args:
        types_list: Google Maps APIから取得したtypesリスト

    Returns:
        str: カンマ区切りのタグ文字列
    """
    tags = []

    if any('dentist' in t.lower() for t in types_list):
        tags.append('歯科')

    if any('pediatric' in t.lower() or 'child' in t.lower() for t in types_list):
        tags.append('小児対応')

    if any('orthodont' in t.lower() for t in types_list):
        tags.append('矯正歯科')

    if any('health' in t.lower() for t in types_list):
        tags.append('健康施設')

    return ', '.join(tags) if tags else '一般歯科'

def search_dental_clinics(location='東京都', limit=10):
    """
    歯科医院を検索

    Args:
        location: 検索エリア
        limit: 取得件数

    Returns:
        list: 歯科医院情報のリスト
    """
    results = []

    # 検索クエリ（小児歯科または矯正歯科）
    queries = [
        f'小児歯科 {location}',
        f'矯正歯科 {location}'
    ]

    seen_place_ids = set()

    for query in queries:
        if len(results) >= limit:
            break

        print(f"\n検索中: {query}")

        try:
            # Text Search実行
            places_result = gmaps.places(
                query=query,
                language='ja',
                region='jp'
            )

            if places_result['status'] == 'OK':
                for place in places_result['results']:
                    if len(results) >= limit:
                        break

                    place_id = place['place_id']

                    # 重複チェック
                    if place_id in seen_place_ids:
                        continue

                    seen_place_ids.add(place_id)

                    # 基本情報
                    name = place.get('name', '')
                    rating = place.get('rating', 0)
                    user_ratings_total = place.get('user_ratings_total', 0)

                    print(f"  取得中: {name} (評価: {rating}, レビュー: {user_ratings_total}件)")

                    # 詳細情報を取得（電話番号、WebサイトURL含む）
                    time.sleep(0.1)  # API制限対策

                    place_details = gmaps.place(
                        place_id=place_id,
                        language='ja',
                        fields=[
                            'name',
                            'formatted_address',
                            'address_component',
                            'formatted_phone_number',
                            'website',
                            'rating',
                            'user_ratings_total',
                            'url',
                            'type',
                            'photo'
                        ]
                    )

                    if place_details['status'] == 'OK':
                        detail = place_details['result']

                        # 郵便番号抽出
                        postal_code = extract_postal_code(
                            detail.get('address_components', [])
                        )

                        clinic_data = {
                            '医院名': detail.get('name', ''),
                            '郵便番号': postal_code,
                            '住所': detail.get('formatted_address', ''),
                            '電話番号': detail.get('formatted_phone_number', ''),
                            'WebサイトURL': detail.get('website', ''),
                            '評価': detail.get('rating', 0),
                            'レビュー件数': detail.get('user_ratings_total', 0),
                            'Google Maps URL': detail.get('url', ''),
                            '診療科目タグ': extract_types_tags(detail.get('types', [])),
                            '写真枚数': len(detail.get('photos', [])),
                            'スコア': 0  # 後で計算
                        }

                        # スコア計算
                        score = calculate_advanced_score(clinic_data, website_analysis=None)
                        clinic_data['スコア'] = score

                        results.append(clinic_data)

                        print(f"    ✓ 取得完了 (スコア: {score})")

        except Exception as e:
            print(f"エラー: {e}")
            continue

    return results

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

    Args:
        clinic_data: 医院データ
        website_analysis: Webサイト分析結果
        return_breakdown: Trueの場合、(score, breakdown)のタプルを返す

    Returns:
        return_breakdown=False: スコア値のみ
        return_breakdown=True: (スコア値, 内訳辞書)
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
        # WebサイトURLボーナス
        if clinic_data.get('WebサイトURL'):
            score += 10
            breakdown["web_activity"]["score"] = 10

        # 写真枚数（最大10点）
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

        # 診療科目タグ（最大15点）
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

    # 3-1. キッズコンテンツ（20点）
    if website_analysis.get('kids_content'):
        kids_score += 20
        breakdown["children_friendliness"]["kids_content"] = 20

    # 3-2. 待合室の写真（15点）
    if website_analysis.get('waiting_room_photo'):
        kids_score += 15
        breakdown["children_friendliness"]["waiting_room_photo"] = 15

    # 3-3. 診療科目（15点）
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

    # 5-1. 営業時間の長さ（10点）
    operating_hours = website_analysis.get('operating_hours', '')
    if operating_hours:
        if '土' in operating_hours or '日' in operating_hours:
            scale_score += 5
            breakdown["clinic_scale"]["weekend_hours"] = 5
        if '19:00' in operating_hours or '20:00' in operating_hours or '21:00' in operating_hours:
            scale_score += 5
            breakdown["clinic_scale"]["evening_hours"] = 5

    # 5-2. 写真枚数（10点）
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
        from datetime import datetime, timedelta
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

def save_to_csv(data, filename='test_dental_leads_10.csv'):
    """CSV出力"""
    if not data:
        print("データがありません")
        return

    # スコア順にソート
    data_sorted = sorted(data, key=lambda x: x['スコア'], reverse=True)

    fieldnames = [
        'スコア',
        '医院名',
        '郵便番号',
        '住所',
        '電話番号',
        'WebサイトURL',
        '評価',
        'レビュー件数',
        '診療科目タグ',
        '写真枚数',
        'Google Maps URL'
    ]

    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_sorted)

    print(f"\n✓ CSV出力完了: {filename}")

def estimate_cost(num_clinics):
    """コスト推定"""
    # Text Search: $32/1,000件
    # Place Details (Basic + Contact): $20/1,000件
    text_search_cost = (num_clinics / 1000) * 32
    place_details_cost = (num_clinics / 1000) * 20
    total_cost_usd = text_search_cost + place_details_cost
    total_cost_jpy = total_cost_usd * 150  # 1ドル=150円

    print(f"\n--- コスト推定 ---")
    print(f"Text Search: ${text_search_cost:.4f}")
    print(f"Place Details: ${place_details_cost:.4f}")
    print(f"合計: ${total_cost_usd:.4f} (約{total_cost_jpy:.0f}円)")

    return total_cost_usd

def main():
    print("=" * 60)
    print("田辺玩具向け歯科医院営業リスト抽出（テスト版：10件）")
    print("=" * 60)

    start_time = datetime.now()

    # 10件抽出
    clinics = search_dental_clinics(location='東京都', limit=10)

    # CSV保存
    output_file = f'test_dental_leads_10_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    save_to_csv(clinics, output_file)

    # 統計情報
    print(f"\n--- 統計情報 ---")
    print(f"取得件数: {len(clinics)}件")

    if clinics:
        avg_rating = sum(c['評価'] for c in clinics) / len(clinics)
        avg_reviews = sum(c['レビュー件数'] for c in clinics) / len(clinics)
        with_website = sum(1 for c in clinics if c['WebサイトURL'])

        print(f"平均評価: {avg_rating:.2f}★")
        print(f"平均レビュー件数: {avg_reviews:.0f}件")
        print(f"Webサイトあり: {with_website}件 ({with_website/len(clinics)*100:.1f}%)")

    # コスト推定
    estimate_cost(10)

    # 5,100件抽出時のコスト推定
    print(f"\n--- 本番実行（5,100件）の場合のコスト推定 ---")
    estimate_cost(5100)

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    print(f"\n実行時間: {elapsed:.1f}秒")
    print(f"\n✓ テスト完了")

if __name__ == '__main__':
    main()
