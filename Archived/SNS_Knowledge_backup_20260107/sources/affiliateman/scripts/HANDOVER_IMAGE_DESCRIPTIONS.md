# 画像説明生成作業の引き継ぎドキュメント

## 作業概要

affiliateman.siteのブログ記事（36件）から取得した全2,172枚の画像に対して、Claude Codeが実際に画像を読み込んで詳細な日本語説明を生成する作業。

## 現在の進捗状況

- **総画像数**: 2,172枚
- **詳細説明済み**: 485枚（22.3%）
- **残り**: 1,687枚
- **進捗ファイル**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/image_inventory_progress.json`

## 作業の背景

### フェーズ1-3: 完了済み
1. ✅ ブログ記事を再スクレイピングして画像をダウンロード（2,172枚）
2. ✅ 画像ファイルを `blog/{category}/images/{記事名}/` に保存
3. ✅ `image_inventory.json` を生成

### フェーズ4: 現在進行中（22.3%完了）
**目的**: 全2,172枚の画像を実際に読み込んで、内容を1-2文の日本語で説明

**重要**: 以前に自動生成した一般的な説明（「インスタグラム運用に関する説明画像...」など）は、実際の画像内容を反映していないため、すべて詳細な説明に置き換える必要がある。

## 作業フロー（1バッチ20枚を処理する標準手順）

### Step 1: 進捗確認

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 find_auto_generated.py
```

**期待される出力例**:
```
総画像数: 2172
詳細説明済み: 236 (10.9%)
自動生成説明: 1936 (89.1%)
```

**最新実行結果（2025-12-29 Batch 445-464実行後）**:
```
総画像数: 2172
詳細説明済み: 485 (22.3%)
自動生成説明: 1687 (77.7%)
```

### Step 2: 次のバッチ取得

```bash
python3 process_next_batch.py 20
```

**出力**: 次に処理すべき20枚の画像パスが表示される

### Step 3: 画像を読み込んで説明生成

Claude Codeで以下を実行:

```python
# 20枚の画像パスに対してReadツールを使用
Read(/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/blog/instagram/images/XXX/image_01.png)
Read(/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/blog/instagram/images/XXX/image_02.png)
# ... 20枚分
```

各画像を見て、以下の形式で説明を生成:
- **長さ**: 1-2文（簡潔に）
- **言語**: 日本語
- **内容**: 画像の具体的な内容（アカウント名、フォロワー数、テーマ、図解の説明など）

**良い説明の例**:
```
「インスタグラムアカウント「suu.333」のプロフィール画面。フォロワー12.8万人、投稿526件。「100均専門おうち遊びクリエイター」という肩書きで、低予算の知育・遊び・モンテッソーリ教育を発信している。」
```

**悪い説明の例（自動生成）**:
```
「インスタグラム運用に関する説明画像または投稿サムネイル。記事「子育てジャンルコンセプトがうまいアカウント紹介」の関連コンテンツ。」
```

### Step 4: スクリプト作成

次のバッチのインデックスを確認（例: 174-193）し、スクリプトを作成:

```bash
# ファイル名: save_batch_174_193.py
```

スクリプトのテンプレート:

```python
#!/usr/bin/env python3
"""
Batch 174-193の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 174-193の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 174,
        "filename": "image_XX.png",
        "description": "ここに実際の画像説明を記載"
    },
    # ... 20件分
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

    print(f"\n✓ Batch 174-193 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
```

### Step 5: スクリプト実行

```bash
python3 save_batch_174_193.py
```

**期待される出力**:
```
[174] image_XX.png: 説明更新
...
✓ Batch 174-193 完了
詳細説明済み: 185/2172 (8.5%)
残り: 1987枚
```

### Step 6: 繰り返し

Step 2-5を繰り返して、全2,172枚を処理

## 重要なファイル

### 進捗管理ファイル
- **`image_inventory_progress.json`**: 全画像の説明を格納（随時更新）
- **`image_inventory.json`**: 元のファイル（バックアップ、読み取り専用）

### スクリプト
- **`process_next_batch.py`**: 次のバッチを取得（自動生成説明を未処理として検出）
- **`find_auto_generated.py`**: 進捗状況を確認
- **`save_batch_XXX_YYY.py`**: 各バッチの説明を保存（セッションごとに新規作成）

