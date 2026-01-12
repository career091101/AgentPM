# Phase 2: 分析・調査 - 詳細手順

**所要時間**: 30-45分（逐次実行）

---

## 実行順序

以下の3スキルを**1→2→3の順序で逐次実行**

> **📋 逐次実行パターン（必須）**
>
> 以下の3つのTaskを**順番に1つずつ実行**すること。
> 各タスク完了後、次のタスクを開始。

---

## STEP 2.1: コンテンツ抽出（5-10分）

### 実行

```python
# Task 1: コンテンツ抽出（5-10分）
Task(
    description="コンテンツ抽出",
    subagent_type="general-purpose",
    model="haiku",
    prompt="""
    extract-contentスキルを実行してください。

    パラメータ:
    - 入力: Stock/programs/副業/projects/SNS/data/tweet_details_{date}.json （12リンク）
    - 出力: Stock/programs/副業/projects/SNS/data/extracted_contents_{date}.json
    - 処理内容:
      - 記事: WebFetch + LLMで本文・メタ情報取得
      - YouTube: 基本情報のみ（字幕抽出は今後実装）
      - PDF: メタ情報のみ（全文抽出は今後実装）

    エラー発生時は即座に停止し、エラー内容を報告してください。
    """
)
```

### 期待出力

`Stock/programs/副業/projects/SNS/data/extracted_contents_{date}.json` (約1,300ワード)

### 完了判定

ファイルが生成され、12リンク中8リンク以上が正常処理されている

---

## STEP 2.2: リプライ分析（10-15分）

### 注意

現時点でリプライデータが取得できない場合、このステップはスキップされます。

### 実行

```python
# Task 2: リプライ分析（10-15分）
Task(
    description="リプライ分析",
    subagent_type="general-purpose",
    model="sonnet",
    prompt="""
    analyze-repliesスキルを実行してください。

    パラメータ:
    - 入力: Stock/programs/副業/projects/SNS/data/tweet_details_{date}.json （40リプライ）
    - 出力: Stock/programs/副業/projects/SNS/data/reply_insights_{date}.json
    - 処理内容:
      - リプライ4カテゴリ分類: 共感・期待、批判・懸念、追加情報・洞察、質問
      - インサイト抽出: 各リプライから投稿作成に有用な洞察を日本語で要約
      - エンゲージメント重視: いいね数が多いリプライを優先分析

    リプライデータが存在しない場合は、スキップして次へ進んでください。
    """
)
```

### 期待出力

`Stock/programs/副業/projects/SNS/data/reply_insights_{date}.json` (24インサイト)

### 完了判定

- **リプライデータあり** → ファイルが生成されている
- **リプライデータなし** → スキップして次へ

---

## STEP 2.3: Web調査（15-20分）

### 実行

```python
# Task 3: Web調査（15-20分）
Task(
    description="Web調査",
    subagent_type="general-purpose",
    model="sonnet",
    prompt="""
    research-topicスキルを実行してください。

    パラメータ:
    - 入力: Stock/programs/副業/projects/SNS/data/top_10_tweets_{date}.json （Top 3トピック）
    - 出力: Stock/programs/副業/projects/SNS/data/research_findings_{date}.json
    - 処理内容:
      - 最新ニュース収集（WebSearch）
      - ファクトチェック実行（数値・主張・予測の信頼性検証）
      - 批判的視点収集（専門家の懐疑的意見・限界点）
      - 専門家意見収集（支持派・懐疑派両論）

    エラー発生時は即座に停止し、エラー内容を報告してください。
    """
)
```

### 期待出力

`Stock/programs/副業/projects/SNS/data/research_findings_{date}.json` (30ソース、7ファクトチェック)

### 完了判定

ファイルが生成され、Top 3トピック中2トピック以上で調査完了

---

## Phase 2完了判定

### 必須条件

- **STEP 2.1（コンテンツ抽出）成功必須**
- **STEP 2.2（リプライ分析）**: データなし時はスキップ可
- **STEP 2.3（Web調査）成功必須**

### 期待される成果物

1. `extracted_contents_{date}.json` - 記事・YouTube・PDF等から抽出したコンテンツ
2. `reply_insights_{date}.json` - リプライから抽出したインサイト（データなし時は生成されない）
3. `research_findings_{date}.json` - Web調査結果、ファクトチェック、専門家意見

**総実行時間**: 30-45分（逐次実行）

---

## エラーハンドリング

### 基本方針

| ステップ | エラー時の対応 | 理由 |
|---------|-----------|------|
| **STEP 2.1** | **即時停止** | 後続処理が依存するため必須 |
| **STEP 2.2** | データなし時はスキップ可 | オプショナル |
| **STEP 2.3** | **即時停止** | Web調査結果は投稿品質を大きく左右 |

### 詳細なエラーハンドリング

リトライ戦略、エラーレスポンス形式、パターン別対応は以下を参照：

📖 **[@_shared/error_handling_patterns.md](../../_shared/error_handling_patterns.md)**
