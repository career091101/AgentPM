---
name: analyze-replies
description: |
  ツイート詳細からリプライを分析し、インサイトを抽出するスキル。
  4カテゴリ分類（共感・期待、批判・懸念、追加情報・洞察、質問）を実施。

  処理内容:
  - リプライ感情分析（LLM使用）
  - カテゴリ別分類（4カテゴリ）
  - インサイト抽出（投稿作成に有用な洞察）
  - エンゲージメント重視（いいね数優先）

  所要時間: 10-15分
  出力: reply_insights_{date}.json

trigger_keywords:
  - "リプライ分析"
  - "analyze-replies"
  - "インサイト抽出"

stage: Phase 2-2
dependencies:
  - scrape-tweet-details (tweet_details_{date}.json)

output_file: Stock/programs/副業/projects/SNS/data/reply_insights_{date}.json
execution_time: 10-15分
priority: P1
model: claude-sonnet-4-5-20250929  # Sonnet 4.5 (2026年1月時点の最新モデル)
thinking: true
---

# Analyze Replies Skill - Phase 2-2

ツイート詳細からリプライを分析し、インサイトを抽出するスキル。

**Version**: 1.0

---

## このSkillでできること

1. **リプライ4カテゴリ分類**
   - 共感・期待: ポジティブな反応
   - 批判・懸念: ネガティブな反応、問題指摘
   - 追加情報・洞察: 新しい情報、深い考察
   - 質問: ユーザーの疑問、興味

2. **インサイト抽出**
   - 投稿作成に有用な洞察を日本語で要約
   - 支持するリプライテキストの保持
   - いいね数による重要度スコアリング

3. **エンゲージメント分析**
   - いいね数が多いリプライを優先分析
   - カテゴリ別分布の可視化

4. **統計情報生成**
   - 総ツイート分析数
   - 総インサイト抽出数
   - カテゴリ別インサイト数

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `tweet_details_{date}.json` (scrape-tweet-detailsスキルの出力) |
| **出力** | `reply_insights_{date}.json` (24インサイト、4カテゴリ) |
| **次のアクション** | generate-sns-postsスキルへの入力として使用 |

---

## Instructions

**実行モード**: 自律実行（LLM分析）
**推定所要時間**: 10-15分
**Thinking モード**: 有効（分析プロセスの可視化）

---

### STEP 1: 入力ファイル読み込み

**実行**: Read tool

**パス**: `Stock/programs/副業/projects/SNS/data/tweet_details_{date}.json`

**検証**:
- ファイル存在確認
- JSONフォーマット検証
- リプライデータ存在確認（最低10件以上）

**エラーハンドリング**:
- ファイル未検出 → **即時停止**、scrape-tweet-detailsスキルの再実行を促す
- JSONパースエラー → **即時停止**、ファイル破損報告
- リプライ不足（<10件） → **警告表示**、継続可能

---

### STEP 2: リプライ抽出とフィルタリング

**処理内容**:
1. 各ツイートからリプライ配列を抽出
2. リプライの前処理:
   - 空のリプライ除外
   - 短すぎるリプライ除外（<10文字）
   - スパムリプライ除外（URLのみ、絵文字のみ）
3. いいね数によるソート（降順）
4. Top 5-10リプライを選定（ツイートごと）

**期待出力**:
- 総リプライ数: 30-50件
- 分析対象リプライ: 20-40件（フィルタリング後）

---

### STEP 3: LLMによるリプライ分析

**実行**: LLM直接推論（ClaudeCode内蔵）

**プロンプト**:
```markdown
以下のリプライを分析し、4カテゴリに分類してインサイトを抽出してください。

ツイート内容:
{tweet_text}

リプライリスト（いいね数順）:
1. "{reply_text_1}" (いいね: {likes_1})
2. "{reply_text_2}" (いいね: {likes_2})
...

分類カテゴリ:
1. **共感・期待**: ポジティブな反応、賛同、期待表明
2. **批判・懸念**: ネガティブな反応、問題指摘、懸念表明
3. **追加情報・洞察**: 新しい情報提供、深い考察、専門的見解
4. **質問**: ユーザーの疑問、興味、追加情報要求

出力形式（JSON配列）:
[
  {
    "type": "共感・期待",
    "content": "NVIDIA CEOからの「extraordinary engineer」という評価は究極の検証。$3T企業トップの言葉は重みが違う",
    "supporting_reply": "When the CEO of a $3T company calls you an 'extraordinary engineer', that is the ultimate validation",
    "likes": 17
  },
  {
    "type": "批判・懸念",
    "content": "賞賛の量を控えてほしい。内容は正しくても、繰り返しの賞賛は過剰に感じる",
    "supporting_reply": "can you cut the praise in quantity, please",
    "likes": 9
  },
  ...
]

注意:
- contentは日本語で要約（投稿作成に有用な洞察）
- supporting_replyは原文をそのまま記録
- いいね数が多いリプライを優先的に抽出
- 各カテゴリ最低1件、最大3件のインサイトを抽出
```

