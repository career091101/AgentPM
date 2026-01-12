#!/usr/bin/env python3
"""
Instagram Web版Insightsページからデータをスクレイピングするスクリプト

使用方法:
1. 初回実行時にブラウザが開き、Instagramにログインを求められます
2. 手動でログインしてください
3. ログイン状態が保存され、次回から自動実行されます
4. 過去90日間の投稿データをCSVファイルに保存します

依存関係:
pip install playwright pandas python-dotenv
playwright install chromium
"""

import os
import json
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
INSIGHTS_URL = "https://www.instagram.com/accounts/insights/content/?media_type=all&metric=views&sort_by=highest&timeframe=90&view_type=card"


def wait_for_login(page, timeout=300000):
    """ログインページを検出し、ユーザーがログインするまで待機"""
    print("Instagramにログインしてください...")
    print("ログイン完了後、Insightsページが表示されるまで自動的に待機します")

    try:
        # Insightsページの特徴的な要素が表示されるまで待機（最大5分）
        page.wait_for_selector('text=コンテンツインサイト', timeout=timeout)
        print("✓ ログイン成功")
        return True
    except PlaywrightTimeout:
        print("✗ タイムアウト: ログインページの読み込みに失敗しました")
        return False


def extract_account_summary(page):
    """アカウント全体のサマリーデータを取得"""
    print("\nアカウントサマリーデータを取得中...")

    # アカウントインサイトページに移動
    page.goto("https://www.instagram.com/accounts/insights/?timeframe=90")
    time.sleep(3)

    summary_data = {
        "期間": "過去90日間",
        "取得日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        # 閲覧数
        views_element = page.locator('text=閲覧').locator('..').locator('h2').first
        if views_element:
            summary_data["総閲覧数"] = views_element.inner_text()

        # リーチしたアカウント数
        reach_element = page.locator('text=リーチしたアカウント数').locator('..').locator('text=/^[0-9]+$/').first
        if reach_element:
            summary_data["リーチしたアカウント数"] = reach_element.inner_text()

        # インタラクション
        interaction_element = page.locator('text=インタラクション').locator('..').locator('h2').first
        if interaction_element:
            summary_data["総インタラクション数"] = interaction_element.inner_text()

        # プロフィールアクティビティ
        profile_element = page.locator('text=プロフィールのアクティビティ').locator('..').locator('h2').first
        if profile_element:
            summary_data["プロフィールアクティビティ"] = profile_element.inner_text()

        # フォロワー数
        followers_element = page.locator('text=合計フォロワー').locator('..').locator('h2').first
        if followers_element:
            summary_data["フォロワー数"] = followers_element.inner_text()

        print(f"✓ アカウントサマリー取得完了: {summary_data}")

    except Exception as e:
        print(f"⚠ サマリー取得エラー: {e}")

    return summary_data


def extract_content_insights(page):
    """コンテンツインサイトから投稿データを取得"""
    print("\nコンテンツインサイトデータを取得中...")

    # コンテンツインサイトページに移動
    page.goto(INSIGHTS_URL)
    time.sleep(3)

    posts_data = []

    try:
        # 表示形式をリストビューに変更（メトリクスを視覚的に確認しやすくする）
        # ※ただし、Web版UIの制約により、カードビューのままで情報取得を試みる

        # すべての投稿ボタンを取得
        post_buttons = page.locator('main button').all()
        print(f"投稿数: {len(post_buttons)}件")

        # 各投稿をクリックして詳細を取得
        for index in range(min(len(post_buttons), 50)):  # 最大50投稿まで
            try:
                print(f"投稿 {index + 1}/{len(post_buttons)} を処理中...")

                # 投稿をクリック
                post_buttons[index].click()
                time.sleep(2)

                # モーダルが開くのを待つ
                page.wait_for_selector('[role="dialog"]', timeout=10000)

                post_data = {
                    "投稿番号": index + 1,
                    "投稿日時": "",
                    "メディアタイプ": "",
                    "インプレッション数": "",
                    "リーチ数": "",
                    "エンゲージメント数": "",
                    "いいね数": "",
                    "コメント数": "",
                    "保存数": "",
                    "シェア数": ""
                }

                # モーダル内からデータを抽出（Instagram UIの構造に依存）
                # ※Instagram Web UIは頻繁に変更されるため、複数のセレクタを試行
                dialog = page.locator('[role="dialog"]').first

                # 投稿日時を取得
                time_elements = dialog.locator('time').all()
                if time_elements:
                    post_data["投稿日時"] = time_elements[0].get_attribute('datetime') or time_elements[0].inner_text()

                # メディアタイプを判定
                if dialog.locator('img[alt*="リール"]').count() > 0:
                    post_data["メディアタイプ"] = "リール動画"
                elif dialog.locator('img[alt*="カルーセル"]').count() > 0:
                    post_data["メディアタイプ"] = "カルーセル"
                elif dialog.locator('img[alt*="ストーリーズ"]').count() > 0:
                    post_data["メディアタイプ"] = "ストーリーズ"
                else:
                    post_data["メディアタイプ"] = "画像投稿"

                # メトリクスを取得（Insights専用のモーダルから）
                # ※Web版は詳細なメトリクスを表示しない場合があるため、取得可能な範囲で記録
                metrics_text = dialog.inner_text()

                # いいね数を抽出
                like_match = page.locator('text=/いいね.*[0-9]+件/').first
                if like_match:
                    post_data["いいね数"] = like_match.inner_text()

                # コメント数を抽出
                comment_match = page.locator('text=/コメント.*[0-9]+件/').first
                if comment_match:
                    post_data["コメント数"] = comment_match.inner_text()

                posts_data.append(post_data)

                # モーダルを閉じる
                close_button = dialog.locator('button[aria-label*="閉じる"], button[aria-label*="Close"]').first
                if close_button:
                    close_button.click()
                    time.sleep(1)
                else:
                    # Escapeキーで閉じる
                    page.keyboard.press('Escape')
                    time.sleep(1)

            except PlaywrightTimeout:
                print(f"⚠ 投稿 {index + 1} のタイムアウト（スキップ）")
                continue
            except Exception as e:
                print(f"⚠ 投稿 {index + 1} の処理エラー: {e}")
                # エラー時はモーダルを閉じる試行
                page.keyboard.press('Escape')
                time.sleep(1)
                continue

        print(f"✓ {len(posts_data)}件の投稿データを取得しました")

    except Exception as e:
        print(f"✗ コンテンツインサイト取得エラー: {e}")

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
        print("⚠ 投稿データが空のため、CSVファイルは作成されませんでした")


def main():
    """メイン処理"""
    print("=" * 60)
    print("Instagram Insights Webスクレイピング")
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
            if "login" in page.url:
                if not wait_for_login(page):
                    print("✗ ログインに失敗しました")
                    return

            # データ取得
            summary_data = extract_account_summary(page)
            posts_data = extract_content_insights(page)

            # CSV保存
            save_to_csv(summary_data, posts_data)

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
