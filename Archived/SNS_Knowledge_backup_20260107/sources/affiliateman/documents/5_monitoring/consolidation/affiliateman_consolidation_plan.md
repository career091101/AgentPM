# affiliateman重複問題 - 統合実行計画

**作成日**: 2025-12-31
**目的**: 独立ディレクトリとSNSノウハウ配下のaffiliateman を統合

---

## 📊 現状分析

### ディレクトリ構造

#### 独立ディレクトリ（副業/projects/affiliateman）
```
affiliateman/
├── llm_optimized_batch2_435-869.md (195K)
├── llm_optimized_batch3_870-1304.md (167K)
└── scripts/ (19ファイル)
    └── save_batch_*.py (バッチ処理スクリプト)
```

**総ファイル数**: 21ファイル

#### SNSノウハウ配下（SNSノウハウ/affiliateman）
```
affiliateman/
├── llm_optimized_batch1_0-434.md (123K)
├── llm_optimized_batch4_1305-1739.md (162K)
├── llm_optimized_batch5_1740-2171.md (125K)
├── metadata_backup.json
├── zoom_consult/ (ZOOMコンサル動画文字起こし)
├── blog_backup/ (ブログ記事バックアップ)
│   ├── twitter/ (19記事)
│   ├── tiktok/ (16記事)
│   └── instagram/ (25記事)
├── documents/
│   └── 1_initiating/
│       └── project_charter.md (プロジェクト憲章)
└── scripts/ (多数のスクリプト + レポート)
```

**総ファイル数**: 100ファイル以上

---

## 🔍 重要な発見

### 1. **重複ではなく欠損**

独立ディレクトリのbatch2とbatch3は、SNSノウハウ配下に**存在しない**重要ファイル。

| ファイル | 独立ディレクトリ | SNSノウハウ配下 |
|---------|:----------------:|:---------------:|
| batch1 (0-434) | ❌ | ✅ |
| **batch2 (435-869)** | **✅** | **❌** |
| **batch3 (870-1304)** | **✅** | **❌** |
| batch4 (1305-1739) | ❌ | ✅ |
| batch5 (1740-2171) | ❌ | ✅ |

**結論**: batch2とbatch3は**欠けているデータ**であり、SNSノウハウ配下に移動すべき。

### 2. scriptsディレクトリの違い

**独立ディレクトリのscripts (19ファイル)**:
- save_batch_1285_1304.py
- save_batch_1365_1384.py
- save_batch_1405_1424.py
- ... (バッチ1285-2064の範囲)

**SNSノウハウ配下のscripts (多数)**:
- save_batch_365_384.py
- save_batch_465_484.py
- youtube_transcriber.py
- scraper.py
- final_validation.py
- ... (より広範囲 + ユーティリティスクリプト)

**結論**: scriptsは異なる範囲をカバー。独立ディレクトリは一部のバッチ処理スクリプトのみ。

---

## 🎯 統合方針

### オプションA: 欠損ファイル移動 + 独立ディレクトリ削除（推奨）

**理由**:
- SNSノウハウ配下が正式プロジェクト（憲章あり）
- 独立ディレクトリは一時的なデータ置き場
- batch2とbatch3を移動すれば全バッチデータが揃う

**手順**:
1. batch2とbatch3をSNSノウハウ配下に移動
2. scriptsディレクトリの内容を比較・評価
3. ユニークなスクリプトがあればSNSノウハウ配下に移動
4. 独立ディレクトリをバックアップ後削除

**リスク**: 低（移動前にバックアップ）

### オプションB: 独立ディレクトリをアーカイブとして保持

**理由**:
- 後で参照する可能性がある
- ディスク容量に余裕がある

**手順**:
1. batch2とbatch3をSNSノウハウ配下にコピー
2. 独立ディレクトリを`_archive_20251231`にリネーム
3. README.mdを追加して経緯を記録

**リスク**: 非常に低（削除しない）

---

## 📋 実行計画（オプションA推奨）

### Phase 1: バックアップ作成

```bash
# 独立ディレクトリ全体をバックアップ
cp -r /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman \
      /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman_backup_20251231
```

**完了基準**: バックアップディレクトリが作成され、21ファイル全てが存在

---

### Phase 2: batch2とbatch3の移動

```bash
# batch2を移動
mv /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/llm_optimized_batch2_435-869.md \
   /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman/

# batch3を移動
mv /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/llm_optimized_batch3_870-1304.md \
   /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman/
```

**完了基準**: SNSノウハウ配下にbatch1-5の全5ファイルが揃う

---

### Phase 3: scriptsの比較と移動判断

#### 3-1. 独立ディレクトリのscriptsをリストアップ

独立ディレクトリのscripts (19ファイル):
- バッチ範囲: 1285-2064
- すべて`save_batch_*.py`形式

#### 3-2. SNSノウハウ配下に同名ファイルが存在するか確認

