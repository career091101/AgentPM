#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1825, "filename": "image_142.png", "description": "SNSサロン質問スレッドのスクリーンショット。サロンプラットフォーム選択やZoomサポートについての複数の質問と回答が表示されている。"},
    {"index": 1826, "filename": "image_143.png", "description": "YouTube関連の質問とKくんの回答のスクリーンショット。恋愛系動画配信のスクールローンチと価格設定についての相談内容が記載されている。"},
    {"index": 1827, "filename": "image_144.png", "description": "KくんとYouTuber「TK属人性なし」の質問応答スクリーンショット。10月の恋愛トークスクールローンチやZoomグループコンサル等の具体的なサービス内容が説明されている。"},
    {"index": 1828, "filename": "image_145.png", "description": "香川あおさんによるアカウント設計とマネタイズ方法に関する長文の質問とKくんの詳細な回答のスクリーンショット。"},
    {"index": 1829, "filename": "image_146.png", "description": "KくんとYouTuberの質問応答スクリーンショット。ビジネス系とメンタルハック系ジャンルの選定、フォロワーターゲット設定についての相談内容が表示されている。"},
    {"index": 1830, "filename": "image_147.png", "description": "十川光さんによるアカウントコンセプトとASP選定に関する質問とKくんの回答のスクリーンショット。"},
    {"index": 1831, "filename": "image_148.png", "description": "NORIさんによるスマートアプリクイズアプリのDL数増加とマネタイズ方法についての質問スクリーンショット。"},
    {"index": 1832, "filename": "image_149.png", "description": "KくんとNORIさんの質問応答スクリーンショット。アフィリエイト広告掲載やインフルエンサー認定に関する相談内容が記載されている。"},
    {"index": 1833, "filename": "image_153.png", "description": "SNS攻略サロン限定の12月Kくんアウトプットを告知するバナー画像。サンタキャラと赤字で「12月のKくんのアウトプット」と記載されている。"},
    {"index": 1834, "filename": "image_154.png", "description": "SNS攻略サロン使い方ガイドのバナー画像。矢印・Q&A・書類アイコンと赤髪キャラが配置され「最大限に使いこなそう」というメッセージが表示されている。"},
    {"index": 1835, "filename": "image_01.png", "description": "2023年10月質疑応答まとめ記事のタイトルバナー。月別の質問回答まとめシリーズの表紙画像。"},
    {"index": 1836, "filename": "image_02.png", "description": "macさんによる金融系アカウント運用の相談内容スクリーンショット。無料相談の獲得方法やフォロワー増加戦略についての質問が記載されている。"},
    {"index": 1837, "filename": "image_03.png", "description": "Kくんのmacさんへの回答スクリーンショット。テーマ選定とアカウント設計、マネタイズ戦略についての詳細なアドバイスが記載されている。"},
    {"index": 1838, "filename": "image_04.png", "description": "ごけしさんによるアカウント初期設定と投稿テーマ選定に関する質問スクリーンショット。"},
    {"index": 1839, "filename": "image_05.png", "description": "Kくんのごけしさんへの回答スクリーンショット。ビジネス系アカウント運用、フォロワーマッチング、及びリール活用についてのアドバイスが記載されている。"},
    {"index": 1840, "filename": "image_06.png", "description": "ひろぺーさんによるジャンル選定と女性層ターゲティングの恋愛コンサル相談スクリーンショット。"},
    {"index": 1841, "filename": "image_07.png", "description": "Kくんのひろぺーさんへの回答スクリーンショット。恋愛ソング系マネタイズ戦略と男性層ターゲティングについてのアドバイスが記載されている。"},
    {"index": 1842, "filename": "image_08.png", "description": "からすさんによるアカウント実績構築と広告掲載戦略に関する質問スクリーンショット。"},
    {"index": 1843, "filename": "image_09.png", "description": "Kくんのからすさんへの回答スクリーンショット。100日ハックの活用、プロフィール最適化、及びストーリーズハイライト設定についてのアドバイスが記載されている。"},
    {"index": 1844, "filename": "image_10.png", "description": "ゆゆさんによるリール動画投稿戦略とフィード投稿活用についての質問スクリーンショット。"},
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

    print(f"\n✓ Batch 1825-1844 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
