#!/usr/bin/env python3
"""
Batch 1525-1544の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1525-1544の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1525,
        "filename": "image_78.png",
        "description": "Instagramダイレクトメッセージに関する質問と回答。フォロワーやストーリーズへのコメント、DMでの案内方法についてのQ&A。K君による詳細なコンサルティング回答。"
    },
    {
        "index": 1526,
        "filename": "image_79.png",
        "description": "Instagram運用とビジネス展開に関する相談内容。アカウント凍結リスク、フォロワー増加戦略、Brain販売との連携についての質問と回答。"
    },
    {
        "index": 1527,
        "filename": "image_80.png",
        "description": "Instagramビジネスアカウント設計に関する質問。プロフィール最適化、リール活用、ハッシュタグ戦略についてのK君による実践的なアドバイス。"
    },
    {
        "index": 1528,
        "filename": "image_81.png",
        "description": "Instagramストーリーズとリール動画の活用法に関する説明。投稿頻度、エンゲージメント向上、フォロワー獲得戦略についての詳細な解説。"
    },
    {
        "index": 1529,
        "filename": "image_82.png",
        "description": "Instagram集客とマネタイズに関する複合的な質問。DMでのリード獲得、無料プレゼント配布、有料商材販売との組み合わせについてのQ&A。"
    },
    {
        "index": 1530,
        "filename": "image_83.png",
        "description": "Instagramアカウント戦略に関する質問と回答。プロフィール設計、ビオの最適化、フォロワー属性の定義についてのK君の指導。"
    },
    {
        "index": 1531,
        "filename": "image_84.png",
        "description": "Instagram運用での躓きについての相談。投稿品質低下の改善、エンゲージメント向上、コンテンツ戦略の見直しについてのアドバイス。"
    },
    {
        "index": 1532,
        "filename": "image_85.png",
        "description": "Instagramコンテンツ企画に関する質問。ネタ帳の作成方法、投稿ペース設定、リール動画企画についてのK君による実践的な回答。"
    },
    {
        "index": 1533,
        "filename": "image_86.png",
        "description": "Instagramフォロワー増加戦略に関する質問。ハッシュタグの活用、プロフィールクリック率向上、エンゲージメント施策についての詳細な説明。"
    },
    {
        "index": 1534,
        "filename": "image_87.png",
        "description": "Instagramリール動画制作に関する相談。動画編集ツール選択、企画方法、アルゴリズム対策についてのK君のコンサルティング回答。"
    },
    {
        "index": 1535,
        "filename": "image_88.png",
        "description": "Instagramハッシュタグ戦略に関する質問と回答。ハッシュタグ選定方法、プロフィールへの導線設計、検索流入対策についての詳細。"
    },
    {
        "index": 1536,
        "filename": "image_89.png",
        "description": "Instagramマネタイズ方法に関する包括的な質問。広告収入、アフィリエイト、自社商材販売、各プラットフォーム連携についてのK君の解説。"
    },
    {
        "index": 1537,
        "filename": "image_90.png",
        "description": "Instagramアカウント作成初期段階での質問。プロフィール設定、ハッシュタグ戦略、初期投稿内容についてのK君による初心者向けアドバイス。"
    },
    {
        "index": 1538,
        "filename": "image_91.png",
        "description": "Instagramビジネス活用に関する複数の質問。DM自動化、ストーリーズへのリンク設置、販売ページへの導線についての実践的な回答。"
    },
    {
        "index": 1539,
        "filename": "image_92.png",
        "description": "Instagramコンテンツ品質向上に関する相談。投稿デザイン改善、キャプション工夫、視認性向上についてのK君による詳細なガイダンス。"
    },
    {
        "index": 1540,
        "filename": "image_93.png",
        "description": "Instagram運用での課題解決に関する質問。投稿頻度、リール活用、フォロワーエンゲージメント向上についての多角的なアドバイス。"
    },
    {
        "index": 1541,
        "filename": "image_94.png",
        "description": "Instagramプロフィール最適化に関する質問と回答。ハイライト設定、リンク設置、プロフィール説明文の工夫についての詳細な指導。"
    },
    {
        "index": 1542,
        "filename": "image_95.png",
        "description": "Instagramダイレクトメール運用に関する相談。DM配信方法、顧客対応、フォロワーフォローバック率向上についてのK君のアドバイス。"
    },
    {
        "index": 1543,
        "filename": "image_96.png",
        "description": "Instagram広告とオーガニック施策に関する質問。広告投資対効果、オーガニック成長戦略、複合的なマーケティング手法についての説明。"
    },
    {
        "index": 1544,
        "filename": "image_97.png",
        "description": "Instagramビジネスアカウント運営の総合的な相談。複数の課題解決、成長戦略、マネタイズ方法についてのK君による包括的なコンサルティング。"
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

    print(f"\n✓ Batch 1525-1544 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
