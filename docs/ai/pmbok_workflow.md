# PMBOKワークフロー詳細

## フェーズ別トリガーワード一覧

### 0. 事前準備（プロジェクト初期化）

| トリガー | 生成物 |
|----------|--------|
| `[プロジェクト名] 始めたい` | プロジェクト構造一式 |
| `プロジェクト初期化` | Flow/Stock ディレクトリ |

### 1. 立ち上げ（Initiating）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| `プロジェクト憲章` | draft_project_charter.md | doc_initiating |
| `ステークホルダー分析` | draft_stakeholder_analysis.md | doc_initiating |
| `プロダクト定義` | draft_program_definition.md | program_dir |

### 2. 発見（Discovery）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| `仮説マップ` | draft_assumption_map.md | doc_discovery |
| `ペルソナ作成` | draft_persona.md | doc_discovery |
| `課題定義` | draft_problem_statement.md | doc_discovery |
| `ジャーニーマップ` | draft_user_journey_map.md | doc_discovery |
| `ソリューション定義` | draft_solution_definition.md | doc_discovery |
| `検証計画` | draft_validation_plan.md | doc_discovery |
| `UXリサーチ` | draft_ux_research_overview.md | doc_discovery |
| `インタビュー設計` | draft_interview_guide.md | doc_discovery |
| `リクルーティング` | draft_recruiting_plan.md | doc_discovery |
| `インタビュー分析` | draft_interview_analysis.md | doc_discovery |
| `リサーチサマリー` | draft_research_summary.md | doc_discovery |
| `仮説バックログ` | draft_hypothesis_backlog.md | doc_discovery |

### 2-B. リサーチ（Research）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| `顧客調査` | draft_customer_research.md | doc_research |
| `競合調査` | draft_competitor_research.md | doc_research |
| `デスクリサーチ` | draft_desk_research.md | doc_research |
| `市場規模推定` | draft_market_size_estimation.md | doc_research |

### 3. 計画（Planning）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| `WBS作成` | draft_wbs.md | doc_planning |
| `プロダクトバックログ初期化` | backlog.yaml | doc_planning |
| `リスク計画` | draft_risk_plan.md | doc_planning |
| `プロジェクトスコープ記述書` | draft_project_scope.md | doc_planning |
| `プロダクト要求仕様書` | draft_prd.md | doc_planning |
| `ロードマップ作成` | draft_product_roadmap.md | doc_planning |

### 4. 実行（Executing）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| `Development` | メニュー表示 | - |
| `開発環境初期化` | draft_setup.md | dev_root |
| `開発計画作成` | draft_development_plan.md | dev_root |
| `ストーリー実装` | draft_story_implementation.md | dev_root |
| `スプリントゴール` | sprint_goal.md | sprint_goals_dir |
| `今日のタスク` | daily_tasks.md | flow_date |

### 5. 監視・コントロール（Monitoring）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| `ステータスレポート` | status_report.md | status_reports_dir |
| `変更要求` | change_request.md | change_requests_dir |

### 6. 終結（Closing）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| `レッスンズラーンド` | lessons_learned.md | lessons_learned_dir |
| `移行文書` | transition_document.md | doc_closing |

## 確定反映フロー

```
Flow/YYYYMM/YYYY-MM-DD/draft_*.md
        ↓ 「確定反映して」
Stock/programs/.../documents/[phase]/*.md
```

## パス変数リファレンス

詳細は `.cursor/rules/basic/pmbok_paths.mdc` を参照。
