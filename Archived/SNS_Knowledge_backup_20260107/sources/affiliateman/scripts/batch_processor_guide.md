# 画像説明生成バッチ処理ガイド

## 現在の進捗

- **完了**: 55/2,172枚（2.5%）
- **残り**: 2,117枚
- **推定残バッチ数**: 約106バッチ（20枚ずつ）または43バッチ（50枚ずつ）

## 処理フロー

### Step 1: 次のバッチ取得
```bash
python3 process_next_batch.py 20  # 20枚のバッチ
```

### Step 2: Claude Codeで画像を読み込み
各画像パスに対してReadツールを使用

### Step 3: 説明生成
画像の内容を1-2文の日本語で説明

### Step 4: スクリプト生成と保存
```python
# save_batch_X_Y.pyを作成
batch_descriptions = [
    {"index": X, "filename": "image_XX.png", "description": "説明文"},
    ...
]
```

### Step 5: 進捗保存
```bash
python3 save_batch_X_Y.py
```

## 継続的な処理方法

### オプション1: 手動継続（現在の方法）
1. `process_next_batch.py 20`で次のバッチ取得
2. Claude Codeで画像読み込み・説明生成
3. スクリプト保存・実行
4. 繰り返し

### オプション2: 半自動化（推奨）
1. 大きなバッチ（50-100枚）を取得
2. Claude Codeで一括処理
3. 進捗を保存して休憩
4. 次のセッションで続きから再開

## 進捗確認

```bash
# 進捗ファイルから統計を確認
python3 -c "
import json
from pathlib import Path
OUTPUT_DIR = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman')
with open(OUTPUT_DIR / 'image_inventory_progress.json') as f:
    inv = json.load(f)
total = len(inv)
completed = sum(1 for i in inv if i.get('description'))
print(f'進捗: {completed}/{total} ({completed/total*100:.1f}%)')
print(f'残り: {total-completed}枚')
"
```

## 最終ステップ（全画像完了後）

### Phase 5: Markdown更新
```bash
python3 scripts/update_image_descriptions.py
```

### Phase 6: RAG更新
```bash
python3 scripts/chunker.py
```

## Tips

- **バッチサイズ**: 20枚（標準）、50枚（高速）
- **進捗保存**: 各バッチ後に必ず実行
- **セッション分割**: 200-300枚ごとに休憩推奨
- **エラー処理**: 進捗ファイルが壊れた場合はバックアップから復元

## トラブルシューティング

### 進捗ファイルが見つからない
```bash
# 最初のバッチスクリプトを再実行
python3 save_batch_descriptions.py
```

### JSONエラー
```bash
# 進捗ファイルをバリデート
python3 -m json.tool image_inventory_progress.json > /dev/null && echo "OK" || echo "NG"
```
