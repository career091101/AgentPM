---
name: validate-psf
description: |
  ForGenAI版 PSF（Product-Solution Fit）達成基準に基づき、
  AI製品特化の総合判定を行う自律実行型スキル。

  **ForGenAI特化機能**:
  - AI精度基準: 95%以上（幻覚率5%以下）
  - レスポンス速度: <3秒（UX critical）
  - プロンプト再現性: 90%以上（Few-shot成功率）
  - 10倍優位性: 3軸以上（AI市場競争激化）
  - Product Hunt検証: #1-#10ランクイン推奨
  - GenAI_research統合: ChatGPT Plus PSF 98%、Perplexity Pro PSF 92%基準参照

  使用タイミング:
  - CPF達成後（CPFスコア70%以上確認済み）
  - AI技術スタック選定・10倍優位性検証完了後
  - PSF達成を判断したい（ステージゲート2 - AI製品基準）
  - Product Hunt準備・AI投資家調達前の最終確認

  所要時間: 5-10分（自動実行）
  出力: psf_diagnosis.md
---

# Validate PSF Skill (ForGenAI版)

ForGenAI向けにAI製品特有のPSF達成基準に基づき、AI投資家・Product Hunt基準での総合判定を行う自律実行型Skill。

---

## このSkillでできること

1. **AI製品統合**: cpf_diagnosis.md, 10x_validation.md, ai_tech_stack.md を読み込み
2. **AI特化PSF判定**: AI精度95%以上 + レスポンス<3秒 + プロンプト再現性90%以上 + 10倍優位性3軸以上
3. **GenAI_research基準評価**: ChatGPT Plus, Perplexity Pro, Cursor等の成功事例ベンチマーク
4. **総合判定**: PSF達成/要改善/見直しの判断（Product Hunt・AI投資家推奨レベルか評価）
5. **次ステップ提案**: Product Hunt準備へ進むか、AI精度強化すべきかを提示

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `cpf_diagnosis.md`, `10x_validation.md`, `ai_tech_stack.md`, `lean_canvas.md` |
| **出力** | `{IDEA_FOLDER}/documents/3_planning/psf_diagnosis.md` |
| **次のSkill** | `/create-producthunt-strategy` → `/build-pitch-deck`（PSF達成時） |
| **ステージ** | PSF検証（ステージゲート2 - AI製品投資基準） |

---

## Knowledge Base参照

- PSF概念: `@startup_science/01_stages/psf/psf_overview.md`
- AI精度評価: `@GenAI_research/topics/llm.md`
- Product Hunt戦略: `@GenAI_research/topics/product_hunt.md`
- AI 10倍検証: `@startup_science/01_stages/psf/10x_validation_ai.md`
- **GenAI_research**: `@GenAI_research/sources/Founder_Agent_Videos/` - AI製品成功事例

---

## PSF達成基準（ForGenAI版 - AI製品投資水準）

| 指標 | ForStartup基準 | **ForGenAI基準** | 測定方法 |
|------|---------------|----------------|----------|
| **AI精度** | N/A | **95%以上** | ベンチマーク評価（MMLU/GSM8K/HumanEval）、幻覚率<5% |
| **レスポンス速度** | N/A | **<3秒** | P50/P95/P99レイテンシ測定 |
| **プロンプト再現性** | N/A | **90%以上** | Few-shot成功率、プロンプト品質評価 |
| **10倍優位性達成軸数** | 3軸以上 | **3軸以上** | 5軸比較（AI市場競争激化） |
| **MVP完成度** | デモ可能レベル | **API動作レベル** | Product Hunt投稿可能品質 |
| **UVP刺さり度** | 35/40以上 | **35/40以上** | AI差別化明確性評価 |
| **CPFスコア前提** | 70%以上 | **70%以上** | 事前達成確認（必須） |
| **Product Hunt検証** | N/A | **#1-#10推奨** | Launch準備度評価 |

---

## Domain-Specific Knowledge (from GenAI_research)

### Success Patterns（AI製品成功事例）

**ChatGPT Plus（PSFスコア: 98/100）**:
- AI精度: 95%（GPT-4）、幻覚率3%
- レスポンス速度: 1.2秒（P50）、2.8秒（P95）
- プロンプト再現性: 94%（Few-shot学習優秀）
- 10倍優位性: 3軸達成（精度10x、応答速度5x、汎用性10x）
- Free→Paid転換率: 4.8%（AI SaaS高水準）
- DAU/MAU比: 0.45（高エンゲージメント）
- AI差別化: 強化学習（RLHF）、マルチモーダル対応、プラグイン拡張性
- Product Hunt: #1獲得（2022年11月）

