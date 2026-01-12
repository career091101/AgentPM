---
name: agent-technical-analyst
description: |
  日経平均先物のテクニカル分析エージェント。8種類のテクニカル指標（移動平均線、MACD、RSI、ボリンジャーバンド、ATR、出来高、VWMA、ストキャスティクス）を計算し、総合的な売買シグナルを生成。エントリー/エグジット/ストップロス価格を提案し、信頼度スコアを算出します。

  使用タイミング：
  - 市場データ収集後のテクニカル分析
  - 価格トレンドとモメンタムの評価
  - エントリー/エグジットポイントの特定

  所要時間：8-12分
  出力：technical_analysis.md（シグナル統合判定 + 各指標詳細）
trigger_keywords:
  - "テクニカル分析"
  - "指標分析"
  - "移動平均"
  - "MACD"
  - "RSI"
stage: Technical Analysis
dependencies:
  - agent-data-collector
output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/technical_analysis.md
execution_time: 8-12分
framework_reference: Stock/programs/資産運用/projects/TradingAgents/knowledge/technical_indicators.md
priority: P0
framework_compliance: 100%
---

# Agent Technical Analyst Skill

日経平均先物のテクニカル分析エージェント。

---

## このSkillでできること

1. **8種類のテクニカル指標計算**: MA, MACD, RSI, BB, ATR, 出来高, VWMA, ストキャスティクス
2. **売買シグナル生成**: 各指標から買い/売り/中立シグナルを判定
3. **価格目標算出**: エントリー/エグジット/ストップロス価格の提案
4. **信頼度スコアリング**: シグナルの強さを0-100%で評価
5. **重み付け統合**: 各指標に重みを設定し、総合判定を算出

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | market_data.json（データ収集エージェントの出力） |
| **出力** | technical_analysis.md（総合シグナル + 各指標詳細 + 価格提案） |
| **次のSkill** | agent-strategy-synthesizer（戦略統合） |

---

## Instructions

**実行モード**: 自律実行
**推定所要時間**: 8-12分

### テクニカル分析ステップ

#### STEP 1: データ読み込み（1分）

```python
# market_data.json から過去データを読み込み
data = read_json("Stock/programs/資産運用/projects/TradingAgents/data/sources/{YYYY-MM-DD}/market_data.json")

current_price = data['current_price']['price']
historical_data = data['historical_data']  # 5年分のOHLCVデータ

# 最新250日分を抽出（1年分）
recent_data = historical_data[-250:]
```

#### STEP 2: テクニカル指標計算（5分）

##### 2-1. 移動平均線（SMA50, SMA200）

```python
# SMA50（50日単純移動平均）
sma50 = sum([d['close'] for d in recent_data[-50:]]) / 50

# SMA200（200日単純移動平均）
sma200 = sum([d['close'] for d in recent_data[-200:]]) / 200

# ゴールデンクロス/デッドクロス判定
if sma50 > sma200 and current_price > sma50:
    ma_signal = "買い"
    ma_strength = 2.0
elif sma50 < sma200 and current_price < sma50:
    ma_signal = "売り"
    ma_strength = 2.0
elif current_price > sma50:
    ma_signal = "やや買い"
    ma_strength = 1.5
elif current_price < sma50:
    ma_signal = "やや売り"
    ma_strength = 1.5
else:
    ma_signal = "中立"
    ma_strength = 1.0
```

##### 2-2. MACD（移動平均収束拡散指標）

```python
# EMA12, EMA26を計算
ema12 = calculate_ema(recent_data, period=12)
ema26 = calculate_ema(recent_data, period=26)

# MACD = EMA12 - EMA26
macd = ema12 - ema26

# Signal = MACD の 9日EMA
signal = calculate_ema(macd_values, period=9)

# ヒストグラム
histogram = macd - signal

# シグナル判定
if macd > signal and macd > 0:
    macd_signal = "買い"
    macd_strength = 1.8
elif macd > signal and macd < 0:
    macd_signal = "やや買い"
    macd_strength = 1.5
elif macd < signal and macd < 0:
    macd_signal = "売り"
    macd_strength = 1.8
elif macd < signal and macd > 0:
    macd_signal = "やや売り"
    macd_strength = 1.5
else:
    macd_signal = "中立"
    macd_strength = 1.0
```

