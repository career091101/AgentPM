# Orchestrate Phase1 Recruit Skill

ForRecruit Edition Phase1全体を自律実行するオーケストレーターSkill。

---

## Skill情報

- **コマンド**: `/orchestrate-phase1-recruit`
- **目的**: ForRecruit Edition Phase1（CPF→PSF→PMF検証）をRing制度準拠で完全自動実行
- **所要時間**: 8-12時間（自動実行、Phase 2統合により2時間増）
- **実行モード**: 自律実行型（Ring 1-3ステージゲートでHuman-in-the-Loop）
- **統合スキル数**: **23スキル**（Phase 1: 18 + Phase 2: 5）

---

## このSkillでできること

1. **Ring制度準拠の段階的検証**: Ring 1（CPF）→ Ring 2（PSF）→ Ring 3（PMF）
2. **社内承認プロセス統合**: 課長→部長→事業部長→役員の段階的承認
3. **23スキルの順次実行**: Discovery → CPF → PSF → PMF → Launch Preparation（Phase 2: リスク管理5スキル統合）
4. **ステージゲート自動判定**: CPF 50%以上、10倍優位性1軸以上、外部顧客100社以上、カニバリゼーション評価、競争優位性持続性、市場タイミング
5. **エラーハンドリング**: 各Skillの失敗時に代替手段を提案、Yellow/Orange/Red Alert時の撤退戦略、リトライ最大3回

---

## Ring制度ステージゲート

### Ring 1（CPF検証）

**判定基準**:
- CPFスコア: **50%以上**（推奨65%以上）
- Problem Commonality: **60%以上**（推奨70%以上）
- User Research: **10件以上**（推奨30件以上）

**承認**: 課長承認（予算50-100万円）

**通過スキル**: `/validate-cpf`

**停止条件**: CPF 50%未満

---

### Ring 2（PSF検証）

**判定基準**:
- 10倍優位性: **1軸以上**（推奨2軸以上）
- MVP完成: **機能する試作品**
- ROI見込み: **1000%以上**
- 社内リソース活用: **1種以上**（推奨3種以上）

**承認**: 部長・事業部長承認（予算500-1,000万円）

**通過スキル**: `/validate-psf`, `/validate-10x`, `/validate-ring-criteria`

**停止条件**: 10倍優位性0軸 or ROI 1000%未満

---

### Ring 3（PMF検証）

**判定基準**:
- 外部顧客獲得: **100社/人以上**（推奨1,000社/人以上）
- 収益化開始: **初期売上発生**
- 3年黒字・5年累損解消計画: **定量的ロードマップ策定済み**
- Unit Economics健全性: **LTV/CAC 3.0以上**（推奨5.0以上）

**承認**: 役員承認（予算5,000万円-3億円、本格事業化判断）

**通過スキル**: `/validate-pmf`, `/validate-ring-criteria`

**停止条件**: 外部顧客獲得失敗 or 収益化困難

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 探索分野キーワード（オプション）、プロジェクトディレクトリ |
| **出力** | Phase1全成果物（`documents/`, `mvp/`, `internal_approval/`） |
| **次のSkill** | Phase2へ進む or Phase1再実行 |

---

## 前提条件

- プロジェクトディレクトリ（{IDEA_FOLDER}）が存在すること
- WebSearch/WebFetch機能が利用可能であること
- Recruit_Product_Researchが参照可能であること

---

## プロンプト

### セッション開始

```markdown
# Phase1 ForRecruit Edition 自律実行オーケストレーター 開始

**実行モード**: 自律実行（Ring 1-3ステージゲートで停止）
**推定所要時間**: 6-10時間
**Ring制度対応**: Ring 1（CPF）→ Ring 2（PSF）→ Ring 3（PMF）

Phase1を以下の順序で自動実行します:

## フェーズ概要

### PHASE 1: Discovery & Planning（発見・計画）
1. `/discover-demand` - 需要発見リサーチ（TAM 50億円以上）
2. **`/validate-market-timing`** - **市場タイミング検証（5次元評価、Too Early/Too Late判定）** ← Phase 2追加
3. `/create-mvv` - MVV早期定義（企業価値観整合性チェック）
4. `/apply-lean-canvas` - リーンキャンバス作成
5. `/build-flywheel` - フライホイール設計（社内エコシステム連携）
6. `/inventory-internal-resources` - 社内リソース棚卸し（6カテゴリ、ROI定量化）
7. **`/build-synergy-map`** - **4象限シナジーマップ作成（カニバリ vs シナジー評価）** ← Phase 2追加

**[Alert Check 1]** → Too Early判定時は `/design-exit-strategy` で撤退計画立案

### PHASE 2: CPF Validation（Ring 1）
8. `/research-problem` - Web課題発見（ForRecruit版、インタビュー10人）
9. `/simulate-interview` - 仮想ペルソナインタビュー（社内ネットワーク活用）
10. `/validate-cpf` - CPF診断（50%以上）

**[ステージゲート1: Ring 1（CPF）]** → 50%以上で通過、未達成時は停止

### PHASE 3: PSF Validation（Ring 2）
11. `/research-competitors` - 競合調査（外部+既存事業）
12. `/validate-10x` - 10倍優位性検証（1軸以上）
13. **`/analyze-competitive-moat`** - **競争優位性持続可能性分析（Moat Score 6.0以上）** ← Phase 2追加
14. **`/validate-cannibalization`** - **カニバリゼーション評価（Yellow Alert以下で通過）** ← Phase 2追加
15. `/validate-psf` - PSF診断（ROI 1000%以上）
16. `/validate-ring-criteria` - Ring 2基準チェック

**[ステージゲート2: Ring 2（PSF）]** → 10倍1軸以上 + Moat Score 6.0以上 + カニバリYellow以下 + ROI 1000%以上で通過、未達成時は停止
**[Alert Check 2]** → Orange Alert以上の場合は `/design-exit-strategy` で差別化戦略立案 or 撤退検討

### PHASE 4: PMF Validation（Ring 3）
17. `/build-lp` - LP構築（社内向け）
18. `/design-pricing` - 価格設定戦略（Airレジ無料モデル等）
19. `/validate-pmf` - PMF診断（外部顧客100社以上）
20. `/validate-ring-criteria` - Ring 3基準チェック

**[ステージゲート3: Ring 3（PMF）]** → 外部顧客100社+収益化開始で通過、未達成時は停止
**[Alert Check 3]** → Red Alert発動時は `/design-exit-strategy` で撤退計画立案

### PHASE 5: Launch Preparation
21. `/analyze-aarrr` - AARRR分析（社内KPI最適化）
22. `/startup-scorecard` - 最終評価（Ring制度評価項目対応）
23. **`/design-exit-strategy`** - **撤退戦略設計（Yellow/Orange/Red Alert時のみ実行）** ← Phase 2追加

---

**探索分野キーワード**（オプション）:
> [ユーザー入力 or スキップ]

[開始しますか？] → 「はい」で自動実行開始
```

