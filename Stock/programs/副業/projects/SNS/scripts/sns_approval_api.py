#!/usr/bin/env python3
"""
SNS Approval API Server
React Webアプリケーション用のFlask APIバックエンド
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
# APSchedulerは削除（Late API統合により不要）
# from flask_apscheduler import APScheduler
import json
import glob
import os
from datetime import datetime
import uuid
import sys
import traceback
import logging
import subprocess
from dotenv import load_dotenv

# .env ファイルから環境変数を読み込み
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)

# ロギング設定
log_dir = '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/logs'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'api.log'),
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# refine_post_variant_claudecode.py から関数をimport（将来的に統合）
# 現時点ではスタブとして実装
sys.path.append('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts')

# ApprovalQueueManagerをimport
from approval_queue_manager import ApprovalQueueManager

app = Flask(__name__)
# すべてのlocalhostポート（3000-3010）を許可
CORS(app, resources={r"/api/*": {"origins": [
    "http://localhost:3000", "http://127.0.0.1:3000",
    "http://localhost:3001", "http://127.0.0.1:3001",
    "http://localhost:3002", "http://127.0.0.1:3002",
    "http://localhost:3003", "http://127.0.0.1:3003",
    "http://localhost:3004", "http://127.0.0.1:3004",
    "http://localhost:3005", "http://127.0.0.1:3005",
    "http://localhost:3006", "http://127.0.0.1:3006",
    "http://localhost:3007", "http://127.0.0.1:3007",
    "http://localhost:3008", "http://127.0.0.1:3008",
    "http://localhost:3009", "http://127.0.0.1:3009",
    "http://localhost:3010", "http://127.0.0.1:3010"
]}})

# APSchedulerは削除（Late API統合により不要）
# Late API経由で直接スケジューリング予約を実行

# データディレクトリ
SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
SCRIPTS_DIR = os.path.dirname(__file__)

# ApprovalQueueManager初期化
approval_manager = ApprovalQueueManager(SNS_DATA_DIR)


@app.route("/api/posts", methods=["GET"])
def get_posts():
    """
    posts_generated_*.json から最新の3案を取得
    ※ 未承認の投稿案がある場合は警告を返す

    Returns:
        JSON: {
            "variant_1": {...},
            "variant_2": {...},
            "variant_3": {...},
            "metadata": {...},
            "warnings": [...] (optional)
        }
    """
    try:
        # 未承認投稿案の数をチェック
        pending_count = approval_manager.check_pending_count()
        warnings = []

        if pending_count > 0:
            warnings.append({
                "type": "PENDING_POSTS_EXIST",
                "message": f"未承認の投稿案が{pending_count}件あります",
                "pending_count": pending_count
            })

        posts_files = glob.glob(f"{SNS_DATA_DIR}/posts_generated_*.json")

        if not posts_files:
            return jsonify({
                "error": "No posts found",
                "message": "posts_generated_*.json ファイルが見つかりません"
            }), 404

        # 最新ファイルを取得
        latest_file = max(posts_files, key=os.path.getctime)

        with open(latest_file, 'r', encoding='utf-8') as f:
            posts_data = json.load(f)

        # メタデータ追加
        posts_data["metadata"] = {
            "file": os.path.basename(latest_file),
            "loaded_at": datetime.now().isoformat()
        }

        # 警告を追加
        if warnings:
            posts_data["warnings"] = warnings

        return jsonify(posts_data), 200

    except json.JSONDecodeError as e:
        return jsonify({
            "error": "Invalid JSON format",
            "message": str(e)
        }), 500

    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "message": str(e),
            "traceback": traceback.format_exc()
        }), 500


@app.route("/api/posts/generate-and-queue", methods=["POST"])
def generate_and_queue():
    """
    新規投稿案を生成してキューに追加

    このエンドポイントは将来的に投稿案生成スクリプトと統合します。
    現時点では、posts_generated_*.json を手動生成後にキューに追加する機能のみ。

    Returns:
        JSON: {
            "success": true,
            "queue_id": "abc12345",
            "pending_count": 1
        }
    """
    try:
        # 最新のposts_generated_*.json を取得
        posts_files = glob.glob(f"{SNS_DATA_DIR}/posts_generated_*.json")

        if not posts_files:
            return jsonify({
                "error": "No posts found",
                "message": "キューに追加する投稿案がありません"
            }), 404

        latest_file = max(posts_files, key=os.path.getctime)

        with open(latest_file, 'r', encoding='utf-8') as f:
            posts_data = json.load(f)

        # キューに追加
        queue_id = approval_manager.add_to_queue(posts_data)

        logger.info(f"Added to queue: {queue_id}, file: {latest_file}")

        return jsonify({
            "success": True,
            "queue_id": queue_id,
            "pending_count": approval_manager.check_pending_count(),
            "message": "投稿案をキューに追加しました"
        }), 200

    except Exception as e:
        logger.error(f"Failed to add to queue: {e}")
        return jsonify({
            "error": "Failed to add to queue",
            "message": str(e)
        }), 500


@app.route("/api/approve", methods=["POST"])
def approve_post():
    """
    選択された投稿案を approval_result_*.json に保存し、
    元の posts_generated_*.json も更新する

    Expected JSON:
        {
            "variant": "案1" | "案2" | "案3",
            "content": "投稿内容",
            "refined": bool,
            "refined_content": "修正後の内容" (optional)
        }

    Returns:
        JSON: {"success": true, "file": "approval_result_*.json"}
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data provided",
                "message": "JSONデータが送信されていません"
            }), 400

        # 必須フィールドチェック
        required_fields = ["variant", "content"]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": f"Missing required field: {field}",
                    "message": f"必須フィールド '{field}' がありません"
                }), 400

        variant_num = data.get("variant")
        refined_content = data.get("refined_content")

        # 承認データ構築
        approval_data = {
            "approved": True,
            "variant": variant_num,
            "content": data.get("content"),
            "refined": data.get("refined", False),
            "refined_content": refined_content,
            "timestamp": datetime.now().isoformat(),
            "user_id": "web_user",
            "user_name": "Web UI"
        }

        # ファイル名生成
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        approval_file = f"{SNS_DATA_DIR}/approval_result_{timestamp}.json"

        # Phase A: approved_post_*.json も同時保存（SNS自動化スキルとの統合用）
        approved_post_file = f"{SNS_DATA_DIR}/approved_post_{timestamp}.json"

        # approved_post形式データ構築（既存のapprove-and-scheduleスキルと互換性確保）
        approved_post_data = {
            "approved": True,
            "approved_at": approval_data["timestamp"],
            "approved_variant": variant_num,
            "content": refined_content if refined_content else data.get("content"),
            "refined": data.get("refined", False),
            "refined_content": refined_content,
            "variant": variant_num,
            "user_id": "web_user",
            "user_name": "Web UI"
        }

        # 保存（approval_result_*.json）
        with open(approval_file, "w", encoding='utf-8') as f:
            json.dump(approval_data, f, ensure_ascii=False, indent=2)

        # 保存（approved_post_*.json）
        with open(approved_post_file, "w", encoding='utf-8') as f:
            json.dump(approved_post_data, f, ensure_ascii=False, indent=2)

        logger.info(f"Approval saved: {approval_file}, {approved_post_file}")

        # 元の posts_generated_*.json を更新（編集内容を反映）
        if refined_content:
            posts_files = glob.glob(f"{SNS_DATA_DIR}/posts_generated_*.json")
            if posts_files:
                latest_file = max(posts_files, key=os.path.getctime)

                with open(latest_file, 'r', encoding='utf-8') as f:
                    posts_data = json.load(f)

                # variant_numから該当するvariantキーを取得
                variant_key_map = {"案1": "variant_1", "案2": "variant_2", "案3": "variant_3"}
                variant_key = variant_key_map.get(variant_num)

                if variant_key and variant_key in posts_data:
                    # 編集内容を反映
                    posts_data[variant_key]["content"] = refined_content
                    posts_data[variant_key]["edited"] = True
                    posts_data[variant_key]["edited_at"] = datetime.now().isoformat()

                    # 更新を保存
                    with open(latest_file, 'w', encoding='utf-8') as f:
                        json.dump(posts_data, f, ensure_ascii=False, indent=2)

                    logger.info(f"Updated {latest_file} with edited content for {variant_num}")

        return jsonify({
            "success": True,
            "approval_file": os.path.basename(approval_file),
            "approved_post_file": os.path.basename(approved_post_file),
            "timestamp": approval_data["timestamp"],
            "updated_posts": refined_content is not None
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to save approval",
            "message": str(e),
            "traceback": traceback.format_exc()
        }), 500


