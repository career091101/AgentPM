#!/usr/bin/env python3
"""
X Timeline Tweet Extractor from DOM HTML

MCPのread_pageツールで取得したHTML文字列を解析し、ツイート情報を抽出します。
日本語aria-labelに対応した正規表現でエンゲージメント指標を抽出します。

使用方法:
    python3 extract_tweets_from_dom.py --input <html_file> --output <json_file>

例:
    python3 extract_tweets_from_dom.py --input /tmp/x_dom_cycle_1.html --output /tmp/tweets_cycle_1.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class TweetExtractor:
    """DOM HTMLからツイート情報を抽出するクラス"""

    # 日本語aria-label正規表現パターン
    LIKE_PATTERN = re.compile(r'([0-9,]+)\s*件のいいね')
    RETWEET_PATTERN = re.compile(r'([0-9,]+)\s*件のリポスト')
    REPLY_PATTERN = re.compile(r'([0-9,]+)\s*件の返信')

    # 英語aria-label正規表現パターン（フォールバック）
    LIKE_PATTERN_EN = re.compile(r'([0-9,]+)\s+Likes?')
    RETWEET_PATTERN_EN = re.compile(r'([0-9,]+)\s+Retweets?')
    REPLY_PATTERN_EN = re.compile(r'([0-9,]+)\s+Replies')

    # ツイートID抽出パターン
    TWEET_ID_PATTERN = re.compile(r'/status/(\d+)')

    def __init__(self, html_content: str):
        """
        Args:
            html_content: read_pageツールで取得したHTML文字列
        """
        self.html_content = html_content
        self.tweets: List[Dict] = []

    def parse_aria_label(self, label: str, pattern_ja: re.Pattern, pattern_en: re.Pattern) -> int:
        """aria-labelから数値を抽出

        Args:
            label: aria-label文字列
            pattern_ja: 日本語パターン
            pattern_en: 英語パターン（フォールバック）

        Returns:
            抽出された数値（見つからない場合は0）
        """
        if not label:
            return 0

        # 日本語パターン優先
        match = pattern_ja.search(label)
        if match:
            return int(match.group(1).replace(',', ''))

        # 英語パターン（フォールバック）
        match = pattern_en.search(label)
        if match:
            return int(match.group(1).replace(',', ''))

        return 0

    def extract_tweet_id(self, article_html: str) -> Optional[str]:
        """記事HTMLからツイートIDを抽出

        Args:
            article_html: <article>タグ内のHTML

        Returns:
            ツイートID（見つからない場合はNone）
        """
        match = self.TWEET_ID_PATTERN.search(article_html)
        return match.group(1) if match else None

    def extract_text(self, article_html: str) -> str:
        """記事HTMLからツイート本文を抽出

        Args:
            article_html: <article>タグ内のHTML

        Returns:
            ツイート本文（見つからない場合は空文字列）
        """
        # data-testid="tweetText" を探す
        pattern = re.compile(r'data-testid="tweetText"[^>]*>(.*?)</div>', re.DOTALL)
        match = pattern.search(article_html)

        if match:
            text_html = match.group(1)
            # HTMLタグを除去（簡易的な処理）
            text = re.sub(r'<[^>]+>', '', text_html)
            # HTML エンティティのデコード（一部）
            text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
            return text.strip()

        return ''

    def extract_timestamp(self, article_html: str) -> str:
        """記事HTMLからタイムスタンプを抽出

        Args:
            article_html: <article>タグ内のHTML

        Returns:
            ISO形式のタイムスタンプ（見つからない場合は空文字列）
        """
        # <time datetime="..."> を探す
        pattern = re.compile(r'<time[^>]+datetime="([^"]+)"')
        match = pattern.search(article_html)
        return match.group(1) if match else ''

    def extract_engagement_from_article(self, article_html: str) -> Dict[str, int]:
        """記事HTMLからエンゲージメント指標を抽出

        Args:
            article_html: <article>タグ内のHTML

        Returns:
            {'likes': int, 'retweets': int, 'replies': int}
        """
        # data-testid="like" のaria-label
        like_pattern = re.compile(r'data-testid="like"[^>]+aria-label="([^"]*)"')
        like_match = like_pattern.search(article_html)
        like_label = like_match.group(1) if like_match else ''
        likes = self.parse_aria_label(like_label, self.LIKE_PATTERN, self.LIKE_PATTERN_EN)

        # data-testid="retweet" のaria-label
        retweet_pattern = re.compile(r'data-testid="retweet"[^>]+aria-label="([^"]*)"')
        retweet_match = retweet_pattern.search(article_html)
        retweet_label = retweet_match.group(1) if retweet_match else ''
        retweets = self.parse_aria_label(retweet_label, self.RETWEET_PATTERN, self.RETWEET_PATTERN_EN)

        # data-testid="reply" のaria-label
        reply_pattern = re.compile(r'data-testid="reply"[^>]+aria-label="([^"]*)"')
        reply_match = reply_pattern.search(article_html)
        reply_label = reply_match.group(1) if reply_match else ''
        replies = self.parse_aria_label(reply_label, self.REPLY_PATTERN, self.REPLY_PATTERN_EN)

        return {
            'likes': likes,
            'retweets': retweets,
            'replies': replies
        }

    def extract_tweets(self) -> List[Dict]:
        """HTML全体からツイートリストを抽出

        Returns:
            ツイート情報の辞書リスト
        """
        # <article data-testid="tweet"> を全て抽出
        article_pattern = re.compile(r'<article[^>]*data-testid="tweet"[^>]*>(.*?)</article>', re.DOTALL)
        articles = article_pattern.findall(self.html_content)

        tweets = []

        for article_html in articles:
            try:
                # ツイートID抽出
                tweet_id = self.extract_tweet_id(article_html)
                if not tweet_id:
                    continue  # ツイートIDがない場合はスキップ

                # テキスト抽出
                text = self.extract_text(article_html)

                # タイムスタンプ抽出
                timestamp = self.extract_timestamp(article_html)

                # エンゲージメント指標抽出
                engagement = self.extract_engagement_from_article(article_html)

                tweet = {
                    'tweet_id': tweet_id,
                    'text': text,
                    'likes': engagement['likes'],
                    'retweets': engagement['retweets'],
                    'replies': engagement['replies'],
                    'timestamp': timestamp,
                    'collected_at': datetime.now().isoformat()
                }

                tweets.append(tweet)

            except Exception as e:
                # エラーは記録するが処理は継続
                print(f"⚠️  ツイート抽出エラー: {e}", file=sys.stderr)
                continue

        self.tweets = tweets
        return tweets

    def save_to_json(self, output_path: Path) -> bool:
        """抽出結果をJSONファイルに保存

        Args:
            output_path: 出力先JSONファイルパス

        Returns:
            成功時True、失敗時False
        """
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.tweets, f, ensure_ascii=False, indent=2)

            return True

        except Exception as e:
            print(f"❌ JSON保存エラー: {e}", file=sys.stderr)
            return False


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description='X Timeline DOM HTMLからツイート情報を抽出'
    )
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='入力HTMLファイルパス'
    )
    parser.add_argument(
        '--output',
        type=str,
        required=True,
        help='出力JSONファイルパス'
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    # HTMLファイル読み込み
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"❌ エラー: ファイルが見つかりません: {input_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ エラー: ファイル読み込み失敗: {e}", file=sys.stderr)
        sys.exit(1)

    # ツイート抽出
    extractor = TweetExtractor(html_content)
    tweets = extractor.extract_tweets()

    print(f"✅ {len(tweets)} 件のツイートを抽出しました")

    # JSON保存
    if extractor.save_to_json(output_path):
        print(f"✅ 保存完了: {output_path}")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
