#!/usr/bin/env python3
"""
バックテスト検証エージェント
統合戦略を過去データで検証し、シャープレシオ・WF効率・レジーム別評価を実施
"""

import json
import numpy as np
from datetime import datetime
from pathlib import Path

def backtest_validator():
    """バックテスト検証のメイン処理"""

    print("🔄 バックテスト検証開始")
    print()

    # ============================================
    # STEP 1: データ読み込み
    # ============================================
    print("1️⃣  データ読み込み中...")

    # 統合戦略の読み込み
    with open('data/results/2026-01-02/synthesized_strategy.json', 'r') as f:
        strategy = json.load(f)

    entry_price = strategy['pricing']['entry']
    target_price = strategy['pricing']['target']

    # ストップロスの修正（統合戦略の計算ミス対応）
    # 最大リスク-1.79%からストップロスを再計算
    max_risk_pct = abs(strategy['risk_reward']['max_risk'])
    stop_loss = entry_price * (1 - max_risk_pct / 100)

    print(f"   エントリー: {entry_price:,.2f}円")
    print(f"   目標価格: {target_price:,.2f}円")
    print(f"   ストップロス: {stop_loss:,.2f}円（修正: 最大リスク-{max_risk_pct:.2f}%から再計算）")

    # 市場データの読み込み
    with open('data/sources/2026-01-02/market_data.json', 'r') as f:
        market_data = json.load(f)

    historical_data = market_data['historical_data']

    print(f"   ヒストリカルデータ: {len(historical_data)}営業日")
    print()

    # ============================================
    # STEP 2: データ分割（Train 60% / Test 40%）
    # ============================================
    print("2️⃣  データ分割中（Train 60% / Test 40%）...")

    total_points = len(historical_data)
    train_size = int(total_points * 0.6)

    train_data = historical_data[:train_size]
    test_data = historical_data[train_size:]

    print(f"   Train期間: {train_data[0]['date']} ~ {train_data[-1]['date']} ({len(train_data)}日)")
    print(f"   Test期間: {test_data[0]['date']} ~ {test_data[-1]['date']} ({len(test_data)}日)")
    print()

    # ============================================
    # STEP 3: Train期間でのバックテスト
    # ============================================
    print("3️⃣  Train期間バックテスト実行中...")

    train_results = run_backtest(train_data, entry_price, target_price, stop_loss)

    print(f"   総トレード数: {train_results['total_trades']}回")
    print(f"   勝ちトレード: {train_results['winning_trades']}回")
    print(f"   負けトレード: {train_results['losing_trades']}回")
    print(f"   勝率: {train_results['win_rate']:.1f}%")
    print(f"   平均利益: {train_results['avg_profit']:.2f}%")
    print(f"   平均損失: {train_results['avg_loss']:.2f}%")
    print(f"   シャープレシオ: {train_results['sharpe_ratio']:.2f}")
    print(f"   最大ドローダウン: {train_results['max_drawdown']:.2f}%")
    print()

    # ============================================
    # STEP 4: Test期間でのバックテスト
    # ============================================
    print("4️⃣  Test期間バックテスト実行中...")

    test_results = run_backtest(test_data, entry_price, target_price, stop_loss)

    print(f"   総トレード数: {test_results['total_trades']}回")
    print(f"   勝ちトレード: {test_results['winning_trades']}回")
    print(f"   負けトレード: {test_results['losing_trades']}回")
    print(f"   勝率: {test_results['win_rate']:.1f}%")
    print(f"   平均利益: {test_results['avg_profit']:.2f}%")
    print(f"   平均損失: {test_results['avg_loss']:.2f}%")
    print(f"   シャープレシオ: {test_results['sharpe_ratio']:.2f}")
    print(f"   最大ドローダウン: {test_results['max_drawdown']:.2f}%")
    print()

    # ============================================
    # STEP 5: ウォークフォワード効率算出
    # ============================================
    print("5️⃣  ウォークフォワード効率算出中...")

    # WF効率 = (Test期間のシャープレシオ / Train期間のシャープレシオ) × 100%
    if train_results['sharpe_ratio'] > 0:
        wf_efficiency = (test_results['sharpe_ratio'] / train_results['sharpe_ratio']) * 100
    else:
        wf_efficiency = 0

    print(f"   Train期間シャープレシオ: {train_results['sharpe_ratio']:.2f}")
    print(f"   Test期間シャープレシオ: {test_results['sharpe_ratio']:.2f}")
    print(f"   WF効率: {wf_efficiency:.1f}%（基準: 50%以上）")
    print()

    # ============================================
    # STEP 6: マーケットレジーム別評価
    # ============================================
    print("6️⃣  マーケットレジーム別評価中...")

    regime_results = evaluate_by_regime(historical_data, entry_price, target_price, stop_loss)

    print(f"   上昇相場: {regime_results['uptrend']['trades']}トレード、シャープレシオ {regime_results['uptrend']['sharpe']:.2f}")
    print(f"   下降相場: {regime_results['downtrend']['trades']}トレード、シャープレシオ {regime_results['downtrend']['sharpe']:.2f}")
    print(f"   レンジ相場: {regime_results['sideways']['trades']}トレード、シャープレシオ {regime_results['sideways']['sharpe']:.2f}")
    print()

    # ============================================
    # STEP 7: 合格/不合格判定
    # ============================================
    print("7️⃣  合格/不合格判定中...")

    # 判定基準
    sharpe_threshold = 1.0
    wf_threshold = 50.0
    regime_sharpe_threshold = 0.3

    # 各基準の判定
    sharpe_pass = train_results['sharpe_ratio'] >= sharpe_threshold
    wf_pass = wf_efficiency >= wf_threshold
    regime_pass = (
        regime_results['uptrend']['sharpe'] > regime_sharpe_threshold and
        regime_results['downtrend']['sharpe'] > regime_sharpe_threshold and
        regime_results['sideways']['sharpe'] > regime_sharpe_threshold
    )

    overall_pass = sharpe_pass and wf_pass and regime_pass

    print(f"   シャープレシオ ≥ {sharpe_threshold}: {'✅ 合格' if sharpe_pass else '❌ 不合格'} ({train_results['sharpe_ratio']:.2f})")
    print(f"   WF効率 ≥ {wf_threshold}%: {'✅ 合格' if wf_pass else '❌ 不合格'} ({wf_efficiency:.1f}%)")
    print(f"   全レジームでシャープレシオ > {regime_sharpe_threshold}: {'✅ 合格' if regime_pass else '❌ 不合格'}")
    print()

    if overall_pass:
        print("✅ バックテスト検証: 合格")
        validation_status = "合格"
    else:
        print("❌ バックテスト検証: 不合格")
        validation_status = "不合格"

        # 不合格の場合の対応提案
        print()
        print("📋 対応提案:")
        if not sharpe_pass:
            print("   - シャープレシオが基準未満 → 戦略パラメータの調整が必要")
        if not wf_pass:
            print("   - WF効率が低い → オーバーフィッティングの可能性、汎用性向上が必要")
        if not regime_pass:
            print("   - 特定レジームで性能不足 → レジーム別戦略の検討が必要")

    print()

    # ============================================
    # JSON保存
    # ============================================
    output_data = {
        'timestamp': datetime.now().isoformat(),
        'validation_status': validation_status,
        'strategy': {
            'entry': entry_price,
            'target': target_price,
            'stop_loss': stop_loss
        },
        'data_split': {
            'train_period': f"{train_data[0]['date']} ~ {train_data[-1]['date']}",
            'test_period': f"{test_data[0]['date']} ~ {test_data[-1]['date']}",
            'train_size': len(train_data),
            'test_size': len(test_data)
        },
        'train_performance': train_results,
        'test_performance': test_results,
        'walk_forward': {
            'efficiency': round(wf_efficiency, 2),
            'pass': int(wf_pass)
        },
        'regime_analysis': regime_results,
        'criteria': {
            'sharpe_ratio': {'threshold': sharpe_threshold, 'pass': int(sharpe_pass)},
            'wf_efficiency': {'threshold': wf_threshold, 'pass': int(wf_pass)},
            'regime_sharpe': {'threshold': regime_sharpe_threshold, 'pass': int(regime_pass)}
        },
        'overall_pass': int(overall_pass)
    }

    output_file = 'data/results/2026-01-02/backtest_validation.json'
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"✅ バックテスト検証完了")
    print(f"   出力ファイル: {output_file}")

    return output_data


