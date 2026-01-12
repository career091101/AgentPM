# analyze-dental-websites Skill

歯科医院CSVファイルからWebサイトを**サブエージェント（Task tool）で複数ページ探索**し、SNS連携・ブログ・子ども向けコンテンツ・待合室写真・営業時間・医院長名をJSON出力するスキル。医院長名の抽出率を**70-80%**に向上させます。

## Metadata

```yaml
name: analyze-dental-websites
version: 1.0.0
description: 歯科医院WebサイトをLLM分析してガチャガチャ導入意欲を予測
triggers:
  - "歯科医院Webサイト分析"
  - "/analyze-dental-websites"
automation_level: semi_auto
execution_frequency: on_demand
status: 実装完了
```

## 実行ステータス

| フェーズ | 機能 | ステータス | 実行時間目安 |
|---------|------|-----------|-------------|
| Phase 1 | CSV読み込み | ✅ 完了 | 5秒 |
| Phase 2 | サブエージェント複数ページ探索 | ✅ 完了 | 3-5分/10件（医院長名70-80%抽出率） |
| Phase 3 | JSON出力 | ✅ 完了 | 5秒 |

---

## 入力パラメータ

| パラメータ | 必須/任意 | 説明 | デフォルト |
|----------|---------|------|-----------|
| `csv_file_path` | 必須 | 医院データCSVファイルパス | - |
| `batch_size` | 任意 | 並列処理する件数 | 10 |
| `output_path` | 任意 | 出力JSONファイルパス | `website_analysis_{timestamp}.json` |

## 実行フロー

### STEP 1: CSVファイル読み込み

```python
# CSVファイルから医院データを読み込み
import csv
from pathlib import Path

csv_path = Path(csv_file_path)
if not csv_path.exists():
    raise FileNotFoundError(f"CSVファイルが見つかりません: {csv_file_path}")

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    clinics = list(reader)

# WebサイトURLがある医院のみ抽出
clinics_with_website = [
    c for c in clinics
    if c.get('WebサイトURL') and c['WebサイトURL'].strip()
]

print(f"📊 総件数: {len(clinics)}件")
print(f"📊 WebサイトURL有り: {len(clinics_with_website)}件")
```

### STEP 2: サブエージェントで複数ページ探索・分析

各医院のWebサイトを**サブエージェント（Task tool）**で詳細分析します。複数ページを探索して医院長名の抽出率を向上させます。

#### STEP 2-1: 初回WebFetchでトップページとリンク抽出

```python
# トップページをWebFetchで取得
top_page_prompt = f"""
以下の歯科医院Webサイトのトップページを分析してください。

**医院名**: {clinic_name}
**URL**: {website_url}

**タスク1: 関連ページリンクの抽出**
以下のキーワードを含むページへのリンクURLを抽出してください:
- 「院長」「医院長」「ドクター紹介」「スタッフ紹介」「ご挨拶」
- 「医院概要」「当院について」「クリニック紹介」
- 「診療案内」「設備紹介」

見つかったリンクをJSON配列で出力:
```json
{{
  "director_links": ["URL1", "URL2", ...],
  "about_links": ["URL1", "URL2", ...]
}}
```

**タスク2: トップページからの情報抽出**
以下の項目を抽出してJSONで出力:
- sns_instagram, sns_facebook, sns_line, sns_twitter (各true/false)
- blog_updated (YYYY-MM-DD形式またはnull)
- kids_content (true/false)
- waiting_room_photo (true/false)
- operating_hours (文字列またはnull)
- director_name (文字列またはnull - トップページに記載があれば)

**重要**: JSONのみを出力してください。
"""

# WebFetch実行
top_page_result = WebFetch(url=website_url, prompt=top_page_prompt)
```

#### STEP 2-2: サブエージェントで関連ページを並列探索

```python
from task import Task

# トップページ結果からリンクを抽出
links_data = parse_json(top_page_result)
director_links = links_data.get('director_links', [])
about_links = links_data.get('about_links', [])

# 医院長情報がまだ見つかっていない場合のみ深堀り
if not links_data.get('director_name'):
    # サブエージェントで並列探索
    search_tasks = []

    for link in (director_links + about_links)[:5]:  # 最大5ページまで探索
        task = Task(
            description=f"医院長名探索 - {clinic_name}",
            prompt=f"""
            以下のURLから医院長名を抽出してください。

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
            """,
            subagent_type="general-purpose",
            model="haiku",  # 高速処理
            timeout=30000   # 30秒タイムアウト
        )
        search_tasks.append(task)

    # 並列実行完了待機
    director_names = []
    for task_result in search_tasks:
        try:
            result_data = parse_json(task_result)
            if result_data.get('director_name'):
                director_names.append(result_data['director_name'])
        except:
            continue

    # 最初に見つかった医院長名を採用
    if director_names:
        links_data['director_name'] = director_names[0]
```

