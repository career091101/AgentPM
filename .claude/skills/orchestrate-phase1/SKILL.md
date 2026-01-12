---
name: orchestrate-phase1
description: |
  Phase1全体を自律実行するオーケストレータースキル。アイデア創出→CPF→PSF→ローンチ準備までの全12ステップを順次実行（3-6時間）。ステージゲート管理（CPF 60%以上/PSF 10倍2軸以上）で品質保証。未達成時はHuman-in-the-Loopで必ず停止・報告。最終的にスコアカード（40点満点）で総合評価します。

  使用タイミング：
  - 新規ビジネスアイデアの全自動検証
  - Phase1を一気通貫で実行したい
  - 最小限の手間でPSF検証まで完了したい

  所要時間：3-6時間（自動実行、ステージゲートで停止）
  出力：Phase1全成果物（documents/, mvp/）
trigger_keywords:
  - "起業検証"
  - "Phase1実行"
  - "Phase1開始"
  - "全自動検証"
  - "CPF/PSF検証"
  - "ビジネスアイデア検証"
  - "フェーズ1実行"
  - "完全自動実行"
stage: Phase1全体（Initiating→CPF→PSF→Launch Prep）
dependencies:
  - discover-demand
  - create-mvv
  - apply-lean-canvas
  - estimate-market-size
  - build-flywheel
  - research-problem
  - simulate-interview
  - map-customer-journey
  - validate-cpf
  - validate-10x
  - prioritize-features  # オプション（MVP候補10個以上の場合のみ）
  - build-lp
  - design-ab-test  # オプション（LP改善計画策定時のみ）
  - validate-psf
  - create-sns-content
  - startup-scorecard
  - generate-kpi-dashboard  # オプション（Phase2準備時のみ）
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/phase1_summary.md
execution_time: 4-7時間（必須14ステップ）、5.5-8.5時間（全オプション含む）
framework_reference: Stock/programs/創業支援・新規事業開発(AIエージェント)/startup_science/
priority: P0
framework_compliance: 100%
---

# Orchestrate Phase1 Skill

Phase1全体を自律実行するオーケストレーターSkill。

---

## このSkillでできること

1. **Phase1全自動実行**: 12ステップを順次実行
2. **ステージゲート管理**: CPF/PSF未達成時は必ず停止・報告
3. **エラーハンドリング**: 各Skillの失敗時に代替手段を提案
4. **進捗管理**: 各Skillの完了状況を可視化
5. **最終評価**: スコアカードで総合判定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | なし（探索分野キーワードはオプション） |
| **出力** | Phase1全成果物（`documents/`, `mvp/`） |
| **次のSkill** | Phase2へ進む or Phase1再実行 |

---

## Instructions

**実行モード**: 自律実行（ステージゲートで停止）
**推定所要時間**: 4-7時間（必須14ステップ）、5.5-8.5時間（全オプション含む）

### Phase1実行ステップ（必須14ステップ + オプション3ステップ）

#### Discovery & Planning（発見・計画）

1. `/discover-demand` - 需要発見リサーチ（15-30分）
2. `/create-mvv` - MVV早期定義（20-40分）
3. `/apply-lean-canvas` - リーンキャンバス作成（60-90分）
4. `/estimate-market-size` - 市場規模推定（30-50分）**[NEW]**
5. `/build-flywheel` - フライホイール設計（30-50分）

**[ステージゲート0: 市場規模]**
- 判定基準: TAM ≥ ¥100億、SAM ≥ ¥50億
- 通過 → STEP 6へ進む
- 未達成 → **停止**、Pivot提案（Human-in-the-Loop必須）

#### Validation（検証）

6. `/research-problem` - Web課題発見（30-60分）
7. `/simulate-interview` - 仮想ペルソナインタビュー（25-45分）
8. `/map-customer-journey` - カスタマージャーニーマップ（30-40分）**[NEW]**
9. `/validate-cpf` - CPF診断（20-30分）

**[ステージゲート1: CPF]**
- 判定基準: CPFスコア60%以上
- 通過 → STEP 10へ進む
- 未達成 → **停止**、改善アクション提示、ユーザー承認後に再開 or 再実行

#### PSF Validation（PSF検証）

10. `/validate-10x` - 10倍優位性検証（40-70分）
11. `[OPTIONAL] /prioritize-features` - 機能優先順位付け（20-30分）**[NEW]**
    - 実行条件: MVP候補10個以上の場合のみ
12. `/build-lp` - LP構築（40-80分）
13. `[OPTIONAL] /design-ab-test` - A/Bテスト設計（30-40分）**[NEW]**
    - 実行条件: LP改善計画策定時のみ
14. `/validate-psf` - PSF診断（5-10分）

**[ステージゲート2: PSF]**
- 判定基準: 10倍2軸以上 + MVP選定完了 + UVP明確
- 通過 → STEP 15へ進む
- 未達成 → **停止**、改善アクション提示、ユーザー承認後に再開 or 再実行

#### Launch Preparation（ローンチ準備）

