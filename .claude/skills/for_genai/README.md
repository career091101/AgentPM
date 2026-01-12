# Founder Agent - ForGenAI（生成AI特化版）

**バージョン**: 1.0
**最終更新**: 2026-01-03
**ベース**: Founder Agent Origin + AI技術スタック選定・Product Hunt戦略最適化

---

## 概要

Founder Agent ForGenAIは、生成AI製品開発に特化した創業支援エージェントです。LLMプロバイダー選定、プロンプト最適化、Product Hunt戦略、プレローンチコミュニティ構築、AI競合分析、モデル更新追跡など、AI製品特有の課題に対応する6つの新規スキルを含む22スキルを提供します。

---

## 対象ユーザー

- 生成AI製品を開発する創業者・起業家
- ChatGPT等の既存AI製品と差別化するプロダクト開発者
- AI技術スタック選定・コスト最適化が必要な方
- Product Huntローンチを計画しているAI製品開発者
- 最新LLMモデル動向を追跡したい開発者

---

## Originとの主な違い

### 1. AI製品特化の評価基準

| 基準 | Origin | ForGenAI | 理由 |
|------|--------|----------|------|
| **CPFスコア** | 60%以上 | **70%以上** | AI市場は競争が激しく、高い課題の切実度が必要 |
| **10倍優位性** | 2軸以上 | **3軸以上** | ChatGPT等の既存製品との差別化が必須 |
| **技術的差別化** | 機能差 | **モデル精度・速度・コストの定量比較** | AI製品は技術的優位性が重要 |

### 2. 追加フレームワーク（AI製品特化）

- **AI技術スタック選定** - OpenAI vs Anthropic vs Gemini、Vector DB選択、Orchestration層
- **Product Hunt戦略** - AI製品特化のLaunch timing、Hunter選定、デモ動画作成
- **プロンプト品質最適化** - Chain-of-Thought、Few-shot、Structured output
- **AI競合分析** - ChatGPT等との差別化、ベンチマーク比較
- **モデル更新追跡** - GPT-4o、Claude 3.7等の月次更新対応

### 3. GenAI_research統合

**統合ナレッジソース**:
- `GenAI_research/LLM/01_LifeisBeautiful_insights.md` - AIトレンド、モデル進化の方向性
- `GenAI_research/technologies/` - OpenAI、Anthropic、Google、LangChain、LlamaIndex
- `GenAI_research/topics/` - Prompt Engineering、LLM、RAG、Agents
- `GenAI_research/case_studies/` - Perplexity、Cursor、Notion AI、Jasper、Character.AI等60件

**主要洞察**:
- **モデル進化**: 強化学習による「考える力」獲得、コモディティ化トレンド
- **コスト最適化**: ジェボンズのパラドックス、マルチLLM戦略で40%削減
- **プロダクト置き換え**: SaaS→エージェント、UI/ビジネスロジック置換
- **Product Hunt**: Cursor CAC 1/3.4削減（$12→$3.5）、#1獲得効果

---

## 特化機能（AI製品特化スキル5件）

### 1. AI技術スタック選定（/select-ai-tech-stack）

**目的**: OpenAI vs Anthropic vs Gemini比較、最適技術スタック選定

**主要機能**:
- LLMプロバイダー比較（コスト、精度、レイテンシ、コンテキスト長）
- Vector DB選択（Pinecone vs Weaviate vs Chroma）
- Orchestration層（LangChain vs LlamaIndex vs Custom）
- 推論コスト試算式、スケーラビリティ評価（10万→100万ユーザー）

**Tier 2ケーススタディ**（12件）:
- Perplexity LLM移行（OpenAI→マルチプロバイダー、コスト40%削減）
- Cursor Anthropic選定（Claude 3.5 Sonnet、コーディング精度95%）
- Notion AI RAG構成（GPT-4 + Pinecone、検索精度95%）
- その他9件

---

### 2. Product Hunt戦略立案（/create-producthunt-strategy）

