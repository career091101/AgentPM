#!/usr/bin/env python3
"""
Xタイムラインデータから高野式投稿に最適なツイートを評価するスクリプト
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Tuple


class TweetEvaluator:
    """ツイート評価クラス"""

    # AI関連キーワード（大文字・小文字混在、全角・半角混在対応）
    AI_HIGH_KEYWORDS = [
        "LLM", "生成AI", "AIエージェント", "Claude", "GPT", "Gemini",
        "ChatGPT", "プロンプト", "RAG", "Copilot", "AI モデル", "機械学習モデル",
        "transformer", "Transformer", "ファインチューニング", "fine-tuning",
        "embedding", "エンベディング", "AI API", "OpenAI", "Anthropic",
        "自然言語処理", "NLP", "深層学習", "ディープラーニング", "AI開発"
    ]

    AI_MEDIUM_KEYWORDS = [
        "OpenAI", "Anthropic", "Google AI", "Microsoft AI", "Meta AI",
        "DeepMind", "AI企業", "AI スタートアップ", "資金調達", "AI ニュース"
    ]

    AI_LOW_KEYWORDS = [
        "ML", "機械学習", "データサイエンス", "自動化", "automation",
        "予測モデル", "アルゴリズム"
    ]

    # 除外キーワード（これらが主題の場合はスコアを下げる）
    EXCLUDE_KEYWORDS = [
        "IQ", "リーダーシップ", "経営論", "人材育成", "マネジメント",
        "ビジネススキル", "コミュニケーション"
    ]

    def __init__(self):
        pass

    def normalize_text(self, text: str) -> str:
        """テキストの正規化（全角・半角統一）"""
        # 全角英数字を半角に変換
        normalized = text.translate(str.maketrans(
            "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ０１２３４５６７８９",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        ))
        return normalized

    def evaluate_ai_relevance(self, text: str) -> int:
        """AI関連度を評価（0-3点）"""
        normalized_text = self.normalize_text(text)

        # 除外キーワードチェック（AI技術の言及がない場合）
        has_ai_tech = any(keyword.lower() in normalized_text.lower()
                          for keyword in self.AI_HIGH_KEYWORDS + self.AI_MEDIUM_KEYWORDS)
        has_exclude = any(keyword in text for keyword in self.EXCLUDE_KEYWORDS)

        if has_exclude and not has_ai_tech:
            return 0

        # 高レベル: 明示的なAI技術キーワード
        for keyword in self.AI_HIGH_KEYWORDS:
            if keyword.lower() in normalized_text.lower():
                return 3

        # 中レベル: AI企業・組織名 + ニュース/発表/資金調達
        for keyword in self.AI_MEDIUM_KEYWORDS:
            if keyword in text:
                if any(news_word in text for news_word in ["ニュース", "発表", "資金調達", "リリース", "発売"]):
                    return 2

        # 低レベル: ML/データサイエンス/自動化が主題
        for keyword in self.AI_LOW_KEYWORDS:
            if keyword in text:
                # 主題として扱われているかチェック（文の先頭付近にある）
                if text.find(keyword) < len(text) // 2:
                    return 1

        return 0

    def evaluate_takano_fit(self, text: str, timestamp_text: str) -> Dict[str, int]:
        """高野式パターン適合度を評価（各要素0-1点）"""
        details = {
            "数値データ": 0,
            "論争性": 0,
            "速報性": 0,
            "専門家見解": 0,
            "実体験": 0,
            "予測": 0
        }

        # 1. 数値データ含有（2つ以上の数字）
        numbers = re.findall(r'\d+(?:,\d+)*(?:\.\d+)?[%億万千円ドル]?', text)
        if len(numbers) >= 2:
            details["数値データ"] = 1

        # 2. 論争性・議論性
        controversy_keywords = [
            "しかし", "だが", "一方で", "とはいえ", "問題", "課題", "批判",
            "賛否", "議論", "異論", "反論", "疑問", "懸念"
        ]
        if any(keyword in text for keyword in controversy_keywords):
            details["論争性"] = 1

        # 3. 速報性・新規性（タイムスタンプから24時間以内か判定）
        try:
            tweet_time = datetime.strptime(timestamp_text, "%a %b %d %H:%M:%S %z %Y")
            now = datetime.now(tweet_time.tzinfo)
            if (now - tweet_time).total_seconds() < 86400:  # 24時間
                # 速報キーワードも確認
                breaking_keywords = ["速報", "新発表", "リリース", "発表", "公開", "ローンチ"]
                if any(keyword in text for keyword in breaking_keywords):
                    details["速報性"] = 1
        except:
            pass

        # 4. 専門家の見解
        expert_keywords = ["研究者", "教授", "博士", "CEO", "CTO", "専門家", "氏", "さん曰く", "によると"]
        if any(keyword in text for keyword in expert_keywords):
            details["専門家見解"] = 1

        # 5. 実体験・ケーススタディ
        experience_keywords = [
            "使ってみた", "試した", "実際に", "体験", "導入した", "実装した",
            "やってみた", "検証", "テスト", "結果"
        ]
        if any(keyword in text for keyword in experience_keywords):
            details["実体験"] = 1

        # 6. 予測・未来洞察
        prediction_keywords = [
            "なる", "だろう", "予測", "見込み", "予想", "将来", "今後",
            "2026", "2027", "2030", "未来"
        ]
        if any(keyword in text for keyword in prediction_keywords):
            details["予測"] = 1

        return details

    def recommend_pattern(self, ai_score: int, takano_details: Dict[str, int], text: str) -> Tuple[int, str]:
        """高野式7パターンから最適なパターンを推奨"""

        # パターン1: 断定型主張 → データ展開
        if takano_details["数値データ"] == 1 and takano_details["論争性"] == 1:
            return (1, "数値データと論争性を含む断定型主張に最適")

        # パターン2: 問題提起 → 反論 → 正論
        if takano_details["論争性"] == 1 and takano_details["専門家見解"] == 1:
            return (2, "専門家の見解を含む論争的内容で問題提起型に適合")

        # パターン3: ニュース引用 → 深掘り
        if takano_details["速報性"] == 1 or "ニュース" in text or "発表" in text:
            return (3, "速報性・ニュース性が高く引用型に最適")

        # パターン4: リスト型衝撃ファクト
        if takano_details["数値データ"] == 1 and ai_score >= 2:
            return (4, "数値データとAI関連性が高くリスト型に適合")

        # パターン5: イベント体験レポート
        if takano_details["実体験"] == 1:
            return (5, "実体験・ケーススタディを含むレポート型に最適")

        # パターン6: サービス紹介CTA
        if "サービス" in text or "ツール" in text or "製品" in text:
            return (6, "サービス・製品紹介を含みCTA型に適合")

        # パターン7: 有料サロン訴求（デフォルト）
        return (7, "予測・洞察を含む深掘り型コンテンツに適合")

    def evaluate_tweet(self, tweet: Dict) -> Dict:
        """単一ツイートを評価"""
        text = tweet["text"]
        timestamp = tweet["timestamp_text"]

        # AI関連度評価
        ai_score = self.evaluate_ai_relevance(text)

        # AI関連度が0の場合はスキップ
        if ai_score == 0:
            return None

        # 高野式適合度評価
        takano_details = self.evaluate_takano_fit(text, timestamp)
        takano_score = sum(takano_details.values())

        # 総合品質スコア
        total_score = ai_score + takano_score

        # 推奨パターン
        pattern, pattern_reason = self.recommend_pattern(ai_score, takano_details, text)

        return {
            "tweet_id": tweet["tweet_id"],
            "username": tweet["username"],
            "text": text,
            "likes": tweet["likes"],
            "retweets": tweet["retweets"],
            "ai_relevance_score": ai_score,
            "takano_fit_details": takano_details,
            "takano_fit_score": takano_score,
            "total_quality_score": total_score,
            "recommended_pattern": pattern,
            "pattern_reason": pattern_reason,
            "timestamp_text": timestamp
        }

    def evaluate_all_tweets(self, input_file: str, output_file: str):
        """全ツイートを評価してJSON出力"""
        # 入力ファイル読み込み
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        tweets = data["tweets"]
        evaluated_tweets = []

        print(f"総ツイート数: {len(tweets)}")

        for i, tweet in enumerate(tweets):
            result = self.evaluate_tweet(tweet)
            if result:
                evaluated_tweets.append(result)

            if (i + 1) % 50 == 0:
                print(f"進捗: {i + 1}/{len(tweets)} 件処理完了")

        # AI関連度順にソート（降順）
        evaluated_tweets.sort(key=lambda x: (x["total_quality_score"], x["likes"]), reverse=True)

        # 出力ファイル生成
        output_data = {
            "evaluated_at": datetime.now().isoformat(),
            "total_evaluated": len(evaluated_tweets),
            "source_file": input_file,
            "evaluation_criteria": {
                "ai_relevance": "0-3点（高=3, 中=2, 低=1, 対象外=0）",
                "takano_fit": "0-6点（数値データ、論争性、速報性、専門家見解、実体験、予測の6要素）",
                "total_quality": "0-9点（AI関連度 + 高野式適合度）"
            },
            "tweets": evaluated_tweets
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"\n評価完了:")
        print(f"  AI関連ツイート数: {len(evaluated_tweets)}/{len(tweets)} 件")
        print(f"  出力ファイル: {output_file}")

        # トップ10を表示
        print("\n【総合品質スコア トップ10】")
        for i, tweet in enumerate(evaluated_tweets[:10]):
            print(f"{i+1}. スコア {tweet['total_quality_score']} (AI:{tweet['ai_relevance_score']}, 高野:{tweet['takano_fit_score']}) - @{tweet['username']}")
            print(f"   パターン{tweet['recommended_pattern']}: {tweet['pattern_reason']}")
            print(f"   {tweet['text'][:100]}...")
            print()


def main():
    input_file = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260105_164603.json"
    output_file = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/quality_scored_tweets_20260105.json"

    evaluator = TweetEvaluator()
    evaluator.evaluate_all_tweets(input_file, output_file)


if __name__ == "__main__":
    main()