@app.route("/api/refine", methods=["POST"])
def refine_variant():
    """
    AI修正を実行（将来的にrefine_post関数を統合）

    Expected JSON:
        {
            "variant_num": "案1" | "案2" | "案3",
            "instruction": "修正指示",
            "session_id": "セッションID" (optional)
        }

    Returns:
        JSON: {
            "success": true,
            "refined_content": "修正後の内容",
            "session_id": "セッションID"
        }
    """
    try:
        data = request.get_json()

        if not data:
            logger.warning("Refine request received with no data")
            return jsonify({
                "error": "No data provided",
                "message": "JSONデータが送信されていません"
            }), 400

        variant_num = data.get("variant_num")
        instruction = data.get("instruction")
        session_id = data.get("session_id", str(uuid.uuid4()))

        # リクエスト情報をログに記録
        instruction_preview = instruction[:50] + "..." if instruction and len(instruction) > 50 else instruction
        logger.info(f"Refine request received: variant={variant_num}, instruction={instruction_preview}, session={session_id}")

        # 必須フィールドチェック
        if not variant_num or not instruction:
            return jsonify({
                "error": "Missing required fields",
                "message": "variant_num と instruction は必須です"
            }), 400

        # 元の投稿内容を取得
        posts_files = glob.glob(f"{SNS_DATA_DIR}/posts_generated_*.json")
        if not posts_files:
            return jsonify({
                "error": "No posts found",
                "message": "posts_generated_*.json ファイルが見つかりません"
            }), 404

        latest_file = max(posts_files, key=os.path.getctime)
        with open(latest_file, 'r', encoding='utf-8') as f:
            posts_data = json.load(f)

        # variant_numから該当するvariantキーを取得（"案1" -> "variant_1", "案2" -> "variant_2", "案3" -> "variant_3"）
        variant_key_map = {"案1": "variant_1", "案2": "variant_2", "案3": "variant_3"}
        variant_key = variant_key_map.get(variant_num)

        if not variant_key or variant_key not in posts_data:
            return jsonify({
                "error": "Invalid variant",
                "message": f"該当する投稿案が見つかりません: {variant_num}"
            }), 400

        original_content = posts_data[variant_key]["content"]

        # OpenAI APIでAI修正を実行
        from openai import OpenAI

        # OpenAI APIキーを環境変数から取得
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            logger.error("OPENAI_API_KEY not found in environment variables")
            return jsonify({
                "error": "Configuration error",
                "message": "OpenAI APIキーが設定されていません"
            }), 500

        client = OpenAI(api_key=openai_api_key)

        prompt = f"""以下の投稿内容を、指示に従って修正してください。

【元の投稿内容】
{original_content}

【修正指示】
{instruction}

【重要】
- 修正後の投稿内容のみを出力してください（説明は不要です）
- 元の文体とトーンを維持してください
- ハッシュタグは適切に残してください
- 出力は修正後のテキストのみとし、余計な説明や装飾は一切含めないでください"""

        try:
            # OpenAI API呼び出し（gpt-5.2-chat-latestを使用）
            # gpt-5.2-chat-latest: 低レイテンシ版（リアルタイム会話・チャットボット向け）
            logger.info(f"Starting OpenAI API execution for session {session_id}")
            response = client.chat.completions.create(
                model="gpt-5.2-chat-latest",
                messages=[
                    {"role": "system", "content": "あなたはSNS投稿の編集アシスタントです。指示に従って投稿内容を修正し、修正後のテキストのみを返してください。"},
                    {"role": "user", "content": prompt}
                ],
                # GPT-5.2では temperature はデフォルト値(1)のみサポート
                max_completion_tokens=1000  # GPT-5.2では max_tokens の代わりに max_completion_tokens を使用
            )

            # APIレスポンスから修正内容を抽出
            refined_content = response.choices[0].message.content.strip()
            logger.info(f"OpenAI API execution completed: output_length={len(refined_content)}")

            # 出力の妥当性チェック
            if not refined_content:
                logger.error("OpenAI API returned empty output")
                raise Exception("OpenAI API returned empty output")

            # 長さチェック（元の投稿と大きく異なる場合は警告）
            if len(refined_content) < len(original_content) * 0.3:
                logger.warning(f"Refined content is too short: original={len(original_content)}, refined={len(refined_content)}")
                return jsonify({
                    "error": "Output validation failed",
                    "message": "修正後の内容が短すぎます。再度お試しください。",
                    "original_length": len(original_content),
                    "refined_length": len(refined_content),
                    "retry": True
                }), 422

            # 特定の禁止パターンチェック（エラーメッセージの混入など）
            if "error" in refined_content.lower()[:100] or "failed" in refined_content.lower()[:100]:
                logger.warning(f"Potential error message in output: {refined_content[:100]}")
                return jsonify({
                    "error": "Invalid output detected",
                    "message": "AIの出力にエラーメッセージが含まれている可能性があります",
                    "refined_content": refined_content,
                    "retry": True
                }), 422

        except Exception as e:
            logger.error(f"OpenAI API error for session {session_id}: {str(e)}")
            return jsonify({
                "error": "AI modification failed",
                "message": f"AI修正に失敗しました: {str(e)}",
                "retry": True
            }), 500

        # 修正履歴を保存（失敗しても修正結果は返す）
        try:
            context_file = f"{SNS_DATA_DIR}/refine_context_{session_id}.json"

            if os.path.exists(context_file):
                with open(context_file, 'r', encoding='utf-8') as f:
                    context = json.load(f)
            else:
                context = {
                    "session_id": session_id,
                    "variant": variant_num,
                    "original_content": original_content,
                    "history": []
                }

            # 履歴追加
            context["history"].append({
                "instruction": instruction,
                "refined_content": refined_content,
                "timestamp": datetime.now().isoformat(),
                "status": "completed"
            })

            with open(context_file, 'w', encoding='utf-8') as f:
                json.dump(context, f, ensure_ascii=False, indent=2)

            logger.info(f"Refine history saved: session={session_id}, history_count={len(context['history'])}")

        except Exception as e:
            # 履歴保存失敗しても修正結果は返す
            logger.warning(f"Failed to save refine history: {e}")
            # このエラーは無視（修正結果は正常）

        logger.info(f"Refine request completed successfully: session={session_id}")
        return jsonify({
            "success": True,
            "refined_content": refined_content,
            "session_id": session_id,
            "original_content": original_content
        }), 200

    except Exception as e:
        logger.error(f"Refine request failed: {e}", exc_info=True)
        return jsonify({
            "error": "Failed to refine post",
            "message": str(e),
            "traceback": traceback.format_exc()
        }), 500


