---
name: trading-phase1-analysts
description: |
  Phase1アナリストチーム全体を自律実行するオーケストレータースキル。
  Market/Fundamentals/News/Sentimentの4軸で日経平均先物を包括分析（60-90分）。
  WebSearch/WebFetchで実データ収集し、4エージェント完了後に統合見解を生成。
  ステージゲート管理（4エージェント完了・コンセンサス判定明確）で品質保証。

  使用タイミング：
  - 日経平均先物のトレード戦略立案開始時
  - 市場全体の包括的分析が必要な時
  - Phase1を一気通貫で実行したい

  所要時間：60-90分（自動実行）
  出力：analysts_summary.md

trigger_keywords:
  - "Phase1実行"
  - "アナリスト分析"
  - "市場分析開始"
  - "トレード分析開始"

stage: Phase1 - Analysts Team

dependencies:
  - agent-market-analyst
  - agent-fundamentals-analyst
  - agent-news-analyst
  - agent-sentiment-analyst

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md

execution_time: 60-90分（自動実行）

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P0

framework_compliance: 100%
---

# Trading Phase1 Analysts Orchestrator Skill

Phase1アナリストチーム全体を自律実行するオーケストレーターSkill。

---

## このSkillでできること

1. **Phase1全自動実行**: 4エージェントを順次実行
2. **ステージゲート管理**: 4エージェント完了・コンセンサス判定確認
3. **統合分析**: 4軸（テクニカル・ファンダメンタルズ・ニュース・センチメント）の統合見解生成
4. **進捗管理**: 各エージェントの完了状況を可視化
5. **最終評価**: コンセンサススコアで総合判定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | なし（自動実行） |
| **出力** | Phase1全成果物（`phase1/{YYYY-MM-DD}/`） |
| **次のSkill** | Phase2へ進む or Phase1再実行 |

---

## Instructions

**実行モード**: 自律実行（ステージゲートで停止）
**推定所要時間**: 60-90分

### 前提条件確認

#### ステップ1: 環境情報取得

1. **現在日時取得**: 2025年12月29日
2. **対象銘柄**: 日経平均先物（日経225）
3. **分析期間**: 今後1週間（5営業日）
4. **出力先確認**: `Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/2025-12-29/`

### Phase1実行ステップ（全4エージェント）

**注意**: Claude Code は並列実行非対応のため順次実行。
各エージェントは独立設計のため、将来並列化可能。

#### エージェント1: Market Analyst（テクニカル分析）

**実行**: `/agent-market-analyst`

**推定時間**: 20-30分

**期待成果物**:
- `market_analysis.md`
- 8つのテクニカル指標分析完了
- 総合判定（強気/弱気/中立）
- データソースURL 3件以上

**完了確認**:
- [ ] `market_analysis.md` 存在確認
- [ ] 8指標すべて分析完了
- [ ] 総合判定明記
- [ ] WebSearch実行履歴 3件以上

---

#### エージェント2: Fundamentals Analyst（マクロ経済分析）

**実行**: `/agent-fundamentals-analyst`

**推定時間**: 20-30分

**期待成果物**:
- `fundamentals_analysis.md`
- 日銀・FRB政策分析
- 為替（USD/JPY）分析
- 経済指標カレンダー
- 総合判定（追い風/逆風/中立）

**完了確認**:
- [ ] `fundamentals_analysis.md` 存在確認
- [ ] 金融政策分析完了
- [ ] 為替分析完了
- [ ] 総合スコア算出

---

#### エージェント3: News Analyst（ニュース分析）

**実行**: `/agent-news-analyst`

**推定時間**: 10-15分

**期待成果物**:
- `news_analysis.md`
- 過去7日間ニュース収集（20件以上）
- 重要度・センチメント分類
- 市場テーマ抽出
- 総合センチメント判定

**完了確認**:
- [ ] `news_analysis.md` 存在確認
- [ ] ニュース20件以上収集
- [ ] センチメント分類完了
- [ ] 総合センチメント明記

---

#### エージェント4: Sentiment Analyst（市場心理分析）

**実行**: `/agent-sentiment-analyst`

**推定時間**: 10-15分

**期待成果物**:
- `sentiment_analysis.md`
- VIX指数分析
- Fear & Greed Index
- Put/Call比率
- SNS分析
- 逆張りシグナル判定

**完了確認**:
- [ ] `sentiment_analysis.md` 存在確認
- [ ] 4指標すべて分析完了
- [ ] 逆張りシグナル判定明記
- [ ] 総合センチメントスコア算出

