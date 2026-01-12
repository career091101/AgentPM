# Batch 003 WebFetch Execution Prompt

このプロンプトをClaude Code対話モードで実行してください。

## 実行内容

Batch 003の119ユニーク医院に対して、WebFetchを強制実行し、医院長名抽出率70%以上を達成します。

## 実行手順

### STEP 1: CSVから119ユニーク医院を抽出

```python
import csv
from pathlib import Path
from collections import defaultdict

csv_path = Path('/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads/scoring_batches/batch_003_to_score.csv')

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    all_rows = list(reader)

# ユニーク医院抽出
unique_clinics = {}
for row in all_rows:
    clinic_name = row.get('医院名', '').strip()
    website_url = row.get('WebサイトURL', '').strip()

    if not clinic_name or not website_url:
        continue

    unique_key = f"{clinic_name}|{website_url}"

    if unique_key not in unique_clinics:
        unique_clinics[unique_key] = {
            'clinic_name': clinic_name,
            'website_url': website_url,
            'raw_data': row
        }

print(f"ユニーク医院数: {len(unique_clinics)}")
```

### STEP 2: 各医院に対してWebFetch実行

以下のプロンプトテンプレートを使用して、各医院のWebサイトを分析してください：

```python
# 医院ごとにWebFetch実行
import json
import time

website_analysis = {}
director_names_found = 0

for idx, (unique_key, clinic_info) in enumerate(unique_clinics.items(), 1):
    clinic_name = clinic_info['clinic_name']
    website_url = clinic_info['website_url']

    print(f"\n[{idx}/{len(unique_clinics)}] {clinic_name}")
    print(f"URL: {website_url}")

    # WebFetchプロンプト
    webfetch_prompt = f"""以下の歯科医院Webサイトのトップページを分析してください。

**医院名**: {clinic_name}
**URL**: {website_url}

**タスク1: 関連ページリンクの抽出**
以下のキーワードを含むページへのリンクURLを抽出してください（絶対URLで）:
- 「院長」「医院長」「ドクター紹介」「スタッフ紹介」「ご挨拶」
- 「医院概要」「当院について」「クリニック紹介」

**タスク2: トップページからの情報抽出**
以下の項目を抽出してJSONで出力:
- sns_instagram, sns_facebook, sns_line, sns_twitter (各true/false)
- blog_updated (YYYY-MM-DD形式またはnull)
- kids_content (true/false)
- waiting_room_photo (true/false)
- operating_hours (文字列またはnull)
- director_name (文字列またはnull - トップページに記載があれば)
- director_links (配列 - 医院長関連ページのURL、最大5件)

**出力形式**:
```json
{{
  "sns_instagram": false,
  "sns_facebook": false,
  "sns_line": false,
  "sns_twitter": false,
  "blog_updated": null,
  "kids_content": false,
  "waiting_room_photo": false,
  "operating_hours": null,
  "director_name": null,
  "director_links": []
}}
```

**重要**: JSONのみを出力してください。説明文は不要です。
"""

    try:
        # WebFetch実行
        result = WebFetch(url=website_url, prompt=webfetch_prompt)

        # JSONパース
        result_json = json.loads(result)

        # STEP 2-2: 医院長名が未取得の場合、director_linksを探索
        if not result_json.get('director_name') and result_json.get('director_links'):
            director_links = result_json['director_links'][:3]  # 最大3ページ

            for link in director_links:
                director_prompt = f"""以下のURLから医院長名を抽出してください。

**医院名**: {clinic_name}
**URL**: {link}

**抽出指示**:
1. 「院長」「医院長」「理事長」「代表」などの肩書きと共に記載されている名前を探す
2. フルネーム（姓名）で抽出（例: "田中太郎"）
3. 見つからない場合は null

**出力形式**:
```json
{{
  "director_name": "田中太郎"
}}
```

**重要**: JSONのみを出力してください。
"""

                try:
                    # サブページをWebFetch
                    sub_result = WebFetch(url=link, prompt=director_prompt)
                    sub_json = json.loads(sub_result)

                    if sub_json.get('director_name'):
                        result_json['director_name'] = sub_json['director_name']
                        print(f"  ✓ 医院長名発見: {sub_json['director_name']}")
                        break

                except Exception as e:
                    print(f"  ✗ サブページエラー ({link}): {e}")
                    continue

        # 結果を保存
        website_analysis[clinic_name] = result_json

        if result_json.get('director_name'):
            director_names_found += 1

        # レート制限対策
        time.sleep(1)

    except Exception as e:
        print(f"  ✗ WebFetchエラー: {e}")
        website_analysis[clinic_name] = {
            'sns_instagram': False,
            'sns_facebook': False,
            'sns_line': False,
            'sns_twitter': False,
            'blog_updated': None,
            'kids_content': False,
            'waiting_room_photo': False,
            'operating_hours': None,
            'director_name': None,
            'error': str(e)
        }

print(f"\n完了: {len(website_analysis)}件")
print(f"医院長名取得: {director_names_found}件 ({director_names_found/len(website_analysis)*100:.1f}%)")
```

### STEP 3: スコアリング実行

