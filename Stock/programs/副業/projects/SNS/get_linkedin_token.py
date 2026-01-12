#!/usr/bin/env python3
"""
LinkedIn Access Token取得スクリプト
"""

import requests
import json

# 認証情報
CLIENT_ID = "867hg8t3ohiz3g"
CLIENT_SECRET = "WPL_AP1.68UESLjBlJODtCFP.FOPrZg=="
CODE = "AQQTkkurXm_mMUgtx-kOjfsRwcDgvhGkTNOlGNklHm-ePQHUKatYSbYReMwqb8DB0KAUNz1X79_c_aASswmGQl-Dt4n2o84n-q9dNGgWnRXY9t9ZyuI6J1jijL405FwgiQETGCQwRDHkoKEJCcrh0aPnwomg0WyeOmpeaA9gLLXaA_lBdN_w8BZP6q4GIsir4b-X_zde9Lq0F6M_lxA"
REDIRECT_URI = "http://localhost:8080/callback"

print("=" * 50)
print("LinkedIn Access Token取得")
print("=" * 50)
print()

# Access Token取得
url = "https://www.linkedin.com/oauth/v2/accessToken"
data = {
    "grant_type": "authorization_code",
    "code": CODE,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "redirect_uri": REDIRECT_URI
}

print("📡 LinkedIn APIに接続中...")
response = requests.post(url, data=data)

if response.status_code == 200:
    token_data = response.json()
    print("✅ Access Token取得成功！")
    print()
    print(json.dumps(token_data, indent=2))
    print()

    # Access Tokenを保存
    access_token = token_data.get("access_token")
    expires_in = token_data.get("expires_in")

    print(f"Access Token: {access_token[:30]}...")
    print(f"有効期限: {expires_in} 秒 ({expires_in // 86400} 日)")

else:
    print(f"❌ エラー: {response.status_code}")
    print(response.text)
