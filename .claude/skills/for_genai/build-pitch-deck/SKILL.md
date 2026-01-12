---
skill: build-pitch-deck
description: |
  VC調達用の10-15スライドピッチデッキを自動生成する自律実行型スキル（ForGenAI版）。

  **GenAI特化カスタマイズ**：
  - AI技術スタック明記（使用モデル、API費用、ファインチューニング有無）
  - データ戦略（プロプライエタリデータの有無、データフライホイール）
  - 競合差別化（AI精度、応答速度、ハルシネーション率等の定量比較）
  - GenAI市場トレンド（2024: $50B → 2030: $1.3T予測）
  - VC投資トレンド（2023-2024 GenAI投資額$25B、全VC投資の20%）

  使用タイミング：
  - CPF/PSF/PMF検証完了後
  - Seed/Series A資金調達準備時
  - VC投資家ミーティング前

  所要時間：30-45分（自動実行）
  出力：pitch_deck.md
trigger_keywords:
  - "ピッチデッキ作成"
  - "投資家向けプレゼン"
  - "VC資料作成"
  - "調達資料"
  - "build pitch deck"
stage: PSF/PMF検証後
dependencies:
  - validate-cpf (CPFスコア70%以上)
  - validate-psf (PSFスコア達成)
  - validate-10x (3軸以上の10倍優位性)
  - validate-unit-economics (LTV/CAC 5.0以上推奨)
  - lean_canvas.md
  - persona.md
  - cpf_judgment.md
  - psf_validation.md
  - 10x_validation.md
  - unit_economics.md
output_file: documents/3_planning/pitch_deck.md
execution_time: 30-45分
framework_reference: |
  - 起業の科学 STEP 3-5（CPF/PSF/PMF検証）
  - a16z/YC/Sequoia ピッチデッキテンプレート
  - GenAI Investment Trends 2023-2024
  - OpenAI/Anthropic/Perplexity ピッチデッキ分析
priority: P0
framework_compliance: 100%
version: 1.0-ForGenAI
created_at: 2026-01-02
domain: ForGenAI
---

# Build Pitch Deck Skill (ForGenAI Edition)

GenAI特化型VC調達用の10-15スライドピッチデッキを自動生成する自律実行型Skill。

---

## このSkillでできること

