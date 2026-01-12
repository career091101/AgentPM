---
name: analyze-aarrr
description: |
  AARRR（Acquisition/Activation/Retention/Referral/Revenue）フレームワークで成長ファネルを測定（ForRecruit特化版）。社内ベータテスト→外部展開の2段階Acquisition、社内KPI基準（Geppo回答率96%、Airレジ継続率等）を反映。リクルート製品研究31件の成功パターンを統合。

  ForRecruit調整:
  - Acquisition: 社内+外部顧客の2段階評価
  - Activation: 社内実績基準（Geppo 96%、Airレジ初回利用率80%）
  - Retention: 継続率98%目標（Geppo基準）
  - Revenue: 3年黒字計画必須
  - Referral: 社内NPS基準（60-80）

  使用タイミング：
  - Ring 3段階、外部顧客獲得後
  - 月次/週次の成長レビュー
  - Phase3（スケール）実行時

  所要時間：40-60分（社内外データ統合含む）
  出力：AARRR分析レポート（ForRecruit版）、改善施策優先順位リスト
trigger_keywords:
  - "AARRR"
  - "パイレーツメトリクス"
  - "成長ファネル"
  - "ファネル分析"
  - "グロースハック"
stage: Phase3（スケール）、Ring 3段階
dependencies:
  - validate-pmf（PMF達成が前提）
  - validate-ring-criteria（Ring 3承認可が前提）
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/aarrr_analysis_forrecruit.md
execution_time: 40-60分
framework_reference: Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
priority: P0
framework_compliance: 100%
---

# Analyze AARRR Skill (ForRecruit Edition)

AARRR（Pirate Metrics）5段階ファネルを測定し、成長ボトルネックを特定する自律実行型Skill（ForRecruit特化版）。リクルート製品研究31件から抽出した社内実績基準とベストプラクティスを統合。

---

## このSkillでできること

1. **5段階ファネル測定（社内外統合）**: Acquisition（社内+外部）→ Activation → Retention → Referral → Revenue の転換率を自動計測
2. **リクルート実績基準での評価**: Geppo、Airレジ、Airペイ等の成功製品KPIをベンチマーク化
3. **社内リソース活用パターン分析**: 営業網、既存顧客基盤、ブランド力の活用度評価
4. **改善施策の優先順位付け**: インパクトと実装難易度でQuick Winsを特定
5. **Ring 3基準準拠チェック**: 3年黒字・5年累損解消計画との整合性確認

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `pmf_diagnosis.md`, `ring_criteria_diagnosis.md`, アナリティクスデータ, 社内外顧客データ |
| **出力** | `Flow/{YYYYMM}/{YYYY-MM-DD}/aarrr_analysis_forrecruit.md` |
| **次のSkill** | `/build-approval-deck`（役員承認申請） or 個別改善施策の実行 |

---

## Domain-Specific Knowledge (from Recruit_Product_Research)

### Success Patterns

**1. Airレジ（AARRR成功事例）**
- **Acquisition**: 1年10万店舗、営業網2,000名活用でCAC 1-2万円（競合の1/5〜1/10）
- **Activation**: 初回利用率80%以上（推定）、オンボーディング1日以内（導入時間7倍短縮）
- **Retention**: 継続率60%以上（推定）、Churn率10-15%
- **Referral**: NPS 60-70（推定）
- **Revenue**: 3年黒字達成、Airペイクロスセル57%

**2. Airペイ（AARRR成功事例）**
- **Acquisition**: 1年20万店舗、Airレジクロスセル率57%（業界標準5-15%の4-11倍）
- **Activation**: 初回決済導入率80%以上（推定）
- **Retention**: 継続率60%以上（推定）、Churn率10%
- **Referral**: NPS 70-80（推定）、決済手数料最安で口コミ拡散
- **Revenue**: 初年度売上5億円、3年黒字達成

**3. Geppo（AARRR成功事例）**
- **Acquisition**: 2年300社（BtoB SaaS）、社内先行運用4年の実績を営業資料化
- **Activation**: 回答率96%（業界標準50-70%の1.4-1.9倍）、回答負荷10倍削減（30分→3分）
- **Retention**: 継続率98%（業界標準60-80%の1.2-1.6倍）
- **Referral**: NPS 70-80（推定）、人事部門評価、離職率改善効果実証
- **Revenue**: 3年黒字達成

**4. スタディサプリ（AARRR成功事例）**
- **Acquisition**: 初年度30万ユーザー、進学ブック100万人配布基盤活用
- **Activation**: 初回学習開始率70%以上（推定）
- **Retention**: 継続率50%以上（学習継続）、DAU/MAU 30-40%
- **Referral**: NPS 60-70（推定）、教育効果実証
- **Revenue**: 初年度から黒字、3年黒字達成

### Common Pitfalls

**失敗パターン1: 外部顧客獲得失敗（社内実証のみ）**
- **エリクラ**: 6年間実証実験レベル継続、外部ユーザー10万人（目標1,000万人未達）→ 撤退
- **DAU/MAU低迷**: 推定10%未満（競合タイミー30%以上）
- **教訓**: Ring 3では社内実証のみでは不可、1-2年でPMF判断、外部スケール必須

**失敗パターン2: 収益化失敗**
- **スタディサプリ個別指導**: 月額10,780円では講師人件費を賄えず、1.5年で撤退
- **Unit Economics不健全**: LTV/CAC比 1-2倍（赤字または微益）
- **教訓**: Unit Economics健全性（LTV/CAC 5.0以上）を厳守、収益性犠牲の成長は持続しない

