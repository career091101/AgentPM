#!/usr/bin/env python3
"""
最新データ検証スクリプト（サンプルデータ版）

サンプルデータを使用してシステムの動作確認を行う。

Usage:
    python3 scripts/validate_latest_data_sample.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.market_regime import MarketRegimeDetector
from src.strategy.adaptive_strategy import AdaptiveStrategy
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


def generate_sample_data(days: int = 90):
    """Generate sample OHLCV data"""
    dates = pd.date_range(
        start=datetime.now() - timedelta(days=days),
        end=datetime.now(),
        freq='D'
    )

    # Generate realistic price movements
    np.random.seed(42)
    close_prices = 40000 + np.random.randn(len(dates)).cumsum() * 100

    data = pd.DataFrame({
        'date': dates,
        'open': close_prices + np.random.randn(len(dates)) * 50,
        'high': close_prices + np.abs(np.random.randn(len(dates))) * 100,
        'low': close_prices - np.abs(np.random.randn(len(dates))) * 100,
        'close': close_prices,
        'volume': np.random.randint(100000, 1000000, len(dates))
    })

    data['date'] = pd.to_datetime(data['date'])
    data = data.set_index('date')

    return data


def validate_latest_data():
    """Validate latest 30 days of data"""
    print("=" * 70)
    print("最新データ検証開始（サンプルデータ版）")
    print("=" * 70)

    # 1. データ生成
    print("\n1. サンプルデータ生成...")
    try:
        data = generate_sample_data(days=90)
        print(f"   ✅ データ生成成功: {len(data)}ポイント")
    except Exception as e:
        print(f"   ❌ データ生成失敗: {e}")
        return False

    # 2. データ品質チェック
    print("\n2. データ品質チェック...")

    # 欠損値チェック
    missing_count = data.isnull().sum().sum()
    if missing_count > 0:
        print(f"   ⚠️  欠損値あり: {missing_count}個")
    else:
        print("   ✅ 欠損値なし")

    # 異常値チェック（0以下の価格）
    invalid_prices = (data[['open', 'high', 'low', 'close']] <= 0).any().any()
    if invalid_prices:
        print("   ❌ 異常値あり（0以下の価格）")
        return False
    else:
        print("   ✅ 異常値なし")

    # データ完全性
    expected_days = 90
    actual_days = len(data)
    completeness = (actual_days / expected_days) * 100
    print(f"   📊 データ完全性: {completeness:.1f}% ({actual_days}/{expected_days}日)")

    # 3. レジーム検出動作確認
    print("\n3. レジーム検出動作確認...")

    try:
        regime_detector = MarketRegimeDetector(data)
        regime_series = regime_detector.detect_regime_combined()
        current_regime = regime_series.iloc[-1]
        print(f"   ✅ レジーム検出成功: {current_regime}")

        # レジーム分布
        regime_dist = regime_series.value_counts()
        print(f"   📊 レジーム分布: {regime_dist.to_dict()}")
    except Exception as e:
        print(f"   ❌ レジーム検出失敗: {e}")
        import traceback
        traceback.print_exc()
        return False

    # 4. シグナル生成動作確認
    print("\n4. シグナル生成動作確認...")

    try:
        regime_params = {
            'bull': {'ma_short': 10, 'ma_long': 30, 'position_size_pct': 1.0},
            'bear': {'ma_short': 30, 'ma_long': 60, 'position_size_pct': 0.8},
            'sideways': {'bb_period': 20, 'bb_std': 2.0, 'position_size_pct': 0.9}
        }

        strategy = AdaptiveStrategy(regime_detector, regime_params)

        # 最新日のシグナル生成
        latest_date = data.index[-1]
        signal = strategy.generate_signal(data, latest_date)

        print(f"   ✅ シグナル生成成功")
        print(f"   📊 最新シグナル: {signal['action']}")
        print(f"   📊 信頼度: {signal['confidence']:.2f}")

    except Exception as e:
        print(f"   ❌ シグナル生成失敗: {e}")
        import traceback
        traceback.print_exc()
        return False

    print("\n" + "=" * 70)
    print("✅ 最新データ検証完了: 全チェック成功")
    print("=" * 70)

    return True


if __name__ == "__main__":
    success = validate_latest_data()
    sys.exit(0 if success else 1)
