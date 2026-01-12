---
name: analyze-aarrr-for-genai
description: |
  AARRR（Acquisition/Activation/Retention/Referral/Revenue）フレームワークで成長ファネルを測定（ForGenAI特化版）。Product Hunt/GitHub/Hacker Newsでの獲得、初回プロンプト成功率、月次リテンション、バイラル係数、Free→Paid転換率を評価。AI製品特化の追加指標（プロンプト再利用率、API利用率、精度改善率）を統合。

  ForGenAI調整:
  - Acquisition: Product Hunt Top 5、GitHub Stars 1,000以上
  - Activation: 初回プロンプト成功率80%以上
  - Retention: 月次リテンション40%以上（プロンプト再利用）
  - Revenue: Free→Paid転換率10%以上
  - Referral: バイラル係数1.2以上（AI生成コンテンツ共有）

  使用タイミング：
  - Product Huntローンチ後
  - 月次/週次の成長レビュー
  - VC調達申請前の健全性確認

  所要時間：40-60分（AI特化メトリクス含む）
  出力：AARRR分析レポート（ForGenAI版）、改善施策優先順位リスト
trigger_keywords:
  - "AARRR"
  - "パイレーツメトリクス"
  - "成長ファネル"
  - "ファネル分析"
  - "グロースハック"
  - "AI製品メトリクス"
stage: Phase3（スケール）、Product Huntローンチ後
dependencies:
  - validate-pmf（PMF達成が前提）
  - create-producthunt-strategy（Product Huntローンチ完了が前提）
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/aarrr_analysis_forgenai.md
execution_time: 40-60分
framework_reference: Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
priority: P0
framework_compliance: 100%
---

# Analyze AARRR Skill (ForGenAI Edition)

AARRR（Pirate Metrics）5段階ファネルを測定し、成長ボトルネックを特定する自律実行型Skill（ForGenAI特化版）。AI製品成功事例から抽出したProduct Hunt/GitHub基準とベストプラクティスを統合。

---

## このSkillでできること

1. **5段階ファネル測定（AI製品特化）**: Acquisition（Product Hunt/GitHub）→ Activation（初回プロンプト成功）→ Retention（プロンプト再利用）→ Referral（バイラル係数）→ Revenue（Freemium転換）の転換率を自動計測
2. **AI製品実績基準での評価**: ChatGPT、Jasper、Midjourney等の成功製品KPIをベンチマーク化
3. **AI特化メトリクス分析**: プロンプト再利用率、API利用率、精度改善率の評価
4. **改善施策の優先順位付け**: インパクトと実装難易度でQuick Winsを特定
5. **VC調達基準準拠チェック**: 月次成長率20%以上、年次3倍以上との整合性確認

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `pmf_diagnosis.md`, `producthunt_results.md`, アナリティクスデータ, GitHub統計 |
| **出力** | `Flow/{YYYYMM}/{YYYY-MM-DD}/aarrr_analysis_forgenai.md` |
| **次のSkill** | `/for-genai-prepare-vc-meeting`（VC調達準備） or 個別改善施策の実行 |

---

## Domain-Specific Knowledge (from GenAI_research)

### Success Patterns

**1. ChatGPT（AARRR成功事例）**
- **Acquisition**: 史上最速1億ユーザー達成（2ヶ月）、Product Hunt未ローンチでもバイラル拡散
- **Activation**: 初回プロンプト成功率90%以上（推定）、直感的UI
- **Retention**: 月次リテンション60%以上（推定）、DAU/MAU 50%
- **Referral**: バイラル係数3.0（SNSシェア爆発的拡散）
- **Revenue**: ChatGPT Plus月額$20、転換率推定5-10%

**2. Jasper（AARRR成功事例）**
- **Acquisition**: Product Hunt Top 5達成、1年10万ユーザー
- **Activation**: 初回コンテンツ生成成功率85%以上（推定）
- **Retention**: 月次リテンション50%以上（推定）、DAU/MAU 40%
- **Referral**: バイラル係数1.5（マーケターコミュニティでの口コミ）
- **Revenue**: 月額$99、Freemium転換率15%

**3. Midjourney（AARRR成功事例）**
- **Acquisition**: Product Hunt Top 1達成、Discord統合で1年1,500万ユーザー
- **Activation**: 初回画像生成成功率95%以上（推定）
- **Retention**: 月次リテンション60%以上（推定）、DAU/MAU 50%
- **Referral**: バイラル係数2.5（Discord + SNSシェア）
- **Revenue**: 月額$30、Freemium転換率20%

