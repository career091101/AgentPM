---
name: extract-content
description: |
  Xタイムライン・ツイート詳細からコンテンツを抽出するスキル。
  リンク先の記事本文、メタ情報、動画情報を取得します。

  処理内容:
  - 記事: WebFetch + LLMで本文・メタ情報取得
  - YouTube: 基本情報のみ（字幕抽出は今後実装）
  - PDF: メタ情報のみ（全文抽出は今後実装）

  所要時間: 5-10分
  出力: extracted_contents_{date}.json

trigger_keywords:
  - "コンテンツ抽出"
  - "extract-content"
  - "記事抽出"

stage: Phase 2-1
dependencies:
  - scrape-tweet-details (tweet_details_{date}.json)

output_file: Stock/programs/副業/projects/SNS/data/extracted_contents_{date}.json
execution_time: 5-10分
priority: P1
model: claude-haiku-4-5-20251001  # Haiku 4.5 (2026年1月時点の最新モデル)
---

# Extract Content Skill - Phase 2-1

Xタイムライン・ツイート詳細からコンテンツを抽出するスキル。

**Version**: 1.0

---

## このSkillでできること

1. **リンク先記事の抽出**
   - タイトル、本文、メタディスクリプション取得
   - WebFetch toolを使用した高速抽出
   - エラーハンドリング（403 Forbidden等）

2. **YouTube動画情報取得**
   - 基本情報（タイトル、説明文）
   - 字幕抽出は今後実装予定

3. **PDF情報取得**
   - メタ情報のみ
   - 全文抽出は今後実装予定

4. **統計情報生成**
   - 成功率、エラー率、総単語数
   - リンクタイプ別分類

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `tweet_details_{date}.json` (scrape-tweet-detailsスキルの出力) |
| **出力** | `extracted_contents_{date}.json` (約1,300ワード、12リンク) |
| **次のアクション** | analyze-repliesスキルとresearch-topicスキルに並列起動 |

---

## Instructions

**実行モード**: 自律実行（エラーハンドリング自動）
**推定所要時間**: 5-10分

---

### STEP 1: 入力ファイル読み込み

**実行**: Read tool

**パス**: `Stock/programs/副業/projects/SNS/data/tweet_details_{date}.json`

**検証**:
- ファイル存在確認
- JSONフォーマット検証
- リンクデータ存在確認（最低5件以上）

**エラーハンドリング**:
- ファイル未検出 → **即時停止**、scrape-tweet-detailsスキルの再実行を促す
- JSONパースエラー → **即時停止**、ファイル破損報告
- リンク不足（<5件） → **警告表示**、継続可能

---

### STEP 2: リンク分類とフィルタリング

**処理内容**:
1. URL抽出（tweet_details内の全リンク）
2. ドメイン分類:
   - 記事: 一般的なニュースサイト、ブログ
   - YouTube: youtube.com, youtu.be
   - PDF: .pdf拡張子
   - その他: 広告、SNS内部リンク（除外）
3. 重複URL除外
4. 処理優先順位設定（記事 > YouTube > PDF）

**期待出力**:
- 記事URL: 8-12件
- YouTube URL: 0-3件
- PDF URL: 0-2件

---

### STEP 3: 記事コンテンツ抽出

**実行**: WebFetch tool（並列処理推奨）

**プロンプト**:
```markdown
以下のURLから記事コンテンツを抽出してください:

URL: {url}

抽出項目:
1. タイトル（<title>タグまたは<h1>）
2. 本文（メイン記事部分、広告・ナビゲーション除外）
3. メタディスクリプション（<meta name="description">）
4. 単語数カウント（日本語は文字数÷2で概算）

出力形式（JSON）:
{
  "url": "...",
  "type": "article",
  "title": "...",
  "content": "...",
  "meta_description": "...",
  "word_count": 150,
  "extracted_at": "2026-01-03T...",
  "status": "success"
}

エラー時は以下の形式で返却:
{
  "url": "...",
  "type": "article",
  "status": "error",
  "error": "403 Client Error: Forbidden for url: ..."
}
```

**エラーハンドリング**:
- 403 Forbidden → **スキップ**、エラー記録
- Timeout → **リトライ1回**、失敗時スキップ
- 404 Not Found → **スキップ**、エラー記録
- 成功率<50% → **警告表示**、継続可能

**処理時間**: 並列処理で3-5分（12リンク想定）

---

### STEP 4: YouTube動画情報取得

**実行**: WebFetch tool

