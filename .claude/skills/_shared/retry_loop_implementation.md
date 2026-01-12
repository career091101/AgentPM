# Retry Loop Implementation - リトライループ実装ガイド

レビューループにおけるリトライループの詳細実装仕様。

**最終更新**: 2026-01-02
**バージョン**: 1.0（Week 6）

---

## 概要

品質スコアが閾値未満の場合、Manager Skillは最大3回までリトライを実行します。各イテレーションでリプラン分析を行い、SubAgentへの修正指示を更新します。

**目的**:
- 自動的な品質改善ループの実現
- Human介入率の最小化（5%以下）
- 初回成功率の向上（85%以上）

---

## リトライループの基本構造

```python
MAX_RETRIES = 3
QUALITY_THRESHOLD = 70

for iteration in range(1, MAX_RETRIES + 1):
    print(f"=== Iteration {iteration}/{MAX_RETRIES} ===")

    # STEP 1: 証拠記録ディレクトリ作成
    evidence_dir = create_evidence_directory(iteration)

    # STEP 2: タスク分解（初回のみ） or タスク更新（リプラン時）
    if iteration == 1:
        tasks = decompose_tasks(requirements)
        save_task_breakdown(tasks, evidence_dir)
    else:
        tasks = update_tasks_with_replan(tasks, replan_instructions)
        save_task_breakdown_updated(tasks, evidence_dir)

    # STEP 3: SubAgent並列実行
    results = execute_subagents_parallel(tasks)
    save_subagent_outputs(results, evidence_dir)

    # STEP 4: Review Agent起動
    review_reports = execute_review_agents(tasks, results, iteration, evidence_dir)

    # STEP 5: 統合可否判定
    decision = make_integration_decision(review_reports, iteration, evidence_dir)

    if decision == "INTEGRATE":
        # STEP 6: 統合完了
        integrate_and_finalize(results, evidence_dir)
        return "SUCCESS"

    elif decision == "REPLAN":
        if iteration == MAX_RETRIES:
            # STEP 7: Human-in-the-Loop
            return trigger_human_intervention(review_reports, evidence_dir)
        else:
            # STEP 8: リプラン実行
            replan_instructions = analyze_and_replan(review_reports, iteration, evidence_dir)
            continue

    else:
        # STEP 7: エラー処理
        return handle_error(decision)
```

---

## イテレーション状態管理

### 状態遷移図

```
START
  ↓
┌─────────────────┐
│ Iteration 1     │
│ - タスク分解    │
│ - SubAgent実行  │
│ - Review        │
└────┬────────────┘
     │
     ├─ ✅ 合格（70点以上）→ 統合完了 → END
     │
     └─ ❌ 不合格（70点未満）
           ↓
    ┌─────────────────┐
    │ Iteration 2     │
    │ - リプラン      │
    │ - SubAgent再実行│
    │ - Review        │
    └────┬────────────┘
         │
         ├─ ✅ 合格 → 統合完了 → END
         │
         └─ ❌ 不合格
               ↓
        ┌─────────────────┐
        │ Iteration 3     │
        │ - リプラン      │
        │ - SubAgent再実行│
        │ - Review        │
        └────┬────────────┘
             │
             ├─ ✅ 合格 → 統合完了 → END
             │
             └─ ❌ 不合格 → Human-in-the-Loop → END
```

### 状態管理変数

```python
iteration_state = {
    "current_iteration": 1,
    "max_retries": 3,
    "quality_threshold": 70,
    "tasks": [],
    "results": [],
    "review_reports": [],
    "replan_instructions": None,
    "status": "in_progress"  # in_progress | completed | failed
}
```

---

## STEP 1: 証拠記録ディレクトリ作成

