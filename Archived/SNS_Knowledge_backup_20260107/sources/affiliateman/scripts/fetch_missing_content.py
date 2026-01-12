#!/usr/bin/env python3
"""
未取得コンテンツの追加取得スクリプト

以下を取得：
- TikTok追加ページ（3件）
- Twitter追加ページ（2件）
- Instagram追加ページ（1件）
- PDF資料（2件）
"""

import os
import re
import time
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup

# 設定
BASE_URL = "https://affiliateman.site"
PASSWORD = "snshack"
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
DELAY = 1

class MissingContentFetcher:
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
        time.sleep(DELAY)
        response = self.session.get(url)
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')

    def save_markdown(self, content, filepath):
        """Markdown形式で保存"""
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ 保存: {filepath.name}")

    def download_pdf(self, url, filepath):
        """PDFをダウンロード"""
        try:
            response = self.session.get(url, timeout=30)
            if response.status_code == 200:
                filepath.parent.mkdir(parents=True, exist_ok=True)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                file_size = len(response.content) / 1024  # KB
                print(f"  ✓ ダウンロード: {filepath.name} ({file_size:.1f} KB)")
                return True
        except Exception as e:
            print(f"  ✗ エラー: {e}")
        return False

    def scrape_blog_post(self, url, category):
        """ブログ記事を取得"""
        soup = self.get_page(url)

        # タイトル
        title_elem = soup.find('h1', class_='entry-title') or soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"

        # 本文
        content_elem = soup.find('div', class_='entry-content') or soup.find('article')
        if not content_elem:
            print(f"  ✗ コンテンツが見つかりません: {url}")
            return None

        # Markdown形式に変換
        markdown = f"# {title}\n\n"
        markdown += f"**URL**: {url}\n\n"
        markdown += "---\n\n"

        # 見出しと段落を抽出
        for elem in content_elem.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol']):
            if elem.name == 'h1':
                markdown += f"# {elem.get_text(strip=True)}\n\n"
            elif elem.name == 'h2':
                markdown += f"## {elem.get_text(strip=True)}\n\n"
            elif elem.name == 'h3':
                markdown += f"### {elem.get_text(strip=True)}\n\n"
            elif elem.name == 'h4':
                markdown += f"#### {elem.get_text(strip=True)}\n\n"
            elif elem.name == 'p':
                text = elem.get_text(strip=True)
                if text:
                    markdown += f"{text}\n\n"
            elif elem.name in ['ul', 'ol']:
                for li in elem.find_all('li', recursive=False):
                    markdown += f"- {li.get_text(strip=True)}\n"
                markdown += "\n"

        # ファイル名をサニタイズ
        filename = re.sub(r'[^\w\s-]', '', title)[:100] + '.md'
        filepath = OUTPUT_DIR / 'blog' / category / filename

        self.save_markdown(markdown, filepath)
        return {
            'title': title,
            'url': url,
            'category': category,
            'filepath': str(filepath)
        }

    def run(self):
        """メイン実行"""
        print("=" * 60)
        print("未取得コンテンツの追加取得")
        print("=" * 60)
        print()

        if not self.login():
            return

        results = {
            'blog': [],
            'pdf': []
        }

        # TikTok追加ページ（3件）
        print("=== TikTok追加ページ ===")
        tiktok_urls = [
            "https://affiliateman.site/tiktok_baz/",
            "https://affiliateman.site/tiktok_contentsbaz/",
            "https://affiliateman.site/tiktok_monetize/"
        ]

        for url in tiktok_urls:
            try:
                result = self.scrape_blog_post(url, 'tiktok')
                if result:
                    results['blog'].append(result)
            except Exception as e:
                print(f"  ✗ エラー: {url} - {e}")

        print()

        # Twitter追加ページ（2件）
        print("=== Twitter追加ページ ===")
        twitter_urls = [
            "https://affiliateman.site/twitter-20man/",
            "https://affiliateman.site/twitter_anya/"
        ]

        for url in twitter_urls:
            try:
                result = self.scrape_blog_post(url, 'twitter')
                if result:
                    results['blog'].append(result)
            except Exception as e:
                print(f"  ✗ エラー: {url} - {e}")

        print()

        # Instagram追加ページ（1件）
        print("=== Instagram追加ページ ===")
        instagram_urls = [
            "https://affiliateman.site/instagram-book/"
        ]

        for url in instagram_urls:
            try:
                result = self.scrape_blog_post(url, 'instagram')
                if result:
                    results['blog'].append(result)
            except Exception as e:
                print(f"  ✗ エラー: {url} - {e}")

        print()

        # PDF資料（2件）
        print("=== PDF資料 ===")
        pdf_urls = [
            "https://affiliateman.site/wp-content/uploads/2022/11/SNS攻略サロンインタビュー資料.pdf",
            "https://affiliateman.site/wp-content/uploads/2022/11/マイメアリー資料-2.pdf"
        ]

        pdf_dir = OUTPUT_DIR / 'resources' / 'pdf'
        for url in pdf_urls:
            filename = url.split('/')[-1]
            filepath = pdf_dir / filename
            try:
                if self.download_pdf(url, filepath):
                    results['pdf'].append({
                        'url': url,
                        'filepath': str(filepath)
                    })
            except Exception as e:
                print(f"  ✗ エラー: {url} - {e}")

        print()
        print("=" * 60)
        print("追加取得完了")
        print("=" * 60)
        print(f"ブログ記事: {len(results['blog'])}件")
        print(f"PDF資料: {len(results['pdf'])}件")
        print()

        # 既存のメタデータに追加
        metadata_file = OUTPUT_DIR / 'metadata.json'
        if metadata_file.exists():
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
        else:
            metadata = {'blog': [], 'videos': [], 'interviews': [], 'zoom': [], 'pdf': []}

        # 新規コンテンツを追加
        metadata['blog'].extend(results['blog'])
        if 'pdf' not in metadata:
            metadata['pdf'] = []
        metadata['pdf'].extend(results['pdf'])

        # 重複削除
        seen_urls = set()
        unique_blog = []
        for item in metadata['blog']:
            url = item.get('url')
            if url not in seen_urls:
                seen_urls.add(url)
                unique_blog.append(item)
        metadata['blog'] = unique_blog

        # メタデータを保存
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        print(f"✓ メタデータ更新: {metadata_file}")
        print(f"  総ブログ記事: {len(metadata['blog'])}件")
        print(f"  総PDF資料: {len(metadata.get('pdf', []))}件")
        print("=" * 60)


if __name__ == "__main__":
    fetcher = MissingContentFetcher()
    fetcher.run()
