# Phase 4: LinkedIn予約投稿 - 詳細手順（Late API統合版）

**所要時間**: 2-5分（並列自動化）

---

## 概要

3つの投稿案をLate API経由で個別に予約投稿します。既存予約との競合を自動検出し、利用可能な日付に自動分散。Slack承認不要の完全自動化。

---

## STEP 4.0: 既存予約投稿の競合検出（30秒）

### 目的

Late APIから既存の予約投稿を取得し、8:00 AM JSTの予約済み日付を抽出

### 実行

LLM推論 + Late API GET request

```python
import requests
import json
from datetime import datetime, timedelta
import pytz

# Late API設定読み込み
with open("Stock/programs/副業/projects/SNS/config/late_api_config.json", "r") as f:
    config = json.load(f)

API_KEY = config["api_key"]
BASE_URL = config["base_url"]

# 既存の予約投稿を取得
response = requests.get(
    f'{BASE_URL}/posts',
    headers={
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    },
    params={'status': 'scheduled'},
    timeout=30
)

scheduled_posts = response.json()

# 8:00 AM JST予約済み日付を抽出
jst = pytz.timezone('Asia/Tokyo')
reserved_dates = set()

for post in scheduled_posts.get('posts', []):
    scheduled_for = post.get('scheduledFor')
    if scheduled_for:
        dt = datetime.fromisoformat(scheduled_for.replace('Z', '+00:00'))
        dt_jst = dt.astimezone(jst)

        # Only 8:00 AM reservations
        if dt_jst.hour == 8 and dt_jst.minute == 0:
            reserved_dates.add(dt_jst.date())

print(f"📊 既存予約投稿: {len(scheduled_posts.get('posts', []))}件")
print(f"🚫 8:00 AM予約済み日付: {sorted(reserved_dates)}")
```

### 期待出力

- `reserved_dates`: 8:00 AM予約済み日付のset
- 例: `{datetime.date(2026, 1, 6)}`

---

## STEP 4.1: 利用可能日付の特定とスコアベース投稿計画（30秒）

### 目的

競合を回避した上で、直近3日間の8:00 AMを確保し、スコア順に割り当て

### 実行

LLM推論

```python
# 利用可能な日付を検索（競合回避）
available_dates = []
current_date = datetime.now(jst).date() + timedelta(days=1)

while len(available_dates) < 3:
    if current_date not in reserved_dates:
        available_dates.append(current_date)
    current_date += timedelta(days=1)

print(f"✅ 利用可能日付: {[str(d) for d in available_dates]}")

# スコアベース投稿計画（最高スコア案 → 最初の利用可能日）
# 前提: Phase 3で案2=95点、案1=92点、案3=88点
posting_plan = [
    {
        'date': str(available_dates[0]),
        'time': '08:00',
        'variant': '案2（95点、最推奨）'
    },
    {
        'date': str(available_dates[1]),
        'time': '08:00',
        'variant': '案1（92点）'
    },
    {
        'date': str(available_dates[2]),
        'time': '08:00',
        'variant': '案3（88点）'
    }
]

# 計画を保存
plan_output = {
    'existing_scheduled_count': len(scheduled_posts.get('posts', [])),
    'reserved_8am_dates': [str(d) for d in sorted(reserved_dates)],
    'available_dates': [str(d) for d in available_dates],
    'posting_plan': posting_plan
}

with open(f"Stock/programs/副業/projects/SNS/data/available_dates_{date}.json", "w", encoding="utf-8") as f:
    json.dump(plan_output, f, indent=2, ensure_ascii=False)

print(f"📄 投稿計画保存: available_dates_{date}.json")
```

### 期待出力

- `available_dates_{date}.json`: 投稿計画（3日分の日付とバリアント割り当て）

---

## STEP 4.2: Phase 3出力の読み込みとコンテンツ抽出（1分）

### 実行

LLM推論 + 修正済みregexパターン