```python
from datetime import datetime

scoring_results = []

for row in all_rows:
    clinic_name = row.get('医院名', '').strip()

    if not clinic_name:
        continue

    # Webサイト分析結果を取得
    analysis = website_analysis.get(clinic_name, {})

    # RAWデータ
    try:
        rating = float(row.get('評価', 0) or 0)
    except ValueError:
        rating = 0.0

    try:
        user_ratings_total = int(row.get('レビュー件数', 0) or 0)
    except ValueError:
        user_ratings_total = 0

    # スコアリング計算

    # 1. 基礎評価 (20点)
    score_基礎評価 = min(rating * 4, 20)

    # 2. 来院患者数 (20点)
    if user_ratings_total >= 100:
        score_来院患者数 = 20
    elif user_ratings_total >= 50:
        score_来院患者数 = 15
    elif user_ratings_total >= 20:
        score_来院患者数 = 10
    elif user_ratings_total >= 10:
        score_来院患者数 = 5
    else:
        score_来院患者数 = 0

    # 3. 子ども対応力 (30点)
    score_子ども対応力 = 0
    if analysis.get('kids_content'):
        score_子ども対応力 += 15
    if any(kw in clinic_name for kw in ['小児', 'こども', '子ども', 'キッズ', '矯正']):
        score_子ども対応力 += 10
    if analysis.get('waiting_room_photo'):
        score_子ども対応力 += 5
    score_子ども対応力 = min(score_子ども対応力, 30)

    # 4. Web積極性 (15点)
    sns_count = sum([
        analysis.get('sns_instagram', False),
        analysis.get('sns_facebook', False),
        analysis.get('sns_line', False),
        analysis.get('sns_twitter', False)
    ])
    score_Web積極性 = min(sns_count * 5, 15)

    # 5. 医院規模 (10点)
    score_医院規模 = 0
    if analysis.get('operating_hours'):
        score_医院規模 += 5
    try:
        photos = int(row.get('写真枚数', 0) or 0)
        if photos >= 10:
            score_医院規模 += 5
    except ValueError:
        pass

    # 6. ブログ活動 (5点)
    score_ブログ活動 = 0
    blog_updated = analysis.get('blog_updated')
    if blog_updated:
        try:
            blog_date = datetime.strptime(blog_updated, '%Y-%m-%d')
            days_ago = (datetime.now() - blog_date).days

            if days_ago <= 30:
                score_ブログ活動 = 5
            elif days_ago <= 60:
                score_ブログ活動 = 4
            elif days_ago <= 90:
                score_ブログ活動 = 3
            elif days_ago <= 180:
                score_ブログ活動 = 2
            elif days_ago <= 365:
                score_ブログ活動 = 1
        except ValueError:
            pass

    # 総合スコア
    total_score = (
        score_基礎評価 +
        score_来院患者数 +
        score_子ども対応力 +
        score_Web積極性 +
        score_医院規模 +
        score_ブログ活動
    )

    # 結果レコード
    result = {
        'clinic_name': clinic_name,
        'total_score': round(total_score, 1),
        'scores': {
            '基礎評価': round(score_基礎評価, 1),
            '来院患者数': score_来院患者数,
            '子ども対応力': score_子ども対応力,
            'Web積極性': score_Web積極性,
            '医院規模': score_医院規模,
            'ブログ活動': score_ブログ活動
        },
        'website_analysis': analysis,
        'raw_data': {
            'rating': rating,
            'user_ratings_total': user_ratings_total,
            'formatted_address': row.get('住所', ''),
            'formatted_phone_number': row.get('電話番号', ''),
            'website': row.get('WebサイトURL', ''),
            'photos': row.get('写真枚数', ''),
            'operating_hours': row.get('営業時間', ''),
            'google_maps_url': row.get('Google Maps URL', '')
        }
    }

    scoring_results.append(result)

print(f"スコアリング完了: {len(scoring_results)}件")
```

### STEP 4: JSON出力

```python
from datetime import datetime
import json
from pathlib import Path

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = f'scoring_results_batch_003_retry_{timestamp}.json'

output_data = {
    'metadata': {
        'batch_file': 'batch_003_to_score.csv',
        'total_clinics': len(all_rows),
        'unique_clinics': len(unique_clinics),
        'timestamp': datetime.now().isoformat(),
        'retry_execution': True,
        'webfetch_forced': True,
        'director_names_found': director_names_found,
        'director_extraction_rate': f"{director_names_found/len(unique_clinics)*100:.1f}%"
    },
    'results': scoring_results
}

output_file = Path('/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads') / output_path

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"✓ JSON出力完了: {output_file}")
print(f"✓ 医院長名取得率: {director_names_found}/{len(unique_clinics)} ({director_names_found/len(unique_clinics)*100:.1f}%)")

# スコア統計
scores = [r['total_score'] for r in scoring_results]
avg_score = sum(scores) / len(scores) if scores else 0
max_score = max(scores) if scores else 0
min_score = min(scores) if scores else 0

print(f"\n📊 スコア統計:")
print(f"   平均スコア: {avg_score:.1f}点")
print(f"   最高スコア: {max_score:.1f}点")
print(f"   最低スコア: {min_score:.1f}点")

# 高スコア医院TOP 10
top_10 = sorted(scoring_results, key=lambda x: x['total_score'], reverse=True)[:10]
print(f"\n🏆 高スコア医院 TOP 10:")
for i, clinic in enumerate(top_10, 1):
    print(f"   {i}. {clinic['clinic_name']}: {clinic['total_score']}点")
```

## 実行時間の目安

- 119ユニーク医院 × (トップページ10秒 + サブページ30秒) = 約80分
- 医院長名抽出率目標: 70%以上

## 注意事項

1. **WebFetchタイムアウト**: 一部の医院はタイムアウトする可能性があります。その場合はエラーハンドリングでデフォルト値を設定します。
2. **医院長名抽出率**: トップページのみでは30%、サブページ探索で70-80%を目指します。
3. **レート制限**: 1秒待機でレート制限を回避しています。

## 実行後の確認事項

- [ ] JSON出力ファイルが生成されているか
- [ ] 医院長名抽出率が70%以上か
- [ ] スコアリングが正常に実行されているか
- [ ] エラー件数が10%未満か
