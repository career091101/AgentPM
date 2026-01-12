#!/usr/bin/env python3
"""
Instagram Insights ページの構造をデバッグするスクリプト

実際のページ構造を確認し、正しい要素セレクタを特定します。
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

# Instagram URLs
INSIGHTS_HOME = "https://www.instagram.com/accounts/insights/?timeframe=90"
INSIGHTS_CONTENT = "https://www.instagram.com/accounts/insights/content/?media_type=all&metric=views&sort_by=highest&timeframe=90&view_type=card"


def debug_page(page, page_name):
    """ページの情報をデバッグ出力"""
    print(f"\n{'=' * 60}")
    print(f"デバッグ: {page_name}")
    print(f"{'=' * 60}")

    # 現在のURL
    print(f"URL: {page.url}")

    # スクリーンショット保存
    screenshot_path = DEBUG_DIR / f"{page_name}.png"
    page.screenshot(path=str(screenshot_path))
    print(f"✓ スクリーンショット保存: {screenshot_path}")

    # ページタイトル
    print(f"タイトル: {page.title()}")

    # main要素の存在確認
    main_count = page.locator('main').count()
    print(f"main要素: {main_count}個")

    # 見出し要素を探す
    print("\n【見出し要素 (h1, h2, h3)】")
    for tag in ['h1', 'h2', 'h3']:
        elements = page.locator(tag).all()
        for i, elem in enumerate(elements[:5]):  # 最初の5個まで
            try:
                text = elem.inner_text()
                print(f"  {tag}[{i}]: {text}")
            except:
                pass

    # ページ内のテキストを部分的に取得
    print("\n【ページテキスト（最初の500文字）】")
    try:
        main_text = page.locator('main').inner_text()
        print(main_text[:500])
    except Exception as e:
        print(f"  エラー: {e}")

    # 特定のキーワードを含む要素を検索
    print("\n【キーワード検索】")
    keywords = ["閲覧", "インプレッション", "リーチ", "エンゲージメント", "フォロワー",
                "コンテンツ", "インサイト", "アカウント"]

    for keyword in keywords:
        count = page.locator(f'text={keyword}').count()
        if count > 0:
            print(f"  '{keyword}': {count}個見つかりました")
            try:
                first = page.locator(f'text={keyword}').first
                print(f"    最初の要素: {first.inner_text()}")
            except:
                pass

    # ボタン要素
    print("\n【ボタン要素】")
    buttons = page.locator('button').all()
    print(f"  ボタン総数: {len(buttons)}個")
    for i, btn in enumerate(buttons[:10]):  # 最初の10個
        try:
            text = btn.inner_text()
            if text.strip():
                print(f"  button[{i}]: {text[:50]}")
        except:
            pass

    # HTML構造をファイルに保存
    html_path = DEBUG_DIR / f"{page_name}.html"
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
    print("Instagram Insights UI デバッグ")
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
            print(f"\n1. Insights ホームページにアクセス...")
            page.goto(INSIGHTS_HOME)
            time.sleep(5)  # ページ読み込み待機
            debug_page(page, "insights_home")

            # 2. Insights コンテンツページ
            print(f"\n2. Insights コンテンツページにアクセス...")
            page.goto(INSIGHTS_CONTENT)
            time.sleep(5)  # ページ読み込み待機
            debug_page(page, "insights_content")

            # 3. スクロールして動的コンテンツを読み込む
            print(f"\n3. ページをスクロールして動的コンテンツを読み込み...")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)

            screenshot_path = DEBUG_DIR / "insights_content_scrolled.png"
            page.screenshot(path=str(screenshot_path))
            print(f"✓ スクロール後のスクリーンショット: {screenshot_path}")

            print("\n" + "=" * 60)
            print("デバッグ完了")
            print("=" * 60)
            print(f"\n結果の確認:")
            print(f"  スクリーンショット: {DEBUG_DIR}/")
            print(f"  HTMLファイル: {DEBUG_DIR}/")
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
