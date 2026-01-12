# Phase 6 実装計画: 戦略改善と最終検証

## プロジェクト情報

| 項目 | 内容 |
|------|------|
| フェーズ | Phase 6: 戦略改善と最終検証 |
| 作成日 | 2026-01-01 |
| 前提条件 | Phase 5完了（システム基盤✅、戦略性能❌） |

---

## Phase 5完了サマリー

### 達成事項
- ✅ バックテストエンジン信頼性: 97.5%
- ✅ 週次レポート自動生成: 3秒実行（98%改善）
- ✅ 運用マニュアル: 8セクション完備

### 重大課題
- ❌ **Overfitting**: Train-Test gap -150% to -270% (目標30%以内)
- ❌ **Dynamic戦略**: Fixed戦略より340%悪化
- ❌ **Test Sharpe**: -0.21 (negative)

**総合判定**: 🟡 部分的成功 → **Phase 6での戦略改善が必須**

---

## Phase 6目標

### 1. 戦略性能の根本的改善

**KPI達成目標**:
| KPI | Phase 5結果 | Phase 6目標 | 達成条件 |
|-----|-------------|-------------|----------|
| Train-Test gap | -150% ~ -270% | <30% | Overfitting解消 |
| Test Sharpe | -0.21 | >0.5 | 安定収益 |
| Test Win Rate | 35% | >50% | 予測精度向上 |
| Dynamic vs Fixed | -340% | >0% | レジーム適応有効性 |
| Max Drawdown | -45% | <-20% | リスク管理 |

### 2. Walk-forward分析の完全実装

- Strategy関数インターフェース修正（シグナルList vs KPI Dict）
- 57ウィンドウ統計評価
- ロバスト性検証

### 3. 本番運用準備

- Python 3.10+環境移行
- Real data validation（yfinance日経225 2020-2025）
- Go/No-go判断基準明確化

---

## 並列実行計画（3エージェント）

### Agent 1: 戦略改善（Strategy Improvement）

**担当**: 新戦略実装とOverfitting解消

**実装戦略**:

1. **Mean Reversion Strategy**（逆張り戦略）
   - RSI contrarian: RSI<30で買い、RSI>70で売り
   - Bollinger Bands mean reversion: BB下限タッチで買い、上限で売り
   - **適用レジーム**: Sideways（レンジ相場）

2. **Trend Following Strategy**（順張り戦略）
   - MACD crossover: MACD>Signal で買い、MACD<Signalで売り
   - ATR-based position sizing: ボラティリティ適応
   - **適用レジーム**: Bull/Bear（トレンド相場）

3. **Portfolio Strategy**（ポートフォリオ戦略）
   - 複数戦略の組み合わせ（Mean Reversion 40% + Trend Following 60%）
   - リスク分散によるOverfitting低減
   - Dynamic weight adjustment

**成果物**:
- `src/strategy/mean_reversion_strategy.py`
- `src/strategy/trend_following_strategy.py`
- `src/strategy/portfolio_strategy.py`
- `src/tests/test_strategy_improvement.py`

**成功基準**:
- [ ] Train-Test gap <30%
- [ ] Test Sharpe >0.5
- [ ] Test Win Rate >50%
- [ ] テスト成功率100%

**推定時間**: 3時間

---

### Agent 2: Walk-forward分析完成（Walk-forward Completion）

**担当**: Walk-forward分析の完全実装と統計検証

**実装内容**:

1. **Strategy関数インターフェース修正**
   - 現状: `run_backtest(data, params) -> {'sharpe': ...}` (KPI Dict)
   - 修正後: `generate_signals(data, params) -> [{'date': ..., 'action': ...}]` (シグナルList)
   - WalkForwardAnalyzer.run_analysis()の修正

2. **57ウィンドウ統計評価**
   - Train期間: 6ヶ月
   - Test期間: 3ヶ月
   - Step: 3ヶ月
   - Total windows: 57（2020-2025の5年間）

3. **統計的ロバスト性検証**
   - Test Sharpe分布（平均、標準偏差、Q25/Q50/Q75）
   - Win Rate安定性
   - Max Drawdown分布
   - Train-Test相関分析

