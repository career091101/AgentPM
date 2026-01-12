#!/bin/bash

# 進捗自動更新スクリプト
# 用途: 各ティアの完了件数をカウントし、進捗情報を出力

echo "## 進捗更新 ($(date '+%Y-%m-%d %H:%M'))"
echo ""

# 各ティアの完了件数カウント
legendary=$(find documents/01_Legendary -name "FOUNDER_*.md" 2>/dev/null | wc -l | tr -d ' ')
unicorn=$(find documents/02_Unicorn -name "FOUNDER_*.md" 2>/dev/null | wc -l | tr -d ' ')
vc_backed=$(find documents/03_VC_Backed -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
ipo_japan=$(find documents/04_IPO_Japan -name "FOUNDER_*.md" 2>/dev/null | wc -l | tr -d ' ')
ipo_global=$(find documents/05_IPO_Global -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
pivot=$(find documents/06_Pivot_Success -name "PIVOT_*.md" 2>/dev/null | wc -l | tr -d ' ')
failure=$(find documents/07_Failure_Study -name "FAILURE_*.md" 2>/dev/null | wc -l | tr -d ' ')
emerging=$(find documents/08_Emerging -name "EMERGING_*.md" 2>/dev/null | wc -l | tr -d ' ')

total=$((legendary + unicorn + vc_backed + ipo_japan + ipo_global + pivot + failure + emerging))

if [[ "$total" -gt 0 ]]; then
  progress=$(echo "scale=1; $total*100/500" | bc 2>/dev/null || echo "0")
else
  progress="0"
fi

echo "総計: $total/500 ($progress%)"
echo ""
echo "| ティア | 完了件数 | 進捗率 |"
echo "|--------|---------|--------|"

# 01_Legendary
if [[ "$legendary" -gt 0 ]]; then
  legendary_pct=$(echo "scale=1; $legendary*100/50" | bc 2>/dev/null || echo "0")
else
  legendary_pct="0"
fi
echo "| 01_Legendary | $legendary/50 | $legendary_pct% |"

# 02_Unicorn
if [[ "$unicorn" -gt 0 ]]; then
  unicorn_pct=$(echo "scale=1; $unicorn*100/100" | bc 2>/dev/null || echo "0")
else
  unicorn_pct="0"
fi
echo "| 02_Unicorn | $unicorn/100 | $unicorn_pct% |"

# 03_VC_Backed
if [[ "$vc_backed" -gt 0 ]]; then
  vc_pct=$(echo "scale=1; $vc_backed*100/150" | bc 2>/dev/null || echo "0")
else
  vc_pct="0"
fi
echo "| 03_VC_Backed | $vc_backed/150 | $vc_pct% |"

# 04_IPO_Japan
if [[ "$ipo_japan" -gt 0 ]]; then
  japan_pct=$(echo "scale=1; $ipo_japan*100/50" | bc 2>/dev/null || echo "0")
else
  japan_pct="0"
fi
echo "| 04_IPO_Japan | $ipo_japan/50 | $japan_pct% |"

# 05_IPO_Global
if [[ "$ipo_global" -gt 0 ]]; then
  global_pct=$(echo "scale=1; $ipo_global*100/50" | bc 2>/dev/null || echo "0")
else
  global_pct="0"
fi
echo "| 05_IPO_Global | $ipo_global/50 | $global_pct% |"

# 06_Pivot_Success
if [[ "$pivot" -gt 0 ]]; then
  pivot_pct=$(echo "scale=1; $pivot*100/30" | bc 2>/dev/null || echo "0")
else
  pivot_pct="0"
fi
echo "| 06_Pivot_Success | $pivot/30 | $pivot_pct% |"

# 07_Failure_Study
if [[ "$failure" -gt 0 ]]; then
  failure_pct=$(echo "scale=1; $failure*100/30" | bc 2>/dev/null || echo "0")
else
  failure_pct="0"
fi
echo "| 07_Failure_Study | $failure/30 | $failure_pct% |"

# 08_Emerging
if [[ "$emerging" -gt 0 ]]; then
  emerging_pct=$(echo "scale=1; $emerging*100/40" | bc 2>/dev/null || echo "0")
else
  emerging_pct="0"
fi
echo "| 08_Emerging | $emerging/40 | $emerging_pct% |"
