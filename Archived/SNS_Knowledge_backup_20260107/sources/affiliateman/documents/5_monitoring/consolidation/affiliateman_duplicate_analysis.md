# affiliatemanディレクトリ重複問題の分析

**作成日**: 2025-12-31
**問題**: affiliatemanが2箇所に存在している

---

## 🔍 発見事項

### 1. SNSノウハウプロジェクト配下（憲章あり）

**パス**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman/`

**憲章パス**: `documents/1_initiating/project_charter.md`

**憲章内容**:
- プロジェクト名: affiliateman - コンテンツ取得プロジェクト
- 目的: KくんのSNS攻略サロン限定コンテンツを体系的に取得・整理
- ステータス: ✅ 完了（2025-12-28）
- 成果物:
  - ブログ60件
  - 対談動画3件
  - ZOOMコンサル3件
  - PDF1件
  - 総チャンク数316件（RAG用）

### 2. 独立プロジェクトディレクトリ（憲章なし）

**パス**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman/`

**内容**:
```
- llm_optimized_batch2_435-869.md
- llm_optimized_batch3_870-1304.md
- scripts/ (21ファイル)
```

**推測**: データ処理の途中生成物またはバックアップ

---

## 💡 推奨対応

### オプションA: 重複ディレクトリの削除（推奨）

**理由**:
- SNSノウハウ配下のaffilatemanが正式プロジェクト
- 独立ディレクトリは処理途中のデータ置き場として作られた可能性
- プロジェクト構造の一貫性を保つ

**手順**:
1. 独立ディレクトリの内容を確認（重要データがないか）
2. 重要データがあればSNSノウハウ/affiliatemanへ移動
3. 独立ディレクトリを削除

### オプションB: シンボリックリンク化

**理由**:
- 両方のパスからアクセス可能にしたい場合
- 過去のスクリプトが独立ディレクトリを参照している可能性

**手順**:
1. 独立ディレクトリをリネーム（バックアップ）
2. SNSノウハウ/affiliatemanへのシンボリックリンクを作成

### オプションC: 独立プロジェクトとして正式化

**理由**:
- affiliatemanを副業プログラム直下の独立プロジェクトとして管理したい場合
- SNSノウハウから独立させたい明確な理由がある場合

**手順**:
1. 独立ディレクトリに憲章を作成
2. SNSノウハウ/affiliatemanの内容を統合
3. SNSノウハウ/affiliatemanは削除またはアーカイブ

---

## ⚠️ 確認が必要な項目

1. **独立ディレクトリの内容の重要性**:
   - llm_optimized_batch2_435-869.md
   - llm_optimized_batch3_870-1304.md
   - scripts/配下の21ファイル
   これらは既にSNSノウハウ/affiliatemanに含まれているか？

2. **参照関係**:
   - 他のスクリプトやドキュメントが独立ディレクトリを参照しているか？

3. **ユーザーの意図**:
   - affiliatemanをどちらで管理したいか？

---

## 🎯 次のアクション（推奨）

1. 独立ディレクトリの内容とSNSノウハウ/affiliatemanの内容を比較
2. 重複していれば独立ディレクトリを削除
3. ユニークなファイルがあればSNSノウハウ/affiliatemanへ移動
4. project_charter_checklist.mdを更新（affiliatemanは実質的に憲章あり）

---

**結論**: affiliatemanは**実質的に憲章が存在**している（SNSノウハウ配下）。独立ディレクトリは整理が必要。

