#!/usr/bin/env python3
"""
Threads Web版Insightsページからデータをスクレイピングするスクリプト

使用方法:
1. 初回実行時にブラウザが開き、Threadsにログインを求められます
2. 手動でログインしてください（Instagramと同じアカウント）
3. ログイン状態が保存され、次回から自動実行されます
4. 週間総括データをCSVファイルに保存します

注意:
- Threadsの洞察データはフォロワー100人以上で利用可能
- フォロワー100人未満の場合は週間総括のみ取得可能

依存関係:
pip install playwright pandas python-dotenv
playwright install chromium
"""

import os
import json
import time
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# プロジェクトルートディレクトリ
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "Threads"
DATA_DIR.mkdir(exist_ok=True)

# ブラウザ状態保存ディレクトリ（Instagramと共有）
BROWSER_STATE_DIR = PROJECT_ROOT / ".browser_state"
BROWSER_STATE_DIR.mkdir(exist_ok=True)

# Threads Insights URL
INSIGHTS_URL = "https://www.threads.com/insights?days=90"
WEEKLY_RECAP_URL = "https://www.threads.com/insights/weekly_recap/"


def wait_for_login(page, timeout=300000):
    """ログインページを検出し、ユーザーがログインするまで待機"""
    print("Threadsにログインしてください...")
    print("ログイン完了後、Insightsページが表示されるまで自動的に待機します")

    try:
        # Insightsページの特徴的な要素が表示されるまで待機（最大5分）
        page.wait_for_selector('text=洞察', timeout=timeout)
        print("✓ ログイン成功")
        return True
    except PlaywrightTimeout:
        print("✗ タイムアウト: ログインページの読み込みに失敗しました")
        return False


def check_follower_requirement(page):
    """フォロワー数が100人以上かチェック"""
    try:
        # 「洞察が待っています」メッセージの有無を確認
        waiting_message = page.locator('text=洞察が待っています').count()
        if waiting_message > 0:
            print("⚠ フォロワー数が100人未満のため、詳細な洞察データは利用できません")
            print("  週間総括データのみ取得します")
            return False
        else:
            print("✓ 詳細な洞察データが利用可能です")
            return True
    except Exception as e:
        print(f"⚠ フォロワー数チェックエラー: {e}")
        return False


def extract_weekly_recap_data(page):
    """週間総括データを取得"""
    print("\n週間総括データを取得中...")

    # 週間総括ページに移動
    page.goto(WEEKLY_RECAP_URL)
    time.sleep(3)

    weekly_data = []

    try:
        # ページ内のテキストを全て取得
        page_text = page.locator('main').inner_text()

        # 期間を抽出（例: "12月24日から12月31日"）
        period_match = page.locator('text=/[0-9]+月[0-9]+日から[0-9]+月[0-9]+日/').first
        period = period_match.inner_text() if period_match.count() > 0 else ""

        # 各メトリクスを抽出
        metrics = {}

        # 投稿数
        posts_section = page.locator('text=つのポスト').locator('..')
        if posts_section.count() > 0:
            posts_text = posts_section.first.inner_text()
            # "3つのポスト"から数字を抽出
            import re
            posts_match = re.search(r'(\d+)', posts_text)
            if posts_match:
                metrics["投稿数"] = posts_match.group(1)

        # 表示モード（ビュー数）
        views_section = page.locator('text=表示モード').locator('..')
        if views_section.count() > 0:
            # 次の要素から数字を取得
            views_elements = page.locator('text=/^[0-9]+$/').all()
            for elem in views_elements:
                text = elem.inner_text()
                if text.isdigit():
                    metrics["表示モード"] = text
                    break

        # 返信数
        replies_section = page.locator('text=返信').locator('..')
        if replies_section.count() > 0:
            replies_elements = page.locator('text=/^[0-9]+$/').all()
            # 表示モードの次の数字が返信数
            count = 0
            for elem in replies_elements:
                text = elem.inner_text()
                if text.isdigit():
                    count += 1
                    if count == 2:  # 2番目の数字が返信数
                        metrics["返信数"] = text
                        break

        # 新たなフォロワー
        followers_section = page.locator('text=新たなフォロワー').locator('..')
        if followers_section.count() > 0:
            # 直後の数字要素を取得
            next_sibling = page.locator('text=新たなフォロワー').locator('..').locator('..').locator('text=/^[0-9]+$/').first
            if next_sibling.count() > 0:
                metrics["新たなフォロワー"] = next_sibling.inner_text()

        # データを構造化
        weekly_data.append({
            "期間": period,
            "取得日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "投稿数": metrics.get("投稿数", "0"),
            "表示モード": metrics.get("表示モード", "0"),
            "返信数": metrics.get("返信数", "0"),
            "新たなフォロワー": metrics.get("新たなフォロワー", "0")
        })

        print(f"✓ 週間総括データ取得完了: {weekly_data[0]}")

    except Exception as e:
        print(f"✗ 週間総括データ取得エラー: {e}")
        import traceback
        traceback.print_exc()

    return weekly_data


