#!/bin/bash
# Batch 2-3 自動品質スコアリングスクリプト
# 作成日: 2025-12-29

DOCS_DIR="/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents"
OUTPUT="/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-29/quality_scores_batch2_3.txt"

echo "╔══════════════════════════════════════════════════════════════╗" | tee "$OUTPUT"
echo "║     Batch 2-3 自動品質スコアリング (18件)                     ║" | tee -a "$OUTPUT"
echo "╠══════════════════════════════════════════════════════════════╣" | tee -a "$OUTPUT"
echo "║ 実行時刻: $(date '+%Y-%m-%d %H:%M:%S')                              ║" | tee -a "$OUTPUT"
echo "╚══════════════════════════════════════════════════════════════╝" | tee -a "$OUTPUT"
echo "" | tee -a "$OUTPUT"

# Batch 2ファイルリスト (7件)
BATCH2_FILES=(
  "$DOCS_DIR/03_VC_Backed/FOUNDER_151_airbnb.md"
  "$DOCS_DIR/03_VC_Backed/FOUNDER_152_coinbase.md"
  "$DOCS_DIR/05_IPO_Global/FOUNDER_351_jan_koum_whatsapp.md"
  "$DOCS_DIR/05_IPO_Global/FOUNDER_352_eric_yuan_zoom.md"
  "$DOCS_DIR/03_VC_Backed/FOUNDER_157_github.md"
  "$DOCS_DIR/05_IPO_Global/FOUNDER_355_coinbase.md"
  "$DOCS_DIR/07_Failure_Study/FAILURE_008_jawbone.md"
)

# Batch 3ファイルリスト (11件)
BATCH3_FILES=(
  "$DOCS_DIR/07_Failure_Study/FAILURE_009_quibi.md"
  "$DOCS_DIR/07_Failure_Study/FAILURE_010_getaround.md"
  "$DOCS_DIR/07_Failure_Study/FAILURE_011_humane_ai.md"
  "$DOCS_DIR/03_VC_Backed/FOUNDER_159_palantir.md"
  "$DOCS_DIR/03_VC_Backed/FOUNDER_160_okta.md"
  "$DOCS_DIR/06_Pivot_Success/PIVOT_004_box.md"
  "$DOCS_DIR/06_Pivot_Success/PIVOT_005_jasper_ai.md"
  "$DOCS_DIR/08_Emerging/EMERGING_001_stability_ai.md"
  "$DOCS_DIR/08_Emerging/EMERGING_002_character_ai.md"
  "$DOCS_DIR/08_Emerging/EMERGING_003_midjourney.md"
  "$DOCS_DIR/08_Emerging/EMERGING_004_runway.md"
)

# 全ファイルリスト結合
ALL_FILES=("${BATCH2_FILES[@]}" "${BATCH3_FILES[@]}")

# 集計変数初期化
total_files=0
total_nulls=0
total_sources=0
total_fact_check_pass=0
total_ten_x_axes=0
files_with_nulls=0

echo "=== Batch 2 (7件) ===" | tee -a "$OUTPUT"
echo "" | tee -a "$OUTPUT"

