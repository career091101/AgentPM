---
name: research-competitors
description: |
  ForSolo Edition: ソロプレナー向け競合調査スキル。
  直接競合・間接競合をWebSearchで収集し、5軸（時間/コスト/使いやすさ/成果/導入障壁）で
  ベンチマーク表を作成。ポジショニングマップと空白地帯を特定し、
  1人実行可能性を重視した差別化戦略を提案します。

  使用タイミング：
  - CPF検証完了後、PSF検証開始時
  - 10倍検証の前準備
  - 市場参入戦略の策定時

  所要時間：20-40分（自動実行）
  出力：competitor_research.md
---

# Research Competitors Skill (ForSolo Edition)

ソロプレナー向け競合・代替案調査スキル。1人実行可能性を重視した差別化戦略を提案。

---

## このSkillでできること

1. **直接競合調査**: 同じ課題を解決するプロダクト・サービスの収集
2. **間接競合調査**: 代替手段（DIY、人力サービス等）の収集
3. **5軸ベンチマーク**: 時間/コスト/使いやすさ/成果/導入障壁で比較
4. **ポジショニングマップ**: 市場の構造を可視化
5. **空白地帯特定**: 参入余地のある領域を発見
6. **[ForSolo追加]** 1人実行可能な差別化ポイントの特定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `demand_discovery.md`、`lean_canvas.md`（オプション） |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/3_planning/competitor_research.md` |
| **次のSkill** | `/for-solo-validate-10x` |
| **ステージ** | PSF検証（ForSolo特化） |

---

## Knowledge Base参照

### ForSolo Edition専用
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/Solopreneur_Research/documents/01_App/case_studies/*.md`
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/knowledge_base/tier2_case_studies/research-competitors/*.md`

### 共通Knowledge Base
- @startup_science/01_stages/psf/10x_validation.md
- @startup_science/01_stages/psf/psf_overview.md
- @startup_science/01_stages/psf/uvp_canvas.md

---

## Solopreneur固有ドメイン知識

### 1人実行可能性パターン
- **Micro-SaaS**: シンプルな機能に特化、複雑な機能は避ける
- **Boilerplate/Template**: Next.js/Supabase/Stripe等の頻出スタック活用
- **API活用型**: 既存APIを組み合わせ、フロントエンドに注力

### Build in Public戦略
- **透明性**: 開発プロセスをX/Twitterで公開
- **差別化**: 大企業ができない「個人の顔が見える」サービス

---

## 更新履歴

- 2026-01-02: ForSolo Edition作成（1人実行可能性重視）
