#!/usr/bin/env python3
"""
Late API テスト投稿実行スクリプト v2

LinkedIn、X (Twitter)、Threads への URL参照付き投稿をLate API経由で実行
"""

import os
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from pathlib import Path


def load_env_vars():
    """環境変数読み込み（.envファイルから直接パース）"""
    env_path = Path("/Users/yuichi/agentpm/Stock/programs/副業/projects/SNS/.env")

    env_vars = {}
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()

    api_key = env_vars.get("LATE_API_KEY")
    linkedin_account_id = env_vars.get("LATE_LINKEDIN_ACCOUNT_ID")
    twitter_account_id = env_vars.get("LATE_TWITTER_ACCOUNT_ID")
    threads_account_id = env_vars.get("LATE_THREADS_ACCOUNT_ID")

    if not all([api_key, linkedin_account_id, twitter_account_id, threads_account_id]):
        raise ValueError("Required environment variables not found")

    return {
        "api_key": api_key,
        "linkedin_account_id": linkedin_account_id,
        "twitter_account_id": twitter_account_id,
        "threads_account_id": threads_account_id
    }


def post_to_late_api(payload: dict, api_key: str) -> dict:
    """
    Late API POST /v1/posts にリクエスト送信

    Args:
        payload: リクエストボディ
        api_key: Late API キー

    Returns:
        dict: APIレスポンス
    """
    base_url = "https://getlate.dev/api/v1"
    endpoint = f"{base_url}/posts"

    print(f"📤 Posting to Late API: {endpoint}")
    print(f"📦 Payload:\n{json.dumps(payload, ensure_ascii=False, indent=2)}\n")

    # リクエスト作成
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    # リクエスト送信
    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode('utf-8')
            response_data = json.loads(response_body)

            print(f"📨 Response Status: {response.status}")
            print(f"📨 Response Body:\n{json.dumps(response_data, ensure_ascii=False, indent=2)}\n")

            return response_data
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        print(f"📨 Error Body:\n{error_body}\n")
        raise
    except urllib.error.URLError as e:
        print(f"❌ URL Error: {e.reason}")
        raise


# LinkedIn投稿（firstComment付き）
def create_linkedin_payload(env_vars: dict, scheduled_time: datetime) -> dict:
    scheduled_str = scheduled_time.strftime("%Y-%m-%dT%H:%M:%S+09:00")

    content = """**AIエージェントの本質は「スキル」にある。**

答えは単純だ。SlashCommandでもSubagentでもない。最大の武器は「ポータビリティー」なんだよね。

NappsTechnologiesの榎本氏が年末に公開したnote記事を読んで、痺れた。

**これはテスト投稿です（URL参照機能検証）**"""

    return {
        "content": content,
        "scheduledFor": scheduled_str,
        "timezone": "Asia/Tokyo",
        "platforms": [{
            "platform": "linkedin",
            "accountId": env_vars["linkedin_account_id"],
            "platformSpecificData": {
                "firstComment": """■ ソース

https://note.com/napps_technologies
https://www.anthropic.com/claude-code"""
            }
        }]
    }


# X投稿（スレッド、最後にURL）
def create_twitter_payload(env_vars: dict, scheduled_time: datetime) -> dict:
    scheduled_str = scheduled_time.strftime("%Y-%m-%dT%H:%M:%S+09:00")

    content = "AIコーディングの実務で効いた5つの型が公開された\n\n松尾研究所の中川氏がZennで詳細レポート"

    return {
        "content": content,
        "scheduledFor": scheduled_str,
        "timezone": "Asia/Tokyo",
        "platforms": [{
            "platform": "twitter",
            "accountId": env_vars["twitter_account_id"],
            "platformSpecificData": {
                "threadItems": [
                    {"content": "なぜAIコーディングは「補助」では不十分なのか？\n\n答えはシンプル"},
                    {"content": "あなたはAIコーディングをどう位置づけていますか？\n\n**テスト投稿（URL参照機能検証）**\n\n■ ソース\n\nhttps://zenn.dev/matsuo_lab\nhttps://www.anthropic.com/claude-code"}
                ]
            }
        }]
    }


# Threads投稿（単一投稿、最後にURL）
def create_threads_payload(env_vars: dict, scheduled_time: datetime) -> dict:
    scheduled_str = scheduled_time.strftime("%Y-%m-%dT%H:%M:%S+09:00")

    content = """AI Code Reviewsが開発を変える

CodeRabbitのレポートが示すデータが衝撃的

**これはテスト投稿です（URL参照機能検証）**

■ ソース

https://coderabbit.ai/blog/
https://github.blog/ai-and-ml/"""

    return {
        "content": content,
        "scheduledFor": scheduled_str,
        "timezone": "Asia/Tokyo",
        "platforms": [{
            "platform": "threads",
            "accountId": env_vars["threads_account_id"]
        }]
    }


def main():
    """メイン処理"""

    print("="*70)
    print("Late API テスト投稿実行 v2")
    print("="*70)
    print()

    # 環境変数読み込み
    print("📂 Loading environment variables...")
    env_vars = load_env_vars()
    print("✅ Environment variables loaded\n")

    # スケジュール時刻設定（現在時刻の5分後）
    scheduled_time = datetime.now() + timedelta(minutes=5)
    print(f"⏰ Scheduled time: {scheduled_time.strftime('%Y-%m-%d %H:%M:%S JST')}\n")

    results = {}

    # LinkedIn投稿
    try:
        print("="*70)
        print("1️⃣  LinkedIn テスト投稿（firstComment付き）")
        print("="*70)
        payload = create_linkedin_payload(env_vars, scheduled_time)
        results["linkedin"] = post_to_late_api(payload, env_vars["api_key"])
        print("✅ LinkedIn post scheduled successfully\n")
    except Exception as e:
        print(f"❌ LinkedIn post failed: {e}\n")
        results["linkedin"] = {"error": str(e)}

    # X投稿
    try:
        print("="*70)
        print("2️⃣  X (Twitter) テスト投稿（スレッド、最後にURL）")
        print("="*70)
        payload = create_twitter_payload(env_vars, scheduled_time + timedelta(minutes=5))
        results["twitter"] = post_to_late_api(payload, env_vars["api_key"])
        print("✅ Twitter thread scheduled successfully\n")
    except Exception as e:
        print(f"❌ Twitter post failed: {e}\n")
        results["twitter"] = {"error": str(e)}

    # Threads投稿
    try:
        print("="*70)
        print("3️⃣  Threads テスト投稿（最後にURL）")
        print("="*70)
        payload = create_threads_payload(env_vars, scheduled_time + timedelta(minutes=10))
        results["threads"] = post_to_late_api(payload, env_vars["api_key"])
        print("✅ Threads post scheduled successfully\n")
    except Exception as e:
        print(f"❌ Threads post failed: {e}\n")
        results["threads"] = {"error": str(e)}

    # 結果サマリー
    print("="*70)
    print("📊 テスト投稿結果サマリー")
    print("="*70)

    success_count = sum(1 for r in results.values() if r and "error" not in r)

    print(f"\n✅ 成功: {success_count}/3")
    print(f"❌ 失敗: {3 - success_count}/3\n")

    for platform, result in results.items():
        if result and "error" not in result:
            print(f"✅ {platform.upper()}: Posted successfully")
        else:
            print(f"❌ {platform.upper()}: Failed")

    # 結果をJSONファイルに保存
    output_path = Path("/Users/yuichi/agentpm/Flow/202601/2026-01-12/late_api_test_results_v2.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n📝 Results saved to: {output_path}")

    return results


if __name__ == "__main__":
    main()
