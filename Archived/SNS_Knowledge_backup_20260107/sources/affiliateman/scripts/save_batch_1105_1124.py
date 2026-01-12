#!/usr/bin/env python3
"""
Batch 1105-1124の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1105-1124の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1105,
        "filename": "image_71.png",
        "description": "インスタグラムDM質問機能のスクリーンショット。ユーザー「吉田」が転職のInstagram活用について5つの具体的な質問を投稿。リール投稿の表示設定やキャプション作成方法、フォロワー増加戦略などについて相談している。"
    },
    {
        "index": 1106,
        "filename": "image_72.png",
        "description": "KKくんの回答コメント。フォロー周りとフォロワー周りの質問について、統一性とエンゲージメント率を重視したフォロー・フォロー除外の戦略を詳しく説明している。"
    },
    {
        "index": 1107,
        "filename": "image_73.png",
        "description": "ゆみユーザーからの相談。インスタ投稿を3月8日から開始したばかりで、アカウント設計や投稿方向についてのアドバイスを求めている。KKくんが回答を提供。"
    },
    {
        "index": 1108,
        "filename": "image_74.png",
        "description": "KKくんの詳細な回答。ターゲット設定方法、ジャンル選定のポイント、アカウント設計の重要性について、具体的なインスタグラムアカウント例を挙げながら説明している。"
    },
    {
        "index": 1109,
        "filename": "image_75.png",
        "description": "楷ユーザーからのリール質問。ベビー服やグッズについてのフィードから、リール投稿時の動画バイラル化方法についての相談。KKくんが複数のアカウント例を提示して回答。"
    },
    {
        "index": 1110,
        "filename": "image_76.png",
        "description": "KKくんの回答コメント。スライドショーとリールの使い分け、フィード投稿と動画コンテンツの活用方法についての詳しい説明を記載している。"
    },
    {
        "index": 1111,
        "filename": "image_77.png",
        "description": "楷ユーザーの追加質問。子供向けコンテンツのターゲット設定やアカウント設計、リール動画の活用方法について、より具体的なアドバイスを求めている。"
    },
    {
        "index": 1112,
        "filename": "image_78.png",
        "description": "びよみユーザーからの質問。過去ジャンル選定についての相談で、FXやアフィリエイト関連の質問を提示。KKくんが初心者向けのアドバイスを提供している。"
    },
    {
        "index": 1113,
        "filename": "image_79.png",
        "description": "KKくんの詳細な回答。Instagram運用でのジャンル選定と成功条件、アカウント設計と投稿戦略、アフィリエイトジャンルの選択について実践的なアドバイスを記載している。"
    },
    {
        "index": 1114,
        "filename": "image_80.png",
        "description": "ミヤダイユーザーからのフォロー周りとフォロワー周りの質問。アカウント初期段階でのフォロー数増加戦略について3つの具体的なQ&Aが記載されている。"
    },
    {
        "index": 1115,
        "filename": "image_81.png",
        "description": "ミヤダイユーザーからの追加相談。アカウント新規開設時のストーリー投稿とリール投稿のタイミング、インプレッション管理についての質問。KKくんが実践的なアドバイスを提供。"
    },
    {
        "index": 1116,
        "filename": "image_82.png",
        "description": "こいぞユーザーの相談。テラサーワーク男性でのアカウント コンセプト選定について、複数のアフィリエイト商材選択肢（検索SIM、楽天ROOM、プロテインなど）の提案と説明。"
    },
    {
        "index": 1117,
        "filename": "image_83.png",
        "description": "こいぞユーザーの追加質問。メンズコスメジャンル選定についての相談で、フォロワー獲得と商品売上の両立方法についてのアドバイスを求めている。"
    },
    {
        "index": 1118,
        "filename": "image_84.png",
        "description": "楷ユーザーのアカウント運用相談。ターゲット設定の重要性や、自身のアカウントでのアクション設計についての詳しい説明を記載している。"
    },
    {
        "index": 1119,
        "filename": "image_85.png",
        "description": "KKくんの回答。アカウント別運用戦略とフォロワー増加のためのコンテンツ戦略について、具体的なInstagramアカウント例を挙げながら説明。"
    },
    {
        "index": 1120,
        "filename": "image_86.png",
        "description": "S ユーザーからの相談。新規アカウント開設5日目でのリール投稿投稿数と初期インプレッション確保についての質問。ハッシュタグとトレンド音声の活用方法について。"
    },
    {
        "index": 1121,
        "filename": "image_87.png",
        "description": "KKくんの回答とS ユーザーの追加質問。初期アカウントの再生回数データ（250M再生、100M再生達成）の実例と、フォロワー増加の段階的な推移についての説明。"
    },
    {
        "index": 1122,
        "filename": "image_88.png",
        "description": "みかさユーザーの相談。美容クリニック系アカウント運用でのホーム率保存率向上方法、類似アカウント参考について、複数の医院系アカウント例（麻酔歯科医、先生など）の提案。"
    },
    {
        "index": 1123,
        "filename": "image_89.png",
        "description": "KKくんの回答。マネタイズジャンル選定と英語学習コンテンツの活用方法、恋愛系やDIY系アカウントのコンセプト決定プロセスについての詳しい説明。"
    },
    {
        "index": 1124,
        "filename": "image_90.png",
        "description": "ゆーとユーザーからの相談。3000人超えたフォロワーアカウントでの英語教育とハリウッドスター美容法からのアフィリエイト展開についての質問と、KKくんの詳細なアドバイス。"
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

    print(f"\n✓ Batch 1105-1124 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