##### 2-3. RSI（相対力指数）

```python
# 14日RSIを計算
gains = []
losses = []

for i in range(1, 15):
    change = recent_data[-i]['close'] - recent_data[-i-1]['close']
    if change > 0:
        gains.append(change)
        losses.append(0)
    else:
        gains.append(0)
        losses.append(abs(change))

avg_gain = sum(gains) / 14
avg_loss = sum(losses) / 14

if avg_loss == 0:
    rsi = 100
else:
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

# シグナル判定
if rsi > 70:
    rsi_signal = "売り"  # 買われすぎ
    rsi_strength = 1.6
elif rsi < 30:
    rsi_signal = "買い"  # 売られすぎ
    rsi_strength = 1.6
elif 50 < rsi < 70:
    rsi_signal = "やや買い"
    rsi_strength = 1.3
elif 30 < rsi < 50:
    rsi_signal = "やや売り"
    rsi_strength = 1.3
else:
    rsi_signal = "中立"
    rsi_strength = 1.0
```

##### 2-4. ボリンジャーバンド

```python
# 20日移動平均
sma20 = sum([d['close'] for d in recent_data[-20:]]) / 20

# 標準偏差
variance = sum([(d['close'] - sma20)**2 for d in recent_data[-20:]]) / 20
std_dev = variance ** 0.5

# バンド
upper_band = sma20 + (2 * std_dev)
lower_band = sma20 - (2 * std_dev)

# シグナル判定
if current_price > upper_band:
    bb_signal = "売り"  # 上限タッチ
    bb_strength = 1.4
elif current_price < lower_band:
    bb_signal = "買い"  # 下限タッチ
    bb_strength = 1.4
elif current_price > sma20:
    bb_signal = "やや買い"
    bb_strength = 1.2
elif current_price < sma20:
    bb_signal = "やや売り"
    bb_strength = 1.2
else:
    bb_signal = "中立"
    bb_strength = 1.0
```

##### 2-5. ATR（平均真の範囲）

```python
# 14日ATRを計算
true_ranges = []

for i in range(1, 15):
    high = recent_data[-i]['high']
    low = recent_data[-i]['low']
    prev_close = recent_data[-i-1]['close']

    tr = max(
        high - low,
        abs(high - prev_close),
        abs(low - prev_close)
    )
    true_ranges.append(tr)

atr = sum(true_ranges) / 14

# ボラティリティ評価（ATR / 現在価格）
volatility_pct = (atr / current_price) * 100

# ボラティリティ判定
if volatility_pct > 3:
    volatility_level = "高"
elif volatility_pct > 2:
    volatility_level = "中"
else:
    volatility_level = "低"
```

##### 2-6. 出来高分析

```python
# 20日平均出来高
avg_volume = sum([d['volume'] for d in recent_data[-20:]]) / 20

# 最新出来高
latest_volume = recent_data[-1]['volume']

# 出来高比率
volume_ratio = latest_volume / avg_volume

# トレンド強度判定
if volume_ratio > 1.5:
    volume_strength = "強い"
    volume_signal = "トレンド継続"
elif volume_ratio > 1.2:
    volume_strength = "中程度"
    volume_signal = "トレンド継続"
else:
    volume_strength = "弱い"
    volume_signal = "トレンド弱化"
```

##### 2-7. VWMA（出来高加重移動平均）

```python
# 20日VWMA
numerator = sum([d['close'] * d['volume'] for d in recent_data[-20:]])
denominator = sum([d['volume'] for d in recent_data[-20:]])
vwma20 = numerator / denominator

# シグナル判定
if current_price > vwma20:
    vwma_signal = "買い"
    vwma_strength = 1.5
elif current_price < vwma20:
    vwma_signal = "売り"
    vwma_strength = 1.5
else:
    vwma_signal = "中立"
    vwma_strength = 1.0
```

##### 2-8. ストキャスティクス