**成果物**:
- `src/backtest/walk_forward_analyzer.py`（修正版）
- `scripts/run_walk_forward_full.py`
- `data/results/walk_forward_statistical_report.md`
- `src/tests/test_walk_forward_complete.py`

**成功基準**:
- [ ] 57ウィンドウ全実行完了
- [ ] Test Sharpe平均>0.5
- [ ] Train-Test相関>0.7（安定性）
- [ ] テスト成功率100%

**推定時間**: 2.5時間

---

### Agent 3: 最終検証・本番準備（Final Validation & Production Readiness）

**担当**: 実データ検証と本番運用Go/No-go判断

**実装内容**:

1. **Python 3.10+環境移行**（オプショナル）
   - 環境確認スクリプト
   - yfinance互換性検証
   - Real data fetch（日経225 2020-2025）

2. **Real Data Validation**
   - yfinanceから実データ取得
   - 改善戦略でバックテスト再実行
   - Phase 5結果との比較

3. **Go/No-go判断基準**
   - ✅ Go条件:
     - Test Sharpe >0.5
     - Train-Test gap <30%
     - Win Rate >50%
     - Max Drawdown <-20%
   - ❌ No-go条件:
     - いずれか1つでも未達成

4. **本番運用チェックリスト**
   - データ取得（yfinance API）
   - 週次レポート生成
   - エラーハンドリング（E001-E005）
   - Performance monitor
   - Operation manual

**成果物**:
- `scripts/check_python_environment.py`
- `scripts/run_final_validation.py`
- `data/results/PHASE6_FINAL_VALIDATION_REPORT.md`
- `documents/5_operations/production_readiness_checklist.md`
- `src/tests/test_production_readiness.py`

**成功基準**:
- [ ] Real dataでTest Sharpe >0.5
- [ ] Go/No-go判断完了
- [ ] 本番運用チェックリスト100%
- [ ] テスト成功率100%

**推定時間**: 2時間

---

## 統合スケジュール

```
Phase 6: 戦略改善と最終検証（並列実行）
├─ Agent 1: 戦略改善（3h）
│  └─ Mean Reversion + Trend Following + Portfolio
├─ Agent 2: Walk-forward完成（2.5h）
│  └─ 57ウィンドウ統計評価
└─ Agent 3: 最終検証・本番準備（2h）
   └─ Real data validation + Go/No-go判断

Total: 3h（並列実行）
```

---

## Phase 6成功基準

### 必須条件（Must-have）
- [ ] Test Sharpe >0.5（現状-0.21）
- [ ] Train-Test gap <30%（現状-150%~-270%）
- [ ] Test Win Rate >50%（現状35%）
- [ ] Max Drawdown <-20%（現状-45%）

### 推奨条件（Should-have）
- [ ] Dynamic戦略がFixed戦略より優位（現状-340%）
- [ ] Walk-forward 57ウィンドウ全成功
- [ ] Real data validation成功（Python 3.10+環境）

### オプション条件（Nice-to-have）
- [ ] Test Sharpe >1.0（Challenge目標）
- [ ] Train-Test相関>0.8（高安定性）

---

## リスクと対策

### リスク1: 戦略改善でもOverfitting解消できない
- **確率**: 30%
- **対策**: Portfolio戦略で複数戦略を組み合わせてリスク分散

### リスク2: Walk-forward分析で性能悪化判明
- **確率**: 40%
- **対策**: レジーム別戦略の再最適化、パラメータ調整

### リスク3: Python 3.9環境でyfinance使用不可
- **確率**: 50%（既知）
- **対策**: Sample dataで先行検証、Python 3.10+移行は後回し

---

## Phase 6完了後のアクション

### Go判断の場合
1. 本番運用開始準備
2. 週次レポート定期実行設定
3. Performance monitoring開始

### No-go判断の場合
1. Phase 7: Advanced Strategy Researchを計画
2. Machine Learning手法の検討（LSTM, Transformer）
3. Alternative dataの活用検討

---

## 変更履歴

| バージョン | 日付 | 変更内容 |
|-----------|------|---------|
| 1.0 | 2026-01-01 | Phase 6実装計画初版作成 |
