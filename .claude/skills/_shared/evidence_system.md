# Evidence Recording System - 証拠記録システム

レビューループにおける証拠記録の標準仕様。

**最終更新**: 2026-01-02
**バージョン**: 1.0（Week 4）

---

## 概要

Manager Skill → SubAgent → Review Agent → Integration のループ全体で生成される成果物を体系的に記録し、後からトレーサビリティを確保するための証拠記録システム。

**目的**:
- イテレーションごとの成果物の完全保存
- レビュー結果の可視化とトレーサビリティ
- リプラン判断の根拠記録
- Human-in-the-Loop時の情報提供

---

## ディレクトリ構造

```
Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/
├── iteration_001/
│   ├── task_breakdown.md              # タスク分解結果
│   ├── subagent_001_output.md         # SubAgent 1の出力ドキュメント
│   ├── subagent_002_output.md         # SubAgent 2の出力ドキュメント
│   ├── subagent_003_output.md         # SubAgent 3の出力ドキュメント
│   ├── quality_score_001.json         # 品質スコア（全タスク統合）
│   ├── review_report_001.md           # レビューレポート
│   └── decision_001.md                # 統合/リプラン判定記録
│
├── iteration_002/                     # リプラン後の2回目
│   ├── replan_analysis.md             # リプラン分析レポート
│   ├── task_breakdown_updated.md      # 更新されたタスク分解
│   ├── subagent_001_output.md         # SubAgent 1の修正版
│   ├── quality_score_002.json         # 品質スコア（修正版）
│   ├── review_report_002.md           # レビューレポート（修正版）
│   └── decision_002.md                # 統合/リプラン判定記録
│
├── iteration_003/                     # 3回目（必要に応じて）
│   └── ...
│
└── final_summary.md                   # 最終サマリー
```

### パス規則

- **ルートパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/`
- **イテレーションフォルダ**: `iteration_{NNN}/`（001から3桁ゼロパディング）
- **SubAgent出力**: `subagent_{NNN}_output.md`（タスクIDに対応）
- **品質スコア**: `quality_score_{NNN}.json`（イテレーション番号）
- **レビューレポート**: `review_report_{NNN}.md`（イテレーション番号）

---

## ファイル形式定義

### 1. task_breakdown.md

Manager Skillによるタスク分解結果の記録。

```markdown
# Task Breakdown - Iteration {N}

**作成日時**: 2026-01-02 14:00:00
**Manager**: orchestrate-review-loop

## タスク一覧

### Task 001: CPF判定レポート作成
- **説明**: 顧客セグメント、課題、解決策を含むCPF検証レポート作成
- **ドキュメントタイプ**: cpf_judgment
- **出力ファイル**: Flow/202601/2026-01-02/cpf_judgment.md
- **依存関係**: なし
- **並列グループ**: 1
- **品質閾値**: 70点

### Task 002: リーンキャンバス作成
- **説明**: CPF判定を元にリーンキャンバスを作成
- **ドキュメントタイプ**: lean_canvas
- **出力ファイル**: Flow/202601/2026-01-02/lean_canvas.md
- **依存関係**: Task 001
- **並列グループ**: 2
- **品質閾値**: 70点

## 必須セクション定義

### cpf_judgment
- 顧客セグメント
- 課題
- 解決策
- 独自の価値提案
- 不公正な優位性
- 主要指標
- チャネル
- コスト構造
- 収益の流れ
- CPFスコア

### lean_canvas
- 課題
- ソリューション
- 独自の価値提案
- 圧倒的な優位性
- 顧客セグメント
- 既存の代替品
- チャネル
- 収益の流れ
- コスト構造
- 主要指標
```

### 2. subagent_{NNN}_output.md

SubAgentが生成したドキュメント（そのままコピー）。

```markdown
# CPF判定レポート

## 顧客セグメント
[SubAgentが生成した内容]

## 課題
[SubAgentが生成した内容]

