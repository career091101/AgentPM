#!/usr/bin/env python3
"""
affiliateman.site コンテンツスクレイパー

会員制サイトから以下のコンテンツを取得：
- ブログ記事
- 動画教材（YouTube URL + テキスト + 資料画像）
- 対談動画（YouTube URL + テキスト + 資料画像）
- ZOOMコンサル（YouTube URL）
"""

import os
import re
import time
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs
import requests
from bs4 import BeautifulSoup

# 設定
BASE_URL = "https://affiliateman.site"
PASSWORD = "snshack"
OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")
DELAY = 1  # リクエスト間隔（秒）

class AffiliateManScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })

    def login(self):
        """パスワード認証"""
        print("ログイン中...")

        # まずログインページにアクセスしてリダイレクトURLを取得
        response = self.session.get(BASE_URL, allow_redirects=True)

        # パスワード送信
        login_data = {
            'password_protected_pwd': PASSWORD,
            'password_protected_rememberme': '1',
            'Submit': 'ログイン'
        }

        response = self.session.post(
            response.url,  # リダイレクト先のURL
            data=login_data,
            allow_redirects=True
        )

        # Cookieを確認（Password Protected プラグインの認証Cookie）
        auth_cookies = ['wp-postpass', 'password_protected_auth']
        is_authenticated = any(cookie_name in str(self.session.cookies) for cookie_name in auth_cookies)

        if is_authenticated:
            print("✓ ログイン成功")
            return True
        else:
            print("✗ ログイン失敗")
            print(f"Cookies: {self.session.cookies}")
            return False

    def get_page(self, url):
        """ページを取得"""
        time.sleep(DELAY)
        response = self.session.get(url)
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')

    def extract_youtube_id(self, url):
        """YouTube URLからvideo_idを抽出"""
        if not url:
            return None

        # youtube.com/watch?v=...
        if 'youtube.com/watch' in url:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            return params.get('v', [None])[0]

        # youtu.be/...
        if 'youtu.be/' in url:
            return url.split('youtu.be/')[-1].split('?')[0]

        return None

    def save_markdown(self, content, filepath):
        """Markdown形式で保存"""
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  保存: {filepath}")

    def download_image(self, url, filepath):
        """画像をダウンロード"""
        try:
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                filepath.parent.mkdir(parents=True, exist_ok=True)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                return True
        except Exception as e:
            print(f"  画像DLエラー: {e}")
        return False

    def _extract_images_from_content(self, content_elem, base_url):
        """記事本文から画像URLを抽出"""
        images = []
        for idx, img in enumerate(content_elem.find_all('img')):
            img_url = img.get('src') or img.get('data-src') or img.get('data-lazy-src')
            if not img_url:
                continue
            img_url = urljoin(base_url, img_url)
            if not img_url.startswith(('http://', 'https://')):
                continue
            images.append({
                'src': img_url,
                'alt': img.get('alt', ''),
                'position': idx
            })
        return images

    def _download_blog_images(self, images, image_dir):
        """画像をダウンロード"""
        downloaded = []
        for i, img_info in enumerate(images):
            ext = os.path.splitext(urlparse(img_info['src']).path)[1] or '.jpg'
            filename = f"image_{i+1:02d}{ext}"
            filepath = image_dir / filename

            if self.download_image(img_info['src'], filepath):
                downloaded.append({
                    'original_url': img_info['src'],
                    'local_path': str(filepath.relative_to(OUTPUT_DIR)),
                    'alt': img_info['alt'],
                    'position': img_info['position'],
                    'filename': filename
                })
                print(f"  ✓ 画像DL: {filename}")
        return downloaded

    def scrape_blog_post(self, url, category):
        """ブログ記事を取得（画像含む）"""
        soup = self.get_page(url)

        # タイトル
        title_elem = soup.find('h1', class_='entry-title') or soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"

        # 本文
        content_elem = soup.find('div', class_='entry-content') or soup.find('article')
        if not content_elem:
            return None

        # NEW: 画像抽出
        images = self._extract_images_from_content(content_elem, url)
        print(f"  画像検出: {len(images)}枚")

        # NEW: 画像ダウンロード
        downloaded_images = []
        if images:
            sanitized_title = re.sub(r'[^\w\s-]', '', title)[:100]
            image_dir = OUTPUT_DIR / 'blog' / category / 'images' / sanitized_title
            downloaded_images = self._download_blog_images(images, image_dir)

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

        # NEW: 画像をMarkdownに追加（プレースホルダー付き）
        if downloaded_images:
            markdown += "\n---\n\n## 記事内画像\n\n"
            sanitized_title_for_path = re.sub(r'[^\w\s-]', '', title)[:100]
            for img in downloaded_images:
                placeholder = f"PLACEHOLDER:{img['filename']}"
                relative_path = f"images/{sanitized_title_for_path}/{img['filename']}"
                markdown += f"![{placeholder}]({relative_path})\n\n"

        # ファイル名をサニタイズ
        filename = re.sub(r'[^\w\s-]', '', title)[:100] + '.md'
        filepath = OUTPUT_DIR / 'blog' / category / filename

        self.save_markdown(markdown, filepath)
        return {
            'title': title,
            'url': url,
            'category': category,
            'filepath': str(filepath),
            'images': len(downloaded_images),  # NEW
            'image_metadata': downloaded_images  # NEW
        }

    def scrape_video_content(self, url, content_type='video_tutorials'):
        """動画コンテンツを取得（YouTube URL + テキスト + 資料画像）"""
        soup = self.get_page(url)

        # タイトル
        title_elem = soup.find('h1', class_='entry-title') or soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"

        # YouTube URL
        youtube_url = None
        youtube_link = soup.find('a', href=re.compile(r'youtube\.com|youtu\.be'))
        if youtube_link:
            youtube_url = youtube_link['href']

        youtube_id = self.extract_youtube_id(youtube_url) if youtube_url else None

        # 話した内容のリスト
        content_list = []
        content_section = soup.find('div', text=re.compile('動画で話した内容'))
        if content_section:
            parent = content_section.find_parent()
            if parent:
                for li in parent.find_all('li'):
                    content_list.append(li.get_text(strip=True))

        # 資料画像
        images = []
        resource_section = soup.find('div', text=re.compile('資料|スライド'))
        if resource_section:
            parent = resource_section.find_parent()
            if parent:
                for img in parent.find_all('img'):
                    img_url = img.get('src') or img.get('data-src')
                    if img_url:
                        images.append(urljoin(BASE_URL, img_url))

        # Markdown作成
        markdown = f"# {title}\n\n"
        markdown += f"**URL**: {url}\n\n"
        if youtube_url:
            markdown += f"**YouTube**: {youtube_url}\n"
            markdown += f"**Video ID**: {youtube_id}\n\n"
        markdown += "---\n\n"

        if content_list:
            markdown += "## 動画で話した内容\n\n"
            for item in content_list:
                markdown += f"- {item}\n"
            markdown += "\n"

        # ファイル保存
        filename = re.sub(r'[^\w\s-]', '', title)[:100]
        if content_type == 'interviews':
            base_dir = OUTPUT_DIR / 'interviews' / filename
            base_dir.mkdir(parents=True, exist_ok=True)
            filepath = base_dir / 'summary.md'
        else:
            filepath = OUTPUT_DIR / content_type / (filename + '.md')

        self.save_markdown(markdown, filepath)

        # 資料画像をダウンロード
        if images and content_type == 'interviews':
            resource_dir = base_dir / 'resources'
            for i, img_url in enumerate(images):
                ext = os.path.splitext(urlparse(img_url).path)[1] or '.jpg'
                img_path = resource_dir / f"slide_{i+1:02d}{ext}"
                self.download_image(img_url, img_path)

        return {
            'title': title,
            'url': url,
            'youtube_url': youtube_url,
            'youtube_id': youtube_id,
            'content_type': content_type,
            'filepath': str(filepath),
            'images': len(images)
        }

    def scrape_homepage(self):
        """ホームページから記事URLを収集"""
        print("\n=== ホームページを解析中 ===")
        soup = self.get_page(BASE_URL)

        # ブログ記事のURLを収集
        blog_urls = []

        # インスタ攻略
        for link in soup.find_all('a', text=re.compile('インスタ')):
            href = link.get('href')
            if href and BASE_URL in href:
                blog_urls.append(('instagram', href))

        # Twitter攻略
        for link in soup.find_all('a', text=re.compile('Twitter|ツイッター')):
            href = link.get('href')
            if href and BASE_URL in href:
                blog_urls.append(('twitter', href))

        # TikTok
        for link in soup.find_all('a', text=re.compile('TikTok')):
            href = link.get('href')
            if href and BASE_URL in href:
                blog_urls.append(('tiktok', href))

        return blog_urls

    def scrape_zoom_consults(self):
        """ZOOMコンサルのYouTube URLを収集"""
        print("\n=== ZOOMコンサルを検索中 ===")
        soup = self.get_page(BASE_URL)

        zoom_videos = []

        # ページ内の全YouTube URLを収集
        all_youtube_links = soup.find_all('a', href=re.compile(r'youtube\.com|youtu\.be'))

        # すでに処理済みのYouTube URLを追跡（対談動画と重複しないように）
        processed_urls = set()

        for link in all_youtube_links:
            youtube_url = link['href']
            video_id = self.extract_youtube_id(youtube_url)

            if not video_id or video_id in processed_urls:
                continue

            # リンクテキストまたは親要素からタイトルを推測
            title = link.get_text(strip=True)

            # タイトルが空の場合、親要素から探す
            if not title or len(title) < 5:
                parent = link.find_parent()
                if parent:
                    title = parent.get_text(strip=True)[:100]

            # ZOOMやコンサル関連のキーワードがあるかチェック
            if re.search(r'ZOOM|コンサル|月|スペース', title, re.IGNORECASE):
                zoom_videos.append({
                    'title': title or f"ZOOM_{video_id}",
                    'youtube_url': youtube_url,
                    'youtube_id': video_id
                })
                processed_urls.add(video_id)
                print(f"  発見: {title[:50]}... ({video_id})")

        return zoom_videos

    def run(self):
        """メイン実行"""
        print("=" * 60)
        print("affiliateman.site コンテンツ取得開始")
        print("=" * 60)

        if not self.login():
            return

        metadata = {
            'blog': [],
            'videos': [],
            'interviews': [],
            'zoom': []
        }

        # ホームページから記事を収集
        blog_urls = self.scrape_homepage()

        # ブログ記事を取得
        if blog_urls:
            print(f"\n=== ブログ記事取得 ({len(blog_urls)}件) ===")
            for category, url in blog_urls:
                try:
                    result = self.scrape_blog_post(url, category)
                    if result:
                        metadata['blog'].append(result)
                except Exception as e:
                    print(f"エラー: {url} - {e}")

        # 動画コンテンツページを取得
        print("\n=== 動画コンテンツを取得中 ===")
        movies_url = f"{BASE_URL}/movies/"
        soup = self.get_page(movies_url)

        # 対談動画のURLを収集
        for link in soup.find_all('a', href=re.compile(r'/talk_|/con_')):
            url = urljoin(BASE_URL, link['href'])
            try:
                result = self.scrape_video_content(url, 'interviews')
                metadata['interviews'].append(result)
            except Exception as e:
                print(f"エラー: {url} - {e}")

        # ZOOMコンサルを取得
        zoom_videos = self.scrape_zoom_consults()
        if zoom_videos:
            print(f"\n=== ZOOMコンサル取得 ({len(zoom_videos)}件) ===")
            for video in zoom_videos:
                # ZOOMコンサル用のMarkdown作成
                title = video['title']
                filename = re.sub(r'[^\w\s-]', '', title)[:100]
                filepath = OUTPUT_DIR / 'zoom_consult' / f"{filename}.md"

                filepath.parent.mkdir(parents=True, exist_ok=True)

                markdown = f"# {title}\n\n"
                markdown += f"**YouTube**: {video['youtube_url']}\n"
                markdown += f"**Video ID**: {video['youtube_id']}\n\n"
                markdown += "---\n\n"
                markdown += "※文字起こしは別途取得\n"

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(markdown)

                metadata['zoom'].append({
                    'title': title,
                    'youtube_url': video['youtube_url'],
                    'youtube_id': video['youtube_id'],
                    'filepath': str(filepath)
                })

                print(f"  保存: {filepath}")

        # メタデータを保存
        metadata_file = OUTPUT_DIR / 'metadata.json'
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        print("\n" + "=" * 60)
        print("取得完了")
        print(f"ブログ記事: {len(metadata['blog'])}件")
        print(f"対談動画: {len(metadata['interviews'])}件")
        print(f"ZOOMコンサル: {len(metadata['zoom'])}件")
        print("=" * 60)


if __name__ == "__main__":
    scraper = AffiliateManScraper()
    scraper.run()
