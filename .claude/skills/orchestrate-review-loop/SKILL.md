---
name: orchestrate-review-loop
description: |
  Main → SubAgent → Review → Integrationのレビューループを実行するオーケストレータースキル。

  SubAgentがドキュメントを生成して終わりではなく、Mainが要件・フレームワーク・評価基準を把握し、
  SubAgentが並列でドキュメント作成、MainがClaude Code LLMで品質レビュー、ズレがあれば即リプランして次の指示に反映します。

  「作成→レビュー→修正→統合」のループが自動で回り、ドキュメント品質70点以上を自動保証します。

  ✨ NEW: UI検証機能統合（Phase 2.5）
  - WebアプリケーションUIを5観点で自動検証（視覚品質、レスポンス速度、アクセシビリティ、ユーザビリティ、モバイル対応）
  - Chrome MCPを活用した動的テスト（スクリーンショット、レスポンス測定、キーボード操作）
  - UI品質スコア70点以上で統合OK
  - ドキュメント + UI の複合判定ロジック

  使用タイミング:
  - 複数ドキュメントを高品質で作成したい
  - レビューと修正のループを自動化したい
  - SubAgentの生成品質を保証したい
  - WebアプリケーションのUI品質も同時に検証したい

  所要時間: タスク数×35分（1タスクあたり作成10分+ドキュメントレビュー10分+UI検証15分）
  出力: 全ドキュメント + UI検証レポート + review_loop_evidence/（証拠記録）

trigger_keywords:
  - "レビューループ実行"
  - "自動レビュー実行"
  - "品質管理実行"
  - "ドキュメント並列レビュー"
  - "ドキュメントレビュー統合"

stage: Manager→SubAgent→Review→Integration
dependencies: []
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/final_summary.md
execution_time: タスク数×20分（最大3イテレーション）
priority: P1
---

# Orchestrate Review Loop Skill - ドキュメント品質保証版

Main → SubAgent → Review → Integrationのレビューループを自動実行するオーケストレーターSkill。

**Version**: 2.0（ドキュメント品質版 - Week 3.5）

---

## このSkillでできること

1. **タスク分解**: 要件を3-5個のドキュメント作成タスクに自動分解
2. **SubAgent並列実行**: Task toolで3-5エージェント同時起動
3. **自動レビュー（ドキュメント）**: Claude Code LLMで5観点評価（完全性・論理性・具体性・エビデンス・フレームワーク準拠性）
4. **✨ 自動UI検証**: Chrome MCPで5観点評価（視覚品質・レスポンス速度・アクセシビリティ・ユーザビリティ・モバイル対応）
5. **自動リプラン**: 品質スコア70点未満の場合、修正指示生成（ドキュメント・UI・両方を自動判定）
6. **証拠記録**: イテレーション別の完全トレース（quality_score, review_report, ui_verification_report, screenshots）
7. **品質保証**: ドキュメント70点以上 & UI70点以上で統合完了、3回失敗でHuman-in-the-Loop
8. **複合判定**: ドキュメントとUIの両方を評価し、どちらが不合格かを自動判定してリプラン範囲を決定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 要件ファイル、ドキュメントタイプ、品質基準（オプション） |
| **出力** | 全ドキュメント（.md） + review_loop_evidence/ |
| **次のSkill** | 統合完了 or Human介入 |

---

## Instructions

**実行モード**: 自律実行（品質ゲートで停止）
**推定所要時間**: タスク数×20分（最大3イテレーション）

### Phase 1: 要件分析・タスク分解

#### STEP 1: 要件ファイル読み込み

```markdown
## 入力例

**要件ファイル**: `{IDEA_FOLDER}/requirements.md`

```markdown
# 要件

新規プロダクト「AIタスク管理ツール」のCPF検証レポートを作成してください。

## 作成ドキュメント
- CPF判定レポート（cpf_judgment.md）
- リーンキャンバス（lean_canvas.md）
- ピッチデッキ（pitch_deck.md）

## 参照
- @startup_science/01_frameworks/cpf_validation.md
- @startup_science/02_tools/lean_canvas_template.md
```
```

#### STEP 2: タスク分解

要件を3-5個のドキュメント作成タスクに分解：

**分解基準**:
- 1タスクあたり10分以内で完了可能
- タスク間の依存関係を最小化
- 並列実行可能なタスクをグループ化

**出力例**:

```yaml
tasks:
  - id: T001
    title: "CPF判定レポート作成"
    description: "顧客セグメント、課題、解決策を含むCPF検証レポート作成"
    doc_type: "cpf_judgment"
    dependencies: []
    parallel_group: 1
    expected_files:
      - Flow/202601/2026-01-02/cpf_judgment.md
    expected_sections:
      - "顧客セグメント"
      - "課題"
      - "解決策"
      - "独自の価値提案"
      - "不公正な優位性"
      - "主要指標"
      - "チャネル"
      - "コスト構造"
      - "収益の流れ"
      - "CPFスコア"
    quality_threshold: 70

  - id: T002
    title: "リーンキャンバス作成"
    description: "CPF検証結果を元にリーンキャンバス作成"
    doc_type: "lean_canvas"
    dependencies: [T001]
    parallel_group: 2
    expected_files:
      - Flow/202601/2026-01-02/lean_canvas.md
    expected_sections:
      - "課題"
      - "ソリューション"
      - "独自の価値提案"
      - "圧倒的な優位性"
      - "顧客セグメント"
      - "既存の代替品"
      - "チャネル"
      - "収益の流れ"
      - "コスト構造"
      - "主要指標"
    quality_threshold: 70

  - id: T003
    title: "ピッチデッキ作成"
    description: "投資家向けピッチデッキ作成"
    doc_type: "pitch_deck"
    dependencies: [T001, T002]
    parallel_group: 3
    expected_files:
      - Flow/202601/2026-01-02/pitch_deck.md
    expected_sections:
      - "タイトル"
      - "課題"
      - "ソリューション"
      - "市場規模"
      - "ビジネスモデル"
      - "トラクション"
      - "競合優位性"
      - "チーム"
      - "資金調達"
    quality_threshold: 70
```