```python
def create_evidence_directory(iteration: int) -> str:
    """
    証拠記録ディレクトリを作成

    Args:
        iteration: イテレーション番号（1, 2, 3）

    Returns:
        evidence_dir: 証拠記録ディレクトリパス
    """
    from datetime import datetime
    from pathlib import Path

    # 日付フォルダパス
    today = datetime.now()
    year_month = today.strftime("%Y%m")
    date_str = today.strftime("%Y-%m-%d")

    # 証拠記録ディレクトリパス
    evidence_dir = Path(f"Flow/{year_month}/{date_str}/review_loop_evidence/iteration_{iteration:03d}")

    # ディレクトリ作成（存在しない場合）
    evidence_dir.mkdir(parents=True, exist_ok=True)

    print(f"📁 証拠記録ディレクトリ作成: {evidence_dir}")

    return str(evidence_dir)
```

**実行タイミング**: 各イテレーションの最初

**出力**:
```
Flow/202601/2026-01-02/review_loop_evidence/iteration_001/
Flow/202601/2026-01-02/review_loop_evidence/iteration_002/
Flow/202601/2026-01-02/review_loop_evidence/iteration_003/
```

---

## STEP 2: タスク分解 or タスク更新

### 初回（Iteration 1）

```python
def decompose_tasks(requirements: str) -> list:
    """
    要件を3-5個のタスクに分解

    Args:
        requirements: 要件ファイルパスまたは要件テキスト

    Returns:
        tasks: タスクリスト
    """
    # 要件を読み込み
    if Path(requirements).exists():
        requirements_text = Path(requirements).read_text()
    else:
        requirements_text = requirements

    # タスク分解ロジック（Manager Skillが実行）
    tasks = [
        {
            "id": "T001",
            "title": "CPF判定レポート作成",
            "description": "顧客セグメント、課題、解決策を含むCPF検証レポート作成",
            "doc_type": "cpf_judgment",
            "output_file": "Flow/202601/2026-01-02/cpf_judgment.md",
            "dependencies": [],
            "parallel_group": 1,
            "quality_threshold": 70
        },
        # ... T002, T003
    ]

    return tasks
```

### リプラン時（Iteration 2+）

```python
def update_tasks_with_replan(tasks: list, replan_instructions: dict) -> list:
    """
    リプラン指示を元にタスクを更新

    Args:
        tasks: 既存タスクリスト
        replan_instructions: リプラン指示

    Returns:
        updated_tasks: 更新されたタスクリスト
    """
    updated_tasks = []

    for task in tasks:
        task_id = task["id"]

        # リプラン指示を取得
        if task_id in replan_instructions:
            task["additional_instructions"] = replan_instructions[task_id]

        updated_tasks.append(task)

    return updated_tasks
```

---

## STEP 3: SubAgent並列実行

```python
def execute_subagents_parallel(tasks: list) -> list:
    """
    SubAgentを並列実行

    Args:
        tasks: タスクリスト

    Returns:
        results: SubAgent実行結果リスト
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    results = []

    # 並列グループ別に実行
    parallel_groups = {}
    for task in tasks:
        group = task["parallel_group"]
        if group not in parallel_groups:
            parallel_groups[group] = []
        parallel_groups[group].append(task)

    # グループ順に並列実行
    for group_id in sorted(parallel_groups.keys()):
        group_tasks = parallel_groups[group_id]

        print(f"🚀 並列グループ{group_id}実行開始（{len(group_tasks)}タスク）")

        with ThreadPoolExecutor(max_workers=len(group_tasks)) as executor:
            futures = {
                executor.submit(execute_subagent, task): task
                for task in group_tasks
            }

            for future in as_completed(futures):
                task = futures[future]
                try:
                    result = future.result(timeout=1800)  # 30分タイムアウト
                    results.append(result)
                    print(f"✅ {task['id']}: {task['title']} 完了")
                except Exception as e:
                    print(f"❌ {task['id']}: {task['title']} 失敗 - {e}")
                    raise

    return results

def execute_subagent(task: dict) -> dict:
    """
    単一SubAgentを実行（Task tool使用）

    Args:
        task: タスク定義

    Returns:
        result: SubAgent実行結果
    """
    # Task toolでSubAgent起動
    result = Task(
        description=f"ドキュメント作成: {task['title']}",
        prompt=generate_subagent_prompt(task),
        subagent_type="general-purpose",
        model="sonnet"
    )

    return {
        "task_id": task["id"],
        "output_file": task["output_file"],
        "status": "completed"
    }
```

