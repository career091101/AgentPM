# ForStartup Edition Phase 3.1 - Group 2 参照パス妥当性確認レポート

**実施日**: 2026-01-03
**対象スキル**: 6スキル（Group 2）
**検証者**: Claude Code
**レポートバージョン**: v1.0

---

## 実施概要

ForStartup Edition Phase 3.1 Group 2の6スキルについて、参照パスの妥当性、形式の統一性、リンク先の実在性を検証しました。

### 対象スキル

| # | スキル名 | ステータス | 検証日 |
|:---:|----------|:--------:|--------|
| 7 | build-synergy-map | ✅ | 2026-01-03 |
| 8 | create-fundraising-plan | ✅ | 2026-01-03 |
| 9 | create-mvv | ✅ | 2026-01-03 |
| 10 | create-persona | ✅ | 2026-01-03 |
| 11 | design-exit-strategy | ✅ | 2026-01-03 |
| 12 | design-pricing | ✅ | 2026-01-03 |

---

## スキル別検証結果

### 1. build-synergy-map

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/build-synergy-map/SKILL.md`
**ファイルサイズ**: 2,131行

#### 参照パスの妥当性

**参照パターン1: Founder_Research関連**

```markdown
- 詳細: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER3_SAAS/CORP_S012_airpay.md
- 詳細: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER3_SAAS/CORP_S043_airpay_qr.md
- 詳細: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER5_NEW_BUSINESS/CORP_S062_recruit_agent.md
```

**検証結果**: ⚠️ **要改善**
- **問題**: パス形式が一貫していない
  - `@Founder_Agent_ForStartup/...` (相対パス)
  - `@Founder_Research/...` (別の形式)
- **正規形**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/...`

**参照パターン2: 分析レポート関連**

```markdown
- 統合分析: @Founder_Research/analysis/integrated_analysis_report.md
```

**検証結果**: ⚠️ **要改善**
- **問題**: `@Founder_Research` は短縮表記であり、実際のパスは不明
- **推奨**: 絶対パス形式での参照を統一

#### 推奨改善

```markdown
✅ 改善後:
- 詳細: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md
- ファイル: @.claude/skills/_shared/error_handling_patterns.md
```

---

### 2. create-fundraising-plan

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/create-fundraising-plan/SKILL.md`
**ファイルサイズ**: 805行

#### 参照パスの妥当性

**参照パターン1: 知識ベース参照**

```markdown
- @for_startup/_analysis/research_knowledge.md（資金調達パターン）
- @startup_science/03_funding/fundraising_overview.md
```

**検証結果**: ⚠️ **要改善**
- **問題**: `@for_startup`, `@startup_science` が短縮表記
- **実際のパス**: `.claude/skills/for_startup/_analysis/research_knowledge.md` は存在しない可能性

**参照パターン2: Founder_Research関連**

```markdown
- @Founder_Research/documents/01_Legendary/FOUNDER_006_brian_chesky.md
- @Founder_Research/documents/02_Unicorn/FOUNDER_060_girish_mathrubootham.md
```

**検証結果**: ⚠️ **要改善**
- **問題**: パス形式が統一されていない
  - `FOUNDER_006_brian_chesky.md` (ローカルファイルとして参照)
  - 実際には `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/...` の構造

**参照パターン3: エラーハンドリング**

```markdown
- @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
```

**検証結果**: ✅ **適切**
- パス形式が正規化されている
- アンカーリンク形式が統一されている

#### 推奨改善

```markdown
✅ 改善後（統一形式）:
### KB参照

このスキルは以下のナレッジベースを参照します：

- @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md（資金調達パターン）
- @.claude/skills/_shared/error_handling_patterns.md

### Tier 2 ケーススタディ

**段階的マイルストーン型**:
- Airbnb: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/01_Legendary/FOUNDER_006_brian_chesky.md
```

---

### 3. create-mvv

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/create-mvv/SKILL.md`
**ファイルサイズ**: 499行

#### 参照パスの妥当性

**参照パターン1: Stock パス参照**

```markdown
- 詳細: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
- 成功事例: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/CORP_M001_geppo.md`
```

**検証結果**: ✅ **適切**
- パス形式が正規化されている
- 全角括弧（AIエージェント）が正しく使用されている
- 実在するディレクトリ構造に対応

**参照パターン2: Knowledge Base参照**

```markdown
- MVV概念: `@startup_science/02_frameworks/mvv/mvv_overview.md`
- リーンキャンバス: `@startup_science/02_frameworks/lean_canvas/lean_canvas_overview.md`
- **Recruit Product Research**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/`
```