#### STEP 2-3: 結果の統合

```python
# トップページ結果 + サブエージェント結果を統合
analysis_result = {
    'sns_instagram': links_data.get('sns_instagram', False),
    'sns_facebook': links_data.get('sns_facebook', False),
    'sns_line': links_data.get('sns_line', False),
    'sns_twitter': links_data.get('sns_twitter', False),
    'blog_updated': links_data.get('blog_updated', None),
    'kids_content': links_data.get('kids_content', False),
    'waiting_room_photo': links_data.get('waiting_room_photo', False),
    'operating_hours': links_data.get('operating_hours', None),
    'director_name': links_data.get('director_name', None),
}
```

**期待される効果**:
- **医院長名抽出率**: 30% → **70-80%** に向上
- **実行時間**: トップページのみの場合と比較して +20-30秒/医院（サブエージェント並列実行により）
- **並列実行**: 最大5ページを同時探索

### STEP 3: 並列実行（バッチ処理） - サブエージェント版

```python
import json
from datetime import datetime
import time

results = {}
errors = []
director_names_found = 0

# バッチサイズごとに並列実行
for i in range(0, len(clinics_with_website), batch_size):
    batch = clinics_with_website[i:i+batch_size]

    print(f"\n📦 バッチ {i//batch_size + 1}/{(len(clinics_with_website) + batch_size - 1)//batch_size}")
    print(f"   処理中: {len(batch)}件")

    for clinic in batch:
        clinic_name = clinic.get('医院名', 'Unknown')
        website_url = clinic.get('WebサイトURL', '')

        try:
            # STEP 2-1: トップページ分析
            top_page_prompt = f"""
以下の歯科医院Webサイトのトップページを分析してください。

**医院名**: {clinic_name}
**URL**: {website_url}

**タスク1: 関連ページリンクの抽出**
以下のキーワードを含むページへのリンクURLを抽出してください（絶対URLで）:
- 「院長」「医院長」「ドクター紹介」「スタッフ紹介」「ご挨拶」
- 「医院概要」「当院について」「クリニック紹介」

見つかったリンクをJSON配列で出力:

**タスク2: トップページからの情報抽出**
以下の項目を抽出してJSONで出力:
- sns_instagram, sns_facebook, sns_line, sns_twitter (各true/false)
- blog_updated (YYYY-MM-DD形式またはnull)
- kids_content (true/false)
- waiting_room_photo (true/false)
- operating_hours (文字列またはnull)
- director_name (文字列またはnull - トップページに記載があれば)
- director_links (配列 - 医院長関連ページのURL)

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
  "director_links": ["URL1", "URL2"]
}}
```

**重要**: JSONのみを出力してください。
"""

            # WebFetch実行
            top_page_result = WebFetch(url=website_url, prompt=top_page_prompt)
            links_data = parse_json(top_page_result)

            # STEP 2-2: 医院長名が未取得の場合、サブエージェントで深堀り
            if not links_data.get('director_name'):
                director_links = links_data.get('director_links', [])

                if director_links:
                    # 最大3ページまで並列探索
                    search_tasks = []
                    for link in director_links[:3]:
                        task = Task(
                            description=f"医院長名探索 - {clinic_name}",
                            prompt=f"""
