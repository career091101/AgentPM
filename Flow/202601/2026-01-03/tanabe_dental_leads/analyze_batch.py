#!/usr/bin/env python3
"""
バッチ単位のWebサイト分析＋スコアリングスクリプト

使用方法:
  python3 analyze_batch.py --batch 2
"""

import os
import sys
import json
import csv
import argparse
import glob
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic

# .env読み込み
load_dotenv()

# ANTHROPIC_API_KEYを環境変数から直接取得
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    print("❌ エラー: ANTHROPIC_API_KEY環境変数が設定されていません")
    print("   ~/.zshrc または ~/.bashrc に以下を追加してください:")
    print("   export ANTHROPIC_API_KEY='your-api-key-here'")
    sys.exit(1)

def analyze_website_with_claude(url, name):
    """
    Claude APIでWebサイトを分析

    分析項目:
    - 小児歯科の有無
    - キッズコンテンツ（絵本、おもちゃ、キッズスペース等の記載）
    - 待合室の写真
    - SNS連携（Instagram, Facebook, LINE, Twitter/X）
    - 営業時間
    - ブログ最終更新日
    - 院長名
    """
    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""
あなたは歯科医院のWebサイト分析エキスパートです。

以下のWebサイトを分析し、JSON形式で回答してください。

医院名: {name}
WebサイトURL: {url}

【分析項目】
1. has_pediatric: 小児歯科の診療科目があるか（true/false）
2. kids_content: キッズコンテンツの記載（絵本、おもちゃ、キッズスペース、子ども専用待合室等）があるか（true/false）
3. waiting_room_photo: 待合室の写真があるか（true/false）
4. sns_instagram: Instagramへのリンクがあるか（true/false）
5. sns_facebook: Facebookへのリンクがあるか（true/false）
6. sns_line: LINEへのリンクまたはQRコードがあるか（true/false）
7. sns_twitter: Twitter/Xへのリンクがあるか（true/false）
8. operating_hours: 営業時間（テキスト、例: "月-金 9:00-18:00"）
9. blog_updated: ブログ最終更新日（YYYY-MM-DD形式、ブログがない場合はnull）
10. director_name: 院長名（フルネーム、記載がない場合は空文字）

【出力形式】
{{
  "has_pediatric": true,
  "kids_content": true,
  "waiting_room_photo": false,
  "sns_instagram": true,
  "sns_facebook": false,
  "sns_line": true,
  "sns_twitter": false,
  "operating_hours": "月-金 9:00-18:00、土 9:00-13:00",
  "blog_updated": "2025-12-25",
  "director_name": "田中太郎"
}}

注意:
- WebサイトにアクセスせずにURLから判断してください
- 情報が不明な場合はfalse/null/空文字を返してください
- 必ずJSON形式で回答してください
"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = message.content[0].text

        # JSON抽出（マークダウンコードブロックを除去）
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.find("```", json_start)
            response_text = response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.find("```") + 3
            json_end = response_text.find("```", json_start)
            response_text = response_text[json_start:json_end].strip()

        analysis = json.loads(response_text)
        return analysis

    except Exception as e:
        print(f"⚠️  {name} の分析エラー: {e}")
        return {
            "has_pediatric": False,
            "kids_content": False,
            "waiting_room_photo": False,
            "sns_instagram": False,
            "sns_facebook": False,
            "sns_line": False,
            "sns_twitter": False,
            "operating_hours": "",
            "blog_updated": None,
            "director_name": ""
        }

