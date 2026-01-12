#!/usr/bin/env python3
"""
Batch 925-944の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 925-944の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 925,
        "filename": "image_101.png",
        "description": "instagramのコメント。ユーザー「たろー」がインスタ投稿について投稿のデザイン・内容の見分け方や構成についての質問。分析結果を含むキャプションが長く、コピーしにくいといった実務的な課題について相談している。"
    },
    {
        "index": 926,
        "filename": "image_102.png",
        "description": "instagramのコメント。ユーザー「Kくん」が投稿について・プロフ内容・固定ピンの活用・アフィリエイト売上の具体例と参考アカウントを列挙し、フォロワー増加のための実践的な施策を提案している。"
    },
    {
        "index": 927,
        "filename": "image_103.png",
        "description": "instagramのコメント。ユーザー「たろー」が月100記事作成によるフォロワー増加の効果について、100記事でも1000人未満という実例に基づいた質問をしている。"
    },
    {
        "index": 928,
        "filename": "image_104.png",
        "description": "instagramのコメント。ユーザー「みの」がフォロワー伸びの原因分析・フォロワー転換率・アカウント改善方法について詳細な質問をし、K君が具体的な数字（フォロワー2550人・6ヶ月運用・73%転換率）を含む回答を提供している。"
    },
    {
        "index": 929,
        "filename": "image_105.png",
        "description": "instagramのコメント。ユーザー「Kくん」がアラサー独身・サラフォー独身といったテーマのアカウントについて、ターゲット層の活動を詳しく説明し、ブログ・marriage・marriage情報の活用について具体例を挙げている。"
    },
    {
        "index": 930,
        "filename": "image_106.png",
        "description": "instagramのコメント。ユーザー「きなこもち」がアラフォーバイチ子持ち記事についての相談で、K君が類似アカウント例（キママちゃん・シングルマザー）を参考に、プロフの副業マネタイズについてアドバイスしている。"
    },
    {
        "index": 931,
        "filename": "image_107.png",
        "description": "instagramのコメント。ユーザー「きなこもち」がアラフォーシングルマザーの婚活アカウント化についての質問に、K君が副業と婚活の組み合わせの可能性について実例と判断基準を説明している。"
    },
    {
        "index": 932,
        "filename": "image_108.png",
        "description": "instagramのコメント。ユーザー「りょー」がアカウントジャンルについてスレッド一通りの相談に続き、『インスタのフォロワー0人からの増やし方』について有効性を確認している。"
    },
    {
        "index": 933,
        "filename": "image_109.png",
        "description": "instagramのコメント。ユーザー「T」がリールからの集客をメインにしたいという相談で、目標（月に3人成約）とKPI設定について、リール・ストーリーの使い分けとマッチングアプリについてアドバイスを求めている。"
    },
    {
        "index": 934,
        "filename": "image_110.png",
        "description": "instagramのコメント。K君が「メッション」「リールのハック」「インスタ外部流入」についての3つの重要ポイントを箱条書きで説明し、月100万円達成までのロードマップを提示している。"
    },
    {
        "index": 935,
        "filename": "image_111.png",
        "description": "instagramのコメント。ユーザー「T」がリール投稿について毎日投稿の必要性・1日1本投稿で月30分相談機能の有効性について実例を交えた質問。K君が月ZOOMコンサルの実施と具体的な施策を説明している。"
    },
    {
        "index": 936,
        "filename": "image_112.png",
        "description": "instagramのコメント。ユーザー「misaki」がアカウント立ち上げのコンセプト（新作男の子ママ・卵アレルギー向けレシピ）について相談し、K君がレシピ系アカウントの特性と利益化戦略について具体的なアドバイスをしている。"
    },
    {
        "index": 937,
        "filename": "image_113.png",
        "description": "instagramのコメント。前のメッセージの続きで、レシピ系アカウントの特徴（フォロワー3-5円程度）と類似ニッチの判断基準、アフィリエイト活用について詳しく説明されている。"
    },
    {
        "index": 938,
        "filename": "image_114.png",
        "description": "instagramのコメント。ユーザー「平良信人」が参入ジャンルについてアドバイスを求め、副業（月10万目標・半属人制）・健康（自転車・運動・セルフケア）・仕事術のジャンル選択と実装方法について詳しく説明されている。"
    },
    {
        "index": 939,
        "filename": "image_115.png",
        "description": "instagramのコメント。K君が副業ジャンル選択後の具体的な戦略（ブログ＋SNS・SNS運用代行・副業特化）について、各ジャンルの利益化方法と競合分析を詳細に説明している。"
    },
    {
        "index": 940,
        "filename": "image_116.png",
        "description": "instagramのコメント。K君が最適なジャンル選択（サロンメンバーの活動例）・SNS運用代行の効果・動画編集のニッチについて、マネタイズとフォロワー増加の関連性を説明している。"
    },
    {
        "index": 941,
        "filename": "image_117.png",
        "description": "instagramのコメント。K君がサロンメンバーの実例を通じて、コンセプト設定・ジャンル選択の重要性、アカウント立ち上げ段階でのアドバイス内容について詳しく説明している。"
    },
    {
        "index": 942,
        "filename": "image_118.png",
        "description": "instagramのコメント。ユーザー「ささみん」がスウィーツダイエット（25kg痩せた実例）とコンセプト、スウィーツレシピの自分で作成・ダイエット情報・統一感の3つの質問をしている。"
    },
    {
        "index": 943,
        "filename": "image_119.png",
        "description": "instagramのコメント。K君がスウィーツレシピの自分で作成・ダイエット情報の教育・統一感の重要性について、リール・ストーリー・フィードの活用方法と複数アカウント戦略について説明している。"
    },
    {
        "index": 944,
        "filename": "image_120.png",
        "description": "instagramのコメント。K君がリポスト・リール新規獲得・ダイエット情報の教育・ブログについての4つの項目に対し、それぞれのタイミング最適化とアカウント構築方針についてアドバイスを提供している。"
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

    print(f"\n✓ Batch 925-944 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
