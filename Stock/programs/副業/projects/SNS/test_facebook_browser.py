#!/usr/bin/env python3
"""
Facebook投稿ブラウザ操作テスト（投稿直前で停止）
Playwrightを使用してブラウザ自動操作
"""
import json
import time
from playwright.sync_api import sync_playwright

def load_facebook_post():
    """Facebook投稿内容を読み込み"""
    data_file = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/posts_generated_ai_20260102.json"

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 案2（衝撃発言型）の全文を取得
    approved_post = data["posts"][1]

    return approved_post["content"]

def test_facebook_post_browser():
    """ブラウザでFacebook投稿テスト（投稿直前で停止）"""

    print("=" * 60)
    print("Facebook投稿ブラウザ操作テスト")
    print("=" * 60)

    # 投稿内容読み込み
    print("\n📂 投稿内容読み込み中...")
    post_content = load_facebook_post()
    print(f"✅ 読み込み完了: {len(post_content)}字")

    print("\n🌐 ブラウザ起動中...")

    with sync_playwright() as p:
        # ブラウザ起動（headless=False で画面表示）
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        # クッキーファイルを読み込み
        print("   クッキー読み込み中...")
        try:
            with open("facebook_cookies.json", "r") as f:
                storage_state = json.load(f)

            # クッキーを使用してコンテキスト作成
            context = browser.new_context(storage_state=storage_state)
            print("   ✅ クッキー読み込み成功（ログイン済み状態）")
        except FileNotFoundError:
            print("   ⚠️  クッキーファイルが見つかりません（手動ログインが必要）")
            context = browser.new_context()

        page = context.new_page()

        try:
            # Step 1: Facebookにアクセス
            print("\n📍 Step 1: Facebookにアクセス中...")
            page.goto("https://www.facebook.com", wait_until="networkidle")
            print("✅ Facebook読み込み完了")

            # ログイン状態確認
            print("\n🔍 ログイン状態確認中...")
            time.sleep(3)

            # ログインボタンが表示されている場合は未ログイン
            if page.locator("input[name='email']").is_visible():
                print("⚠️  Facebookに未ログインです")
                print("\n" + "-" * 60)
                print("📌 手動操作が必要:")
                print("-" * 60)
                print("1. ブラウザウィンドウでFacebookにログインしてください")
                print("2. 60秒後に自動的に続行します")
                print("-" * 60)
                print("\n⏳ 60秒待機中...")
                time.sleep(60)

                # ログイン後にホームページを再読み込み
                page.goto("https://www.facebook.com", wait_until="networkidle")
                time.sleep(3)

            print("✅ ログイン確認完了")

            # Step 2: 投稿ボックスを探す
            print("\n📍 Step 2: 投稿ボックスを検索中...")

            # 投稿ボックスのセレクタ候補（Facebookの仕様変更に対応）
            post_box_selectors = [
                "div[aria-label*='投稿を作成']",
                "div[aria-label*='今何してる']",
                "div[role='button'][tabindex='0']",
                "span:has-text('今何してる')",
                "div.x1i10hfl"  # Facebookの投稿ボックスクラス
            ]

            post_box = None
            for selector in post_box_selectors:
                try:
                    if page.locator(selector).first.is_visible():
                        post_box = page.locator(selector).first
                        print(f"✅ 投稿ボックス検出: {selector}")
                        break
                except:
                    continue

            if not post_box:
                print("⚠️  投稿ボックスが自動検出できませんでした")
                print("\n" + "-" * 60)
                print("📌 手動操作が必要:")
                print("-" * 60)
                print("1. ブラウザで「今何してる？」投稿ボックスをクリック")
                print("2. 30秒後に自動的に続行します")
                print("-" * 60)
                print("\n⏳ 30秒待機中...")
                time.sleep(30)
            else:
                # 投稿ボックスをクリック
                print("\n📍 Step 3: 投稿ボックスをクリック中...")
                post_box.click()
                time.sleep(2)
                print("✅ 投稿ボックスをクリック")

            # Step 4: 投稿エディタに文章を入力
            print("\n📍 Step 4: 投稿文を入力中...")

            # 投稿エディタのセレクタ候補
            editor_selectors = [
                "div[role='textbox'][contenteditable='true']",
                "div[aria-label*='投稿を作成']",
                "div.notranslate._5rpu"
            ]

            editor = None
            for selector in editor_selectors:
                try:
                    if page.locator(selector).first.is_visible():
                        editor = page.locator(selector).first
                        print(f"✅ エディタ検出: {selector}")
                        break
                except:
                    continue

            if not editor:
                print("⚠️  投稿エディタが自動検出できませんでした")
                print("\n" + "-" * 60)
                print("📌 手動操作:")
                print("-" * 60)
                print("投稿文をクリップボードにコピーしました。")
                print("ブラウザの投稿ボックスに貼り付けてください。")
                print("-" * 60)
            else:
                # エディタに投稿文を入力
                editor.click()
                time.sleep(1)

                # 投稿文を入力（一文字ずつゆっくり入力）
                print("   入力中...")
                editor.fill(post_content)
                time.sleep(2)
                print(f"✅ 投稿文入力完了: {len(post_content)}字")

            # Step 5: 投稿ボタンを探す（クリックはしない）
            print("\n📍 Step 5: 投稿ボタンを検索中...")

            post_button_selectors = [
                "div[aria-label='投稿']",
                "div[aria-label='Post']",
                "div[role='button']:has-text('投稿')",
                "div[role='button']:has-text('Post')"
            ]

            post_button = None
            for selector in post_button_selectors:
                try:
                    if page.locator(selector).first.is_visible():
                        post_button = page.locator(selector).first
                        print(f"✅ 投稿ボタン検出: {selector}")
                        break
                except:
                    continue

            if not post_button:
                print("⚠️  投稿ボタンが自動検出できませんでした")

            # テスト完了メッセージ
            print("\n" + "=" * 60)
            print("✅ Facebook投稿テスト完了（投稿直前で停止）")
            print("=" * 60)
            print("\n📝 投稿プレビュー:")
            print("-" * 60)
            print(post_content[:200] + "..." if len(post_content) > 200 else post_content)
            print("-" * 60)

            print("\n🛑 テストモード: 投稿ボタンはクリックしません")

            print("\n" + "-" * 60)
            print("📌 実際に投稿する場合:")
            print("-" * 60)
            print("ブラウザ画面で「投稿」ボタンをクリックしてください")
            print("-" * 60)

            # ブラウザを開いたままにする（60秒）
            print("\n⏸️  ブラウザを開いたままにします（60秒）")
            print("   投稿内容を確認してください")
            print("   60秒後に自動的にブラウザを閉じます")
            print("\n⏳ 60秒待機中...")
            for i in range(60, 0, -10):
                print(f"   残り {i} 秒...")
                time.sleep(10)

        except Exception as e:
            print(f"\n❌ エラー発生: {e}")
            print("\nブラウザを開いたままにします（30秒）")
            print("\n⏳ 30秒待機中...")
            time.sleep(30)

        finally:
            # ブラウザを閉じる
            print("\n🔒 ブラウザを閉じています...")
            context.close()
            browser.close()
            print("✅ ブラウザクローズ完了")

    print("\n" + "=" * 60)
    print("Facebook投稿ブラウザテスト完了")
    print("=" * 60)

if __name__ == "__main__":
    test_facebook_post_browser()
