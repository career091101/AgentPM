# Phase 1: データ整合性チェック 中間レポート

**作成日**: 2025-01-29
**対象**: Corporate_Product_Research プロジェクト

---

## エグゼクティブサマリー

**主要な発見**:
- 実ファイル数: 25件（SUCCESS 14件、FAILURE 11件）
- master_index.md記載: 26件（全く異なるID体系を使用）
- データ整合性の問題: master_index.mdは古いID体系を参照し、実ファイルと完全に不一致
- 削除ファイル: 2025-12-29のバックアップ/マージ作業により、旧ID体系のファイルがArchivedに移動

**修正アクション**:
1. master_index.mdを実ファイルに基づいて完全に書き換え
2. research_progress.mdを実態に合わせて更新

---

## 1.1 実ファイル数の確定

### SUCCESS (14件)

#### TIER2_MEGA_HIT (6件)
1. CORP_S006 - ゼクシィ
2. CORP_S007 - SUUMO（スーモ）
3. CORP_S009 - ホットペッパービューティー
4. CORP_S011 - リクナビNEXT
5. CORP_S014 - カーセンサー
6. CORP_S015 - とらばーゆ

#### TIER3_SAAS (3件)
1. CORP_S005 - Airレジ
2. CORP_S012 - Airペイ
3. CORP_S016 - Airリザーブ

#### TIER5_NEW_BUSINESS (5件)
1. CORP_S003 - スタディサプリ
2. CORP_S018 - スタディサプリ for TEACHERS
3. CORP_S020 - ゼクシィ縁結び
4. CORP_S024 - リクナビ派遣
5. CORP_S025 - ゼクシィ相談カウンター

### FAILURE (11件)

#### TIER6_CLEAR_WITHDRAWAL (10件)
1. CORP_F001 - ポンパレモール
2. CORP_F002 - R25
3. CORP_F004 - ナースフル
4. CORP_F005 - Quipper Video（戦略的統合事例）
5. CORP_F006 - ISIZE（アイサイズ）
6. CORP_F008 - AB-ROAD紙版（エービーロード）
7. CORP_F012 - リクルートブック紙版
8. CORP_F013 - 進学ブック紙版
9. CORP_F014 - タウンワークスキマ
10. CORP_F015 - ケイコとマナブ（完全撤退）

#### TIER8_STRATEGIC_EXIT (1件)
1. CORP_F010 - ケイコとマナブ

---

## 1.2 master_index.mdとの同期確認

### 不一致の詳細

**master_index.mdの記載（26件）**:
- SUCCESS: 17件（TIER1: 3件、TIER2: 4件、TIER3: 4件、TIER5: 6件）
- FAILURE: 9件（TIER6: 5件、TIER7: 1件、TIER8: 3件）
- 使用ID範囲: CORP_S001-S031, CORP_F003-F020

**実ファイル（25件）**:
- SUCCESS: 14件（TIER2: 6件、TIER3: 3件、TIER5: 5件）
- FAILURE: 11件（TIER6: 10件、TIER8: 1件）
- 使用ID範囲: CORP_S003-S025, CORP_F001-F015

**不一致の原因**:
- master_index.mdは旧ID体系を参照
- 実ファイルは新ID体系に更新済み
- ID体系が完全に異なり、照合不可

---

## 1.3 削除されたファイルの調査

### Archivedディレクトリの確認

**場所**: `/Users/yuichi/AIPM/aipm_v0/Archived/merge_backup_2025-12-29/`

**発見内容**:
- `source_半角_backup/projects/Corporate_Product_Research/documents/`に旧ID体系のファイルが存在
- master_index.mdに記載されているIDと一致
- 以下のファイルがアーカイブに存在（実ファイルには不在）:
  - TIER1_GLOBAL_MA: CORP_S001 (Indeed), S002 (Glassdoor), S023 (Indeed Prime)
  - TIER2_MEGA_HIT: CORP_S004 (じゃらん), S008 (ホットペッパーグルメ), S010 (リクナビ), S013 (タウンワーク)
  - TIER3_SAAS: CORP_S017 (Airシフト), S019 (Quipper School), S022 (スーモカウンター), S028 (Airワーク採用管理)
  - TIER5_NEW_BUSINESS: CORP_S021 (リクルートカード), S026 (SUUMO B2B), S027 (進学総研), S029 (リクルートライフスタイル), S030 (リクルートジョブズ), S031 (リクルート住まいカンパニー)
  - TIER6_CLEAR_WITHDRAWAL: CORP_F003 (ATND), F007 (ホットペッパービューティーコスメ), F009 (ガテン), F011 (フロムエー紙版), F016 (リクルートブック就職版)
  - TIER7_STRATEGIC_RESTRUCTURE: CORP_F017 (住まいの窓口)
  - TIER8_STRATEGIC_EXIT: CORP_F018 (リクルートコスモス), F019 (フロムエーナビ紙版), F020 (リクルートエージェント旧体制)

