#!/usr/bin/env python3
"""
X Timeline Collector
====================

AI業界インフルエンサー50名のタイムラインを監視し、
高エンゲージメント投稿を自動収集するスクリプト。

主要機能:
- Twitter API v2でタイムライン取得
- エンゲージメント率によるフィルタリング（imp>1000, ER>5%, 24時間以内）
- スコアリング: (likes + RTs + replies) / impressions
- 上位5-10件の投稿を抽出
- JSON形式でデータ保存

使用方法:
    python x_timeline_collector.py --config ../config/automation_config.yaml --output ../data/x_timeline_$(date +%Y%m%d).json

必須環境変数:
    TWITTER_API_KEY: Twitter API Key
    TWITTER_API_SECRET: Twitter API Secret
    TWITTER_ACCESS_TOKEN: Twitter Access Token
    TWITTER_ACCESS_SECRET: Twitter Access Token Secret
    TWITTER_BEARER_TOKEN: Twitter Bearer Token (API v2用)

作成日: 2026-01-01
プロジェクト: SNS運用戦略 Month 1 Week 1
"""

import os
import sys
import json
import yaml
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import argparse

# Twitter API v2クライアント（tweepyを使用）
try:
    import tweepy
except ImportError:
    print("❌ tweepyがインストールされていません。")
    print("   インストール: pip install tweepy")
    sys.exit(1)

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class Tweet:
    """ツイートデータクラス"""
    tweet_id: str
    author_id: str
    author_username: str
    author_name: str
    text: str
    created_at: str
    impressions: int
    likes: int
    retweets: int
    replies: int
    engagement_rate: float
    engagement_score: float
    url: str


