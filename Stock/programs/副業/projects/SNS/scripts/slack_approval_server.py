#!/usr/bin/env python3
"""
Slack Interactive Buttons受信サーバー（Flask）
ボタンクリックを受信して承認結果をファイルに保存
スレッド返信で修正フィードバック対応
"""
from flask import Flask, request, jsonify
import os
import json
from datetime import datetime
import hashlib
import hmac
import subprocess
import re
import requests

app = Flask(__name__)

# 環境変数
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL")
SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
SCRIPTS_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts"


def verify_slack_request(request):
    """
    Slack署名検証（セキュリティ）
    https://api.slack.com/authentication/verifying-requests-from-slack
    """
    if not SLACK_SIGNING_SECRET:
        print("⚠️  SLACK_SIGNING_SECRET未設定 - 署名検証スキップ")
        return True

    timestamp = request.headers.get("X-Slack-Request-Timestamp", "")
    slack_signature = request.headers.get("X-Slack-Signature", "")

    # リプレイ攻撃防止（5分以内のリクエストのみ受付）
    if abs(datetime.now().timestamp() - int(timestamp)) > 60 * 5:
        return False

    # 署名検証
    sig_basestring = f"v0:{timestamp}:{request.get_data().decode('utf-8')}"
    my_signature = "v0=" + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(my_signature, slack_signature)


def parse_refine_instruction(message_text):
    """
    修正指示を解析（refine_post_variant.pyと同じロジック）

    Returns:
        tuple: (variant_num, instruction) or (None, None)
    """
    # パターン1: 案N をに .+
    pattern1 = r'案(\d+)\s*[をに]\s*(.+)'
    match = re.search(pattern1, message_text)
    if match:
        return int(match.group(1)), match.group(2).strip()

    # パターン2: 案N: .+ or 案N .+
    pattern2 = r'案(\d+)[:：\s]\s*(.+)'
    match = re.search(pattern2, message_text)
    if match:
        return int(match.group(1)), match.group(2).strip()

    return None, None


def post_slack_message(thread_ts, text, blocks=None):
    """Slackスレッドにメッセージを投稿"""
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    }

    payload = {
        "channel": SLACK_CHANNEL,
        "thread_ts": thread_ts,
        "text": text
    }

    if blocks:
        payload["blocks"] = blocks

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers=headers,
        json=payload
    )

    return response.json()


def handle_thread_reply(event):
    """
    Slackスレッド返信を解析して修正処理を実行
    """
    thread_ts = event["thread_ts"]
    message_text = event["text"]
    user_id = event["user"]
    user_name = event.get("username", user_id)

    print(f"\n📨 スレッド返信受信")
    print(f"   ユーザー: {user_name} ({user_id})")
    print(f"   メッセージ: {message_text}")
    print(f"   thread_ts: {thread_ts}")

    # Bot自身のメッセージは無視
    if event.get("bot_id"):
        print("   → Bot自身のメッセージのためスキップ")
        return

    # 修正指示解析
    variant_num, instruction = parse_refine_instruction(message_text)

    if variant_num is None:
        print("   → 修正指示として認識できませんでした")
        return

    print(f"   → 修正対象: 案{variant_num}, 指示: {instruction}")

    # 修正回数チェック
    refine_context_file = os.path.join(SNS_DATA_DIR, f"refine_context_{thread_ts}.json")
    if os.path.exists(refine_context_file):
        with open(refine_context_file, "r", encoding="utf-8") as f:
            context = json.load(f)
        if context["refine_count"] >= 10:
            post_slack_message(thread_ts, "⚠️ 修正回数が上限（10回）に達しました。新しい承認フローを開始してください。")
            print("   → 修正回数上限到達")
            return

    # 処理中メッセージ
    post_slack_message(thread_ts, f"🔄 案{variant_num}を修正中...（5-10秒お待ちください）")

    # refine_post_variant_claudecode.py をsubprocessで実行（ClaudeCode統合版）
    try:
        result = subprocess.run(
            ["python3", "refine_post_variant_claudecode.py", str(variant_num), instruction, thread_ts],
            capture_output=True,
            text=True,
            cwd=SCRIPTS_DIR,
            timeout=120
        )

        if result.returncode != 0:
            error_msg = result.stderr or result.stdout
            print(f"   ❌ 修正処理エラー: {error_msg}")
            post_slack_message(thread_ts, f"❌ 修正処理でエラーが発生しました:\n```{error_msg}```")
            return

        # 修正結果を取得
        print(f"   📄 stdout: {result.stdout[:200]}")  # デバッグ用
        print(f"   📄 stderr: {result.stderr[:200]}")  # デバッグ用

        if not result.stdout or not result.stdout.strip():
            print(f"   ❌ 修正処理の出力が空です")
            print(f"   stderr: {result.stderr}")
            post_slack_message(thread_ts, f"❌ 修正処理の出力が空です。詳細はログを確認してください。")
            return

        try:
            refine_result = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            print(f"   ❌ JSON解析エラー: {str(e)}")
            print(f"   stdout: {result.stdout}")
            print(f"   stderr: {result.stderr}")
            post_slack_message(thread_ts, f"❌ 修正結果の解析に失敗しました:\n```{str(e)}\nstdout: {result.stdout[:100]}```")
            return

        if not refine_result.get("success"):
            print(f"   ❌ 修正失敗: {refine_result.get('error')}")
            post_slack_message(thread_ts, f"❌ {refine_result.get('error')}")
            return

        print(f"   ✅ 修正成功（修正回数: {refine_result['refine_count']}）")

        # 修正案を投稿
        post_refined_variant(thread_ts, refine_result)

    except subprocess.TimeoutExpired:
        print("   ❌ タイムアウト（120秒超過）")
        post_slack_message(thread_ts, "❌ 修正処理がタイムアウトしました（120秒超過）")
    except Exception as e:
        print(f"   ❌ 予期しないエラー: {str(e)}")
        post_slack_message(thread_ts, f"❌ 予期しないエラー: {str(e)}")