**4. Perplexity（AARRR成功事例）**
- **Acquisition**: Product Hunt Top 3達成、1年1,000万ユーザー
- **Activation**: 初回検索成功率90%以上（推定）
- **Retention**: 月次リテンション40%以上（推定）、DAU/MAU 35%
- **Referral**: バイラル係数1.2（検索精度の口コミ）
- **Revenue**: 月額$20、Freemium転換率12%

### Common Pitfalls

**失敗パターン1: Product Hunt未ローンチ**
- **汎用AI製品の失敗**: 初期ユーザー獲得困難、テックコミュニティ認知度0
- **教訓**: Product Hunt Top 5達成で月間1,000ユーザー獲得、初速確保必須

**失敗パターン2: Activation低迷（初回プロンプト失敗）**
- **AI製品の失敗**: 初回プロンプト成功率60%以下、ユーザー離脱70%
- **教訓**: 直感的UI、テンプレートプロンプト提供で成功率80%以上達成

**失敗パターン3: Retention低迷（プロンプト再利用なし）**
- **AI製品の失敗**: 月次リテンション20%以下、DAU/MAU 10%未満
- **教訓**: プロンプトライブラリ、履歴機能でリテンション40%以上達成

**失敗パターン4: Revenue低迷（Freemium転換率3%以下）**
- **AI製品の失敗**: 無料プランで十分、有料プラン価値不足
- **教訓**: Free→Paid差別化（精度・速度・API回数制限）で転換率10%以上達成

### Quantitative Benchmarks

**Acquisition（獲得）**:
- Product Hunt Top 5: 月間1,000ユーザー獲得
- GitHub Stars 1,000以上: テックコミュニティ認知度高い
- Hacker News フロントページ: 1日5,000ユーザー獲得（推定）

**Activation（活性化）**:
- 初回プロンプト成功率: 80%以上（ChatGPT 90%、Jasper 85%、Midjourney 95%）
- 初回生成時間: 3秒以内（Perplexity 2秒、Jasper 3秒）
- テンプレートプロンプト利用率: 50%以上（初心者向け）

**Retention（継続）**:
- 月次リテンション: 40%以上（ChatGPT 60%、Midjourney 60%、Jasper 50%、Perplexity 40%）
- DAU/MAU比率: 35%以上（ChatGPT 50%、Midjourney 50%、Jasper 40%、Perplexity 35%）
- プロンプト再利用率: 60%以上（過去プロンプトの再実行）

**Referral（紹介）**:
- バイラル係数: 1.2以上（ChatGPT 3.0、Midjourney 2.5、Jasper 1.5、Perplexity 1.2）
- SNSシェア率: 20%以上（AI生成コンテンツのX/Twitter投稿）
- NPS: 60以上（ChatGPT 80、Jasper 70、Midjourney 75、Perplexity 65）

**Revenue（収益化）**:
- Freemium転換率: 10%以上（Midjourney 20%、Jasper 15%、Perplexity 12%、ChatGPT推定5-10%）
- 月額課金: $20-99（ChatGPT $20、Perplexity $20、Midjourney $30、Jasper $99）
- API利用率（有料ユーザー）: 70%以上（月次アクティブ利用）

**AI特化メトリクス**:
- プロンプト再利用率: 60%以上
- API利用率（有料ユーザー）: 70%以上
- 精度改善率: 月次+2%（ユーザーフィードバック反映）

### Best Practices

1. **Product Hunt戦略によるAcquisition加速**:
   - 事前コミュニティ参加: 3ヶ月前からHacker News、Reddit参加
   - Hunter確保: 影響力のあるHunter（フォロワー10,000人以上）に依頼
   - ローンチ日最適化: 火曜-木曜が最適、金曜-月曜は避ける
   - 効果: Product Hunt Top 5で月間1,000ユーザー獲得

2. **直感的UIとテンプレートプロンプトでActivation向上**:
   - テンプレートプロンプト提供: 初心者向け10-20種類
   - ワンクリック生成: プロンプト入力なしで生成開始
   - リアルタイムプレビュー: 生成過程を可視化
   - 効果: 初回プロンプト成功率60% → 80%向上

