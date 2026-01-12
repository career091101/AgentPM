#!/usr/bin/env python3
"""
Instagram Web版Insightsページからデータをスクレイピングするスクリプト (改良版)

デバッグ結果に基づいて要素セレクタを修正しました。
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

# Instagram Insights URL
INSIGHTS_HOME_URL = "https://www.instagram.com/accounts/insights/?timeframe=90"


def extract_account_summary(page):
    """アカウント全体のサマリーデータを取得（改良版）"""
    print("\nアカウントサマリーデータを取得中...")

    # Insightsホームページに移動
    page.goto(INSIGHTS_HOME_URL)
    time.sleep(5)  # ページ読み込み待機

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
                # 数値のみを抽出
                if text.replace(',', '').isdigit():
                    h1_values.append(text)
            except:
                pass

        print(f"  h1要素から取得した数値: {h1_values}")

        # 順番に基づいてデータを割り当て（デバッグ結果から）
        # h1[0]: 7021（ビュー）, h1[1]: 12（インタラクション）, h1[2]: 191（プロフィール）, h1[3]: 283（フォロワー）
        if len(h1_values) >= 1:
            summary_data["総ビュー数"] = h1_values[0]
        if len(h1_values) >= 2:
            summary_data["総インタラクション数"] = h1_values[1]
        if len(h1_values) >= 3:
            summary_data["プロフィールアクティビティ"] = h1_values[2]
        if len(h1_values) >= 4:
            summary_data["フォロワー数"] = h1_values[3]

        # キーワードで確認
        keywords_found = []
        for keyword in ["閲覧", "インタラクション", "プロフィール", "フォロワー"]:
            count = page.locator(f'text={keyword}').count()
            if count > 0:
                keywords_found.append(keyword)

        print(f"  確認されたキーワード: {keywords_found}")
        print(f"✓ サマリーデータ取得完了: {summary_data}")

    except Exception as e:
        print(f"⚠ サマリー取得エラー: {e}")
        import traceback
        traceback.print_exc()

    return summary_data


def save_to_csv(summary_data):
    """データをCSVファイルに保存"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # サマリーデータを保存
    summary_file = DATA_DIR / f"instagram_summary_{timestamp}.csv"
    summary_df = pd.DataFrame([summary_data])
    summary_df.to_csv(summary_file, index=False, encoding='utf-8-sig')
    print(f"✓ サマリーデータ保存: {summary_file}")


def main():
    """メイン処理"""
    print("=" * 60)
    print("Instagram Insights Webスクレイピング (改良版)")
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
            # データ取得
            summary_data = extract_account_summary(page)

            # CSV保存
            save_to_csv(summary_data)

            print("\n" + "=" * 60)
            print("✓ データ取得完了")
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
