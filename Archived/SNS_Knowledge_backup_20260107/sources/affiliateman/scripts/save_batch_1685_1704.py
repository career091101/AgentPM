#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1685, "filename": "image_02.png", "description": "サロンメンバーのKKくんとaiがコンテンツ販売とジャンル選択について対話するスクリーンショット。高額コンテンツ販売の仕組みとビジネス系向けの活用方法が説明されている。"},
    {"index": 1686, "filename": "image_03.png", "description": "fukuユーザーがストーリーやハイライト機能の使い方について相談する質問スレッド。恋愛系アカウントでの活用方法が詳しく解説されている。"},
    {"index": 1687, "filename": "image_04.png", "description": "fukuユーザーが間隔短めなストーリーリール活用と他ジャンルとの掛け合わせについて質問するスクリーンショット。複数のジャンル組み合わせ戦略が提案されている。"},
    {"index": 1688, "filename": "image_05.png", "description": "KKくんが振抜け男子系アカウントの時間確保と収益化について回答するスレッド。マネタイズのハードルと個人特性の見極めについてアドバイスされている。"},
    {"index": 1689, "filename": "image_06.png", "description": "ビジネス系とマネタイズについての複雑な議論を展開するスクリーンショット。100日企画と振抜け男子系の組み合わせ方が詳しく説明されている。"},
    {"index": 1690, "filename": "image_07.png", "description": "takaユーザーがInstagramの恋愛アフィリエイトアカウント運営について質問するスレッド。公式LINE連携やセクター出会い方法など実践的な施策が提案されている。"},
    {"index": 1691, "filename": "image_08.png", "description": "takaユーザーが恋愛系転身時のリール動画とNote販売の連携について相談する質問。TikTokでのバイラル活動と連動した戦略が提案されている。"},
    {"index": 1692, "filename": "image_09.png", "description": "takaユーザーがフォロワーをファン化するリール投稿方法について質問するスレッド。TikTokと連動した投稿戦略や毎日リール活用のポイントが説明されている。"},
    {"index": 1693, "filename": "image_10.png", "description": "KKくんがエロテック系noteプラットフォーム選択について回答するスクリーンショット。ターゲット層の分析と販売戦略に関するアドバイスが記載されている。"},
    {"index": 1694, "filename": "image_11.png", "description": "大橋薫ユーザーがInstagram・TikTokでのアフィリエイト準備について質問するスレッド。結婚相談所ジャンルのターゲット設定と年代別アプローチが提案されている。"},
    {"index": 1695, "filename": "image_12.png", "description": "複数ユーザーが婚活・結婚コンサルのアフィリエイト販売について相談するスクリーンショット。ターゲット層の特性と販売方法の工夫について議論されている。"},
    {"index": 1696, "filename": "image_13.png", "description": "KKくんが個別相談と婚活戦略セミナーの販売フローについて説明するスレッド。150万フォロワーのコンサルビジネス構築における段階的なアプローチが記載されている。"},
    {"index": 1697, "filename": "image_14.png", "description": "ひとみユーザーが在宅ワークジャンルのInstagram運用について詳しく質問するスクリーンショット。ブログ・SNS連携やブログハウス系のマネタイズ方法が提案されている。"},
    {"index": 1698, "filename": "image_15.png", "description": "KKくんがフォロワー増やし方やコンテンツ追加戦略について回答するスレッド。投稿内容の多様性とバランス、見出し方の工夫が説明されている。"},
    {"index": 1699, "filename": "image_16.png", "description": "ドラフラユーザーが東京23区限定の美容系アカウント戦略について質問するスクリーンショット。地域限定ターゲティングと月30-100万円の目標設定について相談されている。"},
    {"index": 1700, "filename": "image_17.png", "description": "しゅんユーザーがプロフィール改善とフィード投稿のInsta運用について相談するスレッド。リール活用とコンテンツ内容のバランス調整に関するアドバイスが記載されている。"},
    {"index": 1701, "filename": "image_18.png", "description": "KKくんがフォロワー増加とリール投稿添削について詳しく説明するスクリーンショット。コンテンツ難度の調整と投稿パターンの工夫について実例を交えて解説されている。"},
    {"index": 1702, "filename": "image_19.png", "description": "まひろユーザーがビジネス系アカウントのTikTok・Instagram併用戦略について質問するスレッド。ジャンル別マネタイズ傾向とAI活用の可能性について提案されている。"},
    {"index": 1703, "filename": "image_20.png", "description": "KKくんがビジネス系アカウント運営の基本戦略とChatGPT活用について説明するスクリーンショット。SNS×ブログ攻略と実績構築に必要な情報提供のポイントが記載されている。"},
    {"index": 1704, "filename": "image_21.png", "description": "まひろユーザーとKKくんがInstagram戦略とchatGPT・AIアカウント活用の使い分けについて議論するスレッド。実績構築の重要性と段階的なマネタイズアプローチが説明されている。"},
]

def is_auto_generated(desc):
    patterns = [
        "インスタグラム運用に関する",
        "説明画像または投稿サムネイル",
        "運用に関する説明画像",
        "投稿用のサムネイル",
    ]
    return any(p in desc for p in patterns)

def update_inventory_with_descriptions(batch_descriptions):
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'

    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {desc['filename']}: 説明更新")

    completed = sum(1 for item in inventory if not is_auto_generated(item.get('description', '')))
    total = len(inventory)
    remaining = total - completed
    percentage = (completed / total) * 100

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Batch 1685-1704 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