def calculate_score(raw_data, website_analysis):
    """
    130点満点でスコア計算

    配点:
    - 基礎評価: 10点（Google評価★4.0以上）
    - 来院患者数: 15点（レビュー件数100件以上で満点）
    - 子ども対応力: 30点（小児歯科15 + キッズコンテンツ15）
    - Web積極性: 25点（SNS 各5点 × 4種類 + Webサイトあり5点）
    - 医院規模: 20点（写真枚数10 + 営業時間10）
    - ブログ活動: 30点（30日以内更新で満点）
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
    rating = raw_data.get('rating', 0)
    if rating >= 4.0:
        breakdown["base_evaluation"] = 10
        score += 10

    # 2. 来院患者数（15点）
    reviews = raw_data.get('user_ratings_total', 0)
    if reviews >= 100:
        breakdown["patient_volume"] = 15
        score += 15
    elif reviews >= 50:
        breakdown["patient_volume"] = 10
        score += 10
    elif reviews >= 20:
        breakdown["patient_volume"] = 5
        score += 5

    # 3. 子ども対応力（30点）
    if website_analysis.get('has_pediatric'):
        breakdown["children_friendliness"] += 15
        score += 15
    if website_analysis.get('kids_content'):
        breakdown["children_friendliness"] += 15
        score += 15

    # 4. Web積極性（25点）
    if website_analysis.get('sns_instagram'):
        breakdown["web_activity"] += 5
        score += 5
    if website_analysis.get('sns_facebook'):
        breakdown["web_activity"] += 5
        score += 5
    if website_analysis.get('sns_line'):
        breakdown["web_activity"] += 5
        score += 5
    if website_analysis.get('sns_twitter'):
        breakdown["web_activity"] += 5
        score += 5
    if raw_data.get('website'):
        breakdown["web_activity"] += 5
        score += 5

    # 5. 医院規模（20点）
    photos = raw_data.get('photos', [])
    photo_count = len(photos) if isinstance(photos, list) else 0
    if photo_count >= 10:
        breakdown["clinic_scale"] += 10
        score += 10
    elif photo_count >= 5:
        breakdown["clinic_scale"] += 5
        score += 5

    operating_hours = website_analysis.get('operating_hours', '')
    if operating_hours:
        if '土' in operating_hours or '日' in operating_hours:
            breakdown["clinic_scale"] += 5
            score += 5
        if '18:00' in operating_hours or '19:00' in operating_hours:
            breakdown["clinic_scale"] += 5
            score += 5

    # 6. ブログ活動（30点）
    blog_updated = website_analysis.get('blog_updated')
    if blog_updated:
        try:
            last_update = datetime.strptime(blog_updated, '%Y-%m-%d')
            days_ago = (datetime.now() - last_update).days

            if days_ago <= 30:
                breakdown["blog_activity"] = 30
                score += 30
            elif days_ago <= 90:
                breakdown["blog_activity"] = 20
                score += 20
            elif days_ago <= 180:
                breakdown["blog_activity"] = 10
                score += 10
        except:
            pass

    return score, breakdown

def main():
    parser = argparse.ArgumentParser(description='バッチ単位のWebサイト分析＋スコアリング')
    parser.add_argument('--batch', type=int, required=True, help='バッチ番号（1-360）')
    parser.add_argument('--limit', type=int, default=None, help='処理件数制限（テスト用）')
    args = parser.parse_args()

    batch_num = args.batch

    print("=" * 60)
    print(f"バッチ {batch_num}/360 の分析開始")
    print("=" * 60)

    # RAWデータ読み込み
    pattern = f"batch_{batch_num:03d}_raw_data_*.json"
    files = glob.glob(pattern)

    if not files:
        print(f"❌ エラー: {pattern} が見つかりません")
        sys.exit(1)

    raw_file = files[0]
    print(f"\n📂 RAWデータ読み込み: {raw_file}")

    with open(raw_file, 'r', encoding='utf-8') as f:
        raw_json = json.load(f)

    # JSONフォーマットに応じて clinics リストを取得
    if isinstance(raw_json, dict) and 'clinics' in raw_json:
        raw_data_list = raw_json['clinics']
    elif isinstance(raw_json, list):
        raw_data_list = raw_json
    else:
        print(f"❌ エラー: 不明なJSONフォーマット")
        sys.exit(1)

    # limit指定がある場合は先頭N件のみ処理
    if args.limit:
        raw_data_list = raw_data_list[:args.limit]
        print(f"✅ {len(raw_data_list)}件のデータを読み込みました（--limit {args.limit} 指定）")
    else:
        print(f"✅ {len(raw_data_list)}件のデータを読み込みました")

    # Webサイト分析
    print(f"\n🔍 Webサイト分析開始...")

    results = []
    total = len(raw_data_list)

    for i, raw_data in enumerate(raw_data_list, 1):
        name = raw_data.get('name', 'Unknown')
        url = raw_data.get('website', '')

        print(f"   [{i}/{total}] {name}")

        if not url:
            print(f"      ⚠️  WebサイトURLなし → スキップ")
            website_analysis = {
                "has_pediatric": False,
                "kids_content": False,
                "waiting_room_photo": False,
                "sns_instagram": False,
                "sns_facebook": False,
                "sns_line": False,
                "sns_twitter": False,
                "operating_hours": "",
                "blog_updated": None,
                "director_name": ""
            }
        else:
            website_analysis = analyze_website_with_claude(url, name)

        # スコア計算
        score, breakdown = calculate_score(raw_data, website_analysis)

        # CSV行作成
        sns_list = []
        if website_analysis.get('sns_instagram'):
            sns_list.append('Instagram')
        if website_analysis.get('sns_facebook'):
            sns_list.append('Facebook')
        if website_analysis.get('sns_line'):
            sns_list.append('LINE')
        if website_analysis.get('sns_twitter'):
            sns_list.append('X')

        row = {
            'スコア': score,
            '医院名': name,
            '医院長名': website_analysis.get('director_name', ''),
            '郵便番号': '',  # Google Maps APIにはない
            '住所': raw_data.get('formatted_address', ''),
            '基礎評価': breakdown['base_evaluation'],
            '来院患者数': breakdown['patient_volume'],
            '子ども対応力': breakdown['children_friendliness'],
            'Web積極性': breakdown['web_activity'],
            '医院規模': breakdown['clinic_scale'],
            'ブログ活動': breakdown['blog_activity'],
            '営業時間': website_analysis.get('operating_hours', ''),
            'ブログ更新日': website_analysis.get('blog_updated', ''),
            '電話番号': raw_data.get('formatted_phone_number', ''),
            'WebサイトURL': url,
            '評価': raw_data.get('rating', 0),
            'レビュー件数': raw_data.get('user_ratings_total', 0),
            '診療科目タグ': ','.join(raw_data.get('types', [])),
            '写真枚数': len(raw_data.get('photos', [])),
            'SNS連携': ','.join(sns_list) if sns_list else '',
            '子ども対応力スコア': breakdown['children_friendliness'],
            'Google Maps URL': f"https://maps.google.com/?cid={raw_data.get('place_id', '')}"
        }

        results.append(row)

    # スコア順にソート
    results_sorted = sorted(results, key=lambda x: x['スコア'], reverse=True)

    # CSV出力
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_output = f"batch_{batch_num:03d}_leads_{timestamp}.csv"

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

    print(f"\n✅ CSV出力完了: {csv_output}")

    # 統計情報
    print(f"\n--- 統計情報 ---")
    print(f"総件数: {len(results)}件")

    if results:
        avg_score = sum(r['スコア'] for r in results) / len(results)
        print(f"平均スコア: {avg_score:.1f}点")

        high_score_count = sum(1 for r in results if r['スコア'] >= 80)
        print(f"高スコア（80点以上）: {high_score_count}件")

        print(f"\nTop 3医院:")
        for i, row in enumerate(results_sorted[:3], 1):
            print(f"  {i}. {row['医院名']}: {row['スコア']}点")

    print(f"\n✅ バッチ {batch_num} 処理完了")

if __name__ == '__main__':
    main()
