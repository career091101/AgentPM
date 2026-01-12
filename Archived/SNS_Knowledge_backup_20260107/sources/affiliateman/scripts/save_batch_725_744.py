#!/usr/bin/env python3
"""
Batch 725-744の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 725-744の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 725,
        "filename": "image_125.png",
        "description": "Instagram質疑応答スレッド。ユーザーRNがフォロワー増加の悩みを投稿し、KKくんやその他ユーザーがアカウント運用やジャンル選択についてアドバイスしている。"
    },
    {
        "index": 726,
        "filename": "image_126.png",
        "description": "Instagram質疑応答スレッド。RNが副業アカウント運用について相談し、KKくんが資産運用ジャンルやニッチなジャンル選択のアドバイスをしている画面。"
    },
    {
        "index": 727,
        "filename": "image_127.png",
        "description": "Instagram質疑応答スレッド。RNがインスタからアフィリエイト完結する副業について質問し、KKくんがnoteやフォロワー目標についてアドバイスしている。"
    },
    {
        "index": 728,
        "filename": "image_128.png",
        "description": "Instagram質疑応答スレッド。KKくんがSNSの王様についての質問に、サロンメンバー限定コンサルの有無についてアドバイスしている。また、コンサル業やメルカリ情報発信についても言及。"
    },
    {
        "index": 729,
        "filename": "image_129.png",
        "description": "Instagram質疑応答スレッド。KKくんが複数のInstagramアカウント戦略と、アカウント運用の継続についてアドバイスしている長いテキスト投稿。"
    },
    {
        "index": 730,
        "filename": "image_130.png",
        "description": "Instagram質疑応答スレッド。KKくんが不要なイラストレイター探しと行動力についてのアドバイス、RNが早速実行するという返信が表示されている。"
    },
    {
        "index": 731,
        "filename": "image_131.png",
        "description": "Instagram質疑応答スレッド。ナツというユーザーがInstagram運用について質問し、KKくんがコンサル、アフィリエイト、noteの出口戦略についてアドバイスしている。"
    },
    {
        "index": 732,
        "filename": "image_132.png",
        "description": "Instagram質疑応答スレッド。ねこが、イラスト・アート系フォロワーを増やす方法について相談し、複数のフォロー戦略についてのアドバイスが書かれている。"
    },
    {
        "index": 733,
        "filename": "image_133.png",
        "description": "Instagram質疑応答スレッド。ねこがデザイナー向けInstagram戦略について質問し、複数のクリエイター紹介アカウントのURLが記載されている。"
    },
    {
        "index": 734,
        "filename": "image_134.png",
        "description": "Instagram質疑応答スレッド。KKくんがリールやフォロワー増加についてのアドバイス、ねこがマネタイズについて質問している長い投稿スレッド。"
    },
    {
        "index": 735,
        "filename": "image_135.png",
        "description": "Instagram質疑応答スレッド。ふみが住まい・インテリアカテゴリのアカウント運用について相談し、KKくんが発信内容やターゲティングについてアドバイスしている。"
    },
    {
        "index": 736,
        "filename": "image_136.png",
        "description": "Instagram質疑応答スレッド。吉田が不動産費用アカウント運用について複数質問し、KKくんがリール投稿やマネタイズについてアドバイスしている。"
    },
    {
        "index": 737,
        "filename": "image_137.png",
        "description": "Instagram質疑応答スレッド。KKくんが吉田のアドバイス質問に返信し、フィード写真やリール運用のマネタイズについて詳しく説明しているテキスト。"
    },
    {
        "index": 738,
        "filename": "image_138.png",
        "description": "Instagram質疑応答スレッド。すもも、吉田などのユーザーがガジェットやアラサー向けInstagram運用について相談し、KKくんがジャンルやターゲット選定についてアドバイスしている。"
    },
    {
        "index": 739,
        "filename": "image_139.png",
        "description": "Instagram質疑応答スレッド。しろあんが恋愛系アカウントのツイート頻度や投稿戦略について質問し、KKくんがフォロワー属性や投稿タイミングについてアドバイスしている。"
    },
    {
        "index": 740,
        "filename": "image_140.png",
        "description": "Instagram質疑応答スレッド。KKくんがbot活用やフォロワー増加の具体例を説明し、しろあんがbot導入についての質問に返信している。"
    },
    {
        "index": 741,
        "filename": "image_141.png",
        "description": "Instagram質疑応答スレッド。Yasuが精力剤アフィリエイトのTwitter戦略について相談し、KKくんがTwitter運用のアドバイスと参考記事リンクを提示している。"
    },
    {
        "index": 742,
        "filename": "image_142.png",
        "description": "Instagram質疑応答スレッド。吉田がTwitterアダルト系アフィリエイト戦略について複数の質問をし、コンサルント選択についてのアドバイスが表示されている。"
    },
    {
        "index": 743,
        "filename": "image_143.png",
        "description": "Instagram質疑応答スレッド。KKくんが吉田のアダルト系アフィリエイトに関する複数の質問に、詳しい出口戦略やコンサル候補についてアドバイスしている。"
    },
    {
        "index": 744,
        "filename": "image_144.png",
        "description": "Instagram質疑応答スレッド。ちゃむがアカウント凍結対応について質問し、凍結原因の可能性（50以上のいいね周り、メディア登録など）と新規作成についてのアドバイスが表示されている。"
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

    print(f"\n✓ Batch 725-744 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