15. `/create-sns-content` - SNSコンテンツ作成（30-50分）
16. `/startup-scorecard` - 最終評価（20-40分）
17. `[OPTIONAL] /generate-kpi-dashboard` - KPIダッシュボード生成（20-30分）**[NEW]**
    - 実行条件: Phase2準備時のみ（スコアカード32点以上推奨）

### ステージゲート判定

**ステージゲート0: 市場規模**
- **合格条件**: TAM ≥ ¥100億、SAM ≥ ¥50億
- **未達成時**: 停止（Human-in-the-Loop必須）
  - 改善アクション提示: 市場セグメント再定義/ターゲット拡大/別アイデア探索
  - ユーザー承認後に再開 or Phase1再実行

**ステージゲート1: CPF**
- **合格条件**: CPFスコア60%以上
- **未達成時**: 停止（Human-in-the-Loop必須）
  - 改善アクション提示: Problem再定義/Persona絞り込み/UVP調整
  - ユーザー承認後に再開 or Phase1再実行

**ステージゲート2: PSF**
- **合格条件**: 10倍優位性2軸以上達成 + MVP選定完了
- **未達成時**: 停止（Human-in-the-Loop必須）
  - 改善アクション提示: Solution再設計/10倍軸の強化/MVP類型変更
  - ユーザー承認後に再開 or Phase1再実行

### 最終判定（スコアカード）

| 合計スコア | 判定 | 次のアクション |
|:---------:|------|--------------|
| 32-40点 | ✅ Phase1完了 | Phase2へ進む |
| 20-31点 | ⚠️ 要改善 | 低スコア視点を改善後、再評価 |
| 0-19点 | ❌ 要再実行 | Phase1を最初からやり直し |

---

## 成果物

### 最終成果物一覧

```
{IDEA_FOLDER}/
├── documents/
│   ├── 1_initiating/
│   │   ├── demand_discovery.md
│   │   ├── business_idea.md
│   │   └── market_size_estimation.md ← 新規追加（STEP 4）
│   ├── 2_discovery/
│   │   ├── lean_canvas.md
│   │   ├── persona.md
│   │   ├── flywheel.md
│   │   ├── problem_research.md
│   │   ├── interview_simulation.md
│   │   ├── customer_journey_map.md ← 新規追加（STEP 8）
│   │   └── 10x_validation.md
│   ├── 3_planning/
│   │   ├── mvv.md
│   │   ├── cpf_diagnosis.md
│   │   ├── psf_diagnosis.md
│   │   └── ab_test_design.md ← 新規追加（STEP 13、オプション）
│   ├── 4_product/
│   │   └── feature_prioritization.md ← 新規追加（STEP 11、オプション）
│   └── 5_monitoring/
│       ├── scorecard.md
│       └── kpi_dashboard.md ← 新規追加（STEP 17、オプション）
├── mvp/
│   ├── lp/（README.md）
│   └── sns_contents/（posts.md）
└── phase1_summary.md
```

---

## Knowledge Base参照

- 全Skillsドキュメント: `.claude/skills/`
- CPF概念: `@startup_science/01_stages/cpf/cpf_overview.md`
- PSF概念: `@startup_science/01_stages/psf/psf_overview.md`
- PMF概念: `@startup_science/01_stages/pmf/pmf_overview.md`

---

## 使用例

```
User: /orchestrate-phase1

Skill: 探索分野キーワードを入力してください（省略可）:

User: AIツール 業務効率化

Skill:
# Phase1 自律実行開始

探索分野: 「AIツール 業務効率化」
推定所要時間: 4-7時間（必須14ステップ）

[自動実行中...]

## STEP 1: /discover-demand ✅ 完了（30分）
最有望候補: 「議事録自動生成」(スコア: 17/20)

## STEP 2: /create-mvv ✅ 完了（25分）
判定: ✅ MVV完了 (5/5項目合格)

## STEP 3: /apply-lean-canvas ✅ 完了（75分）
判定: ✅ リーンキャンバス完成

## STEP 4: /estimate-market-size ✅ 完了（40分）← 新規
TAM: ¥1.5兆円、SAM: ¥75億円、SOM（5年後）: ¥3.75億円
判定: ⚠️ 要検討（SOM最低基準¥10億未満）

【ステージゲート0: 市場規模】⚠️ 条件付き通過
- SAM ≥ ¥50億（✅）、但しSOM要改善
- 推奨: ターゲット市場拡大またはシェア仮説見直し

[... STEP 5-8 実行 ...]

## STEP 8: /map-customer-journey ✅ 完了（35分）← 新規
6段階マッピング完了、ペインポイント4箇所特定、Quick Wins 6個

## STEP 9: /validate-cpf ✅ 完了（20分）
CPFスコア: 75%

【ステージゲート1: CPF】✅ 通過（75% ≥ 60%）

[... STEP 10-14 実行 ...]

【ステージゲート2: PSF】✅ 通過（10倍3軸 + MVP完了）

[... STEP 15-16 実行 ...]

## Phase1 完了

総所要時間: 7時間5分
総合判定: ✅ Phase1完了
総合スコア: 39/40点

次のアクション:
1. LP公開（Netlify）
2. 広告配信開始
3. Phase2へ進む（/orchestrate-phase2）
```
