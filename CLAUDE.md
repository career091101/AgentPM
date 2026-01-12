# CLAUDE.md

## プロジェクト概要

**aipm_v0** - PMBOK × Lean UX × Agile のハイブリッドプロジェクト管理システム。

## 基本ルール

1. **言語**: ユーザーは日本人なので日本語で出力
2. **タスク管理**: 1セッション = 1機能/1プロジェクトに限定、完了後は `/clear`
3. **コンテキスト節約**: サブエージェント活用（Task tool）を優先

## 3層フォルダ構造

- `Flow/` - ドラフト・作業中（年月/日付で階層化）
- `Stock/` - 確定版ドキュメント
- `Archived/` - 完了プロジェクト

## PMBOKフェーズ

1. Initiating - プロジェクト憲章、ステークホルダー
2. Discovery - ペルソナ、ジャーニー、仮説マップ
3. Research - 競合調査、市場規模
4. Planning - WBS、PRD、バックログ
5. Executing - 開発計画、ストーリー実装
6. Monitoring - ステータスレポート
7. Closing - レッスンズラーンド

## ルール参照ガイド（必要時のみ参照）

以下のルールは**自動読み込みされません**。必要に応じて `@` 記法で明示的に参照してください。

### 📋 コア機能（よく使う）
- **プロジェクト詳細**: `@docs/ai/overview.md`
- **PMBOKワークフロー**: `@docs/ai/pmbok_workflow.md`
- **コンテキスト管理**: `@.claude/rules/context_management.md`
- **実行方針**: `@.claude/rules/execution_preference.md`
- **並列実行**: `@.claude/rules/parallel_execution.md`

### 🔧 高度な機能（必要時のみ）
- **レビューループ**: `@.claude/rules/review_loop.md`
- **パス規約**: `@.claude/rules/path_conventions.md`
- **UI検証**: `@.claude/rules/ui_testing.md`
- **Ralph Wiggum**: `@.claude/rules/ralph_wiggum.md`

### 📚 実装ガイド（Week 1-8）
- **全Week概要**: `@.claude/rules/WEEK_IMPLEMENTATIONS.md`
- **詳細ガイド**: `@docs/implementation_guides/week[1-8]_*.md`

### 📊 PMBOK各フェーズ
- **Discovery**: `@.claude/rules/pmbok_discovery.md`
- **Planning**: `@.claude/rules/pmbok_planning.md`
- **Executing**: `@.claude/rules/pmbok_executing.md`
- その他: `.claude/rules/pmbok_*.md`

## 禁止事項

- ルールを独自解釈で変更しない
- パス構造を勝手に変更しない
- 失敗時は代替手段を取らず報告する

## 作業引継ぎ

作業中断時は `HANDOVER.md` を生成すること。

---

**使い方のヒント**:
- 初めてのタスク → `@docs/ai/overview.md` で全体像を把握
- 並列実行したい → `@.claude/rules/parallel_execution.md` 参照
- コンテキスト節約したい → `@.claude/rules/context_management.md` 参照
