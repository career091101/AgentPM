#!/usr/bin/env python3
"""
Batch 1605-1624の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1605-1624の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1605,
        "filename": "image_483.png",
        "description": "インスタグラム女性アカウント向けのマネタイズ相談。ビジネス系からの転換、1000人フォロワー達成、スタイル・美容ジャンルでのポジション取得についての質問。"
    },
    {
        "index": 1606,
        "filename": "image_484.png",
        "description": "K君によるビジネス系からの転換戦略アドバイス。スタイル・美容ジャンルの選択、複合マネタイズ、月50-70万円の売上目標達成法についての詳細指導。"
    },
    {
        "index": 1607,
        "filename": "image_485.png",
        "description": "夜職女性によるマネタイズ初期段階の相談。TikTok500フォロワー、Twitter150フォロワー、教材販売開始検討についての複数の質問。"
    },
    {
        "index": 1608,
        "filename": "image_486.png",
        "description": "K君による夜職ジャンルマネタイズ戦略。TikTok・Twitter併用ポジション、複合マネタイズ、月100-150万円の売上構築法についての戦略的指導。"
    },
    {
        "index": 1609,
        "filename": "image_487.png",
        "description": "不動産営業女性によるビジネス垢マネタイズ相談。1500フォロワー達成、不動産・ビジネス系ジャンル、教材販売・コンサル開始についての質問。"
    },
    {
        "index": 1610,
        "filename": "image_488.png",
        "description": "K君による不動産ビジネス垢マネタイズ戦略。実績作り、複合マネタイズ、月150-200万円の売上達成法、Twitter併用戦略についての詳細アドバイス。"
    },
    {
        "index": 1611,
        "filename": "image_489.png",
        "description": "美容師によるSNS運用初期段階の相談。ビジネス系・美容系発信、フォロワー増加、パーソナルブランド構築についての基本的質問。"
    },
    {
        "index": 1612,
        "filename": "image_490.png",
        "description": "K君による美容師向け複合ジャンル戦略。ビジネス系・美容系併用、ポジション取得、月100万円以上の売上構築、キャリアシフトについての指導。"
    },
    {
        "index": 1613,
        "filename": "image_491.png",
        "description": "経営者男性によるコンテンツ販売相談。既存ビジネス、新規教材開発、販売戦略、顧客層分析についての複数の課題提示。"
    },
    {
        "index": 1614,
        "filename": "image_492.png",
        "description": "K君による経営者向け教材販売戦略。既存ビジネス顧客の活用、新規顧客開拓、販売チャネル最適化、月300万円以上の売上化についての戦略。"
    },
    {
        "index": 1615,
        "filename": "image_493.png",
        "description": "転職相談者によるビジネス系SNS発信相談。キャリアチェンジ、ポジション取得、フォロワー獲得、マネタイズ開始についての初期段階の質問。"
    },
    {
        "index": 1616,
        "filename": "image_494.png",
        "description": "K君による転職者向けキャリア発信戦略。実績の見える化、ポジション取得、複合マネタイズ、月100-150万円の売上構築についての詳細指導。"
    },
    {
        "index": 1617,
        "filename": "image_495.png",
        "description": "フリーランス女性によるInstagram運用相談。バナー制作サービス、フォロワー1200人達成、パッケージ販売、価格設定についての複数の質問。"
    },
    {
        "index": 1618,
        "filename": "image_496.png",
        "description": "K君によるフリーランス向けサービス販売戦略。バナー制作の高単価化、複合商品化、月150-200万円の売上構築、クライアント教育についての指導。"
    },
    {
        "index": 1619,
        "filename": "image_497.png",
        "description": "ゼネコン営業によるビジネス系発信相談。業界経験を活かした発信、フォロワー増加、マネタイズ検討、コンサル化についての質問。"
    },
    {
        "index": 1620,
        "filename": "image_498.png",
        "description": "K君によるゼネコン営業向けビジネス発信戦略。業界ノウハウのコンテンツ化、複合マネタイズ、月200万円以上の売上化、継続的な実績作りについての戦略。"
    },
    {
        "index": 1621,
        "filename": "image_499.png",
        "description": "実業家男性によるSNS活用・マネタイズ相談。既存ビジネス拡大、複数プラットフォーム運用、高単価商品開発についての複合的な質問。"
    },
    {
        "index": 1622,
        "filename": "image_500.png",
        "description": "K君による実業家向け複合マネタイズ戦略。既存ビジネスとSNSの融合、複数チャネル活用、月500万円以上の売上構築、スケーリング戦略についての総合指導。"
    },
    {
        "index": 1623,
        "filename": "image_501.png",
        "description": "コンサルタント女性による高度なマネタイズ相談。既存クライアント、オンラインコース開発、複合販売モデル、スケーリング戦略についての戦略的質問。"
    },
    {
        "index": 1624,
        "filename": "image_502.png",
        "description": "K君によるコンサルタント向け最高度なマネタイズ戦略。オンラインコース高単価化、複数商品による売上最大化、VIPクライアント層開拓、月1000万円規模の売上構築についての総合的アドバイス。"
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

    print(f"\n✓ Batch 1605-1624 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