```bash
# 重複チェック
for file in /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/scripts/*.py; do
  filename=$(basename "$file")
  if [ -f "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman/scripts/$filename" ]; then
    echo "重複: $filename"
  else
    echo "ユニーク: $filename"
  fi
done
```

#### 3-3. 判断基準

| ケース | 対応 |
|--------|------|
| 同名ファイルが存在 | ハッシュ値比較 → 同じなら独立版を削除、異なれば`_独立版`サフィックス付きで移動 |
| 同名ファイルが存在しない | SNSノウハウ配下に移動 |

**完了基準**: 全スクリプトが評価され、移動または削除が決定

---

### Phase 4: 独立ディレクトリの削除

```bash
# 空になったディレクトリを削除
rm -rf /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman
```

**前提条件**:
- batch2とbatch3が移動済み
- scriptsが評価・移動済み
- バックアップが存在

**完了基準**: 独立ディレクトリが削除され、SNSノウハウ配下のみが存在

---

### Phase 5: 検証

#### 5-1. batchファイルの完全性チェック

```bash
# SNSノウハウ配下にbatch1-5が全て存在するか確認
ls -lh /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman/llm_optimized_batch*.md
```

**期待結果**: 5ファイル（batch1-5）が表示される

#### 5-2. バッチ範囲の連続性確認

| ファイル | 範囲 | サイズ |
|---------|------|--------|
| batch1 | 0-434 | 123K |
| batch2 | 435-869 | 195K |
| batch3 | 870-1304 | 167K |
| batch4 | 1305-1739 | 162K |
| batch5 | 1740-2171 | 125K |

**総範囲**: 0-2171（連続）

#### 5-3. プロジェクト憲章の確認

```bash
cat /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman/documents/1_initiating/project_charter.md
```

**確認事項**:
- プロジェクト名: affiliateman - コンテンツ取得プロジェクト
- ステータス: 完了（2025-12-28）
- 総チャンク数: 316件

#### 5-4. 完了レポート作成

**成果物**: `affiliateman_consolidation_completion_report.md`

**含む内容**:
- 移動したファイルリスト
- scriptsの評価結果
- 検証結果
- 次のアクション（該当あれば）

**完了基準**: レポートが作成され、全検証項目が✅

---

## ⚠️ リスク管理

### リスク1: batch2とbatch3のデータ損失

**対策**: Phase 1でバックアップ作成

**復旧手順**:
```bash
# バックアップから復元
cp /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman_backup_20251231/llm_optimized_batch2_435-869.md \
   /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman/
```

### リスク2: scriptsの重複・競合

**対策**: Phase 3でハッシュ値比較

**復旧手順**: バックアップから必要なスクリプトを個別復元

### リスク3: 参照パスの破損

**対策**: 移動前にGrepで参照パスを確認

```bash
grep -r "副業/projects/affiliateman" /Users/yuichi/AIPM/aipm_v0/
```

**復旧手順**: 発見した参照を手動で修正

---

## 🚀 実行コマンド概要

```bash
# Phase 1: バックアップ
cp -r affiliateman affiliateman_backup_20251231

# Phase 2: batch移動
mv affiliateman/llm_optimized_batch2_435-869.md SNSノウハウ/affiliateman/
mv affiliateman/llm_optimized_batch3_870-1304.md SNSノウハウ/affiliateman/

# Phase 3: scripts評価（個別判断）
# → ユーザー確認後に実行

# Phase 4: 独立ディレクトリ削除
rm -rf affiliateman

# Phase 5: 検証
ls -lh SNSノウハウ/affiliateman/llm_optimized_batch*.md
```

---

## ✅ ユーザー確認事項

### 確認1: 実行方針の承認

**質問**: オプションA（欠損ファイル移動 + 削除）で進めてよいですか？

**選択肢**:
- A: はい、オプションAで進める（推奨）
- B: オプションB（アーカイブ保持）で進める
- C: 実行を保留

### 確認2: scriptsの扱い

**質問**: 独立ディレクトリのscripts (19ファイル) をどう扱いますか？

**選択肢**:
- A: ハッシュ値比較して、ユニークなものだけ移動
- B: 全て移動（同名ファイルは`_独立版`サフィックス付き）
- C: scriptsは移動せず、batch2とbatch3のみ移動

### 確認3: 削除のタイミング

**質問**: 独立ディレクトリをいつ削除しますか？

**選択肢**:
- A: 検証完了後すぐに削除
- B: 1週間後に削除（様子見）
- C: アーカイブとして保持（削除しない）

---

## 📝 次のステップ

1. **ユーザー確認**: 上記3つの確認事項に回答
2. **Phase 1実行**: バックアップ作成
3. **Phase 2実行**: batch2とbatch3の移動
4. **Phase 3実行**: scripts評価（確認2の回答に基づく）
5. **Phase 4実行**: 独立ディレクトリ削除（確認3の回答に基づく）
6. **Phase 5実行**: 検証とレポート作成

---

**作成者**: Claude Sonnet 4.5
**実行待機中**: ユーザー確認待ち
