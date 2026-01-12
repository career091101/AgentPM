---
name: research-topic
description: |
  トピックリサーチと知見抽出を行うスキル。
  最新ニュース、ファクトチェック、批判的視点、専門家意見を収集。

  処理内容:
  - WebSearch による最新情報収集
  - ファクトチェック実行（数値・主張・予測の信頼性検証）
  - 批判的視点収集（専門家の懐疑的意見・限界点）
  - 専門家意見収集（支持派・懐疑派両論）

  所要時間: 15-20分
  出力: research_findings_{date}.json

trigger_keywords:
  - "トピックリサーチ"
  - "research-topic"
  - "Web調査"

stage: Phase 2-3
dependencies:
  - extract-top-tweets (top_10_tweets_{date}.json)

output_file: Stock/programs/副業/projects/SNS/data/research_findings_{date}.json
execution_time: 15-20分
priority: P1
model: claude-sonnet-4-5-20250929  # Sonnet 4.5 (2026年1月時点の最新モデル)
thinking: true
---

# Research Topic Skill - Phase 2-3

トピックリサーチと知見抽出を行うスキル。

**Version**: 1.0

---

## このSkillでできること

1. **最新ニュース収集**
   - WebSearch tool使用
   - 信頼性の高いソース優先
   - 発表日・著者情報の記録

2. **ファクトチェック**
   - 数値データの検証
   - 主張の信頼性評価
   - 予測の根拠確認

3. **批判的視点収集**
   - 専門家の懐疑的意見
   - 技術的限界点
   - リスク・課題の指摘

4. **専門家意見収集**
   - 支持派意見（ポジティブ）
   - 懐疑派意見（ネガティブ）
   - 両論併記の実現

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `top_10_tweets_{date}.json` (extract-top-tweetsスキルの出力) |
| **出力** | `research_findings_{date}.json` (30ソース、7ファクトチェック) |
| **次のアクション** | generate-sns-postsスキルへの入力として使用 |

---

## Instructions

**実行モード**: 自律実行（WebSearch + LLM分析）
**推定所要時間**: 15-20分
**Thinking モード**: 有効（リサーチプロセスの可視化）

---

### STEP 1: 入力ファイル読み込み

**実行**: Read tool

**パス**: `Stock/programs/副業/projects/SNS/data/top_10_tweets_{date}.json`

**検証**:
- ファイル存在確認
- JSONフォーマット検証
- ツイートデータ存在確認（最低3件以上）

**エラーハンドリング**:
- ファイル未検出 → **即時停止**、extract-top-tweetsスキルの再実行を促す
- JSONパースエラー → **即時停止**、ファイル破損報告
- ツイート不足（<3件） → **警告表示**、継続可能

---

### STEP 2: リサーチトピック選定

**処理内容**:
1. Top 10ツイートからトピックを抽出
2. トピックの重要度スコアリング:
   - エンゲージメントスコア（高い順）
   - トピックの新規性（最新トレンド優先）
   - 調査可能性（Web上の情報量）
3. Top 3トピックを選定

**期待出力**:
- リサーチ対象トピック: 3件
- 各トピックのキーワード抽出（検索クエリ用）

**例**:
```
トピック1: Tesla Optimus × NVIDIA Jensen Huang
キーワード: "Tesla Optimus 2026", "NVIDIA Jensen Huang robot", "humanoid robot market"

トピック2: RAGの本質的問題 - 組織・インセンティブ
キーワード: "RAG limitations 2026", "RAG vs fine-tuning", "enterprise RAG challenges"

トピック3: LLM新モデル発表
キーワード: "LLM models 2026", "Claude 4.5", "GPT-5 news"
```

---

### STEP 3: 最新ニュース収集

**実行**: WebSearch tool（トピックごとに並列実行）

**プロンプト**:
```markdown
以下のトピックについて、2025年12月〜2026年1月の最新ニュースを検索してください:

トピック: {topic}
検索クエリ: {keywords}

検索条件:
- 時期: 2025年12月〜2026年1月
- 言語: 英語優先、日本語も含む
- ソース優先度: 公式発表 > ニュースメディア > 専門家ブログ > SNS

出力項目:
1. 見出し（Headline）
2. 要約（Summary、100-200文字）
3. 発表日（Published Date）
4. ソースURL
5. 信頼性スコア（High/Medium/Low）

期待ソース数: 8-12件/トピック
```

**処理時間**: 5-8分（3トピック並列）

**エラーハンドリング**:
- WebSearch失敗 → **リトライ1回**
- ソース不足（<5件） → **警告表示**、継続可能

