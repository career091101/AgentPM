#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2165, "filename": "image_57.png", "description": "インスタグラム運用の全体戦略を示す図解。新規フォロワーと既存フォロワーに対してそれぞれいいね周り、ハッシュタグ流入、リポストメディア掲載依頼、競合アカ協力、複数サテライトアカなど異なるアプローチを指示し、信頼構築後にアフィ商品提案へ導く段階的な仕組み。"},
    {"index": 2166, "filename": "image_58.png", "description": "インスタで稼ぐための月100万円狙いジャンルとマネタイズ戦略を共有するバナー画像。黄色の背景に金銭と稲妻アイコンでアフィリエイト収入を視覚化。"},
    {"index": 2167, "filename": "image_59.png", "description": "インスタマネタイズとガチで売れるストーリー施策、稼げる最強施策まとめを紹介するバナー画像。ロケットアイコンと男性キャラでアクセルフェーズのコンテンツを表示。"},
    {"index": 2168, "filename": "image_60.png", "description": "フォロワー増加の10施策とインスタ・Twitterでフォロワー爆伸びに関する成功事例紹介のバナー画像。青色背景にTwitterロゴとInstagramロゴで複数プラットフォーム連携を示唆。"},
    {"index": 2169, "filename": "image_61.png", "description": "2023年インスタ攻略ブルーオーシャン16選バナー。紫色背景で今後伸びそうなお宝ジャンルをピックアップし、男性キャラが提案する形式で新規ジャンル開拓のコンテンツ。"},
    {"index": 2170, "filename": "image_62.png", "description": "インスタで稼ぐための固定ピン活用事例まとめのバナー。赤色背景とロケーションピンアイコンでフォロー率・売上UP向上に関する実践的な施策を集約したコンテンツ。"},
    {"index": 2171, "filename": "image_63.png", "description": "2023年インスタ攻略コンセプト設計基礎バナー。紫色背景にターゲットアイコンで圧倒的な差別化戦略に関する基礎知識を提供するコンテンツ。"}
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

    print(f"\n✓ Batch 2165-2171 完了（最終バッチ！）")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

    if remaining == 0:
        print("\n🎉 全2,172枚の画像説明が完了しました！ 🎉")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
