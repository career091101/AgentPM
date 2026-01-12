---
name: for-solo-orchestrate-phase1-solo
description: ForSolo Edition Phase1全体を自律実行するオーケストレータースキル
---

# ForSolo Orchestrate Phase1 Solo Command

このコマンドはForSolo Edition Phase1（需要発見→CPF→PSF→PMF検証→Launch準備）を完全自動実行します。

## 実行内容

ForSolo Edition Phase1の20スキルを順次自動実行:

### Phase 1A: 需要発見（Discovery）
1. `/for-solo-discover-demand` - 需要発見
2. `/for-solo-research-problem` - 課題調査
3. `/for-solo-validate-solo-fit` - 1人実行可能性検証

### Phase 1B: CPF検証
4. `/for-solo-create-persona` - ペルソナ作成
5. `/for-solo-simulate-interview` - インタビューシミュレーション
6. `/for-solo-validate-cpf` - CPF検証
7. `/for-solo-research-competitors` - 競合調査
8. `/for-solo-validate-10x` - 10倍優位性検証

### Phase 1C: PSF検証
9. `/for-solo-validate-psf` - PSF検証

### Phase 1D: PMF検証
10. `/for-solo-validate-pmf` - PMF検証

### Phase 1E: Launch準備
11. `/for-solo-create-mvv` - MVV作成
12. `/for-solo-design-micro-saas-model` - Micro-SaaS収益化モデル設計
13. `/for-solo-create-bip-strategy` - Build in Public戦略作成
14. `/for-solo-build-flywheel` - 成長フライホイール構築
15. `/for-solo-create-content-flywheel` - コンテンツフライホイール作成
16. `/for-solo-optimize-tool-stack` - ツールスタック最適化
17. `/for-solo-measure-aarrr` - AARRR測定
18. `/for-solo-monitor-burn-rate` - バーンレートモニタリング
19. `/for-solo-validate-unit-economics` - ユニットエコノミクス検証
20. `/for-solo-startup-scorecard-forsolo` - スタートアップスコアカード

## ステージゲート判定

### Gate 1: CPF検証
- **CPFスコア**: 50%以上（課題共通率60%以上、3Uスコア7点以上）
- **実行可能性スコア**: 6点満点
- **判定**: 達成時→PSF検証へ、未達成→改善 or ピボット

### Gate 2: PSF検証
- **初期ユーザー数**: 30人以上
- **ソリューション満足度**: 70%以上
- **価格受容性**: 60%以上（月額$10-$50）
- **判定**: 達成時→PMF検証へ、未達成→CPF再検証

### Gate 3: PMF検証
- **PMF Score**: 6.0以上（40%が「very disappointed」）
- **初期顧客数**: 30人以上
- **LTV/CAC**: 10.0以上
- **判定**: 達成時→Launch準備へ、未達成→PSF再検証

### Gate 4: Launch準備
- **MRR**: $1K以上
- **利益率**: 80%以上
- **月次成長率**: 10%以上
- **判定**: 達成時→Phase2へ、未達成→改善

## 所要時間

- **合計**: 8-12時間（自動実行）
- **Discovery**: 1-2時間
- **CPF検証**: 2-3時間
- **PSF検証**: 1-2時間
- **PMF検証**: 2-3時間
- **Launch準備**: 2-3時間

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/`配下に全成果物を出力

## 次のコマンド

Phase1完了後:
- Phase2へ進む（成長フェーズ）
- Phase1再実行（ピボット時）

## 参照

- スキル詳細: @.claude/skills/for_solo/orchestrate-phase1-solo/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
- Tier 2 Cases: @knowledge_base/tier2_case_studies/
