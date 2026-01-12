---
name: research-topic
description: |
  Top 10ツイートのトピックをWeb調査し、最新ニュース、ファクトチェック、専門家意見を収集するスキル。
  ClaudeCode LLMが直接WebSearchツールを使用して情報を収集・分析します。
  調査量は従来の2倍、専門家意見を重点的に収集します。

  使用タイミング：
  - SNS投稿作成前のファクトチェックが必要な時
  - トピックの最新動向を把握したい時
  - 専門家の多様な意見を収集したい時

  所要時間：25-35分
  出力：research_findings_ai_{YYYYMMDD}.json
trigger_keywords:
  - "トピック調査"
  - "Web調査"
  - "research topic"
  - "ファクトチェック"
  - "専門家意見"
stage: Phase 2 - Topic Research
dependencies: ["extract-top-tweets"]
output_file: Stock/programs/副業/projects/SNS/data/research_findings_ai_{YYYYMMDD}.json
execution_time: 25-35分
framework_reference: Stock/programs/副業/projects/SNS/
priority: P1
model: claude-sonnet-4-5-20250929  # Sonnet 4.5 (2026年1月時点の最新モデル)
thinking: true
---

# Research Topic Skill

Top 10ツイートのトピックをWeb調査し、最新ニュース・ファクトチェック・専門家意見を収集するスキル。
**調査量2倍**、**専門家意見重点収集**バージョン。

---

## このSkillでできること

1. **最新ニュース収集（2倍量）**: WebSearchで2026年の最新情報を複数クエリで網羅的に検索
2. **ファクトチェック実行（2倍量）**: 数値・主張・予測の信頼性を複数ソースで検証
3. **専門家意見収集（大幅拡充）**: 6-8名の専門家意見を収集（業界リーダー、研究者、アナリスト、実務家）
4. **構造化レポート生成**: 3カテゴリ（最新ニュース、ファクトチェック、専門家意見）で整理

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | top_10_ai_tweets_{YYYYMMDD}.json（AI関連Top 10） |
| **出力** | research_findings_ai_{YYYYMMDD}.json（調査レポート） |
| **次のアクション** | generate-sns-posts（投稿生成） |

---

## Instructions

**実行モード**: ClaudeCode LLM自律実行（思考モード有効）
**推定所要時間**: 25-35分（従来の約1.5-2倍）

### STEP 1: 入力ファイル読み込み（30秒）

**Readツール使用**:
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/top_10_ai_tweets_{最新日付}.json
```

**確認項目**:
- ファイル存在確認
- `top_tweets` 配列の読み込み
- 各ツイートのrank、engagement_scoreを確認

**フォールバック**:
- 最新日付ファイルが見つからない場合、`top_10_ai_tweets_*.json` の最新ファイルを検索

---

### STEP 2: 調査対象トピック選定（1分）

**優先順位**:
1. **High priority**: Rank 1-3（エンゲージメントTop 3）→ 詳細調査
2. **Medium priority**: Rank 4-6 → 標準調査
3. **Low priority**: Rank 7-10 → 概要調査

**選定基準**:
```python
# 疑似コード（調査量2倍対応）
high_priority_topics = [t for t in top_tweets if t['rank'] <= 3]  # 詳細調査
medium_priority_topics = [t for t in top_tweets if 4 <= t['rank'] <= 6]  # 標準調査
low_priority_topics = [t for t in top_tweets if t['rank'] >= 7]  # 概要調査

# 全6件を調査（従来の2倍）
topics_to_research = high_priority_topics + medium_priority_topics
```

**ユーザーに報告**:
```
📊 調査対象トピック（2倍調査モード）
- High priority: 3件（詳細調査 - 専門家6-8名）
- Medium priority: 3件（標準調査 - 専門家4-6名）
- Low priority: 4件（概要のみ）

合計6トピックの詳細調査を開始します...
```

---

### STEP 3: トピック別Web調査（20-28分）

**各トピックに対して以下の3カテゴリを調査**:

#### 3A. 最新ニュース収集（4-6分/トピック）【2倍量】

**WebSearchクエリ（複数実行）**:
```
Topic 1: Tesla Optimus × NVIDIA Jensen Huang

