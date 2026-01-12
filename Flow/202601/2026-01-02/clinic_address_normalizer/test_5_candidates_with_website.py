#!/usr/bin/env python3
"""
5件候補抽出 + Googleレビュー情報 + 公式ウェブサイトURL取得テスト
"""

import os
import csv
import requests

API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")

if not API_KEY:
    print("❌ Error: GOOGLE_MAPS_API_KEY environment variable not set")
    exit(1)

def search_and_get_details(query: str) -> list:
    """
    Places Text Search で5件取得 → 各候補の詳細情報を取得
    """
    # Step 1: Places Text Search (最大5件)
    print(f"\n🔍 Searching: {query}")
    search_url = "https://places.googleapis.com/v1/places:searchText"
    search_headers = {
        "X-Goog-Api-Key": API_KEY,
        "Content-Type": "application/json",
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.rating,places.userRatingCount,places.googleMapsUri,places.websiteUri"
    }
    search_body = {
        "textQuery": query,
        "languageCode": "ja",  # 日本語で取得
        "maxResultCount": 5
    }

    try:
        response = requests.post(search_url, headers=search_headers, json=search_body, timeout=20)

        if response.status_code != 200:
            print(f"❌ Search failed: {response.status_code} - {response.text}")
            return []

        data = response.json()
        places = data.get("places", [])

        if not places:
            print("⚠️  No results found")
            return []

        print(f"✅ Found {len(places)} candidates")

        # Step 2: 各候補の詳細情報を取得（郵便番号のため）
        results = []
        for i, place in enumerate(places, 1):
            place_id = place.get("id")
            display_name = place.get("displayName", {}).get("text", "")
            formatted_address = place.get("formattedAddress", "")
            rating = place.get("rating", "")
            user_rating_count = place.get("userRatingCount", 0)
            google_maps_uri = place.get("googleMapsUri", "")
            website_uri = place.get("websiteUri", "")  # 公式ウェブサイト

            # Place Details で郵便番号取得
            postal_code = ""
            details_url = f"https://places.googleapis.com/v1/places/{place_id}"
            details_headers = {
                "X-Goog-Api-Key": API_KEY,
                "X-Goog-FieldMask": "addressComponents"
            }
            details_params = {
                "languageCode": "ja"
            }

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
                print(f"  [WARN] Failed to get postal code for {display_name}: {e}")

            results.append({
                "順位": i,
                "医院名": display_name,
                "住所": formatted_address,
                "郵便番号": postal_code,
                "Google Maps URL": google_maps_uri,
                "公式ウェブサイト": website_uri,
                "評価": rating,
                "口コミ件数": user_rating_count
            })

            website_status = f"🌐 {website_uri[:40]}..." if website_uri else "❌ なし"
            print(f"  [{i}] {display_name} ⭐{rating} ({user_rating_count}件) - {website_status}")

        return results

    except Exception as e:
        print(f"❌ Exception: {e}")
        return []


# テスト実行
test_queries = [
    "田中歯科クリニック 東京都 渋谷区",
    "慶應義塾大学病院 東京都",
    "梅ヶ丘歯科クリニック 東京都"
]

all_results = []

for query in test_queries:
    results = search_and_get_details(query)
    all_results.extend(results)
    print()

# CSV出力
if all_results:
    output_file = "test_with_website_output.csv"
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ["順位", "医院名", "住所", "郵便番号", "Google Maps URL", "公式ウェブサイト", "評価", "口コミ件数"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    print(f"\n✅ Results saved to: {output_file}")
    print(f"📊 Total candidates: {len(all_results)}")

    # 公式ウェブサイトが取得できた件数を集計
    has_website = sum(1 for r in all_results if r["公式ウェブサイト"])
    print(f"🌐 公式ウェブサイトあり: {has_website}/{len(all_results)} ({has_website/len(all_results)*100:.1f}%)")
else:
    print("\n❌ No results to save")