@app.route("/api/refine/<session_id>", methods=["GET"])
def get_refine_history(session_id):
    """
    修正履歴を取得

    Returns:
        JSON: {
            "session_id": "...",
            "variant": "案1",
            "history": [...]
        }
    """
    try:
        context_file = f"{SNS_DATA_DIR}/refine_context_{session_id}.json"

        if not os.path.exists(context_file):
            return jsonify({
                "error": "Session not found",
                "message": f"セッションID '{session_id}' が見つかりません"
            }), 404

        with open(context_file, 'r', encoding='utf-8') as f:
            context = json.load(f)

        return jsonify(context), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to get refine history",
            "message": str(e),
            "traceback": traceback.format_exc()
        }), 500


@app.route("/api/schedule", methods=["POST"])
def schedule_post():
    """
    Phase C: 承認された投稿をLate API経由でスケジュール予約

    Expected JSON:
        {
            "platforms": ["X", "Threads", "LinkedIn"],
            "scheduled_time": "2026-01-04T20:00:00+09:00" (ISO 8601形式、必須)
        }

    Returns:
        JSON: {
            "success": true,
            "job_id": "post_scheduled_...",
            "scheduled_time": "...",
            "platforms": [...],
            "late_post_id": "Late APIから返されたpost ID"
        }
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data provided",
                "message": "JSONデータが送信されていません"
            }), 400

        # 必須フィールドチェック
        if "scheduled_time" not in data:
            return jsonify({
                "error": "Missing required field",
                "message": "scheduled_time は必須です（ISO 8601形式）"
            }), 400

        # 最新の approved_post_*.json を読み込み
        approved_files = glob.glob(f"{SNS_DATA_DIR}/approved_post_*.json")

        if not approved_files:
            return jsonify({
                "error": "No approval found",
                "message": "approved_post_*.json が見つかりません。先に投稿を承認してください。"
            }), 404

        latest_approved = max(approved_files, key=os.path.getctime)

        # ジョブID生成
        job_id = f"post_scheduled_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # プラットフォームリスト
        platforms = data.get("platforms", ["LinkedIn", "X", "Facebook", "Threads"])

        # スケジューリング時刻（ISO 8601形式）
        scheduled_time = data["scheduled_time"]

        # post_to_sns_late.py を呼び出し（Late API経由でスケジュール予約）
        cmd = [
            "python3",
            os.path.join(SCRIPTS_DIR, "post_to_sns_late.py"),
            "--file", os.path.basename(latest_approved),
            "--platforms", *platforms,
            "--scheduled-time", scheduled_time,
            "--scheduled-post-id", job_id
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f"post_to_sns_late.py failed: {result.stderr}")

            # Late APIエラーの詳細を抽出
            error_message = "Late APIスケジューリングに失敗しました"
            error_details = None

            # stderrから詳細なエラーメッセージを抽出
            if "Cast to ObjectId failed" in result.stderr:
                if "facebook" in result.stderr.lower():
                    error_message = "Facebookアカウントが未設定です"
                    error_details = "Late APIダッシュボードでFacebookアカウントを接続してください。または、Facebookを除外して再試行してください。"
                else:
                    error_message = "無効なアカウントIDが指定されています"
                    error_details = ".envファイルのアカウントID設定を確認してください"
            elif "500 Server Error" in result.stderr:
                error_message = "Late APIサーバーエラー"
                error_details = "Late APIに問題が発生しています。しばらく待ってから再試行してください。"
            elif "401" in result.stderr or "Unauthorized" in result.stderr:
                error_message = "Late API認証エラー"
                error_details = "APIキーが無効です。.envファイルのLATE_API_KEYを確認してください。"
            elif "404" in result.stderr:
                error_message = "アカウントが見つかりません"
                error_details = "Late APIダッシュボードでアカウントが接続されているか確認してください。"

            return jsonify({
                "error": error_message,
                "details": error_details,
                "stderr": result.stderr,
                "stdout": result.stdout
            }), 500

        logger.info(f"Scheduled post via Late API: job_id={job_id}, scheduled_time={scheduled_time}, platforms={platforms}")
        logger.info(f"Late API output: {result.stdout}")

        return jsonify({
            "success": True,
            "job_id": job_id,
            "scheduled_time": scheduled_time,
            "platforms": platforms,
            "approved_file": os.path.basename(latest_approved),
            "late_api_output": result.stdout
        }), 200

    except Exception as e:
        logger.error(f"Failed to schedule post: {e}", exc_info=True)
        return jsonify({
            "error": "Failed to schedule post",
            "message": str(e),
            "traceback": traceback.format_exc()
        }), 500


# execute_scheduled_post関数は削除（Late API統合により不要）
# Late API経由で直接スケジューリング予約を行うため、APSchedulerのコールバックは不要


@app.route("/api/scheduled-jobs", methods=["GET"])
def get_scheduled_jobs():
    """
    Late API経由でスケジュール済み投稿を取得

    NOTE: Late APIにはジョブ一覧取得APIがないため、
    post_result_*.json ファイルから情報を取得

    Returns:
        JSON: {
            "jobs": [
                {
                    "job_id": "...",
                    "scheduled_time": "...",
                    "platforms": [...],
                    "late_post_id": "..."
                }
            ]
        }
    """
    try:
        jobs = []

        # post_result_*.json ファイルを検索
        result_files = glob.glob(os.path.join(SNS_DATA_DIR, "post_result_*.json"))

        for result_file in result_files:
            try:
                with open(result_file, "r", encoding="utf-8") as f:
                    result_data = json.load(f)

                # Late APIのレスポンスから情報を抽出
                post_data = result_data.get("post", {})
                jobs.append({
                    "job_id": os.path.basename(result_file).replace("post_result_", "").replace(".json", ""),
                    "scheduled_time": post_data.get("scheduledFor"),
                    "platforms": [p.get("platform") for p in post_data.get("platforms", [])],
                    "late_post_id": post_data.get("_id"),
                    "status": post_data.get("status", "unknown")
                })
            except Exception as e:
                logger.warning(f"Failed to parse {result_file}: {e}")
                continue

        return jsonify({
            "jobs": jobs,
            "count": len(jobs)
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to get scheduled jobs",
            "message": str(e)
        }), 500


@app.route("/api/queue/pending", methods=["GET"])
def get_pending_queue():
    """未承認投稿案の一覧を取得"""
    try:
        pending_posts = approval_manager.get_pending_posts()
        return jsonify({
            "pending_posts": pending_posts,
            "count": len(pending_posts)
        }), 200
    except Exception as e:
        logger.error(f"Failed to get pending queue: {e}")
        return jsonify({
            "error": "Failed to get pending queue",
            "message": str(e)
        }), 500


@app.route("/api/queue/approved", methods=["GET"])
def get_approved_queue():
    """承認済み投稿案の一覧を取得（スケジュール待ち）"""
    try:
        approved_posts = approval_manager.get_approved_posts()
        return jsonify({
            "approved_posts": approved_posts,
            "count": len(approved_posts)
        }), 200
    except Exception as e:
        logger.error(f"Failed to get approved queue: {e}")
        return jsonify({
            "error": "Failed to get approved queue",
            "message": str(e)
        }), 500


@app.route("/api/queue/approve", methods=["POST"])
def approve_from_queue():
    """
    投稿案を承認してapproved/に移動

    Expected JSON:
        {
            "queue_id": "abc12345",
            "variant_index": 0,
            "refined_content": "修正後の内容" (optional)
        }
    """
    try:
        data = request.get_json()
        queue_id = data.get("queue_id")
        variant_index = data.get("variant_index", 0)
        refined_content = data.get("refined_content")

        if not queue_id:
            return jsonify({
                "error": "queue_id is required"
            }), 400

        success = approval_manager.approve_post(queue_id, variant_index, refined_content)

        if success:
            return jsonify({
                "success": True,
                "message": "投稿案を承認しました",
                "queue_id": queue_id
            }), 200
        else:
            return jsonify({
                "error": "Approval failed",
                "message": "投稿案が見つかりませんでした"
            }), 404

    except Exception as e:
        logger.error(f"Failed to approve post: {e}")
        return jsonify({
            "error": "Failed to approve post",
            "message": str(e)
        }), 500


@app.route("/api/queue/delete-approved", methods=["POST"])
def delete_approved_post():
    """
    承認済み投稿を削除

    Expected JSON:
        {
            "queue_id": "abc12345"
        }
    """
    try:
        data = request.get_json()
        queue_id = data.get("queue_id")

        if not queue_id:
            return jsonify({
                "error": "queue_id is required"
            }), 400

        success = approval_manager.delete_approved_post(queue_id)

        if success:
            return jsonify({
                "success": True,
                "message": "承認済み投稿を削除しました",
                "queue_id": queue_id
            }), 200
        else:
            return jsonify({
                "error": "Delete failed",
                "message": "承認済み投稿が見つかりませんでした"
            }), 404

    except Exception as e:
        logger.error(f"Failed to delete approved post: {e}")
        return jsonify({
            "error": "Failed to delete approved post",
            "message": str(e)
        }), 500


@app.route("/api/queue/reject", methods=["POST"])
def reject_from_queue():
    """
    投稿案を却下してarchived/に移動

    Expected JSON:
        {
            "queue_id": "abc12345",
            "reason": "却下理由"
        }
    """
    try:
        data = request.get_json()
        queue_id = data.get("queue_id")
        reason = data.get("reason", "User rejected")

        if not queue_id:
            return jsonify({
                "error": "queue_id is required"
            }), 400

        success = approval_manager.reject_post(queue_id, reason)

        if success:
            return jsonify({
                "success": True,
                "message": "投稿案を却下しました",
                "queue_id": queue_id
            }), 200
        else:
            return jsonify({
                "error": "Rejection failed",
                "message": "投稿案が見つかりませんでした"
            }), 404

    except Exception as e:
        logger.error(f"Failed to reject post: {e}")
        return jsonify({
            "error": "Failed to reject post",
            "message": str(e)
        }), 500


@app.route("/api/queue/delete-pending", methods=["POST"])
def delete_pending_post():
    """
    未承認投稿案を削除

    Expected JSON:
        {
            "queue_id": "abc12345"
        }
    """
    try:
        data = request.get_json()
        queue_id = data.get("queue_id")

        if not queue_id:
            return jsonify({
                "error": "queue_id is required"
            }), 400

        success = approval_manager.delete_pending_post(queue_id)

        if success:
            logger.info(f"Deleted pending post: queue_id={queue_id}")
            return jsonify({
                "success": True,
                "message": "投稿案を削除しました",
                "queue_id": queue_id
            }), 200
        else:
            return jsonify({
                "error": "Delete failed",
                "message": "投稿案が見つかりませんでした"
            }), 404

    except Exception as e:
        logger.error(f"Failed to delete pending post: {e}")
        return jsonify({
            "error": "Failed to delete pending post",
            "message": str(e)
        }), 500


@app.route("/api/queue/pending/<queue_id>/update", methods=["POST"])
def update_pending_queue(queue_id):
    """
    未承認キューの投稿案を更新

    Expected JSON:
        {
            "variant_index": 0-2,
            "new_content": "編集後の内容"
        }

    Returns:
        JSON: {
            "success": true,
            "queue_id": "...",
            "updated_variant": 0
        }
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data provided"
            }), 400

        variant_index = data.get('variant_index')
        new_content = data.get('new_content')

        if variant_index is None or not new_content:
            return jsonify({
                "error": "variant_index and new_content are required"
            }), 400

        success = approval_manager.update_pending_post(
            queue_id, variant_index, new_content
        )

        if success:
            logger.info(f"Updated pending post: queue_id={queue_id}, variant={variant_index}")
            return jsonify({
                "success": True,
                "queue_id": queue_id,
                "updated_variant": variant_index
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "更新に失敗しました"
            }), 400

    except Exception as e:
        logger.error(f"Failed to update pending post: {e}")
        return jsonify({
            "error": "Failed to update pending post",
            "message": str(e)
        }), 500


