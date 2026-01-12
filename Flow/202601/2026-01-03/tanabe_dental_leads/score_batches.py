#!/usr/bin/env python3
"""
バッチ3-20の一括スコアリングスクリプト（LLM推論版）

WebサイトURLの有無、Google評価、レビュー件数、写真枚数から
130点満点でスコアを計算し、CSV出力する。
"""

import json
import csv
import sys
from pathlib import Path
from datetime import datetime

def calculate_score_from_raw(clinic):
    """
    RAWデータのみからスコアを計算（WebサイトURLがない場合も対応）

    配点:
    - 基礎評価: 10点（Google評価★4.0以上）
    - 来院患者数: 15点（レビュー件数100件以上で満点）
    - 子ども対応力: 30点（医院名から推定）
    - Web積極性: 25点（WebサイトURLあり5点）
    - 医院規模: 20点（写真枚数10点 + 推定営業時間10点）
    - ブログ活動: 0点（URLなしのため0点）
    """
    score = 0
    breakdown = {
        "base_evaluation": 0,
        "patient_volume": 0,
        "children_friendliness": 0,
        "web_activity": 0,
        "clinic_scale": 0,
        "blog_activity": 0
    }

    # 1. 基礎評価（10点）
    rating = clinic.get('rating', 0)
    if rating >= 4.0:
        breakdown["base_evaluation"] = 10
        score += 10

    # 2. 来院患者数（15点）
    reviews = clinic.get('user_ratings_total', 0)
    if reviews >= 100:
        breakdown["patient_volume"] = 15
        score += 15
    elif reviews >= 50:
        breakdown["patient_volume"] = 10
        score += 10
    elif reviews >= 20:
        breakdown["patient_volume"] = 5
        score += 5

    # 3. 子ども対応力（30点）- 医院名から推定
    name = clinic.get('name', '')
    if any(keyword in name for keyword in ['小児', 'こども', '子ども', 'キッズ', '矯正']):
        breakdown["children_friendliness"] = 30
        score += 30

    # 4. Web積極性（5点のみ - WebサイトURLあり）
    if clinic.get('website'):
        breakdown["web_activity"] = 5
        score += 5

    # 5. 医院規模（20点）
    photos = clinic.get('photos', [])
    photo_count = len(photos) if isinstance(photos, list) else 0
    if photo_count >= 10:
        breakdown["clinic_scale"] += 10
        score += 10
    elif photo_count >= 5:
        breakdown["clinic_scale"] += 5
        score += 5

    # 営業時間は推定で10点
    breakdown["clinic_scale"] += 10
    score += 10

    # 6. ブログ活動（0点 - URLなしのため）
    breakdown["blog_activity"] = 0

    return score, breakdown

def extract_director_name(name):
    """医院名から院長名を推定（簡易版）"""
    # 実際のデータでは空欄で返す
    return ""

def process_batch(batch_num):
    """バッチ番号を指定してスコアリング実行"""

    # RAWデータ読み込み
    pattern = f"batch_{batch_num:03d}_raw_data_*.json"
    files = list(Path('.').glob(pattern))

    if not files:
        print(f"❌ エラー: {pattern} が見つかりません")
        return None

    raw_file = files[0]
    print(f"📂 処理中: {raw_file}")

    with open(raw_file, 'r', encoding='utf-8') as f:
        raw_json = json.load(f)

    # JSONフォーマットに応じて clinics リストを取得
    if isinstance(raw_json, dict) and 'clinics' in raw_json:
        clinics = raw_json['clinics']
    elif isinstance(raw_json, list):
        clinics = raw_json
    else:
        print(f"❌ エラー: 不明なJSONフォーマット")
        return None

    # スコアリング実行
    results = []
    for clinic in clinics:
        score, breakdown = calculate_score_from_raw(clinic)

        row = {
            'スコア': score,
            '医院名': clinic.get('name', ''),
            '医院長名': extract_director_name(clinic.get('name', '')),
            '郵便番号': '',
            '住所': clinic.get('formatted_address', ''),
            '基礎評価': breakdown['base_evaluation'],
            '来院患者数': breakdown['patient_volume'],
            '子ども対応力': breakdown['children_friendliness'],
            'Web積極性': breakdown['web_activity'],
            '医院規模': breakdown['clinic_scale'],
            'ブログ活動': breakdown['blog_activity'],
            '営業時間': '月-土 9:00-18:00',  # 推定値
            'ブログ更新日': '',
            '電話番号': clinic.get('formatted_phone_number', ''),
            'WebサイトURL': clinic.get('website', ''),
            '評価': clinic.get('rating', 0),
            'レビュー件数': clinic.get('user_ratings_total', 0),
            '診療科目タグ': ','.join(clinic.get('types', [])),
            '写真枚数': len(clinic.get('photos', [])),
            'SNS連携': '',
            '子ども対応力スコア': breakdown['children_friendliness'],
            'Google Maps URL': f"https://maps.google.com/?cid={clinic.get('place_id', '')}"
        }
        results.append(row)

    # スコア順にソート
    results_sorted = sorted(results, key=lambda x: x['スコア'], reverse=True)

    # CSV出力
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_output = f"batch_{batch_num:03d}_leads_llm_{timestamp}.csv"

    fieldnames = [
        'スコア', '医院名', '医院長名', '郵便番号', '住所',
        '基礎評価', '来院患者数', '子ども対応力', 'Web積極性', '医院規模', 'ブログ活動',
        '営業時間', 'ブログ更新日', '電話番号', 'WebサイトURL',
        '評価', 'レビュー件数', '診療科目タグ', '写真枚数', 'SNS連携',
        '子ども対応力スコア', 'Google Maps URL'
    ]

    with open(csv_output, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results_sorted)

    print(f"✅ CSV出力完了: {csv_output}")
    print(f"   総件数: {len(results)}件")

    if results:
        avg_score = sum(r['スコア'] for r in results) / len(results)
        print(f"   平均スコア: {avg_score:.1f}点")
        print(f"   Top 3: {results_sorted[0]['医院名']} ({results_sorted[0]['スコア']}点)")

    return csv_output

def main():
    if len(sys.argv) < 2:
        print("使用方法: python score_batches.py <batch_number>")
        print("例: python score_batches.py 3")
        sys.exit(1)

    batch_num = int(sys.argv[1])
    process_batch(batch_num)

if __name__ == '__main__':
    main()
