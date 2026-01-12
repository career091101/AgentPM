#!/usr/bin/env python3
"""
パスワード保護されたPDFをダウンロード
"""

import requests
from pathlib import Path

PASSWORD = "snshack"
PDF_URL = "https://affiliateman.site/wp-content/uploads/2022/11/SNS攻略サロンインタビュー資料.pdf"
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/resources/pdf")

def download_pdf():
    """PDFをダウンロード"""
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })

    # まずサイトのトップページにアクセスしてログイン
    print("ログイン中...")
    response = session.get("https://affiliateman.site", allow_redirects=True)

    login_data = {
        'password_protected_pwd': PASSWORD,
        'password_protected_rememberme': '1',
        'Submit': 'ログイン'
    }

    response = session.post(response.url, data=login_data, allow_redirects=True)

    auth_cookies = ['wp-postpass', 'password_protected_auth']
    is_authenticated = any(cookie_name in str(session.cookies) for cookie_name in auth_cookies)

    if not is_authenticated:
        print("✗ ログイン失敗")
        return False

    print("✓ ログイン成功")

    # PDFをダウンロード
    print(f"PDFダウンロード中: {PDF_URL}")
    response = session.get(PDF_URL, stream=True)

    if response.status_code != 200:
        print(f"✗ ダウンロード失敗: HTTP {response.status_code}")
        return False

    # 出力ディレクトリを作成
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ファイルを保存
    output_file = OUTPUT_DIR / "SNS攻略サロンインタビュー資料.pdf"
    with open(output_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    file_size = output_file.stat().st_size
    print(f"✓ ダウンロード完了: {output_file}")
    print(f"  ファイルサイズ: {file_size / 1024:.1f} KB")

    return True

if __name__ == "__main__":
    print("=" * 60)
    print("PDF資料ダウンロード")
    print("=" * 60)
    download_pdf()
