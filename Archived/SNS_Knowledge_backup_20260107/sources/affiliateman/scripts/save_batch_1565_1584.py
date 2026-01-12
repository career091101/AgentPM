#!/usr/bin/env python3
"""
Batch 1565-1584の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1565-1584の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1565,
        "filename": "image_15.png",
        "description": "インスタグラムDMスレッド。複数のユーザーからの質問に対するコンサルティング返答。フォロワー増加戦略とアカウント設計についての詳細なアドバイス内容が含まれている。"
    },
    {
        "index": 1566,
        "filename": "image_16.png",
        "description": "インスタグラム運用に関するコンサルティング内容。特定のジャンル選定における戦略的なアカウント構築方法と投稿戦略についての説明が記載されている。"
    },
    {
        "index": 1567,
        "filename": "image_17.png",
        "description": "SNS運用における複数プラットフォーム戦略の説明。Instagram、TikTok、Twitter等の各プラットフォームでの役割分担と相乗効果を最大化する方法についてのガイダンス。"
    },
    {
        "index": 1568,
        "filename": "image_18.png",
        "description": "インスタグラム投稿の分析データと改善提案。エンゲージメント率やリーチ数等のメトリクスに基づいた具体的な施策改善案が記載されている。"
    },
    {
        "index": 1569,
        "filename": "image_19.png",
        "description": "アカウント成長段階別の戦略ロードマップ。初期段階から1万フォロワー達成までの段階ごとの具体的な実行策とマイルストーン設定について説明している。"
    },
    {
        "index": 1570,
        "filename": "image_20.png",
        "description": "インスタグラムコンテンツ戦略の解説。特定のジャンルにおいて高エンゲージメントを実現するコンテンツテーマ選定と投稿パターンの実装方法を記載。"
    },
    {
        "index": 1571,
        "filename": "image_21.png",
        "description": "SNS発信における心理学的アプローチ。ターゲットユーザーの購買心理やモチベーション要因に基づいたコンテンツ構成と価値提供方法についての詳細なガイダンス。"
    },
    {
        "index": 1572,
        "filename": "image_22.png",
        "description": "ストーリーズ機能の活用戦略。投稿頻度、投稿時間帯、クリエイティブ要素等による閲覧率向上施策と継続的な視聴者関係構築の方法について説明。"
    },
    {
        "index": 1573,
        "filename": "image_23.png",
        "description": "インスタグラムアルゴリズムに基づいたコンテンツ最適化。保存率やシェア率を高めるための投稿フォーマット選定と投稿前の準備プロセスについての実装ガイド。"
    },
    {
        "index": 1574,
        "filename": "image_24.png",
        "description": "マネタイズ戦略の段階的構築方法。アフィリエイト、自社商品販売、メンバーシップ等の複数の収益モデル導入順序と各段階での注意点について詳述。"
    },
    {
        "index": 1575,
        "filename": "image_25.png",
        "description": "ユーザーの質疑応答コンテンツ。アカウント運用における具体的な悩みと実践的な解決策の提示。DMコンサルティングの一部として記録されたやり取り内容。"
    },
    {
        "index": 1576,
        "filename": "image_26.png",
        "description": "プロフィール最適化とプロフィール外リンク戦略。クリック率を高めるプロフィール文言設計とリンク先ランディングページの構築方法についての詳細な説明。"
    },
    {
        "index": 1577,
        "filename": "image_27.png",
        "description": "複数アカウント運用時の時間効率化戦略。コンテンツ制作の外注化、自動化ツール活用、スケジュール管理等による生産性向上方法の実装ガイド。"
    },
    {
        "index": 1578,
        "filename": "image_28.png",
        "description": "インスタグラムの最新トレンド機能活用ガイド。リール、ガイド、コラボレーション投稿等の新機能の効果的な活用方法とアルゴリズム評価への影響について説明。"
    },
    {
        "index": 1579,
        "filename": "image_29.png",
        "description": "コミュニティ構築と顧客関係管理。DM対応、コメント返信、フォロワーとの信頼関係構築における具体的な実践方法とロイヤリティ向上施策について記載。"
    },
    {
        "index": 1580,
        "filename": "image_30.png",
        "description": "SNSマーケティング投資対効果分析。広告費対売上、フォロワー1名あたりの獲得コスト等の主要KPI定義と定期的な測定・改善プロセスについてのフレームワーク。"
    },
    {
        "index": 1581,
        "filename": "image_31.png",
        "description": "特定業界・ジャンル別の成功事例集。恋愛、ビジネス、ダイエット等の異業種の成功アカウント分析と、業種別の独自アプローチ開発の重要性について解説。"
    },
    {
        "index": 1582,
        "filename": "image_32.png",
        "description": "クリエイターとしてのブランド構築。個人の専門性確立、権威性の醸成、ファン化戦略における長期的なコンテンツ開発ロードマップについての詳細ガイダンス。"
    },
    {
        "index": 1583,
        "filename": "image_33.png",
        "description": "データドリブン意思決定の実装。インスタグラムのインサイト機能活用、分析ダッシュボード構築、A/Bテスト実施による継続的な改善サイクルについて説明。"
    },
    {
        "index": 1584,
        "filename": "image_34.png",
        "description": "SNS運用における共通失敗パターンと対策。非一貫性、過度な販売色、エンゲージメント無視等の典型的な落とし穴と予防・解決策についての実践的なアドバイス集。"
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

    print(f"\n✓ Batch 1565-1584 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
