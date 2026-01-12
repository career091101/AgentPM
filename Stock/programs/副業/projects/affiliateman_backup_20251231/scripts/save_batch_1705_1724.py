#!/usr/bin/env python3
"""
Batch 1705-1724の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1705-1724の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1705,
        "filename": "image_22.png",
        "description": "Instagram初期段階でのアカウント運用とジャンル選定についての相談。ユーザーがサロンでの就職と兼任しながらInstagramアカウントを運用する際の「恋愛×地方」という特化テーマの選定についてのアドバイス。"
    },
    {
        "index": 1706,
        "filename": "image_23.png",
        "description": "美容系アカウント運用における「note」や「コンサル」販売の戦略についての質問と回答。リール投稿のメインテーマ設定、サプリメント&アフィリの売上目標設定についてのガイダンス。"
    },
    {
        "index": 1707,
        "filename": "image_24.png",
        "description": "Twitter活用とInstagram攻略についての具体的な質問。男性向けコンテンツ発信における恋愛イメージの作り方や、女性フォロワーの獲得方法についてのコンサルティング内容。"
    },
    {
        "index": 1708,
        "filename": "image_25.png",
        "description": "メンズ美容アカウント運用における「人物主導」vs「情報主導」の戦略選択についての質問。Instagram上で人物性（美容の知識）を打ち出すことの重要性についての説明。"
    },
    {
        "index": 1709,
        "filename": "image_26.png",
        "description": "マッチングアプリのマネタイズ戦略を第一軸としたInstagramアカウント運用についての相談。恋愛コンサル×note販売×マッチングアプリアフィの複合マネタイズモデルの構築についての提案。"
    },
    {
        "index": 1710,
        "filename": "image_27.png",
        "description": "マッチングアプリ関連アカウント運用における複数のマネタイズ選択肢（note、コンサル、TikTok）についての選定基準の説明。年間100万円の利益目標達成に向けた戦略アドバイス。"
    },
    {
        "index": 1711,
        "filename": "image_28.png",
        "description": "恋愛テーマのアカウント運用における情報発信の最適化についての質問。外見×内面のバランスを取った情報発信アプローチや、男性フォロワーの獲得方法についての実践的ガイダンス。"
    },
    {
        "index": 1712,
        "filename": "image_29.png",
        "description": "Instagram攻略とTikTok動画制作の並行実施についてのアドバイス。月100万円の利益を目指す場合の投稿頻度と継続期間、リール・TikTok活用についての具体的な推奨値。"
    },
    {
        "index": 1713,
        "filename": "image_30.png",
        "description": "自動化ツール（Excel）を使用したInstagramアカウント分析と戦略構築についての相談。フォロワー数と投稿品質のバランス調整、ニッチ選定の重要性についての説明。"
    },
    {
        "index": 1714,
        "filename": "image_31.png",
        "description": "投稿時間の最適化と、年齢30万円レベルでの就職とInstagram運用の両立についての質問。フォロワー到達や売上目標の設定にあたり、継続期間の重要性についてのアドバイス。"
    },
    {
        "index": 1715,
        "filename": "image_32.png",
        "description": "プロフィール表記方法と自己開示レベルについての技術的な質問。フレーズの配置順序や右左への記載方法の工夫で、ユーザーの視線誘導を改善する方法についての細かいテクニック。"
    },
    {
        "index": 1716,
        "filename": "image_33.png",
        "description": "Instagram運用に関する複数の実践的質問まとめ。記事投稿のコンセプト構成やストーリーズ活用、フォロワーのリアルコメント獲得戦略についての相談内容。"
    },
    {
        "index": 1717,
        "filename": "image_34.png",
        "description": "アカウント分析と参入ジャンル選定に関する具体的なコンサルティング相談。資産運用とダイエット×恋愛という複合テーマのニッチ選定についての複数提案と検討過程。"
    },
    {
        "index": 1718,
        "filename": "image_35.png",
        "description": "投稿品質とフォロワー数の関係性についての認識と、転職時の仕事とInstagram運用の両立方法についての相談。Excel活用や個別分析の重要性についてのアドバイス。"
    },
    {
        "index": 1719,
        "filename": "image_36.png",
        "description": "Instagram初期フェーズとTikTok活用についてのアドバイス。初期段階ではフォロワー数重視、その後ジャンル拡張やTikTok導入による収益向上についての段階的戦略。"
    },
    {
        "index": 1720,
        "filename": "image_37.png",
        "description": "リール投稿の品質向上とフォロワー数加速についての相談。50投稿で5000フォロワー達成経験に基づいた、次段階での分析アプローチについてのガイダンス。"
    },
    {
        "index": 1721,
        "filename": "image_38.png",
        "description": "Instagram初期フェーズでのリール制作とフォロワー獲得方法についての質問。150フォロワー達成時の次のステップとしてのTikTok活用や競合分析についてのアドバイス。"
    },
    {
        "index": 1722,
        "filename": "image_39.png",
        "description": "ED薬情報系のアカウント運用とアフィリエイト販売についての複合的な質問。サプリメント販売との併用戦略や、フォロワー数に応じた売上目標設定についての説明。"
    },
    {
        "index": 1723,
        "filename": "image_40.png",
        "description": "ED薬アフィリエイト運用における悩み解決専門アカウント設計についての相談。Instagram上での信頼構築と、ジャンル参入時の差別化要素についての実践的アドバイス。"
    },
    {
        "index": 1724,
        "filename": "image_41.png",
        "description": "SNS運用におけるジャンル選定と複数アカウント展開の相談。短期間での売上達成に向けた投稿頻度設定と、1-3ヶ月ごとのピボット戦略についての提案。"
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

    print(f"\n✓ Batch 1705-1724 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
