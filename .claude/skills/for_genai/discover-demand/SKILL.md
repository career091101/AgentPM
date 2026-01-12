---
name: discover-demand (ForGenAI)
description: |
  GenAI特化版の需要発見スキル（Product Hunt戦略統合版）。生成AI市場における有望な需要を発見し、Product Hunt #1獲得可能性、プロンプトエンジニアリング品質、AI技術スタック選定基準を統合評価。CPF閾値70%以上、LLM競合分析（OpenAI vs Anthropic vs Gemini）、Chain-of-Thought/Few-shot等のプロンプトパターン評価を実施します。

  使用タイミング：
  - GenAI製品のアイデア発見段階
  - Product Hunt戦略検討前
  - AI技術スタック選定前
  - プロンプトエンジニアリング品質評価時

  所要時間：30-50分（自動実行、GenAI_research参照含む）
  出力：demand_discovery_forgenai.md
---

# Discover Demand Skill (ForGenAI Edition)

GenAI特化版の需要発見スキル。Product Hunt戦略、プロンプトエンジニアリング、AI技術スタック選定を統合した自律実行型スキル。

---

## このSkillでできること

1. **GenAI特化の生ログ収集**: Reddit r/ChatGPT、Product Hunt、X #AI等から需要収集
2. **5軸スコアリング（GenAI強化版）**: 切実度/頻度/支払い匂い/未解決度/**AI差別化軸**で評価（25点満点）
3. **Product Hunt適合性評価**: #1獲得可能性、ローンチタイミング、Hunter確保戦略
4. **AI技術スタック選定**: OpenAI vs Anthropic vs Gemini の選定基準
5. **プロンプトパターン評価**: Chain-of-Thought、Few-shot、Self-Consistency等の適合性
6. **需要候補抽出**: スコア18/25以上（CPF 70%基準）の有望候補を特定
7. **GenAI_Research統合**: 12件のAI需要分析事例を参照

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 探索分野キーワード（オプション、例: "AI画像生成", "プロンプト最適化"） |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/1_initiating/demand_discovery_forgenai.md` |
| **次のSkill** | `/create-mvv` → `/validate-cpf` (CPFスコア70%以上必須) |
| **ステージ** | Idea検証（GenAI市場） |

---

## ForGenAI特化カスタマイズ

### Origin版との差分

| 項目 | Origin | ForGenAI | 変更理由 |
|------|--------|---------|---------|
| **評価軸数** | 4軸 | **5軸** | AI差別化軸を追加（LLM性能、プロンプト品質等） |
| **満点** | 20点 | **25点** | AI差別化軸5点を追加 |
| **合格基準** | 12/20点 | **18/25点** | CPF 70%基準（GenAI市場は競争激化） |
| **Product Hunt評価** | なし | **追加** | GenAI製品のローンチ戦略必須 |
| **AI技術スタック** | なし | **追加** | OpenAI/Anthropic/Gemini選定基準 |
| **プロンプトパターン** | なし | **追加** | Chain-of-Thought、Few-shot等の評価 |

### 評価基準の厳格化

**AI差別化軸スコア（新設）**: 5点満点

| 点数 | 基準（AI差別化の明確性） |
|------|--------------------------|
| 5点 | LLM性能が10倍優位、独自プロンプトパターン、Fine-tuning済み |
| 4点 | LLM性能が5倍優位、標準プロンプトの最適化、RAG活用 |
| 3点 | LLM性能が2倍優位、既存プロンプトの改良 |
| 2点以下 | AI差別化が不明確、汎用LLM APIのみ使用（競合参入容易） |

**総合判定**:
- 21-25点: ✅ Product Hunt #1獲得可能性高 → 優先的に活用
- 18-20点: ⚠️ 検討余地 → AI差別化軸の強化、プロンプト品質向上
- 1-17点: ❌ 見送り → AI優位性の再設計必須

---

## Instructions

### セッション開始

探索分野キーワードを入力してください（省略可、例: "AI画像生成", "プロンプト最適化"）:

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-50分（GenAI_research参照含む）

以下のステップを自動実行します:
1. 検索クエリ生成（日本語・英語各5個以上、GenAI特化）
2. 生ログ収集（Reddit r/ChatGPT、Product Hunt、X #AI等）
3. 需要候補の構造化
4. **5軸スコアリング**（AI差別化軸を追加）
5. **Product Hunt適合性評価**（#1獲得可能性、ローンチタイミング）
6. **AI技術スタック選定**（OpenAI vs Anthropic vs Gemini）
7. **プロンプトパターン評価**（Chain-of-Thought、Few-shot等）
8. **GenAI_Research統合**（12件の需要分析事例参照）
9. 解決アイデア生成（AI特化）
10. マネタイズ仮説策定（SaaS/API/Freemium）
11. 成果物出力

### 自動実行フロー

**STEP 1: 検索クエリ生成（GenAI特化）**
- ツール: 内部生成
- 出力: 日本語クエリ5-10個、英語クエリ5-10個
- **GenAI特化クエリ例**:
  - 日本語: "ChatGPT 困りごと", "AI画像生成 使いにくい", "プロンプト 失敗"
  - 英語: "ChatGPT pain points", "AI image generation frustrated", "prompt engineering difficult"

**STEP 2: 生ログ収集（GenAI特化）**
- ツール: WebSearch
- 対象: Reddit r/ChatGPT, Product Hunt, X #AI, Hacker News
- 収集基準: AI関連の「困っている」「うまくいかない」発言、Product Huntの低評価レビュー
- **GenAI特化**: Product Huntの#2-#10製品のレビューから不満を抽出

**STEP 3: Product Hunt市場調査**
- ツール: WebSearch
- 対象: Product Hunt Daily Top 5（過去3ヶ月のAI製品）
- 分析: #1獲得製品の共通パターン、ローンチタイミング、Hunter戦略
- **参照**: GenAI_research/LLM/01_LifeisBeautiful_insights.md（AIトレンド分析）

**STEP 4: 需要候補の構造化**
- 処理: 収集した生ログから需要候補を抽出
- 出力: 最低5件の需要候補（AI差別化軸を含む）

**STEP 5: 5軸スコアリング（GenAI強化版）**

| 項目 | 5点 | 3点 | 1点 |
|------|-----|-----|-----|
| **切実度** | 「AI使えない」「業務止まる」 | 「できれば改善したい」 | 「別にいい」 |
| **頻度** | 同様の声10件以上 | 3-9件 | 1-2件 |
| **支払い匂い** | 「有料でも使いたい」発言あり | 時間コスト言及 | 無料希望が明確 |
| **未解決度** | 既存AI toolsでは不十分 | 既存あるが不満多数 | 十分解決済み |
| **AI差別化軸** | LLM性能10倍優位、独自プロンプト | LLM性能5倍優位、最適化 | AI優位性不明確 |

**総合判定**:
- 21-25点: ✅ Product Hunt #1獲得可能性高
- 18-20点: ⚠️ AI差別化軸の強化必須
- 1-17点: ❌ AI優位性の再設計必須

**STEP 6: Product Hunt適合性評価**

各需要候補について以下を評価:

1. **#1獲得可能性**:
   - **ビジュアル**: スクリーンショット、デモ動画、GIFアニメの魅力度
   - **Hunter確保**: 既存Hunterネットワーク、過去実績、フォロワー数
   - **ローンチタイミング**: 火-木曜日 PST午前0:01推奨、競合ローンチ回避
   - **事前コミュニティ**: Product Hunt事前登録、X/Twitterでのティーザー
   - **参考**: Perplexity AI（#1獲得）、Jasper AI（#2）のパターン分析

2. **Product Hunt戦略**:
   - 参照: @GenAI_research/LLM/01_LifeisBeautiful_insights.md
   - **成功パターン**: 事前コミュニティ参加、既存Hunter経由、ビジュアル強化

**STEP 7: AI技術スタック選定**

各需要候補について最適なLLMを選定:

| LLM | 得意領域 | コスト | 推奨ユースケース |
|-----|---------|--------|-----------------|
| **OpenAI GPT-4o** | 汎用性、推論、コード生成 | 高 | 複雑な推論、コード生成、マルチモーダル |
| **Anthropic Claude** | 長文処理、安全性、指示追従 | 中 | ドキュメント分析、コンプライアンス |
| **Google Gemini** | マルチモーダル、低コスト | 低-中 | 画像・動画分析、コスト重視 |

**選定基準**:
- **精度優先**: OpenAI GPT-4o
- **コスト優先**: Google Gemini
- **安全性優先**: Anthropic Claude

**STEP 8: プロンプトパターン評価**

各需要候補に最適なプロンプトパターンを選定:

| パターン | 説明 | 適用ケース |
|---------|------|----------|
| **Chain-of-Thought** | ステップバイステップ推論 | 複雑な問題解決、数学、論理推論 |
| **Few-shot** | 例示による学習 | フォーマット変換、スタイル統一 |
| **Self-Consistency** | 複数回生成→多数決 | 精度重視、曖昧性排除 |
| **ReAct** | 推論+行動の組み合わせ | ツール利用、複数ステップ実行 |

**評価基準**:
- プロンプトパターンが明確 → AI差別化軸 +2点
- 独自プロンプトテンプレート → AI差別化軸 +1点

**STEP 9: GenAI_Research統合（12件参照）**

需要候補分析時に以下の事例を参照:

#### 事例1: ChatGPT需要爆発（2022-2023）
- **需要**: 「簡単にAIと対話したい」「プログラミング不要でAI利用」
- **CPFスコア**: 95%（歴史的高スコア）
- **市場規模**: TAM $100B+（汎用AI市場）
- **Product Hunt**: 未ローンチ（口コミのみで爆発的成長）
- **出典**: @GenAI_research/LLM/01_LifeisBeautiful_insights.md

#### 事例2: Perplexity AI（検索エンジン再定義）
- **需要**: 「Google検索は広告多すぎ」「引用元を明示してほしい」
- **CPFスコア**: 85%
- **AI差別化軸**: Citation機能、Hallucination削減（5/5点）
- **Product Hunt**: #1獲得（2023年12月）
- **出典**: @GenAI_research/topics/llm/（Perplexity関連記事）

#### 事例3: Midjourney（画像生成需要）
- **需要**: 「デザイナー雇えない」「画像素材が高い」
- **CPFスコア**: 90%
- **AI差別化軸**: 画像品質10倍優位（5/5点）
- **Product Hunt**: 未ローンチ（Discord経由成長）
- **月額売上**: $200M（2024年推定）
- **出典**: @GenAI_research/use_cases/（画像生成ケース）

#### 事例4-12: その他GenAI需要事例
4. **Jasper AI**（マーケティングコピー生成）: CPF 80%、Product Hunt #2
5. **Character.AI**（AI会話エンターテインメント）: CPF 92%、MAU 100M+
6. **GitHub Copilot**（コード生成）: CPF 88%、$10/月で収益化成功
7. **Notion AI**（ドキュメント拡張）: CPF 75%、既存ユーザー基盤活用
8. **Runway ML**（動画生成）: CPF 85%、クリエイター特化
9. **ElevenLabs**（音声合成）: CPF 90%、多言語対応
10. **Claude by Anthropic**（長文処理）: CPF 78%、安全性差別化
11. **Grammarly AI**（ライティング支援）: CPF 82%、既存製品AI強化
12. **Otter.ai**（文字起こし）: CPF 80%、リアルタイム処理

**STEP 10: 解決アイデア生成（AI特化）**
- 対象: スコア18/25以上の候補
- 出力: ソリューション案、技術的実現可能性、**AI差別化戦略**
- **GenAI追加**: MVP開発コスト、初期ユーザー獲得戦略（Product Hunt前）、プロンプト品質評価

**STEP 11: マネタイズ仮説策定（GenAI特化）**
- 出力: 誰が/何に/いくら払うか
- **GenAI追加**:
  - 課金形態: SaaS（月額） / API（従量課金） / Freemium（無料+有料）
  - 価格帯: $10-50/月（個人）、$100-500/月（チーム）、$1,000+/月（エンタープライズ）
  - ARR目標: Year 1 $100K、Year 2 $1M、Year 3 $10M

**STEP 12: 成果物出力**
- ツール: Write
- パス: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/1_initiating/demand_discovery_forgenai.md`

---

## 成果物フォーマット

```markdown
# 需要発見レポート（ForGenAI版）

**作成日**: [YYYY-MM-DD]
**探索分野**: [キーワード or 自動探索]
**総合判定**: ✅Product Hunt #1可能 / ⚠️AI差別化不足 / ❌見送り

---

## エグゼクティブサマリー

| 順位 | 需要候補 | スコア | AI差別化 | Product Hunt | 判定 |
|:----:|---------|:------:|:--------:|:------------:|:----:|
| 1 | [タイトル] | XX/25 | 5/5 | #1可能 | ✅ |
| 2 | [タイトル] | XX/25 | 3/5 | #2-5 | ⚠️ |

---

## 需要候補詳細

### 需要候補 #1: [タイトル]

#### 生ログ引用
> "[日本語原文]"
> 出典: [Reddit r/ChatGPT]

> "[English quote]"
> Source: [Product Hunt Review]

#### 需要スコア（5軸評価、GenAI版）
| 評価項目 | スコア | 根拠 |
|---------|:------:|------|
| 切実度 | X/5 | [根拠] |
| 頻度 | X/5 | [根拠] |
| 支払い匂い | X/5 | [根拠] |
| 未解決度 | X/5 | [根拠] |
| **AI差別化軸** | **X/5** | **[LLM性能、プロンプト品質、Fine-tuning]** |
| **合計** | **XX/25** | |

#### Product Hunt適合性評価

| 指標 | 評価 | 根拠 |
|------|------|------|
| #1獲得可能性 | 高/中/低 | [ビジュアル、Hunter、タイミング] |
| ローンチタイミング | 火-木 PST 0:01 | [競合回避、最適化] |
| Hunter確保 | 済/未 | [既存ネットワーク、過去実績] |
| 事前コミュニティ | 済/未 | [X/Twitter、Product Hunt登録] |

**参考事例**: Perplexity AI #1獲得パターン
- Hunter: [実績あるHunter経由]
- ローンチタイミング: 火曜日 PST 0:01
- 事前コミュニティ: X/Twitterで2週間ティーザー
- 出典: @GenAI_research/topics/llm/（Perplexity関連記事）

#### AI技術スタック選定

| 要素 | 選定結果 | 理由 |
|------|---------|------|
| LLM | OpenAI GPT-4o / Anthropic Claude / Gemini | [精度優先/コスト優先/安全性優先] |
| プロンプトパターン | Chain-of-Thought / Few-shot / Self-Consistency | [ユースケース適合性] |
| Fine-tuning | 必要/不要 | [独自データの有無] |
| RAG | 必要/不要 | [外部知識の必要性] |

#### プロンプト品質評価

**プロンプトパターン**: Chain-of-Thought
**評価**: 5/5（独自プロンプトテンプレート、Few-shot例示含む）
**例**:
```
あなたは[ドメイン専門家]です。以下の手順で分析してください:
1. [ステップ1]
2. [ステップ2]
3. [ステップ3]

例:
入力: [例1]
出力: [期待出力1]

入力: [例2]
出力: [期待出力2]

では、以下の入力を処理してください:
入力: [実際の入力]
```

#### 解決アイデア（AI特化）
- **ソリューション案**: [具体的な形態]
- **AI差別化戦略**: [LLM性能10倍、独自プロンプト、Fine-tuning]
- **技術的実現可能性**: [評価]
- **MVP開発コスト**: [推定、API費用含む]
- **初期ユーザー獲得戦略**: [Product Hunt前の戦略]

#### マネタイズ仮説（GenAI特化）
| 項目 | 内容 |
|------|------|
| 課金形態 | SaaS月額 / API従量 / Freemium |
| 個人向け価格 | $10-50/月 |
| チーム向け価格 | $100-500/月 |
| エンタープライズ | $1,000+/月 |
| **ARR目標** | **Year 1 $100K → Year 3 $10M** |

#### GenAI_Research参照事例

最も類似する成功事例:
- **Perplexity AI**: CPF 85%、Product Hunt #1、Citation差別化
- **学び**: 引用元明示が差別化、Google検索の不満解消
- **適用**: 同様の「既存サービスの不満」を解消する戦略
- **出典**: @GenAI_research/topics/llm/（Perplexity関連）
```

---

## Domain-Specific Knowledge (from GenAI_Research)

### Success Patterns（GenAI需要分析の成功パターン）

#### 1. ChatGPT - 汎用AI需要の爆発的発見
- **需要**: 「簡単にAIと対話したい」「プログラミング不要でAI利用」
- **CPFスコア**: 95%（歴史的高スコア）
- **市場規模**: TAM $100B+（汎用AI市場）
- **AI差別化**: GPT-3.5 Turboの性能、対話UI、無料提供
- **成長**: 2ヶ月で100M MAU（史上最速）
- **出典**: @GenAI_research/LLM/01_LifeisBeautiful_insights.md

#### 2. Perplexity AI - 検索エンジン再定義
- **需要**: 「Google検索は広告多すぎ」「引用元を明示してほしい」
- **CPFスコア**: 85%
- **AI差別化軸**: Citation機能、Hallucination削減（5/5点）
- **Product Hunt**: #1獲得（2023年12月）
- **ARR**: $20M（2024年推定）
- **出典**: @GenAI_research/topics/llm/（Perplexity関連記事）

#### 3. Midjourney - 画像生成需要の発見
- **需要**: 「デザイナー雇えない」「画像素材が高い」
- **CPFスコア**: 90%
- **AI差別化軸**: 画像品質10倍優位（5/5点）
- **Product Hunt**: 未ローンチ（Discord経由成長）
- **月額売上**: $200M（2024年推定）
- **出典**: @GenAI_research/use_cases/（画像生成ケース）

### Common Pitfalls（GenAI需要発見の失敗パターン）

1. **AI差別化軸の不明確化**:
   - ❌ 汎用LLM APIのみ使用、プロンプト品質低い
   - ✅ 独自プロンプトパターン、Fine-tuning、RAG活用
   - **教訓**: AI差別化軸なしでは競合参入時に無効化される

2. **Product Hunt戦略の欠如**:
   - ❌ ローンチタイミング未考慮、Hunter未確保、事前コミュニティなし
   - ✅ 火-木 PST 0:01、既存Hunter経由、X/Twitter事前ティーザー
   - **教訓**: GenAI製品はProduct Hunt #1-3が初期トラクション獲得の鍵

3. **プロンプトエンジニアリング品質の過小評価**:
   - ❌ "ChatGPTと同じことができる" → 差別化なし
   - ✅ Chain-of-Thought、Few-shot、Self-Consistency等の独自パターン
   - **教訓**: プロンプト品質がUX差別化の最重要要素

### Quantitative Benchmarks（GenAI需要発見の定量指標）

| 指標 | GenAI市場基準 | Origin基準 | 出典 |
|------|-------------|----------|------|
| **CPFスコア** | **70%以上** | 60%以上 | GenAI競争激化により厳格化 |
| **AI差別化軸** | **3/5以上** | - | @GenAI_research分析 |
| **Product Hunt順位** | **#1-3推奨** | - | 初期トラクション獲得の鍵 |
| **プロンプト品質** | **4/5以上** | - | UX差別化の最重要要素 |

### Best Practices（GenAI需要発見のベストプラクティス）

1. **Reddit r/ChatGPT、Product Huntレビューから不満を抽出**:
   - ChatGPT/Perplexity/Midjourney等の既存AI toolsのレビューを徹底分析
   - #2-#10製品の低評価レビューから「未解決の不満」を発見

2. **AI差別化軸の明確化**:
   - LLM性能（GPT-4o vs Claude vs Gemini）
   - プロンプトパターン（Chain-of-Thought、Few-shot等）
   - Fine-tuning、RAG活用

3. **Product Hunt戦略の事前設計**:
   - ローンチタイミング: 火-木 PST 0:01
   - Hunter確保: 既存ネットワーク、過去実績確認
   - 事前コミュニティ: X/Twitter 2週間ティーザー

4. **GenAI_Research事例の活用**:
   - 12件の成功事例から最も類似するパターンを特定
   - 失敗パターンの回避（AI差別化不足、Product Hunt失敗等）

### Reference（詳細ドキュメント）

- **GenAI_Research統合**: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`
- **Product Hunt戦略**: `@GenAI_research/topics/llm/（Perplexity、Jasper等）`
- **プロンプトパターン**: `@GenAI_research/LLM/10_prompt_template.md`

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **WebSearch失敗**: @.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

### ForGenAI特有のエラー

**Product Huntデータ取得失敗**:
1. Product Hunt APIが利用できない場合
2. Web Scrapingにフォールバック（過去ローンチ記事）
3. それでも不可の場合はHuman-in-the-Loop（ユーザーにProduct Hunt戦略を問い合わせ）

**AI技術スタック選定の不確実性**:
1. 複数LLMの性能比較データが不足する場合
2. デフォルトで OpenAI GPT-4o を推奨（汎用性重視）
3. コスト重視の場合は Gemini、安全性重視の場合は Claude を提案

---

## KB参照

このスキルは以下のナレッジベースを参照します：

- @startup_science/01_stages/cpf/3u_validation.md
- @startup_science/01_stages/cpf/persona_creation.md
- @startup_science/03_tactics/founder_issue_fit/fif_overview.md
- @startup_science/01_stages/cpf/cpf_overview.md
- @.claude/skills/_shared/skill_chains.md
- @.claude/skills/_shared/error_handling_patterns.md
- **@GenAI_research/LLM/01_LifeisBeautiful_insights.md** （GenAI追加）
- **@GenAI_research/LLM/02_Ochyai_Note_insights.md** （GenAI追加）
- **@GenAI_research/topics/llm/** （GenAI追加）
- **@GenAI_research/use_cases/** （GenAI追加）

### Tier 2ケーススタディ（GenAI需要分析12件）

discover-demandスキルから参照する12件のGenAI需要分析事例:

1. **ChatGPT** - 汎用AI需要の爆発的発見
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/01_chatgpt_demand_explosion.md
   - CPF 95%、2ヶ月で100M MAU、汎用AI市場TAM $100B+

2. **Perplexity AI** - 検索エンジン再定義
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/02_perplexity_search_redefinition.md
   - CPF 85%、Citation差別化、Product Hunt #1

3. **Midjourney** - 画像生成需要
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/03_midjourney_image_generation.md
   - CPF 90%、月額売上$200M、Discord経由成長

4. **Jasper AI** - マーケティングコピー生成
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/04_jasper_marketing_copy.md
   - CPF 80%、Product Hunt #2、ARR $75M

5. **Character.AI** - AI会話エンターテインメント
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/05_character_ai_conversation.md
   - CPF 92%、MAU 100M+、エンタメ特化

6. **GitHub Copilot** - コード生成需要
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/06_github_copilot_code_generation.md
   - CPF 88%、$10/月、開発者生産性10倍

7. **Notion AI** - ドキュメント拡張
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/07_notion_ai_document_enhancement.md
   - CPF 75%、既存ユーザー基盤活用、ARR $10B目標

8. **Runway ML** - 動画生成需要
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/08_runway_video_generation.md
   - CPF 85%、クリエイター特化、$1.5B評価額

9. **ElevenLabs** - 音声合成需要
   - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/09_elevenlabs_voice_synthesis.md
   - CPF 90%、多言語対応、月額$1M ARR

10. **Claude by Anthropic** - 長文処理需要
    - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/10_claude_long_context.md
    - CPF 78%、安全性差別化、200K context window

11. **Grammarly AI** - ライティング支援
    - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/11_grammarly_writing_assist.md
    - CPF 82%、既存製品AI強化、30M DAU

12. **Otter.ai** - 文字起こし需要
    - 参照: @Founder_Agent_ForGenAI/research/case_studies/tier2/discover-demand/12_otter_transcription.md
    - CPF 80%、リアルタイム処理、Zoom統合

---

## 使用例

```
User: /discover-demand

Skill: 探索分野キーワードを入力してください（省略可、例: "AI画像生成", "プロンプト最適化"）:

User: プロンプト最適化

Skill:
# 需要発見リサーチ 自律実行開始（ForGenAI版）

探索分野: 「プロンプト最適化」

[自動実行中...]
- STEP 1: 検索クエリ生成 ✅ (GenAI特化クエリ10個)
- STEP 2: 生ログ収集（Reddit r/ChatGPT） ✅ (15件)
- STEP 3: Product Hunt市場調査 ✅ (過去3ヶ月AI製品分析)
- STEP 4: 需要候補構造化 ✅ (8候補)
- STEP 5: 5軸スコアリング ✅ (AI差別化軸含む)
- STEP 6: Product Hunt適合性評価 ✅
- STEP 7: AI技術スタック選定 ✅ (OpenAI GPT-4o推奨)
- STEP 8: プロンプトパターン評価 ✅ (Chain-of-Thought 5/5)
- STEP 9: GenAI_Research統合 ✅ (Perplexity AI事例参照)
- STEP 10: 解決アイデア生成 ✅
- STEP 11: マネタイズ仮説 ✅ (SaaS $20/月、ARR $1M目標)
- STEP 12: 成果物出力 ✅

## 完了

成果物: demand_discovery_forgenai.md
最有望候補: 「プロンプトテンプレート管理ツール」(スコア: 23/25)
- CPFスコア: 92%
- AI差別化軸: 5/5（独自Chain-of-Thoughtパターン、Few-shot例示）
- Product Hunt: #1獲得可能性高（火曜ローンチ、Hunter確保済み）
- AI技術スタック: OpenAI GPT-4o（精度優先）
- ARR目標: Year 1 $100K → Year 3 $10M

推奨: `/create-mvv` でMVV定義 → `/validate-cpf` でCPFスコア70%以上を目指す
```

---

## 改訂履歴

| 日付 | バージョン | 変更内容 |
|------|-----------|---------|
| 2026-01-02 | 1.0 | ForGenAI版初版作成（Origin版からカスタマイズ） |

**変更点**:
- 5軸評価に変更（AI差別化軸を追加）
- 合格基準を18/25点に厳格化（CPF 70%）
- Product Hunt適合性評価を追加（#1獲得戦略）
- AI技術スタック選定を追加（OpenAI vs Anthropic vs Gemini）
- プロンプトパターン評価を追加（Chain-of-Thought、Few-shot等）
- GenAI_Research統合（12件の成功事例）
- Tier 2ケーススタディ12件作成予定