# Batch 2処理
for file in "${BATCH2_FILES[@]}"; do
  if [ ! -f "$file" ]; then
    echo "⚠️  ファイル未発見: $(basename "$file")" | tee -a "$OUTPUT"
    continue
  fi

  total_files=$((total_files + 1))
  filename=$(basename "$file")

  # Null数カウント (validation_dataセクション内のみ)
  null_count=$(sed -n '/^validation_data:/,/^cross_reference:/p' "$file" | grep -c ": null" 2>/dev/null || echo "0")
  total_nulls=$((total_nulls + null_count))
  if [ "$null_count" -gt 0 ]; then
    files_with_nulls=$((files_with_nulls + 1))
  fi

  # ソース数
  sources=$(grep "sources_count:" "$file" | awk '{print $2}' 2>/dev/null || echo "0")
  total_sources=$((total_sources + sources))

  # Fact Check
  fact_check=$(grep "fact_check:" "$file" | awk '{print $2}' | tr -d '"' 2>/dev/null || echo "unknown")
  if [ "$fact_check" = "pass" ]; then
    total_fact_check_pass=$((total_fact_check_pass + 1))
    fact_icon="✅"
  else
    fact_icon="❌"
  fi

  # 10x axes数
  axes_count=$(sed -n '/ten_x_axes:/,/mvp_type:/p' "$file" | grep -c "axis:" 2>/dev/null || echo "0")
  total_ten_x_axes=$((total_ten_x_axes + axes_count))

  # スコア計算 (簡易版 100点満点)
  score=0

  # データ完全性 (15点) - null数に応じて減点
  if [ "$null_count" -eq 0 ]; then
    score=$((score + 15))
  elif [ "$null_count" -le 2 ]; then
    score=$((score + 10))
  elif [ "$null_count" -le 4 ]; then
    score=$((score + 5))
  fi

  # ソース数 (15点)
  if [ "$sources" -ge 15 ]; then
    score=$((score + 15))
  elif [ "$sources" -ge 12 ]; then
    score=$((score + 12))
  elif [ "$sources" -ge 10 ]; then
    score=$((score + 10))
  elif [ "$sources" -ge 3 ]; then
    score=$((score + 5))
  fi

  # Fact Check (30点)
  if [ "$fact_check" = "pass" ]; then
    score=$((score + 30))
  fi

  # 10x axes (15点)
  if [ "$axes_count" -ge 4 ]; then
    score=$((score + 15))
  elif [ "$axes_count" -ge 2 ]; then
    score=$((score + 12))
  elif [ "$axes_count" -ge 1 ]; then
    score=$((score + 5))
  fi

  # MVP type確認 (10点)
  mvp_type=$(grep "mvp_type:" "$file" | awk '{print $2}' | tr -d '"' 2>/dev/null || echo "null")
  if [ "$mvp_type" != "null" ] && [ "$mvp_type" != "" ]; then
    score=$((score + 10))
  fi

  # Support Confirmation (仮: orchestrate-phase1セクション確認) (10点)
  orchestrate_section=$(grep -c "orchestrate-phase1への示唆" "$file" 2>/dev/null || echo "0")
  if [ "$orchestrate_section" -gt 0 ]; then
    score=$((score + 10))
  fi

  # Grade判定
  if [ "$score" -ge 90 ]; then
    grade="A"
  elif [ "$score" -ge 80 ]; then
    grade="B"
  elif [ "$score" -ge 70 ]; then
    grade="C"
  elif [ "$score" -ge 65 ]; then
    grade="D"
  else
    grade="F"
  fi

  # 結果出力
  printf "%-40s | Score: %3d | Grade: %s | Nulls: %d | Sources: %2d | FC: %s | Axes: %d\n" \
    "$filename" "$score" "$grade" "$null_count" "$sources" "$fact_icon" "$axes_count" | tee -a "$OUTPUT"
done

echo "" | tee -a "$OUTPUT"
echo "=== Batch 3 (11件) ===" | tee -a "$OUTPUT"
echo "" | tee -a "$OUTPUT"

