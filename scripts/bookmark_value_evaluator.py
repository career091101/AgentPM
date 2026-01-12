#!/usr/bin/env python3
"""
X Bookmark Value Evaluator

823件の実ブックマークデータから抽出した7軸評価モデルで
X投稿のブックマーク価値を0-100点でスコアリング。

使用例:
    python bookmark_value_evaluator.py --text "投稿本文" --author "username" --likes 1234
    python bookmark_value_evaluator.py --json post.json
    python bookmark_value_evaluator.py --batch posts.json
"""

import re
import json
import argparse
from datetime import datetime, timedelta
from typing import Dict, Any, List
from pathlib import Path


class BookmarkValueEvaluator:
    """X投稿のブックマーク価値評価クラス"""

    # TOP 20 専門性著者（実データから抽出）
    SPECIALIST_AUTHORS = {
        'tetumemo': 10,         # avg 2,761 likes
        'kenn': 10,             # avg 1,535 likes
        'shinyaaa_code': 9,     # avg 1,258 likes
        'AIBoom4': 9,           # avg 1,237 likes
        'ai_database': 8,       # avg 1,150 likes
        'kumarobo': 8,
        'kamome885': 7,
        '_kentakodama': 7,
        'gomi_ningen': 7,
        'shibe97': 6,
        'takapon_jp': 6,
        'ai_syatyou': 6,
        'AINow_jp': 5,
        'shota7180': 5,
        'masa_kazama': 5,
        'yamato_sokonan': 5,
        'hironsan13': 4,
        'masuidrive': 4,
        'yoheinakajima': 4,
        'ylabo_jp': 4,
    }

    def evaluate(self, post: Dict[str, Any]) -> Dict[str, Any]:
        """
        投稿を7軸評価モデルで評価

        Args:
            post: 投稿データ（text, author_username, engagement, posted_at）

        Returns:
            評価結果辞書（総合スコア、判定、詳細スコア等）
        """
        text = post.get('text', '')
        author = post.get('author_username', '').replace('@', '')
        engagement = post.get('engagement', {})
        posted_at = post.get('posted_at', datetime.now().isoformat())

        # 7軸評価
        scores = {
            '実践的価値': self._eval_practical_value(text),
            '最新性': self._eval_recency(posted_at),
            'データドリブン': self._eval_data_driven(text),
            '引用・参照性': self._eval_citation(text),
            '集合知評価': self._eval_engagement(engagement),
            '発信者専門性': self._eval_author(author),
            '情報の深さ': self._eval_depth(text),
        }

        total = sum(scores.values())

        return {
            '総合スコア': round(total, 1),
            '判定': self._judge(total),
            '評価詳細': scores,
            '理由': self._generate_reason(scores, text, engagement, author),
            'カテゴリ': self._categorize(text),
            '概念的タイプ': self._classify_type(text),
            '推奨アクション': self._recommend_action(total),
        }

    def _eval_practical_value(self, text: str) -> int:
        """実践的価値（20点満点）- 概念的学習の質を重視"""
        score = 0

        # 理論・原理（最高評価、10.8%が該当）
        if any(kw in text for kw in ['とは', 'とは？', '仕組み', '原理', '理論', '解説', 'なぜ']):
            score += 10

        # 比較・分析（10.1%が該当）
        if any(kw in text for kw in ['vs', 'VS', 'より', 'に比べて', '比較', '違い', '差']):
            score += 6

        # トレンド・ニュース（9.5%が該当）
        if any(kw in text for kw in ['発表', 'リリース', '公開', 'ローンチ', '速報']):
            score += 4

        # すぐ実装可能（ボーナス、0.5%の稀少価値）
        has_url = bool(re.search(r'https?://[^\s]+', text))
        has_code = bool(re.search(r'```|`[^`]+`', text))
        if has_url and (has_code or 'ダウンロード' in text or 'インストール' in text):
            score += 10

        # ベストプラクティス（1.5%）
        if any(kw in text for kw in ['Tips', 'ベストプラクティス', 'コツ', 'ポイント', '注意点']):
            score += 3

        return min(score, 20)

    def _eval_recency(self, posted_at: str) -> int:
        """最新性（15点満点）"""
        try:
            posted_date = datetime.fromisoformat(posted_at.replace('Z', '+00:00'))
            now = datetime.now(posted_date.tzinfo) if posted_date.tzinfo else datetime.now()
            days_ago = (now - posted_date).days

            if days_ago <= 7:
                return 15  # 1週間以内
            elif days_ago <= 30:
                return 10  # 1ヶ月以内
            elif days_ago <= 90:
                return 5   # 3ヶ月以内
            else:
                return 0   # それ以上古い
        except Exception:
            return 5  # パース失敗時はデフォルト

    def _eval_data_driven(self, text: str) -> int:
        """データドリブン（15点満点）"""
        score = 0

        # 数値データの有無
        if re.search(r'\d+%', text):  # パーセンテージ
            score += 5
        if re.search(r'\d+倍', text):  # 倍数
            score += 5
        if re.search(r'\d+件', text):  # 件数
            score += 3

        # 実験結果・統計
        if any(kw in text for kw in ['実験', '結果', '検証', 'データ', '統計', '測定']):
            score += 5

        # 具体的数値
        if re.search(r'\d{2,}', text):  # 2桁以上の数値
            score += 2

        return min(score, 15)

    def _eval_citation(self, text: str) -> int:
        """引用・参照性（15点満点）- 36.7%が引用あり"""
        score = 0

        # 引用符（36.7%が該当）
        if '「' in text or '」' in text or '"' in text:
            score += 10

        # URL参照
        url_count = len(re.findall(r'https?://', text))
        score += min(url_count * 3, 5)

        return min(score, 15)

    def _eval_engagement(self, engagement: Dict[str, int]) -> int:
        """集合知評価（15点満点）- いいね・RT相関0.89"""
        likes = engagement.get('likes', 0)

        # いいね基準（実データ分布から）
        if likes >= 2000:
            return 15  # 超高エンゲージメント（TOP 5%）
        elif likes >= 1000:
            return 12  # 高エンゲージメント（TOP 15%）
        elif likes >= 500:
            return 8   # 中エンゲージメント
        elif likes >= 100:
            return 5   # 低エンゲージメント
        else:
            return 2   # 最低限

    def _eval_author(self, author: str) -> int:
        """発信者専門性（10点満点）"""
        return self.SPECIALIST_AUTHORS.get(author, 3)  # デフォルト3点

    def _eval_depth(self, text: str) -> int:
        """情報の深さ（10点満点）"""
        score = 0

        # 深い洞察のキーワード
        if any(kw in text for kw in ['洞察', '考察', '本質', '背景', '文脈', '意味']):
            score += 5

        # 批判的視点
        if any(kw in text for kw in ['課題', '限界', '問題', 'しかし', 'ただし', 'だが']):
            score += 3

        # 今後の展望
        if any(kw in text for kw in ['今後', '将来', '可能性', '期待', '予測']):
            score += 2

        return min(score, 10)

    def _judge(self, score: float) -> str:
        """総合判定"""
        if score >= 80:
            return 'VERY HIGH (即ブックマーク)'
        elif score >= 60:
            return 'HIGH (ブックマーク推奨)'
        elif score >= 40:
            return 'MEDIUM (興味あれば)'
        else:
            return 'LOW (スキップ推奨)'

    def _generate_reason(self, scores: Dict[str, int], text: str,
                        engagement: Dict[str, int], author: str) -> str:
        """判定理由を生成"""
        reasons = []

        # 上位3項目を抽出
        top_3 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

        for item, score in top_3:
            if item == '実践的価値' and score >= 10:
                if 'とは' in text or '仕組み' in text:
                    reasons.append('理論的解説あり')
                elif 'vs' in text or '比較' in text:
                    reasons.append('比較分析あり')
            elif item == '集合知評価' and score >= 10:
                likes = engagement.get('likes', 0)
                reasons.append(f'高エンゲージメント（{likes}いいね）')
            elif item == '発信者専門性' and score >= 8:
                reasons.append(f'専門性の高い著者（@{author}）')
            elif item == 'データドリブン' and score >= 10:
                reasons.append('数値データ・実験結果あり')
            elif item == '引用・参照性' and score >= 10:
                reasons.append('引用・参照リンクあり')

        category = self._categorize(text)
        conceptual_type = self._classify_type(text)

        reason = f"{category}カテゴリ、{conceptual_type}タイプ。"
        if reasons:
            reason += " " + "、".join(reasons) + "。"

        return reason

    def _categorize(self, text: str) -> str:
        """カテゴリ判定（70.7%がAI・生成AI）"""
        text_lower = text.lower()
        if any(kw in text_lower for kw in ['claude', 'gpt', 'ai', 'llm', 'openai', 'anthropic', 'gemini']):
            return 'AI・生成AI'
        elif any(kw in text for kw in ['ビジネス', '起業', 'スタートアップ', '経営']):
            return 'ビジネス・起業'
        elif any(kw in text for kw in ['開発', 'エンジニア', 'プログラミング', 'コード']):
            return '開発'
        elif any(kw in text for kw in ['デザイン', 'UX', 'UI']):
            return 'デザイン・UX'
        elif any(kw in text for kw in ['生産性', 'ツール', '効率']):
            return '生産性'
        else:
            return 'その他'

    def _classify_type(self, text: str) -> str:
        """概念的タイプ判定"""
        if any(kw in text for kw in ['とは', 'とは？', '仕組み', '原理', '理論']):
            return '理論・原理'
        elif any(kw in text for kw in ['vs', 'VS', 'より', '比較', '違い']):
            return '比較・分析'
        elif any(kw in text for kw in ['発表', 'リリース', 'ローンチ']):
            return 'トレンド・ニュース'
        elif any(kw in text for kw in ['まとめ', '〇選', 'リスト', '一覧']):
            return 'まとめ'
        elif any(kw in text for kw in ['やってみた', '試した', '使った', '使ってみた']):
            return '事例紹介'
        elif any(kw in text for kw in ['Tips', 'コツ', 'ベストプラクティス']):
            return 'ベストプラクティス'
        elif any(kw in text for kw in ['思う', '考える', '視点', '洞察']):
            return '思考・考察'
        else:
            return 'その他'

    def _recommend_action(self, score: float) -> str:
        """推奨アクション"""
        if score >= 80:
            return '即ブックマーク＋Notion登録＋要精読'
        elif score >= 60:
            return 'ブックマーク＋後でNotion整理'
        elif score >= 40:
            return 'とりあえず保存'
        else:
            return 'スキップ推奨'

    def evaluate_batch(self, posts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """複数投稿を一括評価"""
        results = []
        for post in posts:
            result = self.evaluate(post)
            result['original_post'] = post
            results.append(result)

        # スコア順にソート
        results.sort(key=lambda x: x['総合スコア'], reverse=True)
        return results


def main():
    parser = argparse.ArgumentParser(
        description='X投稿のブックマーク価値を7軸評価モデルで判定'
    )

    # 入力方式
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--text', help='投稿本文')
    input_group.add_argument('--json', help='投稿JSON ファイル')
    input_group.add_argument('--batch', help='複数投稿JSON ファイル（配列）')

    # オプション引数（--text 使用時）
    parser.add_argument('--author', default='', help='著者名（@なし）')
    parser.add_argument('--likes', type=int, default=0, help='いいね数')
    parser.add_argument('--retweets', type=int, default=0, help='RT数')
    parser.add_argument('--replies', type=int, default=0, help='返信数')
    parser.add_argument('--posted-at', help='投稿日時（ISO 8601形式）')

    # 出力オプション
    parser.add_argument('--output', help='結果出力先JSONファイル')
    parser.add_argument('--pretty', action='store_true', help='見やすい形式で出力')

    args = parser.parse_args()

    evaluator = BookmarkValueEvaluator()

    # 入力データ準備
    if args.text:
        post = {
            'text': args.text,
            'author_username': args.author,
            'engagement': {
                'likes': args.likes,
                'retweets': args.retweets,
                'replies': args.replies,
            },
            'posted_at': args.posted_at or datetime.now().isoformat(),
        }
        result = evaluator.evaluate(post)
        results = [result]

    elif args.json:
        with open(args.json, 'r', encoding='utf-8') as f:
            post = json.load(f)
        result = evaluator.evaluate(post)
        results = [result]

    elif args.batch:
        with open(args.batch, 'r', encoding='utf-8') as f:
            posts = json.load(f)
        results = evaluator.evaluate_batch(posts)

    # 出力
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"結果を {args.output} に保存しました。")
    else:
        if args.pretty:
            for i, result in enumerate(results, 1):
                print(f"\n{'='*60}")
                print(f"評価 #{i}")
                print(f"{'='*60}")
                print(f"総合スコア: {result['総合スコア']}点")
                print(f"判定: {result['判定']}")
                print(f"カテゴリ: {result['カテゴリ']}")
                print(f"概念的タイプ: {result['概念的タイプ']}")
                print(f"\n評価詳細:")
                for axis, score in result['評価詳細'].items():
                    print(f"  {axis}: {score}点")
                print(f"\n理由: {result['理由']}")
                print(f"推奨アクション: {result['推奨アクション']}")
        else:
            print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