@app.route("/api/queue/approved/<queue_id>/update", methods=["POST"])
def update_approved_queue(queue_id):
    """
    承認済みキューの投稿案を更新

    Expected JSON:
        {
            "new_content": "編集後の内容"
        }

    Returns:
        JSON: {
            "success": true,
            "queue_id": "..."
        }
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data provided"
            }), 400

        new_content = data.get('new_content')

        if not new_content:
            return jsonify({
                "error": "new_content is required"
            }), 400

        success = approval_manager.update_approved_post(queue_id, new_content)

        if success:
            logger.info(f"Updated approved post: queue_id={queue_id}")
            return jsonify({
                "success": True,
                "queue_id": queue_id
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "更新に失敗しました"
            }), 400

    except Exception as e:
        logger.error(f"Failed to update approved post: {e}")
        return jsonify({
            "error": "Failed to update approved post",
            "message": str(e)
        }), 500


@app.route("/api/queue/approved/<queue_id>/schedule", methods=["POST"])
def schedule_approved_queue(queue_id):
    """
    承認済みキューをスケジューリング

    Expected JSON:
        {
            "scheduled_time": "ISO 8601形式",
            "platforms": ["X", "Threads"]
        }

    Returns:
        JSON: {
            "success": true,
            "queue_id": "...",
            "scheduled_time": "...",
            "late_post_id": "..."
        }
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data provided"
            }), 400

        scheduled_time = data.get('scheduled_time')
        platforms = data.get('platforms', ['X', 'Threads'])

        if not scheduled_time:
            return jsonify({
                "error": "scheduled_time is required (ISO 8601 format)"
            }), 400

        # 承認済み投稿案の内容を取得
        approved_post = approval_manager.get_approved_post_content(queue_id)

        if not approved_post:
            return jsonify({
                "error": "Approved post not found",
                "message": f"承認済み投稿案が見つかりません: {queue_id}"
            }), 404

        # 一時ファイルに保存（post_to_sns_late.pyが読み込むため）
        temp_file = f"{SNS_DATA_DIR}/temp_approved_{queue_id}.json"
        temp_data = {
            "approved": True,
            "content": approved_post.get("content"),
            "variant": approved_post.get("variant"),
            "approved_at": datetime.now().isoformat()
        }

        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(temp_data, f, ensure_ascii=False, indent=2)

        # post_to_sns_late.py を呼び出し
        job_id = f"queue_scheduled_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        cmd = [
            "python3",
            os.path.join(SCRIPTS_DIR, "post_to_sns_late.py"),
            "--file", os.path.basename(temp_file),
            "--platforms", *platforms,
            "--scheduled-time", scheduled_time,
            "--scheduled-post-id", job_id
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        # 一時ファイル削除
        if os.path.exists(temp_file):
            os.remove(temp_file)

        if result.returncode != 0:
            logger.error(f"post_to_sns_late.py failed: {result.stderr}")

            # エラーメッセージ抽出
            error_message = "Late APIスケジューリングに失敗しました"
            error_details = None

            if "Cast to ObjectId failed" in result.stderr:
                if "facebook" in result.stderr.lower():
                    error_message = "Facebookアカウントが未設定です"
                    error_details = "Late APIダッシュボードでFacebookアカウントを接続してください"
                else:
                    error_message = "無効なアカウントIDが指定されています"
            elif "500 Server Error" in result.stderr:
                error_message = "Late APIサーバーエラー"
            elif "401" in result.stderr or "Unauthorized" in result.stderr:
                error_message = "Late API認証エラー"

            return jsonify({
                "error": error_message,
                "details": error_details,
                "stderr": result.stderr
            }), 500

        # スケジュール情報を記録
        late_post_id = job_id  # 実際にはLate APIのレスポンスから取得すべきだが、簡略化
        success = approval_manager.mark_as_scheduled(queue_id, scheduled_time, late_post_id)

        if not success:
            logger.warning(f"Failed to mark as scheduled: queue_id={queue_id}")

        logger.info(f"Scheduled approved post: queue_id={queue_id}, scheduled_time={scheduled_time}")

        return jsonify({
            "success": True,
            "queue_id": queue_id,
            "scheduled_time": scheduled_time,
            "platforms": platforms,
            "late_post_id": late_post_id
        }), 200

    except Exception as e:
        logger.error(f"Failed to schedule approved post: {e}")
        return jsonify({
            "error": "Failed to schedule approved post",
            "message": str(e),
            "traceback": traceback.format_exc()
        }), 500


