# Review Loop Rules

レビューループ制御のルール。

## トリガー

- Manager Skillから自動起動
- SubAgent完了後

## 実行手順

### 1. Review Agent起動

SubAgentの完了を確認後、Task tool経由でReview Agentを起動：

```python
# Manager Skill内でのTask tool実装例
from task import Task

# SubAgent並列実行
results = execute_subagents_parallel(tasks)

# Review Agent起動（Task tool経由）
review_result = Task(
    description=f"品質レビュー - イテレーション {iteration}",
    prompt=f"""
    @.claude/agents/review-agent.md の仕様に従い、以下のドキュメントをレビューしてください。

    **ドキュメント情報**:
    - ドキュメントパス: `{document_path}`
    - ドキュメントタイプ: `{doc_type}`
    - イテレーション: {iteration}

    **評価指示**:
    5観点（完全性、論理性、具体性、エビデンス、フレームワーク準拠性）で評価し、
    以下のファイルを出力してください:

    1. `quality_score.json`: 各スコアと総合点
    2. `review_report.md`: 詳細レビューレポート

    **出力先**: `{evidence_dir}/iteration_{iteration:03d}/`

    **重要**: 出力ファイルは必ず上記ディレクトリに保存してください。
    評価基準は @.claude/skills/_shared/review_criteria.md を参照してください。
    """,
    subagent_type="general-purpose",
    model="sonnet",
    timeout=600000  # 10分 = 600,000ミリ秒
)

# quality_score.jsonから総合点を取得
quality_score = parse_quality_score(review_result, evidence_dir, iteration)
```

**重要ポイント**:
- `@.claude/agents/review-agent.md` をプロンプトで参照し、仕様を継承
- `model="sonnet"` を推奨（バランス重視）
- `timeout=600000` で10分タイムアウト設定
- `subagent_type="general-purpose"` でTask tool経由起動

### 2. 品質ゲート判定

```python
if review_report.quality_score >= 70:
    # 統合完了
    integrate_and_finalize(results)
    return "SUCCESS"
elif review_report.quality_score >= 60:
    # 条件付き合格
    log_warning(review_report.issues)
    integrate_and_finalize(results)
    return "SUCCESS_WITH_WARNING"
else:
    # 不合格 → リプラン
    if iteration < MAX_RETRIES:
        replan_instructions = manager_skill.replan(review_report)
        return replan_instructions
    else:
        # Human-in-the-Loop
        return trigger_human_intervention(review_report)
```

### 3. リトライループ（Task tool統合版）

```python
from task import Task

MAX_RETRIES = 3
QUALITY_THRESHOLD = 70

for iteration in range(1, MAX_RETRIES + 1):
    # STEP 1: 証拠記録ディレクトリ作成
    iteration_dir = f"{evidence_dir}/iteration_{iteration:03d}"
    os.makedirs(iteration_dir, exist_ok=True)

    # STEP 2: SubAgent並列実行
    results = execute_subagents_parallel(tasks)

    # STEP 3: SubAgent出力を証拠記録に保存
    save_subagent_outputs(results, iteration_dir)

    # STEP 4: Review Agent起動（Task tool経由）
    review_reports = []
    for task in tasks:
        review_result = Task(
            description=f"品質レビュー - {task['title']} (イテレーション {iteration})",
            prompt=f"""
            @.claude/agents/review-agent.md の仕様に従い、以下のドキュメントをレビューしてください。

            **ドキュメント情報**:
            - ドキュメントパス: `{task['output_path']}`
            - ドキュメントタイプ: `{task['doc_type']}`
            - イテレーション: {iteration}

            **評価指示**:
            5観点で評価し、以下を出力:
            1. `quality_score.json`: 総合点（100点満点）
            2. `review_report.md`: 詳細レビュー

            **出力先**: `{iteration_dir}/review_{task['id']}/`

            評価基準: @.claude/skills/_shared/review_criteria.md
            """,
            subagent_type="general-purpose",
            model="sonnet",
            timeout=600000  # 10分
        )
        review_reports.append(review_result)

    # STEP 5: 統合可否判定
    all_passed = True
    for i, review in enumerate(review_reports):
        quality_score = parse_quality_score(review, iteration_dir, tasks[i]['id'])

        if quality_score < QUALITY_THRESHOLD:
            all_passed = False
            save_decision(tasks[i], quality_score, "REPLAN", iteration, iteration_dir)
        else:
            save_decision(tasks[i], quality_score, "INTEGRATE", iteration, iteration_dir)

    # STEP 6: 合格判定
    if all_passed:
        integrate_and_finalize(results, iteration_dir)
        return {
            "status": "SUCCESS",
            "iteration": iteration,
            "quality_scores": [parse_quality_score(r, iteration_dir, t['id']) for r, t in zip(review_reports, tasks)]
        }

    # STEP 7: リトライ上限チェック
    if iteration == MAX_RETRIES:
        return {
            "status": "HUMAN_INTERVENTION_REQUIRED",
            "iteration": iteration,
            "review_reports": review_reports,
            "reason": "3回のリトライ後も品質基準未達"
        }

    # STEP 8: リプラン実行
    replan_instructions = analyze_and_replan(review_reports, iteration, iteration_dir)
    tasks = update_tasks_with_replan(tasks, replan_instructions)

    # STEP 9: リプラン内容を証拠記録に保存
    save_replan_instructions(replan_instructions, iteration_dir)
```

**実装の鍵**:
1. **Task tool経由起動**: `Task(subagent_type="general-purpose", model="sonnet")`
2. **証拠記録の徹底**: イテレーション毎に `iteration_{N:03d}/` ディレクトリを作成
3. **タイムアウト設定**: `timeout=600000` (10分)
4. **複数タスク対応**: 各タスクごとにReview Agentを起動
5. **全合格判定**: すべてのタスクが70点以上で統合完了

## タイムアウト設定

- **SubAgent実行**: 30分/タスク
- **Review Agent**: 10分
- **リプラン生成**: 10分

タイムアウト時はPattern 7（Replan Timeout）を適用。

## Week 1 実装完了状況（2026-01-03）

### 検証済み項目
- ✅ Task tool経由でのReview Agent起動成功
- ✅ 高品質ドキュメント（100点）の正常評価
- ✅ 低品質ドキュメント（34点）の正常検出
- ✅ セクション欠落（15.425点）の完全性評価
- ✅ Manager Skillへの統合パターン実装
- ✅ quality_score.json, review_report.md 自動生成確認

### 実装済み機能
1. **Task tool統合**: `Task(subagent_type="general-purpose", model="sonnet")`
2. **タイムアウト設定**: 10分（600,000ミリ秒）
3. **リトライループ**: 最大3回、70点基準
4. **証拠記録**: イテレーション毎のディレクトリ保存
5. **複数タスク対応**: 各タスクごとのレビュー実行

### 次のステップ（Week 2以降）
- Discovery Automation Agent作成
- API Integration Agent作成
- Research Index Agent作成（P1）

## 参照

- @.claude/agents/review-agent.md - Review Agent仕様書（502行）
- @.claude/skills/orchestrate-review-loop/SKILL.md - Manager Skill実装（843+行）
- @.claude/skills/_shared/review_criteria.md - 品質評価基準（373行）
- @.claude/skills/_shared/error_handling_patterns.md#pattern-7 - タイムアウト処理パターン
- @.claude/rules/parallel_execution.md - 並列実行ガイドライン
- @Flow/202601/2026-01-03/review/ - テスト出力ファイル保存場所
