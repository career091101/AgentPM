#!/bin/bash
# 30分ごとの進捗監視スクリプト

INTERVAL=1800  # 30分 = 1800秒
CHECK_SCRIPT="/Users/yuichi/AIPM/aipm_v0/scripts/check_progress.sh"
REPORT_FILE="/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/progress_reports.txt"

# 初回レポート
echo "========================================" | tee -a "$REPORT_FILE"
echo "Phase 3.5 進捗監視開始" | tee -a "$REPORT_FILE"
echo "開始時刻: $(date '+%Y-%m-%d %H:%M:%S')" | tee -a "$REPORT_FILE"
echo "========================================" | tee -a "$REPORT_FILE"

# 30分ごとにチェック（最大6回 = 3時間）
for i in {1..6}; do
    sleep $INTERVAL
    echo "" | tee -a "$REPORT_FILE"
    echo "========================================" | tee -a "$REPORT_FILE"
    echo "進捗レポート #$i（$(date '+%Y-%m-%d %H:%M:%S')）" | tee -a "$REPORT_FILE"
    echo "========================================" | tee -a "$REPORT_FILE"
    $CHECK_SCRIPT | tee -a "$REPORT_FILE"
    
    # 完了チェック
    if grep -q "処理完了！" /Users/yuichi/AIPM/aipm_v0/scripts/enricher_full_run.log; then
        echo "" | tee -a "$REPORT_FILE"
        echo "✅ 全件処理が完了しました！" | tee -a "$REPORT_FILE"
        break
    fi
done