```python
# 14日ストキャスティクス
highest_high = max([d['high'] for d in recent_data[-14:]])
lowest_low = min([d['low'] for d in recent_data[-14:]])

# %K
k_value = ((current_price - lowest_low) / (highest_high - lowest_low)) * 100

# %D（%Kの3日移動平均）
# 簡易版として%Kのみ使用

# シグナル判定
if k_value > 80:
    stoch_signal = "売り"  # 買われすぎ
    stoch_strength = 1.4
elif k_value < 20:
    stoch_signal = "買い"  # 売られすぎ
    stoch_strength = 1.4
else:
    stoch_signal = "中立"
    stoch_strength = 1.0
```

#### STEP 3: シグナル統合（2分）

```python
# 各指標の重み
WEIGHTS = {
    'ma': 2.0,
    'macd': 1.8,
    'rsi': 1.6,
    'bb': 1.4,
    'vwma': 1.5,
    'stoch': 1.4
}

# 買い/売りスコア計算
buy_score = 0
sell_score = 0

if ma_signal in ["買い", "やや買い"]:
    buy_score += WEIGHTS['ma'] * (2.0 if ma_signal == "買い" else 1.0)
elif ma_signal in ["売り", "やや売り"]:
    sell_score += WEIGHTS['ma'] * (2.0 if ma_signal == "売り" else 1.0)

# ... 他の指標も同様に計算 ...

# 総合スコア
total_weight = sum(WEIGHTS.values())
net_score = (buy_score - sell_score) / total_weight

# 総合シグナル判定
if net_score > 0.3:
    overall_signal = "強気"
    confidence = min(100, int(net_score * 100))
elif net_score > 0.1:
    overall_signal = "やや強気"
    confidence = min(100, int(net_score * 80))
elif net_score < -0.3:
    overall_signal = "弱気"
    confidence = min(100, int(abs(net_score) * 100))
elif net_score < -0.1:
    overall_signal = "やや弱気"
    confidence = min(100, int(abs(net_score) * 80))
else:
    overall_signal = "中立"
    confidence = 50
```

#### STEP 4: 価格目標算出（1分）

```python
# エントリー価格（現在価格の±0.2%）
if overall_signal in ["強気", "やや強気"]:
    entry_price = current_price * 0.998  # -0.2%（押し目）
else:
    entry_price = current_price * 1.002  # +0.2%（戻り売り）

# 目標価格（ATRベース）
if overall_signal in ["強気", "やや強気"]:
    # 上昇目標: 現在価格 + 2×ATR
    exit_price = current_price + (2 * atr)
else:
    # 下落目標: 現在価格 - 2×ATR
    exit_price = current_price - (2 * atr)

# ストップロス（ATRベース）
if overall_signal in ["強気", "やや強気"]:
    # 買いのストップロス: エントリー - 1×ATR
    stop_loss = entry_price - atr
else:
    # 売りのストップロス: エントリー + 1×ATR
    stop_loss = entry_price + atr

# リスク・リワード比率
risk = abs(entry_price - stop_loss)
reward = abs(exit_price - entry_price)
risk_reward_ratio = reward / risk
```

---

## 成果物フォーマット

**technical_analysis.md**:

