---
name: generate-sns-posts
description: |
  マルチプラットフォーム投稿コンテンツ生成スキル。
  Phase 2データを統合し、LinkedIn/X/Facebook/Threads向けの投稿3案を生成。

  処理内容:
  - トピック選定（Top 3から対話選択）
  - 統合コンテキスト作成（Phase 2全データ）
  - 3案同時生成（数字型・衝撃型・問題提起型）
  - 比較表・最推奨案提示
  - 高野メソッドv6準拠チェック

  所要時間: 20-30分
  出力: posts_generated_{date}.json

trigger_keywords:
  - "投稿生成"
  - "generate-sns-posts"
  - "SNS投稿作成"

stage: Phase 3-1
dependencies:
  - extract-content (extracted_contents_{date}.json)
  - analyze-replies (reply_insights_{date}.json)
  - research-topic (research_findings_{date}.json)
  - extract-top-tweets (top_10_tweets_{date}.json)

output_file: Stock/programs/副業/projects/SNS/data/posts_generated_{date}.json
execution_time: 20-30分
priority: P0
model: claude-opus-4-5-20251101  # Opus 4.5 (2026年1月時点の最新モデル)
thinking: true
---

# Generate SNS Posts Skill - Phase 3-1

マルチプラットフォーム投稿コンテンツ生成スキル。

**Version**: 1.0

---

## このSkillでできること

1. **トピック選定（対話式）**
   - Top 3トピックから選択
   - エンゲージメント予測提示
   - トピックの新規性・調査可能性評価

2. **統合コンテキスト作成**
   - Phase 2全データ統合（1,300ワード + 24インサイト + 30ソース）
   - トランスクリプト変換（LLM処理用）
   - 高野メソッドv6準拠チェック

3. **3案同時生成**
   - 案1: 数字インパクト型
   - 案2: 衝撃発言型
   - 案3: 問題提起型

4. **比較表・推奨案提示**
   - 7項目比較（文字数、フック効果、データ密度等）
   - 予測ER（エンゲージメント率）算出
   - 投稿ティップス提供

5. **プラットフォーム別最適化**
   - LinkedIn: 1,150-1,300文字、プロフェッショナルトーン
   - X/Twitter: 280文字制限、スレッド対応
   - Facebook: 長文OK、カジュアルトーン
   - Threads: 500文字制限、カジュアルトーン

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | Phase 2全データ（extracted_contents, reply_insights, research_findings, top_10_tweets） |
| **出力** | `posts_generated_{date}.json` (3案 + 比較表 + 推奨案) |
| **次のアクション** | approve-and-scheduleスキルへの入力として使用 |

---

## Instructions

**実行モード**: 対話式自律実行（トピック選定のみユーザー選択）
**推定所要時間**: 20-30分
**Thinking モード**: 有効（生成プロセスの可視化）

---

### STEP 1: Phase 2データ読み込み

**実行**: Read tool（4ファイル並列読み込み）

**パス**:
1. `Stock/programs/副業/projects/SNS/data/extracted_contents_{date}.json`
2. `Stock/programs/副業/projects/SNS/data/reply_insights_{date}.json`
3. `Stock/programs/副業/projects/SNS/data/research_findings_{date}.json`
4. `Stock/programs/副業/projects/SNS/data/top_10_tweets_{date}.json`

**検証**:
- 4ファイル全て存在確認
- JSONフォーマット検証
- データ品質確認（最低基準: 1,000ワード、20インサイト、25ソース）

**エラーハンドリング**:
- ファイル未検出 → **即時停止**、Phase 2の再実行を促す
- データ不足 → **警告表示**、継続可能（品質低下の可能性）

---

### STEP 2: トピック選定（対話式）

**実行**: AskUserQuestion tool

