#!/usr/bin/env python3
"""
田辺玩具向け歯科医院営業リスト - バッチ処理スクリプト（50件/バッチ版）

使用方法:
    python extract_batch_50.py --batch 1

バッチ番号:
    1-360 (50件ずつ、総計15,880件)
    - バッチ1-8: 青森県（353件）
    - バッチ9-16: 岩手県（353件）
    - ... (全45都府県)
    - バッチ353-360: 鹿児島県（352件）
"""

import os
import sys
import json
import csv
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import googlemaps
import argparse

# 環境変数読み込み
load_dotenv()
API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

if not API_KEY:
    print("❌ Error: GOOGLE_MAPS_API_KEY not found in .env")
    sys.exit(1)

# Google Maps Clientの初期化
gmaps = googlemaps.Client(key=API_KEY)

# 都道府県リスト（本州・四国・九州45都府県）
PREFECTURES = [
    # 東北（6県）
    '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県',
    # 関東（7都県）
    '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県',
    # 中部（9県）
    '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県',
    # 近畿（7府県）
    '三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県',
    # 中国（5県）
    '鳥取県', '島根県', '岡山県', '広島県', '山口県',
    # 四国（4県）
    '徳島県', '香川県', '愛媛県', '高知県',
    # 九州（7県）
    '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県'
]

# 検索キーワード
SEARCH_KEYWORDS = ['小児歯科', '矯正歯科']

# 重複排除用グローバルセット
seen_place_ids = set()


def load_existing_place_ids(batch_num):
    """既存バッチから既にクロールしたplace_idを読み込み、重複を防ぐ"""
    global seen_place_ids

    for i in range(1, batch_num):
        csv_file = f"dental_leads_production_batch_{i:03d}.csv"
        if Path(csv_file).exists():
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Google Maps URLからplace_idを抽出（簡易実装）
                    # 実際のURLパース処理が必要な場合は追加実装
                    seen_place_ids.add(row.get('Google Maps URL', ''))


def clean_address(address, postal_code):
    """住所から「日本、」と「〒郵便番号 」を削除"""
    cleaned = address.replace('日本、', '')
    if postal_code:
        cleaned = cleaned.replace(f'〒{postal_code} ', '')
        cleaned = cleaned.replace(f'〒{postal_code}', '')
    return cleaned.strip()


def extract_postal_code(address_components):
    """address_componentsから郵便番号を抽出"""
    for component in address_components:
        if 'postal_code' in component['types']:
            return component['long_name']
    return None


def search_dental_clinics(prefecture, keyword, max_results=25):
    """
    指定都道府県で歯科医院を検索

    Args:
        prefecture: 都道府県名
        keyword: 検索キーワード（小児歯科 or 矯正歯科）
        max_results: 最大取得件数

    Returns:
        list: Place Details情報のリスト
    """
    query = f"{keyword} {prefecture}"
    results = []

    try:
        # Text Search APIで検索
        places_result = gmaps.places(
            query=query,
            language='ja',
            region='jp'
        )

        # 最初の20件を取得
        initial_results = places_result.get('results', [])[:20]

        for place in initial_results:
            place_id = place['place_id']

            # 重複チェック
            if place_id in seen_place_ids:
                continue

            # Place Details APIで詳細情報取得
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

                details = place_details.get('result', {})

                # 必須フィールドチェック
                if not details.get('name'):
                    continue

                seen_place_ids.add(place_id)
                results.append(details)

                # 最大件数チェック
                if len(results) >= max_results:
                    break

                # API制限対策
                time.sleep(0.1)

            except Exception as e:
                print(f"⚠️  Place Details API error for {place_id}: {e}")
                continue

        # 次のページがあれば取得（最大60件まで）
        next_page_token = places_result.get('next_page_token')
        if next_page_token and len(results) < max_results:
            time.sleep(2)  # next_page_tokenは2秒後に有効化
            try:
                next_result = gmaps.places(
                    page_token=next_page_token,
                    language='ja'
                )

                for place in next_result.get('results', []):
                    place_id = place['place_id']

                    if place_id in seen_place_ids:
                        continue

                    place_details = gmaps.place(
                        place_id=place_id,
                        language='ja',
                        fields=[
                            'name', 'formatted_address', 'address_component',
                            'formatted_phone_number', 'website', 'rating',
                            'user_ratings_total', 'url', 'type', 'photo'
                        ]
                    )

                    details = place_details.get('result', {})

                    if not details.get('name'):
                        continue

                    seen_place_ids.add(place_id)
                    results.append(details)

                    if len(results) >= max_results:
                        break

                    time.sleep(0.1)

            except Exception as e:
                print(f"⚠️  Next page fetch error: {e}")

    except Exception as e:
        print(f"❌ Search error for {query}: {e}")

    return results


def extract_batch(batch_num, target_count=50):
    """
    指定バッチ番号の50件を取得

    Args:
        batch_num: バッチ番号（1-360）
        target_count: 目標取得件数（デフォルト50）

    Returns:
        list: 取得した歯科医院データ
    """
    print(f"\n{'='*60}")
    print(f"バッチ {batch_num}/360 開始（目標: {target_count}件）")
    print(f"{'='*60}\n")

    # 既存place_idを読み込み（重複排除）
    load_existing_place_ids(batch_num)
    print(f"✅ 既存データ読み込み完了: {len(seen_place_ids)}件のplace_idをスキップ\n")

    results = []
    pref_idx = 0
    keyword_idx = 0

    while len(results) < target_count and pref_idx < len(PREFECTURES):
        prefecture = PREFECTURES[pref_idx]
        keyword = SEARCH_KEYWORDS[keyword_idx]

        print(f"🔍 検索中: {keyword} {prefecture} (現在: {len(results)}/{target_count}件)")

        # 検索実行（最大25件）
        batch_results = search_dental_clinics(prefecture, keyword, max_results=25)
        results.extend(batch_results)

        print(f"   → {len(batch_results)}件取得（累計: {len(results)}件）\n")

        # 次のキーワードへ
        keyword_idx += 1
        if keyword_idx >= len(SEARCH_KEYWORDS):
            keyword_idx = 0
            pref_idx += 1

        # API制限対策
        time.sleep(1)

    print(f"\n✅ バッチ {batch_num} データ取得完了: {len(results)}件\n")

    return results[:target_count]


def main():
    parser = argparse.ArgumentParser(description='田辺玩具向け歯科医院営業リスト - バッチ処理')
    parser.add_argument('--batch', type=int, required=True, help='バッチ番号（1-360）')
    args = parser.parse_args()

    batch_num = args.batch

    if batch_num < 1 or batch_num > 360:
        print("❌ Error: バッチ番号は1-360の範囲で指定してください")
        sys.exit(1)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # バッチ実行
    clinics = extract_batch(batch_num, target_count=50)

    if not clinics:
        print("❌ Error: データ取得に失敗しました")
        sys.exit(1)

    # JSON保存（後でサブエージェントに渡す）
    json_file = f"batch_{batch_num:03d}_raw_data_{timestamp}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'batch_number': batch_num,
                'total_clinics': len(clinics),
                'timestamp': timestamp
            },
            'clinics': clinics
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✅ RAWデータ保存完了: {json_file}")
    print(f"\n次のステップ:")
    print(f"1. サブエージェント（/analyze-dental-websites）でWebサイト分析を実行")
    print(f"2. 分析結果とこのJSONを統合してCSV出力\n")


if __name__ == '__main__':
    main()