def run_backtest(data, entry_price, target_price, stop_loss):
    """
    戦略のバックテストを実行

    ロジック:
    1. 価格がエントリー価格以下になったらエントリー（買い）
    2. エントリー後、目標価格到達で利益確定、ストップロス到達で損切り
    3. 全トレードのリターンからシャープレシオを計算
    """

    trades = []
    in_position = False
    entry_date = None
    entry_actual = None

    for i, day in enumerate(data):
        close_price = day['close']

        # エントリー条件: 価格がエントリー価格以下
        if not in_position and close_price <= entry_price:
            in_position = True
            entry_date = day['date']
            entry_actual = close_price

        # ポジション保有中
        elif in_position:
            # 利益確定: 価格が目標価格以上
            if close_price >= target_price:
                profit = ((target_price - entry_actual) / entry_actual) * 100
                trades.append({
                    'entry_date': entry_date,
                    'exit_date': day['date'],
                    'entry_price': entry_actual,
                    'exit_price': target_price,
                    'profit_pct': profit,
                    'outcome': 'win'
                })
                in_position = False

            # 損切り: 価格がストップロス以下
            elif close_price <= stop_loss:
                loss = ((stop_loss - entry_actual) / entry_actual) * 100
                trades.append({
                    'entry_date': entry_date,
                    'exit_date': day['date'],
                    'entry_price': entry_actual,
                    'exit_price': stop_loss,
                    'profit_pct': loss,
                    'outcome': 'loss'
                })
                in_position = False

    # 統計計算
    if len(trades) == 0:
        return {
            'total_trades': 0,
            'winning_trades': 0,
            'losing_trades': 0,
            'win_rate': 0,
            'avg_profit': 0,
            'avg_loss': 0,
            'sharpe_ratio': 0,
            'max_drawdown': 0
        }

    winning_trades = [t for t in trades if t['outcome'] == 'win']
    losing_trades = [t for t in trades if t['outcome'] == 'loss']

    win_rate = (len(winning_trades) / len(trades)) * 100

    avg_profit = np.mean([t['profit_pct'] for t in winning_trades]) if winning_trades else 0
    avg_loss = np.mean([t['profit_pct'] for t in losing_trades]) if losing_trades else 0

    # シャープレシオ = (平均リターン - リスクフリーレート) / リターンの標準偏差
    # リスクフリーレート = 0% と仮定
    returns = [t['profit_pct'] for t in trades]
    avg_return = np.mean(returns)
    std_return = np.std(returns)

    sharpe_ratio = (avg_return / std_return) if std_return > 0 else 0

    # 最大ドローダウン計算
    cumulative_returns = np.cumsum(returns)
    running_max = np.maximum.accumulate(cumulative_returns)
    drawdown = running_max - cumulative_returns
    max_drawdown = np.max(drawdown) if len(drawdown) > 0 else 0

    return {
        'total_trades': len(trades),
        'winning_trades': len(winning_trades),
        'losing_trades': len(losing_trades),
        'win_rate': round(win_rate, 1),
        'avg_profit': round(avg_profit, 2),
        'avg_loss': round(avg_loss, 2),
        'sharpe_ratio': round(sharpe_ratio, 2),
        'max_drawdown': round(max_drawdown, 2),
        'trades': trades
    }