Query 1: "Elon Musk NVIDIA Jensen Huang Optimus humanoid robot 2026"
Query 2: "Tesla Optimus production timeline 2026 factory"
Query 3: "humanoid robot market Tesla Boston Dynamics Figure 2026"
Query 4: "Optimus robot capabilities demonstration latest"
```

**抽出情報（2倍量）**:
- 要約（3-5文）
- 主要な進展（6-10個）
- 情報ソースURL（6-10個）
- 関連企業・競合の動向

**WebSearch実行（並列4クエリ）**:
```
WebSearch(query="Elon Musk NVIDIA Jensen Huang Optimus humanoid robot 2026")
WebSearch(query="Tesla Optimus production timeline 2026 factory")
WebSearch(query="humanoid robot market Tesla Boston Dynamics Figure 2026")
WebSearch(query="Optimus robot capabilities demonstration latest")
```

**抽出結果構造化**:
```json
{
  "summary": "NVIDIA CEO Jensen Huangは、Tesla Optimusが「次の数兆ドル産業」になると予測。2026年にはOptimus V3プロトタイプが登場し、年末までに年間100万台の生産体制を目指す。競合のBoston Dynamics、Figure AIも2026年に商用化を加速。",
  "key_developments": [
    "Jensen HuangがElon Muskを「extraordinary engineer」と評価",
    "2026年末に火星へOptimus搭載のStarship打ち上げを計画",
    "Huangは「ロボティクスの10年」と宣言",
    "Figure AIがBMWとの提携で工場導入開始",
    "Boston DynamicsがAtlas商用版を発表",
    "中国Unitree社が低価格ヒューマノイドで市場参入"
  ],
  "sources": [
    "https://www.ccn.com/news/technology/nvidia-ceo-humanoid-robot...",
    "https://fortune.com/2025/01/12/nvidia-jensen-huang-elon-musk...",
    "https://finance.yahoo.com/news/teslas-optimus-may-first...",
    "https://www.reuters.com/technology/humanoid-robot-race-2026...",
    "https://techcrunch.com/2026/01/figure-ai-bmw-partnership...",
    "https://www.bloomberg.com/news/articles/boston-dynamics-atlas..."
  ],
  "competitor_updates": [
    {"company": "Figure AI", "update": "BMW工場で商用導入開始"},
    {"company": "Boston Dynamics", "update": "Atlas商用版発表"},
    {"company": "Unitree", "update": "G1ヒューマノイド$16,000で販売開始"}
  ]
}
```

#### 3B. ファクトチェック実行（3-5分/トピック）【2倍量】

**検証対象（2倍）**:
- 数値（生産目標、価格、年度、市場規模）
- 主張（「次の数兆ドル産業」「ロボティクスの10年」等）
- 予測（「2026年V3プロトタイプ」「100万台生産」等）
- 技術的主張（自律性、タスク能力、バッテリー性能等）

**WebSearchクエリ（複数実行）**:
```
Query 1: "Tesla Optimus production 2026 million units verification"
Query 2: "humanoid robot market size 2026 2030 forecast"
Query 3: "Tesla Optimus price $20000 $30000 cost analysis"
Query 4: "Optimus autonomous capability teleoperation fact check"
```

**ファクトチェック構造化（2倍量）**:
```json
{
  "claim_1": {
    "claim": "2026年末までに年間100万台の生産体制",
    "verification": "未検証 - Muskの公約だが、独立報道によれば2025年の生産実績は数百台レベル",
    "reliability": "低",
    "sources": ["reuters.com", "bloomberg.com"]
  },
  "claim_2": {
    "claim": "価格目標 $20,000-$30,000",
    "verification": "未実証 - 大量生産時のコスト曲線が未確定",
    "reliability": "中",
    "sources": ["electrek.co", "teslarati.com"]
  },
  "claim_3": {
    "claim": "ヒューマノイドロボット市場は数兆ドル規模になる",
    "verification": "部分的に検証 - Goldman Sachs予測で2035年までに$380B市場",
    "reliability": "中",
    "sources": ["goldmansachs.com", "mckinsey.com"]
  },
  "claim_4": {
    "claim": "Optimusは完全自律で動作可能",
    "verification": "誤り - 現時点ではテレオペレーション（遠隔操作）が必要",
    "reliability": "低",
    "sources": ["theverge.com", "wired.com"]
  }
}
```

#### 3C. 専門家意見収集（6-8分/トピック）【大幅拡充】

**WebSearchクエリ（複数実行）**:
```
Query 1: "Jensen Huang Optimus robot opinion 2026"
Query 2: "Rodney Brooks humanoid robot criticism Tesla"
Query 3: "AI robotics expert analysis Optimus Figure Boston Dynamics"
Query 4: "venture capital investor humanoid robot market outlook"
Query 5: "academic researcher humanoid robot feasibility study"
Query 6: "industry analyst Tesla Optimus market potential"
```

**収集対象（6-8名に拡充）**:

| カテゴリ | 人数 | 例 |
|---------|------|-----|
| **業界リーダー** | 2名 | CEO、CTO、創業者 |
| **研究者・学者** | 2名 | 大学教授、研究所長 |
| **アナリスト** | 2名 | 投資銀行、調査会社 |
| **実務家・エンジニア** | 2名 | ロボット開発者、AI研究者 |

**専門家意見構造化（拡充版）**:
```json
{
  "industry_leaders": [
    {
      "expert": "Jensen Huang",
      "title": "NVIDIA CEO",
      "opinion": "Optimusは大量生産と技術スケールを達成する最初のヒューマノイドロボットになる可能性が高い。ロボティクスの10年が始まった。",
      "credibility": "高",
      "credibility_reason": "$3T企業のCEO、AI/ロボティクスハードウェアの権威",
      "source": "https://fortune.com/..."
    },
    {
      "expert": "Brett Adcock",
      "title": "Figure AI CEO",
      "opinion": "ヒューマノイドロボットは労働力不足を解決する。2026年には工場での実用化が本格化する。",
      "credibility": "高",
      "credibility_reason": "Figure AI創業者、元Archer Aviation CEO",
      "source": "https://techcrunch.com/..."
    }
  ],
  "researchers": [
    {
      "expert": "Rodney Brooks",
      "title": "iRobot共同創業者、MIT名誉教授",
      "opinion": "万能アシスタントとしてのヒューマノイドロボットというMuskのビジョンは純粋なファンタジー思考。実用化には10年以上かかる。",
      "credibility": "非常に高",
      "credibility_reason": "Roomba開発者、ロボティクス分野の先駆者、50年以上の研究経験",
      "source": "https://www.techradar.com/..."
    },
    {
      "expert": "Daniela Rus",
      "title": "MIT CSAIL所長",
      "opinion": "ヒューマノイドロボットの進歩は著しいが、人間環境での汎用性達成にはまだ多くの課題がある。",
      "credibility": "非常に高",
      "credibility_reason": "MIT AI研究所所長、ロボット工学の世界的権威",
      "source": "https://news.mit.edu/..."
    }
  ],
  "analysts": [
    {
      "expert": "Goldman Sachs Equity Research",
      "title": "投資銀行リサーチ",
      "opinion": "ヒューマノイドロボット市場は2035年までに$380Bに成長。Teslaは製造能力で優位性あり。",
      "credibility": "高",
      "credibility_reason": "大手投資銀行のリサーチチーム、定量分析に基づく",
      "source": "https://www.goldmansachs.com/..."
    },
    {
      "expert": "ARK Invest",
      "title": "投資運用会社",
      "opinion": "Optimusは2030年までにTeslaの時価総額を2倍にする可能性がある。",
      "credibility": "中",
      "credibility_reason": "テクノロジー投資に特化、ただしTesla強気ポジションあり",
      "source": "https://ark-invest.com/..."
    }
  ],
  "practitioners": [
    {
      "expert": "Marc Raibert",
      "title": "Boston Dynamics創業者",
      "opinion": "ヒューマノイドロボットの動的バランス制御は解決済み。次の課題は汎用マニピュレーションと認知能力。",
      "credibility": "非常に高",
      "credibility_reason": "Boston Dynamics創業者、動的ロボット研究の第一人者",
      "source": "https://spectrum.ieee.org/..."
    },
    {
      "expert": "Pieter Abbeel",
      "title": "UC Berkeley教授、Covariant共同創業者",
      "opinion": "強化学習とシミュレーションの進歩により、ロボットの訓練効率が飛躍的に向上している。",
      "credibility": "非常に高",
      "credibility_reason": "ロボット学習研究の第一人者、実用化にも携わる",
      "source": "https://covariant.ai/..."
    }
  ],
  "summary": {
    "consensus_points": [
      "ヒューマノイドロボット市場は急成長中",
      "製造・物流分野での実用化が先行",
      "完全自律は現時点では未達成"
    ],
    "disagreement_points": [
      "実用化のタイムライン（楽観派: 2-3年、慎重派: 10年以上）",
      "家庭用汎用ロボットの実現可能性",
      "Teslaの技術的優位性の持続性"
    ],
    "expert_count": 8,
    "credibility_breakdown": {
      "very_high": 4,
      "high": 3,
      "medium": 1
    }
  }
}
```

---

### STEP 4: 結果集計（1分）

**統計情報計算（2倍量対応）**:
```python
# 疑似コード
total_sources = sum([len(topic['latest_news']['sources']) for topic in researched_topics])
# 目標: 60以上（従来の2倍）

