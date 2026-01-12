---
name: validate-solo-fit
description: |
  1人で実行可能かを多角的に検証する、ForSolo Edition専用スキル。

  **ソロプレナー最適化**：
  - 実行可能性スコア: **6点以上**（ForStartupの4点から強化）
  - 必須スキルチェック: コーディング、マーケティング、CS
  - 時間確保計画: 週20-40時間
  - コスト制約: 月額$100以下

  使用タイミング：
  - アイデア検証フェーズ（CPF検証前）
  - 1人実行可能性を判断したい
  - スキル不足領域を特定したい

  所要時間：10-15分（自動実行）
  出力：solo_fit_validation.md
---

# Validate Solo Fit Skill (ForSolo Edition)

1人で実行可能かを多角的に検証し、ソロプレナーとしての適合性を判定する自律実行型Skill。

---

## このSkillでできること

1. **成果物統合**: persona.md, lean_canvas.md, founder_skills.md を読み込み
2. **6軸評価**: 実行可能性、スキル充足度、時間確保、コスト制約等
3. **必須スキルチェック**: コーディング、マーケティング、CSの3スキル評価
4. **時間配分モデル**: 開発50%、マーケ30%、CS20%の実現可能性検証
5. **Researchナレッジ統合**: Marc Lou, Tony Dinh等25件の1人実行パターン
6. **総合判定**: Solo Fit達成/要改善/見直しの判断
7. **次ステップ提案**: スキル補強策、外注可能性、リソース確保策を提示

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `persona.md`, `lean_canvas.md`, `founder_skills.md` |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/2_discovery/solo_fit_validation.md` |
| **次のSkill** | `/validate-cpf`（Solo Fit達成時） |
| **ステージ** | Solo Fit検証（ソロプレナー適合性） |

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @for_solo/_shared/evaluation_criteria.md（ForSolo評価基準）
- @Solopreneur_Research/documents/01_App/case_studies/004_marc_lou.md
- @Solopreneur_Research/documents/01_App/case_studies/018_tony_dinh.md
- @Solopreneur_Research/documents/01_App/case_studies/003_pieter_levels.md

---

## Solo Fit達成基準（ForSolo版）

| 指標 | 目標値 | 測定方法 | ForStartup基準からの変更 |
|------|--------|----------|------------------------|
| **実行可能性スコア** | **6点以上** | 6軸総合評価 | 4点 → **6点**（最重要） |
| **必須スキル充足度** | **70%以上** | 3スキル×各10点評価 | **新規追加** |
| **時間確保可能性** | **週20時間以上** | 稼働計画チェック | **新規追加** |
| **コスト制約** | **月額$100以下** | ツールスタック試算 | **新規追加** |

---

## 6軸実行可能性評価（ForSolo版）

| 軸 | 評価基準 | 配点 | 判定閾値 |
|------|---------|------|---------|
| **1. 技術実行可能性** | フルスタック開発orNo-Code活用で実装可能か | 10点 | 8点以上 |
| **2. スキル充足度** | 必須3スキル（コーディング、マーケ、CS）の習得度 | 10点 | 7点以上 |
| **3. 時間確保可能性** | 週20-40時間を6ヶ月以上確保可能か | 10点 | 7点以上 |
| **4. コスト実現可能性** | 初期投資$1,000以下、月額$100以下で運用可能か | 10点 | 8点以上 |
| **5. マーケティング実行可能性** | SEO or Build in Publicを自力で実行可能か | 10点 | 6点以上 |
| **6. サポート実行可能性** | カスタマーサポートを週10時間以内で対応可能か | 10点 | 6点以上 |

**総合判定**:
- **45点以上**（75%以上）: ✅ Solo Fit達成（1人実行可能）
- **35-44点**（58-73%）: ⚠️ 要改善（一部外注検討）
- **34点以下**（56%以下）: ❌ 見直し（チーム組成orピボット）

---

## 必須スキルチェック（ForSolo新機能）

### 3つの必須スキル

| スキル | 評価項目 | 合格基準 |
|--------|---------|---------|
| **コーディング** | フルスタック開発 or No-Code活用 | 7点以上 |
| **マーケティング** | SEO、SNS、Build in Publicのいずれか | 6点以上 |
| **カスタマーサポート** | 問い合わせ対応、FAQ作成 | 5点以上 |

#### コーディングスキル詳細評価

| レベル | 説明 | 点数 | 判定 |
|--------|------|------|------|
| **フルスタック** | Next.js + Supabase等でMVP自力構築可能 | 10点 | ✅ 理想 |
| **フロント重視** | React/Vue得意、バックエンドはFirebase等で補完 | 8点 | ✅ 許容 |
| **No-Code熟練** | Bubble, Webflow等でMVP構築可能 | 7点 | ✅ 許容 |
| **No-Code初級** | Bubble等を学習中 | 5点 | ⚠️ 要学習 |
| **未経験** | コーディング未経験 | 0点 | ❌ 不可 |

#### マーケティングスキル詳細評価

| レベル | 説明 | 点数 | 判定 |
|--------|------|------|------|
| **SEO熟練** | ブログ50本以上執筆、Google上位表示実績 | 10点 | ✅ 理想 |
| **Build in Public実践** | X/Twitter 1K+ フォロワー、透明性投稿実績 | 9点 | ✅ 理想 |
| **SEO初級** | ブログ10本以上、基本的なSEO知識 | 7点 | ✅ 許容 |
| **SNS活用** | X/Twitter 500+ フォロワー、継続投稿 | 6点 | ✅ 許容 |
| **未経験** | マーケティング未経験 | 0点 | ❌ 不可 |

---

## 時間配分モデル（ForSolo推奨）

### 標準時間配分（週40時間の場合）

| 領域 | 時間 | 割合 | 主な作業 |
|------|------|------|---------|
| **開発** | 20時間 | 50% | MVP構築、機能追加、バグ修正 |
| **マーケティング** | 12時間 | 30% | SEO記事、X投稿、Product Hunt準備 |
| **カスタマーサポート** | 8時間 | 20% | 問い合わせ対応、FAQ更新、改善提案 |

### フェーズ別時間配分調整

| フェーズ | 開発 | マーケ | CS | 期間 |
|---------|------|--------|-----|------|
| **Phase 0: MVP構築** | 80% | 15% | 5% | 1-2ヶ月 |
| **Phase 1: ローンチ** | 40% | 50% | 10% | 3-6ヶ月 |
| **Phase 2: 成長** | 30% | 40% | 30% | 6-12ヶ月 |
| **Phase 3: スケール** | 20% | 30% | 50% | 12ヶ月以降 |

---

## Domain-Specific Knowledge (from Solopreneur Research)

### Success Patterns（1人実行パターン）

#### 高Solo Fitスコア（80点以上）

1. **[Marc Lou - ShipFast]** (Solo Fit 85/100): @Solopreneur_Research/documents/01_App/case_studies/004_marc_lou.md
   - **技術**: Next.js フルスタック（10点）
   - **マーケ**: Build in Public、X 20万フォロワー（10点）
   - **時間**: フルタイム転換（6ヶ月目、MRR $5K達成後）
   - **コスト**: 月額$50以下（Vercel無料枠活用）
   - **教訓**: 27個のプロダクト失敗を経て、Boilerplateビジネスモデル確立

2. **[Tony Dinh - TypingMind]** (Solo Fit 90/100): @Solopreneur_Research/documents/01_App/case_studies/018_tony_dinh.md
   - **技術**: フルスタック、数日でMVP構築（10点）
   - **マーケ**: Product Hunt #1複数回獲得（10点）
   - **時間**: サイドプロジェクトから3ヶ月でフルタイム転換
   - **コスト**: 初期投資ほぼゼロ
   - **教訓**: ChatGPT API公開直後の速攻リリースでファーストムーバー獲得

3. **[Pieter Levels - NomadList等]** (Solo Fit 95/100): @Solopreneur_Research/documents/01_App/case_studies/003_pieter_levels.md
   - **技術**: PHP/jQuery（レガシーでも問題なし、10点）
   - **マーケ**: SEO特化、"12 Startups in 12 Months"でバイラル（10点）
   - **時間**: 複数プロダクト並行運営（週60時間稼働）
   - **コスト**: 極限まで最小化（VPS $5/月等）
   - **教訓**: 70+個の失敗プロダクトを経て、95%失敗率でも成功

### Common Pitfalls（よくある失敗パターン）

1. **[技術過信型失敗]**: コーディングは得意だがマーケティング未経験
   - **リスク**: 素晴らしいプロダクトを作っても誰にも知られず終了
   - **対策**: MVP構築前にマーケティング戦略確立、Build in Public開始

2. **[完璧主義型失敗]**: 半年以上MVP構築に時間をかけすぎる
   - **リスク**: ローンチ前に資金・モチベーション枯渇
   - **対策**: 1週間MVP（Marc Lou流）、Boilerplate活用で時間短縮

3. **[スキル不足放置型失敗]**: 必須スキルが欠けているのに外注もしない
   - **リスク**: 品質低下、顧客不満、継続困難
   - **対策**: Fiverr等で$50-100の外注活用（ロゴ、LP等）

### Quantitative Benchmarks（定量ベンチマーク）

| 指標 | ForSolo基準 | 出典 |
|------|-----------|------|
| 実行可能性スコア | **6点以上** | @Solopreneur_Research 187件分析 |
| 必須スキル充足度 | **70%以上** | Marc Lou, Tony Dinh等25件 |
| 開発期間（MVP） | **1-4週間** | Marc Lou 1週間、Tony Dinh数日 |
| 月額ツールコスト | **$100以下** | 85%の事例が達成 |
| 初期投資額 | **$1,000以下** | 90%の事例が達成 |

### Best Practices（ベストプラクティス）

1. **Boilerplate活用**: ShipFast等で開発期間1週間に短縮
2. **Build in Public開始**: MVP構築前からX/Twitterで透明性投稿
3. **無料枠最大活用**: Vercel, Supabase, Railway等の無料枠
4. **最小限外注**: ロゴ、LP等は$50-100でFiverr活用
5. **Product Hunt準備**: ローンチ1ヶ月前からコミュニティ参加

### Tier 2 ケーススタディ（研究ナレッジベース統合）

**目的**: Solo Fit判定の実践的ベンチマーク、必須スキルセットの定量基準

#### 技術実行可能性 × マーケ実行可能性 型

- **[Marc Lou - ShipFast]**: @knowledge_base/tier2_case_studies/validate-solo-fit/01_marc_lou_solo_execution.md
  - 技術10点（Next.js フルスタック）、マーケ10点（Build in Public）
  - Boilerplateビジネスモデル、1週間MVP、月額$50コスト

- **[Tony Dinh - TypingMind]**: @knowledge_base/tier2_case_studies/validate-solo-fit/02_tony_dinh_solo_execution.md
  - 技術10点（数日MVP構築）、マーケ10点（Product Hunt #1複数回）
  - ChatGPT API活用、初期投資ゼロ、3ヶ月でフルタイム転換

#### [その他23社の例を記載]

### Reference
- 詳細: @knowledge_base/tier2_case_studies/validate-solo-fit/
- Solopreneur Research: @Solopreneur_Research/documents/01_App/case_studies/

---

## 判定基準（ForSolo版）

### 個別指標判定

| 指標 | ✅ 達成 | ⚠️ 要改善 | ❌ 見直し |
|------|---------|----------|---------|
| **実行可能性スコア** | 45点以上 | 35-44点 | 34点以下 |
| **必須スキル充足度** | 21点以上（70%） | 15-20点（50-66%） | 14点以下 |
| **時間確保** | 週20時間以上 | 週10-19時間 | 週10時間未満 |
| **コスト制約** | 月額$100以下 | 月額$100-300 | 月額$300以上 |

### 総合判定

| 判定 | 条件 | 次のアクション |
|------|------|---------------|
| ✅ **Solo Fit達成** | 実行可能性45点以上 + スキル21点以上 | `/validate-cpf` で課題検証へ |
| ⚠️ **要改善** | 実行可能性35-44点 or スキル15-20点 | スキル補強策・外注可能性検討 |
| ❌ **見直し** | 実行可能性34点以下 or スキル14点以下 | チーム組成 or ピボット検討 |

---

## Instructions

### 自動実行フロー

**STEP 1**: 成果物読み込み
- `persona.md`（ターゲット顧客、市場規模）
- `lean_canvas.md`（ソリューション、MVP、コスト構造）
- `founder_skills.md`（スキルセット、経験、学習計画）

**STEP 2**: 6軸実行可能性評価
1. **技術実行可能性**: 技術スタック、MVP構築可能性
2. **スキル充足度**: 必須3スキル（コーディング、マーケ、CS）
3. **時間確保可能性**: 週次稼働時間、6ヶ月継続可能性
4. **コスト実現可能性**: 初期投資、月次コスト試算
5. **マーケティング実行可能性**: SEO or Build in Public実行可能性
6. **サポート実行可能性**: CS対応時間、自動化可能性

**STEP 3**: 必須スキルチェック
- コーディング: 10点満点評価（フルスタック10点、No-Code 7点等）
- マーケティング: 10点満点評価（SEO熟練10点、SNS活用6点等）
- カスタマーサポート: 10点満点評価（自動化8点、手動対応5点等）

**STEP 4**: 時間配分シミュレーション
- 週次稼働時間 × 開発/マーケ/CS配分（50%/30%/20%）
- フェーズ別配分調整（MVP構築80%/15%/5% → 成長30%/40%/30%）

**STEP 5**: コスト試算
- 初期投資: ドメイン$10 + ホスティング$0-50 + Boilerplate $200等
- 月次コスト: Vercel無料枠、Supabase無料枠、合計$50-100

**STEP 6**: 総合判定
- 実行可能性スコア: 45点以上でSolo Fit達成
- 必須スキル充足度: 21点以上で許容
- 総合判定: 達成/要改善/見直し

**STEP 7**: 次ステップ提案
- ✅ Solo Fit達成: `/validate-cpf` で課題検証へ
- ⚠️ 要改善: スキル補強策（Udemy講座、外注活用等）提示
- ❌ 見直し: チーム組成 or ピボット検討

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：
- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#pattern-1
- **データ不足**: @.claude/skills/_shared/error_handling_patterns.md#pattern-2
- **判定不能**: @.claude/skills/_shared/error_handling_patterns.md#pattern-3

---

## 更新履歴

- 2026-01-02: ForSolo版初版作成（Solopreneur_Research 25件統合）
