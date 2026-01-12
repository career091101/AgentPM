# SNS投稿自動レビュー自動化セットアップガイド

## 概要

投稿生成直後と予約投稿の1日後に自動的にレビューを実行する仕組みを構築しました。

**実行タイミング**:
1. **投稿生成直後**: 投稿ファイル生成後に即座にレビュー実行
2. **予約投稿の1日後**: Late API予約投稿の公開日の1日後にレビュー実行（効果測定）

---

## ファイル構成

### 1. コアスクリプト

#### auto_review_scheduler.py
**パス**: `.claude/skills/sns-automation/review-and-improve-skill/automation/auto_review_scheduler.py`

**機能**:
- 投稿生成直後のレビュー実行
- 予約投稿の1日後のレビューをスケジュール
- スケジュールされたレビューの実行（日次）
- レビュー結果の記録と通知

**サブコマンド**:
```bash
# 投稿生成直後のレビュー
python3 auto_review_scheduler.py immediate --post-file <投稿ファイル>

# 予約投稿の1日後のレビューをスケジュール
python3 auto_review_scheduler.py schedule \
  --post-file <投稿ファイル> \
  --publication-date YYYY-MM-DD

# スケジュールされたレビューを実行（日次実行想定）
python3 auto_review_scheduler.py run

# スケジュール一覧を表示
python3 auto_review_scheduler.py list
```

### 2. 設定ファイル

#### schedule_config.json
**パス**: `.claude/skills/sns-automation/review-and-improve-skill/automation/schedule_config.json`

**主要設定**:
```json
{
  "immediate_review": {
    "enabled": true,              // 投稿生成直後のレビューを有効化
    "auto_apply": false,          // 自動修正を無効（手動確認推奨）
    "priority": ["P0", "P1"]      // 優先度P0, P1の問題のみ対応
  },
  "post_publication_review": {
    "enabled": true,              // 予約投稿の1日後のレビューを有効化
    "delay_days": 1,              // 公開日の1日後に実行
    "auto_apply": true,           // 自動修正を有効化
    "priority": ["P0", "P1"]
  },
  "notification": {
    "enabled": true,
    "method": "file"              // ファイル通知（Slack/メール未実装）
  }
}
```

### 3. フックスクリプト

#### post_generation_hook.py
**パス**: `Stock/programs/副業/projects/SNS/scripts/hooks/post_generation_hook.py`

**機能**: 投稿生成直後に自動レビューをトリガー

**使用方法**:
```bash
python3 post_generation_hook.py <投稿ファイル>
```

#### late_api_post_hook.py
**パス**: `Stock/programs/副業/projects/SNS/scripts/hooks/late_api_post_hook.py`

**機能**: Late API投稿後に予約投稿の1日後のレビューをスケジュール

**使用方法**:
```bash
python3 late_api_post_hook.py <投稿ファイル> '<Late APIレスポンスJSON>'
```

### 4. cronセットアップスクリプト

#### setup_cron.sh
**パス**: `.claude/skills/sns-automation/review-and-improve-skill/automation/setup_cron.sh`

**機能**: 日次レビュー実行のcronジョブを自動設定

**使用方法**:
```bash
chmod +x setup_cron.sh
./setup_cron.sh
```

---

## セットアップ手順

### Step 1: cronジョブの設定

日次でスケジュールされたレビューを実行するcronジョブを設定します。

```bash
cd /Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/review-and-improve-skill/automation
chmod +x setup_cron.sh
./setup_cron.sh
```

**設定内容**:
- 実行時刻: 毎日9時
- 実行内容: `python3 auto_review_scheduler.py run`
- ログ出力: `Flow/logs/review_automation/review_automation_YYYYMMDD.log`

**確認**:
```bash
crontab -l | grep auto_review_scheduler
```

### Step 2: 投稿生成スクリプトへの統合

投稿生成スクリプトに自動レビューフックを追加します。

