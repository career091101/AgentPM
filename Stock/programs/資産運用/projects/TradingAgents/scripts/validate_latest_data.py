#!/usr/bin/env python3
"""
最新データ検証スクリプト

最新30日間のデータを取得し、品質・動作確認を行う。

Usage:
    python3 scripts/validate_latest_data.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data.real_data_loader import RealDataLoader
from src.utils.market_regime import MarketRegimeDetector
from src.strategy.adaptive_strategy import AdaptiveStrategy
from datetime import datetime, timedelta
import pandas as pd


def validate_latest_data():
    """Validate latest 30 days of data"""
    print("=" * 70)
    print("最新データ検証開始")
    print("=" * 70)

    # 1. データ取得
    print("\n1. 最新30日間データ取得...")
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d")

    loader = RealDataLoader(
        ticker="^N225",
        start_date=start_date,
        end_date=end_date
    )

    try:
        data = loader.fetch_data()
        print(f"   ✅ データ取得成功: {len(data)}ポイント")
    except Exception as e:
        print(f"   ❌ データ取得失敗: {e}")
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
    expected_days = 30
    actual_days = len(data[data.index >= (datetime.now() - timedelta(days=30))])
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

    except Exception as e:
        print(f"   ❌ シグナル生成失敗: {e}")
        return False

    print("\n" + "=" * 70)
    print("✅ 最新データ検証完了: 全チェック成功")
    print("=" * 70)

    return True


if __name__ == "__main__":
    success = validate_latest_data()
    sys.exit(0 if success else 1)
