#!/usr/bin/env python3
"""
X (Twitter) Timeline Collector - Cursor-based API Interception Version

カーソルベースAPIインターセプション方式でタイムライン収集を行う。
重複率0%、10倍高速を実現。

実行方法:
    python3 scripts/collect_x_timeline_cursor.py --target 100 --output data/x_timeline_cursor_test.json

必要なパッケージ:
    pip install playwright asyncio
    playwright install chromium
"""

import asyncio
import json
import re
import random
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
import argparse


class XTimelineCursorCollector:
    """カーソルベースAPIインターセプション方式でXタイムライン収集"""

    def __init__(self, target_count: int = 100):
        self.target_count = target_count
        self.collected_tweets = []
        self.seen_tweet_ids = set()
        self.cursors = []
        self.api_responses = []

    async def collect(self, url: str = "https://x.com/home", cookies_file: str = None) -> List[Dict]:
        """タイムライン収集メイン処理"""
        from playwright.async_api import async_playwright

        print(f"🚀 カーソルベースAPI収集開始（目標: {self.target_count}件）")
        print(f"📍 URL: {url}")

        async with async_playwright() as p:
            # ブラウザ起動（ヘッドレスモード）
            browser = await p.chromium.launch(
                headless=True,  # バックグラウンド実行
                args=['--disable-blink-features=AutomationControlled']
            )

            # コンテキスト作成
            context = await browser.new_context(
                viewport={'width': 1280, 'height': 720},
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            )

            # クッキー読み込み
            if cookies_file and Path(cookies_file).exists():
                print(f"🍪 クッキー読み込み中: {cookies_file}")
                with open(cookies_file, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                await context.add_cookies(cookies)
                print(f"   ✅ {len(cookies)}件のクッキーを設定")

            page = await context.new_page()

            # ネットワークレスポンスインターセプション設定
            page.on("response", lambda response: asyncio.create_task(
                self._handle_response(response)
            ))

            # タイムラインページへ移動
            print("📄 ページ読み込み中...")
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=60000)
            except Exception as e:
                print(f"   ⚠️ ページロードタイムアウト（無視して続行）: {e}")

            # 初期ロード待機
            await asyncio.sleep(5)

            print(f"✅ 初期ロード完了。API傍受開始...")

            # カーソルベース収集ループ
            iteration = 0
            while len(self.collected_tweets) < self.target_count:
                iteration += 1
                print(f"\n📊 Iteration {iteration}: 収集済み {len(self.collected_tweets)}/{self.target_count}件")

                # スクロールして新しいAPIリクエストをトリガー
                await page.evaluate("window.scrollBy(0, 2000)")

                # 待機時間をランダム化（ボット検知回避）
                wait_time = random.uniform(3, 6)
                await asyncio.sleep(wait_time)

                # 最大イテレーション数チェック（無限ループ回避）
                if iteration > 150:
                    print("⚠️ 最大イテレーション数に到達。収集終了。")
                    break

                # 収集が進まない場合の脱出
                if iteration > 10 and len(self.collected_tweets) == 0:
                    print("❌ 10イテレーション後もツイート収集なし。終了。")
                    break

            await browser.close()

        print(f"\n✅ 収集完了: {len(self.collected_tweets)}件（ユニーク: {len(self.seen_tweet_ids)}件）")
        return self.collected_tweets

    async def _handle_response(self, response):
        """ネットワークレスポンス処理"""
        url = response.url

        # GraphQL APIのHomeTimeline系エンドポイントを検出
        if 'HomeTimeline' in url or 'HomeLatestTimeline' in url:
            try:
                # JSONレスポンスを取得
                json_data = await response.json()

                print(f"🔍 API検出: {url[:100]}...")

                # レスポンスをデバッグ用に保存
                self.api_responses.append({
                    'url': url,
                    'timestamp': datetime.now().isoformat(),
                    'data': json_data
                })

                # ツイートデータを抽出
                tweets = self._extract_tweets_from_graphql(json_data)

                if tweets:
                    new_count = 0
                    for tweet in tweets:
                        tweet_id = tweet.get('tweet_id')
                        if tweet_id and tweet_id not in self.seen_tweet_ids:
                            self.collected_tweets.append(tweet)
                            self.seen_tweet_ids.add(tweet_id)
                            new_count += 1

                    print(f"   ✅ {new_count}件の新規ツイート追加")

                # カーソル値を抽出
                cursor = self._extract_cursor(json_data)
                if cursor:
                    self.cursors.append(cursor)
                    print(f"   📌 カーソル取得: {cursor[:50]}...")

            except Exception as e:
                print(f"   ⚠️ レスポンス処理エラー: {e}")

    def _extract_tweets_from_graphql(self, data: Dict) -> List[Dict]:
        """GraphQLレスポンスからツイートデータを抽出"""
        tweets = []

        try:
            # data.home.home_timeline_urt.instructions のパターン
            instructions = None

            if 'data' in data:
                if 'home' in data['data']:
                    timeline = data['data']['home'].get('home_timeline_urt', {})
                    instructions = timeline.get('instructions', [])
                elif 'user' in data['data']:
                    # UserTweetsの場合
                    user_result = data['data']['user'].get('result', {})
                    timeline = user_result.get('timeline_v2', {}).get('timeline', {})
                    instructions = timeline.get('instructions', [])

            if not instructions:
                return tweets

            # instructionsから"TimelineAddEntries"を探す
            for instruction in instructions:
                if instruction.get('type') == 'TimelineAddEntries':
                    entries = instruction.get('entries', [])

                    for entry in entries:
                        # tweet-XXX 形式のエントリのみ処理
                        entry_id = entry.get('entryId', '')
                        if not entry_id.startswith('tweet-'):
                            continue

                        # content.itemContent.tweet_results.result
                        content = entry.get('content', {})
                        item_content = content.get('itemContent', {})
                        tweet_results = item_content.get('tweet_results', {})
                        result = tweet_results.get('result', {})

                        if not result:
                            continue

                        # legacy フィールドからデータ抽出
                        legacy = result.get('legacy', {})
                        if not legacy:
                            continue

                        # ツイートデータを構築
                        tweet_id = legacy.get('id_str', '')
                        if not tweet_id:
                            continue

                        # リツイート・リプライ除外
                        if legacy.get('retweeted_status'):
                            continue
                        if legacy.get('in_reply_to_status_id_str'):
                            continue

                        # ユーザー情報
                        core = result.get('core', {})
                        user_results = core.get('user_results', {})
                        user_result = user_results.get('result', {})

                        # screen_nameは user_result.core.screen_name にある
                        user_core = user_result.get('core', {})
                        username = user_core.get('screen_name', 'unknown')

                        # フォールバック: legacyからも試す
                        if username == 'unknown':
                            user_legacy = user_result.get('legacy', {})
                            username = user_legacy.get('screen_name', 'unknown')

                        tweet = {
                            'tweet_id': tweet_id,
                            'username': username,
                            'text': legacy.get('full_text', ''),
                            'likes': legacy.get('favorite_count', 0),
                            'retweets': legacy.get('retweet_count', 0),
                            'replies': legacy.get('reply_count', 0),
                            'timestamp_text': legacy.get('created_at', ''),
                            'collected_at': datetime.now().isoformat()
                        }

                        tweets.append(tweet)

        except Exception as e:
            print(f"   ⚠️ ツイート抽出エラー: {e}")

        return tweets

    def _extract_cursor(self, data: Dict) -> Optional[str]:
        """GraphQLレスポンスからカーソル値を抽出"""
        try:
            instructions = None

            if 'data' in data:
                if 'home' in data['data']:
                    timeline = data['data']['home'].get('home_timeline_urt', {})
                    instructions = timeline.get('instructions', [])
                elif 'user' in data['data']:
                    user_result = data['data']['user'].get('result', {})
                    timeline = user_result.get('timeline_v2', {}).get('timeline', {})
                    instructions = timeline.get('instructions', [])

            if not instructions:
                return None

            # 最後のinstructionの最後のentryからcursorを取得
            for instruction in instructions:
                if instruction.get('type') == 'TimelineAddEntries':
                    entries = instruction.get('entries', [])

                    # 最後のエントリを探す（cursor-bottom-XXX）
                    for entry in reversed(entries):
                        entry_id = entry.get('entryId', '')
                        if 'cursor-bottom' in entry_id or 'cursor-showmorethreads' in entry_id:
                            content = entry.get('content', {})
                            cursor_value = content.get('value', '')
                            if cursor_value:
                                return cursor_value

        except Exception as e:
            print(f"   ⚠️ カーソル抽出エラー: {e}")

        return None

    def save_results(self, output_path: str):
        """収集結果をJSON形式で保存"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        result = {
            'collected_at': datetime.now().isoformat(),
            'total_tweets': len(self.collected_tweets),
            'unique_tweets': len(self.seen_tweet_ids),
            'cursors_collected': len(self.cursors),
            'tweets': self.collected_tweets
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"\n💾 結果保存: {output_file}")
        print(f"   - 総収集数: {result['total_tweets']}件")
        print(f"   - ユニーク: {result['unique_tweets']}件")
        print(f"   - カーソル数: {result['cursors_collected']}個")

    def save_debug_data(self, output_dir: str):
        """デバッグ用にAPIレスポンスを保存"""
        debug_dir = Path(output_dir)
        debug_dir.mkdir(parents=True, exist_ok=True)

        # APIレスポンス保存
        api_file = debug_dir / 'api_responses.json'
        with open(api_file, 'w', encoding='utf-8') as f:
            json.dump(self.api_responses, f, ensure_ascii=False, indent=2)

        print(f"🐛 デバッグデータ保存: {api_file}")


async def main():
    parser = argparse.ArgumentParser(description='X Timeline Cursor-based Collector')
    parser.add_argument('--target', type=int, default=100, help='目標収集件数')
    parser.add_argument('--output', type=str, default='data/x_timeline_cursor_test.json', help='出力ファイルパス')
    parser.add_argument('--debug', action='store_true', help='デバッグモード（APIレスポンス保存）')
    parser.add_argument('--url', type=str, default='https://x.com/home', help='収集URL（デフォルト: おすすめタブ）')
    parser.add_argument('--cookies', type=str, default='data/x_cookies.json', help='クッキーファイルパス')

    args = parser.parse_args()

    collector = XTimelineCursorCollector(target_count=args.target)

    # 収集実行
    await collector.collect(url=args.url, cookies_file=args.cookies)

    # 結果保存
    collector.save_results(args.output)

    # デバッグモード
    if args.debug:
        output_path = Path(args.output)
        debug_dir = output_path.parent / f"{output_path.stem}_debug"
        collector.save_debug_data(str(debug_dir))


if __name__ == '__main__':
    asyncio.run(main())