...
```

**注意**:
- SubAgentの出力をそのまま保存（編集しない）
- ファイル名はタスクIDと対応（subagent_001 = Task 001）

### 3. quality_score_{NNN}.json

Review Agentによる品質スコアの記録。

```json
{
  "iteration": 1,
  "timestamp": "2026-01-02T15:30:00",
  "total_score": 74,
  "threshold": 70,
  "passed": true,
  "breakdown": {
    "completeness": {
      "score": 20,
      "max": 25,
      "weight": 0.25,
      "percentage": 80
    },
    "logic": {
      "score": 18,
      "max": 25,
      "weight": 0.25,
      "percentage": 72
    },
    "specificity": {
      "score": 14,
      "max": 20,
      "weight": 0.20,
      "percentage": 70
    },
    "evidence": {
      "score": 10,
      "max": 15,
      "weight": 0.15,
      "percentage": 67
    },
    "framework_compliance": {
      "score": 12,
      "max": 15,
      "weight": 0.15,
      "percentage": 80
    }
  },
  "issues": [
    {
      "category": "completeness",
      "severity": "warning",
      "message": "未実装セクション: 不公正な優位性"
    },
    {
      "category": "evidence",
      "severity": "error",
      "message": "市場規模の出典が不明"
    }
  ],
  "document_path": "Flow/202601/2026-01-02/cpf_judgment.md",
  "document_type": "cpf_judgment"
}
```

**フィールド説明**:
- `iteration`: イテレーション番号
- `timestamp`: レビュー実行日時
- `total_score`: 総合スコア（0-100点）
- `threshold`: 合格閾値
- `passed`: 合格判定（true/false）
- `breakdown`: 5観点の詳細スコア
- `issues`: 問題点リスト
- `document_path`: 評価対象ドキュメントのパス
- `document_type`: ドキュメントタイプ

### 4. review_report_{NNN}.md

Review Agentによるレビューレポート（人間可読形式）。

```markdown
# Review Report - Iteration 1

**ドキュメント**: cpf_judgment.md
**タイムスタンプ**: 2026-01-02 15:30:00

## 品質スコア

| 項目 | スコア | 満点 | 達成率 |
|------|--------|------|--------|
| 完全性 | 20 | 25 | 80% |
| 論理性 | 18 | 25 | 72% |
| 具体性 | 14 | 20 | 70% |
| エビデンス | 10 | 15 | 67% |
| フレームワーク準拠性 | 12 | 15 | 80% |
| **合計** | **74** | **100** | **74%** |

**判定**: ✅ 合格（74点 ≥ 70点）

## 完全性チェック

**検出セクション**: 9/10件（90%）
**未実装セクション**: 1件
- 不公正な優位性

## 論理性チェック

**一貫性**: ✅ PASS
**因果関係**: ✅ PASS
**結論**: ⚠️ WARNING

**問題点**:
- CPFスコアの根拠が不明確

## 具体性チェック

**数値データ**: ✅ PASS
**固有名詞**: ✅ PASS
**事例**: ❌ FAIL

**抽象的な表現**:
- 「多くのユーザー」→ 具体的な数値なし
- 「優れたUX」→ 具体的な説明なし

## エビデンスチェック

**データ裏付け**: ⚠️ WARNING
**出典引用**: ❌ FAIL
**定量データ**: ✅ PASS

**エビデンス不足**:
- 市場規模の出典が不明
- 競合分析のデータソースが不明

## フレームワーク準拠性チェック

**CPF準拠**: ✅ PASS
**PSF準拠**: ⚠️ WARNING
**PMF準拠**: N/A

**改善点**:
- PSF: 技術的実現可能性の評価が不十分

## 次のアクション

✅ 統合完了（品質スコア70点以上）

**推奨改善**:
1. 「不公正な優位性」セクションを追加
2. 市場規模の出典を明記（総務省、McKinsey等）
3. 抽象的な表現を具体的な数値に置き換え
```

### 5. decision_{NNN}.md

統合またはリプランの判定記録。

```markdown
# Decision Record - Iteration 1

**判定日時**: 2026-01-02 15:35:00
**判定者**: Manager Skill (orchestrate-review-loop)

## 判定結果