**処理時間**: 5-10分（LLM推論、並列処理）

---

### STEP 4: インサイト統合と品質チェック

**処理内容**:
1. ツイートごとのインサイトを統合
2. 品質チェック:
   - 各カテゴリ最低1件のインサイトを確保
   - 重複インサイトの除外
   - いいね数0のインサイト除外（低品質）
3. トピック名の抽出:
   - ツイート本文から主要トピックを抽出
   - 日本語で簡潔に要約（15-30文字）

**期待出力**:
- 総インサイト数: 20-30件
- カテゴリ別分布:
  - 共感・期待: 5-10件
  - 批判・懸念: 3-7件
  - 追加情報・洞察: 5-10件
  - 質問: 2-5件

---

### STEP 5: 統計情報生成と出力

**処理内容**:
1. メタデータ生成:
   - 分析日時
   - 分析方法（ClaudeCode LLM direct analysis）
   - 総ツイート分析数
   - 総インサイト抽出数
2. ツイートIDごとのインサイト構造化

**出力形式**:
```json
{
  "metadata": {
    "analyzed_at": "2026-01-03T12:41:28.590494",
    "analysis_method": "ClaudeCode LLM direct analysis",
    "total_tweets_analyzed": 5,
    "total_insights_extracted": 24
  },
  "reply_insights": {
    "2006676783991787563": {
      "tweet_username": "cb_doge",
      "topic": "Optimusヒューマノイドロボット × NVIDIA Jensen Huang",
      "insights": [
        {
          "type": "共感・期待",
          "content": "NVIDIA CEOからの「extraordinary engineer」という評価は究極の検証。$3T企業トップの言葉は重みが違う",
          "supporting_reply": "When the CEO of a $3T company calls you an 'extraordinary engineer', that is the ultimate validation",
          "likes": 17
        },
        {
          "type": "批判・懸念",
          "content": "賞賛の量を控えてほしい。内容は正しくても、繰り返しの賞賛は過剰に感じる",
          "supporting_reply": "can you cut the praise in quantity, please",
          "likes": 9
        },
        ...
      ]
    },
    ...
  }
}
```

**パス**: `Stock/programs/副業/projects/SNS/data/reply_insights_{date}.json`

**実行**: Write tool

---

## エラーハンドリング

### 基本方針

| エラータイプ | 対応 | 理由 |
|------------|------|------|
| **入力ファイル未検出** | 即時停止 | 前段階の再実行が必要 |
| **リプライ不足（<10件）** | 警告表示 | 少数でも分析可能 |
| **LLM分析失敗** | リトライ1回 | 一時的なエラーの可能性 |
| **インサイト0件** | 即時停止 | 品質不足で後続処理不可 |

### リトライ戦略

- LLMタイムアウト: 1回リトライ
- JSON生成エラー: 1回リトライ（プロンプト調整）
- ネットワークエラー: 1回リトライ

参照: `.claude/skills/_shared/error_handling_patterns.md`

---

## 品質基準

- **総インサイト数**: 20件以上
- **カテゴリバランス**: 各カテゴリ最低2件以上
- **いいね数平均**: 5以上
- **処理時間**: 15分以内

---

## 使用例

```
User: /analyze-replies

Skill:
# リプライ分析開始

入力: Stock/programs/副業/projects/SNS/data/tweet_details_20260103.json

🔄 STEP 1: 入力ファイル読み込み中...
✅ 入力ファイル読み込み完了（5ツイート、40リプライ検出）

🔄 STEP 2: リプライ抽出とフィルタリング中...
✅ リプライ抽出完了（分析対象: 35件）

🔄 STEP 3: LLMによるリプライ分析中...
   - ツイート1/5: 「Optimusヒューマノイドロボット × NVIDIA Jensen Huang」分析中...
     ✅ 5件のインサイト抽出（共感2, 批判2, 追加情報1）
   - ツイート2/5: 「RAGの本質的問題 - 組織・インセンティブ」分析中...
     ✅ 4件のインサイト抽出（共感1, 批判1, 追加情報2）
   ...
✅ LLM分析完了（24件のインサイト抽出）

🔄 STEP 4: インサイト統合と品質チェック中...
✅ 品質チェック完了（重複0件除外、低品質1件除外）

🔄 STEP 5: 統計情報生成と出力中...
✅ 統計情報生成完了

---

# リプライ分析完了

出力: Stock/programs/副業/projects/SNS/data/reply_insights_20260103.json

統計:
- 総ツイート分析数: 5件
- 総インサイト抽出数: 24件
- カテゴリ別分布:
  - 共感・期待: 8件
  - 批判・懸念: 6件
  - 追加情報・洞察: 7件
  - 質問: 3件

次のアクション:
1. research-topicスキルを並列起動
2. generate-sns-postsスキルへの入力として使用
```

---

## Knowledge Base参照

- **LLM直接推論**: `.claude/rules/execution_preference.md`
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
