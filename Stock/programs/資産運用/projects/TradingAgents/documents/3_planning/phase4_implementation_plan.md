# Phase 4実装計画: 実データ検証・戦略最適化

**作成日**: 2026-01-01
**プロジェクト**: TradingAgents - 日経平均先物トレード戦略システム
**フェーズ**: Phase 4 - 検証・最適化・実運用準備

---

## 1. Phase 4の目的

Phase 3で構築した高信頼性バックテストエンジン（信頼性97.5%）を用いて、**実データでの検証**と**レジーム別戦略最適化**を実施し、実運用に向けた最終準備を完了する。

### Phase 3の成果（継承するもの）

- ✅ Look-ahead bias除去（次日寄り値でエントリー）
- ✅ Slippage実装（0.1%デフォルト）
- ✅ Market regime分析（Bull/Bear/Sideways検出）
- ✅ Parameter optimization（Grid search + Sensitivity analysis）
- ✅ Overfitting防止機構
- ✅ 可視化機能（Equity curve, Regime performance, Drawdown）
- ✅ Market impact制約（最大1%流動性制約）

### Phase 4で追加する価値

1. **実データ検証**: 日経225実データ（2020-2025、5年間）での包括的バックテスト
2. **レジーム別最適化**: Bull/Bear/Sideways各レジームに最適化された戦略パラメータ
3. **KPI目標再評価**: 実データ結果に基づく現実的な目標値への調整
4. **Walk-forward分析**: 時系列クロスバリデーションによる頑健性確認
5. **実運用シミュレーション**: 週次戦略レポート自動生成の実装

---

## 2. 実装項目と優先度

### 優先度1: 実データバックテスト実行（Agent 1）

**目的**: 日経225実データ（2020-2025）を用いた包括的バックテスト

**実装内容**:
1. データ取得モジュール作成
   - `src/data/real_data_loader.py`
   - yfinanceを使用して日経225データ取得（^N225）
   - 2020-01-01〜2025-12-31の5年間
   - OHLCV + Volumeデータ

2. バックテスト実行スクリプト作成
   - `scripts/run_real_data_backtest.py`
   - 全期間（2020-2025）でのバックテスト
   - Train期間: 2020-2022 (3年)
   - Test期間: 2023-2025 (3年)
   - Slippage: 0.1%
   - Commission: 0.05%
   - Initial capital: 10,000,000円

3. 結果レポート自動生成
   - `data/results/phase4_real_data_backtest_report.md`
   - 全5年間の統計（Sharpe ratio, Win rate, Total return等）
   - Train vs Test比較（Overfitting検出）
   - レジーム別パフォーマンス
   - 可視化（Equity curve, Drawdown, Regime performance）

**成功基準**:
- Train/Test両方でKPI目標の80%以上達成
- Overfitting検出（Train-Test差が30%以内）
- 全レジームで正のリターン

**推定作業時間**: 8-10時間（エージェント実行: 並列で短縮）

---

### 優先度2: レジーム別戦略最適化（Agent 2）

**目的**: Bull/Bear/Sideways各レジームに最適化されたパラメータセット作成

**実装内容**:
1. レジーム別パラメータ最適化モジュール
   - `src/strategy/regime_specific_optimizer.py`
   - Bull専用パラメータ（MA短期化、RSI閾値低め）
   - Bear専用パラメータ（MA長期化、RSI閾値高め）
   - Sideways専用パラメータ（レンジ戦略、ボリンジャー重視）

2. 動的レジーム切り替えロジック
   - `src/strategy/adaptive_strategy.py`
   - リアルタイムでレジーム検出
   - 検出レジームに応じてパラメータ自動切り替え
   - レジーム変化の閾値設定（頻繁な切り替え防止）

3. レジーム別バックテスト
   - 各レジーム期間を抽出してバックテスト
   - レジーム固定戦略 vs 動的切り替え戦略の比較
   - 結果レポート: `data/results/phase4_regime_optimization_report.md`

**成功基準**:
- 各レジームで固定戦略よりSharpe ratio +20%以上改善
- 動的切り替え戦略が全期間で固定戦略を上回る
- レジーム誤判定時の損失が-5%以内

