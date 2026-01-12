---
name: for-solo-optimize-tool-stack
description: ForSolo特化版ツールスタック最適化スキルを実行
---

# ForSolo Optimize Tool Stack Command

このコマンドはForSolo特化版のツールスタック最適化スキルを実行します。

## 実行内容

`/optimize-tool-stack` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. 現在のツールスタック評価
2. コスト最適化提案
3. 無料枠活用戦略
4. 技術スタック最適化
5. ツールスタック推奨リスト作成

## ForSolo特化要素

- **月次コスト目標**: $50以下
- **推奨ツール**:
  - ホスティング: Vercel、Railway（無料枠）
  - DB: Supabase、PlanetScale（無料枠）
  - 認証: Clerk、Supabase Auth（無料枠）
  - 決済: Stripe（成功報酬のみ）
  - メール: Resend（無料枠）
- **技術スタック**: Next.js、Tailwind CSS、TypeScript
- Solopreneur Research統合: 85件

## 使用タイミング

- プロジェクト開始時（技術選定）
- コスト最適化が必要な時
- Solo-Fit検証時

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/solopreneur/tool_stack_optimization.md`

## 次のコマンド

最適化完了後:
- `/for-solo-validate-solo-fit` - Solo-Fit検証へ
- `/for-solo-monitor-burn-rate` - バーンレートモニタリングへ

## 参照

- スキル詳細: @.claude/skills/for_solo/optimize-tool-stack/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
