#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1725, "filename": "image_42.png", "description": "まひろ氏からのDMでSNS×ブログ攻略系アカウントについて4つの質問が記載されているスクリーンショット。"},
    {"index": 1726, "filename": "image_43.png", "description": "K氏からまひろ氏への返信DMで、ブログ作成スキルアップの有益なポイントについて詳細に説明している画像。"},
    {"index": 1727, "filename": "image_44.png", "description": "なお氏からのDMで、子なし移住生活をテーマにしたインスタグラムアカウント運用について相談内容が記載されている。"},
    {"index": 1728, "filename": "image_45.png", "description": "K氏からなお氏への返信DMで、アカウント選択とターゲット設定について詳細なアドバイスが記載されている。"},
    {"index": 1729, "filename": "image_46.png", "description": "けいと氏からのDM。Web系フリーモード副業を志望し、その実現方法についてK氏に相談している内容のスクリーンショット。"},
    {"index": 1730, "filename": "image_47.png", "description": "けいと氏からの続きのDM。Web系フリーランスエンジニアを目指す際の戦略や学習方法についての相談が記載されている。"},
    {"index": 1731, "filename": "image_48.png", "description": "K氏からけいと氏への返信DM。フリーランスエンジニア戦略、ジャンル選定、マネタイズ方法について複数のポイントを解説している。"},
    {"index": 1732, "filename": "image_49.png", "description": "K氏からけいと氏へのDM。Web系フリーモードでの働き方選択と具体的なキャリアパスについて詳細にアドバイスしている。"},
    {"index": 1733, "filename": "image_50.png", "description": "けいと氏からのDMで、フォロワー周りについての相談とWeb特化型転職アカウント戦略の詳細な検討内容が記載されている。"},
    {"index": 1734, "filename": "image_51.png", "description": "K氏からけいと氏への返信DM。フリーランスジャンルの選定、アカウント構築、ビジネス展開方法についての具体的なアドバイス。"},
    {"index": 1735, "filename": "image_52.png", "description": "けいと氏のDMで、Web系フリーランスエンジニア転職とビジネス参入の2択判断についてK氏に相談している内容。"},
    {"index": 1736, "filename": "image_53.png", "description": "K氏からけいと氏へのDM。全体の広告のところでセールスファネルとビジネス参入戦略について詳細に述べている。"},
    {"index": 1737, "filename": "image_54.png", "description": "ゆう氏からのDM。TIKTOKマネタイズ実装攻略動画について2点の質問を記載したスクリーンショット。"},
    {"index": 1738, "filename": "image_55.png", "description": "ゆう氏からのDM続き。動画作成時のコンテンツ展開方法とエクセルジャンル参入戦略についての相談内容。"},
    {"index": 1739, "filename": "image_56.png", "description": "K氏からゆう氏への返信DM。インスタやTikTokでのビジネス参入アドバイスと高単価商品販売の具体的な戦略を説明。"},
    {"index": 1740, "filename": "image_57.png", "description": "せいぬ氏からのDM。ChatGPTやTikTokショート動画でのビジネス展開について複数の質問が記載されている。"},
    {"index": 1741, "filename": "image_58.png", "description": "K氏からせいぬ氏への返信DM。AIツール活用とコンテンツ販売、Tips型ビジネスのジャンル選択について詳細に説明している。"},
    {"index": 1742, "filename": "image_59.png", "description": "じゅり氏からのDM。Kさんの動画全体を拝見し、インスタアカウント設定とマネタイズについて相談している内容。"},
    {"index": 1743, "filename": "image_60.png", "description": "じゅり氏からの続きのDM。夫婦コンサル設計と職業経験を活かしたアカウント構築戦略についての相談が記載されている。"},
    {"index": 1744, "filename": "image_61.png", "description": "じゅり氏のDM。マネタイズ方法とリール構成についてK氏からのアドバイスを受けながら、ハイライトとアフィリエイト配置の重要性を学んでいる。"},
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

    print(f"\n✓ Batch 1725-1744 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
