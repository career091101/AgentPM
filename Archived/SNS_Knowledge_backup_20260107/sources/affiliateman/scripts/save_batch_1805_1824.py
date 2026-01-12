#!/usr/bin/env python3
"""
Batch 1805-1824の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1805-1824の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1805,
        "filename": "image_122.png",
        "description": "フォロワーの「あちゃくん」による公式LINE導入についての相談と、KKんからのアフィリエイト商品紹介の具体的な実装方法についての回答スクリーンショット。"
    },
    {
        "index": 1806,
        "filename": "image_123.png",
        "description": "「とっしー」というユーザーの転職・ビジネス英語学習のジャンル相談。Twitter中心の発信から英語学習コンテンツ作成についての質問と対策が記載されている。"
    },
    {
        "index": 1807,
        "filename": "image_124.png",
        "description": "KKんによる実践的なコンテンツ作成アドバイス。ノウハウ系動画、バズ攻略、具体的な数字（月100万円売上）を交えた詳細なマネタイズ戦略について。"
    },
    {
        "index": 1808,
        "filename": "image_125.png",
        "description": "KKんからの3つの質問項目への詳細な回答。実践的な内容の抽象度、コンテンツ分析ツール、TikTok運用ツールについての具体的なアドバイス。"
    },
    {
        "index": 1809,
        "filename": "image_126.png",
        "description": "リリというユーザーからのオプチャ扱い希望についての相談。公式LINE導入、バックエンド商品、個人ブランド構築の3つのテーマについての質問内容。"
    },
    {
        "index": 1810,
        "filename": "image_127.png",
        "description": "KKんによる恋愛系ジャンルでの1対Nスケール戦略についての回答。個人扱いとオプチャ扱いの違い、1:1から1:Nへの段階的スケーリング方法について。"
    },
    {
        "index": 1811,
        "filename": "image_128.png",
        "description": "リリの追加質問への回答。1ヶ月で結果を出すための期間設定、3ヶ月契約の価値、松竹梅プラン構築についてのKKんからの実践的アドバイス。"
    },
    {
        "index": 1812,
        "filename": "image_129.png",
        "description": "KKんによるコンサル期間や動画コンテンツの提供方法についての詳細説明。A・B・Cの3つのサポートプランパターンと、その選択基準について。"
    },
    {
        "index": 1813,
        "filename": "image_130.png",
        "description": "「まひろ」ユーザーからのコンテンツ販売と相談業務についての複合的な質問。決済サービス選定やコンサルの具体的な価格設定についての相談。"
    },
    {
        "index": 1814,
        "filename": "image_131.png",
        "description": "「ゆきの」ユーザーの副業初期段階での相談。実績ツイートの方針、Tipsのリツイート戦略、アフィリエイト報酬についてのKKんからの指導内容。"
    },
    {
        "index": 1815,
        "filename": "image_132.png",
        "description": "ゆきのの追加相談。CANVASの活用、推し機能の活用、アフィリエイト収入可能性についてのKKんからの回答とDM連携の実施について。"
    },
    {
        "index": 1816,
        "filename": "image_133.png",
        "description": "「てくん」というYouTubeアカウント運営者（97万人登録）から、マネタイズ戦略についての相談。別アカウント作成かメインアカウント活用かの戦略選択についての質問。"
    },
    {
        "index": 1817,
        "filename": "image_134.png",
        "description": "てくんの続きのやり取り。YouTubeの攻略系noteやコンサル、チャンネル伸び悩みの対策についての具体的なアドバイス。"
    },
    {
        "index": 1818,
        "filename": "image_135.png",
        "description": "「くっち」ユーザーからのYouTubeとTikTok選定相談。自己資金発信、Noteコンサルの販売、マネタイズ戦略についての包括的な質問。"
    },
    {
        "index": 1819,
        "filename": "image_136.png",
        "description": "くっちの続きのやり取り。Note販売、TikTok活用、新ジャンル参入時のマネタイズ商品作成の流れについてのKKんからのアドバイス。"
    },
    {
        "index": 1820,
        "filename": "image_137.png",
        "description": "「シトラス」ユーザーからの転職ノウハウビジネス相談。転職関連コンテンツ販売、有料Note・Tipsについて、プログへの誘導方法についての具体的な質問。"
    },
    {
        "index": 1821,
        "filename": "image_138.png",
        "description": "シトラスへのKKんからの詳細回答。noteやコンサルの活用、有料コンサル化についてのステップ、金額設定についての実践的なガイダンス。"
    },
    {
        "index": 1822,
        "filename": "image_139.png",
        "description": "「めい」ユーザーからの家づくり・家計管理ブログのマネタイズ相談。ターゲット設定、ブログからSNS展開、オシャレ系の写真撮影についての相談。"
    },
    {
        "index": 1823,
        "filename": "image_140.png",
        "description": "めいへのKKんからの回答。マネタイズ難易度、コンサル化戦略、転職エージェント・美容系アフィリについての具体的な提案。"
    },
    {
        "index": 1824,
        "filename": "image_141.png",
        "description": "「みおまる」ユーザーからの占いスピリチュアル販売と高単価商品について。LINE登録、オンラインセミナー、スクール運営についての複合的なビジネス構築相談。"
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

    print(f"\n✓ Batch 1805-1824 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