---

## 自動実行フロー

### STEP 0: 事前準備

```yaml
処理: プロジェクトディレクトリ確認・作成
出力:
  - {IDEA_FOLDER}/documents/1_initiating/
  - {IDEA_FOLDER}/documents/2_discovery/
  - {IDEA_FOLDER}/documents/3_planning/
  - {IDEA_FOLDER}/documents/5_monitoring/
  - {IDEA_FOLDER}/documents/internal_approval/
  - {IDEA_FOLDER}/mvp/lp/
  - {IDEA_FOLDER}/mvp/sns_contents/
```

---

### PHASE 1: Discovery & Planning（発見・計画）

#### STEP 1: /discover-demand

```yaml
目的: 需要発見リサーチ（ForRecruit版、TAM 50億円以上）
入力: 探索分野キーワード（オプション）
出力: demand_discovery.md
成功基準: スコア12/20以上、TAM 50億円以上
失敗時対応:
  - スコア12未満 → 別の探索分野を試行（最大3回）
  - TAM 50億円未満 → ニッチ化提案 or Human-in-the-Loop
```

#### STEP 2: /create-mvv

```yaml
目的: MVV早期定義（企業価値観整合性チェック）
入力: demand_discovery.md
出力: mvv.md
成功基準: 5/5項目合格、企業価値観整合性チェック通過
失敗時対応:
  - 不合格項目を再生成（最大3回）
  - 企業価値観との整合性低下 → Human-in-the-Loop
```

#### STEP 3: /apply-lean-canvas

```yaml
目的: リーンキャンバス作成
入力: demand_discovery.md, mvv.md
出力: lean_canvas.md
成功基準: 9セクションすべて完成
失敗時対応:
  - 不完全セクションを再生成（最大3回）
  - 3回失敗 → Human-in-the-Loop
```

#### STEP 4: /build-flywheel

```yaml
目的: フライホイール設計（社内エコシステム連携）
入力: lean_canvas.md
出力: flywheel.md
成功基準: 8/10点以上、社内エコシステム連携明示
失敗時対応:
  - 低スコア項目を再設計（最大3回）
  - 社内エコシステム連携不明確 → Human-in-the-Loop
```

#### STEP 5: /inventory-internal-resources

```yaml
目的: 社内リソース棚卸し（6カテゴリ、ROI定量化）
入力: lean_canvas.md
出力: resource_inventory.md
成功基準: リソース3種以上活用、ROI 1000%以上
失敗時対応:
  - リソース3種未満 → 追加リソース検討提案
  - ROI 1000%未満 → リソース活用強化提案 or Human-in-the-Loop
```

---

### PHASE 2: CPF Validation（Ring 1）

#### STEP 6: /research-problem

```yaml
目的: Web課題発見（ForRecruit版、インタビュー10人）
入力: lean_canvas.md, persona.md
出力: problem_research.md
成功基準: 35/50点以上（強い裏付け）、Problem Commonality 60%以上
失敗時対応:
  - 20-34点 → ニッチ化を試行
  - 19点以下 → 課題仮説見直し提案
  - Problem Commonality 60%未満 → ターゲット見直し提案
  - Human-in-the-Loop
```

#### STEP 7: /simulate-interview

```yaml
目的: 仮想ペルソナインタビュー（社内ネットワーク活用）
入力: persona.md, lean_canvas.md
出力: interview_simulation.md
成功基準: 32/40点以上（良好）、10件以上のインタビュー
失敗時対応:
  - 24-31点 → UVP調整
  - 23点以下 → Problem/ペルソナ見直し提案
  - インタビュー10件未満 → 追加インタビュー推奨
  - Human-in-the-Loop
```

#### STEP 8: /validate-cpf

```yaml
目的: CPF診断（50%以上）
入力: lean_canvas.md, problem_research.md, interview_simulation.md
出力: cpf_diagnosis.md
成功基準: CPFスコア50%以上
失敗時対応:
  - 50%未満 → **ステージゲート1停止**（Human-in-the-Loop必須）
```

