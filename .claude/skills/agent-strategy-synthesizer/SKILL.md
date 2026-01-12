---
name: agent-strategy-synthesizer
description: |
  3エージェント（テクニカル/エリオット波動/センチメント）の分析結果を重み付け投票で統合し、最終的なトレード戦略を生成するエージェント。エントリー価格は加重平均、目標価格は最も保守的な値、ストップロスは最も近い値を採用してリスクを最小化。リスク・リワード比率と期待値を算出し、実行可能性を評価します。

  使用タイミング：
  - テクニカル/エリオット/センチメント分析完了後
  - 各エージェントの結果を統合して最終判断
  - 具体的なトレード戦略を生成

  所要時間：15-20分
  出力：synthesized_strategy.md（統合判定 + 価格提案 + リスク評価）
trigger_keywords:
  - "戦略統合"
  - "統合分析"
  - "最終判定"
stage: Strategy Synthesis
dependencies:
  - agent-technical-analyst
  - agent-elliott-wave-analyst
  - agent-sentiment-analyst
output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/synthesized_strategy.md
execution_time: 15-20分
framework_reference: Stock/programs/資産運用/projects/TradingAgents/knowledge/
priority: P0
framework_compliance: 100%
---

# Agent Strategy Synthesizer Skill

3エージェントの分析結果を統合し、最終トレード戦略を生成するエージェント。

---

## このSkillでできること

1. **重み付け投票**: 各エージェントに重みを設定し、シグナルを統合
2. **価格目標統合**: エントリー/エグジット/ストップロスを加重平均で算出
3. **信頼度評価**: 統合シグナルの信頼度を0-100%で評価
4. **リスク・リワード比率算出**: 期待リターンと最大リスクから比率を計算
5. **実行可能性評価**: 市場流動性、ボラティリティ、実行難易度を判定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | technical_analysis.md, elliott_wave_analysis.md, sentiment_analysis.md（各分析エージェントの出力） |
| **出力** | synthesized_strategy.md（統合判定 + 具体的価格 + リスク評価） |
| **次のSkill** | agent-backtest-validator（バックテスト検証） |

---

## Instructions

**実行モード**: 自律実行
**推定所要時間**: 15-20分

### 戦略統合ステップ

#### STEP 1: 各エージェントの分析結果読み込み（2分）

```python
# 各エージェントの出力を読み込み
technical = read_md("Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/technical_analysis.md")
elliott = read_md("Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/elliott_wave_analysis.md")
sentiment = read_md("Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/sentiment_analysis.md")

# 各エージェントのシグナル抽出
technical_signal = technical['総合シグナル']  # "強気" or "弱気" etc.
technical_confidence = technical['信頼度']  # 75%
technical_entry = technical['推奨エントリー']  # 33,150円
technical_target = technical['目標価格']  # 34,500円
technical_stop = technical['ストップロス']  # 32,500円

elliott_signal = elliott['方向']  # "Up" or "Down"
elliott_confidence = elliott['確度']  # 70%
elliott_entry_range = elliott['エントリーレンジ']  # (33,000, 33,200)
elliott_target = elliott['目標価格']  # 34,500円
elliott_stop = elliott['ストップロス']  # 32,000円

sentiment_signal = sentiment['市場心理']  # "リスクオン（強気）" or "リスクオフ（弱気）"
sentiment_confidence = sentiment['信頼度']  # 60%
sentiment_risk_level = sentiment['リスク警戒度']  # "中"
```

#### STEP 2: シグナル統合（5分）