**タイムアウト設定**: 1タスクあたり30分（1800秒）

**エラーハンドリング**: タイムアウトまたはエラー時は即座にループを中断し、Human-in-the-Loopを発動

---

## STEP 4: Review Agent起動

```python
def execute_review_agents(tasks: list, results: list, iteration: int, evidence_dir: str) -> list:
    """
    Review Agentを起動して品質スコアを計算

    Args:
        tasks: タスクリスト
        results: SubAgent実行結果リスト
        iteration: イテレーション番号
        evidence_dir: 証拠記録ディレクトリパス

    Returns:
        review_reports: レビューレポートリスト
    """
    review_reports = []

    for task, result in zip(tasks, results):
        print(f"🔍 レビュー開始: {task['id']} - {task['title']}")

        # Review Agent起動（Task tool）
        review_report = Task(
            description=f"レビュー: {task['title']}",
            prompt=generate_review_prompt(task, result, iteration, evidence_dir),
            subagent_type="general-purpose",
            model="sonnet"
        )

        review_reports.append(review_report)

        print(f"📊 品質スコア: {review_report['total_score']}点")

    return review_reports
```

**Review Agentへの指示に含める情報**:
- ドキュメントファイルパス
- ドキュメントタイプ
- イテレーション番号
- 証拠記録ディレクトリパス

---

## STEP 5: 統合可否判定

```python
def make_integration_decision(review_reports: list, iteration: int, evidence_dir: str) -> str:
    """
    統合可否を判定

    Args:
        review_reports: レビューレポートリスト
        iteration: イテレーション番号
        evidence_dir: 証拠記録ディレクトリパス

    Returns:
        decision: "INTEGRATE" | "REPLAN" | "ERROR"
    """
    # 全タスクの品質スコアを確認
    all_passed = all(report["total_score"] >= 70 for report in review_reports)

    if all_passed:
        decision = "INTEGRATE"
        decision_reason = f"全タスク合格（品質スコア ≥ 70点）"
    else:
        decision = "REPLAN"
        failed_tasks = [
            f"{report['task_id']}: {report['total_score']}点"
            for report in review_reports
            if report["total_score"] < 70
        ]
        decision_reason = f"不合格タスクあり: {', '.join(failed_tasks)}"

    # decision_{NNN}.mdを生成
    save_decision_record(decision, decision_reason, review_reports, iteration, evidence_dir)

    print(f"⚖️  判定: {decision} - {decision_reason}")

    return decision
```

**判定ロジック**:
- **INTEGRATE**: 全タスクのスコアが70点以上
- **REPLAN**: 1つでもスコアが70点未満のタスクあり
- **ERROR**: Review Agent実行エラー

---

## STEP 6: 統合完了

```python
def integrate_and_finalize(results: list, evidence_dir: str) -> None:
    """
    ドキュメントを統合し、final_summary.mdを生成

    Args:
        results: SubAgent実行結果リスト
        evidence_dir: 証拠記録ディレクトリパス（親ディレクトリ）
    """
    print("🎉 統合完了処理開始")

    # ドキュメントをStockフォルダに移動（省略）

    # final_summary.mdを生成
    summary_path = Path(evidence_dir).parent / "final_summary.md"
    generate_final_summary(results, summary_path)

    print(f"📄 最終サマリー生成: {summary_path}")
    print("✅ レビューループ完了")
```

---

## STEP 7: Human-in-the-Loop

