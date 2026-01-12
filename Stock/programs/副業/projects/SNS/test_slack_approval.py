#!/usr/bin/env python3
"""
Slack承認テストスクリプト
"""
import os
import json
import time
from datetime import datetime
import requests

# 環境変数読み込み
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL")

def load_posts_data():
    """Phase 3出力ファイルを読み込み"""
    data_file = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/posts_generated_ai_20260102.json"

    with open(data_file, "r", encoding="utf-8") as f:
        return json.load(f)

def create_slack_message(data):
    """Slack通知メッセージを作成"""
    topic = data["metadata"]["topic_selected"]
    generated_at = data["metadata"]["generated_at"]

    posts = data["posts"]

    # 各案の全文を取得
    post_details = []
    for i, post in enumerate(posts, 1):
        post_details.append({
            "variant": post["variant"],
            "rating": post["rating"],
            "er": post["predicted_er"],
            "count": post["character_count"],
            "content": post["content"],  # 全文を使用
            "recommended": "✅ 推奨" if post.get("recommended") else ""
        })

    # Slackメッセージテキスト作成（全文表示）
    message_text = f"""
🚀 *LinkedIn投稿3案生成完了*

*トピック*: {topic}
*生成日時*: {generated_at}
*高野メソッド準拠率*: 100%

━━━━━━━━━━━━━━━━━━━━

*案1: {post_details[0]['variant']}* ({post_details[0]['rating']}) {post_details[0]['recommended']}
文字数: {post_details[0]['count']}字 | 予測ER: {post_details[0]['er']}

{post_details[0]['content']}

━━━━━━━━━━━━━━━━━━━━

*案2: {post_details[1]['variant']}* ({post_details[1]['rating']}) {post_details[1]['recommended']}
文字数: {post_details[1]['count']}字 | 予測ER: {post_details[1]['er']}

{post_details[1]['content']}

━━━━━━━━━━━━━━━━━━━━

*案3: {post_details[2]['variant']}* ({post_details[2]['rating']}) {post_details[2]['recommended']}
文字数: {post_details[2]['count']}字 | 予測ER: {post_details[2]['er']}

{post_details[2]['content']}

━━━━━━━━━━━━━━━━━━━━

✅ *承認方法*: このスレッドに「1」「2」「3」のいずれかを返信してください。
⏱️ タイムアウト: 24時間（返信がない場合は推奨案を自動承認）
"""

    return message_text

def send_slack_message(message_text):
    """Slackにメッセージを送信"""
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    }

    payload = {
        "channel": SLACK_CHANNEL,
        "text": message_text,
        "unfurl_links": False,
        "unfurl_media": False
    }

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers=headers,
        json=payload
    )

    result = response.json()

    if result.get("ok"):
        print(f"✅ Slack通知送信成功")
        print(f"   チャンネル: {result.get('channel')}")
        print(f"   タイムスタンプ: {result.get('ts')}")
        return result.get("ts")
    else:
        print(f"❌ Slack通知送信失敗: {result.get('error')}")
        return None

def check_thread_replies(thread_ts, timeout=300):
    """スレッド返信をチェック（ポーリング）"""
    print("\n⏳ Slack承認待機中...")
    print(f"   Slackの #{SLACK_CHANNEL} チャンネルのスレッドに「1」「2」「3」を返信してください")
    print(f"   タイムアウト: {timeout}秒")

    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }

    start_time = time.time()
    check_interval = 10  # 10秒ごとにチェック

    while time.time() - start_time < timeout:
        # スレッドの返信を取得
        response = requests.get(
            "https://slack.com/api/conversations.replies",
            headers=headers,
            params={
                "channel": SLACK_CHANNEL,
                "ts": thread_ts
            }
        )

        result = response.json()

        if result.get("ok"):
            messages = result.get("messages", [])

            # 最初のメッセージ（親メッセージ）をスキップし、返信のみをチェック
            for msg in messages[1:]:
                text = msg.get("text", "").strip()

                if text in ["1", "2", "3"]:
                    print(f"\n✅ 案{text}が承認されました！")
                    print(f"   承認者: {msg.get('user')}")
                    print(f"   承認時刻: {datetime.fromtimestamp(float(msg.get('ts')))}")
                    return text

        # 待機
        time.sleep(check_interval)
        elapsed = int(time.time() - start_time)
        print(f"   経過時間: {elapsed}秒 / {timeout}秒", end="\r")

    print("\n⚠️  タイムアウト: 推奨案（案2）を自動承認します")
    return "2"

def main():
    print("=" * 60)
    print("Slack承認テスト開始")
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

    # Slackメッセージ作成
    print(f"\n📝 Slack通知メッセージ作成中...")
    message_text = create_slack_message(data)
    print(f"✅ メッセージ作成完了（{len(message_text)}文字）")

    # Slack送信
    print(f"\n📤 Slack通知送信中...")
    thread_ts = send_slack_message(message_text)

    if not thread_ts:
        print("❌ テスト失敗")
        return

    # 承認待機
    approved_variant = check_thread_replies(thread_ts, timeout=300)  # 5分タイムアウト（テスト用）

    # 結果保存
    approval_result = {
        "approved_variant": f"案{approved_variant}",
        "approved_at": datetime.now().isoformat(),
        "thread_ts": thread_ts,
        "test_mode": True
    }

    output_file = f"/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/approval_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(approval_result, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 承認結果保存: {output_file}")
    print(f"\n承認された案: 案{approved_variant}")
    print("\n" + "=" * 60)
    print("Slack承認テスト完了")
    print("=" * 60)

if __name__ == "__main__":
    main()