**プロンプト**:
```markdown
Phase 2で収集したTop 10ツイートから、以下の3つのトピックを抽出しました。

投稿文を生成するトピックを選んでください：

1. **Tesla Optimus × NVIDIA Jensen Huang** (推奨★★★★★)
   - エンゲージメント: 7,479（いいね4,114, RT655, リプライ280）
   - 予測ER: 4-5%
   - 新規性: ★★★★★（2026年最新予測）
   - 調査可能性: ★★★★★（30ソース収集済み）

2. **RAGの本質的問題 - 組織・インセンティブ** (推奨★★★☆☆)
   - エンゲージメント: 3,245（いいね2,100, RT450, リプライ120）
   - 予測ER: 3-4%
   - 新規性: ★★★★☆（技術的洞察）
   - 調査可能性: ★★★☆☆（20ソース収集済み）

3. **LLM新モデル発表** (推奨★★★☆☆)
   - エンゲージメント: 2,890（いいね1,800, RT390, リプライ95）
   - 予測ER: 2-3%
   - 新規性: ★★★☆☆（定期発表）
   - 調査可能性: ★★★★☆（25ソース収集済み）

選択してください: [1/2/3]
```

**ユーザー入力待機**: 1, 2, または 3

**期待出力**: 選択されたトピックID

---

### STEP 3: 統合コンテキスト作成

**処理内容**:
1. **Phase 2データ統合**:
   - extracted_contents: 約1,300ワード
   - reply_insights: 24インサイト
   - research_findings: 30ソース、7ファクトチェック
   - top_10_tweets: 選択されたトピックの元ツイート

2. **トランスクリプト変換**:
   - LLM処理用にマークダウン形式に変換
   - 階層構造化（見出し、箇条書き）
   - 重要情報のハイライト

3. **高野メソッドv6準拠チェック**:
   - 引き込み: 冒頭の衝撃性
   - データ/事例: 数値・具体例
   - 共感: 読者の感情共鳴
   - 洞察: 新しい視点
   - アドバイス: 実行可能な助言
   - 問いかけ: 行動喚起
   - 固有名詞: 権威性・信頼性

**期待出力**:
```markdown
# 統合コンテキスト: Tesla Optimus × NVIDIA Jensen Huang

## 元ツイート情報
- ユーザー: @cb_doge
- エンゲージメント: いいね4,114, RT655, リプライ280
- 本文: [ツイート本文]

## 記事コンテンツ（1,322ワード）
### 主要ソース
1. Fortune 2025: "NVIDIA CEO Jensen Huang predicts..."
2. MIT Tech Review: "Humanoid robots face technical challenges..."
...

## リプライ分析（24インサイト）
### 共感・期待（8件）
- "NVIDIA CEOからの評価は究極の検証"
...

### 批判・懸念（6件）
- "賞賛の量を控えてほしい"
...

## Web調査（30ソース）
### 最新ニュース
- Jensen HuangがElon Muskを「extraordinary engineer」と評価
...

### ファクトチェック（7件）
- 生産目標100万台: 未検証（2025年実績は数百台）
...

### 批判的視点（13件）
- Rodney Brooks: "万能アシスタントは純粋なファンタジー"
...

### 専門家意見（9件）
- 支持派: Jensen Huang, Elon Musk
- 懐疑派: Rodney Brooks, Gary Marcus
```

---

### STEP 4: 3案同時生成（LLM）

**実行**: LLM直接推論（Opus、Thinking モード有効）

**プロンプト**:
```markdown
以下の統合コンテキストを基に、LinkedIn投稿3案を生成してください。

【統合コンテキスト】
{統合コンテキスト全文}

【生成条件】
1. **高野メソッドv6準拠**: 7要素すべて必須
   - 引き込み、データ/事例、共感、洞察、アドバイス、問いかけ、固有名詞

2. **ターゲット**: 経営者・起業家（特に製造業・技術系）

3. **文字数**: 800-1,300文字（LinkedIn最適範囲）

4. **3つのバリエーション**:
   - **案1: 数字インパクト型**
     - 冒頭に数字3つ以上配置
     - データ密度最大化
     - 客観性重視

   - **案2: 衝撃発言型**
     - 権威者の発言を引用
     - 感情喚起最大化
     - カジュアルトーン併用

   - **案3: 問題提起型**
     - 「なぜ〜ないのか？」形式
     - 課題を明確化
     - 解決策提示

5. **必須要素**:
   - 支持派と懐疑派の両論併記
   - ファクトチェック結果の反映
   - 具体的アクション3つ提示
   - 問いかけで締めくくり

6. **予測ER算出**:
   - フック効果、データ密度、感情喚起等を総合評価
   - LinkedIn業界平均2-3%を基準とした予測

【出力形式（JSON）】
{
  "variant": "案1: 数字インパクト型",
  "rating": "★★★★☆",
  "predicted_er": "3.2%",
  "character_count": 892,
  "content": "[投稿本文]",
  "hook_strategy": "[フック戦略の説明]",
  "recommended": false
}
```

