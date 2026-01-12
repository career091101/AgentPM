#!/usr/bin/env python3
"""
Instagram Insights コンテンツページの構造をデバッグするスクリプト

個別投稿データの取得に必要な要素セレクタを特定します。
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

# Instagram コンテンツページURL
INSIGHTS_CONTENT = "https://www.instagram.com/accounts/insights/content/?media_type=all&metric=accounts_engaged&sort_by=highest&timeframe=90&view_type=card"


def debug_content_page(page):
    """コンテンツページの情報をデバッグ出力"""
    print(f"\n{'=' * 60}")
    print(f"デバッグ: Instagram コンテンツページ")
    print(f"{'=' * 60}")

    # 現在のURL
    print(f"URL: {page.url}")

    # スクリーンショット保存
    screenshot_path = DEBUG_DIR / "instagram_content_debug.png"
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

    # article要素（投稿カード）を探す
    print("\n【article要素（投稿カード候補）】")
    articles = page.locator('article').all()
    print(f"  article要素数: {len(articles)}個")
    for i, article in enumerate(articles[:3]):
        try:
            text = article.inner_text()
            print(f"  article[{i}]: {text[:200]}")
        except:
            pass

    # div要素で投稿を探す
    print("\n【div[role='button']要素（クリック可能な投稿候補）】")
    clickable_divs = page.locator('div[role="button"]').all()
    print(f"  クリック可能なdiv要素数: {len(clickable_divs)}個")
    for i, div in enumerate(clickable_divs[:5]):
        try:
            text = div.inner_text()
            aria_label = div.get_attribute('aria-label')
            print(f"  div[{i}]: aria-label={aria_label}, text={text[:100]}")
        except:
            pass

    # a要素（リンク）を探す
    print("\n【a要素（投稿リンク候補）】")
    links = page.locator('a').all()
    print(f"  リンク要素数: {len(links)}個")
    for i, link in enumerate(links[:10]):
        try:
            href = link.get_attribute('href')
            text = link.inner_text()
            if '/p/' in href or '/reel/' in href:  # 投稿リンクの可能性
                print(f"  a[{i}]: href={href}, text={text[:50]}")
        except:
            pass

    # img要素（サムネイル）を探す
    print("\n【img要素（投稿サムネイル候補）】")
    images = page.locator('img').all()
    print(f"  画像要素数: {len(images)}個")
    for i, img in enumerate(images[:5]):
        try:
            alt = img.get_attribute('alt')
            src = img.get_attribute('src')
            print(f"  img[{i}]: alt={alt}, src={src[:100] if src else 'None'}")
        except:
            pass

    # 数値を含む要素を探す（インプレッション、リーチなど）
    print("\n【数値データ要素】")
    for keyword in ["インプレッション", "リーチ", "エンゲージメント", "いいね", "コメント", "保存", "シェア"]:
        count = page.locator(f'text={keyword}').count()
        if count > 0:
            print(f"  '{keyword}': {count}個見つかりました")
            try:
                first = page.locator(f'text={keyword}').first
                parent_text = first.locator('..').inner_text()
                print(f"    親要素のテキスト: {parent_text[:200]}")
            except:
                pass

    # スクロール可能なコンテナを探す
    print("\n【スクロール可能なコンテナ】")
    scrollable = page.locator('[style*="overflow"]').all()
    print(f"  スクロール可能要素数: {len(scrollable)}個")

    # HTML構造をファイルに保存
    html_path = DEBUG_DIR / "instagram_content_debug.html"
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
    print("Instagram Insights コンテンツページ デバッグ")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_STATE_DIR),
            headless=False,
            viewport={'width': 1280, 'height': 1024}
        )

        page = browser.new_page()

        try:
            # コンテンツページにアクセス
            print(f"\nコンテンツページにアクセス...")
            page.goto(INSIGHTS_CONTENT)
            time.sleep(8)  # ページ読み込み待機（動的コンテンツのため長めに）

            # デバッグ情報出力
            debug_content_page(page)

            # スクロールして追加のコンテンツを読み込む
            print(f"\nページをスクロールして動的コンテンツを読み込み...")
            for i in range(3):
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                print(f"  スクロール {i+1}/3")

            # スクロール後のスクリーンショット
            screenshot_path = DEBUG_DIR / "instagram_content_scrolled.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"✓ スクロール後のスクリーンショット: {screenshot_path}")

            print("\n" + "=" * 60)
            print("デバッグ完了")
            print("=" * 60)
            print(f"\n結果の確認:")
            print(f"  スクリーンショット: {DEBUG_DIR}/instagram_content_debug.png")
            print(f"  スクロール後: {DEBUG_DIR}/instagram_content_scrolled.png")
            print(f"  HTMLファイル: {DEBUG_DIR}/instagram_content_debug.html")
            print("\nこれらのファイルを確認して、投稿データの要素セレクタを特定してください。")

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
