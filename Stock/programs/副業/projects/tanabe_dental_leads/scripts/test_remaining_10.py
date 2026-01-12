#!/usr/bin/env python3
"""
残り43都府県データ取得テスト版（10件）

テスト内容:
- 宮城県から10件取得
- APIフィールド名の動作確認
- JSON保存形式の確認
"""

import googlemaps
import json
import os
from datetime import datetime
import time
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
if not API_KEY:
    raise ValueError("環境変数 GOOGLE_MAPS_API_KEY が設定されていません")

gmaps = googlemaps.Client(key=API_KEY)

def search_dental_clinics_test(prefecture='宮城県', limit=10):
    """
    テスト検索（10件）

    Args:
        prefecture: 都道府県名
        limit: 取得件数

    Returns:
        list: 医院データリスト
    """
    results = []
    seen_place_ids = set()

    queries = [
        f'小児歯科 {prefecture}',
        f'矯正歯科 {prefecture}'
    ]

    for query in queries:
        if len(results) >= limit:
            break

        print(f"\n検索中: {query}")

        try:
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

                    if place_id in seen_place_ids:
                        continue

                    seen_place_ids.add(place_id)

                    # 詳細情報取得
                    time.sleep(0.1)

                    try:
                        place_details = gmaps.place(
                            place_id=place_id,
                            language='ja',
                            fields=[
                                'name', 'formatted_address', 'address_component',
                                'formatted_phone_number', 'website', 'rating',
                                'user_ratings_total', 'url', 'type', 'photo'
                            ]
                        )

                        if place_details['status'] == 'OK':
                            detail = place_details['result']
                            results.append(detail)

                            name = detail.get('name', '')
                            rating = detail.get('rating', 0)
                            print(f"  ✓ {name} (評価: {rating})")

                    except Exception as e:
                        print(f"  ⚠️ 詳細取得エラー: {str(e)}")
                        continue

            time.sleep(0.2)

        except Exception as e:
            print(f"⚠️ 検索エラー ({query}): {str(e)}")
            continue

    return results

def main():
    print("=" * 60)
    print("残り43都府県データ取得テスト版（10件）")
    print("=" * 60)

    start_time = datetime.now()

    # テスト実行
    print("\n[TEST] 宮城県から10件取得中...")
    clinics = search_dental_clinics_test(prefecture='宮城県', limit=10)

    print(f"\n✅ テスト取得完了: {len(clinics)}件")

    # JSON保存（バッチ1-20と同じ形式）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"test_batch_raw_data_{timestamp}.json"

    batch_json = {
        "metadata": {
            "batch_number": "TEST",
            "total_clinics": len(clinics),
            "timestamp": timestamp,
            "prefecture": "宮城県"
        },
        "clinics": clinics
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(batch_json, f, ensure_ascii=False, indent=2)

    end_time = datetime.now()
    elapsed = end_time - start_time

    print(f"\n✅ JSON保存完了: {filename}")
    print(f"所要時間: {elapsed}")
    print(f"\n次のステップ: score_batches.py でスコアリングテスト")

    return clinics

if __name__ == '__main__':
    main()