total_fact_checks = sum([len(topic['fact_check']) for topic in researched_topics])
# 目標: 14以上（従来の2倍）

total_experts = sum([
    len(topic['expert_opinions']['industry_leaders']) +
    len(topic['expert_opinions']['researchers']) +
    len(topic['expert_opinions']['analysts']) +
    len(topic['expert_opinions']['practitioners'])
    for topic in researched_topics
])
# 目標: 36以上（6トピック × 6-8名）
```

---

### STEP 5: 出力ファイル生成（30秒）

**出力JSONフォーマット**:
```json
{
  "metadata": {
    "researched_at": "2026-01-04T19:00:00",
    "research_method": "ClaudeCode WebSearch + LLM analysis (2x volume)",
    "total_topics": 10,
    "high_priority_count": 3,
    "medium_priority_count": 3,
    "topics_researched": 6,
    "research_completion_rate": "100% (6/6 priority topics)",
    "research_categories": [
      "latest_news",
      "fact_check",
      "expert_opinions"
    ],
    "research_summary": {
      "total_sources_found": 60,
      "fact_checks_performed": 14,
      "expert_opinions_collected": 40,
      "expert_credibility": {
        "very_high": 24,
        "high": 12,
        "medium": 4
      }
    },
    "version": "2.0 - 2x volume, expert-focused"
  },
  "research_findings": {
    "2006676783991787563": {
      "tweet_username": "cb_doge",
      "topic": "Tesla Optimus × NVIDIA Jensen Huang",
      "latest_news": {...},
      "fact_check": {...},
      "expert_opinions": {...}
    }
  },
  "topics": [...]
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/research_findings_ai_{YYYYMMDD}.json`

---

### STEP 6: サマリーレポート生成（30秒）

**ユーザーへの報告**:
```
✅ トピック調査完了（2倍調査モード）

📊 Summary:
  - Topics researched: 6/6 (High + Medium priority)
  - Total sources found: 60 (2x)
  - Fact checks performed: 14 (2x)
  - Expert opinions collected: 40 (4x)
    - Very high credibility: 24
    - High credibility: 12
    - Medium credibility: 4

🎓 Expert Consensus:
  ✓ ヒューマノイドロボット市場は急成長中
  ✓ 製造・物流分野での実用化が先行
  ✗ 完全自律は現時点では未達成

⚖️ Key Disagreements:
  - 実用化タイムライン: 楽観派 vs 慎重派
  - 家庭用汎用ロボットの実現可能性
  - Teslaの技術的優位性

💾 Output: research_findings_ai_20260104.json (45KB)

📌 Next: generate-sns-posts（専門家意見を反映した投稿生成）
```

---

## 調査カテゴリ詳細

### 最新ニュース（latest_news）【2倍量】
**目的**: トピックの最新動向を網羅的に把握
**情報源**: ニュースサイト、公式発表、専門メディア、競合情報
**重視する情報**:
- 発表日が2026年または2025年後半
- 公式ソースまたは信頼性の高いメディア
- 具体的な数値・日程・計画
- 競合企業の動向

**調査量**:
- クエリ数: 4（従来の2倍）
- ソース数: 6-10（従来の2倍）

### ファクトチェック（fact_check）【2倍量】
**目的**: 主張・数値・予測の信頼性を複数ソースで検証
**検証項目**:
- 数値の出典（公式発表 vs 予測）
- 実現可能性（過去の実績との比較）
- 技術的主張の妥当性
- 市場規模予測の根拠
- 信頼性評価（高/中/低）

**調査量**:
- 検証項目数: 4（従来の2倍）
- 参照ソース: 各項目2以上

### 専門家意見（expert_opinions）【大幅拡充】
**目的**: 多角的な専門家の見解を収集し、バランスの取れた視点を獲得
**収集対象（6-8名/トピック）**:
- **業界リーダー** (2名): CEO、CTO、創業者
- **研究者・学者** (2名): 大学教授、研究所長
- **アナリスト** (2名): 投資銀行、調査会社
- **実務家・エンジニア** (2名): 開発者、AI研究者

**評価項目**:
- 専門性（分野での経験年数、実績）
- 信頼性（very_high / high / medium）
- ポジションの利益相反（投資ポジション、競合関係等）

**調査量**:
- 専門家数: 6-8名/トピック（従来の4倍）
- 検索クエリ: 6（従来の2倍）

---

## エラーハンドリング

### WebSearch結果が0件の場合
- **対応**: クエリを変更して再検索（英語→日本語、キーワード追加）
- **リトライ**: 最大3回（従来の1.5倍）
- **失敗時**: `status: "no_results"` で記録、次のトピックへ

### ソース情報が不十分な場合
- **対応**: 部分的な情報でも記録（`status: "partial"`）
- **ログ**: `note: "情報源が限定的"` を追記

### 専門家意見が不足の場合
- **対応**: 関連分野の専門家で補完
- **最低要件**: 4名/トピック（6-8名が目標）

### LLM分析失敗
- **原因**: WebSearch結果が断片的、関連性が低い
- **対応**: `status: "analysis_failed"` で記録、次のカテゴリへ

---

## データ品質保証

| 品質指標 | 目標（2倍量） | 従来 |
|---------|-------------|------|
| **調査トピック数** | ≥6 | 3 |
| **総ソース数** | ≥60 | 30 |
| **ファクトチェック数** | ≥14 | 7 |
| **専門家意見数** | ≥40 | 9 |
| **高信頼性専門家比率** | ≥80% | - |

---

## 使用例

### 基本的な使用

```
User: トピック調査
```

システムが自動的に：
1. 最新の `top_10_ai_tweets_*.json` を読み込み
2. High + Medium priorityトピック（6件）を選定
3. 各トピックに対して3カテゴリの調査を実行（2倍量）
4. WebSearchで最新ニュース・専門家意見を重点収集
5. JSON出力生成
6. サマリーレポート表示

### カスタム調査範囲

```
User: トピック調査（全10件）
```

システムが自動的に：
- Top 10全てを調査（所要時間: 50-70分）
- 各トピックに対して3カテゴリ調査（2倍量）

---

## 依存ツール

**必須**:
- `Read`: 入力ファイル読み込み
- `WebSearch`: Web調査実行（複数並列クエリ対応）
- `Write`: 出力ファイル保存
- ClaudeCode LLM内部処理（思考モード有効）

---

## 次のアクション提案

調査完了後、以下のアクションを提案します：

1. **generate-sns-posts**: 専門家意見を反映した投稿文生成
2. **専門家引用型投稿**: 高信頼性専門家のコメントを引用
3. **多角的視点投稿**: 業界リーダー vs 研究者の見解を対比
4. **ファクトチェック済み投稿**: 検証済み数値のみを使用

---

## 更新履歴

- 2026-01-04: v2.0 - 調査量2倍、専門家意見重点収集版
  - 批判的視点カテゴリを削除
  - 専門家意見を6-8名/トピックに拡充（4カテゴリ）
  - 調査トピック数を3→6に増加
  - ソース数目標を30→60に増加
  - ファクトチェック数を7→14に増加
  - 専門家意見数を9→40に増加
- 2026-01-02: v1.0 - 初版作成（ClaudeCode WebSearch実行型）
