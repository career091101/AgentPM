#!/bin/bash
# 週次レポート自動実行スクリプト
#
# cron設定例（毎週月曜 8:00実行）:
# 0 8 * * 1 /Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents/scripts/cron_weekly_report.sh

# プロジェクトルートに移動
cd "$(dirname "$0")/.." || exit 1

# ログディレクトリ作成
mkdir -p logs

# 前週の期間を自動計算（macOS対応）
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    WEEK_START=$(date -v-14d -v+mon +%Y-%m-%d)
    WEEK_END=$(date -v-7d -v+fri +%Y-%m-%d)
else
    # Linux
    WEEK_START=$(date -d "last monday -7 days" +%Y-%m-%d)
    WEEK_END=$(date -d "last friday" +%Y-%m-%d)
fi

echo "================================================"
echo "週次レポート自動実行"
echo "対象期間: $WEEK_START 〜 $WEEK_END"
echo "実行日時: $(date '+%Y-%m-%d %H:%M:%S')"
echo "================================================"

# Python環境確認
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "❌ Pythonが見つかりません"
    exit 1
fi

echo "Python: $($PYTHON_CMD --version)"

# レポート生成
$PYTHON_CMD scripts/generate_weekly_report.py \
    --week-start "$WEEK_START" \
    --week-end "$WEEK_END" \
    >> "logs/weekly_report_$(date +%Y%m%d).log" 2>&1

# 成功/失敗通知
if [ $? -eq 0 ]; then
    echo "✅ 週次レポート生成成功"
    echo "ログ: logs/weekly_report_$(date +%Y%m%d).log"

    # メール通知（オプション: 必要に応じてコメント解除）
    # mail -s "TradingAgents 週次レポート生成完了" user@example.com < "logs/weekly_report_$(date +%Y%m%d).log"

else
    echo "❌ 週次レポート生成失敗"
    echo "ログを確認してください: logs/weekly_report_$(date +%Y%m%d).log"

    # エラー通知（オプション: 必要に応じてコメント解除）
    # mail -s "TradingAgents 週次レポート生成エラー" user@example.com < "logs/weekly_report_$(date +%Y%m%d).log"

    exit 1
fi

echo "================================================"
