#!/usr/bin/env python3
"""
Google Maps Platform (Places API New / Geocoding API) を使った医院データ正規化ツール

入力CSV: clinic_query, prefecture, city?, area_hint?, google_maps_url?
出力CSV: 入力項目 + place_id, display_name, formatted_address, postal_code, lat, lng,
         match_confidence, needs_manual_review, error_code, error_message
"""

import csv
import os
import re
import sys
import time
import urllib.parse
from typing import Optional, Dict, List, Tuple

import requests


# ========== 定数 ==========
PLACES_SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"
PLACES_DETAILS_URL = "https://places.googleapis.com/v1/places/{place_id}"
GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json"

MAX_RETRIES = 5
TIMEOUT = 20
MAX_NETWORK_RETRIES = 2

# APIキー
API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")

# キャッシュ（place_idごとに詳細情報を保存）
place_details_cache = {}


# ========== ヘルパー関数 ==========

def extract_place_id_from_url(url: str) -> Optional[str]:
    """
    Google Maps URLからplace_idを抽出

    対応パターン:
    - https://www.google.com/maps/place/.../?q=place_id:ChIJ...
    - https://maps.google.com/?cid=12345... (CIDはplace_idではないので未対応)
    - https://goo.gl/maps/... (短縮URLは展開が必要)

    注: 短縮URLの展開は実装していません（必要に応じて requests.head で Location 取得）
    """
    if not url:
        return None

    # place_id:ChIJ... パターン
    match = re.search(r'place_id[=:]([A-Za-z0-9_-]+)', url)
    if match:
        return match.group(1)

    # /place/.../ パターンから抽出は難しいため、place_idパラメータがない場合はNone
    return None


def exponential_backoff_retry(func, *args, **kwargs):
    """
    指数バックオフでリトライ

    - 429 (OVER_QUERY_LIMIT): 最大5回リトライ
    - Timeout: 最大5回リトライ
    - Network Error: 最大2回リトライ
    """
    last_exception = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = func(*args, **kwargs)

            # 429 Rate Limit
            if response.status_code == 429:
                wait_time = 2 ** attempt
                print(f"  [WARN] Rate limit (429), retrying in {wait_time}s (attempt {attempt}/{MAX_RETRIES})")
                time.sleep(wait_time)
                continue

            return response

        except requests.exceptions.Timeout as e:
            last_exception = e
            if attempt == MAX_RETRIES:
                raise
            wait_time = 2 ** attempt
            print(f"  [WARN] Timeout, retrying in {wait_time}s (attempt {attempt}/{MAX_RETRIES})")
            time.sleep(wait_time)

        except requests.exceptions.RequestException as e:
            last_exception = e
            if attempt >= MAX_NETWORK_RETRIES:
                raise
            wait_time = 2 ** attempt
            print(f"  [WARN] Network error, retrying in {wait_time}s (attempt {attempt}/{MAX_NETWORK_RETRIES})")
            time.sleep(wait_time)

    if last_exception:
        raise last_exception

    return None


# ========== API呼び出し ==========

def places_text_search(query: str, api_key: str) -> List[Dict]:
    """
    Places Text Search (New)

    Endpoint: POST https://places.googleapis.com/v1/places:searchText
    FieldMask: places.id,places.displayName,places.formattedAddress,places.location
    最大5件取得
    """
    headers = {
        "X-Goog-Api-Key": api_key,
        "Content-Type": "application/json",
        "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.location"
    }
    body = {
        "textQuery": query,
        "maxResultCount": 5
    }

    try:
        response = exponential_backoff_retry(
            requests.post,
            PLACES_SEARCH_URL,
            headers=headers,
            json=body,
            timeout=TIMEOUT
        )

        if response and response.status_code == 200:
            data = response.json()
            return data.get("places", [])

    except Exception as e:
        print(f"  [ERROR] Places Text Search failed: {e}")

    return []


def place_details(place_id: str, api_key: str) -> Optional[Dict]:
    """
    Place Details (New)

    Endpoint: GET https://places.googleapis.com/v1/places/{place_id}
    FieldMask: id,displayName,formattedAddress,addressComponents,location

    キャッシュを使用して重複リクエストを防止
    """
    if place_id in place_details_cache:
        return place_details_cache[place_id]

    url = PLACES_DETAILS_URL.format(place_id=place_id)
    headers = {
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "id,displayName,formattedAddress,addressComponents,location"
    }

    try:
        response = exponential_backoff_retry(
            requests.get,
            url,
            headers=headers,
            timeout=TIMEOUT
        )

        if response and response.status_code == 200:
            data = response.json()
            place_details_cache[place_id] = data
            return data

    except Exception as e:
        print(f"  [ERROR] Place Details failed: {e}")

    return None


