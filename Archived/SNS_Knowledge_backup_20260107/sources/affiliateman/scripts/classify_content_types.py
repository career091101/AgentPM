#!/usr/bin/env python3
"""
affiliateman.site コンテンツタイプ分類スクリプト

全URLのコンテンツタイプを自動分類し、画像メタデータを含む
Markdownレポートを生成する。
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple
import argparse

BASE_URL = "https://affiliateman.site"
PASSWORD = "snshack"
PROJECT_DIR = Path(__file__).parent.parent
ALL_URLS_FILE = PROJECT_DIR / "all_urls_list.md"
OUTPUT_FILE = PROJECT_DIR / "content_type_classification_report.md"


class URLListParser:
    """all_urls_list.md をパースしてURL一覧を抽出"""

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def parse(self) -> List[Dict[str, str]]:
        """
        MarkdownファイルからタイトルとURLを抽出

        Returns:
            [{"title": "記事タイトル", "url": "https://...", "category": "Instagram攻略"}, ...]
        """
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        urls = []
        current_category = None

        # カテゴリ名を抽出（例: ## 1. Instagram攻略（17件））
        category_pattern = re.compile(r'^## \d+\. (.+?)（\d+件）$', re.MULTILINE)
        # リンクを抽出（例: 1. [タイトル](URL)）
        link_pattern = re.compile(r'^\d+\.\s+\[(.+?)\]\((https://[^\)]+)\)', re.MULTILINE)

        lines = content.split('\n')

        for line in lines:
            # カテゴリ名更新
            category_match = category_pattern.match(line)
            if category_match:
                current_category = category_match.group(1)
                continue

            # リンク抽出
            link_match = link_pattern.match(line)
            if link_match and current_category:
                title = link_match.group(1)
                url = link_match.group(2)
                urls.append({
                    "title": title,
                    "url": url,
                    "category": current_category
                })

        return urls


class ContentTypeClassifier:
    """コンテンツタイプを分類し、メタデータを抽出"""

    CONTENT_TYPES = {
        "TEXT_ARTICLE": "テキスト記事",
        "YOUTUBE_EMBEDDED_WITH_TEXT": "YouTube埋め込み+テキスト",
        "YOUTUBE_EMBEDDED": "YouTube埋め込み",
        "Q_AND_A_LIST": "Q&A形式",
        "LIST_PAGE": "リンク集",
        "PDF_RESOURCE": "PDF",
        "EXTERNAL_LINKS": "外部リンク",
        "OTHER": "その他"
    }

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })

    def login(self) -> bool:
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

    def fetch_page(self, url: str, timeout: int = 10) -> BeautifulSoup:
        """ページを取得してBeautifulSoupオブジェクトを返す"""
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'lxml')
        except Exception as e:
            print(f"  エラー: {e}")
            return None

    def extract_youtube_urls(self, soup: BeautifulSoup) -> List[str]:
        """YouTube埋め込みURLを抽出"""
        youtube_urls = []
        iframes = soup.find_all('iframe', src=re.compile(r'youtube\.com|youtu\.be'))

        for iframe in iframes:
            src = iframe.get('src', '')
            if src:
                youtube_urls.append(src)

        return youtube_urls

    def extract_images(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """
        画像メタデータを抽出

        Returns:
            [{"url": "...", "alt": "...", "width": "...", "height": "..."}, ...]
        """
        images = []
        img_tags = soup.find_all('img')

        for idx, img in enumerate(img_tags, start=1):
            src = img.get('src', '')
            # data-src（遅延読み込み）もチェック
            if not src:
                src = img.get('data-src', '')

            if src:
                images.append({
                    "position": idx,
                    "url": src,
                    "alt": img.get('alt', '').strip(),
                    "width": img.get('width', ''),
                    "height": img.get('height', '')
                })

        return images

    def classify(self, url: str) -> Dict:
        """
        URLのコンテンツタイプを分類してメタデータを返す

        Returns:
            {
                "content_type": "TEXT_ARTICLE",
                "paragraph_count": 23,
                "link_count": 5,
                "youtube_urls": [...],
                "images": [...],
                "has_pdf": False,
                "error": None
            }
        """
        soup = self.fetch_page(url)

        if soup is None:
            return {
                "content_type": "OTHER",
                "paragraph_count": 0,
                "link_count": 0,
                "youtube_urls": [],
                "images": [],
                "has_pdf": False,
                "error": "ページ取得失敗"
            }

        # メタデータ収集
        paragraphs = soup.find_all('p')
        links = soup.find_all('a')
        youtube_urls = self.extract_youtube_urls(soup)
        images = self.extract_images(soup)

        # PDF検出
        has_pdf = bool(soup.find('a', href=re.compile(r'\.pdf$', re.I))) or \
                  bool(soup.find('embed', src=re.compile(r'\.pdf$', re.I)))

        # 外部iframeチェック（YouTube以外）
        external_iframes = soup.find_all('iframe', src=True)
        has_external_iframe = any(
            iframe.get('src', '').startswith('http') and
            'youtube' not in iframe.get('src', '') and
            'affiliateman.site' not in iframe.get('src', '')
            for iframe in external_iframes
        )

        # Q&A形式チェック（h3/h4が質問形式）
        headings = soup.find_all(['h3', 'h4'])
        question_pattern = re.compile(r'[？\?]|どう|なぜ|いつ|どこ|誰|何')
        is_qa = sum(1 for h in headings if question_pattern.search(h.get_text())) >= 3

        paragraph_count = len(paragraphs)
        link_count = len(links)

        # 分類ロジック（優先順位順）
        content_type = "OTHER"

        if has_pdf:
            content_type = "PDF_RESOURCE"
        elif has_external_iframe:
            content_type = "EXTERNAL_LINKS"
        elif youtube_urls and paragraph_count >= 5:
            content_type = "YOUTUBE_EMBEDDED_WITH_TEXT"
        elif youtube_urls and paragraph_count < 5:
            content_type = "YOUTUBE_EMBEDDED"
        elif link_count >= 10 and paragraph_count < 5:
            content_type = "LIST_PAGE"
        elif is_qa:
            content_type = "Q_AND_A_LIST"
        elif paragraph_count >= 5:
            content_type = "TEXT_ARTICLE"

        return {
            "content_type": content_type,
            "paragraph_count": paragraph_count,
            "link_count": link_count,
            "youtube_urls": youtube_urls,
            "images": images,
            "has_pdf": has_pdf,
            "error": None
        }


class MarkdownReportGenerator:
    """分類結果をMarkdownレポートとして出力"""

    def __init__(self, results: List[Dict]):
        self.results = results

    def generate(self, output_path: Path):
        """Markdownレポートを生成"""
        lines = []

        # ヘッダー
        lines.append("# affiliateman.site コンテンツタイプ分類レポート")
        lines.append("")
        lines.append("## 分類日時")
        lines.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        lines.append("")
        lines.append("## 概要")
        lines.append(f"全{len(self.results)}URLのコンテンツタイプを自動分類しました。")
        lines.append("")
        lines.append("---")
        lines.append("")

        # カテゴリ別分類結果
        lines.append("## カテゴリ別分類結果")
        lines.append("")

        # カテゴリごとにグループ化
        by_category = {}
        for result in self.results:
            category = result.get('category', 'その他')
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(result)

        # カテゴリ番号を付与
        category_num = 1
        for category, items in by_category.items():
            lines.append(f"### {category_num}. {category}（{len(items)}件）")
            lines.append("")

            # テーブルヘッダー
            lines.append("| # | タイトル | URL | コンテンツタイプ | 段落数 | 画像数 | YouTube | 備考 |")
            lines.append("|---|---------|-----|---------------|-------|-------|---------|------|")

            # テーブル行
            for idx, item in enumerate(items, start=1):
                title = item.get('title', '').replace('|', '\\|')
                url = item.get('url', '')
                content_type_code = item.get('content_type', 'OTHER')
                content_type_label = ContentTypeClassifier.CONTENT_TYPES.get(content_type_code, 'その他')
                paragraph_count = item.get('paragraph_count', 0)
                image_count = len(item.get('images', []))
                youtube_urls = item.get('youtube_urls', [])
                youtube_display = "○" if youtube_urls else "-"
                error = item.get('error', '')
                remarks = error if error else "-"

                lines.append(f"| {idx} | {title} | {url} | {content_type_label} | {paragraph_count} | {image_count} | {youtube_display} | {remarks} |")

            lines.append("")

            # 画像詳細（画像が存在する記事のみ）
            has_images = any(len(item.get('images', [])) > 0 for item in items)
            if has_images:
                lines.append(f"#### {category} - 画像詳細")
                lines.append("")

                for item in items:
                    images = item.get('images', [])
                    if images:
                        title = item.get('title', '')
                        lines.append(f"**{title}**")
                        lines.append("")
                        for img in images:
                            alt_text = img.get('alt', '(altなし)')
                            img_url = img.get('url', '')
                            position = img.get('position', 0)
                            lines.append(f"{position}. ![{alt_text}]({img_url})")
                            if img.get('width') or img.get('height'):
                                lines.append(f"   - サイズ: {img.get('width', '?')} x {img.get('height', '?')}")
                        lines.append("")

            lines.append("---")
            lines.append("")
            category_num += 1

        # コンテンツタイプ別統計
        lines.append("## コンテンツタイプ別統計")
        lines.append("")

        type_counts = {}
        type_image_counts = {}
        for result in self.results:
            ct = result.get('content_type', 'OTHER')
            type_counts[ct] = type_counts.get(ct, 0) + 1

            image_count = len(result.get('images', []))
            if ct not in type_image_counts:
                type_image_counts[ct] = []
            type_image_counts[ct].append(image_count)

        lines.append("| コンテンツタイプ | 件数 | 割合 | 平均画像数 |")
        lines.append("|----------------|-----|------|-----------|")

        total = len(self.results)
        for ct_code, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
            ct_label = ContentTypeClassifier.CONTENT_TYPES.get(ct_code, 'その他')
            percentage = (count / total * 100) if total > 0 else 0
            avg_images = sum(type_image_counts[ct_code]) / len(type_image_counts[ct_code]) if type_image_counts[ct_code] else 0
            lines.append(f"| {ct_label} | {count} | {percentage:.1f}% | {avg_images:.1f}枚 |")

        lines.append("")
        lines.append("---")
        lines.append("")

        # メタ情報
        lines.append("## メタ情報")
        lines.append("")
        lines.append(f"- 総URL数: {total}件")
        lines.append(f"- 総画像数: {sum(len(r.get('images', [])) for r in self.results)}枚")
        lines.append(f"- YouTube埋め込み: {sum(1 for r in self.results if r.get('youtube_urls'))}件")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("**作成者**: Claude (Sonnet 4.5)")
        lines.append("")

        # ファイル書き込み
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        print(f"\n✓ レポート生成完了: {output_path}")


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(description='affiliateman.site コンテンツタイプ分類')
    parser.add_argument('--test', action='store_true', help='テストモード（最初の5件のみ処理）')
    args = parser.parse_args()

    print("=" * 60)
    print("affiliateman.site コンテンツタイプ分類スクリプト")
    print("=" * 60)
    print()

    # URLリスト読み込み
    print(f"URLリスト読み込み: {ALL_URLS_FILE}")
    url_parser = URLListParser(ALL_URLS_FILE)
    urls = url_parser.parse()
    print(f"✓ {len(urls)}件のURLを抽出")
    print()

    # テストモード
    if args.test:
        urls = urls[:5]
        print(f"[テストモード] 最初の{len(urls)}件のみ処理します")
        print()

    # ログイン
    classifier = ContentTypeClassifier()
    if not classifier.login():
        print("ログインに失敗しました。終了します。")
        return

    # 分類処理
    results = []
    total = len(urls)

    for idx, url_data in enumerate(urls, start=1):
        url = url_data['url']
        title = url_data['title']
        category = url_data['category']

        print(f"処理中: {idx}/{total} - {title}")
        print(f"  URL: {url}")

        classification = classifier.classify(url)

        result = {
            **url_data,
            **classification
        }
        results.append(result)

        content_type_label = ContentTypeClassifier.CONTENT_TYPES.get(
            classification['content_type'], 'その他'
        )
        print(f"  タイプ: {content_type_label}")
        print(f"  段落: {classification['paragraph_count']}, "
              f"画像: {len(classification['images'])}, "
              f"YouTube: {len(classification['youtube_urls'])}")
        print()

        # レート制限
        if idx < total:
            time.sleep(1)

    # レポート生成
    print("=" * 60)
    print("レポート生成中...")
    print("=" * 60)
    print()

    report_gen = MarkdownReportGenerator(results)
    report_gen.generate(OUTPUT_FILE)

    print()
    print("=" * 60)
    print("完了！")
    print("=" * 60)


if __name__ == "__main__":
    main()