**推定作業時間**: 10-12時間（エージェント実行: 並列で短縮）

---

### 優先度3: KPI目標再評価とWalk-forward分析（Agent 3）

**目的**: 実データ結果に基づく現実的なKPI目標設定とWalk-forward検証

**実装内容**:
1. Walk-forward分析実装
   - `src/backtest/walk_forward_analyzer.py`
   - 6ヶ月Trainウィンドウ、3ヶ月Testウィンドウ
   - ローリングウィンドウで全期間を分割
   - 各ウィンドウでパラメータ最適化→前方テスト

2. KPI統計分析
   - `scripts/analyze_kpi_statistics.py`
   - 全Walk-forwardウィンドウのKPI分布
   - 中央値、25%ile、75%ile、最大/最小
   - 達成可能なKPI目標の提案

3. 新KPI目標設定
   - 実データ結果の中央値ベース
   - 保守的目標（50%ile）、標準目標（75%ile）、挑戦目標（90%ile）
   - プロジェクト憲章への反映

4. 結果レポート
   - `data/results/phase4_kpi_reevaluation_report.md`
   - Walk-forward全結果の可視化
   - 新旧KPI目標の比較表
   - 目標達成確率の推定

**成功基準**:
- Walk-forward全ウィンドウの80%以上で正のリターン
- 新KPI目標が実データ中央値以下（達成可能性50%以上）
- Train-Test乖離が全ウィンドウで30%以内

**推定作業時間**: 8-10時間（エージェント実行: 並列で短縮）

---

## 3. 並列実行計画

### Batch 1: 3エージェント同時起動（推奨）

```
Agent 1 (実データバックテスト): model=sonnet, 8-10時間
Agent 2 (レジーム別最適化): model=sonnet, 10-12時間
Agent 3 (KPI再評価・Walk-forward): model=sonnet, 8-10時間

総実行時間: 10-12時間（最遅エージェント2に依存）
効率化率: 73%短縮（シーケンシャル26-32時間 → 並列10-12時間）
```

### 並列実行の前提条件

- 各エージェントは独立動作（共有ファイルなし）
- データ取得はAgent 1が先行するが、他エージェントは既存テストデータで開発可能
- 最終統合テストはBatch 1完了後に実施

---

## 4. 成果物一覧

### コードモジュール

1. `src/data/real_data_loader.py` - 日経225実データ取得
2. `src/strategy/regime_specific_optimizer.py` - レジーム別パラメータ最適化
3. `src/strategy/adaptive_strategy.py` - 動的レジーム切り替え戦略
4. `src/backtest/walk_forward_analyzer.py` - Walk-forward分析エンジン
5. `scripts/run_real_data_backtest.py` - 実データバックテスト実行スクリプト
6. `scripts/analyze_kpi_statistics.py` - KPI統計分析スクリプト

### テストコード

1. `src/tests/test_real_data_loader.py` - データ取得テスト
2. `src/tests/test_regime_optimizer.py` - レジーム最適化テスト
3. `src/tests/test_adaptive_strategy.py` - 動的戦略テスト
4. `src/tests/test_walk_forward.py` - Walk-forward分析テスト
5. `src/tests/test_phase4_integration.py` - Phase 4統合テスト

### ドキュメント

1. `data/results/phase4_real_data_backtest_report.md` - 実データバックテスト結果
2. `data/results/phase4_regime_optimization_report.md` - レジーム最適化結果
3. `data/results/phase4_kpi_reevaluation_report.md` - KPI再評価結果
4. `data/results/phase4_walk_forward_analysis.md` - Walk-forward分析結果
5. `data/results/phase4_final_validation_report.md` - 最終検証レポート
6. `data/results/PHASE4_COMPLETION_CERTIFICATE.md` - Phase 4完了証明書
7. `documents/3_planning/phase4_completion_summary.md` - Phase 4完了サマリー

---

## 5. Phase 4成功基準

### 必須達成項目（100%必須）