```python
# 各エージェントの重み設定
AGENT_WEIGHTS = {
    'technical': 2.0,      # テクニカル分析（最重要）
    'elliott': 1.8,        # エリオット波動
    'sentiment': 1.2       # センチメント分析（補助的）
}

# シグナルを数値化
# 買い = +2.0, やや買い = +1.0, 中立 = 0.0, やや売り = -1.0, 売り = -2.0

def signal_to_score(signal, signal_type='technical'):
    if signal_type == 'technical':
        if signal == "強気":
            return 2.0
        elif signal == "やや強気":
            return 1.0
        elif signal == "中立":
            return 0.0
        elif signal == "やや弱気":
            return -1.0
        elif signal == "弱気":
            return -2.0

    elif signal_type == 'elliott':
        if signal == "Up":
            return 2.0
        elif signal == "Correction":
            return 0.0
        elif signal == "Down":
            return -2.0

    elif signal_type == 'sentiment':
        if "強気" in signal:
            return 2.0 if "強気）" in signal else 1.0
        elif "弱気" in signal:
            return -2.0 if "弱気）" in signal else -1.0
        else:
            return 0.0

# スコア計算
technical_score = signal_to_score(technical_signal, 'technical')
elliott_score = signal_to_score(elliott_signal, 'elliott')
sentiment_score = signal_to_score(sentiment_signal, 'sentiment')

# 重み付けスコア
weighted_score = (
    technical_score * AGENT_WEIGHTS['technical'] +
    elliott_score * AGENT_WEIGHTS['elliott'] +
    sentiment_score * AGENT_WEIGHTS['sentiment']
)

# 総重み
total_weight = sum(AGENT_WEIGHTS.values())

# 正規化スコア（-1.0 ~ +1.0）
normalized_score = weighted_score / (total_weight * 2.0)

# 総合シグナル判定
if normalized_score > 0.4:
    overall_signal = "買い"
    overall_confidence = min(100, int(normalized_score * 100 + 50))
elif normalized_score > 0.1:
    overall_signal = "やや買い"
    overall_confidence = min(100, int(normalized_score * 80 + 40))
elif normalized_score < -0.4:
    overall_signal = "売り"
    overall_confidence = min(100, int(abs(normalized_score) * 100 + 50))
elif normalized_score < -0.1:
    overall_signal = "やや売り"
    overall_confidence = min(100, int(abs(normalized_score) * 80 + 40))
else:
    overall_signal = "中立"
    overall_confidence = 50

# エージェント別スコアテーブル
agent_scores = [
    {'agent': 'テクニカル分析', 'signal': technical_signal, 'confidence': technical_confidence, 'weight': AGENT_WEIGHTS['technical'], 'score': technical_score * AGENT_WEIGHTS['technical']},
    {'agent': 'エリオット波動', 'signal': elliott_signal, 'confidence': elliott_confidence, 'weight': AGENT_WEIGHTS['elliott'], 'score': elliott_score * AGENT_WEIGHTS['elliott']},
    {'agent': 'センチメント分析', 'signal': sentiment_signal, 'confidence': sentiment_confidence, 'weight': AGENT_WEIGHTS['sentiment'], 'score': sentiment_score * AGENT_WEIGHTS['sentiment']}
]
```

#### STEP 3: 価格目標統合（5分）

```python
# エントリー価格の加重平均
if overall_signal in ["買い", "やや買い"]:
    # 買いシグナル

    # 各エージェントのエントリー価格
    technical_entry_price = technical_entry
    elliott_entry_price = (elliott_entry_range[0] + elliott_entry_range[1]) / 2
    sentiment_entry_price = technical_entry  # センチメントはエントリー価格を提示しないため、テクニカルを使用

    # 加重平均
    weighted_entry = (
        technical_entry_price * AGENT_WEIGHTS['technical'] +
        elliott_entry_price * AGENT_WEIGHTS['elliott'] +
        sentiment_entry_price * AGENT_WEIGHTS['sentiment']
    ) / total_weight

    # 目標価格（最も保守的な値を採用）
    targets = [technical_target, elliott_target]
    target_price = min(targets)  # 保守的に低い方を採用

    # ストップロス（最も近い値を採用 = リスク最小化）
    stops = [technical_stop, elliott_stop]
    stop_loss = max(stops)  # エントリーから最も近い（＝リスク小）

elif overall_signal in ["売り", "やや売り"]:
    # 売りシグナル（ショート）

    weighted_entry = (
        technical_entry_price * AGENT_WEIGHTS['technical'] +
        elliott_entry_price * AGENT_WEIGHTS['elliott'] +
        sentiment_entry_price * AGENT_WEIGHTS['sentiment']
    ) / total_weight

    # 目標価格（ショートの場合は高い方が保守的）
    target_price = max(targets)

    # ストップロス（ショートの場合は低い方がリスク小）
    stop_loss = min(stops)

else:
    # 中立シグナル（トレード非推奨）
    weighted_entry = None
    target_price = None
    stop_loss = None
```

#### STEP 4: リスク・リワード比率算出（2分）

```python
if weighted_entry and target_price and stop_loss:
    # リスク（損失幅）
    risk = abs(weighted_entry - stop_loss)

    # リワード（利益幅）
    reward = abs(target_price - weighted_entry)

    # リスク・リワード比率
    risk_reward_ratio = reward / risk

    # 期待リターン（%）
    expected_return = ((target_price - weighted_entry) / weighted_entry) * 100

    # 最大リスク（%）
    max_risk = ((weighted_entry - stop_loss) / weighted_entry) * 100

    # 期待値（勝率を仮定）
    # 仮定: 信頼度が勝率の近似値
    win_rate = overall_confidence / 100
    lose_rate = 1 - win_rate

    expected_value = (win_rate * expected_return) + (lose_rate * (-max_risk))

else:
    risk_reward_ratio = None
    expected_return = None
    max_risk = None
    expected_value = None
```