def post_refined_variant(thread_ts, refine_result):
    """修正案をSlackスレッドに投稿（承認ボタン付き）"""
    refined_post = refine_result["refined_post"]
    refine_count = refine_result["refine_count"]
    variant_num = refined_post["refined_from"]

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"🔄 修正案{refine_count}回目（元: 案{variant_num}）",
                "emoji": True
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*バリエーション:*\n{refined_post['variant']}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*評価:*\n{refined_post['rating']}"
                }
            ]
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*文字数:* {refined_post['character_count']}字 | *予測ER:* {refined_post['predicted_er']}\n\n{refined_post['content']}"
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "✅ 修正案を承認",
                        "emoji": True
                    },
                    "value": f"refined_variant_{variant_num}_{refine_count}",
                    "action_id": f"approve_refined_variant_{variant_num}",
                    "style": "primary"
                }
            ]
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"残り修正回数: {3 - refine_count}回"
                }
            ]
        }
    ]

    # スレッド返信として投稿
    post_slack_message(thread_ts, f"修正案{refine_count}回目が生成されました", blocks=blocks)


@app.route("/slack/events", methods=["POST"])
def handle_slack_events():
    """Slack Events API（スレッド返信受信）"""
    payload = request.json

    print(f"\n📡 Slack Event受信")
    print(f"   Type: {payload.get('type')}")

    # URL Verification Challenge（初回設定時）
    if payload.get("type") == "url_verification":
        return jsonify({"challenge": payload["challenge"]})

    # Event受信
    if payload.get("type") == "event_callback":
        event = payload["event"]
        print(f"   Event Type: {event.get('type')}")
        print(f"   Event Keys: {list(event.keys())}")
        print(f"   Has thread_ts: {'thread_ts' in event}")

        # スレッド返信のみ処理
        if event.get("type") == "message" and "thread_ts" in event:
            handle_thread_reply(event)
        else:
            print(f"   → 条件不一致: type={event.get('type')}, thread_ts={'thread_ts' in event}")

    return jsonify({"status": "ok"}), 200


