# analyze-sns-weekly

X (Twitter)、LinkedIn、Threadsの3プラットフォームを対象とした週次パフォーマンス分析レポートを自動生成します。

## 概要

**目的**: SNS投稿のパフォーマンス測定、コンテンツ最適化、週次トレンド分析

**対象プラットフォーム**:
- LinkedIn
- X (Twitter)
- Threads

**実行時間**: 15-20分/週

**出力形式**: Markdown レポート

## 前提条件

### 必須
- Late API契約 + Analytics Addon契約
- Late API設定ファイル: `Stock/programs/副業/projects/SNS/config/late_api_config.json`
- KPI目標設定ファイル: `Stock/programs/副業/projects/SNS/scripts/kpi_targets.json`

### 推奨
- 過去データ: `Stock/programs/副業/projects/SNS/history.json`（4週トレンド分析用）

## 使用方法

```bash
# 基本実行（過去7日間）
/analyze-sns-weekly

# 期間指定
/analyze-sns-weekly --from-date 2026-01-03 --to-date 2026-01-10

# 出力先指定
/analyze-sns-weekly --output Stock/programs/副業/projects/SNS/reports/report_20260110.md
```

## 実行フロー

### STEP 1: パラメータ設定
- 分析期間の設定（デフォルト: 過去7日間）
- 出力パスの設定
- Late API設定のロード

### STEP 2: Late APIデータ収集（10分）
- LinkedIn投稿データ収集
- X (Twitter)投稿データ収集
- Threads投稿データ収集
- **並列実行**: 3プラットフォーム同時収集

### STEP 3: LLM分析（3-5分）
- KPI集計（インプレッション、エンゲージメント、エンゲージメント率）
- KPI達成状況判定
- Top 5投稿の特定
- 成功パターン抽出

### STEP 4: レポート生成（2-5分）
- Markdownテンプレート適用
- プレースホルダー置換
- ファイル出力

### STEP 5: history.json更新
- 4週ローリングウィンドウ管理
- 週次データ追加
- 古いデータ削除（4週以前）

### STEP 6: サマリー表示
- 総合評価
- 各プラットフォームのハイライト
- 推奨アクション

## 出力ファイル

### メインレポート
`Stock/programs/副業/projects/SNS/reports/sns_performance_report_YYYYMMDD.md`

**構成**:
1. エグゼクティブサマリー
2. プラットフォーム別詳細
   - LinkedIn
   - X (Twitter)
   - Threads
3. Top 5投稿分析
4. 前週比較
5. 4週トレンド分析
6. 推奨アクション
7. 成功パターン

### データファイル
- `Stock/programs/副業/projects/SNS/data/late_api_analytics_YYYYMMDD-YYYYMMDD.json` - 生データ
- `Stock/programs/副業/projects/SNS/history.json` - 履歴データ（4週ローリング）

## KPI定義

### LinkedIn
- **インプレッション**: 目標 1,000/週
- **エンゲージメント**: 目標 50/週
- **エンゲージメント率**: 目標 5%

### X (Twitter)
- **インプレッション**: 目標 2,000/週
- **エンゲージメント**: 目標 100/週
- **エンゲージメント率**: 目標 5%

### Threads
- **インプレッション**: 測定不可（常に0）
- **エンゲージメント**: 目標 30/週
- **エンゲージメント率**: 算出不可（インプレッション0のため）

**注意**: Threadsはインプレッション数が常に0を返すため、エンゲージメント絶対数で評価します。

## 技術仕様

### Late API統合
- **エンドポイント**: `/api/v1/analytics`
- **パラメータ**: `dateFrom`, `dateTo`, `platform`
- **ページネーション**: 最適化済み（N+1問題解決）
- **リトライ**: 3回、指数バックオフ

### LLM推論
- **データ統合**: Haiku（軽量・高速）
- **分析・レポート生成**: Sonnet（バランス重視）
- **コンテキスト管理**: サブエージェント活用

### テンプレートシステム
- **プレースホルダー形式**: `{{PLACEHOLDER_NAME}}`
- **置換ロジック**: 正規表現ベース
- **テンプレートファイル**: `templates/report_template.md`

## エラーハンドリング

### Analytics Addon未契約
```
❌ Analytics Addon契約が必要です
   https://app.getlate.dev/settings/billing で契約してください
```

### データ収集失敗
- リトライ: 最大3回
- タイムアウト: 60秒/リクエスト
- フォールバック: 部分データでレポート生成（警告付き）

### history.json破損
- バックアップから復元
- 復元不可の場合: 新規作成（警告付き）

## 成功基準

### Phase 1（現在）
- [x] Late API Analytics Addon契約確認
- [ ] データ収集成功率 ≥ 95%
- [ ] レポート生成時間 ≤ 20分
- [ ] history.json自動更新成功率 100%

### Phase 2（将来）
- [ ] 競合分析機能追加
- [ ] レポート生成時間 ≤ 35分（最適化後25分）

## 参照

- **Late API実装**: `Stock/programs/副業/projects/SNS/scripts/fetch_late_analytics_optimized.py`
- **KPI設定**: `Stock/programs/副業/projects/SNS/scripts/kpi_targets.json`
- **テンプレート**: `templates/report_template.md`
- **実装計画**: `@/Users/yuichi/.claude/plans/temporal-kindling-rose.md`

## 更新履歴

- **2026-01-10**: Phase 1実装開始（3プラットフォーム対応）
