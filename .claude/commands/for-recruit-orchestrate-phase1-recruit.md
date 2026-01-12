# Command: /orchestrate-phase1-recruit

ForRecruit Edition Phase1全体を自律実行するオーケストレーターコマンド。

---

## 概要

**目的**: ForRecruit Edition Phase1（CPF→PSF→PMF検証）をRing制度準拠で完全自動実行

**所要時間**: 6-10時間（自動実行）

**対象ユーザー**: リクルートグループ等の企業内新規事業担当者、イントレプレナー、Ring制度参加者

---

## 実行方法

```bash
/orchestrate-phase1-recruit
```

**オプション**:
- 探索分野キーワード入力（省略可）
- プロジェクトディレクトリ指定（デフォルト: 現在のディレクトリ）

---

## 実行内容

### PHASE 1: Discovery & Planning（発見・計画）
1. `/discover-demand` - 需要発見リサーチ（TAM 50億円以上）
2. `/create-mvv` - MVV早期定義（企業価値観整合性チェック）
3. `/apply-lean-canvas` - リーンキャンバス作成
4. `/build-flywheel` - フライホイール設計（社内エコシステム連携）
5. `/inventory-internal-resources` - 社内リソース棚卸し（6カテゴリ、ROI定量化）

### PHASE 2: CPF Validation（Ring 1）
6. `/research-problem` - Web課題発見（ForRecruit版、インタビュー10人）
7. `/simulate-interview` - 仮想ペルソナインタビュー（社内ネットワーク活用）
8. `/validate-cpf` - CPF診断（50%以上）

**ステージゲート1: Ring 1（CPF）** → 50%以上で通過、未達成時は停止

### PHASE 3: PSF Validation（Ring 2）
9. `/research-competitors` - 競合調査（外部+既存事業）
10. `/validate-10x` - 10倍優位性検証（1軸以上）
11. `/validate-psf` - PSF診断（ROI 1000%以上）
12. `/validate-ring-criteria` - Ring 2基準チェック

**ステージゲート2: Ring 2（PSF）** → 10倍1軸以上+ROI 1000%以上で通過、未達成時は停止

### PHASE 4: PMF Validation（Ring 3）
13. `/build-lp` - LP構築（社内向け）
14. `/design-pricing` - 価格設定戦略（Airレジ無料モデル等）
15. `/validate-pmf` - PMF診断（外部顧客100社以上）
16. `/validate-ring-criteria` - Ring 3基準チェック

**ステージゲート3: Ring 3（PMF）** → 外部顧客100社+収益化開始で通過、未達成時は停止

### PHASE 5: Launch Preparation
17. `/analyze-aarrr` - AARRR分析（社内KPI最適化）
18. `/startup-scorecard` - 最終評価（Ring制度評価項目対応）

---

## Ring制度ステージゲート

### Ring 1（CPF検証）
- **判定基準**: CPFスコア50%以上、Problem Commonality 60%以上、User Research 10件以上
- **承認**: 課長承認（予算50-100万円）
- **停止条件**: CPF 50%未満

### Ring 2（PSF検証）
- **判定基準**: 10倍優位性1軸以上、ROI 1000%以上、MVP完成、社内リソース活用1種以上
- **承認**: 部長・事業部長承認（予算500-1,000万円）
- **停止条件**: 10倍優位性0軸 or ROI 1000%未満

### Ring 3（PMF検証）
- **判定基準**: 外部顧客100社以上、収益化開始、3年黒字計画策定済み、LTV/CAC 3.0以上
- **承認**: 役員承認（予算5,000万円-3億円、本格事業化判断）
- **停止条件**: 外部顧客獲得失敗 or 収益化困難

---

## 成果物

```
{IDEA_FOLDER}/
├── documents/
│   ├── 1_initiating/
│   │   ├── demand_discovery.md
│   │   └── business_idea.md
│   ├── 2_discovery/
│   │   ├── lean_canvas.md
│   │   ├── persona.md
│   │   ├── flywheel.md
│   │   ├── problem_research.md
│   │   ├── interview_simulation.md
│   │   ├── competitor_research.md
│   │   └── 10x_validation.md
│   ├── 3_planning/
│   │   ├── mvv.md
│   │   ├── cpf_diagnosis.md
│   │   ├── psf_diagnosis.md
│   │   ├── pmf_diagnosis.md
│   │   ├── pricing_strategy.md
│   │   └── aarrr_analysis.md
│   ├── 5_monitoring/
│   │   └── scorecard.md
│   └── internal_approval/
│       ├── resource_inventory.md
│       ├── ring1_criteria_check.md
│       ├── ring2_criteria_check.md
│       └── ring3_criteria_check.md
├── mvp/
│   └── lp/
└── phase1_summary.md
```

---

## 関連スキル

- **詳細**: `.claude/skills/for_recruit/orchestrate-phase1-recruit/SKILL.md`
- **Ring基準チェック**: `/validate-ring-criteria`
- **社内承認デッキ作成**: `/build-approval-deck`
- **社内リソース棚卸し**: `/inventory-internal-resources`

---

## 参考

- **Recruit_Product_Research**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/`
- **Ring制度**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/README.md`

---

**作成日**: 2026-01-02
**Domain**: ForRecruit
