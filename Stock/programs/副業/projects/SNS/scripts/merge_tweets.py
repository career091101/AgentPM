#!/usr/bin/env python3
"""
X Timeline Tweets Merger and Filter

複数サイクルで収集したツイートJSONファイルをマージし、
重複排除、エンゲージメントスコア計算、フィルタリングを行います。

使用方法:
    python3 merge_tweets.py --input /tmp/tweets_cycle_*.json --output data/x_timeline_20260101.json --config config/automation_config.yaml --top-n 10

例:
    python3 merge_tweets.py --input "/tmp/tweets_cycle_*.json" --output data/x_timeline_20260101.json --top-n 10
"""

import argparse
import glob
import json
import sys
import yaml
from pathlib import Path
from typing import Dict, List
from datetime import datetime


class TweetMerger:
    """ツイートマージ・フィルタリングクラス"""

    # デフォルト設定
    DEFAULT_MIN_IMPRESSIONS = 1000
    DEFAULT_MIN_ENGAGEMENT_RATE = 0.05  # 5%
    DEFAULT_TOP_N = 10
    DEFAULT_ENGAGEMENT_WEIGHTS = {
        'like': 1,
        'retweet': 3,
        'reply': 5
    }

    def __init__(self, config_path: Path = None):
        """
        Args:
            config_path: automation_config.yamlのパス（オプション）
        """
        self.config = self._load_config(config_path) if config_path else {}
        self.tweets: List[Dict] = []

    def _load_config(self, config_path: Path) -> Dict:
        """設定ファイルを読み込む

        Args:
            config_path: YAMLファイルパス

        Returns:
            設定辞書
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"⚠️  設定ファイル読み込みエラー（デフォルト値を使用）: {e}", file=sys.stderr)
            return {}

    def load_tweets_from_files(self, file_pattern: str) -> int:
        """パターンに一致する全JSONファイルからツイートを読み込む

        Args:
            file_pattern: ファイルパターン（例: "/tmp/tweets_cycle_*.json"）

        Returns:
            読み込んだファイル数
        """
        files = glob.glob(file_pattern)

        if not files:
            print(f"⚠️  パターンに一致するファイルが見つかりません: {file_pattern}", file=sys.stderr)
            return 0

        all_tweets = []
        for file_path in sorted(files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    tweets = json.load(f)

                if isinstance(tweets, list):
                    all_tweets.extend(tweets)
                else:
                    print(f"⚠️  {file_path} はリスト形式ではありません", file=sys.stderr)

            except Exception as e:
                print(f"⚠️  {file_path} 読み込みエラー: {e}", file=sys.stderr)
                continue

        self.tweets = all_tweets
        print(f"✅ {len(files)} ファイルから {len(all_tweets)} 件のツイートを読み込みました")
        return len(files)

    def deduplicate(self) -> int:
        """ツイートIDで重複排除

        Returns:
            削除された重複件数
        """
        before_count = len(self.tweets)

        seen_ids = set()
        unique_tweets = []

        for tweet in self.tweets:
            tweet_id = tweet.get('tweet_id')
            if tweet_id and tweet_id not in seen_ids:
                seen_ids.add(tweet_id)
                unique_tweets.append(tweet)

        self.tweets = unique_tweets
        removed_count = before_count - len(unique_tweets)

        print(f"✅ 重複排除: {removed_count} 件削除（{before_count} → {len(unique_tweets)}）")
        return removed_count

    def calculate_engagement_metrics(self) -> None:
        """全ツイートにエンゲージメント指標を計算・追加"""
        weights = self.config.get('engagement_weights', self.DEFAULT_ENGAGEMENT_WEIGHTS)

        for tweet in self.tweets:
            likes = tweet.get('likes', 0)
            retweets = tweet.get('retweets', 0)
            replies = tweet.get('replies', 0)

            # エンゲージメントスコア計算
            engagement_score = (
                likes * weights.get('like', 1) +
                retweets * weights.get('retweet', 3) +
                replies * weights.get('reply', 5)
            )
            tweet['engagement_score'] = engagement_score

            # インプレッション推定（エンゲージメント率2%と仮定）
            total_engagement = likes + retweets + replies
            impressions_estimated = int(total_engagement / 0.02) if total_engagement > 0 else 0
            tweet['impressions_estimated'] = impressions_estimated

            # エンゲージメント率計算
            engagement_rate = (
                total_engagement / impressions_estimated
                if impressions_estimated > 0 else 0
            )
            tweet['engagement_rate'] = engagement_rate

        print(f"✅ エンゲージメント指標計算完了")

    def filter_tweets(self, min_impressions: int = None, min_engagement_rate: float = None) -> int:
        """フィルタリング基準に基づいてツイートをフィルタ

        Args:
            min_impressions: 最小インプレッション数
            min_engagement_rate: 最小エンゲージメント率

        Returns:
            フィルタ後の件数
        """
        filters_config = self.config.get('filters', {})

        min_imp = min_impressions if min_impressions is not None else filters_config.get('min_impressions', self.DEFAULT_MIN_IMPRESSIONS)
        min_er = min_engagement_rate if min_engagement_rate is not None else filters_config.get('min_engagement_rate', self.DEFAULT_MIN_ENGAGEMENT_RATE)

        before_count = len(self.tweets)

        filtered_tweets = [
            tweet for tweet in self.tweets
            if (tweet.get('impressions_estimated', 0) >= min_imp and
                tweet.get('engagement_rate', 0) >= min_er)
        ]

        self.tweets = filtered_tweets
        print(f"✅ フィルタリング: {before_count - len(filtered_tweets)} 件削除（{before_count} → {len(filtered_tweets)}）")
        print(f"   基準: impressions ≥ {min_imp}, engagement_rate ≥ {min_er*100:.0f}%")
        return len(filtered_tweets)

    def sort_and_top_n(self, top_n: int = None) -> int:
        """エンゲージメントスコア順にソートし、上位N件を取得

        Args:
            top_n: 上位N件を取得（Noneの場合は全件）

        Returns:
            取得後の件数
        """
        n = top_n if top_n is not None else self.config.get('filters', {}).get('top_n', self.DEFAULT_TOP_N)

        # エンゲージメントスコア降順でソート
        self.tweets.sort(key=lambda t: t.get('engagement_score', 0), reverse=True)

        if n and len(self.tweets) > n:
            self.tweets = self.tweets[:n]
            print(f"✅ 上位 {n} 件を抽出")

        return len(self.tweets)

    def save_to_json(self, output_path: Path) -> bool:
        """結果をJSONファイルに保存

        Args:
            output_path: 出力先JSONファイルパス

        Returns:
            成功時True、失敗時False
        """
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # メタデータ付きで保存
            output_data = {
                'collected_at': datetime.now().isoformat(),
                'total_tweets': len(self.tweets),
                'tweets': self.tweets
            }

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, ensure_ascii=False, indent=2)

            print(f"✅ 保存完了: {output_path}")
            print(f"   最終ツイート数: {len(self.tweets)}")
            return True

        except Exception as e:
            print(f"❌ JSON保存エラー: {e}", file=sys.stderr)
            return False

    def print_summary(self) -> None:
        """結果サマリーを表示"""
        if not self.tweets:
            print("\nツイートがありません")
            return

        print("\n" + "="*60)
        print("📊 X Timeline Collection Summary")
        print("="*60)

        top_3 = self.tweets[:3]
        for i, tweet in enumerate(top_3, 1):
            print(f"\n{i}. ❤️  {tweet.get('likes', 0)} 🔁 {tweet.get('retweets', 0)} 💬 {tweet.get('replies', 0)}")
            print(f"   Score: {tweet.get('engagement_score', 0)}, ER: {tweet.get('engagement_rate', 0)*100:.1f}%")
            text = tweet.get('text', '')
            preview = text[:60] + '...' if len(text) > 60 else text
            print(f"   {preview}")

        print("\n" + "="*60)


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description='複数サイクルのツイートJSONをマージ・フィルタ'
    )
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='入力JSONファイルパターン（例: "/tmp/tweets_cycle_*.json"）'
    )
    parser.add_argument(
        '--output',
        type=str,
        required=True,
        help='出力JSONファイルパス'
    )
    parser.add_argument(
        '--config',
        type=str,
        default=None,
        help='設定ファイルパス（automation_config.yaml）'
    )
    parser.add_argument(
        '--top-n',
        type=int,
        default=None,
        help='上位N件を抽出（デフォルト: 10）'
    )
    parser.add_argument(
        '--min-impressions',
        type=int,
        default=None,
        help='最小インプレッション数（デフォルト: 1000）'
    )
    parser.add_argument(
        '--min-engagement-rate',
        type=float,
        default=None,
        help='最小エンゲージメント率（デフォルト: 0.05）'
    )

    args = parser.parse_args()

    output_path = Path(args.output)
    config_path = Path(args.config) if args.config else None

    # マージャー初期化
    merger = TweetMerger(config_path)

    # 処理フロー
    if merger.load_tweets_from_files(args.input) == 0:
        print("❌ 処理するファイルがありません", file=sys.stderr)
        sys.exit(1)

    merger.deduplicate()
    merger.calculate_engagement_metrics()
    merger.filter_tweets(args.min_impressions, args.min_engagement_rate)
    merger.sort_and_top_n(args.top_n)

    # サマリー表示
    merger.print_summary()

    # 保存
    if merger.save_to_json(output_path):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
