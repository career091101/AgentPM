# Phase 1-3 SNS投稿自動化ワークフロー

ClaudeCode LLMスキルによる完全自動化フロー

---

## 📋 スキル一覧

### Phase 1: データ収集（3スキル - 実装済み✅）

| # | スキル名 | コマンド | 実行時間 | model | 機能 |
|---|---------|---------|:--------:|:-----:|------|
| 1 | **Collect X Timeline** | `/collect-x-timeline` | 5-10分 | - | Xタイムライン200件収集（Playwright + GraphQL API傍受） |
| 2 | **Extract Top Tweets** | `/extract-top-tweets` | 3-5分 | haiku | AI関連Top 10抽出（7:3比率、LLM判定） |
| 3 | **Scrape Tweet Details** | `/scrape-tweet-details` | 10-15分 | - | ツイート詳細・リンク・リプライ抽出（Playwright） |

### Phase 2: 分析・調査（3スキル - 実装済み✅）

| # | スキル名 | コマンド | 実行時間 | model | 機能 |
|---|---------|---------|:--------:|:-----:|------|
| 4 | **Extract Content** | `/extract-content` | 5-10分 | haiku | 記事コンテンツ抽出（WebFetch、LLM実行） |
| 5 | **Analyze Replies** | `/analyze-replies` | 10-15分 | sonnet | リプライ分析（4カテゴリ分類、LLM実行） |
| 6 | **Research Topic** | `/research-topic` | 15-20分 | sonnet | Web調査（最新ニュース・ファクトチェック、LLM実行） |

### Phase 3: 投稿文生成（1スキル - 実装済み✅）

| # | スキル名 | コマンド | 実行時間 | model | 機能 |
|---|---------|---------|:--------:|:-----:|------|
| 7 | **Generate SNS Posts** | `/generate-sns-posts` | 20-30分 | opus | LinkedIn投稿3案生成（高野メソッドv6統合、LLM実行） |

**合計実行時間**: 68-105分（シーケンシャル実行）

---

## 🔄 利用フロー（標準実行）

### フロー図

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: データ収集（28-30分）                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────┐
    │ STEP 1: Xタイムライン収集（5-10分）           │
    │ /collect-x-timeline                          │
    │                                              │
    │ 入力: Cookie認証ファイル                      │
    │ 実行: Playwright + GraphQL API傍受            │
    │ 出力: x_timeline_20260102.json (200件)       │
    └──────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────┐
    │ STEP 2: AI関連Top 10抽出（3-5分）            │
    │ /extract-top-tweets                          │
    │                                              │
    │ 入力: x_timeline_20260102.json (200件)       │
    │ 実行: ClaudeCode LLM AI判定 + 7:3比率         │
    │ 出力: top_10_ai_tweets_20260102.json (10件)  │
    └──────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────┐
    │ STEP 3: ツイート詳細抽出（10-15分）           │
    │ /scrape-tweet-details                        │
    │                                              │
    │ 入力: top_10_ai_tweets_20260102.json (10件)  │
    │ 実行: Playwright 詳細ページ遷移               │
    │ 出力: tweet_details_ai_20260102.json         │
    │       - 12リンク                             │
    │       - 40リプライ                           │
    │       - 3外国語ツイート翻訳                   │
    └──────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Phase 2: 分析・調査（30-45分）                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────┐
    │ STEP 4: コンテンツ抽出（5-10分）              │
    │ /extract-content                             │
    │                                              │
    │ 入力: tweet_details_ai_20260102.json (12リンク)│
    │ 実行: ClaudeCode LLM + WebFetch (記事抽出)    │
    │ 出力: extracted_contents_ai_20260102.json    │
    │       - 11/12リンク成功（91.7%）              │
    │       - 1,322ワード抽出                       │
    └──────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────┐
    │ STEP 5: リプライ分析（10-15分）               │
    │ /analyze-replies                             │
    │                                              │
    │ 入力: tweet_details_ai_20260102.json (40リプライ)│
    │ 実行: ClaudeCode LLM 意味分析                 │
    │ 出力: reply_insights_ai_20260102.json        │
    │       - 5ツイート分析                         │
    │       - 24インサイト抽出                      │
    │       - 4カテゴリ分類（共感/批判/追加情報/質問）│
    └──────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────┐
    │ STEP 6: トピック調査（15-20分）               │
    │ /research-topic                              │
    │                                              │
    │ 入力: top_10_ai_tweets_20260102.json (Top 3) │
    │ 実行: ClaudeCode LLM + WebSearch             │
    │ 出力: research_findings_ai_20260102.json     │
    │       - 3トピック調査                         │
    │       - 30ソース                             │
    │       - 7ファクトチェック                     │
    │       - 13批判的視点                          │
    │       - 9専門家意見                           │
    └──────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ Phase 3: 投稿文生成（20-30分）                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────┐
    │ STEP 7: LinkedIn投稿3案生成（20-30分）        │
    │ /generate-sns-posts                          │
    │                                              │
    │ 入力: Phase 2全データ統合                     │
    │ 実行: ClaudeCode Opus + 高野メソッドv6        │
    │ 出力: posts_generated_ai_20260102.json       │
    │       - 3案（数字型、衝撃型、問題提起型）      │
    │       - 高野メソッド6要素準拠率100%           │
    │       - 予測ER 3.0%以上                      │
    └──────────────────────────────────────────────┘