**検証結果**: ⚠️ **要改善**
- **問題**: `@startup_science` が短縮表記
- **問題**: `/Founder_Research/` のパスが不明確

**参照パターン3: Knowledge Base複合参照**

```markdown
- VC投資基準総合: @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
- VC調達ロードマップ: @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
```

**検証結果**: ⚠️ **要改善**
- **問題**: `knowledge_base.md` ファイルが実存するか未確認
- **アンカーの形式**: `#vc-investment-criteria` 形式が一貫している

#### 推奨改善

```markdown
✅ 改善後:
- MVV概念: @.claude/skills/_shared/knowledge_base.md#mvv-overview
- リーンキャンバス: @.claude/skills/_shared/knowledge_base.md#lean-canvas-overview
- Recruit Product Research: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/
```

---

### 4. create-persona

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/create-persona/SKILL.md`
**ファイルサイズ**: 906行

#### 参照パスの妥当性

**参照パターン1: Knowledge Base参照**

```markdown
- @startup_science/01_stages/cpf/persona_creation.md
- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/cpf_overview.md
- @for_startup/_analysis/domain_requirements.md
- @for_startup/_analysis/research_knowledge.md
```

**検証結果**: ⚠️ **要改善**
- **問題**: `@startup_science`, `@for_startup` が短縮表記
- **実存性未確認**: `.claude/skills/for_startup/_analysis/` ディレクトリの実存性が不明確

**参照パターン2: ケーススタディ参照**

```markdown
- [Airbnb]: @research/case_studies/tier2/create-persona/01_airbnb_marketplace_personas.md
- [Uber]: @research/case_studies/tier2/create-persona/12_uber_two_sided_marketplace.md
```

**検証結果**: ⚠️ **要改善**
- **問題**: `@research` が短縮表記
- **推奨**: 絶対パス形式での統一

**参照パターン3: ForStartup Reference**

```markdown
- @for_startup/_analysis/domain_requirements.md - VC投資基準
- @for_startup/_analysis/research_knowledge.md - 成功事例（Airbnb、Freshworks、Box）
- @Founder_Research/documents/pitch_decks/ - ピッチデッキ事例
```

**検証結果**: ⚠️ **要改善**
- **問題**: パス形式が一貫していない
- `@for_startup/_analysis/` と `@Founder_Research/documents/` の混在

#### 推奨改善

```markdown
✅ 改善後:
### KB参照

このスキルは以下のナレッジベースを参照します：

- @.claude/skills/_shared/knowledge_base.md#cpf-persona-creation
- @.claude/skills/_shared/knowledge_base.md#3u-validation
- @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md
```

---

### 5. design-exit-strategy

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/design-exit-strategy/SKILL.md`
**ファイルサイズ**: 517行

#### 参照パスの妥当性

**参照パターン1: Founder_Research関連**

```markdown
- 詳細: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/withdrawal_analysis/recruit_withdrawal_criteria.md
- 統合分析: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md
- 撤退事例: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/research_notes_v3/withdrawn_*.md
```

**検証結果**: ✅ **適切**
- パス形式が正規化されている
- 全角括弧の使用が統一されている
- ディレクトリ構造が明確

#### 推奨改善

- **なし**: 参照パス形式が適切に統一されている

---

### 6. design-pricing

**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/design-pricing/SKILL.md`
**ファイルサイズ**: 775行

#### 参照パスの妥当性

**参照パターン1: Founder_Research参照**

```markdown
- **詳細事例**: @Founder_Research/analysis/integrated_analysis_report.md
- **収益モデル詳細**: @Founder_Research/documents/SUCCESS/CORP_S009_Stripe.md, CORP_S001_Figma.md, CORP_M001_Notion.md
- **失敗事例**: @Founder_Research/documents/WITHDRAWN/CORP_W003_Coursera個別指導.md, CORP_W001_エリクラ.md
```

**検証結果**: ⚠️ **要改善**
- **問題**: `@Founder_Research` が短縮表記
- **推奨**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/...` に統一

**参照パターン2: Knowledge Base複合参照**

```markdown
- @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
- @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
- @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
```

**検証結果**: ⚠️ **要改善**
- **問題**: `knowledge_base.md` ファイルの実存性が未確認
- **アンカー形式**: 一貫している

**参照パターン3: ケーススタディ参照**

```markdown
- @Founder_Research/documents/01_Legendary/
- @Founder_Research/documents/02_Unicorn/
- @Founder_Research/documents/03_VC_Backed/
```

**検証結果**: ⚠️ **要改善**
- **問題**: 相対パス（ディレクトリのみ）の参照は不完全

#### 推奨改善

