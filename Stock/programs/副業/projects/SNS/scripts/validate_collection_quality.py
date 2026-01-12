#!/usr/bin/env python3
"""
X Timeline Collection Quality Validator

収集したツイートデータの品質を検証し、DOM構造変更による破綻を早期検知します。

使用方法:
    python3 validate_collection_quality.py <json_file>

例:
    python3 validate_collection_quality.py data/x_timeline_20260101.json
"""

import json
import sys
from pathlib import Path
from typing import Dict, List


class CollectionQualityValidator:
    """ツイート収集データの品質検証クラス"""

    # 品質基準
    MIN_ENGAGEMENT_RATE = 0.80  # 80%以上のツイートにエンゲージメントデータが必要
    MIN_TOTAL_TWEETS = 50  # 最低収集件数
    EXPECTED_TWEETS = 180  # 期待収集件数（20サイクル × 9件/サイクル平均）

    def __init__(self, json_file: Path):
        """
        Args:
            json_file: 検証対象のJSONファイルパス
        """
        self.json_file = json_file
        self.tweets: List[Dict] = []
        self.stats: Dict = {}

    def load_data(self) -> bool:
        """JSONファイルを読み込む

        Returns:
            成功時True、失敗時False
        """
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # リスト形式とメタデータ付き辞書形式の両方に対応
            if isinstance(data, list):
                self.tweets = data
            elif isinstance(data, dict) and 'tweets' in data:
                self.tweets = data['tweets']
            else:
                print(f"❌ エラー: JSONファイルがリスト形式またはメタデータ付き辞書形式ではありません")
                return False

            return True

        except FileNotFoundError:
            print(f"❌ エラー: ファイルが見つかりません: {self.json_file}")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ エラー: JSON解析エラー: {e}")
            return False
        except Exception as e:
            print(f"❌ エラー: ファイル読み込みエラー: {e}")
            return False

    def calculate_stats(self) -> Dict:
        """統計情報を計算

        Returns:
            統計情報の辞書
        """
        total_tweets = len(self.tweets)

        if total_tweets == 0:
            return {
                'total_tweets': 0,
                'with_engagement': 0,
                'engagement_rate': 0.0,
                'avg_likes': 0,
                'avg_retweets': 0,
                'avg_replies': 0,
                'top_3_likes': []
            }

        # エンゲージメントデータ有りのツイート数
        with_engagement = 0
        total_likes = 0
        total_retweets = 0
        total_replies = 0

        for tweet in self.tweets:
            likes = tweet.get('likes', 0)
            retweets = tweet.get('retweets', 0)
            replies = tweet.get('replies', 0)

            if likes > 0 or retweets > 0 or replies > 0:
                with_engagement += 1

            total_likes += likes
            total_retweets += retweets
            total_replies += replies

        # Top 3 ツイート（いいね数順）
        top_3 = sorted(self.tweets, key=lambda t: t.get('likes', 0), reverse=True)[:3]
        top_3_likes = [
            {
                'tweet_id': t.get('tweet_id', 'unknown'),
                'likes': t.get('likes', 0),
                'retweets': t.get('retweets', 0),
                'replies': t.get('replies', 0),
                'text_preview': t.get('text', '')[:50] + '...' if len(t.get('text', '')) > 50 else t.get('text', '')
            }
            for t in top_3
        ]

        self.stats = {
            'total_tweets': total_tweets,
            'with_engagement': with_engagement,
            'engagement_rate': with_engagement / total_tweets if total_tweets > 0 else 0,
            'avg_likes': total_likes / total_tweets if total_tweets > 0 else 0,
            'avg_retweets': total_retweets / total_tweets if total_tweets > 0 else 0,
            'avg_replies': total_replies / total_tweets if total_tweets > 0 else 0,
            'top_3_likes': top_3_likes
        }

        return self.stats

    def validate(self) -> bool:
        """品質検証を実行

        Returns:
            品質基準を満たす場合True、満たさない場合False
        """
        stats = self.stats

        # 検証結果の表示
        print("\n" + "="*60)
        print(f"📊 X Timeline Collection Quality Report")
        print("="*60)
        print(f"\n📁 ファイル: {self.json_file.name}")
        print(f"📅 ファイル更新日時: {self.json_file.stat().st_mtime}")

        print(f"\n【収集統計】")
        print(f"  総ツイート数: {stats['total_tweets']}")
        print(f"  エンゲージメント有り: {stats['with_engagement']} ({stats['engagement_rate']*100:.1f}%)")
        print(f"  エンゲージメント無し: {stats['total_tweets'] - stats['with_engagement']}")

        print(f"\n【平均エンゲージメント】")
        print(f"  平均いいね数: {stats['avg_likes']:.1f}")
        print(f"  平均リツイート数: {stats['avg_retweets']:.1f}")
        print(f"  平均リプライ数: {stats['avg_replies']:.1f}")

        print(f"\n【Top 3 ツイート（いいね順）】")
        for i, tweet in enumerate(stats['top_3_likes'], 1):
            print(f"  {i}. ❤️ {tweet['likes']} 🔁 {tweet['retweets']} 💬 {tweet['replies']}")
            print(f"     {tweet['text_preview']}")

        # 品質判定
        print(f"\n【品質判定】")

        passed = True

        # 基準1: 最低収集件数
        if stats['total_tweets'] < self.MIN_TOTAL_TWEETS:
            print(f"  ❌ 総ツイート数不足: {stats['total_tweets']} < {self.MIN_TOTAL_TWEETS}")
            passed = False
        else:
            print(f"  ✅ 総ツイート数: {stats['total_tweets']} ≥ {self.MIN_TOTAL_TWEETS}")

        # 基準2: エンゲージメント率
        if stats['engagement_rate'] < self.MIN_ENGAGEMENT_RATE:
            print(f"  ❌ エンゲージメント率低下: {stats['engagement_rate']*100:.1f}% < {self.MIN_ENGAGEMENT_RATE*100:.0f}%")
            print(f"     ⚠️  DOM構造変更の可能性があります！")
            print(f"     ⚠️  final_x_collector.js の正規表現を確認してください。")
            passed = False
        else:
            print(f"  ✅ エンゲージメント率: {stats['engagement_rate']*100:.1f}% ≥ {self.MIN_ENGAGEMENT_RATE*100:.0f}%")

        # 基準3: 期待収集件数との比較（警告のみ）
        if stats['total_tweets'] < self.EXPECTED_TWEETS * 0.7:  # 期待値の70%未満
            print(f"  ⚠️  収集件数が期待値より少ない: {stats['total_tweets']} < {self.EXPECTED_TWEETS}")
            print(f"     （期待値の {stats['total_tweets']/self.EXPECTED_TWEETS*100:.0f}%）")

        # 基準4: Top 3 ツイートの品質（警告のみ）
        if stats['top_3_likes'] and stats['top_3_likes'][0]['likes'] == 0:
            print(f"  ⚠️  Top 1ツイートのいいね数が0です（データ抽出失敗の可能性）")

        print("\n" + "="*60)

        if passed:
            print("✅ 品質検証: 合格")
            print("="*60 + "\n")
            return True
        else:
            print("❌ 品質検証: 不合格")
            print("="*60 + "\n")
            return False

    def run(self) -> bool:
        """品質検証プロセス全体を実行

        Returns:
            検証成功時True、失敗時False
        """
        # データ読み込み
        if not self.load_data():
            return False

        # 統計計算
        self.calculate_stats()

        # 検証実行
        return self.validate()


def main():
    """メイン関数"""
    if len(sys.argv) != 2:
        print("使用方法: python3 validate_collection_quality.py <json_file>")
        print("\n例:")
        print("  python3 validate_collection_quality.py data/x_timeline_20260101.json")
        sys.exit(1)

    json_file = Path(sys.argv[1])

    validator = CollectionQualityValidator(json_file)

    if validator.run():
        sys.exit(0)  # 成功
    else:
        sys.exit(1)  # 失敗


if __name__ == "__main__":
    main()