**決定**: 統合完了（Integration）

**理由**:
- 品質スコア 74点 ≥ 閾値 70点
- すべての必須セクションが存在（90%以上）
- 論理的整合性に重大な矛盾なし

## 次のアクション

1. cpf_judgment.mdをStockフォルダに移動
2. final_summary.mdを生成
3. レビューループ完了

## 推奨改善（オプショナル）

- 「不公正な優位性」セクションを追加
- 市場規模の出典を明記
- 抽象的な表現を具体的な数値に置き換え

**補足**: 推奨改善は次回のイテレーションで反映可能（今回は統合完了）
```

**リプラン判定の場合**:

```markdown
# Decision Record - Iteration 1

**判定日時**: 2026-01-02 15:35:00
**判定者**: Manager Skill (orchestrate-review-loop)

## 判定結果

**決定**: リプラン必須（Replan Required）

**理由**:
- 品質スコア 56点 < 閾値 70点
- 論理性スコア 12点 < 15点（論理的矛盾あり）
- エビデンススコア 6点 < 9点（エビデンス不足）

## 問題分析

### Pattern 2: 論理的矛盾
**問題箇所**: CPFスコア算出ロジック
**矛盾内容**: 「市場規模が小さい」と言いながら「急成長市場」と主張
**修正指示**: 市場規模の定義を明確化し、成長率との関係を整理

### Pattern 4: エビデンス不足
**問題箇所**: 市場規模推定セクション
**不足内容**: 出典・データソースの明記なし
**修正指示**: 総務省調査、McKinsey Report等の公的データを引用

## 次のアクション

1. Iteration 2を開始
2. SubAgentに修正指示を追加
3. タスク分解を更新（task_breakdown_updated.md）

## 修正タスク

### Task 001（修正版）
**追加指示**:
- 市場規模の定義を明確化（TAM/SAM/SOMの区別）
- 総務省「情報通信白書2024」からデータを引用
- 成長率と市場規模の関係を論理的に説明

### Task 002（修正版）
**追加指示**:
- CPFスコアの算出根拠を明記
- 各項目の評価基準を具体化
```

### 6. replan_analysis.md

リプラン分析レポート（Iteration 2以降）。

```markdown
# Replan Analysis - Iteration 2

**分析日時**: 2026-01-02 15:40:00
**前回イテレーション**: Iteration 1

## 前回の問題点

### 1. 論理的矛盾（logic_score: 12/25）
**問題箇所**: CPFスコア算出ロジック
**矛盾内容**: 「市場規模が小さい」と言いながら「急成長市場」と主張

**修正方針**:
- 市場規模の定義を明確化（TAM/SAM/SOMの区別）
- 成長率と市場規模の関係を論理的に説明

### 2. エビデンス不足（evidence_score: 6/15）
**問題箇所**: 市場規模推定セクション
**不足内容**: 出典・データソースの明記なし

**修正方針**:
- 総務省「情報通信白書2024」からデータを引用
- McKinsey Global Report等の権威あるソースを追加

## SubAgentへの追加指示

### Task 001: CPF判定レポート作成（修正版）
**基本指示**: （変更なし）
**追加指示**:
1. 市場規模の定義を明確化（TAM/SAM/SOMの区別）
2. 総務省「情報通信白書2024」からデータを引用
3. 成長率と市場規模の関係を論理的に説明
4. CPFスコアの算出根拠を明記（各項目の評価基準を具体化）

## 期待される改善

| 項目 | Iteration 1 | 目標（Iteration 2） |
|------|-------------|-------------------|
| 論理性スコア | 12点 | 20点以上 |
| エビデンススコア | 6点 | 12点以上 |
| 総合スコア | 56点 | 70点以上 |
```

### 7. final_summary.md

レビューループ完了時の最終サマリー。

```markdown
# Final Summary - Review Loop Completed

**完了日時**: 2026-01-02 16:00:00
**タスク**: CPF判定レポート作成、リーンキャンバス作成
**総イテレーション数**: 2回

## 成果物

