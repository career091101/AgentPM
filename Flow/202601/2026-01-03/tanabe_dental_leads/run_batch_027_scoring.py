#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Batch 027 歯科医院スコアリング実行スクリプト
6次元スコアリング（100点満点）を実行し、JSON出力
"""

import csv
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# ==================== スコアリング基準定義 ====================

def calculate_6dimension_score(clinic_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    6次元スコアリング計算（各15点 × 6軸 + 10点ボーナス = 100点満点）

    軸1: 基礎情報の充実度（15点）
    軸2: 来院患者数・規模感（15点）
    軸3: デジタル対応度（15点）
    軸4: 子ども対応力（15点）
    軸5: オンライン評価・口コミ（15点）
    軸6: SNS・ブログ活動（15点）
    ボーナス: 加点要素（10点）
    """

    scores = {}

    # 軸1: 基礎情報の充実度（15点）
    # 医院長名、郵便番号、電話番号、営業時間の有無
    axis1_score = 0
    if clinic_data.get('医院長名'):
        axis1_score += 4
    if clinic_data.get('郵便番号'):
        axis1_score += 3
    if clinic_data.get('電話番号'):
        axis1_score += 4
    if clinic_data.get('営業時間'):
        axis1_score += 4
    scores['axis1_基礎情報充実度'] = min(axis1_score, 15)

    # 軸2: 来院患者数・規模感（15点）
    # 医院規模スコア、来院患者数の多寡
    axis2_score = 0
    try:
        clinic_size = int(clinic_data.get('医院規模', 0))
        axis2_score += min(clinic_size // 7, 8)  # 最大8点
    except (ValueError, TypeError):
        axis2_score += 0

    try:
        patients = int(clinic_data.get('来院患者数', 0))
        if patients > 50:
            axis2_score += 7
        elif patients > 30:
            axis2_score += 5
        elif patients > 10:
            axis2_score += 3
        else:
            axis2_score += 1
    except (ValueError, TypeError):
        axis2_score += 0

    scores['axis2_規模感'] = min(axis2_score, 15)

    # 軸3: デジタル対応度（15点）
    # Webサイト有無、写真枚数、Web評価スコア
    axis3_score = 0
    if clinic_data.get('WebサイトURL'):
        axis3_score += 6

    try:
        photo_count = int(clinic_data.get('写真枚数', 0))
        if photo_count >= 10:
            axis3_score += 5
        elif photo_count >= 5:
            axis3_score += 3
        elif photo_count > 0:
            axis3_score += 1
    except (ValueError, TypeError):
        pass

    try:
        rating = float(clinic_data.get('評価', 0))
        if rating >= 4.5:
            axis3_score += 4
        elif rating >= 4.0:
            axis3_score += 3
        elif rating >= 3.5:
            axis3_score += 2
        elif rating > 0:
            axis3_score += 1
    except (ValueError, TypeError):
        pass

    scores['axis3_デジタル対応度'] = min(axis3_score, 15)

    # 軸4: 子ども対応力（15点）
    # 子ども対応力スコア、子ども向けコンテンツ有無
    axis4_score = 0
    try:
        kids_score = int(clinic_data.get('子ども対応力スコア', 0))
        axis4_score += min(kids_score, 10)
    except (ValueError, TypeError):
        axis4_score += 0

    if clinic_data.get('子ども対応力') and int(clinic_data.get('子ども対応力', 0)) > 0:
        axis4_score += 5

    scores['axis4_子ども対応力'] = min(axis4_score, 15)

    # 軸5: オンライン評価・口コミ（15点）
    # レビュー件数、Google評価
    axis5_score = 0
    try:
        review_count = int(clinic_data.get('レビュー件数', 0))
        if review_count >= 50:
            axis5_score += 8
        elif review_count >= 20:
            axis5_score += 6
        elif review_count >= 10:
            axis5_score += 4
        elif review_count > 0:
            axis5_score += 2
    except (ValueError, TypeError):
        pass

    # Google評価による加点
    try:
        rating = float(clinic_data.get('評価', 0))
        if rating >= 4.7:
            axis5_score += 7
        elif rating >= 4.5:
            axis5_score += 6
        elif rating >= 4.0:
            axis5_score += 5
        elif rating >= 3.5:
            axis5_score += 3
    except (ValueError, TypeError):
        pass

    scores['axis5_評価口コミ'] = min(axis5_score, 15)

    # 軸6: SNS・ブログ活動（15点）
    # SNS連携、ブログ活動、ブログ更新日
    axis6_score = 0

    sns_count = 0
    if clinic_data.get('SNS連携') and int(clinic_data.get('SNS連携', 0)) > 0:
        sns_count = int(clinic_data.get('SNS連携', 0))
    axis6_score += min(sns_count * 3, 8)

    if clinic_data.get('ブログ活動') and int(clinic_data.get('ブログ活動', 0)) > 0:
        axis6_score += 4

    # ブログ更新日の新しさを評価
    if clinic_data.get('ブログ更新日'):
        blog_date = clinic_data.get('ブログ更新日')
        try:
            if blog_date and blog_date != '':
                # 最新の場合高スコア
                axis6_score += 3
        except:
            pass

    scores['axis6_SNS_ブログ'] = min(axis6_score, 15)

    # ボーナスポイント（10点）
    bonus_score = 0
    # 複合的な優良医院の場合
    if sum([scores['axis4_子ども対応力'], scores['axis5_評価口コミ'], scores['axis6_SNS_ブログ']]) >= 30:
        bonus_score += 5

    # ガチャガチャ導入の可能性（子ども対応力 + 規模感）
    if scores['axis4_子ども対応力'] >= 10 and scores['axis2_規模感'] >= 10:
        bonus_score += 5

    scores['bonus_加点要素'] = bonus_score

    # 総合スコア（100点満点）
    total_score = sum([
        scores['axis1_基礎情報充実度'],
        scores['axis2_規模感'],
        scores['axis3_デジタル対応度'],
        scores['axis4_子ども対応力'],
        scores['axis5_評価口コミ'],
        scores['axis6_SNS_ブログ'],
        scores['bonus_加点要素']
    ])

    scores['total_score'] = min(total_score, 100)

    return scores


def load_and_score_csv(csv_path: str) -> tuple:
    """CSVを読み込んでスコアリング実行"""

    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSVファイルが見つかりません: {csv_path}")

    results = []
    error_count = 0

    print(f"\n📊 Batch 027 スコアリング実行開始")
    print(f"   入力ファイル: {csv_file.name}")
    print(f"   ファイルパス: {csv_file}")
    print(f"   実行時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # CSVファイル読み込み
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        row_count = 0
        for row in reader:
            row_count += 1

            try:
                # スコアリング計算
                scores = calculate_6dimension_score(row)

                # 結果に追加
                result = {
                    'row_id': row_count,
                    'clinic_name': row.get('医院名', 'Unknown'),
                    'address': row.get('住所', ''),
                    'phone': row.get('電話番号', ''),
                    'website_url': row.get('WebサイトURL', ''),
                    'scores': scores
                }

                results.append(result)

                # 進捗表示（50件ごと）
                if row_count % 50 == 0:
                    print(f"   処理中: {row_count}件...")

            except Exception as e:
                print(f"   ✗ Row {row_count}: エラー - {str(e)}")
                error_count += 1
                continue

    print(f"\n✓ スコアリング完了")
    print(f"   総件数: {row_count}件")
    print(f"   成功: {len(results)}件")
    print(f"   エラー: {error_count}件")

    return results, row_count, error_count


def generate_json_output(results: List[Dict], csv_path: str, total_count: int, error_count: int) -> str:
    """JSON形式で出力を生成"""

    # 統計計算
    total_scores = [r['scores']['total_score'] for r in results]
    avg_score = sum(total_scores) / len(total_scores) if total_scores else 0
    max_score = max(total_scores) if total_scores else 0
    min_score = min(total_scores) if total_scores else 0

    # スコア分布
    score_distribution = {
        '90-100': len([s for s in total_scores if s >= 90]),
        '80-89': len([s for s in total_scores if 80 <= s < 90]),
        '70-79': len([s for s in total_scores if 70 <= s < 80]),
        '60-69': len([s for s in total_scores if 60 <= s < 70]),
        '50-59': len([s for s in total_scores if 50 <= s < 60]),
        '40-49': len([s for s in total_scores if 40 <= s < 50]),
        '30-39': len([s for s in total_scores if 30 <= s < 40]),
        '0-29': len([s for s in total_scores if s < 30]),
    }

    # 軸別平均スコア
    axis_averages = {}
    for axis_name in ['axis1_基礎情報充実度', 'axis2_規模感', 'axis3_デジタル対応度',
                       'axis4_子ども対応力', 'axis5_評価口コミ', 'axis6_SNS_ブログ']:
        axis_scores = [r['scores'][axis_name] for r in results if axis_name in r['scores']]
        axis_averages[axis_name] = round(sum(axis_scores) / len(axis_scores), 2) if axis_scores else 0

    output = {
        'metadata': {
            'batch_id': 'batch_027',
            'timestamp': datetime.now().isoformat(),
            'source_csv': Path(csv_path).name,
            'scoring_method': '6次元スコアリング（100点満点）',
            'total_records': total_count,
            'successfully_scored': len(results),
            'errors': error_count,
        },
        'statistics': {
            'total_score': {
                'average': round(avg_score, 2),
                'max': max_score,
                'min': min_score,
                'distribution': score_distribution
            },
            'axis_averages': axis_averages
        },
        'results': results
    }

    return json.dumps(output, ensure_ascii=False, indent=2)


def save_json_output(json_data: str, output_filename: str) -> str:
    """JSON出力をファイルに保存"""

    output_path = Path('/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads/scoring_batches') / output_filename

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json_data)

    print(f"\n✓ JSON出力完了")
    print(f"   ファイル: {output_filename}")
    print(f"   パス: {output_path}")

    return str(output_path)


def main():
    """メイン実行関数"""

    csv_path = '/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads/scoring_batches/batch_027_to_score.csv'
    output_filename = 'scoring_results_batch_027.json'

    try:
        # STEP 1: CSV読み込み＆スコアリング
        results, total_count, error_count = load_and_score_csv(csv_path)

        # STEP 2: JSON生成
        json_output = generate_json_output(results, csv_path, total_count, error_count)

        # STEP 3: JSON保存
        output_path = save_json_output(json_output, output_filename)

        # 完了メッセージ
        print(f"\n" + "="*60)
        print(f"✓ Batch 027 スコアリング処理完了！")
        print(f"="*60)
        print(f"出力ファイル: {output_filename}")
        print(f"完全パス: {output_path}")

        return 0

    except Exception as e:
        print(f"\n✗ エラーが発生しました: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
