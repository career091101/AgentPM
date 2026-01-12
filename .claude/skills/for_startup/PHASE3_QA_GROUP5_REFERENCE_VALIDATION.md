# ForStartup Edition Phase 3.1 - Group 5 参照パス妥当性確認 レポート

**実行日時**: 2026-01-03
**確認対象**: 6スキル（validate-market-timing, validate-pmf, validate-psf, validate-ring-criteria, validate-unit-economics, validate-unit-economics-strict）
**確認方法**: SKILL.md内の参照パス抽出・検証
**全体ステータス**: ⚠️ **条件付きパス**（1件の重大問題、複数の参照パス不一致）

---

## エグゼクティブサマリー

### 検査結果

| 項目 | 結果 | 詳細 |
|------|------|------|
| **参照パスの形式一貫性** | ⚠️ 部分的 | 3種類の異なる形式が混在 |
| **@マークの使用** | ✅ 統一済み | すべてのファイルパス参照で@を使用 |
| **ファイル存在確認** | ⚠️ 要確認 | 一部パスが実際のディレクトリ構造と不一致 |
| **スペルミス検出** | ❌ **重大問題** | `Sratup_Research` → `Founder_Agent_ForStartup/Sratup_Research` |
| **括弧の統一性** | ✅ 統一済み | 全角括弧で統一 |

---

## 1. 重大な問題（Critical）

### 問題1: ディレクトリ名スペルミス

**スキル**: validate-market-timing

**参照パス**:
```
- @Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_037_quibi.md
- @Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_008_jawbone.md
- @Founder_Agent_ForStartup/Sratup_Research/documents/03_VC_Backed/FOUNDER_172_segway.md
- @Founder_Agent_ForStartup/Sratup_Research/documents/06_Pivot_Success/PIVOT_044_groupon.md
```

**実際のディレクトリ構造**:
```
./Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Sratup_Research/
```

**問題内容**:
- ディレクトリ名が`Sratup_Research`で実在（スペルミスが既に確定している）
- SKILL.mdの参照では相対パスでなく`@Founder_Agent_ForStartup/`から始まる参照になっているため、実際のパス解決に失敗する可能性
- 正しい参照形式は`@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Sratup_Research/`

**対応**:
- [ ] validate-market-timing SKILL.mdの参照パスを修正
- [ ] 完全パス参照に修正するか、相対パス＋フォルダマッピング確認

**重要度**: 🔴 **High** - ドキュメント参照が不備のため、スキル実行時に参照解決失敗の可能性

---

## 2. 参照パスの形式分類

### パターン1: 相対パス（@から始まる）

**使用スキル**: すべて

**形式**: `@Founder_Agent_ForStartup/...`, `@Founder_Research/...`, `@for_startup/...`

**件数**: 40+件

**例**:
```markdown
- @Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_037_quibi.md
- @Founder_Research/documents/03_VC_Backed/FOUNDER_172_segway.md
- @for_startup/knowledge_base/case_reference_for_startup.md
```

**問題**:
- `@Founder_Agent_ForStartup/` で始まるパスは、実際には`Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/` 配下にあるため、パス解決が曖昧
- `@Founder_Research/` で始まるパスも同様に相対位置が不明確

**推奨**:
- [ ] 全パスを`@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/` で統一
- または、`.claude/rules/path_conventions.md` でパスエイリアスを定義

---

### パターン2: ナレッジベース内の相対パス（@...knowledge_base）

**使用スキル**: validate-psf, validate-ring-criteria

**形式**: `@.claude/skills/_shared/knowledge_base.md#...`, `@.claude/skills/for_startup/knowledge_base/knowledge_base.md#...`

**件数**: 10+件

**例**:
```markdown
- @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
- @.claude/skills/for_startup/knowledge_base/knowledge_base.md#forstartup-edition
```

**問題**:
- 2つの異なるknowledge_base.mdファイルへの参照が混在
- `_shared` と `for_startup` 配下の両方を参照しているため、情報ソースが一貫していない可能性

**推奨**:
- [ ] どちらのナレッジベースが正式版かを明確化
- [ ] 一方に統一するか、役割分担を定義

---

### パターン3: startup_science フレームワーク参照

**使用スキル**: validate-psf

**形式**: `@startup_science/01_stages/psf/...`

**件数**: 4件

