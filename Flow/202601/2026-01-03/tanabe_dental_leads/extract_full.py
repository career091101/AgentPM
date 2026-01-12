#!/usr/bin/env python3
"""
田辺玩具向け歯科医院営業リスト抽出（本番：5,100件）

実行フロー:
1. Google Maps APIで5,100件取得（40分）
2. analyze-dental-websites SkillでWebサイト分析（2-3時間）
3. 精緻スコアリング実行
4. CSV出力
"""

import googlemaps
import csv
import os
import json
from datetime import datetime
import time
from dotenv import load_dotenv
import subprocess
import sys

# 環境変数読み込み
load_dotenv()

API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
if not API_KEY:
    raise ValueError("環境変数 GOOGLE_MAPS_API_KEY が設定されていません")

gmaps = googlemaps.Client(key=API_KEY)

# test_extract_10.py の関数をインポート
sys.path.insert(0, os.path.dirname(__file__))
from test_extract_10 import (
    extract_postal_code,
    extract_types_tags,
    calculate_advanced_score
)

def search_dental_clinics_full(prefectures, target_count=5100):
    """
    本州・四国・九州の45都府県から小児歯科・矯正歯科を検索

    Args:
        prefectures: 都道府県リスト
        target_count: 目標件数（5,100件）

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
            print(f"\n検索中: {search_query}")

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

                            results.append(clinic_data)

                            print(f"  取得: {clinic_data['医院名']} ({len(results)}/{target_count})")

            except Exception as e:
                print(f"エラー: {e}")
                continue

        if len(results) >= target_count:
            break

    return results

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
    print("田辺玩具向け歯科医院営業リスト抽出（本番：5,100件）")
    print("=" * 60)

    start_time = datetime.now()

    # 本州・四国・九州の45都府県
    prefectures = [
        # 東北
        '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県',
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

    # STEP 1: Google Maps APIで5,100件取得（40分）
    print("\n[STEP 1] Google Maps APIで医院データ取得中...")
    clinics = search_dental_clinics_full(prefectures, target_count=5100)

    # 中間保存
    intermediate_csv = f'dental_leads_phase_a_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    fieldnames = [
        '医院名',
        '郵便番号',
        '住所',
        '電話番号',
        'WebサイトURL',
        '評価',
        'レビュー件数',
        '診療科目タグ',
        '写真枚数',
        'Google Maps URL',
        'スコア'
    ]

    with open(intermediate_csv, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clinics)

    print(f"\n✓ Phase A完了: {intermediate_csv}")
    print(f"  取得件数: {len(clinics)}件")

    # STEP 2: Webサイト分析（2-3時間）
    print("\n[STEP 2] Webサイト分析実行中...")
    print("  ⚠️ この処理は2-3時間かかります")
    print(f"  Claude Codeで以下のコマンドを実行してください:")
    print(f"  /analyze-dental-websites {intermediate_csv}")
    print()

    # ユーザーに分析実行を促す
    input("Webサイト分析が完了したら、Enterキーを押してください...")

    # STEP 3: Webサイト分析結果を読み込み
    print("\n[STEP 3] Webサイト分析結果の読み込み中...")

    # 最新のanalysis JSONファイルを探す
    analysis_files = [f for f in os.listdir('.') if f.startswith('website_analysis_') and f.endswith('.json')]

    if not analysis_files:
        print("⚠️ Webサイト分析結果ファイルが見つかりません。")
        print("   Phase Aのスコアリング（簡易版）で続行します。")
        website_analysis_data = {}
    else:
        # 最新のファイルを使用
        latest_analysis = sorted(analysis_files)[-1]
        print(f"  読み込み: {latest_analysis}")

        with open(latest_analysis, 'r', encoding='utf-8') as f:
            analysis_json = json.load(f)
            website_analysis_data = analysis_json.get('results', {})

        print(f"✓ 分析結果読み込み: {len(website_analysis_data)}件")

    # STEP 4: 精緻スコアリング実行
    print("\n[STEP 4] 精緻スコアリング実行中...")

    for clinic in clinics:
        analysis = website_analysis_data.get(clinic['医院名'], None)
        score = calculate_advanced_score(clinic, website_analysis=analysis)
        clinic['スコア'] = score

        # SNS連携情報を追加
        if analysis and 'error' not in analysis:
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

            # 子ども対応力スコアを計算
            kids_score = 0
            if analysis.get('kids_content'):
                kids_score += 20
            if analysis.get('waiting_room_photo'):
                kids_score += 15
            if '小児対応' in clinic.get('診療科目タグ', ''):
                kids_score += 15

            clinic['子ども対応力スコア'] = kids_score
        else:
            clinic['SNS連携'] = 'なし'
            clinic['子ども対応力スコア'] = 0

    # スコア順にソート
    clinics_sorted = sorted(clinics, key=lambda x: x['スコア'], reverse=True)

    # STEP 5: 最終CSV出力
    output_file = f'dental_leads_final_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

    final_fieldnames = [
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
        'SNS連携',
        '子ども対応力スコア',
        'Google Maps URL'
    ]

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=final_fieldnames)
        writer.writeheader()
        writer.writerows(clinics_sorted)

    print(f"\n✓ 最終CSV出力完了: {output_file}")

    # 統計情報
    print(f"\n--- 統計情報 ---")
    print(f"総件数: {len(clinics)}件")

    avg_score = sum(c['スコア'] for c in clinics) / len(clinics)
    print(f"平均スコア: {avg_score:.1f}点")

    high_score_count = sum(1 for c in clinics if c['スコア'] >= 150)
    print(f"高スコア（150点以上）: {high_score_count}件")

    with_website = sum(1 for c in clinics if c['WebサイトURL'])
    print(f"Webサイトあり: {with_website}件 ({with_website/len(clinics)*100:.1f}%)")

    if website_analysis_data:
        sns_any = sum(1 for c in clinics if c.get('SNS連携') and c['SNS連携'] != 'なし')
        print(f"SNS連携あり: {sns_any}件 ({sns_any/len(clinics)*100:.1f}%)")

        kids_high = sum(1 for c in clinics if c.get('子ども対応力スコア', 0) >= 30)
        print(f"子ども対応力高（30点以上）: {kids_high}件 ({kids_high/len(clinics)*100:.1f}%)")

    # コスト推定
    estimate_cost(len(clinics))

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds() / 60

    print(f"\n総実行時間: {elapsed:.0f}分")
    print(f"\n✓ 処理完了")

if __name__ == '__main__':
    main()