```python
import re

# Phase 3出力を読み込み
with open(f"Stock/programs/副業/projects/SNS/data/posts_generated_takano_{date}.md", "r", encoding="utf-8") as f:
    markdown_content = f.read()

def extract_post_content(markdown, variant_number):
    """
    案Nの本文を抽出（タイトル重複・装飾除去版）

    修正内容:
    - タイトル重複を削除（本文に既に含まれているため）
    - Markdown装飾（**太字**等）を除去
    - 余分な箇条書き・番号付きリストを除去
    """
    # 修正済みパターン: group(1)=タイトル, group(2)=本文
    pattern = rf'## 案{variant_number}:.*?\n### タイトル\n\*\*(.*?)\*\*\n\n### 本文.*?\n(.*?)(?=\n### First Comment|$)'
    match = re.search(pattern, markdown, re.DOTALL)

    if match:
        # group(2) = 本文（既にタイトルが含まれているため、titleは使用しない）
        body = match.group(2).strip()

        # Markdown装飾を除去
        body = re.sub(r'\*\*(.+?)\*\*', r'\1', body)  # 太字除去
        body = re.sub(r'^\- ', '', body, flags=re.MULTILINE)  # 箇条書き除去
        body = re.sub(r'^\d+\. ', '', body, flags=re.MULTILINE)  # 番号付きリスト除去

        return body

    return None

# 案1-3のコンテンツ抽出
variant_contents = {}
for variant_num in [1, 2, 3]:
    content = extract_post_content(markdown_content, variant_num)
    if content:
        variant_contents[f"案{variant_num}"] = content
        print(f"✅ 案{variant_num}抽出成功: {len(content)}文字")
    else:
        print(f"❌ 案{variant_num}抽出失敗")
```

### 期待出力

- `variant_contents`: 案1-3のコンテンツ辞書
- 例: `{"案1": "...", "案2": "...", "案3": "..."}`

### 重要

修正済みregexパターンを使用:
- `match.group(2)` で本文を取得（旧: `group(3)`）
- 文字数カウント部分を除外（`### 本文.*?\n` に変更）

---

## STEP 4.3: Late API予約投稿（競合回避・スコア順・多日分散、1-2分）

### 重要

複数案を個別投稿するため、**必ずPythonスクリプトを使用**すること。LLM推論での投稿は禁止。

### 実行

`late_api_multi_post_v2.py`スクリプト（競合回避機能付き、確実な3回独立POST）

```bash
# 自動実行（確認プロンプトあり）
cd Stock/programs/副業/projects/SNS
python3 scripts/late_api_multi_post_v2.py

# または標準入力で自動確認
echo "y" | python3 scripts/late_api_multi_post_v2.py
```

### スクリプトの動作（v2.1: 競合回避機能統合）

1. **Late APIから既存予約投稿を取得**（GET /posts?status=scheduled）
2. **8:00 AM JST予約済み日付を抽出**して競合を検出
3. **利用可能な日付を自動検索**（競合日を避けて直近3日間を確保）
4. `posts_generated_takano_{date}.md` から3案を個別抽出
5. 各案を完全に独立したコンテンツとして準備
6. **3回の独立したPOSTリクエスト**を送信（バリアント結合なし、競合回避済み日付で予約）
7. 結果を `late_api_fixed_{date}.json` に保存

### 実行時の出力例

```
🔍 既存予約投稿をチェック中...
   既存予約投稿: 8件
   8:00 AM予約済み日付: ['2026-01-06', '2026-01-07', '2026-01-08', '2026-01-09', '2026-01-10']

✅ 利用可能日付: ['2026-01-11', '2026-01-12', '2026-01-13']

============================================================
投稿計画（競合回避済み）
============================================================
📅 2026-01-11 08:00 JST
   案2: OpenAIが「ひっそり公開」したGPT-5.2プロンプトガイド...

📅 2026-01-12 08:00 JST
   案1: Claudeが3Dモデリングを完全自動化...

📅 2026-01-13 08:00 JST
   案3: OpenAIが社員に平均年収2.2億円払う理由...
```

### 保存ファイル例

```json
{
  "executed_at": "2026-01-05T17:54:23+09:00",
  "target_dates": ["2026-01-11", "2026-01-12", "2026-01-13"],
  "platform": "linkedin",
  "existing_reservations": {
    "total": 8,
    "reserved_8am_dates": ["2026-01-06", "2026-01-07", "2026-01-08", "2026-01-09", "2026-01-10"]
  },
  "results": [
    {
      "variant": "案2",
      "status": "success",
      "post_id": "695b7c3a72371c896d844b7c",
      "scheduled_for": "2026-01-11T08:00:00+09:00",
      "platform": "linkedin",
      "title": "OpenAIが「ひっそり公開」したGPT-5.2プロンプトガイド..."
    },
    {
      "variant": "案1",
      "status": "success",
      "post_id": "695b7c3c04c93004f19b809f",
      "scheduled_for": "2026-01-12T08:00:00+09:00",
      "platform": "linkedin",
      "title": "Claudeが3Dモデリングを完全自動化..."
    },
    {
      "variant": "案3",
      "status": "success",
      "post_id": "695b7c3e72371c896d844bdb",
      "scheduled_for": "2026-01-13T08:00:00+09:00",
      "platform": "linkedin",
      "title": "OpenAIが社員に平均年収2.2億円払う理由..."
    }
  ]
}
```

