# Late API Analytics セットアップガイド

**最終更新**: 2026-01-03

データドリブン運用のための完全自動化セットアップ手順

---

## 📋 実装内容

### Phase 1: データ収集基盤（✅ 完了）
- 日次データ自動収集スクリプト
- SQLiteデータベース（analytics.db）
- CSVバックアップ機能

### Phase 2: KPIダッシュボード（✅ 完了）
- Streamlitリアルタイムダッシュボード
- プラットフォーム別分析
- 目標達成率可視化

### Phase 3: 勝ちパターン分析（✅ 完了）
- トップ/ボトム投稿自動分析
- 5W1H分析（時間帯、曜日）
- インサイトレポート自動生成

### Phase 4: 予測分析（✅ 完了）
- 時間帯×曜日ヒートマップ
- 最適投稿時間予測
- Top 3 / Worst 3時間帯特定

---

## 🚀 セットアップ手順

### ステップ1: 必要なパッケージインストール

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 必要なPythonパッケージをインストール
pip3 install requests pandas plotly streamlit
```

### ステップ2: ログディレクトリ作成

```bash
mkdir -p logs
mkdir -p data/insights
mkdir -p data/predictions
mkdir -p data/analytics_backup
```

### ステップ3: Late API設定確認

`.env`ファイルにAPI Keyが設定されていることを確認：

```bash
# .env
LATE_API_KEY=sk_your_api_key_here
```

`config/late_api_config.json`が正しく設定されていることを確認：

```json
{
  "api_key": "${LATE_API_KEY}",
  "base_url": "https://getlate.dev/api/v1",
  "accounts": {
    "linkedin": {
      "accountId": "ln_xxx",
      "platform": "linkedin"
    },
    "twitter": {
      "accountId": "tw_xxx",
      "platform": "twitter"
    },
    "facebook": {
      "accountId": "fb_xxx",
      "platform": "facebook"
    },
    "threads": {
      "accountId": "th_xxx",
      "platform": "threads"
    }
  }
}
```

### ステップ4: 初回データ収集テスト

```bash
# 環境変数を読み込み
source ../.env

# 初回データ収集を手動実行（前日データ取得）
python3 scripts/daily_analytics_collection.py
```

**期待される出力**:
```
🚀 Late API 日次アナリティクス収集開始
📅 収集対象日: 2026-01-02

📊 FACEBOOK データ取得中...
   取得件数: 5件
📊 LINKEDIN データ取得中...
   取得件数: 3件
📊 TWITTER データ取得中...
   取得件数: 2件
📊 THREADS データ取得中...
   取得件数: 1件

✅ データベース保存完了: 11件新規, 0件更新
✅ CSVバックアップ保存: data/analytics_backup/analytics_2026-01-02.csv

✅ 日次アナリティクス収集完了
```

データベース確認:
```bash
sqlite3 data/analytics.db "SELECT COUNT(*) FROM analytics;"
# 出力例: 11
```

### ステップ5: KPIダッシュボード起動

```bash
streamlit run scripts/kpi_dashboard.py
```

ブラウザで `http://localhost:8501` にアクセスしてダッシュボード確認。

### ステップ6: 勝ちパターン分析実行

```bash
python3 scripts/analyze_winning_patterns.py
```

**出力ファイル**:
- `data/insights/insights_report_20260103.md` - Markdownレポート
- `data/insights/insights_data_20260103.json` - JSONデータ

### ステップ7: 予測分析実行

```bash
python3 scripts/predict_optimal_time.py
```

**出力ファイル**:
- `data/predictions/heatmap_facebook_20260103.html` - ヒートマップ（ブラウザで開く）
- `data/predictions/prediction_facebook_20260103.md` - 予測レポート

---

## ⏰ 定期実行設定（自動化）

### 方法1: launchd（macOS推奨）

#### 1. 環境変数を設定

`com.sns.analytics.daily.plist`を編集し、`${LATE_API_KEY}`を実際のAPI Keyに置換：

```bash
# API Keyを取得
echo $LATE_API_KEY

# plistファイルを編集
nano config/com.sns.analytics.daily.plist
```

`<string>${LATE_API_KEY}</string>`を`<string>sk_your_actual_api_key</string>`に変更。

#### 2. launchdに登録

```bash
# plistファイルをLaunchAgentsにコピー
cp config/com.sns.analytics.daily.plist ~/Library/LaunchAgents/

# launchdに読み込み
launchctl load ~/Library/LaunchAgents/com.sns.analytics.daily.plist

# ステータス確認
launchctl list | grep com.sns.analytics.daily
```

#### 3. 今すぐテスト実行

```bash
launchctl start com.sns.analytics.daily

# ログ確認
tail -f logs/daily_analytics.log
```

#### 4. 停止・削除（必要時）

```bash
# 停止
launchctl unload ~/Library/LaunchAgents/com.sns.analytics.daily.plist

# 削除
rm ~/Library/LaunchAgents/com.sns.analytics.daily.plist
```