@app.route("/slack/interactive", methods=["POST"])
def handle_slack_interaction():
    """
    Slackのボタンクリックを受信するエンドポイント
    """
    # 署名検証
    if not verify_slack_request(request):
        return jsonify({"error": "Invalid signature"}), 403

    # Slackから送られるpayloadはform-encoded
    payload = json.loads(request.form.get("payload"))

    # アクション情報を取得
    action = payload["actions"][0]
    action_id = action["action_id"]
    variant_value = action["value"]
    user_id = payload["user"]["id"]
    user_name = payload["user"]["name"]

    print(f"\n📥 ボタンクリック受信")
    print(f"   アクション: {action_id}")
    print(f"   値: {variant_value}")
    print(f"   ユーザー: {user_name} ({user_id})")

    # 修正案承認の場合
    if "approve_refined_variant_" in action_id:
        variant_num = action_id.replace("approve_refined_variant_", "")

        # thread_ts取得（メッセージまたはコンテナから）
        thread_ts = payload.get("message", {}).get("thread_ts") or payload.get("container", {}).get("thread_ts")

        # refine_context から修正案内容を取得
        refine_context_file = os.path.join(SNS_DATA_DIR, f"refine_context_{thread_ts}.json")

        if not os.path.exists(refine_context_file):
            return jsonify({
                "response_type": "ephemeral",
                "text": "❌ 修正履歴が見つかりません"
            }), 400

        with open(refine_context_file, "r", encoding="utf-8") as f:
            context = json.load(f)

        # 最新の修正案を取得
        if not context["history"]:
            return jsonify({
                "response_type": "ephemeral",
                "text": "❌ 修正履歴が空です"
            }), 400

        latest_refined = context["history"][-1]

        # approval_result に保存
        approval_data = {
            "approved": True,
            "variant": f"案{variant_num}（修正版）",
            "refined": True,
            "refined_content": latest_refined["refined_content"],
            "refine_count": context["refine_count"],
            "instruction": latest_refined["instruction"],
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "user_name": user_name
        }

        approval_file = os.path.join(
            SNS_DATA_DIR,
            f"approval_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        with open(approval_file, "w", encoding="utf-8") as f:
            json.dump(approval_data, f, ensure_ascii=False, indent=2)

        print(f"✅ 修正案承認結果保存: {approval_file}")

        # 承認完了メッセージを投稿
        post_slack_message(
            thread_ts,
            f"✅ 修正案{context['refine_count']}回目が承認されました！\n投稿をスケジューリングします。\n承認者: <@{user_id}>"
        )

        # ボタンを無効化した状態でメッセージを更新
        return jsonify({
            "response_type": "in_channel",
            "replace_original": True,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"✅ *修正案{context['refine_count']}回目が承認されました*\n承認者: <@{user_id}>"
                    }
                }
            ],
            "text": f"✅ 修正案{context['refine_count']}回目が承認されました"
        })

    # 通常の承認処理（元の案）
    if "approve_variant_" in action_id:
        variant_num = action_id.replace("approve_variant_", "")
        approved_variant = f"案{variant_num}"

        # 承認結果を保存
        approval_data = {
            "approved": True,
            "variant": approved_variant,
            "refined": False,
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "user_name": user_name
        }

        # 承認結果をファイルに保存
        approval_file = os.path.join(
            SNS_DATA_DIR,
            f"approval_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        with open(approval_file, "w", encoding="utf-8") as f:
            json.dump(approval_data, f, ensure_ascii=False, indent=2)

        print(f"✅ 承認結果保存: {approval_file}")

        # Slackに応答（メッセージを更新して承認済みを表示）
        return jsonify({
            "response_type": "in_channel",
            "replace_original": True,
            "text": f"✅ {approved_variant}が承認されました！\n投稿をスケジューリングします。\n承認者: @{user_name}"
        })

    # 不明なアクション
    return jsonify({
        "response_type": "ephemeral",
        "text": "❌ Invalid action"
    }), 400


@app.route("/health", methods=["GET"])
def health_check():
    """ヘルスチェック用エンドポイント"""
    return jsonify({"status": "ok", "service": "slack-approval-server"}), 200


if __name__ == "__main__":
    print("=" * 60)
    print("Slack Interactive Buttons受信サーバー起動")
    print("=" * 60)
    print(f"\n📡 リスニング中: http://0.0.0.0:5000")
    print(f"   エンドポイント: /slack/interactive")
    print(f"   ヘルスチェック: /health")
    print(f"\n⚠️  ngrokでRequest URLを設定してください:")
    print(f"   1. 別ターミナルで: ngrok http 5000")
    print(f"   2. Forwarding URLをコピー（例: https://xxxx.ngrok-free.app）")
    print(f"   3. Slack App Management > Interactivity & Shortcuts > Request URL")
    print(f"   4. Request URLに設定: https://xxxx.ngrok-free.app/slack/interactive")
    print("\n" + "=" * 60)

    # サーバー起動（0.0.0.0で外部アクセス許可）
    # ポート5000が使用中の場合は5001を使用
    port = int(os.environ.get("FLASK_PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
