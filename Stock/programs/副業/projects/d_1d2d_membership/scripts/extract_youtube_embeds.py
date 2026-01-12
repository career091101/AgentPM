#!/usr/bin/env python3
"""
記事内のYouTube埋め込み動画を抽出してMarkdownに追記するスクリプト
"""
import json
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs
import requests
from bs4 import BeautifulSoup
import time

def load_session_with_cookies(cookies_path):
    """クッキーをロードしてセッションを作成"""
    session = requests.Session()
    cookies_json = json.loads(Path(cookies_path).read_text(encoding='utf-8'))
    cookies_data = cookies_json.get('cookies', cookies_json)  # 'cookies'キーがあればそれを使用
    for cookie in cookies_data:
        session.cookies.set(
            name=cookie['name'],
            value=cookie['value'],
            domain=cookie.get('domain', ''),
            path=cookie.get('path', '/')
        )
    return session

def extract_youtube_urls(soup):
    """HTMLからYouTube埋め込みURLを抽出"""
    youtube_urls = []

    # iframeタグからYouTube URLを抽出
    iframes = soup.find_all('iframe')
    for iframe in iframes:
        src = iframe.get('src', '')
        if 'youtube.com/embed' in src or 'youtube-nocookie.com/embed' in src:
            # 埋め込みURLから通常のwatch URLに変換
            video_id_match = re.search(r'/embed/([a-zA-Z0-9_-]+)', src)
            if video_id_match:
                video_id = video_id_match.group(1)
                watch_url = f"https://www.youtube.com/watch?v={video_id}"
                youtube_urls.append(watch_url)

    # aタグからYouTube URLを抽出
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if 'youtube.com/watch' in href or 'youtu.be/' in href:
            youtube_urls.append(href)

    # 重複を削除
    return list(dict.fromkeys(youtube_urls))

def format_youtube_markdown(urls):
    """YouTube URLをMarkdown形式にフォーマット"""
    if not urls:
        return ""

    markdown_lines = ["\n## 📺 YouTube動画\n"]
    for idx, url in enumerate(urls, 1):
        markdown_lines.append(f"{idx}. [{url}]({url})")

    return "\n".join(markdown_lines) + "\n"

def process_article_youtube(session, metadata_path, md_path):
    """記事のYouTube埋め込みを抽出してMarkdownに追記"""
    # メタデータを読み込み
    metadata = json.loads(metadata_path.read_text(encoding='utf-8'))
    article_url = metadata.get('url')

    if not article_url:
        return 0

    # 既存のMarkdownを読み込み
    existing_markdown = md_path.read_text(encoding='utf-8')

    # すでにYouTube動画セクションがある場合はスキップ
    if '## 📺 YouTube動画' in existing_markdown:
        print(f"  ⏭️  Already has YouTube section: {md_path.name}")
        return 0

    # 記事HTMLを取得
    try:
        response = session.get(article_url, timeout=30)
        response.raise_for_status()
        html = response.text
    except Exception as e:
        print(f"  ⚠️  Failed to fetch {article_url}: {e}")
        return 0

    # YouTube URLを抽出
    soup = BeautifulSoup(html, 'html.parser')
    youtube_urls = extract_youtube_urls(soup)

    if not youtube_urls:
        return 0

    # Markdownに追記
    youtube_markdown = format_youtube_markdown(youtube_urls)
    updated_markdown = existing_markdown.rstrip() + "\n" + youtube_markdown
    md_path.write_text(updated_markdown, encoding='utf-8')

    print(f"  ✅ Added {len(youtube_urls)} YouTube URL(s): {md_path.name}")
    return len(youtube_urls)

def main():
    cookies_path = "../data/cookies/d_1d2d_cookies.json"
    articles_dir = Path("../data/d_1d2d_articles/articles")

    # セッション作成
    session = load_session_with_cookies(cookies_path)

    # すべてのJSONファイルを取得
    json_files = sorted(articles_dir.glob("*.json"))
    print(f"📚 Processing {len(json_files)} articles for YouTube embeds...\n")

    total_videos = 0
    articles_with_videos = 0

    for json_path in json_files:
        md_path = json_path.with_suffix('.md')

        if not md_path.exists():
            continue

        videos_found = process_article_youtube(session, json_path, md_path)
        if videos_found > 0:
            total_videos += videos_found
            articles_with_videos += 1

        # レート制限を避けるため少し待機
        time.sleep(0.5)

    print(f"\n✅ Complete!")
    print(f"   Articles with YouTube: {articles_with_videos}/{len(json_files)}")
    print(f"   Total YouTube URLs: {total_videos}")

if __name__ == "__main__":
    main()
