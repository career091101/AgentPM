# TradingAgents 運用マニュアル

**バージョン**: 1.0
**最終更新**: 2026-01-01
**対象**: Phase 5完了後の実運用

---

## 1. システム概要

TradingAgentsは日経平均先物のスイングトレード戦略システムです。

### 主要機能

- レジーム別最適化（Bull/Bear/Sideways）
- 動的レジーム切り替え戦略
- 週次戦略レポート自動生成
- Walk-forward分析
- バックテスト信頼性97.5%

---

## 2. 起動手順

### 2-1. Python環境確認

```bash
python3 --version
# Python 3.9以上必須、3.10+推奨
```

### 2-2. 依存パッケージインストール

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents
pip3 install -r requirements.txt
```

### 2-3. 最新データ検証

```bash
python3 scripts/validate_latest_data.py
```

**期待される出力**:
- ✅ データ取得成功
- ✅ データ品質OK
- ✅ レジーム検出成功
- ✅ シグナル生成成功

---

## 3. 週次レポート生成手順

### 手動実行

```bash
# 前週のレポート生成（自動で前週期間を計算）
python3 scripts/generate_weekly_report.py

# 特定期間のレポート生成
python3 scripts/generate_weekly_report.py \
    --week-start 2025-12-23 \
    --week-end 2025-12-27
```

### 自動実行（cron設定）

```bash
# cron設定を編集
crontab -e

# 以下を追加（毎週月曜 8:00実行）
0 8 * * 1 /path/to/TradingAgents/scripts/cron_weekly_report.sh
```

---

## 4. トラブルシューティング

### エラー1: yfinanceデータ取得失敗

**症状**:
```
❌ データ取得失敗: HTTPError 429
```

**原因**: API制限

**対処法**:
1. 5分待ってリトライ
2. ローカルキャッシュ使用: `--use-cache`フラグ
3. サンプルデータで代替

### エラー2: レジーム検出失敗

**症状**:
```
ValueError: No periods found for regime: BULL
```

**原因**: データ期間が短い、または特定レジームが存在しない

**対処法**:
1. データ期間を延長（最低6ヶ月推奨）
2. 他のレジームで実行
3. 複合レジーム検出使用

### エラー3: メモリ不足

**症状**:
```
MemoryError
```

**原因**: データ量が大きすぎる

**対処法**:
1. データ期間を短縮
2. メモリ解放: `gc.collect()`
3. バッチ処理に分割

### エラー4: シグナル生成失敗

**症状**:
```
❌ シグナル生成失敗: KeyError
```

**原因**: データカラム不足、または計算エラー

**対処法**:
1. データ整合性確認: `validate_latest_data.py`実行
2. テクニカル指標計算に必要な最小期間（200日）確保
3. ログファイル確認: `logs/`

### エラー5: パフォーマンスモニター初期化失敗

**症状**:
```
ImportError: No module named 'psutil'
```

**原因**: 依存パッケージ未インストール

**対処法**:
```bash
pip3 install psutil
```

---

## 5. エラーコード一覧

| コード | 説明 | 対処法 |
|--------|------|--------|
| E001 | データ取得失敗 | API制限確認、リトライ |
| E002 | レジーム検出失敗 | データ期間確認 |
| E003 | シグナル生成失敗 | パラメータ確認 |
| E004 | バックテスト失敗 | データ品質確認 |
| E005 | レポート生成失敗 | テンプレート確認 |

---

## 6. メンテナンス手順

### 月次メンテナンス

1. ログファイル削除（30日以上前）
   ```bash
   find logs/ -name "*.log" -mtime +30 -delete
   ```

2. キャッシュ更新
   ```bash
   rm -f data/cache/*.csv
   python3 scripts/validate_latest_data.py
   ```

3. パフォーマンス確認
   ```bash
   python3 scripts/run_live_simulation.py --days 30
   ```

### 年次メンテナンス

1. 全データ再取得
2. バックテスト再実行
3. KPI目標再評価
4. システムアップデート

---

## 7. 緊急時対応

### システム停止手順

```bash
# 実行中プロセス確認
ps aux | grep python3

# プロセス終了
kill -9 [PID]
```

### データ復旧手順

```bash
# バックアップから復元
cp data/backup/*.csv data/cache/

# データ整合性確認
python3 scripts/validate_latest_data.py
```

---

## 8. パフォーマンス最適化

### メモリ使用量削減

- データロード時の期間を必要最小限に制限
- 不要な中間データの削除（`del`, `gc.collect()`）
- チャンク処理の活用

### 実行時間短縮

- キャッシュの活用（`--use-cache`）
- 並列処理の検討（multiprocessing）
- レジーム検出頻度の調整

---

## 9. 問い合わせ先

- システム担当: Claude Code
- プロジェクトオーナー: yuichi
- ドキュメント: documents/

---

## 10. 推奨運用フロー

### 週次運用

1. **月曜日 8:00**: 自動で週次レポート生成
2. **月曜日 9:00**: レポート確認、戦略パラメータ調整検討
3. **火曜日〜金曜日**: 日次でシグナル確認（オプション）
4. **金曜日 17:00**: 週次パフォーマンスレビュー

### 月次運用

1. **月初**: 前月パフォーマンスサマリー作成
2. **月初**: ログ・キャッシュクリーンアップ
3. **月末**: 次月パラメータ調整検討

---

**免責事項**: このシステムは情報提供のみを目的としており、投資助言ではありません。