**失敗パターン3: エンゲージメント低迷**
- **エリクラ**: DAU/MAU推定10-20%（競合タイミー30%以上）
- **教訓**: エンゲージメント低迷はPMF未達成の明確なサイン、ユーザー定着施策強化

### Quantitative Benchmarks

**Acquisition（獲得）**:
- 営業網活用: CAC 1-2万円（Airレジ、競合の1/5〜1/10）
- クロスセル率: 57%（Airレジ→Airペイ、業界標準5-15%の4-11倍）
- 社内先行運用: 4年（Geppo）、実績を営業資料化

**Activation（活性化）**:
- 回答率: 96%（Geppo、業界標準50-70%の1.4-1.9倍）
- 初回利用率: 80%以上（Airレジ、推定）
- 回答負荷: 10倍削減（Geppo、30分→3分）

**Retention（継続）**:
- 継続率: 98%（Geppo、業界標準60-80%の1.2-1.6倍）
- Churn率: 10-15%（Airレジ）、10%（Airペイ）、2%（Geppo）
- DAU/MAU比率: 30-40%（スタディサプリ）、40%以上（Airレジ推定）

**Referral（紹介）**:
- NPS: 60-70（Airレジ）、70-80（Airペイ、Geppo）、60-70（スタディサプリ）
- 口コミ拡散: 決済手数料最安（Airペイ）、人事部門評価（Geppo）

**Revenue（収益化）**:
- 初年度売上: 5億円（Airペイ）、3,000万円（Geppo推定）
- 3年黒字達成: Airレジ、Airペイ、スタディサプリ、Geppo
- Unit Economics: LTV/CAC 15-30倍（Airレジ）、10-15倍（Airペイ）、20倍（Geppo）

### Best Practices

1. **社内ベータテスト→外部展開の2段階Acquisition**:
   - Geppo: リクルート1,200名先行運用→外販300社（2年）
   - Airレジ: ホットペッパーグルメ既存顧客30社PoC→10万店舗（1年）
   - 効果: 社内実証データが営業資料になる、リスク低減

2. **営業網活用によるCAC削減**:
   - ホットペッパーグルメ2,000名→Airレジ・Airペイ直販
   - CAC 1-2万円（競合の1/5〜1/10）
   - 効果: 初速スケール、Airレジ1年10万店舗

3. **クロスセル戦略**:
   - Airレジ90.4万 → Airペイ51.5万、クロスセル率57%（業界標準5-15%の4-11倍）
   - 効果: CAC削減、LTV向上、エコシステム固定化

4. **エンゲージメント最大化**:
   - Geppo: 回答負荷10倍削減（30分→3分）→ 回答率96%、継続率98%
   - Airレジ: 導入時間7倍短縮（1週間→1日以内）→ 初回利用率80%以上

5. **Unit Economics健全性**:
   - LTV/CAC 10-30倍（Airレジ15-30倍、Airペイ10-15倍、Geppo 20倍）
   - Churn率10-15%以下（Geppo 2%）
   - 3年黒字・5年累損解消計画必須

### Reference

- 詳細: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/analysis/integrated_analysis_report.md`
- 個別事例: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/documents/SUCCESS/`

---

## Instructions

**実行モード**: 自律実行（ユーザー介入不要）
**推定所要時間**: 40-60分

### 自動実行ステップ

#### STEP 1: PMF・Ring 3判定確認

- PMF診断レポート（`pmf_diagnosis.md`）を読み込み
- Ring 3診断レポート（`ring_criteria_diagnosis.md`）を読み込み
- 以下の前提条件を確認:
  - [ ] PMF達成判定が「✅ PMF達成（Ring 3承認可）」
  - [ ] 外部顧客獲得100社/人以上
  - [ ] 収益化開始（初期売上発生）
  - [ ] 3年黒字・5年累損解消計画策定済み
- 未達成の場合は警告を表示し、処理を中断

#### STEP 2: AARRR 5段階の定義（ForRecruit版）

AARRRフレームワークの5段階をForRecruit基準で明確化:

| 段階 | 定義 | 主要KPI | ForRecruit調整 |
|-----|------|---------|---------------|
| **Acquisition（獲得）** | 訪問者・問い合わせ獲得 | 社内顧客数、外部顧客数、流入チャネル別内訳 | **社内+外部の2段階評価** |
| **Activation（活性化）** | 初回利用で価値実感 | 初回利用率、回答率（Geppo基準） | **社内実績基準（96%、80%）** |
| **Retention（継続）** | 継続的に利用 | 継続率、Churn Rate | **継続率98%目標（Geppo基準）** |
| **Referral（紹介）** | 他の人に紹介 | NPS、紹介率 | **社内NPS基準（60-80）** |
| **Revenue（収益）** | 収益を生む | ARPU、MRR、LTV/CAC | **3年黒字計画必須** |

#### STEP 3: リクルート実績ベンチマーク設定

Recruit_Product_Researchから抽出したベンチマークを設定:

**ForRecruit Benchmark（成功製品実績）**:

| 段階 | KPI | 目標値 | 出典 |
|-----|-----|-------|------|
| Acquisition | CAC | 1-2万円 | Airレジ（営業網活用、競合の1/5〜1/10） |
| Acquisition | クロスセル率 | 57% | Airレジ→Airペイ（業界標準5-15%の4-11倍） |
| Activation | 回答率 | 96% | Geppo（業界標準50-70%の1.4-1.9倍） |
| Activation | 初回利用率 | 80%+ | Airレジ（推定） |
| Retention | 継続率 | 98% | Geppo（業界標準60-80%の1.2-1.6倍） |
| Retention | Churn Rate | 2-15% | Geppo 2%、Airレジ10-15%、Airペイ10% |
| Retention | DAU/MAU | 30-40% | スタディサプリ30-40%、Airレジ40%+ |
| Referral | NPS | 60-80 | Airレジ60-70、Airペイ70-80、Geppo 70-80 |
| Revenue | 初年度売上 | 3,000万円〜5億円 | Geppo 3,000万円、Airペイ5億円 |
| Revenue | LTV/CAC比 | 10-30倍 | Airレジ15-30倍、Airペイ10-15倍、Geppo 20倍 |
| Revenue | 3年黒字達成 | 必須 | Airレジ、Airペイ、スタディサプリ、Geppo |

