#!/bin/bash

# 品質スコアリングスクリプト
# 用途: 各ケーススタディを100点満点で評価

OUTPUT="analysis/quality_scores_$(date +%Y%m%d).md"

echo "# 品質スコアリングレポート" > "$OUTPUT"
echo "" >> "$OUTPUT"
echo "実行日時: $(date '+%Y-%m-%d %H:%M:%S')" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "## スコアリング基準" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "| 項目 | 配点 | 条件 |" >> "$OUTPUT"
echo "|------|------|------|" >> "$OUTPUT"
echo "| interview_count | 10点 | 数値記載あり |" >> "$OUTPUT"
echo "| problem_commonality | 10点 | 数値記載あり |" >> "$OUTPUT"
echo "| wtp_confirmed | 10点 | true/false明記 |" >> "$OUTPUT"
echo "| ten_x_axes | 15点 | 2軸以上 |" >> "$OUTPUT"
echo "| mvp_type | 10点 | 記載あり |" >> "$OUTPUT"
echo "| primary_sources | 15点 | 3件以上 |" >> "$OUTPUT"
echo "| fact_check | 30点 | pass判定 |" >> "$OUTPUT"
echo "| **合計** | **100点** | |" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "---" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "## ケース別スコア" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "| ファイル | IC | PC | WTP | 10x | MVP | Src | FC | 合計 | ランク |" >> "$OUTPUT"
echo "|---------|----|----|-----|-----|-----|-----|-------|------|-------|" >> "$OUTPUT"

total_score=0
total_files=0

for file in $(find documents -name "*.md" -type f | sort); do
  filename=$(basename "$file")
  score=0

  # interview_count (10点)
  if grep -q "interview_count: [0-9]" "$file" 2>/dev/null; then
    score=$((score + 10))
    ic="10"
  else
    ic="0"
  fi

  # problem_commonality (10点)
  if grep -q "problem_commonality: [0-9]" "$file" 2>/dev/null; then
    score=$((score + 10))
    pc="10"
  else
    pc="0"
  fi

  # wtp_confirmed (10点)
  if grep -q "wtp_confirmed: true\|wtp_confirmed: false" "$file" 2>/dev/null; then
    score=$((score + 10))
    wtp="10"
  else
    wtp="0"
  fi

  # ten_x_axes (15点) - 2軸以上
  ten_x_count=$(grep -c "axis:" "$file" 2>/dev/null || echo "0")
  if [[ "$ten_x_count" -ge 2 ]]; then
    score=$((score + 15))
    ten_x="15"
  else
    ten_x="0"
  fi

  # mvp_type (10点)
  if grep -q 'mvp_type: "[^"]' "$file" 2>/dev/null; then
    score=$((score + 10))
    mvp="10"
  else
    mvp="0"
  fi

  # primary_sources (15点) - 3件以上
  sources_count=$(grep -A 10 "primary_sources:" "$file" 2>/dev/null | grep "  -" | wc -l | tr -d ' ')
  if [[ "$sources_count" -ge 3 ]]; then
    score=$((score + 15))
    src="15"
  else
    src="0"
  fi

  # fact_check (30点)
  if grep -q 'fact_check: "pass"' "$file" 2>/dev/null; then
    score=$((score + 30))
    fc="30"
  else
    fc="0"
  fi

  # ランク判定
  if [[ "$score" -ge 90 ]]; then
    rank="A"
  elif [[ "$score" -ge 80 ]]; then
    rank="B"
  elif [[ "$score" -ge 70 ]]; then
    rank="C"
  elif [[ "$score" -ge 60 ]]; then
    rank="D"
  else
    rank="F"
  fi

  echo "| $filename | $ic | $pc | $wtp | $ten_x | $mvp | $src | $fc | $score | $rank |" >> "$OUTPUT"

  total_score=$((total_score + score))
  total_files=$((total_files + 1))
done

echo "" >> "$OUTPUT"
echo "---" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "## ランク分布" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "| ランク | 件数 | 割合 |" >> "$OUTPUT"
echo "|--------|------|------|" >> "$OUTPUT"

for rank in A B C D F; do
  count=$(grep "| $rank |" "$OUTPUT" | wc -l | tr -d ' ')
  if [[ "$total_files" -gt 0 ]]; then
    pct=$(echo "scale=1; $count*100/$total_files" | bc 2>/dev/null || echo "0")
  else
    pct="0"
  fi
  echo "| $rank | $count | $pct% |" >> "$OUTPUT"
done

echo "" >> "$OUTPUT"
echo "---" >> "$OUTPUT"
echo "" >> "$OUTPUT"
echo "## 統計サマリー" >> "$OUTPUT"
echo "" >> "$OUTPUT"

if [[ "$total_files" -gt 0 ]]; then
  avg_score=$(echo "scale=1; $total_score/$total_files" | bc 2>/dev/null || echo "0")
else
  avg_score="0"
fi

echo "- **総ケース数**: $total_files 件" >> "$OUTPUT"
echo "- **平均スコア**: $avg_score 点" >> "$OUTPUT"
echo "- **目標**: 85点以上" >> "$OUTPUT"
echo "" >> "$OUTPUT"

echo ""
echo "✅ スコアリング完了: $OUTPUT"
echo ""
echo "=== サマリー ==="
echo "総ケース数: $total_files 件"
echo "平均スコア: $avg_score 点"
