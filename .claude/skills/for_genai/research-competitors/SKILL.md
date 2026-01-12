---
skill_id: for-genai-research-competitors
skill_name: Competitive Research (ForGenAI)
domain: ForGenAI
phase: 3_planning
category: market_analysis
origin: for_startup
cpf_threshold: 70%
quality_target: 95/100
version: 1.0.0
last_updated: 2026-01-02
dependencies:
  - for-genai-discover-demand
  - for-genai-validate-cpf
integration_sources:
  - GenAI_research/case_studies/
  - GenAI_research/LLM/01_LifeisBeautiful_insights.md
  - GenAI_research/topics/llm/
output_path: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/3_planning/competitor_research_forgenai.md
---

# Research Competitors Skill (ForGenAI Edition)

**生成AI特化版競合調査スキル** - ChatGPT/Claude/Gemini等のAI巨人、AIツール群、Product Hunt AI製品を徹底分析。AI公共財化シナリオを考慮した10倍優位性検証。

---

## このSkillでできること

1. **AI巨人分析（ChatGPT/Claude/Gemini）**: OpenAI、Anthropic、Googleの戦略・価格・機能・資金調達
2. **AIツール競合調査**: Perplexity、Midjourney、Jasper等の特化型AIツール
3. **Product Hunt AI製品調査**: 直近6ヶ月のProduct Hunt #1〜#10 AI製品分析
4. **AI技術スタック比較**: LLMモデル性能、API価格、マルチモーダル対応
5. **プロンプトパターン分析**: 競合がどのプロンプト手法を使用しているか
6. **5軸ベンチマーク（ForGenAI特化版）**: 時間/コスト/使いやすさ/成果/導入障壁 + AI差別化軸
7. **ポジショニングマップ**: AI市場の構造を可視化
8. **空白地帯特定（AI公共財化対応）**: 参入余地のある領域を発見
9. **10倍優位性の検証（3軸以上）**: ForGenAI基準の3軸10倍優位性を満たしているか確認

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `demand_discovery_forgenai.md`、`cpf_judgment_forgenai.md`（オプション） |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/3_planning/competitor_research_forgenai.md` |
| **次のSkill** | `/validate-10x` (3軸10倍優位性の厳格検証) |
| **ステージ** | PSF検証（AI市場競争分析） |

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @GenAI_research/case_studies/ - ChatGPT, Perplexity, Midjourney等の成功事例
- @GenAI_research/LLM/01_LifeisBeautiful_insights.md - AI民主化、公共財化トレンド
- @GenAI_research/topics/llm/ - LLMモデル比較、プロンプトパターン
- @GenAI_research/technologies/ - AI技術スタック、API価格比較

### Tier 2 ケーススタディ（12件）
以下のTier 2ケーススタディが利用可能です：
- @GenAI_research/case_studies/tier2/research-competitors/

**AI競合分析の実践例**:
1. **GENAI_COMP_001_chatgpt_vs_claude.md** - OpenAI vs Anthropic戦略比較
2. **GENAI_COMP_002_perplexity_vs_google.md** - AI検索 vs 従来検索
3. **GENAI_COMP_003_midjourney_vs_dalle.md** - AI画像生成競争
4. **GENAI_COMP_004_jasper_vs_copy_ai.md** - AIライティングツール比較
5. **GENAI_COMP_005_character_ai_vs_replika.md** - AI会話ツール競争
6. **GENAI_COMP_006_github_copilot_vs_cursor.md** - AIコード生成競争
7. **GENAI_COMP_007_notion_ai_vs_clickup.md** - 生産性ツール×AI
8. **GENAI_COMP_008_runway_vs_pika.md** - AI動画生成競争
9. **GENAI_COMP_009_elevenlabs_vs_play_ht.md** - AI音声生成競争
10. **GENAI_COMP_010_grammarly_vs_quillbot.md** - AIライティング支援競争
11. **GENAI_COMP_011_gemini_entry_impact.md** - Googleの参入インパクト
12. **GENAI_COMP_012_open_source_llm_threat.md** - オープンソースLLMの脅威（Llama, Mistral）

---

## Domain-Specific Knowledge (from GenAI_Research)

### Success Patterns（AI競合分析成功事例）

#### 事例1: Perplexity AI（AI検索での差別化）
- **直接競合**: Google検索、Bing AI、ChatGPT
- **差別化軸**:
  | 軸 | Google検索 | ChatGPT | Perplexity AI | 倍率 |
  |---|---|---|---|---|
  | 情報信頼性 | リンク羅列（判断はユーザー） | 引用なし（信頼性不明） | Citation付き回答 | 10x |
  | 検索スピード | 0.5秒 | 5秒（GPT-4） | 2秒（最適化） | 2.5x |
  | 使いやすさ | 10リンク確認 | 1回答（検証不可） | 1回答+引用確認可 | 5x |
- **市場タイミング**: ChatGPTブーム直後のローンチ → AI検索ニーズの高まり
- **資金調達**: Seed $3.2M → Series A $25M（評価額$150M）
- **Product Hunt**: #1獲得（3,200 upvotes）

**学習ポイント**:
- ChatGPTの弱点（引用なし）を攻撃
- Product Hunt #1で初期ユーザー爆発的獲得
- Citation機能で差別化（ChatGPTにない機能）

#### 事例2: Midjourney（AI画像生成での差別化）
- **直接競合**: DALL-E 3、Stable Diffusion、Adobe Firefly
- **差別化軸**:
  | 軸 | DALL-E 3 | Stable Diffusion | Midjourney | 倍率 |
  |---|---|---|---|---|
  | 画像品質 | 高品質 | 可変品質 | 最高品質（V5/V6） | 3x |
  | 使いやすさ | ChatGPT統合 | 技術的（ComfyUI等） | Discord直感操作 | 10x |
  | コスト | $20/月（ChatGPT Plus） | 無料（自前GPU） | $10-60/月 | 2x（有料だが高品質） |
- **Discord戦略**: コミュニティ主導のフィードバック、バイラル拡散
- **資金調達**: 非公開（推定$100M+）
- **収益**: $200M monthly revenue

**学習ポイント**:
- 非技術者向けUX最優先（Discordで完結）
- 高品質画像で差別化（V5/V6でDALL-E 3超え）
- コミュニティ主導の成長戦略

#### 事例3: GitHub Copilot（AIコード生成での差別化）
- **直接競合**: ChatGPT Code Interpreter、Cursor、Codeium
- **差別化軸**:
  | 軸 | ChatGPT | Cursor | GitHub Copilot | 倍率 |
  |---|---|---|---|---|
  | 統合度 | 別画面 | エディタ統合 | VS Code完全統合 | 5x |
  | コード精度 | 汎用 | 汎用 | GitHub学習データ | 3x |
  | 導入障壁 | 高（コピペ必要） | 中（新エディタ） | 低（既存VS Code） | 10x |
- **市場タイミング**: VS Code普及後のローンチ → 既存ユーザー基盤活用
- **資金調達**: Microsoft出資（正確な額非公開）
- **ユーザー数**: 1M+ developers

**学習ポイント**:
- 既存ツール（VS Code）完全統合で導入障壁ゼロ
- GitHub学習データで精度向上
- Microsoft資本力でスケーリング

### Common Pitfalls（AI競合分析の失敗パターン）

#### 失敗パターン1: 「ChatGPTと同じ」差別化不足
- **教訓**: ChatGPTと同じ汎用AI対話では差別化不可能
- **対策**: 特定ドメインへの深い特化（Jasper: マーケティング、Copilot: コード生成）

#### 失敗パターン2: 無料AIツールとの競合無視
- **教訓**: ChatGPT無料版、Claude無料版、Gemini無料版との差別化が必須
- **対策**: 有料化理由の明確化（速度、精度、機能、データプライバシー）

#### 失敗パターン3: オープンソースLLMの脅威軽視
- **教訓**: Llama 3、Mistral等のオープンソースLLMが商用モデルに接近
- **対策**: モデル性能だけに依存せず、統合・運用・ガバナンスで差別化

#### 失敗パターン4: Googleの参入インパクト軽視
- **教訓**: Gemini参入で市場構造が激変（無料で高性能）
- **対策**: Googleにできない差別化軸（プライバシー、カスタマイズ、専門性）

### Quantitative Benchmarks（AI市場の競合分析指標）

| 指標 | 基準値 | 出典 |
|------|--------|------|
| **LLMモデル性能（MMLU）** | > 85% | ChatGPT 90%, Claude 89%, Gemini 90% |
| **API価格（$/ 1M tokens）** | < $10 | GPT-4o $2.5, Claude Sonnet $3, Gemini Pro $0.5 |
| **Product Hunt #1 Upvotes** | > 3,000 | Perplexity 3,200, Notion AI 2,800 |
| **MAU成長率（Year 1）** | > 月次15% | ChatGPT 100M in 2 months, Character.AI 100M+ |
| **API Response Time（95%ile）** | < 2秒 | ChatGPT 1.5秒, Claude 1.8秒, Gemini 1.2秒 |
| **プロンプト成功率** | > 80% | ChatGPT 85%, Claude 88%, Gemini 82% |
| **10倍優位性の軸数** | 3軸以上 | Perplexity 3軸（信頼性、スピード、UX）、Midjourney 2軸（品質、UX） |

### Best Practices（AI競合分析のベストプラクティス）

1. **ChatGPT/Claude/Geminiとの明確な差別化**: 汎用AIと同じことをしない
2. **Product Hunt AI製品の継続調査**: 直近6ヶ月の#1〜#10製品を分析
3. **LLMモデル更新の追跡**: GPT-5、Claude 4、Gemini 2.0等の次世代モデル動向
4. **オープンソースLLMの監視**: Llama、Mistral、Falcon等の性能向上
5. **AI公共財化シナリオの考慮**: モデルがコモディティ化した場合の差別化戦略

### Reference
- 詳細: @GenAI_research/case_studies/（Perplexity vs Google、Midjourney vs DALL-E等）
- AI市場基準: @GenAI_research/LLM/01_LifeisBeautiful_insights.md（AI公共財化論考）

---

## Instructions

### セッション開始

調査対象の課題/ソリューションを入力してください（省略時は `demand_discovery_forgenai.md` を参照）:

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-60分（AI技術スタック分析含む）
**ForGenAI強化項目**: AI巨人分析、Product Hunt AI製品調査、LLMモデル比較、プロンプトパターン分析

### 自動実行フロー

**STEP 1: 入力情報の取得**
- `demand_discovery_forgenai.md` が存在する場合: 最有望需要候補を読み込み
- `cpf_judgment_forgenai.md` が存在する場合: AI差別化軸を参照
- 存在しない場合: ユーザー入力から課題情報を取得

**STEP 2: 検索クエリ生成（ForGenAI強化版）**
- AI巨人クエリ（各5個）: "ChatGPT vs Claude", "Gemini capabilities", "OpenAI API pricing"
- AIツール競合クエリ（各5個）: "Perplexity AI features", "Midjourney pricing", "Jasper AI review"
- Product Hunt AIクエリ（各3個）: "Product Hunt AI products 2025", "Product Hunt #1 AI tools"
- LLMモデル比較クエリ（各3個）: "GPT-4o vs Claude Sonnet", "LLM benchmark 2025"
- オープンソースLLMクエリ（各2個）: "Llama 3 performance", "Mistral Large"

**STEP 3: AI巨人分析（ChatGPT/Claude/Gemini）**
- ツール: WebSearch
- 対象: OpenAI ChatGPT、Anthropic Claude、Google Gemini
- 収集項目:
  - **モデル性能**: MMLU、GSM8K、HumanEval等のベンチマーク
  - **API価格**: $/ 1M tokens（Input/Output別）
  - **主要機能**: 長文処理、マルチモーダル、ファインチューニング対応
  - **無料版制限**: 無料版の機能制限、有料版との差
  - **資金調達**: 評価額、主要投資家
  - **ユーザー数**: MAU、DAU、API利用企業数
- 目標: 3社（ChatGPT、Claude、Gemini）必須

**STEP 4: AIツール競合収集（特化型AIツール）**
- ツール: WebSearch
- 対象: Perplexity、Midjourney、Jasper、Character.AI等の特化型AIツール
- 収集項目:
  - **特化領域**: 検索、画像生成、ライティング、会話等
  - **差別化ポイント**: ChatGPTにない機能
  - **価格**: 月額料金、無料プラン有無
  - **Product Hunt成績**: #1獲得有無、upvotes数
  - **資金調達**: 調達ラウンド、評価額
  - **ユーザー数**: MAU、成長率
- 目標: 5-10件

**STEP 5: Product Hunt AI製品調査（新規追加）**
- ツール: WebSearch
- 対象: 直近6ヶ月のProduct Hunt #1〜#10 AI製品
- 収集項目:
  - **製品名**: Product名、tagline
  - **カテゴリ**: AI Search、AI Image、AI Writing等
  - **Upvotes数**: #1獲得時のupvotes数
  - **ローンチタイミング**: 曜日、時刻
  - **Hunter**: 誰がHuntしたか
  - **差別化ポイント**: 他AIツールとの差
- 目標: 直近6ヶ月の#1 AI製品10件以上

**STEP 6: AI技術スタック比較（新規追加）**
- ツール: WebSearch
- 対象: LLMモデル、API、プロンプトパターン
- 収集項目:
  - **LLMモデル性能**: MMLU、GSM8K、HumanEval
  - **API価格比較**: GPT-4o vs Claude Sonnet vs Gemini Pro
  - **マルチモーダル対応**: 画像、音声、動画生成機能
  - **プロンプトパターン**: Chain-of-Thought、Few-shot、ReAct使用状況
  - **オープンソースLLM**: Llama 3、Mistral Largeの性能
- 目標: 5モデル以上の比較

**STEP 7: 5軸ベンチマーク表作成（ForGenAI強化版）**
- 時間効率（API Response Time）
- コスト（API価格、月額料金）
- 使いやすさ（プロンプト成功率、UI/UX）
- 成果・効果（精度、品質）
- 導入障壁（無料プラン有無、API統合難易度）
- **AI差別化軸（新規追加）**:
  - **モデル性能**: MMLU、GSM8Kスコア
  - **プロンプト品質**: 成功率、失敗率
  - **AI倫理・安全性**: Constitutional AI、バイアス検出

**STEP 8: ポジショニングマップ作成（AI市場版）**
- 2軸でマッピング（例: 汎用性 vs 特化度、価格 vs 性能）
- 空白地帯の特定
- **AI公共財化対応**: モデルコモディティ化後も価値提供できる領域の特定

**STEP 9: 差別化ポイント整理（ForGenAI強化版）**
- **3軸以上の10倍優位性の検証**（ForGenAI基準）
- ChatGPT/Claude/Geminiとの明確な差別化
- 参入戦略の提案
- **AI公共財化シナリオ**: モデルコモディティ化後の差別化戦略

**STEP 10: 成果物出力**
- ツール: Write
- パス: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/3_planning/competitor_research_forgenai.md`

