#!/usr/bin/env python3
"""
Approval Queue Manager
承認キュー管理システム

Directory Structure:
- posts_queue/     : 未承認の投稿案
- posts_approved/  : 承認済み（スケジュール待ち）
- posts_archived/  : 却下 or 投稿完了
"""

import json
import os
import glob
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import shutil
import uuid
import pytz


# プラットフォーム別デフォルト投稿時刻（JST）
PLATFORM_DEFAULT_TIMES = {
    "LinkedIn": {"hour": 8, "minute": 0},   # 朝8:00 JST
    "X": {"hour": 20, "minute": 0},         # 夜20:00 JST
    "Threads": {"hour": 20, "minute": 0},   # 夜20:00 JST
    "Facebook": {"hour": 20, "minute": 0}   # 夜20:00 JST（将来用）
}


class ApprovalQueueManager:
    """承認キュー管理クラス"""

    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.queue_dir = os.path.join(data_dir, "posts_queue")
        self.approved_dir = os.path.join(data_dir, "posts_approved")
        self.archived_dir = os.path.join(data_dir, "posts_archived")

        # ディレクトリ作成
        os.makedirs(self.queue_dir, exist_ok=True)
        os.makedirs(self.approved_dir, exist_ok=True)
        os.makedirs(self.archived_dir, exist_ok=True)

    def add_to_queue(self, posts_data: Dict) -> str:
        """
        新規投稿案をキューに追加

        Args:
            posts_data: 投稿案データ（posts_generated_*.jsonの内容）

        Returns:
            queue_id: 生成されたキューID
        """
        queue_id = str(uuid.uuid4())[:8]
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # キューファイル作成
        queue_file = os.path.join(self.queue_dir, f"pending_{timestamp}_{queue_id}.json")

        # ステータス情報を追加
        queue_data = {
            "queue_id": queue_id,
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "approved_at": None,
            "rejected_at": None,
            "scheduled_at": None,
            "posted_at": None,
            "metadata": posts_data.get("metadata", {}),
            "topic": posts_data.get("topic", {}),
            "posts": []
        }

        # 各投稿案にステータスを追加
        for post in posts_data.get("posts", []):
            queue_data["posts"].append({
                **post,
                "post_status": "pending",  # pending / approved / rejected
                "approved_at": None,
                "rejected_at": None,
                "rejection_reason": None
            })

        # 保存
        with open(queue_file, 'w', encoding='utf-8') as f:
            json.dump(queue_data, f, ensure_ascii=False, indent=2)

        return queue_id

    def get_pending_posts(self) -> List[Dict]:
        """
        未承認の投稿案一覧を取得

        Returns:
            List[Dict]: 未承認投稿案のリスト
        """
        pending_files = glob.glob(os.path.join(self.queue_dir, "pending_*.json"))
        pending_posts = []

        for file_path in sorted(pending_files, key=os.path.getctime, reverse=True):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    data["file_path"] = file_path
                    pending_posts.append(data)
            except Exception as e:
                print(f"Error loading {file_path}: {e}")

        return pending_posts

    def approve_post(self, queue_id: str, variant_index: int,
                     refined_content: Optional[str] = None) -> bool:
        """
        投稿案を承認してapproved/に移動

        Args:
            queue_id: キューID
            variant_index: 承認する投稿案のインデックス（0-2）
            refined_content: 修正後の内容（オプション）

        Returns:
            bool: 成功/失敗
        """
        # キューファイルを検索
        queue_file = self._find_queue_file(queue_id)
        if not queue_file:
            return False

        # データ読み込み
        with open(queue_file, 'r', encoding='utf-8') as f:
            queue_data = json.load(f)

        # variant_indexのバリデーション
        if variant_index < 0 or variant_index >= len(queue_data["posts"]):
            return False

        # 承認情報を更新
        queue_data["posts"][variant_index]["post_status"] = "approved"
        queue_data["posts"][variant_index]["approved_at"] = datetime.now().isoformat()

        if refined_content:
            queue_data["posts"][variant_index]["refined_content"] = refined_content
            queue_data["posts"][variant_index]["content"] = refined_content

        # approved/に移動
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        approved_file = os.path.join(
            self.approved_dir,
            f"approved_{timestamp}_{queue_id}.json"
        )

        # 承認データ作成（承認された投稿案のみ）
        approved_data = {
            "queue_id": queue_id,
            "status": "approved",
            "approved_at": datetime.now().isoformat(),
            "scheduled_at": None,
            "posted_at": None,
            "metadata": queue_data["metadata"],
            "topic": queue_data["topic"],
            "approved_post": queue_data["posts"][variant_index]
        }

        # 保存
        with open(approved_file, 'w', encoding='utf-8') as f:
            json.dump(approved_data, f, ensure_ascii=False, indent=2)

        # 元のキューファイルを削除
        os.remove(queue_file)

        return True

    def reject_post(self, queue_id: str, reason: str = "User rejected") -> bool:
        """
        投稿案を却下してarchived/に移動

        Args:
            queue_id: キューID
            reason: 却下理由

        Returns:
            bool: 成功/失敗
        """
        # キューファイルを検索
        queue_file = self._find_queue_file(queue_id)
        if not queue_file:
            return False

        # データ読み込み
        with open(queue_file, 'r', encoding='utf-8') as f:
            queue_data = json.load(f)

        # 却下情報を更新
        queue_data["status"] = "rejected"
        queue_data["rejected_at"] = datetime.now().isoformat()
        queue_data["rejection_reason"] = reason

        # archived/に移動
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        archived_file = os.path.join(
            self.archived_dir,
            f"rejected_{timestamp}_{queue_id}.json"
        )

        # 保存
        with open(archived_file, 'w', encoding='utf-8') as f:
            json.dump(queue_data, f, ensure_ascii=False, indent=2)

        # 元のキューファイルを削除
        os.remove(queue_file)

        return True

    def get_approved_posts(self) -> List[Dict]:
        """
        承認済み投稿案一覧を取得（スケジュール待ち）

        Returns:
            List[Dict]: 承認済み投稿案のリスト
        """
        approved_files = glob.glob(os.path.join(self.approved_dir, "approved_*.json"))
        approved_posts = []

        for file_path in sorted(approved_files, key=os.path.getctime, reverse=True):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    data["file_path"] = file_path
                    approved_posts.append(data)
            except Exception as e:
                print(f"Error loading {file_path}: {e}")

        return approved_posts

    def mark_as_scheduled(self, queue_id: str, scheduled_info: Optional[Dict[str, Dict]] = None,
                          scheduled_time: Optional[str] = None, late_post_id: Optional[str] = None) -> bool:
        """
        承認済み投稿案をスケジュール済みとしてマーク

        Args:
            queue_id: キューID
            scheduled_info: プラットフォーム別スケジュール情報（新方式）
                {
                    "LinkedIn": {"scheduled_time": "...", "late_post_id": "..."},
                    "X": {"scheduled_time": "...", "late_post_id": "..."},
                    ...
                }
            scheduled_time: スケジュール日時（ISO 8601）（旧方式互換性用）
            late_post_id: Late APIのPost ID（旧方式互換性用）

        Returns:
            bool: 成功/失敗
        """
        approved_file = self._find_approved_file(queue_id)
        if not approved_file:
            return False

        # データ読み込み
        with open(approved_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # スケジュール情報を更新
        data["status"] = "scheduled"

        # 新方式（プラットフォーム別）
        if scheduled_info:
            data["scheduled_info"] = scheduled_info
            data["scheduled_at"] = datetime.now(pytz.timezone('Asia/Tokyo')).isoformat()

        # 旧方式（互換性維持）
        elif scheduled_time and late_post_id:
            data["scheduled_at"] = scheduled_time
            data["late_post_id"] = late_post_id

        # 保存
        with open(approved_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return True

    def delete_pending_post(self, queue_id: str) -> bool:
        """
        未承認投稿を削除

        Args:
            queue_id: キューID

        Returns:
            bool: 成功/失敗
        """
        queue_file = self._find_queue_file(queue_id)
        if not queue_file:
            return False

        try:
            os.remove(queue_file)
            return True
        except Exception as e:
            print(f"Error deleting pending post: {e}")
            return False

    def delete_approved_post(self, queue_id: str) -> bool:
        """
        承認済み投稿を削除

        Args:
            queue_id: キューID

        Returns:
            bool: 成功/失敗
        """
        approved_file = self._find_approved_file(queue_id)
        if not approved_file:
            return False

        try:
            os.remove(approved_file)
            return True
        except Exception as e:
            print(f"Error deleting approved post: {e}")
            return False

    def mark_as_posted(self, queue_id: str) -> bool:
        """
        投稿完了としてマークし、archived/に移動

        Args:
            queue_id: キューID

        Returns:
            bool: 成功/失敗
        """
        approved_file = self._find_approved_file(queue_id)
        if not approved_file:
            return False

        # データ読み込み
        with open(approved_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 投稿完了情報を更新
        data["status"] = "posted"
        data["posted_at"] = datetime.now().isoformat()

        # archived/に移動
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        archived_file = os.path.join(
            self.archived_dir,
            f"posted_{timestamp}_{queue_id}.json"
        )

        # 保存
        with open(archived_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # 元のapprovedファイルを削除
        os.remove(approved_file)

        return True

    def check_pending_count(self) -> int:
        """
        未承認投稿案の数を確認

        Returns:
            int: 未承認投稿案の数
        """
        pending_files = glob.glob(os.path.join(self.queue_dir, "pending_*.json"))
        return len(pending_files)

    def _find_queue_file(self, queue_id: str) -> Optional[str]:
        """キューIDからファイルパスを検索"""
        # パターン1: pending_{timestamp}_{queue_id}.json（新形式）
        pattern1 = os.path.join(self.queue_dir, f"pending_*_{queue_id}.json")
        files = glob.glob(pattern1)
        if files:
            return files[0]

        # パターン2: pending_{queue_id}.json（旧形式・queue_idがタイムスタンプの場合）
        pattern2 = os.path.join(self.queue_dir, f"pending_{queue_id}.json")
        if os.path.exists(pattern2):
            return pattern2

        # パターン3: 全ファイルからqueue_idを検索（JSONの中身を確認）
        all_files = glob.glob(os.path.join(self.queue_dir, "pending_*.json"))
        for file_path in all_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data.get("queue_id") == queue_id:
                        return file_path
            except Exception:
                continue

        return None

    def _find_approved_file(self, queue_id: str) -> Optional[str]:
        """キューIDから承認済みファイルパスを検索"""
        pattern = os.path.join(self.approved_dir, f"approved_*_{queue_id}.json")
        files = glob.glob(pattern)
        return files[0] if files else None

    def update_pending_post(self, queue_id: str, variant_index: int,
                            new_content: str) -> bool:
        """
        未承認キューの投稿案を更新

        Args:
            queue_id: キューID
            variant_index: バリエーションインデックス（0-2）
            new_content: 新しい投稿内容

        Returns:
            bool: 成功/失敗
        """
        # キューファイルを検索
        queue_file = self._find_queue_file(queue_id)
        if not queue_file:
            return False

        # データ読み込み
        with open(queue_file, 'r', encoding='utf-8') as f:
            queue_data = json.load(f)

        # variant_indexのバリデーション
        if variant_index < 0 or variant_index >= len(queue_data["posts"]):
            return False

        # 内容を更新
        queue_data["posts"][variant_index]["content"] = new_content

        # 保存
        with open(queue_file, 'w', encoding='utf-8') as f:
            json.dump(queue_data, f, ensure_ascii=False, indent=2)

        return True

    def update_approved_post(self, queue_id: str, new_content: str) -> bool:
        """
        承認済みキューの投稿案を更新

        Args:
            queue_id: キューID
            new_content: 新しい投稿内容

        Returns:
            bool: 成功/失敗
        """
        approved_file = self._find_approved_file(queue_id)
        if not approved_file:
            return False

        # データ読み込み
        with open(approved_file, 'r', encoding='utf-8') as f:
            approved_data = json.load(f)

        # 内容を更新
        approved_data["approved_post"]["content"] = new_content

        # 保存
        with open(approved_file, 'w', encoding='utf-8') as f:
            json.dump(approved_data, f, ensure_ascii=False, indent=2)

        return True

    def get_approved_post_content(self, queue_id: str) -> Optional[Dict]:
        """
        承認済み投稿案の内容を取得（スケジューリング用）

        Args:
            queue_id: キューID

        Returns:
            Dict: approved_post データまたはNone
        """
        approved_file = self._find_approved_file(queue_id)
        if not approved_file:
            return None

        # データ読み込み
        with open(approved_file, 'r', encoding='utf-8') as f:
            approved_data = json.load(f)

        return approved_data.get("approved_post")

    def schedule_post_auto(
        self,
        queue_id: str,
        platforms: List[str]
    ) -> Dict[str, any]:
        """
        承認済み投稿を自動スケジューリング（プラットフォーム別最適化あり）

        Args:
            queue_id: キューID
            platforms: 投稿先プラットフォームリスト（例: ["LinkedIn", "X", "Threads"]）
                       注意: "Facebook"は自動投稿対象外（除外される）

        Returns:
            Dict: {
                "success": True,
                "scheduled_info": {
                    "LinkedIn": {
                        "scheduled_time": "2026-01-06T08:00:00+09:00",
                        "late_post_id": "late_abc123",
                        "optimized_content": "..."
                    },
                    "X": {...},
                    "Threads": {...}
                }
            }
        """
        # STEP 1: 承認済みファイルパスを取得
        approved_file = self._find_approved_file(queue_id)
        if not approved_file:
            return {"success": False, "error": "承認済み投稿が見つかりません"}

        # STEP 1.5: Facebookを除外
        platforms = [p for p in platforms if p != "Facebook"]
        if not platforms:
            return {"success": False, "error": "自動投稿対象プラットフォームがありません（Facebookは対象外）"}

        # STEP 2: プラットフォーム別最適化を実行
        with open(approved_file, 'r', encoding='utf-8') as f:
            approved_data = json.load(f)

        linkedin_content = approved_data.get("approved_post", {}).get("content", "")

        try:
            from platform_optimizer import optimize_all_platforms
            optimization_results = optimize_all_platforms(linkedin_content, platforms)
            print(f"✅ プラットフォーム別最適化完了")
        except Exception as e:
            print(f"⚠️ 最適化失敗、元の投稿を使用: {e}")
            # フォールバック: LinkedIn投稿をそのまま使用
            optimization_results = {
                platform: {"optimized_content": linkedin_content}
                for platform in platforms
            }

        # STEP 3: 次回投稿時刻を取得（プラットフォーム別）
        next_times = self.get_next_available_schedule_times()

        # STEP 4: Late APIで投稿予約（プラットフォームごと）
        scheduled_info = {}

        for platform in platforms:
            if platform not in next_times:
                continue

            scheduled_time = next_times[platform]

            # プラットフォーム別最適化内容を取得
            optimized_data = optimization_results.get(platform, {})
            optimized_content = optimized_data.get("optimized_content", linkedin_content)
            thread_posts = optimized_data.get("thread_posts", [])
            recommended_format = optimized_data.get("recommended_format", "single")

            # Late API呼び出し（post_to_sns_late.py）
            late_result = self._call_late_api(
                queue_id=queue_id,
                approved_file=approved_file,
                scheduled_time=scheduled_time,
                platforms=[platform],
                optimized_content=optimized_content,
                thread_posts=thread_posts,
                recommended_format=recommended_format
            )

            if late_result["success"]:
                scheduled_info[platform] = {
                    "scheduled_time": scheduled_time.isoformat(),
                    "late_post_id": late_result.get("late_post_id"),
                    "optimized_content": optimized_content[:100] + "...",  # 先頭100文字
                    "format": recommended_format
                }
            else:
                return {
                    "success": False,
                    "error": f"{platform}のスケジューリング失敗: {late_result.get('error')}"
                }

        # STEP 5: approved_*.json にスケジュール情報を保存
        self.mark_as_scheduled(queue_id, scheduled_info)

        return {
            "success": True,
            "scheduled_info": scheduled_info
        }

    def _call_late_api(
        self,
        queue_id: str,
        approved_file: str,
        scheduled_time: datetime,
        platforms: List[str],
        optimized_content: Optional[str] = None,
        thread_posts: Optional[List[str]] = None,
        recommended_format: Optional[str] = None
    ) -> Dict[str, any]:
        """
        Late APIを呼び出して投稿予約（プラットフォーム別最適化対応）

        Args:
            queue_id: キューID
            approved_file: 承認済みファイルのパス
            scheduled_time: 予約時刻
            platforms: 投稿先プラットフォームリスト
            optimized_content: 最適化された投稿内容（オプション）
            thread_posts: スレッド投稿リスト（オプション）
            recommended_format: "single" or "thread"（オプション）

        Returns:
            Dict: {"success": True, "late_post_id": "late_abc123"}
        """
        import subprocess

        # post_to_sns_late.py を実行（既存実装を再利用）
        scripts_dir = os.path.dirname(os.path.abspath(__file__))
        late_script = os.path.join(scripts_dir, "post_to_sns_late.py")

        # scheduled_post_idを生成（queue_id + timestamp）
        scheduled_post_id = f"{queue_id}_{scheduled_time.strftime('%Y%m%d_%H%M%S')}"

        # コマンドライン引数を構築
        cmd = [
            "python3",
            late_script,
            "--file", approved_file,
            "--platforms", *platforms,
            "--scheduled-time", scheduled_time.isoformat(),
            "--scheduled-post-id", scheduled_post_id
        ]

        # 最適化内容を引数に追加
        if optimized_content:
            cmd.extend(["--optimized-content", optimized_content])

        if thread_posts:
            cmd.extend(["--thread-posts", json.dumps(thread_posts, ensure_ascii=False)])

        if recommended_format:
            cmd.extend(["--recommended-format", recommended_format])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            # 成功: Late Post IDを抽出
            output = result.stdout
            # 例: "Late Post ID: late_abc123" という出力を想定
            late_post_id = self._extract_late_post_id(output)
            return {"success": True, "late_post_id": late_post_id}
        else:
            return {"success": False, "error": result.stderr}

    def _extract_late_post_id(self, output: str) -> str:
        """Late API出力からPost IDを抽出"""
        import re
        # "Late Post ID: late_abc123" のようなパターンを想定
        match = re.search(r'Late Post ID:\s*(\S+)', output)
        if match:
            return match.group(1)
        # 見つからない場合はタイムスタンプベースのIDを生成
        return f"late_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def get_next_available_schedule_times(self) -> Dict[str, datetime]:
        """
        次に利用可能な投稿時刻を取得（プラットフォーム別）

        Returns:
            Dict[str, datetime]: {
                "LinkedIn": datetime(2026, 1, 6, 8, 0, tzinfo=JST),
                "X": datetime(2026, 1, 6, 20, 0, tzinfo=JST),
                "Threads": datetime(2026, 1, 6, 20, 0, tzinfo=JST)
            }
        """
        JST = pytz.timezone('Asia/Tokyo')
        now = datetime.now(JST)

        # 既存のスケジュールを全て読み込み
        existing_schedules = self._load_all_scheduled_posts()

        # プラットフォーム別の次回投稿時刻を計算
        next_times = {}

        for platform in ["LinkedIn", "X", "Threads"]:
            # デフォルト時刻取得（8:00 or 20:00）
            default_hour = PLATFORM_DEFAULT_TIMES[platform]["hour"]
            default_minute = PLATFORM_DEFAULT_TIMES[platform]["minute"]

            # 明日の該当時刻を初期値とする
            candidate = (now + timedelta(days=1)).replace(
                hour=default_hour,
                minute=default_minute,
                second=0,
                microsecond=0
            )

            # 既存スケジュールと衝突しないか確認
            while self._is_time_slot_occupied(candidate, platform, existing_schedules):
                # 1時間ずらす
                candidate += timedelta(hours=1)

            next_times[platform] = candidate

        return next_times

    def _is_time_slot_occupied(
        self,
        candidate_time: datetime,
        platform: str,
        existing_schedules: List[Dict]
    ) -> bool:
        """指定時刻が既に使用されているか確認"""
        for schedule in existing_schedules:
            scheduled_info = schedule.get("scheduled_info", {})
            if platform not in scheduled_info:
                continue

            scheduled_time_str = scheduled_info[platform]["scheduled_time"]
            scheduled_time = datetime.fromisoformat(scheduled_time_str)

            # 同じ時刻（1時間以内）なら衝突
            if abs((candidate_time - scheduled_time).total_seconds()) < 3600:
                return True

        return False

    def _load_all_scheduled_posts(self) -> List[Dict]:
        """全ての承認済みキューからスケジュール情報を取得"""
        approved_files = glob.glob(
            os.path.join(self.approved_dir, "approved_*_*.json")
        )

        schedules = []
        for file_path in approved_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if data.get("status") == "scheduled":
                        schedules.append(data)
            except Exception as e:
                print(f"Error loading {file_path}: {e}")

        return schedules


# 使用例
if __name__ == "__main__":
    data_dir = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
    manager = ApprovalQueueManager(data_dir)

    # 未承認投稿案の数を確認
    pending_count = manager.check_pending_count()
    print(f"未承認投稿案: {pending_count}件")

    # 未承認投稿案一覧
    pending_posts = manager.get_pending_posts()
    for post in pending_posts:
        print(f"Queue ID: {post['queue_id']}, Created: {post['created_at']}")

    # 承認済み投稿案一覧
    approved_posts = manager.get_approved_posts()
    for post in approved_posts:
        print(f"Queue ID: {post['queue_id']}, Approved: {post['approved_at']}")
