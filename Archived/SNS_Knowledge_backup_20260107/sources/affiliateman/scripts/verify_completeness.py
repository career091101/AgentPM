#!/usr/bin/env python3
"""
affiliateman.site コンテンツ完全性検証スクリプト

既に取得したコンテンツとサイトの実際のコンテンツを比較し、
取得漏れがないかを確認する。
"""

import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import time

BASE_URL = "https://affiliateman.site"
PASSWORD = "snshack"
METADATA_FILE = Path(__file__).parent.parent / "metadata.json"

class ContentVerifier:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })

    def login(self):
        """パスワード認証"""
        print("ログイン中...")
        response = self.session.get(BASE_URL, allow_redirects=True)

        login_data = {
            'password_protected_pwd': PASSWORD,
            'password_protected_rememberme': '1',
            'Submit': 'ログイン'
        }

        response = self.session.post(response.url, data=login_data, allow_redirects=True)

        auth_cookies = ['wp-postpass', 'password_protected_auth']
        is_authenticated = any(cookie_name in str(self.session.cookies) for cookie_name in auth_cookies)

        if is_authenticated:
            print("✓ ログイン成功\n")
            return True
        else:
            print("✗ ログイン失敗")
            return False

    def get_page(self, url):
        """ページを取得"""
        time.sleep(1)
        response = self.session.get(url)
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')

    def count_homepage_links(self):
        """ホームページのリンク数をカウント"""
        print("=== ホームページのリンク数を確認 ===")
        soup = self.get_page(BASE_URL)

        # すべてのリンクを取得
        all_links = soup.find_all('a', href=True)

        categories = {
            'instagram': set(),
            'twitter': set(),
            'tiktok': set(),
            'movies': set(),
            'other': set()
        }

        for link in all_links:
            href = link.get('href', '')
            text = link.get_text(strip=True).lower()

            if BASE_URL not in href:
                continue

            # カテゴリ分類
            if 'インスタ' in text or 'instagram' in href.lower():
                categories['instagram'].add(href)
            elif 'twitter' in text.lower() or 'ツイッター' in text or 'twitter' in href.lower():
                categories['twitter'].add(href)
            elif 'tiktok' in text.lower() or 'tiktok' in href.lower():
                categories['tiktok'].add(href)
            elif '/movies/' in href or '/talk_' in href or '/con_' in href:
                categories['movies'].add(href)
            else:
                categories['other'].add(href)

        print(f"Instagram関連: {len(categories['instagram'])}件")
        print(f"Twitter関連: {len(categories['twitter'])}件")
        print(f"TikTok関連: {len(categories['tiktok'])}件")
        print(f"Movies関連: {len(categories['movies'])}件")
        print(f"その他: {len(categories['other'])}件")
        print()

        return categories

    def check_movies_page(self):
        """Moviesページの動画数を確認"""
        print("=== /movies/ ページを確認 ===")
        movies_url = f"{BASE_URL}/movies/"
        soup = self.get_page(movies_url)

        # 動画コンテンツへのリンクを探す
        video_links = soup.find_all('a', href=True)

        interviews = set()
        tutorials = set()

        for link in video_links:
            href = link['href']
            if '/talk_' in href or '/con_' in href:
                interviews.add(href)
            elif BASE_URL in href and any(x in href for x in ['/video', '/movie']):
                tutorials.add(href)

        print(f"対談動画: {len(interviews)}件")
        print(f"動画教材: {len(tutorials)}件")
        print()

        # 見つかったURLをリスト表示
        if interviews:
            print("対談動画URL:")
            for url in sorted(interviews):
                print(f"  - {url}")

        if tutorials:
            print("動画教材URL:")
            for url in sorted(tutorials):
                print(f"  - {url}")

        print()
        return {'interviews': interviews, 'tutorials': tutorials}

    def compare_with_metadata(self):
        """取得済みメタデータと比較"""
        print("=== 取得済みコンテンツと比較 ===")

        if not METADATA_FILE.exists():
            print("メタデータファイルが見つかりません")
            return

        with open(METADATA_FILE, 'r', encoding='utf-8') as f:
            metadata = json.load(f)

        print(f"取得済みブログ記事: {len(metadata.get('blog', []))}件")
        print(f"取得済み対談動画: {len(metadata.get('interviews', []))}件")
        print(f"取得済みZOOMコンサル: {len(metadata.get('zoom', []))}件")
        print()

        # URLリストを作成
        fetched_urls = set()
        for item in metadata.get('blog', []):
            fetched_urls.add(item.get('url', ''))
        for item in metadata.get('interviews', []):
            fetched_urls.add(item.get('url', ''))

        print(f"取得済みURL総数: {len(fetched_urls)}件")
        print()

        return fetched_urls

    def run(self):
        """検証実行"""
        print("=" * 60)
        print("affiliateman.site コンテンツ完全性検証")
        print("=" * 60)
        print()

        if not self.login():
            return

        # ホームページのリンク数を確認
        homepage_links = self.count_homepage_links()

        # Moviesページを確認
        movies_content = self.check_movies_page()

        # 取得済みコンテンツと比較
        fetched_urls = self.compare_with_metadata()

        # サイト上の総URL数
        site_urls = set()
        for category, urls in homepage_links.items():
            site_urls.update(urls)
        site_urls.update(movies_content['interviews'])
        site_urls.update(movies_content['tutorials'])

        print("=" * 60)
        print("検証結果サマリー")
        print("=" * 60)
        print(f"サイト上の総コンテンツURL: {len(site_urls)}件")
        print(f"取得済みURL: {len(fetched_urls)}件")

        # 取得漏れを確認
        if fetched_urls:
            missing_urls = site_urls - fetched_urls
            if missing_urls:
                print(f"\n⚠️ 取得漏れの可能性: {len(missing_urls)}件")
                print("\n未取得URL:")
                for url in sorted(missing_urls):
                    print(f"  - {url}")
            else:
                print("\n✅ すべてのコンテンツを取得済みです")

        print("=" * 60)

if __name__ == "__main__":
    verifier = ContentVerifier()
    verifier.run()