#### STEP 4: 実績データ入力ガイド（ForRecruit版）

ユーザーに以下のデータ入力を依頼（社内外データ統合）:

**Acquisition（獲得）**:
- **社内顧客数**: XXX社/人（リクルートグループ内）
- **外部顧客数**: XXX社/人（社外顧客のみ）
- **総顧客数**: XXX社/人（社内+外部）
- **主要獲得チャネル**:
  - 営業網（ホットペッパー、じゃらん等）: XX%
  - 既存顧客クロスセル: XX%
  - SEO・広告: XX%
  - リファラル: XX%
- **CAC（顧客獲得コスト）**: ¥XX,XXX/社

**Activation（活性化）**:
- **初回利用率**: XX%（サインアップ → 初回利用）
- **回答率/利用開始率**: XX%（Geppo基準96%、Airレジ基準80%）
- **Aha Moment達成数**: XXX社/人
- **Aha Moment達成率**: XX%
- **初回利用までの時間**: X日（Airレジ基準1日以内）

**Retention（継続）**:
- **MAU（月間アクティブユーザー）**: XXX社/人
- **DAU（日次アクティブユーザー）**: XXX社/人
- **DAU/MAU比率**: XX%（目標30-40%）
- **継続率（1ヶ月）**: XX%（目標98%、Geppo基準）
- **継続率（3ヶ月）**: XX%
- **継続率（6ヶ月）**: XX%
- **Churn Rate**: XX%/月（目標2-15%）

**Referral（紹介）**:
- **紹介経由の新規顧客数**: XXX社/人
- **紹介率**: XX%
- **NPS**: XX点（目標60-80、Promoters% - Detractors%）
- **口コミ/評価**: [定性的評価]

**Revenue（収益）**:
- **有料顧客数**: XXX社/人
- **課金転換率**: XX%
- **ARPU（月間平均顧客単価）**: ¥XXX
- **MRR（月次経常収益）**: ¥XXX,XXX
- **LTV（顧客生涯価値）**: ¥XXX,XXX
- **LTV/CAC比**: X.XX（目標10-30倍）
- **初年度売上**: ¥XXX,XXX,XXX（目標3,000万円〜5億円）
- **3年黒字計画**: [策定済み / 未策定]

**データソース例**:
- Google Analytics 4（訪問者、サインアップ）
- Mixpanel / Amplitude（ユーザー行動、継続率）
- 社内CRM（顧客管理、営業網経由獲得）
- 決済システム（Stripe, Paddle等）（収益）
- 社内アンケート（NPS）

#### STEP 5: ファネル分析（社内外統合）

各段階の転換率を計算（社内外データ統合）:

```
総顧客獲得（社内+外部）: A社/人
  ├ 社内顧客: A1社/人
  └ 外部顧客: A2社/人（Ring 3基準100社/人以上）
  ↓ 初回利用率: B%
初回利用: B社/人
  ↓ Aha Moment達成率: C%
活性化ユーザー: C社/人
  ↓ 継続率（1ヶ月）: D%
継続ユーザー: D社/人
  ↓ 課金転換率: E%
有料ユーザー: E社/人
  ↓ ARPU: ¥F
MRR: ¥G
```

**総合転換率**:
```
顧客獲得 → 収益転換率 = (E / A) × 100%
```

**ForRecruit特化指標**:
```
社内顧客比率 = (A1 / A) × 100%
外部顧客比率 = (A2 / A) × 100%
営業網経由獲得比率 = XX%
クロスセル経由獲得比率 = XX%
```

#### STEP 6: ボトルネック自動検出（ForRecruit基準）

各段階をForRecruit実績ベンチマークと比較:

**判定基準**:
- ✅ **良好**: ForRecruit Benchmark以上
- ⚠️ **ボトルネック**: Benchmark - 10%以内
- ❌ **重大ボトルネック**: Benchmark - 10%未満

**ForRecruit Benchmark比較**:

| 段階 | KPI | 実績値 | Benchmark | 差分 | 判定 |
|-----|-----|-------|-----------|------|:----:|
| Acquisition | CAC | ¥XX,XXX | ¥10,000-20,000 | +/-¥X,XXX | ✅/⚠️/❌ |
| Acquisition | クロスセル率 | XX% | 57% | +/-XX% | ✅/⚠️/❌ |
| Activation | 回答率/初回利用率 | XX% | 80-96% | +/-XX% | ✅/⚠️/❌ |
| Retention | 継続率（1ヶ月） | XX% | 98% | +/-XX% | ✅/⚠️/❌ |
| Retention | Churn Rate | XX%/月 | 2-15% | +/-XX% | ✅/⚠️/❌ |
| Referral | NPS | XX | 60-80 | +/-XX | ✅/⚠️/❌ |
| Revenue | LTV/CAC比 | X.XX | 10-30倍 | +/-X.XX | ✅/⚠️/❌ |
| Revenue | 3年黒字計画 | [策定済み / 未策定] | 策定済み | - | ✅/❌ |

**ボトルネック特定ロジック**:
1. 各段階の実績値をForRecruit Benchmarkと比較
2. 差分が最も大きい段階を「最優先ボトルネック」として特定
3. 差分の大きい順にランク付け

