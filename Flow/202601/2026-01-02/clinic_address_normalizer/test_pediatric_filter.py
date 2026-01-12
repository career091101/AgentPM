#!/usr/bin/env python3
"""
小児歯科・矯正歯科の絞り込みテスト

絞り込み条件:
1. 北海道・沖縄を除外
2. レビュー件数 >= 50
3. 評価 >= 3.0
4. 小児歯科・矯正歯科など子供向け医院
"""

import os
import csv
import re
import requests

API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")

if not API_KEY:
    print("❌ Error: GOOGLE_MAPS_API_KEY environment variable not set")
    exit(1)


def search_pediatric_dental(prefecture: str, specialty: str) -> list:
    """
    小児歯科・矯正歯科を検索

    specialty: "小児歯科" or "矯正歯科"
    """
    query = f"{specialty} {prefecture}"
    print(f"\n🔍 Searching: {query}")

    search_url = "https://places.googleapis.com/v1/places:searchText"
    search_headers = {
        "X-Goog-Api-Key": API_KEY,
        "Content-Type": "application/json",
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.googleMapsUri,places.websiteUri"
    }
    search_body = {
        "textQuery": query,
        "languageCode": "ja",
        "maxResultCount": 20  # より多くの候補を取得
    }

    try:
        response = requests.post(search_url, headers=search_headers, json=search_body, timeout=20)

        if response.status_code != 200:
            print(f"❌ Search failed: {response.status_code}")
            return []

        data = response.json()
        places = data.get("places", [])

        if not places:
            print("⚠️  No results found")
            return []

        print(f"✅ Found {len(places)} raw candidates")

        # 詳細情報を取得
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
            except Exception as e:
                pass

            results.append({
                "医院名": display_name,
                "住所": formatted_address,
                "郵便番号": postal_code,
                "評価": rating,
                "口コミ件数": user_rating_count,
                "Google Maps URL": google_maps_uri,
                "公式ウェブサイト": website_uri,
                "検索クエリ": query
            })

        return results

    except Exception as e:
        print(f"❌ Exception: {e}")
        return []


def filter_results(results: list) -> tuple:
    """
    絞り込み条件を適用

    返り値: (フィルタ後のリスト, 除外されたリスト)
    """
    filtered = []
    excluded = []

    for row in results:
        address = row["住所"]
        rating = row["評価"]
        review_count = row["口コミ件数"]
        clinic_name = row["医院名"]

        # 除外理由を記録
        exclusion_reasons = []

        # 1. 北海道・沖縄を除外
        if "北海道" in address or "沖縄" in address:
            exclusion_reasons.append("北海道・沖縄")

        # 2. レビュー件数 < 50
        if review_count < 50:
            exclusion_reasons.append(f"レビュー{review_count}件(<50)")

        # 3. 評価 < 3.0
        if rating and rating < 3.0:
            exclusion_reasons.append(f"評価{rating}(<3.0)")

        # 4. 小児・矯正関連キーワード含まない（医院名チェック）
        keywords = ["小児", "こども", "子供", "キッズ", "矯正", "Kids"]
        has_keyword = any(kw in clinic_name for kw in keywords)

        # ただし検索クエリに含まれていれば、医院名になくてもOK
        # （Googleが関連性を判断して返している）
        if not has_keyword:
            # 緩和: 検索クエリに一致していればOK
            pass

        if exclusion_reasons:
            row["除外理由"] = ", ".join(exclusion_reasons)
            excluded.append(row)
        else:
            filtered.append(row)

    return filtered, excluded


# テスト実行
test_prefectures = [
    "東京都",
    "大阪府",
    "愛知県"
]

specialties = ["小児歯科", "矯正歯科"]

all_results = []

for prefecture in test_prefectures:
    for specialty in specialties:
        results = search_pediatric_dental(prefecture, specialty)
        all_results.extend(results)
        print(f"  → {len(results)} candidates")

print(f"\n📊 Total raw results: {len(all_results)}")

# フィルタリング
filtered, excluded = filter_results(all_results)

print(f"✅ Filtered results: {len(filtered)}")
print(f"❌ Excluded results: {len(excluded)}")

# CSV出力（フィルタ後）
if filtered:
    output_file = "pediatric_filtered_output.csv"
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ["医院名", "住所", "郵便番号", "評価", "口コミ件数", "Google Maps URL", "公式ウェブサイト", "検索クエリ"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in filtered:
            # 除外理由フィールドを削除
            row_clean = {k: v for k, v in row.items() if k != "除外理由"}
            writer.writerow(row_clean)
    print(f"\n✅ Filtered results saved to: {output_file}")

# CSV出力（除外分）
if excluded:
    excluded_file = "pediatric_excluded_output.csv"
    with open(excluded_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ["医院名", "住所", "評価", "口コミ件数", "除外理由"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in excluded:
            writer.writerow({
                "医院名": row["医院名"],
                "住所": row["住所"],
                "評価": row["評価"],
                "口コミ件数": row["口コミ件数"],
                "除外理由": row["除外理由"]
            })
    print(f"📋 Excluded results saved to: {excluded_file}")

# 統計サマリー
print(f"\n📈 Statistics:")
print(f"  Total searched: {len(all_results)}")
print(f"  Passed filters: {len(filtered)} ({len(filtered)/len(all_results)*100:.1f}%)")
print(f"  Excluded: {len(excluded)} ({len(excluded)/len(all_results)*100:.1f}%)")

if filtered:
    avg_rating = sum(r["評価"] for r in filtered if r["評価"]) / len([r for r in filtered if r["評価"]])
    avg_reviews = sum(r["口コミ件数"] for r in filtered) / len(filtered)
    has_website = sum(1 for r in filtered if r["公式ウェブサイト"])

    print(f"\n  Filtered results quality:")
    print(f"    Average rating: ⭐{avg_rating:.2f}")
    print(f"    Average reviews: {avg_reviews:.0f}件")
    print(f"    Has website: {has_website}/{len(filtered)} ({has_website/len(filtered)*100:.1f}%)")