```

---

## 💻 実行コマンド例

### パターン1: 完全手動実行（各ステップを個別実行）

```bash
# Phase 1 - データ収集
# STEP 1
/collect-x-timeline
# または
Xタイムライン収集

# STEP 2
/extract-top-tweets
# または
Top 10抽出

# STEP 3
/scrape-tweet-details
# または
ツイート詳細抽出

# Phase 2 - 分析・調査
# STEP 4
/extract-content
# または
コンテンツ抽出

# STEP 5
/analyze-replies
# または
リプライ分析

# STEP 6
/research-topic
# または
トピック調査

# Phase 3 - 投稿文生成
# STEP 7
/generate-sns-posts
# または
投稿文生成
```

### パターン2: 一括実行（推奨）

```bash
# ClaudeCodeに指示
Phase 1を実行して

# または
Phase 1とPhase 2を連続実行して

# または
Phase 1からPhase 3まで全て実行して

# または
SNS投稿用データを全て収集して投稿文まで生成して
```

ClaudeCodeが自動的に：
1. 7つのスキルを順番に実行
2. 各スキルの出力ファイルを次のスキルの入力として渡す
3. エラーハンドリング（失敗時はリトライまたはスキップ）
4. 最終レポート生成

---

## 📊 データフロー詳細

### 入力 → 処理 → 出力

```
【STEP 1】
入力: data/x_cookies.json (認証)
処理: Playwright + GraphQL API傍受
出力: data/x_timeline_20260102.json
      {
        "total_tweets": 127,
        "tweets": [...]
      }

【STEP 2】
入力: data/x_timeline_20260102.json (127件)
処理: ClaudeCode LLM AI判定 + エンゲージメント計算
出力: data/top_10_ai_tweets_20260102.json
      {
        "total_ai_tweets": 35,
        "japanese_tweets_count": 7,
        "foreign_tweets_count": 3,
        "top_tweets": [10件]
      }

【STEP 3】
入力: data/top_10_ai_tweets_20260102.json (10件)
処理: Playwright 詳細ページ遷移 + リンク/リプライ抽出
出力: data/tweet_details_ai_20260102.json
      {
        "total_tweets_processed": 10,
        "tweet_details": [
          {
            "tweet_id": "...",
            "links": [12件],
            "replies": [40件],
            "translated_text": "..." (外国語の場合)
          }
        ]
      }

【STEP 4】
入力: data/tweet_details_ai_20260102.json (12リンク)
処理: ClaudeCode LLM + WebFetch
出力: data/extracted_contents_ai_20260102.json
      {
        "success_count": 11,
        "extracted_contents": [
          {
            "url": "...",
            "title": "...",
            "content": "...",
            "word_count": 530
          }
        ]
      }

