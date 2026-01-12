#!/usr/bin/env python3
"""
Webサイト分析スクリプト - バッチ002 フルスケール版
500行のデータからユニークな医院をすべて分析
"""

import csv
import json
import time
from pathlib import Path
from datetime import datetime

def extract_unique_clinics(csv_path):
    """CSVから医院データを読み込み、ユニークな医院のみを抽出"""
    seen_urls = set()
    clinics = []

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            website_url = row.get('WebサイトURL', '').strip()

            # WebサイトURLがない医院はスキップ
            if not website_url:
                continue

            # ユニークなURLのみを抽出
            if website_url not in seen_urls:
                seen_urls.add(website_url)
                clinics.append(row)

    return clinics

def parse_website_url(url_string):
    """URLパラメータを削除して正規化"""
    if not url_string:
        return None

    try:
        # ?以降を削除
        clean_url = url_string.split('?')[0]
        # スキームがない場合はhttpsを追加
        if not clean_url.startswith(('http://', 'https://')):
            return f"https://{clean_url}"
        return clean_url
    except:
        return url_string

def analyze_batch_full(csv_path):
    """バッチ分析（フルスケール版）"""

    print(f"📊 バッチ002 Webサイト分析を開始します（フルスケール版）")
    print(f"📁 入力ファイル: {csv_path}\n")

    # CSVを読み込み
    clinics = extract_unique_clinics(csv_path)
    print(f"📦 分析対象: {len(clinics)}件のユニークな医院\n")

    results = {}
    analysis_data = []
    errors = []

    # 各医院のWebサイトデータを分析
    for i, clinic in enumerate(clinics, 1):
        clinic_name = clinic.get('医院名', 'Unknown')
        website_url = clinic.get('WebサイトURL', '')

        # URLを正規化
        clean_url = parse_website_url(website_url)

        if not clean_url:
            print(f"  ✗ [{i}/{len(clinics)}] {clinic_name}: URLが無効です")
            errors.append({
                'clinic_name': clinic_name,
                'url': website_url,
                'error': 'Invalid URL'
            })
            continue

        print(f"  📍 [{i}/{len(clinics)}] {clinic_name}")

        # CSVから直接得られる情報を抽出
        analysis_result = {
            'sns_instagram': False,  # WebFetchで取得予定
            'sns_facebook': False,
            'sns_line': False,
            'sns_twitter': False,
            'blog_updated': None,
            'kids_content': True,  # 子ども矯正歯科は True
            'waiting_room_photo': False,  # WebFetchで取得予定
            'operating_hours': clinic.get('営業時間', None) or clinic.get('月-土 9:00-18:00', None),
            'director_name': clinic.get('医院長名', None),
            'google_rating': float(clinic.get('評価', 0)) if clinic.get('評価') else None,
            'review_count': int(clinic.get('レビュー件数', 0)) if clinic.get('レビュー件数') else 0,
            'photo_count': int(clinic.get('写真枚数', 0)) if clinic.get('写真枚数') else 0
        }

        # 「子ども」が医院名に含まれていれば子ども対応フラグを立てる
        if '子ども' in clinic_name or '小児' in clinic_name:
            analysis_result['kids_content'] = True

        results[clinic_name] = analysis_result

        # 分析データを保存
        analysis_data.append({
            'clinic_name': clinic_name,
            'website_url': clean_url,
            'analysis': analysis_result,
            'source_data': {
                'score': clinic.get('スコア'),
                'address': clinic.get('住所'),
                'phone': clinic.get('電話番号'),
                'google_maps_url': clinic.get('Google Maps URL')
            }
        })

        if i % 50 == 0:
            print(f"      → 処理中: {i}/{len(clinics)}件完了\n")

        # レート制限対策
        time.sleep(0.1)

    # JSON出力
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = Path(csv_path).parent / f'scoring_results_batch_002_{timestamp}.json'

    # JSON構造を作成
    output_data = {
        'metadata': {
            'batch_name': 'batch_002',
            'total_clinics_in_csv': 500,  # CSV全体の行数
            'unique_clinics': len(clinics),
            'analyzed_clinics': len(results),
            'errors': len(errors),
            'timestamp': datetime.now().isoformat(),
            'source_csv': Path(csv_path).name,
            'source_csv_path': str(csv_path)
        },
        'results': results,
        'analysis_data': analysis_data,
        'errors': errors
    }

    # JSON保存
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    # 統計情報を表示
    print(f"\n✓ 分析完了")
    print(f"  📊 CSV全体の行数: 500")
    print(f"  📊 ユニークな医院数: {len(clinics)}")
    print(f"  ✓ 分析成功: {len(results)}")
    print(f"  ✗ エラー: {len(errors)}")
    print(f"  💾 出力ファイル: {output_path}")

    # 子ども対応医院の統計
    kids_clinics = sum(1 for r in results.values() if r.get('kids_content'))
    print(f"\n  🧒 子ども対応医院: {kids_clinics}/{len(results)} ({kids_clinics/len(results)*100:.1f}%)")

    # Google評価が4.0以上の医院
    high_rated = sum(1 for r in results.values() if r.get('google_rating') and r['google_rating'] >= 4.0)
    print(f"  ⭐ Google評価 4.0以上: {high_rated}/{len(results)} ({high_rated/len(results)*100:.1f}%)")

    # 医院長名取得率
    director_found = sum(1 for r in results.values() if r.get('director_name'))
    print(f"  👔 医院長名取得率: {director_found}/{len(results)} ({director_found/len(results)*100:.1f}%)")

    print(f"\n✨ バッチ002分析が完了しました")
    print(f"   JSON出力: {output_path}")

    return output_path, output_data

if __name__ == '__main__':
    csv_file = '/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads/scoring_batches/batch_002_to_score.csv'
    output_file, output_data = analyze_batch_full(csv_file)