**処理時間**: 15-20分（Opus、3案同時生成）

**期待出力**:
- 3案の投稿本文（JSON配列）
- 各案の評価（rating、predicted_er、hook_strategy）
- 推奨フラグ（recommended）

---

### STEP 5: 比較表生成

**実行**: LLM直接推論

**プロンプト**:
```markdown
以下の3案を7項目で比較評価してください。

【3案】
{案1, 案2, 案3のJSONデータ}

【比較項目】
1. 文字数
2. フック効果（★1-5）
3. データ密度（★1-5）
4. 感情喚起（★1-5）
5. 権威性活用（★1-5）
6. 行動喚起（★1-5）
7. 予測ER
8. ターゲット適合性

【出力形式（JSON）】
{
  "headers": ["項目", "案1（数字型）", "案2（衝撃型）", "案3（問題提起型）"],
  "rows": [
    ["文字数", "892字", "1,247字", "923字"],
    ["フック効果", "★★★★☆", "★★★★★", "★★★☆☆"],
    ...
  ]
}
```

**処理時間**: 2-3分

---

### STEP 6: 最推奨案選定と理由説明

**実行**: LLM直接推論

**プロンプト**:
```markdown
3案の中から最推奨案を選定し、理由を説明してください。

【選定基準】
1. 予測ER（最重要）
2. 高野メソッド準拠度
3. ターゲット適合性
4. データ活用度
5. 行動喚起力

【出力形式（JSON）】
{
  "best_variant": "案2: 衝撃発言型",
  "reasons": [
    "フック効果: Jensen Huang氏の発言を最大活用",
    "権威性活用: $3兆企業CEOの発言は最高レベル",
    ...
  ],
  "posting_tips": [
    "投稿時間: 火曜〜木曜の朝7:30-8:30または昼12:00-13:00が最適",
    "初動対応: 投稿後30分以内のコメントには必ず返信",
    ...
  ]
}
```

**処理時間**: 2-3分

---

### STEP 7: 出力ファイル生成

**処理内容**:
1. メタデータ生成:
   - トピック選定情報
   - 生成方法（ClaudeCode Opus + 高野メソッドv6）
   - 生成日時
   - 元ツイートエンゲージメント
   - 高野メソッド準拠チェック結果

2. 統合JSON生成:
   - metadata
   - posts（3案配列）
   - comparison_table
   - recommendation

**出力形式**:
```json
{
  "metadata": {
    "topic_selected": "Tesla Optimus × NVIDIA Jensen Huang - ヒューマノイドロボットの未来",
    "generation_method": "ClaudeCode Opus + 高野メソッドv6",
    "generated_at": "2026-01-03T09:00:00+09:00",
    "source_tweet_engagement": {
      "likes": 4114,
      "retweets": 655,
      "replies": 280,
      "total": 7479
    },
    "takano_method_compliance": {
      "引き込み": "✅",
      "データ/事例": "✅",
      "共感": "✅",
      "洞察": "✅",
      "アドバイス": "✅",
      "問いかけ": "✅",
      "固有名詞": "✅"
    }
  },
  "posts": [
    { "variant": "案1: 数字インパクト型", ... },
    { "variant": "案2: 衝撃発言型", ... },
    { "variant": "案3: 問題提起型", ... }
  ],
  "comparison_table": { ... },
  "recommendation": { ... }
}
```