### 削除の意図

**推測**:
- 2025-12-29にバックアップ/マージ作業が実施された
- 旧ID体系（CORP_S001-S031）から新ID体系（CORP_S003-S025）への移行
- 一部のケーススタディが統合または除外された
- 意図的な整理と判断

**証拠**:
- Archivedディレクトリのタイムスタンプ: 2025-12-29
- バックアップフォルダ名: `merge_backup_2025-12-29`
- 実ファイルのcreated_at/updated_at: 2025-12-28または2025-12-29

---

## 1.4 research_progress.mdとの整合性

### 記載内容の矛盾

**research_progress.mdの記載**:
- Phase 4完了: 51件達成
- 統計: PASS基準達成率100%、平均ソース数13.2件

**実態**:
- 実ファイル: 25件のみ
- 差異: 26件の不足

**矛盾の原因**:
- research_progress.mdは旧ID体系での集計を記録
- バックアップ/マージ作業後に未更新
- 実態と大幅に乖離

---

## 修正アクション

### 1. master_index.mdの完全書き換え

**実施内容**:
- 実ファイル25件を正として、master_index.mdを新規作成
- 統計サマリーを実態に合わせて更新（総ケース数: 25件、成功17件 → 14件、失敗9件 → 11件）
- TIER別の分類を実ファイルに基づいて再構成

### 2. research_progress.mdの更新

**実施内容**:
- 進捗記録を実態の25件に修正
- 旧データ（51件）に関する注記を追加
- 2025-12-29のバックアップ/マージ作業の経緯を記録

### 3. 削除ファイル調査結果の記録

**実施内容**:
- Archivedディレクトリの状況を文書化
- 旧ID体系から新ID体系への移行を記録
- 今後の参照用にアーカイブファイルのリストを保存

---

## 次のステップ

1. master_index.mdの書き換え実施
2. research_progress.mdの更新実施
3. Phase 2（テンプレート準拠性チェック）に移行

---

## 付録: 完全なファイルリスト

### 実ファイル（25件）

**SUCCESS (14件)**:
```
SUCCESS/TIER2_MEGA_HIT/CORP_S006_zexy.md
SUCCESS/TIER2_MEGA_HIT/CORP_S007_suumo.md
SUCCESS/TIER2_MEGA_HIT/CORP_S009_hotpepper_beauty.md
SUCCESS/TIER2_MEGA_HIT/CORP_S011_rikunabi_next.md
SUCCESS/TIER2_MEGA_HIT/CORP_S014_carsensor.md
SUCCESS/TIER2_MEGA_HIT/CORP_S015_torabayu.md
SUCCESS/TIER3_SAAS/CORP_S005_airregi.md
SUCCESS/TIER3_SAAS/CORP_S012_airpay.md
SUCCESS/TIER3_SAAS/CORP_S016_air_reserve.md
SUCCESS/TIER5_NEW_BUSINESS/CORP_S003_studysapuri.md
SUCCESS/TIER5_NEW_BUSINESS/CORP_S018_studysapuri_teachers.md
SUCCESS/TIER5_NEW_BUSINESS/CORP_S020_zexy_enmusubi.md
SUCCESS/TIER5_NEW_BUSINESS/CORP_S024_rikunabi_haken.md
SUCCESS/TIER5_NEW_BUSINESS/CORP_S025_zexy_counter.md
```

**FAILURE (11件)**:
```
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F001_ponparemall.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F002_r25.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F004_nurseful.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F005_quipper_video.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F006_isize.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F008_abroad_print.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F012_recruit_book_print.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F013_shinagaku_book_print.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F014_townwork_sukima.md
FAILURE/TIER6_CLEAR_WITHDRAWAL/CORP_F015_keiko_to_manabu_full.md
FAILURE/TIER8_STRATEGIC_EXIT/CORP_F010_keiko_to_manabu.md
```

---

**作成者**: Claude Code
**次回更新予定**: Phase 1完了時