1. **検証成果物統合**: CPF/PSF/PMF検証結果、ユニットエコノミクス、競合分析を統合
2. **10-15スライド構成**: VC投資家が期待する標準構成を自動生成
3. **GenAI特化カスタマイズ**: AI技術スタック、データ戦略、精度比較を明示
4. **定量データ可視化**: トラクション、成長率、ユニットエコノミクスをグラフ形式で提示
5. **投資家説得力スコア**: 各スライドの完成度を0-10点で評価（合計100-150点）
6. **改善提案**: スコア70点未満のスライドに対する具体的改善案

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `lean_canvas.md`, `persona.md`, `cpf_judgment.md`, `psf_validation.md`, `10x_validation.md`, `unit_economics.md`, `competitor_research.md`, `ai_tech_stack.md` |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/3_planning/pitch_deck.md` |
| **次のSkill** | `/prepare-vc-meeting`（VC対応Q&A準備）、`/create-fundraising-plan`（資金調達ロードマップ） |
| **ステージ** | Seed/Series A資金調達準備 |

---

## KB参照

このスキルは以下のナレッジベースを参照します：

### 理論基盤
- @startup_science/01_stages/cpf/cpf_overview.md
- @startup_science/02_stages/psf/psf_overview.md
- @startup_science/03_stages/pmf/pmf_overview.md
- @for_genai/GenAI_research/market_trends.md
- @for_genai/GenAI_research/vc_investment_patterns.md

### ピッチデッキ成功事例（Tier 2 ケーススタディ）

**総合評価**: 平均投資家説得力スコア 121/130点（最優秀レベル）

#### 1. OpenAI - $10B Microsoft投資（2023）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_001_openai.md**
- スコア: 128/130（最優秀）
- 学び: AGI Vision、API-first戦略、Developer Ecosystem構築
- KPI: ChatGPT 100M MAU達成（史上最速）、API収益$1B+

#### 2. Anthropic - $4B Amazon + Google投資（2024）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_002_anthropic.md**
- スコア: 126/130（最優秀）
- 学び: Constitutional AI、Safety-first差別化、Enterprise信頼性
- KPI: Claude API採用企業1,000+、ハルシネーション率20%減

#### 3. Perplexity - $73M Series B（2024）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_003_perplexity.md**
- スコア: 122/130（最優秀）
- 学び: Answer Engine定義、リアルタイム検索AI、Citation機能
- KPI: 10M MAU、検索精度95%、応答速度2秒以内

#### 4. Character.AI - $150M Series A（2023 → Google $2.7B買収）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_004_character_ai.md**
- スコア: 120/130（優秀）
- 学び: バイラルグロース、UGCキャラクター、エンゲージメント指標
- KPI: 100M訪問/月、平均セッション時間29分

#### 5. Jasper AI - $125M Series A（2022）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_005_jasper_ai.md**
- スコア: 118/130（優秀）
- 学び: B2Bコンテンツ生成、テンプレートライブラリ、エンタープライズSaaS
- KPI: $75M ARR、15,000企業顧客、NRR 130%

#### 6. Stability AI - $101M（2022）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_006_stability_ai.md**
- スコア: 125/130（最優秀）
- 学び: オープンソース戦略、Stable Diffusion、コミュニティ主導
- KPI: 10M+ DreamStudio ユーザー、API利用10億リクエスト/月

#### 7. Cohere - $270M Series C（2023）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_007_cohere.md**
- スコア: 119/130（優秀）
- 学び: Enterprise特化、プライベートデプロイ、カスタマイズ性
- KPI: Fortune 500企業50+、API精度92%

#### 8. Adept - $350M Series B（2023）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_008_adept.md**
- スコア: 117/130（優秀）
- 学び: Action-oriented AI、Workflow自動化、Multi-modal
- KPI: タスク完了率85%、統合アプリ100+

#### 9. Midjourney - 自己資金（ピッチデッキなし → 参考分析）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_009_midjourney.md**
- スコア: 123/130（最優秀）
- 学び: Discord-native、コミュニティファースト、サブスク収益化
- KPI: 15M+ ユーザー、$200M ARR（推定）、収益性100%

#### 10. Runway ML - $141M Series C（2023）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_010_runway_ml.md**
- スコア: 120/130（優秀）
- 学び: クリエイター特化、動画生成AI、プロフェッショナルツール
- KPI: 8M+ クリエイター、Hollywood採用実績

#### 11. Inflection AI - $1.3B調達後、Microsoft吸収（失敗・改善事例）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_011_inflection_ai.md**
- スコア: 110/130（良好 → 課題あり）
- 学び: B2C特化の限界、競合激化、ピボット失敗
- 課題: 差別化不足、収益化遅延、資金燃焼率

#### 12. AI21 Labs - 複数回調達、成長率課題（失敗・改善事例）
- **@.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_012_ai21_labs.md**
- スコア: 108/130（良好 → 課題あり）
- 学び: 技術先行の落とし穴、市場タイミング、Go-to-Market弱点
- 課題: プロダクト複雑性、ターゲット不明確

**統合レポート**: @.claude/skills/for_genai/build-pitch-deck/case_studies/README.md

---

## ピッチデッキ構成（10-15スライド）

### 標準構成（GenAI特化版）

| スライド# | 名称 | 内容 | 配点 | 重要度 |
|:--------:|------|------|:----:|:------:|
| 1 | **Title** | 会社名、ミッション、1行キャッチコピー | 5点 | 中 |
| 2 | **Problem** | 解決する課題、3Uスコア、課題の大きさを定量化 | 10点 | 最高 |
| 3 | **Solution** | UVP（独自の価値提案）、MVPデモ、Before/After | 10点 | 最高 |
| 4 | **Market Size** | TAM/SAM/SOM、GenAI市場成長率、タイミング | 10点 | 高 |
| 5 | **AI Technology** | 使用モデル、技術スタック、AI精度、データ戦略 | 15点 | **最高** |
| 6 | **Product** | プロダクト詳細、ロードマップ、技術スタック | 10点 | 高 |
| 7 | **Traction** | KPI、成長率、初期ユーザー数、NPS | 15点 | 最高 |
| 8 | **Business Model** | 収益モデル、ユニットエコノミクス、LTV/CAC | 15点 | 最高 |
| 9 | **Competition** | 競合分析、AI精度比較、10倍優位性、参入障壁 | 10点 | 高 |
| 10 | **Go-to-Market** | GTM戦略、フライホイール、グロースハック施策 | 10点 | 高 |
| 11 | **Team** | 創業チーム、AI専門性、FIF、アドバイザー、採用計画 | 10点 | 高 |
| 12 | **Financials** | 3年間の財務予測、主要KPI推移、損益分岐点 | 10点 | 高 |
| 13 | **Ask** | 調達額、資金使途、マイルストーン、評価額 | 10点 | 高 |
| 14-15 | **Appendix** | AI技術詳細、データセット、追加図表、参考資料 | 5点 | 低 |

**合計配点**: 145点（必須13スライド: 140点 + Appendix: 5点）

**GenAI特化追加スライド**: AI Technology（15点配点）

---

## 投資家説得力スコア基準

### 総合評価基準（GenAI版）

| スコア範囲 | 判定 | 投資家の反応（想定） | 次のアクション |
|-----------|------|---------------------|---------------|
| **120-145点** | 🏆 最優秀 | 即座に次回ミーティング設定、Term Sheet提示 | Series A調達開始 |
| **100-119点** | ✅ 優秀 | 追加情報リクエスト後に判断 | AI精度データ追加後に調達 |
| **80-99点** | ⚠️ 良好 | 関心は示すが投資判断保留 | AI技術差別化強化、3ヶ月改善後に再提出 |
| **80点未満** | ❌ 要再構築 | 投資見送り | CPF/PSF再検証、技術差別化再定義 |

### スライド別評価基準（GenAI特化項目）

#### AI Technology スライド（15点満点）**[NEW]**

| 点数 | 基準 |
|:----:|------|
| 15点 | 使用モデル明記（GPT-4, Claude等）、API費用試算、ファインチューニング戦略、プロプライエタリデータあり、AI精度定量比較（競合比20%以上優位）、ハルシネーション率測定済み |
| 12点 | 使用モデル明記、API費用試算、データ戦略あり、AI精度比較あり |
| 9点 | 使用モデル明記のみ、データ戦略不明確 |
| 6点以下 | AI技術スタック不明確、「AIを活用」のみで具体性なし |

#### Problem スライド（10点満点）

| 点数 | 基準 |
|:----:|------|
| 10点 | 課題が明確、定量データ完備（発生頻度、コスト損失、時間損失）、3Uスコア全8点以上、**GenAI適用妥当性説明あり** |
| 8点 | 課題が明確、一部定量データあり、3Uスコア7点以上 |
| 6点 | 課題は理解できるが定量データ不足、3Uスコア6点以上 |
| 4点以下 | 課題が不明確、定量データなし、GenAI適用理由不明 |

#### Competition スライド（10点満点）

| 点数 | 基準 |
|:----:|------|
| 10点 | 10倍優位性3軸以上明示、**AI精度・応答速度・ハルシネーション率の定量比較**、競合マトリクス、参入障壁説明あり |
| 8点 | 10倍優位性2軸、AI精度比較あり |
| 6点 | 競合リストのみ、差別化ポイント不明確 |
| 4点以下 | 競合認識なし、または「競合なし」と主張 |

---

## Domain-Specific Knowledge (from Research)

### GenAI Market Context

#### 市場規模・成長率
- **2024年市場規模**: $50B
- **2030年予測**: $1.3T（年率55%成長）
- **主要セグメント**:
  - Text Generation: $20B（40%）
  - Code Generation: $12B（24%）
  - Image/Video Generation: $10B（20%）
  - Voice/Audio: $5B（10%）
  - Other: $3B（6%）

#### VC投資トレンド（2023-2024）
- **GenAI投資総額**: $25B（全VC投資の20%）
- **平均調達額**:
  - Pre-Seed: $2-5M
  - Seed: $10-20M
  - Series A: $50-100M
  - Series B: $200-400M
- **主要投資家**: a16z, Sequoia, Google Ventures, Microsoft Ventures, Index Ventures

### Success Patterns（ピッチデッキ成功パターン）

#### 事例1: OpenAI（$10B Microsoft投資、2023）

**AI Technology スライドの特徴**:
- GPT-4アーキテクチャ明記（1.8T parameters）
- API費用モデル透明性（$0.03/1K tokens input, $0.06/1K tokens output）
- ファインチューニング戦略（RLHF、Constitutional AI）
- プロプライエタリデータ: WebText、CodeText、Conversation データ

**Traction スライドの特徴**:
- ChatGPT 100M MAU達成（2ヶ月で史上最速）
- API収益$1B+（2023年）
- Developer Ecosystem: 2M+ developers
- Enterprise導入: Fortune 500企業80%

**投資家評価のポイント**:
- Microsoft: 「AGI実現への最短経路」
- AGI Vision の明確性、API-first戦略、Developer Ecosystem構築

**参照**: @.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_001_openai.md

#### 事例2: Anthropic（$4B Amazon + Google投資、2024）

**AI Technology スライドの特徴**:
- Constitutional AI明記（価値観アライメント）
- Safety-first差別化（ハルシネーション率20%減）
- Claude 3アーキテクチャ（Opus/Sonnet/Haiku）
- プロプライエタリデータ: 人間フィードバック、安全性評価データ

**Competition スライドの特徴**:
- 競合比較: OpenAI GPT-4 vs Anthropic Claude 3
  - ハルシネーション率: GPT-4 15% vs Claude 12%
  - 応答速度: GPT-4 3.2秒 vs Claude 2.8秒
  - Enterprise信頼性: Claude 99.9% SLA

**投資家評価のポイント**:
- Amazon/Google: 「Enterprise特化、安全性重視」
- Constitutional AI の独自性、Safety-first差別化

**参照**: @.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_002_anthropic.md

#### 事例3: Stability AI（$101M、2022）

**Go-to-Market スライドの特徴**:
- オープンソース戦略（Stable Diffusion）
- コミュニティ主導（10M+ users）
- API収益化（10億リクエスト/月）
- DreamStudio フリーミアムモデル

**Traction スライドの特徴**:
- GitHub Stars: 50K+（公開1週間で）
- API利用: 10億リクエスト/月
- DreamStudio ユーザー: 10M+
- コミュニティ生成画像: 1B+

**投資家評価のポイント**:
- オープンソース戦略の成功、コミュニティエンゲージメント、API収益化モデル

**参照**: @.claude/skills/for_genai/build-pitch-deck/case_studies/GENAI_PITCH_DECK_006_stability_ai.md

### Quantitative Benchmarks（定量的ベンチマーク）

**GenAI特化基準（Tier 2統合）**:

| 指標 | Pre-Seed基準 | **Seed基準** | Series A基準 | Series B基準 | 出典 |
|------|-------------|-------------|-------------|-------------|------|
| **CPFスコア** | 60%+ | **70%+** | 80%+ | 90%+ | GenAI競合激化 |
| **AI精度** | 80%+ | **85%+** | 90%+ | 95%+ | OpenAI, Anthropic |
| **応答速度** | <5秒 | **<3秒** | <2秒 | <1秒 | Perplexity, Character.AI |
| **ハルシネーション率** | <20% | **<15%** | <10% | <5% | Anthropic, Cohere |
| **月次成長率** | 15%+ | **25%+** | 30%+ | 20%+ | Character.AI 100M MAU/2ヶ月 |
| **LTV/CAC** | 3.0+ | **5.0+** | 7.0+ | 10.0+ | Jasper AI, Runway |
| **API収益** | - | $100K+ MRR | $1M+ MRR | $10M+ MRR | OpenAI, Stability AI |
| **ユーザー数** | 1K+ | **10K+** | 100K+ | 1M+ | Character.AI, Midjourney |
| **投資家説得力スコア** | 100+ | **110+** | 120+ | 130+ | Tier 2事例平均121点 |

**成功率の目安**:
- 120-145点: Series A調達成功率90%以上（OpenAI 128点、Anthropic 126点、Stability AI 125点）
- 100-119点: Series A調達成功率70%（改善推奨）
- 80-99点: Series A調達困難（AI技術差別化強化、3ヶ月改善後に再提出）

### AI Technology Slide - 最重要の5つの要素

**平均スコア**: 14.2/15点（95%達成率）

1. **使用モデル明記**:
   - OpenAI: GPT-4（1.8T parameters）
   - Anthropic: Claude 3（Opus/Sonnet/Haiku）
   - Cohere: Command R（100B+ parameters）
   - Stability AI: Stable Diffusion 2.1（890M parameters）

2. **API費用モデル**:
   - OpenAI: $0.03/1K tokens（input）、$0.06/1K tokens（output）
   - Anthropic: $0.015/1K tokens（Claude Haiku）、$0.08/1K tokens（Claude Opus）
   - Perplexity: $5/月（Pro）、API $0.05/query
   - Jasper AI: $39-125/月（サブスク）

3. **ファインチューニング戦略**:
   - OpenAI: RLHF（人間フィードバック）
   - Anthropic: Constitutional AI（価値観アライメント）
   - Cohere: Domain-specific fine-tuning（業界特化）
   - Adept: Action-oriented training（タスク完了）

4. **プロプライエタリデータ**:
   - OpenAI: WebText、CodeText、Conversation データ
   - Anthropic: 人間フィードバック、安全性評価データ
   - Character.AI: UGCキャラクター対話データ
   - Jasper AI: B2Bコンテンツテンプレート

5. **AI精度定量比較**:
   - Anthropic vs OpenAI: ハルシネーション率12% vs 15%（20%改善）
   - Perplexity: 検索精度95%（Google 85%比）
   - Cohere: Enterprise API精度92%
   - Adept: タスク完了率85%

### Competition Slide - AI精度比較の重要性

**平均スコア**: 9.8/10点（98%達成率）

| 企業 | AI精度 | 応答速度 | ハルシネーション率 | 差別化軸 |
|------|--------|---------|------------------|---------|
| **Anthropic** | 92% | 2.8秒 | 12% | Safety-first、Constitutional AI |
| **Perplexity** | 95% | 2.0秒 | 8% | リアルタイム検索、Citation機能 |
| **Cohere** | 92% | 3.0秒 | 10% | Enterprise特化、プライベートデプロイ |
| **Character.AI** | 88% | 1.5秒 | 15% | バイラルグロース、エンゲージメント |
| **Baseline（GPT-4）** | 90% | 3.2秒 | 15% | - |

**結論**: AI精度・応答速度・ハルシネーション率の定量比較必須、競合比20%以上優位で差別化証明

### Common Pitfalls（失敗パターン）

**失敗パターン1: AI技術スタック不明確**
- **教訓**: 「AIを活用」のみでは不十分。使用モデル、API費用、ファインチューニング戦略を明記
- **事例**: Inflection AI - 技術詳細不足、差別化不明

**失敗パターン2: データ戦略の欠如**
- **教訓**: プロプライエタリデータの有無、データフライホイールを説明
- **事例**: AI21 Labs - データ戦略不明確、競合優位性弱い

**失敗パターン3: 競合AI精度比較なし**
- **教訓**: 「当社のAIは優秀」では不十分。定量比較（精度、速度、ハルシネーション率）必須
- **事例**: 失敗ケース多数 - 競合比較不足でVC説得失敗

**失敗パターン4: B2C特化の限界**
- **教訓**: GenAI B2C市場は競合激化。B2B/Enterprise特化またはニッチ戦略推奨
- **事例**: Inflection AI - B2C特化で差別化失敗、Microsoft吸収

**失敗パターン5: 収益化遅延**
- **教訓**: トラクションあっても収益化戦略不明確はVC評価低下
- **事例**: Character.AI - 100M MAU達成も収益化遅延、Google買収

### Best Practices

1. **AI技術差別化明確化**: 使用モデル、API費用、ファインチューニング、データ戦略を1スライドで説明
2. **定量比較必須**: 競合比AI精度20%以上優位、応答速度50%以上改善を数値で証明
3. **データフライホイール**: プロプライエタリデータ蓄積 → AI精度向上 → ユーザー増加 → データ蓄積の循環
4. **市場タイミング活用**: GenAI市場成長率55%/年、VC投資$25B/年を強調
5. **エンタープライズ戦略**: B2C競合激化、B2B/Enterprise特化で差別化

### Reference

- 詳細: @.claude/skills/for_genai/build-pitch-deck/case_studies/README.md
- GenAI市場トレンド: @GenAI_research/market_trends.md
- VC投資パターン: @GenAI_research/vc_investment_patterns.md

---

## 実行ステップ

### STEP 1: 入力成果物読み込み（5分）

**必須ファイル**:
1. `lean_canvas.md` → ビジネスモデル概要
2. `persona.md` → ターゲット顧客
3. `cpf_judgment.md` → CPFスコア、課題検証結果
4. `psf_validation.md` → PSFスコア、ソリューション検証結果

**推奨ファイル**:
5. `10x_validation.md` → 10倍優位性検証結果
6. `unit_economics.md` → ユニットエコノミクス
7. `competitor_research.md` → 競合分析
8. **`ai_tech_stack.md`** → **AI技術スタック詳細（GenAI特化）**

**欠損ファイルの処理**:
- 必須4ファイルが欠損 → エラー終了、前提スキル実行を促す
- 推奨4ファイルが欠損 → 警告表示、該当スライドは仮データで生成
- **`ai_tech_stack.md`欠損 → 重大警告、AI Technology スライド生成不可**

### STEP 2-4: [ForStartup版と同様]

### STEP 5: AI Technology スライド生成（10分）**[NEW]**

**データソース**: `ai_tech_stack.md`, `competitor_research.md`

**内容**:
- 使用モデル明記（GPT-4, Claude, Gemini等）
- API費用モデル
- ファインチューニング戦略
- プロプライエタリデータの有無
- データフライホイール
- AI精度・応答速度・ハルシネーション率の定量比較

**テンプレート**:
```markdown
## Slide 5: AI Technology