#### STEP 7: 社内リソース活用パターン分析

Recruit_Product_Researchの「資産活用と成功の相関分析」を参照:

| 資産活用数 | 該当製品数 | 平均PMFスコア | 成功率 | 代表製品 |
|----------|----------|------------|-------|---------|
| **3種以上** | 8 | **8.8** | **100%** | Airレジ、Airペイ、Geppo |
| **1-2種** | 15 | **7.5** | **80%** | SUUMO、じゃらん、スタディサプリ |
| **0種** | 8 | **5.2** | **25%** | CODE.SCORE、termhub |

**あなたのプロジェクトの資産活用状況**:

| 資産タイプ | 活用状況 | 活用度 | 具体例 |
|----------|---------|-------|--------|
| **営業網** | [活用 / 未活用] | XX% | ホットペッパー2,000名活用等 |
| **既存顧客基盤** | [活用 / 未活用] | XX% | クロスセル率XX% |
| **ブランド力** | [活用 / 未活用] | XX% | リクルートブランド信頼性 |
| **データ資産** | [活用 / 未活用] | XX% | 決済データ、顧客データ活用 |
| **プラットフォーム** | [活用 / 未活用] | XX% | Airシリーズ連携等 |
| **インフラ** | [活用 / 未活用] | XX% | リクルートクラウド基盤 |

**総合評価**:
- 資産活用数: X種
- 期待PMFスコア: X.X
- 期待成功率: XX%

**推奨アクション**:
- 資産活用が3種未満の場合: 追加活用施策を検討（成功率向上）

#### STEP 8: ボトルネック優先順位付け

**評価軸**:
1. **Impact（影響度）**: 改善時の全体への影響（1-10点）
   - ファネル上流ほど影響大（Acquisitionが最も影響大）
   - 計算式: `Impact = (後続ステップ数 + 1) × 転換率差分% × ForRecruit Benchmark達成度`

2. **Ease（実装容易性）**: 改善施策の実装難易度（1-10点）
   - 簡単: 社内リソース活用強化、営業網活用（8-10点）
   - 中程度: 機能追加、フロー変更（4-7点）
   - 困難: プロダクト再設計、技術的難題（1-3点）

**優先スコア**:
```
Priority Score = Impact × Ease
```

高スコア順に改善施策を並べる。

#### STEP 9: 改善施策提案（ForRecruit版）

各ボトルネック段階ごとに3-5個の改善施策を提案（ForRecruit Researchから抽出）:

**Acquisition改善施策例（ForRecruit版）**:
1. **営業網活用強化**: ホットペッパーグルメ2,000名、じゃらん営業網への展開
   - 期待効果: CAC 1-2万円（競合の1/5〜1/10）
   - 実装難易度: 中（営業網との連携調整必要）
   - 成功事例: Airレジ1年10万店舗、Airペイ1年20万店舗

2. **クロスセル強化**: 既存サービス（SUUMO、じゃらん、ホットペッパー等）からの誘導
   - 期待効果: クロスセル率57%（Airレジ→Airペイ実績）
   - 実装難易度: 中（連携機能開発必要）
   - 成功事例: Airレジ90.4万→Airペイ51.5万

3. **社内実証データの営業資料化**: 社内PoC結果を外部営業に活用
   - 期待効果: 信頼性向上、導入ハードル低下
   - 実装難易度: 低（既存データの整理のみ）
   - 成功事例: Geppo社内4年先行運用→300社獲得（2年）

4. **リクルートブランド活用**: 「リクルート発の新規事業」として露出
   - 期待効果: 初期信頼獲得、CAC削減
   - 実装難易度: 低（広報との連携）
   - 成功事例: 全リクルート製品

5. **既存メディア掲載**: ホットペッパー、じゃらん、SUUMOへの製品紹介
   - 期待効果: 大量リーチ、低コスト獲得
   - 実装難易度: 中（メディア編集部との調整）
   - 成功事例: リクルート各製品の初期獲得

**Activation改善施策例（ForRecruit版）**:
1. **回答負荷削減**: Geppo方式（30分→3分、10倍削減）の適用
   - 期待効果: 回答率・初回利用率96%
   - 実装難易度: 中（UI/UX改善）
   - 成功事例: Geppo回答率96%（業界標準50-70%の1.4-1.9倍）

2. **導入時間短縮**: Airレジ方式（1週間→1日以内、7倍短縮）の適用
   - 期待効果: 初回利用率80%以上
   - 実装難易度: 中（オンボーディングフロー改善）
   - 成功事例: Airレジ初回利用率80%以上（推定）

3. **社内ベータテスト強化**: Geppo方式（リクルート1,200名先行導入）
   - 期待効果: フィードバック収集、製品改善
   - 実装難易度: 低（社内リソース活用）
   - 成功事例: Geppo社内先行運用4年

**Retention改善施策例（ForRecruit版）**:
1. **継続率98%目標設定**: Geppo基準の適用
   - 期待効果: Churn率2%（業界トップクラス）
   - 実装難易度: 高（製品価値の継続的向上）
   - 成功事例: Geppo継続率98%（業界標準60-80%の1.2-1.6倍）

2. **エコシステム連携**: Airシリーズ方式（Airレジ・Airペイ・Airキャッシュ連携）
   - 期待効果: スイッチングコスト構築、Churn率低減
   - 実装難易度: 高（複数サービス連携）
   - 成功事例: Airシリーズ、リクルートID

3. **カスタマーサクセス体制**: BtoB製品の伴走支援
   - 期待効果: 継続率向上、解約防止
   - 実装難易度: 中（CS人員確保）
   - 成功事例: Geppo運用代行サービス

