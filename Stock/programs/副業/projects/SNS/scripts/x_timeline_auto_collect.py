#!/usr/bin/env python3
"""
X Timeline Auto Collector
修正版JavaScript関数を使用してタイムラインデータを自動収集
"""

import time
import json
from pathlib import Path
from datetime import datetime

# Seleniumは既存タブを直接操作できないため、
# ブラウザコンソールに手動で関数を注入する前提で、
# データ取得と保存のみを行うスクリプトとして実装

# データディレクトリ
DATA_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# 出力ファイル
OUTPUT_FILE = DATA_DIR / "x_timeline_20260101_fixed.json"
OUTPUT_FILE_TOP30 = DATA_DIR / "x_timeline_20260101_fixed_top30.json"

print("=" * 80)
print("X Timeline Auto Collector - 修正版")
print("=" * 80)
print()
print("このスクリプトは、ブラウザコンソールでJavaScript関数を実行し、")
print("データをlocalStorageから取得する想定です。")
print()
print("【手動実行手順】")
print()
print("1. X.com/homeをブラウザで開く")
print()
print("2. ブラウザのコンソール（F12 → Console）を開く")
print()
print("3. 以下のJavaScript関数を実行:")
print()
print("```javascript")
print("// 修正版スクリプトを読み込み")
with open("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/x_timeline_collector_fixed.js", "r") as f:
    print(f.read())
print("```")
print()
print("4. Cycle 1-20を実行:")
print()
print("```javascript")
print("for (let i = 1; i <= 20; i++) {")
print("  console.log(`Cycle ${i}...`);")
print("  window.scrollBy(0, window.innerHeight * 15);")
print("  await new Promise(r => setTimeout(r, 5000));")
print("  const result = extractTweetsAndAccumulateFixed();")
print("  console.log(result);")
print("}")
print("```")
print()
print("5. データを取得:")
print()
print("```javascript")
print("const finalData = {")
print("  tweets: window.XTimelineCollectorState.allTweets,")
print("  metadata: {")
print("    total_collected: window.XTimelineCollectorState.seenIds.size,")
print("    cycles_completed: window.XTimelineCollectorState.cycleCount,")
print("    collection_start: window.XTimelineCollectorState.startTime,")
print("    collection_end: new Date().toISOString()")
print("  }")
print("};")
print("console.log(JSON.stringify(finalData, null, 2));")
print("```")
print()
print("6. コンソール出力をコピーして、以下のファイルに保存:")
print(f"   {OUTPUT_FILE}")
print()
print("=" * 80)
print()
print("注: Claude In Chromeの制約により、JavaScript関数の直接注入が")
print("    困難なため、手動実行手順を提示しています。")
print()