### 注意事項

- スクリプトは `.env` ファイルから環境変数を読み込みます
- インラインコメント（例: `VAR="value"  # comment`）は使用禁止
- **既存予約との競合を自動検出・回避**（8:00 AM JST予約済み日付をスキップ）
- Late APIダッシュボード（https://getlate.dev/dashboard）で投稿を確認可能

### 期待出力

- `late_api_fixed_{date}.json`: 3案の予約結果（競合回避済み、異なる日付に分散）
- 予約日時は既存予約を避けた最も早い3日間（8:00 AM JST）

---

## STEP 4.1.3: Late API失敗時のフォールバック

Late APIが失敗した案については、Markdownファイルを生成:

```python
# Late API失敗案のMarkdownファイル生成
failed_posts = [r for r in results if r["status"] == "error"]

if failed_posts:
    fallback_dir = "Stock/programs/副業/projects/SNS/data/manual_posts"
    os.makedirs(fallback_dir, exist_ok=True)

    for failed in failed_posts:
        variant_num = failed["variant"].replace("案", "")
        fallback_path = f"{fallback_dir}/linkedin_{date}_variant{variant_num}.md"

        with open(fallback_path, "w", encoding="utf-8") as f:
            f.write(f"# LinkedIn投稿 - {failed['variant']}\n\n")
            f.write(f"**予定投稿日時**: {tomorrow_8am.strftime('%Y-%m-%d %H:%M JST')}\n\n")
            f.write(f"**Late APIエラー**: {failed.get('error_message', 'Unknown')}\n\n")
            f.write("---\n\n")
            f.write(posts[int(variant_num)-1])

        print(f"📝 手動投稿用Markdown生成: {fallback_path}")
```

---

## STEP 4.1.4: 結果サマリー表示

```python
success_count = len([r for r in results if r["status"] == "success"])
failed_count = len([r for r in results if r["status"] == "error"])

print(f"\n{'='*50}")
print(f"Late API予約投稿完了")
print(f"{'='*50}")
print(f"✅ 成功: {success_count}/3案")
print(f"❌ 失敗: {failed_count}/3案")
print(f"📅 予約投稿日時: {tomorrow_8am.strftime('%Y-%m-%d %H:%M JST')}")
print(f"{'='*50}\n")
```

---

## Late API統合詳細

### Late API特有のエラー処理

Late APIのエラーコード別対応、リトライ戦略、完全失敗時の対応については以下を参照：