---

### 【ステージゲート1: Ring 1（CPF）】

```yaml
判定基準: CPFスコア50%以上
通過 → PHASE 3へ進む
未達成 → 停止、改善アクション提示、ユーザー承認後に再開 or 再実行

改善アクション例:
  - CPFスコア50%未満 → 追加インタビュー20件実施
  - Problem Commonality 60%未満 → ターゲット顧客セグメント見直し
  - User Research 10件未満 → 社内ネットワーク活用で追加ヒアリング

承認フロー:
  - /build-approval-deck Ring 1テンプレート作成
  - 課長承認プレゼン実施（予算50-100万円）
  - 承認後 → Ring 2へ進む
```

---

### PHASE 3: PSF Validation（Ring 2）

#### STEP 9: /research-competitors

```yaml
目的: 競合調査（外部+既存事業）
入力: lean_canvas.md, problem_validation.md
出力: competitor_research.md
成功基準: 競合3社以上分析、既存事業との差別化明確
失敗時対応:
  - 競合3社未満 → 追加競合調査
  - 既存事業とのカニバリ懸念 → 差別化戦略再設計 or Human-in-the-Loop
```

#### STEP 10: /validate-10x

```yaml
目的: 10倍優位性検証（1軸以上）
入力: lean_canvas.md, competitor_research.md, resource_inventory.md
出力: 10x_validation.md
成功基準: 1軸以上で10倍達成
失敗時対応:
  - 1軸未満 → 社内リソース活用強化提案 or ソリューション見直し
  - Human-in-the-Loop
```

#### STEP 11: /validate-psf

```yaml
目的: PSF診断（ROI 1000%以上）
入力: lean_canvas.md, 10x_validation.md, resource_inventory.md
出力: psf_diagnosis.md
成功基準: ROI 1000%以上、10倍優位性1軸以上
失敗時対応:
  - ROI 1000%未満 → リソース活用強化提案
  - 10倍優位性0軸 → ソリューション見直し提案
  - Human-in-the-Loop
```

#### STEP 12: /validate-ring-criteria

```yaml
目的: Ring 2基準チェック
入力: cpf_diagnosis.md, psf_diagnosis.md, 10x_validation.md, resource_inventory.md
出力: ring2_criteria_check.md
成功基準: Ring 2基準クリア（10倍1軸以上、ROI 1000%以上、MVP完成）
失敗時対応:
  - Ring 2基準未達 → **ステージゲート2停止**（Human-in-the-Loop必須）
```

---

### 【ステージゲート2: Ring 2（PSF）】

```yaml
判定基準: 10倍優位性1軸以上 + ROI 1000%以上 + MVP完成
通過 → PHASE 4へ進む
未達成 → 停止、改善アクション提示、ユーザー承認後に再開 or 再実行

改善アクション例:
  - 10倍優位性0軸 → 社内リソース活用軸追加（営業網、データ資産等）
  - ROI 1000%未満 → リソース3種以上活用でROI向上
  - MVP未完成 → 開発スプリント追加

承認フロー:
  - /build-approval-deck Ring 2テンプレート作成
  - 部長・事業部長承認プレゼン実施（予算500-1,000万円）
  - 社内PoC実施許可獲得
  - 承認後 → Ring 3へ進む
```

---

### PHASE 4: PMF Validation（Ring 3）

#### STEP 13: /build-lp

```yaml
目的: LP構築（社内向け）
入力: lean_canvas.md, persona.md, psf_diagnosis.md
出力: mvp/lp/
成功基準: 5/5項目合格、社内PoC用LP完成
失敗時対応:
  - 不合格項目を修正（最大3回）
  - 3回失敗 → Human-in-the-Loop
```

#### STEP 14: /design-pricing

```yaml
目的: 価格設定戦略（Airレジ無料モデル等）
入力: lean_canvas.md, competitor_research.md, resource_inventory.md
出力: pricing_strategy.md
成功基準: 価格モデル3パターン以上、収益化ロードマップ策定
失敗時対応:
  - 価格モデル不足 → 追加パターン提案
  - 収益化困難 → ビジネスモデル見直し提案 or Human-in-the-Loop
```

#### STEP 15: /validate-pmf

```yaml
目的: PMF診断（外部顧客100社以上）
入力: lean_canvas.md, mvp/lp/, pricing_strategy.md
出力: pmf_diagnosis.md
成功基準: 外部顧客100社以上、収益化開始、NPS 50以上
失敗時対応:
  - 外部顧客100社未満 → 社内PoC延長 or 外部展開戦略見直し
  - 収益化困難 → 価格設定見直し or ビジネスモデル変更
  - NPS 50未満 → MVP改善 or ターゲット見直し
  - Human-in-the-Loop
```

#### STEP 16: /validate-ring-criteria

```yaml
目的: Ring 3基準チェック
入力: pmf_diagnosis.md, pricing_strategy.md, resource_inventory.md
出力: ring3_criteria_check.md
成功基準: Ring 3基準クリア（外部顧客100社以上、収益化開始、3年黒字計画策定済み）
失敗時対応:
  - Ring 3基準未達 → **ステージゲート3停止**（Human-in-the-Loop必須）
```

---

### 【ステージゲート3: Ring 3（PMF）】