@app.route("/api/queue/approve-and-schedule", methods=["POST"])
def approve_and_schedule():
    """
    未承認キューを承認し、自動スケジューリング

    Request Body:
    {
        "queue_id": "26c8a87e",
        "variant_index": 0,
        "platforms": ["LinkedIn", "X", "Threads"]
    }

    Response:
    {
        "success": true,
        "queue_id": "26c8a87e",
        "scheduled_info": {
            "LinkedIn": {
                "scheduled_time": "2026-01-06T08:00:00+09:00",
                "late_post_id": "late_abc123"
            },
            "X": {...},
            "Threads": {...}
        }
    }
    """
    try:
        data = request.get_json()
        queue_id = data.get('queue_id')
        variant_index = data.get('variant_index')
        platforms = data.get('platforms', ['LinkedIn', 'X', 'Threads'])

        # バリデーション
        if not queue_id:
            return jsonify({
                "success": False,
                "error": "queue_id is required"
            }), 400

        if variant_index is None:
            return jsonify({
                "success": False,
                "error": "variant_index is required"
            }), 400

        # STEP 1: 承認処理（既存メソッド）
        logger.info(f"Approving post: queue_id={queue_id}, variant_index={variant_index}")
        approval_result = approval_manager.approve_post(queue_id, variant_index)

        if not approval_result:
            return jsonify({
                "success": False,
                "error": "承認に失敗しました"
            }), 400

        # STEP 2: 自動スケジューリング
        logger.info(f"Auto-scheduling post: queue_id={queue_id}, platforms={platforms}")
        schedule_result = approval_manager.schedule_post_auto(
            queue_id,
            platforms
        )

        if not schedule_result.get("success"):
            return jsonify({
                "success": False,
                "error": schedule_result.get("error", "スケジューリングに失敗しました")
            }), 400

        logger.info(f"Successfully approved and scheduled: queue_id={queue_id}")
        return jsonify({
            "success": True,
            "queue_id": queue_id,
            "scheduled_info": schedule_result.get("scheduled_info", {})
        })

    except Exception as e:
        logger.error(f"Error in approve-and-schedule: {e}", exc_info=True)
        return jsonify({
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500


@app.route("/api/health", methods=["GET"])
def health_check():
    """ヘルスチェック"""
    # Late API経由での投稿予約数をカウント
    result_files = glob.glob(os.path.join(SNS_DATA_DIR, "post_result_*.json"))

    # 承認キュー統計
    pending_count = approval_manager.check_pending_count()
    approved_posts = approval_manager.get_approved_posts()

    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "data_dir": SNS_DATA_DIR,
        "data_dir_exists": os.path.exists(SNS_DATA_DIR),
        "late_api_integration": True,
        "scheduled_posts_count": len(result_files),
        "approval_queue": {
            "pending": pending_count,
            "approved": len(approved_posts)
        }
    }), 200


