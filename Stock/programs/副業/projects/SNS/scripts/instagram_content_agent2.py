#!/usr/bin/env python3
"""
Instagram Insights コンテンツページのスクリーンショット取得スクリプト (Agent2)
並列実行用に設計されたスクリプト
"""

import os
import time
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
import csv

# パス設定
BASE_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS")
USER_DATA_DIR = BASE_DIR / ".browser_state_2"
SCREENSHOT_PATH = BASE_DIR / "screenshots" / "instagram_content_agent2.png"
CSV_PATH = BASE_DIR / "Instagram" / "instagram_content_parallel_agent2.csv"

# Instagram URL
INSTAGRAM_URL = "https://www.instagram.com/accounts/insights/content/?media_type=all&metric=accounts_engaged&sort_by=highest&timeframe=90&view_type=card"

def main():
    print("=" * 60)
    print("Instagram Insights コンテンツデータ取得 (Agent2)")
    print("=" * 60)

    # スクリーンショットディレクトリの作成
    SCREENSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        print(f"\n[1/7] ブラウザを起動中...")
        print(f"  - User Data Dir: {USER_DATA_DIR}")

        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            args=['--no-sandbox', '--disable-setuid-sandbox']
        )

        try:
            page = browser.pages[0] if browser.pages else browser.new_page()

            print(f"\n[2/7] URLに移動中...")
            print(f"  - URL: {INSTAGRAM_URL}")
            # networkidleではなくloadで待機（Instagramは動的コンテンツが多いため）
            page.goto(INSTAGRAM_URL, wait_until='load', timeout=60000)

            print(f"\n[3/7] ページ読み込み待機中 (8秒)...")
            time.sleep(8)

            print(f"\n[4/7] フルページスクリーンショット撮影中...")
            page.screenshot(path=str(SCREENSHOT_PATH), full_page=True)
            print(f"  ✓ 保存完了: {SCREENSHOT_PATH}")

            print(f"\n[5/7] ページ情報を取得中...")
            # 基本的なページ情報を取得
            page_title = page.title()
            current_url = page.url

            print(f"  - ページタイトル: {page_title}")
            print(f"  - 現在のURL: {current_url}")

            # 投稿要素の数をカウント（可能な場合）
            post_count = 0
            try:
                # Instagram Insightsの投稿カード要素を探す
                # 複数のセレクタを試す
                selectors = [
                    'article[role="presentation"]',
                    'div[role="button"] img',
                    'a[href*="/p/"]',
                    'img[src*="scontent"]'
                ]

                for selector in selectors:
                    elements = page.query_selector_all(selector)
                    if elements:
                        post_count = len(elements)
                        print(f"  - 検出された投稿要素数: {post_count} (selector: {selector})")
                        break

                if post_count == 0:
                    print(f"  - 投稿要素が検出できませんでした（手動確認が必要）")

            except Exception as e:
                print(f"  - 投稿数カウント中にエラー: {str(e)}")

            print(f"\n[6/7] CSVファイルに保存中...")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # CSVに保存
            with open(CSV_PATH, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['投稿番号', '取得日時', 'データソース', '備考'])

                if post_count > 0:
                    for i in range(1, post_count + 1):
                        writer.writerow([
                            i,
                            timestamp,
                            '並列実行Agent2',
                            f'スクリーンショット分析により検出 (合計{post_count}件)'
                        ])
                else:
                    # 投稿数が取得できなかった場合は1行のみ記録
                    writer.writerow([
                        '-',
                        timestamp,
                        '並列実行Agent2',
                        f'スクリーンショット撮影完了。詳細は画像分析が必要: {SCREENSHOT_PATH}'
                    ])

            print(f"  ✓ 保存完了: {CSV_PATH}")

        except Exception as e:
            print(f"\n❌ エラーが発生しました: {str(e)}")
            import traceback
            traceback.print_exc()

            # エラー情報をCSVに記録
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(CSV_PATH, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['投稿番号', '取得日時', 'データソース', '備考'])
                writer.writerow([
                    '-',
                    timestamp,
                    '並列実行Agent2',
                    f'エラー発生: {str(e)}'
                ])

            raise

        finally:
            print(f"\n[7/7] ブラウザを閉じています...")
            browser.close()
            print("  ✓ ブラウザを閉じました")

    print("\n" + "=" * 60)
    print("取得完了サマリー")
    print("=" * 60)
    print(f"スクリーンショット: {SCREENSHOT_PATH}")
    print(f"CSVファイル: {CSV_PATH}")
    if post_count > 0:
        print(f"検出された投稿数: {post_count}件")
    else:
        print(f"投稿数: 画像分析が必要")
    print("=" * 60)

if __name__ == "__main__":
    main()
