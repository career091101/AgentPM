---
description: SNS調査を完全自動オーケストレーションし、残りの調査対象を順次処理する
---

# /orchestrate_sns ワークフロー

**バージョン**: 1.0  
**作成日**: 2025-12-26  
**参照**: `/research_sns_growth` ワークフロー（v3.3）

---

## 概要

SNS成長戦略調査を完全自動化するマスターオーケストレーター。
残りの調査対象を優先順位に従って自動処理します。

```text
┌─────────────────────────────────────────────────────────────────────┐
│  SNS Research Orchestration Flow v1.0                               │
├─────────────────────────────────────────────────────────────────────┤
│  STEP 0:  初期化・進捗確認                                          │
│           └─ sns_research_progress.md を読み込み                    │
│           └─ sns_targets_list.md から未調査対象を特定               │
│                                                                     │
│  STEP 1:  ✅ バッチ1-2 確認（完了済み）                             │
│           └─ Tier1 & Tier2前半: 計20件                              │
│                                                                     │
│  STEP 2:  🔄 バッチ3: Tier2後半（#21-30）                           │
│           └─ Yasser Elsaid, Roy, Daniel Bitton 等                   │
│                                                                     │
│  STEP 3:  📈 バッチ4-8: Tier3（#31-60）                             │
│           └─ 5件/バッチ × 6バッチ                                   │
│                                                                     │
│  STEP 4:  📚 バッチ9-15: Tier4（#61-94）                            │
│           └─ 5件/バッチ × 7バッチ                                   │
│                                                                     │
│  STEP 5:  🌟 バッチ16-37: SNS特化成功者（#95-200）                  │
│           └─ 5件/バッチ × 22バッチ                                  │
│                                                                     │
│  STEP 6:  完了レポート生成                                          │
│           └─ sns_research_completion.md                             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 前提条件

**ファイルパス（絶対パス）**:

```text
BASE_PATH: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research

進捗ファイル: {BASE_PATH}/documents/03_SNS/sns_research_progress.md
対象リスト: {BASE_PATH}/documents/03_SNS/sns_targets_list.md
事例出力先: {BASE_PATH}/documents/03_SNS/case_studies/
ワークフロー: /Users/yuichi/AIPM/aipm_v0/.agent/workflows/research_sns_growth.md
```

---

## 実行モード

```bash
/orchestrate_sns                    # 全体実行（中断pointから再開）
/orchestrate_sns 進捗確認           # 現在の進捗を表示
/orchestrate_sns 次の1バッチ        # 次の5件のみ処理
/orchestrate_sns 次の1件            # 次の1件のみ処理
/orchestrate_sns Tier2のみ          # Tier2のみ処理
/orchestrate_sns Tier3のみ          # Tier3のみ処理
/orchestrate_sns Tier4のみ          # Tier4のみ処理
/orchestrate_sns SNS特化のみ        # #95-200のみ処理
```

---

## 実行手順

### STEP 0: 初期化・進捗確認

// turbo
```text
ツール: view_file
入力: 
  1. sns_research_progress.md
  2. sns_targets_list.md

処理:
  1. 進捗ファイルを読み込み
  2. Tier別の未調査件数をカウント
  3. case_studies/ フォルダ内の既存レポートを確認
  4. 推定完了時間を計算（25分/件）
  5. 進捗サマリーを表示
