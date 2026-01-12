#!/bin/bash

# データ品質監査スクリプト
# 用途: 全ケーススタディの品質メトリクスを計算し、レポートを生成

# 実行ディレクトリの確認
if [[ ! -d "documents" ]]; then
  echo "エラー: documentsディレクトリが見つかりません"
  echo "Founder_Researchプロジェクトのルートディレクトリで実行してください"
  exit 1
fi

# 出力ファイル名
OUTPUT_FILE="analysis/data_quality_audit_$(date +%Y%m%d).md"

# レポート生成開始
cat > "$OUTPUT_FILE" << 'EOF'
# データ品質監査レポート

実行日時: $(date '+%Y-%m-%d %H:%M:%S')
調査対象: 全ケーススタディ

## サマリー

EOF

# 総ファイル数カウント
total=$(find documents -name "*.md" -type f | wc -l | tr -d ' ')
echo "総ケース数: $total 件" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# interview_count記載数
interview_filled=$(grep -r "interview_count: [0-9]" documents --include="*.md" | wc -l | tr -d ' ')
interview_null=$(grep -r "interview_count: null" documents --include="*.md" | wc -l | tr -d ' ')
interview_pct=$(echo "scale=1; $interview_filled*100/$total" | bc 2>/dev/null || echo "0")

# problem_commonality記載数
commonality_filled=$(grep -r "problem_commonality: [0-9]" documents --include="*.md" | wc -l | tr -d ' ')
commonality_null=$(grep -r "problem_commonality: null" documents --include="*.md" | wc -l | tr -d ' ')
commonality_pct=$(echo "scale=1; $commonality_filled*100/$total" | bc 2>/dev/null || echo "0")

# Fact Check
fact_pass=$(grep -r 'fact_check: "pass"' documents --include="*.md" | wc -l | tr -d ' ')
fact_pct=$(echo "scale=1; $fact_pass*100/$total" | bc 2>/dev/null || echo "0")

# サマリーテーブル生成
cat >> "$OUTPUT_FILE" << EOF
| 指標 | 記載あり | 記載なし | 記載率 | 目標 | 達成度 |
|------|---------|---------|--------|------|--------|
| interview_count | $interview_filled | $interview_null | $interview_pct% | 80% | $(echo "scale=1; $interview_pct*100/80" | bc 2>/dev/null || echo "0")% |
| problem_commonality | $commonality_filled | $commonality_null | $commonality_pct% | 80% | $(echo "scale=1; $commonality_pct*100/80" | bc 2>/dev/null || echo "0")% |
| Fact Check (pass) | $fact_pass | $((total - fact_pass)) | $fact_pct% | 100% | $fact_pct% |

---

## 品質警告

EOF

# 品質警告の生成
if (( $(echo "$interview_pct < 80" | bc -l 2>/dev/null || echo "1") )); then
  echo "⚠️  WARNING: interview_count記載率が目標未達（現在${interview_pct}%、目標80%）" >> "$OUTPUT_FILE"
fi

if (( $(echo "$commonality_pct < 80" | bc -l 2>/dev/null || echo "1") )); then
  echo "⚠️  WARNING: problem_commonality記載率が目標未達（現在${commonality_pct}%、目標80%）" >> "$OUTPUT_FILE"
fi

if (( $(echo "$fact_pct < 100" | bc -l 2>/dev/null || echo "1") )); then
  echo "⚠️  WARNING: Fact Check未完了のケースあり（現在${fact_pct}%）" >> "$OUTPUT_FILE"
fi

echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# ティア別詳細分析
cat >> "$OUTPUT_FILE" << 'EOF'
## ティア別詳細

EOF

for tier_dir in documents/*/; do
  if [[ ! -d "$tier_dir" ]]; then
    continue
  fi

  tier=$(basename "$tier_dir")
  echo "### $tier" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"

  tier_files=$(find "$tier_dir" -name "*.md" -type f | wc -l | tr -d ' ')
  if [[ "$tier_files" -eq 0 ]]; then
    echo "（ケースなし）" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    continue
  fi

  echo "完了件数: $tier_files 件" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"

  # interview_count欠落ファイル
  echo "#### interview_count欠落ファイル" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"

  has_missing=false
  while IFS= read -r file; do
    if grep -q "interview_count: null" "$file" 2>/dev/null; then
      filename=$(basename "$file")
      echo "- ⚠️  $filename: interview_count=null" >> "$OUTPUT_FILE"
      has_missing=true
    fi
  done < <(find "$tier_dir" -name "*.md" -type f | sort)

  if [[ "$has_missing" == "false" ]]; then
    echo "（なし）✅" >> "$OUTPUT_FILE"
  fi
  echo "" >> "$OUTPUT_FILE"

  # problem_commonality欠落ファイル
  echo "#### problem_commonality欠落ファイル" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"

  has_missing=false
  while IFS= read -r file; do
    if grep -q "problem_commonality: null" "$file" 2>/dev/null; then
      filename=$(basename "$file")
      echo "- ⚠️  $filename: problem_commonality=null" >> "$OUTPUT_FILE"
      has_missing=true
    fi
  done < <(find "$tier_dir" -name "*.md" -type f | sort)

  if [[ "$has_missing" == "false" ]]; then
    echo "（なし）✅" >> "$OUTPUT_FILE"
  fi
  echo "" >> "$OUTPUT_FILE"

  echo "---" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"
done

# 改善優先順位
cat >> "$OUTPUT_FILE" << 'EOF'
## 改善優先順位

1. **01_Legendary**: 最優先でデータ補完（影響力大、事例として重要）
2. **02_Unicorn**: 次優先（件数多、新規調査と並行して補完）
3. **04_IPO_Japan**: 資料豊富、効率的に補完可能
4. **06_Pivot_Success**: 件数少、orchestrate-phase1連携で重要

---

## 次のアクション

- [ ] 01_Legendary全43件のinterview_count補完
- [ ] 01_Legendary全43件のproblem_commonality補完
- [ ] 品質スコアリング実施（90点以上を目標）
- [ ] 新規調査時は100%記載を徹底

---

## 使用方法

### 再実行
```bash
cd Founder_Research
./scripts/audit_data_quality.sh
```

### 出力確認
```bash
cat analysis/data_quality_audit_YYYYMMDD.md
```

EOF

echo "✅ レポート生成完了: $OUTPUT_FILE"
echo ""
echo "=== サマリー ==="
echo "総ケース数: $total 件"
echo "interview_count記載率: $interview_pct%"
echo "problem_commonality記載率: $commonality_pct%"
echo "Fact Check Pass率: $fact_pct%"
