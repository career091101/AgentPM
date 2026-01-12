#!/usr/bin/env python3
"""
Batch 1485-1504の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1485-1504の画像説明（詳細な説明を生成）
batch_descriptions = [
    {
        "index": 1485,
        "filename": "image_38.png",
        "description": "ユーザーとKくんのDM対話。インスタグラムの初期投稿戦略とコンテンツ方針についての相談。アカウント設立時の投稿ペース設定やジャンル選定の重要性についてのアドバイス。"
    },
    {
        "index": 1486,
        "filename": "image_39.png",
        "description": "ユーザーからのInstagram投稿データに関する質問。リーチ数、フォロー増加数、いいね率などの数値データが含まれた投稿分析の画像。Kくんからの改善提案。"
    },
    {
        "index": 1487,
        "filename": "image_40.png",
        "description": "複数ユーザーからのSNS運用に関するDM。ビジネスジャンルのアカウント設計方針、プロフィール表記の工夫、フォロワー増加施策についての複合的なアドバイス。"
    },
    {
        "index": 1488,
        "filename": "image_41.png",
        "description": "Kくんによるコンテンツ販売戦略の説明。Note・Brain・Tipsの使い分けについての詳細なガイダンス。各プラットフォームの特性と収益化の優先順位についての解説。"
    },
    {
        "index": 1489,
        "filename": "image_42.png",
        "description": "ユーザーからのTwitterとInstagramの並行運用についての相談。発信軸の統一、コンテンツ分配戦略、フォロワー増加施策についてのKくんの詳細アドバイス。"
    },
    {
        "index": 1490,
        "filename": "image_43.png",
        "description": "ユーザーの収益報告と今後の戦略相談。月3万円の収益達成に向けた次のステップ、高単価商品の販売戦略、マネタイズ方法の多角化についての協議。"
    },
    {
        "index": 1491,
        "filename": "image_44.png",
        "description": "Instagramストーリーズとハイライト機能の活用に関するQ&A。視聴率向上、カテゴリ選定、フォロワー増加への影響についての詳細な説明。"
    },
    {
        "index": 1492,
        "filename": "image_45.png",
        "description": "ユーザーからのTikTok基本設定に関する多数の質問。アカウント作成時のポイント、初期投稿戦略、フォローとハッシュタグ戦略についてのKくんの実践的ガイダンス。"
    },
    {
        "index": 1493,
        "filename": "image_46.png",
        "description": "恋愛系ジャンルの情報販売についての相談。ターゲット設定、コンテンツテーマの選定、価格設定についてのアドバイス。初心者向けの販売開始戦略。"
    },
    {
        "index": 1494,
        "filename": "image_47.png",
        "description": "Kくんによる美容系アカウント運用の実例解説。フォロワー構成分析、ビジネスコンバージョン率向上、高単価商品への導線設計についての具体的なケーススタディ。"
    },
    {
        "index": 1495,
        "filename": "image_48.png",
        "description": "ユーザーからのLINE公式アカウント導入についての相談。エルステップ連携、ステップメール構築、顧客獲得単価最適化についてのKくんのアドバイス。"
    },
    {
        "index": 1496,
        "filename": "image_49.png",
        "description": "複数ジャンルの並行運用についての相談。稼ぐ系とジャンル特化、アカウント分離の判断基準、リソース配分についての詳細なアドバイス。"
    },
    {
        "index": 1497,
        "filename": "image_50.png",
        "description": "YouTubeとSNSの連携戦略に関するQ&A。長尺動画と短編動画の配分、チャンネル登録者増加施策、マネタイズタイミングについての説明。"
    },
    {
        "index": 1498,
        "filename": "image_51.png",
        "description": "ユーザーからのブログ記事作成に関する質問。SEO対策、キーワード選定、内部リンク構築、読者エンゲージメント向上についてのKくんの実践的ガイド。"
    },
    {
        "index": 1499,
        "filename": "image_52.png",
        "description": "アフィリエイト教材販売についての相談。商材選定、ターゲット層分析、セールスレター作成についてのKくんの具体的なアドバイス。"
    },
    {
        "index": 1500,
        "filename": "image_53.png",
        "description": "Instagramリール制作戦略に関するQ&A。編集ツール選定、トレンド活用、ハッシュタグ最適化、エンゲージメント向上についての詳細な解説。"
    },
    {
        "index": 1501,
        "filename": "image_54.png",
        "description": "ユーザーからのDM分析と返信戦略についての相談。フォロワーとの関係構築、コンサルティング営業への導線、信頼構築メッセージについてのアドバイス。"
    },
    {
        "index": 1502,
        "filename": "image_55.png",
        "description": "Canvaを使ったサムネイル・画像作成テンプレートの紹介。無料版活用方法、デザイン効率化、視覚的インパクト向上についてのKくんのおすすめ設定。"
    },
    {
        "index": 1503,
        "filename": "image_56.png",
        "description": "ユーザーからの複合的なSNS戦略相談。Instagram・Twitter・TikTok・YouTubeの最適配分、時間管理、コンテンツの使い回し方についての詳細な計画立案。"
    },
    {
        "index": 1504,
        "filename": "image_57.png",
        "description": "Kくんによる月収50万円達成ロードマップの説明。段階的な施策実装、マネタイズの優先順位、稼ぐ系情報販売の具体的な実行計画についての総括的なガイダンス。"
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

    print(f"\n✓ Batch 1485-1504 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