```

**出力例**:
```text
=== SNS Research Progress ===
✅ バッチ1 (Tier1 #1-10):     9/10 完了 (1件スキップ)
✅ バッチ2 (Tier2前半 #11-20): 7/10 完了 (3件スキップ)
🔄 バッチ3 (Tier2後半 #21-30): 0/10 完了 (残り10件, 約4時間)
🔲 バッチ4-8 (Tier3 #31-60):  0/30 完了 (残り30件, 約12.5時間)
🔲 バッチ9-15 (Tier4 #61-94): 0/34 完了 (残り34件, 約14時間)
🔲 バッチ16-37 (SNS特化 #95-200): 0/106 完了 (残り106件, 約44時間)
----------------------------------------
総計: 16/200 完了 (8%)
推定残り時間: 約75時間
次の調査対象: #21 Yasser Elsaid
```

---

### STEP 1: バッチ1-2 確認（完了済み）

// turbo
```text
対象: Tier1 (#1-10) + Tier2前半 (#11-20)
ステータス: ✅ 完了済み

確認項目:
  1. 各レポートがv3.3準拠であることを確認
  2. 行数200行以上
  3. 必須13セクション充足
  4. ファクトチェックPASS

完了済みレポート (17件):
  - Pieter Levels, Marc Lou, Zach Yadegari
  - Romain Torres, Tony Dinh, Danny Postma
  - ウマたん, Wesley Tian, Anton Osika
  - Max Artemov, Connor, Nico Jeannen
  - Tibo Louis-Lucas, Steven Cravotta
  - Blake Anderson, Alex Finn

スキップ済み (3件):
  - Brock氏, Marko氏, David Bressler氏, David Park氏
```

---

### STEP 2: バッチ3 - Tier2後半調査（#21-30）

// turbo-mandatory
```text
対象（10件）:
  #21. Yasser Elsaid（年6億）
  #22. Roy氏（21歳・36日で月1600万）
  #23. Daniel Bitton（17歳・月9000万）
  #24. Bhanu Teja氏（インド・月1500万）
  #25. Sumit Kumar氏（月1500万）
  #26. Damon Chen氏（月2000万）
  #27. John Rush氏（年3億）
  #28. Ping氏（月3800万）
  #29. Yong-Soo Chung氏（年30億）
  #30. Guillaume氏（200億価値）

各調査の実行フロー:
  1. 対象者を特定（sns_targets_list.mdから情報取得）
  2. /research_sns_growth を実行
     - Web検索: "[名前] twitter indie hacker revenue"
     - ブラウザ確認: Twitterプロフィール
     - 詳細調査: 収益、失敗プロダクト、成長戦略
  3. v3.3品質チェック（200行以上、13セクション）
  4. ファクトチェック実施
  5. case_studies/[名前]/sns_analysis.md として保存
  6. sns_research_progress.md を更新
  7. 次の対象へ

完了条件: Tier2後半10件すべて完了
推定時間: 4時間
```

---

### STEP 3: バッチ4-8 - Tier3調査（#31-60）

// turbo-mandatory
```text
対象: Tier3 成長ポテンシャル層（30件）

バッチ構成:
  - Batch 4: #31-35 (5件)
  - Batch 5: #36-40 (5件)
  - Batch 6: #41-45 (5件)
  - Batch 7: #46-50 (5件)
  - Batch 8: #51-55 (5件)
  - Batch 9: #56-60 (5件)

各バッチ実行フロー:
  1. sns_targets_list.mdから🔲ステータスの対象を5件特定
  2. /research_sns_growth を順次実行
  3. v3.3品質チェック
  4. 不足があれば自動再調査
  5. sns_research_progress.md を更新
  6. 次のバッチへ

完了条件: Tier3 30件すべて完了
推定時間: 12.5時間
```

---

### STEP 4: バッチ9-15 - Tier4調査（#61-94）

// turbo-mandatory
```text
対象: Tier4 参考層（34件）

バッチ構成:
  - Batch 10-16: 5件 × 7バッチ = 35件（34件+予備）

各バッチ実行フロー:
  1. 🔲ステータスの対象を5件特定
  2. /research_sns_growth を順次実行
  3. v3.3品質チェック
  4. sns_research_progress.md を更新
  5. 次のバッチへ

完了条件: Tier4 34件すべて完了
推定時間: 14時間
```

---

### STEP 5: バッチ16-37 - SNS特化成功者調査（#95-200）

// turbo-mandatory
```text
対象: SNS特化成功者（106件）
  - Twitter/X 特化: #95-102 (8件)
  - TikTok 特化: #103-108 (6件)
  - Instagram/マルチ: #109-114 (6件)
  - LinkedIn 特化: #115-129 (15件)
  - クリエイターエコノミー: #130-140 (11件)
  - Facebook: #141-144 (4件)
  - YouTube: #145-150 (6件)
  - Podcast/Newsletter: #151-160 (10件)
  - 日本/アジア: #161-164 (4件)
  - Eコマース: #165-168 (4件)
  - SaaS: #169-174 (6件)
  - 教育/コーチング: #175-180 (6件)
  - Indie Hacker: #181-190 (10件)
  - 追加枠: #191-200 (10件)

バッチ構成:
  - Batch 17-38: 5件 × 22バッチ = 110件（106件+予備）

各バッチ実行フロー:
  1. 🔲ステータスの対象を5件特定
  2. /research_sns_growth を順次実行
  3. v3.3品質チェック
  4. sns_research_progress.md を更新
  5. 次のバッチへ

完了条件: SNS特化成功者106件すべて完了
推定時間: 44時間
```

---

### STEP 6: 完了レポート生成

// turbo
```text
ツール: write_to_file
出力: {BASE_PATH}/documents/03_SNS/sns_research_completion.md

レポート内容:
  - 調査完了日時
  - Tier別統計
  - SNS活用タイプ別分析
  - 成功パターンTop 10
  - 日本市場適用性Top 20
  - 次のアクション推奨
```

**レポートテンプレート**:
```markdown
# SNS成長戦略調査完了レポート

**完了日時**: [日時]
**所要時間**: [時間]
**バージョン**: v1.0

## 調査統計

| カテゴリ | 完了数 | 成功率 |
|---------|--------|--------|
| Tier1 最優先 | 9/10 | 90% |
| Tier2 高優先 | 17/20 | 85% |
| Tier3 優先 | 30/30 | 100% |
| Tier4 参考 | 34/34 | 100% |
| SNS特化成功者 | 106/106 | 100% |
| **合計** | **196/200** | **98%** |

## SNS活用タイプ別分析

| タイプ | 件数 | 平均収益 | 代表事例 |
|--------|------|---------|---------|
| Twitter型 | 62件 | $XXK | Pieter Levels |
| TikTok型 | 18件 | $XXK | Steven Cravotta |
| Instagram型 | 10件 | $XXK | - |
| LinkedIn型 | 18件 | $XXK | Justin Welsh |
| マルチ型 | 46件 | $XXK | - |

## 成功パターンTop 10

1. **Build in Public**: [件数]件
2. **TikTokマーケティング**: [件数]件
3. **ポートフォリオ戦略**: [件数]件
4. **AI×早期参入**: [件数]件
5. **プログラマティックSEO**: [件数]件
...

## 日本市場適用性Top 20

| # | 人物名 | 適用性スコア | 主要戦略 |
|---|--------|-------------|---------|
| 1 | ウマたん | 5.0/5 | 教育×マルチチャネル |
| 2 | [名前] | X.X/5 | [戦略] |
...

## 次のアクション

1. [ ] 高適用性事例を基にSNS戦略を設計
2. [ ] 成功パターンのフレームワーク化
3. [ ] /plan_solo_marketing 実行
4. [ ] /create_sns_content でコンテンツ作成
```

---

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| Xアカウントが見つからない | Web検索 → 代替ソースで調査 |
| フォロワー数乖離20%超 | 再調査（最大2回）→ 修正 |
| 品質基準未達（200行未満） | 自動再調査トリガー |
| 必須セクション欠落 | 自動再調査トリガー |
| 3回リトライ失敗 | 「⚠️要確認」フラグを付けて次へ |
| ブラウザ接続タイムアウト | 5秒待機後リトライ（最大3回） |

---

## 中断・再開機能

オーケストレーションは中断しても再開可能：

1. **進捗の永続化**: 各調査完了時に `sns_research_progress.md` を更新
2. **再開時の動作**: 🔲ステータスの対象から自動的に継続
3. **手動中断**: ユーザーが停止した場合、次回は中断地点から再開

---

## v3.3準拠チェック（自動実行）

各調査完了時に以下を自動チェック:

```python
必須セクション（13個）:
  1. 📋 基本情報
  2. 📱 SNSプレゼンス
  3. 💰 収益情報
  4. 📈 成長曲線分析
  5. ❌ 失敗プロダクト詳細
  6. 🔥 バズ投稿TOP5
  7. 🎯 成長戦略パターン
  8. 💸 収益化導線
  9. 🇯🇵 日本市場適用性評価
  10. ✅ ファクトチェック結果
  11. 📚 情報源リスト
  12. 🔄 修正履歴
  13. 💡 自身のSNS戦略への示唆

行数チェック:
  - 200行以上: ✅ PASS
  - 200行未満: ⚠️ WARN → セクション充足なら続行
  - 13セクション未満: ❌ FAIL → 再調査必須
```

---

## Human-in-the-Loop ポイント

以下の状況では**確認を求める**：

| ポイント | 条件 | 選択肢 |
|---------|------|--------|
| バッチ完了時 | 5件調査完了後 | 継続 / 一時停止 / 中止 |
| Tier完了時 | 各Tier終了後 | 継続 / レビュー要求 |
| 大量エラー発生 | 1バッチで3件以上失敗 | リトライ / スキップ / 中止 |
| 50%完了時 | 中間チェックポイント | 継続 / レビュー要求 |
| SNS特化調査前 | 大量調査の確認 | 実行 / スキップ |

---

## 変更履歴

| バージョン | 日付 | 変更内容 |
|-----------|------|---------|
| v1.0 | 2025-12-26 | 初版作成 |

---

## 実行コマンド

このワークフロー全体を開始するには：
```
/orchestrate_sns
```

個別Tierのみ実行する場合：
```
/orchestrate_sns Tier2のみ
/orchestrate_sns Tier3のみ
/orchestrate_sns SNS特化のみ
```

進捗確認のみ：
```
/orchestrate_sns 進捗確認
```

次の1件のみ：
```
/orchestrate_sns 次の1件
```

次の1バッチ（5件）のみ：
```
/orchestrate_sns 次の1バッチ
```
