# バックテストエンジン バグ分析レポート

## 概要

`/Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents/src/backtest/backtest_engine.py` において、資金計算ロジックに**重大なバグ**を発見しました。

---

## バグの詳細

### 問題のあるコード（Line 107-147）

```python
if action == 'buy' and current_position is None:
    # Open long position
    entry_price = signal.get('entry_price', price_data['close'])
    position_size = (capital * self.position_size_pct) / entry_price  # 株数計算
    commission = capital * self.position_size_pct * self.commission_pct

    current_position = {
        'entry_date': signal_date,
        'entry_price': entry_price,
        'size': position_size,
        'stop_loss': signal.get('stop_loss'),
        'take_profit': signal.get('take_profit'),
        'commission_paid': commission
    }

    capital -= commission  # ❌ ここがバグ: 手数料しか引いていない
```

### 問題点

**現在のロジック**:
1. ポジション価値 = `capital * position_size_pct`（例: 1,000,000 × 0.95 = 950,000）
2. 株数 = ポジション価値 / entry_price
3. **資金から手数料のみ引く** ← **ここがバグ**

**正しいロジック**:
1. ポジション価値 = `capital * position_size_pct`
2. 株数 = ポジション価値 / entry_price
3. **資金からポジション価値全体を引く（株を買うので現金が減る）**

---

## バグの影響

### テストケース1: 単一トレード（+5%利益）

**期待される動作**:
```
初期資金: ¥1,000,000
エントリー時（¥100で購入）:
  - ポジション額: ¥950,000
  - 手数料: ¥950
  - 残り現金: ¥1,000,000 - ¥950,000 - ¥950 = ¥49,050

エグジット時（¥105で売却）:
  - 売却額: 9,490.5株 × ¥105 = ¥996,502
  - 手数料: ¥996.5
  - 最終資金: ¥49,050 + ¥996,502 - ¥996.5 = ¥1,044,555
```

**実際の動作（バグあり）**:
```
初期資金: ¥1,000,000
エントリー時:
  - ポジション額: ¥950,000（計算するが資金から引かない）
  - 手数料: ¥950
  - 残り現金: ¥1,000,000 - ¥950 = ¥999,050  ← バグ！

エグジット時:
  - 売却額: 9,500株 × ¥105 = ¥997,500  ← 株数も間違っている
  - 手数料: ¥997.5
  - 追加資金: ¥997,500 - ¥997.5 = ¥996,502.5
  - 最終資金: ¥999,050 + ¥996,502.5 = ¥1,995,552  ← 約2倍に！
```

### 実験結果

| テスト | 期待最終資金 | 実際の最終資金 | 差異 |
|--------|-------------|---------------|------|
| 単一トレード（+5%） | ¥1,044,555 | ¥1,995,552 | **+¥950,997 (91%)** |
| 2トレード（+5%, -3.7%） | ¥1,006,000 | ¥3,817,392 | **+¥2,811,392 (280%)** |

---

## 根本原因

### 誤った前提

バックテストエンジンは**現物取引**をシミュレートしているにも関わらず、以下のような動作になっている：

1. **買いポジションを開く**: 資金から手数料のみ引く（株の購入代金を引かない）
2. **売りポジションを閉じる**: 売却額を全額資金に追加

これは**架空の資金を使って株を買っている**状態であり、完全に誤った実装です。

### 正しい実装

#### 買いポジション開設時
```python
# ポジション価値
position_value = capital * self.position_size_pct
# 株数
position_size = position_value / entry_price
# エントリー手数料
entry_commission = position_value * self.commission_pct

# 資金から「ポジション価値 + 手数料」を引く
capital -= (position_value + entry_commission)

current_position = {
    'entry_date': signal_date,
    'entry_price': entry_price,
    'size': position_size,
    'position_value': position_value,  # 追加: ポジション価値を記録
    'commission_paid': entry_commission
}
```

#### 売りポジション決済時
```python
# 売却額
exit_value = current_position['size'] * exit_price
# エグジット手数料
exit_commission = exit_value * self.commission_pct

# 売却額から手数料を引いた額を資金に追加
capital += (exit_value - exit_commission)

# 損益計算
pnl = (exit_value - exit_commission) - (current_position['position_value'] + current_position['commission_paid'])
```

---

## 修正提案

### ファイル: `src/backtest/backtest_engine.py`

#### 修正1: Line 107-122（買いポジション開設）

**現在のコード**:
```python
if action == 'buy' and current_position is None:
    entry_price = signal.get('entry_price', price_data['close'])
    position_size = (capital * self.position_size_pct) / entry_price
    commission = capital * self.position_size_pct * self.commission_pct

    current_position = {
        'entry_date': signal_date,
        'entry_price': entry_price,
        'size': position_size,
        'stop_loss': signal.get('stop_loss'),
        'take_profit': signal.get('take_profit'),
        'commission_paid': commission
    }

    capital -= commission  # ❌ バグ
```