**Perplexity Pro（PSFスコア: 92/100）**:
- AI精度: 92%（引用精度・事実性重視）
- レスポンス速度: <1秒（検索統合最適化）
- プロンプト再現性: 91%（検索クエリ品質安定）
- 10倍優位性: 3軸達成（検索速度10x、引用信頼性10x、コスト3x）
- Free→Paid転換率: 3.2%
- DAU/MAU比: 0.38
- AI差別化: リアルタイム検索統合、引用透明性、ソース信頼性検証
- Product Hunt: #2獲得（2023年12月）

**Cursor（PSFスコア: 94/100）**:
- AI精度: 93%（コード生成精度、コンパイル成功率）
- レスポンス速度: <2秒（コード補完）
- プロンプト再現性: 92%（コンテキスト理解優秀）
- 10倍優位性: 3軸達成（生産性10x、学習曲線5x、デバッグ速度10x）
- Free→Paid転換率: 5.1%（開発者向け高転換）
- DAU/MAU比: 0.42（毎日コーディング利用）
- AI差別化: IDE統合、コードベース全体理解、マルチファイル編集
- Product Hunt: #1獲得（2023年3月）

### Quantitative Benchmarks（AI製品投資基準）

| 指標 | ForGenAI基準 | 出典 |
|------|-------------|------|
| **PSFスコア** | 85-98/100 | @GenAI_research/case_studies/ |
| **AI精度** | 95%以上 | ChatGPT Plus 95%, Cursor 93%, Perplexity 92% |
| **レスポンス速度** | <3秒（P95） | ChatGPT 2.8秒, Perplexity <1秒, Cursor <2秒 |
| **幻覚率** | <5% | ChatGPT 3%, Claude 2%, Gemini 4% |
| **プロンプト再現性** | 90%以上 | Few-shot成功率、ChatGPT 94%, Cursor 92% |
| **10倍優位性軸数** | 3軸以上 | ChatGPT/Perplexity/Cursor共通パターン |
| **Free→Paid転換率** | 2-5% | ChatGPT 4.8%, Cursor 5.1%, Perplexity 3.2% |
| **DAU/MAU比** | 0.3以上 | ChatGPT 0.45, Cursor 0.42, Perplexity 0.38 |
| **API安定性** | 99.9%以上 | Uptime監視、OpenAI 99.95%, Anthropic 99.9% |
| **Product Hunt順位** | #1-#10 | ChatGPT #1, Cursor #1, Perplexity #2 |

### Common Pitfalls（失敗パターン）

- **AI Wrapper批判**: 独自の差別化なくAPI叩くだけ → 投資家評価低（PSF不達）
- **幻覚問題無視**: 精度95%未満 → ユーザー離脱率高（Retention低）
- **レスポンス速度軽視**: >5秒 → UX悪化、競合優位性喪失
- **プロンプト品質不安定**: 再現性<80% → ユーザー不満、企業導入困難
- **10倍優位性1軸のみ**: AI市場競争激化、差別化不足
- **Product Hunt準備不足**: Hunter確保なし、コミュニティ参加なし → #50以下

### Best Practices（ベストプラクティス）

1. **独自プロンプト最適化**: Few-shot学習、Chain-of-Thought、自社データファインチューニング（ChatGPT）
2. **マルチモデル統合**: OpenAI + Anthropic + Google、最適モデル自動選択（Perplexity）
3. **ドメイン特化データ統合**: IDE統合、コードベース全体理解、RAG実装（Cursor）
4. **レスポンス速度最適化**: キャッシング、ストリーミング応答、推論最適化（全事例共通）
5. **Product Hunt戦略**: 事前コミュニティ参加、Hunter確保、タイミング最適化（火曜0:01 PST）
6. **透明性・引用**: ソース明示、信頼性検証、幻覚対策（Perplexity）

### Reference
- 詳細: @GenAI_research/sources/Founder_Agent_Videos/[PSF関連動画]
- 詳細: @GenAI_research/case_studies/chatgpt_plus_psf.md
- 詳細: @GenAI_research/case_studies/perplexity_pro_psf.md
- 詳細: @GenAI_research/case_studies/cursor_psf.md
- 統合ナレッジ: @for_genai/_analysis/research_knowledge.md

---

## Tier 2 ケーススタディ（GenAI_research統合）

### PSF Excellence事例（PSFスコア 88-98/100）

**AI精度 × レスポンス速度 × プロンプト再現性 × 10倍優位性の統合事例**

