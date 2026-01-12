#!/usr/bin/env python3
"""
history.json 自動更新スクリプト

4週ローリングウィンドウでKPIデータを管理します。

Usage:
    python3 update_history.py --week-id 2026-W02 --data kpi_data.json
"""

import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, List


def load_history(history_path: Path) -> Dict:
    """history.jsonをロード"""
    if not history_path.exists():
        return {
            "version": "1.0",
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "weeks": []
        }

    with open(history_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_history(history_path: Path, data: Dict):
    """history.jsonを保存"""
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")

    with open(history_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ history.json更新完了: {history_path}")


def add_week_data(history: Dict, week_data: Dict) -> Dict:
    """
    週次データを追加し、4週ローリングウィンドウを維持

    Args:
        history: 既存のhistory.jsonデータ
        week_data: 追加する週次データ

    Returns:
        更新されたhistoryデータ
    """
    weeks = history.get("weeks", [])

    # 同じweek_idが既に存在する場合は更新
    existing_index = None
    for i, week in enumerate(weeks):
        if week.get("week_id") == week_data.get("week_id"):
            existing_index = i
            break

    if existing_index is not None:
        weeks[existing_index] = week_data
        print(f"📝 week {week_data['week_id']} を更新")
    else:
        weeks.insert(0, week_data)  # 最新週を先頭に追加
        print(f"➕ week {week_data['week_id']} を追加")

    # 4週を超える古いデータを削除
    if len(weeks) > 4:
        removed = weeks[4:]
        weeks = weeks[:4]
        print(f"🗑  古いデータを削除: {[w['week_id'] for w in removed]}")

    history["weeks"] = weeks
    return history


def validate_week_data(week_data: Dict) -> bool:
    """週次データの妥当性をチェック"""
    required_fields = ["week_id", "period_start", "period_end", "kpi"]

    for field in required_fields:
        if field not in week_data:
            print(f"❌ 必須フィールドが不足: {field}")
            return False

    # KPIデータの妥当性チェック
    kpi = week_data["kpi"]
    if "platforms" not in kpi:
        print("❌ kpi.platforms が不足")
        return False

    # プラットフォーム別データの確認
    required_platforms = ["linkedin", "x", "threads"]
    for platform in required_platforms:
        if platform not in kpi["platforms"]:
            print(f"❌ プラットフォームデータが不足: {platform}")
            return False

    return True


def main():
    parser = argparse.ArgumentParser(description="history.json 自動更新")
    parser.add_argument("--week-id", required=True, help="週ID (例: 2026-W02)")
    parser.add_argument("--data", required=True, help="週次データJSONファイル")
    parser.add_argument("--history", default="Stock/programs/副業/projects/SNS/history.json",
                       help="history.jsonパス")

    args = parser.parse_args()

    # パス設定
    project_root = Path(__file__).parent.parent.parent.parent.parent
    history_path = project_root / args.history
    data_path = Path(args.data)

    if not data_path.exists():
        print(f"❌ データファイルが見つかりません: {data_path}")
        return 1

    # 週次データをロード
    with open(data_path, 'r', encoding='utf-8') as f:
        week_data = json.load(f)

    # week_idを設定
    week_data["week_id"] = args.week_id

    # 妥当性チェック
    if not validate_week_data(week_data):
        print("❌ データ検証失敗")
        return 1

    # historyをロード
    history = load_history(history_path)

    # 週次データを追加
    history = add_week_data(history, week_data)

    # 保存
    save_history(history_path, history)

    # サマリー表示
    print(f"\n📊 現在のhistory.json状態:")
    print(f"   総週数: {len(history['weeks'])}週")
    for i, week in enumerate(history['weeks']):
        print(f"   {i+1}. {week['week_id']} ({week['period_start']} 〜 {week['period_end']})")

    return 0


if __name__ == "__main__":
    exit(main())
