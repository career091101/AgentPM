#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

def load_csv(file_path: str) -> List[Dict[str, str]]:
    """CSVファイルを読み込み"""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)

def calculate_scores(clinics: List[Dict[str, str]]) -> Dict[str, Any]:
    """6次元スコアリングを計算
    
    スコア構成（100点満点）:
    1. 基礎評価 (20点): rating × 4
    2. 来院患者数 (20点): レビュー件数ベース
    3. 子ども対応力 (30点): kids_content + 医院名キーワード + waiting_room_photo
    4. Web積極性 (15点): SNS数 × 5
    5. 医院規模 (10点): 営業時間 + 写真数
    6. ブログ活動 (5点): ブログ更新日ベース
    """
    results = []
    
    for clinic in clinics:
        clinic_name = clinic.get('医院名', 'Unknown')
        
        try:
            # 各スコアを初期化
            scores = {
                'clinic_name': clinic_name,
                'scores': {},
                'total_score': 0
            }
            
            # 1. 基礎評価 (20点): rating × 4
            try:
                rating = float(clinic.get('評価', '0'))
                base_score = min(20, rating * 4)
            except (ValueError, TypeError):
                base_score = 0
            scores['scores']['基礎評価'] = base_score
            
            # 2. 来院患者数 (20点): レビュー件数ベース
            try:
                reviews = int(clinic.get('レビュー件数', '0'))
                if reviews == 0:
                    review_score = 0
                elif reviews < 10:
                    review_score = 5
                elif reviews < 50:
                    review_score = 10
                elif reviews < 100:
                    review_score = 15
                else:
                    review_score = 20
            except (ValueError, TypeError):
                review_score = 0
            scores['scores']['来院患者数'] = review_score
            
            # 3. 子ども対応力 (30点): 
            #    - kids_content: 15点
            #    - 医院名に子ども関連キーワード: 10点
            #    - waiting_room_photo: 5点
            kids_content = clinic.get('子ども対応力スコア', '0')
            kids_score = 0
            
            # kids_content列をチェック
            if kids_content and kids_content.strip() and int(kids_content) > 0:
                kids_score += 15
            
            # 医院名に「こども」「小児」「キッズ」を含むかチェック
            clinic_name_lower = clinic_name.lower()
            if any(keyword in clinic_name for keyword in ['こども', '小児', 'キッズ', '子ども']):
                kids_score += 10
            
            # waiting_room_photo（今はデータなし、構造上は対応）
            # kids_score += 5
            
            kids_score = min(30, kids_score)
            scores['scores']['子ども対応力'] = kids_score
            
            # 4. Web積極性 (15点): SNS連携数 × 5
            sns_count = 0
            sns_str = clinic.get('SNS連携', '')
            if sns_str:
                # SNS連携がカウント数またはリスト形式の場合
                try:
                    sns_count = int(sns_str)
                except:
                    # カンマ区切りの場合
                    sns_count = len([s for s in sns_str.split(',') if s.strip()])
            
            web_score = min(15, sns_count * 5)
            scores['scores']['Web積極性'] = web_score
            
            # 5. 医院規模 (10点): 営業時間 + 写真数
            scale_score = 0
            
            # 営業時間の有無
            operating_hours = clinic.get('営業時間', '')
            if operating_hours and operating_hours.strip():
                scale_score += 5
            
            # 写真枚数
            try:
                photos = int(clinic.get('写真枚数', '0'))
                if photos > 0:
                    scale_score += 5
            except (ValueError, TypeError):
                pass
            
            scores['scores']['医院規模'] = scale_score
            
            # 6. ブログ活動 (5点): ブログ更新日ベース
            blog_score = 0
            blog_date = clinic.get('ブログ更新日', '')
            if blog_date and blog_date.strip():
                try:
                    # YYYY-MM-DD形式を想定
                    blog_date_obj = datetime.strptime(blog_date, '%Y-%m-%d')
                    days_ago = (datetime.now() - blog_date_obj).days
                    
                    if days_ago <= 30:
                        blog_score = 5
                    elif days_ago <= 90:
                        blog_score = 3
                    elif days_ago <= 180:
                        blog_score = 1
                except:
                    # 日付形式が異なる場合や空の場合
                    pass
            
            scores['scores']['ブログ活動'] = blog_score
            
            # 合計スコア計算
            total_score = sum(scores['scores'].values())
            scores['total_score'] = round(total_score, 1)
            
            results.append(scores)
            
        except Exception as e:
            print(f"エラー: {clinic_name} - {str(e)}")
            continue
    
    return results

def main():
    # ファイルパス設定
    csv_file = Path('/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads/scoring_batches/batch_011_to_score.csv')
    output_file = Path('/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads/scoring_results_batch_011.json')
    
    print(f"📊 Batch 011スコアリング開始")
    print(f"📂 入力ファイル: {csv_file}")
    
    # CSVを読み込み
    clinics = load_csv(str(csv_file))
    print(f"📊 読み込み件数: {len(clinics)}件")
    
    # スコアリング実行
    results = calculate_scores(clinics)
    print(f"✓ スコアリング完了: {len(results)}件")
    
    # JSON出力
    output_data = {
        'metadata': {
            'batch': 'batch_011',
            'total_clinics': len(clinics),
            'scored_clinics': len(results),
            'timestamp': datetime.now().isoformat(),
            'scoring_criteria': {
                '基礎評価': '20点（rating × 4）',
                '来院患者数': '20点（レビュー件数ベース）',
                '子ども対応力': '30点（kids_content + 医院名キーワード + waiting_room_photo）',
                'Web積極性': '15点（SNS数 × 5）',
                '医院規模': '10点（営業時間 + 写真数）',
                'ブログ活動': '5点（ブログ更新日ベース）'
            }
        },
        'results': results
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ JSON出力完了: {output_file}")
    
    # 統計情報の表示
    scores_array = [r['total_score'] for r in results]
    if scores_array:
        avg_score = sum(scores_array) / len(scores_array)
        max_score = max(scores_array)
        min_score = min(scores_array)
        
        print(f"\n📈 スコア統計:")
        print(f"   平均: {avg_score:.1f}点")
        print(f"   最高: {max_score:.1f}点")
        print(f"   最低: {min_score:.1f}点")
    
    return output_file

if __name__ == '__main__':
    main()