---

### ステージゲート判定

**ステージゲート1: Phase1完了確認**

- **合格条件**:
  1. 4エージェント全実行完了
  2. 各エージェントの成果物存在
  3. 各エージェントでデータソースURL 3件以上
  4. コンセンサス判定明確（強気/弱気/中立）

- **未達成時**: 停止（Human-in-the-Loop必須）
  - 不足エージェント特定
  - 再実行 or データソース追加WebSearch
  - 最大3回リトライ

**チェックリスト**:
```markdown
Phase1 完了確認:
- [ ] agent-market-analyst 完了
- [ ] agent-fundamentals-analyst 完了
- [ ] agent-news-analyst 完了
- [ ] agent-sentiment-analyst 完了
- [ ] 各成果物にデータソースURL 3件以上
- [ ] コンセンサス判定明確
- [ ] 総合スコア算出完了
```

---

### 統合分析：analysts_summary.md生成

#### ステップ2: 各成果物読み込み

```markdown
1. Read: `market_analysis.md`
   - 総合判定: [強気/弱気/中立]
   - 8指標スコア: XX/8
   - 推奨方向: [ロング/ショート/中立]

2. Read: `fundamentals_analysis.md`
   - 総合判定: [追い風/逆風/中立]
   - Tailwinds: X件（スコア: XX）
   - Headwinds: X件（スコア: XX）

3. Read: `news_analysis.md`
   - 総合センチメント: [ポジティブ/ネガティブ/中立]
   - ポジティブ: XX件（XX%）
   - ネガティブ: XX件（XX%）

4. Read: `sentiment_analysis.md`
   - 総合センチメント: [恐怖/中立/楽観]
   - センチメントスコア: XX/100
   - 逆張りシグナル: [あり/なし]
```

#### ステップ3: コンセンサス判定

**判定ロジック**:

```python
# 4軸判定スコア
scores = {
    "market": 1 if market_判定 == "強気" else -1 if market_判定 == "弱気" else 0,
    "fundamentals": 1 if fundamentals_判定 == "追い風" else -1 if fundamentals_判定 == "逆風" else 0,
    "news": 1 if news_判定 == "ポジティブ" else -1 if news_判定 == "ネガティブ" else 0,
    "sentiment": 1 if sentiment_判定 == "楽観" else -1 if sentiment_判定 == "恐怖" else 0
}

total_score = sum(scores.values())

# コンセンサス判定
if total_score >= 2:
    consensus = "強気（Bull）"
    confidence = "高" if total_score >= 3 else "中"
elif total_score <= -2:
    consensus = "弱気（Bear）"
    confidence = "高" if total_score <= -3 else "中"
else:
    consensus = "中立（Neutral）"
    confidence = "低"
```

**コンセンサス判定基準**:

| 合計スコア | 判定 | 信頼度 | 推奨アクション |
|:---------:|------|--------|---------------|
| +4 | ✅ 強気（全員一致） | 非常に高 | ロング推奨 |
| +3 | ✅ 強気（3軸一致） | 高 | ロング推奨 |
| +2 | ⚠️ やや強気 | 中 | 慎重なロング |
| +1 | ⚠️ やや強気 | 低 | 中立〜ロング |
| 0 | ⚡ 中立（意見分散） | - | 見送り推奨 |
| -1 | ⚠️ やや弱気 | 低 | 中立〜ショート |
| -2 | ⚠️ やや弱気 | 中 | 慎重なショート |
| -3 | ❌ 弱気（3軸一致） | 高 | ショート推奨 |
| -4 | ❌ 弱気（全員一致） | 非常に高 | ショート推奨 |

---

### 最終成果物: analysts_summary.md