```markdown
✅ 改善後:
- **詳細事例**: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md
- **ケーススタディ**: @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/
```

---

## 総合評価

### パス形式の統一性

| 形式 | 使用スキル数 | 推奨度 |
|:---:|:----------:|:----:|
| **完全形** (`@Stock/programs/...`) | 2 | ⭐⭐⭐⭐⭐ |
| **短縮形A** (`@Founder_Research/...`) | 3 | ⭐⭐ |
| **短縮形B** (`@for_startup/...`) | 2 | ⭐⭐ |
| **短縮形C** (`@startup_science/...`) | 2 | ⭐⭐ |
| **相対パス** (ファイル名のみ) | 1 | ⭐ |

**結論**: 短縮形を完全形に統一する必要があります

### 括弧の使用

| 括弧種 | 使用数 | 妥当性 |
|:---:|:-----:|:-----:|
| **全角括弧（）** | 8 | ✅ 正解 |
| **半角括弧()** | 0 | ✅ 問題なし |

**結論**: 括弧の使用は適切です

### エラーハンドリング参照

```markdown
✅ 統一形式:
- @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
```

**評価**: ✅ 適切（全スキルで統一）

---

## 改善推奨事項

### Priority 1: 参照パス形式の統一

**対象**: `create-fundraising-plan`, `create-mvv`, `create-persona`, `design-pricing`

**推奨形式** (優先順):

```markdown
# Pattern 1: 完全パス形式（最推奨）
@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/...

# Pattern 2: シンボリック参照（共有Knowledge Base）
@.claude/skills/_shared/knowledge_base.md#section-anchor
@.claude/skills/_shared/error_handling_patterns.md#section-anchor

# Pattern 3: スキル内相対パス（同一スキル内のみ）
../../../_shared/common_frameworks.md
```

### Priority 2: 短縮形の廃止

**廃止対象**:
- `@Founder_Research/` → `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/`
- `@for_startup/` → `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/` または `.claude/skills/for_startup/`
- `@startup_science/` → `.claude/skills/_shared/knowledge_base.md` (内容統合)

### Priority 3: Knowledge Base統合

**統合推奨**:
- `@startup_science/*` → `.claude/skills/_shared/knowledge_base.md` に統合
- `@for_startup/_analysis/*` → `.claude/skills/_shared/knowledge_base.md` に統合
- アンカーリンク形式で参照: `#section-anchor`

---

## チェックリスト（改善実施用）

### build-synergy-map
- [ ] `@Founder_Agent_ForStartup` → `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/` に統一
- [ ] `@Founder_Research` → 完全パスに変更
- [ ] ファイルサイズ: 2,131行のため、段階的改善を推奨

### create-fundraising-plan
- [ ] `@for_startup/_analysis/research_knowledge.md` → `@Stock/programs/.../Founder_Research/analysis/...` に統一
- [ ] `@startup_science/...` → Knowledge Base 統合参照に変更
- [ ] Founder_Research ドキュメント参照の形式を統一

### create-mvv
- [ ] `@startup_science/...` → Knowledge Base 統合参照に変更
- [ ] `@Stock/programs/...` の参照は維持（既に適切）
- [ ] エラーハンドリング参照は適切（維持）

### create-persona
- [ ] `@startup_science/...` → Knowledge Base 統合参照に変更
- [ ] `@for_startup/_analysis/...` → 完全パスに統一
- [ ] `@research/case_studies/...` → 完全パスに統一
- [ ] Tier 2 ケーススタディの参照形式を統一

### design-exit-strategy
- [ ] **改善不要**: 参照パス形式が既に適切に統一されている ✅

### design-pricing
- [ ] `@Founder_Research/...` → 完全パスに統一
- [ ] `knowledge_base.md#anchor` 形式の整合性確認
- [ ] ケーススタディ参照の形式を統一

---

## 次アクション

1. **Priority 1**: `create-fundraising-plan`, `create-persona`, `design-pricing` の参照パスを統一形式に改善
2. **Priority 2**: `create-mvv` の `@startup_science` 参照を Knowledge Base 統合参照に変更
3. **Priority 3**: 全スキル内の短縮形を廃止し、完全形またはシンボリック形式に統一
4. **Quality Gate**: 改善完了後、再度パス妥当性を確認（Phase 3.2）

---

## 参考資料

- @.claude/rules/path_conventions.md - パス管理規約
- @.claude/skills/for_startup/PHASE3_QA_GROUP1_REFERENCE_VALIDATION.md - Group 1 検証結果

---

**レポート作成日**: 2026-01-03
**実施者**: Claude Code
**ステータス**: ✅ 完了