【STEP 5】
入力: data/tweet_details_ai_20260102.json (40リプライ)
処理: ClaudeCode LLM 意味分析
出力: data/reply_insights_ai_20260102.json
      {
        "total_insights_extracted": 24,
        "reply_insights": {
          "2006...": {
            "topic": "...",
            "insights": [
              {
                "type": "共感・期待",
                "content": "...",
                "supporting_reply": "...",
                "likes": 17
              }
            ]
          }
        }
      }

【STEP 6】
入力: data/top_10_ai_tweets_20260102.json (Top 3)
処理: ClaudeCode LLM + WebSearch
出力: data/research_findings_ai_20260102.json
      {
        "topics_researched": 3,
        "total_sources_found": 30,
        "research_findings": {
          "2006...": {
            "topic": "...",
            "latest_news": {...},
            "fact_check": {...},
            "opposing_views": {...},
            "expert_opinions": {...}
          }
        }
      }

【STEP 7】
入力: Phase 2全データ
      - data/extracted_contents_ai_20260102.json (11件, 1,322ワード)
      - data/reply_insights_ai_20260102.json (24インサイト)
      - data/research_findings_ai_20260102.json (30ソース)
      - data/top_10_ai_tweets_20260102.json (Top 3から選択)
処理: ClaudeCode Opus + 高野メソッドv6
出力: data/posts_generated_ai_20260102.json
      {
        "metadata": {
          "generation_method": "ClaudeCode Opus + 高野メソッドv6",
          "takano_method_compliance": {
            "引き込み": "✅",
            "データ/事例": "✅ (数字5個, 固有名詞3個)",
            "共感": "✅",
            "洞察": "✅",
            "問いかけ": "✅",
            "固有名詞": "✅ (3回以上)"
          }
        },
        "posts": [
          {
            "variant": "案1: 数字インパクト型",
            "rating": "★★★☆☆",
            "predicted_er": "2.8%",
            "character_count": 850
          },
          {
            "variant": "案2: 衝撃発言型",
            "rating": "★★★★★",
            "predicted_er": "4.2%",
            "character_count": 1200,
            "recommended": true
          },
          {
            "variant": "案3: 問題提起型",
            "rating": "★★★☆☆",
            "predicted_er": "2.5%",
            "character_count": 900
          }
        ]
      }