**Referral改善施策例（ForRecruit版）**:
1. **NPS 60-80目標設定**: ForRecruit成功製品基準
   - 期待効果: 口コミ拡散、自然流入増加
   - 実装難易度: 中（製品品質向上）
   - 成功事例: Airレジ60-70、Airペイ70-80、Geppo 70-80

2. **成果レポート共有機能**: 人事部門評価（Geppo方式）
   - 期待効果: 社内評価向上、紹介増加
   - 実装難易度: 低（レポート機能追加）
   - 成功事例: Geppo離職率改善効果実証

3. **リファラルプログラム**: 紹介者・被紹介者双方にインセンティブ
   - 期待効果: 紹介率向上
   - 実装難易度: 中（プログラム設計・運用）
   - 成功事例: 一般的グロースハック手法

**Revenue改善施策例（ForRecruit版）**:
1. **3年黒字・5年累損解消計画の厳守**: Ring 3基準
   - 期待効果: 投資判断の明確化
   - 実装難易度: 低（計画策定・進捗管理）
   - 成功事例: Airレジ、Airペイ、スタディサプリ、Geppo

2. **Unit Economics健全性確保**: LTV/CAC 10-30倍目標
   - 期待効果: 持続的成長、投資回収
   - 実装難易度: 中（CAC削減、LTV向上施策）
   - 成功事例: Airレジ15-30倍、Airペイ10-15倍、Geppo 20倍

3. **クロスセル・アップセル**: Airシリーズ方式（周辺サービス展開）
   - 期待効果: ARPU向上、LTV向上
   - 実装難易度: 高（追加サービス開発）
   - 成功事例: Airレジ→Airペイ、Airキャッシュ、Airカード

#### STEP 10: Quick Wins特定（ForRecruit版）

**Quick Wins条件**:
- Impact ≥ 7点
- Ease ≥ 7点
- Priority Score ≥ 49点
- **ForRecruit資産活用度が高い**（営業網、既存顧客基盤、ブランド力）

**ForRecruit Quick Wins優先例**:
1. **営業網活用強化**: Impact 9点、Ease 8点、Score 72点
2. **社内実証データの営業資料化**: Impact 7点、Ease 9点、Score 63点
3. **既存メディア掲載**: Impact 8点、Ease 7点、Score 56点
4. **リクルートブランド活用**: Impact 7点、Ease 9点、Score 63点

Quick Winsを最優先実装リストとして表示。

#### STEP 11: 実装ロードマップ作成（ForRecruit版）

**1ヶ月計画（短期）**:
- Week 1: Quick Wins施策1（営業網活用強化、既に接点ある営業チームとの連携）
- Week 2: Quick Wins施策2（社内実証データの営業資料化）
- Week 3: ボトルネック1の改善施策（中難易度、例: 回答負荷削減）
- Week 4: 効果測定・分析（KPI更新、次月計画策定）

**3ヶ月計画（中期）**:
- Month 1: Quick Wins + ボトルネック1（Activation強化）
- Month 2: ボトルネック2改善（Retention強化） + A/Bテスト
- Month 3: ボトルネック3改善（Revenue強化） + 総合評価

**Ring 3承認申請準備**:
- 3ヶ月後の目標: KPI改善、3年黒字計画の進捗確認
- 役員承認用資料作成: `/build-approval-deck`

#### STEP 12: 成果物出力

以下のMarkdown形式でレポートを生成:

---

## 成果物テンプレート