#### STEP 2.5: 証拠記録ディレクトリの作成

**実行**: Bash tool（mkdir -p）

**ディレクトリ構造**:
```
Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/
├── iteration_001/
│   ├── task_breakdown.md              # STEP 2.6で作成
│   ├── subagent_001_output.md         # STEP 3.5で作成
│   ├── subagent_002_output.md
│   ├── subagent_003_output.md
│   ├── quality_score_001.json         # Review Agentが作成
│   ├── review_report_001.md           # Review Agentが作成
│   └── decision_001.md                # STEP 5.5で作成
```

**コマンド例**:
```bash
mkdir -p "Flow/202601/2026-01-02/review_loop_evidence/iteration_001"
```

#### STEP 2.6: task_breakdown.mdの保存

**実行**: Write tool

**パス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/iteration_001/task_breakdown.md`

**内容**: STEP 2で生成したタスク分解結果をそのまま保存

**フォーマット例**:
```markdown
# Task Breakdown - Iteration 1

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

...（以下省略）
```

---

### Phase 2: SubAgent並列実行

#### STEP 3: 並列グループ別にSubAgent起動

**並列グループ1**（依存関係なし）:
- Task tool でT001を起動（model: sonnet, subagent_type: general-purpose）

**並列グループ2**（T001完了後）:
- Task tool でT002を起動（model: sonnet, subagent_type: general-purpose）

**並列グループ3**（T002完了後）:
- Task tool でT003を起動（model: sonnet, subagent_type: general-purpose）

**SubAgentへの指示例**:

```markdown
## タスク: T001 - CPF判定レポート作成

### 要件
AIタスク管理ツールのCPF検証レポートを作成してください。

### 必須セクション
1. 顧客セグメント: ターゲットユーザーを明確化
2. 課題: 解決すべき課題を具体的に記述
3. 解決策: ソリューションの概要
4. 独自の価値提案: 他との差別化ポイント
5. 不公正な優位性: 模倣困難な要素
6. 主要指標: 検証すべきKPI
7. チャネル: 顧客獲得経路
8. コスト構造: 主要なコスト項目
9. 収益の流れ: 収益化方法
10. CPFスコア: 評価結果（60点以上推奨）

### 品質基準
- 完全性: 全セクション含めること（25点）
- 論理性: 矛盾のない論理構成（25点）
- 具体性: 数値・固有名詞・事例を含めること（20点）
- エビデンス: データ・出典を明記（15点）
- フレームワーク準拠性: スタートアップサイエンス準拠（15点）
- **合計70点以上**

### 参照
- @startup_science/01_frameworks/cpf_validation.md
- @.claude/skills/_shared/review_criteria.md

### 出力先
Flow/202601/2026-01-02/cpf_judgment.md
```

#### STEP 3.5: SubAgent出力の証拠記録保存

**実行**: Read tool（SubAgent出力を読み込み）+ Write tool（証拠記録に保存）

**処理フロー**:
1. SubAgentが生成したドキュメントをReadツールで読み込み
2. 証拠記録ディレクトリに`subagent_{NNN}_output.md`として保存

**例**:
- **読み込み元**: `Flow/202601/2026-01-02/cpf_judgment.md`
- **保存先**: `Flow/202601/2026-01-02/review_loop_evidence/iteration_001/subagent_001_output.md`

**コマンド例**（擬似コード）:
```python
# Task 001の出力を読み込み
cpf_judgment_content = Read("Flow/202601/2026-01-02/cpf_judgment.md")

# 証拠記録に保存
Write(
    "Flow/202601/2026-01-02/review_loop_evidence/iteration_001/subagent_001_output.md",
    cpf_judgment_content
)

# Task 002, 003も同様に処理
```

**注意点**:
- SubAgentの出力をそのままコピー（編集しない）
- タスクID（001, 002, 003...）と対応させる
- 全SubAgent完了後にまとめて保存

---

### Phase 2.5: UI Verification（Task tool） - ✨ NEW

**目的**: SubAgentが生成したドキュメントと並行して、WebアプリケーションのUI品質を自動検証します。

**実行タイミング**: Phase 2（SubAgent実行）完了後、Phase 3（Review Agent）と並列実行可能

**適用条件**: 要件にWebアプリケーションUIが含まれる場合のみ実行

#### STEP 3.7: UI Verification Agent起動（Task tool）

**実行**: Task tool（subagent_type: general-purpose, model: sonnet）

**前提条件**:
- テスト対象URLが指定されている（例: `http://localhost:3000`、`https://staging.example.com`）
- Chrome拡張MCPサーバーが接続可能
- WebアプリケーションがUIを持つプロジェクト

**UI Verification Agentへの指示**:

```markdown
## タスク: WebアプリケーションUI品質検証

### 検証対象
- テスト対象URL: {target_url}
- プロジェクト名: {project_name}
- イテレーション: {iteration}

### 検証内容

@.claude/agents/ui-verification-agent.md の仕様に従い、以下のUI品質を検証してください。

#### 検証シナリオ（5パターン実行）

`.claude/config/ui_verification.json` から以下のシナリオを読み込み、順次実行：

1. **ログインフロー検証** - ログインフォームの入力・送信・成功/失敗時の挙動
2. **フォームバリデーション検証** - 必須フィールド、形式チェックの動作
3. **レスポンシブデザイン検証** - 3つのブレークポイント（モバイル、タブレット、デスクトップ）での表示
4. **キーボードナビゲーション検証** - Tab/Enter/Escapeキーでの操作可能性
5. **エラーハンドリング検証** - エラーメッセージの品質と回復手段の提示

#### 評価基準（5観点・100点満点）

1. **視覚品質**（25点満点）
   - レイアウト一貫性（10点）
   - 配色とコントラスト（8点）- WCAG AA準拠
   - タイポグラフィ（7点）

2. **レスポンス速度**（20点満点）
   - ページ読み込み（10点）- 2秒以内目標
   - インタラクション反応（6点）- 100ms以内目標
   - アニメーション（4点）- 60fps目標

3. **アクセシビリティ**（20点満点）
   - ARIA属性（8点）
   - キーボード操作（8点）
   - セマンティックHTML（4点）

4. **ユーザビリティ**（20点満点）
   - ナビゲーション（8点）
   - エラーハンドリング（6点）
   - フィードバック（6点）

5. **モバイル対応**（15点満点）
   - レスポンシブレイアウト（8点）
   - タッチターゲット（4点）- 44x44px推奨
   - モバイル最適化（3点）

**合計70点以上で統合OK**

### 出力先

以下の2ファイルを生成してください：

1. **quality_score.json**:
   `{evidence_dir}/iteration_{iteration:03d}/ui_quality_score.json`

```json
{
  "total_score": 82,
  "visual_quality_score": 22,
  "response_speed_score": 16,
  "accessibility_score": 14,
  "usability_score": 18,
  "mobile_support_score": 12,
  "pass": true,
  "grade": "A",
  "timestamp": "2026-01-03T10:30:00Z"
}
```

2. **ui_verification_report.md**:
   `{evidence_dir}/iteration_{iteration:03d}/ui_verification_report.md`

   詳細レポート（スクリーンショット付き、問題点と推奨事項を含む）

### タイムアウト設定

15分（900,000ミリ秒）

### エラーハンドリング

- Chrome拡張接続エラー: 再試行3回、失敗時はUI検証スキップ（ドキュメントレビューのみ実行）
- タイムアウトエラー: UI検証スキップ、警告ログ出力
- 要素検出エラー: 該当シナリオのみスキップ、他シナリオ継続

### 参照

- @.claude/agents/ui-verification-agent.md（仕様書502行）
- @.claude/config/ui_verification.json（検証シナリオ定義）
- @.claude/skills/verify-ui-quality/SKILL.md（UIスキル詳細）
```

**Task tool実行例**:

```python
# UI Verification Agent起動
ui_verification_result = Task(
    description=f"UI品質検証 - Iteration {iteration}",
    prompt=f"""
    @.claude/agents/ui-verification-agent.md の仕様に従い、WebアプリケーションのUIを検証してください。

    **テスト対象URL**: `{target_url}`
    **出力先**: `{evidence_dir}/iteration_{iteration:03d}/`
    **検証シナリオ**: 全5シナリオ実行

    詳細は上記「UI Verification Agentへの指示」を参照してください。
    """,
    subagent_type="general-purpose",
    model="sonnet",
    timeout=900000  # 15分
)

# UI品質スコアの取得
ui_quality_score = parse_ui_quality_score(
    evidence_dir=evidence_dir,
    iteration=iteration
)
```

#### STEP 3.8: UI検証結果の証拠記録保存

**実行**: Read tool + Write tool

**処理フロー**:
1. UI Verification Agentが生成した2ファイルをReadツールで読み込み
2. 証拠記録ディレクトリに保存済みであることを確認
3. `ui_quality_score.json`からスコアを抽出

**保存先**:
- `{evidence_dir}/iteration_{iteration:03d}/ui_quality_score.json`（UI Verification Agentが直接保存）
- `{evidence_dir}/iteration_{iteration:03d}/ui_verification_report.md`（UI Verification Agentが直接保存）
- `{evidence_dir}/iteration_{iteration:03d}/screenshots/`（スクリーンショット群）

**スコア抽出例**:

```python
import json
from pathlib import Path

# UI品質スコア読み込み
ui_score_path = Path(evidence_dir) / f"iteration_{iteration:03d}" / "ui_quality_score.json"

if ui_score_path.exists():
    with open(ui_score_path, "r") as f:
        ui_score_data = json.load(f)

    ui_total_score = ui_score_data["total_score"]
    ui_pass = ui_score_data["pass"]
    ui_grade = ui_score_data.get("grade", "N/A")

    # ログ出力
    print(f"✅ UI Quality Score: {ui_total_score}/100 ({ui_grade}), Pass: {ui_pass}")
else:
    print("⚠️ UI検証スキップ: ui_quality_score.json が見つかりません")
    ui_total_score = None
    ui_pass = True  # UI検証なしの場合は自動的にパス扱い
```

**証拠記録ディレクトリ構造**:
```
Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/iteration_{NNN}/
├── task_breakdown.md              # SubAgent分解計画
├── subagent_001_output.md         # ドキュメント生成結果
├── quality_score_001.json         # Document Review結果
├── review_report_001.md           # Document Review詳細
├── ui_quality_score.json          # ✨ UI Verification結果（新規）
├── ui_verification_report.md      # ✨ UI Verification詳細（新規）
├── screenshots/                   # ✨ UI検証スクリーンショット（新規）
│   ├── 01_desktop_initial.png
│   ├── 02_desktop_navigation.png
│   ├── 03_desktop_form_error.png
│   ├── 04_tablet_768x1024.png
│   ├── 05_mobile_375x667.png
│   ├── 06_keyboard_focus.png
│   └── 07_modal_dialog.png
└── decision_001.md                # 統合判定記録
```

#### STEP 3.9: UI検証スキップ判定