```python
def trigger_human_intervention(review_reports: list, evidence_dir: str) -> str:
    """
    3回失敗時にHuman-in-the-Loopを発動

    Args:
        review_reports: レビューレポートリスト
        evidence_dir: 証拠記録ディレクトリパス

    Returns:
        status: "HUMAN_INTERVENTION_REQUIRED"
    """
    print("🚨 Human-in-the-Loop 発動")
    print(f"🔄 最大リトライ回数（{MAX_RETRIES}回）に達しました")

    # 失敗レポートを生成
    failure_report = generate_failure_report(review_reports, evidence_dir)

    print(f"📊 失敗レポート: {failure_report}")
    print("\n⚠️  ユーザー判断が必要です:")
    print("1. 手動修正を実施")
    print("2. 要件見直し")
    print("3. 中断")

    return "HUMAN_INTERVENTION_REQUIRED"

def generate_failure_report(review_reports: list, evidence_dir: str) -> str:
    """
    失敗レポートを生成

    Args:
        review_reports: レビューレポートリスト
        evidence_dir: 証拠記録ディレクトリパス

    Returns:
        failure_report_path: 失敗レポートのパス
    """
    failure_report_path = Path(evidence_dir).parent / "failure_report.md"

    content = f"""# Failure Report - Human Intervention Required

**失敗日時**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**総イテレーション数**: {MAX_RETRIES}回

## 失敗理由

3回のイテレーション後も品質スコア70点以上を達成できませんでした。

## イテレーション履歴

{generate_iteration_history(review_reports, evidence_dir)}

## 推奨アクション

1. **手動修正**: 証拠記録を確認し、問題箇所を手動修正
2. **要件見直し**: 要件が現実的か再確認
3. **中断**: プロジェクト中断またはアプローチ変更

## 証拠記録

- Iteration 1: `iteration_001/`
- Iteration 2: `iteration_002/`
- Iteration 3: `iteration_003/`
"""

    failure_report_path.write_text(content)

    return str(failure_report_path)
```

**Human-in-the-Loop発動条件**:
1. 3回連続不合格（total_score < 70）
2. スコア改善なし（±2点以内）
3. Review Agentエラー

---

## STEP 8: リプラン実行

```python
def analyze_and_replan(review_reports: list, iteration: int, evidence_dir: str) -> dict:
    """
    問題分析とリプラン実行

    Args:
        review_reports: レビューレポートリスト
        iteration: 現在のイテレーション番号
        evidence_dir: 証拠記録ディレクトリパス

    Returns:
        replan_instructions: タスク別のリプラン指示
    """
    print(f"🔄 リプラン実行（Iteration {iteration} → {iteration + 1}）")

    replan_instructions = {}

    for report in review_reports:
        if report["total_score"] < 70:
            task_id = report["task_id"]

            # 問題パターンを特定
            patterns = identify_problem_patterns(report)

            # パターン別の修正指示を生成
            instructions = generate_修正指示(patterns, report)

            replan_instructions[task_id] = instructions

            print(f"📝 {task_id}: {len(patterns)}件の問題パターン検出")

    # replan_analysis.mdを保存
    next_evidence_dir = create_evidence_directory(iteration + 1)
    save_replan_analysis(replan_instructions, next_evidence_dir)

    return replan_instructions

def identify_problem_patterns(report: dict) -> list:
    """
    問題パターンを特定

    Args:
        report: レビューレポート

    Returns:
        patterns: 問題パターンリスト
    """
    patterns = []

    if report["completeness_score"] < 15:
        patterns.append("Pattern 1: セクション不足")
    if report["logic_score"] < 15:
        patterns.append("Pattern 2: 論理的矛盾")
    if report["specificity_score"] < 12:
        patterns.append("Pattern 3: 抽象的表現")
    if report["evidence_score"] < 9:
        patterns.append("Pattern 4: エビデンス不足")
    if report["framework_compliance_score"] < 9:
        patterns.append("Pattern 5: フレームワーク逸脱")

    return patterns
```

**リプラン指示の生成**: `.claude/skills/_shared/replan_patterns.md`を参照

---

## タイムアウト処理

### SubAgent実行タイムアウト

```python
SUBAGENT_TIMEOUT = 1800  # 30分

try:
    result = future.result(timeout=SUBAGENT_TIMEOUT)
except TimeoutError:
    print(f"⏱️  タイムアウト: {task['id']} - 30分経過")
    return trigger_human_intervention(review_reports, evidence_dir)
```

### Review Agent実行タイムアウト