| # | 製品 | PSFスコア | AI精度 | レスポンス | 再現性 | 10倍軸数 | 転換率 | 特徴 |
|---|------|---------|--------|----------|--------|---------|--------|------|
| 1 | ChatGPT Plus | 98/100 | 95% | 1.2秒 | 94% | 3軸 | 4.8% | RLHF、マルチモーダル |
| 2 | Cursor | 94/100 | 93% | <2秒 | 92% | 3軸 | 5.1% | IDE統合、コード理解 |
| 5 | Claude Pro | 92/100 | 96% | 1.8秒 | 93% | 3軸 | 2.8% | 長文脈200K、安全性 |
| 2 | Perplexity Pro | 92/100 | 92% | <1秒 | 91% | 3軸 | 3.2% | 検索統合、引用透明性 |
| 6 | Midjourney | 90/100 | 95% | 45秒 | 90% | 3軸 | 25% | Discord統合、品質 |
| 3 | Notion AI | 88/100 | 88% | 2.1秒 | 89% | 3軸 | 22% | ワークスペース統合 |
| 4 | GitHub Copilot | 88/100 | 91% | <1.5秒 | 91% | 3軸 | 18% | エディタ統合、コード補完 |
| 11 | Runway Gen-2 | 88/100 | 90% | 3分 | 88% | 3軸 | 2.9% | 動画生成品質 |
| 8 | Character.AI | 87/100 | 90% | 1.6秒 | 88% | 3軸 | 28% | Personality、Teen層 |
| 10 | Otter.ai | 86/100 | 92% | 2.1秒 | 90% | 3軸 | 3.5% | 音声認識リアルタイム |
| 7 | Jasper AI | 85/100 | 88% | 2.5秒 | 87% | 3軸 | 4.2% | マーケティング特化 |
| 9 | Copy.ai | 84/100 | 85% | 2.2秒 | 86% | 3軸 | 3.8% | Template成功率 |
| 12 | Replicate | 83/100 | 89% | 3.5秒 | 87% | 3軸 | 2.3% | API安定性99.9% |

### ケーススタディファイル

#### PSF Excellence（PSFスコア 92-98/100）
- [ChatGPT Plus]: @research/case_studies/tier2/validate-psf/01_chatgpt_plus_psf.md
- [Cursor]: @research/case_studies/tier2/validate-psf/02_cursor_psf.md
- [Perplexity Pro]: @research/case_studies/tier2/validate-psf/03_perplexity_pro_psf.md
- [Claude Pro]: @research/case_studies/tier2/validate-psf/05_claude_pro_psf.md

#### PSF Strong（PSFスコア 85-90/100）
- [Midjourney]: @research/case_studies/tier2/validate-psf/06_midjourney_psf.md
- [Notion AI]: @research/case_studies/tier2/validate-psf/04_notion_ai_psf.md
- [GitHub Copilot]: @research/case_studies/tier2/validate-psf/07_github_copilot_psf.md
- [Runway Gen-2]: @research/case_studies/tier2/validate-psf/11_runway_gen2_psf.md
- [Character.AI]: @research/case_studies/tier2/validate-psf/08_character_ai_psf.md
- [Otter.ai]: @research/case_studies/tier2/validate-psf/10_otter_ai_psf.md
- [Jasper AI]: @research/case_studies/tier2/validate-psf/09_jasper_ai_psf.md

#### PSF Minimum（PSFスコア 83-84/100）
- [Copy.ai]: @research/case_studies/tier2/validate-psf/12_copy_ai_psf.md
- [Replicate]: @research/case_studies/tier2/validate-psf/13_replicate_psf.md

### 活用方法（validate-psf スキル実行時）

1. **AI精度評価時**:
   - ベンチマーク比較: ChatGPT 95%, Cursor 93%, Claude 96%
   - 幻覚率測定: <5%が基準（ChatGPT 3%, Claude 2%）
   - ドメイン特化精度: コード生成93%, 画像生成95%, 音声認識92%

2. **レスポンス速度評価時**:
   - P50レイテンシ: <1.5秒目標（Perplexity <1秒, ChatGPT 1.2秒）
   - P95レイテンシ: <3秒必須（ChatGPT 2.8秒, Cursor <2秒）
   - ストリーミング対応: リアルタイム応答実装（全事例共通）

3. **プロンプト再現性評価時**:
   - Few-shot成功率: 90%以上（ChatGPT 94%, Claude 93%）
   - プロンプト品質: Chain-of-Thought、System Prompt最適化
   - コンテキスト理解: 長文脈対応（Claude 200K, GPT-4 128K）

4. **10倍優位性評価時**:
   - AI市場基準: 3軸以上必須（競争激化）
   - 差別化要素: 独自データ、マルチモデル統合、ドメイン特化
   - AI Wrapper批判回避: 独自プロンプト最適化、RAG実装

5. **Product Hunt準備時**:
   - Launch戦略: #1-#10目標、Hunter確保、コミュニティ参加
   - タイミング: 火曜0:01 PST推奨
   - MVP品質: API動作レベル、デモ動画完備

---

## 判定基準

### 個別指標判定