**条件**: 以下のいずれかに該当する場合、UI検証をスキップ

1. テスト対象URLが指定されていない
2. プロジェクトがWebアプリケーションではない（CLIツール、ライブラリ等）
3. Chrome拡張接続エラーが3回連続失敗

**スキップ時の処理**:

```python
if not target_url or not is_web_application:
    print("ℹ️ UI検証をスキップ: Webアプリケーションではありません")
    ui_total_score = None
    ui_pass = True  # UI検証なしの場合は自動的にパス扱い
elif chrome_extension_connection_failed:
    print("⚠️ UI検証をスキップ: Chrome拡張接続エラー")
    ui_total_score = None
    ui_pass = True
else:
    # 正常にUI検証実行
    ui_total_score = parse_ui_quality_score(evidence_dir, iteration)
    ui_pass = ui_total_score >= 70
```

---

### Phase 3: Review Agent起動（Task tool）

#### STEP 4: Review AgentをTask toolで起動

**実行**: Task tool（subagent_type: general-purpose, model: sonnet）

**Review Agentへの指示**:

```markdown
## タスク: T001ドキュメントのレビュー

### レビュー対象
- ドキュメント: Flow/202601/2026-01-02/cpf_judgment.md
- ドキュメントタイプ: cpf_judgment

### レビュー観点（5観点・100点満点）

#### 1. 完全性チェック（25点満点）

必須セクション10件の有無を確認：
- Readツールでドキュメント読み込み
- Markdown見出し（`## セクション名`）を抽出
- 必須セクションリストと照合（@.claude/skills/_shared/review_criteria.md参照）
- completeness_score = (found / required) * 25

#### 2. 論理性チェック（25点満点）

Claude Code LLMで直接評価：
- 文書内に矛盾がないか
- 主張に対する根拠が明確か
- 結論が前提から適切に導かれているか
- logic_score = LLM評価（0-25点）

#### 3. 具体性チェック（20点満点）

Claude Code LLMで直接評価：
- 具体的な数値が含まれているか
- 固有名詞（企業名、製品名、技術名）が含まれているか
- 具体的な事例が含まれているか
- specificity_score = LLM評価（0-20点）

#### 4. エビデンスチェック（15点満点）

Claude Code LLMで直接評価：
- 主張がデータに基づいているか
- 出典・参照が明記されているか
- 定量的なデータが含まれているか
- evidence_score = LLM評価（0-15点）

#### 5. フレームワーク準拠性チェック（15点満点）

Claude Code LLMで直接評価：
- CPF/PSF/PMF検証の評価軸が適切か
- Lean Startupのフレームワークに準拠しているか
- スタートアップサイエンス（馬田隆明）に準拠しているか
- framework_compliance_score = LLM評価（0-15点）

### 出力

#### quality_score.json
```json
{
  "total_score": 74,
  "completeness_score": 20,
  "logic_score": 18,
  "specificity_score": 14,
  "evidence_score": 10,
  "framework_compliance_score": 12,
  "passed": true,
  "threshold": 70,
  "issues": [...]
}
```

#### review_report.md
Markdown形式のレビューレポート（詳細は@.claude/agents/review-agent.md参照）

### 参照
- @.claude/agents/review-agent.md（Review Agent定義）
- @.claude/skills/_shared/review_criteria.md（品質基準）
```

**保存先**:
- `{IDEA_FOLDER}/review_loop_evidence/iteration_001/quality_score_001.json`
- `{IDEA_FOLDER}/review_loop_evidence/iteration_001/review_report_001.md`

#### STEP 4.5: Task tool実装例（Week 1完了）

**実際のTask tool呼び出しパターン**:

```python
# Review AgentをTask tool経由で起動
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
    model="sonnet"
)
```

**パラメータ説明**:
- `document_path`: レビュー対象ドキュメントの絶対パス
  - 例: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/cpf_judgment.md`
- `doc_type`: ドキュメントタイプ
  - 例: `cpf_judgment`, `lean_canvas`, `pitch_deck`
- `iteration`: 現在のイテレーション番号（1, 2, 3）
- `evidence_dir`: 証拠記録ルートディレクトリ
  - 例: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-03/review_loop_evidence`

**リトライループ実装例**:

```python
MAX_RETRIES = 3
QUALITY_THRESHOLD = 70

for iteration in range(1, MAX_RETRIES + 1):
    # STEP 3: SubAgent並列実行
    results = execute_subagents_parallel(tasks)

    # STEP 3.5: 証拠記録保存
    save_subagent_outputs(results, iteration)

    # STEP 4: Review Agent起動
    review_reports = []
    for task in tasks:
        review_result = Task(
            description=f"品質レビュー - {task['title']} (イテレーション {iteration})",
            prompt=generate_review_prompt(task, iteration, evidence_dir),
            subagent_type="general-purpose",
            model="sonnet"
        )
        review_reports.append(review_result)

    # STEP 5: 統合可否判定
    all_passed = True
    for i, review in enumerate(review_reports):
        quality_score = parse_quality_score(review, tasks[i]['id'], iteration, evidence_dir)

        if quality_score < QUALITY_THRESHOLD:
            all_passed = False
            # STEP 5.5: リプラン必須の判定記録
            save_decision(tasks[i], quality_score, "REPLAN", iteration, evidence_dir)
        else:
            # STEP 5.5: 統合完了の判定記録
            save_decision(tasks[i], quality_score, "INTEGRATE", iteration, evidence_dir)

    if all_passed:
        # 全タスク合格 → 統合完了
        integrate_and_finalize(results)
        return "SUCCESS"

    if iteration == MAX_RETRIES:
        # 3回失敗 → Human-in-the-Loop
        return trigger_human_intervention(review_reports, iteration)

    # リプラン実行
    # STEP 6: 問題分析
    replan_instructions = analyze_and_replan(review_reports, iteration)

    # STEP 7: タスク更新
    tasks = update_tasks_with_replan(tasks, replan_instructions)
