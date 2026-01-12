# T009 FounderResearch マージ完了レポート（T009-7）

**生成日時**: 2025-12-30

## マージ戦略サマリー

- ベース（統合先）: `aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research`
- 統合元: `aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research`
- 方針: folder2 → folder1 へ **ユニークファイルのみコピー（上書きなし）**
- 重複ファイルの扱い: folder1 を正（差異がある重複 12 件は全て folder1 が新しいため、folder1 を維持）

## 処理内容

- ベースフォルダ: folder1
- コピーしたファイル数: 0（`rsync --ignore-existing` により全て既存扱い）
- 重複処理したファイル数: 0（上書き/リネーム等の追加処理なし）

## ファイル数統計

- フォルダ1: 657 ファイル
- フォルダ2: 657 ファイル
- マージ後（フォルダ1）: 657 ファイル

## 差分サマリー

- ユニークファイル: 0
- 重複ファイル: 657
  - うち内容差異あり: 12（`duplicates_differing.txt` 参照）
  - 対応: folder1 を維持（folder2 側はバックアップで保全）

## バックアップ

- バックアップパス: `aipm_v0/Archived/FounderResearch_Backup_20251230/`
  - folder1 バックアップ: `aipm_v0/Archived/FounderResearch_Backup_20251230/folder1`
  - folder2 バックアップ: `aipm_v0/Archived/FounderResearch_Backup_20251230/folder2`

## 参照（ログ/検証）

- 差分分析: `aipm_v0/Flow/202512/2025-12-30/T009_FounderResearch_merge/diff_analysis.md`
- マージ戦略: `aipm_v0/Flow/202512/2025-12-30/T009_FounderResearch_merge/merge_strategy.md`
- 実行ログ: `aipm_v0/Flow/202512/2025-12-30/T009_FounderResearch_merge/merge_execution.log`
- 検証レポート: `aipm_v0/Flow/202512/2025-12-30/T009_FounderResearch_merge/verification_report.md`

## 次のアクション（任意）

1. `Founder_Agent_ForStartup/Founder_Research` を参照しているリンク/スクリプトが無いか確認
2. 問題なければ、folder2 をアーカイブ移動または削除（削除前に本バックアップの存在を再確認）

