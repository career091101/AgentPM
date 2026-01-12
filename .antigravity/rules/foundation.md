# Antigravity Foundation Rules

## プロジェクト概要

このリポジトリは **aipm_v0** - PMBOK × Lean UX × Agile のハイブリッドプロジェクト管理システムです。

## 参照ドキュメント

- @docs/ai/overview.md - プロダクト概要
- @docs/ai/setup.md - セットアップ
- @docs/ai/commands.md - コマンド一覧
- @docs/ai/pmbok_workflow.md - PMBOKワークフロー
- @docs/ai/conventions.md - コーディング規約
- @docs/ai/security.md - セキュリティ

## 基本ルール

1. **ルールは正確に実行** - 独自解釈で変更しない
2. **パス構造を尊重** - Flow/年月/日付の階層を必ず守る
3. **失敗時は報告** - 代替手段を取らず、ユーザーに確認

## ディレクトリ構造

- `Flow/` - ドラフト・作業中
- `Stock/` - 確定版ドキュメント
- `Archived/` - 完了プロジェクト

## ワークフロー

`.antigravity/workflows/` 配下のワークフローを参照してPMBOKフェーズを実行。
