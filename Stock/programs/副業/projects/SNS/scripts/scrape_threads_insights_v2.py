#!/usr/bin/env python3
"""
Threads 週間総括ページからデータをスクレイピングするスクリプト (改良版)

デバッグ結果に基づいて週間総括ページに特化しました。
フォロワー100人未満でも利用可能な週間総括データを取得します。
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
DATA_DIR = PROJECT_ROOT / "Threads"
DATA_DIR.mkdir(exist_ok=True)

# ブラウザ状態保存ディレクトリ
BROWSER_STATE_DIR = PROJECT_ROOT / ".browser_state"
BROWSER_STATE_DIR.mkdir(exist_ok=True)

# Threads 週間総括 URL
THREADS_WEEKLY_RECAP_URL = "https://www.threads.com/insights/weekly_recap?xmt=AQF0fRzSJPDc1cQ3HORNSmykkoBYA3Ug__fhworAp2V9DZI"


def extract_weekly_recap_data(page):
    """週間総括データを取得（改良版）"""
    print("\n週間総括データを取得中...")

    # 週間総括ページに移動
    page.goto(THREADS_WEEKLY_RECAP_URL)
    time.sleep(8)  # ページ読み込み待機

    weekly_data = {
        "取得日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "データソース": "週間総括"
    }

    try:
        # すべてのspan要素から数値を取得
        span_elements = page.locator('span').all()
        numeric_values = []

        for elem in span_elements:
            try:
                text = elem.inner_text().strip()
                # 数値（カンマ含む）を抽出
                if text.replace(',', '').isdigit():
                    numeric_values.append(text)
            except:
                pass

        print(f"  抽出した数値: {numeric_values}")

        # キーワードでデータを特定
        # "投稿X件" のパターン
        try:
            posts_elem = page.locator('text=投稿').first
            posts_text = posts_elem.inner_text()
            # "投稿3件" から "3" を抽出
            posts_count = ''.join(filter(str.isdigit, posts_text))
            if posts_count:
                weekly_data["投稿数"] = posts_count
                print(f"  投稿数: {posts_count}")
        except:
            print("  ⚠ 投稿数の取得に失敗")

        # span要素の順番から推測（デバッグ結果: ['3', '267', '0', '2']）
        # 0番目: 投稿数 (既に取得済み)
        # 1番目: 表示回数/インプレッション
        # 2番目: 新規フォロワー
        # 3番目: 返信数

        if len(numeric_values) >= 2:
            weekly_data["表示回数"] = numeric_values[1]
            print(f"  表示回数: {numeric_values[1]}")

        if len(numeric_values) >= 3:
            weekly_data["新規フォロワー"] = numeric_values[2]
            print(f"  新規フォロワー: {numeric_values[2]}")

        if len(numeric_values) >= 4:
            weekly_data["返信数"] = numeric_values[3]
            print(f"  返信数: {numeric_values[3]}")

        # キーワード確認（デバッグ用）
        keywords_found = []
        for keyword in ["投稿", "フォロワー", "返信"]:
            count = page.locator(f'text={keyword}').count()
            if count > 0:
                keywords_found.append(keyword)

        print(f"  確認されたキーワード: {keywords_found}")
        print(f"✓ 週間総括データ取得完了: {weekly_data}")

    except Exception as e:
        print(f"⚠ データ取得エラー: {e}")
        import traceback
        traceback.print_exc()

    return weekly_data


def save_to_csv(weekly_data):
    """データをCSVファイルに保存"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 週間総括データを保存
    weekly_file = DATA_DIR / f"threads_weekly_recap_{timestamp}.csv"
    weekly_df = pd.DataFrame([weekly_data])
    weekly_df.to_csv(weekly_file, index=False, encoding='utf-8-sig')
    print(f"✓ 週間総括データ保存: {weekly_file}")


def main():
    """メイン処理"""
    print("=" * 60)
    print("Threads 週間総括 Webスクレイピング (改良版)")
    print("=" * 60)
    print("\n注意: Threads Insightsは100人フォロワー制限があります。")
    print("      週間総括データは誰でも利用可能です。")

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
            weekly_data = extract_weekly_recap_data(page)

            # CSV保存
            save_to_csv(weekly_data)

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