def extract_insights_data(page):
    """洞察データを取得（フォロワー100人以上の場合）"""
    print("\n洞察データを取得中...")

    # 洞察ページに移動
    page.goto(INSIGHTS_URL)
    time.sleep(3)

    insights_data = {
        "期間": "過去90日間",
        "取得日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        # ページ内のメトリクスを取得
        # ※Threads UIの構造に応じて調整が必要

        # 総ビュー数
        views_element = page.locator('text=ビュー').locator('..').locator('text=/^[0-9,]+$/').first
        if views_element.count() > 0:
            insights_data["総ビュー数"] = views_element.inner_text()

        # エンゲージメント
        engagement_element = page.locator('text=エンゲージメント').locator('..').locator('text=/^[0-9,]+$/').first
        if engagement_element.count() > 0:
            insights_data["総エンゲージメント数"] = engagement_element.inner_text()

        # フォロワー数
        followers_element = page.locator('text=フォロワー').locator('..').locator('text=/^[0-9,]+$/').first
        if followers_element.count() > 0:
            insights_data["フォロワー数"] = followers_element.inner_text()

        print(f"✓ 洞察データ取得完了: {insights_data}")

    except Exception as e:
        print(f"⚠ 洞察データ取得エラー: {e}")

    return insights_data


def save_to_csv(weekly_data, insights_data=None):
    """データをCSVファイルに保存"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 週間総括データを保存
    if weekly_data:
        weekly_file = DATA_DIR / f"threads_weekly_recap_{timestamp}.csv"
        weekly_df = pd.DataFrame(weekly_data)
        weekly_df.to_csv(weekly_file, index=False, encoding='utf-8-sig')
        print(f"✓ 週間総括データ保存: {weekly_file}")
    else:
        print("⚠ 週間総括データが空のため、CSVファイルは作成されませんでした")

    # 洞察データを保存（フォロワー100人以上の場合）
    if insights_data and isinstance(insights_data, dict) and len(insights_data) > 2:
        insights_file = DATA_DIR / f"threads_insights_{timestamp}.csv"
        insights_df = pd.DataFrame([insights_data])
        insights_df.to_csv(insights_file, index=False, encoding='utf-8-sig')
        print(f"✓ 洞察データ保存: {insights_file}")


def main():
    """メイン処理"""
    print("=" * 60)
    print("Threads Insights Webスクレイピング")
    print("=" * 60)

    with sync_playwright() as p:
        # ブラウザを起動（ヘッドレスモード無効 = ブラウザウィンドウを表示）
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_STATE_DIR),
            headless=False,  # ログイン時にブラウザを表示
            viewport={'width': 1280, 'height': 1024}
        )

        page = browser.new_page()

        try:
            # Insightsページにアクセス
            print(f"\nInsightsページにアクセス: {INSIGHTS_URL}")
            page.goto(INSIGHTS_URL)
            time.sleep(3)

            # ログインが必要な場合は待機
            if "login" in page.url or page.locator('text=ログイン').count() > 0:
                if not wait_for_login(page):
                    print("✗ ログインに失敗しました")
                    return

            # フォロワー数チェック
            has_insights = check_follower_requirement(page)

            # 週間総括データ取得（常に実行）
            weekly_data = extract_weekly_recap_data(page)

            # 洞察データ取得（フォロワー100人以上の場合）
            insights_data = None
            if has_insights:
                insights_data = extract_insights_data(page)

            # CSV保存
            save_to_csv(weekly_data, insights_data)

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
