# AgentSkills エラーハンドリング標準パターン

**最終更新**: 2025-12-30
**バージョン**: 1.0
**対象**: 全AgentSkills（Founder Agent 16スキル + Trading Agent 24スキル + 共有 1スキル）

---

## 1. 外部API失敗（WebSearch、WebFetch等）

### パターン: Retry with Exponential Backoff

**適用ケース**:
- WebSearch失敗
- WebFetch失敗
- 外部API呼び出し失敗

**実装**:
```markdown
### エラーハンドリング: WebSearch失敗時

**リトライ戦略**:
- max_retries = 3
- retry_delays = [5, 15, 30] 秒
- クエリ変更で再試行

**Iteration N**:
**Thought（思考）**: [仮説]
**Action（行動）**: WebSearch(query="[クエリ1]")
**Observation（観察）**: ❌ 失敗 - タイムアウト

**Retry 1**:
- 待機: 5秒
- クエリ変更: "[クエリ2]"（より具体的に）
- WebSearch(query="[クエリ2]")

**Retry 2**:
- 待機: 15秒
- クエリ変更: "[クエリ3]"（別の角度から）
- WebSearch(query="[クエリ3]")

**Retry 3**:
- 待機: 30秒
- クエリ変更: "[クエリ4]"（最も単純化）
- WebSearch(query="[クエリ4]")

**Final Result**:
- 3回リトライ後も失敗 → エラー報告（パターン5参照）
```

**期待効果**:
- 一時的なネットワークエラーからの自動回復
- リトライ成功率 70% → 90%

---

## 2. ファイル読み込み失敗

### パターン: Fallback Path

**適用ケース**:
- 必須ファイルが存在しない
- 前ステップの成果物が未生成
- パス誤り

**実装**:
```markdown
### エラーハンドリング: ファイル読み込み失敗時

**フォールバック戦略**:

**STEP 1**: 主ファイル読み込み
- ファイル: `{IDEA_FOLDER}/documents/2_discovery/persona.md`
- 失敗 → STEP 2へ

**STEP 2**: フォールバックファイル読み込み
- ファイル: `{IDEA_FOLDER}/documents/1_initiating/demand_discovery.md`
- ペルソナ情報を推論
- 成功 → 警告表示して続行
- 失敗 → STEP 3へ

**STEP 3**: エラー報告
- status: error
- error_code: FILE_NOT_FOUND
- message: "ペルソナファイルが存在しません。`/create-persona`スキルを実行してください。"
- action: "Human-in-the-Loop"
```

**期待効果**:
- 代替データからの処理継続
- 処理中断の最小化

---

## 3. データ検証失敗（スコア計算等）

### パターン: Validation + Graceful Degradation

**適用ケース**:
- CPF/PSFスコア計算で必須項目不足
- 数値データの異常値検出
- 必須フィールドの欠落

**実装**:
```markdown
### エラーハンドリング: CPFスコア計算失敗時

**必須項目チェック**:
- [ ] ペルソナ定義（name, age, occupation）
- [ ] 3U+1スコア（Unworkable, Unavoidable, Urgent, Underserved）
- [ ] インタビュー件数（最低5件）

**判定ロジック**:

| 必須項目充足率 | 対応 |
|-------------|------|
| 100% | 通常計算、スコア表示 |
| 80-99% | 警告表示 + 部分スコア計算 + 続行 |
| <80% | エラー報告 + 停止 |

**警告表示例** (80-99%):
```yaml
status: warning
message: "ペルソナの職業情報が不足しています。スコアは参考値です。"
partial_score: 65%
missing_fields: ["occupation"]
action: "項目補完を推奨"
```

**エラー報告例** (<80%):
```yaml
status: error
error_code: VALIDATION_ERROR
message: "CPFスコア計算に必要な情報が不足しています（充足率: 70%）"
missing_fields: ["persona.age", "3u.Urgent", "interview_count"]
action: "Human-in-the-Loop"
```
```

**期待効果**:
- 部分データでの処理継続
- 明確なエラー原因特定

---

## 4. タイムアウト

### パターン: Progress Indication + Graceful Exit

**適用ケース**:
- 長時間実行スキル（orchestrate-phase1等）
- 大量データ処理
- 外部API待機時間超過

**実装**:
```markdown
### エラーハンドリング: タイムアウト時

**進捗表示**:
```markdown
## Phase1 実行中...

