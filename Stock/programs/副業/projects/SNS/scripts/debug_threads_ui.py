#!/usr/bin/env python3
"""
Threads Insights ページの構造をデバッグするスクリプト

正しい要素セレクタとログイン問題を特定します。
"""

import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent
BROWSER_STATE_DIR = PROJECT_ROOT / ".browser_state"
DEBUG_DIR = PROJECT_ROOT / "debug_screenshots"
DEBUG_DIR.mkdir(exist_ok=True)

# Threads URLs
THREADS_INSIGHTS_HOME = "https://www.threads.com/insights?days=90"
THREADS_WEEKLY_RECAP = "https://www.threads.com/insights/weekly_recap?xmt=AQF0fRzSJPDc1cQ3HORNSmykkoBYA3Ug__fhworAp2V9DZI"


def debug_page(page, page_name, url):
    """ページの情報をデバッグ出力"""
    print(f"\n{'=' * 60}")
    print(f"デバッグ: {page_name}")
    print(f"{'=' * 60}")

    # 現在のURL
    print(f"URL: {page.url}")

    # スクリーンショット保存
    screenshot_path = DEBUG_DIR / f"threads_{page_name}.png"
    page.screenshot(path=str(screenshot_path), full_page=True)
    print(f"✓ スクリーンショット保存: {screenshot_path}")

    # ページタイトル
    print(f"タイトル: {page.title()}")

    # 見出し要素を探す
    print("\n【見出し要素 (h1, h2, h3, h4)】")
    for tag in ['h1', 'h2', 'h3', 'h4']:
        elements = page.locator(tag).all()
        for i, elem in enumerate(elements[:10]):
            try:
                text = elem.inner_text()
                print(f"  {tag}[{i}]: {text[:100]}")
            except:
                pass

    # span要素（数値データ候補）
    print("\n【span要素（数値データ候補）】")
    spans = page.locator('span').all()
    numeric_spans = []
    for span in spans[:50]:  # 最初の50個をチェック
        try:
            text = span.inner_text().strip()
            # 数値またはカンマ区切りの数値をチェック
            if text and (text.replace(',', '').isdigit() or text.replace('.', '').replace('K', '').replace('M', '').isdigit()):
                numeric_spans.append(text)
        except:
            pass
    print(f"  数値を含むspan要素: {numeric_spans[:20]}")

    # 特定のキーワードを含む要素を検索
    print("\n【キーワード検索】")
    keywords = [
        # 日本語
        "洞察", "インサイト", "投稿", "フォロワー", "表示", "返信", "週間総括",
        # 英語
        "Insights", "Posts", "Followers", "Views", "Replies", "Weekly recap",
        "Engagement"
    ]

    for keyword in keywords:
        count = page.locator(f'text={keyword}').count()
        if count > 0:
            print(f"  '{keyword}': {count}個見つかりました")
            try:
                first = page.locator(f'text={keyword}').first
                print(f"    最初の要素: {first.inner_text()[:100]}")
            except:
                pass

    # div要素でデータカードを探す
    print("\n【div要素（データカード候補）】")
    divs_with_role = page.locator('div[role]').all()
    print(f"  role属性を持つdiv要素数: {len(divs_with_role)}個")
    for i, div in enumerate(divs_with_role[:10]):
        try:
            role = div.get_attribute('role')
            text = div.inner_text()
            print(f"  div[{i}]: role={role}, text={text[:100]}")
        except:
            pass

    # main要素の存在確認
    main_count = page.locator('main').count()
    print(f"\n【main要素】: {main_count}個")
    if main_count > 0:
        try:
            main_text = page.locator('main').first.inner_text()
            print(f"  main要素のテキスト（最初の500文字）: {main_text[:500]}")
        except:
            pass

    # ログイン状態の確認
    print("\n【ログイン状態確認】")
    login_keywords = ["ログイン", "Login", "Sign in", "続ける", "Continue"]
    is_logged_in = True
    for keyword in login_keywords:
        count = page.locator(f'text={keyword}').count()
        if count > 0:
            print(f"  ⚠️ '{keyword}' が見つかりました - ログインページの可能性")
            is_logged_in = False

    if is_logged_in:
        print(f"  ✓ ログイン済みと推定")

    # HTML構造をファイルに保存
    html_path = DEBUG_DIR / f"threads_{page_name}.html"
    try:
        html_content = page.content()
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"\n✓ HTML保存: {html_path}")
    except Exception as e:
        print(f"\n✗ HTML保存エラー: {e}")


def main():
    """メイン処理"""
    print("=" * 60)
    print("Threads Insights UI デバッグ")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_STATE_DIR),
            headless=False,
            viewport={'width': 1280, 'height': 1024}
        )

        page = browser.new_page()

        try:
            # 1. Insights ホームページ
            print(f"\n1. Threads Insights ホームページにアクセス...")
            page.goto(THREADS_INSIGHTS_HOME)
            time.sleep(8)  # ページ読み込み待機
            debug_page(page, "insights_home", THREADS_INSIGHTS_HOME)

            # 2. 週間総括ページ
            print(f"\n2. Threads 週間総括ページにアクセス...")
            page.goto(THREADS_WEEKLY_RECAP)
            time.sleep(8)  # ページ読み込み待機
            debug_page(page, "weekly_recap", THREADS_WEEKLY_RECAP)

            # 3. スクロールして動的コンテンツを読み込む
            print(f"\n3. ページをスクロールして動的コンテンツを読み込み...")
            for i in range(3):
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                print(f"  スクロール {i+1}/3")

            screenshot_path = DEBUG_DIR / "threads_scrolled.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"✓ スクロール後のスクリーンショット: {screenshot_path}")

            print("\n" + "=" * 60)
            print("デバッグ完了")
            print("=" * 60)
            print(f"\n結果の確認:")
            print(f"  スクリーンショット: {DEBUG_DIR}/threads_*.png")
            print(f"  HTMLファイル: {DEBUG_DIR}/threads_*.html")
            print("\nこれらのファイルを確認して、正しい要素セレクタを特定してください。")

            # ブラウザを開いたまま待機（手動確認用）
            print("\n5秒後に自動的にブラウザを閉じます...")
            time.sleep(5)

        except Exception as e:
            print(f"\n✗ エラー発生: {e}")
            import traceback
            traceback.print_exc()

        finally:
            browser.close()


if __name__ == "__main__":
    main()