---

## 5軸ベンチマーク基準（ForGenAI強化版）

| 軸 | 評価ポイント | 10倍達成の例 | AI市場での重要性 |
|------|-------------|-------------|---------------|
| **時間効率** | API Response Time | 10秒 → 1秒 | リアルタイム性が競争力 |
| **コスト** | API価格、月額料金 | $100/月 → $10/月 | ChatGPT Plus $20との比較 |
| **使いやすさ** | プロンプト成功率 | 30% → 90% | 非技術者向けUX重要 |
| **成果・効果** | 精度、品質 | MMLU 50% → 90% | モデル性能が基礎 |
| **導入障壁** | 無料プラン、API統合 | API統合1週間 → 1時間 | 開発者エクスペリエンス |
| **AI差別化** | 独自プロンプト、ドメイン特化データ | 汎用AI → 専門AI（10x精度） | AI Wrapper批判回避 |

**ForGenAI追加基準**:
- **3軸以上で10倍優位性を達成**していない場合、AI市場で埋もれる可能性大
- ChatGPT/Claude/Geminiと同じ汎用性では差別化不可能

---

## 成果物フォーマット（ForGenAI強化版）

```markdown
# 競合・AI市場調査レポート (ForGenAI Edition)

**作成日**: [YYYY-MM-DD]
**調査対象**: [課題/ソリューション名]
**5軸スコア**: XX/60点（AI差別化軸追加）
**ForGenAI評価**: AI市場競争可能 / 要改善 / 要再設計

---

## エグゼクティブサマリー

| 項目 | 結果 |
|------|------|
| AI巨人競合数 | 3件（ChatGPT、Claude、Gemini） |
| AIツール競合数 | X件 |
| Product Hunt AI製品 | X件（直近6ヶ月#1製品） |
| 市場規模（TAM） | XXX億円 |
| 空白地帯 | [特定された領域] |
| **10倍達成可能軸** | **[3軸以上]** ✅ / [2軸以下] ❌ |
| **AI公共財化対応** | 対応済み ✅ / 要対応 ⚠️ |

---

## AI巨人分析（ChatGPT/Claude/Gemini）

### ChatGPT（OpenAI）

| 項目 | 内容 |
|------|------|
| モデル | GPT-4o、GPT-4 Turbo、GPT-3.5 |
| MMLU性能 | 90% |
| API価格 | GPT-4o: $2.5/1M tokens（Input）、$10/1M tokens（Output） |
| 月額料金 | ChatGPT Plus: $20/月、ChatGPT Team: $25/月 |
| 無料版制限 | GPT-3.5のみ、画像生成なし、優先アクセスなし |
| 主要機能 | テキスト生成、コード生成、画像生成（DALL-E 3）、音声認識、ファインチューニング |
| 強み | 汎用性、知名度、エコシステム（GPTs） |
| 弱み | 引用なし（信頼性不明）、長文処理弱い（128K tokens） |
| ユーザー数 | 100M+ MAU、150M+ ChatGPT Plus subscribers |
| 資金調達 | Microsoft $10B投資、評価額$86B |
| 成長率 | 100M MAU in 2 months（史上最速） |

### Claude（Anthropic）

| 項目 | 内容 |
|------|------|
| モデル | Claude 3.5 Sonnet、Claude 3 Opus、Claude 3 Haiku |
| MMLU性能 | 89%（Opus）、88%（Sonnet） |
| API価格 | Claude Sonnet: $3/1M tokens（Input）、$15/1M tokens（Output） |
| 月額料金 | Claude Pro: $20/月 |
| 無料版制限 | Claude 3 Haikuのみ、優先アクセスなし |
| 主要機能 | 長文処理（200K tokens）、Constitutional AI、安全性重視 |
| 強み | 長文処理、安全性、指示追従精度 |
| 弱み | 画像生成なし、マルチモーダル限定的 |
| ユーザー数 | 10M+ MAU（推定） |
| 資金調達 | Google $300M、評価額$5B |
| 成長率 | 月次20%（推定） |

### Gemini（Google）

| 項目 | 内容 |
|------|------|
| モデル | Gemini 1.5 Pro、Gemini 1.5 Flash |
| MMLU性能 | 90%（1.5 Pro） |
| API価格 | Gemini Pro: $0.5/1M tokens（Input）、$1.5/1M tokens（Output） |
| 月額料金 | Google One AI Premium: $19.99/月 |
| 無料版制限 | Gemini Flash無料、優先アクセスなし |
| 主要機能 | マルチモーダル（画像、動画、音声）、1M context window、Google統合 |
| 強み | 低価格、マルチモーダル、長文処理（1M tokens） |
| 弱み | エコシステム弱い、知名度ChatGPTに劣る |
| ユーザー数 | 不明（Google Search統合） |
| 資金調達 | Google内製（DeepMind統合） |
| 成長率 | 不明 |

**AI巨人との差別化ポイント**:
- ChatGPT: 引用なし → **Citation機能で差別化**（Perplexity戦略）
- Claude: 画像生成なし → **マルチモーダル統合で差別化**
- Gemini: エコシステム弱い → **専門コミュニティで差別化**

---

## AIツール競合分析（ForGenAI強化版）

### 競合1: Perplexity AI

| 項目 | 内容 |
|------|------|
| 概要 | AI検索エンジン、Citation付き回答 |
| 価格 | Perplexity Pro: $20/月 |
| 主要機能 | 引用付き回答、リアルタイム検索、フォローアップ質問 |
| 強み | 信頼性（Citation）、検索特化 |
| 弱み | 汎用性低い、ChatGPT比較で機能少ない |
| ユーザー数/売上 | 10M+ MAU |
| 調達ラウンド | Series A $25M |
| 評価額（最新） | $150M |
| ARR/MRR | 不明 |
| 成長率 | 月次25%（推定） |
| **Product Hunt** | **#1獲得（3,200 upvotes）** |
| **AI差別化** | **Citation機能（ChatGPTにない）** |

### 競合2: Midjourney

| 項目 | 内容 |
|------|------|
| 概要 | AI画像生成ツール、Discord統合 |
| 価格 | $10/月〜$60/月 |
| 主要機能 | 高品質画像生成（V5/V6）、Discord操作 |
| 強み | 画像品質最高、非技術者向けUX |
| 弱み | Discordのみ（Web版なし）、API非公開 |
| ユーザー数/売上 | $200M monthly revenue |
| 調達ラウンド | 非公開 |
| 評価額（最新） | 推定$1B+ |
| ARR/MRR | $2.4B ARR |
| 成長率 | 月次15%（推定） |
| **Product Hunt** | **非掲載（Discord先行戦略）** |
| **AI差別化** | **最高品質画像（DALL-E 3超え）** |

### 競合3: [他AIツール]
...

---

## Product Hunt AI製品調査（新規追加）

### 直近6ヶ月の#1 AI製品

| 製品名 | カテゴリ | Upvotes | ローンチ日 | Hunter | 差別化ポイント |
|--------|---------|---------|----------|--------|-------------|
| [製品1] | AI Search | 3,200 | 2025-12-15 | [Hunter名] | Citation機能 |
| [製品2] | AI Image | 2,800 | 2025-11-20 | [Hunter名] | リアルタイム生成 |
| [製品3] | AI Writing | 2,500 | 2025-10-25 | [Hunter名] | マーケティング特化 |
| ... | ... | ... | ... | ... | ... |

**学習ポイント**:
- **ローンチタイミング**: Tuesday-Thursday PST 0:01が多数（70%）
- **Upvotes閾値**: #1獲得には3,000+ upvotes必要
- **差別化**: 既存AIツール（ChatGPT/Claude/Gemini）にない機能が必須

---

## AI技術スタック比較（新規追加）

### LLMモデル性能比較

| モデル | MMLU | GSM8K | HumanEval | API価格（$/1M tokens Input） |
|--------|------|-------|-----------|---------------------------|
| GPT-4o | 90% | 92% | 90% | $2.5 |
| Claude Sonnet | 88% | 90% | 88% | $3 |
| Gemini Pro | 90% | 91% | 87% | $0.5 |
| Llama 3 70B | 82% | 85% | 81% | 無料（自前ホスティング） |
| Mistral Large | 81% | 83% | 80% | $2 |

**オープンソースLLMの脅威**:
- Llama 3 70B: 商用モデルに性能接近（MMLU 82%）
- 自前ホスティングで$0コスト → API課金モデルの脅威

### プロンプトパターン分析

| プロンプトパターン | ChatGPT | Claude | Gemini | 提案ソリューション |
|-----------------|---------|--------|--------|-----------------|
| Chain-of-Thought | ✅ | ✅ | ✅ | ✅ 独自最適化 |
| Few-shot | ✅ | ✅ | ✅ | ✅ ドメイン特化Few-shot |
| Self-Consistency | ✅ | ✅ | ⚠️ | ✅ |
| ReAct | ⚠️ | ✅ | ⚠️ | ✅ 独自実装 |

---

## 5軸ベンチマーク表（ForGenAI強化版）

| 軸 | ChatGPT | Claude | Gemini | 競合AIツール | 提案ソリューション | 10倍達成 |
|----|---------|--------|--------|------------|------------------|---------|
| 時間効率（API Response Time） | 1.5秒 | 1.8秒 | 1.2秒 | 2秒 | **0.8秒** | ✅（1.5倍） |
| コスト（API価格） | $2.5/1M | $3/1M | $0.5/1M | $5/1M | **$1/1M** | ⚠️（2-5倍） |
| 使いやすさ（プロンプト成功率） | 85% | 88% | 82% | 70% | **95%** | ✅（1.4倍） |
| 成果・効果（MMLU性能） | 90% | 88% | 90% | 75% | **92%** | ❌（1.02倍） |
| 導入障壁（API統合） | 中 | 中 | 中 | 高 | **低** | ✅（10倍） |
| AI差別化（独自機能） | 汎用 | 長文処理 | マルチモーダル | 特化型 | **[独自差別化]** | ✅（10倍） |

**10倍達成軸数**: [3軸以上 ✅ / 2軸以下 ❌]
**ForGenAI基準評価**: [合格 ✅ / 不合格 ❌]
**根拠**: [根拠]

---

## ポジショニングマップ（AI市場版）

```
              汎用性（高）
                 │
    ChatGPT      │  Claude
    Gemini       │
                 │
 ───────────────┼───────────────
   低特化度     │  高特化度
                 │
                 │  🎯 提案ソリューション
                 │  Perplexity（AI検索）
                 │  Midjourney（AI画像）
              汎用性（低）
