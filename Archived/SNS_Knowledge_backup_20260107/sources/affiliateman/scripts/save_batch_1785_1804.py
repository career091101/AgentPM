#!/usr/bin/env python3
"""
Batch 1785-1804の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1785-1804の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1785,
        "filename": "image_102.png",
        "description": "Instagram運用とTwitterの使い分けについてのDM相談。アカウント発信のジャンル選定やSNS活用戦略についての具体的なアドバイス。"
    },
    {
        "index": 1786,
        "filename": "image_103.png",
        "description": "Twitterのデザインレベルと図解作成についての質問。インスタグラムとTwitterのビジュアルレベルの差別化についての実践的な回答。"
    },
    {
        "index": 1787,
        "filename": "image_104.png",
        "description": "SNS発信のジャンル選定と複数ジャンル運用についての相談。4つの具体的なジャンル選択肢（副業・SNS・資産運用・お金情報）が提案されている。"
    },
    {
        "index": 1788,
        "filename": "image_105.png",
        "description": "Instagram運用のターゲット設定と撮影戦略についての質問。ターゲット層の明確化と適切なコンテンツ作成についてのコンサルティング内容。"
    },
    {
        "index": 1789,
        "filename": "image_106.png",
        "description": "写真素材とカメラスキルの習得についての相談。Zoomコンサル参加者からの質問で、写真撮影技術とコンテンツ制作スキルの向上方法が説明されている。"
    },
    {
        "index": 1790,
        "filename": "image_107.png",
        "description": "Instagramのフォロワー増加と継続運用についての相談。リンク公開やZoom参加への誘導、アカウント構築プロセスについての回答スクリーンショット。"
    },
    {
        "index": 1791,
        "filename": "image_108.png",
        "description": "アカウント構築と有料note販売についての質問。無料noteのフォロワー企画と有料販売への導線設計についての具体的なアドバイス。"
    },
    {
        "index": 1792,
        "filename": "image_109.png",
        "description": "フォロワー規模と企画内容についての相談。公式LINE誘導とリスト拡散について、1000人規模でのマーケティング施策が説明されている。"
    },
    {
        "index": 1793,
        "filename": "image_110.png",
        "description": "公式ラインのマーケティング活用とリンク配信についての質問。フォロワー企画の仕組みと公式LINE登録後のセグメント配信戦略が記載されている。"
    },
    {
        "index": 1794,
        "filename": "image_111.png",
        "description": "Twitterの運用方針とプロフィール設定についての複数の質問。アイコン変更、予約投稿機能、プロフィール最適化についての実務的なアドバイス。"
    },
    {
        "index": 1795,
        "filename": "image_112.png",
        "description": "プロフィール文字数制限と予約投稿機能についての質問。RTやリツイート活用、プレゼント企画の効果的な運用についてのアドバイス記載。"
    },
    {
        "index": 1796,
        "filename": "image_113.png",
        "description": "SNS初心者向けのコンサル相談内容。アカウント向性の診断と参加型コンテンツ制作についてのガイダンスが説明されている。"
    },
    {
        "index": 1797,
        "filename": "image_114.png",
        "description": "恋愛コンサルとマッチングアプリ運用についての相談。フォロワー増加とファン化の違いについて、具体的な事例が複数紹介されている。"
    },
    {
        "index": 1798,
        "filename": "image_115.png",
        "description": "TikTok運用と恋愛系マネタイズについての質問。イラスト系と写真系の動画制作アプローチの違いについての具体的な説明。"
    },
    {
        "index": 1799,
        "filename": "image_116.png",
        "description": "TikTokでのマネタイズ戦略とコンテンツ制作についての相談。占い系動画とSNS集客について、複数の実例やリンク提示がされている。"
    },
    {
        "index": 1800,
        "filename": "image_117.png",
        "description": "占い系SNSコンテンツの制作方法についての質問。恋愛占いのジャンル選定と、TikTok・Instagram・Twitterでの発信方法についての提案。"
    },
    {
        "index": 1801,
        "filename": "image_118.png",
        "description": "TikTokマネタイズチャレンジと業種選択についての相談。サロンビジネスとInstagram運用の組み合わせについてのアドバイスが記載されている。"
    },
    {
        "index": 1802,
        "filename": "image_119.png",
        "description": "恋愛占いコンサルと売上向上についての複数の質問。cupcut編集ツールの活用と、無料版の利用可能性についてのアドバイス。"
    },
    {
        "index": 1803,
        "filename": "image_120.png",
        "description": "Kei31さんの相談内容で、TikTok運用と恋愛系マネタイズについての複数の質問への回答スクリーンショット。"
    },
    {
        "index": 1804,
        "filename": "image_121.png",
        "description": "女性向け恋愛系SNS運用の質疑応答。月100万インスタ・TikTok・YouTubeなど複数SNS活用時の効果的な使い分けについての詳細な回答。"
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

    print(f"\n✓ Batch 1785-1804 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
