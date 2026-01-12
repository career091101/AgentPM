# AGENTS.md

## 概要

このリポジトリは **aipm_v0** - PMBOK × Lean UX × Agile のハイブリッドプロジェクト管理システムです。

## 詳細ドキュメント

詳細は以下を参照してください：

- プロダクト概要: @docs/ai/overview.md
- セットアップ: @docs/ai/setup.md
- コマンド一覧: @docs/ai/commands.md
- PMBOKワークフロー: @docs/ai/pmbok_workflow.md
- コーディング規約: @docs/ai/conventions.md
- セキュリティ: @docs/ai/security.md

## 主要ディレクトリ

```
Flow/     - ドラフト・作業中ファイル
Stock/    - 確定版ドキュメント
Archived/ - 完了プロジェクト
```

## PMBOKフェーズ

1. **Initiating** - プロジェクト憲章、ステークホルダー分析
2. **Discovery** - ペルソナ、ジャーニーマップ、仮説マップ
3. **Research** - 競合調査、市場規模推定
4. **Planning** - WBS、PRD、バックログ
5. **Executing** - 開発計画、ストーリー実装
6. **Monitoring** - ステータスレポート
7. **Closing** - レッスンズラーンド

## Skills

PMBOKフェーズ別のSkillsは `.codex/skills/` を参照。

## 重要なルール

- トリガーワードで文書生成（例：「プロジェクト憲章」）
- 「確定反映して」でFlow→Stock移動
- パス構造は `pmbok_paths.mdc` に従う