3. **プロンプトライブラリでRetention向上**:
   - プロンプト履歴保存: 過去プロンプトの再利用
   - お気に入り機能: 頻繁に使うプロンプトをブックマーク
   - プロンプト共有: コミュニティでの共有機能
   - 効果: 月次リテンション30% → 40%向上、プロンプト再利用率60%

4. **Free→Paid差別化でRevenue向上**:
   - 精度差別化: Free 85%、Paid 92%（ファインチューニング）
   - 速度差別化: Free 5秒、Paid 2秒（優先処理）
   - API回数制限: Free 月100回、Paid 無制限
   - 効果: Freemium転換率5% → 10%向上

5. **SNSシェア機能でReferral加速**:
   - X/Twitterシェアボタン: AI生成コンテンツの即座投稿
   - 透かし追加: 生成画像にブランドロゴ
   - Discord統合: Midjourneyモデル（1,500万メンバー）
   - 効果: バイラル係数1.0 → 1.5向上

### Reference

- 詳細: @GenAI_research/case_studies/ai_product_success_patterns.md
- AARRR分析: @GenAI_research/metrics/ai_aarrr_benchmarks.md

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 40-60分

### 自動実行ステップ

1. 全データソース読み込み（アナリティクス、Product Hunt、GitHub）
2. **Acquisition（獲得）評価**
3. **Activation（活性化）評価**
4. **Retention（継続）評価**
5. **Referral（紹介）評価**
6. **Revenue（収益化）評価**
7. **AI特化メトリクス評価**（プロンプト再利用率、API利用率、精度改善率）
8. ボトルネック特定
9. 改善施策の優先順位付け（インパクト × 実装難易度）
10. ベンチマーク比較（成功AI製品との比較）
11. 成果物出力

### 5段階ファネル評価基準（ForGenAI版）

**Acquisition（獲得）**:
| 指標 | 合格基準 | 評価 |
|------|---------|------|
| Product Hunt実績 | Top 5達成 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| 月間新規ユーザー | 1,000人以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| GitHub Stars | 1,000以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| CAC | $20以内 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |

**Activation（活性化）**:
| 指標 | 合格基準 | 評価 |
|------|---------|------|
| 初回プロンプト成功率 | 80%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| 初回生成時間 | 3秒以内 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| テンプレートプロンプト利用率 | 50%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |

**Retention（継続）**:
| 指標 | 合格基準 | 評価 |
|------|---------|------|
| 月次リテンション | 40%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| DAU/MAU比率 | 35%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| プロンプト再利用率 | 60%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |

**Referral（紹介）**:
| 指標 | 合格基準 | 評価 |
|------|---------|------|
| バイラル係数 | 1.2以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| SNSシェア率 | 20%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| NPS | 60以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |

**Revenue（収益化）**:
| 指標 | 合格基準 | 評価 |
|------|---------|------|
| Freemium転換率 | 10%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| 月額課金 | $20-99 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| API利用率（有料ユーザー） | 70%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| LTV/CAC比 | 5.0以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |

**AI特化メトリクス**:
| 指標 | 合格基準 | 評価 |
|------|---------|------|
| プロンプト再利用率 | 60%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| API利用率（有料ユーザー） | 70%以上 | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |
| 精度改善率 | 月次+2% | ✅ 良好 / ⚠️ 要改善 / ❌ 未達 |

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @startup_science/03_stages/scale/aarrr_metrics.md
- @.claude/skills/_shared/skill_chains.md
- @.claude/skills/_shared/error_handling_patterns.md
- **@GenAI_research/case_studies/ai_product_success_patterns.md**
- **@GenAI_research/metrics/ai_aarrr_benchmarks.md**

---

## ForGenAI Knowledge Base Reference

### 評価基準・フレームワーク
- CPF/PSF/PMF基準: @.claude/skills/_shared/knowledge_base.md#forgenai-evaluation
- AI技術スタック選定: @.claude/skills/_shared/knowledge_base.md#ai-tech-stack
- Product Hunt戦略: @.claude/skills/_shared/knowledge_base.md#producthunt-strategy
- ForGenAI評価基準: @.claude/skills/_shared/knowledge_base.md#forgenai-evaluation

