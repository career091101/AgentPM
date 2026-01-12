#!/usr/bin/env python3
"""
SNS投稿自動レビュースケジューラー

投稿生成直後と予約投稿の1日後に自動的にレビューを実行
"""

import os
import sys
import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional


class AutoReviewScheduler:
    """自動レビュースケジューラー"""

    def __init__(self, config_path: Optional[str] = None):
        """初期化"""
        self.base_dir = Path(__file__).parent.parent.parent.parent.parent
        self.config_path = config_path or self.base_dir / ".claude/skills/sns-automation/review-and-improve-skill/automation/schedule_config.json"
        self.schedule_db_path = self.base_dir / ".claude/skills/sns-automation/review-and-improve-skill/automation/schedule_db.json"
        self.load_config()
        self.load_schedule_db()

    def load_config(self):
        """設定ファイルを読み込み"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            # デフォルト設定
            self.config = {
                "immediate_review": {
                    "enabled": True,
                    "auto_apply": False,
                    "priority": ["P0", "P1"]
                },
                "post_publication_review": {
                    "enabled": True,
                    "delay_days": 1,
                    "auto_apply": True,
                    "priority": ["P0", "P1"]
                },
                "notification": {
                    "enabled": True,
                    "method": "file"  # "file", "slack", "email"
                }
            }
            self.save_config()

    def save_config(self):
        """設定ファイルを保存"""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def load_schedule_db(self):
        """スケジュールDBを読み込み"""
        if self.schedule_db_path.exists():
            with open(self.schedule_db_path, 'r', encoding='utf-8') as f:
                self.schedule_db = json.load(f)
        else:
            self.schedule_db = {
                "scheduled_reviews": [],
                "completed_reviews": []
            }
            self.save_schedule_db()

    def save_schedule_db(self):
        """スケジュールDBを保存"""
        self.schedule_db_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.schedule_db_path, 'w', encoding='utf-8') as f:
            json.dump(self.schedule_db, f, ensure_ascii=False, indent=2)

    def schedule_immediate_review(self, post_file_path: str) -> Dict:
        """投稿生成直後のレビューをスケジュール"""

        if not self.config["immediate_review"]["enabled"]:
            return {"status": "skipped", "reason": "immediate_review is disabled"}

        print(f"📋 投稿生成直後のレビューを実行します...")
        print(f"   対象ファイル: {post_file_path}")

        # レビュー実行
        result = self.run_review(
            post_file_path=post_file_path,
            review_type="immediate",
            auto_apply=self.config["immediate_review"]["auto_apply"],
            priority=self.config["immediate_review"]["priority"]
        )

        # 結果を記録
        self.record_review_result(
            post_file_path=post_file_path,
            review_type="immediate",
            result=result
        )

        return result

    def schedule_post_publication_review(self, post_file_path: str, publication_date: str) -> Dict:
        """予約投稿の1日後のレビューをスケジュール"""

        if not self.config["post_publication_review"]["enabled"]:
            return {"status": "skipped", "reason": "post_publication_review is disabled"}

        # 公開日の1日後を計算
        pub_date = datetime.strptime(publication_date, "%Y-%m-%d")
        review_date = pub_date + timedelta(days=self.config["post_publication_review"]["delay_days"])

        # スケジュールに追加
        schedule_entry = {
            "id": f"review_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "post_file_path": post_file_path,
            "publication_date": publication_date,
            "review_date": review_date.strftime("%Y-%m-%d"),
            "review_type": "post_publication",
            "auto_apply": self.config["post_publication_review"]["auto_apply"],
            "priority": self.config["post_publication_review"]["priority"],
            "status": "scheduled",
            "created_at": datetime.now().isoformat()
        }

        self.schedule_db["scheduled_reviews"].append(schedule_entry)
        self.save_schedule_db()

        print(f"📅 投稿公開1日後のレビューをスケジュールしました")
        print(f"   公開予定日: {publication_date}")
        print(f"   レビュー実行日: {review_date.strftime('%Y-%m-%d')}")
        print(f"   スケジュールID: {schedule_entry['id']}")

        return {
            "status": "scheduled",
            "schedule_id": schedule_entry["id"],
            "review_date": review_date.strftime("%Y-%m-%d")
        }

    def run_scheduled_reviews(self) -> List[Dict]:
        """スケジュールされたレビューを実行（日次実行想定）"""

        today = datetime.now().strftime("%Y-%m-%d")
        results = []

        print(f"🔍 スケジュールされたレビューをチェック中... (日付: {today})")

        # 実行すべきレビューを抽出
        pending_reviews = [
            r for r in self.schedule_db["scheduled_reviews"]
            if r["review_date"] == today and r["status"] == "scheduled"
        ]

        if not pending_reviews:
            print("   実行すべきレビューはありません")
            return results

        print(f"   実行すべきレビュー: {len(pending_reviews)}件")

        for review in pending_reviews:
            print(f"\n📋 レビュー実行中: {review['id']}")
            print(f"   対象ファイル: {review['post_file_path']}")

            # レビュー実行
            result = self.run_review(
                post_file_path=review["post_file_path"],
                review_type=review["review_type"],
                auto_apply=review["auto_apply"],
                priority=review["priority"]
            )

            # ステータス更新
            review["status"] = "completed"
            review["completed_at"] = datetime.now().isoformat()
            review["result"] = result

            # 完了リストに移動
            self.schedule_db["completed_reviews"].append(review)
            self.schedule_db["scheduled_reviews"].remove(review)

            results.append(result)

        self.save_schedule_db()

        # 通知
        self.send_notification(
            f"スケジュールされたレビューを{len(results)}件実行しました",
            results
        )

        return results

    def run_review(self, post_file_path: str, review_type: str, auto_apply: bool, priority: List[str]) -> Dict:
        """レビューを実行"""

        try:
            # 投稿ファイルを読み込み
            post_content = self.read_post_file(post_file_path)

            # validators/check_required_elements.pyを使用して評価
            from ..validators.check_required_elements import check_all_elements, format_report

            result = check_all_elements(post_content)
            report = format_report(result)

            # レポート保存
            report_path = self.save_review_report(
                post_file_path=post_file_path,
                review_type=review_type,
                report=report,
                result=result
            )

            print(f"\n{report}")
            print(f"\n✅ レビューレポートを保存しました: {report_path}")

            # 自動適用（設定されている場合）
            if auto_apply and result["total_score"] < 70:
                print(f"\n🔧 スキル自動改善を実行します（優先度: {', '.join(priority)}）")
                improvement_result = self.run_auto_improvement(result, priority)
                result["improvement"] = improvement_result

            return {
                "status": "success",
                "review_type": review_type,
                "total_score": result["total_score"],
                "report_path": str(report_path),
                "auto_apply": auto_apply,
                "result": result
            }

        except Exception as e:
            print(f"❌ レビュー実行エラー: {str(e)}")
            import traceback
            traceback.print_exc()
            return {
                "status": "error",
                "review_type": review_type,
                "error": str(e)
            }

    def read_post_file(self, post_file_path: str) -> str:
        """投稿ファイルを読み込み（案1-3から最推奨案を抽出）"""

        with open(post_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 🏆最推奨案を抽出
        import re
        pattern = r'🏆.*?案\s*\d+.*?\n\n(.*?)(?=\n\n#{1,3}\s|$)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            return match.group(1).strip()

        # 最推奨案が見つからない場合は案1を抽出
        pattern = r'##\s*案\s*1.*?\n\n(.*?)(?=\n\n#{1,3}\s|$)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            return match.group(1).strip()

        # それでも見つからない場合はファイル全体を返す
        return content

    def save_review_report(self, post_file_path: str, review_type: str, report: str, result: Dict) -> Path:
        """レビューレポートを保存"""

        post_path = Path(post_file_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # レポート保存先
        report_dir = post_path.parent / "reviews"
        report_dir.mkdir(exist_ok=True)

        report_filename = f"review_report_{review_type}_{timestamp}.md"
        report_path = report_dir / report_filename

        # レポート内容
        full_report = f"""# SNS投稿レビューレポート

