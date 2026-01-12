#!/usr/bin/env python3
"""
Late API レスポンステスト - APIの構造確認
"""

import requests
import json

API_KEY = "sk_25a52d19aa714c4811832be20a11717c27c3b77c59c1d0df62f270609429cff4"
BASE_URL = "https://getlate.dev/api/v1"

def get_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

# プロフィール取得
print("=== プロフィール取得 ===")
response = requests.get(f"{BASE_URL}/profiles", headers=get_headers())
print(f"Status: {response.status_code}")
print(f"Response Type: {type(response.json())}")
print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

# アカウント取得
print("\n=== アカウント取得 ===")
response = requests.get(f"{BASE_URL}/accounts", headers=get_headers())
print(f"Status: {response.status_code}")
print(f"Response Type: {type(response.json())}")
print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