```yaml
判定基準: 外部顧客100社以上 + 収益化開始 + 3年黒字・5年累損解消計画策定済み
通過 → PHASE 5へ進む
未達成 → 停止、改善アクション提示、撤退判断 or ユーザー承認後に再開

改善アクション例:
  - 外部顧客100社未満 → 社内PoC延長、クロスセル強化
  - 収益化困難 → 価格設定見直し、サブスクモデル導入
  - 3年黒字計画未策定 → 財務シミュレーション再実施

撤退判断:
  - 5年累損解消不可能 → 撤退推奨
  - 市場縮小・競合優位性喪失 → 撤退推奨
  - コア事業とのシナジーなし → 撤退推奨

承認フロー:
  - /build-approval-deck Ring 3テンプレート作成
  - 役員承認プレゼン実施（予算5,000万円-3億円、本格事業化判断）
  - 独立事業部化判断
  - 承認後 → PHASE 5へ進む
```

---

### PHASE 5: Launch Preparation

#### STEP 17: /analyze-aarrr

```yaml
目的: AARRR分析（社内KPI最適化）
入力: pmf_diagnosis.md, pricing_strategy.md
出力: aarrr_analysis.md
成功基準: AARRR各指標設定、改善施策3つ以上
失敗時対応:
  - 指標不足 → 追加指標設定
  - 改善施策不足 → 追加施策提案 or Human-in-the-Loop
```

#### STEP 18: /startup-scorecard

```yaml
目的: 最終評価（Ring制度評価項目対応）
入力: 全成果物
出力: scorecard.md
成功基準: 32/40点以上（健全）
失敗時対応:
  - 20-31点 → 低スコア視点を改善提案
  - 19点以下 → Phase1再実行提案
  - Human-in-the-Loop
```

#### STEP 19: 最終報告

```yaml
処理: 全成果物のサマリー生成
出力: phase1_summary.md
内容:
  - 成果物一覧
  - 各ステージゲート結果（Ring 1-3）
  - 社内承認プロセス状況
  - 次のアクション
```

---

## 判定ロジック

### ステージゲート1: Ring 1（CPF）

| 判定基準 | 合格条件 | 停止条件 |
|---------|---------|---------|
| CPFスコア | 50%以上 | 50%未満 |
| Problem Commonality | 60%以上（推奨70%以上） | 60%未満 |
| User Research | 10件以上（推奨30件以上） | 10件未満 |

**未達成時の対応**:
1. 停止（Human-in-the-Loop必須）
2. 改善アクション提示:
   - CPFスコア50%未満 → 追加インタビュー20件実施
   - Problem Commonality 60%未満 → ターゲット顧客セグメント見直し
   - User Research 10件未満 → 社内ネットワーク活用で追加ヒアリング
3. ユーザー承認後に再開 or Phase1再実行

---

### ステージゲート2: Ring 2（PSF）

| 判定基準 | 合格条件 | 停止条件 |
|---------|---------|---------|
| 10倍優位性 | 1軸以上達成 | 0軸 |
| ROI見込み | 1000%以上 | 1000%未満 |
| MVP完成 | 完了 | 未完了 |
| 社内リソース活用 | 1種以上（推奨3種以上） | 0種 |

**未達成時の対応**:
1. 停止（Human-in-the-Loop必須）
2. 改善アクション提示:
   - 10倍優位性0軸 → 社内リソース活用軸追加（営業網、データ資産等）
   - ROI 1000%未満 → リソース3種以上活用でROI向上
   - MVP未完成 → 開発スプリント追加
   - 社内リソース0種 → /inventory-internal-resources 再実行
3. ユーザー承認後に再開 or Phase1再実行

---

### ステージゲート3: Ring 3（PMF）

| 判定基準 | 合格条件 | 停止条件 |
|---------|---------|---------|
| 外部顧客獲得 | 100社/人以上 | 100社/人未満 |
| 収益化開始 | 開始 | 未開始 |
| 3年黒字・5年累損解消計画 | 策定済み | 未策定 |
| Unit Economics | LTV/CAC 3.0以上（推奨5.0以上） | LTV/CAC 3.0未満 |

**未達成時の対応**:
1. 停止（Human-in-the-Loop必須）
2. 改善アクション提示:
   - 外部顧客100社未満 → 社内PoC延長、クロスセル強化
   - 収益化困難 → 価格設定見直し、サブスクモデル導入
   - 3年黒字計画未策定 → 財務シミュレーション再実施
   - LTV/CAC 3.0未満 → Unit Economics改善施策実施
3. 撤退判断 or ユーザー承認後に再開

**撤退判断**:
- 5年累損解消不可能 → 撤退推奨
- 市場縮小・競合優位性喪失 → 撤退推奨
- コア事業とのシナジーなし → 撤退推奨

---

### 最終判定（スコアカード）

| 合計スコア | 判定 | 次のアクション |
|:---------:|------|--------------|
| 32-40点 | ✅ Phase1完了 | 本格事業化推奨 |
| 20-31点 | ⚠️ 要改善 | 低スコア視点を改善後、再評価 |
| 0-19点 | ❌ 要再実行 | Phase1を最初からやり直し |

---

## エラーハンドリング

| エラー種別 | 対応 | リトライ上限 |
|-----------|------|:----------:|
| Skill実行失敗 | 代替手段提案 | 3回 |
| ステージゲート未達成 | 停止、改善アクション提示 | - |
| 3回連続失敗 | Human-in-the-Loop | - |
| ユーザー中断 | 進捗保存、再開可能 | - |

**エラーパターン詳細**: @.claude/skills/_shared/error_handling_patterns.md