```

**タイムアウト設定**:
- SubAgent実行: 30分/タスク
- Review Agent: 10分
- リプラン生成: 10分
- 1イテレーション合計: 最大50分

---

### Phase 4: 統合判定

#### STEP 5: 統合可否判定（Document + UI 複合判定） - ✨ UPDATED

**判定基準**:

| ドキュメントスコア | UIスコア | 判定 | 対応 |
|----------------|---------|------|------|
| 70点以上 | 70点以上 | ✅ 合格 | 統合完了（高品質） |
| 60-69点 | 60-69点 | ⚠️ 条件付き合格 | 警告ログ記録 + 統合 |
| 70点以上 | 60-69点 | ⚠️ 条件付き合格 | UI改善推奨 + 統合 |
| 60-69点 | 70点以上 | ⚠️ 条件付き合格 | ドキュメント改善推奨 + 統合 |
| 60点未満 | -（任意） | ❌ 不合格 | ドキュメントリプラン必須 |
| -（任意） | 60点未満 | ❌ 不合格 | UIリプラン必須 |
| UI検証スキップ | - | ℹ️ ドキュメントのみ | UIスコアを無視して判定 |

**複合判定ロジック**:

```python
def integrate_decision(document_score, ui_score, ui_skipped=False):
    """
    ドキュメントとUIの複合判定

    Returns:
        - "SUCCESS": 統合完了（高品質）
        - "SUCCESS_WITH_WARNING": 条件付き統合（警告あり）
        - "REPLAN_DOCUMENT": ドキュメントリプラン必須
        - "REPLAN_UI": UIリプラン必須
        - "REPLAN_BOTH": 両方リプラン必須
    """
    # UI検証スキップの場合
    if ui_skipped:
        if document_score >= 70:
            return "SUCCESS"
        elif document_score >= 60:
            return "SUCCESS_WITH_WARNING"
        else:
            return "REPLAN_DOCUMENT"

    # 両方が70点以上 → 統合完了（高品質）
    if document_score >= 70 and ui_score >= 70:
        return "SUCCESS"

    # 両方が60点以上 → 条件付き統合
    if document_score >= 60 and ui_score >= 60:
        return "SUCCESS_WITH_WARNING"

    # ドキュメントのみ60点未満 → ドキュメントリプラン
    if document_score < 60 and ui_score >= 60:
        return "REPLAN_DOCUMENT"

    # UIのみ60点未満 → UIリプラン
    if document_score >= 60 and ui_score < 60:
        return "REPLAN_UI"

    # 両方60点未満 → 両方リプラン
    if document_score < 60 and ui_score < 60:
        return "REPLAN_BOTH"
```

**合格の場合**:
- STEP 5.5で統合完了の判定記録を保存（Document + UI の両スコア記載）
- STEP 8でfinal_summary.md生成（UIスコア含む）
- 完了

**不合格の場合**:
- STEP 5.5でリプラン必須の判定記録を保存（どちらが不合格かを明記）
- Iteration 2へ進む（Phase 5: リプラン）
  - **ドキュメントリプラン**: SubAgent再実行（ドキュメント品質70点未満の場合）
  - **UIリプラン**: UI改善 + 再検証（UI品質60点未満の場合）
  - **両方リプラン**: 両方を並列実行（両方が基準未達の場合）

**リプラン判定の詳細**:

```python
def determine_replan_scope(document_score, ui_score, ui_skipped):
    """
    リプラン範囲の判定

    Returns:
        - "DOCUMENT_ONLY": ドキュメントのみリプラン
        - "UI_ONLY": UIのみリプラン
        - "BOTH": 両方リプラン
        - "NONE": リプラン不要（統合完了）
    """
    # UI検証スキップの場合
    if ui_skipped:
        if document_score < 70:
            return "DOCUMENT_ONLY"
        else:
            return "NONE"

    # 両方が基準未達
    if document_score < 70 and ui_score < 60:
        return "BOTH"

    # ドキュメントのみ基準未達
    if document_score < 70:
        return "DOCUMENT_ONLY"

    # UIのみ基準未達
    if ui_score < 60:
        return "UI_ONLY"

    # 両方とも合格
    return "NONE"
```

**リプラン実行フロー**:

| リプラン範囲 | 実行内容 | 推定時間 |
|------------|---------|---------|
| DOCUMENT_ONLY | SubAgent再実行（修正指示付き） | 20分 |
| UI_ONLY | UI改善 + UI Verification Agent再実行 | 25分 |
| BOTH | SubAgent + UI Verification Agent並列実行 | 30分 |

#### STEP 5.5: 判定記録の保存（decision_{NNN}.md）

**実行**: Write tool

**パス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/iteration_{NNN}/decision_{NNN}.md`

**内容**:

**統合完了の場合（UIスコア含む）**:
```markdown
# Decision Record - Iteration 1

**判定日時**: 2026-01-02 15:35:00
**判定者**: Manager Skill (orchestrate-review-loop)

## 判定結果

**決定**: 統合完了（Integration）

**理由**:
- **ドキュメント品質スコア**: 74点 ≥ 閾値 70点 ✅
- **UI品質スコア**: 72点 ≥ 閾値 70点 ✅
- すべての必須セクションが存在（90%以上）
- 論理的整合性に重大な矛盾なし
- UIの視覚品質・アクセシビリティ・ユーザビリティが基準を満たす

## 品質スコア詳細

### ドキュメント品質（74点）
| 項目 | スコア | 満点 |
|------|--------|------|
| 完全性 | 20 | 25 |
| 論理性 | 18 | 25 |
| 具体性 | 14 | 20 |
| エビデンス | 10 | 15 |
| フレームワーク準拠性 | 12 | 15 |

### UI品質（72点）
| 項目 | スコア | 満点 |
|------|--------|------|
| 視覚品質 | 19 | 25 |
| レスポンス速度 | 16 | 20 |
| アクセシビリティ | 14 | 20 |
| ユーザビリティ | 15 | 20 |
| モバイル対応 | 11 | 15 |

## 次のアクション

1. cpf_judgment.mdをStockフォルダに移動
2. final_summary.mdを生成（UIスコア含む）
3. レビューループ完了

## 推奨改善（オプショナル）

### ドキュメント
- 「不公正な優位性」セクションを追加
- 市場規模の出典を明記
- 抽象的な表現を具体的な数値に置き換え

### UI
- 本文の行間を1.5以上に設定（現在1.2）
- リンクテキストのコントラスト比を4.5:1以上に改善（現在3.8:1）
- タップターゲットを44x44px以上に拡大（3つのボタンが基準未達）

**補足**: 推奨改善は次回のイテレーションで反映可能（今回は統合完了）
```

**リプラン必須の場合（UIスコア含む）**:
```markdown
# Decision Record - Iteration 1

**判定日時**: 2026-01-02 15:35:00
**判定者**: Manager Skill (orchestrate-review-loop)

## 判定結果

**決定**: リプラン必須（Replan Required）

**理由**:
- **ドキュメント品質スコア**: 56点 < 閾値 70点 ❌
- **UI品質スコア**: 58点 < 閾値 60点 ❌
- **リプラン範囲**: BOTH（ドキュメント + UI両方）

## 品質スコア詳細

### ドキュメント品質（56点 < 70点） ❌
| 項目 | スコア | 満点 | 状態 |
|------|--------|------|------|
| 完全性 | 18 | 25 | ⚠️ WARNING |
| 論理性 | 12 | 25 | ❌ FAIL |
| 具体性 | 10 | 20 | ⚠️ WARNING |
| エビデンス | 6 | 15 | ❌ FAIL |
| フレームワーク準拠性 | 10 | 15 | ⚠️ WARNING |

### UI品質（58点 < 60点） ❌
| 項目 | スコア | 満点 | 状態 |
|------|--------|------|------|
| 視覚品質 | 14 | 25 | ❌ FAIL |
| レスポンス速度 | 12 | 20 | ⚠️ WARNING |
| アクセシビリティ | 10 | 20 | ❌ FAIL |
| ユーザビリティ | 12 | 20 | ⚠️ WARNING |
| モバイル対応 | 8 | 15 | ❌ FAIL |

## 問題分析

### ドキュメント問題

#### Pattern 2: 論理的矛盾
**問題箇所**: CPFスコア算出ロジック
**矛盾内容**: 「市場規模が小さい」と言いながら「急成長市場」と主張
**修正指示**: 市場規模の定義を明確化し、成長率との関係を整理

#### Pattern 4: エビデンス不足
**問題箇所**: 市場規模推定セクション
**不足内容**: 出典・データソースの明記なし
**修正指示**: 総務省調査、McKinsey Report等の公的データを引用

### UI問題

#### 視覚品質（14/25点）
**問題箇所**: レイアウト一貫性、配色
**問題内容**:
- ヘッダーとコンテンツ間のマージンが不均一（16px vs 32px）
- リンクテキストのコントラスト比2.8:1（推奨4.5:1以上）
**修正指示**: CSSグリッドシステムの導入、WCAG AA準拠の配色に変更

#### アクセシビリティ（10/20点）
**問題箇所**: ARIA属性、キーボード操作
**問題内容**:
- メインナビゲーションにrole="navigation"が未設定
- 画像の代替テキスト（alt属性）が5件不足
- フォーカスインジケーターが不明瞭
**修正指示**: ARIA属性の追加、alt属性の設定、:focus-visibleスタイルの追加

#### モバイル対応（8/15点）
**問題箇所**: レスポンシブデザイン、タッチターゲット
**問題内容**:
- タブレットサイズ（768px）で横スクロールが発生
- 5つのボタンが44x44px未満（最小32x32px）
**修正指示**: メディアクエリの調整、ボタンサイズの拡大

## 次のアクション

1. Iteration 2を開始
2. **ドキュメント**: SubAgentに修正指示を追加
3. **UI**: UI改善 + UI Verification Agent再実行
4. タスク分解を更新（task_breakdown_updated.md）
5. 両方を並列実行（推定30分）
```

---

### Phase 5: リプラン（不合格時のみ）

#### STEP 6: 問題分析

**リプランパターン判定**:

```yaml
# Pattern 1: セクション不足
条件: completeness_score < 15
原因: 必須セクションの理解不足
修正指示: 未実装セクションを具体例付きで指示

# Pattern 2: 論理的矛盾
条件: logic_score < 15
原因: 論理の飛躍、矛盾した主張
修正指示: 矛盾箇所を明示、修正案提示

# Pattern 3: 抽象的表現
条件: specificity_score < 12
原因: 具体的なデータ・事例不足
修正指示: 具体的な数値・事例を要求

# Pattern 4: エビデンス不足
条件: evidence_score < 9
原因: データ裏付け・出典不明
修正指示: データ・出典の追加を指示

# Pattern 5: フレームワーク逸脱
条件: framework_compliance_score < 9
原因: スタートアップサイエンスの理解不足
修正指示: フレームワーク基準を明示
```

**出力例**:

```markdown
# Replan Analysis - Iteration 2

**原因パターン**: Pattern 4（エビデンス不足）

**問題詳細**:
- evidence_score: 6点（目標: 9点以上）
- 問題箇所:
  - 市場規模の出典が不明
  - 競合分析のデータソースが不明
  - CPFスコアの算出根拠が不明

**修正指示**:
1. 市場規模に出典を追加（総務省、McKinsey等の信頼できるソース）
2. 競合分析に具体的なデータソースを明記
3. CPFスコアの算出根拠を明示（6項目中何項目合格か）
```

#### STEP 6.5: リプラン分析の保存（replan_analysis.md）

**実行**: Write tool

**パス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/iteration_{NNN}/replan_analysis.md`

**内容**: STEP 6で生成したリプラン分析結果をそのまま保存

**フォーマット**: 上記の出力例を参照

**注意点**:
- リプラン時（Iteration 2以降）のみ生成
- Iteration 1では生成しない
- 次のイテレーションのディレクトリに保存（例: iteration_002/replan_analysis.md）

#### STEP 7: SubAgent再実行

修正指示を含めてSubAgentを再起動（Iteration 2）

**処理フロー**:
1. STEP 2.5: 新しいイテレーションディレクトリを作成（iteration_002/）
2. STEP 2.6: 更新されたtask_breakdown.mdを保存（task_breakdown_updated.md）
3. STEP 3: SubAgent再実行（修正指示を追加）
4. STEP 3.5: SubAgent出力を証拠記録に保存（subagent_001_output.md）
5. STEP 4: Review Agent再起動
6. STEP 5: 統合可否判定
7. STEP 5.5: 判定記録を保存（decision_002.md）

**リトライ上限**: 3回まで（3回失敗でHuman-in-the-Loop）

---

### Phase 6: リトライループ（最大3回）

```python
MAX_RETRIES = 3

for iteration in range(1, MAX_RETRIES + 1):
    # タスク分解（初回のみ）
    if iteration == 1:
        tasks = decompose_tasks(requirements)

    # SubAgent並列実行（Task tool）
    results = []
    for task in tasks:
        result = Task(
            description=f"ドキュメント作成: {task.title}",
            prompt=generate_prompt(task),
            subagent_type="general-purpose",
            model="sonnet"
        )
        results.append(result)

    # Review Agent起動（Task tool）
    review_reports = []
    for task, result in zip(tasks, results):
        review_report = Task(
            description=f"レビュー: {task.title}",
            prompt=generate_review_prompt(task, result),
            subagent_type="general-purpose",
            model="sonnet"
        )
        review_reports.append(review_report)

    # 判定
    if all(report.total_score >= 70 for report in review_reports):
        # 統合完了
        integrate_and_finalize(results)
        return "SUCCESS"

    # リトライ上限チェック
    if iteration == MAX_RETRIES:
        # Human-in-the-Loop
        return trigger_human_intervention(review_reports)

    # リプラン
    replan_instructions = manager_skill.replan(review_reports)
    tasks = update_tasks_with_replan(tasks, replan_instructions)
```

---

### Phase 7: 完了処理（統合完了時）

#### STEP 8: final_summary.md の生成

**実行**: Write tool

**パス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/final_summary.md`

**内容**:

```markdown
# Final Summary - Review Loop Completed

**完了日時**: 2026-01-02 16:00:00
**タスク**: CPF判定レポート作成、リーンキャンバス作成、ピッチデッキ作成
**総イテレーション数**: 2回

## 成果物

| ドキュメント | 最終スコア（Doc） | 最終スコア（UI） | 判定 | 保存先 |
|------------|-----------------|----------------|------|--------|
| cpf_judgment.md | 74点 | N/A | ✅ 合格 | Stock/programs/.../documents/1_initiating/ |
| lean_canvas.md | 82点 | N/A | ✅ 合格 | Stock/programs/.../documents/2_discovery/ |
| pitch_deck.md | 78点 | 72点 | ✅ 合格 | Stock/programs/.../documents/3_planning/ |

**注**: pitch_deck.mdはWebアプリケーション実装を含むため、UI検証を実施

## イテレーション履歴

### Iteration 1
- **実行時間**: 40分（ドキュメント25分 + UI検証15分）
- **結果**: 不合格
  - ドキュメント: 56点 < 70点 ❌
  - UI: 58点 < 60点 ❌
- **主な問題**:
  - ドキュメント: 論理的矛盾、エビデンス不足
  - UI: 視覚品質不足、アクセシビリティ問題、モバイル対応不足
- **対応**: 両方リプラン実施

### Iteration 2
- **実行時間**: 45分（ドキュメント30分 + UI検証15分）
- **結果**: 合格
  - ドキュメント: 74点 ≥ 70点 ✅
  - UI: 72点 ≥ 70点 ✅
- **改善点**:
  - ドキュメント: 市場規模データ追加、論理的整合性確保
  - UI: CSSグリッド導入、ARIA属性追加、レスポンシブ改善

## 品質スコア推移

### ドキュメント品質
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

### UI品質（pitch_deck.md）
```
Iteration 1: 58点 → Iteration 2: 72点（+14点改善）
```

| 項目 | Iter 1 | Iter 2 | 改善 |
|------|--------|--------|------|
| 視覚品質 | 14点 | 19点 | +5 |
| レスポンス速度 | 12点 | 16点 | +4 |
| アクセシビリティ | 10点 | 14点 | +4 |
| ユーザビリティ | 12点 | 15点 | +3 |
| モバイル対応 | 8点 | 11点 | +3 |

## 主要な学び

### ドキュメント品質
1. **市場規模の定義**: TAM/SAM/SOMの区別が重要
2. **エビデンスの重要性**: 公的データソースの引用が信頼性を向上
3. **論理的整合性**: 矛盾する主張を避けるための慎重な記述

### UI品質
1. **アクセシビリティファースト**: ARIA属性・alt属性の設定は最初から実装すべき
2. **レスポンシブ設計の重要性**: タブレットサイズのテスト不足が問題を引き起こした
3. **WCAG準拠の配色**: コントラスト比4.5:1以上を最初から考慮すべき
4. **タッチターゲット**: モバイル対応では44x44px以上が必須

## 証拠記録

- **イテレーション1**: `iteration_001/`
  - ドキュメント: `quality_score_001.json`, `review_report_001.md`
  - UI: `ui_quality_score.json`, `ui_verification_report.md`, `screenshots/`
- **イテレーション2**: `iteration_002/`
  - ドキュメント: `quality_score_002.json`, `review_report_002.md`
  - UI: `ui_quality_score.json`, `ui_verification_report.md`, `screenshots/`

## 次のアクション

1. cpf_judgment.md、lean_canvas.md、pitch_deck.mdをStockフォルダに移動
2. プロジェクト憲章を更新（CPF検証完了を記録、UI品質70点以上を達成）
3. 次フェーズ（PSF検証）の準備
4. UIスクリーンショットをプロジェクトドキュメントに添付
```

