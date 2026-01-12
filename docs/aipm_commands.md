# AIPMシステム コマンド一覧

このドキュメントは、AIPMシステムで使用できるすべてのコマンド（トリガーワード）をフェーズ別にまとめたリファレンスです。

---

## 📋 立ち上げフェーズ（Initiating）

| コマンド | 概要 | 出力ファイル |
|---------|------|-------------|
| `プロジェクト初期化` / `プロジェクト開始` / `プロジェクト立ち上げ` | プログラム・プロジェクト構造を作成 | (ディレクトリ構造) |
| `"XXX始めたい"` / `"XXX作りたい"` | プロジェクト名+開始したいでプロジェクト開始 | (ディレクトリ構造) |
| `プロダクト定義` / `プログラム定義` / `Product定義` | プロダクト（プログラム）定義書作成 | `draft_program_definition.md` |
| `プロジェクト憲章` / `プロジェクトチャーター` | プロジェクト憲章作成 | `draft_project_charter.md` |
| `ステークホルダー分析` / `ステークホルダーマップ` | ステークホルダー分析書作成 | `draft_stakeholder_analysis.md` |
| `リスク分析` / `リスク計画` | リスク分析と対策計画の作成 | `draft_risk_plan.md` |
| `作業開始` / `work start` / `今日の作業開始` | 今日の日付フォルダとタスクファイル作成 | `daily_tasks.md` |

---

## 🔬 リサーチフェーズ（Research）

| コマンド | 概要 | 出力ファイル |
|---------|------|-------------|
| `Research` / `リサーチ` | リサーチメニュー表示 | - |
| `顧客調査` / `Customer Research` | 顧客調査レポート作成 | `draft_customer_research.md` |
| `競合調査` / `Competitor Research` | 競合分析レポート作成 | `draft_competitor_research.md` |
| `デスクリサーチ` / `Desk Research` | 市場・業界総合調査 | `draft_desk_research.md` |
| `市場規模推定` / `TAM SAM SOM` / `フェルミ推定` | TAM/SAM/SOM分析 | `draft_market_size_estimation.md` |

---

## 💡 発見フェーズ（Discovery）

| コマンド | 概要 | 出力ファイル |
|---------|------|-------------|
| `Discovery` / `ディスカバリー` | Discoveryメニュー表示 | - |
| `仮説マップ` / `Assumption Map` | 前提条件マップ作成 | `draft_assumption_map.md` |
| `ペルソナ作成` / `Persona` | ユーザーペルソナ作成 | `draft_persona.md` |
| `課題定義` / `Problem Statement` | 問題定義書作成 | `draft_problem_statement.md` |
| `ジャーニーマップ` / `User Journey Map` / `ユーザージャーニーマップ` | ユーザージャーニーマップ作成 | `draft_user_journey_map.md` |
| `ソリューション定義` / `Solution Definition` | ソリューション定義書作成 | `draft_solution_definition.md` |
| `検証計画` / `Validation Plan` | 仮説検証計画作成 | `draft_validation_plan.md` |
| `UXリサーチ` / `ユーザー調査` / `UX調査` | UXリサーチ調査概要 | `draft_ux_research_overview.md` |
| `インタビュー設計` / `インタビュー質問` / `質問表作成` | インタビュー質問表作成 | `draft_interview_guide.md` |
| `リクルーティング` / `ユーザー募集` / `被験者募集` | 参加者募集計画 | `draft_recruiting_plan.md` |
| `インタビュー分析` / `インタビュー結果` / `インタビュー記録` | インタビュー結果分析 | `draft_interview_analysis_{{participant_id}}.md` |
| `リサーチサマリー` / `調査サマリー` / `全体分析` | 調査全体のサマリー | `draft_research_summary.md` |
| `仮説バックログ` / `Hypothesis` | 仮説リスト作成 | `draft_hypothesis_backlog.md` |
| `アイディア発散` | アイデア発散・収束ワーク | `draft_flow_assist.md` |
| `プレゼン資料生成` | Marpスライド作成 | `draft_presentation.md` |
| `図表生成` | Draw.io図表テンプレート作成 | `assets/diagram.drawio` |

---

## 📐 計画フェーズ（Planning）

| コマンド | 概要 | 出力ファイル |
|---------|------|-------------|
| `プロジェクトスコープ記述書` / `Project Scope Statement` | スコープ定義書作成 | `draft_project_scope_statement.md` |
| `プロダクト要求仕様書` / `PRD` / `Product Requirements Document` | PRD作成 | `draft_product_requirements.md` |
| `Design Doc` / `デザインドック` / `設計文書` | 設計ドキュメント作成 | `draft_design_doc.md` |
| `WBS作成` / `作業分解構造` | 作業分解構造作成 | `draft_wbs.md` |
| `プロダクトバックログ初期化` / `backlog初期化` / `バックログ初期化` | バックログ初期化 | `backlog.yaml`, `epics.yaml` |
| `ルーチンタスク定義` / `routines作成` / `ルーティン定義` | 定期タスク定義 | `routines.yaml` |
| `ロードマップ作成` / `プロダクトロードマップ` / `リリース計画` | リリース計画作成 | `draft_product_roadmap.md` |
| `バックログ検証` / `バックログ確認` / `バックログチェック` | バックログの構文確認 | (検証結果) |
| `ルーチンタスク検証` / `ルーチン検証` / `ルーチンチェック` | ルーチンタスクの構文確認 | (検証結果) |