---

## Knowledge Base参照

### ForRecruit特化ナレッジ

- **Recruit_Product_Research**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/analysis/integrated_analysis_report.md`
- **Ring制度ガイドライン**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/README.md`
- **社内承認プロセス**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/analysis/approval_deck_templates.md`（将来作成予定）

### 共通ナレッジ

- **CPF概念**: `@startup_science/01_stages/cpf/cpf_overview.md`
- **PSF概念**: `@startup_science/01_stages/psf/psf_overview.md`
- **PMF概念**: `@startup_science/01_stages/pmf/pmf_overview.md`
- **全Skillsドキュメント**: `.claude/skills/for_recruit/`

---

## 成果物フォーマット

### 最終成果物一覧

```
{IDEA_FOLDER}/
├── documents/
│   ├── 1_initiating/
│   │   ├── demand_discovery.md       # STEP 1
│   │   └── business_idea.md          # 自動生成
│   ├── 2_discovery/
│   │   ├── lean_canvas.md            # STEP 3
│   │   ├── persona.md                # 自動生成
│   │   ├── flywheel.md               # STEP 4
│   │   ├── problem_research.md       # STEP 6
│   │   ├── interview_simulation.md   # STEP 7
│   │   ├── competitor_research.md    # STEP 9
│   │   └── 10x_validation.md         # STEP 10
│   ├── 3_planning/
│   │   ├── mvv.md                    # STEP 2
│   │   ├── cpf_diagnosis.md          # STEP 8
│   │   ├── psf_diagnosis.md          # STEP 11
│   │   ├── pmf_diagnosis.md          # STEP 15
│   │   ├── pricing_strategy.md       # STEP 14
│   │   └── aarrr_analysis.md         # STEP 17
│   ├── 5_monitoring/
│   │   └── scorecard.md              # STEP 18
│   └── internal_approval/            # ForRecruit特化
│       ├── resource_inventory.md     # STEP 5
│       ├── ring1_criteria_check.md   # STEP 8（自動生成）
│       ├── ring2_criteria_check.md   # STEP 12
│       ├── ring3_criteria_check.md   # STEP 16
│       └── approval_deck_ringX.md    # /build-approval-deck 実行時
├── mvp/
│   ├── lp/                           # STEP 13
│   │   ├── index.html
│   │   ├── css/
│   │   ├── js/
│   │   └── README.md
│   └── sns_contents/                 # 将来作成予定
│       ├── posts_x.md
│       ├── posts_linkedin.md
│       ├── hashtags.md
│       └── schedule.md
└── phase1_summary.md                 # STEP 19
```

---

### phase1_summary.md 例

```markdown
# Phase1 ForRecruit Edition 完了報告

**作成日**: [YYYY-MM-DD]
**プロジェクト**: [プロジェクト名]
**総合判定**: ✅Phase1完了 / ⚠️要改善 / ❌要再実行
**総合スコア**: [X/40点]
**Ring制度**: Ring 1-3すべて通過 / Ring [X]まで通過

---

## エグゼクティブサマリー

### 成果物一覧

| # | Skill | 成果物 | 判定 |
|:-:|-------|--------|:----:|
| 1 | `/discover-demand` | demand_discovery.md | ✅/⚠️/❌ |
| 2 | `/create-mvv` | mvv.md | ✅/⚠️/❌ |
| 3 | `/apply-lean-canvas` | lean_canvas.md | ✅/⚠️/❌ |
| 4 | `/build-flywheel` | flywheel.md | ✅/⚠️/❌ |
| 5 | `/inventory-internal-resources` | resource_inventory.md | ✅/⚠️/❌ |
| 6 | `/research-problem` | problem_research.md | ✅/⚠️/❌ |
| 7 | `/simulate-interview` | interview_simulation.md | ✅/⚠️/❌ |
| 8 | `/validate-cpf` | cpf_diagnosis.md | ✅/⚠️/❌ |
| 9 | `/research-competitors` | competitor_research.md | ✅/⚠️/❌ |
| 10 | `/validate-10x` | 10x_validation.md | ✅/⚠️/❌ |
| 11 | `/validate-psf` | psf_diagnosis.md | ✅/⚠️/❌ |
| 12 | `/validate-ring-criteria` (Ring 2) | ring2_criteria_check.md | ✅/⚠️/❌ |
| 13 | `/build-lp` | mvp/lp/ | ✅/⚠️/❌ |
| 14 | `/design-pricing` | pricing_strategy.md | ✅/⚠️/❌ |
| 15 | `/validate-pmf` | pmf_diagnosis.md | ✅/⚠️/❌ |
| 16 | `/validate-ring-criteria` (Ring 3) | ring3_criteria_check.md | ✅/⚠️/❌ |
| 17 | `/analyze-aarrr` | aarrr_analysis.md | ✅/⚠️/❌ |
| 18 | `/startup-scorecard` | scorecard.md | ✅/⚠️/❌ |

**完成度**: [X/18]

---

### Ring制度ステージゲート結果

#### Ring 1（CPF検証）

**判定**: [✅ 通過 / ❌ 未達成]

**CPFスコア**: [X%]

| 基準 | 目標 | 実績 | 判定 |
|------|------|------|:----:|
| CPFスコア | ≥ 50% | [X%] | ✅/❌ |
| Problem Commonality | ≥ 60% | [X%] | ✅/❌ |
| User Research | ≥ 10件 | [X件] | ✅/❌ |

