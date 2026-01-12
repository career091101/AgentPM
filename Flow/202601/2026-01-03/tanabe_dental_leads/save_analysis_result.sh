#!/bin/bash
# Webサイト分析結果を保存するスクリプト

# 使用方法:
# bash save_analysis_result.sh 1 '{...JSON...}'

CLINIC_NUM=$1
JSON_RESULT=$2

if [ -z "$CLINIC_NUM" ] || [ -z "$JSON_RESULT" ]; then
    echo "Usage: bash save_analysis_result.sh <clinic_number> '<json_result>'"
    exit 1
fi

# 医院名を抽出（簡易実装）
CLINIC_NAME=$(echo "$JSON_RESULT" | grep -o '"clinic_name": "[^"]*"' | cut -d'"' -f4)

# ファイル名生成
OUTPUT_FILE="analysis_$(printf '%03d' $CLINIC_NUM)_${CLINIC_NAME}.json"

# JSON保存
echo "$JSON_RESULT" > "$OUTPUT_FILE"

echo "✅ 保存完了: $OUTPUT_FILE"
