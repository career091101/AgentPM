---
name: orchestrate-review-loop
description: |
  Main → SubAgent → Review → Integrationのレビューループを実行するオーケストレータースキル。

  SubAgentがドキュメントを生成して終わりではなく、Mainが要件・フレームワーク・評価基準を把握し、
  SubAgentが並列でドキュメント作成、MainがClaude Code LLMで品質レビュー、ズレがあれば即リプランして次の指示に反映します。

  「作成→レビュー→修正→統合」のループが自動で回り、ドキュメント品質70点以上を自動保証します。

  使用タイミング:
  - 複数ドキュメントを高品質で作成したい
  - レビューと修正のループを自動化したい
  - SubAgentの生成品質を保証したい

  所要時間: タスク数×20分（1タスクあたり作成10分+レビュー10分）
  出力: 全ドキュメント + review_loop_evidence/（証拠記録）

trigger_keywords:
  - "レビューループ実行"
  - "自動レビュー実行"
  - "品質管理実行"
  - "ドキュメント並列レビュー"
  - "ドキュメントレビュー統合"

stage: executing
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
3. **自動レビュー**: Claude Code LLMで5観点評価（完全性・論理性・具体性・エビデンス・フレームワーク準拠性）
4. **自動リプラン**: 品質スコア70点未満の場合、修正指示生成
5. **証拠記録**: イテレーション別の完全トレース（quality_score, review_report）
6. **品質保証**: 70点以上で統合完了、3回失敗でHuman-in-the-Loop

---

## Domain-Specific Knowledge (from Founder_Research)

### 評価基準・フレームワーク
- NRR（Net Revenue Retention）≥120%、年次成長率 ≥300%（SaaS基準）

### Success Patterns

**1. Superhuman - 反復的PMF測定による品質向上**
- **パターン**: 四半期ごとのSean Ellisテスト（22% → 32% → 58%への段階的向上）
- **品質ゲート**: 40%未満は不合格、セグメンテーション分析で「非常に残念」グループに焦点
- **イテレーション戦略**: High Expectation機能の優先実装、Low Impactフィードバックは無視
- **成果**: 58%達成（業界最高水準、ベンチマーク40%を18ポイント上回る）
- **適用**: `/validate-pmf` 実行時、品質スコア50%未満の場合に反復改善プロセスを適用

**2. Airbnb - ボトルネック発見と即座の対応**
- **パターン**: 100人以上のホスト訪問で写真品質問題を特定 → 創業者自ら写真撮影
- **品質評価**: トラクション停滞を検知（ニューヨーク市場での予約低迷）
- **リプラン**: 「Do Things That Don't Scale」戦略で手動介入
- **成果**: 予約2-3倍増、月次成長率25-30%回復
- **適用**: `/validate-cpf` `/build-pitch-deck` 実行時、トラクション指標が基準未達の場合にボトルネック分析を実施

**3. Airbnb Pitch Deck - 視覚的ストーリーテリングによる投資家説得**
- **パターン**: Problem→Solution→Tractionの論理的整合性を徹底検証
- **品質基準**: 総合投資家説得力スコア120/130点（優秀レベル）
- **レビュー観点**:
  - Problem Slide: 9/10以上（定量データ裏付け必須）
  - Traction Slide: 15/15満点（成長率だけでなく「どう達成したか」を説明）
  - Market Size Slide: TAM/SAM/SOM明確化 + Why Now 3つ以上
- **成果**: Sequoia Capital Series A調達成功、IPO時$100B評価額
- **適用**: `/build-pitch-deck` 実行時、各スライドの品質スコア基準として適用

**4. Airbnb Scorecard - 包括的評価による投資判断**
- **パターン**: 6カテゴリ50点満点評価（Market 8点、CPF 10点、PSF 10点、Business Model 10点、Execution 10点、Uniqueness 10点）
- **品質ゲート**:
  - 45-50点: 最優秀（Top 5%）- 即Series A推奨
  - 40-44点: 優秀（Top 15%）- Series A推奨（軽微な改善後）
  - 35-39点: 良好（Top 30%）- Seed → Series A（6-12ヶ月後）
  - 30-34点: 要改善 - Seed推奨、3-6ヶ月後再評価
  - 30点未満: 再構築 - VC投資非推奨