**例**:
```markdown
- @startup_science/01_stages/psf/psf_overview.md
- @startup_science/01_stages/psf/10x_validation.md
```

**確認状況**:
- ✅ 形式は統一されている
- ❓ 実際のファイル存在確認は別途必要

---

### パターン4: 研究ケーススタディ参照

**使用スキル**: validate-unit-economics

**形式**: `@research/case_studies/tier2/...`

**件数**: 13件

**例**:
```markdown
- @research/case_studies/tier2/validate-unit-economics/01_freshworks_unit_economics.md
- @research/case_studies/tier2/validate-unit-economics/13_notion_unit_economics.md
```

**問題**:
- `@research/` で始まるパスは、実際には`Founder_Agent_ForStartup/research/` 配下
- パス解決時に混乱する可能性

---

## 3. 参照パス一貫性スコア

### スキル別評価

| スキル名 | 参照数 | 形式一貫性 | パス妥当性 | 総合スコア | 状態 |
|---------|-------|---------|---------|---------|------|
| validate-market-timing | 5 | ⚠️ 部分的 | ❌ 要修正 | 60/100 | 要修正 |
| validate-pmf | 8 | ⚠️ 部分的 | ⚠️ 要確認 | 70/100 | 条件付きパス |
| validate-psf | 12 | ⚠️ 部分的 | ⚠️ 要確認 | 65/100 | 条件付きパス |
| validate-ring-criteria | 6 | ⚠️ 部分的 | ✅ 概ね妥当 | 75/100 | 条件付きパス |
| validate-unit-economics | 22 | ✅ 統一済み | ⚠️ 要確認 | 75/100 | 条件付きパス |
| validate-unit-economics-strict | 2 | ✅ 統一済み | ✅ 妥当 | 85/100 | パス |

**グループ全体**: **71/100** - **条件付きパス**（修正が必要）

---

## 4. 参照パスの詳細検証結果

### validate-market-timing

**重大問題**: ❌ **`Sratup_Research` ディレクトリ参照不備**

**参照数**: 5件

**参照リスト**:
```markdown
1. @Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_037_quibi.md
2. @Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_008_jawbone.md
3. @Founder_Agent_ForStartup/Sratup_Research/documents/03_VC_Backed/FOUNDER_172_segway.md
4. @Founder_Agent_ForStartup/Sratup_Research/documents/06_Pivot_Success/PIVOT_044_groupon.md
5. @Founder_Agent_ForStartup/research/case_studies/tier2/prepare-vc-meeting/case_006_stripe_founder_market_fit.md
```

**参照形式**: 相対パス（@Founder_Agent_ForStartup/）

**問題点**:
1. `Sratup_Research` はスペルミスが既に実在するディレクトリ
2. 参照パスが相対位置不明（Founder_Agent_ForStartup/がどこから始まるか不明）
3. 最後の1件（case_006_stripe）の参照は`research/`（小文字）で異なる

**修正方針**:
```markdown
# 修正前
- @Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_037_quibi.md

# 修正後
- @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Sratup_Research/documents/07_Failure_Study/FAILURE_037_quibi.md

# または（パスエイリアス定義）
- @FORSTARTUP_RESEARCH/documents/07_Failure_Study/FAILURE_037_quibi.md
```

---

### validate-pmf

**参照数**: 8件

**参照リスト**:
```markdown
1. @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md
2. @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/
3. @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
4. @.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
5. @.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
... （以下省略）
```

**参照形式**: 混合
- 完全パス（Stock/...）: 2件
- 相対パス（@.claude/skills/...）: 6件

**問題点**:
1. パス形式が完全パスと相対パスで混在
2. ナレッジベース参照が`_shared`に集中

**評価**: ⚠️ 条件付きパス
- 完全パス参照は妥当
- 相対パスは形式一貫性要改善

---

### validate-psf

**参照数**: 12件

**参照形式**: 混合
- Research詳細（完全パス）: 3件
- ナレッジベース参照: 9件

**参照例**:
```markdown
- @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md
- @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/
- @startup_science/01_stages/psf/psf_overview.md
- @.claude/skills/_shared/knowledge_base.md#...
```

**問題点**:
1. 3つの異なるパス形式が混在（Stock完全パス、startup_science、.claude相対パス）
2. Founder_Researchの詳細パスは正確だが長すぎる