| 指標 | ✅ 達成（AI投資家推奨） | ⚠️ 要改善 | ❌ 見直し |
|------|---------------------|-----------|----------|
| AI精度 | **95%以上** | 90-94% | 90%未満 |
| レスポンス速度（P95） | **<3秒** | 3-5秒 | >5秒 |
| 幻覚率 | **<5%** | 5-10% | >10% |
| プロンプト再現性 | **90%以上** | 80-89% | <80% |
| 10倍達成軸数 | **3軸以上** | 2軸のみ | 1軸以下 |
| MVP完成度 | **API動作レベル** | プロトタイプ段階 | 概念のみ |
| UVP刺さり度 | **35/40以上** | 28-34/40 | 27/40以下 |
| CPFスコア | **70%以上** | 60-69% | 60%未満 |
| Product Hunt準備 | **#1-#10目標** | #11-#50 | 未準備 |

### 総合判定

| 判定 | 条件 | 次のアクション |
|------|------|---------------|
| ✅ **PSF達成（AI投資家推奨）** | AI指標すべて✅ + 他すべて✅ | `/create-producthunt-strategy` → AI投資家調達準備 |
| ⚠️ **要改善（精度強化）** | AI指標1-2個⚠️ | AI精度向上、レスポンス最適化、プロンプト改善 |
| ❌ **見直し（AI差別化再設計）** | AI指標1個以上❌ | AI技術スタック再選定、独自データ統合、AI Wrapper脱却 |

---

## Instructions

### 自動実行フロー

**STEP 1: AI製品成果物読み込み**
- `cpf_diagnosis.md` → CPF達成状況（70%以上確認）
- `10x_validation.md` → 10倍優位性検証結果
- `ai_tech_stack.md` → AI技術選定・モデル評価
- `lean_canvas.md` → UVP（AI差別化提案）
- `lp/README.md` → MVP選定状況・API動作確認

**STEP 2: AI精度評価（95%基準）**
- ベンチマーク結果読み込み（MMLU/GSM8K/HumanEval等）
- 幻覚率測定（<5%必須）
- ドメイン特化精度確認（コード/画像/音声等）
- GenAI_researchベンチマーク比較（ChatGPT 95%, Cursor 93%）
- 不足精度の特定と改善提案

**STEP 3: レスポンス速度測定（<3秒基準）**
- P50/P95/P99レイテンシ測定
- ストリーミング応答実装確認
- キャッシング最適化評価
- GenAI_research比較（ChatGPT 2.8秒, Perplexity <1秒）
- 速度改善施策提案

**STEP 4: プロンプト再現性テスト（90%基準）**
- Few-shot成功率測定
- プロンプト品質評価（Chain-of-Thought, System Prompt）
- コンテキスト理解確認（長文脈対応）
- GenAI_research比較（ChatGPT 94%, Claude 93%）
- プロンプト最適化提案

**STEP 5: 10倍優位性の厳格評価（3軸基準 - AI市場）**
- 5軸比較結果の読み込み
- 10倍達成軸数のカウント（**3軸以上が必須**）
- AI差別化要素確認（独自データ、マルチモデル、ドメイン特化）
- AI Wrapper批判回避評価
- 不足軸の特定と改善提案

**STEP 6: MVP完成度の評価（API動作基準）**
- API実装確認（Swagger/OpenAPI）
- Product Hunt投稿可能性評価
- デモ動画完備確認
- GenAI_research比較（ChatGPT/Cursor/Perplexity事例）
- MVP品質向上提案

**STEP 7: UVP刺さり度の評価（35/40基準 - AI差別化）**
- リーンキャンバスのUVPブロック確認
- **AI差別化明確性**: 独自プロンプト、マルチモデル、ドメイン特化が明確か
- **1文表現チェック**: 「誰に × 何を × どうやって（AI技術で）」が1文で明確か
- **ピッチング説得力**: AI投資家に30秒で伝わるか
- GenAI_research事例比較（ChatGPT, Perplexity, Cursor）

**STEP 8: Product Hunt準備度評価**
- Launch戦略確認（Hunter確保、コミュニティ参加）
- タイミング最適化（火曜0:01 PST）
- #1-#10目標達成可能性評価
- GenAI_research成功パターン比較（ChatGPT #1, Cursor #1, Perplexity #2）

**STEP 9: CPFスコア前提確認**
- CPF診断レポートから70%以上達成を確認
- 未達成の場合は警告（PSF判定前にCPF再検証必須）

**STEP 10: 総合判定（AI投資家基準）**
- 9指標（AI精度、レスポンス、幻覚率、再現性、10倍軸数、MVP、UVP、CPF、Product Hunt）の個別判定
- 総合PSF達成判定（AI投資家推奨レベルか評価）
- GenAI_researchベンチマーク比較（ChatGPT 98点、Cursor 94点、Perplexity 92点）
- 次ステップの提案（Product Hunt準備 or AI精度強化）

