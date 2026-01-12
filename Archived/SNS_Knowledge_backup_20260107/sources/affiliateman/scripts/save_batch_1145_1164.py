#!/usr/bin/env python3
"""
Batch 1145-1164の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1145-1164の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1145,
        "filename": "image_111.png",
        "description": "KKくんのTikTok投稿に対する回答。固定勤画でテコ入れが必要、TIKTOKアフィは教育しないといういうないなど、マネタイズについての具体的なアドバイスを示すコメント欄スクリーンショット。"
    },
    {
        "index": 1146,
        "filename": "image_112.png",
        "description": "はるかユーザーからのアカウント運用についての質問とそれに対するKKくんの詳細な回答。男性向け・女性向けの恋愛アカウントについて、マッチングアプリ・占いアフィエイトでの収益化や動画再生数・フォロワー数の増やし方についてのTikTok質疑応答。"
    },
    {
        "index": 1147,
        "filename": "image_113.png",
        "description": "こい（@koi.sou）ユーザーからの声優向けアカウント運用についての質問と回答。基本的には愛要のテーマで音声と動画で発信すること、直近で伸びているアカウントの特徴などが述べられた回答スクリーンショット。"
    },
    {
        "index": 1148,
        "filename": "image_114.png",
        "description": "吉田ユーザーからの転職アカウント利用についての3つの質問。TikTokからツイッターへの流入方法、恋愛アフィリエイトの推奨、転職アフィリエイトについての質問とそれに対するKKくんの詳細な回答が記載。"
    },
    {
        "index": 1149,
        "filename": "image_115.png",
        "description": "KKくんからの吉田ユーザーへの回答。TikTokからツイッターへの流入、オープンチャットの活用、転職コンサルについてのアドバイスが述べられたインスタグラム質疑応答スクリーンショット。"
    },
    {
        "index": 1150,
        "filename": "image_116.png",
        "description": "けーちゃんユーザーからの複数質問。会社内でのSNS事業展開についての悩みや、個人的なInstagram運用、飲食店PR運用代行についての相談内容とそれに対する詳細な回答コメント欄。"
    },
    {
        "index": 1151,
        "filename": "image_117.png",
        "description": "KKくんからけーちゃんへの詳細な回答。飲食店運用代行について個人的な経験を交えた具体的なアドバイス、SNS事業の立ち上げ方についての説明が記載されたInstagram質疑応答。"
    },
    {
        "index": 1152,
        "filename": "image_118.png",
        "description": "KKくんからけーちゃんへの継続回答。飲食店の利用代行についての具体的なコンサル例、個人的な経験に基づいたアドバイス、利益を出すための具体的な施策についての説明スクリーンショット。"
    },
    {
        "index": 1153,
        "filename": "image_119.png",
        "description": "momoka（初めまして）ユーザーからのSNSスクール運用広告についての質問。広告の質が低くなった、LPが成功できないセミナーについての相談内容とそれに対する詳細な回答を示すInstagram質疑応答。"
    },
    {
        "index": 1154,
        "filename": "image_120.png",
        "description": "KKくんからmomokaユーザーへの回答。Twitter×noteやインスタフィリエイトの活用法についてのアドバイス、広告アカウントの運用についての説明が記載された長文の回答スクリーンショット。"
    },
    {
        "index": 1155,
        "filename": "image_121.png",
        "description": "Romuユーザーからの質問。奥さんを使った美容コスメのTikTok運用についての相談、テーマはエロ系美容で最近伸び悩んでいるなどの質問と、それに対するKKくんの回答スクリーンショット。"
    },
    {
        "index": 1156,
        "filename": "image_122.png",
        "description": "KKくんからRomuへの詳細な回答。月15万円程度のアフィリエイト収入についての具体的なアドバイス、マネートラックやお薬EXPRESSなどのASPについての説明が述べられたInstagram回答。"
    },
    {
        "index": 1157,
        "filename": "image_123.png",
        "description": "りユーザーからのオンラインサロン立ち上げについての質問。ハイライト・ストーリーズから誘導するCV、100万のKGIから逆算したKPI決定についての相談と、KKくんによる詳細な回答スクリーンショット。"
    },
    {
        "index": 1158,
        "filename": "image_124.png",
        "description": "たいがユーザーからのnoteについての質問と、KKくんからの回答。有料noteの無料部分の書き込みについてのアドバイス、クローズドなコミュニティ運用についての説明が記載されたInstagram質疑応答。"
    },
    {
        "index": 1159,
        "filename": "image_125.png",
        "description": "たいがユーザーからの継続質問。note構成についての詳細なアドバイス、マッチングアプリの攻略noteやマネタイズ専線についての説明、具体的なコンテンツ例が示されたInstagram回答。"
    },
    {
        "index": 1160,
        "filename": "image_126.png",
        "description": "KKくんからたいがへの回答続き。マネタイズの専線についてのさらに詳細な説明、オープンチャットやサロン販売についてのコンテンツ例が示された長文のInstagram質疑応答スクリーンショット。"
    },
    {
        "index": 1161,
        "filename": "image_127.png",
        "description": "KKくんからたいがへのマネタイズ専線についての詳細な説明。有料noteの販売、オープンチャット購入者限定、公式LINE無料サポート、有料サロンへの招待などの複数マネタイズ戦略が具体的に提示されている。"
    },
    {
        "index": 1162,
        "filename": "image_128.png",
        "description": "KKくんからたいがへの最終回答。無料オープンチャットと有料サロンの差別化ポイント、情報量についての具体的な説明、オープンチャットの運用内容についてのアドバイスが記載されたスクリーンショット。"
    },
    {
        "index": 1163,
        "filename": "image_129.png",
        "description": "たいがユーザーからの継続質問。有料noteについてのコミュニティ限定特典についての詳細な説明、noteの値段3980円や4980円での販売についてのアドバイスが示されたInstagram質疑応答。"
    },
    {
        "index": 1164,
        "filename": "image_130.png",
        "description": "ゆーと（23日前）ユーザーからの質問。ハリウッドスター関係のマネタイズ、U-NEXTを活用した推し洋画の見つけ方、マネタイズについての複数の相談とそれに対するKKくんの詳細な回答を含むInstagram質疑応答。"
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

    print(f"\n✓ Batch 1145-1164 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
