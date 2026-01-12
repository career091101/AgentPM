#!/usr/bin/env python3
"""
週次戦略レポート自動生成スクリプト

Usage:
    python3 scripts/generate_weekly_report.py
    python3 scripts/generate_weekly_report.py --week-start 2025-12-23 --week-end 2025-12-27
"""

import argparse
from pathlib import Path
import pandas as pd
from datetime import datetime, timedelta
import sys
import numpy as np

# プロジェクトルート追加
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from data.real_data_loader import RealDataLoader
from strategy.adaptive_strategy import AdaptiveStrategy
from utils.market_regime import MarketRegimeDetector
from utils.visualizer import plot_equity_curve, plot_drawdown
from backtest.backtest_engine import BacktestEngine


class WeeklyReportGenerator:
    def __init__(self, week_start: str, week_end: str):
        """
        Initialize weekly report generator.

        Args:
            week_start: Week start date (YYYY-MM-DD)
            week_end: Week end date (YYYY-MM-DD)
        """
        self.week_start = pd.to_datetime(week_start)
        self.week_end = pd.to_datetime(week_end)
        self.report_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.project_root = project_root

    def fetch_data(self):
        """Fetch data for the week + lookback period"""
        print(f"  データ期間: {self.week_start.strftime('%Y-%m-%d')} 〜 {self.week_end.strftime('%Y-%m-%d')}")

        # 4週間前からデータ取得（テクニカル指標計算のため）
        lookback_start = (self.week_start - timedelta(days=30)).strftime("%Y-%m-%d")
        week_end_str = self.week_end.strftime("%Y-%m-%d")

        loader = RealDataLoader(
            ticker="^N225",
            start_date=lookback_start,
            end_date=week_end_str
        )

        self.data = loader.fetch_data()

        if self.data is None or len(self.data) == 0:
            raise ValueError("データ取得に失敗しました")

        # Ensure date column is set as index
        if 'date' in self.data.columns:
            self.data['date'] = pd.to_datetime(self.data['date'])
            self.data = self.data.set_index('date')

        self.week_data = self.data[
            (self.data.index >= self.week_start) &
            (self.data.index <= self.week_end)
        ]

        print(f"  取得データ: 全{len(self.data)}日分、今週{len(self.week_data)}日分")

    def generate_signals(self):
        """Generate trading signals for the week"""
        print(f"  レジーム検出を実行中...")

        regime_detector = MarketRegimeDetector(self.data)

        # デフォルトパラメータ
        regime_params = {
            'bull': {
                'ma_short': 10,
                'ma_long': 30,
                'position_size_pct': 1.0,
                'rsi_period': 14,
                'rsi_overbought': 70
            },
            'bear': {
                'ma_short': 30,
                'ma_long': 60,
                'position_size_pct': 0.8,
                'rsi_period': 14,
                'rsi_oversold': 30
            },
            'sideways': {
                'bb_period': 20,
                'bb_std': 2.0,
                'position_size_pct': 0.9,
                'rsi_period': 14,
                'rsi_oversold': 30,
                'rsi_overbought': 70
            }
        }

        strategy = AdaptiveStrategy(regime_detector, regime_params)

        # 週次シグナル生成
        self.signals = []
        for date in self.week_data.index:
            signal = strategy.generate_signal(self.data, date)
            if signal['action'] != 'hold':
                # バックテストエンジン用にフォーマット変換
                signal_formatted = {
                    'date': date.strftime('%Y-%m-%d'),
                    'action': signal['action'],
                    'entry_price': signal.get('price', self.data.loc[date, 'close']),
                    'stop_loss': None,  # 簡易版ではNone
                    'take_profit': None
                }
                self.signals.append(signal_formatted)

        self.regime_stats = strategy.get_regime_statistics()
        self.current_regime = strategy.current_regime if strategy.current_regime else 'sideways'

        print(f"  生成シグナル: {len(self.signals)}件")

    def calculate_performance(self):
        """Calculate weekly performance metrics"""
        print(f"  パフォーマンス計算中...")

        if len(self.signals) == 0:
            print("    シグナルがないため、デフォルト値を使用")
            self.performance = {
                'weekly_return': 0.0,
                'win_rate': 0.0,
                'sharpe_ratio': 0.0,
                'max_dd': 0.0,
                'total_trades': 0,
                'win_trades': 0,
                'lose_trades': 0,
                'profit_factor': 0.0,
                'avg_profit': 0.0,
                'avg_loss': 0.0,
            }
            self.equity_curve = pd.Series([10000000], index=[self.week_start])
            return

        # バックテストエンジンで計算
        engine = BacktestEngine(
            self.week_data,
            initial_capital=10000000,
            commission_pct=0.0005,
            slippage_pct=0.001
        )

        results = engine.run_backtest(self.signals)

        # 平均利益・損失を計算
        trades = results.get('trades', [])
        winning_pnls = [t['pnl'] for t in trades if t['pnl'] > 0]
        losing_pnls = [t['pnl'] for t in trades if t['pnl'] < 0]

        avg_profit = np.mean(winning_pnls) if winning_pnls else 0.0
        avg_loss = np.mean(losing_pnls) if losing_pnls else 0.0

        # Profit Factor計算
        total_profit = sum(winning_pnls) if winning_pnls else 0.0
        total_loss = abs(sum(losing_pnls)) if losing_pnls else 1.0
        profit_factor = total_profit / total_loss if total_loss > 0 else 0.0

        self.performance = {
            'weekly_return': results['total_return'],
            'win_rate': results['win_rate'],
            'sharpe_ratio': results['sharpe_ratio'],
            'max_dd': results['max_drawdown'],
            'total_trades': results['total_trades'],
            'win_trades': results['winning_trades'],
            'lose_trades': results['losing_trades'],
            'profit_factor': profit_factor,
            'avg_profit': avg_profit,
            'avg_loss': avg_loss,
        }

        # Equity curveをSeriesに変換
        equity_values = results.get('equity_curve', [10000000])
        equity_dates = self.week_data.index[:len(equity_values)]
        self.equity_curve = pd.Series(equity_values, index=equity_dates)

        print(f"  計算完了: トレード{self.performance['total_trades']}件、勝率{self.performance['win_rate']:.1f}%")

    def detect_current_regime(self):
        """Detect current market regime"""
        print(f"  レジーム分析中...")

        regime_detector = MarketRegimeDetector(self.data)
        latest_date = self.week_data.index[-1]

        # レジーム検出（複数手法の投票）
        regime_series = regime_detector.detect_regime_combined()
        self.current_regime = regime_series.iloc[-1]

        # 信頼度計算（簡略版: 過去5日間の一致度）
        recent_regimes = regime_series.tail(5)
        regime_counts = recent_regimes.value_counts()
        self.regime_confidence = (regime_counts.iloc[0] / len(recent_regimes) * 100) if len(regime_counts) > 0 else 75.0

        # レジーム継続期間
        self.regime_duration = 0
        for i in range(len(regime_series) - 1, -1, -1):
            if regime_series.iloc[i] == self.current_regime:
                self.regime_duration += 1
            else:
                break

        print(f"  現在のレジーム: {self.current_regime} (信頼度{self.regime_confidence:.1f}%, 継続{self.regime_duration}日)")

    def generate_visualizations(self):
        """Generate performance charts"""
        print(f"  可視化生成中...")

        charts_dir = self.project_root / "data" / "results" / "charts"
        charts_dir.mkdir(parents=True, exist_ok=True)

        week_id = self.week_start.strftime("%Y%m%d")

        # Equity curve
        if hasattr(self, 'equity_curve') and len(self.equity_curve) > 0:
            try:
                plot_equity_curve(
                    self.equity_curve,
                    save_path=str(charts_dir / f"equity_curve_{week_id}.png"),
                    title=f"Equity Curve: {self.week_start.strftime('%Y-%m-%d')} 〜 {self.week_end.strftime('%Y-%m-%d')}"
                )
                print(f"    ✓ Equity curve生成完了")
            except Exception as e:
                print(f"    ⚠ Equity curve生成エラー: {e}")

            # Drawdown
            try:
                plot_drawdown(
                    self.equity_curve,
                    save_path=str(charts_dir / f"drawdown_{week_id}.png")
                )
                print(f"    ✓ Drawdown生成完了")
            except Exception as e:
                print(f"    ⚠ Drawdown生成エラー: {e}")
        else:
            print(f"    ⚠ Equity curveデータがないため、可視化をスキップ")

    def render_report(self):
        """Render final report from template"""
        print(f"  レポート生成中...")

        template_path = self.project_root / "templates" / "weekly_strategy_report_template.md"

        # テンプレート読み込み
        if template_path.exists():
            template = template_path.read_text(encoding='utf-8')
        else:
            # テンプレートがない場合は簡易版
            template = self._get_default_template()

        # トレード詳細テーブル生成
        trade_details = self._format_trade_details()

        # レジーム履歴生成
        regime_history = self._format_regime_history()

        # エントリー推奨生成
        entry_recommendations = self._format_entry_recommendations()

        # プレースホルダー置換
        report_content = template.format(
            week_start=self.week_start.strftime("%Y-%m-%d"),
            week_end=self.week_end.strftime("%Y-%m-%d"),
            report_date=self.report_date,
            current_regime=self.current_regime.upper(),
            regime_confidence=f"{self.regime_confidence:.1f}",
            weekly_return=f"{self.performance['weekly_return']:.2f}",
            win_rate=f"{self.performance['win_rate']:.1f}",
            sharpe_ratio=f"{self.performance['sharpe_ratio']:.2f}",
            max_dd=f"{self.performance['max_dd']:.2f}",
            total_trades=self.performance['total_trades'],
            win_trades=self.performance['win_trades'],
            lose_trades=self.performance['lose_trades'],
            profit_factor=f"{self.performance.get('profit_factor', 0.0):.2f}",
            avg_profit=f"{self.performance.get('avg_profit', 0.0):,.0f}",
            avg_loss=f"{self.performance.get('avg_loss', 0.0):,.0f}",
            # その他のプレースホルダーはデフォルト値
            last_week_return="N/A",
            return_change="N/A",
            last_week_win_rate="N/A",
            win_rate_change="N/A",
            last_week_sharpe="N/A",
            sharpe_change="N/A",
            last_week_max_dd="N/A",
            dd_change="N/A",
            key_point_1=f"今週のパフォーマンス: リターン{self.performance['weekly_return']:.2f}%",
            key_point_2=f"{self.performance['total_trades']}件のトレードを実行（勝率{self.performance['win_rate']:.1f}%）",
            key_point_3=f"現在のレジーム: {self.current_regime.upper()}（{self.regime_duration}日継続中）",
            trade_details=trade_details,
            regime_duration=str(self.regime_duration),
            last_regime_switch="N/A",
            regime_history=regime_history,
            entry_recommendations=entry_recommendations,
            position_size="2.0",
            stop_loss="現在価格の2%下",
            take_profit="リスクリワード比1:2目標",
            max_risk="2.0",
            risk_warnings=self._get_risk_warnings(),
            week_id=self.week_start.strftime("%Y%m%d"),
            sma_20=self._get_indicator_value('sma_20'),
            sma_50=self._get_indicator_value('sma_50'),
            rsi=self._get_indicator_value('rsi'),
            macd="N/A",
            bb_upper=self._get_indicator_value('bb_upper'),
            bb_middle=self._get_indicator_value('bb_middle'),
            bb_lower=self._get_indicator_value('bb_lower'),
            data_completeness="100.0",
            regime_accuracy=f"{self.regime_confidence:.1f}",
            last_update=self.report_date,
        )

        # レポート保存
        output_path = self.project_root / "data" / "results" / f"weekly_report_{self.week_start.strftime('%Y%m%d')}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report_content, encoding='utf-8')

        print(f"  レポート保存完了: {output_path.name}")

        return str(output_path)

    def _format_trade_details(self) -> str:
        """Format trade details table"""
        if self.performance['total_trades'] == 0:
            return "| - | トレードなし | - | - | - | - |"

        # 簡易版: シグナル情報を表示
        rows = []
        cumulative_pnl = 0
        for i, signal in enumerate(self.signals[:10], 1):  # 最大10件
            action = "エントリー" if signal['action'] == 'buy' else "イグジット"
            rows.append(
                f"| {signal['date']} | {action} | {signal['entry_price']:,.0f} | - | - | - |"
            )

        if len(self.signals) > 10:
            rows.append(f"| ... | （他{len(self.signals)-10}件）| ... | ... | ... | ... |")

        return "\n".join(rows)

    def _format_regime_history(self) -> str:
        """Format regime history"""
        if not hasattr(self, 'regime_stats') or not self.regime_stats:
            return "レジーム履歴データなし"

        distribution = self.regime_stats.get('regime_distribution', {})
        total_days = self.regime_stats.get('total_days', 0)

        lines = []
        for regime, count in distribution.items():
            percentage = (count / total_days * 100) if total_days > 0 else 0
            lines.append(f"- **{regime.upper()}**: {count}日 ({percentage:.1f}%)")

        return "\n".join(lines) if lines else "レジーム履歴データなし"

    def _format_entry_recommendations(self) -> str:
        """Format entry recommendations based on current regime"""
        if self.current_regime == 'bull':
            return """
- トレンドフォロー戦略を推奨
- 短期移動平均が長期移動平均を上回る際のエントリー
- RSIが70以下であることを確認
"""
        elif self.current_regime == 'bear':
            return """
- 保守的なエントリーを推奨
- 大きな反発を待つ
- RSIが30以下の過剰売られ状態を狙う
"""
        else:  # sideways
            return """
- レンジ取引（ミーンリバージョン）を推奨
- ボリンジャーバンド下限でのエントリー
- RSIが30以下の過剰売られ状態を確認
"""

    def _get_risk_warnings(self) -> str:
        """Get risk warnings based on current conditions"""
        warnings = []

        if self.performance['max_dd'] > 10:
            warnings.append("最大ドローダウンが10%を超えています。ポジションサイズの縮小を検討してください。")

        if self.performance['win_rate'] < 40:
            warnings.append("勝率が40%未満です。戦略の見直しが必要な可能性があります。")

        if self.regime_confidence < 60:
            warnings.append("レジーム検出の信頼度が低いです。市場状況が不安定な可能性があります。")

        return "\n".join([f"- {w}" for w in warnings]) if warnings else "特になし"

    def _get_indicator_value(self, indicator_name: str) -> str:
        """Get indicator value from latest data"""
        try:
            if len(self.week_data) == 0:
                return "N/A"

            latest_close = self.week_data['close'].iloc[-1]

            if indicator_name == 'sma_20':
                sma = self.week_data['close'].rolling(20).mean().iloc[-1]
                return f"{sma:,.0f}"
            elif indicator_name == 'sma_50':
                if len(self.data) >= 50:
                    sma = self.data['close'].rolling(50).mean().iloc[-1]
                    return f"{sma:,.0f}"
                return "N/A"
            elif indicator_name == 'rsi':
                # 簡易RSI計算
                delta = self.week_data['close'].diff()
                gain = delta.where(delta > 0, 0).rolling(14).mean()
                loss = -delta.where(delta < 0, 0).rolling(14).mean()
                rs = gain / loss
                rsi = 100 - (100 / (1 + rs))
                return f"{rsi.iloc[-1]:.1f}" if not pd.isna(rsi.iloc[-1]) else "N/A"
            elif indicator_name == 'bb_upper':
                sma = self.week_data['close'].rolling(20).mean()
                std = self.week_data['close'].rolling(20).std()
                bb_upper = sma + 2 * std
                return f"{bb_upper.iloc[-1]:,.0f}" if not pd.isna(bb_upper.iloc[-1]) else "N/A"
            elif indicator_name == 'bb_middle':
                sma = self.week_data['close'].rolling(20).mean()
                return f"{sma.iloc[-1]:,.0f}" if not pd.isna(sma.iloc[-1]) else "N/A"
            elif indicator_name == 'bb_lower':
                sma = self.week_data['close'].rolling(20).mean()
                std = self.week_data['close'].rolling(20).std()
                bb_lower = sma - 2 * std
                return f"{bb_lower.iloc[-1]:,.0f}" if not pd.isna(bb_lower.iloc[-1]) else "N/A"

            return "N/A"
        except Exception as e:
            return "N/A"

    def _get_default_template(self):
        """Get default template if file doesn't exist"""
        return """# 週次トレード戦略レポート

**期間**: {week_start} 〜 {week_end}
**レジーム**: {current_regime}

## パフォーマンス

- 週間リターン: {weekly_return}%
- 勝率: {win_rate}%
- Sharpe ratio: {sharpe_ratio}
- トレード数: {total_trades}

生成日時: {report_date}
"""

    def generate(self):
        """Generate complete weekly report"""
        print("=" * 60)
        print("週次レポート生成開始")
        print("=" * 60)

        try:
            print("\n1. データ取得...")
            self.fetch_data()

            print("\n2. シグナル生成...")
            self.generate_signals()

            print("\n3. パフォーマンス計算...")
            self.calculate_performance()

            print("\n4. レジーム検出...")
            self.detect_current_regime()

            print("\n5. 可視化生成...")
            self.generate_visualizations()

            print("\n6. レポート作成...")
            report_path = self.render_report()

            print("\n" + "=" * 60)
            print(f"✅ 週次レポート生成完了")
            print(f"出力ファイル: {report_path}")
            print("=" * 60)

            return report_path

        except Exception as e:
            print(f"\n❌ エラーが発生しました: {e}")
            import traceback
            traceback.print_exc()
            return None


def main():
    parser = argparse.ArgumentParser(description="Generate weekly strategy report")
    parser.add_argument(
        "--week-start",
        default=(datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
        help="Week start date (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--week-end",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Week end date (YYYY-MM-DD)"
    )

    args = parser.parse_args()

    generator = WeeklyReportGenerator(args.week_start, args.week_end)
    generator.generate()


if __name__ == "__main__":
    main()
