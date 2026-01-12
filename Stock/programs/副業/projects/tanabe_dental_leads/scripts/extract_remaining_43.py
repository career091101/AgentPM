#!/usr/bin/env python3
"""
田辺玩具向け歯科医院営業リスト抽出（残り43都府県、4,100件）

実行フロー:
1. Google Maps APIで4,100件取得（40分）
2. 50件ずつバッチ分割してJSON保存
3. バッチ21-102の82バッチを作成
"""

import googlemaps
import csv
import os
import json
from datetime import datetime
import time
from dotenv import load_dotenv
import sys

# 環境変数読み込み
load_dotenv()

API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
if not API_KEY:
    raise ValueError("環境変数 GOOGLE_MAPS_API_KEY が設定されていません")

gmaps = googlemaps.Client(key=API_KEY)

def search_dental_clinics_remaining(prefectures, target_count=4100):
    """
    残り43都府県から小児歯科・矯正歯科を検索

    Args:
        prefectures: 都道府県リスト（青森・岩手を除く43都府県）
        target_count: 目標件数（4,100件）

    Returns:
        list: 医院データリスト
    """
    results = []
    seen_place_ids = set()

    queries = [
        '小児歯科',
        '矯正歯科'
    ]

    for prefecture in prefectures:
        for query in queries:
            if len(results) >= target_count:
                break

            search_query = f'{query} {prefecture}'
            print(f"\n検索中: {search_query} (進捗: {len(results)}/{target_count})")

            try:
                places_result = gmaps.places(
                    query=search_query,
                    language='ja',
                    region='jp'
                )

                if places_result['status'] == 'OK':
                    for place in places_result['results']:
                        if len(results) >= target_count:
                            break

                        place_id = place['place_id']

                        if place_id in seen_place_ids:
                            continue

                        seen_place_ids.add(place_id)

                        # 詳細情報取得
                        time.sleep(0.1)  # API制限対策

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

                                if len(results) % 50 == 0:
                                    print(f"✓ {len(results)}件取得完了")

                        except Exception as e:
                            print(f"⚠️ 詳細取得エラー ({place_id}): {str(e)}")
                            continue

                time.sleep(0.2)  # API制限対策

            except Exception as e:
                print(f"⚠️ 検索エラー ({search_query}): {str(e)}")
                continue

        if len(results) >= target_count:
            break

    return results

def save_batches(clinics, start_batch_num=21):
    """
    50件ずつバッチ分割してJSON保存

    Args:
        clinics: 医院データリスト
        start_batch_num: 開始バッチ番号（21）

    Returns:
        list: 保存したファイル名リスト
    """
    batch_size = 50
    total_batches = (len(clinics) + batch_size - 1) // batch_size
    saved_files = []

    print(f"\n{len(clinics)}件を{total_batches}バッチに分割して保存します...")

    for i in range(total_batches):
        batch_num = start_batch_num + i
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, len(clinics))
        batch_data = clinics[start_idx:end_idx]

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"batch_{batch_num:03d}_raw_data_{timestamp}.json"

        batch_json = {
            "metadata": {
                "batch_number": batch_num,
                "total_clinics": len(batch_data),
                "timestamp": timestamp
            },
            "clinics": batch_data
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(batch_json, f, ensure_ascii=False, indent=2)

        saved_files.append(filename)
        print(f"✓ バッチ{batch_num:03d} 保存完了: {filename} ({len(batch_data)}件)")

    return saved_files

def estimate_cost(num_clinics):
    """コスト推定"""
    # Text Search: $32/1,000件
    # Place Details (Basic + Contact): $20/1,000件
    text_search_cost = (num_clinics / 1000) * 32
    place_details_cost = (num_clinics / 1000) * 20
    total_cost_usd = text_search_cost + place_details_cost
    total_cost_jpy = total_cost_usd * 150  # 1ドル=150円

    print(f"\n--- コスト推定 ---")
    print(f"Text Search: ${text_search_cost:.2f}")
    print(f"Place Details: ${place_details_cost:.2f}")
    print(f"合計: ${total_cost_usd:.2f} (約{total_cost_jpy:.0f}円)")

    return total_cost_usd

def main():
    print("=" * 70)
    print("田辺玩具向け歯科医院営業リスト抽出（残り43都府県、4,100件）")
    print("=" * 70)

    start_time = datetime.now()

    # 残り43都府県（青森・岩手を除く）
    prefectures = [
        # 東北（残り4県）
        '宮城県', '秋田県', '山形県', '福島県',
        # 関東
        '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県',
        # 中部
        '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県',
        # 近畿
        '三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県',
        # 中国
        '鳥取県', '島根県', '岡山県', '広島県', '山口県',
        # 四国
        '徳島県', '香川県', '愛媛県', '高知県',
        # 九州
        '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県'
    ]

    print(f"\n対象都府県: {len(prefectures)}都府県")
    print(f"目標件数: 4,100件")

    # コスト推定
    estimate_cost(4100)

    # 実行確認（自動実行モード）
    print("\n⚠️  Google Maps APIを使用します。")
    print("   約40分かかります。")
    print("   自動実行モードで開始します...")

    # STEP 1: Google Maps APIでデータ取得
    print("\n[STEP 1] Google Maps APIで医院データ取得中...")
    clinics = search_dental_clinics_remaining(prefectures, target_count=4100)

    print(f"\n✅ データ取得完了: {len(clinics)}件")

    # STEP 2: バッチ分割して保存
    print("\n[STEP 2] バッチ分割してJSON保存中...")
    saved_files = save_batches(clinics, start_batch_num=21)

    end_time = datetime.now()
    elapsed = end_time - start_time

    print("\n" + "=" * 70)
    print("✅ データ取得完了")
    print("=" * 70)
    print(f"総件数: {len(clinics)}件")
    print(f"バッチ数: {len(saved_files)}バッチ (バッチ021-{21+len(saved_files)-1:03d})")
    print(f"所要時間: {elapsed}")
    print(f"\n次のステップ:")
    print(f"  1. score_batches.py でバッチ21-{21+len(saved_files)-1:03d}をスコアリング")
    print(f"  2. merge_all_batches.py で全バッチを統合")

    return clinics, saved_files

if __name__ == '__main__':
    main()