- **成果**: Airbnb 45/50点、即Series A調達推奨判定
- **適用**: `/startup-scorecard` 実行時、総合スコアによる品質判定基準として適用

**5. Airbnb CPF検証 - 統計的有意性の確保**
- **パターン**: 100人以上のインタビューで課題共通率85%達成（VC基準70%を15ポイント上回る）
- **品質基準**:
  - インタビュー数: 30人以上（VC最低基準） → Airbnbは100人以上（3倍）
  - 課題共通率: 70%以上（VC基準） → Airbnbは85%
  - WTP検証: 実績ベース（初期3名が$80/泊支払い）が最強の証拠
- **成果**: CPFスコア85/100、VC投資推奨レベル
- **適用**: `/validate-cpf` 実行時、サンプルサイズと課題共通率の品質ゲートとして適用

### Common Pitfalls

**1. 不十分なサンプルサイズによる誤判定**
- **失敗パターン**: インタビュー10-20人程度でCPF達成と判断 → 実際は統計的有意性不足
- **Airbnb教訓**: 100人以上のインタビューで信頼性確保（VC基準30人の3倍）
- **対策**: `/validate-cpf` 実行時、インタビュー数が30人未満の場合は警告表示、追加インタビュー推奨

**2. 抽象的な表現によるエビデンス不足**
- **失敗パターン**: 「市場が大きい」「競合より優れている」等の根拠なき主張
- **Airbnb Pitch Deck教訓**: TAM $1.3T、SAM $85B、SOM $1Bと具体的数値を明示
- **対策**: Review Agent実行時、数値・固有名詞・出典の有無をチェック（具体性スコア20点満点中12点未満で不合格）

**3. 論理的矛盾によるVC不信**
- **失敗パターン**: 「市場が小さい」と言いながら「急成長市場」と主張
- **対策**: Review Agent実行時、論理性スコア25点満点中15点未満で不合格、矛盾箇所を明示してリプラン

**4. セグメンテーション不足によるPMF誤判定**
- **Superhuman教訓**: 初回Sean Ellis 22% → セグメンテーション分析で「非常に残念」グループ特定 → 58%達成
- **失敗パターン**: 全ユーザーの平均値のみで判断、ターゲット市場の再定義を怠る
- **対策**: `/validate-pmf` 実行時、Sean Ellis < 50%の場合にセグメンテーション分析を必須化

### Quantitative Benchmarks

**品質ゲート基準（VC投資判断）**
- **CPFスコア**: 70%以上（Airbnb実績85% = +15%）
- **PMF Sean Ellisテスト**: 50%以上（ForStartup厳格基準、Origin 40% → 50%）、Superhuman実績58%
- **月次成長率**: 20%以上（Airbnb実績25-30%）
- **総合Scorecard**: 40点以上/50点満点で優秀判定（Airbnb 45点）
- **Pitch Deck投資家説得力**: 110点以上/130点満点で優秀判定（Airbnb 120点）

**レビュー品質スコア閾値**
- **完全性（25点満点）**: 20点以上（80%の必須セクション実装）
- **論理性（25点満点）**: 18点以上（論理的矛盾なし）
- **具体性（20点満点）**: 14点以上（数値・固有名詞・事例含む）
- **エビデンス（15点満点）**: 10点以上（データ・出典明記）
- **フレームワーク準拠性（15点満点）**: 12点以上（スタートアップサイエンス準拠）
- **総合（100点満点）**: **70点以上で合格**、60-69点は条件付き合格、60点未満はリプラン必須

**反復改善の効果**
- **Superhuman**: Iteration 1（22%） → Iteration 2（32%） → Iteration 3（58%）、3回で36ポイント向上
- **Airbnb写真改善**: Iteration 1（低品質写真） → Iteration 2（プロ撮影） → 予約2-3倍増
- **期待改善率**: 1イテレーションあたり+10-20ポイント、3イテレーションで目標達成

### Best Practices

**1. 早期レビューの実施（作成直後、統合前）**
- SubAgent完了直後にReview Agentを起動（Phase 3）
- 統合前に品質ゲート判定（Phase 4）
- 不合格の場合は即リプラン（Phase 5）、統合後の手戻りを防ぐ