✅ STEP 1: discover-demand（完了 30分）
✅ STEP 2: create-mvv（完了 25分）
✅ STEP 3: apply-lean-canvas（完了 80分）
🔄 STEP 4: build-flywheel（実行中... 50分経過）
⏸️ タイムアウト検知（制限時間: 60分）

**部分成果物保存中...**
```

**Graceful Exit手順**:

1. **進捗状況保存**
   - ファイル: `{IDEA_FOLDER}/phase1_progress.json`
   - 内容: 完了ステップ、実行中ステップ、中間成果物パス

2. **部分成果物保存**
   - `documents/1_initiating/`（完了）
   - `documents/2_discovery/lean_canvas.md`（完了）
   - `documents/2_discovery/flywheel.md`（部分完成・保存）

3. **再開指示提示**
   ```yaml
   status: timeout
   completed_steps: ["discover-demand", "create-mvv", "apply-lean-canvas"]
   current_step: "build-flywheel"
   progress_file: "{IDEA_FOLDER}/phase1_progress.json"
   action: "再開するには `/resume-phase1` を実行してください"
   ```
```

**期待効果**:
- 作業の部分保存
- 再開可能性の提供

---

## 5. 標準エラーレスポンス形式

### YAML形式

すべてのスキルは、エラー発生時に以下の形式でエラー情報を出力する：

```yaml
status: error | warning | timeout | incomplete
error_code: API_FAILURE | FILE_NOT_FOUND | VALIDATION_ERROR | TIMEOUT | UNKNOWN
message: "ユーザー向けメッセージ（日本語、具体的かつ簡潔に）"
skill_name: "[スキル名]"
step: "[失敗したステップ]"
timestamp: "2025-12-30 14:35:22"
details:
  attempted_action: "[試みた操作]"
  failure_reason: "[失敗原因]"
  retry_count: N
action: "Human-in-the-Loop" | "Retry推奨" | "代替手段提示" | "スキップ可能"
next_steps:
  - "[推奨アクション1]"
  - "[推奨アクション2]"
```

### Markdown形式（ユーザー表示用）

```markdown
## ❌ エラー発生

**スキル**: `/validate-cpf`
**ステップ**: CPFスコア計算
**時刻**: 2025-12-30 14:35:22

### エラー内容
ペルソナファイルが存在しません。

### 試みた操作
- `{IDEA_FOLDER}/documents/2_discovery/persona.md` 読み込み
- フォールバック: `demand_discovery.md` 読み込み

### 次のアクション
1. `/create-persona` スキルを実行してペルソナを作成してください
2. または、手動で `persona.md` を作成してください
3. 完了後、`/validate-cpf` を再実行してください

---
**エラーコード**: FILE_NOT_FOUND
**サポート**: `.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗`
```

---

## 6. Human-in-the-Loop トリガー条件

### 自動停止が必須のケース

以下のケースでは、必ずHuman-in-the-Loopで停止し、ユーザー判断を仰ぐ：

1. **ステージゲート未達成**
   - CPFスコア 60%未満
   - PSFスコア（10倍1軸以下）
   - PMFスコア（NPS 50未満 or Retention 40%未満）

2. **重大な検証エラー**
   - 必須ファイル3つ以上欠落
   - WebSearch 3回リトライ全失敗
   - データ検証エラー（充足率 <80%）

3. **ピボット判断**
   - Pivot推奨スコア 70%以上
   - 複数ステージで連続失敗

4. **予期しないエラー**
   - UNKNOWN エラーコード
   - システムリソース不足

### Human-in-the-Loop プロンプト標準形式

```markdown
## ⚠️ Human-in-the-Loop: ユーザー判断が必要です

**状況**: CPFステージゲート未達成

### 現在の状態
- CPFスコア: 55%（目標: 60%以上）
- 3Uスコア: Unworkable 7点、Unavoidable 6点、Urgent 5点
- インタビュー: 12件（目標: 20件以上）

### 推奨アクション（選択肢）
1. **改善して再検証** （推奨）
   - Urgent（緊急性）を高める課題設定に変更
   - インタビュー8件追加実施
   - 推定時間: 4-6時間

2. **条件付きで進行**
   - リスク: PSFステージで失敗する可能性40%
   - 推定時間: そのまま継続（2-3時間）

3. **ピボット検討**
   - 課題・ターゲット・ソリューションを見直し
   - 推定時間: 1-2日

### どの選択肢を選びますか？
（番号で回答してください: 1/2/3）
```