```markdown
# テクニカル分析レポート

生成日時: {YYYY-MM-DD HH:MM:SS}

---

## シグナル統合判定

- **総合シグナル**: {強気/やや強気/中立/やや弱気/弱気} (信頼度: XX%)
- **推奨取引方向**: {買い/売り}
- **推奨エントリー**: XX,XXX円（現在価格: XX,XXX円）
- **目標価格**: XX,XXX円（+X.X%）
- **ストップロス**: XX,XXX円（-X.X%）
- **リスク・リワード比率**: 1対X.XX

---

## 各指標詳細

### 1. 移動平均線
- **SMA50**: XX,XXX円
- **SMA200**: XX,XXX円
- **現在価格**: XX,XXX円
- **状態**: {ゴールデンクロス維持/デッドクロス/中立}
- **シグナル**: {買い/売り/中立} (重み: 2.0)
- **詳細**: [説明]

### 2. MACD
- **MACD**: XXX
- **Signal**: XXX
- **Histogram**: XXX
- **状態**: {ゴールデンクロス、プラス圏/デッドクロス、マイナス圏}
- **シグナル**: {買い/売り/中立} (重み: 1.8)
- **詳細**: [説明]

### 3. RSI（14日）
- **RSI値**: XX.X
- **判定**: {買われすぎ/売られすぎ/適正範囲}
- **シグナル**: {買い/売り/中立} (重み: 1.6)
- **詳細**: [説明]

### 4. ボリンジャーバンド（20日、2σ）
- **上限**: XX,XXX円
- **中心線（SMA20）**: XX,XXX円
- **下限**: XX,XXX円
- **現在位置**: {上限タッチ/上半分/中心付近/下半分/下限タッチ}
- **シグナル**: {買い/売り/中立} (重み: 1.4)
- **詳細**: [説明]

### 5. ATR（14日）
- **ATR値**: XXX円
- **ボラティリティ**: X.X%
- **レベル**: {高/中/低}
- **評価**: [説明]

### 6. 出来高分析
- **最新出来高**: X,XXX,XXX
- **平均出来高（20日）**: X,XXX,XXX
- **出来高比率**: X.XX倍
- **トレンド強度**: {強い/中程度/弱い}
- **評価**: [説明]

### 7. VWMA（20日）
- **VWMA値**: XX,XXX円
- **現在価格**: XX,XXX円
- **シグナル**: {買い/売り/中立} (重み: 1.5)
- **詳細**: [説明]

### 8. ストキャスティクス（14日）
- **%K値**: XX.X
- **判定**: {買われすぎ/売られすぎ/中立}
- **シグナル**: {買い/売り/中立} (重み: 1.4)
- **詳細**: [説明]

---

## 統合スコアリング

| 指標 | シグナル | 重み | スコア貢献 |
|-----|---------|------|----------|
| 移動平均線 | {買い/売り/中立} | 2.0 | +X.X |
| MACD | {買い/売り/中立} | 1.8 | +X.X |
| RSI | {買い/売り/中立} | 1.6 | +X.X |
| ボリンジャーバンド | {買い/売り/中立} | 1.4 | +X.X |
| VWMA | {買い/売り/中立} | 1.5 | +X.X |
| ストキャスティクス | {買い/売り/中立} | 1.4 | +X.X |
| **総合** | **{買い/売り}** | **10.7** | **+X.X (XX%)** |

---

## トレード推奨

### 推奨ポジション
- **方向**: {ロング（買い）/ショート（売り）}
- **エントリー**: XX,XXX円
- **目標価格**: XX,XXX円
- **ストップロス**: XX,XXX円
- **期待リターン**: +X.X%
- **最大リスク**: -X.X%
- **R:R比率**: 1:X.XX

### 執行戦略
1. **エントリータイミング**: [具体的なタイミング]
2. **ポジションサイズ**: 資金の2%以内推奨
3. **利益確定**: [段階的利確の提案]
4. **損切り**: [明確なストップロス設定]

---

## リスク要因

1. **ボラティリティ**: {高/中/低} - ATR {X.X%}
2. **トレンド強度**: {強い/中程度/弱い} - 出来高比率 {X.XX倍}
3. **過熱感**: RSI {XX.X} {買われすぎ/売られすぎ/適正}

---

## 次のアクション

- エリオット波動分析との統合
- センチメント分析との統合
- 最終戦略判定へ

---

**免責事項**: 本分析は過去データに基づくテクニカル指標の計算結果であり、将来の価格変動を保証するものではありません。
```

---

## Knowledge Base参照

- テクニカル指標解説: `Stock/programs/資産運用/projects/TradingAgents/knowledge/technical_indicators.md`

---

## 使用例

### 基本的な使用

```
User: テクニカル分析を実行
```

システムが自動的に：
1. market_data.json から過去データ読み込み
2. 8種類のテクニカル指標計算
3. シグナル統合判定
4. 価格目標算出
5. technical_analysis.md 生成

---

## 更新履歴

- 2025-12-29: 初版作成（MVP Phase 1）