**2. 定量的評価基準の明示**
- 5観点（完全性・論理性・具体性・エビデンス・フレームワーク準拠性）で100点満点評価
- 各観点の配点と合格ラインを事前に明示（透明性確保）
- 証拠記録（quality_score.json、review_report.md）で再現性確保

**3. セグメンテーション分析の徹底**
- Superhuman戦略: 「非常に残念」グループの深掘りインタビュー
- 全体平均ではなく、ターゲット市場のスコアに焦点
- Low Impactフィードバックは無視、High Expectation機能に集中

**4. Human-in-the-Loopの適切なタイミング**
- 3回のリトライ後も品質スコア70点未満の場合、必ず停止しユーザー判断を仰ぐ
- 自動化と人間の判断のバランスを保つ
- ユーザーに3つの選択肢を提示: 手動修正 / 要件見直し / 中断

**5. 証拠記録による学習ループ**
- イテレーション別の完全トレース（task_breakdown.md、subagent_output.md、quality_score.json、review_report.md、decision.md）
- final_summary.mdで主要な学びを記録
- 次回の実行時に過去のイテレーション履歴を参照し、改善速度向上

### Reference
- 詳細: @Founder_Agent_ForStartup/research/case_studies/tier2/
  - validate-cpf/01_airbnb_cpf_validation.md（CPF検証、100人インタビュー、課題共通率85%）
  - validate-pmf/01_superhuman_pmf_framework.md（PMFフレームワーク、Sean Ellis 22%→58%、セグメンテーション戦略）
  - build-pitch-deck/01_airbnb_visual_storytelling.md（ピッチデッキ品質基準、投資家説得力120/130点）
  - startup-scorecard/01_airbnb_comprehensive_scorecard.md（包括的評価、45/50点、VC投資判断基準）

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
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#cpf-validation
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#lean-canvas
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
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/review_criteria.md

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
- 必須セクションリストと照合（/Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/review_criteria.md参照）
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
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/review_criteria.md（品質基準）
```

**保存先**:
- `{IDEA_FOLDER}/review_loop_evidence/iteration_001/quality_score_001.json`
- `{IDEA_FOLDER}/review_loop_evidence/iteration_001/review_report_001.md`

---

### Phase 4: 統合判定

#### STEP 5: 統合可否判定

**判定基準**:

| 品質スコア | 判定 | 対応 |
|-----------|------|------|
| 70点以上 | ✅ 合格 | 統合完了 |
| 60-69点 | ⚠️ 条件付き合格 | 警告ログ記録 + 統合 |
| 60点未満 | ❌ 不合格 | リプラン必須 |

**合格の場合**:
- STEP 5.5で統合完了の判定記録を保存
- STEP 8でfinal_summary.md生成
- 完了

**不合格の場合**:
- STEP 5.5でリプラン必須の判定記録を保存
- Iteration 2へ進む（Phase 5: リプラン）

#### STEP 5.5: 判定記録の保存（decision_{NNN}.md）

**実行**: Write tool

**パス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/iteration_{NNN}/decision_{NNN}.md`

**内容**:

**統合完了の場合**:
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

**リプラン必須の場合**:
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

| ドキュメント | 最終スコア | 判定 | 保存先 |
|------------|-----------|------|--------|
| cpf_judgment.md | 74点 | ✅ 合格 | Stock/programs/.../documents/1_initiating/ |
| lean_canvas.md | 82点 | ✅ 合格 | Stock/programs/.../documents/2_discovery/ |
| pitch_deck.md | 78点 | ✅ 合格 | Stock/programs/.../documents/3_planning/ |

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

1. cpf_judgment.md、lean_canvas.md、pitch_deck.mdをStockフォルダに移動
2. プロジェクト憲章を更新（CPF検証完了を記録）
3. 次フェーズ（PSF検証）の準備
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

- Review Agent定義: `.claude/agents/review-agent.md`
- ドキュメント品質基準: `.claude/skills/_shared/review_criteria.md`（Week 3.5で作成）
- エラーハンドリング: `.claude/skills/_shared/error_handling_patterns.md`
- 並列実行ルール: `.claude/rules/parallel_execution.md`
- レビューループ制御: `.claude/rules/review_loop.md`
- リプランパターン: `.claude/skills/_shared/replan_patterns.md`（Week 5で作成）

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
