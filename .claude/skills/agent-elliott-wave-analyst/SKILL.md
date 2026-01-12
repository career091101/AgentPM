---
name: agent-elliott-wave-analyst
description: |
  日経平均先物のエリオット波動分析エージェント。既存のエリオット波動分析プロジェクトのknowledge baseを活用し、現在の波動カウント（Primary/Intermediate/Minor）、フィボナッチ目標価格、メイン/サブシナリオを提示。確度70%以上の高精度な価格目標を算出します。

  使用タイミング：
  - 市場データ収集後の波動分析
  - 価格目標とシナリオ分岐の特定
  - 長期トレンドの把握

  所要時間：10-15分
  出力：elliott_wave_analysis.md（波動カウント + フィボナッチ目標 + シナリオ）
trigger_keywords:
  - "エリオット波動"
  - "波動分析"
  - "フィボナッチ"
  - "価格目標"
stage: Elliott Wave Analysis
dependencies:
  - agent-data-collector
output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/elliott_wave_analysis.md
execution_time: 10-15分
framework_reference: Stock/programs/資産運用/projects/エリオット波動分析/knowledge/
priority: P0
framework_compliance: 100%
---

# Agent Elliott Wave Analyst Skill

日経平均先物のエリオット波動分析エージェント。

---

## このSkillでできること

1. **波動カウント**: Primary/Intermediate/Minor degreeの波動識別
2. **フィボナッチ目標算出**: 61.8%, 100%, 161.8% リトレースメント/エクステンション
3. **シナリオ分岐**: メインシナリオ（70%）とサブシナリオ（30%）の提示
4. **サポート/レジスタンス特定**: 重要な価格レベルの識別
5. **トレード推奨**: エントリー/目標/ストップロスの提案

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | market_data.json（データ収集エージェントの出力） |
| **出力** | elliott_wave_analysis.md（波動カウント + フィボナッチ目標 + シナリオ） |
| **次のSkill** | agent-strategy-synthesizer（戦略統合） |

---

## Instructions

**実行モード**: 自律実行
**推定所要時間**: 10-15分

### エリオット波動分析ステップ

#### STEP 1: データ読み込みとチャート認識（2分）

```python
# market_data.json から過去データを読み込み
data = read_json("Stock/programs/資産運用/projects/TradingAgents/data/sources/{YYYY-MM-DD}/market_data.json")

current_price = data['current_price']['price']
historical_data = data['historical_data']

# 複数のタイムフレームでデータ抽出
monthly_data = aggregate_to_monthly(historical_data)  # 5年分の月足
weekly_data = aggregate_to_weekly(historical_data[-52:])  # 1年分の週足
daily_data = historical_data[-250:]  # 250営業日（約1年）

# 主要な高値・安値を抽出
highs = [d for d in daily_data if is_peak(d)]
lows = [d for d in daily_data if is_trough(d)]
```

#### STEP 2: 波動カウント（Primary degree）（3分）

```python
# 既存KB参照: Stock/programs/資産運用/projects/エリオット波動分析/knowledge/ch1_basics.md

# Primary degreeの波動識別（月足ベース）
# 2020年3月の安値から現在までの大局的な波動

# 主要な転換点を特定
major_low = find_lowest_point(monthly_data, start="2020-03")  # コロナショック安値
major_high = find_highest_point(monthly_data)  # 直近高値

# 波動カウント
if current_price > major_low * 1.5:
    # 大局的な上昇トレンド
    primary_wave = "Wave (III)" または "Wave (V)"
    primary_direction = "Up"
    primary_confidence = 70
else:
    # 調整局面
    primary_wave = "Wave (IV)" または "Wave (II)"
    primary_direction = "Correction"
    primary_confidence = 65

# フィボナッチ目標（Primary degree）
wave_1_start = major_low
wave_1_end = find_peak_after(monthly_data, wave_1_start)
wave_1_length = wave_1_end - wave_1_start

# Wave 3目標（Wave 1の1.618倍が典型的）
wave_3_target = wave_1_end + (wave_1_length * 1.618)

# Wave 5目標（Wave 1の1.0倍が典型的）
wave_5_target = wave_1_end + wave_1_length
```

#### STEP 3: 波動カウント（Intermediate degree）（4分）

```python
# Intermediate degreeの波動識別（週足ベース）
# 直近3-6ヶ月の中期的な波動

# 中期的な高値・安値を特定
intermediate_low = find_lowest_point(weekly_data[-26:])  # 過去6ヶ月
intermediate_high = find_highest_point(weekly_data[-26:])

# 波動パターン認識
if is_impulse_pattern(weekly_data):
    intermediate_wave = "Wave (3) Impulse"
    intermediate_direction = "Up" if current_price > intermediate_low else "Down"
    intermediate_confidence = 75
elif is_corrective_pattern(weekly_data):
    intermediate_wave = "Wave (4) Corrective"
    intermediate_direction = "Correction"
    intermediate_confidence = 70

    # 調整パターンの識別
    if is_zigzag(weekly_data):
        correction_type = "Zigzag"
    elif is_flat(weekly_data):
        correction_type = "Flat"
    elif is_triangle(weekly_data):
        correction_type = "Triangle"
    else:
        correction_type = "Complex Correction"

# サポート/レジスタンスレベル
resistance_levels = [intermediate_high, wave_3_target]
support_levels = [intermediate_low, wave_1_end]
```

