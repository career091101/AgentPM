# SNS Performance Analysis - Weekly SKILL

直近1週間のSNS投稿パフォーマンスを分析し、KPI達成状況を可視化するスキルです。

## 📋 概要

### 機能

- **対象プラットフォーム**: LinkedIn、X (Twitter)、Threads
- **分析期間**: 実行日から7日遡り
- **出力形式**: Markdown形式レポート
- **実行時間**: 10-15分
- **KPI比較**: 目標値との達成率を自動算出

### 分析内容

1. **プラットフォーム別集計**
   - 投稿数
   - 総インプレッション
   - 総エンゲージメント
   - エンゲージメント率
   - 投稿あたり平均インプレッション

2. **全体サマリー**
   - 総投稿数
   - 総インプレッション
   - 総エンゲージメント
   - 平均エンゲージメント率

3. **KPI達成状況**
   - 総インプレッション vs 目標150,000
   - 平均エンゲージメント率 vs 目標1.5%
   - LinkedIn投稿あたり平均 vs 目標8,000
   - X投稿あたり平均 vs 目標2,000

4. **トップ5投稿**
   - インプレッション降順
   - プラットフォーム、日時、エンゲージメント率、内容プレビュー

---

## 🚀 使い方

### 前提条件

#### 必須

1. **Late API Analytics Addon契約**
   - 契約URL: https://app.getlate.dev/settings/billing
   - プラン: Basic以上（Pro推奨）

2. **環境変数設定**
   - `.env` ファイルに `LATE_API_KEY` を設定
   - パス: `/Users/yuichi/AIPM/aipm_v0/.env`

3. **Python 3.x**
   - `python3 --version` で確認
   - 必要なライブラリ: `requests`, `argparse`

#### 推奨

- **tmux**: 並列実行環境（Week 3実装）
- **Git**: バージョン管理

### 基本的な実行方法

```bash
# Claude Code CLI で実行
claude

# プロンプト入力
SNS週次分析
```

または

```bash
# Skillツール経由で起動
claude --skill analyze-sns-performance-weekly
```

### 出力ファイル

実行後、以下のファイルが生成されます：

```
Flow/{YYYYMM}/{YYYY-MM-DD}/
├── late_api_analytics_{YYYYMMDD}-{YYYYMMDD}.json  # Late APIデータ（中間ファイル）
└── sns_performance_report_{YYYYMMDD}.md           # 最終レポート
```

**例**:
```
Flow/202601/2026-01-10/
├── late_api_analytics_20260103-20260110.json
└── sns_performance_report_20260110.md
```

---

## 📊 KPI目標値

デフォルトの目標値は `kpi_targets.json` に定義されています：

| KPI指標 | 目標値 | 説明 |
|---------|--------|------|
| 総インプレッション（週間） | 150,000 | 週間の全プラットフォーム合計 |
| 平均エンゲージメント率（週間） | 1.5% | Threads除外で計算 |
| LinkedIn投稿あたり平均インプレッション | 8,000 | ビジネス向けプラットフォーム目標 |
| X投稿あたり平均インプレッション | 2,000 | 短文投稿プラットフォーム目標 |

### 目標値のカスタマイズ

`kpi_targets.json` を編集して目標値を変更できます：

```json
{
  "version": "1.0",
  "last_updated": "2026-01-10",
  "targets": {
    "total_impressions": {
      "weekly": 200000  // ← 目標値を変更
    },
    // ...
  }
}
```

---

## ⚠️ Threads 特例処理

### なぜ Threads はインプレッション0なのか？

Late API の制約により、Threads プラットフォームのインプレッション数は常に0を返します。

**理由**:
1. **Threadsプラットフォーム側の仕様**: 公式APIでインプレッション数を提供していない
2. **Late APIの対応状況**: インプレッションデータを取得できない
3. **代替指標**: エンゲージメント絶対数（いいね、コメント、シェア）のみ評価

### 処理方法

- **レポート表示**: "計測不可（Late API未対応）"と表記
- **エンゲージメント率**: 計算しない（分母が0のため）
- **全体集計**: Threadsを除外してエンゲージメント率を計算

---

## 🛠️ トラブルシューティング

### エラー1: Analytics Addon未契約（402）

**症状**:
```
❌ Analytics Addon契約が必要です
   https://app.getlate.dev/settings/billing で契約してください
```

**解決策**:
1. Late API ダッシュボードにアクセス
2. Settings → Billing に移動
3. Analytics Addon を契約
4. 契約後、5-10分待機してから再実行

---

### エラー2: 環境変数未設定

**症状**:
```
❌ エラー: LATE_API_KEY が設定されていません
```

**解決策**:
1. `.env` ファイルを確認
2. `LATE_API_KEY=xxxxx` が設定されているか確認
3. **インラインコメント禁止**: コメント記号（#）を同じ行に書かない

**正しい .env 例**:
```bash
# Late API Key
LATE_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```

**間違った .env 例**:
```bash
LATE_API_KEY=xxxxxxxxxxxxxxxxxxxxx # My API Key ← これは NG
```

---

### エラー3: レート制限（429）

**症状**:
```
⚠️  Rate limit exceeded. Retrying in 1 hour...
```