#### 統合例（generate-sns-posts-takano スキル実行後）

**方法1: スキル実行後に手動実行**
```bash
# 投稿生成
claude-code skill sns-automation/generate-sns-posts-takano \
  --input "ソースデータ"

# 生成直後のレビュー
python3 Stock/programs/副業/projects/SNS/scripts/hooks/post_generation_hook.py \
  Flow/202601/2026-01-06/posts_generated_takano_20260106.md
```

**方法2: 自動実行スクリプトの作成**

新規ファイル: `Stock/programs/副業/projects/SNS/scripts/generate_and_review.sh`

```bash
#!/bin/bash
# 投稿生成 + 自動レビュー

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../../../../.." && pwd)"

# 投稿生成
echo "📝 投稿を生成中..."
claude-code skill sns-automation/generate-sns-posts-takano "$@"

# 最新の投稿ファイルを取得
LATEST_POST=$(ls -t "$BASE_DIR"/Flow/202601/*/posts_generated_takano_*.md | head -n 1)

if [ -z "$LATEST_POST" ]; then
    echo "❌ 投稿ファイルが見つかりません"
    exit 1
fi

echo "✅ 投稿生成完了: $LATEST_POST"

# 自動レビュー実行
echo ""
python3 "$SCRIPT_DIR/hooks/post_generation_hook.py" "$LATEST_POST"
```

使用方法:
```bash
chmod +x Stock/programs/副業/projects/SNS/scripts/generate_and_review.sh
./Stock/programs/副業/projects/SNS/scripts/generate_and_review.sh --input "ソースデータ"
```

### Step 3: Late API投稿スクリプトへの統合

Late API投稿スクリプトに予約投稿の1日後のレビューをスケジュールするフックを追加します。

#### fix_late_api_multi_post.py への統合

**修正箇所**: `Stock/programs/副業/projects/SNS/scripts/fix_late_api_multi_post.py` の最終部分

**修正前**:
```python
# Late API投稿実行
response = post_to_late_api(title, body, scheduled_time)
print(f"✅ Late APIへの投稿完了")
print(f"   Post ID: {response.get('id', 'N/A')}")
```

**修正後**:
```python
# Late API投稿実行
response = post_to_late_api(title, body, scheduled_time)
print(f"✅ Late APIへの投稿完了")
print(f"   Post ID: {response.get('id', 'N/A')}")

# 予約投稿の1日後のレビューをスケジュール
import subprocess
import json

hook_script = Path(__file__).parent / "hooks/late_api_post_hook.py"
if hook_script.exists():
    try:
        subprocess.run([
            "python3", str(hook_script),
            str(markdown_file),
            json.dumps(response)
        ], check=True)
    except Exception as e:
        print(f"⚠️  レビュースケジュール登録エラー: {str(e)}")
```

---

## 動作フロー

### フロー1: 投稿生成直後のレビュー

```
1. ユーザーが投稿生成スキルを実行
   ↓
2. 投稿ファイル生成（posts_generated_takano_YYYYMMDD.md）
   ↓
3. post_generation_hook.py が自動実行される
   ↓
4. auto_review_scheduler.py immediate が実行される
   ↓
5. check_required_elements.py で品質評価
   ↓
6. レビューレポート生成（Flow/.../reviews/review_report_immediate_*.md）
   ↓
7. スコアが70点未満の場合、改善提案を表示
   ↓
8. 通知ファイル生成（Flow/notifications/review_notification_*.md）
```

### フロー2: 予約投稿の1日後のレビュー