def geocode_address(address: str, api_key: str) -> Optional[str]:
    """
    Geocoding API で postal_code を補完

    Place Details で postal_code が取得できなかった場合のみ使用
    """
    params = {
        "address": address,
        "key": api_key
    }

    try:
        response = exponential_backoff_retry(
            requests.get,
            GEOCODING_URL,
            params=params,
            timeout=TIMEOUT
        )

        if response and response.status_code == 200:
            data = response.json()
            if data.get("status") == "OK" and data.get("results"):
                components = data["results"][0].get("address_components", [])
                for component in components:
                    if "postal_code" in component.get("types", []):
                        return component.get("long_name", "")

    except Exception as e:
        print(f"  [ERROR] Geocoding failed: {e}")

    return None


# ========== スコアリング ==========

def score_candidate(place: Dict, clinic_query: str, prefecture: str, city: Optional[str]) -> int:
    """
    候補をスコアリング

    - formattedAddress に prefecture 含む: +2
    - displayName に clinic_query 主要語一致: +2
    - formattedAddress に city 含む: +1 (任意)
    """
    score = 0
    formatted_address = place.get("formattedAddress", "")
    display_name = place.get("displayName", {}).get("text", "")

    # prefecture 含む +2
    if prefecture in formatted_address:
        score += 2

    # clinic_query 主要語一致 +2
    # 主要語の定義: clinic_queryから「医院」「クリニック」「病院」等を除いた部分
    main_word = re.sub(r'(医院|クリニック|病院|歯科|整形外科|内科|外科|耳鼻科|眼科|皮膚科|小児科)', '', clinic_query).strip()
    if main_word and main_word in display_name:
        score += 2

    # city 含む +1
    if city and city in formatted_address:
        score += 1

    return score


def extract_postal_code_from_address_components(components: List[Dict]) -> Optional[str]:
    """
    addressComponents から postal_code を抽出
    """
    for component in components:
        if "postal_code" in component.get("types", []):
            return component.get("longText", "")
    return None


# ========== メイン処理 ==========

