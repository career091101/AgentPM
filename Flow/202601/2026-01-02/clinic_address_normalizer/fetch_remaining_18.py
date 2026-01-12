#!/usr/bin/env python3
"""
残り18クエリ（愛媛〜鹿児島）の子供向け歯科医院データ取得
"""

import os
import csv
import time
import requests
from datetime import datetime

API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")

if not API_KEY:
    print("❌ Error: GOOGLE_MAPS_API_KEY environment variable not set")
    exit(1)

# 残り9県（愛媛〜鹿児島）
PREFECTURES = [
    "愛媛県", "高知県",
    "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県"
]

SPECIALTIES = ["小児歯科", "矯正歯科"]


def search_clinics(prefecture: str, specialty: str) -> list:
    """歯科医院を検索"""
    query = f"{specialty} {prefecture}"

    search_url = "https://places.googleapis.com/v1/places:searchText"
    search_headers = {
        "X-Goog-Api-Key": API_KEY,
        "Content-Type": "application/json",
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.googleMapsUri,places.websiteUri"
    }
    search_body = {
        "textQuery": query,
        "languageCode": "ja",
        "maxResultCount": 20
    }

    try:
        response = requests.post(search_url, headers=search_headers, json=search_body, timeout=20)

        if response.status_code != 200:
            print(f" ❌ {response.status_code}")
            return []

        data = response.json()
        places = data.get("places", [])

        if not places:
            return []

        results = []
        for place in places:
            place_id = place.get("id")
            display_name = place.get("displayName", {}).get("text", "")
            formatted_address = place.get("formattedAddress", "")
            rating = place.get("rating", 0)
            user_rating_count = place.get("userRatingCount", 0)
            google_maps_uri = place.get("googleMapsUri", "")
            website_uri = place.get("websiteUri", "")

            # Place Details で郵便番号取得
            postal_code = ""
            details_url = f"https://places.googleapis.com/v1/places/{place_id}"
            details_headers = {
                "X-Goog-Api-Key": API_KEY,
                "X-Goog-FieldMask": "addressComponents"
            }
            details_params = {"languageCode": "ja"}

            try:
                details_response = requests.get(details_url, headers=details_headers, params=details_params, timeout=20)
                if details_response.status_code == 200:
                    details_data = details_response.json()
                    address_components = details_data.get("addressComponents", [])
                    for component in address_components:
                        if "postal_code" in component.get("types", []):
                            postal_code = component.get("longText", "")
                            break
            except:
                pass

            results.append({
                "place_id": place_id,
                "医院名": display_name,
                "住所": formatted_address,
                "郵便番号": postal_code,
                "評価": rating,
                "口コミ件数": user_rating_count,
                "Google Maps URL": google_maps_uri,
                "公式ウェブサイト": website_uri,
                "都道府県": prefecture,
                "診療科目": specialty
            })

        return results

    except Exception as e:
        print(f" ❌ {e}")
        return []


def filter_results(results: list) -> list:
    """フィルタリング: レビュー50件以上、評価3.0以上"""
    filtered = []

    for row in results:
        address = row["住所"]
        rating = row["評価"]
        review_count = row["口コミ件数"]

        if "北海道" in address or "沖縄" in address:
            continue
        if review_count < 50:
            continue
        if rating and rating < 3.0:
            continue

        filtered.append(row)

    return filtered


def deduplicate(results: list) -> list:
    """place_idで重複削除"""
    seen = set()
    unique = []

    for row in results:
        pid = row["place_id"]
        if pid not in seen:
            seen.add(pid)
            unique.append(row)

    return unique


# メイン処理
print("=" * 60)
print("残り18クエリデータ取得（愛媛〜鹿児島）")
print("=" * 60)
print(f"対象: {len(PREFECTURES)}県 × {len(SPECIALTIES)}パターン = {len(PREFECTURES) * len(SPECIALTIES)}クエリ\n")

all_results = []
total_queries = len(PREFECTURES) * len(SPECIALTIES)
current_query = 0

for prefecture in PREFECTURES:
    for specialty in SPECIALTIES:
        current_query += 1
        print(f"[{current_query}/{total_queries}] {prefecture} - {specialty}...", end="", flush=True)

        results = search_clinics(prefecture, specialty)
        all_results.extend(results)

        print(f" ✅ {len(results)}件")
        time.sleep(0.5)  # Rate Limit対策（少し長めに）

print(f"\n{'=' * 60}")
print(f"検索完了: {len(all_results)}件（重複含む）")

# 重複削除
unique_results = deduplicate(all_results)
print(f"重複削除後: {len(unique_results)}件")

# フィルタリング
filtered_results = filter_results(unique_results)
print(f"フィルタ後: {len(filtered_results)}件")

# CSV出力
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f"pediatric_dental_remaining_{timestamp}.csv"

if filtered_results:
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ["医院名", "住所", "郵便番号", "評価", "口コミ件数", "Google Maps URL", "公式ウェブサイト", "都道府県", "診療科目"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in filtered_results:
            writer.writerow({k: row[k] for k in fieldnames})

    print(f"\n✅ 出力完了: {output_file}")

    # 統計
    if filtered_results:
        avg_rating = sum(r["評価"] for r in filtered_results if r["評価"]) / len([r for r in filtered_results if r["評価"]])
        avg_reviews = sum(r["口コミ件数"] for r in filtered_results) / len(filtered_results)
        has_website = sum(1 for r in filtered_results if r["公式ウェブサイト"])

        print(f"\n📊 品質指標:")
        print(f"  平均評価: ⭐{avg_rating:.2f}")
        print(f"  平均口コミ件数: {avg_reviews:.0f}件")
        print(f"  公式ウェブサイトあり: {has_website}/{len(filtered_results)} ({has_website/len(filtered_results)*100:.1f}%)")

        # 都道府県別内訳
        from collections import Counter
        prefecture_counts = Counter(r["都道府県"] for r in filtered_results)
        print(f"\n都道府県別内訳:")
        for pref, count in sorted(prefecture_counts.items()):
            print(f"  {pref}: {count}件")

print(f"\n完了時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
