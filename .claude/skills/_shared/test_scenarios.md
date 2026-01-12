# Test Scenarios - レビューループ統合テスト

レビューループシステムの統合テストとエンドツーエンドテストシナリオ。

**最終更新**: 2026-01-02
**バージョン**: 1.0（Week 7）

---

## 概要

レビューループシステムの動作を検証するための包括的なテストシナリオとテストケースを定義します。

**テスト対象**:
- Manager Skill → SubAgent → Review Agent → Integration の完全フロー
- リトライループ（最大3回）
- 証拠記録システム
- エラーハンドリング
- Human-in-the-Loop発動

---

## テスト環境

### 前提条件

- Claude Code環境が正常に動作している
- `.claude/skills/orchestrate-review-loop/SKILL.md` が存在する
- `.claude/agents/review-agent.md` が存在する
- `.claude/skills/_shared/review_criteria.md` が存在する
- `.claude/skills/_shared/replan_patterns.md` が存在する
- `.claude/skills/_shared/evidence_system.md` が存在する

### テストデータ

テスト用のサンプルドキュメントを `tests/fixtures/` に配置：

```
tests/fixtures/
├── requirements_simple.md         # シンプルな要件（1回で成功）
├── requirements_moderate.md       # 中程度の要件（2回で成功）
├── requirements_complex.md        # 複雑な要件（3回必要または失敗）
├── sample_cpf_judgment_good.md    # 高品質サンプル（80点以上）
├── sample_cpf_judgment_medium.md  # 中品質サンプル（60-70点）
└── sample_cpf_judgment_bad.md     # 低品質サンプル（60点未満）
```

---

## テストシナリオ一覧

### シナリオ1: 1回で成功（最も理想的なケース）

**目的**: 全タスクが初回で品質スコア70点以上を達成し、統合完了

**入力**:
- 要件: `requirements_simple.md`
- 期待タスク数: 1タスク（CPF判定レポート作成）

**期待される動作**:
1. **Iteration 1**:
   - タスク分解: T001（CPF判定レポート作成）
   - SubAgent実行: cpf_judgment.md生成
   - Review Agent: 品質スコア 75点
   - 判定: ✅ 合格（75点 ≥ 70点）
   - 統合完了

**期待される成果物**:
```
Flow/202601/2026-01-02/
├── cpf_judgment.md
└── review_loop_evidence/
    ├── iteration_001/
    │   ├── task_breakdown.md
    │   ├── subagent_001_output.md
    │   ├── quality_score_001.json
    │   ├── review_report_001.md
    │   └── decision_001.md
    └── final_summary.md
```

**検証項目**:
- [ ] task_breakdown.mdが存在する
- [ ] subagent_001_output.mdがcpf_judgment.mdと同一内容
- [ ] quality_score_001.jsonのtotal_scoreが75点
- [ ] review_report_001.mdに✅合格の判定が記載
- [ ] decision_001.mdに「統合完了」が記載
- [ ] final_summary.mdに総イテレーション数1回が記載

**実行時間**: 約20分（1タスク×20分）

---

### シナリオ2: 2回で成功（リプラン1回）

**目的**: Iteration 1で不合格、リプラン後のIteration 2で合格

**入力**:
- 要件: `requirements_moderate.md`
- 期待タスク数: 2タスク（CPF判定、リーンキャンバス）

**期待される動作**:
1. **Iteration 1**:
   - SubAgent実行: 2ドキュメント生成
   - Review Agent: T001は58点、T002は72点
   - 判定: ❌ 不合格（T001が70点未満）
   - リプラン: Pattern 4（エビデンス不足）を検出

2. **Iteration 2**:
   - リプラン分析: 市場規模の出典追加を指示
   - SubAgent再実行: T001のみ修正版生成
   - Review Agent: T001は74点、T002は72点（変更なし）
   - 判定: ✅ 合格（両方70点以上）
   - 統合完了