**パス**: `Stock/programs/副業/projects/SNS/data/posts_generated_{date}.json`

**実行**: Write tool

---

## エラーハンドリング

### 基本方針

| エラータイプ | 対応 | 理由 |
|------------|------|------|
| **Phase 2データ不足** | 即時停止 | 品質担保のため必須 |
| **トピック選定タイムアウト** | デフォルト選択（トピック1） | 自動継続 |
| **LLM生成失敗** | リトライ1回 | 一時的なエラーの可能性 |
| **高野メソッド未達** | 警告表示 | 継続可能（品質低下） |

### リトライ戦略

- LLMタイムアウト: 1回リトライ
- JSON生成エラー: 1回リトライ（プロンプト調整）
- 品質基準未達: 再生成1回

参照: `.claude/skills/_shared/error_handling_patterns.md`

---

## 品質基準

- **高野メソッド準拠**: 7要素すべて達成
- **予測ER**: 最推奨案で3.5%以上
- **文字数**: 800-1,300文字（LinkedIn最適）
- **処理時間**: 30分以内

---

## プラットフォーム別最適化（将来拡張）

| プラットフォーム | 文字数制限 | トーン | 特徴 |
|----------------|----------|--------|------|
| **LinkedIn** | 1,150-1,300 | Professional | データ重視、高野メソッド |
| **X/Twitter** | 280/ツイート | Casual | スレッド対応、数字インパクト |
| **Facebook** | 制限なし | Casual | 長文OK、画像推奨 |
| **Threads** | 500 | Casual | スレッド対応、親しみやすさ |

---

## 使用例

```
User: /generate-sns-posts

Skill:
# 投稿生成開始

🔄 STEP 1: Phase 2データ読み込み中...
✅ Phase 2データ読み込み完了
   - extracted_contents: 1,322ワード
   - reply_insights: 24インサイト
   - research_findings: 30ソース
   - top_10_tweets: 10ツイート

🔄 STEP 2: トピック選定中...

以下の3つのトピックから選んでください：

1. Tesla Optimus × NVIDIA Jensen Huang (推奨★★★★★)
2. RAGの本質的問題 (推奨★★★☆☆)
3. LLM新モデル発表 (推奨★★★☆☆)

選択: [ユーザー入力: 1]

✅ トピック選定完了: Tesla Optimus × NVIDIA Jensen Huang

🔄 STEP 3: 統合コンテキスト作成中...
✅ 統合コンテキスト作成完了（2,500ワード相当）

🔄 STEP 4: 3案同時生成中...（Opus、Thinking モード）
   - 案1: 数字インパクト型生成中...
   - 案2: 衝撃発言型生成中...
   - 案3: 問題提起型生成中...
✅ 3案生成完了（総文字数: 3,062字）

🔄 STEP 5: 比較表生成中...
✅ 比較表生成完了（7項目比較）

🔄 STEP 6: 最推奨案選定中...
✅ 最推奨案選定完了: 案2（衝撃発言型）

🔄 STEP 7: 出力ファイル生成中...
✅ 出力ファイル生成完了

---

# 投稿生成完了

出力: Stock/programs/副業/projects/SNS/data/posts_generated_20260103.json

統計:
- 生成案数: 3案
- 総文字数: 3,062字
- 最推奨案: 案2（衝撃発言型）
- 予測ER: 4.5%
- 高野メソッド準拠: 7要素すべて達成

次のアクション:
1. approve-and-scheduleスキルでSlack承認
2. 承認後、Late API経由で自動投稿
```

---

## Knowledge Base参照

- **LLM直接推論**: `.claude/rules/execution_preference.md`
- **高野メソッドv6**: `.claude/skills/_shared/knowledge_base.md`
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`
- **Phase 3全体フロー**: `.claude/skills/sns-automation/SKILL.md`

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-03 | 1.0 | 初版作成 |

---

**実装日**: 2026-01-03
**バージョン**: 1.0