## 基本情報

- **レビュータイプ**: {review_type}
- **対象ファイル**: {post_file_path}
- **実行日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **総合スコア**: {result['total_score']:.1f}点 ({result['status']})

---

{report}

---

## 詳細データ

```json
{json.dumps(result, ensure_ascii=False, indent=2)}
```

---

**生成日時**: {datetime.now().isoformat()}
"""

        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(full_report)

        return report_path

    def run_auto_improvement(self, review_result: Dict, priority: List[str]) -> Dict:
        """スキル自動改善を実行"""

        # ここでは簡易実装（実際にはSKILL.mdの修正ロジックを実装）
        print("⚠️  自動改善機能は現在開発中です")
        print("   検出された問題を手動で確認してください")

        return {
            "status": "pending",
            "message": "自動改善機能は現在開発中",
            "detected_issues": [
                data['suggestion'] for data in review_result['scores'].values()
                if data.get('suggestion')
            ]
        }

    def send_notification(self, message: str, details: Optional[List[Dict]] = None):
        """通知を送信"""

        if not self.config["notification"]["enabled"]:
            return

        method = self.config["notification"]["method"]

        if method == "file":
            self.send_file_notification(message, details)
        elif method == "slack":
            self.send_slack_notification(message, details)
        elif method == "email":
            self.send_email_notification(message, details)

    def send_file_notification(self, message: str, details: Optional[List[Dict]] = None):
        """ファイル通知"""

        notification_dir = self.base_dir / "Flow/notifications"
        notification_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        notification_file = notification_dir / f"review_notification_{timestamp}.md"

        content = f"""# レビュー通知