```markdown
# AARRR分析レポート（ForRecruit Edition）

**作成日**: {YYYY-MM-DD}
**分析対象期間**: {YYYY-MM-DD} ~ {YYYY-MM-DD}
**総合判定**: ✅ 良好（Ring 3基準達成） / ⚠️ 改善必要 / ❌ 要緊急対応
**Ring 3承認**: [承認可 / 要改善 / 承認不可]

---

## エグゼクティブサマリー

### ファネルサマリー（社内外統合）

| 指標 | 値 | ForRecruit Benchmark | 判定 |
|-----|------|---------------------|:----:|
| 総顧客数（社内+外部） | XXX社/人 | - | - |
| └ 社内顧客数 | XXX社/人 | - | - |
| └ **外部顧客数** | **XXX社/人** | **100社/人以上** | ✅/⚠️/❌ |
| 初回利用数 | XXX社/人 | - | - |
| 活性化ユーザー数 | XXX社/人 | - | - |
| 継続ユーザー数（1ヶ月） | XXX社/人 | - | - |
| 有料ユーザー数 | XXX社/人 | - | - |
| MRR | ¥XXX,XXX | - | - |
| **総合転換率（顧客→収益）** | **XX%** | - | - |

### 最優先ボトルネック

**🚨 {ステージ名}**: {理由}

- 実績値: XX%
- ForRecruit Benchmark: XX%
- 差分: -XX%
- 優先度: 🔴 高 / 🟡 中 / 🟢 低

**ForRecruit成功事例との比較**:
- Airレジ: [KPI] XX%
- Airペイ: [KPI] XX%
- Geppo: [KPI] XX%
- あなたのプロジェクト: [KPI] XX% → [評価]

---

## 5段階詳細分析（ForRecruit版）

### 1. Acquisition（獲得）

**KPI**:
- 総顧客数（社内+外部）: XXX社/人
- 社内顧客数: XXX社/人（XX%）
- **外部顧客数**: **XXX社/人**（XX%）**[Ring 3基準100社/人以上]**
- 前月比成長率: +XX%

**流入チャネル内訳**:
| チャネル | 顧客数 | 割合 |
|---------|-------|------|
| **営業網（ホットペッパー、じゃらん等）** | XXX | XX% |
| **既存顧客クロスセル** | XXX | XX% |
| SEO（自然検索） | XXX | XX% |
| SNS（ソーシャル） | XXX | XX% |
| 広告（有料） | XXX | XX% |
| ダイレクト | XXX | XX% |
| リファラル（紹介） | XXX | XX% |

**CAC（顧客獲得コスト）**:
- 実績値: ¥XX,XXX/社
- ForRecruit Benchmark: ¥10,000-20,000/社（Airレジ、営業網活用）
- 差分: +/-¥X,XXX
- 判定: ✅ 良好 / ⚠️ 改善必要 / ❌ 要改善

**ForRecruit Benchmark比較**:
| KPI | 実績値 | Benchmark | 差分 | 判定 |
|-----|-------|-----------|------|:----:|
| 外部顧客数 | XXX社/人 | 100社/人以上 | +/-XXX | ✅/⚠️/❌ |
| CAC | ¥XX,XXX | ¥10,000-20,000 | +/-¥X,XXX | ✅/⚠️/❌ |
| クロスセル率 | XX% | 57% | +/-XX% | ✅/⚠️/❌ |

**コメント**:
[顧客獲得のトレンド、営業網活用状況、クロスセル実績]

**ForRecruit成功事例**:
- Airレジ: 1年10万店舗、CAC 1-2万円（営業網2,000名活用）
- Airペイ: 1年20万店舗、Airレジクロスセル率57%
- あなたのプロジェクト: [比較コメント]

---

### 2. Activation（活性化）

**KPI**:
- 初回利用率: XX%
- 回答率/利用開始率: XX%
- Aha Moment達成率: XX%
- 初回利用までの時間: X日

**ForRecruit Benchmark比較**:
| KPI | 実績値 | Benchmark | 差分 | 判定 |
|-----|-------|-----------|------|:----:|
| 回答率/初回利用率 | XX% | 80-96% | +/-XX% | ✅/⚠️/❌ |
| Aha Moment達成率 | XX% | 40%+ | +/-XX% | ✅/⚠️/❌ |
| 初回利用までの時間 | X日 | 1日以内 | +/-X日 | ✅/⚠️/❌ |

**判定**: ✅ 良好 / ⚠️ ボトルネック / ❌ 重大ボトルネック

**コメント**:
[オンボーディングの状況、回答負荷、導入時間]

**ForRecruit成功事例**:
- Geppo: 回答率96%（業界標準50-70%の1.4-1.9倍）、回答負荷10倍削減（30分→3分）
- Airレジ: 初回利用率80%以上（推定）、導入時間7倍短縮（1週間→1日以内）
- あなたのプロジェクト: [比較コメント]

---

### 3. Retention（継続）

**KPI**:
- DAU/MAU比率: XX%
- 継続率（1ヶ月）: XX%
- 継続率（3ヶ月）: XX%
- 継続率（6ヶ月）: XX%
- Churn Rate: XX%/月

**ForRecruit Benchmark比較**:
| KPI | 実績値 | Benchmark | 差分 | 判定 |
|-----|-------|-----------|------|:----:|
| 継続率（1ヶ月） | XX% | 98% | +/-XX% | ✅/⚠️/❌ |
| Churn Rate | XX%/月 | 2-15% | +/-XX% | ✅/⚠️/❌ |
| DAU/MAU | XX% | 30-40% | +/-XX% | ✅/⚠️/❌ |

**判定**: ✅ 良好 / ⚠️ ボトルネック / ❌ 重大ボトルネック

**コメント**:
[継続率のトレンド、解約理由、エンゲージメント状況]

**ForRecruit成功事例**:
- Geppo: 継続率98%（業界標準60-80%の1.2-1.6倍）、Churn率2%
- Airレジ: 継続率60%以上（推定）、Churn率10-15%
- Airペイ: 継続率60%以上（推定）、Churn率10%
- あなたのプロジェクト: [比較コメント]

---

### 4. Referral（紹介）

**KPI**:
- 紹介率: XX%
- NPS: XX点
- 口コミ/評価: [定性的評価]

**ForRecruit Benchmark比較**:
| KPI | 実績値 | Benchmark | 差分 | 判定 |
|-----|-------|-----------|------|:----:|
| NPS | XX | 60-80 | +/-XX | ✅/⚠️/❌ |
| 紹介率 | XX% | 10-30% | +/-XX% | ✅/⚠️/❌ |

**判定**: ✅ 良好 / ⚠️ ボトルネック / ❌ 重大ボトルネック

**コメント**:
[紹介の仕組み、NPS結果の解釈、口コミ状況]

**ForRecruit成功事例**:
- Airレジ: NPS 60-70（推定）
- Airペイ: NPS 70-80（推定）、決済手数料最安で口コミ拡散
- Geppo: NPS 70-80（推定）、人事部門評価、離職率改善効果実証
- スタディサプリ: NPS 60-70（推定）、教育効果実証
- あなたのプロジェクト: [比較コメント]

---

### 5. Revenue（収益）

**KPI**:
- 課金転換率: XX%
- ARPU: ¥XXX
- MRR: ¥XXX,XXX
- LTV: ¥XXX,XXX
- LTV/CAC比率: X.XX
- 初年度売上: ¥XXX,XXX,XXX
- 3年黒字計画: [策定済み / 未策定]

**ForRecruit Benchmark比較**:
| KPI | 実績値 | Benchmark | 差分 | 判定 |
|-----|-------|-----------|------|:----:|
| 課金転換率 | XX% | 2-5% | +/-XX% | ✅/⚠️/❌ |
| LTV/CAC比率 | X.XX | 10-30倍 | +/-X.XX | ✅/⚠️/❌ |
| 初年度売上 | ¥XXX,XXX,XXX | ¥30,000,000-500,000,000 | +/-¥XXX,XXX,XXX | ✅/⚠️/❌ |
| 3年黒字計画 | [策定済み / 未策定] | 策定済み | - | ✅/❌ |

**判定**: ✅ 良好 / ⚠️ ボトルネック / ❌ 重大ボトルネック

**コメント**:
[収益化の状況、Unit Economics、3年黒字計画の進捗]

**ForRecruit成功事例**:
- Airレジ: LTV/CAC 15-30倍、3年黒字達成
- Airペイ: 初年度売上5億円、LTV/CAC 10-15倍、3年黒字達成
- Geppo: 初年度売上3,000万円（推定）、LTV/CAC 20倍、3年黒字達成
- あなたのプロジェクト: [比較コメント]

---

## 社内リソース活用パターン分析

### 資産活用状況

| 資産タイプ | 活用状況 | 活用度 | 具体例 |
|----------|---------|-------|--------|
| **営業網** | [活用 / 未活用] | XX% | [具体的な活用内容] |
| **既存顧客基盤** | [活用 / 未活用] | XX% | [クロスセル施策等] |
| **ブランド力** | [活用 / 未活用] | XX% | [リクルートブランド活用] |
| **データ資産** | [活用 / 未活用] | XX% | [決済データ、顧客データ活用] |
| **プラットフォーム** | [活用 / 未活用] | XX% | [Airシリーズ連携等] |
| **インフラ** | [活用 / 未活用] | XX% | [リクルートクラウド基盤] |

**総合評価**:
- 資産活用数: X種
- 期待PMFスコア: X.X（Recruit_Product_Research分析結果）
- 期待成功率: XX%

**ForRecruit Benchmark比較**:
| 資産活用数 | 期待PMFスコア | 期待成功率 | 代表製品 |
|----------|------------|----------|---------|
| **3種以上** | **8.8** | **100%** | Airレジ、Airペイ、Geppo |
| **1-2種** | **7.5** | **80%** | SUUMO、じゃらん、スタディサプリ |
| **0種** | **5.2** | **25%** | CODE.SCORE、termhub |
| **あなたのプロジェクト** | **X.X** | **XX%** | - |

**推奨アクション**:
- [資産活用が3種未満の場合の具体的施策]

---

## ボトルネック特定

### 優先順位付け（ForRecruit基準）

| ランク | ステージ | 問題点 | Impact | Ease | Priority Score | 判定 |
|:-----:|---------|--------|:------:|:----:|:--------------:|:----:|
| 1 | {ステージ} | {問題点} | XX | XX | XXX | 🔴 高 |
| 2 | {ステージ} | {問題点} | XX | XX | XXX | 🟡 中 |
| 3 | {ステージ} | {問題点} | XX | XX | XXX | 🟢 低 |

---

## 改善施策（優先順位順）

### Quick Wins（即実行推奨、ForRecruit資産活用型）

1. **{施策名}** - {ステージ}
   - **期待効果**: {転換率XX% → XX%、MRR +¥XXX,XXX}
   - **実装難易度**: 低（X週間）
   - **Impact**: XX/10
   - **Ease**: XX/10
   - **Priority Score**: XXX
   - **ForRecruit資産活用**: {営業網 / 既存顧客基盤 / ブランド力 等}
   - **具体的アクション**: {実装内容}
   - **成功事例**: {Airレジ / Airペイ / Geppo 等}

2. **{施策名}** - {ステージ}
   - （同上）

### 中期施策（1-3ヶ月）

3. **{施策名}** - {ステージ}
   - **期待効果**: {内容}
   - **実装難易度**: 中（XX週間）
   - **Impact**: XX/10
   - **Ease**: XX/10
   - **Priority Score**: XXX
   - **具体的アクション**: {実装内容}
   - **成功事例**: {Airレジ / Airペイ / Geppo 等}

### 長期施策（3ヶ月以上）

5. **{施策名}** - {ステージ}
   - **期待効果**: {内容}
   - **実装難易度**: 高（XX週間）
   - **Impact**: XX/10
   - **Ease**: XX/10
   - **Priority Score**: XXX
   - **具体的アクション**: {実装内容}

---

## 実装ロードマップ（ForRecruit版）

### 1ヶ月計画（短期）

| Week | 施策 | ステージ | 目標 | ForRecruit資産活用 |
|:----:|------|---------|------|--------------------|
| Week 1 | {Quick Wins施策1} | {ステージ} | {KPI目標} | {営業網 / 既存顧客基盤 等} |
| Week 2 | {Quick Wins施策2} | {ステージ} | {KPI目標} | {ブランド力 / データ資産 等} |
| Week 3 | {ボトルネック1改善} | {ステージ} | {KPI目標} | {プラットフォーム 等} |
| Week 4 | 効果測定・分析 | - | AARRRレポート更新 | - |

### 3ヶ月計画（中期）

| Month | 主要施策 | 目標KPI | Ring 3基準進捗 |
|:-----:|---------|---------|---------------|
| Month 1 | Quick Wins実行 + ボトルネック1 | {Activation率 XX% → XX%} | 外部顧客XXX社/人 |
| Month 2 | ボトルネック2改善 + A/Bテスト | {Retention率 XX% → XX%} | 継続率XX%達成 |
| Month 3 | ボトルネック3 + 総合評価 | {MRR ¥XXX,XXX → ¥XXX,XXX} | 3年黒字計画進捗確認 |

**3ヶ月後の目標ファネル**:
```
総顧客数: XXX社/人（現状比+XX%）
  ├ 社内顧客: XXX社/人
  └ 外部顧客: XXX社/人（Ring 3基準100社/人以上達成）
  ↓ 初回利用率: XX%（+XX%、目標80-96%）