# Batch 3処理
for file in "${BATCH3_FILES[@]}"; do
  if [ ! -f "$file" ]; then
    echo "⚠️  ファイル未発見: $(basename "$file")" | tee -a "$OUTPUT"
    continue
  fi

  total_files=$((total_files + 1))
  filename=$(basename "$file")

  # Null数カウント
  null_count=$(sed -n '/^validation_data:/,/^cross_reference:/p' "$file" | grep -c ": null" 2>/dev/null || echo "0")
  total_nulls=$((total_nulls + null_count))
  if [ "$null_count" -gt 0 ]; then
    files_with_nulls=$((files_with_nulls + 1))
  fi

  # ソース数
  sources=$(grep "sources_count:" "$file" | awk '{print $2}' 2>/dev/null || echo "0")
  total_sources=$((total_sources + sources))

  # Fact Check
  fact_check=$(grep "fact_check:" "$file" | awk '{print $2}' | tr -d '"' 2>/dev/null || echo "unknown")
  if [ "$fact_check" = "pass" ]; then
    total_fact_check_pass=$((total_fact_check_pass + 1))
    fact_icon="✅"
  else
    fact_icon="❌"
  fi

  # 10x axes数
  axes_count=$(sed -n '/ten_x_axes:/,/mvp_type:/p' "$file" | grep -c "axis:" 2>/dev/null || echo "0")
  total_ten_x_axes=$((total_ten_x_axes + axes_count))

  # スコア計算 (Batch 2と同じロジック)
  score=0

  if [ "$null_count" -eq 0 ]; then
    score=$((score + 15))
  elif [ "$null_count" -le 2 ]; then
    score=$((score + 10))
  elif [ "$null_count" -le 4 ]; then
    score=$((score + 5))
  fi

  if [ "$sources" -ge 15 ]; then
    score=$((score + 15))
  elif [ "$sources" -ge 12 ]; then
    score=$((score + 12))
  elif [ "$sources" -ge 10 ]; then
    score=$((score + 10))
  elif [ "$sources" -ge 3 ]; then
    score=$((score + 5))
  fi

  if [ "$fact_check" = "pass" ]; then
    score=$((score + 30))
  fi

  if [ "$axes_count" -ge 4 ]; then
    score=$((score + 15))
  elif [ "$axes_count" -ge 2 ]; then
    score=$((score + 12))
  elif [ "$axes_count" -ge 1 ]; then
    score=$((score + 5))
  fi

  mvp_type=$(grep "mvp_type:" "$file" | awk '{print $2}' | tr -d '"' 2>/dev/null || echo "null")
  if [ "$mvp_type" != "null" ] && [ "$mvp_type" != "" ]; then
    score=$((score + 10))
  fi

  orchestrate_section=$(grep -c "orchestrate-phase1への示唆" "$file" 2>/dev/null || echo "0")
  if [ "$orchestrate_section" -gt 0 ]; then
    score=$((score + 10))
  fi

  # Grade判定
  if [ "$score" -ge 90 ]; then
    grade="A"
  elif [ "$score" -ge 80 ]; then
    grade="B"
  elif [ "$score" -ge 70 ]; then
    grade="C"
  elif [ "$score" -ge 65 ]; then
    grade="D"
  else
    grade="F"
  fi

  # 結果出力
  printf "%-40s | Score: %3d | Grade: %s | Nulls: %d | Sources: %2d | FC: %s | Axes: %d\n" \
    "$filename" "$score" "$grade" "$null_count" "$sources" "$fact_icon" "$axes_count" | tee -a "$OUTPUT"
done

echo "" | tee -a "$OUTPUT"
echo "╔══════════════════════════════════════════════════════════════╗" | tee -a "$OUTPUT"
echo "║ サマリー統計                                                  ║" | tee -a "$OUTPUT"
echo "╠══════════════════════════════════════════════════════════════╣" | tee -a "$OUTPUT"

# 平均計算
if [ "$total_files" -gt 0 ]; then
  avg_sources=$((total_sources / total_files))
  avg_axes=$((total_ten_x_axes / total_files))
  pass_rate=$((total_fact_check_pass * 100 / total_files))
  null_rate=$((files_with_nulls * 100 / total_files))
else
  avg_sources=0
  avg_axes=0
  pass_rate=0
  null_rate=0
fi

echo "║ 総ファイル数: $total_files                                           ║" | tee -a "$OUTPUT"
echo "║ Fact Check Pass率: $pass_rate% ($total_fact_check_pass/$total_files)                       ║" | tee -a "$OUTPUT"
echo "║ 平均ソース数: $avg_sources件                                       ║" | tee -a "$OUTPUT"
echo "║ 総Null数: $total_nulls件                                         ║" | tee -a "$OUTPUT"
echo "║ Nullを含むファイル: $files_with_nulls件 ($null_rate%)                       ║" | tee -a "$OUTPUT"
echo "║ 平均10x axes: $avg_axes軸                                       ║" | tee -a "$OUTPUT"
echo "╚══════════════════════════════════════════════════════════════╝" | tee -a "$OUTPUT"

echo "" | tee -a "$OUTPUT"
echo "✅ 品質スコアリング完了" | tee -a "$OUTPUT"
echo "📄 詳細結果: $OUTPUT" | tee -a "$OUTPUT"

# 成功判定
if [ "$pass_rate" -eq 100 ] && [ "$avg_sources" -ge 12 ]; then
  echo "🎉 品質基準達成: Fact Check 100%, 平均ソース12+件" | tee -a "$OUTPUT"
  exit 0
else
  echo "⚠️  品質改善余地あり" | tee -a "$OUTPUT"
  exit 1
fi
