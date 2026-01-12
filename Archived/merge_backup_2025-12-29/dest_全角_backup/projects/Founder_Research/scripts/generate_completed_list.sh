#!/bin/bash

# 完了リスト生成スクリプト
# 用途: 完了済みケーススタディの一覧を生成

echo "# 完了済みケーススタディ一覧"
echo ""
echo "最終更新: $(date '+%Y-%m-%d')"
total=$(find documents -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
echo "総件数: $total/500 ($(echo "scale=1; $total*100/500" | bc 2>/dev/null || echo "0")%)"
echo ""

echo "## サマリー"
echo ""
echo "| ティア | 完了件数 |"
echo "|--------|---------|"

for tier_dir in documents/*/; do
  if [[ ! -d "$tier_dir" ]]; then
    continue
  fi

  tier=$(basename "$tier_dir")
  count=$(find "$tier_dir" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')

  echo "| $tier | $count |"
done

echo ""
echo "---"
echo ""

for tier_dir in documents/*/; do
  if [[ ! -d "$tier_dir" ]]; then
    continue
  fi

  tier=$(basename "$tier_dir")
  count=$(find "$tier_dir" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')

  echo "## $tier ($count件)"
  echo ""

  if [[ "$count" -eq 0 ]]; then
    echo "（なし）"
    echo ""
    continue
  fi

  find "$tier_dir" -name "*.md" -type f | sort | while read file; do
    filename=$(basename "$file")
    echo "- $filename"
  done

  echo ""
done

echo "---"
echo ""
echo "最終更新: $(date '+%Y-%m-%d')"
echo "更新者: Claude Code"