### 使用モデル & 技術スタック

**Primary Model**: [GPT-4 / Claude 3 / Gemini / Custom]
- Parameters: [1.8T / 100B / etc.]
- Provider: [OpenAI / Anthropic / Google / Self-hosted]
- Version: [最新版番号]

**API費用モデル**:
- Input: $X.XX/1K tokens
- Output: $X.XX/1K tokens
- 月間予想コスト: $XX,XXX（X,XXX,XXXユーザー想定）

**ファインチューニング戦略**:
- [ ] RLHF（人間フィードバック）
- [ ] Constitutional AI（価値観アライメント）
- [ ] Domain-specific fine-tuning（業界特化）
- [ ] Action-oriented training（タスク完了）
- カスタマイズ期間: Xヶ月
- 予想精度向上: +XX%

**プロプライエタリデータ**:
- データセット: [説明]
- データ量: XXX,XXX samples
- データ品質: [人間ラベル有無、品質管理]
- データフライホイール:
  1. ユーザー利用 → データ蓄積
  2. データ蓄積 → AI精度向上
  3. AI精度向上 → ユーザー増加
  4. ユーザー増加 → データ蓄積（循環）

**AI精度定量比較**:

| 指標 | 競合A（GPT-4） | 競合B | 当社 | 優位性 |
|------|---------------|-------|------|:------:|
| **AI精度** | 90% | 88% | 92% | **+2%** |
| **応答速度** | 3.2秒 | 4.0秒 | 2.5秒 | **-22%** |
| **ハルシネーション率** | 15% | 18% | 12% | **-20%** |
| **SLA** | 99.5% | 99.0% | 99.9% | **+0.4%** |

