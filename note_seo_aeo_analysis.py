#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import json
import re
import time
from datetime import datetime
from collections import Counter
import urllib.parse

class NoteArticleAnalyzer:
    def __init__(self):
        self.articles = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def analyze_article(self, url):
        """記事のSEO/AEO要素を分析"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')

            # タイトル取得
            title_tag = soup.find('title') or soup.find('h1')
            title = title_tag.text.strip() if title_tag else 'N/A'

            # メタディスクリプション
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            description = meta_desc.get('content', '') if meta_desc else 'N/A'

            # 記事本文取得
            article_content = soup.find('article') or soup.find('div', class_='article')
            if not article_content:
                # note.comの構造に合わせた探索
                article_content = soup.find('div', class_=re.compile(r'noteBody|article-content'))

            if not article_content:
                article_content = soup

            text_content = article_content.get_text()
            char_count = len(text_content.replace('\n', '').replace(' ', ''))

            # 見出し構造
            h2_count = len(article_content.find_all('h2'))
            h3_count = len(article_content.find_all('h3'))

            # ハッシュタグ取得 (note.com特有)
            hashtags = article_content.find_all(re.compile(r'a'), href=re.compile(r'#'))
            hashtag_count = len(hashtags)
            hashtag_list = [h.text.strip() for h in hashtags[:10]]

            # キーワード密度計算
            words = re.findall(r'\w+', text_content.lower())
            word_freq = Counter(words)

            # リスト構造
            ul_li_count = len(article_content.find_all('li'))

            # 画像数
            img_count = len(article_content.find_all('img'))

            # 段落数
            paragraph_count = len(article_content.find_all('p'))

            # 外部リンク数
            external_links = 0
            internal_links = 0
            for link in article_content.find_all('a', href=True):
                href = link.get('href', '')
                if href.startswith('http'):
                    if 'note.com' not in href:
                        external_links += 1
                    else:
                        internal_links += 1

            # スキ数・コメント数の推定（ページ内スクリプトから抽出可能性）
            # JSONLDデータの確認
            json_ld = soup.find('script', type='application/ld+json')
            engagement_data = {}
            if json_ld:
                try:
                    ld_data = json.loads(json_ld.string)
                    if 'aggregateRating' in ld_data:
                        engagement_data['rating_count'] = ld_data['aggregateRating'].get('ratingCount', 'N/A')
                except:
                    pass

            # FAQ形式の有無
            faq_present = len(soup.find_all(re.compile(r'h\d'), string=re.compile(r'Q\.|質問|FAQ'))) > 0

            # Answer-First構造（最初の200文字でポイント判定）
            first_paragraph = article_content.find('p')
            first_text = first_paragraph.text if first_paragraph else ''
            has_answer_first = len(first_text) > 30

            article_data = {
                'url': url,
                'title': title,
                'title_length': len(title),
                'char_count': char_count,
                'description': description[:100] if description != 'N/A' else 'N/A',
                'h2_count': h2_count,
                'h3_count': h3_count,
                'total_headings': h2_count + h3_count,
                'hashtag_count': hashtag_count,
                'hashtags': ','.join(hashtag_list),
                'ul_li_count': ul_li_count,
                'img_count': img_count,
                'paragraph_count': paragraph_count,
                'external_links': external_links,
                'internal_links': internal_links,
                'faq_present': faq_present,
                'answer_first': has_answer_first,
                'top_keywords': ','.join([w for w, _ in word_freq.most_common(5)]),
            }

            return article_data

        except Exception as e:
            print(f"Error analyzing {url}: {str(e)}")
            return None

    def calculate_seo_score(self, article):
        """SEOスコアを計算（0-100）"""
        score = 0

        # タイトル長（30-60文字が最適）
        title_len = article['title_length']
        if 30 <= title_len <= 60:
            score += 15
        elif 20 <= title_len <= 70:
            score += 10

        # 文字数（2000-5000字が最適）
        char_count = article['char_count']
        if 2000 <= char_count <= 5000:
            score += 20
        elif 1500 <= char_count <= 6000:
            score += 15

        # 見出し構造（H2：3-5個が最適）
        if 3 <= article['h2_count'] <= 5:
            score += 15
        elif 2 <= article['h2_count'] <= 7:
            score += 10

        # ハッシュタグ（3-5個が最適）
        if 3 <= article['hashtag_count'] <= 5:
            score += 10
        elif 1 <= article['hashtag_count'] <= 7:
            score += 5

        # リスト構造
        if article['ul_li_count'] > 0:
            score += 8

        # 外部リンク（3個以上が理想）
        if article['external_links'] >= 3:
            score += 10
        elif article['external_links'] >= 1:
            score += 5

        # 画像（2個以上が理想）
        if article['img_count'] >= 2:
            score += 7
        else:
            score += 3

        return min(score, 100)

    def calculate_aeo_score(self, article):
        """AEOスコアを計算（0-100）"""
        score = 0

        # FAQ形式
        if article['faq_present']:
            score += 25

        # Answer-First構造
        if article['answer_first']:
            score += 20

        # 見出しの充実度
        if article['total_headings'] >= 5:
            score += 15
        elif article['total_headings'] >= 3:
            score += 10

        # リスト形式
        if article['ul_li_count'] >= 5:
            score += 15
        elif article['ul_li_count'] >= 2:
            score += 10

        # 内部リンク（エンティティ相互参照）
        if article['internal_links'] >= 2:
            score += 15
        elif article['internal_links'] >= 1:
            score += 10

        return min(score, 100)

# メイン処理
if __name__ == '__main__':
    analyzer = NoteArticleAnalyzer()

    # サンプルURLリスト（実際にはGoogleから取得）
    sample_urls = [
        'https://note.com/ai_labo/n/n123456789abcd',
        # 複数のURLを追加
    ]

    print("Note記事SEO/AEO分析ツール起動")
    print(f"分析開始時刻: {datetime.now().isoformat()}")