```

### 空白地帯（AI公共財化対応）

| 領域 | 現状 | 参入機会 | AI公共財化後の価値 |
|------|------|---------|------------------|
| [領域1] | ChatGPT汎用性高いが特化度低い | ✅ 参入余地大 | 高（ドメイン特化データ） |
| [領域2] | Gemini低価格だがエコシステム弱い | ✅ 参入余地大 | 高（コミュニティ・統合） |

---

## 差別化戦略（ForGenAI強化版）

### 主要な差別化ポイント

| # | 差別化要素 | 詳細 | ChatGPT/Claude/Geminiとの比較 | 10倍達成 | AI公共財化対応 |
|:-:|-----------|------|------------------------------|---------|-------------|
| 1 | [要素1] | [詳細] | [比較] | ✅ | 統合・運用で差別化 |
| 2 | [要素2] | [詳細] | [比較] | ✅ | ガバナンス・信頼で差別化 |
| 3 | [要素3] | [詳細] | [比較] | ✅ | ドメイン特化データで差別化 |

**3軸10倍優位性**: [達成 ✅ / 未達成 ❌]

### 推奨ポジショニング

**「[一言で表現するポジショニング]」**

例:
- Perplexity: 「信頼できるAI検索エンジン」
- Midjourney: 「最高品質のAI画像生成」
- Jasper: 「マーケター専用AIライター」

### AI公共財化シナリオ対応

| フェーズ | 時期 | 差別化戦略 |
|---------|------|----------|
| **Phase 1（Year 1-2）** | モデル性能競争 | 独自プロンプト最適化、特化型ファインチューニング |
| **Phase 2（Year 2-4）** | モデルコモディティ化 | 統合・UXでの差別化、ワークフロー自動化 |
| **Phase 3（Year 4-5）** | 完全公共財化 | ガバナンス・信頼での差別化、企業向けコンプライアンス |

---

## リスクと対策

| リスク | 深刻度 | 対策 | AI市場特有の懸念 |
|--------|:------:|------|---------------|
| ChatGPTの無料版強化 | 高 | 有料化理由の明確化（速度、精度、プライバシー） | ChatGPT Plus $20超える価値提供 |
| Googleの参入（Gemini） | 高 | Googleにできない差別化（プライバシー、カスタマイズ） | 無料・低価格との競合 |
| オープンソースLLM（Llama 3） | 中 | モデル性能以外での差別化（統合、運用、ガバナンス） | API課金モデルの脅威 |
| Product Hunt #1未達成 | 中 | 事前コミュニティ構築、Hunter確保、ローンチタイミング最適化 | 初期ユーザー獲得失敗 |

---

## 次のステップ

| コマンド | 内容 |
|----------|------|
| `/validate-10x` | 3軸10倍優位性の厳格検証（ForGenAI基準） |
| `/create-producthunt-strategy` | Product Hunt #1獲得戦略策定 |
| `/select-ai-tech-stack` | AI技術スタック最終決定（GPT-4o vs Claude vs Gemini） |
| `/build-prompt-library` | プロンプトパターンライブラリ構築 |
```