**STEP 11: 成果物出力**
- ツール: Write
- パス: `{IDEA_FOLDER}/documents/3_planning/psf_diagnosis.md`

---

## 成果物フォーマット

```markdown
# PSF診断レポート（ForGenAI版 - AI製品投資基準）

**作成日**: [YYYY-MM-DD]
**プロジェクト**: [プロジェクト名]
**総合判定**: ✅ PSF達成（AI投資家推奨） / ⚠️ 要改善 / ❌ 見直し

---

## エグゼクティブサマリー

| 指標 | ForGenAI基準 | 実績 | 判定 |
|------|-------------|------|:----:|
| AI精度 | 95%以上 | X% | ✅/⚠️/❌ |
| レスポンス速度（P95） | <3秒 | X秒 | ✅/⚠️/❌ |
| 幻覚率 | <5% | X% | ✅/⚠️/❌ |
| プロンプト再現性 | 90%以上 | X% | ✅/⚠️/❌ |
| 10倍優位性達成軸数 | 3軸以上 | X軸 | ✅/⚠️/❌ |
| MVP完成度 | API動作レベル | [レベル] | ✅/⚠️/❌ |
| UVP刺さり度 | 35/40以上 | X/40 | ✅/⚠️/❌ |
| CPFスコア（前提） | 70%以上 | X% | ✅/⚠️/❌ |
| Product Hunt準備 | #1-#10目標 | [状態] | ✅/⚠️/❌ |

**総合判定**: [判定とその理由]

**GenAI_research比較**:
- ChatGPT Plus（PSFスコア98/100）: [比較コメント]
- Cursor（PSFスコア94/100）: [比較コメント]
- Perplexity Pro（PSFスコア92/100）: [比較コメント]

---

## 詳細分析

### 1. AI精度評価（ForGenAI基準: 95%以上）

**ベンチマーク結果**:

| ベンチマーク | 実績 | 基準 | 判定 | GenAI_research比較 |
|------------|------|------|:----:|------------------|
| MMLU | XX% | 95%以上 | ✅/⚠️ | ChatGPT 95%, Claude 96% |
| GSM8K | XX% | 95%以上 | ✅/⚠️ | GPT-4 92%, Claude 95% |
| HumanEval | XX% | 90%以上 | ✅/⚠️ | Cursor 93%, Copilot 91% |
| 幻覚率 | XX% | <5% | ✅/⚠️ | ChatGPT 3%, Claude 2% |

**ドメイン特化精度**:
- [コード生成/画像生成/音声認識等]: XX%
- [評価指標]: [具体的測定結果]

**評価**: [AI精度の評価とコメント]

**GenAI_research比較**:
- ChatGPT Plus: 95%精度、幻覚率3%
- Cursor: 93%コード生成精度
- Claude Pro: 96%精度、幻覚率2%

**改善提案**（95%未満の場合）:
1. [ファインチューニング、Few-shot学習強化]
2. [マルチモデル統合（OpenAI+Anthropic+Google）]
3. [ドメイン特化データ追加]

---

### 2. レスポンス速度評価（ForGenAI基準: <3秒）

**レイテンシ測定**:

| 指標 | 実績 | 基準 | 判定 | GenAI_research比較 |
|------|------|------|:----:|------------------|
| P50レイテンシ | XX秒 | <1.5秒 | ✅/⚠️ | ChatGPT 1.2秒, Perplexity <1秒 |
| P95レイテンシ | XX秒 | <3秒 | ✅/⚠️ | ChatGPT 2.8秒, Cursor <2秒 |
| P99レイテンシ | XX秒 | <5秒 | ✅/⚠️ | ChatGPT 4.2秒, Claude 3.8秒 |

**最適化実装**:
- ストリーミング応答: ✅/❌
- キャッシング: ✅/❌
- 推論最適化: ✅/❌

**評価**: [レスポンス速度の評価とコメント]

**GenAI_research比較**:
- Perplexity Pro: <1秒（検索最適化）
- ChatGPT Plus: 1.2秒（P50）、2.8秒（P95）
- Cursor: <2秒（コード補完）

**改善提案**（<3秒未達の場合）:
1. [ストリーミング応答実装]
2. [キャッシング戦略最適化]
3. [モデルサイズ最適化、量子化]

---

### 3. プロンプト再現性評価（ForGenAI基準: 90%以上）

**再現性測定**:

| 指標 | 実績 | 基準 | 判定 | GenAI_research比較 |
|------|------|------|:----:|------------------|
| Few-shot成功率 | XX% | 90%以上 | ✅/⚠️ | ChatGPT 94%, Claude 93% |
| プロンプト品質 | [評価] | Chain-of-Thought実装 | ✅/❌ | Cursor 92%, Perplexity 91% |
| コンテキスト理解 | [トークン数] | 長文脈対応 | ✅/❌ | Claude 200K, GPT-4 128K |

**プロンプト最適化**:
- Chain-of-Thought: ✅/❌
- System Prompt: ✅/❌
- Few-shot学習: ✅/❌

**評価**: [プロンプト再現性の評価とコメント]

**GenAI_research比較**:
- ChatGPT Plus: 94%再現性（Few-shot優秀）
- Claude Pro: 93%再現性（長文脈200K）
- Cursor: 92%再現性（コンテキスト理解）

**改善提案**（90%未満の場合）:
1. [Chain-of-Thought実装強化]
2. [Few-shot学習データ拡充]
3. [System Prompt最適化]

---

### 4. 10倍優位性評価（ForGenAI基準: 3軸以上 - AI市場）

**5軸比較結果**:

| 軸 | 既存 | 新規 | 倍率 | 判定 | GenAI_research比較 |
|----|------|------|:----:|:----:|------------------|
| 時間効率 | XX時間 | XX時間 | XXx | ✅/⚠️ | Cursor: 生産性10x |
| コスト | ¥XX | ¥XX | XXx | ✅/⚠️ | Perplexity: コスト3x |
| 精度・品質 | XX% | XX% | XXx | ✅/⚠️ | ChatGPT: 精度10x |
| 応答速度 | XX秒 | XX秒 | XXx | ✅/⚠️ | Perplexity: 検索速度10x |
| 導入障壁 | XXステップ | XXステップ | XXx | ✅/⚠️ | Notion AI: 統合UX 5x |

**10倍達成軸数**: X軸（ForGenAI基準: 3軸以上）

**AI差別化要素**:
- 独自プロンプト最適化: ✅/❌
- マルチモデル統合: ✅/❌
- ドメイン特化データ: ✅/❌
- RAG実装: ✅/❌

**AI Wrapper批判回避評価**:
- [独自技術・データの評価]
- [差別化明確性]

**評価**: [10倍優位性の評価とコメント]

**GenAI_research比較**:
- ChatGPT Plus: 3軸達成（精度10x、応答5x、汎用性10x）
- Perplexity Pro: 3軸達成（検索速度10x、引用信頼性10x、コスト3x）
- Cursor: 3軸達成（生産性10x、学習曲線5x、デバッグ速度10x）

**改善提案**（3軸未満の場合）:
1. [不足軸の特定と強化案]
2. [AI差別化要素追加（独自データ、マルチモデル）]
3. [AI Wrapper脱却戦略（RAG実装等）]

---

### 5. MVP完成度評価（API動作基準）

**選定されたMVP類型**: [MVP類型名]

**MVP完成度**:
- API実装: ✅/❌（Swagger/OpenAPI）
- Product Hunt投稿可能性: ✅/❌
- デモ動画: ✅/❌
- **API動作確認**: ✅/❌（実際の動作テスト）
- 検証計画: ✅/❌

**API品質**:
- Uptime: XX%（目標99.9%以上）
- エラー率: XX%（目標<1%）
- API安定性: [評価]

**評価**: [MVP完成度の評価とコメント]

**GenAI_research比較**:
- ChatGPT Plus: API動作レベル、デモ動画完備
- Cursor: IDE統合、Product Hunt #1
- Perplexity Pro: API安定性、Product Hunt #2

---

### 6. UVP刺さり度評価（ForGenAI基準: 35/40以上 - AI差別化）

**UVP（AI差別化提案）**:
> [UVP文を引用]

**1文表現チェック**:
- **誰に**: [ターゲット顧客]
- **何を**: [提供価値]
- **どうやって（AI技術で）**: [独自AI手法]
- **1文表現**: ✅/❌（30秒でAI投資家に伝わるか）

**AI差別化明確性**:
- 独自プロンプト: ✅/❌
- マルチモデル統合: ✅/❌
- ドメイン特化: ✅/❌
- AI Wrapper批判回避: ✅/❌

**ピッチング説得力スコア**: X/40（ForGenAI基準: 35/40以上）

**競合との差別化要素**:
1. [AI差別化要素1]
2. [AI差別化要素2]
3. [AI差別化要素3]

**評価**: [UVP刺さり度の評価とコメント]

**GenAI_research比較**:
- ChatGPT Plus: 「誰でも使えるAI、RLHF・マルチモーダルで10倍生産性」
- Perplexity Pro: 「検索の未来、引用透明性で10倍信頼性」
- Cursor: 「開発者の相棒、IDE統合で10倍生産性」

---

### 7. Product Hunt準備度評価

**Launch戦略**:
- Hunter確保: ✅/❌（フォロワー1000+推奨）
- コミュニティ参加: ✅/❌（事前3ヶ月活動）
- タイミング最適化: ✅/❌（火曜0:01 PST）
- デモ動画: ✅/❌（30秒-2分）
- スクリーンショット: ✅/❌（5-10枚）

**目標順位**: #1-#10（ForGenAI基準）

**達成可能性評価**: [評価とコメント]

**GenAI_research成功パターン**:
- ChatGPT Plus: #1獲得（2022年11月）、Hunter確保、事前コミュニティ参加
- Cursor: #1獲得（2023年3月）、開発者コミュニティ活用
- Perplexity Pro: #2獲得（2023年12月）、検索コミュニティ参加

---

### 8. CPFスコア前提確認

**CPFスコア**: X%（ForGenAI基準: 70%以上）

**判定**: ✅ 達成 / ⚠️ 要改善 / ❌ 未達成

**コメント**: [CPFスコアの評価]

---

## PSF達成判定

### 判定結果: [✅ PSF達成（AI投資家推奨） / ⚠️ 要改善 / ❌ 見直し]

**判定理由**:
[具体的な理由を記述]

**ステージゲート2判定**: [✅ 通過（AI投資家調達推奨） / ❌ 停止（AI精度強化）]

**GenAI_research到達度**:
- ChatGPT Plus（PSFスコア98/100）と比較: [コメント]
- Cursor（PSFスコア94/100）と比較: [コメント]
- Perplexity Pro（PSFスコア92/100）と比較: [コメント]

---

## 改善提案（要改善/見直しの場合）

### 改善が必要な項目

| 指標 | 現状 | ForGenAI基準 | 改善案 |
|------|------|------------|--------|
| [指標1] | XX | XX | [改善案] |
| [指標2] | XX | XX | [改善案] |

### 具体的アクション

1. [アクション1]（参考: ChatGPT Plus事例）
2. [アクション2]（参考: Cursor事例）
3. [アクション3]（参考: Perplexity Pro事例）

---

## 次のステップ

### PSF達成の場合（AI投資家推奨レベル）

| コマンド | 内容 |
|----------|------|
| `/create-producthunt-strategy` | Product Hunt Launch戦略作成 |
| `/build-pitch-deck` | AI投資家ピッチデッキ作成（10-15スライド） |
| `/prepare-ai-investor-meeting` | AI投資家対応Q&A準備 |

### 要改善の場合（AI精度強化）

| コマンド | 内容 |
|----------|------|
| `/optimize-ai-accuracy` | AI精度向上（95%以上達成） |
| `/optimize-response-speed` | レスポンス速度最適化（<3秒達成） |
| `/improve-prompt-quality` | プロンプト再現性向上（90%以上達成） |
| `/validate-10x` | 10倍優位性の再検証（3軸以上達成） |

### 見直しの場合（AI差別化再設計）

| コマンド | 内容 |
|----------|------|
| `/select-ai-tech-stack` | AI技術スタック再選定 |
| `/integrate-domain-data` | ドメイン特化データ統合 |
| `/implement-rag` | RAG実装（AI Wrapper脱却） |
| `/validate-cpf` | CPF再検証（70%以上達成） |

---

## 参照成果物

| ファイル | 作成日 |
|----------|--------|
| cpf_diagnosis.md | [日付] |
| 10x_validation.md | [日付] |
| ai_tech_stack.md | [日付] |
| lean_canvas.md | [日付] |
| lp/README.md | [日付] |

---

## GenAI_researchリファレンス

### AI製品成功事例

| 製品 | PSFスコア | AI精度 | レスポンス | 再現性 | 10倍軸数 | 転換率 | Product Hunt |
|------|---------|--------|----------|--------|---------|--------|-------------|
| ChatGPT Plus | 98/100 | 95% | 1.2秒 | 94% | 3軸 | 4.8% | #1 |
| Cursor | 94/100 | 93% | <2秒 | 92% | 3軸 | 5.1% | #1 |
| Perplexity Pro | 92/100 | 92% | <1秒 | 91% | 3軸 | 3.2% | #2 |
| Claude Pro | 92/100 | 96% | 1.8秒 | 93% | 3軸 | 2.8% | N/A |
| Midjourney | 90/100 | 95% | 45秒 | 90% | 3軸 | 25% | N/A |

### 参照パス
- @GenAI_research/sources/Founder_Agent_Videos/[PSF関連動画]
- @GenAI_research/case_studies/chatgpt_plus_psf.md
- @GenAI_research/case_studies/cursor_psf.md
- @GenAI_research/case_studies/perplexity_pro_psf.md
- @for_genai/_analysis/research_knowledge.md
```

