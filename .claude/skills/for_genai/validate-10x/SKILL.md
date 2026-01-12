---
name: validate-10x-for-genai
description: |
  ForGenAI特化版: 既存代替案と比較して10倍優位性を検証する自律実行型スキル。AI市場における3軸必須（精度、速度、コスト）での10倍優位性をChatGPT/Claude/Gemini比較で評価。GenAI_Research 12件のAI製品成功パターン（Perplexity AI精度10倍、Midjourney品質10倍、GitHub Copilot速度10倍等）を統合。

  ForGenAI固有の特徴:
  - 10倍優位性軸数: 2軸以上 → 3軸必須（AI差別化軸: 精度、速度、コスト）
  - LLM競合比較: ChatGPT/Claude/Gemini との定量比較必須
  - プロンプト品質評価: Chain-of-Thought、Few-shot等のパターン評価
  - GenAI_Research統合（12件の成功事例、失敗教訓）

  使用タイミング:
  - リーンキャンバス作成後
  - PSF検証の一環として
  - Product Hunt準備前の競合優位性確認

  所要時間: 50-80分（自動実行）
  出力: 10x_validation_forgenai.md
---

# Validate 10x Skill (ForGenAI Edition)

既存代替案と比較して10倍優位性を検証する自律実行型Skill（ForGenAI特化版）。GenAI_Research 12件から抽出した10倍優位性パターン（Perplexity AI精度10倍、Midjourney品質10倍、GitHub Copilot速度10倍、ElevenLabs音声合成10倍等）を統合し、AI市場の厳格基準（3軸必須）に準拠した判定を実施。

---

## このSkillでできること

1. **競合・代替案の特定**: ChatGPT/Claude/Gemini等の直接競合、間接競合、既存対処法を洗い出し
2. **9軸比較**: 精度/速度/コスト/使いやすさ/プロンプト品質/Fine-tuning/RAG/API料金/レスポンス時間で定量比較
3. **10倍判定（ForGenAI基準）**: 3軸以上で10倍優位性があるか判定（AI市場必須条件）
4. **LLM競合比較**: ChatGPT/Claude/Gemini との定量比較（API料金、精度、速度）
5. **プロンプトパターン評価**: Chain-of-Thought、Few-shot、Self-Consistency等の品質評価
6. **改善アクション策定**: 未達成軸の改善案を提示
7. **GenAI_Researchベンチマーク**: 12件の成功事例との比較

---

## Domain-Specific Knowledge (from GenAI_Research)

### Success Patterns

#### 1. Perplexity AI - 精度10倍優位性（Citation機能）

**10倍優位性パターン**:
- **精度軸**: Hallucination削減（引用元明示により信頼性10倍向上）
- **速度軸**: Google検索より5倍高速（複数検索→集約の時間削減）
- **コスト軸**: 無料プラン提供（Google検索と同等）

**結果**:
- CPFスコア 85%
- Product Hunt #1獲得（2023年12月）
- ARR $20M（2024年推定）
- 出典: @GenAI_research/LLM/01_LifeisBeautiful_insights.md

**ForGenAI教訓**:
- Citation機能が精度差別化の決定打（引用元明示で信頼性10倍）
- Hallucination削減は定量評価可能（引用ミス率 vs ChatGPT）
- Google検索の不満解消（広告多い、引用元不明）が需要源泉

#### 2. Midjourney - 画像品質10倍優位性

**10倍優位性パターン**:
- **品質軸**: 画像クオリティ10倍（Stable Diffusionの10倍の解像度・ディテール）
- **速度軸**: 生成時間5倍高速（30秒 vs Stable Diffusion 150秒）
- **コスト軸**: 月額$10-60（デザイナー外注$500-5,000の1/50〜1/500）

**結果**:
- CPFスコア 90%
- 月額売上$200M（2024年推定）
- Discord経由で爆発的成長（Product Hunt未ローンチ）

**ForGenAI教訓**:
- 画像品質の視覚的優位性が決定打（ブラインドテストで10倍評価）
- Discord コミュニティ戦略（Product Huntなしで成長可能）
- デザイナー外注コスト削減が明確なROI