### ディレクトリ構造
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/
├── blog/
│   └── instagram/images/
│       └── {記事名}/
│           ├── image_01.png
│           ├── image_02.png
│           └── ...
├── scripts/
│   ├── process_next_batch.py
│   ├── find_auto_generated.py
│   ├── save_batch_305_324.py (最新)
│   └── save_batch_XXX_YYY.py (次に作成)
├── image_inventory.json (元データ)
└── image_inventory_progress.json (進捗)
```

## 完了後の作業（Phase 5-6）

全2,172枚の説明生成が完了したら:

### Phase 5: Markdownファイル更新

```bash
python3 scripts/update_image_descriptions.py
```

プレースホルダー `![PLACEHOLDER:image_XX.png](...)` を実際の説明 `![詳細説明](...)` に置換

### Phase 6: RAGチャンク更新

```bash
python3 scripts/chunker.py
```

画像説明を含むRAGチャンクを再生成

## トラブルシューティング

### Q: 進捗ファイルが見つからない
```bash
# 最新のバッチスクリプトを再実行
python3 save_batch_144_173.py
```

### Q: インデックス番号がわからない
```bash
# process_next_batch.pyの出力を確認
python3 process_next_batch.py 1 | head -1
# 出力例: [174] /Users/.../image_XX.png
# → 次のバッチは174から開始
```

### Q: 自動生成と詳細説明の見分け方
**自動生成の特徴**:
- 「運用に関する説明画像または...」
- 「記事のバナー画像またはメインビジュアル。」（後に具体的な記事タイトルなし）

**詳細説明の特徴**:
- 具体的なアカウント名、フォロワー数
- 画像内のテキストや要素の説明
- 1-2文の具体的な内容

## 推定残り作業量

- **残り枚数**: 1,936枚
- **バッチ数（20枚ずつ）**: 約97バッチ
- **1バッチあたりの所要時間**: 5-10分
- **必要セッション数**: 6-8セッション
- **推定総所要時間**: 1日程度（断続的に実行）

## 完了済みバッチ一覧

- ✅ Batch 0-19 (画像: 0-19) - 完了
- ✅ Batch 20-39 (画像: 20-39) - 完了
- ✅ Batch 40-59 (画像: 40-59) - 完了
- ✅ Batch 60-79 (画像: 60-79) - 完了
- ✅ Batch 80-99 (画像: 80-99) - 完了
- ✅ Batch 100-119 (画像: 100-119) - 完了
- ✅ Batch 120-144 (画像: 120-144) - 完了
- ✅ Batch 144-173 (画像: 144-173) - 完了
- ✅ Batch 305-324 (画像: 305-324) - 完了（2025-12-29 09:45）
- ✅ Batch 445-464 (画像: 445-464) - 完了（2025-12-29 12月質疑応答まとめ記事）
- ✅ Batch 505-524 (画像: 505-524) - 完了（2025-12-29 Twitter Q&A質問応答まとめ 20枚）

**進捗ステータス**: 445枚完了 (20.5%) → Batch 505-524完了後に445枚に更新


## 作業のコツ

1. **バッチサイズ**: 20枚が標準。慣れてきたら30枚に増やしてもOK
2. **説明の簡潔さ**: 長すぎる説明は避ける。重要な情報のみ抽出
3. **同じ記事の連続画像**: パターンを把握すれば効率的に処理可能
4. **進捗保存**: 各バッチ処理後に必ずスクリプトを実行して保存

## 最終確認

全画像処理完了後:

```bash
# 1. 進捗確認
python3 find_auto_generated.py
# 期待値: 詳細説明済み: 2172 (100%)

# 2. サンプル確認
python3 -c "
import json
with open('../image_inventory_progress.json') as f:
    inv = json.load(f)
for i in [0, 500, 1000, 1500, 2000]:
    print(f'[{i}] {inv[i][\"filename\"]}: {inv[i][\"description\"][:60]}...')
"

# 3. Phase 5-6を実行
python3 update_image_descriptions.py
python3 chunker.py
```

## 成功基準

✅ 全2,172枚の `description` フィールドに具体的な説明が入っている
✅ 自動生成パターン（"運用に関する..."）が0件
✅ Markdownファイルのプレースホルダーがすべて置換されている
✅ RAGチャンクに画像説明が含まれている
