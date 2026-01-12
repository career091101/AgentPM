#!/usr/bin/env python3
"""
Threads週間総括データ取得スクリプト（Agent3）
スクリーンショット撮影 → 画像分析 → CSV保存
"""

import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import csv
import os

async def main():
    # 保存先パス
    screenshot_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/screenshots/threads_weekly_agent3.png"
    csv_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/Threads/threads_weekly_parallel_agent3.csv"
    user_data_dir = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/.browser_state_3"
    url = "https://www.threads.com/insights/weekly_recap?xmt=AQF0fRzSJPDc1cQ3HORNSmykkoBYA3Ug__fhworAp2V9DZI"

    # ディレクトリ作成
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Playwrightブラウザ起動中...")

    async with async_playwright() as p:
        # ブラウザ起動
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            viewport={'width': 1920, 'height': 1080}
        )

        try:
            page = browser.pages[0] if browser.pages else await browser.new_page()

            print(f"[{datetime.now().strftime('%H:%M:%S')}] URLに移動: {url}")
            await page.goto(url, wait_until='domcontentloaded', timeout=30000)

            print(f"[{datetime.now().strftime('%H:%M:%S')}] 8秒待機中...")
            await asyncio.sleep(8)

            print(f"[{datetime.now().strftime('%H:%M:%S')}] スクリーンショット撮影中...")
            await page.screenshot(path=screenshot_path, full_page=True)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] スクリーンショット保存完了: {screenshot_path}")

            # ここで画像分析用のフラグファイルを作成
            flag_path = "/tmp/threads_screenshot_ready_agent3.flag"
            with open(flag_path, 'w') as f:
                f.write(screenshot_path)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] フラグファイル作成: {flag_path}")

        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] エラー発生: {str(e)}")
            raise
        finally:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ブラウザを閉じています...")
            await browser.close()
            print(f"[{datetime.now().strftime('%H:%M:%S')}] 完了")

if __name__ == "__main__":
    asyncio.run(main())