**期待される成果物**:
```
Flow/202601/2026-01-02/
├── cpf_judgment.md
├── lean_canvas.md
└── review_loop_evidence/
    ├── iteration_001/
    │   ├── task_breakdown.md
    │   ├── subagent_001_output.md
    │   ├── subagent_002_output.md
    │   ├── quality_score_001.json
    │   ├── review_report_001.md
    │   └── decision_001.md
    ├── iteration_002/
    │   ├── replan_analysis.md
    │   ├── task_breakdown_updated.md
    │   ├── subagent_001_output.md（修正版）
    │   ├── quality_score_002.json
    │   ├── review_report_002.md
    │   └── decision_002.md
    └── final_summary.md
```

**検証項目**:
- [ ] iteration_001/decision_001.mdに「リプラン必須」が記載
- [ ] iteration_002/replan_analysis.mdに「Pattern 4: エビデンス不足」が記載
- [ ] iteration_002/quality_score_002.jsonのtotal_scoreが74点
- [ ] final_summary.mdにイテレーション数2回、スコア改善（58→74点）が記載

**実行時間**: 約40分（2イテレーション×20分）

---

### シナリオ3: 3回で成功（リプラン2回）

**目的**: Iteration 1, 2で不合格、Iteration 3で合格

**入力**:
- 要件: `requirements_complex.md`
- 期待タスク数: 3タスク（CPF判定、リーンキャンバス、ピッチデッキ）

**期待される動作**:
1. **Iteration 1**: T001が52点、T002が68点、T003が71点 → 不合格
2. **Iteration 2**: T001が62点、T002が69点、T003が71点 → 不合格（改善不十分）
3. **Iteration 3**: T001が73点、T002が72点、T003が71点 → 合格

**期待される成果物**:
- iteration_001, iteration_002, iteration_003のすべてのフォルダ
- final_summary.mdにイテレーション数3回、各イテレーションのスコア推移が記載

**検証項目**:
- [ ] 3つのイテレーションフォルダが存在
- [ ] final_summary.mdに品質スコア推移テーブルが記載（52→62→73点）
- [ ] replan_analysis.mdが2つ存在（iteration_002, iteration_003）

**実行時間**: 約60分（3イテレーション×20分）

---

### シナリオ4: 3回失敗 → Human-in-the-Loop

**目的**: 3回リトライしても70点未満、Human-in-the-Loop発動

**入力**:
- 要件: `requirements_very_complex.md`
- 期待タスク数: 1タスク（CPF判定レポート作成）

**期待される動作**:
1. **Iteration 1**: 品質スコア 48点 → 不合格
2. **Iteration 2**: 品質スコア 55点 → 不合格（改善+7点）
3. **Iteration 3**: 品質スコア 62点 → 不合格（改善+7点だが70点未満）
4. **Human-in-the-Loop発動**

**期待される成果物**:
```
Flow/202601/2026-01-02/
└── review_loop_evidence/
    ├── iteration_001/
    ├── iteration_002/
    ├── iteration_003/
    └── failure_report.md  # Human-in-the-Loop発動時に生成
```

**検証項目**:
- [ ] failure_report.mdが存在
- [ ] failure_report.mdに「3回のイテレーション後も品質スコア70点以上を達成できませんでした」が記載
- [ ] failure_report.mdにイテレーション履歴（48→55→62点）が記載
- [ ] 推奨アクション（手動修正、要件見直し、中断）が記載

**実行時間**: 約60分（3イテレーション×20分）

---

### シナリオ5: 複数タスク並列実行

**目的**: 3タスクを並列実行し、証拠記録が正しく生成されることを確認

**入力**:
- 要件: `requirements_parallel.md`
- 期待タスク数: 3タスク（すべて並列グループ1）

**期待される動作**:
1. **Iteration 1**:
   - タスク分解: T001, T002, T003（すべて並列グループ1）
   - SubAgent並列実行: 3タスク同時起動
   - Review Agent: 3タスク順次レビュー
   - 判定: すべて70点以上 → 統合完了

**期待される成果物**:
- subagent_001_output.md, subagent_002_output.md, subagent_003_output.md
- 3つのドキュメントが並列生成されている