# ============================================================
# Slack統合API（Phase: Slack承認 → Web UI統合）
# ============================================================

import hmac
import hashlib
import requests

# Slack環境変数
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")


def verify_slack_request(req):
    """Slack署名検証"""
    if not SLACK_SIGNING_SECRET:
        logger.warning("SLACK_SIGNING_SECRET未設定 - 署名検証スキップ")
        return True

    timestamp = req.headers.get("X-Slack-Request-Timestamp", "")
    slack_signature = req.headers.get("X-Slack-Signature", "")

    # リプレイ攻撃防止（5分以内のリクエストのみ受付）
    try:
        if abs(datetime.now().timestamp() - int(timestamp)) > 60 * 5:
            return False
    except (ValueError, TypeError):
        return False

    sig_basestring = f"v0:{timestamp}:{req.get_data().decode('utf-8')}"
    my_signature = "v0=" + hmac.new(
        SLACK_SIGNING_SECRET.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(my_signature, slack_signature)


def post_slack_message(channel, text, thread_ts=None, blocks=None):
    """Slackにメッセージを投稿"""
    if not SLACK_BOT_TOKEN:
        logger.warning("SLACK_BOT_TOKEN未設定")
        return None

    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    }

    payload = {
        "channel": channel,
        "text": text
    }

    if thread_ts:
        payload["thread_ts"] = thread_ts
    if blocks:
        payload["blocks"] = blocks

    try:
        response = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers=headers,
            json=payload,
            timeout=10
        )
        return response.json()
    except Exception as e:
        logger.error(f"Slack投稿エラー: {e}")
        return None


