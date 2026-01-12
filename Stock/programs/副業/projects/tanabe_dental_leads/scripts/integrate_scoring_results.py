#!/usr/bin/env python3
"""
Phase 3: 36個のスコアリング結果JSONを統合して最終CSV出力

使用方法:
    python integrate_scoring_results.py
"""

import json
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# バッチファイルマッピング（batch_completion_status.txtから生成）
BATCH_FILES = {
    1: "./scoring_results_batch_001_20260104_125755.json",
    2: "./scoring_batches/scoring_results_batch_002_20260104_125843.json",
    3: "./scoring_results_batch_003.json",
    4: "./scoring_results_batch_004.json",
    5: "./scoring_results_batch_005.json",
    6: "./scoring_results_batch_006.json",
    7: "./scoring_results_batch_007.json",
    8: "./scoring_results_batch_008.json",
    9: "./scoring_results_batch_009.json",
    10: "./scoring_results/scoring_results_batch_010.json",
    11: "./scoring_results_batch_011.json",
    12: "./scoring_results_batch_012.json",
    13: "./scoring_results_batch_013.json",
    14: "./scoring_results_batch_014.json",
    15: "./scoring_batches/scoring_results_batch_015.json",
    16: "./scoring_results_batch_016.json",
    17: "./scoring_results_batch_017.json",
    18: "./scoring_results_batch_018.json",
    19: "./scoring_results_batch_019.json",
    20: "./scoring_results_batch_020.json",
    21: "./scoring_results_batch_021.json",
    22: "./scoring_results_batch_022.json",
    23: "./scoring_results_batch_023.json",
    24: "./scoring_results_batch_024.json",
    25: "./scoring_results_batch_025.json",
    26: "./scoring_results/scoring_results_batch_026.json",
    27: "./scoring_batches/scoring_results_batch_027.json",
    28: "./scoring_batches/scoring_results_batch_028.json",
    29: "./scoring_batches/scoring_results_batch_029.json",
    30: "./scoring_batches/scoring_results_batch_030.json",
    31: "./scoring_results_batch_031.json",
    32: "./scoring_batches/scoring_results_batch_032.json",
    33: "./scoring_results_batch_033.json",
    34: "./scoring_results_batch_034.json",
    35: "./scoring_results_batch_035.json",
    36: "./scoring_batches/scoring_results_batch_036_20260104_125856.json",
}