```python
REVIEW_AGENT_TIMEOUT = 600  # 10分

try:
    review_report = future.result(timeout=REVIEW_AGENT_TIMEOUT)
except TimeoutError:
    print(f"⏱️  レビュータイムアウト: {task['id']} - 10分経過")
    return trigger_human_intervention(review_reports, evidence_dir)
```

### 総実行時間制限

```python
TOTAL_TIMEOUT = 7200  # 2時間

start_time = time.time()

for iteration in range(1, MAX_RETRIES + 1):
    if time.time() - start_time > TOTAL_TIMEOUT:
        print("⏱️  総実行時間制限に達しました（2時間）")
        return trigger_human_intervention(review_reports, evidence_dir)
```

---

## エラーハンドリング

### Pattern 6: Review Failure（error_handling_patterns.mdから拡張）

```python
try:
    review_reports = execute_review_agents(tasks, results, iteration, evidence_dir)
except Exception as e:
    print(f"❌ Review Agentエラー: {e}")

    # エラーログ記録
    error_log = {
        "timestamp": datetime.now().isoformat(),
        "iteration": iteration,
        "error_type": type(e).__name__,
        "error_message": str(e),
        "traceback": traceback.format_exc()
    }

    save_error_log(error_log, evidence_dir)

    # Human-in-the-Loop発動
    return trigger_human_intervention(review_reports, evidence_dir)
```

### Pattern 7: Replan Timeout（error_handling_patterns.mdから拡張）

```python
REPLAN_TIMEOUT = 600  # 10分

try:
    replan_instructions = analyze_and_replan(review_reports, iteration, evidence_dir)
except TimeoutError:
    print("⏱️  リプランタイムアウト: 10分経過")

    # Graceful Exit
    partial_results = {
        "completed_iterations": iteration,
        "partial_success_tasks": [r for r in review_reports if r["total_score"] >= 70],
        "failed_tasks": [r for r in review_reports if r["total_score"] < 70]
    }

    save_partial_results(partial_results, evidence_dir)

    return trigger_human_intervention(review_reports, evidence_dir)
```

---

## 実行ログ

各イテレーションの実行ログを記録します。

```python
def log_iteration(iteration: int, status: str, duration: float, quality_scores: list) -> None:
    """
    イテレーションログを記録

    Args:
        iteration: イテレーション番号
        status: "SUCCESS" | "REPLAN" | "FAILED"
        duration: 実行時間（秒）
        quality_scores: 品質スコアリスト
    """
    log_entry = {
        "iteration": iteration,
        "timestamp": datetime.now().isoformat(),
        "status": status,
        "duration_seconds": duration,
        "average_quality_score": sum(quality_scores) / len(quality_scores),
        "min_quality_score": min(quality_scores),
        "max_quality_score": max(quality_scores)
    }

    # ログファイルに追記
    log_file = Path("review_loop_execution.log")
    with log_file.open("a") as f:
        f.write(json.dumps(log_entry) + "\n")
```

---

## 成功パターン分析

Week 7のテストで使用する成功パターン分析データを記録します。

```python
def analyze_success_pattern(review_reports: list, iteration: int) -> dict:
    """
    成功パターンを分析

    Args:
        review_reports: レビューレポートリスト
        iteration: 成功したイテレーション番号

    Returns:
        success_pattern: 成功パターン分析結果
    """
    success_pattern = {
        "iteration_count": iteration,
        "initial_quality_scores": [],
        "final_quality_scores": [r["total_score"] for r in review_reports],
        "improvement_delta": [],
        "problem_patterns_resolved": [],
        "critical_success_factors": []
    }

    # 成功パターンをデータベースに記録（将来的に機械学習に活用）
    save_success_pattern(success_pattern)

    return success_pattern
```

---

## 関連ドキュメント

- **品質基準**: `.claude/skills/_shared/review_criteria.md`
- **リプランパターン**: `.claude/skills/_shared/replan_patterns.md`
- **証拠記録システム**: `.claude/skills/_shared/evidence_system.md`
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`
- **Manager Skill**: `.claude/skills/orchestrate-review-loop/SKILL.md`
- **Review Agent**: `.claude/agents/review-agent.md`