def update_slack_message(channel, ts, text, blocks=None):
    """Slackメッセージを更新"""
    if not SLACK_BOT_TOKEN:
        return None

    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    }

    payload = {
        "channel": channel,
        "ts": ts,
        "text": text
    }

    if blocks:
        payload["blocks"] = blocks

    try:
        response = requests.post(
            "https://slack.com/api/chat.update",
            headers=headers,
            json=payload,
            timeout=10
        )
        return response.json()
    except Exception as e:
        logger.error(f"Slackメッセージ更新エラー: {e}")
        return None


@app.route("/api/slack/interactive", methods=["POST"])
def handle_slack_interactive():
    """
    Slackのインタラクティブボタン受信エンドポイント（統合版）

    Slack Interactive Components → この API → Queue System → Web UI更新

    Returns:
        JSON応答（Slackメッセージ更新用）
    """
    # 署名検証
    if not verify_slack_request(request):
        logger.warning("Slack署名検証失敗")
        return jsonify({"error": "Invalid signature"}), 403

    # Slackから送られるpayloadはform-encoded
    payload = json.loads(request.form.get("payload"))

    action = payload["actions"][0]
    action_id = action["action_id"]
    variant_value = action["value"]
    user_id = payload["user"]["id"]
    user_name = payload["user"]["name"]
    channel_id = payload.get("channel", {}).get("id", SLACK_CHANNEL)
    message_ts = payload.get("message", {}).get("ts")
    thread_ts = payload.get("message", {}).get("thread_ts") or message_ts

    logger.info(f"Slackボタンクリック: action={action_id}, value={variant_value}, user={user_name}")

    # 案N承認
    if "approve_variant_" in action_id:
        variant_num = action_id.replace("approve_variant_", "")
        approved_variant = f"案{variant_num}"

        # 統一された承認処理
        approval_data = {
            "approved": True,
            "variant": approved_variant,
            "refined": False,
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "user_name": user_name,
            "source": "slack",
            "slack_channel": channel_id,
            "slack_thread_ts": thread_ts,
            "slack_message_ts": message_ts
        }

        # approval_result_*.json 保存
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        approval_file = f"{SNS_DATA_DIR}/approval_result_{timestamp}.json"
        approved_post_file = f"{SNS_DATA_DIR}/approved_post_{timestamp}.json"

        # 元の投稿内容を取得
        posts_files = glob.glob(f"{SNS_DATA_DIR}/posts_generated_*.json")
        content = ""
        if posts_files:
            latest_file = max(posts_files, key=os.path.getctime)
            with open(latest_file, 'r', encoding='utf-8') as f:
                posts_data = json.load(f)
            variant_key_map = {"1": "variant_1", "2": "variant_2", "3": "variant_3"}
            variant_key = variant_key_map.get(variant_num)
            if variant_key and variant_key in posts_data:
                content = posts_data[variant_key].get("content", "")

        # approved_post形式
        approved_post_data = {
            "approved": True,
            "approved_at": approval_data["timestamp"],
            "approved_variant": approved_variant,
            "content": content,
            "refined": False,
            "variant": approved_variant,
            "user_id": user_id,
            "user_name": user_name,
            "source": "slack",
            "slack_channel": channel_id,
            "slack_thread_ts": thread_ts
        }

        with open(approval_file, "w", encoding='utf-8') as f:
            json.dump(approval_data, f, ensure_ascii=False, indent=2)

        with open(approved_post_file, "w", encoding='utf-8') as f:
            json.dump(approved_post_data, f, ensure_ascii=False, indent=2)

        logger.info(f"Slack承認保存: {approval_file}")

        # Web UIのURL生成（ローカル開発用）
        web_ui_url = f"http://localhost:3000/approved/{timestamp}"

        # Slackメッセージ更新
        return jsonify({
            "response_type": "in_channel",
            "replace_original": True,
            "text": f"✅ {approved_variant}が承認されました！\n承認者: <@{user_id}>\n🌐 Web UI: {web_ui_url}"
        })

    # 修正案承認
    if "approve_refined_variant_" in action_id:
        variant_num = action_id.replace("approve_refined_variant_", "")

        # refine_context から修正案内容を取得
        refine_context_file = f"{SNS_DATA_DIR}/refine_context_{thread_ts}.json"

        if not os.path.exists(refine_context_file):
            return jsonify({
                "response_type": "ephemeral",
                "text": "❌ 修正履歴が見つかりません"
            }), 400

        with open(refine_context_file, "r", encoding="utf-8") as f:
            context = json.load(f)

        if not context.get("history"):
            return jsonify({
                "response_type": "ephemeral",
                "text": "❌ 修正履歴が空です"
            }), 400

        latest_refined = context["history"][-1]

        approval_data = {
            "approved": True,
            "variant": f"案{variant_num}（修正版）",
            "refined": True,
            "refined_content": latest_refined["refined_content"],
            "refine_count": context["refine_count"],
            "instruction": latest_refined["instruction"],
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "user_name": user_name,
            "source": "slack",
            "slack_channel": channel_id,
            "slack_thread_ts": thread_ts
        }

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        approval_file = f"{SNS_DATA_DIR}/approval_result_{timestamp}.json"
        approved_post_file = f"{SNS_DATA_DIR}/approved_post_{timestamp}.json"

        approved_post_data = {
            "approved": True,
            "approved_at": approval_data["timestamp"],
            "approved_variant": f"案{variant_num}（修正版）",
            "content": latest_refined["refined_content"],
            "refined": True,
            "variant": f"案{variant_num}",
            "user_id": user_id,
            "user_name": user_name,
            "source": "slack",
            "slack_channel": channel_id,
            "slack_thread_ts": thread_ts
        }

        with open(approval_file, "w", encoding='utf-8') as f:
            json.dump(approval_data, f, ensure_ascii=False, indent=2)

        with open(approved_post_file, "w", encoding='utf-8') as f:
            json.dump(approved_post_data, f, ensure_ascii=False, indent=2)

        logger.info(f"Slack修正案承認保存: {approval_file}")

        # スレッドに承認完了メッセージ
        post_slack_message(
            channel_id,
            f"✅ 修正案{context['refine_count']}回目が承認されました！\n承認者: <@{user_id}>",
            thread_ts=thread_ts
        )

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

    return jsonify({"response_type": "ephemeral", "text": "❌ 不明なアクション"}), 400


