# ForStartup Edition - Phase 3.2 実行計画

**策定日**: 2026-01-03
**Phase**: Phase 3.2（Research深化フェーズ）
**前提**: Phase 3.1完了（総合品質スコア95/100達成）

---

## Phase 3.2 概要

Phase 3.1で特定した問題を修正し、Tier 2ケーススタディをさらに深化させ、Tier 3統合を実施します。

---

## 実行タスク

### タスク1: P0推奨事項の実施（4件）

**優先度**: 🔴 最高
**推定時間**: 1時間

#### 修正対象

1. **measure-aarrr/SKILL.md** - 参照パス修正
   - 修正箇所: Line 943
   - 修正内容: `@startup_science/05_scale/aarrr_framework.md` → `@for_startup/_analysis/research_knowledge.md`

2. **orchestrate-review-loop/SKILL.md** - 参照パス修正
   - 修正箇所: Line 214
   - 修正内容: `@startup_science/01_frameworks/cpf_validation.md` → `@.claude/skills/_shared/knowledge_base.md`

3. **integrated_analysis_report.md参照削除** - 5スキルで参照削除
   - 対象スキル: analyze-aarrr、analyze-competitive-moat、build-approval-deck、build-flywheel、その他
   - 修正内容: Reference セクションから削除

4. **SUCCESS/WITHDRAWN参照変更** - 既存カテゴリ別フォルダへ変更
   - 対象スキル: build-approval-deck、その他
   - 修正内容: `SUCCESS/WITHDRAWN` → `01_Legendary/` または `03_VC_Backed/` 等の実在パスへ変更

**成果物**: P0修正完了レポート（PHASE3_2_P0_FIXES_REPORT.md）

---

### タスク2: P1問題の修正（参照パス形式統一）

**優先度**: 🟡 高
**推定時間**: 2時間

#### 修正対象

**Group 2全スキル**（6スキル）:
- build-synergy-map
- create-fundraising-plan
- create-mvv
- create-persona
- design-exit-strategy
- design-pricing

**修正内容**:
- 4つの異なる参照パス形式を統一
  - `@Founder_Research/...` ← **標準形式に統一**
  - `@for_startup/_analysis/...` → `@.claude/skills/for_startup/_analysis/...`
  - `@startup_science/...` → `@.claude/skills/for_startup/_analysis/research_knowledge.md`
  - `@Stock/programs/...`（完全形） → `@Founder_Research/...`（相対形式に変更）

**成果物**: P1修正完了レポート（PHASE3_2_P1_FIXES_REPORT.md）

---

### タスク3: Tier 3ケーススタディ追加統合（5スキル）

**優先度**: 🟢 中
**推定時間**: 3-4時間

#### 対象スキル（優先順位順）

1. **validate-pmf** - Tier 2: 4件 → Tier 3: +3件
   - 追加予定: Notion、Figma、Databricks
   - 焦点: Product-Market Fit達成プロセス、Sean Ellisテストの段階的向上

2. **validate-cpf** - Tier 2: 5件 → Tier 3: +3件
   - 追加予定: Canva、Ramp、Discord
   - 焦点: Customer-Problem Fit検証、課題共通率70%以上達成プロセス

3. **build-pitch-deck** - Tier 2: 3件 → Tier 3: +3件
   - 追加予定: 最新のPitch Deck成功事例（2024-2025年）
   - 焦点: 投資家説得力110点以上達成のベストプラクティス

4. **startup-scorecard** - Tier 2: 2件 → Tier 3: +3件
   - 追加予定: YC Top企業のScorecard評価事例
   - 焦点: 総合スコア40点以上/50点達成プロセス

5. **validate-market-timing** - Tier 2: 7件 → Tier 3: +3件
   - 追加予定: 2024-2025年の市場タイミング成功/失敗事例
   - 焦点: 5次元評価（技術成熟度、顧客準備度、競合状況、規制環境、市場成長率）

**実行方式**: 並列エージェント5グループ（各スキル1エージェント）

**成果物**:
- 各スキルのTier 3統合レポート（5件）
- Tier 3統合統括レポート（PHASE3_2_TIER3_INTEGRATION_CONSOLIDATED.md）

---

### タスク4: 失敗事例拡充（10件以上）

**優先度**: 🟢 中
**推定時間**: 2-3時間

#### 追加予定失敗事例

**リクルート系失敗事例**（5件）:
1. CODE.SCORE - 早期撤退（技術成熟度不足）
2. エリクラ - 市場タイミング誤り（ギグエコノミー未成熟）
3. リクルートDMPフォロー - 技術負債と市場変化
4. CAREER CARVER - 市場参入遅延（競合先行）
5. その他リクルート撤退事業

**VC調達型失敗事例**（5件以上）:
1. WeWork - 過大評価からの崩壊（評価額$47B → 倒産危機）
2. Theranos - 詐欺事例（技術的実現不可能性を隠蔽）
3. Quibi - 市場タイミング誤り（COVID-19との矛盾）
4. Jawbone - 早すぎる参入 + 品質問題
5. Segway - 早すぎる参入 + 規制未整備
6. その他VC調達型失敗事例

**統合対象スキル**:
- validate-cpf（失敗パターンの拡充）
- validate-pmf（失敗パターンの拡充）
- validate-market-timing（失敗パターンの拡充）
- startup-scorecard（失敗スコアの定量化）
- その他関連スキル

**成果物**: 失敗事例拡充レポート（PHASE3_2_FAILURE_CASE_EXPANSION_REPORT.md）

---

### タスク5: 2025-2026年最新事例追加（5件以上）

**優先度**: 🟢 低
**推定時間**: 1-2時間