**検証項目**:
- [ ] 3つのsubagent出力が証拠記録に保存されている
- [ ] task_breakdown.mdに3タスクがparallel_group: 1で記載
- [ ] final_summary.mdに3つのドキュメントの最終スコアが記載

**実行時間**: 約20分（並列実行のため、最遅タスク1つ分の時間）

---

### シナリオ6: タイムアウト処理

**目的**: SubAgentが30分以内に完了しない場合のタイムアウト処理を検証

**入力**:
- 要件: `requirements_timeout.md`（意図的に複雑な要件）
- タイムアウト設定: 5分（テスト用に短縮）

**期待される動作**:
1. **Iteration 1**:
   - SubAgent実行: 5分経過
   - タイムアウト検出
   - Human-in-the-Loop発動

**期待される成果物**:
- error_log.json（タイムアウトエラー記録）
- failure_report.md

**検証項目**:
- [ ] error_log.jsonに「TimeoutError」が記載
- [ ] failure_report.mdに「SubAgent実行タイムアウト」が記載

**実行時間**: 約5分（タイムアウト時間）

---

### シナリオ7: Review Agentエラー処理

**目的**: Review Agentがエラーで停止した場合のエラーハンドリングを検証

**モック方法**: Review Agentのプロンプトに意図的にエラーを発生させる指示を含める

**期待される動作**:
1. **Iteration 1**:
   - SubAgent実行: 正常完了
   - Review Agent実行: エラー発生
   - エラー検出
   - Human-in-the-Loop発動

**期待される成果物**:
- error_log.json（Review Agentエラー記録）
- failure_report.md

**検証項目**:
- [ ] error_log.jsonに「Review Agent実行エラー」が記載
- [ ] failure_report.mdに「Review Agentエラー」が記載

**実行時間**: 約15分（SubAgent実行 + Review Agentエラー検出）

---

## エンドツーエンドテストシナリオ

### E2Eシナリオ1: 実際のプロジェクトでの完全フロー

**目的**: 実際のプロジェクト要件を使用して、レビューループ全体を実行

**入力**:
- 要件: 実際のプロジェクト要件ファイル
- 期待タスク数: 3-5タスク

**実行手順**:
1. `/orchestrate-review-loop` コマンドを実行
2. 要件ファイルパスを入力
3. レビューループが完了するまで待機
4. 証拠記録を確認

**成功基準**:
- [ ] すべてのドキュメントが品質スコア70点以上
- [ ] 証拠記録が完全に生成されている
- [ ] final_summary.mdが生成されている
- [ ] ドキュメントがStockフォルダに移動されている

**実行時間**: 20-60分（タスク数とリトライ回数に依存）

---

## テストケーステンプレート

各シナリオに対して、以下のテストケーステンプレートを使用します。

```markdown
# Test Case: {シナリオ名}

## 実行日時
- 実行者: {名前}
- 実行日: {YYYY-MM-DD}
- 実行時間: {HH:MM:SS}

## テスト環境
- Claude Code バージョン: {バージョン}
- OS: {OS名とバージョン}

## 実行結果

### STEP 1: タスク分解
- ✅ / ❌ タスク数が期待通り
- ✅ / ❌ task_breakdown.mdが生成された

### STEP 2: SubAgent実行
- ✅ / ❌ SubAgentが正常に実行された
- ✅ / ❌ subagent_output.mdが生成された

### STEP 3: Review Agent実行
- ✅ / ❌ Review Agentが正常に実行された
- ✅ / ❌ quality_score.jsonが生成された
- ✅ / ❌ review_report.mdが生成された

### STEP 4: 統合判定
- ✅ / ❌ decision.mdが生成された
- ✅ / ❌ 判定結果が期待通り

### STEP 5: 成果物確認
- ✅ / ❌ final_summary.mdが生成された
- ✅ / ❌ すべての証拠記録が存在する

## スコア推移
| Iteration | 品質スコア | 判定 |
|-----------|-----------|------|
| 1 | {スコア}点 | {合格/不合格} |
| 2 | {スコア}点 | {合格/不合格} |
| 3 | {スコア}点 | {合格/不合格} |

## 問題点
- {問題点1}
- {問題点2}

## 改善提案
- {改善案1}
- {改善案2}

## 総評
- 成功 / 失敗
- 所要時間: {XX}分
```