```markdown
---
phase: phase1
timestamp: 2025-12-29 12:00:00
status: completed
target: 日経平均先物（日経225）
period: 2025-12-30 ~ 2026-01-10（1週間）
---

# Phase1 Analysts Team 統合分析レポート

## エグゼクティブサマリー

**総合判定**: [強気/弱気/中立]
**信頼度**: [非常に高/高/中/低]
**コンセンサススコア**: +X/4（4軸中X軸が[強気/弱気]）
**推奨方向**: [ロング/ショート/見送り]

**要約**:
- Market Analyst: [判定] - [根拠]
- Fundamentals Analyst: [判定] - [根拠]
- News Analyst: [判定] - [根拠]
- Sentiment Analyst: [判定] - [根拠]

---

## 1. 4エージェント分析サマリー

### 1.1 Market Analyst（テクニカル分析）

**総合判定**: [強気/弱気/中立]
**スコア**: X/8指標が[強気/弱気]シグナル

**主要指標**:
- 200日SMA: [状態] → [シグナル]
- 50日SMA: [状態] → [シグナル]
- MACD: [状態] → [シグナル]
- RSI: [値] → [シグナル]

**エントリー候補価格**:
- ロング: XX,XXX-XX,XXX円
- ショート: XX,XXX-XX,XXX円

**詳細**: `market_analysis.md` 参照

---

### 1.2 Fundamentals Analyst（マクロ経済分析）

**総合判定**: [追い風/逆風/中立]
**スコア**: 追い風 XX点 vs 逆風 XX点

**主要ファクター**:
- 日銀政策: [状態] → [影響]
- FRB政策: [状態] → [影響]
- USD/JPY: [状態] → [影響]
- 経済指標: [状態] → [影響]

**1週間見通し**: [予測]

**詳細**: `fundamentals_analysis.md` 参照

---

### 1.3 News Analyst（ニュース分析）

**総合センチメント**: [ポジティブ優勢/ネガティブ優勢/中立]
**収集ニュース数**: XX件

**センチメント内訳**:
- ポジティブ: XX件（XX%）
- ネガティブ: XX件（XX%）
- 中立: XX件（XX%）

**主要テーマ**:
1. [テーマ1]: [センチメント] - [影響]
2. [テーマ2]: [センチメント] - [影響]

**詳細**: `news_analysis.md` 参照

---

### 1.4 Sentiment Analyst（市場心理分析）

**総合センチメント**: [極端な恐怖/恐怖/中立/楽観/極端な楽観]
**センチメントスコア**: XX/100
**逆張りシグナル**: [あり/なし]

**主要指標**:
- VIX指数: XX → [恐怖/平常/楽観]
- Fear & Greed: XX/100 → [判定]
- Put/Call比: X.XX → [弱気/中立/強気]
- SNS: XX%ポジティブ → [判定]

**詳細**: `sentiment_analysis.md` 参照

---

## 2. コンセンサス分析

### 2.1 4軸判定マトリックス

| エージェント | 判定 | スコア | 重み | 加重スコア |
|-------------|------|--------|------|-----------|
| Market Analyst | [強気/弱気/中立] | +1/0/-1 | 1.0 | +X |
| Fundamentals | [追い風/逆風/中立] | +1/0/-1 | 1.0 | +X |
| News | [ポジティブ/ネガティブ/中立] | +1/0/-1 | 1.0 | +X |
| Sentiment | [楽観/恐怖/中立] | +1/0/-1 | 1.0 | +X |

**合計スコア**: +X/4

---

### 2.2 総合コンセンサス

**判定**: [強気（Bull）/弱気（Bear）/中立（Neutral）]
**信頼度**: [非常に高/高/中/低]

**根拠**:
- 4エージェント中X軸が[強気/弱気]判定
- [一致している主要ファクター]
- [意見が分かれているポイント]

**推奨アクション**:
- [具体的な推奨]

---

### 2.3 意見の一致度分析

**コンセンサスレベル**: [全員一致/高/中/低/意見分散]

**一致ポイント**:
- [ポイント1]
- [ポイント2]

**相違ポイント**:
- [ポイント1]: Market は[判定1]、Sentiment は[判定2]
- [ポイント2]: [詳細]

**解釈**:
[相違の理由と総合的な解釈]

---

## 3. Phase2への引き継ぎ事項

### 3.1 主要な検証ポイント

Phase2（リサーチチーム）で深掘りすべき項目:

1. **強気シナリオの前提条件**:
   - [前提1]
   - [前提2]

2. **弱気シナリオのリスク要因**:
   - [リスク1]
   - [リスク2]

3. **不確実性の高い要素**:
   - [要素1]
   - [要素2]

### 3.2 推奨リサーチ方向

**Bull Researcher への指示**:
- [具体的な強気根拠の深掘り指示]

**Bear Researcher への指示**:
- [具体的な弱気リスクの深掘り指示]

---

## 4. データ品質監査

### 4.1 データソース検証

| エージェント | WebSearchクエリ数 | WebFetch URL数 | データソース数 | 検証結果 |
|-------------|-----------------|---------------|--------------|---------|
| Market | X | X | X | ✅ 合格 |
| Fundamentals | X | X | X | ✅ 合格 |
| News | X | X | X | ✅ 合格 |
| Sentiment | X | X | X | ✅ 合格 |

**総計**: WebSearch XXクエリ、WebFetch XX URLs、データソース XX件

### 4.2 ハルシネーション防止確認

- [ ] 全データにソースURL明記
- [ ] 複数ソースでのクロスチェック実施
- [ ] 推測箇所に「推測:」ラベル明記
- [ ] 数値の異常値検出なし

**検証結果**: ✅ ハルシネーション防止基準クリア

---

## 5. ステージゲート判定結果

### Phase1 完了基準チェック

- [x] 4エージェント全実行完了
- [x] 各成果物存在確認
- [x] 各エージェントでデータソースURL 3件以上
- [x] コンセンサス判定明確
- [x] 総合スコア算出完了

**判定**: ✅ Phase1完了

**次のアクション**: Phase2へ進む

---

## メタデータ

- **実行開始**: 2025-12-29 XX:XX:XX
- **実行完了**: 2025-12-29 XX:XX:XX
- **総実行時間**: XX分
- **4エージェント実行時間**:
  - Market Analyst: XX分
  - Fundamentals Analyst: XX分
  - News Analyst: XX分
  - Sentiment Analyst: XX分

---

## Phase1 成果物一覧

```
Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/2025-12-29/
├── market_analysis.md          ✅ 完了
├── fundamentals_analysis.md    ✅ 完了
├── news_analysis.md            ✅ 完了
├── sentiment_analysis.md       ✅ 完了
└── analysts_summary.md         ✅ 完了（本ファイル）
```

---

## 次のステップ

1. **Phase2実行**: `/trading-phase2-research`
   - Bull Researcher: 強気シナリオ構築
   - Bear Researcher: 弱気シナリオ構築
   - Research Manager: 統合判断

2. **または**: Phase1結果を精査し、必要に応じて個別エージェント再実行

3. **または**: 直接Phase3へスキップ（リスク管理チーム）
```