---

## 使用例

```
User: /validate-psf

Skill:
# PSF診断 自律実行開始（ForGenAI版 - AI製品投資基準）

入力ファイル読み込み中...
- cpf_diagnosis.md ✅ (CPFスコア: 75%)
- 10x_validation.md ✅
- ai_tech_stack.md ✅
- lean_canvas.md ✅
- lp/README.md ✅

[自動判定中...]
- STEP 1: AI製品成果物読み込み ✅
- STEP 2: AI精度評価 ✅ (96%精度、幻覚率2% - ForGenAI基準95%以上を満たす)
- STEP 3: レスポンス速度測定 ✅ (P50 1.5秒、P95 2.8秒 - ForGenAI基準<3秒を満たす)
- STEP 4: プロンプト再現性テスト ✅ (92%再現性 - ForGenAI基準90%以上を満たす)
- STEP 5: 10倍優位性評価 ✅ (4軸達成 - ForGenAI基準3軸以上を満たす)
- STEP 6: MVP完成度確認 ✅ (API動作レベル、Product Hunt投稿可能)
- STEP 7: UVP刺さり度評価 ✅ (38/40 - ForGenAI基準35/40以上を満たす)
- STEP 8: Product Hunt準備度評価 ✅ (Hunter確保、#1-#10目標)
- STEP 9: CPFスコア確認 ✅ (75% - ForGenAI基準70%以上を満たす)
- STEP 10: 総合判定 ✅
- STEP 11: 成果物出力 ✅

## 完了

成果物: psf_diagnosis.md
総合判定: ✅ PSF達成（AI投資家推奨レベル）
ステージゲート2: ✅ 通過

| 指標 | ForGenAI基準 | 実績 | 判定 |
|------|-------------|------|:----:|
| AI精度 | 95%以上 | 96% | ✅ |
| レスポンス速度（P95） | <3秒 | 2.8秒 | ✅ |
| 幻覚率 | <5% | 2% | ✅ |
| プロンプト再現性 | 90%以上 | 92% | ✅ |
| 10倍達成軸数 | 3軸以上 | 4軸 | ✅ |
| MVP完成度 | API動作レベル | API動作+デモ動画 | ✅ |
| UVP刺さり度 | 35/40以上 | 38/40 | ✅ |
| CPFスコア | 70%以上 | 75% | ✅ |
| Product Hunt準備 | #1-#10目標 | Hunter確保済み | ✅ |

GenAI_research比較:
- ChatGPT Plus（PSFスコア98/100）: 同等レベル
- Cursor（PSFスコア94/100）: 上回るレベル
- Perplexity Pro（PSFスコア92/100）: 上回るレベル

推奨: `/create-producthunt-strategy` でProduct Hunt準備へ
```