---

### STEP 4: ファクトチェック実行

**実行**: LLM直接推論 + WebSearch補助

**プロンプト**:
```markdown
以下のトピックに関する主張・数値・予測をファクトチェックしてください:

トピック: {topic}
収集ニュース: {news_summaries}

ファクトチェック項目:
1. **数値データの検証**:
   - 主張された数値が正確か
   - 出典が明確か
   - 複数ソースで確認できるか

2. **主張の信頼性評価**:
   - 公式発表か、噂か
   - 独立報道機関の検証があるか
   - 利益相反の可能性

3. **予測の根拠確認**:
   - 楽観的すぎないか
   - 過去の実績との整合性
   - 専門家のコンセンサスがあるか

出力形式（JSON）:
{
  "claim_1": {
    "claim": "2026年末までに年間100万台の生産体制",
    "verification": "未検証 - Muskの公約だが、独立報道によれば2025年の生産実績は数百台レベル",
    "reliability": "低 - Muskの楽観的予測は戦略的目的で使われることが多い"
  },
  "claim_2": {
    "claim": "価格目標 $20,000-$30,000",
    "verification": "未実証 - 大量生産時のコスト曲線が未確定",
    "reliability": "中 - 目標値であり確定価格ではない"
  }
}

期待ファクトチェック数: 2-3件/トピック
```

**処理時間**: 3-5分（LLM推論）

---

### STEP 5: 批判的視点収集

**実行**: WebSearch tool + LLM分析

**プロンプト**:
```markdown
以下のトピックに関する批判的視点・懐疑的意見を収集してください:

トピック: {topic}
検索クエリ: "{topic} criticism", "{topic} limitations", "{topic} risks"

収集項目:
1. **技術的限界点**:
   - 現在の技術では達成困難な部分
   - 未解決の課題

2. **専門家の懐疑的意見**:
   - 懐疑派の主張
   - リスク指摘
   - 過去の失敗事例との比較

3. **市場・ビジネス上の課題**:
   - 収益化の困難性
   - 競合との比較
   - 規制リスク

出力形式（JSON配列）:
[
  {
    "criticism": "技術的実現性への疑問 - 自律性・安全性の未確立",
    "source": "MIT Tech Review 2025",
    "category": "技術的限界"
  },
  {
    "criticism": "投資家の懸念 - 収益化モデルが不透明",
    "source": "Bloomberg 2026",
    "category": "ビジネス上の課題"
  }
]

期待批判数: 3-5件/トピック
```

**処理時間**: 5-7分（WebSearch + LLM）

---

### STEP 6: 専門家意見収集

**実行**: WebSearch tool + LLM分析

**プロンプト**:
```markdown
以下のトピックに関する専門家意見を収集してください（支持派・懐疑派両論）:

トピック: {topic}
検索クエリ: "{topic} expert opinion", "{topic} analysis", "{topic} future"

収集項目:
1. **支持派意見（ポジティブ）**:
   - 技術的可能性の評価
   - 市場ポテンシャル
   - 社会的インパクト

2. **懐疑派意見（ネガティブ）**:
   - リスク評価
   - 実現可能性への疑問
   - 過大評価の指摘

出力形式（JSON）:
{
  "supportive_experts": [
    {
      "expert": "Jensen Huang (NVIDIA CEO)",
      "opinion": "ロボティクスの10年 - 5年以内に工場でのヒューマノイドロボット標準化",
      "source": "Fortune 2025"
    }
  ],
  "skeptical_experts": [
    {
      "expert": "Rodney Brooks (Robotics Pioneer)",
      "opinion": "楽観的すぎる予測 - ロボット普及は段階的で時間がかかる",
      "source": "MIT Tech Review 2025"
    }
  ]
}

期待専門家意見数: 2-4件/トピック（支持派・懐疑派合計）
```

**処理時間**: 5-7分（WebSearch + LLM）

---

### STEP 7: 統計情報生成と出力

**処理内容**:
1. メタデータ生成:
   - リサーチ日時
   - リサーチ方法（ClaudeCode WebSearch + LLM analysis）
   - 総トピック数
   - 高優先度トピック数
   - リサーチ完了率
2. リサーチカテゴリ別統計:
   - 総ソース数
   - ファクトチェック実施数
   - 批判的視点特定数
   - 専門家意見収集数