---

## 成果物

### 最終成果物一覧

```
TradingAgents/data/results/phase1/2025-12-29/
├── market_analysis.md
├── fundamentals_analysis.md
├── news_analysis.md
├── sentiment_analysis.md
└── analysts_summary.md ← このスキルが生成
```

---

## Knowledge Base参照

- Market Analyst: `.claude/skills/agent-market-analyst/SKILL.md`
- Fundamentals Analyst: `.claude/skills/agent-fundamentals-analyst/SKILL.md`
- News Analyst: `.claude/skills/agent-news-analyst/SKILL.md`
- Sentiment Analyst: `.claude/skills/agent-sentiment-analyst/SKILL.md`
- Project Requirements: `@Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md`

---

## 使用例

```
User: /trading-phase1-analysts

Skill:
# Phase1 Analysts Team 自律実行開始

対象: 日経平均先物（日経225）
分析期間: 今後1週間（2025-12-30 ~ 2026-01-10）
推定所要時間: 60-90分

[自動実行中...]

## エージェント1: Market Analyst ✅ 完了（25分）
- 総合判定: 強気
- 8指標スコア: 6/8が強気シグナル
- 推奨: ロング（32,600-32,800円）

## エージェント2: Fundamentals Analyst ✅ 完了（28分）
- 総合判定: 追い風
- スコア: 追い風15点 vs 逆風8点
- 1週間見通し: ポジティブ

## エージェント3: News Analyst ✅ 完了（12分）
- 総合センチメント: ポジティブ優勢
- ポジティブ: 25件（43%）
- ネガティブ: 20件（34%）

## エージェント4: Sentiment Analyst ✅ 完了（13分）
- 総合センチメント: 中立やや弱気
- センチメントスコア: 42/100
- 逆張りシグナル: 弱い買いシグナル

## ステージゲート判定 ✅ 通過
- 4エージェント全完了
- データソースURL: 合計20件
- コンセンサス: 強気（+3/4）

## Phase1 完了

総実行時間: 78分
総合判定: ✅ 強気（Bull）
信頼度: 高
コンセンサススコア: +3/4（4軸中3軸が強気）

次のアクション:
1. Phase2へ進む（/trading-phase2-research）
2. 個別エージェント詳細確認
3. 直接Phase3へスキップ

成果物: analysts_summary.md 生成完了
```
