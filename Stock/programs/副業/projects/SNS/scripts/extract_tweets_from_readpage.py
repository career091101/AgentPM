#!/usr/bin/env python3
"""
X Timeline Tweet Extractor from MCP read_page output

MCPのread_pageツールで取得したアクセシビリティツリー出力を解析し、
ツイート情報を抽出します。

使用方法:
    python3 extract_tweets_from_readpage.py --input <text_file> --output <json_file>
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List
from datetime import datetime


class ReadPageTweetExtractor:
    """read_page出力からツイート情報を抽出するクラス"""

    def __init__(self, readpage_output: str):
        """
        Args:
            readpage_output: read_pageツールの出力テキスト
        """
        self.output = readpage_output
        self.tweets: List[Dict] = []

    def extract_tweets(self) -> List[Dict]:
        """read_page出力から全ツイートを抽出

        Returns:
            ツイート情報の辞書リスト
        """
        # article要素で分割
        articles = re.split(r'\n\s*article \[ref_\d+\]', self.output)

        for article_text in articles[1:]:  # 最初の要素はarticle前のテキストなのでスキップ
            try:
                tweet = self._parse_article(article_text)
                if tweet:
                    self.tweets.append(tweet)
            except Exception as e:
                print(f"⚠️  記事解析エラー: {e}", file=sys.stderr)
                continue

        return self.tweets

    def _parse_article(self, article_text: str) -> Dict:
        """記事テキストから1ツイートの情報を抽出

        Args:
            article_text: article要素内のテキスト

        Returns:
            ツイート辞書（抽出できない場合はNone）
        """
        # ツイートID抽出（/status/数字 のURL）
        tweet_id_match = re.search(r'/status/(\d+)', article_text)
        if not tweet_id_match:
            return None
        tweet_id = tweet_id_match.group(1)

        # ユーザー名抽出（@username）
        username_match = re.search(r'@(\w+)', article_text)
        username = username_match.group(1) if username_match else ''

        # ツイート本文抽出（generic要素のテキスト、最長のものを選択）
        # 本文は通常、複数行に渡る長いgeneric要素に含まれる
        generic_texts = re.findall(r'generic "([^"]{20,})"', article_text)
        text = max(generic_texts, key=len) if generic_texts else ''

        # エンゲージメント指標抽出
        # "14 件の返信。返信する"
        replies_match = re.search(r'(\d+[\d,]*)\s*件の返信', article_text)
        replies = int(replies_match.group(1).replace(',', '')) if replies_match else 0

        # "327 件のリポスト件。リポスト"
        retweets_match = re.search(r'(\d+[\d,]*)\s*件のリポスト', article_text)
        retweets = int(retweets_match.group(1).replace(',', '')) if retweets_match else 0

        # "1618 件のいいね。いいねする"
        likes_match = re.search(r'(\d+[\d,]*)\s*件のいいね', article_text)
        likes = int(likes_match.group(1).replace(',', '')) if likes_match else 0

        # タイムスタンプ抽出（"23 時間前"、"1 時間前"等）
        time_match = re.search(r'generic "(\d+(?:時間|分|日))', article_text)
        timestamp_text = time_match.group(1) if time_match else ''

        return {
            'tweet_id': tweet_id,
            'username': username,
            'text': text.strip(),
            'likes': likes,
            'retweets': retweets,
            'replies': replies,
            'timestamp_text': timestamp_text,
            'collected_at': datetime.now().isoformat()
        }

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
        description='MCP read_page出力からツイート情報を抽出'
    )
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='入力テキストファイルパス（read_page出力）'
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

    # テキストファイル読み込み
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            readpage_output = f.read()
    except FileNotFoundError:
        print(f"❌ エラー: ファイルが見つかりません: {input_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ エラー: ファイル読み込み失敗: {e}", file=sys.stderr)
        sys.exit(1)

    # ツイート抽出
    extractor = ReadPageTweetExtractor(readpage_output)
    tweets = extractor.extract_tweets()

    print(f"✅ {len(tweets)} 件のツイートを抽出しました")

    # 簡易統計表示
    with_engagement = sum(1 for t in tweets if t['likes'] > 0 or t['retweets'] > 0 or t['replies'] > 0)
    print(f"   エンゲージメント有り: {with_engagement}/{len(tweets)} ({with_engagement/len(tweets)*100:.1f}%)")

    # JSON保存
    if extractor.save_to_json(output_path):
        print(f"✅ 保存完了: {output_path}")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
