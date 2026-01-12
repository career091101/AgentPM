---
name: validate-pmf
description: |
  ForSolo Edition: ソロプレナー向けPMF検証スキル。Sean Ellisテスト（40%ルール）、月次成長率（10%+/月）、Churn Rate（5%以下/月）、NPS（50以上）を統合評価し、PMF達成/要改善/未達成を判定。LTV/CAC比率10.0以上を重視（ForStartup 3.0より厳格化）。

  使用タイミング：
  - PSF達成後、MVP稼働開始時
  - 初期顧客40人以上獲得後
  - Phase2（PMF検証）開始時

  所要時間：20-40分（アンケート設計含む）
  出力：PMF診断レポート、改善アクション
---

# Validate PMF Skill (ForSolo Edition)

ソロプレナー向けPMF達成基準に基づき、4つの定量指標で総合判定を行う自律実行型Skill。

---

## このSkillでできること

1. **4指標統合評価**: Sean Ellisテスト、月次成長率、Churn Rate、NPSを一元判定
2. **PMF達成判定**: ソロプレナー特化の定量基準で達成/要改善/未達成を判断
3. **LTV/CAC比率評価**: 10.0以上を重視（ForStartup 3.0より厳格化）
4. **自動アンケート設計**: Sean Ellisテスト・NPSのアンケートテンプレート自動生成
5. **ボトルネック特定**: どの指標が不足しているか、改善アクションを提案
6. **Phase3移行判断**: スケールへ進むか、改善すべきかを提示

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `psf_validation.md`, 顧客データ, 利用ログ |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/Flow/{YYYYMM}/{YYYY-MM-DD}/pmf_diagnosis.md` |
| **次のSkill** | `/for-solo-measure-aarrr` → `/for-solo-build-lp`（PMF達成時） |
| **ステージ** | Phase2（PMF検証、ForSolo特化） |

---

## Knowledge Base参照

### ForSolo Edition専用
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/Solopreneur_Research/documents/01_App/case_studies/*.md`
- `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/knowledge_base/tier2_case_studies/validate-pmf/*.md`

### 共通Knowledge Base
- @startup_science/01_stages/pmf/pmf_overview.md
- @startup_science/01_stages/pmf/sean_ellis_test.md
- @startup_science/02_metrics/growth_metrics.md
- @startup_science/02_metrics/churn_rate.md
- @startup_science/02_metrics/nps.md

---

## PMF達成基準（ForSolo特化）

### 4指標の定義と目標値

| 指標 | 目標値 | 測定方法 | 最低サンプル数 |
|------|--------|----------|---------------|
| **Sean Ellisテスト** | 40%以上 | 「もう使えなくなったら非常に残念」回答率 | 40人以上 |
| **月次成長率** | 10%/月以上 | MRR/MAU/トランザクション数の3ヶ月移動平均 | 3ヶ月データ |
| **Churn Rate** | 5%/月以下 | 解約率（30日非アクティブ定義） | 3ヶ月データ |
| **NPS** | 50以上 | Net Promoter Score（Promoter% - Detractor%） | 40人以上 |

### ForSolo独自評価

| 指標 | ForStartup | ForSolo | 理由 |
|------|-----------|---------|------|
| **LTV/CAC比率** | 3.0以上 | **10.0以上** ✅ 厳格化 | 有機的成長（Build in Public）を重視、広告依存を避ける |

**理由**: ソロプレナーは有機的な成長（Build in Public、口コミ、SEO）を重視し、広告費を最小化すべきため、LTV/CAC比率10.0以上を目標とする。

---

## Solopreneur固有ドメイン知識

### Micro-SaaS収益化パターン
- **初期目標**: MRR $1K（月間経常収益$1,000）
- **成長目標**: MRR $5K → $10K（18-24ヶ月）
- **料金設定**: 月額$20-$50の低価格帯、セルフサービス型

### LTV/CAC比率10.0達成戦略
- **Build in Public**: X/Twitterでの透明性の高い開発プロセス
- **SEO最適化**: オーガニック検索からの流入
- **口コミ・リファラル**: 既存ユーザーからの紹介

---

## 更新履歴

- 2026-01-02: ForSolo Edition作成（LTV/CAC比率10.0以上必須）