**生成タイミング**: 統合完了判定後、すべてのドキュメントが合格した時点

**注意点**:
- イテレーション数は実際の回数を記録
- 品質スコア推移はすべてのイテレーションを含める
- 主要な学びは自動生成ではなく、Manager Skillが分析して記述

---

## 成果物

### 最終成果物一覧

```
{IDEA_FOLDER}/
├── review_loop_evidence/
│   ├── iteration_001/
│   │   ├── task_分解.md
│   │   ├── subagent_001_output.md
│   │   ├── subagent_002_output.md
│   │   ├── subagent_003_output.md
│   │   ├── quality_score_001.json
│   │   └── review_report_001.md
│   ├── iteration_002/（リプラン時のみ）
│   │   ├── replan_analysis.md
│   │   ├── subagent_001_output.md（修正版）
│   │   ├── quality_score_002.json
│   │   └── review_report_002.md
│   └── final_summary.md
├── cpf_judgment.md
├── lean_canvas.md
└── pitch_deck.md
```

---

## Knowledge Base参照

- **Review Agent定義**: `.claude/agents/review-agent.md`（ドキュメント品質レビュー）
- **✨ UI Verification Agent定義**: `.claude/agents/ui-verification-agent.md`（UI品質検証）
- **ドキュメント品質基準**: `.claude/skills/_shared/review_criteria.md`（Week 3.5で作成）
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`
- **並列実行ルール**: `.claude/rules/parallel_execution.md`
- **レビューループ制御**: `.claude/rules/review_loop.md`
- **リプランパターン**: `.claude/skills/_shared/replan_patterns.md`（Week 5で作成）
- **UI検証実装ガイド**: `@docs/implementation_guides/week1_ui_testing.md`（Week 1実装ガイド）

---

## 使用例

```
User: /orchestrate-review-loop

Skill: 要件ファイルのパスを入力してください:

User: aipm_v0/Flow/202601/2026-01-02/requirements.md

Skill:
# レビューループ実行開始

要件: AIタスク管理ツールのCPF検証ドキュメント作成
推定所要時間: 60分（3タスク×20分）

## STEP 1: タスク分解 ✅ 完了
- T001: CPF判定レポート作成
- T002: リーンキャンバス作成
- T003: ピッチデッキ作成

## STEP 2: SubAgent並列実行（並列グループ1） ✅ 完了（10分）
- T001: cpf_judgment.md 生成完了

## STEP 3: Review Agent起動 ✅ 完了（10分）
- 完全性: 20/25点（未実装セクション1件: 不公正な優位性）
- 論理性: 18/25点（スコア算出根拠が不明確）
- 具体性: 14/20点（抽象的な表現2件）
- エビデンス: 10/15点（出典不明3件）
- フレームワーク準拠性: 12/15点（PSF評価が弱い）
- 品質スコア: 74点

【判定】✅ 合格（74点 ≥ 70点）

## STEP 2-3繰り返し: T002, T003実行

[... 同様に実行 ...]

## レビューループ完了

総所要時間: 60分
総合判定: ✅ 全タスク合格
統合完了:
  - cpf_judgment.md
  - lean_canvas.md
  - pitch_deck.md

証拠記録: Flow/202601/2026-01-02/review_loop_evidence/
```

---

## 注意事項

### 実装状況（Week 3.5完了）

**実装完了**:
- タスク分解ロジック（STEP 1-2）
- Review Agent定義（5観点評価）
- ドキュメント品質基準定義

**未実装**（Week 4以降）:
- SubAgent並列実行の自動化
- Review Agentの完全自動化
- 証拠記録システム
- リプランロジックの完全実装
- リトライループの完全実装

### Human-in-the-Loop

3回のリトライ後も品質スコア70点未満の場合、必ず停止しユーザー判断を仰ぐ：

```markdown
## ⚠️ Human-in-the-Loop: ユーザー判断が必要です

**状況**: 3回のリトライ後も品質スコア70点未満

### 失敗理由
- Iteration 1: evidence_score 6点（エビデンス不足）
- Iteration 2: logic_score 12点（論理的矛盾）
- Iteration 3: completeness_score 10点（セクション不足）

### 推奨アクション
1. **手動修正** - 不足箇所を手動で追記
2. **要件見直し** - 要件が不明確な可能性あり
3. **中断** - 別の方法を検討

どの選択肢を選びますか？（番号で回答: 1/2/3）
```

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-02 | 0.1 | 初版作成（Week 1: タスク分解のみ） |
| 2026-01-02 | 2.0 | ドキュメント品質レビュー版に完全刷新（Week 3.5） |
