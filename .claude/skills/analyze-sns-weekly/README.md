# analyze-sns-weekly

X (Twitter)、LinkedIn、Threadsの3プラットフォームを対象とした週次パフォーマンス分析レポート自動生成スキル。

## 概要

### 主な機能
- Late APIからの3プラットフォームデータ収集（LinkedIn, X, Threads）
- KPI達成状況の自動判定
- Top 5投稿の特定と成功パターン分析
- 前週比較と4週トレンド分析
- Markdown形式レポート自動生成
- history.json自動更新（4週ローリングウィンドウ）

### 実行時間
- Phase 1: 15-20分/週

### 対応状況
- ✅ Phase 1: 3プラットフォーム基本分析（現在）
- 🔜 Phase 2: 競合分析追加（将来）

## セットアップ

### 前提条件

1. **Late API契約**
   - Late API契約必須
   - Analytics Addon契約必須
   - 設定ファイル: `Stock/programs/副業/projects/SNS/config/late_api_config.json`

2. **Pythonパッケージ**
   ```bash
   pip3 install requests
   ```

3. **ファイル構成**
   ```
   .claude/skills/analyze-sns-weekly/
   ├── SKILL.md              # スキル仕様書
   ├── README.md             # 本ファイル
   ├── config/
   │   └── kpi_targets.json  # KPI目標値
   ├── templates/
   │   └── report_template.md # レポートテンプレート
   ├── scripts/
   │   └── update_history.py  # history.json更新スクリプト
   └── tests/
       └── (Phase 2で追加予定)

   Stock/programs/副業/projects/SNS/
   ├── config/
   │   └── late_api_config.json     # Late API設定
   ├── scripts/
   │   ├── kpi_targets.json         # KPI目標値
   │   └── fetch_late_analytics_optimized.py # データ収集スクリプト
   ├── history.json                  # 履歴データ（4週分）
   ├── data/                         # 生データ保存先
   └── reports/                      # レポート出力先
   ```

## 使い方

### 基本実行

```bash
# 過去7日間の分析
/analyze-sns-weekly

# 期間指定
/analyze-sns-weekly --from-date 2026-01-03 --to-date 2026-01-10

# 出力先指定
/analyze-sns-weekly --output Stock/programs/副業/projects/SNS/reports/report_20260110.md
```

### データ収集のみ

```bash
cd Stock/programs/副業/projects/SNS
python3 scripts/fetch_late_analytics_optimized.py --from-date 2026-01-03 --to-date 2026-01-10
```

### history.json更新のみ

```bash
python3 .claude/skills/analyze-sns-weekly/scripts/update_history.py \
  --week-id 2026-W02 \
  --data kpi_data.json
```

## KPI目標値

設定ファイル: `Stock/programs/副業/projects/SNS/scripts/kpi_targets.json`

| プラットフォーム | インプレッション | エンゲージメント | エンゲージメント率 |
|----------------|----------------|----------------|------------------|
| LinkedIn       | 1,000/週       | 50/週          | 5%               |
| X (Twitter)    | 2,000/週       | 100/週         | 5%               |
| Threads        | N/A※          | 30/週          | N/A※            |

※ Threadsはインプレッション数が常に0を返すため、エンゲージメント絶対数で評価

## 出力ファイル

### 週次レポート
`Stock/programs/副業/projects/SNS/reports/sns_performance_report_YYYYMMDD.md`

**構成**:
1. エグゼクティブサマリー
2. プラットフォーム別詳細（LinkedIn, X, Threads）
3. Top 5投稿分析
4. 前週比較
5. 4週トレンド分析
6. 推奨アクション
7. 次週の戦略

### データファイル
- `Stock/programs/副業/projects/SNS/data/late_api_analytics_YYYYMMDD-YYYYMMDD.json` - 生データ
- `Stock/programs/副業/projects/SNS/history.json` - 履歴データ（4週ローリング）

## トラブルシューティング

### Analytics Addon未契約エラー

```
❌ Analytics Addon契約が必要です
   https://app.getlate.dev/settings/billing で契約してください
```

**解決策**: Late APIのBilling画面でAnalytics Addonを契約

### データ収集失敗

**症状**: API呼び出しがタイムアウトまたはエラー

**解決策**:
1. `late_api_config.json` のAPI Keyを確認
2. ネットワーク接続を確認
3. Late APIのステータスを確認: https://status.getlate.dev

### Threadsインプレッション0問題

**症状**: Threadsのインプレッション数が常に0

**解決策**: これは仕様です。Late API制約によりThreadsのインプレッション数は取得できません。エンゲージメント絶対数で評価してください。

### history.json破損

**症状**: history.jsonが読み込めない

**解決策**:
1. `history.json.backup` から復元
2. 復元不可の場合は空の構造を作成:
   ```json
   {
     "version": "1.0",
     "last_updated": "2026-01-10",
     "weeks": []
   }
   ```

## 技術仕様

### Late API統合
- **エンドポイント**: `/api/v1/analytics`
- **認証**: Bearer Token
- **パラメータ**: `dateFrom`, `dateTo`, `platform`
- **リトライ**: 3回、指数バックオフ
- **タイムアウト**: 60秒/リクエスト

### LLM推論
- **データ統合**: Haiku（軽量・高速）
- **分析・レポート生成**: Sonnet（バランス重視）
- **コンテキスト管理**: サブエージェント活用

### 4週ローリングウィンドウ
- 最新4週分のデータを保持
- 5週目以降のデータは自動削除
- `history.json` で管理

## 開発ロードマップ

### Phase 1（現在）✅
- [x] 3プラットフォームデータ収集
- [x] KPI達成状況判定
- [x] レポートテンプレート作成
- [x] history.json自動更新
- [ ] 統合テスト（レポート生成時間 ≤ 20分）

### Phase 2（将来）🔜
- [ ] 競合アカウントデータ収集
- [ ] 競合比較テーブル生成
- [ ] 成功パターン横断分析
- [ ] レポート生成時間最適化（≤ 25分）

## 参照

- **Late API実装**: `Stock/programs/副業/projects/SNS/scripts/fetch_late_analytics_optimized.py`
- **KPI設定**: `Stock/programs/副業/projects/SNS/scripts/kpi_targets.json`
- **テンプレート**: `templates/report_template.md`
- **実装計画**: `/Users/yuichi/.claude/plans/temporal-kindling-rose.md`

## ライセンス

プロジェクト内部使用

## 更新履歴

- **2026-01-10**: Phase 1実装完了
  - SKILL.md作成
  - report_template.md作成（200行）
  - update_history.py作成（150行）
  - kpi_targets.json作成
  - README.md作成
