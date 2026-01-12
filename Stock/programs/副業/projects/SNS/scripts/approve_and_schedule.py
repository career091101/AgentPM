#!/usr/bin/env python3
"""
approve-and-schedule スキル実装
Slack Interactive Buttonsで投稿承認 + 自動スケジューリング
"""
import os
import sys
import json
import time
import glob
from datetime import datetime, timedelta
import pytz
import requests
from pathlib import Path
from dotenv import load_dotenv

# .envファイル読み込み（プロジェクトルート）
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# 環境変数読み込み
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL")
SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"

# グローバル変数（thread_ts管理）
CURRENT_THREAD_TS = None


def load_posts_data(date_str=None):
    """Phase 3（generate-sns-posts）出力ファイルを読み込み"""
    if date_str:
        data_file = f"{SNS_DATA_DIR}/posts_generated_{date_str}.json"
    else:
        # 最新ファイルを自動検索
        files = glob.glob(f"{SNS_DATA_DIR}/posts_generated_*.json")
        if not files:
            raise FileNotFoundError("posts_generated_*.json が見つかりません")
        data_file = max(files, key=os.path.getctime)

    print(f"📂 読み込み: {data_file}")

    with open(data_file, "r", encoding="utf-8") as f:
        return json.load(f)


def create_slack_blocks(data):
    """Block Kitでインタラクティブボタン付きメッセージを作成"""
    topic = data["metadata"]["topic_selected"]
    generated_at = data["metadata"]["generated_at"]
    posts = data["posts"]

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🚀 LinkedIn投稿3案生成完了",
                "emoji": True
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*トピック:*\n{topic}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*生成日時:*\n{generated_at}"
                }
            ]
        },
        {
            "type": "divider"
        }
    ]

    # 各案のセクションとボタンを追加
    for i, post in enumerate(posts, 1):
        recommended_badge = " ✅ 推奨" if post.get("recommended") else ""

        # 投稿内容セクション
        blocks.extend([
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*案{i}: {post['variant']}* ({post['rating']}){recommended_badge}\n文字数: {post['character_count']}字 | 予測ER: {post['predicted_er']}\n\n{post['content']}"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        **({
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": f"✅ 案{i}を承認",
                                "emoji": True
                            },
                            "value": f"variant_{i}",
                            "action_id": f"approve_variant_{i}",
                            "style": "primary"
                        } if post.get("recommended") else {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": f"✅ 案{i}を承認",
                                "emoji": True
                            },
                            "value": f"variant_{i}",
                            "action_id": f"approve_variant_{i}"
                        })
                    }
                ]
            },
            {
                "type": "divider"
            }
        ])

    # フッター情報
    blocks.append({
        "type": "context",
        "elements": [
            {
                "type": "mrkdwn",
                "text": "⏱️ タイムアウト: 24時間（承認がない場合は推奨案を自動承認）\n📅 投稿予定時刻: LinkedIn 8:00 JST, Facebook/X 20:00 JST"
            }
        ]
    })

    return blocks


def send_slack_message_with_buttons(blocks):
    """Block Kit形式のメッセージをSlackに送信"""
    global CURRENT_THREAD_TS

    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    }

    payload = {
        "channel": SLACK_CHANNEL,
        "blocks": blocks,
        "text": "LinkedIn投稿3案生成完了 - 承認をお願いします"  # fallback text
    }

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers=headers,
        json=payload
    )

    result = response.json()

    if result.get("ok"):
        CURRENT_THREAD_TS = result.get("ts")  # グローバル変数に保存
        print(f"✅ Slack通知送信成功")
        print(f"   チャンネル: {result.get('channel')}")
        print(f"   タイムスタンプ: {CURRENT_THREAD_TS}")
        return CURRENT_THREAD_TS
    else:
        print(f"❌ Slack通知送信失敗: {result.get('error')}")
        return None


def wait_for_approval(timeout=300):
    """承認結果をポーリングで確認（5分タイムアウト）"""
    print(f"\n⏳ Slack承認待機中...")
    print(f"   Slackの #{SLACK_CHANNEL} チャンネルでボタンをクリックしてください")
    print(f"   タイムアウト: {timeout}秒")

    start_time = time.time()
    check_interval = 5  # 5秒ごとにチェック

    while time.time() - start_time < timeout:
        # 承認結果ファイルを探す
        approval_files = glob.glob(f"{SNS_DATA_DIR}/approval_result_*.json")

        if approval_files:
            # 最新の承認結果を読み込み
            latest_approval = max(approval_files, key=os.path.getctime)

            with open(latest_approval, "r", encoding="utf-8") as f:
                approval_data = json.load(f)

            if approval_data.get("approved"):
                print(f"\n✅ {approval_data['variant']}が承認されました！")
                print(f"   承認者: {approval_data['user_id']}")
                print(f"   承認時刻: {approval_data['timestamp']}")

                # 承認結果ファイルを削除（次回実行時の誤検出防止）
                os.remove(latest_approval)

                return approval_data["variant"]

        # 待機
        time.sleep(check_interval)
        elapsed = int(time.time() - start_time)
        print(f"   経過時間: {elapsed}秒 / {timeout}秒", end="\r")

    print("\n⚠️  タイムアウト: 推奨案を自動承認します")
    return "案1"  # デフォルトで推奨案（案1）を承認


