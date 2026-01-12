#!/usr/bin/env python3
"""
SNS Approval API Test Script
Flask APIの各エンドポイントをテスト
"""

import requests
import json
import time
import sys
from datetime import datetime

API_BASE_URL = "http://localhost:5555/api"

def test_get_posts():
    """GET /api/posts のテスト"""
    print("\n[TEST 1] GET /api/posts")
    print("-" * 50)

    try:
        response = requests.get(f"{API_BASE_URL}/posts", timeout=5)

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("✅ 成功: 投稿データ取得")
            print(f"   variant_1: {data.get('variant_1', {}).get('title', 'N/A')}")
            print(f"   variant_2: {data.get('variant_2', {}).get('title', 'N/A')}")
            print(f"   variant_3: {data.get('variant_3', {}).get('title', 'N/A')}")
            print(f"   metadata: {data.get('metadata', {}).get('file', 'N/A')}")
            return True
        else:
            print(f"❌ 失敗: {response.text}")
            return False

    except requests.exceptions.ConnectionError:
        print("❌ 失敗: APIサーバーに接続できません")
        print("   → python3 scripts/sns_approval_api.py を先に起動してください")
        return False
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False


def test_approve_post():
    """POST /api/approve のテスト"""
    print("\n[TEST 2] POST /api/approve")
    print("-" * 50)

    test_data = {
        "variant": "案1",
        "content": "テスト投稿: AI活用事例紹介",
        "refined": False
    }

    try:
        response = requests.post(
            f"{API_BASE_URL}/approve",
            json=test_data,
            timeout=5
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("✅ 成功: 投稿承認")
            print(f"   File: {data.get('file', 'N/A')}")
            print(f"   Timestamp: {data.get('timestamp', 'N/A')}")
            return True
        else:
            print(f"❌ 失敗: {response.text}")
            return False

    except Exception as e:
        print(f"❌ エラー: {e}")
        return False


def test_refine_variant():
    """POST /api/refine のテスト"""
    print("\n[TEST 3] POST /api/refine")
    print("-" * 50)

    test_data = {
        "variant_num": "案1",
        "instruction": "もっとカジュアルに、絵文字を追加してください"
    }

    try:
        response = requests.post(
            f"{API_BASE_URL}/refine",
            json=test_data,
            timeout=30  # AI処理のため長めに設定
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("✅ 成功: AI修正実行")
            print(f"   Session ID: {data.get('session_id', 'N/A')}")
            print(f"   Refined Content (first 100 chars): {data.get('refined_content', '')[:100]}...")
            return True
        else:
            print(f"❌ 失敗: {response.text}")
            return False

    except Exception as e:
        print(f"❌ エラー: {e}")
        return False


def test_schedule_post():
    """POST /api/schedule のテスト"""
    print("\n[TEST 4] POST /api/schedule")
    print("-" * 50)

    test_data = {
        "variant": "案1",
        "content": "スケジュールテスト投稿",
        "platforms": ["X", "LinkedIn"],
        "scheduled_time": "2026-01-05T10:00:00"
    }

    try:
        response = requests.post(
            f"{API_BASE_URL}/schedule",
            json=test_data,
            timeout=10
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("✅ 成功: スケジュール投稿")
            print(f"   Scheduled: {data.get('scheduled', 'N/A')}")
            return True
        else:
            print(f"❌ 失敗: {response.text}")
            return False

    except Exception as e:
        print(f"❌ エラー: {e}")
        return False


def main():
    print("=" * 50)
    print("SNS Approval API Test Suite")
    print(f"Started at: {datetime.now().isoformat()}")
    print("=" * 50)

    results = []

    # Test 1: GET /api/posts
    results.append(("GET /api/posts", test_get_posts()))
    time.sleep(1)

    # Test 2: POST /api/approve
    results.append(("POST /api/approve", test_approve_post()))
    time.sleep(1)

    # Test 3: POST /api/refine (スキップ可能 - AI処理時間がかかる)
    # results.append(("POST /api/refine", test_refine_variant()))
    # time.sleep(1)

    # Test 4: POST /api/schedule
    results.append(("POST /api/schedule", test_schedule_post()))

    # サマリー表示
    print("\n" + "=" * 50)
    print("Test Summary")
    print("=" * 50)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")

    print("-" * 50)
    print(f"Total: {passed}/{total} tests passed")
    print(f"Success Rate: {passed/total*100:.1f}%")
    print("=" * 50)

    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