```
1. ユーザーがLate API投稿スクリプトを実行
   ↓
2. Late APIに予約投稿（scheduled_time: 2026-01-10T09:00:00Z）
   ↓
3. late_api_post_hook.py が自動実行される
   ↓
4. auto_review_scheduler.py schedule が実行される
   ↓
5. スケジュールDB（schedule_db.json）に登録
   - publication_date: 2026-01-10
   - review_date: 2026-01-11（1日後）
   ↓
6. cronジョブが毎日9時に auto_review_scheduler.py run を実行
   ↓
7. 2026-01-11 9時にスケジュールされたレビューが実行される
   ↓
8. check_required_elements.py で品質評価
   ↓
9. レビューレポート生成（Flow/.../reviews/review_report_post_publication_*.md）
   ↓
10. auto_apply=trueの場合、スキル自動改善を実行（現在は未実装）
   ↓
11. 通知ファイル生成
```

---

## 出力ファイル

### 1. レビューレポート

**保存先**: `Flow/202601/YYYY-MM-DD/reviews/review_report_<type>_<timestamp>.md`

**例**:
```
Flow/202601/2026-01-06/reviews/review_report_immediate_20260106_143000.md
Flow/202601/2026-01-11/reviews/review_report_post_publication_20260111_090000.md
```

**内容**:
- 総合スコア
- 各評価項目の詳細（口語体、拡張フレーズ、数値データ、企業名、文字数）
- 改善提案
- 詳細データ（JSON）

### 2. スケジュールDB

**保存先**: `.claude/skills/sns-automation/review-and-improve-skill/automation/schedule_db.json`

**内容**:
```json
{
  "scheduled_reviews": [
    {
      "id": "review_20260106_143000",
      "post_file_path": "Flow/202601/2026-01-06/posts_generated_takano_20260106.md",
      "publication_date": "2026-01-10",
      "review_date": "2026-01-11",
      "review_type": "post_publication",
      "auto_apply": true,
      "priority": ["P0", "P1"],
      "status": "scheduled",
      "created_at": "2026-01-06T14:30:00"
    }
  ],
  "completed_reviews": []
}
```

### 3. 通知ファイル

**保存先**: `Flow/notifications/review_notification_<timestamp>.md`

**内容**:
- レビュー実行日時
- メッセージ
- 結果詳細（ステータス、スコア、レポートパス）

### 4. 実行ログ

**保存先**: `Flow/logs/review_automation/review_automation_YYYYMMDD.log`

**内容**:
- cronジョブ実行ログ
- スケジュールされたレビューの実行結果
- エラーログ

---

## トラブルシューティング

### 問題1: cronジョブが実行されない

**原因**: cronが無効、またはパスの問題

**確認方法**:
```bash
# cronサービスの状態確認（Linux）
sudo systemctl status cron

# macOS
sudo launchctl list | grep cron
```

**手動テスト**:
```bash
cd /Users/yuichi/AIPM/aipm_v0
python3 .claude/skills/sns-automation/review-and-improve-skill/automation/auto_review_scheduler.py run
```

### 問題2: レビューレポートが生成されない

**原因**: 投稿ファイルのパスが間違っている、または形式が不正

**確認方法**:
```bash
# 投稿ファイルの存在確認
ls -la Flow/202601/2026-01-06/posts_generated_takano_*.md

# 手動レビュー実行
python3 .claude/skills/sns-automation/review-and-improve-skill/automation/auto_review_scheduler.py \
  immediate --post-file "Flow/202601/2026-01-06/posts_generated_takano_20260106.md"
```

### 問題3: スケジュールDBが更新されない

**原因**: 書き込み権限の問題、またはJSON形式エラー

**確認方法**:
```bash
# 権限確認
ls -la .claude/skills/sns-automation/review-and-improve-skill/automation/schedule_db.json

# JSON形式確認
cat .claude/skills/sns-automation/review-and-improve-skill/automation/schedule_db.json | python3 -m json.tool
```

### 問題4: Late APIレスポンスのパースエラー

**原因**: Late APIのレスポンス形式が想定と異なる

**対処法**:
```bash
# Late APIレスポンスの確認
# late_api_post_hook.py を修正して実際のレスポンス形式に対応
```

実際のレスポンス例をログに出力して確認し、`extract_publication_date_from_late_response()` 関数を調整してください。

---

## カスタマイズ

