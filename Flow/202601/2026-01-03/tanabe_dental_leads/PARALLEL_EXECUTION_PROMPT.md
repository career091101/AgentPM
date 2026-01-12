# 田辺玩具向け歯科医院リード生成 - 並列実行用システムプロンプト

## 新規チャットで以下をコピー＆ペーストしてください

---

## プロジェクト概要

田辺玩具向けの歯科医院営業リスト生成プロジェクトの**バッチ2-360の並列実行**を担当してください。

### 基本情報
- **総対象件数**: 15,880件
- **総バッチ数**: 360バッチ（50件/バッチ）
- **既完了**: バッチ1（50件、青森県の一部）
- **残タスク**: バッチ2-360（15,830件）

### プロジェクトディレクトリ
```
/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads/
```

### 重要ファイル
- `extract_batch_50.py`: Google Maps API実行スクリプト（360バッチ対応済み）
- `.env`: Google Maps APIキー（設定済み）
- `prefecture_allocation_15880.json`: 都道府県別割り当てデータ
- `EXECUTION_PLAN.md`: 実行計画詳細
- `batch_001_raw_data_20260103_235857.json`: バッチ1の完了データ（参考）

---

## 実行タスク: バッチ2-360の並列実行

### Phase A: バッチ2-20（並列5バッチずつ）

以下の手順で実行してください:

#### STEP 1: 作業ディレクトリ移動
```bash
cd /Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads
```

#### STEP 2: バッチ2-6を並列実行（第1グループ）
```bash
python3 extract_batch_50.py --batch 2 &
python3 extract_batch_50.py --batch 3 &
python3 extract_batch_50.py --batch 4 &
python3 extract_batch_50.py --batch 5 &
python3 extract_batch_50.py --batch 6 &
wait
```

**期待される出力**:
- `batch_002_raw_data_[タイムスタンプ].json`
- `batch_003_raw_data_[タイムスタンプ].json`
- `batch_004_raw_data_[タイムスタンプ].json`
- `batch_005_raw_data_[タイムスタンプ].json`
- `batch_006_raw_data_[タイムスタンプ].json`

#### STEP 3: バッチ7-11を並列実行（第2グループ）
```bash
python3 extract_batch_50.py --batch 7 &
python3 extract_batch_50.py --batch 8 &
python3 extract_batch_50.py --batch 9 &
python3 extract_batch_50.py --batch 10 &
python3 extract_batch_50.py --batch 11 &
wait
```

#### STEP 4: バッチ12-16を並列実行（第3グループ）
```bash
python3 extract_batch_50.py --batch 12 &
python3 extract_batch_50.py --batch 13 &
python3 extract_batch_50.py --batch 14 &
python3 extract_batch_50.py --batch 15 &
python3 extract_batch_50.py --batch 16 &
wait
```

#### STEP 5: バッチ17-20を並列実行（第4グループ）
```bash
python3 extract_batch_50.py --batch 17 &
python3 extract_batch_50.py --batch 18 &
python3 extract_batch_50.py --batch 19 &
python3 extract_batch_50.py --batch 20 &
wait
```

#### STEP 6: 進捗確認
```bash
ls -lh batch_*_raw_data_*.json | wc -l
# 期待値: 20（バッチ1-20）
```

---

## 実行上の注意点

### 1. API制限対策
- **並列実行数**: 最大5バッチまで（Google Maps APIのレート制限: 50リクエスト/秒）
- **待機時間**: 各バッチグループ間で`wait`コマンドで完了待機

### 2. エラーハンドリング
- APIエラーが発生した場合は、該当バッチのみ単独で再実行
- 例: バッチ5が失敗した場合
  ```bash
  python3 extract_batch_50.py --batch 5
  ```

### 3. 重複防止
- `extract_batch_50.py`は自動的に既存バッチのplace_idをスキップ
- 再実行しても重複データは生成されない

### 4. タイムアウト
- 1バッチあたりの実行時間: 約3-5分
- 5バッチ並列実行: 約5-7分で完了
- 20バッチ完了予定時間: 約20-30分

---

## 成功基準

### Phase A完了時（バッチ1-20）
- [x] 20個のJSONファイル生成（`batch_001` - `batch_020`）
- [x] 各JSONファイルに約50件のデータ
- [x] エラー率5%以下
- [x] 総データ取得件数: 約1,000件

---

## 次のフェーズへの移行

Phase A（バッチ1-20）完了後、以下を報告してください:

1. **生成ファイル数**: `ls batch_*_raw_data_*.json | wc -l`
2. **総データ件数**: 各JSONの`total_clinics`の合計
3. **エラー発生状況**: 失敗したバッチ番号（あれば）
4. **実行時間**: STEP 2開始から完了までの時間

報告後、Phase B（バッチ21-40）の指示を出します。

---

## トラブルシューティング

### 問題1: "GOOGLE_MAPS_API_KEY not found"
**解決策**:
```bash
cat .env
# APIキーが存在することを確認
```

### 問題2: "Error: バッチ番号は1-360の範囲で指定してください"
**原因**: スクリプトが更新されていない
**解決策**: 既に更新済みなので発生しないはず。発生した場合は報告してください。

### 問題3: バッチが途中で停止する
**解決策**: 単独で該当バッチを再実行
```bash
python3 extract_batch_50.py --batch [バッチ番号]
```

---

## 実行開始コマンド（コピー用）

```bash
# 作業ディレクトリ移動
cd /Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/tanabe_dental_leads

# バッチ2-6並列実行
python3 extract_batch_50.py --batch 2 &
python3 extract_batch_50.py --batch 3 &
python3 extract_batch_50.py --batch 4 &
python3 extract_batch_50.py --batch 5 &
python3 extract_batch_50.py --batch 6 &
wait

# バッチ7-11並列実行
python3 extract_batch_50.py --batch 7 &
python3 extract_batch_50.py --batch 8 &
python3 extract_batch_50.py --batch 9 &
python3 extract_batch_50.py --batch 10 &
python3 extract_batch_50.py --batch 11 &
wait

# バッチ12-16並列実行
python3 extract_batch_50.py --batch 12 &
python3 extract_batch_50.py --batch 13 &
python3 extract_batch_50.py --batch 14 &
python3 extract_batch_50.py --batch 15 &
python3 extract_batch_50.py --batch 16 &
wait

# バッチ17-20並列実行
python3 extract_batch_50.py --batch 17 &
python3 extract_batch_50.py --batch 18 &
python3 extract_batch_50.py --batch 19 &
python3 extract_batch_50.py --batch 20 &
wait

# 進捗確認
ls -lh batch_*_raw_data_*.json | wc -l
echo "期待値: 20ファイル"
```

---

## このプロンプトの使い方

1. **新規Claude Codeセッション**を開始
2. 上記の「## プロジェクト概要」以降をすべてコピー
3. 新規チャットにペースト
4. Claudeが自動的にバッチ2-20を並列実行します

実行完了後、このチャット（元のチャット）に戻って進捗を報告してください。