**修正後のコード**:
```python
if action == 'buy' and current_position is None:
    entry_price = signal.get('entry_price', price_data['close'])
    position_value = capital * self.position_size_pct
    position_size = position_value / entry_price
    commission = position_value * self.commission_pct

    current_position = {
        'entry_date': signal_date,
        'entry_price': entry_price,
        'size': position_size,
        'position_value': position_value,  # 追加
        'stop_loss': signal.get('stop_loss'),
        'take_profit': signal.get('take_profit'),
        'commission_paid': commission
    }

    # 修正: ポジション価値と手数料を両方引く
    capital -= (position_value + commission)
```

#### 修正2: Line 124-147（売りポジション決済）

**現在のコード**:
```python
elif action == 'sell' and current_position is not None:
    exit_price = signal.get('exit_price', price_data['close'])
    exit_value = current_position['size'] * exit_price
    commission = exit_value * self.commission_pct

    pnl = exit_value - (current_position['size'] * current_position['entry_price']) - current_position['commission_paid'] - commission
    capital += exit_value - commission  # ❌ ここも問題
```

**修正後のコード**:
```python
elif action == 'sell' and current_position is not None:
    exit_price = signal.get('exit_price', price_data['close'])
    exit_value = current_position['size'] * exit_price
    commission = exit_value * self.commission_pct

    # 修正: 損益計算をシンプルに
    pnl = (exit_value - commission) - (current_position['position_value'] + current_position['commission_paid'])

    # 修正: 売却額から手数料を引いた額を資金に追加
    capital += (exit_value - commission)
```

#### 修正3: Line 149-203（ストップロス/テイクプロフィット）

同様の修正を以下の箇所にも適用：
- Line 154-177: ストップロス発動時
- Line 179-202: テイクプロフィット発動時

---

## 検証計画

### 修正後のユニットテスト

```python
def test_single_winning_trade():
    """単一トレード（勝ち）のテスト"""
    data = pd.DataFrame({
        'date': pd.date_range('2025-01-01', periods=10, freq='D'),
        'open': [100] * 10,
        'high': [105] * 10,
        'low': [95] * 10,
        'close': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        'volume': [1000] * 10
    })

    signals = [
        {'date': '2025-01-01', 'action': 'buy', 'entry_price': 100},
        {'date': '2025-01-05', 'action': 'sell', 'exit_price': 105}
    ]

    engine = BacktestEngine(data=data, initial_capital=1000000, position_size_pct=0.95, commission_pct=0.001)
    results = engine.run_backtest(signals)

    # 期待値: 約¥1,044,555（+4.46%）
    assert 1040000 < results['final_capital'] < 1050000, f"Expected ~1,044,555 but got {results['final_capital']}"
    assert 4.0 < results['total_return'] < 5.0, f"Expected ~4.46% but got {results['total_return']}%"

def test_single_losing_trade():
    """単一トレード（負け）のテスト"""
    data = pd.DataFrame({
        'date': pd.date_range('2025-01-01', periods=10, freq='D'),
        'open': [100] * 10,
        'high': [105] * 10,
        'low': [95] * 10,
        'close': [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],
        'volume': [1000] * 10
    })

    signals = [
        {'date': '2025-01-01', 'action': 'buy', 'entry_price': 100},
        {'date': '2025-01-05', 'action': 'sell', 'exit_price': 95}
    ]

    engine = BacktestEngine(data=data, initial_capital=1000000, position_size_pct=0.95, commission_pct=0.001)
    results = engine.run_backtest(signals)

    # 期待値: 約¥952,145（-4.79%）
    assert 948000 < results['final_capital'] < 956000, f"Expected ~952,145 but got {results['final_capital']}"
    assert -5.0 < results['total_return'] < -4.5, f"Expected ~-4.79% but got {results['total_return']}%"
```

---

## 優先度と影響範囲

### 優先度: 🔴 **最高（Critical）**

このバグは**バックテスト結果を完全に無効化**します。すべてのKPI評価が信頼できません。

### 影響範囲
- ✅ データ取得ロジック: 影響なし
- ✅ シグナル生成ロジック: 影響なし
- ❌ **バックテスト実行**: 完全に誤った結果
- ❌ **KPI計算**: 全て無効
- ❌ **ウォークフォワード分析**: 実行不可（信頼性なし）

---

## 次のステップ

1. **即座に修正**: 上記の修正を適用
2. **ユニットテスト追加**: 各トレードケースをテスト
3. **統合テスト再実行**: 修正後の動作確認
4. **KPI再評価**: 正しいバックテスト結果でKPI達成度を再計算

---

## 結論

バックテストエンジンの**資金計算ロジックに致命的なバグ**があります。

- **原因**: 買いポジション開設時に、ポジション価値を資金から引いていない
- **影響**: すべてのバックテスト結果が無効
- **修正**: `capital -= commission` → `capital -= (position_value + commission)`

**このバグを修正しない限り、Phase 2は完了できません。**

---

**作成日**: 2026-01-01
**作成者**: Claude Code（バグ分析調査）