**プロンプト**:
```markdown
以下のYouTube URLから動画情報を抽出してください:

URL: {url}

抽出項目:
1. タイトル
2. 説明文（最初の500文字）
3. チャンネル名

出力形式（JSON）:
{
  "url": "...",
  "type": "youtube",
  "title": "...",
  "description": "...",
  "channel": "...",
  "extracted_at": "2026-01-03T...",
  "status": "success"
}
```

**注意**: 字幕抽出は今後実装予定（現在は基本情報のみ）

---

### STEP 5: PDF情報取得

**実行**: WebFetch tool

**プロンプト**:
```markdown
以下のPDF URLからメタ情報を抽出してください:

URL: {url}

抽出項目:
1. ファイル名
2. ファイルサイズ（可能であれば）

出力形式（JSON）:
{
  "url": "...",
  "type": "pdf",
  "filename": "...",
  "file_size": "1.2 MB",
  "extracted_at": "2026-01-03T...",
  "status": "success"
}
```

**注意**: PDF全文抽出は今後実装予定（現在はメタ情報のみ）

---

### STEP 6: 統計情報生成と出力

**処理内容**:
1. メタデータ生成:
   - 処理日時
   - ソースファイル名
   - 総リンク数
   - 成功/エラーカウント
   - リンクタイプ別分類
2. tweet_id、username、domainの補完
3. 単語数集計（総単語数）

**出力形式**:
```json
{
  "metadata": {
    "processed_at": "2026-01-03T12:38:58.651348",
    "source_file": "tweet_details_{date}.json",
    "total_links": 12,
    "success_count": 11,
    "error_count": 1,
    "link_types": {
      "article": 12,
      "youtube": 0,
      "pdf": 0
    }
  },
  "extracted_contents": [
    {
      "url": "...",
      "type": "article",
      "title": "...",
      "content": "...",
      "meta_description": "...",
      "word_count": 150,
      "extracted_at": "2026-01-03T...",
      "status": "success",
      "tweet_id": "...",
      "username": "...",
      "domain": "..."
    },
    ...
  ]
}
```

**パス**: `Stock/programs/副業/projects/SNS/data/extracted_contents_{date}.json`

**実行**: Write tool

---

## エラーハンドリング

### 基本方針

| エラータイプ | 対応 | 理由 |
|------------|------|------|
| **入力ファイル未検出** | 即時停止 | 前段階の再実行が必要 |
| **リンク抽出失敗** | スキップ | 他のリンクで補完可能 |
| **成功率<50%** | 警告表示 | 品質低下を通知 |
| **全リンク失敗** | 即時停止 | データ不足で後続処理不可 |

### リトライ戦略

- タイムアウト: 1回リトライ
- 403/404: リトライなし、スキップ
- ネットワークエラー: 1回リトライ

参照: `.claude/skills/_shared/error_handling_patterns.md`

---

## 品質基準

- **成功率**: 80%以上（12リンク中10件以上成功）
- **総単語数**: 1,000ワード以上
- **処理時間**: 10分以内

---

## 使用例

```
User: /extract-content

Skill:
# コンテンツ抽出開始

入力: Stock/programs/副業/projects/SNS/data/tweet_details_20260103.json

🔄 STEP 1: 入力ファイル読み込み中...
✅ 入力ファイル読み込み完了（12リンク検出）

🔄 STEP 2: リンク分類とフィルタリング中...
✅ リンク分類完了（記事: 12件、YouTube: 0件、PDF: 0件）

🔄 STEP 3: 記事コンテンツ抽出中...（並列処理）
   - 1/12: https://event.rakuten.co.jp/... ✅ 成功（150ワード）
   - 2/12: https://help.x.com/... ❌ エラー（403 Forbidden）
   - 3/12: https://video.unext.jp/... ✅ 成功（0ワード）
   ...
   - 12/12: https://microlaunch.net/ ✅ 成功（200ワード）
✅ 記事コンテンツ抽出完了（成功率: 91.7%, 11/12件）

🔄 STEP 6: 統計情報生成と出力中...
✅ 統計情報生成完了

---

# コンテンツ抽出完了

出力: Stock/programs/副業/projects/SNS/data/extracted_contents_20260103.json

統計:
- 総リンク数: 12件
- 成功: 11件（91.7%）
- エラー: 1件（8.3%）
- 総単語数: 1,322ワード

次のアクション:
1. analyze-repliesスキルを並列起動
2. research-topicスキルを並列起動
```

---

## Knowledge Base参照

- **WebFetch tool使用例**: `.claude/rules/execution_preference.md`
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`
- **並列実行ルール**: `.claude/rules/parallel_execution.md`
- **Phase 2全体フロー**: `.claude/skills/sns-automation/SKILL.md`

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-03 | 1.0 | 初版作成 |

---

**実装日**: 2026-01-03
**バージョン**: 1.0
