---
name: research-problem-for-genai
description: |
  ForGenAI特化版: Web上の生ログから課題の裏付けを発見する自律実行型スキル。Reddit、Hacker News、X、Product Hunt等から「困りごと」を30件以上収集し、5軸（頻度/深刻度/既存策不満/支払い匂い/緊急性）で50点満点スコアリング。定性インサイト抽出、既存代替案分析を実施し、課題仮説の裏付けを判定します。

  ForGenAI固有の特徴:
  - AI技術動向統合（最新LLMモデル、エージェントフレームワーク、ベクトルDB）
  - AI導入障壁分析（技術的ハードル、コスト、精度不足）
  - 既存AI製品の不足分析（汎用すぎ、精度低い、高コスト）
  - 新技術機会評価（マルチモーダル、エージェント、オンデバイスAI）
  - CPF基準: 70%以上（ForRecruit 50%より厳格、AI市場競争激しい）

  使用タイミング：
  - リーンキャンバス作成後
  - 課題仮説の裏付けを確認したい
  - CPF検証の補強材料が欲しい（AI市場特化）

  所要時間：30-60分（自動実行）
  出力：problem_research.md
---

# Research Problem Skill (ForGenAI Edition)

Web上の生ログから課題の裏付けを発見する自律実行型Skill。**ForGenAI特化版**では、AI技術動向と既存AI製品の不足分析を統合し、生成AI市場特化の課題検証を行います。

---

## このSkillでできること

