#!/usr/bin/env python3
"""
Instagram Insights データ取得スクリプト (Agent1)
過去90日間のホームページデータをスクリーンショットで取得
"""

import os
import time
from playwright.sync_api import sync_playwright

# パス設定
USER_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/.browser_state_1"
SCREENSHOT_PATH = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/screenshots/instagram_home_agent1.png"
URL = "https://www.instagram.com/accounts/insights/?timeframe=90"

def main():
    print("Instagram Insights データ取得を開始します...")

    with sync_playwright() as p:
        # ブラウザを起動（既存のセッションを使用）
        print(f"ブラウザを起動中... (user_data_dir: {USER_DATA_DIR})")
        browser = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1920, "height": 1080},
            args=['--disable-blink-features=AutomationControlled']
        )

        # 新しいページを作成
        page = browser.new_page()

        try:
            # URLに移動
            print(f"URLに移動中: {URL}")
            page.goto(URL, wait_until="domcontentloaded", timeout=60000)

            # 6秒待機（ページ読み込み完了）
            print("ページ読み込み待機中（6秒）...")
            time.sleep(6)

            # フルページスクリーンショット撮影
            print(f"スクリーンショット撮影中: {SCREENSHOT_PATH}")
            page.screenshot(path=SCREENSHOT_PATH, full_page=True)
            print("スクリーンショット撮影完了!")

            # ファイルサイズ確認
            file_size = os.path.getsize(SCREENSHOT_PATH)
            print(f"保存されたファイルサイズ: {file_size:,} bytes")

        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            raise
        finally:
            # ブラウザを閉じる
            print("ブラウザを閉じています...")
            browser.close()
            print("完了しました!")

if __name__ == "__main__":
    main()