**承認状況**: [課長承認取得 / 承認待ち / 未申請]

**結果**: [通過した / 改善アクション実施後に通過 / 未達成]

---

#### Ring 2（PSF検証）

**判定**: [✅ 通過 / ❌ 未達成]

**10倍優位性**: [X/5軸達成]

| 基準 | 目標 | 実績 | 判定 |
|------|------|------|:----:|
| 10倍優位性 | ≥ 1軸 | [X軸] | ✅/❌ |
| ROI見込み | ≥ 1000% | [X%] | ✅/❌ |
| MVP完成 | 完成 | [完成/未完成] | ✅/❌ |
| 社内リソース活用 | ≥ 1種 | [X種] | ✅/❌ |

**承認状況**: [部長・事業部長承認取得 / 承認待ち / 未申請]

**社内PoC**: [実施済み / 実施中 / 未実施]

**結果**: [通過した / 改善アクション実施後に通過 / 未達成]

---

#### Ring 3（PMF検証）

**判定**: [✅ 通過 / ❌ 未達成]

**外部顧客数**: [X社/人]

| 基準 | 目標 | 実績 | 判定 |
|------|------|------|:----:|
| 外部顧客獲得 | ≥ 100社/人 | [X社/人] | ✅/❌ |
| 収益化開始 | 開始 | [開始/未開始] | ✅/❌ |
| 3年黒字計画 | 策定済み | [策定済み/未策定] | ✅/❌ |
| Unit Economics | LTV/CAC ≥ 3.0 | [X] | ✅/❌ |

**承認状況**: [役員承認取得 / 承認待ち / 未申請]

**本格事業化判断**: [承認 / 保留 / 撤退]

**結果**: [通過した / 改善アクション実施後に通過 / 未達成]

---

### 最終スコアカード

| 視点 | スコア | 判定 |
|------|:------:|:----:|
| Financial | X/10 | ✅/⚠️/❌ |
| Customer | X/10 | ✅/⚠️/❌ |
| Internal Process | X/10 | ✅/⚠️/❌ |
| Learning & Growth | X/10 | ✅/⚠️/❌ |
| **合計** | **X/40** | **✅/⚠️/❌** |

---

## プロジェクトサマリー

### ビジネスアイデア

**プロダクト名**: [プロダクト名]

**UVP**: [UVP 30文字以内]

**ターゲット**: [ペルソナ要約]

**課題**: [Problem要約]

**ソリューション**: [Solution要約]

---

### 需要発見結果

**探索分野**: [キーワード]

**TAM**: [XX億円]

**有望候補**: [需要候補タイトル]

**スコア**: [X/20点]

**判定**: [✅有望 / ⚠️検討余地 / ❌見送り]

---

### 社内リソース活用結果

**活用リソース数**: [X種]（目標: 3種以上）

**総合ROI**: [X%]（目標: 1000%以上）

**活用したリソース**:
1. [リソース1]: [活用方法]
2. [リソース2]: [活用方法]
3. [リソース3]: [活用方法]

**コスト削減効果**: [X億円]

**売上増加効果**: [X億円]

---

### CPF検証結果

**CPFスコア**: [X%]

**判定**: [✅ 50%以上 / ❌ 50%未満]

**Problem Commonality**: [X%]

**User Research**: [X件]

**3U検証**:
- Unworkable: [✅/❌]
- Unavoidable: [✅/❌]
- Urgent: [✅/❌]

**課題裏付け**: [強い / 中程度 / 不足]

---

### PSF検証結果

**10倍優位性**: [X/5軸達成]

**達成した軸**:
1. [軸名]: [X倍]
2. [軸名]: [Y倍]

**ROI**: [X%]

**社内リソース活用**: [X種]

**MVP**: [完成 / 未完成]

**社内PoC**: [実施済み / 実施中 / 未実施]

---

### PMF検証結果

**外部顧客数**: [X社/人]

**収益化**: [開始 / 未開始]

**初年度売上**: [X億円]

**Unit Economics**:
- LTV: [X万円]
- CAC: [X万円]
- LTV/CAC比: [X]
- Churn率: [X%]

**3年黒字計画**: [策定済み / 未策定]

**5年累損解消**: [見込みあり / 見込みなし]

---

## 次のアクション

### ✅ Phase1完了の場合

**推奨フロー**:
1. 役員承認プレゼン実施（Ring 3）
2. 本格事業化判断取得
3. 独立事業部化
4. 外部顧客獲得加速（1,000社目標）
5. 3年黒字達成に向けた実行

**具体的ステップ**:
1. /build-approval-deck Ring 3テンプレート作成
2. 役員承認プレゼン実施
3. 予算5,000万円-3億円獲得
4. 独立事業部化、採用強化
5. 本格マーケティング、クロスセル促進

---

### ⚠️ 要改善の場合

**低スコア視点**: [視点名]

**改善アクション**:
1. [アクション1]
2. [アクション2]
3. [アクション3]

**推奨Skill**:
- `/[skill名]`

**改善後**: 再度 `/startup-scorecard` を実行し、32点以上でPhase2へ

---

### ❌ 要再実行の場合

**問題点**: [何が不足しているか]

**推奨アクション**:
1. `/orchestrate-phase1-recruit` を再実行
2. または以下のSkillを個別に再実行:
   - `/discover-demand` - 別の探索分野
   - `/create-mvv` - MVV再定義
   - `/apply-lean-canvas` - Problem/Solution見直し
   - `/inventory-internal-resources` - リソース活用強化

