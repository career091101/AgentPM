#!/usr/bin/env python3
"""
Batch 1165-1184の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1165-1184の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1165,
        "filename": "image_131.png",
        "description": "インスタグラムのDMスクリーンショット。ユーザー「ケくん」が、マネタイズのフォロワー獲得戦略とVOD系アフィリエイトについての質問を送信。複数の質問内容が記載されている。"
    },
    {
        "index": 1166,
        "filename": "image_132.png",
        "description": "インスタグラムのDMスクリーンショット。ユーザー「mayu」が、フォロワー数300〜1400の案件、アフィリエイトの実践例、コンサル稼働について相談中。回答者は詳細なアドバイスを提供している。"
    },
    {
        "index": 1167,
        "filename": "image_133.png",
        "description": "インスタグラムのDMスクリーンショット。ユーザー「トヨ」がnote販売とマネタイズについて質問。現在月売上5～7万円で資料購入に直面、フォロワー1000人達成の目標を設定している状況。"
    },
    {
        "index": 1168,
        "filename": "image_134.png",
        "description": "インスタグラムのDMスクリーンショット。トヨが同じ質問内容を繰り返送信。マネタイズ開始に向けて月30万円以上の目標達成を目指している状況が記載。"
    },
    {
        "index": 1169,
        "filename": "image_135.png",
        "description": "インスタグラムのDMスクリーンショット。トヨとケくんの質問に対する回答。noteのPV数増加戦略、CVR改善、アフィリエイト商品選定のポイントについて、具体的なアドバイスが提供されている。"
    },
    {
        "index": 1170,
        "filename": "image_136.png",
        "description": "インスタグラムのDMスクリーンショット。マネタイズ相談に関する詳細な回答。PV数と売上の比例関係、noteページの入眼数とCV数の最適化、英語系ジャンルの特性について説明されている。"
    },
    {
        "index": 1171,
        "filename": "image_137.png",
        "description": "インスタグラムのDMスクリーンショット。ケくんの質問への回答。note有料化の判断基準、PV数とCV数の関連性、ツイッターとnoteの読導ルートの差別化について詳しく説明。"
    },
    {
        "index": 1172,
        "filename": "image_138.png",
        "description": "インスタグラムのDMスクリーンショット。ユーザー「よっし」がマネタイズに関する相談。元々サチプラ系アカウント、ウリッコ特化への転換、外見コンプレックスについて言及。"
    },
    {
        "index": 1173,
        "filename": "image_139.png",
        "description": "インスタグラムのDMスクリーンショット。よっしへの詳細なアドバイス。フォロワー獲得のための施策6項目（インパクト、商品選定、フォロワー意見集め、ストーリーUP等）を提示。"
    },
    {
        "index": 1174,
        "filename": "image_140.png",
        "description": "インスタグラムのDMスクリーンショット。よっしの継続相談。ビフォーアフター効果、反論提示、売上最大化についてのアドバイスが記載。エマーキットと美容アカウント展開についても言及。"
    },
    {
        "index": 1175,
        "filename": "image_141.png",
        "description": "インスタグラムのDMスクリーンショット。よっしへの追加回答とファンデーション関連のアドバイス。美容液選定、タイアップ機会活用、ハイライト着圧について具体的な提案がある。"
    },
    {
        "index": 1176,
        "filename": "image_142.png",
        "description": "インスタグラムのDMスクリーンショット。ユーザー「ケくん」がエマーキット使用と効果検証、フォロワー1万人達成への戦略について質問。美容分野のマネタイズ関連のコンサル参加希望も述べられている。"
    },
    {
        "index": 1177,
        "filename": "image_143.png",
        "description": "インスタグラムのDMスクリーンショット。ケくんへの詳細な回答。効果検証の方法（ハイライト載せ、フィード対策等）、アカウント1万人達成後のマネタイズ方針、SNS×ブログの相乗効果について言及。"
    },
    {
        "index": 1178,
        "filename": "image_144.png",
        "description": "インスタグラムのDMスクリーンショット。ユーザー「M」がSEOブログとSNS、クライアント業務、WEBデザインに関する複合的なマネタイズ相談を送信。様々なジャンル展開についての質問が記載。"
    },
    {
        "index": 1179,
        "filename": "image_145.png",
        "description": "インスタグラムのDMスクリーンショット。Mへの詳細な返答。ブログURL貼付、SNS×ブログマネタイズ戦略、メインとサーバーアフィリエイト、有料テンプレートの活用についてアドバイス。"
    },
    {
        "index": 1180,
        "filename": "image_146.png",
        "description": "インスタグラムのDMスクリーンショット。Instagram/Twitter/TikTokの投稿作成ツールをテーマにしたバナー画像。CapCutとCanvaが紹介されており、投稿作成ソリューション比較の説明画像。"
    },
    {
        "index": 1181,
        "filename": "image_01.png",
        "description": "インスタグラムのDMスクリーンショット。ユーザー「やまくち」がnote販売で月2,000フォロワー運用中、4月の売上が7万円（有料noteのみ）で、さらなる売上拡大について相談。商品数と質向上、バックエンド構築について言及。"
    },
    {
        "index": 1182,
        "filename": "image_02.png",
        "description": "インスタグラムのDMスクリーンショット。やまくちへの詳細な回答。noteのコンテンツ質向上、本業の充実度との関連、有料noteの価値設定、バックエンド（単価大きく、売りやすさ重視）についてのアドバイス。"
    },
    {
        "index": 1183,
        "filename": "image_03.png",
        "description": "インスタグラムのDMスクリーンショット。やまくちの継続相談。LINE企画について。noteの後半で公式LINE誘導、note購入者へのLINE無料相談会・長期SNSリリアップコンサル提案について言及。"
    },
    {
        "index": 1184,
        "filename": "image_04.png",
        "description": "インスタグラムのDMスクリーンショット。やまくちへの最終的なアドバイス。ブログとSNS連携の戦略、フォロワーに対するnote購入促進のポイント、マネタイズ開始のタイミング判断について提示されている。"
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

    print(f"\n✓ Batch 1165-1184 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