**目的**: Product Hunt #1獲得戦略立案

**主要機能**:
- Launch timing最適化（火曜 12:01 AM PT推奨）
- Hunter選定基準（AI領域influencer、フォロワー10K+）
- Community engagement戦略（Hacker News、r/MachineLearning、AI Discord）
- デモ動画・GIF作成ベストプラクティス
- 初動200+ upvotes達成手法

**Tier 2ケーススタディ**（12件）:
- ChatGPT PH #1獲得（24時間で10K+ upvotes）
- Perplexity Launch戦略（Naval Ravikant Hunter、初動500 upvotes）
- Midjourney Visual戦略（デモ動画10M再生、#1達成）
- その他9件

**CAC低減効果**: #1獲得でCAC 1/2-1/3削減（Cursor事例: $12→$3.5）

---

### 3. プロンプト品質最適化（/optimize-prompt-quality）

**目的**: Chain-of-Thought、Few-shot等のプロンプト品質最適化

**主要機能**:
- Chain-of-Thought適用パターン
- Few-shot examples設計
- System message最適化
- Structured output (JSON mode)
- 再現性90%+達成手法、レスポンス速度<3秒最適化

**Tier 2ケーススタディ**（12件）:
- Anthropic Claude Prompt最適化（Constitutional AI、Chain-of-Thought標準化）
- OpenAI GPT-4 Best Practice（System message設計、Few-shot examples）
- Perplexity 検索プロンプト（引用生成、ファクトチェック）
- その他9件

---

### 4. AI競合分析（/analyze-ai-competitors）

**目的**: AI競合製品分析フレームワーク

**主要機能**:
- there's an AI for that、AI Scout活用
- 技術スタック推定（リバースエンジニアリング）
- ベンチマーク比較（速度、精度、コスト）
- 差別化要素特定（3軸以上）
- マーケットマップ作成

**Tier 2ケーススタディ**（12件）:
- ChatGPT vs Claude比較（精度、安全性、コスト、コンテキスト長）
- Gemini参入分析（Googleエコシステム統合、マルチモーダル）
- Perplexity vs You.com差別化（引用生成、リアルタイム検索）
- その他9件

---

### 5. モデル更新追跡（/monitor-model-updates）

**目的**: GPT-4o、Claude 3.7等の月次モデル更新追跡・対応

**主要機能**:
- リリースノート監視（OpenAI, Anthropic, Google）
- 性能劣化検知（ベンチマーク定期実行）
- コスト変動影響分析
- マイグレーション判断基準
- 月次レポート自動生成

**Tier 2ケーススタディ**（12件）:
- GPT-4 Turbo更新影響（2024年4月、コスト1/2削減、精度維持）
- Claude 3.5対応（2024年6月、Sonnet→Opus切り替え判断）
- Gemini 1.5 Pro統合（2024年2月、200万トークンコンテキスト活用）
- その他9件

---

## 全スキル一覧（21スキル）

### Phase 1: 需要発見・企画（8スキル）

| # | スキル名 | コマンド | 用途 |
|---|---------|---------|------|
| 1 | discover-demand | `/discover-demand` | 需要発見・市場機会特定 |
| 2 | create-mvv | `/create-mvv` | MVV（ミッション・ビジョン・バリュー）策定 |
| 3 | create-persona | `/create-persona` | ターゲットペルソナ作成 |
| 4 | build-lp | `/build-lp` | ランディングページ自動構築 |
| 5 | build-pitch-deck | `/build-pitch-deck` | VCピッチデッキ自動生成 |
| 6 | research-competitors | `/research-competitors` | 競合調査・分析 |
| 7 | analyze-ai-competitors | `/analyze-ai-competitors` | **AI競合製品分析フレームワーク（新規）** |
| 8 | validate-cpf | `/validate-cpf` | CPF（Customer Problem Fit）検証 |

### Phase 2-3: PSF/PMF検証・スケール（8スキル）