1. ✅ 実データバックテスト完了（2020-2025、5年間）
2. ✅ レジーム別最適化完了（Bull/Bear/Sideways各パラメータ確定）
3. ✅ KPI目標再評価完了（新目標値をプロジェクト憲章に反映）
4. ✅ Walk-forward分析完了（全ウィンドウで検証）
5. ✅ 統合テスト成功率80%以上

### KPI目標（実データベース）

**現行目標（Phase 1-3）**:
- 週間平均リターン: 3%以上
- 勝率: 60%以上
- プロフィットファクター: 1.5以上
- 最大ドローダウン: -10%以下
- シャープレシオ: 1.0以上

**Phase 4での再評価基準**:
- 実データ中央値を新標準目標とする
- 保守的目標（25%ile）、挑戦目標（75%ile）も設定
- 達成可能性50%以上の目標値に調整

### 品質基準

1. **Overfitting防止**: Train-Test乖離30%以内
2. **レジーム頑健性**: 全レジームで正のリターン
3. **Walk-forward成功率**: 80%以上のウィンドウで正のリターン
4. **コードカバレッジ**: 80%以上
5. **ドキュメント完全性**: 全成果物が揃っている

---

## 6. リスクと対策

### リスク1: 実データでKPI目標未達

**確率**: 高（Phase 3はテストデータベース）
**影響度**: 中（目標再設定で対応可）
**対策**:
- Phase 4でKPI目標を実データベースに再設定
- 保守的目標/標準目標/挑戦目標の3段階設定
- 達成可能性を確率で表現

### リスク2: レジーム誤判定による損失

**確率**: 中
**影響度**: 中
**対策**:
- レジーム判定に複数手法の投票システム導入済み（Phase 3）
- レジーム切り替え閾値の調整
- 誤判定時の損失を-5%以内に抑制

### リスク3: Overfitting発生

**確率**: 中
**影響度**: 高
**対策**:
- Walk-forward分析で時系列検証
- Train-Test乖離30%以内の基準厳守
- Sensitivity分析でパラメータ安定性確認

### リスク4: データ取得失敗

**確率**: 低
**影響度**: 高
**対策**:
- yfinanceのフォールバック（複数ソース対応）
- データ欠損時の補完ロジック
- ローカルキャッシュ機能

---

## 7. Phase 5への引継ぎ事項

Phase 4完了後、Phase 5（実運用準備）への引継ぎ内容:

1. **確定した戦略パラメータ**
   - レジーム別最適パラメータセット
   - 動的切り替え戦略のロジック

2. **実運用KPI目標**
   - 実データベースの現実的な目標値
   - 週次/月次モニタリング基準

3. **リスク管理パラメータ**
   - Slippage: 0.1%
   - Commission: 0.05%
   - Max volume: 1% of daily volume
   - Stop-loss/Take-profit設定

4. **週次レポート自動生成**
   - Phase 5で実装予定の週次戦略レポート仕様
   - 可視化フォーマット

---

## 8. タイムライン

| 作業項目                     | 担当       | 期間      | ステータス |
| ---------------------------- | ---------- | --------- | ---------- |
| Phase 4計画作成              | Claude     | 1時間     | ✅ 完了    |
| Agent 1: 実データバックテスト | Subagent 1 | 8-10時間  | 🔄 準備中  |
| Agent 2: レジーム別最適化     | Subagent 2 | 10-12時間 | 🔄 準備中  |
| Agent 3: KPI再評価            | Subagent 3 | 8-10時間  | 🔄 準備中  |
| 統合テスト                   | Claude     | 2-3時間   | 予定       |
| 最終ドキュメント作成         | Claude     | 2時間     | 予定       |

**総実行時間（並列）**: 10-12時間
**Phase 4完了予定日**: 2026-01-01

---

## 9. 承認とサインオフ

- [ ] Phase 4実装計画承認
- [ ] 並列エージェント実行開始承認
- [ ] Phase 4完了承認（実装後）

---

## 変更履歴

| バージョン | 日付       | 変更内容       |
| ---------- | ---------- | -------------- |
| 1.0        | 2026-01-01 | Phase 4計画策定 |