| ドキュメント | 最終スコア | 判定 | 保存先 |
|------------|-----------|------|--------|
| cpf_judgment.md | 74点 | ✅ 合格 | Stock/programs/.../documents/1_initiating/ |
| lean_canvas.md | 82点 | ✅ 合格 | Stock/programs/.../documents/2_discovery/ |

## イテレーション履歴

### Iteration 1
- **実行時間**: 25分
- **結果**: 不合格（56点 < 70点）
- **主な問題**: 論理的矛盾、エビデンス不足
- **対応**: リプラン実施

### Iteration 2
- **実行時間**: 30分
- **結果**: 合格（74点 ≥ 70点）
- **改善点**: 市場規模データ追加、論理的整合性確保

## 品質スコア推移

```
Iteration 1: 56点 → Iteration 2: 74点（+18点改善）
```

| 項目 | Iter 1 | Iter 2 | 改善 |
|------|--------|--------|------|
| 完全性 | 18点 | 20点 | +2 |
| 論理性 | 12点 | 18点 | +6 |
| 具体性 | 10点 | 14点 | +4 |
| エビデンス | 6点 | 10点 | +4 |
| フレームワーク準拠性 | 10点 | 12点 | +2 |

## 主要な学び

1. **市場規模の定義**: TAM/SAM/SOMの区別が重要
2. **エビデンスの重要性**: 公的データソースの引用が信頼性を向上
3. **論理的整合性**: 矛盾する主張を避けるための慎重な記述

## 証拠記録

- **イテレーション1**: `iteration_001/`
- **イテレーション2**: `iteration_002/`

## 次のアクション

1. cpf_judgment.mdとlean_canvas.mdをStockフォルダに移動
2. プロジェクト憲章を更新（CPF検証完了を記録）
3. 次フェーズ（PSF検証）の準備
```

---

## 証拠記録の生成タイミング

| ファイル | 生成者 | タイミング |
|---------|--------|-----------|
| `task_breakdown.md` | Manager Skill | タスク分解完了時 |
| `subagent_{NNN}_output.md` | Manager Skill | SubAgent完了時（出力をコピー） |
| `quality_score_{NNN}.json` | Review Agent | レビュー完了時 |
| `review_report_{NNN}.md` | Review Agent | レビュー完了時 |
| `decision_{NNN}.md` | Manager Skill | 統合/リプラン判定時 |
| `replan_analysis.md` | Manager Skill | リプラン判定時（Iteration 2以降） |
| `task_breakdown_updated.md` | Manager Skill | リプラン時（タスク更新） |
| `final_summary.md` | Manager Skill | レビューループ完了時 |

---

## ファイル命名規則

### ゼロパディング
- イテレーション番号: 3桁（`001`, `002`, `003`）
- タスクID: 3桁（`001`, `002`, `003`）

### タイムスタンプ形式
```
YYYY-MM-DD HH:MM:SS
例: 2026-01-02 15:30:00
```

### JSON日時形式
```
ISO 8601形式: YYYY-MM-DDTHH:MM:SS
例: 2026-01-02T15:30:00
```

---

## 証拠記録の活用

### トレーサビリティ
- どのイテレーションで何を修正したかを追跡
- 品質スコアの推移を可視化
- リプラン判断の根拠を記録

### デバッグ
- SubAgentの出力を確認
- Review Agentの評価ロジックを検証
- Manager Skillの判定ロジックを分析

### Human-in-the-Loop
- 3回失敗時にすべての証拠を提示
- ユーザーが問題箇所を特定しやすくする
- 手動修正の指針を提供

### 学習データ
- 成功パターンの抽出
- 失敗パターンの分析
- フィードバックループの改善

---

## 保存期間

- **Flowフォルダ**: 作業中は保持（最大3ヶ月）
- **Archivedフォルダ**: プロジェクト完了後に移動（長期保存）

---

## 関連ドキュメント

- **Review Agent**: `.claude/agents/review-agent.md`
- **Manager Skill**: `.claude/skills/orchestrate-review-loop/SKILL.md`
- **品質基準**: `.claude/skills/_shared/review_criteria.md`
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`