def schedule_posts(approved_variant, posts_data):
    """承認された投稿をスケジューリングキューに追加"""
    # approval_result から修正フラグを確認
    approval_files = glob.glob(f"{SNS_DATA_DIR}/approval_result_*.json")
    if not approval_files:
        print("❌ 承認結果ファイルが見つかりません")
        return None

    latest_approval = max(approval_files, key=os.path.getctime)

    with open(latest_approval, "r", encoding="utf-8") as f:
        approval_data = json.load(f)

    # 修正案か元の案かを判定
    if approval_data.get("refined"):
        # 修正案の場合
        selected_post = {
            "content": approval_data["refined_content"],
            "variant": approval_data["variant"],
            "character_count": len(approval_data["refined_content"]),
            "predicted_er": "未計算（修正版）"
        }
        print(f"✅ 修正案を使用: {approval_data['variant']}（修正{approval_data['refine_count']}回目）")
    else:
        # 元の案の場合（既存ロジック）
        variant_index = int(approved_variant.replace("案", "")) - 1
        selected_post = posts_data["posts"][variant_index]
        print(f"✅ 元の案を使用: {approved_variant}")

    # 日本時間で翌日の投稿時刻を設定
    jst = pytz.timezone("Asia/Tokyo")
    tomorrow = datetime.now(jst) + timedelta(days=1)

    linkedin_time = tomorrow.replace(hour=8, minute=0, second=0, microsecond=0)
    facebook_time = tomorrow.replace(hour=20, minute=0, second=0, microsecond=0)
    x_time = tomorrow.replace(hour=20, minute=0, second=0, microsecond=0)

    # スケジューリングキュー作成
    queue = {
        "approved_at": datetime.now(jst).isoformat(),
        "approved_variant": approved_variant,
        "posts": [
            {
                "platform": "LinkedIn",
                "content": selected_post["content"],
                "scheduled_time": linkedin_time.isoformat(),
                "status": "scheduled"
            },
            {
                "platform": "Facebook",
                "content": selected_post["content"],
                "scheduled_time": facebook_time.isoformat(),
                "status": "scheduled"
            },
            {
                "platform": "X",
                "content": selected_post["content"],
                "scheduled_time": x_time.isoformat(),
                "status": "scheduled"
            }
        ]
    }

    # キューをファイルに保存
    queue_file = f"{SNS_DATA_DIR}/posts_queue_{datetime.now(jst).strftime('%Y%m%d')}.json"

    with open(queue_file, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 投稿スケジューリング完了: {queue_file}")
    print(f"   LinkedIn: {linkedin_time.strftime('%Y-%m-%d %H:%M JST')}")
    print(f"   Facebook/X: {facebook_time.strftime('%Y-%m-%d %H:%M JST')}")

    return queue_file


def main():
    print("=" * 60)
    print("Slack Interactive Buttons承認システム")
    print("=" * 60)

    # 環境変数チェック
    if not SLACK_BOT_TOKEN:
        print("❌ SLACK_BOT_TOKEN が設定されていません")
        return

    if not SLACK_CHANNEL:
        print("❌ SLACK_CHANNEL が設定されていません")
        return

    print(f"\n📋 設定確認")
    print(f"   チャンネル: {SLACK_CHANNEL}")

    # Phase 3データ読み込み
    print(f"\n📂 Phase 3データ読み込み中...")
    data = load_posts_data()
    print(f"✅ 読み込み完了: {data['metadata']['topic_selected']}")

    # Block Kitメッセージ作成
    print(f"\n📝 Slack Block Kitメッセージ作成中...")
    blocks = create_slack_blocks(data)
    print(f"✅ ボタン付きメッセージ作成完了（{len(blocks)}ブロック）")

    # Slack送信
    print(f"\n📤 Slack通知送信中...")
    thread_ts = send_slack_message_with_buttons(blocks)

    if not thread_ts:
        print("❌ テスト失敗")
        return

    # 承認待機
    approved_variant = wait_for_approval(timeout=300)  # 5分タイムアウト

    # スケジューリングキュー作成
    queue_file = schedule_posts(approved_variant, data)

    print(f"\n✅ 承認フロー完了")
    print(f"   承認案: {approved_variant}")
    print(f"   キューファイル: {queue_file}")
    print("\n" + "=" * 60)
    print("処理完了")
    print("=" * 60)


if __name__ == "__main__":
    main()
