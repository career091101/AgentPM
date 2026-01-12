# T009 FounderResearch マージ戦略（T009-3）

**生成日時**: 2025-12-30

## 対象

- folder1（ベース/統合先）: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research`
- folder2（統合元/重複）: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research`

## 事前分析（T009-2 の結果要約）

- 両フォルダのファイルセットは同一（657/657、ユニーク0）
- 内容差異ありは 12 ファイルのみ（`duplicates_differing.txt` 参照）
- 12 ファイルはいずれも **folder1 の方が更新日時が新しい**（`duplicate_comparison.tsv` 参照）

## マージ方針

1. **ベースフォルダは folder1**
   - 既に全ファイルを保持しており、差異ファイルも folder1 が最新版のため
2. **folder2 から folder1 へのコピーは「ユニークファイルのみ」**
   - `rsync --ignore-existing` を用い、上書きは行わない（安全優先）
3. **重複かつ内容差異のある 12 ファイルは folder1 を正として扱う**
   - folder1 側の内容を維持（上書き不要）
   - folder2 側の差異はバックアップにより保存される

## 実行コマンド（T009-5）

- folder2 → folder1 へユニークファイルのみコピー:
  - `rsync -av --ignore-existing [folder2]/ [folder1]/`

## バックアップ方針（T009-4）

- 変更前の両フォルダを `Archived/FounderResearch_Backup_20251230/` にフルコピーして保全する

## 期待結果

- folder1 の内容は（ユニークが無いため）実質変化なし
- 検証では、バックアップ2つと folder1 のファイル総数が一致し、データロス無しを確認する