class XTimelineCollector:
    """Xタイムラインコレクター"""

    def __init__(self, config_path: Optional[Path] = None):
        """
        初期化

        Args:
            config_path: 設定ファイルパス（automation_config.yaml）
        """
        self.config = self._load_config(config_path)
        self.client = self._initialize_api_client()
        self.influencers = self.config.get('influencers', [])
        self.filters = self.config.get('filters', {})

    def _load_config(self, config_path: Optional[Path]) -> Dict:
        """
        設定ファイル読み込み

        Args:
            config_path: 設定ファイルパス

        Returns:
            設定辞書
        """
        if config_path and config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            logger.info(f"✅ 設定ファイル読み込み完了: {config_path}")
            return config
        else:
            logger.warning("⚠️  設定ファイルが見つかりません。デフォルト設定を使用します。")
            return self._default_config()

    def _default_config(self) -> Dict:
        """デフォルト設定"""
        return {
            'influencers': [],
            'filters': {
                'min_impressions': 1000,
                'min_engagement_rate': 0.05,  # 5%
                'time_window_hours': 24,
                'top_n': 10
            }
        }

    def _initialize_api_client(self) -> tweepy.Client:
        """
        Twitter API v2クライアント初期化

        Returns:
            tweepy.Client インスタンス

        Raises:
            ValueError: 環境変数が設定されていない場合
        """
        bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')

        if not bearer_token:
            raise ValueError(
                "❌ TWITTER_BEARER_TOKEN環境変数が設定されていません。\n"
                "   .envファイルに以下を追加してください:\n"
                "   TWITTER_BEARER_TOKEN=your_bearer_token_here"
            )

        client = tweepy.Client(
            bearer_token=bearer_token,
            wait_on_rate_limit=True
        )
        logger.info("✅ Twitter API v2クライアント初期化完了")
        return client

    def fetch_user_timeline(self, username: str, max_results: int = 100) -> List[Dict]:
        """
        特定ユーザーのタイムライン取得

        Args:
            username: Xユーザー名（@なし）
            max_results: 取得最大件数（デフォルト100、最大100）

        Returns:
            ツイートリスト
        """
        try:
            # ユーザーID取得
            user = self.client.get_user(username=username)
            if not user.data:
                logger.warning(f"⚠️  ユーザーが見つかりません: @{username}")
                return []

            user_id = user.data.id

            # タイムライン取得（過去24時間）
            cutoff_time = datetime.now(timezone.utc) - timedelta(
                hours=self.filters['time_window_hours']
            )

            tweets = self.client.get_users_tweets(
                id=user_id,
                max_results=max_results,
                tweet_fields=[
                    'created_at', 'public_metrics', 'author_id',
                    'conversation_id', 'entities'
                ],
                expansions=['author_id'],
                start_time=cutoff_time.isoformat()
            )

            if not tweets.data:
                logger.info(f"   @{username}: 新規ツイートなし（24時間以内）")
                return []

            # ユーザー情報取得
            users_dict = {user.id: user for user in tweets.includes.get('users', [])}

            tweet_list = []
            for tweet in tweets.data:
                author = users_dict.get(tweet.author_id)
                metrics = tweet.public_metrics

                # インプレッション数（API v2では取得不可のため、近似値を使用）
                # 実際にはX Premium APIまたはAnalytics APIが必要
                # ここでは likes + retweets + replies を基にした推定値を使用
                estimated_impressions = self._estimate_impressions(metrics)

                tweet_data = {
                    'tweet_id': tweet.id,
                    'author_id': tweet.author_id,
                    'author_username': author.username if author else username,
                    'author_name': author.name if author else username,
                    'text': tweet.text,
                    'created_at': tweet.created_at.isoformat(),
                    'likes': metrics['like_count'],
                    'retweets': metrics['retweet_count'],
                    'replies': metrics['reply_count'],
                    'impressions': estimated_impressions,
                    'url': f"https://x.com/{author.username if author else username}/status/{tweet.id}"
                }
                tweet_list.append(tweet_data)

            logger.info(f"   @{username}: {len(tweet_list)}件のツイートを取得")
            return tweet_list

        except tweepy.errors.TweepyException as e:
            logger.error(f"❌ @{username}のタイムライン取得エラー: {e}")
            return []

    def _estimate_impressions(self, metrics: Dict) -> int:
        """
        インプレッション数の推定

        Twitter API v2の無料版ではインプレッション数が取得できないため、
        エンゲージメント数から推定値を計算。

        推定ロジック:
        - 一般的なエンゲージメント率: 1-3%
        - エンゲージメント総数 = likes + retweets + replies
        - 推定imp = エンゲージメント総数 / 0.02（2%と仮定）

        Args:
            metrics: public_metrics辞書

        Returns:
            推定インプレッション数
        """
        engagement = (
            metrics['like_count'] +
            metrics['retweet_count'] +
            metrics['reply_count']
        )

        # エンゲージメント率2%と仮定
        estimated_impressions = int(engagement / 0.02) if engagement > 0 else 0

        # 最小値を設定（ゼロ除算回避）
        return max(estimated_impressions, engagement * 10)

    def calculate_engagement_metrics(self, tweet_data: Dict) -> Tweet:
        """
        エンゲージメント指標を計算

        Args:
            tweet_data: ツイートデータ辞書

        Returns:
            Tweetデータクラス
        """
        impressions = tweet_data['impressions']
        likes = tweet_data['likes']
        retweets = tweet_data['retweets']
        replies = tweet_data['replies']

        # エンゲージメント率: (likes + RTs + replies) / impressions
        engagement_rate = (
            (likes + retweets + replies) / impressions
            if impressions > 0 else 0
        )

        # エンゲージメントスコア: 重み付け合計
        # いいね: 1倍, RT: 3倍, リプライ: 5倍
        engagement_score = likes + (retweets * 3) + (replies * 5)

        return Tweet(
            tweet_id=tweet_data['tweet_id'],
            author_id=tweet_data['author_id'],
            author_username=tweet_data['author_username'],
            author_name=tweet_data['author_name'],
            text=tweet_data['text'],
            created_at=tweet_data['created_at'],
            impressions=impressions,
            likes=likes,
            retweets=retweets,
            replies=replies,
            engagement_rate=engagement_rate,
            engagement_score=engagement_score,
            url=tweet_data['url']
        )

    def filter_tweets(self, tweets: List[Tweet]) -> List[Tweet]:
        """
        フィルタリング条件を適用

        Args:
            tweets: ツイートリスト

        Returns:
            フィルタリング後のツイートリスト
        """
        min_impressions = self.filters['min_impressions']
        min_engagement_rate = self.filters['min_engagement_rate']

        filtered = [
            tweet for tweet in tweets
            if (
                tweet.impressions >= min_impressions and
                tweet.engagement_rate >= min_engagement_rate
            )
        ]

        logger.info(
            f"📊 フィルタリング結果: {len(tweets)}件 → {len(filtered)}件 "
            f"(imp≥{min_impressions}, ER≥{min_engagement_rate*100}%)"
        )
        return filtered

    def collect_all_timelines(self) -> List[Tweet]:
        """
        全インフルエンサーのタイムラインを収集

        Returns:
            全ツイートリスト
        """
        all_tweets = []

        logger.info(f"🔍 {len(self.influencers)}名のインフルエンサーのタイムライン収集開始...")

        for influencer in self.influencers:
            username = influencer.get('username')
            if not username:
                continue

            # タイムライン取得
            tweet_list = self.fetch_user_timeline(username)

            # エンゲージメント指標計算
            for tweet_data in tweet_list:
                tweet = self.calculate_engagement_metrics(tweet_data)
                all_tweets.append(tweet)

        logger.info(f"✅ 収集完了: {len(all_tweets)}件のツイート")
        return all_tweets

    def get_top_tweets(self, tweets: List[Tweet], top_n: Optional[int] = None) -> List[Tweet]:
        """
        上位N件のツイートを取得

        Args:
            tweets: ツイートリスト
            top_n: 取得件数（Noneの場合は設定ファイルの値）

        Returns:
            上位ツイートリスト
        """
        if top_n is None:
            top_n = self.filters['top_n']

        # エンゲージメントスコアでソート
        sorted_tweets = sorted(
            tweets,
            key=lambda t: t.engagement_score,
            reverse=True
        )

        top_tweets = sorted_tweets[:top_n]

        logger.info(f"🏆 上位{len(top_tweets)}件を抽出（エンゲージメントスコア順）")
        return top_tweets

    def save_results(self, tweets: List[Tweet], output_path: Path):
        """
        結果をJSON形式で保存

        Args:
            tweets: ツイートリスト
            output_path: 出力ファイルパス
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            'collected_at': datetime.now(timezone.utc).isoformat(),
            'total_tweets': len(tweets),
            'tweets': [asdict(tweet) for tweet in tweets]
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        logger.info(f"💾 結果を保存: {output_path}")

    def print_summary(self, tweets: List[Tweet]):
        """
        収集結果のサマリー表示

        Args:
            tweets: ツイートリスト
        """
        if not tweets:
            logger.warning("⚠️  収集されたツイートがありません。")
            return

        print("\n" + "="*80)
        print("📊 収集結果サマリー")
        print("="*80)
        print(f"総ツイート数: {len(tweets)}件\n")

        for i, tweet in enumerate(tweets, 1):
            print(f"【{i}位】 @{tweet.author_username}")
            print(f"   テキスト: {tweet.text[:100]}{'...' if len(tweet.text) > 100 else ''}")
            print(f"   インプレッション: {tweet.impressions:,}")
            print(f"   エンゲージメント率: {tweet.engagement_rate*100:.2f}%")
            print(f"   スコア: {tweet.engagement_score:,} (❤️{tweet.likes} 🔁{tweet.retweets} 💬{tweet.replies})")
            print(f"   URL: {tweet.url}")
            print()


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(
        description='X Timeline Collector - AI業界インフルエンサーの高エンゲージメント投稿を収集'
    )
    parser.add_argument(
        '--config',
        type=Path,
        default=Path(__file__).parent.parent / 'config' / 'automation_config.yaml',
        help='設定ファイルパス（デフォルト: ../config/automation_config.yaml）'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path(__file__).parent.parent / 'data' / f'x_timeline_{datetime.now().strftime("%Y%m%d")}.json',
        help='出力ファイルパス（デフォルト: ../data/x_timeline_YYYYMMDD.json）'
    )
    parser.add_argument(
        '--top-n',
        type=int,
        help='上位N件のみ保存（デフォルト: 設定ファイルの値）'
    )

    args = parser.parse_args()

    try:
        # コレクター初期化
        collector = XTimelineCollector(config_path=args.config)

        # タイムライン収集
        all_tweets = collector.collect_all_timelines()

        # フィルタリング
        filtered_tweets = collector.filter_tweets(all_tweets)

        # 上位N件取得
        top_tweets = collector.get_top_tweets(filtered_tweets, top_n=args.top_n)

        # 結果保存
        collector.save_results(top_tweets, args.output)

        # サマリー表示
        collector.print_summary(top_tweets)

        logger.info("✅ 収集処理が正常に完了しました。")

    except Exception as e:
        logger.error(f"❌ エラーが発生しました: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
