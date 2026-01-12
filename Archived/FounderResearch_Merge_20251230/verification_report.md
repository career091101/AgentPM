# T009 FounderResearch マージ検証レポート（T009-6）

**生成日時**: 2025-12-30 22:17

## 対象
- merged（folder1）: `aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research`
- folder2: `aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research`
- backup1: `aipm_v0/Archived/FounderResearch_Backup_20251230/folder1`
- backup2: `aipm_v0/Archived/FounderResearch_Backup_20251230/folder2`

## ファイル数検証
- backup1 ファイル数: 657
- backup2 ファイル数: 657
- merged（folder1）ファイル数: 657
- 判定: OK（merged_count >= max(backup1, backup2)）

## データロス検証（merged vs backup1）
- backup1に存在してmergedに無い: 0
- mergedにのみ存在（backup1に無い）: 0
- 同名で内容差異あり: 0

## 参考：folder2との差異（merged vs backup2）
- 同名で内容差異あり: 12

## 結論
- merged（folder1）はバックアップ取得時点のfolder1と完全一致（データロス/意図しない変更なし）

## 付録
- 事前差分（folder1 vs folder2）の一覧: `aipm_v0/Flow/202512/2025-12-30/T009_FounderResearch_merge/duplicates_differing.txt`
- マージ実行ログ: `aipm_v0/Flow/202512/2025-12-30/T009_FounderResearch_merge/merge_execution.log`