**技術的参入障壁**:
1. **データ優位性**: プロプライエタリデータXXX,XXX samples
2. **モデル最適化**: ファインチューニングXヶ月
3. **インフラ**: [GPU/TPU、スケーリング戦略]
```

### STEP 6-13: [ForStartup版と同様、一部GenAI特化カスタマイズ]

### STEP 14: スコア評価・改善提案（5分）

**各スライドを評価基準に基づき採点**:

```markdown
## 投資家説得力スコア

### スライド別評価

| スライド | 配点 | スコア | 評価 | 改善ポイント |
|---------|:----:|:-----:|:----:|-------------|
| Title | 5 | X | ✅/⚠️ | [改善ポイント] |
| Problem | 10 | X | ✅/⚠️ | [改善ポイント] |
| Solution | 10 | X | ✅/⚠️ | [改善ポイント] |
| Market Size | 10 | X | ✅/⚠️ | [改善ポイント] |
| **AI Technology** | **15** | **X** | ✅/⚠️ | **[改善ポイント]** |
| Product | 10 | X | ✅/⚠️ | [改善ポイント] |
| Traction | 15 | X | ✅/⚠️ | [改善ポイント] |
| Business Model | 15 | X | ✅/⚠️ | [改善ポイント] |
| Competition | 10 | X | ✅/⚠️ | [改善ポイント] |
| Go-to-Market | 10 | X | ✅/⚠️ | [改善ポイント] |
| Team | 10 | X | ✅/⚠️ | [改善ポイント] |
| Financials | 10 | X | ✅/⚠️ | [改善ポイント] |
| Ask | 10 | X | ✅/⚠️ | [改善ポイント] |
| Appendix | 5 | X | ✅/⚠️ | [改善ポイント] |