@app.route("/api/slack/events", methods=["POST"])
def handle_slack_events():
    """
    Slack Events API（スレッド返信受信）
    """
    payload = request.json

    logger.info(f"Slack Event受信: type={payload.get('type')}")

    # URL Verification Challenge（初回設定時）
    if payload.get("type") == "url_verification":
        return jsonify({"challenge": payload["challenge"]})

    # Event受信
    if payload.get("type") == "event_callback":
        event = payload.get("event", {})
        event_type = event.get("type")

        # Bot自身のメッセージは無視
        if event.get("bot_id"):
            return jsonify({"status": "ok"}), 200

        # スレッド返信の処理
        if event_type == "message" and "thread_ts" in event:
            # 既存のスレッド返信処理（refine指示）
            # ここは既存のslack_approval_server.pyのhandle_thread_reply相当の処理
            # 将来的には統合予定
            logger.info(f"スレッド返信受信: {event.get('text', '')[:50]}")

    return jsonify({"status": "ok"}), 200


@app.route("/api/approval-events", methods=["GET"])
def get_approval_events():
    """
    承認イベントのポーリング用エンドポイント

    Query Parameters:
        since: ISO 8601形式のタイムスタンプ（この時刻以降のイベントを取得）

    Returns:
        JSON: {
            "events": [
                {
                    "type": "approval",
                    "timestamp": "...",
                    "source": "slack" | "webui",
                    "variant": "案1",
                    ...
                }
            ],
            "last_check": "..."
        }
    """
    try:
        since = request.args.get("since")
        since_dt = None
        if since:
            try:
                since_dt = datetime.fromisoformat(since.replace('Z', '+00:00'))
            except ValueError:
                since_dt = None

        events = []

        # approval_result_*.json をスキャン
        approval_files = glob.glob(f"{SNS_DATA_DIR}/approval_result_*.json")

        for f_path in approval_files:
            try:
                with open(f_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                event_ts = data.get("timestamp")
                if event_ts:
                    event_dt = datetime.fromisoformat(event_ts)

                    # since以降のイベントのみ返す
                    if since_dt is None or event_dt > since_dt:
                        events.append({
                            "type": "approval",
                            "file": os.path.basename(f_path),
                            "timestamp": event_ts,
                            "source": data.get("source", "unknown"),
                            "variant": data.get("variant"),
                            "user_name": data.get("user_name"),
                            "refined": data.get("refined", False),
                            "slack_thread_ts": data.get("slack_thread_ts")
                        })
            except (json.JSONDecodeError, KeyError) as e:
                logger.warning(f"承認ファイル解析エラー: {f_path}, {e}")
                continue

        # タイムスタンプでソート（新しい順）
        events.sort(key=lambda x: x.get("timestamp", ""), reverse=True)

        return jsonify({
            "events": events[:20],  # 最新20件
            "last_check": datetime.now().isoformat(),
            "total_count": len(events)
        }), 200

    except Exception as e:
        logger.error(f"承認イベント取得エラー: {e}")
        return jsonify({
            "error": "Failed to get approval events",
            "message": str(e)
        }), 500


@app.route("/api/notify-slack", methods=["POST"])
def notify_slack_from_webui():
    """
    Web UIから承認した際にSlackに通知

    Expected JSON:
        {
            "variant": "案1",
            "content": "投稿内容",
            "approval_file": "approval_result_20260104_120000.json",
            "slack_thread_ts": "1234567890.123456" (optional)
        }

    Returns:
        JSON: {"success": true, "slack_response": {...}}
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        variant = data.get("variant", "")
        content = data.get("content", "")[:200]  # 最初200文字
        approval_file = data.get("approval_file", "")
        thread_ts = data.get("slack_thread_ts")

        channel = SLACK_CHANNEL or os.getenv("SLACK_CHANNEL_ID")

        if not channel:
            return jsonify({
                "success": False,
                "error": "SLACK_CHANNEL未設定"
            }), 400

        # Slackに通知メッセージを投稿
        message = f"🌐 *Web UIで承認されました*\n\n*{variant}*\n```{content}...```"

        result = post_slack_message(
            channel,
            message,
            thread_ts=thread_ts
        )

        if result and result.get("ok"):
            logger.info(f"Slack通知成功: {approval_file}")
            return jsonify({
                "success": True,
                "slack_response": result
            }), 200
        else:
            logger.warning(f"Slack通知失敗: {result}")
            return jsonify({
                "success": False,
                "error": result.get("error") if result else "Unknown error"
            }), 500

    except Exception as e:
        logger.error(f"Slack通知エラー: {e}")
        return jsonify({
            "error": "Failed to notify Slack",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    PORT = 5555  # macOS AirPlay Receiver conflicts with 5000/5001

    print("=" * 60)
    print("SNS Approval API Server")
    print("=" * 60)
    print(f"Data Directory: {SNS_DATA_DIR}")
    print(f"CORS Enabled: http://localhost:3000")
    print(f"Health Check: http://localhost:{PORT}/api/health")
    print(f"Server: http://localhost:{PORT}")
    print("=" * 60)

    app.run(debug=True, port=PORT, host="0.0.0.0")