def load_json_file(file_path):
    """JSONファイル読み込み"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️  JSON読み込みエラー: {file_path} - {e}")
        return None


def extract_clinic_data(batch_num, json_data):
    """JSONからクリニックデータを抽出"""
    clinics = []

    # resultsキーが存在する場合
    if 'results' in json_data:
        results = json_data['results']

        # resultsが配列の場合
        if isinstance(results, list):
            for clinic in results:
                clinics.append({
                    'batch_num': batch_num,
                    'data': clinic
                })

        # resultsがオブジェクト（医院名がキー）の場合
        elif isinstance(results, dict):
            for clinic_name, clinic_data in results.items():
                # clinic_dataに医院名を追加
                clinic_record = clinic_data.copy() if isinstance(clinic_data, dict) else {}
                clinic_record['clinic_name'] = clinic_name
                clinics.append({
                    'batch_num': batch_num,
                    'data': clinic_record
                })

    # clinicsキーが存在する場合（別の出力形式）
    elif 'clinics' in json_data and isinstance(json_data['clinics'], list):
        for clinic in json_data['clinics']:
            clinics.append({
                'batch_num': batch_num,
                'data': clinic
            })

    # dataキーが存在する場合
    elif 'data' in json_data and isinstance(json_data['data'], list):
        for clinic in json_data['data']:
            clinics.append({
                'batch_num': batch_num,
                'data': clinic
            })

    # トップレベルが配列の場合
    elif isinstance(json_data, list):
        for clinic in json_data:
            clinics.append({
                'batch_num': batch_num,
                'data': clinic
            })

    else:
        print(f"⚠️  バッチ {batch_num:03d}: 不明なJSON構造")

    return clinics


def normalize_clinic_record(batch_num, clinic_data):
    """クリニックデータを統一フォーマットに変換"""

    # スコア情報抽出
    total_score = clinic_data.get('total_score', 0)

    # scoresキーから各スコアを抽出
    scores = clinic_data.get('scores', {})
    if isinstance(scores, dict):
        score_基礎評価 = scores.get('基礎評価', 0)
        score_来院患者数 = scores.get('来院患者数', 0)
        score_子ども対応力 = scores.get('子ども対応力', 0)
        score_Web積極性 = scores.get('Web積極性', 0)
        score_医院規模 = scores.get('医院規模', 0)
        score_ブログ活動 = scores.get('ブログ活動', 0)
    else:
        score_基礎評価 = 0
        score_来院患者数 = 0
        score_子ども対応力 = 0
        score_Web積極性 = 0
        score_医院規模 = 0
        score_ブログ活動 = 0

    # Website analysis情報（オブジェクト形式の場合は'analysis'キー）
    web_analysis = clinic_data.get('website_analysis', clinic_data.get('analysis', {}))

    # Raw data情報（オブジェクト形式の場合は直接clinic_data）
    raw_data = clinic_data.get('raw_data', clinic_data)

    # 医院長名抽出（複数のキーを試行）
    director_name = web_analysis.get('director_name', '')
    if not director_name and 'director_name_extracted' in web_analysis:
        director_name = web_analysis.get('director_name_extracted', '')
    if not director_name and 'csv_director_name' in clinic_data:
        director_name = clinic_data.get('csv_director_name', '')

    # 医院名抽出（複数のキーを試行）
    clinic_name = clinic_data.get('clinic_name', '')
    if not clinic_name:
        clinic_name = raw_data.get('name', '')

    # 住所抽出（複数のキーを試行）
    address = raw_data.get('formatted_address', clinic_data.get('address', ''))

    # 電話番号抽出
    phone = raw_data.get('formatted_phone_number', clinic_data.get('phone', ''))

    # WebサイトURL抽出
    website_url = raw_data.get('website', clinic_data.get('website_url', ''))

    # Google Maps URL抽出
    google_maps_url = raw_data.get('url', clinic_data.get('google_maps_url', ''))

    # 郵便番号抽出
    postal_code = raw_data.get('postal_code', clinic_data.get('postal_code', ''))

    # 統一レコード作成
    return {
        'バッチ番号': batch_num,
        '総合スコア': total_score,
        '医院名': clinic_name,
        '医院長名': director_name,
        '郵便番号': postal_code,
        '住所': address,
        '基礎評価': score_基礎評価,
        '来院患者数': score_来院患者数,
        '子ども対応力': score_子ども対応力,
        'Web積極性': score_Web積極性,
        '医院規模': score_医院規模,
        'ブログ活動': score_ブログ活動,
        '営業時間': web_analysis.get('operating_hours', ''),
        'ブログ更新日': web_analysis.get('blog_updated', ''),
        '電話番号': phone,
        'WebサイトURL': website_url,
        'Google評価': raw_data.get('rating', ''),
        'レビュー件数': raw_data.get('user_ratings_total', ''),
        '診療科目タグ': ','.join(raw_data.get('types', [])) if isinstance(raw_data.get('types'), list) else '',
        '写真枚数': len(raw_data.get('photos', [])) if isinstance(raw_data.get('photos'), list) else 0,
        'SNS Instagram': web_analysis.get('sns_instagram', False),
        'SNS Facebook': web_analysis.get('sns_facebook', False),
        'SNS LINE': web_analysis.get('sns_line', False),
        'SNS Twitter': web_analysis.get('sns_twitter', False),
        'SNS連携数': sum([
            1 if web_analysis.get('sns_instagram') else 0,
            1 if web_analysis.get('sns_facebook') else 0,
            1 if web_analysis.get('sns_line') else 0,
            1 if web_analysis.get('sns_twitter') else 0
        ]),
        '子ども向けコンテンツ': web_analysis.get('kids_content', False),
        '待合室写真': web_analysis.get('waiting_room_photo', False),
        'Google Maps URL': google_maps_url
    }


def main():
    print("=" * 60)
    print("Phase 3: スコアリング結果統合")
    print("=" * 60)

    all_clinics = []
    batch_stats = defaultdict(int)

    # 36バッチを順番に読み込み
    for batch_num in range(1, 37):
        file_path = BATCH_FILES.get(batch_num)

        if not file_path or not Path(file_path).exists():
            print(f"⚠️  バッチ {batch_num:03d}: ファイルが見つかりません")
            continue

        print(f"\n📦 バッチ {batch_num:03d}: {file_path}")

        # JSON読み込み
        json_data = load_json_file(file_path)
        if not json_data:
            continue

        # クリニックデータ抽出
        clinics = extract_clinic_data(batch_num, json_data)
        print(f"   → {len(clinics)}件のクリニックデータを抽出")

        # 正規化して追加
        for clinic_info in clinics:
            normalized = normalize_clinic_record(batch_num, clinic_info['data'])
            all_clinics.append(normalized)

        batch_stats[batch_num] = len(clinics)

    # 統計表示
    print("\n" + "=" * 60)
    print("統計情報")
    print("=" * 60)
    print(f"処理バッチ数: {len(batch_stats)}/36")
    print(f"総クリニック数: {len(all_clinics)}件")

    # スコア分布
    score_distribution = defaultdict(int)
    for clinic in all_clinics:
        score = clinic['総合スコア']
        if score >= 70:
            score_distribution['高スコア（70点以上）'] += 1
        elif score >= 40:
            score_distribution['中スコア（40-69点）'] += 1
        else:
            score_distribution['低スコア（39点以下）'] += 1

    print("\nスコア分布:")
    for category, count in score_distribution.items():
        percentage = count / len(all_clinics) * 100 if all_clinics else 0
        print(f"  {category}: {count}件 ({percentage:.1f}%)")

    # 医院長名抽出率
    director_names_found = sum(1 for c in all_clinics if c['医院長名'])
    director_extraction_rate = director_names_found / len(all_clinics) * 100 if all_clinics else 0
    print(f"\n医院長名抽出率: {director_names_found}/{len(all_clinics)}件 ({director_extraction_rate:.1f}%)")

    # CSV出力
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_csv = f'tanabe_dental_leads_scored_{timestamp}.csv'

    fieldnames = [
        'バッチ番号', '総合スコア', '医院名', '医院長名', '郵便番号', '住所',
        '基礎評価', '来院患者数', '子ども対応力', 'Web積極性', '医院規模', 'ブログ活動',
        '営業時間', 'ブログ更新日', '電話番号', 'WebサイトURL',
        'Google評価', 'レビュー件数', '診療科目タグ', '写真枚数',
        'SNS Instagram', 'SNS Facebook', 'SNS LINE', 'SNS Twitter', 'SNS連携数',
        '子ども向けコンテンツ', '待合室写真', 'Google Maps URL'
    ]

    with open(output_csv, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_clinics)

    print(f"\n✅ CSV出力完了: {output_csv}")
    print(f"✅ 総件数: {len(all_clinics)}件")
    print("=" * 60)


if __name__ == '__main__':
    main()