📖 **[@late_api_integration_guide.md#エラーハンドリング階層](../late_api_integration_guide.md#エラーハンドリング階層)**

### 共通エラーハンドリングパターン

全スキル共通のエラーハンドリングパターン（WebSearch失敗、ファイル読み込みエラー等）は以下を参照：

📖 **[@_shared/error_handling_patterns.md](../../_shared/error_handling_patterns.md)**

---

## プラットフォーム別統合戦略

### LinkedIn: 本文 + First Commentを1投稿に統合

Late APIの予約投稿では、投稿後30秒以内のFirst Comment追加が技術的に困難なため、以下の統合パターンを採用：

```python
LINKEDIN_INTEGRATED_POST = """
[メイン本文: 1,150字]

━━━

【詳報・出典】
[First Comment内容を統合]
- 出典1: [URL]
- 出典2: [URL]
"""
```

**メリット**:
- 予約投稿時の同期問題を回避
- ユーザーは1回の読み込みで全情報取得可能
- エンゲージメント率（ER）への影響は軽微（-5%以内）

### X/Threads: 最初からスレッド形式を採用

個別投稿を後からスレッド化するのは非効率なため、投稿計画段階でスレッド構成を確定：

```python
# X: 7ツイートスレッド（最大140文字/ツイート）
TWITTER_POSTS = [
  "(1/7) [導入部]",
  "(2/7) [本論1]",
  # ... 7ツイート
]

# Threads: 5投稿スレッド（最大500文字/投稿）
THREADS_POSTS = [
  "[導入部 + 本論1]",
  "[本論2]",
  # ... 5投稿
]
```

---

## パフォーマンス

### 実行時間

| 工程 | 所要時間 | 備考 |
|------|---------|------|
| STEP 4.0（競合検出） | 30秒 | Late API GET |
| STEP 4.1（利用可能日付検索） | 30秒 | LLM推論 |
| STEP 4.2（コンテンツ抽出） | 1分 | Regex処理 |
| STEP 4.3（Late API POST） | 1-2分 | 3回独立リクエスト |
| **合計** | **2-5分** | 平均3分 |

### 期待出力

- `Stock/programs/副業/projects/SNS/data/late_api_scheduled_{date}.json` (予約結果)
- 失敗時: `Stock/programs/副業/projects/SNS/data/manual_posts/linkedin_{date}_variant{1-3}.md`

### エラーハンドリング

- **Late API失敗** → 該当案スキップ（Markdownファイル生成）
- **全案失敗** → 警告表示 + Phase 5へ継続

---

## 実装時の重要な注意点（Null2実践から）

### スレッド投稿の必須パラメータ

**🚨 Critical**: スレッド投稿時も`content`フィールドを**必ず設定**すること。

Late APIの仕様上、`threadItems`使用時も`content`フィールドが必須です（最初の投稿内容を設定）。

```python
# ✅ 正しい実装（Null2実践で確認済み）
{
  "content": posts[0],  # 最初の投稿を必ず設定
  "platforms": [{
    "platform": "twitter",
    "accountId": "...",
    "platformSpecificData": {
      "threadItems": [{"content": post} for post in posts]
    }
  }],
  "scheduledFor": "2026-01-07T20:05:00+09:00",
  "timezone": "Asia/Tokyo"
}

# ❌ 誤った実装（エラー発生）
{
  "content": "",  # 空文字列はNG
  "platforms": [{...}]
}
```

**エラー例**:
```
LateAPIError: {"error": "content field is required even when using threadItems"}
```

### スケジューリング時間の分散戦略

**実践例（Null2投稿）**:

| Platform | 予約日時 | 理由 |
|----------|---------|------|
| LinkedIn | 1月7日 08:00 | ビジネスタイム開始（ER 20-30%向上実証済み） |
| Threads | 1月7日 20:00 | 夜のリラックスタイム（高エンゲージメント） |
| X (Twitter) | 1月7日 20:05 | Threadsと5分差（クロスポスト感を軽減） |

**ポイント**:
- 同一日時の一斉投稿を避ける（Bot感の軽減）
- プラットフォーム特性に合わせた時間帯選定
- タイムゾーン統一（`Asia/Tokyo`）

### 画像なし戦略の実践

**結論**: 画像なし投稿でもER低下は限定的（-20%程度）

Null2投稿では、以下の理由から画像なし戦略を採用：

1. **コンテンツ品質優先**: 長文テキストで価値提供
2. **制作工数削減**: 画像作成・承認プロセスの省略
3. **Late API互換性**: 画像アップロード機能の追加実装不要
4. **実測データ**: 過去投稿で画像なし投稿のER 10-15%（画像あり 12-18%）

**今後の方針**:
- Phase 6でClaude Artifactsを活用した自動画像生成を検討
- A/Bテストで定量的効果測定

### エラー時の削除・再作成フロー

**発生事例**: 9件の個別投稿が誤って作成された（スレッド化失敗）

**対処手順**:

1. **Late APIダッシュボードでpost_id確認**
   ```
   https://app.getlate.dev/posts
   → 誤投稿のpost_idをコピー（例: 695864bf38609c72a1d86f08）
   ```

2. **DELETE API呼び出し**
   ```python
   import requests

   DELETE_IDS = [
       "695864bf38609c72a1d86f08",
       "695864bf38609c72a1d86f09",
       # ... 9件
   ]

   for post_id in DELETE_IDS:
       response = requests.delete(
           f"{base_url}/posts/{post_id}",
           headers={"Authorization": f"Bearer {api_key}"},
           timeout=30
       )
       print(f"Deleted: {post_id}, Status: {response.status_code}")
   ```

3. **パラメータ修正後、再投稿**
   ```python
   # 修正済みパラメータで再実行
   post_thread_with_content(
       posts=TWITTER_POSTS,
       platform="twitter",
       scheduled_for="2026-01-07T20:05:00+09:00"
   )
   ```

**教訓**:
- 初回投稿前に必ずDRY RUN（Late API test mode）で検証
- 本番投稿後は即座にダッシュボード確認
- DELETE APIは取り消し不可なので慎重に実行

---

## Phase 4完了判定

以下の条件を満たしていること：

1. ✅ **既存予約投稿の競合検出**（`available_dates_{date}.json` 生成）
2. ✅ **3案のLate API予約投稿**（`late_api_fixed_{date}.json` 生成）
3. ✅ **失敗案のフォールバック処理**（失敗案数分のMarkdown生成）

**予約投稿日時**: 既存予約を回避した最も早い3日間（8:00 AM JST）

**総実行時間**: 2-5分（完全自動化）