| # | スキル名 | コマンド | 用途 |
|---|---------|---------|------|
| 9 | validate-10x | `/validate-10x` | 10倍優位性検証（3軸以上） |
| 10 | validate-psf | `/validate-psf` | PSF（Problem Solution Fit）検証 |
| 11 | **design-pricing** | `/design-pricing` | **AI製品価格設計（Freemium、API従量課金）** |
| 12 | validate-pmf | `/validate-pmf` | PMF（Product Market Fit）検証 |
| 13 | measure-aarrr | `/measure-aarrr` | AARRRメトリクス分析 |
| 14 | validate-unit-economics | `/validate-unit-economics` | ユニットエコノミクス検証 |
| 15 | monitor-burn-rate | `/monitor-burn-rate` | バーンレート・ランウェイ管理 |
| 16 | pivot-decision | `/pivot-decision` | ピボット意思決定支援 |

### AI製品特化（6スキル）- ForGenAI新規

| # | スキル名 | コマンド | 用途 |
|---|---------|---------|------|
| 17 | select-ai-tech-stack | `/select-ai-tech-stack` | **AI技術スタック選定（新規）** |
| 18 | build-community-pre-launch | `/build-community-pre-launch` | **プレローンチコミュニティ構築（新規）** |
| 19 | create-producthunt-strategy | `/create-producthunt-strategy` | **Product Hunt #1獲得戦略（新規）** |
| 20 | optimize-prompt-quality | `/optimize-prompt-quality` | **プロンプト品質最適化（新規）** |
| 21 | monitor-model-updates | `/monitor-model-updates` | **モデル更新追跡（新規）** |
| 22 | prepare-vc-meeting | `/prepare-vc-meeting` | VC対応Q&A準備（50問・8カテゴリ） |

---

## ディレクトリ構造

```
Founder_Agent_ForGenAI/
├── GenAI_research/                # AI技術・トレンド研究（60+件）
│   ├── LLM/
│   │   ├── 01_LifeisBeautiful_insights.md
│   │   └── 10_prompt_template.md
│   ├── technologies/
│   │   ├── openai/
│   │   ├── anthropic/
│   │   ├── google/
│   │   ├── langchain/
│   │   └── llamaindex/
│   ├── topics/
│   │   ├── prompt_engineering/
│   │   ├── llm.md
│   │   ├── rag.md
│   │   └── agents.md
│   └── case_studies/
│       └── tier2/                 # Tier 2ケーススタディ（60件）
│           ├── select-ai-tech-stack/    # 12件
│           ├── create-producthunt-strategy/  # 12件
│           ├── optimize-prompt-quality/      # 12件
│           ├── analyze-ai-competitors/       # 12件
│           └── monitor-model-updates/        # 12件
├── documents/
│   ├── 1_initiating/
│   ├── 2_discovery/
│   ├── 3_planning/
│   │   └── ai_tech_stack_selection.md  # 技術スタック選定書
│   ├── 4_executing/
│   │   ├── producthunt_launch_strategy.md  # Product Hunt戦略
│   │   └── prompt_optimization_guide.md    # プロンプト最適化ガイド
│   └── 5_monitoring/
│       └── model_update_report.md      # モデル更新レポート
└── README.md（本ファイル）
```

---

## 使用方法

### 1. 基本フロー（AI製品開発）

```
/discover-demand                    # 需要発見
↓
/validate-cpf                       # CPF検証（70%以上必須）
↓
/select-ai-tech-stack               # AI技術スタック選定★
↓
/validate-10x                       # 10倍優位性検証（3軸以上）
↓
/optimize-prompt-quality            # プロンプト最適化★
↓
/validate-psf                       # PSF検証
↓
/analyze-ai-competitors             # AI競合分析★
↓
/validate-pmf                       # PMF検証
↓
/create-producthunt-strategy        # Product Hunt戦略★
↓
/monitor-model-updates              # モデル更新追跡★（継続）
```