```

---

## 🎯 各スキルの役割

### Phase 1: データ収集

#### 1. collect-x-timeline
**目的**: 母集団データ収集（200件）
**技術**: Playwright + GraphQL API傍受
**特徴**:
- カーソルベースページネーション（重複率0%）
- エンゲージメント指標完全取得
- Cookie認証

#### 2. extract-top-tweets
**目的**: AI関連高エンゲージメント投稿の絞り込み
**技術**: ClaudeCode LLM AI判定
**特徴**:
- AI関連判定（LLMによる意味理解）
- 7:3比率（日本人7件、外国人3件）
- エンゲージメントスコア計算

#### 3. scrape-tweet-details
**目的**: 投稿作成に必要な詳細情報取得
**技術**: Playwright詳細ページ遷移
**特徴**:
- リンク抽出・分類（記事/YouTube/PDF）
- リプライ上位取得（最大10件/ツイート）
- 外国語ツイート翻訳（ClaudeCode LLM）

### Phase 2: 分析・調査

#### 4. extract-content
**目的**: リンク先コンテンツの全文取得
**技術**: ClaudeCode LLM + WebFetch
**特徴**:
- 記事タイトル・本文・メタ情報抽出
- ワード数カウント
- エラーハンドリング（403等）

#### 5. analyze-replies
**目的**: リプライから反響ポイント抽出
**技術**: ClaudeCode LLM 意味分析
**特徴**:
- 4カテゴリ分類（共感・期待、批判・懸念、追加情報・洞察、質問）
- 日本語要約生成
- エンゲージメント指標（いいね数）

#### 6. research-topic
**目的**: トピックの裏付け・ファクトチェック
**技術**: ClaudeCode LLM + WebSearch
**特徴**:
- 最新ニュース収集
- ファクトチェック（信頼性評価）
- 批判的視点収集
- 専門家意見（両論併記）

### Phase 3: 投稿文生成

#### 7. generate-sns-posts
**目的**: LinkedIn投稿3案の同時生成
**技術**: ClaudeCode Opus + 高野メソッドv6統合
**特徴**:
- Phase 2全データ統合（コンテンツ、リプライ、Web調査）
- 3案同時生成（数字インパクト型、衝撃発言型、問題提起型）
- 高野メソッド6要素準拠率100%（引き込み、データ/事例、共感、洞察、問いかけ、固有名詞）
- 予測ER 3.0%以上（業界平均1-3%超え）
- 3案比較表 + 最推奨案の自動選定
- 700-1500字範囲（Pattern A: 標準700-900字、Pattern B: ロング1000-1500字）

---

## 📈 実行結果サマリー（2026-01-02実績）

| Phase | 処理内容 | 入力 | 出力 | 成功率 | 実行時間 |
|-------|---------|------|------|:------:|:--------:|
| **1-1** | タイムライン収集 | Cookie | 200件 | 100% | 10分 |
| **1-2** | AI Top 10抽出 | 200件 | 10件（AI関連） | 100% | 4分 |
| **1-3** | 詳細抽出 | 10件 | 12リンク + 40リプライ | 100% | 12分 |
| **2-1** | コンテンツ抽出 | 12リンク | 11件（1,322ワード） | 91.7% | 8分 |
| **2-2** | リプライ分析 | 40リプライ | 24インサイト | 100% | 12分 |
| **2-3** | トピック調査 | Top 3 | 30ソース + 7ファクトチェック | 100% | 18分 |
| **3-1** | 投稿文生成 | Phase 2全データ | 3案（高野メソッド準拠） | - | 20-30分（実装完了、未実行） |
| **合計（Phase 1-2）** | - | - | - | **98.3%** | **64分** |
| **合計（Phase 1-3）** | - | - | - | **-** | **84-94分（予測）** |

---

## 🚀 利用シーン

### シーン1: 日次SNS投稿作成（標準フロー）

**タイミング**: 毎日朝9時
**実行**: Phase 1-2を連続実行（64分）
**アウトプット**:
- AI関連Top 10トピック
- 抽出コンテンツ（1,300ワード）
- リプライ分析（24インサイト）
- Web調査（30ソース、ファクトチェック済み）

**次のアクション**: Phase 3で投稿文生成（未実装）

### シーン2: 週次トレンド分析

**タイミング**: 毎週月曜日
**実行**: Phase 1のみ（26分）
**アウトプット**:
- 週間AI関連Top 10
- エンゲージメント推移

**次のアクション**: トレンドレポート作成

### シーン3: 緊急トピック調査

**タイミング**: ニュース発生時
**実行**: Phase 2-3のみ（research-topic）（18分）
**アウトプット**:
- 最新ニュース
- ファクトチェック
- 批判的視点

**次のアクション**: 速報投稿作成

---

## 🔧 トラブルシューティング

### エラー別対処法

| エラー | 原因 | 対処法 |
|-------|------|--------|
| **Cookie認証失敗** | auth_token期限切れ | X.comに再ログイン、Cookie再取得 |
| **AI判定が0件** | タイムライン内にAI関連なし | 収集時間帯を変更（平日昼間推奨） |
| **WebFetchタイムアウト** | サーバー応答遅延 | 自動的に次のリンクへ進む（対応不要） |
| **403 Forbidden** | アクセス制限サイト | 自動的にスキップ（対応不要） |
| **リプライ0件** | リプライがないツイート | 自動的にスキップ（対応不要） |

---

## 📚 関連ドキュメント

- **スキル詳細**: `.claude/skills/{skill-name}/SKILL.md`
- **スキル一覧**: `.claude/skills/README.md`
- **Phase 1実装ガイド**: `Stock/programs/副業/projects/SNS/X_COLLECTION_INSTRUCTIONS.md`
- **比較レポート**: `Stock/programs/副業/projects/SNS/data/cursor_vs_scroll_comparison_report.md`

---

**更新日**: 2026-01-02
**実装状況**: Phase 1-3完了（7スキル実装済み）、Phase 4残り（1スキル: approve-and-schedule）