---

## 使用例

```
User: /research-competitors

Skill:
# AI競合調査（ForGenAI版） 自律実行開始

入力: demand_discovery_forgenai.md（最有望候補: AI検索エンジン）

[自動実行中...]
- STEP 1: 入力情報取得 ✅
- STEP 2: 検索クエリ生成 ✅ (AI巨人、AIツール、Product Hunt AI製品)
- STEP 3: AI巨人分析 ✅ (ChatGPT、Claude、Gemini)
- STEP 4: AIツール競合収集 ✅ (Perplexity、Midjourney等10件)
- STEP 5: Product Hunt AI製品調査 ✅ (直近6ヶ月#1製品12件)
- STEP 6: AI技術スタック比較 ✅ (LLMモデル性能、API価格、プロンプトパターン)
- STEP 7: 5軸ベンチマーク ✅ (AI差別化軸含む)
- STEP 8: ポジショニングマップ ✅ (AI公共財化対応)
- STEP 9: 差別化ポイント整理 ✅ (3軸10倍優位性検証)
- STEP 10: 成果物出力 ✅

## 完了

成果物: competitor_research_forgenai.md
AI巨人競合: 3件（ChatGPT、Claude、Gemini）
AIツール競合: 10件（Perplexity #1 3,200 upvotes等）
Product Hunt AI製品: 12件（直近6ヶ月#1製品）
10倍達成軸数: 3軸（時間、使いやすさ、AI差別化）✅
AI公共財化対応: 対応済み（統合・運用・ガバナンスで差別化）✅
推奨: `/validate-10x` で3軸10倍優位性の厳格検証へ
```

---

## 注意事項

1. **AI巨人（ChatGPT/Claude/Gemini）との差別化必須**: 汎用AIと同じことをしない
2. **Product Hunt AI製品の継続調査**: 直近6ヶ月の#1〜#10製品を分析
3. **LLMモデル更新の追跡**: GPT-5、Claude 4、Gemini 2.0等の次世代モデル動向
4. **オープンソースLLMの監視**: Llama、Mistral、Falcon等の性能向上
5. **AI公共財化シナリオの考慮**: モデルがコモディティ化した場合の差別化戦略
6. **3軸10倍優位性の厳格評価**: ForGenAI基準では2軸以下は不合格

---

## 更新履歴

- 2026-01-02: ForGenAI版として新規作成（AI巨人分析、Product Hunt AI製品調査、LLMモデル比較、AI公共財化対応追加）

