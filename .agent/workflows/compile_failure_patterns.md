---
description: 既存事例から失敗情報を抽出し、failure_patterns.mdを自動生成・更新する
---

# /compile_failure_patterns ワークフロー

**バージョン**: 1.0  
**作成日**: 2025-12-26

---

## 概要

Solo_App/case_studies/ 配下の事例ファイルから失敗情報を抽出し、`failure_patterns.md`を生成・更新する。

## ファイルパス

```
BASE_PATH: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents

入力: {BASE_PATH}/01_App/case_studies/*.md
出力: {BASE_PATH}/01_App/data/failure_patterns.md
```

---

## 実行コマンド

```text
/compile_failure_patterns           # 全件再生成
/compile_failure_patterns --update  # 差分更新のみ
```

---

## ワークフローステップ

### STEP 1: 事例ファイル走査
// turbo
```text
処理:
  1. case_studies/ 内の全 .md ファイルをリスト
  2. 各ファイルの「失敗プロダクト一覧」セクションを検索

ツール: find_by_name, grep_search
対象パターン: "失敗プロダクト一覧" or "🌃 失敗プロダクト"
```

---

### STEP 2: 失敗データ抽出
// turbo
```text
処理:
  各事例ファイルから以下を抽出:
  
  | 抽出項目 | 元の場所 |
  |---------|---------|
  | 人物名 | ## 1. 基本情報 |
  | プロダクト名 | 失敗プロダクト一覧テーブル |
  | カテゴリ | 失敗プロダクト一覧テーブル |
  | 期間 | 失敗プロダクト一覧テーブル |
  | 失敗理由 | 失敗プロダクト一覧テーブル |
  | 学び | 失敗プロダクト一覧テーブル |
  | 総失敗数 | 「総失敗数」行 |
  | 暗黒期の長さ | 「暗黒期の長さ」行 |

ツール: view_file（セクション抽出）
```

---

### STEP 3: パターン分類
// turbo
```text
処理:
  失敗理由をパターンコード（P1〜P10）に分類

分類ルール:
  | キーワード | パターン |
  |-----------|---------|
  | 市場検証なし、ユーザー0、顧客0、長期開発 | P1 |
  | 収益化できず、バズ、購入ボタンなし | P2 |
  | コロナ、外部要因、景気 | P3 |
  | 物理、配送、在庫、EC | P4 |
  | ニッチ、市場規模 | P5 |
  | VC、資金調達 | P6 |
  | 競合、レッドオーシャン、飽和 | P7 |
  | 完璧主義、SOLID、アーキテクチャ | P8 |
  | CVR、リファンド、不満 | P9 |
  | 暗黒期、長期間 | P10 |
```

---

### STEP 4: 統計計算
// turbo
```text
処理:
  1. カテゴリ別失敗件数を集計
  2. パターン別件数を集計
  3. 人物別失敗/成功/成功率を計算
  4. リスク評価を判定:
     - 🔴高リスク: 5件以上 or 成功率10%未満
     - 🟡中リスク: 2-4件 or 成功率10-30%
     - 🟢低リスク: 1件以下 or 成功率30%以上
```

---

### STEP 5: DB生成/更新
// turbo
```text
処理:
  1. failure_pattern_format.md テンプレートを読み込み
  2. 抽出データを各セクションに当てはめ
  3. failure_patterns.md を生成または更新

ツール: write_to_file
```

---

### STEP 6: 差分レポート
// turbo
```text
出力:
  ## 更新レポート
  
  - 処理事例数: XX件
  - 抽出失敗事例数: XX件
  - 新規追加: XX件
  - パターン分類済み: XX件
  
  ### 新規追加失敗事例
  | 人物 | プロダクト | パターン |
  |------|----------|---------|
  ...
```

---

## --update オプション時の動作

```text
1. failure_patterns.md の「更新履歴」から最終更新日を取得
2. case_studies/ 内で最終更新日以降に更新されたファイルのみ処理
3. 既存DBに差分マージ
```

---

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| 「失敗プロダクト一覧」セクションがない | スキップ、ログに記録 |
| パターン分類できない | P10（その他）として記録 |
| ファイル読み込みエラー | スキップ、エラー報告 |

---

## 使用例

### 全件再生成
```text
/compile_failure_patterns
→ 全事例を走査してDBを再生成
```

### 差分更新
```text
/compile_failure_patterns --update
→ 新規追加事例のみを処理してDBに追加
```

### 特定事例のみ追加
```text
/compile_failure_patterns --file 005_brock_anderson.md
→ 指定ファイルのみを処理
```

---

## 依存関係

- `_templates/failure_pattern_format.md` - DBフォーマット定義
- `case_studies/*.md` - 事例ファイル（v3.0テンプレート推奨）