---

### 方法2: cron（シンプル）

#### cron設定

```bash
crontab -e
```

以下を追加（毎日AM 9:00に実行）:

```cron
# Late API 日次データ収集
0 9 * * * cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS && /usr/bin/python3 scripts/daily_analytics_collection.py >> logs/daily_analytics.log 2>&1

# 週次: 勝ちパターン分析（毎週月曜 10:00）
0 10 * * 1 cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS && /usr/bin/python3 scripts/analyze_winning_patterns.py >> logs/weekly_insights.log 2>&1

# 週次: 予測分析（毎週月曜 10:30）
30 10 * * 1 cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS && /usr/bin/python3 scripts/predict_optimal_time.py >> logs/weekly_prediction.log 2>&1
```

**注意**: cronは環境変数を読み込まないため、スクリプト内で直接API Keyを設定するか、以下のように修正：

```cron
0 9 * * * source /Users/yuichi/.env && cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS && /usr/bin/python3 scripts/daily_analytics_collection.py >> logs/daily_analytics.log 2>&1
```

---

## 📊 運用フロー

### 日次（自動実行）
1. **AM 9:00**: `daily_analytics_collection.py`が自動実行
   - 前日のデータを全プラットフォームから取得
   - SQLiteに保存
   - CSVバックアップ

### 週次（自動実行）
2. **月曜 AM 10:00**: `analyze_winning_patterns.py`が自動実行
   - 過去30日のトップ/ボトム投稿を分析
   - インサイトレポート生成

3. **月曜 AM 10:30**: `predict_optimal_time.py`が自動実行
   - 過去90日のデータから最適投稿時間を予測
   - ヒートマップ生成

### 随時（手動実行）
4. **KPIダッシュボード確認**: `streamlit run scripts/kpi_dashboard.py`
   - リアルタイムKPI確認
   - 目標達成率モニタリング

---

## 📈 データフロー

```
Late API
   ↓ (毎日AM 9:00)
daily_analytics_collection.py
   ↓
analytics.db (SQLite)
   ├→ KPIダッシュボード（Streamlit） - リアルタイム表示
   ├→ 勝ちパターン分析 - 週次レポート
   └→ 予測分析 - 週次ヒートマップ
```

---

## 🔧 トラブルシューティング

### 1. データが取得できない

**症状**: `⚠️ データなし`と表示される

**原因**:
- Late API Key が無効
- 前日に投稿がない
- プラットフォーム接続が切れている

**対処**:
```bash
# API Key確認
echo $LATE_API_KEY

# Late APIダッシュボードで接続状態確認
# https://app.getlate.dev/

# 手動でテスト実行
python3 scripts/late_api_analytics.py
```

### 2. launchdが実行されない

**症状**: AM 9:00になっても実行されない

**対処**:
```bash
# launchdステータス確認
launchctl list | grep com.sns.analytics.daily

# エラーログ確認
cat logs/daily_analytics_error.log

# 手動で起動テスト
launchctl start com.sns.analytics.daily
```

### 3. ダッシュボードにデータが表示されない

**症状**: `⚠️ データがありません`と表示される

**対処**:
```bash
# データベースにデータがあるか確認
sqlite3 data/analytics.db "SELECT COUNT(*) FROM analytics;"

# データがない場合は手動収集
python3 scripts/daily_analytics_collection.py
```

### 4. Streamlitが起動しない

**症状**: `streamlit: command not found`

**対処**:
```bash
# Streamlitインストール
pip3 install streamlit

# または
python3 -m pip install streamlit
```

---

## 📊 期待される効果

| 項目 | 導入前 | 導入後 | 削減率 |
|------|--------|--------|--------|
| **手動集計時間** | 15分/日 | 0分 | **-100%** |
| **週次分析時間** | 60分/週 | 0分 | **-100%** |
| **KPI確認時間** | データなし | 5秒 | - |
| **改善サイクル** | なし | 週次 | - |

**月間削減時間**: 450分（7.5時間）+ 240分（4時間）= **690分（11.5時間/月）**

**改善効果（推定）**:
- 勝ちパターン比率向上: **+166,234 imp/月**
- 最適時間帯投稿: **+80,000 imp/月**
- 合計: **+246,234 imp/月（目標ギャップの37.7%解消）**

---

## 🎯 次のステップ

1. **1週間データ蓄積**: まず7日間データを収集
2. **ダッシュボード確認習慣化**: 毎朝ダッシュボードをチェック
3. **週次レポートレビュー**: 月曜のインサイトレポートを投稿計画に反映
4. **A/Bテスト実施**: 予測された最適時間帯でテスト投稿

---

## 📚 参照

- Late API公式ドキュメント: https://docs.getlate.dev/
- Streamlitドキュメント: https://docs.streamlit.io/
- SQLite公式ドキュメント: https://www.sqlite.org/docs.html

---

**セットアップ完了日**: 2026-01-03
**バージョン**: 1.0