---

## 7. スキル別エラーハンドリング適用ガイド

### 優先度P0スキル（必須適用）

| スキル名 | 主要エラー | 適用パターン |
|---------|----------|-----------|
| orchestrate-phase1 | タイムアウト、ステージゲート失敗 | 1, 3, 4, 5, 6 |
| validate-cpf | データ検証失敗 | 2, 3, 5, 6 |
| validate-psf | データ検証失敗、ステージゲート失敗 | 2, 3, 5, 6 |
| validate-10x | WebSearch失敗 | 1, 2, 5 |
| discover-demand | WebSearch失敗 | 1, 5 |

### 優先度P1スキル（推奨適用）

全AgentSkillsに適用推奨。特に：
- WebSearch/WebFetchを使用するスキル → パターン1
- ファイル読み込みがあるスキル → パターン2
- スコア計算・検証があるスキル → パターン3

---

## 8. テスト方法

### 単体テスト

各エラーパターンを意図的に発生させてテスト：

```markdown
**テストケース1: WebSearch失敗**
- 入力: 無効なクエリ "!!@#$%"
- 期待: 3回リトライ → エラー報告（API_FAILURE）

**テストケース2: ファイル未存在**
- 入力: 存在しないファイルパス
- 期待: フォールバック試行 → 警告 or エラー報告

**テストケース3: データ検証失敗**
- 入力: 必須項目50%のみ入力
- 期待: エラー報告（VALIDATION_ERROR）+ 不足項目リスト表示
```

### 統合テスト

orchestrate-phase1全体でのエラーハンドリング連携テスト：

```markdown
**シナリオ**: CPFステージゲート未達成
- STEP 7で CPFスコア 55%
- 期待: Human-in-the-Loop発動 → 3選択肢提示 → ユーザー選択待ち
```

---

## 9. メンテナンス

### エラーログ収集

各スキル実行時にエラーログを記録：

**ログファイル**: `{IDEA_FOLDER}/error_log.yaml`

```yaml
errors:
  - timestamp: "2025-12-30 14:35:22"
    skill: "/validate-cpf"
    error_code: "FILE_NOT_FOUND"
    message: "ペルソナファイルが存在しません"
    resolved: false

  - timestamp: "2025-12-30 15:10:45"
    skill: "/discover-demand"
    error_code: "API_FAILURE"
    message: "WebSearch 3回リトライ失敗"
    resolved: true
    resolution: "クエリ変更で成功"
```

### エラー頻度分析

月次でエラー統計を分析：

| エラーコード | 発生件数 | 解決率 | 平均リトライ回数 |
|------------|--------|--------|---------------|
| API_FAILURE | 45 | 90% | 1.8回 |
| FILE_NOT_FOUND | 23 | 95% | - |
| VALIDATION_ERROR | 18 | 85% | - |

---

## Pattern 6: Review Failure（レビュー失敗）

### パターン: Review Agent Retry + Human-in-the-Loop

**適用ケース**:
- Review Agentの実行エラー
- 品質スコア計算の失敗
- 3回連続でスコア70点未満

**実装**:
```markdown
### エラーハンドリング: Review Failure時

**リトライ戦略**:
- max_retries = 3（イテレーション）
- 各イテレーションでリプラン実行
- 3回失敗でHuman-in-the-Loop

**Iteration 1**:
- SubAgent実行: cpf_judgment.md生成
- Review Agent実行: 品質スコア 56点
- 判定: ❌ 不合格（56点 < 70点）
- リプラン: Pattern 4（エビデンス不足）検出

**Iteration 2**:
- SubAgent再実行（修正版）
- Review Agent実行: 品質スコア 62点
- 判定: ❌ 不合格（62点 < 70点、改善+6点）
- リプラン: Pattern 2（論理的矛盾）追加検出

**Iteration 3**:
- SubAgent再実行（修正版）
- Review Agent実行: 品質スコア 65点
- 判定: ❌ 不合格（65点 < 70点、改善+3点）
- Human-in-the-Loop発動

**Human-in-the-Loop発動**:
```yaml
status: human_intervention_required
error_code: REVIEW_FAILURE_MAX_RETRIES
message: "3回のイテレーション後も品質スコア70点以上を達成できませんでした"
skill_name: "orchestrate-review-loop"
step: "Iteration 3"
timestamp: "2026-01-02 16:30:00"
details:
  iteration_count: 3
  score_progression: [56, 62, 65]
  final_score: 65
  threshold: 70
  detected_patterns: ["Pattern 4: エビデンス不足", "Pattern 2: 論理的矛盾"]