def process_row(row: Dict, api_key: str) -> Dict:
    """
    1行を処理

    フロー:
    1. google_maps_url から place_id 抽出
    2. place_id がない場合、Places Text Search
    3. 候補をスコアリングして上位1件採用
    4. Place Details で詳細取得
    5. postal_code が取れない場合、Geocoding で補完
    """
    clinic_query = row.get("clinic_query", "").strip()
    prefecture = row.get("prefecture", "").strip()
    city = row.get("city", "").strip()
    area_hint = row.get("area_hint", "").strip()
    google_maps_url = row.get("google_maps_url", "").strip()

    result = {
        **row,
        "place_id": "",
        "display_name": "",
        "formatted_address": "",
        "postal_code": "",
        "lat": "",
        "lng": "",
        "match_confidence": "",
        "needs_manual_review": "false",
        "error_code": "",
        "error_message": ""
    }

    try:
        # Step 1: google_maps_url から place_id 抽出
        place_id = None
        if google_maps_url:
            place_id = extract_place_id_from_url(google_maps_url)
            if place_id:
                print(f"  [INFO] Extracted place_id from URL: {place_id}")

        # Step 2: place_id がない場合、Places Text Search
        if not place_id:
            query_parts = [clinic_query, prefecture]
            if city:
                query_parts.append(city)
            if area_hint:
                query_parts.append(area_hint)
            query = " ".join(query_parts)

            print(f"  [INFO] Searching: {query}")
            candidates = places_text_search(query, api_key)

            if not candidates:
                result["error_code"] = "NO_CANDIDATES"
                result["error_message"] = "Places Text Search returned no results"
                result["needs_manual_review"] = "true"
                return result

            # スコアリング
            scored_candidates = [(c, score_candidate(c, clinic_query, prefecture, city)) for c in candidates]
            scored_candidates.sort(key=lambda x: x[1], reverse=True)

            # 上位1件採用
            best_candidate, best_score = scored_candidates[0]
            place_id = best_candidate.get("id")

            print(f"  [INFO] Best candidate: {best_candidate.get('displayName', {}).get('text', '')} (score: {best_score})")

            # スコア僅差や県不一致チェック
            if best_score < 2:  # prefecture が含まれていない
                result["needs_manual_review"] = "true"
                print(f"  [WARN] Low score ({best_score}), manual review recommended")

            if len(scored_candidates) > 1 and scored_candidates[1][1] >= best_score - 1:
                result["needs_manual_review"] = "true"
                print(f"  [WARN] Close scores, manual review recommended")

        # Step 3: Place Details
        if not place_id:
            result["error_code"] = "NO_PLACE_ID"
            result["error_message"] = "Could not obtain place_id"
            result["needs_manual_review"] = "true"
            return result

        details = place_details(place_id, api_key)
        if not details:
            result["error_code"] = "PLACE_DETAILS_FAILED"
            result["error_message"] = "Place Details API failed"
            result["needs_manual_review"] = "true"
            return result

        result["place_id"] = details.get("id", "")
        result["display_name"] = details.get("displayName", {}).get("text", "")
        result["formatted_address"] = details.get("formattedAddress", "")

        location = details.get("location", {})
        result["lat"] = str(location.get("latitude", ""))
        result["lng"] = str(location.get("longitude", ""))

        # postal_code 抽出
        address_components = details.get("addressComponents", [])
        postal_code = extract_postal_code_from_address_components(address_components)

        # Step 4: postal_code が取れない場合、Geocoding
        if not postal_code and result["formatted_address"]:
            print(f"  [INFO] Postal code not found in Place Details, trying Geocoding...")
            postal_code = geocode_address(result["formatted_address"], api_key)

        result["postal_code"] = postal_code or ""

        # match_confidence 判定
        if result["needs_manual_review"] == "true":
            result["match_confidence"] = "low"
        elif postal_code and prefecture in result["formatted_address"]:
            result["match_confidence"] = "high"
        else:
            result["match_confidence"] = "mid"

    except Exception as e:
        result["error_code"] = "EXCEPTION"
        result["error_message"] = str(e)
        result["needs_manual_review"] = "true"
        print(f"  [ERROR] Exception: {e}")

    return result


def main(input_csv: str, output_csv: str, api_key: str):
    """
    メイン処理

    入力CSVを読み込み、各行を処理して出力CSVに書き出す
    """
    if not os.path.exists(input_csv):
        print(f"Error: Input file not found: {input_csv}")
        sys.exit(1)

    with open(input_csv, 'r', encoding='utf-8') as f_in:
        reader = csv.DictReader(f_in)
        rows = list(reader)

    if not rows:
        print("Error: Input CSV is empty")
        sys.exit(1)

    print(f"Processing {len(rows)} rows...")

    results = []
    for i, row in enumerate(rows, 1):
        print(f"\n[{i}/{len(rows)}] {row.get('clinic_query', '')}")
        result = process_row(row, api_key)
        results.append(result)
        time.sleep(0.1)  # Rate limit 対策

    # 出力
    if results:
        fieldnames = list(results[0].keys())
        with open(output_csv, 'w', encoding='utf-8', newline='') as f_out:
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"\n✅ Completed. Output: {output_csv}")

        # 統計
        total = len(results)
        high_confidence = sum(1 for r in results if r["match_confidence"] == "high")
        needs_review = sum(1 for r in results if r["needs_manual_review"] == "true")
        errors = sum(1 for r in results if r["error_code"])

        print(f"\n📊 Statistics:")
        print(f"  Total: {total}")
        print(f"  High confidence: {high_confidence} ({high_confidence/total*100:.1f}%)")
        print(f"  Needs manual review: {needs_review} ({needs_review/total*100:.1f}%)")
        print(f"  Errors: {errors} ({errors/total*100:.1f}%)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <input.csv> <output.csv>")
        print("\nEnvironment variables:")
        print("  GOOGLE_MAPS_API_KEY: Google Maps Platform API key (required)")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not API_KEY:
        print("Error: GOOGLE_MAPS_API_KEY environment variable not set")
        print("\nPlease set your API key:")
        print("  export GOOGLE_MAPS_API_KEY='your_api_key_here'")
        sys.exit(1)

    main(input_file, output_file, API_KEY)