初回利用: XXX社/人
  ↓ Aha Moment達成率: XX%（+XX%）
活性化: XXX社/人
  ↓ 継続率（1ヶ月）: XX%（+XX%、目標98%）
継続: XXX社/人
  ↓ 課金転換率: XX%（+XX%）
有料: XXX社/人
  ↓ ARPU: ¥XXX（+¥XX）
MRR: ¥XXX,XXX（+XX%）
LTV/CAC比: X.XX（目標10-30倍）
```

**Ring 3承認申請準備**:
- 外部顧客100社/人以上達成: [達成 / 未達成]
- 収益化開始: [開始 / 未開始]
- 3年黒字計画進捗: [順調 / 要調整]
- 役員承認用資料作成: `/build-approval-deck`

---

## 次のアクション

1. **即時実行**: Quick Wins施策の実装開始（ForRecruit資産活用型）
2. **Week 1の目標設定**: {具体的な目標KPI}
3. **測定環境整備**: アナリティクスダッシュボード更新（社内外データ統合）
4. **チーム共有**: 本レポートを関係者に展開
5. **Ring 3承認申請準備**: `/build-approval-deck` の実行検討

---

## 参考情報

### ForRecruit Benchmark出典

- Recruit_Product_Research: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/analysis/integrated_analysis_report.md`
- 成功事例: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/documents/SUCCESS/`

### 測定ツール

- Google Analytics 4: {URL}
- Mixpanel/Amplitude: {URL}
- 社内CRM: {URL}
- 決済システム: {URL}

### 関連ドキュメント

- PMF診断レポート: `Flow/{YYYYMM}/{YYYY-MM-DD}/pmf_diagnosis.md`
- Ring 3診断レポート: `Flow/{YYYYMM}/{YYYY-MM-DD}/ring_criteria_diagnosis.md`
- フライホイール設計: `{IDEA_FOLDER}/documents/2_discovery/flywheel.md`
- 社内承認用資料: `/build-approval-deck`

---

**作成者**: Claude Sonnet 4.5
**スキル**: `/analyze-aarrr` (ForRecruit Edition)
**フレームワーク準拠**: 起業の科学 - AARRRフレームワーク + Ring 3基準
**Research統合**: Recruit_Product_Research 31製品分析
**Benchmark製品**: Airレジ、Airペイ、スタディサプリ、Geppo
```

