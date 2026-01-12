#!/bin/bash
# Phase 3.5進捗確認スクリプト

LOG_FILE="/Users/yuichi/AIPM/aipm_v0/scripts/enricher_full_run.log"

echo "============================================================"
echo "Phase 3.5 進捗状況（$(date '+%Y-%m-%d %H:%M:%S')）"
echo "============================================================"

# 処理済み件数を抽出
if [ -f "$LOG_FILE" ]; then
    # 最後の [N/823] を取得
    LAST_PROGRESS=$(grep -oE '\[[0-9]+/823\]' "$LOG_FILE" | tail -1)
    if [ -n "$LAST_PROGRESS" ]; then
        CURRENT=$(echo "$LAST_PROGRESS" | grep -oE '[0-9]+' | head -1)
        TOTAL=823
        PERCENTAGE=$(awk "BEGIN {printf \"%.1f\", ($CURRENT/$TOTAL)*100}")
        
        echo "処理済み: $CURRENT / $TOTAL 件（$PERCENTAGE%）"
        
        # 成功/失敗件数を取得
        SUCCESS=$(grep -c "✅ メディア抽出成功" "$LOG_FILE")
        REPLIES=$(grep -c "✅ リプライ抽出成功" "$LOG_FILE")
        
        echo "メディア抽出成功: $SUCCESS 件"
        echo "リプライ抽出成功: $REPLIES 件"
        
        # 推定残り時間を計算（14.5秒/件ベース）
        REMAINING=$((TOTAL - CURRENT))
        ESTIMATED_SECONDS=$((REMAINING * 15))
        ESTIMATED_MINUTES=$((ESTIMATED_SECONDS / 60))
        ESTIMATED_HOURS=$((ESTIMATED_MINUTES / 60))
        REMAINING_MINUTES=$((ESTIMATED_MINUTES % 60))
        
        echo ""
        echo "推定残り時間: ${ESTIMATED_HOURS}時間${REMAINING_MINUTES}分"
        
        # 完了予定時刻を計算
        COMPLETION_TIME=$(date -v+${ESTIMATED_SECONDS}S '+%Y-%m-%d %H:%M:%S')
        echo "完了予定時刻: $COMPLETION_TIME"
        
        echo ""
        echo "最新ログ（最後の15行）:"
        echo "------------------------------------------------------------"
        tail -15 "$LOG_FILE"
    else
        echo "進捗情報が見つかりません（処理開始前）"
    fi
else
    echo "ログファイルが見つかりません: $LOG_FILE"
fi

echo "============================================================"