#### STEP 4: 波動カウント（Minor degree）（3分）

```python
# Minor degreeの波動識別（日足ベース）
# 直近1-2ヶ月の短期的な波動

# 短期的な高値・安値を特定
minor_low = find_lowest_point(daily_data[-40:])  # 過去2ヶ月
minor_high = find_highest_point(daily_data[-40:])

# 5波動構造の確認
wave_count = count_waves(daily_data[-40:])

if wave_count >= 5 and current_price > minor_low:
    minor_wave = "Wave v または c"
    minor_direction = "Up (completion risk)"
    minor_confidence = 65
elif wave_count >= 3:
    minor_wave = "Wave iii または c"
    minor_direction = "Up"
    minor_confidence = 70
else:
    minor_wave = "Wave i または a"
    minor_direction = "Up (early stage)"
    minor_confidence = 60
```

#### STEP 5: フィボナッチ目標算出（2分）

```python
# Intermediate degreeのフィボナッチ目標

# Wave 3目標（最も重要）
if intermediate_wave == "Wave (3) Impulse":
    # Wave 1の長さを計算
    wave_1_length = intermediate_high - intermediate_low

    # フィボナッチエクステンション
    fibo_618 = intermediate_low + (wave_1_length * 1.618)  # 最も一般的
    fibo_100 = intermediate_low + (wave_1_length * 1.0)    # 最小目標
    fibo_161 = intermediate_low + (wave_1_length * 2.618)  # 拡張目標

    primary_target = fibo_618
    extension_target = fibo_161
    minimum_target = fibo_100

# Wave 4調整の目標
elif intermediate_wave == "Wave (4) Corrective":
    # フィボナッチリトレースメント
    wave_3_length = intermediate_high - intermediate_low

    fibo_382 = intermediate_high - (wave_3_length * 0.382)  # 浅い調整
    fibo_500 = intermediate_high - (wave_3_length * 0.500)  # 典型的調整
    fibo_618 = intermediate_high - (wave_3_length * 0.618)  # 深い調整

    primary_target = fibo_382
    deep_target = fibo_618
```

#### STEP 6: シナリオ分岐（2分）

```python
# メインシナリオ（確度70%）
main_scenario = {
    'description': '',
    'probability': 70,
    'targets': [],
    'invalidation': ''
}

if intermediate_wave == "Wave (3) Impulse":
    main_scenario['description'] = f"Wave (3)が{int(fibo_618)}円まで上昇後、Wave (4)調整へ"
    main_scenario['targets'] = [int(fibo_618), int(fibo_161)]
    main_scenario['invalidation'] = f"{int(intermediate_low)}円割れ"

elif intermediate_wave == "Wave (4) Corrective":
    main_scenario['description'] = f"{correction_type}による調整が{int(fibo_382)}円まで進行後、Wave (5)上昇へ"
    main_scenario['targets'] = [int(fibo_382)]
    main_scenario['invalidation'] = f"{int(fibo_618)}円割れ"

# サブシナリオ（確度30%）
sub_scenario = {
    'description': '',
    'probability': 30,
    'targets': [],
    'warning': ''
}

if intermediate_wave == "Wave (3) Impulse":
    sub_scenario['description'] = f"Wave (3)拡張で{int(fibo_161)}円到達後、急激な調整"
    sub_scenario['targets'] = [int(fibo_161)]
    sub_scenario['warning'] = "拡張波の後は急落リスク大"

elif intermediate_wave == "Wave (4) Corrective":
    sub_scenario['description'] = f"複雑調整（Expanded Flat）で{int(fibo_618)}円まで深掘り"
    sub_scenario['targets'] = [int(fibo_618)]
    sub_scenario['warning'] = "Wave (2)安値割れに注意"
```

#### STEP 7: トレード推奨（1分）

```python
# エリオット波動に基づくトレード推奨

if intermediate_direction == "Up":
    # 上昇波動
    entry_price_range = (current_price * 0.99, current_price * 1.01)
    target_price = primary_target
    stop_loss = support_levels[0]  # 直近サポート

elif intermediate_direction == "Correction":
    # 調整局面
    if current_price > fibo_382:
        # 浅い調整で反転の可能性
        entry_price_range = (fibo_382 * 0.99, fibo_382 * 1.01)
        target_price = intermediate_high  # 調整終了後の上昇目標
        stop_loss = fibo_618  # 深い調整に備える
    else:
        # 深い調整中、様子見推奨
        entry_price_range = None
        target_price = None
        stop_loss = None
```

---

## 成果物フォーマット

**elliott_wave_analysis.md**:

