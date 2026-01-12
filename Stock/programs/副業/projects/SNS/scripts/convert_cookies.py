#!/usr/bin/env python3
"""
Convert Netscape Cookie format to Playwright JSON format
"""
import json
from pathlib import Path

def convert_netscape_to_playwright(netscape_file: str, output_file: str):
    """NetscapeクッキーをPlaywright形式に変換"""
    cookies = []

    with open(netscape_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # コメント行や空行をスキップ
            if not line or line.startswith('#'):
                continue

            try:
                # Netscape形式のパース（スペースまたはタブ区切り）
                import re
                parts = re.split(r'\s+', line)
                if len(parts) < 7:
                    continue

                domain, flag, path, secure, expiration, name, value = parts

                cookie = {
                    "name": name,
                    "value": value,
                    "domain": domain,
                    "path": path,
                    "expires": int(expiration) if expiration != '0' else -1,
                    "httpOnly": False,
                    "secure": secure == 'TRUE',
                    "sameSite": "Lax"
                }

                cookies.append(cookie)

            except Exception as e:
                print(f"⚠️ クッキー解析エラー: {line[:50]}... - {e}")
                continue

    # JSON保存
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cookies, f, ensure_ascii=False, indent=2)

    print(f"✅ クッキー変換完了: {len(cookies)}件")
    print(f"   出力: {output_file}")

    return cookies

if __name__ == '__main__':
    base_dir = Path(__file__).parent.parent
    netscape_file = base_dir / 'data' / 'x_cookies.txt'
    output_file = base_dir / 'data' / 'x_cookies.json'

    convert_netscape_to_playwright(str(netscape_file), str(output_file))