#### STEP 5: 実行可能性評価（3分）

```python
# 市場流動性評価
# 日経平均先物は非常に流動性が高い
liquidity_score = "高"
liquidity_note = "日経平均先物は24時間取引可能、出来高も十分"

# ボラティリティ評価（technical analysisのATRを使用）
atr_pct = technical['ATR']['ボラティリティ']  # 2.1%

if atr_pct > 3:
    volatility_level = "高"
    volatility_note = "高ボラティリティ、スリッページリスク大"
elif atr_pct > 2:
    volatility_level = "中"
    volatility_note = "通常のボラティリティ、実行可能"
else:
    volatility_level = "低"
    volatility_note = "低ボラティリティ、スプレッド小"

# 実行難易度
if risk_reward_ratio and risk_reward_ratio > 1.5:
    execution_difficulty = "低"
    execution_note = "明確なエントリー/エグジットポイント、実行容易"
elif risk_reward_ratio and risk_reward_ratio > 1.0:
    execution_difficulty = "中"
    execution_note = "実行可能だが、タイミング重要"
else:
    execution_difficulty = "高"
    execution_note = "リスク・リワード比率不利、実行非推奨"

# 総合実行可能性
if liquidity_score == "高" and volatility_level in ["低", "中"] and execution_difficulty in ["低", "中"]:
    overall_feasibility = "高"
else:
    overall_feasibility = "中"
```

#### STEP 6: エントリー根拠の統合（2分）

```python
# 各エージェントのエントリー根拠を抽出・統合
entry_rationale = []

# テクニカル分析の根拠
if technical_score > 0:
    technical_reasons = [
        f"移動平均線: {technical['移動平均線']['状態']}",
        f"MACD: {technical['MACD']['状態']}",
        f"RSI: {technical['RSI']['判定']}"
    ]
    entry_rationale.append({
        'agent': 'テクニカル分析',
        'reasons': technical_reasons
    })

# エリオット波動の根拠
if elliott_score > 0:
    elliott_reasons = [
        f"波動カウント: {elliott['Intermediate Degree']['波動カウント']}",
        f"フィボナッチ目標: {elliott['価格目標']['主目標']}円",
        f"確度: {elliott['Intermediate Degree']['確度']}%"
    ]
    entry_rationale.append({
        'agent': 'エリオット波動',
        'reasons': elliott_reasons
    })

# センチメントの根拠
if sentiment_score != 0:
    sentiment_reasons = [
        f"Fear & Greed Index: {sentiment['Fear & Greed Index']['判定']}",
        f"リスク警戒度: {sentiment_risk_level}"
    ]
    entry_rationale.append({
        'agent': 'センチメント分析',
        'reasons': sentiment_reasons
    })
```

---

## 成果物フォーマット

**synthesized_strategy.md**:

```markdown
# 統合戦略レポート

生成日時: {YYYY-MM-DD HH:MM:SS}

---

## 統合判定

- **取引方向**: {買い/売り/中立}
- **信頼度**: XX%
- **推奨エントリー価格**: XX,XXX円
- **目標価格（利益確定）**: XX,XXX円
- **ストップロス価格（損切り）**: XX,XXX円
- **リスク・リワード比率**: 1対X.XX
- **期待リターン**: +X.X%
- **最大リスク**: -X.X%
- **期待値**: +X.X%

---

## エージェント別判定

| エージェント | シグナル | 信頼度 | 重み | スコア貢献 |
|-------------|---------|-------|------|----------|
| テクニカル分析 | {強気/弱気/中立} | XX% | 2.0 | +X.X |
| エリオット波動 | {Up/Down/Correction} | XX% | 1.8 | +X.X |
| センチメント分析 | {リスクオン/リスクオフ} | XX% | 1.2 | +X.X |
| **統合判定** | **{買い/売り}** | **XX%** | **5.0** | **+X.X** |

---

## エントリー根拠

### 1. テクニカル分析（重み: 2.0）
- {根拠1}
- {根拠2}
- {根拠3}

### 2. エリオット波動分析（重み: 1.8）
- {根拠1}
- {根拠2}
- {根拠3}

### 3. センチメント分析（重み: 1.2）
- {根拠1}
- {根拠2}

---

## 価格目標の統合ロジック

### エントリー価格: XX,XXX円
**算出方法**: 加重平均
- テクニカル: XX,XXX円 × 2.0 = XX,XXX
- エリオット: XX,XXX円 × 1.8 = XX,XXX
- 合計 / 総重み(5.0) = **XX,XXX円**

### 目標価格: XX,XXX円
**算出方法**: 最も保守的な値を採用（リスク回避）
- テクニカル: XX,XXX円
- エリオット: XX,XXX円
- **採用**: XX,XXX円（低い方）

### ストップロス: XX,XXX円
**算出方法**: 最も近い値を採用（リスク最小化）
- テクニカル: XX,XXX円
- エリオット: XX,XXX円
- **採用**: XX,XXX円（エントリーから近い方）

---

## リスク評価

### リスク・リワード分析
- **リスク幅**: XXX円（-X.X%）
- **リワード幅**: X,XXX円（+X.X%）
- **R:R比率**: 1:X.XX

### 期待値計算
```
期待値 = (勝率 × 平均利益) - (負け率 × 平均損失)
       = (XX% × +X.X%) - (XX% × -X.X%)
       = +X.X%