---

## 🛠️ 開発フェーズ（Development）

| コマンド | 概要 | 出力ファイル |
|---------|------|-------------|
| `Development` / `開発フェーズ` / `実装フェーズ` | 開発メニュー表示 | - |
| `開発環境初期化` / `Development初期化` / `実装環境セットアップ` | 環境セットアップ | `draft_dev_setup.md` |
| `開発計画作成` / `Development計画` / `実装計画` | 実装計画書作成 | `draft_dev_plan.md` |
| `実装順序計画` / `開発順序` / `ストーリー依存関係` | 依存関係を考慮した実装順序定義 | `draft_implementation_order.md` |
| `ストーリー実装` / `実装開始` / `ユーザーストーリー実装` | ストーリー実装計画 | `draft_dev_story.md` |
| `記事執筆` / `ドキュメント作成` / `記事作成` | ドキュメント執筆 | `draft_dev_article.md` |
| `成果物確認` / `実装確認` / `確定レビュー` | 実装レビュー | `draft_development_review.md` |

---

## 🚀 実行フェーズ（Executing）

| コマンド | 概要 | 出力ファイル |
|---------|------|-------------|
| `スプリントゴール` / `Sprint Goal` | スプリント目標設定 | `draft_sprint_goal_{{sprint_number}}.md` |
| `今日のタスク` / `日次タスク作成` / `Daily tasks` | 日次タスクリスト生成 | `daily_tasks.md` |
| `週次レビュー` / `Weekly review` | 週次レビュー作成 | `weekly_review.md` |
| `Sync` / `WBSと同期` / `リスクログと同期` | 対象アーティファクトの更新 | (既存ファイルを更新) |
| `議事録` / `ミーティングノート` | 会議議事録作成 | `draft_meeting_minutes.md` |

---

## 📊 監視・コントロールフェーズ（Monitoring）

| コマンド | 概要 | 出力ファイル |
|---------|------|-------------|
| `変更要求` / `チェンジリクエスト` | 変更要求テンプレート作成 | `draft_change_request.md` |
| `スプリントレビュー作成` / `Sprint Review` | スプリントレビュー自動生成 | `draft_sprint_review_{{sprint_id}}.md` |

---

## 🏁 終結フェーズ（Closing）

| コマンド | 概要 | 出力ファイル |
|---------|------|-------------|
| `教訓記録` / `レッスンラーニド` / `レッスンずらーんど` | Lessons Learned作成 | `draft_lessons_learned.md` |
| `移管ドキュメント作成` | 引き継ぎ資料作成 | `draft_transition_document.md` |

---

## ⚙️ システムコマンド（ユーティリティ）

| コマンド | 概要 |
|---------|------|
| `確定反映して` | Flow→Stockへのドラフト同期実行 |
| `フェーズ追加` / `Phase追加` / `新フェーズ作成` | 新しいフェーズルールの雛形生成 |

---

## 📌 補足情報

### ファイル出力先
- **Draft（下書き）**: `Flow/YYYYMM/YYYY-MM-DD/` フォルダに生成
- **確定版**: `確定反映して` コマンドで `Stock` フォルダへ移動・正式化

### 使い方
1. Cursorのチャットでコマンド（トリガーワード）を入力
2. AIが質問形式で必要な情報を収集
3. 回答に基づいてドキュメントを自動生成
4. 内容確認後、`確定反映して` で正式化

### 参考ルールファイル
- `basic/00_master_rules.mdc` - マスタールール
- `basic/01_pmbok_initiating.mdc` - 立ち上げフェーズ
- `basic/02_pmbok_discovery.mdc` - 発見フェーズ
- `basic/02_pmbok_research.mdc` - 調査フェーズ
- `basic/02_pmbok_presentation.mdc` - プレゼンテーション
- `basic/03_pmbok_planning.mdc` - 計画フェーズ
- `basic/04_pmbok_executing.mdc` - 実行フェーズ
- `basic/05_pmbok_monitoring.mdc` - 監視・コントロール
- `basic/06_pmbok_closing.mdc` - 終結フェーズ
- `basic/07_task_management.mdc` - タスク管理
- `basic/08_pmbok_flow_assist.mdc` - フロー支援
- `basic/09_pmbok_development.mdc` - 開発フェーズ
- `basic/flow_to_stock_rules.mdc` - 自動同期ルール