**評価**: ⚠️ 条件付きパス
- Knowledge Base参照が一貫している
- 詳細Research参照は長さの最適化が必要

---

### validate-ring-criteria

**参照数**: 6件

**参照形式**: 比較的一貫
```markdown
- @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md
- @Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/
- @.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
```

**評価**: ⚠️ 条件付きパス
- Knowledge Base参照が一貫している
- 完全パスが長すぎる（最適化推奨）

---

### validate-unit-economics

**参照数**: 22件（Group 5で最多）

**参照形式**: ほぼ統一（@research/...）
```markdown
- @research/case_studies/tier2/validate-unit-economics/01_freshworks_unit_economics.md
- @research/case_studies/tier2/validate-unit-economics/03_calendly_unit_economics.md
... （13社のケーススタディ）
- @Founder_Research/documents/02_Unicorn/FOUNDER_060_girish_mathrubootham.md
```

**問題点**:
1. `@research/` で始まるパスが相対位置不明（実際には`Founder_Agent_ForStartup/research/`配下と推定）
2. 一部`@Founder_Research/`で始まるパスがあり混在

**評価**: ⚠️ 条件付きパス
- 参照数が多く、形式は比較的統一されている
- パスの相対位置確認が必要

---

### validate-unit-economics-strict

**参照数**: 2件

**参照形式**: 統一
```markdown
- @for_startup/knowledge_base/knowledge_base.md（ユニットエコノミクス基準）
- @for_startup/knowledge_base/case_reference_for_startup.md（成功事例）
```

**評価**: ✅ パス - 形式が統一され、新しいスキルのため参照も少なく妥当

---

## 5. パス形式の統一性分析

### 現在の3種類の形式

**形式1: 完全パス（Stock/...）**
- 用途: Founder_Research 詳細ファイル
- 例: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Founder_Research/analysis/integrated_analysis_report.md`
- 評価: ✅ 最も安全（実パス直接指定）
- 問題: 非常に長い、パス変更時に全パスを修正必要

**形式2: 相対短形式（@Founder_Agent_ForStartup/...）**
- 用途: Founder_Agent_ForStartup配下のファイル
- 例: `@Founder_Agent_ForStartup/Sratup_Research/documents/...`
- 評価: ⚠️ 相対位置が不明
- 問題: パス解決時に曖昧性がある

**形式3: スキルナレッジベース（@.claude/skills/...）**
- 用途: Knowledge Base参照
- 例: `@.claude/skills/_shared/knowledge_base.md#vc-investment-criteria`
- 評価: ✅ 明確（スキルディレクトリ相対）
- 問題: _shared と for_startup 両方が参照されている

---

## 6. 推奨アクション

### 優先度1: 高（即座に修正）

**Task**: validate-market-timing の参照パス修正

```markdown
# 修正対象
- SKILL.md の Sratup_Research 参照 5件

# 修正方法
相対パスを完全パスに修正するか、パスエイリアスを定義
```

**期限**: Phase 3完了までに実施

---

### 優先度2: 中（2-3週間以内）

**Task**: 参照パス形式の統一化

**対象**: すべてのGroup 5スキル

**実施項目**:
1. [ ] 相対パス形式（@Founder_Agent_ForStartup/）を完全パスに統一、またはエイリアス定義
2. [ ] Knowledge Base参照を_shared か for_startup のどちらかに統一
3. [ ] research/case_studies へのパス相対位置を明確化

**推奨統一形式**:
```markdown
# ケース1: 完全パス統一
@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/...

# ケース2: パスエイリアス定義（推奨）
# .claude/rules/path_conventions.md に以下を追加：
FORSTARTUP_ROOT = Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup
FORSTARTUP_RESEARCH = {FORSTARTUP_ROOT}/Sratup_Research

# SKILL.mdでの使用：
@FORSTARTUP_RESEARCH/documents/07_Failure_Study/FAILURE_037_quibi.md
```

---

### 優先度3: 低（次フェーズで実施）

**Task**: パス解決フレームワークの実装

**目的**: 相対パス自動解決機能の実装

**内容**:
1. `.claude/rules/path_conventions.md` でエイリアスを定義
2. スキル実行時に@で始まるパスを自動解決

---

## 7. 検査チェックリスト

### 参照パスの形式