#### 3. GitHub Copilot - コード生成速度10倍優位性

**10倍優位性パターン**:
- **速度軸**: コーディング速度10倍（単純コード生成で開発時間1/10）
- **精度軸**: コード正確性8倍（コンパイルエラー率 vs 人間初心者）
- **コスト軸**: 月額$10（ジュニアエンジニア外注$2,000-5,000の1/200〜1/500）

**結果**:
- CPFスコア 88%
- $10/月で収益化成功
- GitHub既存ユーザー基盤活用（初期トラクション獲得）

**ForGenAI教訓**:
- 開発速度10倍は定量測定可能（タスク完了時間比較）
- 既存エコシステム統合が初期トラクション獲得の鍵
- ジュニアエンジニア代替という明確な価値提案

### Quantitative Benchmarks

#### 10倍優位性の評価軸（GenAI特化）

| 優位性軸 | 定義 | ベンチマーク | 代表製品 |
|---------|------|------------|---------|
| **精度（Accuracy）** | Hallucination削減、Citation精度、MOS評価 | 10倍 | Perplexity AI（Citation）、ElevenLabs（MOS 4.8 vs 3.5） |
| **速度（Speed）** | API応答時間、生成時間、タスク完了時間 | 5-10倍 | GitHub Copilot（開発速度10倍）、Midjourney（生成時間5倍） |
| **コスト（Cost）** | API料金、月額料金、外注代替コスト | 10-500倍 | GitHub Copilot（外注1/200〜1/500）、Midjourney（デザイナー1/50〜1/500） |
| **プロンプト品質** | Chain-of-Thought、Few-shot、Self-Consistency等のパターン活用 | 3-5倍 | 独自プロンプトテンプレート活用製品 |
| **Fine-tuning** | ドメイン特化Fine-tuning、カスタムモデル | 2-5倍 | Jasper AI（マーケティング特化Fine-tuning） |
| **RAG活用** | 外部知識統合、リアルタイムデータ取得 | 3-5倍 | Perplexity AI（検索結果RAG統合） |
| **API料金削減** | 効率化技術によるAPI料金削減 | 10倍 | Gemini活用（$0.001/1K vs GPT-4 $0.03/1K） |

#### 10倍優位性軸数と成功率（GenAI市場）

| 軸数 | 成功率 | CPFスコア | 代表製品 |
|------|--------|---------|---------|
| **3軸以上** | 90-100% | 85-95% | Perplexity AI、Midjourney、GitHub Copilot |
| **2軸** | 60-80% | 75-85% | Jasper AI、Notion AI |
| **1軸** | 30-50% | 60-75% | ChatGPT Wrapper系（失敗リスク高） |
| **0軸** | 0-10% | 40-60% | 汎用LLM APIのみ使用（ほぼ失敗） |

**ForGenAI基準**:
- **3軸以上**: CPF 70%以上合格、Product Hunt #1-3狙い
- **2軸**: 要改善、AI差別化軸の強化必須
- **1軸以下**: AI優位性の再設計必須

---

## 注意事項

1. **ForGenAI特化調整**:
   - 10倍優位性3軸以上必須（Origin版は2軸以上）
   - AI差別化軸を追加評価（精度、速度、コスト、プロンプト品質、Fine-tuning、RAG）
   - ChatGPT/Claude/Gemini との定量比較必須

2. **AI差別化3軸の重要性**:
   - 精度軸: Hallucination削減、Citation精度、MOS評価
   - 速度軸: API応答時間、生成時間、タスク完了時間
   - コスト軸: API料金削減、外注代替コスト

3. **LLM競合比較の徹底**:
   - API料金: $0.001-0.03/1K tokens（10-60倍差）
   - 精度: MMLU 85-89%（2-4%差）
   - 速度: 30-70 tokens/sec（2-3倍差）

---

## 更新履歴

- 2026-01-03: ForGenAI特化版として新規作成、GenAI_Research 12製品分析統合
- AI差別化3軸必須（精度、速度、コスト）
- LLM競合比較追加（ChatGPT/Claude/Gemini）
- プロンプトパターン評価追加（Chain-of-Thought、Few-shot、Self-Consistency）