**解決策**:
- **自動リトライ**: 1時間待機後に再実行（最大3回）
- **手動対応**: プランをアップグレード（Basic 30/min → Pro 300/min）

---

### エラー4: タイムアウト

**症状**:
```
❌ タイムアウト (Page 1)
```

**解決策**:
- **自動リトライ**: 30秒待機後に再実行（最大3回）
- ネットワーク接続を確認
- VPN使用時は切断して再試行

---

### エラー5: データ欠損（404）

**症状**:
```
⚠️  データが見つかりません (404)
```

**解決策**:
- 部分的に処理継続（取得できたデータのみでレポート生成）
- 期間を調整して再実行
- プラットフォーム別にデータ取得を試行

---

### エラー6: Python/ライブラリ未インストール

**症状**:
```
python3: command not found
ModuleNotFoundError: No module named 'requests'
```

**解決策**:
```bash
# Python 3.x インストール確認
python3 --version

# 必要なライブラリインストール
pip3 install requests
```

---

### エラー7: 日付計算エラー（Linux環境）

**症状**:
```
date: illegal option -- v
```

**解決策**:

macOSとLinuxで日付コマンドが異なります。SKILL.mdの該当箇所を確認してください：

**macOS**:
```bash
WEEK_AGO=$(date -v-7d +%Y-%m-%d)
```

**Linux**:
```bash
WEEK_AGO=$(date -d '7 days ago' +%Y-%m-%d)
```

---

## 📂 ファイル構成

```
.claude/skills/analyze-sns-performance-weekly/
├── SKILL.md                  # メインスキル定義（実行フロー）
├── README.md                 # 本ファイル（使い方ガイド）
├── kpi_targets.json          # KPI目標値定義
└── report_template.md        # Markdownレポートテンプレート
```

---

## 🔗 関連ドキュメント

### 内部参照

- **SKILL定義**: `@.claude/skills/analyze-sns-performance-weekly/SKILL.md`
- **KPI目標値**: `@.claude/skills/analyze-sns-performance-weekly/kpi_targets.json`
- **レポートテンプレート**: `@.claude/skills/analyze-sns-performance-weekly/report_template.md`

### 既存資産

- **Late APIスクリプト**: `@Stock/programs/副業/projects/SNS/scripts/fetch_late_analytics_optimized.py`
- **Late API OpenAPI仕様**: `@Flow/202601/2026-01-10/late-api-openapi.yaml`
- **Late API制約**: `@.claude/skills/sns-automation/LATE_API_CONSTRAINTS_AND_NOTES.md`
- **参考レポート**: `@Flow/202601/2026-01-10/sns_performance_analysis_20260101-0110.md`

---

## 📝 よくある質問（FAQ）

### Q1: Threadsのインプレッション数が0なのはバグですか？

A: いいえ、Late API の仕様です。Threadsプラットフォームが公式APIでインプレッション数を提供していないため、Late APIも取得できません。エンゲージメント絶対数（いいね、コメント、シェア）のみで評価してください。

### Q2: KPI目標値を変更したい

A: `kpi_targets.json` を編集してください。変更後は即座に反映されます。

### Q3: 過去のレポートを再生成したい

A: 可能です。Late APIスクリプトの `--from-date` と `--to-date` を指定して任意の期間のデータを取得できます。ただし、Late API のデータ保存期間に制限がある可能性があります。

### Q4: 他のプラットフォーム（Instagram、TikTok等）を追加したい

A: SKILL.mdを編集し、プラットフォーム別集計ロジックとレポートテンプレートにセクションを追加してください。Late APIが対応していれば、同じ方法でデータ取得できます。

### Q5: レポート形式をPDFに変更したい

A: 現在はMarkdown形式のみですが、`pandoc` 等のツールで変換可能です：
```bash
pandoc sns_performance_report_20260110.md -o sns_performance_report_20260110.pdf
```

---

## 🎯 成功基準

このSKILLが正常に動作していることを確認するチェックリスト：

- [ ] 実行時間が10-15分以内
- [ ] Markdownレポートが正しく生成される（5セクション構成）
- [ ] 表形式が崩れていない
- [ ] 数値フォーマットが適切（カンマ区切り、%表記）
- [ ] Threads特例表記が適切（"計測不可"）
- [ ] KPI達成率が正しく計算されている（4指標すべて）
- [ ] トップ5投稿が正しく抽出されている
- [ ] Analytics Addon未契約時に402エラー検出
- [ ] タイムアウト時に自動リトライ（最大3回）

---

## 📅 更新履歴

- **2026-01-10**: 初版リリース
  - 基本機能実装（LinkedIn、X、Threads対応）
  - KPI目標値比較機能
  - Threads特例処理実装
  - エラーハンドリング（402, 429, タイムアウト等）

---

## 📧 サポート

問題が解決しない場合は、以下の情報を含めて報告してください：

1. エラーメッセージ全文
2. 実行環境（macOS/Linux、Python version）
3. `.env` ファイルの設定状況（API Keyは伏せ字で）
4. Late API Analytics Addon契約状況
5. 実行時のコンソール出力

---

**作成者**: Claude Code
**バージョン**: 1.0.0
**最終更新**: 2026-01-10
