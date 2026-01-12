#!/usr/bin/env python3
"""
Instagram Insightsページからスクリーンショット+OCRでデータを取得するスクリプト

DOM要素のスクレイピングではなく、スクリーンショットを撮影して
Claude APIの画像認識機能で文字起こしを行い、データを抽出します。
"""

import os
import time
import base64
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import anthropic

# 環境変数読み込み
load_dotenv()

# プロジェクトルートディレクトリ
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "Instagram"
DATA_DIR.mkdir(exist_ok=True)

# スクリーンショット保存ディレクトリ
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

# ブラウザ状態保存ディレクトリ
BROWSER_STATE_DIR = PROJECT_ROOT / ".browser_state"
BROWSER_STATE_DIR.mkdir(exist_ok=True)

# Instagram Insights URLs
INSIGHTS_HOME_URL = "https://www.instagram.com/accounts/insights/?timeframe=90"
INSIGHTS_CONTENT_URL = "https://www.instagram.com/accounts/insights/content/?media_type=all&metric=accounts_engaged&sort_by=highest&timeframe=90&view_type=card"


def take_screenshot(page, url, screenshot_name):
    """指定URLのスクリーンショットを撮影"""
    print(f"\n{screenshot_name}のスクリーンショットを撮影中...")

    # ページに移動
    page.goto(url)
    time.sleep(6)  # ページ読み込み待機

    # スクリーンショット保存
    screenshot_path = SCREENSHOT_DIR / f"{screenshot_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    page.screenshot(path=str(screenshot_path), full_page=False)

    print(f"✓ スクリーンショット保存: {screenshot_path}")
    return screenshot_path


def extract_data_with_claude(screenshot_path, data_type="summary"):
    """Claude APIでスクリーンショットからデータを抽出"""
    print(f"\nClaude APIで{data_type}データを抽出中...")

    # APIキー確認
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEYが設定されていません。\n"
            ".envファイルにAPIキーを設定してください。\n"
            "APIキーは https://console.anthropic.com/ から取得できます。"
        )

    # 画像を読み込んでBase64エンコード
    with open(screenshot_path, "rb") as image_file:
        image_data = base64.standard_b64encode(image_file.read()).decode("utf-8")

    # Claude APIクライアント初期化
    client = anthropic.Anthropic(api_key=api_key)

    # データタイプに応じたプロンプトを作成
    if data_type == "summary":
        prompt = """このInstagram Insightsページのスクリーンショットから、以下のデータを抽出してJSON形式で返してください：

必要なデータ：
- 総ビュー数（閲覧数）
- 総インタラクション数
- プロフィールアクティビティ
- フォロワー数

出力形式（JSON）：
{
    "総ビュー数": "7021",
    "総インタラクション数": "12",
    "プロフィールアクティビティ": "191",
    "フォロワー数": "283"
}

注意：
- 数値はカンマ区切りの文字列として返してください
- 数値が見つからない場合は "N/A" を返してください
- JSONのみを返し、他の説明は不要です"""

    elif data_type == "content":
        prompt = """このInstagram Insightsコンテンツページのスクリーンショットから、表示されている投稿の情報を抽出してJSON形式で返してください：

必要なデータ（各投稿ごと）：
- 投稿番号（1から順番に）
- インプレッション数（表示されている場合）
- リーチ数（表示されている場合）
- エンゲージメント数（表示されている場合）

出力形式（JSON配列）：
[
    {
        "投稿番号": 1,
        "インプレッション数": "1234",
        "リーチ数": "567",
        "エンゲージメント数": "89"
    },
    ...
]

注意：
- 数値はカンマ区切りの文字列として返してください
- 数値が見つからない場合は "N/A" を返してください
- JSONのみを返し、他の説明は不要です"""

    # Claude APIにリクエスト
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ],
                }
            ],
        )

        # レスポンスからテキストを取得
        response_text = message.content[0].text
        print(f"  Claude APIレスポンス: {response_text[:200]}...")

        # JSONをパース
        data = json.loads(response_text)
        print(f"✓ データ抽出完了")

        return data

    except Exception as e:
        print(f"✗ Claude API エラー: {e}")
        import traceback
        traceback.print_exc()
        return None


def save_to_csv(summary_data, posts_data=None):
    """データをCSVファイルに保存"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # サマリーデータを保存
    if summary_data:
        summary_data["期間"] = "過去90日間"
        summary_data["取得日時"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        summary_data["データソース"] = "OCR (Claude API)"

        summary_file = DATA_DIR / f"instagram_summary_ocr_{timestamp}.csv"
        summary_df = pd.DataFrame([summary_data])
        summary_df.to_csv(summary_file, index=False, encoding='utf-8-sig')
        print(f"✓ サマリーデータ保存: {summary_file}")

    # 投稿データを保存
    if posts_data:
        posts_file = DATA_DIR / f"instagram_posts_ocr_{timestamp}.csv"
        posts_df = pd.DataFrame(posts_data)
        posts_df.to_csv(posts_file, index=False, encoding='utf-8-sig')
        print(f"✓ 投稿データ保存: {posts_file}")


def main():
    """メイン処理"""
    print("=" * 60)
    print("Instagram Insights OCRスクレイピング")
    print("=" * 60)
    print("\n方式: スクリーンショット + Claude API 画像認識")

    with sync_playwright() as p:
        # ブラウザを起動
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_STATE_DIR),
            headless=False,
            viewport={'width': 1280, 'height': 1024}
        )

        page = browser.new_page()

        try:
            # 1. Insightsホームページのスクリーンショット撮影
            summary_screenshot = take_screenshot(
                page,
                INSIGHTS_HOME_URL,
                "instagram_insights_home"
            )

            # 2. コンテンツページのスクリーンショット撮影
            content_screenshot = take_screenshot(
                page,
                INSIGHTS_CONTENT_URL,
                "instagram_insights_content"
            )

            print("\n" + "=" * 60)
            print("スクリーンショット撮影完了")
            print("=" * 60)

            # ブラウザを閉じる
            browser.close()

            # 3. Claude APIでサマリーデータ抽出
            summary_data = extract_data_with_claude(summary_screenshot, "summary")

            # 4. Claude APIで投稿データ抽出
            posts_data = extract_data_with_claude(content_screenshot, "content")

            # 5. CSV保存
            save_to_csv(summary_data, posts_data)

            print("\n" + "=" * 60)
            print("✓ データ取得完了")
            print("=" * 60)

            if summary_data:
                print("\n【取得データ】")
                for key, value in summary_data.items():
                    if key not in ["期間", "取得日時", "データソース"]:
                        print(f"  {key}: {value}")

            if posts_data:
                print(f"\n【投稿データ】: {len(posts_data)}件取得")

        except Exception as e:
            print(f"\n✗ エラー発生: {e}")
            import traceback
            traceback.print_exc()

            # エラー時もブラウザを閉じる
            try:
                browser.close()
            except:
                pass


if __name__ == "__main__":
    main()