**日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## メッセージ

{message}

## 詳細

"""

        if details:
            for i, detail in enumerate(details, 1):
                content += f"""
### 結果 {i}

- **ステータス**: {detail.get('status', 'unknown')}
- **レビュータイプ**: {detail.get('review_type', 'unknown')}
- **総合スコア**: {detail.get('total_score', 'N/A')}点
- **レポート**: {detail.get('report_path', 'N/A')}

"""

        with open(notification_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n📬 通知を保存しました: {notification_file}")

    def send_slack_notification(self, message: str, details: Optional[List[Dict]] = None):
        """Slack通知（未実装）"""
        print("⚠️  Slack通知は未実装です")

    def send_email_notification(self, message: str, details: Optional[List[Dict]] = None):
        """メール通知（未実装）"""
        print("⚠️  メール通知は未実装です")

    def record_review_result(self, post_file_path: str, review_type: str, result: Dict):
        """レビュー結果を記録"""

        record_entry = {
            "post_file_path": post_file_path,
            "review_type": review_type,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }

        self.schedule_db["completed_reviews"].append(record_entry)
        self.save_schedule_db()


def main():
    """メイン実行"""

    import argparse

    parser = argparse.ArgumentParser(description="SNS投稿自動レビュースケジューラー")

    subparsers = parser.add_subparsers(dest='command', help='サブコマンド')

    # immediate: 投稿生成直後のレビュー
    immediate_parser = subparsers.add_parser('immediate', help='投稿生成直後のレビューを実行')
    immediate_parser.add_argument('--post-file', required=True, help='投稿ファイルのパス')

    # schedule: 予約投稿の1日後のレビューをスケジュール
    schedule_parser = subparsers.add_parser('schedule', help='予約投稿の1日後のレビューをスケジュール')
    schedule_parser.add_argument('--post-file', required=True, help='投稿ファイルのパス')
    schedule_parser.add_argument('--publication-date', required=True, help='公開予定日（YYYY-MM-DD）')

    # run: スケジュールされたレビューを実行
    run_parser = subparsers.add_parser('run', help='スケジュールされたレビューを実行（日次実行想定）')

    # list: スケジュール一覧を表示
    list_parser = subparsers.add_parser('list', help='スケジュール一覧を表示')

    args = parser.parse_args()

    scheduler = AutoReviewScheduler()

    if args.command == 'immediate':
        result = scheduler.schedule_immediate_review(args.post_file)
        print(f"\n✅ 実行完了: {json.dumps(result, ensure_ascii=False, indent=2)}")

    elif args.command == 'schedule':
        result = scheduler.schedule_post_publication_review(args.post_file, args.publication_date)
        print(f"\n✅ スケジュール登録完了: {json.dumps(result, ensure_ascii=False, indent=2)}")

    elif args.command == 'run':
        results = scheduler.run_scheduled_reviews()
        print(f"\n✅ 実行完了: {len(results)}件")

    elif args.command == 'list':
        print("\n📋 スケジュール一覧\n")
        print(f"予定: {len(scheduler.schedule_db['scheduled_reviews'])}件")
        for review in scheduler.schedule_db['scheduled_reviews']:
            print(f"  - {review['id']}: {review['review_date']} ({review['review_type']})")

        print(f"\n完了: {len(scheduler.schedule_db['completed_reviews'])}件")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