### レビュー実行時刻の変更

**ファイル**: `.claude/skills/sns-automation/review-and-improve-skill/automation/schedule_config.json`

```json
{
  "schedule_check": {
    "cron_expression": "0 21 * * *",  // 21時に変更
    "description": "毎日21時にスケジュールされたレビューを実行"
  }
}
```

cronジョブも同様に変更:
```bash
crontab -e

# 変更前
0 9 * * * cd /Users/yuichi/AIPM/aipm_v0 && python3 ...

# 変更後
0 21 * * * cd /Users/yuichi/AIPM/aipm_v0 && python3 ...
```

### 予約投稿の遅延日数の変更

**ファイル**: `.claude/skills/sns-automation/review-and-improve-skill/automation/schedule_config.json`

```json
{
  "post_publication_review": {
    "delay_days": 3  // 3日後に変更
  }
}
```

### 自動修正の有効化（投稿生成直後）

**ファイル**: `.claude/skills/sns-automation/review-and-improve-skill/automation/schedule_config.json`

```json
{
  "immediate_review": {
    "auto_apply": true  // 有効化（現在は未実装）
  }
}
```

**注意**: 自動修正機能は現在開発中です。有効化しても実際の修正は実行されません。

---

## 次のステップ

### 即時対応（1週間以内）

1. **cronジョブの設定**
   ```bash
   cd /Users/yuichi/AIPM/aipm_v0/.claude/skills/sns-automation/review-and-improve-skill/automation
   ./setup_cron.sh
   ```

2. **テスト実行**
   ```bash
   # 投稿生成直後のレビューをテスト
   python3 auto_review_scheduler.py immediate \
     --post-file "Flow/202601/2026-01-06/posts_generated_takano_20260105.md"

   # スケジュール登録をテスト
   python3 auto_review_scheduler.py schedule \
     --post-file "Flow/202601/2026-01-06/posts_generated_takano_20260105.md" \
     --publication-date "2026-01-10"

   # スケジュール実行をテスト（今日の日付に設定して確認）
   python3 auto_review_scheduler.py run
   ```

### 短期対応（2週間以内）

3. **Late API投稿スクリプトへの統合**
   - `fix_late_api_multi_post.py` に `late_api_post_hook.py` の呼び出しを追加
   - 実際のLate APIレスポンス形式を確認して調整

4. **自動投稿生成スクリプトの作成**
   - `generate_and_review.sh` を作成
   - 投稿生成 → 自動レビュー → Late API投稿の一連のフローを自動化

### 中期対応（1ヶ月以内）

5. **自動修正機能の実装**
   - `auto_review_scheduler.py` の `run_auto_improvement()` メソッドを実装
   - SKILL.mdの自動修正ロジックを追加

6. **Slack/メール通知の実装**
   - `send_slack_notification()` メソッドの実装
   - `send_email_notification()` メソッドの実装

---

## 関連ドキュメント

- **スキル定義**: `.claude/skills/sns-automation/review-and-improve-skill/SKILL.md`
- **スケジューラー**: `.claude/skills/sns-automation/review-and-improve-skill/automation/auto_review_scheduler.py`
- **設定ファイル**: `.claude/skills/sns-automation/review-and-improve-skill/automation/schedule_config.json`
- **フックスクリプト**:
  - `Stock/programs/副業/projects/SNS/scripts/hooks/post_generation_hook.py`
  - `Stock/programs/副業/projects/SNS/scripts/hooks/late_api_post_hook.py`
- **投稿生成スキル**: `.claude/skills/sns-automation/generate-sns-posts-takano/SKILL.md`
- **Late API投稿スクリプト**: `Stock/programs/副業/projects/SNS/scripts/fix_late_api_multi_post.py`

---

**作成日**: 2026-01-06
**作成者**: Claude Code (Sonnet 4.5)
**バージョン**: 1.0.0
**適用範囲**: SNS投稿の品質管理自動化