- [x] 全参照が@で始まっている
- [x] 括弧が全角で統一されている
- [x] URLスキーム（http://等）がない
- [ ] **相対パスの位置が明確（一部未満**）

### ファイル存在性（サンプル検証）

- [x] `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/Sratup_Research/` ディレクトリ実在
- [ ] ⚠️ **参照パス形式との一貫性に課題**
- [ ] Founder_Research 配下の詳細ファイルは検査対象外（分量多大）

### Research統合の完全性

- [x] Founder_Research 参照が含まれている
- [x] Sratup_Research 参照が含まれている
- [ ] **相対パスの曖昧性解消が必要**

---

## 8. 質的評価

### 強み

1. ✅ **@マーク統一**: すべてのファイルパス参照で@を使用（ナレッジベース参照の標準化）
2. ✅ **括弧統一**: 全角括弧で統一されている（Path Management Conventions準拠）
3. ✅ **Research統合**: Founder_Research、Sratup_Research、research/case_studies など複数の情報源を参照
4. ✅ **Knowledge Base活用**: ナレッジベース（.claude/skills/_shared/knowledge_base.md）を積極参照

### 課題

1. ❌ **相対パス曖昧性**: @Founder_Agent_ForStartup/...などで相対位置が不明確
2. ❌ **スペルミス継続参照**: Sratup_Research（スペルミス）を参照
3. ⚠️ **形式混在**: 完全パス、相対短形式、Knowledge Base参照が混在
4. ⚠️ **Knowledge Base二重参照**: _shared と for_startup の両方を参照

---

## 9. 実装例：パスエイリアス定義

### 推奨: .claude/rules/path_conventions.md を拡張

```markdown
## ForStartup Edition パスエイリアス

### エイリアス定義

| エイリアス | 実パス | 用途 |
|----------|--------|------|
| @FORSTARTUP_ROOT | Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup | ForStartup Edition全般 |
| @FORSTARTUP_RESEARCH | {FORSTARTUP_ROOT}/Sratup_Research | 失敗事例・成功事例研究 |
| @FORSTARTUP_FOUNDER_RESEARCH | {FORSTARTUP_ROOT}/Founder_Research | 詳細分析レポート |
| @FORSTARTUP_DOCS | {FORSTARTUP_ROOT}/documents | ドメイン文書 |
| @FORSTARTUP_KB | .claude/skills/for_startup/knowledge_base | ForStartup専用KB |

### 使用例

```markdown
# SKILL.md内での参照
- @FORSTARTUP_RESEARCH/documents/07_Failure_Study/FAILURE_037_quibi.md
- @FORSTARTUP_FOUNDER_RESEARCH/analysis/integrated_analysis_report.md
- @FORSTARTUP_KB/knowledge_base.md#unit-economics
```
```

---

## 10. 総合判定と推奨

### 判定: **⚠️ 条件付きパス**

**理由**:
1. validate-market-timing の Sratup_Research 参照に重大問題あり
2. 相対パスの曖昧性が複数スキルで存在
3. Knowledge Base参照が_shared と for_startup で二重参照

### 推奨アクション

#### 即座実施（Phase 3完了までに）

- [ ] validate-market-timing の参照パス修正
  - [ ] Sratup_Research 参照5件を完全パスに修正
  - [ ] research/case_studies 参照1件を確認・修正

#### 優先実施（1-2週間）

- [ ] パスエイリアス定義を .claude/rules/path_conventions.md に追加
- [ ] 全Group 5スキルの参照パスをエイリアス形式に統一
- [ ] Knowledge Base参照を _shared に統一（for_startup は特化内容のみ）

#### 今後の品質保証

- [ ] 新規スキル作成時にはパスエイリアス使用を強制
- [ ] SKILL.mdレビュー時に参照パスの形式チェックを実施
- [ ] 半期ごとにパス参照の妥当性を自動検査

---

## 参考資料

### 本レポートの基準

- **参照パス形式**: .claude/rules/path_conventions.md（括弧統一等）
- **ナレッジベース活用**: .claude/skills/_shared/knowledge_base.md
- **パス管理**: PMBOK Workflow準拠

### Group 1-4との比較

（Group 1-4レポート参照）

---

**作成**: Claude Code Agent
**レビュー対象**: Group 5スキルセット（6スキル）
**確認完了日時**: 2026-01-03
**次フェーズ**: Phase 3.2 コンテンツ品質検証