**出力形式**:
```json
{
  "metadata": {
    "researched_at": "2026-01-03T12:51:35.000000",
    "research_method": "ClaudeCode WebSearch + LLM analysis",
    "total_topics": 10,
    "high_priority_count": 3,
    "topics_researched": 3,
    "research_completion_rate": "100% (3/3 high-priority topics)",
    "research_categories": [
      "latest_news",
      "fact_check",
      "opposing_views",
      "expert_opinions"
    ],
    "research_summary": {
      "total_sources_found": 30,
      "fact_checks_performed": 7,
      "criticisms_identified": 13,
      "expert_opinions_collected": 9
    }
  },
  "research_findings": {
    "2006676783991787563": {
      "tweet_username": "cb_doge",
      "topic": "Tesla Optimus × NVIDIA Jensen Huang - ヒューマノイドロボットの未来",
      "latest_news": {
        "summary": "...",
        "key_developments": [...],
        "sources": [...]
      },
      "fact_check": {
        "claim_1": {...},
        "claim_2": {...}
      },
      "opposing_views": {
        "criticisms": [...]
      },
      "expert_opinions": {
        "supportive_experts": [...],
        "skeptical_experts": [...]
      }
    },
    ...
  }
}
```

**パス**: `Stock/programs/副業/projects/SNS/data/research_findings_{date}.json`

**実行**: Write tool

---

## エラーハンドリング

### 基本方針

| エラータイプ | 対応 | 理由 |
|------------|------|------|
| **入力ファイル未検出** | 即時停止 | 前段階の再実行が必要 |
| **WebSearch失敗** | リトライ1回 | ネットワーク一時的エラーの可能性 |
| **ソース不足（<5件）** | 警告表示 | 少数でもリサーチ可能 |
| **LLM分析失敗** | リトライ1回 | 一時的なエラーの可能性 |
| **全トピックリサーチ失敗** | 即時停止 | データ不足で後続処理不可 |

### リトライ戦略

- WebSearchタイムアウト: 1回リトライ
- LLMタイムアウト: 1回リトライ
- JSON生成エラー: 1回リトライ（プロンプト調整）

参照: `.claude/skills/_shared/error_handling_patterns.md`

---

## 品質基準

- **総ソース数**: 25件以上（3トピック合計）
- **ファクトチェック**: 6件以上（3トピック合計）
- **批判的視点**: 9件以上（3トピック合計）
- **専門家意見**: 6件以上（3トピック合計）
- **処理時間**: 20分以内

---

## 使用例

```
User: /research-topic

Skill:
# トピックリサーチ開始

入力: Stock/programs/副業/projects/SNS/data/top_10_tweets_20260103.json

🔄 STEP 1: 入力ファイル読み込み中...
✅ 入力ファイル読み込み完了（10ツイート検出）

🔄 STEP 2: リサーチトピック選定中...
✅ Top 3トピック選定完了:
   1. Tesla Optimus × NVIDIA Jensen Huang
   2. RAGの本質的問題 - 組織・インセンティブ
   3. LLM新モデル発表

🔄 STEP 3: 最新ニュース収集中...（並列実行）
   - トピック1: 10件のソース収集
   - トピック2: 8件のソース収集
   - トピック3: 12件のソース収集
✅ 最新ニュース収集完了（30ソース）

🔄 STEP 4: ファクトチェック実行中...
   - トピック1: 2件のファクトチェック実施
   - トピック2: 3件のファクトチェック実施
   - トピック3: 2件のファクトチェック実施
✅ ファクトチェック完了（7件）

🔄 STEP 5: 批判的視点収集中...
   - トピック1: 5件の批判収集
   - トピック2: 4件の批判収集
   - トピック3: 4件の批判収集
✅ 批判的視点収集完了（13件）

🔄 STEP 6: 専門家意見収集中...
   - トピック1: 支持派2件、懐疑派2件
   - トピック2: 支持派1件、懐疑派2件
   - トピック3: 支持派1件、懐疑派1件
✅ 専門家意見収集完了（9件）

🔄 STEP 7: 統計情報生成と出力中...
✅ 統計情報生成完了

---

# トピックリサーチ完了

出力: Stock/programs/副業/projects/SNS/data/research_findings_20260103.json

統計:
- 総トピック数: 10件
- リサーチ対象: 3件（高優先度）
- 総ソース数: 30件
- ファクトチェック: 7件
- 批判的視点: 13件
- 専門家意見: 9件

次のアクション:
1. generate-sns-postsスキルへの入力として使用
```

---

## Knowledge Base参照

- **WebSearch tool使用例**: `.claude/rules/execution_preference.md`
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