1. **生ログ収集**: Reddit/Hacker News/X/Product Hunt/Stack Overflow等から「困りごと」を収集
2. **5軸スコアリング**: 頻度/深刻度/既存策不満/支払い匂い/緊急性で評価（50点満点）
3. **定性インサイト抽出**: 生の声から本質的課題を発見
4. **既存代替案分析**: 何が使われていて、何が不満か
5. **課題裏付け判定**: 仮説が正しいかを判定
6. **ForGenAI適合性評価**: AI技術動向、既存AI製品の不足、新技術機会を評価

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `persona.md`（必須）, `lean_canvas.md`（オプション） |
| **フォールバック** | persona.md未存在時 → demand_discovery.mdから課題情報を取得 |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/2_discovery/problem_research.md` |
| **次のSkill** | `/for-genai-validate-cpf` |
| **ステージ** | CPF検証（生成AI市場特化） |

---

## ForGenAI固有の評価基準

### 課題検証基準（厳格化版）

| 指標 | Origin基準 | ForGenAI基準 | 理由 |
|------|----------|-------------|------|
| インタビュー数 | 20人以上 | **20人以上** | AI市場競争激しく、十分な検証が必要 |
| 課題共通率 | 70%以上 | **70%以上** | 差別化が困難、明確な課題が必須 |
| 緊急性スコア | 7/10以上 | **7/10以上** | AI技術の陳腐化リスクが高い、早期解決ニーズ重要 |

### AI技術動向統合

#### 調査対象
1. **最新LLMモデル**: GPT-4 Turbo, Claude 3.5 Sonnet, Gemini 1.5 Pro, Llama 3
2. **エージェントフレームワーク**: LangChain, AutoGPT, CrewAI, LlamaIndex
3. **ベクトルDB**: Pinecone, Weaviate, ChromaDB, Qdrant
4. **AI市場レポート**: Gartner, McKinsey, a16z AI Report, NVIDIA AI Insights

#### 課題分析の追加軸
- **AI導入障壁**: 技術的ハードル（プロンプトエンジニアリング難しい）、コスト（API料金高額）、精度不足（ハルシネーション）
- **既存AI製品の不足**: 汎用すぎ（ドメイン特化が必要）、精度低い（ファインチューニング未対応）、高コスト（月額$20+）
- **新技術機会**: マルチモーダル（画像+テキスト）、エージェント（自律タスク実行）、オンデバイスAI（プライバシー保護）

---

## Domain-Specific Knowledge (from GenAI_research)

### Success Patterns（課題検証成功事例）

1. **Perplexity（検索AI）**:
   - **課題**: Google検索の情報過多・信頼性不足
   - **課題共通率**: 75%（推定、AI活用ユーザー）
   - **検証手法**: Hacker News、Reddit（r/MachineLearning）での声収集50件
   - **インタビュー数**: 30回（推定、テックコミュニティ中心）
   - **成果**: 月間1,000万ユーザー、検索精度でGoogle比1.5倍（ユーザー評価）

2. **Jasper（コンテンツ生成AI）**:
   - **課題**: マーケティングコンテンツ作成の時間コスト（1記事3-5時間）
   - **課題共通率**: 80%（マーケター対象）
   - **検証手法**: マーケターインタビュー100回、ベータテスト
   - **インタビュー数**: 100回
   - **成果**: 月額$99プラン、10万ユーザー突破、ファインチューニングで精度92%達成

3. **Midjourney（画像生成AI）**:
   - **課題**: デザイナー不在の中小企業・個人クリエイターの画像制作難
   - **課題共通率**: 70%（推定、非デザイナー層）
   - **検証手法**: Discord統合でユーザーフィードバック収集（1日1,000件以上）
   - **インタビュー数**: 推定50回（初期ベータユーザー）
   - **成果**: 1,500万ユーザー、Discord統合でRetention 60%

4. **ChatGPT**:
   - **課題**: 情報検索・文章作成の効率化（検索→要約の2ステップ削減）
   - **課題共通率**: 85%（推定、ナレッジワーカー全般）
   - **検証手法**: OpenAI内部ユーザーテスト、段階的公開
   - **インタビュー数**: 推定100回（内部テスト）
   - **成果**: 史上最速1億ユーザー達成（2ヶ月）、バイラル係数3.0

5. **Grammarly（AI文章校正）**:
   - **課題**: 英語非ネイティブの文章品質向上（スペルミス、文法ミス）
   - **課題共通率**: 80%（英語非ネイティブ）
   - **検証手法**: 大学生・ビジネスパーソンインタビュー50回
   - **インタビュー数**: 50回
   - **成果**: 月間3,000万アクティブユーザー、Freemium転換率15%

### Common Pitfalls（失敗パターン）

1. **汎用AI製品の失敗**:
   - **失敗要因**: 課題が広すぎて差別化不可、ChatGPTで代替可能
   - **教訓**: ドメイン特化が必須、「ChatGPTで十分」と言われたら終わり
   - **ForGenAI教訓**: 10倍優位性の3軸（精度・速度・コスト）で差別化必須

2. **ハルシネーション対策不足**:
   - **失敗要因**: AI誤情報生成（ハルシネーション）への対策なし、信頼性低下
   - **教訓**: RAG（Retrieval-Augmented Generation）、ファクトチェック機構必須
   - **ForGenAI教訓**: 精度90%以上を保証する仕組みが必要

3. **API料金コスト倒れ**:
   - **失敗要因**: OpenAI API料金がユーザー課金を上回る、収益性崩壊
   - **教訓**: Unit Economics厳密計算、API料金20%以内に抑制
   - **ForGenAI教訓**: ファインチューニング・小型モデル活用でコスト削減

### Quantitative Benchmarks

- **課題共通率**: 成功AI製品平均78.0%、ForGenAI推奨: **70%以上**
- **User Research Count**: 成功AI製品平均66.0回、ForGenAI推奨: **20回以上**
- **Product Hunt実績**: Top 5達成率60%（成功AI製品）
- **検証期間**: 成功AI製品平均1-2ヶ月、ForGenAI推奨: **1-2ヶ月以内にCPF判断**

### Reference

- 詳細: @GenAI_research/problem_analysis/ai_adoption_barriers.md
- 統合分析: @GenAI_research/case_studies/ai_product_success_patterns.md

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-60分

### 自動実行ステップ

1. リーンキャンバス・ペルソナ読み込み
2. 検索クエリ生成（日本語・英語各10個以上）
3. 生ログ収集（日本語圏30件以上）
4. 生ログ収集（英語圏30件以上）
5. **AI技術動向調査（追加）**
6. 5軸スコアリング
7. 定性インサイト抽出
8. 既存代替案分析（既存AI製品含む）
9. 課題裏付け判定
10. **ForGenAI適合性評価（追加）**
11. 成果物出力

### 5軸スコアリング基準（50点満点）

| 項目 | 10点 | 6-9点 | 3-5点 | 0-2点 |
|------|------|-------|-------|-------|
| **頻度** | 同様の声10件以上 | 5-9件 | 2-4件 | 1件以下 |
| **深刻度** | 「困り果てている」「限界」 | 「困っている」 | 「できれば解決したい」 | 「別にいい」 |
| **既存策不満** | 「ChatGPTでは不十分」多数 | 不満の声多い | 一部不満あり | 概ね満足 |
| **支払い匂い** | 「月額$50払ってでも」発言あり | 時間・労力コスト言及 | コスト意識なし | 無料希望明確 |
| **緊急性** | 「今すぐ」「早く」多数 | 「近いうちに」 | 「いつか」 | 急がない |

### 判定基準（ForGenAI調整版）

**総合判定**:
- 40-50点: ✅ 強い裏付け → CPF検証へ進む
- **30-39点**: ⚠️ 中程度の裏付け → **Product Hunt戦略検討**（ForGenAI推奨）
- **25-29点**: ⚠️ 弱い裏付け → ニッチ化または追加検証
- 0-24点: ❌ 裏付け不足 → 課題仮説見直し

**起業の科学CPF基準との対応**:
- スコア40点以上 → CPF検証の補強材料として有効
- スコア30-39点 → **Product Huntで初期ユーザー獲得**（ForGenAI推奨）
- スコア25-29点 → 追加インタビューで深堀り、またはニッチ化検討
- スコア24点以下 → 課題仮説の根本見直し、`/for-genai-discover-demand`で別課題を探索

**次ステップへの連携（ForGenAI調整版）**:
| スコア | 次のアクション |
|:------:|---------------|
| 40点以上 | `/for-genai-validate-cpf` で総合判定へ |
| 30-39点 | **Product Hunt戦略策定**（`/for-genai-create-producthunt-strategy`） |
| 25-29点 | `/for-genai-simulate-interview` で追加検証 |
| 24点以下 | `/for-genai-discover-demand` で別課題を探索 |

### ForGenAI適合性評価（追加ステップ）

課題について、以下を評価:

| 評価項目 | 評価基準 | 配点 |
|---------|---------|------|
| **AI技術適合性** | 最新LLMモデル・エージェントフレームワークで解決可能か | 7点満点 |
| **差別化可能性** | 既存AI製品（ChatGPT等）より10倍優れているか | 5点満点 |
| **技術実現可能性** | ファインチューニング・RAG等で精度90%以上達成可能か | 3点満点 |
| **コスト最適化** | API料金をユーザー課金の20%以内に抑制可能か | 3点満点 |
| **Product Hunt適合性** | テックコミュニティで注目される課題か | 2点満点 |

**ForGenAI適合性スコア**: 20点満点
- 15点以上: ✅ AI技術活用の好機、Product Huntローンチ推奨
- 10-14点: ⚠️ 一部技術課題あり、技術検証と併用
- 9点以下: ❌ AI技術活用困難、Origin基準で再評価

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **WebSearch失敗**: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @startup_science/01_stages/cpf/cpf_overview.md
- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/customer_interview.md
- @startup_science/01_stages/cpf/persona_creation.md
- @.claude/skills/_shared/skill_chains.md
- @.claude/skills/_shared/error_handling_patterns.md
- **@GenAI_research/problem_analysis/ai_adoption_barriers.md**
- **@GenAI_research/case_studies/ai_product_success_patterns.md**

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
- Perplexity事例: @GenAI_research/case_studies/success/perplexity_search_ai.md
- Jasper事例: @GenAI_research/case_studies/success/jasper_content_generation.md

### 全体参照
- ForGenAI全体概要: @.claude/skills/_shared/knowledge_base.md#forgenai-edition
- AI技術動向: @GenAI_research/technology_trends/
- AI倫理対応: @.claude/skills/_shared/knowledge_base.md#ai-ethics

---

## 使用例

```
User: /for-genai-research-problem