action: "Human-in-the-Loop"
next_steps:
  - "証拠記録を確認し、問題箇所を手動修正"
  - "要件が現実的か再確認"
  - "プロジェクト中断またはアプローチ変更"
evidence_dir: "Flow/202601/2026-01-02/review_loop_evidence/"
failure_report: "Flow/202601/2026-01-02/review_loop_evidence/failure_report.md"
```
```

**期待効果**:
- 自動リプラン→修正→再レビューのループ
- 3回までの自動改善
- 改善不十分時はHuman介入

---

## Pattern 7: Replan Timeout（リプランタイムアウト）

### パターン: Progress Saving + Graceful Exit

**適用ケース**:
- リプラン分析に10分以上かかる
- SubAgent実行が30分以上
- 総実行時間が2時間超過

**実装**:
```markdown
### エラーハンドリング: Replan Timeout時

**タイムアウト設定**:
- SubAgent実行: 30分/タスク
- Review Agent実行: 10分
- リプラン分析: 10分
- 総実行時間: 2時間

**タイムアウト検出**:
```markdown
## Iteration 2 実行中...

✅ STEP 1: タスク分解（完了 2分）
✅ STEP 2: SubAgent実行（完了 18分）
✅ STEP 3: Review Agent実行（完了 12分）
✅ STEP 4: 統合判定（不合格 56点）
🔄 STEP 5: リプラン分析（実行中... 10分経過）
⏸️ タイムアウト検知（制限時間: 10分）

**部分成果物保存中...**
```

**Graceful Exit手順**:

1. **進捗状況保存**
   - ファイル: `{evidence_dir}/progress.json`
   - 内容:
   ```json
   {
     "status": "timeout",
     "current_iteration": 2,
     "completed_steps": ["task_breakdown", "subagent_execution", "review", "decision"],
     "timeout_step": "replan_analysis",
     "elapsed_time_seconds": 1800,
     "timeout_limit_seconds": 600
   }
   ```

2. **部分成果物保存**
   - Iteration 1完了分: すべて保存済み
   - Iteration 2部分完了: subagent出力、review_report、decision保存
   - リプラン分析未完: replan_analysis.md未生成

3. **タイムアウトレポート生成**
   ```yaml
   status: timeout
   error_code: REPLAN_TIMEOUT
   message: "リプラン分析が10分以内に完了しませんでした"
   skill_name: "orchestrate-review-loop"
   step: "Iteration 2 - リプラン分析"
   timestamp: "2026-01-02 15:45:00"
   details:
     elapsed_time_seconds: 600
     timeout_limit_seconds: 600
     completed_iterations: 1
     partial_iteration: 2
   action: "部分成果物を保存し、Human判断を仰ぐ"
   next_steps:
     - "証拠記録を確認（iteration_001/は完了）"
     - "Iteration 2の部分成果物を確認"
     - "手動でリプラン分析を実施するか、要件を簡素化"
   evidence_dir: "Flow/202601/2026-01-02/review_loop_evidence/"
   partial_results:
     completed_tasks: ["T001"]
     partial_success_tasks: []
     failed_tasks: ["T001"]
   ```
```

**期待効果**:
- 作業の部分保存
- タイムアウト後も証拠記録は保持
- 再開可能性の提供（将来実装）

---

## 10. 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2025-12-30 | 1.0 | 初版作成（5パターン + Human-in-the-Loop + 標準形式） |
| 2026-01-02 | 2.0 | Pattern 6（Review Failure）、Pattern 7（Replan Timeout）追加（Week 8） |

---

## 関連ドキュメント

- **AgentSkills全体**: `.claude/skills/`
- **テストガイドライン**: `.claude/skills/_shared/testing_guidelines.md`（予定）
- **ベストプラクティス**: `.claude/skills/_shared/best_practices.md`（予定）

---

**Base Path**:
```
/Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/
```
