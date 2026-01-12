#!/usr/bin/env python3
"""
Batch 1185-1204の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
2023年5月質疑応答のまとめ記事から20枚を処理
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1185-1204の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1185,
        "filename": "image_05.png",
        "description": "インスタグラムでのフォロワー獲得戦略に関する質疑応答。ユーザー「みの」が出口商品選定に関するアドバイスを求めており、婚期希望層や恋愛マッチング層へのアプローチ方法について検討している。"
    },
    {
        "index": 1186,
        "filename": "image_06.png",
        "description": "英語ジャンルのマネタイズ戦略に関する質疑応答。無料note→ラインorオープンチャット→サロン月2980円の流れを検討している女性起業家からの相談内容。"
    },
    {
        "index": 1187,
        "filename": "image_07.png",
        "description": "ビジネス系とダイエット系の複数ジャンル展開に関する質疑応答。K くんが参考となるインスタグラムアカウントを提示し、ジャンル戦略のアドバイスを提供している。"
    },
    {
        "index": 1188,
        "filename": "image_08.png",
        "description": "初期段階のアカウント運用戦略に関する質疑応答。ユーザーMがお金の知識発信アカウントでフォロワーを増やす方法について、プロフィール設計やコンテンツ戦略のアドバイスを求めている。"
    },
    {
        "index": 1189,
        "filename": "image_09.png",
        "description": "フォロワー獲得と出口商品設計に関するアドバイス。K くんが複数アカウント戦略で初期層はリール中心、コンセプト選定やターゲット決定の重要性を説明している。"
    },
    {
        "index": 1190,
        "filename": "image_10.png",
        "description": "コンサルカフェアカウント運用戦略に関する質疑応答。Key(きー)がインスタグラムポータルサイト掲載数増加を目的とした現在・過去施策の課題解決法を提案している。"
    },
    {
        "index": 1191,
        "filename": "image_11.png",
        "description": "ストーリーズ活用とフォロワー増加に関する詳細な質疑応答。K くんがコンカフェでのフォロワー悩みに対し、悩み回収→相談→発信という流れでリーチ数を増やす戦略を説明している。"
    },
    {
        "index": 1192,
        "filename": "image_12.png",
        "description": "リール投稿頻度とフォロワー増加に関する質疑応答。ユーザーが1ヶ月でフォロワーを3000-5000人増やすリール戦略の相談をし、K くんが発見タブ掲載8割超えの重要性をアドバイスしている。"
    },
    {
        "index": 1193,
        "filename": "image_13.png",
        "description": "NFTと投資ジャンルの可能性に関する質疑応答。ユーザーがNFTジャンルでリール・フィード投稿→ハイライト→ブログアフィリエイトの収益化について相談している。"
    },
    {
        "index": 1194,
        "filename": "image_14.png",
        "description": "インスタグラムアカウント統計表示画面。リーチしたアカウント数1,263、フォロー済みフォロワー1,251と中央部に円グラフ表示。下部にはインプレッション3,265件（ホーム1,486件、その他914件、プロフィール807件、発見から53件）の詳細統計が表示されている。"
    },
    {
        "index": 1195,
        "filename": "image_15.png",
        "description": "恋愛キャリアカウンセラーからの相談。LINE登録やメルマガ登録数の問題、オープンチャット活用による月の収益化の可能性について、K くんにアドバイスを求めている会話形式。"
    },
    {
        "index": 1196,
        "filename": "image_16.png",
        "description": "オープンチャット開設報告と運用継続に関する質疑応答。宮本ちほが短期間でコメントをもらいながらもオープンチャット利用について褒めており、K くんが今後の施策方針をアドバイスしている。"
    },
    {
        "index": 1197,
        "filename": "image_17.png",
        "description": "NFTジャンル副業化と収益化戦略に関する質疑応答。ユーザーがリール・フィード投稿からハイライト→ブログアフィリエイトへの収益化パターンについてK くんに相談している。"
    },
    {
        "index": 1198,
        "filename": "image_18.png",
        "description": "NFT関連アカウント構築とマネタイズに関する質疑応答。ユーザーがNFT案件の可能性やAIツール活用によるインスタ作成効率化について、K くんにアドバイスを求めている。"
    },
    {
        "index": 1199,
        "filename": "image_19.png",
        "description": "ダイエットアカウント戦略に関する長文相談。ユーザーがマネタイズ可能性、アフィリエイト・note販売など複数出口戦略について詳細に説明し、K くんのアドバイスを求めている。"
    },
    {
        "index": 1200,
        "filename": "image_20.png",
        "description": "マネタイズ戦略に関する相談への回答。K くんがマネタイズは無理だろうと思っていた点について、アフィリエイト・noteなどの活用で初期段階の知識不足をカバーできることを説明している。"
    },
    {
        "index": 1201,
        "filename": "image_21.png",
        "description": "インスタリール運用とマネタイズに関する質疑応答。ユーザーがTikTok集客によるTwitter誘導からのマネタイズ、インスタリールのみでの集客可能性について相談している。"
    },
    {
        "index": 1202,
        "filename": "image_22.png",
        "description": "美肌関連アカウント構築に関する質疑応答。ユーザーがプロフィール記載内容、マネタイズ方法、目的設定などについて詳細にK くんに相談している。"
    },
    {
        "index": 1203,
        "filename": "image_23.png",
        "description": "インスタリール運用とシャドウバン対策に関する質疑応答。ユーザーがリール→Twitterへの導線作成時のシャドウバン懸念について、K くんにアドバイスを求めている。"
    },
    {
        "index": 1204,
        "filename": "image_24.png",
        "description": "初期段階の発信内容と方向性に関する長文相談。ユーザーよるとが膳活・健康・美容・メンタル・ダイエットなど複数テーマの発信可能性について、詳細にK くんに相談しアドバイスを求めている。"
    },
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

    print(f"\n✓ Batch 1185-1204 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