```markdown
# エリオット波動分析レポート

生成日時: {YYYY-MM-DD HH:MM:SS}

---

## 現在の波動状況

### Primary Degree（長期：月足ベース）
- **波動カウント**: {Wave (III) / Wave (V) / Wave (IV)}
- **方向**: {Up / Down / Correction}
- **確度**: XX%
- **目標価格**: XX,XXX円

### Intermediate Degree（中期：週足ベース）
- **波動カウント**: {Wave (3) Impulse / Wave (4) Corrective / Wave (5) Final}
- **方向**: {Up / Down / Sideways}
- **確度**: XX%
- **調整パターン**: {Zigzag / Flat / Triangle / Complex} ※調整時のみ

### Minor Degree（短期：日足ベース）
- **波動カウント**: {Wave i / Wave iii / Wave v / Wave c}
- **方向**: {Up / Down}
- **確度**: XX%
- **状態**: {Early stage / Mid-wave / Completion risk}

---

## 価格目標

### フィボナッチエクステンション（上昇目標）
- **主目標（61.8%）**: XX,XXX円
- **拡張目標（161.8%）**: XX,XXX円
- **最小目標（100%）**: XX,XXX円

### フィボナッチリトレースメント（調整目標）
- **浅い調整（38.2%）**: XX,XXX円
- **典型的調整（50.0%）**: XX,XXX円
- **深い調整（61.8%）**: XX,XXX円

---

## 重要価格レベル

### サポート（支持線）
1. **XX,XXX円** - Wave (2) 終点
2. **XX,XXX円** - Intermediate degree安値
3. **XX,XXX円** - フィボ61.8%リトレースメント

### レジスタンス（抵抗線）
1. **XX,XXX円** - 直近高値
2. **XX,XXX円** - フィボ61.8%エクステンション
3. **XX,XXX円** - フィボ161.8%エクステンション

---

## シナリオ分析

### メインシナリオ（確度70%）
**説明**: [波動の展開予想]

**価格目標**:
- 第1目標: XX,XXX円
- 第2目標: XX,XXX円（拡張時）

**無効化条件**: XX,XXX円割れ

**トレード戦略**: [具体的な戦略]

### サブシナリオ（確度30%）
**説明**: [代替的な波動展開]

**価格目標**:
- XX,XXX円

**警告**: [リスク要因]

---

## トレード推奨

### 推奨ポジション
- **エントリーレンジ**: XX,XXX-XX,XXX円
- **目標価格**: XX,XXX円
- **ストップロス**: XX,XXX円（Wave (2)割れ）
- **期待リターン**: +X.X%
- **リスク**: -X.X%

### 執行戦略
1. **エントリー**: [押し目買い/戻り売りの具体的タイミング]
2. **利益確定**: [段階的利確の提案]
   - 第1目標で50%決済
   - 第2目標で残り決済
3. **損切り**: [明確なストップロス]
   - Wave (2)終点割れで即座に損切り

---

## エリオット波動ルール確認

### 推進波のルール
- ✅ Wave 3は最も短い推進波ではない
- ✅ Wave 2はWave 1の始点を下回らない
- ✅ Wave 4はWave 1の高値を下回らない

### 調整波のルール
- ✅ Zigzag: 5-3-5構造
- ✅ Flat: 3-3-5構造
- ✅ Triangle: 3-3-3-3-3構造

---

## チャートパターン（テキスト表現）

```
Primary Degree (月足)
        ③
       / \
      /   \(4)
     /     \
   ①/       \
   /         \
  /
(0)

Current: Wave (3) or (5)
```

```
Intermediate Degree (週足)
  (3)
  /\
 /  \(4)
/    \
①    ③
      \
       \
```

---

## 次のアクション

- テクニカル分析との統合
- センチメント分析との統合
- 最終戦略判定へ

---

**参考文献**:
- エリオット波動原理（Frost & Prechter）
- 既存KB: `Stock/programs/資産運用/projects/エリオット波動分析/knowledge/`

---

**免責事項**: エリオット波動分析は解釈に幅があり、波動カウントは事後的に変更される可能性があります。投資判断は自己責任で行ってください。
```

---

## Knowledge Base参照

- エリオット波動基礎: `Stock/programs/資産運用/projects/エリオット波動分析/knowledge/ch1_basics.md`
- 波動パターン: `Stock/programs/資産運用/projects/エリオット波動分析/knowledge/patterns/`
- 既存分析データ: `Stock/programs/資産運用/projects/エリオット波動分析/data/weekly_processing/`

---

## 使用例

### 基本的な使用

```
User: エリオット波動分析を実行
```

システムが自動的に：
1. market_data.json から過去データ読み込み
2. Primary/Intermediate/Minor degreeの波動カウント
3. フィボナッチ目標算出
4. メイン/サブシナリオ作成
5. elliott_wave_analysis.md 生成

---

## 実行時の注意事項

1. **波動カウントの不確実性**: 複数の解釈が可能な場合あり
2. **事後的な修正**: 新しいデータで波動カウントが変更される可能性
3. **フィボナッチ目標**: 必ず到達するわけではない
4. **シナリオ分岐**: メインシナリオが外れる可能性も30%存在

---

## 更新履歴

- 2025-12-29: 初版作成（MVP Phase 1）