def evaluate_by_regime(data, entry_price, target_price, stop_loss):
    """マーケットレジーム別にバックテストを実行"""

    # レジーム判定: SMA50ベース
    # 上昇相場: 価格 > SMA50 かつ SMA50が上昇
    # 下降相場: 価格 < SMA50 かつ SMA50が下降
    # レンジ相場: その他

    uptrend_data = []
    downtrend_data = []
    sideways_data = []

    for i in range(50, len(data)):
        # SMA50計算
        sma50 = np.mean([data[j]['close'] for j in range(i-50, i)])
        sma50_prev = np.mean([data[j]['close'] for j in range(i-51, i-1)])

        price = data[i]['close']

        if price > sma50 and sma50 > sma50_prev:
            uptrend_data.append(data[i])
        elif price < sma50 and sma50 < sma50_prev:
            downtrend_data.append(data[i])
        else:
            sideways_data.append(data[i])

    # 各レジームでバックテスト実行
    uptrend_results = run_backtest(uptrend_data, entry_price, target_price, stop_loss)
    downtrend_results = run_backtest(downtrend_data, entry_price, target_price, stop_loss)
    sideways_results = run_backtest(sideways_data, entry_price, target_price, stop_loss)

    return {
        'uptrend': {
            'trades': uptrend_results['total_trades'],
            'sharpe': uptrend_results['sharpe_ratio'],
            'win_rate': uptrend_results['win_rate']
        },
        'downtrend': {
            'trades': downtrend_results['total_trades'],
            'sharpe': downtrend_results['sharpe_ratio'],
            'win_rate': downtrend_results['win_rate']
        },
        'sideways': {
            'trades': sideways_results['total_trades'],
            'sharpe': sideways_results['sharpe_ratio'],
            'win_rate': sideways_results['win_rate']
        }
    }


if __name__ == "__main__":
    backtest_validator()