---

## 所要時間・リソース

| 項目 | 内容 |
|------|------|
| 総所要時間 | [X時間Y分] |
| Ring 1達成期間 | [Xヶ月] |
| Ring 2達成期間 | [Xヶ月] |
| Ring 3達成期間 | [Xヶ月] |
| ステージゲート停止回数 | [X回] |
| Human-in-the-Loop回数 | [Y回] |
| リトライ回数 | [Z回] |

---

## レッスンズラーンド

### うまくいったこと

1. [良かった点1]
2. [良かった点2]
3. [良かった点3]

### 改善すべきこと

1. [改善点1]
2. [改善点2]
3. [改善点3]

---

## 次回への引継ぎ

本格事業化前に確認すべきこと:
- [ ] 役員承認取得完了
- [ ] 独立事業部化判断
- [ ] 予算確保（5,000万円-3億円）
- [ ] 採用計画策定
- [ ] 外部顧客獲得計画（1,000社目標）
- [ ] 3年黒字・5年累損解消計画の精緻化

Phase2で実施すること:
- 外部顧客1,000社獲得（クロスセル強化）
- 3年黒字達成に向けた実行
- Unit Economics最適化（LTV/CAC 5.0以上）
- 独立事業部としてのガバナンス確立
```

---

## ForRecruit Knowledge Base Reference

### 評価基準・フレームワーク
- CPF/PSF/PMF基準: @.claude/skills/_shared/recruit_specific_frameworks.md#cpf-evaluation
- Ring制度詳細: @.claude/skills/_shared/recruit_specific_frameworks.md#ring-system
- 社内リソース活用: @.claude/skills/_shared/recruit_specific_frameworks.md#resource-leverage
- ForRecruit評価基準: @.claude/skills/_shared/knowledge_base.md#forrecruit-evaluation

### 事例参照
- 成功パターン（Tier 1-4）: @.claude/skills/_shared/case_reference_for_recruit.md#success-patterns
- 失敗パターン: @.claude/skills/_shared/case_reference_for_recruit.md#failure-patterns
- スキル別推奨事例: @.claude/skills/_shared/case_reference_for_recruit.md#skill-mapping-orchestrate
- 18スキル統合フロー: @.claude/skills/_shared/knowledge_base.md#forrecruit-orchestration

### 全体参照
- ForRecruit全体概要: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
- Ring制度ステージゲート: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
- 撤退基準: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---
## 使用例

```
User: /orchestrate-phase1-recruit

Skill:
# Phase1 ForRecruit Edition 自律実行オーケストレーター 開始

探索分野キーワードを入力してください（省略可）:

User: 美容室 予約管理

Skill:
# Phase1 自律実行開始

探索分野: 「美容室 予約管理」
推定所要時間: 6-10時間
Ring制度対応: Ring 1 → Ring 2 → Ring 3

[自動実行中...]

---

## PHASE 1: Discovery & Planning

### STEP 1: /discover-demand
[自動実行中...] ✅ 完了（35分）
- 需要候補: 「美容室向け予約管理システム」
- TAM: 500億円
- スコア: 18/20点
- 判定: ✅ 有望需要あり

---

### STEP 2: /create-mvv
[自動実行中...] ✅ 完了（30分）
- Mission: [Mission文]
- Vision: [Vision文]
- Values: [4個]
- 企業価値観整合性: ✅ 合格
- 判定: ✅ MVV完了 (5/5項目合格)

---

### STEP 3: /apply-lean-canvas
[自動実行中...] ✅ 完了（45分）
- 9セクション完成
- 判定: ✅ 完了

---

### STEP 4: /build-flywheel
[自動実行中...] ✅ 完了（40分）
- 成長エンジン: Sticky（社内エコシステム連携）
- スコア: 9/10点
- 判定: ✅ 完了

---

### STEP 5: /inventory-internal-resources
[自動実行中...] ✅ 完了（60分）
- 活用リソース数: **6種**
- 総合ROI: **2,498%**
- コスト削減効果: 26.57億円
- 売上増加効果: 7.2億円
- 判定: ✅ リソース活用優良（3種以上、ROI 1000%以上）

---

## PHASE 2: CPF Validation (Ring 1)

### STEP 6: /research-problem
[自動実行中...] ✅ 完了（55分）
- 生ログ収集: 100件
- Problem Commonality: 75%
- スコア: 40/50点
- 判定: ✅ 強い裏付け

---

### STEP 7: /simulate-interview
[自動実行中...] ✅ 完了（35分）
- UVP刺さり度: 36/40点
- 3U検証: 14/15点
- インタビュー件数: 15件
- 判定: ✅ 良好

---

### STEP 8: /validate-cpf
[自動実行中...] ✅ 完了（25分）
- CPFスコア: **68%**
- Problem Commonality: 75%
- User Research: 15件
- 判定: ✅ CPF達成

---

## 【ステージゲート1: Ring 1（CPF）】

**判定**: ✅ **通過**（CPFスコア68% ≥ 50%）

**Ring 1基準チェック**:
- CPFスコア: 68% ≥ 50% ✅
- Problem Commonality: 75% ≥ 60% ✅
- User Research: 15件 ≥ 10件 ✅

**推奨**: /build-approval-deck Ring 1テンプレート作成 → 課長承認プレゼン

→ PHASE 3へ進みます

---

## PHASE 3: PSF Validation (Ring 2)

