# Phase 5 - Agent 2: 週次戦略レポート自動生成

## 概要

実運用を想定した週次戦略レポートの自動生成システム。毎週の戦略推奨とパフォーマンス分析を自動化します。

## 実装ファイル

### 1. テンプレート

- **`templates/weekly_strategy_report_template.md`**
  - 週次レポートのMarkdownテンプレート
  - プレースホルダーを使用した動的コンテンツ生成
  - エグゼクティブサマリー、トレード詳細、レジーム分析、戦略推奨を含む

### 2. 自動生成スクリプト

- **`scripts/generate_weekly_report.py`**
  - 週次レポートの完全自動生成
  - データ取得、シグナル生成、パフォーマンス計算、可視化を統合
  - コマンドライン引数で対象週を指定可能

### 3. スケジュール実行スクリプト

- **`scripts/cron_weekly_report.sh`**
  - cron経由での定期実行スクリプト
  - 前週の期間を自動計算
  - macOS/Linux両対応
  - ログ出力とエラー通知機能

### 4. テストコード

- **`src/tests/test_weekly_report_generator.py`**
  - 単体テストとE2Eテスト
  - 各コンポーネントの動作検証
  - pytest互換

### 5. モックデータ生成

- **`scripts/generate_mock_data.py`**
  - yfinance不要のテスト用データ生成
  - 日経225相当のOHLCVデータをランダムウォークで生成

## 使用方法

### 基本実行

```bash
# 最新週（過去7日間）のレポート生成
python3 scripts/generate_weekly_report.py

# 特定期間のレポート生成
python3 scripts/generate_weekly_report.py --week-start 2024-12-16 --week-end 2024-12-20
```

### 定期実行設定

```bash
# cron設定（毎週月曜 8:00実行）
crontab -e

# 以下を追加
0 8 * * 1 /Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents/scripts/cron_weekly_report.sh
```

### テスト実行

```bash
# pytest経由
python3 -m pytest src/tests/test_weekly_report_generator.py -v

# 手動テスト
python3 src/tests/test_weekly_report_generator.py --manual
```

### モックデータ生成

```bash
# yfinanceが使えない環境でのテスト用
python3 scripts/generate_mock_data.py
```

## 出力ファイル

### レポートファイル

- **`data/results/weekly_report_YYYYMMDD.md`**
  - 完全な週次レポート（Markdown形式）
  - 全セクション含む

### 可視化チャート

- **`data/results/charts/equity_curve_YYYYMMDD.png`**
  - 資産推移グラフ（Equity Curve）

- **`data/results/charts/drawdown_YYYYMMDD.png`**
  - ドローダウンチャート

- **`data/results/charts/regime_history_YYYYMMDD.png`**
  - レジーム推移グラフ（将来実装予定）

### ログファイル

- **`logs/weekly_report_YYYYMMDD.log`**
  - 自動実行時のログ（cron経由の場合）

## レポート構成

### 1. エグゼクティブサマリー

- 今週のパフォーマンス（リターン、勝率、Sharpe ratio、最大DD）
- 先週との比較
- 重要事項（3つのキーポイント）

### 2. トレード詳細

- トレード一覧（エントリー/イグジット、価格、損益）
- トレード統計（勝率、Profit Factor、平均利益/損失）

### 3. レジーム分析

- 現在のマーケット状況（検出レジーム、信頼度、継続期間）
- レジーム推移（分布）

### 4. 次週の戦略推奨

- レジーム別エントリーポイント
- リスク管理パラメータ（ポジションサイズ、Stop Loss、Take Profit）
- 注意事項（リスク警告）

### 5. パフォーマンス可視化

- Equity Curve（資産推移）
- Drawdown（ドローダウン）
- レジーム推移

### 6. 付録

- テクニカル指標（SMA、RSI、MACD、Bollinger Bands）
- システム状態（信頼性、データ完全性、レジーム検出精度）

## 技術詳細

### データフロー

```
1. データ取得
   ↓ RealDataLoader (yfinance or cache)
2. シグナル生成
   ↓ AdaptiveStrategy (レジーム別パラメータ)
3. パフォーマンス計算
   ↓ BacktestEngine (シミュレーション)
4. レジーム検出
   ↓ MarketRegimeDetector (複数手法の投票)
5. 可視化生成
   ↓ Visualizer (matplotlib)
6. レポート作成
   ↓ テンプレートエンジン (プレースホルダー置換)
```

### 主要クラス

#### `WeeklyReportGenerator`