★: ForGenAI新規スキル

### 2. Product Huntローンチフロー

```
/validate-psf                       # PSF達成確認
↓
/build-community-pre-launch         # コミュニティ構築（3-6ヶ月前）★
↓
/validate-pmf                       # PMF達成確認
↓
/create-producthunt-strategy        # PH戦略立案（3-4週間前）
↓
/optimize-prompt-quality            # デモ動画用プロンプト最適化
↓
/analyze-ai-competitors             # 差別化ポイント明確化
↓
（Product Hunt Launch）
↓
/measure-aarrr                      # CAC分析、転換率測定
```

### 3. 技術スタック最適化フロー

```
/select-ai-tech-stack               # 初期技術選定
↓
/optimize-prompt-quality            # プロンプト品質改善
↓
/monitor-model-updates              # 月次モデル更新追跡
↓
（性能劣化検知）
↓
/select-ai-tech-stack               # 技術スタック再評価
```

---

## 成功基準（ForGenAI特化）

### Phase 1: CPF検証
- **CPFスコア**: 70%以上（Origin: 60%）
- **インタビュー件数**: 20人以上（AI製品は技術的理解が重要）
- **課題共通率**: 70%以上

### Phase 2: PSF検証
- **10倍優位性**: 3軸以上（技術精度、速度、コスト等）
- **技術的差別化**: ChatGPT等との定量比較（精度+10%、速度2倍、コスト1/2等）
- **UVP刺さり度**: 35/40以上（Origin: 28/40）

### Phase 3: PMF検証
- **NPS**: 50以上
- **継続率**: 60%以上（4週間）
- **プロンプト再現性**: 90%以上

### Product Hunt
- **目標順位**: #1（CAC 1/2-1/3削減効果）
- **初動upvotes**: 1,000+（24-48時間以内）
- **ローンチ日サインアップ**: 1,000+

---

## 参照リソース

### GenAI_research
- **LLM Insights**: モデル進化、コモディティ化トレンド、コスト最適化パターン
- **Technologies**: OpenAI、Anthropic、Google、LangChain、LlamaIndex
- **Topics**: Prompt Engineering、LLM、RAG、Agents
- **Case Studies**: Perplexity、Cursor、Notion AI、Jasper、Character.AI等60件

### 外部リソース
- Product Hunt: https://www.producthunt.com/
- OpenAI Platform: https://platform.openai.com/
- Anthropic Console: https://console.anthropic.com/
- Google AI Studio: https://aistudio.google.com/

---

## Originとの差分サマリー

| 項目 | Origin | ForGenAI | 差分理由 |
|------|--------|----------|---------|
| **スキル数** | 15 | 21 | AI製品特化スキル6件追加 |
| **CPFスコア** | 60%以上 | 70%以上 | AI市場競争激化 |
| **10倍優位性** | 2軸以上 | 3軸以上 | ChatGPT等との差別化必須 |
| **技術選定** | なし | AI技術スタック選定追加 | LLMプロバイダー比較重要 |
| **Product Hunt** | なし | PH戦略追加 | CAC 1/2-1/3削減効果大 |
| **プロンプト最適化** | なし | プロンプト品質最適化追加 | AI製品の競争力源泉 |
| **競合分析** | 汎用 | AI競合分析特化 | ChatGPT等との比較必須 |
| **モデル更新** | なし | モデル更新追跡追加 | 月次更新対応必須 |

---

## 更新履歴

- 2026-01-03: ForGenAI版 v1.1リリース（AI製品特化スキル6件追加、GenAI_research統合、Tier 2ケーススタディ60件統合、build-community-pre-launch追加）
- ベース: Founder Agent Origin v1.0

---

**作成日**: 2026-01-03
**バージョン**: 1.0
**総スキル数**: 21
**新規スキル数**: 6（AI製品特化）
**Tier 2ケーススタディ**: 60件
**品質スコア目標**: 95/100
