#!/usr/bin/env python3
"""
LinkedIn Person URN取得スクリプト
"""

import requests
import json

# Access Token
ACCESS_TOKEN = "AQURojiebY3yqCg-N7SQjTizGIEZa5QKV90UzNQi3v5bikrPdPHuXjamxbM-1SNLmlG716pCQOZSEE4vK6gItOpT0VQ7hKYtMVAj9ZzlD29UPk29Co2Gh0z0MILpUMvAtMzvM__Mx4dcFeOEoqqgehX6-Rv5_1St_R4yX2Dmw1Fv1E7OzHsIohTesRyeB8PM-ss6ufJ2vVLsQrbEGoZPcBJ8K8X7GuZxcZsEnaQgBxYGKJJKZQmszge0zmZLZFtLK0oDLdQvyh0nPLmUSOscf1ojMGXPlTyHxA-nneoko8enicADYGjM2mw5kjkiCskUoWFBbX_RDOB5nx2FMlbcJlxubJGtfQ"

print("=" * 50)
print("LinkedIn Person URN取得")
print("=" * 50)
print()

# Person URN取得
url = "https://api.linkedin.com/v2/userinfo"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

print("📡 LinkedIn APIに接続中...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    userinfo = response.json()
    print("✅ Person URN取得成功！")
    print()
    print(json.dumps(userinfo, indent=2, ensure_ascii=False))
    print()

    # Person URN（sub）
    person_urn = userinfo.get("sub")
    name = userinfo.get("name")
    email = userinfo.get("email")

    print("=" * 50)
    print("LinkedIn認証情報")
    print("=" * 50)
    print(f"名前: {name}")
    print(f"メール: {email}")
    print(f"Person URN (sub): {person_urn}")
    print()
    print("この情報を.envファイルに保存します。")

else:
    print(f"❌ エラー: {response.status_code}")
    print(response.text)
