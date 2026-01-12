#!/usr/bin/env python3
"""
Batch 1905-1924の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1905-1924の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1905,
        "filename": "image_71.png",
        "description": "2023年10月の質疑応答まとめ記事の第1弾スクリーンショット。ユーザー「さささき」がお菓子とジュースの選定に関する相談をしており、複数カテゴリの商品選定についての具体的なアドバイス内容が掲載されている。"
    },
    {
        "index": 1906,
        "filename": "image_72.png",
        "description": "アカウント複数運用についての相談スクリーンショット。小売販売から講師業まで複数ジャンルの事業を展開する際のマネタイズ戦略と、YouTube導入、ビジネスアカウント立ち上げについての段階的なアドバイス。"
    },
    {
        "index": 1907,
        "filename": "image_73.png",
        "description": "ビジネス系ジャンルでのInstagram運用に関する短い質問と回答。リール動画での商品紹介の有効性と、他プラットフォームでの展開についての実務的な意見交換。"
    },
    {
        "index": 1908,
        "filename": "image_74.png",
        "description": "LINE公式アカウントの登録者数が1000人以上に達したユーザーからの相談。ステップメール配信時の有料課金化と、自動化ツール(uatage)の活用についての具体的な説明。"
    },
    {
        "index": 1909,
        "filename": "image_75.png",
        "description": "動画サポートサービスと料金設定に関する複数の質疑応答。フロント商品とサポート体制の価格関係性や、グループコンサルの人数制限についての経営判断と実装手法。"
    },
    {
        "index": 1910,
        "filename": "image_76.png",
        "description": "コンサル価格帯や支援体制についての深掘り相談。3人グループコンサルと1対1コンサルの効果の違いや、支援体制を整備する際の意思決定プロセスについての専門的なアドバイス。"
    },
    {
        "index": 1911,
        "filename": "image_77.png",
        "description": "DM返信対応と差別化戦略についての相談。複数ジャンル運用時の価格設定や、既存コンサル生との価値提供の差別化についての実践的なアドバイス。"
    },
    {
        "index": 1912,
        "filename": "image_78.png",
        "description": "ダイエットカテゴリでのInstagram運用とnoteの収益化についての相談。ダイエットコンサルの有効性と、Twitterでの販売チャネル最適化についての戦略的な回答。"
    },
    {
        "index": 1913,
        "filename": "image_79.png",
        "description": "コンサル商品の構成と価格戦略についての複雑な質疑応答。フォロワー数に基づいた価格設定、Tips販売段階の選定、値上げ前段階の売上についての数字を交えた具体的な説明。"
    },
    {
        "index": 1914,
        "filename": "image_80.png",
        "description": "スクール事業の立ち上げについての段階的なアドバイス。教育型コンテンツの有益性を活かしたスクール設計と、フォロワーの層別による段階的な販売戦略の構築についての相談。"
    },
    {
        "index": 1915,
        "filename": "image_81.png",
        "description": "販売ページ設計と決済方法選定についての質問・回答コンビネーション。Appsやbaseの決済サービスの特性を活かした決済リンク設計と、複数商品の一括販売方法についての技術的ガイド。"
    },
    {
        "index": 1916,
        "filename": "image_82.png",
        "description": "特商法表示と決済会社の名義開示についての相談。LP名義とのズレを調整する際の心理的な懸念と、実務的な解決方法としてのappsツール活用についての専門的な説明。"
    },
    {
        "index": 1917,
        "filename": "image_83.png",
        "description": "Notes販売とTipsの販売戦略についての相談。ビジネス系コンテンツの構成案と、Tipsアフィの拡散方法についての実践的なアドバイスと戦術的な提案。"
    },
    {
        "index": 1918,
        "filename": "image_84.png",
        "description": "ビジネス系コンテンツの価格設定と販売ロードマップについての詳細な相談。初期段階から成熟段階までの販売価格推移と、1年スパンでの目標設定についての段階的なプランニング。"
    },
    {
        "index": 1919,
        "filename": "image_85.png",
        "description": "Twitterのジャンル選定とノウハウの差別化についての相談。長期的なビジネスジャンルの選択とフォロワーの行動量測定による施策改善についての戦略的な思考プロセス。"
    },
    {
        "index": 1920,
        "filename": "image_86.png",
        "description": "ブログ収益化とコンサル事業の組み合わせについての相談。無料プレゼント配布からのステップメール経由での販売フロー設計と、ロイヤルティ構築についての実装方法。"
    },
    {
        "index": 1921,
        "filename": "image_87.png",
        "description": "ツールの自動化と継続ジャンル選定についての相談。外注化による効率化と、継続型ビジネスの構築における課題抽出と戦略的な改善についてのコンサルティング内容。"
    },
    {
        "index": 1922,
        "filename": "image_88.png",
        "description": "SNS初期運用のターゲット選定と基本戦略についての専門的なアドバイス。ターゲット層の明確化、行動パターンの分析、ノウハウの発信方法についての構築的なガイダンス。"
    },
    {
        "index": 1923,
        "filename": "image_89.png",
        "description": "低単価ツール系ジャンルのコンサル料金設定についての深掘り相談。自動化ツールの導入と損益分岐点の計算方法、外注費を踏まえた利益率向上についての経営的な視点。"
    },
    {
        "index": 1924,
        "filename": "image_90.png",
        "description": "ツール系サービスの料金体系と段階的な値上げについての相談。複数段階の価格帯設定と各段階でのお申し込み特典の工夫、継続利用を促進するための施策についての提案。"
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

    print(f"\n✓ Batch 1905-1924 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
