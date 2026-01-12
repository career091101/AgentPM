# 画像説明生成の継続方法

## 現在の状況

- **進捗**: 55/2,172枚（2.5%）
- **処理済み**: Batch 0-54
- **次のバッチ**: Batch 55-79（25枚）
- **残り**: 約2,117枚

## このセッションの目標

Claude Codeの1セッションで全2,172枚を処理するのは、トークン制限とセッション時間の制約から現実的ではありません。

### 推奨アプローチ

1. **このセッション**: 200-300枚を目標に処理（合計10-15バッチ）
2. **進捗保存**: `image_inventory_progress.json`に随時保存
3. **次のセッション**: `process_next_batch.py`で続きから再開

## 次のセッションでの再開方法

```bash
# 1. 進捗確認
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts
python3 -c "
import json
from pathlib import Path
OUTPUT_DIR = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman')
with open(OUTPUT_DIR / 'image_inventory_progress.json') as f:
    inv = json.load(f)
total = len(inv)
completed = sum(1 for i in inv if i.get('description'))
print(f'進捗: {completed}/{total} ({completed/total*100:.1f}%)')
"

# 2. 次のバッチ取得
python3 process_next_batch.py 25

# 3. Claude Codeで画像読み込み・説明生成・保存
# （本セッションと同じフロー）
```

## 高速化のアイデア

### オプション1: バッチサイズ拡大
- 25枚 → 50枚 → 100枚と段階的に増やす
- Token使用量を監視しながら調整

### オプション2: 説明の簡素化
- 1-2文 → 1文のみ
- 重要な情報のみに絞る

### オプション3: 複数セッション並行
- 異なる記事カテゴリを別々のセッションで処理
- 例: Instagram記事（セッション1）、Twitter記事（セッション2）

## 完了予測

- **1セッションあたり**: 200-300枚
- **必要セッション数**: 約7-11セッション
- **推定総所要時間**: 1-2日（断続的に実行）

## 重要ファイル

- `image_inventory_progress.json`: 進捗管理（最重要）
- `process_next_batch.py`: 次のバッチ取得
- `save_batch_X_Y.py`: 各バッチの説明保存
- `batch_processor_guide.md`: 作業ガイド

## トラブルシューティング

### 進捗が消えた場合
```bash
# 最新のバッチスクリプトを再実行
python3 save_batch_35_54.py  # 最後に成功したバッチ
```

### JSON破損
```bash
# 元のinventoryから再構築
cp ../image_inventory.json ../image_inventory_progress.json
# 各バッチスクリプトを順に再実行
python3 save_batch_descriptions.py
python3 save_batch_15_34.py
python3 save_batch_35_54.py
```