---

## 成功基準

1. ✅ **AARRR 5段階すべて測定（社内外統合）**: Acquisition（社内+外部）→ Revenue まで完全測定
2. ✅ **ForRecruit実績ベンチマーク適用**: Airレジ、Airペイ、Geppo等の実績値をベンチマーク化
3. ✅ **ボトルネック自動検出**: 転換率がForRecruit Benchmarkを下回る段階を特定
4. ✅ **改善施策優先順位付け**: Impact × Ease でスコアリング、ForRecruit資産活用度を考慮
5. ✅ **実装ロードマップ自動生成**: 1ヶ月/3ヶ月の具体的な計画、Ring 3承認申請準備
6. ✅ **Quick Wins特定**: 高Impact × 高Ease × ForRecruit資産活用の即実行施策を抽出
7. ✅ **社内リソース活用パターン分析**: 6種資産の活用状況評価、期待PMFスコア・成功率の算出
8. ✅ **Ring 3基準準拠チェック**: 3年黒字・5年累損解消計画との整合性確認

---

## Knowledge Base参照

- AARRRフレームワーク: `@startup_science/05_scale/aarrr_framework.md`（未作成の場合はWebSearchで補完）
- ユニットエコノミクス: `@startup_science/04_pmf/unit_economics.md`
- グロースハック: `@startup_science/05_scale/growth_hacking.md`
- **ForRecruit Research**: `@Recruit_Product_Research/analysis/integrated_analysis_report.md`
- **ForRecruit成功事例**: `@Recruit_Product_Research/documents/SUCCESS/`

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
- スキル別推奨事例: @.claude/skills/_shared/case_reference_for_recruit.md#skill-mapping-analyze-aarrr
- AARRR指標ベンチマーク: @.claude/skills/_shared/knowledge_base.md#forrecruit-aarrr-benchmarks

### 全体参照
- ForRecruit全体概要: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
- Ring制度ステージゲート: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
- 撤退基準: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---
## 注意事項

1. **ForRecruit特化調整**:
   - Acquisition: 社内+外部の2段階評価必須
   - Activation: 社内実績基準（Geppo 96%、Airレジ80%）を適用
   - Retention: 継続率98%目標（Geppo基準）
   - Revenue: 3年黒字・5年累損解消計画必須
   - Referral: 社内NPS基準（60-80）

2. **社内リソース活用の最大化**: 営業網、既存顧客基盤、ブランド力の活用を最優先施策とする

3. **Ring 3基準の厳守**: 外部顧客100社/人以上、収益化開始、3年黒字計画を必須要件とする

4. **ForRecruit Benchmark参照**: Airレジ、Airペイ、Geppo等の成功製品実績を常に参照

5. **失敗パターン回避**: エリクラ（外部スケール失敗）、スタサプ個別（Unit Economics不健全）の教訓を活かす

---

## 更新履歴

- 2026-01-02: ForRecruit特化版として新規作成、Recruit_Product_Research 31製品分析統合
- ForRecruit Benchmark追加（Airレジ、Airペイ、スタディサプリ、Geppo）
- 社内リソース活用パターン分析追加
- Ring 3基準準拠チェック追加
- Domain-Specific Knowledgeセクション追加（18事例統合）