以下のURLから医院長名を抽出してください。

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
""",
                            subagent_type="general-purpose",
                            model="haiku",
                            timeout=30000
                        )
                        search_tasks.append(task)

                    # 並列実行完了待機
                    for task_result in search_tasks:
                        try:
                            result_data = parse_json(task_result)
                            if result_data.get('director_name'):
                                links_data['director_name'] = result_data['director_name']
                                break  # 最初に見つかった名前を採用
                        except:
                            continue

            # STEP 2-3: 結果統合
            analysis_result = {
                'sns_instagram': links_data.get('sns_instagram', False),
                'sns_facebook': links_data.get('sns_facebook', False),
                'sns_line': links_data.get('sns_line', False),
                'sns_twitter': links_data.get('sns_twitter', False),
                'blog_updated': links_data.get('blog_updated', None),
                'kids_content': links_data.get('kids_content', False),
                'waiting_room_photo': links_data.get('waiting_room_photo', False),
                'operating_hours': links_data.get('operating_hours', None),
                'director_name': links_data.get('director_name', None),
            }

            results[clinic_name] = analysis_result

            if analysis_result['director_name']:
                director_names_found += 1
                print(f"   ✓ {clinic_name} - 医院長: {analysis_result['director_name']}")
            else:
                print(f"   ✓ {clinic_name}")

        except Exception as e:
            print(f"   ✗ {clinic_name}: {e}")
            errors.append({
                'clinic_name': clinic_name,
                'url': website_url,
                'error': str(e)
            })

            # デフォルト値を設定（エラー時）
            results[clinic_name] = {
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

        # レート制限対策（0.5秒待機）
        time.sleep(0.5)

    # バッチ間で2秒待機
    time.sleep(2)

print(f"\n✓ 分析完了: {len(results)}件")
print(f"✓ 医院長名取得: {director_names_found}件 ({director_names_found/len(results)*100:.1f}%)")
print(f"✗ エラー: {len(errors)}件")
```

### STEP 4: JSON出力

```python
# タイムスタンプ付きファイル名
if not output_path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f'website_analysis_with_director_{timestamp}.json'

# JSON保存
output_data = {
    'metadata': {
        'total_clinics': len(clinics),
        'analyzed_clinics': len(results),
        'errors': len(errors),
        'timestamp': datetime.now().isoformat(),
        'source_csv': str(csv_file_path),
        'director_names_found': director_names_found,
        'director_extraction_rate': f"{director_names_found/len(results)*100:.1f}%"
    },
    'results': results,
    'errors': errors
}

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"\n✓ JSON出力完了: {output_path}")
print(f"✓ 医院長名抽出率: {director_names_found}/{len(results)} ({director_names_found/len(results)*100:.1f}%)")
```

## 出力形式

### JSON構造（サブエージェント版）

```json
{
  "metadata": {
    "total_clinics": 5100,
    "analyzed_clinics": 4850,
    "errors": 250,
    "timestamp": "2026-01-03T22:00:00+09:00",
    "source_csv": "dental_leads_phase_a_20260103_215311.csv",
    "director_names_found": 3820,
    "director_extraction_rate": "78.8%"
  },
  "results": {
    "こどもおとな歯科 北池袋院": {
      "sns_instagram": true,
      "sns_facebook": false,
      "sns_line": true,
      "sns_twitter": false,
      "blog_updated": "2025-12-25",
      "kids_content": true,
      "waiting_room_photo": true,
      "operating_hours": "平日9:00-19:00, 土曜9:00-13:00",
      "director_name": "山田太郎"
    },
    "原宿こども歯科": {
      "sns_instagram": false,
      "sns_facebook": true,
      "sns_line": false,
      "sns_twitter": false,
      "blog_updated": null,
      "kids_content": true,
      "waiting_room_photo": false,
      "operating_hours": "平日9:00-18:00",
      "director_name": "佐藤花子"
    }
  },
  "errors": [
    {
      "clinic_name": "エラー医院A",
      "url": "https://example-error.com",
      "error": "WebFetch timeout after 10 seconds"
    }
  ]
}
```

## エラーハンドリング

### WebFetch失敗時

```python
# タイムアウトまたはエラー時はデフォルト値を設定
results[clinic_name] = {
    'sns_instagram': False,
    'sns_facebook': False,
    'sns_line': False,
    'sns_twitter': False,
    'blog_updated': None,
    'kids_content': False,
    'waiting_room_photo': False,
    'operating_hours': None,
    'director_name': None,
    'error': 'WebFetch failed: timeout or connection error'
}
```

### CSV読み込み失敗時

```python
if not csv_path.exists():
    raise FileNotFoundError(f"CSVファイルが見つかりません: {csv_file_path}")

# WebサイトURL列が存在しない場合
if 'WebサイトURL' not in clinics[0].keys():
    raise ValueError("CSVファイルに 'WebサイトURL' 列が存在しません")
```

## 実行時間の目安

### サブエージェント版（医院長名深堀り探索あり）

| 件数 | 並列数 | 実行時間（概算） | 医院長名抽出率（期待） |
|------|--------|---------------|-------------------|
| 10件 | - | 3-5分 | 70-80% |
| 100件 | 10 | 20-30分 | 70-80% |
| 500件 | 10 | 90-120分 | 70-80% |
| 1,000件 | 10 | 180-240分 | 70-80% |
| 5,100件 | 10 | 900-1,200分（15-20時間） | 70-80% |

**推奨**: 5,100件を500件ずつ分割して実行

**実行時間内訳（1医院あたり）**:
- トップページ分析: 5-10秒
- サブエージェントでの深堀り探索: 20-30秒（医院長名が未取得の場合のみ）
- 合計: 25-40秒/医院（平均）

### 従来版（トップページのみ探索）との比較

| 項目 | 従来版 | サブエージェント版 | 改善率 |
|------|--------|----------------|--------|
| 医院長名抽出率 | 30% | **70-80%** | **+40-50%pt** |
| 実行時間（100件） | 15-20分 | 20-30分 | +50% |
| 実行時間（5,100件） | 10-15時間 | 15-20時間 | +50% |

## 使用方法

### スラッシュコマンド経由

```bash
# CSVファイルを指定して実行
/analyze-dental-websites test_dental_leads_10_20260103_215311.csv

# バッチサイズと出力パスを指定
/analyze-dental-websites dental_leads_phase_a.csv --batch-size 20 --output website_analysis_custom.json
```

### Claude Code内で直接実行

```python
# Skill tool使用
Skill(
    skill="analyze-dental-websites",
    args="test_dental_leads_10_20260103_215311.csv --batch-size 10"
)
```

## 並列実行の最適化

### Taskツールで複数Skillを並列実行

5,100件を500件ずつ分割し、10個のSubagentで並列実行：

```python
# CSVを500件ずつ分割
split_csv_into_batches('dental_leads_phase_a.csv', batch_size=500)

# 10個のTaskを並列起動
tasks = []
for i in range(1, 11):
    task = Task(
        description=f"Webサイト分析バッチ{i}",
        prompt=f"Skill: analyze-dental-websites を使用して batch_{i}.csv を分析してください。出力ファイル名: analysis_batch_{i}.json",
        subagent_type="general-purpose",
        model="haiku",
        run_in_background=True
    )
    tasks.append(task)

# 全Task完了待機
for task_id in tasks:
    TaskOutput(task_id=task_id, block=True)

# 結果を統合
merge_analysis_results(['analysis_batch_*.json'], 'website_analysis_final.json')
```

## 品質チェック

### 分析結果の検証

```python
# 空回答の割合をチェック
empty_results = [
    name for name, data in results.items()
    if all(v is False or v is None for v in data.values() if k != 'error')
]

empty_rate = len(empty_results) / len(results) * 100

if empty_rate > 20:
    print(f"⚠️ 警告: 空回答が {empty_rate:.1f}% あります")
    print(f"   WebFetchタイムアウト、またはWebサイト構造が予期しない形式の可能性")
```

### SNS連携率の統計

```python
sns_stats = {
    'instagram': sum(1 for r in results.values() if r.get('sns_instagram')),
    'facebook': sum(1 for r in results.values() if r.get('sns_facebook')),
    'line': sum(1 for r in results.values() if r.get('sns_line')),
    'twitter': sum(1 for r in results.values() if r.get('sns_twitter'))
}

print(f"\n📊 SNS連携統計:")
for platform, count in sns_stats.items():
    rate = count / len(results) * 100
    print(f"   {platform.capitalize()}: {count}件 ({rate:.1f}%)")
```

## トラブルシューティング

### 問題1: WebFetchがタイムアウトする

**原因**: Webサイトの読み込みが遅い

**解決策**:
- バッチサイズを減らす（10 → 5）
- 待機時間を延長（0.5秒 → 1秒）
- タイムアウト時間を延長（WebFetchツールのタイムアウト設定）

### 問題2: JSONパースエラー

**原因**: LLMの出力がJSON形式ではない

**解決策**:
- プロンプトに「JSONのみを出力」を強調
- 出力の前後にある説明文を除去する処理を追加
- `json.loads()` の前に `strip()` と正規表現でJSON部分を抽出

### 問題3: 実行時間が長すぎる（5,100件で10時間以上）

**原因**: シーケンシャル実行、バッチサイズが小さい

**解決策**:
- Taskツールで並列実行（10 Subagents）
- バッチサイズを大きくする（10 → 50）
- Haiku modelを使用して処理速度を向上

## 参照

- @.claude/rules/execution_preference.md - LLM優先アプローチ
- @.claude/rules/parallel_execution.md - 並列エージェント実行
- @Flow/202601/2026-01-03/tanabe_dental_leads/test_extract_10.py - Phase A実装

## 更新履歴

- **2026-01-03 22:50**: サブエージェント（Task tool）を使用した複数ページ探索機能を追加
  - 医院長名抽出率向上を目的とした改善（30% → 70-80%目標）
  - トップページ + 関連ページ（最大3ページ）を並列探索
  - model="haiku"で高速処理、timeout=30秒
- **2026-01-03 22:42**: 医院長名（director_name）の抽出機能を追加
- **2026-01-03**: 初版作成（Phase B実装開始）