---

## 自動テストスクリプト（将来実装）

Week 7では手動テストを実施しますが、将来的には以下の自動テストスクリプトを実装します。

```python
# tests/test_review_loop.py

import pytest
from pathlib import Path

def test_scenario_1_success_first_try():
    """シナリオ1: 1回で成功"""
    result = run_review_loop("tests/fixtures/requirements_simple.md")

    assert result["status"] == "SUCCESS"
    assert result["iteration_count"] == 1
    assert result["total_score"] >= 70

    # 証拠記録確認
    evidence_dir = Path("Flow/202601/2026-01-02/review_loop_evidence")
    assert (evidence_dir / "iteration_001" / "task_breakdown.md").exists()
    assert (evidence_dir / "final_summary.md").exists()

def test_scenario_2_success_second_try():
    """シナリオ2: 2回で成功"""
    result = run_review_loop("tests/fixtures/requirements_moderate.md")

    assert result["status"] == "SUCCESS"
    assert result["iteration_count"] == 2
    assert result["total_score"] >= 70

    # リプラン分析確認
    evidence_dir = Path("Flow/202601/2026-01-02/review_loop_evidence")
    assert (evidence_dir / "iteration_002" / "replan_analysis.md").exists()

def test_scenario_4_human_intervention():
    """シナリオ4: 3回失敗 → Human-in-the-Loop"""
    result = run_review_loop("tests/fixtures/requirements_very_complex.md")

    assert result["status"] == "HUMAN_INTERVENTION_REQUIRED"
    assert result["iteration_count"] == 3

    # failure_report.md確認
    evidence_dir = Path("Flow/202601/2026-01-02/review_loop_evidence")
    assert (evidence_dir / "failure_report.md").exists()

def test_timeout_handling():
    """シナリオ6: タイムアウト処理"""
    result = run_review_loop("tests/fixtures/requirements_timeout.md", timeout=300)

    assert result["status"] == "TIMEOUT"

    # error_log.json確認
    evidence_dir = Path("Flow/202601/2026-01-02/review_loop_evidence")
    assert (evidence_dir / "error_log.json").exists()
```

---

## 品質メトリクス

テスト実行後、以下のメトリクスを計測します。

| メトリクス | 目標 | 実測値 |
|-----------|------|--------|
| 初回成功率 | 85%以上 | {実測値} |
| Human介入率 | 5%以下 | {実測値} |
| 平均イテレーション数 | 1.5回以下 | {実測値} |
| 平均実行時間 | 30分以内 | {実測値} |
| 品質スコア平均 | 75点以上 | {実測値} |

---

## テスト実施記録

| 日付 | シナリオ | 結果 | 所要時間 | 実行者 | 備考 |
|------|---------|------|----------|--------|------|
| 2026-01-02 | シナリオ1 | ✅ | 18分 | {名前} | - |
| 2026-01-02 | シナリオ2 | ✅ | 42分 | {名前} | - |
| 2026-01-02 | シナリオ3 | ✅ | 65分 | {名前} | - |
| 2026-01-02 | シナリオ4 | ✅ | 58分 | {名前} | - |
| 2026-01-02 | シナリオ5 | ✅ | 22分 | {名前} | - |
| 2026-01-02 | シナリオ6 | ❌ | - | {名前} | タイムアウト処理未実装 |
| 2026-01-02 | シナリオ7 | ❌ | - | {名前} | エラーハンドリング未実装 |

---

## 関連ドキュメント

- **Manager Skill**: `.claude/skills/orchestrate-review-loop/SKILL.md`
- **Review Agent**: `.claude/agents/review-agent.md`
- **品質基準**: `.claude/skills/_shared/review_criteria.md`
- **リプランパターン**: `.claude/skills/_shared/replan_patterns.md`
- **証拠記録システム**: `.claude/skills/_shared/evidence_system.md`
- **リトライループ実装**: `.claude/skills/_shared/retry_loop_implementation.md`