### 事例参照
- 成功パターン（AI製品）: @GenAI_research/case_studies/success/
- 失敗パターン: @GenAI_research/case_studies/failure/
- ChatGPT事例: @GenAI_research/case_studies/success/chatgpt_viral_growth.md
- Jasper事例: @GenAI_research/case_studies/success/jasper_content_generation.md
- Midjourney事例: @GenAI_research/case_studies/success/midjourney_image_generation.md

### 全体参照
- ForGenAI全体概要: @.claude/skills/_shared/knowledge_base.md#forgenai-edition
- AI技術動向: @GenAI_research/technology_trends/
- AI倫理対応: @.claude/skills/_shared/knowledge_base.md#ai-ethics

---

## 使用例

```
User: /for-genai-analyze-aarrr

Skill:
# AARRR分析 自律実行開始（ForGenAI Edition）

[全データソース読み込み]

[自動実行中...]
- STEP 1: 全データソース読み込み ✅
- STEP 2: Acquisition評価 ✅
- STEP 3: Activation評価 ✅
- STEP 4: Retention評価 ✅
- STEP 5: Referral評価 ✅
- STEP 6: Revenue評価 ✅
- STEP 7: AI特化メトリクス評価 ✅
- STEP 8: ボトルネック特定 ✅
- STEP 9: 改善施策優先順位付け ✅
- STEP 10: ベンチマーク比較 ✅
- STEP 11: 成果物出力 ✅

## 完了

成果物: aarrr_analysis_forgenai.md

【AARRR評価結果】:
- **Acquisition**: ✅ 良好（Product Hunt Top 5、月間1,200ユーザー）
- **Activation**: ⚠️ 要改善（初回プロンプト成功率75%、目標80%未達）
- **Retention**: ✅ 良好（月次リテンション42%、DAU/MAU 38%）
- **Referral**: ⚠️ 要改善（バイラル係数1.0、目標1.2未達）
- **Revenue**: ✅ 良好（Freemium転換率12%）

【AI特化メトリクス】:
- プロンプト再利用率: 65%（✅ 良好）
- API利用率（有料ユーザー）: 72%（✅ 良好）
- 精度改善率: 月次+1.5%（⚠️ 目標+2%未達）

【ボトルネック特定】:
1. **Activation低迷**: 初回プロンプト成功率75%（目標80%未達） → 20%のユーザーが初回失敗で離脱
2. **Referral低迷**: バイラル係数1.0（目標1.2未達） → 口コミ拡散不足

【改善施策優先順位】:
1. **Quick Win - Activation向上（インパクト: 高、実装: 易）**:
   - テンプレートプロンプト10種類追加（実装: 1週間）
   - ワンクリック生成機能追加（実装: 2週間）
   - 期待効果: 初回プロンプト成功率75% → 80%、離脱率20% → 15%

2. **Quick Win - Referral向上（インパクト: 高、実装: 易）**:
   - X/Twitterシェアボタン追加（実装: 1週間）
   - AI生成コンテンツに透かし追加（実装: 1週間）
   - 期待効果: バイラル係数1.0 → 1.3、月間ユーザー1,200 → 1,560（+30%）

3. **中期施策 - 精度改善（インパクト: 中、実装: 難）**:
   - ユーザーフィードバックループ構築（実装: 1ヶ月）
   - ファインチューニング強化（実装: 2ヶ月）
   - 期待効果: 精度改善率+1.5% → +2%、精度92% → 94%

【ベンチマーク比較】:
- ChatGPT: Acquisition（史上最速）、Activation 90%、Retention 60%、Referral 3.0、Revenue 5-10%
- Jasper: Activation 85%、Retention 50%、Referral 1.5、Revenue 15%
- Midjourney: Activation 95%、Retention 60%、Referral 2.5、Revenue 20%
- **現在の製品**: Acquisition ✅、Activation 75%（⚠️）、Retention 42%（✅）、Referral 1.0（⚠️）、Revenue 12%（✅）

推奨アクション:
1. Activation向上施策を2週間以内に実装（Quick Win）
2. Referral向上施策を2週間以内に実装（Quick Win）
3. 次回AARRR分析（1ヶ月後）で効果検証
```

---

**テンプレートバージョン**: v3.1-ForGenAI
**最終更新**: 2026-01-03
**作成者**: Claude Code
**ForGenAI特化要素**: 4件のAI製品成功事例統合、AI特化メトリクス追加、Product Hunt/GitHub評価追加、バイラル係数基準追加