```python
class WeeklyReportGenerator:
    def __init__(self, week_start: str, week_end: str)
    def fetch_data(self) -> None
    def generate_signals(self) -> None
    def calculate_performance(self) -> None
    def detect_current_regime(self) -> None
    def generate_visualizations(self) -> None
    def render_report(self) -> str
    def generate(self) -> str  # 全プロセス統合実行
```

### レジーム別戦略

- **Bull Market (上昇トレンド)**
  - トレンドフォロー戦略
  - MA crossover + RSI確認
  - 短期MA > 長期MA かつ RSI < 70

- **Bear Market (下降トレンド)**
  - 保守的戦略
  - 大きな反発を待つ
  - 短期MA > 長期MA かつ RSI < 30 かつ 価格 > 短期MA

- **Sideways (レンジ相場)**
  - ミーンリバージョン戦略
  - Bollinger Bands + RSI
  - 価格 < BB下限 かつ RSI < 30（買い）
  - 価格 > BB上限 かつ RSI > 70（売り）

### エラーハンドリング

- データ取得失敗時: デフォルト値使用
- シグナルゼロ時: ホールド戦略レポート
- 可視化エラー時: スキップして続行
- yfinance不可時: キャッシュから読み込み

## 成功基準

- [x] 週次レポートテンプレート完成
- [x] 自動生成スクリプト動作確認
- [x] サンプルレポート生成成功
- [x] 可視化2種類（Equity/Drawdown）生成
- [x] スケジュール実行設定完成
- [x] テストコード作成完了
- [x] 実行時間5分以内達成（実測: 約3秒）

## サンプル出力

### 生成されたレポート

- **期間**: 2024-12-16 〜 2024-12-20
- **レジーム**: SIDEWAYS (100%信頼度)
- **トレード数**: 0件（シグナルなし）
- **可視化**: Equity Curve、Drawdown生成完了

### 実行ログ

```
============================================================
週次レポート生成開始
============================================================

1. データ取得...
  データ期間: 2024-12-16 〜 2024-12-20
  取得データ: 全25日分、今週5日分

2. シグナル生成...
  レジーム検出を実行中...
  生成シグナル: 0件

3. パフォーマンス計算...
  パフォーマンス計算中...
    シグナルがないため、デフォルト値を使用

4. レジーム検出...
  レジーム分析中...
  現在のレジーム: sideways (信頼度100.0%, 継続25日)

5. 可視化生成...
  可視化生成中...
    ✓ Equity curve生成完了
    ✓ Drawdown生成完了

6. レポート作成...
  レポート生成中...
  レポート保存完了: weekly_report_20241216.md

============================================================
✅ 週次レポート生成完了
出力ファイル: data/results/weekly_report_20241216.md
============================================================
```

## 今後の拡張

### Phase 5.1 で実装予定

1. **前週比較機能**
   - 前週のレポートを読み込み
   - 変化量（Δ）を計算・表示

2. **レジーム推移グラフ**
   - 過去4週間のレジーム遷移を可視化
   - ヒートマップ形式

3. **メール通知機能**
   - レポート生成完了通知
   - エラー発生時のアラート

4. **PDF出力対応**
   - Markdownから自動変換
   - 印刷可能な形式

5. **Notion連携**
   - Notion APIでデータベースに自動登録
   - ダッシュボード統合

## トラブルシューティング

### yfinanceエラー

```bash
# Python 3.9環境でyfinanceの型ヒントエラーが発生する場合
# → モックデータ生成スクリプトを使用
python3 scripts/generate_mock_data.py
```

### データ取得失敗

```bash
# キャッシュを手動確認
ls -la data/cache/

# 特定日付範囲のキャッシュを生成
python3 -c "
from pathlib import Path
import pandas as pd

cache_file = Path('data/cache/N225_20200101_20241231.csv')
df = pd.read_csv(cache_file)
df['date'] = pd.to_datetime(df['date'])
subset = df[(df['date'] >= '2024-11-16') & (df['date'] <= '2024-12-20')]
subset.to_csv('data/cache/N225_20241116_20241220.csv', index=False)
"
```

### 可視化エラー（日本語フォント）

```bash
# 警告が出ても画像は生成されます（影響なし）
# 日本語フォント設定（オプション）
# matplotlibrc を編集
```

## 関連ドキュメント

- **Phase 5 全体計画**: `documents/9_phase5/phase5_overview.md`
- **Agent 1 (実データバックテスト)**: `documents/9_phase5/agent1_real_backtest_README.md`
- **Agent 3 (実運用シミュレーション)**: `documents/9_phase5/agent3_live_simulation_README.md`

## 作成日

2026-01-01

## ライセンス

このプロジェクトは情報提供のみを目的としています。投資助言ではありません。
