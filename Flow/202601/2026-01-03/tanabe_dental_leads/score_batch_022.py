#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6次元スコアリング実行スクリプト - Batch 022
Batch 022（500件）に対して100点満点の6次元スコアリング実行
"""

import csv
import json
from datetime import datetime
from pathlib import Path

def calculate_six_dimension_score(row):
    """
    6次元スコアリング（100点満点）

    Dimension 1: 基礎医院スペック (25点)
      - 医院規模 (建物登録)
      - Google Maps スコア
      - 診療実績

    Dimension 2: デジタルプレゼンス (20点)
      - Webサイト積極性
      - SNS連携度
      - ブログ活動

    Dimension 3: 患者対応力 (20点)
      - 子ども対応力
      - 営業時間の充実度
      - 来院患者数

    Dimension 4: SEO/検索可視性 (15点)
      - Google Maps登録
      - 医院規模
      - レビュー件数

    Dimension 5: コンテンツ充実度 (10点)
      - ブログ更新
      - 写真枚数
      - 診療情報

    Dimension 6: ガチャガチャ導入適合性 (10点)
      - 患者層 (子ども対応)
      - 施設規模
      - 来院頻度
    """

    scores = {}

    # ==========================================
    # Dimension 1: 基礎医院スペック (25点)
    # ==========================================
    dim1_score = 0

    # 医院規模スコア (10点)
    medical_scale = row.get('医院規模', 0)
    try:
        medical_scale = int(medical_scale) if medical_scale else 0
    except:
        medical_scale = 0

    if medical_scale >= 20:
        dim1_score += 10
    elif medical_scale >= 15:
        dim1_score += 8
    elif medical_scale >= 10:
        dim1_score += 6
    elif medical_scale > 0:
        dim1_score += 3

    # Google Maps評価 (10点)
    google_rating = row.get('評価', 0)
    try:
        google_rating = float(google_rating) if google_rating else 0
    except:
        google_rating = 0

    if google_rating >= 4.5:
        dim1_score += 10
    elif google_rating >= 4.0:
        dim1_score += 8
    elif google_rating >= 3.5:
        dim1_score += 5
    elif google_rating > 0:
        dim1_score += 2

    # 診療実績 (5点)
    review_count = row.get('レビュー件数', 0)
    try:
        review_count = int(review_count) if review_count else 0
    except:
        review_count = 0

    if review_count >= 30:
        dim1_score += 5
    elif review_count >= 20:
        dim1_score += 4
    elif review_count >= 10:
        dim1_score += 3
    elif review_count > 0:
        dim1_score += 1

    scores['dimension_1_basic_spec'] = dim1_score

    # ==========================================
    # Dimension 2: デジタルプレゼンス (20点)
    # ==========================================
    dim2_score = 0

    # Webサイト積極性 (8点)
    web_activity = row.get('Web積極性', 0)
    try:
        web_activity = int(web_activity) if web_activity else 0
    except:
        web_activity = 0

    if web_activity >= 5:
        dim2_score += 8
    elif web_activity >= 3:
        dim2_score += 5
    elif web_activity > 0:
        dim2_score += 2

    # SNS連携度 (8点)
    sns_linkage = row.get('SNS連携', 0)
    if sns_linkage or (isinstance(sns_linkage, str) and sns_linkage.strip()):
        try:
            sns_linkage = int(sns_linkage) if sns_linkage else 0
        except:
            sns_linkage = 0
    else:
        sns_linkage = 0

    if sns_linkage >= 3:
        dim2_score += 8
    elif sns_linkage >= 2:
        dim2_score += 5
    elif sns_linkage >= 1:
        dim2_score += 2

    # ブログ活動 (4点)
    blog_activity = row.get('ブログ活動', 0)
    try:
        blog_activity = int(blog_activity) if blog_activity else 0
    except:
        blog_activity = 0

    if blog_activity > 0:
        dim2_score += 4

    scores['dimension_2_digital_presence'] = dim2_score

    # ==========================================
    # Dimension 3: 患者対応力 (20点)
    # ==========================================
    dim3_score = 0

    # 子ども対応力 (8点)
    kids_ability = row.get('子ども対応力', 0)
    try:
        kids_ability = int(kids_ability) if kids_ability else 0
    except:
        kids_ability = 0

    if kids_ability > 0:
        dim3_score += 8
    elif row.get('子ども対応力スコア', 0):
        dim3_score += 5

    # 営業時間充実度 (7点)
    operating_hours = row.get('営業時間', '')
    operating_hours_str = str(operating_hours) if operating_hours else ''

    if operating_hours_str and '月-土' in operating_hours_str and '18:00' in operating_hours_str:
        dim3_score += 7
    elif operating_hours_str and ('月-土' in operating_hours_str or '9:00' in operating_hours_str):
        dim3_score += 4
    elif operating_hours_str:
        dim3_score += 2

    # 来院患者数 (5点)
    patient_count = row.get('来院患者数', 0)
    try:
        patient_count = int(patient_count) if patient_count else 0
    except:
        patient_count = 0

    if patient_count >= 20:
        dim3_score += 5
    elif patient_count >= 10:
        dim3_score += 3
    elif patient_count > 0:
        dim3_score += 1

    scores['dimension_3_patient_ability'] = dim3_score

    # ==========================================
    # Dimension 4: SEO/検索可視性 (15点)
    # ==========================================
    dim4_score = 0

    # Google Maps登録 (5点)
    maps_url = row.get('Google Maps URL', '')
    maps_registered = bool(maps_url and maps_url.strip() and maps_url != 'https://maps.google.com/?cid=')
    dim4_score += 5 if maps_registered else 0

    # 医院規模と検索可視性の相関 (5点)
    if medical_scale >= 15:
        dim4_score += 5
    elif medical_scale >= 10:
        dim4_score += 3
    elif medical_scale > 0:
        dim4_score += 1

    # レビュー可視性 (5点)
    if review_count >= 30:
        dim4_score += 5
    elif review_count >= 15:
        dim4_score += 3
    elif review_count > 0:
        dim4_score += 1

    scores['dimension_4_seo_visibility'] = min(dim4_score, 15)

    # ==========================================
    # Dimension 5: コンテンツ充実度 (10点)
    # ==========================================
    dim5_score = 0

    # ブログ更新 (5点)
    blog_update_date = row.get('ブログ更新日', '')
    if blog_update_date and str(blog_update_date).strip():
        dim5_score += 5

    # 写真枚数 (3点)
    photo_count = row.get('写真枚数', 0)
    try:
        photo_count = int(photo_count) if photo_count else 0
    except:
        photo_count = 0

    if photo_count >= 10:
        dim5_score += 3
    elif photo_count >= 5:
        dim5_score += 2
    elif photo_count > 0:
        dim5_score += 1

    # 診療情報 (2点)
    diagnosis_tags = row.get('診療科目タグ', '')
    if diagnosis_tags and str(diagnosis_tags).strip():
        dim5_score += 2

    scores['dimension_5_content_richness'] = min(dim5_score, 10)

    # ==========================================
    # Dimension 6: ガチャガチャ導入適合性 (10点)
    # ==========================================
    dim6_score = 0

    # 患者層 (子ども対応) (4点)
    if kids_ability > 0:
        dim6_score += 4
    elif row.get('子ども対応力スコア', 0):
        dim6_score += 2

    # 施設規模 (3点)
    if medical_scale >= 15:
        dim6_score += 3
    elif medical_scale >= 10:
        dim6_score += 2
    elif medical_scale > 0:
        dim6_score += 1

    # 来院頻度 (3点)
    if patient_count >= 15:
        dim6_score += 3
    elif patient_count >= 10:
        dim6_score += 2
    elif patient_count > 0:
        dim6_score += 1

    scores['dimension_6_gacha_fit'] = min(dim6_score, 10)

    # 総合スコア計算 (100点満点)
    total_score = sum(scores.values())
    scores['total_score'] = total_score

    return scores


def main():
    """メイン処理"""

    print("=" * 70)
    print("6次元スコアリング実行 - Batch 022")
    print("=" * 70)

    csv_path = Path(__file__).parent / 'scoring_batches' / 'batch_022_to_score.csv'

    if not csv_path.exists():
        print(f"ERROR: CSVファイルが見つかりません: {csv_path}")
        return

    # CSVファイル読み込み
    print(f"\n📂 CSVファイル読み込み中: {csv_path}")

    clinics = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        clinics = list(reader)

    print(f"✓ 読み込み完了: {len(clinics)}件\n")

    # スコアリング実行
    print("🔍 6次元スコアリング実行中...\n")

    results = {}
    scores_list = []

    for i, clinic in enumerate(clinics, 1):
        clinic_name = clinic.get('医院名', 'Unknown')

        # スコア計算
        scores = calculate_six_dimension_score(clinic)

        # 結果保存
        result = {
            'clinic_name': clinic_name,
            'postal_code': clinic.get('郵便番号', ''),
            'address': clinic.get('住所', ''),
            'director_name': clinic.get('医院長名', ''),
            'phone': clinic.get('電話番号', ''),
            'website_url': clinic.get('WebサイトURL', ''),
            'scores': scores
        }

        results[clinic_name] = result
        scores_list.append({
            'clinic_name': clinic_name,
            'total_score': scores['total_score'],
            'dimension_1': scores['dimension_1_basic_spec'],
            'dimension_2': scores['dimension_2_digital_presence'],
            'dimension_3': scores['dimension_3_patient_ability'],
            'dimension_4': scores['dimension_4_seo_visibility'],
            'dimension_5': scores['dimension_5_content_richness'],
            'dimension_6': scores['dimension_6_gacha_fit']
        })

        if i % 50 == 0:
            print(f"  処理中: {i}/{len(clinics)}件...")

    print(f"✓ スコアリング完了\n")

    # スコア統計
    total_scores = [s['total_score'] for s in scores_list]
    avg_score = sum(total_scores) / len(total_scores)
    max_score = max(total_scores)
    min_score = min(total_scores)

    print("📊 スコア統計:")
    print(f"  総件数: {len(results)}件")
    print(f"  平均スコア: {avg_score:.1f}点")
    print(f"  最高スコア: {max_score}点")
    print(f"  最低スコア: {min_score}点")

    # スコア分布
    distribution = {
        '90-100': len([s for s in total_scores if 90 <= s <= 100]),
        '80-89': len([s for s in total_scores if 80 <= s < 90]),
        '70-79': len([s for s in total_scores if 70 <= s < 80]),
        '60-69': len([s for s in total_scores if 60 <= s < 70]),
        '50-59': len([s for s in total_scores if 50 <= s < 60]),
        '40-49': len([s for s in total_scores if 40 <= s < 50]),
        '0-39': len([s for s in total_scores if s < 40]),
    }

    print("\n📈 スコア分布:")
    for range_key, count in distribution.items():
        rate = count / len(results) * 100
        print(f"  {range_key}点: {count:3d}件 ({rate:5.1f}%)")

    # JSON出力
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'scoring_results_batch_022.json'

    output_data = {
        'metadata': {
            'batch_number': 22,
            'total_clinics': len(results),
            'timestamp': datetime.now().isoformat(),
            'source_csv': str(csv_path),
            'scoring_method': '6次元スコアリング (100点満点)',
            'dimensions': {
                'dimension_1': '基礎医院スペック (25点)',
                'dimension_2': 'デジタルプレゼンス (20点)',
                'dimension_3': '患者対応力 (20点)',
                'dimension_4': 'SEO/検索可視性 (15点)',
                'dimension_5': 'コンテンツ充実度 (10点)',
                'dimension_6': 'ガチャガチャ導入適合性 (10点)'
            }
        },
        'statistics': {
            'average_score': round(avg_score, 1),
            'max_score': max_score,
            'min_score': min_score,
            'distribution': distribution
        },
        'results': results,
        'scores_summary': scores_list
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ JSON出力完了: {output_file}")
    print(f"\n✅ 処理完了\n")

    # トップ10スコア表示
    print("🏆 スコアトップ10:")
    top_10 = sorted(scores_list, key=lambda x: x['total_score'], reverse=True)[:10]
    for idx, clinic_score in enumerate(top_10, 1):
        print(f"  {idx:2d}. {clinic_score['clinic_name']:30s} - {clinic_score['total_score']:3d}点")


if __name__ == '__main__':
    main()