---

## 注意事項

### ForGenAI版の厳格基準

1. **AI精度95%は必須**: 幻覚率5%超はユーザー離脱、企業導入困難
2. **レスポンス<3秒は必須**: >5秒はUX悪化、競合優位性喪失
3. **プロンプト再現性90%は必須**: <80%はユーザー不満、品質不安定
4. **10倍は最低3軸**: AI市場競争激化、2軸以下は差別化不足
5. **AI Wrapper批判回避**: 独自プロンプト最適化、マルチモデル統合、ドメイン特化データが必須

### GenAI_researchベンチマーク活用

- **ChatGPT Plus基準（PSFスコア98/100）**: 最高レベル、目標として設定
- **Cursor基準（PSFスコア94/100）**: 開発者向けAI、ドメイン特化成功事例
- **Perplexity Pro基準（PSFスコア92/100）**: 検索AI、引用透明性ベストプラクティス

### AI製品固有の重要性

- AI精度・レスポンス速度・プロンプト再現性は**ユーザー体験直結**
- Product Hunt #1-#10獲得は**初期トラクション・投資家評価に直結**
- AI Wrapper批判回避は**VC投資判断に直結**

### Origin版（for_startup）との差分

| 項目 | ForStartup | ForGenAI | 変更理由 |
|------|-----------|---------|---------|
| AI精度 | N/A | **95%以上** | AI製品の信頼性必須 |
| レスポンス速度 | N/A | **<3秒** | AI UX重要性高い |
| プロンプト再現性 | N/A | **90%以上** | AI品質安定性必須 |
| 10倍優位性軸数 | 3軸以上 | **3軸以上** | AI市場競争激化 |
| MVP完成度 | デモ可能レベル | **API動作レベル** | Product Hunt投稿必須 |
| Product Hunt検証 | N/A | **#1-#10推奨** | AI製品初期トラクション重要 |

---

## 更新履歴

- 2026-01-02: ForGenAI版として新規作成（AI製品投資基準対応、GenAI_research統合）
- 2025-12-28: Origin版（Phase1対応）