Skill:
# 課題リサーチ 自律実行開始（ForGenAI Edition）

[persona.md読み込み]
ペルソナ: AI活用マーケター
課題: コンテンツ生成の時間コスト（1記事3-5時間）

[自動実行中...]
- STEP 1: リーンキャンバス・ペルソナ読み込み ✅
- STEP 2: 検索クエリ生成 ✅ (日本語10個、英語10個)
- STEP 3: 日本語圏生ログ収集 ✅ (35件)
- STEP 4: 英語圏生ログ収集 ✅ (42件)
- STEP 5: AI技術動向調査 ✅ (最新LLMモデル比較)
- STEP 6: 5軸スコアリング ✅
- STEP 7: 定性インサイト抽出 ✅
- STEP 8: 既存代替案分析 ✅ (ChatGPT、Jasper、Copy.ai比較)
- STEP 9: 課題裏付け判定 ✅
- STEP 10: ForGenAI適合性評価 ✅
- STEP 11: 成果物出力 ✅

## 完了

成果物: problem_research.md
課題スコア: 42/50点（✅ 強い裏付け）
ForGenAI適合性: 18/20点（✅ AI技術活用の好機）

AI技術動向:
- 最新LLMモデル: GPT-4 Turbo（精度92%）、Claude 3.5 Sonnet（長文処理強い）
- エージェントフレームワーク: LangChain（エコシステム広い）、CrewAI（マルチエージェント特化）
- ベクトルDB: Pinecone（高速）、Weaviate（オープンソース）

既存AI製品の不足:
- ChatGPT: 汎用すぎ、マーケティング特化ではない
- Jasper: 月額$99高コスト、中小企業には高額
- Copy.ai: 精度85%、ファインチューニング未対応

技術機会:
- ファインチューニングで精度92%→95%達成可能（Jasper事例）
- RAGでハルシネーション削減、事実確認強化
- オンプレミスLLM活用でAPI料金削減（20%→5%）

推奨: `/for-genai-validate-cpf` で総合判定へ
Product Hunt戦略: テックマーケター向けローンチ
```

---

**テンプレートバージョン**: v3.1-ForGenAI
**最終更新**: 2026-01-03
**作成者**: Claude Code
**ForGenAI特化要素**: 5件のAI製品成功事例統合、AI技術動向調査追加、適合性評価基準追加、Product Hunt連携