### STEP 9: /research-competitors
[自動実行中...] ✅ 完了（60分）
- 競合分析: 4社（TableCheck、STORES予約、トレタ、既存事業）
- 差別化ポイント: 5軸
- 判定: ✅ 完了

---

### STEP 10: /validate-10x
[自動実行中...] ✅ 完了（65分）
- 10倍達成軸: **4/5軸**
  - コスト削減: ∞倍（初期費用0円）
  - 時間短縮: 7倍（導入1週間→1日）
  - 営業網活用: 5倍（CAC削減）
  - エコシステム連携: 3倍（Airレジ・Airペイ統合）
- 判定: ✅ 10倍達成

---

### STEP 11: /validate-psf
[自動実行中...] ✅ 完了（30分）
- ROI: **2,498%**
- 10倍優位性: 4軸
- 社内リソース活用: 6種
- 判定: ✅ PSF達成

---

### STEP 12: /validate-ring-criteria (Ring 2)
[自動実行中...] ✅ 完了（20分）
- 10倍優位性: 4軸 ≥ 1軸 ✅
- ROI: 2,498% ≥ 1000% ✅
- MVP: 完成 ✅
- 社内リソース: 6種 ≥ 1種 ✅
- 判定: ✅ Ring 2基準クリア

---

## 【ステージゲート2: Ring 2（PSF）】

**判定**: ✅ **通過**（10倍4軸 + ROI 2,498% + MVP完成）

**Ring 2基準チェック**:
- 10倍優位性: 4軸 ≥ 1軸 ✅
- ROI: 2,498% ≥ 1000% ✅
- MVP: 完成 ✅
- 社内リソース: 6種 ≥ 1種 ✅

**推奨**: /build-approval-deck Ring 2テンプレート作成 → 部長・事業部長承認プレゼン → 社内PoC実施

→ PHASE 4へ進みます

---

## PHASE 4: PMF Validation (Ring 3)

### STEP 13: /build-lp
[自動実行中...] ✅ 完了（70分）
- LP構築完了（社内PoC用）
- 判定: ✅ 完了 (5/5項目合格)

---

### STEP 14: /design-pricing
[自動実行中...] ✅ 完了（40分）
- 価格モデル: 3パターン（基本3,000円、プレミアム10,000円、エンタープライズ）
- 収益化ロードマップ: 策定済み
- 判定: ✅ 完了

---

### STEP 15: /validate-pmf
[自動実行中...] ✅ 完了（50分）
- 外部顧客数: **15,000店舗**
- 収益化: 開始（初年度売上4.32億円）
- NPS: 65
- 継続率: 85%
- 判定: ✅ PMF達成

---

### STEP 16: /validate-ring-criteria (Ring 3)
[自動実行中...] ✅ 完了（25分）
- 外部顧客: 15,000店舗 ≥ 100社 ✅
- 収益化: 開始 ✅
- 3年黒字計画: 策定済み ✅
- Unit Economics: LTV/CAC 15.0 ≥ 3.0 ✅
- 判定: ✅ Ring 3基準クリア

---

## 【ステージゲート3: Ring 3（PMF）】

**判定**: ✅ **通過**（外部顧客15,000店舗 + 収益化開始 + 3年黒字計画策定済み）

**Ring 3基準チェック**:
- 外部顧客: 15,000店舗 ≥ 100社 ✅
- 収益化: 開始 ✅
- 3年黒字計画: 策定済み ✅
- Unit Economics: LTV/CAC 15.0 ≥ 3.0 ✅

**推奨**: /build-approval-deck Ring 3テンプレート作成 → 役員承認プレゼン → 本格事業化判断

→ PHASE 5へ進みます

---

## PHASE 5: Launch Preparation

### STEP 17: /analyze-aarrr
[自動実行中...] ✅ 完了（45分）
- AARRR各指標設定: 完了
- 改善施策: 5つ
- 判定: ✅ 完了

---

### STEP 18: /startup-scorecard
[自動実行中...] ✅ 完了（30分）
- 総合スコア: **39/40点**
- 判定: ✅ 健全

---

### STEP 19: 最終報告
[生成中...] ✅ 完了（10分）
- phase1_summary.md 生成完了

---

## Phase1 完了

**総所要時間**: 9時間45分
**総合判定**: ✅ Phase1完了
**総合スコア**: 39/40点
**Ring制度**: Ring 1-3すべて通過

**成果物**:
- documents/: 18ファイル
- mvp/lp/: LP一式
- internal_approval/: Ring 1-3承認チェック結果、リソース棚卸し

**次のアクション**:
1. /build-approval-deck Ring 3テンプレート作成
2. 役員承認プレゼン実施
3. 本格事業化判断取得
4. 独立事業部化
5. 外部顧客1,000社獲得に向けた加速

詳細は `phase1_summary.md` を参照してください。
```

---

## 注意事項

1. **Ring制度準拠の徹底**: 各ステージゲートで必ず停止し、基準未達の場合はHuman-in-the-Loop
2. **社内リソース活用**: 3種以上活用でROI 1000%以上、PMFスコア8.8を目標
3. **定量データ重視**: 主観ではなく数値で判断、Recruit_Product_Research事例でベンチマーク
4. **社内承認プロセス**: Ring 1-3各段階で課長→部長→役員承認を取得
5. **撤退基準の明示**: 5年累損解消不可能、市場縮小、競合優位性喪失の場合は撤退推奨

---

## 更新履歴

- 2026-01-02: ForRecruit Edition特化版として新規作成、Ring制度統合、18スキル対応
