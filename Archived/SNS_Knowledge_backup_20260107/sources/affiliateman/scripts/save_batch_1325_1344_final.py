#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1325, "filename": "image_03.png", "description": "Instagramの質疑応答スレッド。ユーザー「たか」がお金の発信とリール運用について相談している最初のコメント。"},
    {"index": 1326, "filename": "image_04.png", "description": "「けんけ」からのアドバイス。ダイエット系とマネタイズ系ジャンルの選択肢の違いについてのコンサル回答。"},
    {"index": 1327, "filename": "image_05.png", "description": "「K く ん」の質問と「けんけ」の長文アドバイス。LINE相談料金設定とビジネス系運用戦略に関する複数の質問への回答。"},
    {"index": 1328, "filename": "image_06.png", "description": "「はや」からの新しいアカウント企画についての相談。インスタで月5～10万円稼ぐビジネスモデルについての質問。"},
    {"index": 1329, "filename": "image_07.png", "description": "「K く ん」の長文回答。新規アカウントで月5万円稼ぐための具体的なコンセプト設定とターゲット戦略の解説。"},
    {"index": 1330, "filename": "image_08.png", "description": "「こむぎ」のハイライト運用と投稿デザインに関する複数の質問。フィード投稿とリール投稿の使い分けについての相談。"},
    {"index": 1331, "filename": "image_09.png", "description": "「し ほ」の子連れアカウント運用に関する質問。毎日投稿・ストーリー更新・フォロワー伸ばしのコツについての相談。"},
    {"index": 1332, "filename": "image_10.png", "description": "「こむぎ」からのハイライト作成と投稿位置についての複数の質問。画像挿入やキャラクター設定の相談内容。"},
    {"index": 1333, "filename": "image_11.png", "description": "「こむぎ」からのフィード投稿デザインに関する相談コメント。色選びやキャラクター統一についてのアドバイス要望。"},
    {"index": 1334, "filename": "image_12.png", "description": "「mayu_100yennail」のストーリーズ投稿間隔と質問方法についての相談。アンケート機能の活用についての複数の質問。"},
    {"index": 1335, "filename": "image_13.png", "description": "「K く ん」からの複数の回答。ストーリーズ投稿のタイミング、アンケート活用、ハイライト設定についての詳細アドバイス。"},
    {"index": 1336, "filename": "image_14.png", "description": "「イツキ」のフィードリーチ数減少についての質問。アルゴリズム対策とリール強化についてのコンサル相談。"},
    {"index": 1337, "filename": "image_15.png", "description": "「K く ん」のシャドウバン対策に関する外部ブログリンク紹介。Instagramのシャドウバン確認方法についての教育的コンテンツ。"},
    {"index": 1338, "filename": "image_16.png", "description": "「str」のリール投稿戦略に関する相談。ファッションコーディネートフィードからリール投稿メインへの変更についての質問。"},
    {"index": 1339, "filename": "image_17.png", "description": "「K く ん」のリール投稿タイミングと内容構成についての複数の回答。フィードとリールの使い分け戦略の解説。"},
    {"index": 1340, "filename": "image_18.png", "description": "「str」からの投稿時間と投稿頻度に関する確認質問。見直しと改善についての短い相談コメント。"},
    {"index": 1341, "filename": "image_19.png", "description": "「シュウ」からのインスタ姿勢改善の進捗と相談。サムネタイトル設定とユーザーターゲティングについての質問。"},
    {"index": 1342, "filename": "image_20.png", "description": "「リリ」のタロット占い・オラクルカード事業とHSP向けターゲティングの相談。フロント商品と潜在顧客分析についての複数質問。"},
    {"index": 1343, "filename": "image_21.png", "description": "「リリ」からの追加質問。恋愛系ジャンル選定とTikTok新規開設についての短いコメント返信。"},
    {"index": 1344, "filename": "image_22.png", "description": "「しらとら」の無料プレゼント企画とハイライト設定に関する相談。プレゼント内容と見せ方の工夫についての複数質問。"},
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

    print(f"\n✓ Batch 1325-1344 再処理完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
