#!/usr/bin/env python3
"""
Batch 1585-1604の画像説明を保存
【2023年8月】質疑応答まとめ - image_35～image_54（20枚）
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1585-1604の詳細な画像説明（記事内容に基づいた実際の説明）
batch_descriptions = [
    {
        "index": 1585,
        "filename": "image_35.png",
        "description": "SNS運用に関するジャンル選定についての質疑応答。インスタグラムのフィード投稿とリール投稿の最適化戦略についての相談とアドバイスが記載されている。"
    },
    {
        "index": 1586,
        "filename": "image_36.png",
        "description": "SNS発信ジャンル・コンセプト設計に関する5つの質問と回答。アカウント設計のポイント、ターゲット設定、コンテンツ方向性について詳細なアドバイスが掲載されている。"
    },
    {
        "index": 1587,
        "filename": "image_37.png",
        "description": "参入予定のジャンルに関する相談。既存競合との差別化ポイント、ニッチ分野でのアカウント構築戦略についての指導内容が記載されている。"
    },
    {
        "index": 1588,
        "filename": "image_38.png",
        "description": "恋愛アカウント運用の具体的な実行計画。1週間のコンテンツ制作スケジュール、投稿頻度、フォロワー増加施策についての詳細な指針が掲載されている。"
    },
    {
        "index": 1589,
        "filename": "image_39.png",
        "description": "AI×恋愛×心理学ジャンルでのアカウント参入戦略。差別化ポイント、コンテンツ企画の具体例、マネタイズまでの導線が示されている。"
    },
    {
        "index": 1590,
        "filename": "image_40.png",
        "description": "マッチングアプリ関連のアカウント設計についての相談。ターゲットユーザー定義、コンテンツテーマ、マネタイズ方法についての実践的なアドバイスが記載されている。"
    },
    {
        "index": 1591,
        "filename": "image_41.png",
        "description": "不動産関連SNSアカウントの運用戦略。物件紹介、投資情報、不動産トレンド発信における効果的なコンテンツ形式についての提案が掲載されている。"
    },
    {
        "index": 1592,
        "filename": "image_42.png",
        "description": "SNS発信における優先順位の整理についての相談。複数のプラットフォーム・ジャンルがある場合の戦略的フォーカス方法についての指導が記載されている。"
    },
    {
        "index": 1593,
        "filename": "image_43.png",
        "description": "インスタグラムのジャンル選定と『尖らせ方』についての相談。ニッチ戦略、ポジショニング、他のアカウントとの差別化についての実践的なテクニックが掲載されている。"
    },
    {
        "index": 1594,
        "filename": "image_44.png",
        "description": "過去に運用していたアカウントの再活用戦略。既存フォロワーベースの有効活用、ジャンル変更時の注意点についての相談と回答が記載されている。"
    },
    {
        "index": 1595,
        "filename": "image_45.png",
        "description": "アカウントのジャンル選定プロセスについての質問。市場分析、トレンド把握、自分の強みに基づいた最適なジャンル選定方法についての指導が掲載されている。"
    },
    {
        "index": 1596,
        "filename": "image_46.png",
        "description": "SNS運用におけるマネタイズ方法についての相談。アフィリエイト、コンテンツ販売、サービス販売など複数の収益化方法と選択基準が記載されている。"
    },
    {
        "index": 1597,
        "filename": "image_47.png",
        "description": "各SNSプラットフォーム（Instagram、TikTok、Twitter等）の攻略方法についての比較。各プラットフォームの最新トレンド、アルゴリズム対策、伸びやすいコンテンツ形式が掲載されている。"
    },
    {
        "index": 1598,
        "filename": "image_48.png",
        "description": "美容関連アカウントのTips機能を活用したマネタイズについての相談。Tipsの販売戦略、価格設定、販売実績の事例が記載されている。"
    },
    {
        "index": 1599,
        "filename": "image_49.png",
        "description": "インフルエンサーとしての報酬妥当性についての質問。SNS運用でのギャラ相場、案件単価、コンサルティング料金についての市場相場が掲載されている。"
    },
    {
        "index": 1600,
        "filename": "image_50.png",
        "description": "Twitter運用における効果的なリプ回し戦略と投稿時間帯についての相談。エンゲージメント最大化、フォロワー増加の時間帯、キャンペーン企画についての指導が記載されている。"
    },
    {
        "index": 1601,
        "filename": "image_51.png",
        "description": "Twitterで伸びるツイート内容についての相談。有益ツイート、バズ狙いツイート、ブランディングツイートのバランス、コンテンツ設計についての指導が掲載されている。"
    },
    {
        "index": 1602,
        "filename": "image_52.png",
        "description": "恋愛攻略系アカウントのフォロワー伸ばし方についての相談。ターゲット層の明確化、共感性の高いコンテンツ、リール戦略についての実践的なアドバイスが記載されている。"
    },
    {
        "index": 1603,
        "filename": "image_53.png",
        "description": "参考にすべき成功しているアカウント事例の紹介。恋愛ジャンル、SNS×マーケティング、複合スキル発信者など参考になるアカウントが複数掲載されている。"
    },
    {
        "index": 1604,
        "filename": "image_54.png",
        "description": "SNS伸びない場合の競合分析と対策についての相談。ライバルアカウントが存在しない時の戦略、ニッチ開拓、Twitter チャレンジ戦略についての指導が記載されている。"
    }
]

def update_inventory_with_descriptions(batch_descriptions):
    """image_inventory_progress.jsonを読み込み、説明を追加"""

    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'
    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {inventory[idx]['filename']}: 説明更新")

    total = len(inventory)

    # 自動生成でない詳細説明のカウント
    def is_auto_generated(desc):
        if not desc:
            return True
        auto_patterns = [
            "運用に関する説明画像または投稿サムネイル。記事",
            "運用に関する説明画像または図解。",
            "記事のバナー画像またはメインビジュアル。",
            "関連コンテンツ。"
        ]
        for pattern in auto_patterns:
            if pattern in desc:
                return True
        return False

    completed = sum(1 for item in inventory if not is_auto_generated(item.get('description', '')))

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    progress_percentage = (completed / total) * 100
    print(f"\n✓ Batch 1585-1604 完了")
    print(f"詳細説明済み: {completed}/{total} ({progress_percentage:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
