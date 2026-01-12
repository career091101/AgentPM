# 新しいセッション用のプロンプト

次のチャットセッションで以下をコピー&ペーストしてください:

---

## 作業継続リクエスト

affiliateman.siteのブログ記事画像（全2,172枚）に詳細な説明を生成する作業を継続してください。

### 現在の状況

- **総画像数**: 2,172枚
- **詳細説明済み**: 165枚（7.6%）
- **残り**: 2,007枚
- **作業ディレクトリ**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts`

### 引き継ぎドキュメント

詳細は以下を参照:
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts/HANDOVER_IMAGE_DESCRIPTIONS.md
```

### 次にすべきこと

1. 引き継ぎドキュメントを読み込む
2. 進捗を確認する（`python3 find_auto_generated.py`）
3. 次のバッチ20枚を処理する

### 作業フロー（1バッチ20枚）

```bash
# Step 1: 次のバッチ取得
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 process_next_batch.py 20

# Step 2: 表示された20枚の画像パスに対してReadツールで画像を読み込む

# Step 3: 各画像の内容を1-2文の日本語で説明

# Step 4: save_batch_XXX_YYY.py を作成して実行
# （XXX_YYYは次のインデックス番号、例: 174-193）
```

### 説明の品質基準

**良い例**:
```
「インスタグラムアカウント「suu.333」のプロフィール画面。フォロワー12.8万人、投稿526件。「100均専門おうち遊びクリエイター」という肩書きで、低予算の知育・遊び・モンテッソーリ教育を発信している。」
```

**避けるべき例（自動生成）**:
```
「インスタグラム運用に関する説明画像または投稿サムネイル。」
```

### 重要なファイル

- **進捗ファイル**: `image_inventory_progress.json`
- **確認スクリプト**: `find_auto_generated.py`
- **バッチ取得**: `process_next_batch.py`
- **参考**: 最新の処理例は `save_batch_144_173.py`

### このセッションの目標

できるだけ多くのバッチ（20-50バッチ = 400-1,000枚）を処理してください。

---

上記の作業を開始してください。まず、引き継ぎドキュメントを読み込んで進捗を確認し、次のバッチの処理を開始してください。