#### 追加予定最新事例

**2025年事例**（3件以上）:
1. 2025年のProduct Hunt #1獲得事例（AI製品中心）
2. 2025年の大型資金調達事例（Series A/B/C）
3. 2025年のピボット成功事例

**2026年事例**（2件以上）:
1. 2026年の最新AI製品ローンチ事例
2. 2026年の市場タイミング成功事例

**統合対象スキル**:
- build-pitch-deck（最新Pitch Deck事例）
- validate-market-timing（最新タイミング事例）
- その他関連スキル

**成果物**: 最新事例追加レポート（PHASE3_2_LATEST_CASE_ADDITION_REPORT.md）

---

### タスク6: Research深化最終レポート作成

**優先度**: 🔴 最高（Phase 3.2完了条件）
**推定時間**: 1時間

**内容**:
- タスク1-5の結果統合
- Tier 3統合による改善効果の定量化
- 失敗事例拡充による教訓の体系化
- 最新事例追加によるトレンド分析
- Phase 3.3への移行条件確認

**成果物**: PHASE3_2_RESEARCH_DEEPENING_FINAL_REPORT.md

---

## 実行スケジュール

### Day 1（2026-01-03）

| 時間帯 | タスク | 推定時間 |
|-------|--------|---------|
| **14:00-15:00** | タスク1: P0推奨事項の実施 | 1時間 |
| **15:00-17:00** | タスク2: P1問題の修正 | 2時間 |
| **17:00-18:00** | 中間レビュー | 1時間 |

### Day 2（2026-01-04）

| 時間帯 | タスク | 推定時間 |
|-------|--------|---------|
| **09:00-13:00** | タスク3: Tier 3統合（並列実行） | 4時間 |
| **14:00-17:00** | タスク4: 失敗事例拡充 | 3時間 |
| **17:00-18:00** | タスク5: 最新事例追加 | 1時間 |

### Day 3（2026-01-05）

| 時間帯 | タスク | 推定時間 |
|-------|--------|---------|
| **09:00-10:00** | タスク6: 最終レポート作成 | 1時間 |
| **10:00-11:00** | Phase 3.2完了確認 | 1時間 |

**総推定時間**: 14時間

---

## Phase 3.2完了基準

### 必須項目チェックリスト

- [ ] P0推奨事項4件の実施完了
- [ ] P1問題（参照パス形式統一）の修正完了
- [ ] Tier 3ケーススタディ15件以上追加（5スキル × 3件）
- [ ] 失敗事例10件以上追加
- [ ] 最新事例5件以上追加
- [ ] Research深化最終レポート作成完了

### 品質基準

| 基準 | 目標 | 現状 |
|-----|:----:|:----:|
| **参照パス有効率** | 95%以上 | 75-80% |
| **参照パス形式統一度** | 90%以上 | 40% |
| **Tier 3統合スキル数** | 5スキル以上 | 0 |
| **失敗事例総数** | 30件以上 | 約20件 |
| **最新事例（2025-2026年）** | 5件以上 | 0 |
| **総合品質スコア** | 98点以上 | 95点 |

---

## リスク管理

### 想定リスク

| リスク | 影響度 | 対策 |
|-------|:-----:|------|
| **Tier 3統合の工数超過** | 高 | 優先スキル5件に限定、段階的実施 |
| **失敗事例の情報不足** | 中 | リクルート内部資料を優先活用 |
| **最新事例の入手困難** | 中 | WebSearchで2025-2026年の公開情報を収集 |
| **参照パス修正の影響範囲拡大** | 中 | 修正前にバックアップ作成、段階的修正 |

---

## 成果物一覧

### Phase 3.2成果物（予定7件）

1. PHASE3_2_EXECUTION_PLAN.md（本計画書）
2. PHASE3_2_P0_FIXES_REPORT.md（P0修正完了レポート）
3. PHASE3_2_P1_FIXES_REPORT.md（P1修正完了レポート）
4. PHASE3_2_TIER3_INTEGRATION_CONSOLIDATED.md（Tier 3統合統括レポート）
5. PHASE3_2_FAILURE_CASE_EXPANSION_REPORT.md（失敗事例拡充レポート）
6. PHASE3_2_LATEST_CASE_ADDITION_REPORT.md（最新事例追加レポート）
7. PHASE3_2_RESEARCH_DEEPENING_FINAL_REPORT.md（Research深化最終レポート）

### 追加成果物（スキル別レポート5件）

8-12. 各スキルのTier 3統合レポート（validate-pmf、validate-cpf、build-pitch-deck、startup-scorecard、validate-market-timing）

---

## Phase 3.3への移行条件

### 完了条件

- [ ] Phase 3.2全タスク完了
- [ ] 参照パス有効率95%以上達成
- [ ] 参照パス形式統一度90%以上達成
- [ ] Tier 3統合15件以上完了
- [ ] 総合品質スコア98点以上達成

### Phase 3.3移行判定

**判定基準**: 上記5項目すべてを達成した場合、Phase 3.3（クロスドメイン展開フェーズ）へ移行可

---

## 次のアクション

### 即座実行

1. タスク1: P0推奨事項の実施（4件）
   - measure-aarrr参照パス修正
   - orchestrate-review-loop参照パス修正
   - integrated_analysis_report.md参照削除
   - SUCCESS/WITHDRAWN参照変更

---

**Phase 3.2実行計画**: ✅ 策定完了
**次のステップ**: タスク1（P0推奨事項の実施）開始

---

**作成日**: 2026-01-03
**作成者**: Claude Sonnet 4.5
**ステータス**: ✅ Phase 3.2実行準備完了

---

**End of Phase 3.2 Execution Plan**