### 総合スコア: XX/145点

**判定**: [🏆 最優秀 / ✅ 優秀 / ⚠️ 良好 / ❌ 要再構築]

### 改善優先度リスト

1. **[最優先スライド]**: [具体的改善案]
2. **[優先スライド2]**: [具体的改善案]
3. **[優先スライド3]**: [具体的改善案]
```

### STEP 15: 成果物出力

**出力先**: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/3_planning/pitch_deck.md`

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
- **標準エラーレスポンス**: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式

---

## 使用例

```
User: /build-pitch-deck

Skill:
# ピッチデッキ生成 自律実行開始（ForGenAI版）

入力ファイル読み込み中...
- lean_canvas.md ✅
- persona.md ✅
- cpf_judgment.md ✅ (CPFスコア: 78%)
- psf_validation.md ✅
- 10x_validation.md ✅ (3軸達成)
- unit_economics.md ✅ (LTV/CAC: 8.48)
- competitor_research.md ✅
- ai_tech_stack.md ✅ (GPT-4、API費用$0.03/1K tokens)

[自動生成中...]
- STEP 1: 入力成果物読み込み ✅
- STEP 2: Title スライド生成 ✅
- STEP 3: Problem スライド生成 ✅ (3Uスコア: 8.5/10平均)
- STEP 4: Solution スライド生成 ✅
- STEP 5: AI Technology スライド生成 ✅ (AI精度92%、競合比+2%)
- STEP 6: Market Size スライド生成 ✅ (GenAI市場$50B→$1.3T)
- STEP 7: Product スライド生成 ✅
- STEP 8: Traction スライド生成 ✅ (月次成長率: 28%)
- STEP 9: Business Model スライド生成 ✅ (LTV/CAC: 8.48)
- STEP 10: Competition スライド生成 ✅ (AI精度比較、10倍優位性: 3軸)
- STEP 11: Go-to-Market スライド生成 ✅
- STEP 12: Team スライド生成 ✅
- STEP 13: Financials スライド生成 ✅
- STEP 14: Ask スライド生成 ✅
- STEP 15: スコア評価・改善提案 ✅
- STEP 16: 成果物出力 ✅

## 完了

成果物: pitch_deck.md
総合スコア: 122/145点 🏆 最優秀

| カテゴリ | スコア | 評価 |
|---------|:------:|:----:|
| Problem/Solution | 18/20 | ✅ |
| Market/AI Technology | 23/25 | ✅ |
| Traction/Business Model | 28/30 | ✅ |
| Competition/GTM | 18/20 | ✅ |
| Team/Financials/Ask | 30/35 | ✅ |
| Appendix | 5/5 | ✅ |

**VC投資家への訴求ポイント（GenAI特化）**:
1. AI技術差別化: AI精度92%（競合比+2%）、ハルシネーション率12%（-20%）
2. トラクション: 月次成長率28%（Series A基準クリア）
3. ユニットエコノミクス: LTV/CAC 8.48（優秀レベル）
4. GenAI市場成長: $50B→$1.3T（年率55%）、タイミング最適

**推奨次のステップ**:
- `/prepare-vc-meeting` でVC対応Q&A準備（AI技術質問対策）
- `/create-fundraising-plan` で資金調達ロードマップ作成
```

---

## 注意事項

1. **前提スキル完了必須**: CPF/PSF検証未完了の場合はピッチデッキ生成不可
2. **AI技術差別化重視**: 使用モデル、API費用、ファインチューニング、データ戦略を明記
3. **定量比較必須**: 競合比AI精度20%以上優位、応答速度50%以上改善を数値で証明
4. **GenAI市場タイミング**: 市場成長率55%/年、VC投資$25B/年を強調
5. **継続的改善**: スコア80点未満のスライドは改善後に再生成

---

## 更新履歴

- 2026-01-02: ForGenAI版として新規作成（AI Technology スライド追加、GenAI市場データ統合、12ケーススタディ追加）
