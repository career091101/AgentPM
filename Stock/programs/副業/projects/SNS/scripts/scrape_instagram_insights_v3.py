#!/usr/bin/env python3
"""
Instagram Web版Insightsページから完全なデータをスクレイピングするスクリプト (v3)

アカウントサマリー + 個別投稿データの両方を取得します。
"""

import os
import time
import pandas as pd
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# プロジェクトルートディレクトリ
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "Instagram"
DATA_DIR.mkdir(exist_ok=True)

# ブラウザ状態保存ディレクトリ
BROWSER_STATE_DIR = PROJECT_ROOT / ".browser_state"
BROWSER_STATE_DIR.mkdir(exist_ok=True)

# Instagram Insights URLs
INSIGHTS_HOME_URL = "https://www.instagram.com/accounts/insights/?timeframe=90"
INSIGHTS_CONTENT_URL = "https://www.instagram.com/accounts/insights/content/?media_type=all&metric=accounts_engaged&sort_by=highest&timeframe=90&view_type=card"


def extract_account_summary(page):
    """アカウント全体のサマリーデータを取得"""
    print("\nアカウントサマリーデータを取得中...")

    # Insightsホームページに移動
    page.goto(INSIGHTS_HOME_URL)
    time.sleep(5)

    summary_data = {
        "期間": "過去90日間",
        "取得日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        # すべてのh1要素（数値）を取得
        h1_elements = page.locator('h1').all()
        h1_values = []
        for elem in h1_elements:
            try:
                text = elem.inner_text().strip()
                if text.replace(',', '').isdigit():
                    h1_values.append(text)
            except:
                pass

        print(f"  h1要素から取得した数値: {h1_values}")

        # データ割り当て
        if len(h1_values) >= 1:
            summary_data["総ビュー数"] = h1_values[0]
        if len(h1_values) >= 2:
            summary_data["総インタラクション数"] = h1_values[1]
        if len(h1_values) >= 3:
            summary_data["プロフィールアクティビティ"] = h1_values[2]
        if len(h1_values) >= 4:
            summary_data["フォロワー数"] = h1_values[3]

        print(f"✓ サマリーデータ取得完了: {summary_data}")

    except Exception as e:
        print(f"⚠ サマリー取得エラー: {e}")

    return summary_data


def extract_content_data(page):
    """コンテンツページから投稿データを取得"""
    print("\n個別投稿データを取得中...")

    # コンテンツページに移動
    page.goto(INSIGHTS_CONTENT_URL)
    time.sleep(8)  # 動的コンテンツ読み込み待機

    posts_data = []

    try:
        # 画像要素を取得（投稿のサムネイル）
        img_elements = page.locator('img').all()
        print(f"  検出した画像数: {len(img_elements)}個")

        # 最初の数枚をスキップ（プロフィール画像など）
        post_images = img_elements[1:22]  # 2番目から22番目まで（最大21投稿）

        for i, img in enumerate(post_images):
            try:
                # 画像のalt属性とsrcを取得
                alt = img.get_attribute('alt')
                src = img.get_attribute('src')

                # 親要素を辿ってリンクを探す
                parent = img.locator('..')
                for _ in range(5):  # 最大5階層上まで探索
                    try:
                        link = parent.locator('a').first
                        href = link.get_attribute('href')
                        if href and ('/p/' in href or '/reel/' in href):
                            post_data = {
                                "投稿番号": i + 1,
                                "投稿URL": f"https://www.instagram.com{href}" if not href.startswith('http') else href,
                                "サムネイルURL": src,
                                "alt": alt
                            }
                            posts_data.append(post_data)
                            print(f"  投稿 {i+1}: {href}")
                            break
                    except:
                        parent = parent.locator('..')
            except Exception as e:
                print(f"  ⚠ 投稿 {i+1} の取得エラー: {e}")
                continue

        print(f"✓ 個別投稿データ取得完了: {len(posts_data)}件")

    except Exception as e:
        print(f"⚠ コンテンツデータ取得エラー: {e}")
        import traceback
        traceback.print_exc()

    return posts_data


def save_to_csv(summary_data, posts_data):
    """データをCSVファイルに保存"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # サマリーデータを保存
    summary_file = DATA_DIR / f"instagram_summary_{timestamp}.csv"
    summary_df = pd.DataFrame([summary_data])
    summary_df.to_csv(summary_file, index=False, encoding='utf-8-sig')
    print(f"✓ サマリーデータ保存: {summary_file}")

    # 投稿データを保存
    if posts_data:
        posts_file = DATA_DIR / f"instagram_posts_{timestamp}.csv"
        posts_df = pd.DataFrame(posts_data)
        posts_df.to_csv(posts_file, index=False, encoding='utf-8-sig')
        print(f"✓ 投稿データ保存: {posts_file}")
    else:
        print("⚠ 投稿データがないため、CSVは作成されませんでした")


def main():
    """メイン処理"""
    print("=" * 60)
    print("Instagram Insights Webスクレイピング (v3 - 完全版)")
    print("=" * 60)

    with sync_playwright() as p:
        # ブラウザを起動
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_STATE_DIR),
            headless=False,
            viewport={'width': 1280, 'height': 1024}
        )

        page = browser.new_page()

        try:
            # アカウントサマリーデータ取得
            summary_data = extract_account_summary(page)

            # 個別投稿データ取得
            posts_data = extract_content_data(page)

            # CSV保存
            save_to_csv(summary_data, posts_data)

            print("\n" + "=" * 60)
            print("✓ データ取得完了")
            print(f"  サマリー: 1件")
            print(f"  投稿: {len(posts_data)}件")
            print("=" * 60)

        except Exception as e:
            print(f"\n✗ エラー発生: {e}")
            import traceback
            traceback.print_exc()

        finally:
            # ブラウザを閉じる
            print("\nブラウザを閉じます...")
            browser.close()


if __name__ == "__main__":
    main()
