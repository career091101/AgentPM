#!/bin/bash
# cron自動レビュー設定スクリプト

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../../../../.." && pwd)"
SCHEDULER_SCRIPT="$SCRIPT_DIR/auto_review_scheduler.py"
LOG_DIR="$BASE_DIR/Flow/logs/review_automation"

# ログディレクトリ作成
mkdir -p "$LOG_DIR"

# cronジョブ設定
CRON_JOB="0 9 * * * cd $BASE_DIR && python3 $SCHEDULER_SCRIPT run >> $LOG_DIR/review_automation_\$(date +\%Y\%m\%d).log 2>&1"

echo "🔧 cron自動レビュー設定"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "以下のcronジョブを追加します:"
echo ""
echo "$CRON_JOB"
echo ""
echo "スケジュール: 毎日9時に実行"
echo "ログ出力先: $LOG_DIR"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 確認
read -p "cronジョブを追加しますか？ (y/n): " confirm

if [ "$confirm" != "y" ]; then
    echo "❌ キャンセルしました"
    exit 0
fi

# 既存のcronジョブを確認
EXISTING_CRON=$(crontab -l 2>/dev/null | grep -F "$SCHEDULER_SCRIPT" || true)

if [ -n "$EXISTING_CRON" ]; then
    echo "⚠️  同じスクリプトのcronジョブが既に存在します:"
    echo "$EXISTING_CRON"
    echo ""
    read -p "既存のジョブを削除して新しいジョブを追加しますか？ (y/n): " replace_confirm

    if [ "$replace_confirm" != "y" ]; then
        echo "❌ キャンセルしました"
        exit 0
    fi

    # 既存のジョブを削除
    crontab -l 2>/dev/null | grep -v -F "$SCHEDULER_SCRIPT" | crontab -
    echo "✅ 既存のジョブを削除しました"
fi

# 新しいcronジョブを追加
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo ""
echo "✅ cronジョブを追加しました"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 現在のcronジョブ一覧:"
echo ""
crontab -l
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔍 手動テスト実行:"
echo ""
echo "  cd $BASE_DIR"
echo "  python3 $SCHEDULER_SCRIPT run"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
