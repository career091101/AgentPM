#!/usr/bin/env python3
"""
5つのCLI並列実行監視ダッシュボード
作成日: 2025-12-29
"""

import os
from pathlib import Path
from datetime import datetime

# ベースディレクトリ
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents")

# 各CLIの担当ティアとファイル数
CLI_ASSIGNMENTS = {
    "CLI-1": {
        "name": "VC投資成功",
        "tiers": ["03_VC_Backed", "05_IPO_Global"],
        "target": 64,
        "vc_range": (7, 50),  # 現在7件、目標50件
        "ipo_range": (10, 31),  # 現在10件、目標31件
    },
    "CLI-2": {
        "name": "Pivot成功",
        "tiers": ["06_Pivot_Success", "05_IPO_Global", "04_IPO_Japan"],
        "target": 64,
        "pivot_range": (13, 50),
        "ipo_range": (31, 50),  # Part2
        "japan_range": (20, 28),  # Part1
    },
    "CLI-3": {
        "name": "失敗企業分析",
        "tiers": ["07_Failure_Study", "04_IPO_Japan"],
        "target": 64,
        "failure_range": (12, 50),
        "japan_range": (28, 50),  # Part2
    },
    "CLI-4": {
        "name": "Emerging Part1",
        "tiers": ["08_Emerging"],
        "target": 66,
        "emerging_range": (9, 75),
    },
    "CLI-5": {
        "name": "Emerging Part2",
        "tiers": ["08_Emerging"],
        "target": 75,
        "emerging_range": (75, 150),
    }
}

def count_files_in_tier(tier):
    """ティア内のファイル数をカウント"""
    tier_path = BASE_DIR / tier
    if tier_path.exists():
        return len(list(tier_path.glob("*.md")))
    return 0

def get_recent_files(tier, minutes=30):
    """最近更新されたファイル数を取得"""
    tier_path = BASE_DIR / tier
    if not tier_path.exists():
        return 0

    import time
    cutoff_time = time.time() - (minutes * 60)
    recent_count = 0

    for file_path in tier_path.glob("*.md"):
        if file_path.stat().st_mtime > cutoff_time:
            recent_count += 1

    return recent_count

def main():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║     5-CLI並列実行監視ダッシュボード                           ║")
    print("╠══════════════════════════════════════════════════════════════╣")
    print(f"║ 更新時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                              ║")
    print("╚══════════════════════════════════════════════════════════════╝\n")

    # ティア別現在数を取得
    tier_counts = {}
    for tier in ["03_VC_Backed", "04_IPO_Japan", "05_IPO_Global",
                  "06_Pivot_Success", "07_Failure_Study", "08_Emerging"]:
        tier_counts[tier] = count_files_in_tier(tier)

    total_current = sum(tier_counts.values()) + 50 + 56  # Legendary + Unicorn
    total_target = 500
    total_progress = (total_current / total_target) * 100

    print(f"📊 全体進捗: {total_current}/500 ({total_progress:.1f}%)")
    print(f"残り: {total_target - total_current}件\n")

    print("=" * 70)
    print()

    # 各CLI進捗
    for cli_id, cli_info in CLI_ASSIGNMENTS.items():
        print(f"### {cli_id}: {cli_info['name']} (目標: {cli_info['target']}件)")

        # 現在のファイル数計算
        current_count = 0
        recent_count = 0

        for tier in cli_info['tiers']:
            tier_count = tier_counts.get(tier, 0)
            tier_recent = get_recent_files(tier, minutes=30)

            # CLI担当範囲の推定 (簡易版)
            if tier == "03_VC_Backed" and cli_id == "CLI-1":
                current_count += tier_count - 7  # 既存7件を除く
                recent_count += tier_recent
            elif tier == "05_IPO_Global" and cli_id == "CLI-1":
                # Part1は約半分
                current_count += max(0, tier_count - 10) // 2
                recent_count += tier_recent // 2
            elif tier == "06_Pivot_Success" and cli_id == "CLI-2":
                current_count += tier_count - 13  # 既存13件を除く
                recent_count += tier_recent
            elif tier == "07_Failure_Study" and cli_id == "CLI-3":
                current_count += tier_count - 12  # 既存12件を除く
                recent_count += tier_recent
            elif tier == "08_Emerging":
                if cli_id == "CLI-4":
                    # Part1: 現在の半分
                    current_count += (tier_count - 9) // 2
                    recent_count += tier_recent // 2
                elif cli_id == "CLI-5":
                    # Part2: 現在の残り半分
                    current_count += (tier_count - 9) - ((tier_count - 9) // 2)
                    recent_count += tier_recent - (tier_recent // 2)

        progress_pct = (current_count / cli_info['target']) * 100 if cli_info['target'] > 0 else 0

        # ステータス判定
        if progress_pct >= 100:
            status = "✅ 完了"
        elif progress_pct >= 75:
            status = "🟢 順調"
        elif progress_pct >= 50:
            status = "🟡 進行中"
        elif progress_pct >= 25:
            status = "🟠 開始"
        else:
            status = "⚪ 準備中"

        print(f"  進捗: {current_count}/{cli_info['target']} ({progress_pct:.1f}%) {status}")
        print(f"  最近30分: +{recent_count}件")

        # 残り時間推定 (1件1分と仮定)
        remaining = cli_info['target'] - current_count
        if remaining > 0 and recent_count > 0:
            rate_per_min = recent_count / 30
            est_minutes = remaining / rate_per_min if rate_per_min > 0 else 0
            print(f"  推定残り時間: {est_minutes:.0f}分 ({est_minutes/60:.1f}時間)")

        print()

    print("=" * 70)
    print()

    # ティア別詳細
    print("📁 ティア別現在数:")
    print(f"  01_Legendary: 50/50 (100%) ✅")
    print(f"  02_Unicorn: 56/50 (112%) ✅")
    print(f"  03_VC_Backed: {tier_counts.get('03_VC_Backed', 0)}/50 ({tier_counts.get('03_VC_Backed', 0)*2}%)")
    print(f"  04_IPO_Japan: {tier_counts.get('04_IPO_Japan', 0)}/50 ({tier_counts.get('04_IPO_Japan', 0)*2}%)")
    print(f"  05_IPO_Global: {tier_counts.get('05_IPO_Global', 0)}/50 ({tier_counts.get('05_IPO_Global', 0)*2}%)")
    print(f"  06_Pivot_Success: {tier_counts.get('06_Pivot_Success', 0)}/50 ({tier_counts.get('06_Pivot_Success', 0)*2}%)")
    print(f"  07_Failure_Study: {tier_counts.get('07_Failure_Study', 0)}/50 ({tier_counts.get('07_Failure_Study', 0)*2}%)")
    print(f"  08_Emerging: {tier_counts.get('08_Emerging', 0)}/150 ({tier_counts.get('08_Emerging', 0)/1.5:.1f}%)")

    print()
    print("💡 次回更新: 30秒後 (watch -n 30コマンド使用時)")
    print(f"📄 詳細ログ: /Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-29/cli_monitor.log")

if __name__ == "__main__":
    main()
