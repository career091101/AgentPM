#!/usr/bin/env python3
"""
NetscapeフォーマットのクッキーをPlaywright JSON形式に変換
"""
import json
from datetime import datetime

def convert_netscape_to_playwright(netscape_file, output_file):
    """Netscapeクッキーファイルをplaywrightのjson形式に変換"""

    cookies = []

    with open(netscape_file, 'r') as f:
        for line in f:
            line = line.strip()

            # コメント行や空行をスキップ
            if not line or line.startswith('#'):
                continue

            # タブ区切りでパース
            parts = line.split('\t')

            if len(parts) >= 7:
                domain = parts[0]
                http_only = parts[1] == 'TRUE'
                path = parts[2]
                secure = parts[3] == 'TRUE'
                expires = int(parts[4])
                name = parts[5]
                value = parts[6]

                # Playwrightのクッキー形式に変換
                cookie = {
                    'name': name,
                    'value': value,
                    'domain': domain,
                    'path': path,
                    'expires': expires if expires > 0 else -1,
                    'httpOnly': http_only,
                    'secure': secure,
                    'sameSite': 'Lax'
                }

                cookies.append(cookie)

    # JSONファイルとして保存
    with open(output_file, 'w') as f:
        json.dump({'cookies': cookies}, f, indent=2)

    print(f"✅ クッキー変換完了: {len(cookies)}個")
    print(f"   入力: {netscape_file}")
    print(f"   出力: {output_file}")

    return cookies

if __name__ == "__main__":
    netscape_file = "facebook_cookies.txt"
    output_file = "facebook_cookies.json"

    cookies = convert_netscape_to_playwright(netscape_file, output_file)

    # クッキー情報を表示
    print("\n📋 変換されたクッキー:")
    for cookie in cookies:
        print(f"   - {cookie['name']}: {cookie['value'][:20]}...")
