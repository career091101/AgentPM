#!/usr/bin/env python3
"""
1月6日手動予約スクリプト
"""
import subprocess
import json
from pathlib import Path

# 承認済みファイルの読み込み
data_dir = Path("data")
approved_file = data_dir / "posts_approved" / "approved_20260104_210519_manual_20260106.json"

with open(approved_file, 'r', encoding='utf-8') as f:
    approved_data = json.load(f)

content = approved_data["approved_post"]["refined_content"]

# LinkedIn: 2026-01-06T08:00:00+09:00
print("📤 Scheduling LinkedIn for 2026-01-06 08:00 JST...")
subprocess.run([
    ".venv/bin/python3", "scripts/post_to_sns_late.py",
    "--file", "approved_post_20260104_135824.json",  # ダミー（中身は使わない）
    "--platforms", "LinkedIn",
    "--scheduled-time", "2026-01-06T08:00:00+09:00",
    "--scheduled-post-id", "manual_20260106_linkedin",
    "--optimized-content", content,
    "--recommended-format", "single"
], check=True)

# X + Threads: 2026-01-06T20:00:00+09:00
print("\n📤 Scheduling X + Threads for 2026-01-06 20:00 JST...")
subprocess.run([
    ".venv/bin/python3", "scripts/post_to_sns_late.py",
    "--file", "approved_post_20260104_135824.json",  # ダミー（中身は使わない）
    "--platforms", "X", "Threads",
    "--scheduled-time", "2026-01-06T20:00:00+09:00",
    "--scheduled-post-id", "manual_20260106_x_threads",
    "--optimized-content", content,
    "--recommended-format", "single"
], check=True)

print("\n✅ All schedules created successfully!")