```

### リスクファクター
1. **ボラティリティ**: {高/中/低} - ATR X.X%
2. **市場リスク**: {説明}
3. **実行リスク**: {説明}

---

## 実現可能性評価

### 市場流動性
- **評価**: {高/中/低}
- **詳細**: [説明]

### ボラティリティ
- **レベル**: {高/中/低}
- **ATR**: X.X%
- **評価**: [説明]

### 実行難易度
- **評価**: {低/中/高}
- **詳細**: [説明]

### 総合実行可能性
- **評価**: {高/中/低}
- **推奨**: [実行推奨 or 見送り推奨]

---

## トレード実行ガイドライン

### 1. ポジションサイズ
- **推奨**: 資金の2%以内
- **計算例**: 資金100万円 → ポジション2万円相当

### 2. エントリータイミング
- **推奨レンジ**: XX,XXX-XX,XXX円
- **執行方法**: [指値/成行の推奨]
- **注意事項**: [具体的な注意点]

### 3. 利益確定戦略
- **第1目標**: XX,XXX円で50%決済
- **第2目標**: XX,XXX円で残り決済
- **トレーリングストップ**: [使用する場合]

### 4. 損切りルール
- **ストップロス**: XX,XXX円
- **執行**: 価格到達で即座に損切り（例外なし）
- **再エントリー**: [条件があれば]

### 5. 保有期間
- **目安**: 最大1週間（5営業日）
- **早期決済条件**: [条件があれば]

---

## シナリオ別対応

### シナリオ1: 目標価格到達（確率XX%）
**対応**: 第1目標で50%決済、第2目標で全決済

### シナリオ2: ストップロス到達（確率XX%）
**対応**: 即座に全量損切り、再エントリーは慎重に判断

### シナリオ3: レンジ相場（確率XX%）
**対応**: [対応策]

---

## 最終推奨

### 推奨アクション
**{トレード実行推奨 / 様子見推奨 / トレード非推奨}**

### 推奨理由
1. {理由1}
2. {理由2}
3. {理由3}

### 注意事項
1. {注意点1}
2. {注意点2}

---

## 次のアクション

- バックテスト検証へ
- 検証合格後、最終戦略レポート生成

---

**免責事項**: 本統合戦略は複数の分析手法を組み合わせた結果であり、将来の投資成果を保証するものではありません。投資判断は自己責任で行ってください。
```

---

## Knowledge Base参照

- 統合分析方法論: `Stock/programs/資産運用/projects/統合分析/documents/2_planning/requirements_definition.md`

---

## 使用例

### 基本的な使用

```
User: 戦略統合を実行
```

システムが自動的に：
1. 各エージェントの分析結果読み込み
2. 重み付け投票でシグナル統合
3. 価格目標統合（エントリー/目標/ストップロス）
4. リスク・リワード比率算出
5. 実行可能性評価
6. synthesized_strategy.md 生成

---

## 実行時の注意事項

1. **エージェント不一致**: 3エージェントのシグナルが分かれた場合、重みの高いテクニカル分析を優先
2. **価格乖離**: 各エージェントの価格提案が大きく乖離する場合、中央値を使用
3. **R:R比率不利**: 1:1未満の場合はトレード非推奨
4. **信頼度低下**: 総合信頼度60%未満の場合は慎重判断

---

## 更新履歴

- 2025-12-29: 初版作成（MVP Phase 1）
