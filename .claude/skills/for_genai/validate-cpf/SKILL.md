---
skill_id: for-genai-validate-cpf
skill_name: CPF Validation (ForGenAI)
domain: ForGenAI
phase: 1_initiating
category: validation
origin: for_startup
cpf_threshold: 70%
quality_target: 95/100
version: 1.0.0
last_updated: 2026-01-02
dependencies:
  - for-genai-discover-demand
  - for-genai-create-mvv
integration_sources:
  - GenAI_research/case_studies/
  - GenAI_research/LLM/01_LifeisBeautiful_insights.md
  - GenAI_research/use_cases/
output_path: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/2_discovery/cpf_judgment_forgenai.md
---

# Validate CPF Skill (ForGenAI Edition)

**生成AI特化版CPF検証スキル** - AI市場競争の激しさを反映し、70%閾値を採用。Product Hunt戦略、AI技術スタック、プロンプト品質を統合した総合判定。

---

## このSkillでできること

1. **成果物統合**: persona.md, interview_simulation.md, problem_research.md を読み込み
2. **GenAI特化4指標評価**: AI差別化軸を含む厳格判定
3. **3Uスコア厳格化**: Unworkable/Unavoidable/Urgentすべて8点以上（AI市場基準）
4. **AI特化定量データ抽出**: API呼び出し頻度、プロンプト失敗率、コスト削減額
5. **GenAI成功事例ベンチマーク**: ChatGPT 95%、Perplexity 95%、Midjourney 90%との比較
6. **Product Hunt準備度評価**: #1獲得可能性スコアリング
7. **総合判定**: CPF達成/要改善/見直しの判断（AI市場競争を考慮）
8. **次ステップ提案**: PSF検証 or Product Hunt戦略 or AI技術スタック再選定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `persona.md`, `interview_simulation.md`, `problem_research.md`, `demand_discovery_forgenai.md` |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/2_discovery/cpf_judgment_forgenai.md` |
| **次のSkill** | `/research-competitors` → `/validate-10x` → `/create-producthunt-strategy`（CPF達成時） |
| **ステージ** | CPF検証（AI市場基準、70%閾値） |

---

## CPF達成基準（ForGenAI版：AI市場競争激化対応）

| 指標 | 目標値 | 測定方法 | Origin基準からの変更 |
|------|--------|----------|---------------------|
| **インタビュー数** | **30人以上** | 実インタビュー + 仮想インタビュー | 20人 → **30人**（競合多数のため統計強化） |
| **課題共通率** | **70%以上** | 同じ課題を挙げた割合 | **変更なし**（AI市場も同基準） |
| **支払い意思（WTP）** | **65%以上** | 「お金を払ってでも解決したい」回答率 | 50% → **65%**（Free AI toolsとの競合考慮） |
| **緊急性スコア** | **平均8.5/10以上** | 「今すぐ解決したい」度合い | 7/10 → **8.5/10**（AI技術進化速度の速さ） |
| **AI差別化スコア** | **平均8/10以上** | 「既存AI toolsでは解決不可」度合い | **新規追加**（GenAI特有） |

### ForGenAI特有の変更点

1. **WTP基準上昇（50% → 65%）**:
   - 理由: ChatGPT, Claude, Gemini等の無料プランとの競合
   - 対策: 明確な差別化価値を証明する必要あり

2. **緊急性スコア上昇（7/10 → 8.5/10）**:
   - 理由: AI技術進化が速く、「今解決しないと手遅れ」感が重要
   - 例: GPT-3.5 → GPT-4 → GPT-4o の進化速度（6ヶ月サイクル）

3. **AI差別化スコア追加（新規）**:
   - 理由: 「AI Wrapper」批判への対応
   - 評価: 既存AIツール（ChatGPT/Claude/Gemini）では解決できない理由の明確化

---

## 3Uスコア厳格基準（ForGenAI専用）

| 要素 | 基準点数 | 評価基準 | Origin基準からの変更 |
|------|---------|---------|---------------------|
| **Unworkable（切実性）** | **8点以上** | 「このAI機能がないと、業務が止まる」レベル | 6点 → **8点** |
| **Unavoidable（不可避性）** | **8点以上** | 「ChatGPT/Claude/Geminiでは解決できない」レベル | 6点 → **8点** |
| **Urgent（今すぐ性）** | **8.5点以上** | 「今月中に解決しないと機会損失」レベル | 6点 → **8.5点**（AI進化速度） |

**AI市場での重要性**:
- 3Uすべて8点以上 = **Product Hunt #1獲得可能性あり**（課題の深刻さが証明されている）
- 1つでも7点以下 = **要改善**（既存AIツールで代替可能な可能性）

---

## GenAI特化定量データ抽出

インタビュー結果から以下のGenAI特化定量データを必ず抽出し、レポートに記載：

### 抽出項目

| 項目 | 抽出方法 | 例 | AI市場での重要性 |
|------|---------|-----|----------------|
| **API呼び出し頻度** | 「週に何回AIに質問するか？」 | 週20回、月100回等 | 高頻度 = 高収益可能性 |
| **プロンプト失敗率** | 「AIが期待通りの回答をしない割合」 | 30%、50%等 | 高失敗率 = 改善ニーズあり |
| **コスト削減額** | 「このAIツールで月いくらコスト削減できるか？」 | 月5万円、年100万円等 | 大きな削減 = 高WTP |
| **時間削減率** | 「AIで作業時間が何%削減されるか？」 | 50%、80%等 | 高削減率 = 生産性インパクト大 |
| **支払い意思額（WTP金額）** | 「月額いくらまで払える？」 | 月額$10〜$50等 | ChatGPT Plus $20を上回るか？ |
| **Product Hunt Upvote意欲** | 「Product Huntで見かけたら投票するか？」 | 80%以上推奨 | #1獲得可能性の指標 |

**AI市場での重要性**:
- **API呼び出し頻度**: 週20回以上 = ヘビーユーザー、収益化可能
- **プロンプト失敗率**: 30%以上 = 既存AIツールの限界、改善ニーズあり
- **WTP**: $20以上 = ChatGPT Plusを上回る価値提供が必須

---

## Domain-Specific Knowledge (from GenAI_Research)

### Success Patterns（成功パターン）

#### 事例1: ChatGPT（CPFスコア 95/100）
- **課題の共通性**: 95%（100M+ MAU獲得、2ヶ月達成）
- **問題**: 「情報検索が遅い」「質問に対して的確な回答が得られない」
- **検証方法**: InstructGPTでの実験データ、APIユーザーのフィードバック
- **WTP確認**: ChatGPT Plus $20/月、150M+ subscribers
- **緊急性**: 9/10（情報アクセスの即時性需要）
- **AI差別化**: 10/10（GPT-3.5時点で他AIを大きく上回る精度）

**学習ポイント**:
- API提供で実データ蓄積 → 課題検証の精度向上
- フリーミアム戦略でWTP検証（Plus $20/月で収益化）

#### 事例2: Perplexity AI（CPFスコア 95/100）
- **課題の共通性**: 90%（検索結果の信頼性不足）
- **問題**: 「Googleで調べても信頼できる情報か不明」「複数サイト確認が面倒」
- **検証方法**: Twitter/Reddit/Hacker Newsでの需要分析
- **WTP確認**: Perplexity Pro $20/月、Product Hunt #1獲得（3,200 upvotes）
- **緊急性**: 9/10（情報の信頼性は即座の需要）
- **AI差別化**: 9/10（Citation機能で差別化、ChatGPTにない機能）

**学習ポイント**:
- Product Hunt #1獲得で初期ユーザー爆発的獲得
- Citation（引用）機能で信頼性を差別化
- Twitter/Reddit/Hacker Newsでの需要分析が有効

#### 事例3: Midjourney（CPFスコア 90/100）
- **課題の共通性**: 95%（非デザイナーのビジュアル作成困難）
- **問題**: 「デザインスキルがないとビジュアル作れない」「Photoshop高額・複雑」
- **検証方法**: Discord beta testing、クリエイターコミュニティでのフィードバック
- **WTP確認**: $10/月〜$60/月、$200M monthly revenue
- **緊急性**: 8/10（クリエイティブ制作の需要）
- **AI差別化**: 10/10（V4/V5モデルで他AI画像生成を圧倒）

**学習ポイント**:
- Discordでのbeta testing → コミュニティ主導の検証
- 非技術者向けUI最適化（プロンプト自動補完）
- 月額課金モデルで安定収益

#### 事例4: Jasper AI（CPFスコア 88/100）
- **課題の共通性**: 85%（マーケティングコンテンツ作成の時間不足）
- **問題**: 「ブログ記事・広告文の作成に週10時間かかる」
- **検証方法**: マーケターコミュニティでのインタビュー50人以上
- **WTP確認**: $49/月〜$125/月、$75M ARR達成
- **緊急性**: 8.5/10（コンテンツマーケティングの即時需要）
- **AI差別化**: 8/10（マーケティング特化プロンプトテンプレート）

**学習ポイント**:
- 特定職種（マーケター）への深い特化
- Product Hunt #2獲得（#1には及ばずも成功）
- テンプレートライブラリで差別化

#### 事例5: Character.AI（CPFスコア 92/100）
- **課題の共通性**: 95%（エンタメ不足、創造的会話相手不在）
- **問題**: 「AIキャラクターと自由に会話したい」「既存チャットボットは単調」
- **検証方法**: Reddit/Discord/TikTokでの需要分析
- **WTP確認**: Character.AI+ $9.99/月、100M+ MAU
- **緊急性**: 7/10（エンタメ需要、緊急性は相対的に低い）
- **AI差別化**: 9/10（キャラクター作成の自由度、ChatGPTにない機能）

**学習ポイント**:
- エンタメ領域でも高CPF達成可能（緊急性7/10でも成功）
- TikTokでのバイラル拡散戦略
- キャラクター作成の自由度で差別化

### Common Pitfalls（失敗パターン）

#### 失敗パターン1: 「AI Wrapper」批判への対応不足
- **教訓**: OpenAI APIをUI化しただけでは差別化不足
- **対策**: 独自プロンプト最適化、ドメイン特化データ、統合価値の明示

#### 失敗パターン2: 無料AIツールとの競合無視
- **教訓**: ChatGPT無料版、Claude無料版、Gemini無料版との差別化が必須
- **対策**: WTP 65%以上、明確な有料化理由（速度、精度、機能）

#### 失敗パターン3: Product Hunt戦略の欠如
- **教訓**: GenAI領域ではProduct Hunt #1が初期成長の鍵
- **対策**: #1獲得可能性スコアリング、Hunter確保、事前コミュニティ構築

#### 失敗パターン4: プロンプト品質の軽視
- **教訓**: プロンプト失敗率30%以上だとユーザー離脱
- **対策**: Few-shot学習、Chain-of-Thought、プロンプト自動最適化

### Quantitative Benchmarks（定量的評価基準）

| 指標 | ForGenAI基準 | Origin基準 | GenAI成功事例 | 出典 |
|------|------------|-----------|-------------|------|
| CPFスコア | **70%以上** | 60%以上 | ChatGPT 95%, Perplexity 95%, Midjourney 90% | @GenAI_research/case_studies/ |
| インタビュー数 | **30人以上** | 20人以上 | Jasper 50人以上 | @GenAI_research/case_studies/Jasper.md |
| 課題共通率 | **70%以上** | 70%以上 | ChatGPT 95%, Perplexity 90% | @GenAI_research/case_studies/ |
| 支払い意思（WTP） | **65%以上** | 50%以上 | ChatGPT Plus 150M+ subscribers | @GenAI_research/case_studies/ChatGPT.md |
| 緊急性スコア | **8.5/10以上** | 7/10以上 | ChatGPT 9/10, Perplexity 9/10 | @GenAI_research/case_studies/ |
| AI差別化スコア | **8/10以上** | なし | Perplexity 9/10（Citation）、Midjourney 10/10 | @GenAI_research/case_studies/ |
| Product Hunt Upvotes | **3,000+** | なし | Perplexity 3,200, Notion AI 2,800 | @GenAI_research/case_studies/Perplexity.md |

### Best Practices（ベストプラクティス）

1. **API提供での実データ蓄積**（ChatGPT、Anthropic Claude）
   - API経由でユーザーフィードバック収集
   - 実際の使用パターンからCPF検証精度向上

2. **Product Hunt #1獲得戦略**（Perplexity、Notion AI）
   - Tuesday-Thursday PST 0:01投稿
   - 影響力あるHunter確保
   - 事前X/Twitterコミュニティ構築

3. **Discord/Slackコミュニティでのbeta testing**（Midjourney、Character.AI）
   - リアルタイムフィードバック収集
   - コミュニティ主導の検証

4. **特定職種への深い特化**（Jasper AI、GitHub Copilot）
   - マーケター、開発者等への専門化
   - テンプレート・ワークフロー最適化

### Tier 2 ケーススタディ（研究ナレッジベース統合）

**CPF検証の実例12社**:
スキル実行時、以下のケーススタディから類似業界・検証手法を参照して精度を向上させます。

#### 高CPFスコア（90-95%）- AI市場で圧倒的成功

1. **[ChatGPT]** (CPF 95%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_001_chatgpt.md
   - 100M MAU in 2 months、WTP: ChatGPT Plus $20/月 150M+ subscribers
   - API提供で実データ蓄積、InstructGPTでの検証

2. **[Perplexity AI]** (CPF 95%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_002_perplexity.md
   - Product Hunt #1獲得（3,200 upvotes）、Citation機能で差別化
   - Twitter/Reddit/Hacker Newsでの需要分析

3. **[Midjourney]** (CPF 90%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_003_midjourney.md
   - $200M monthly revenue、Discord beta testing
   - 非デザイナー向けUI最適化

4. **[Character.AI]** (CPF 92%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_004_character_ai.md
   - 100M+ MAU、TikTokバイラル拡散
   - キャラクター作成の自由度で差別化

5. **[Shopify]** (CPF 95%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_009_shopify.md
   - Snowboards販売の実体験、課題共通率95%
   - EC参入障壁の解消

6. **[Stripe]** (CPF 95%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_008_stripe.md
   - 決済統合の複雑さ、緊急性9/10
   - 開発者特化

#### 中CPFスコア（85-90%）- AI市場で成功

7. **[Jasper AI]** (CPF 88%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_005_jasper.md
   - $75M ARR、マーケター特化
   - Product Hunt #2、テンプレートライブラリ

8. **[GitHub Copilot]** (CPF 88%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_006_copilot.md
   - $10/月、10x developer productivity
   - VS Code統合の徹底

9. **[Notion AI]** (CPF 75%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_007_notion_ai.md
   - Product Hunt #3（2,800 upvotes）、既存ユーザー基盤活用
   - 複数ツール統合

10. **[Runway ML]** (CPF 85%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_010_runway.md
    - クリエイター特化、動画生成AI
    - Discord/Slackコミュニティ

11. **[ElevenLabs]** (CPF 90%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_011_elevenlabs.md
    - 多言語音声生成、15言語以上対応
    - API提供でB2B収益化

12. **[Grammarly AI]** (CPF 82%): @GenAI_research/case_studies/tier2/validate-cpf/GENAI_CPF_012_grammarly.md
    - 30M DAU、長期信頼構築
    - ライティング支援特化

### Reference
- 詳細: @GenAI_research/case_studies/
- AI市場基準: @GenAI_research/LLM/01_LifeisBeautiful_insights.md
- Product Hunt戦略: @GenAI_research/topics/llm/

---

## 判定基準（ForGenAI版）

### 個別指標判定

| 指標 | ✅ 達成 | ⚠️ 要改善 | ❌ 見直し |
|------|---------|-----------|----------|
| インタビュー数 | **30人以上** | 20-29人 | 19人以下 |
| 課題共通率 | **70%以上** | 60-69% | 60%未満 |
| 支払い意思 | **65%以上** | 55-64% | 55%未満 |
| 緊急性 | **8.5/10以上** | 7.5-8.4/10 | 7.5未満 |
| AI差別化スコア | **8/10以上** | 6-7.9/10 | 6未満 |
| 3Uスコア（Unworkable） | **8点以上** | 7点 | 6点以下 |
| 3Uスコア（Unavoidable） | **8点以上** | 7点 | 6点以下 |
| 3Uスコア（Urgent） | **8.5点以上** | 7.5-8.4点 | 7.5点以下 |
| Product Hunt準備度 | **80%以上** | 60-79% | 60%未満 |

### 総合判定

| 判定 | 条件 | 次のアクション |
|------|------|---------------|
| ✅ **CPF達成（AI市場基準）** | すべて✅ | PSF検証へ（/research-competitors）、Product Hunt戦略策定 |
| ⚠️ **要改善** | 3個以上⚠️ | 追加インタビュー30人、AI差別化軸の強化 |
| ❌ **見直し** | 1個以上❌ | 課題仮説を根本から再検討、既存AIツールとの差別化再定義 |

---

## Product Hunt準備度評価（ForGenAI新機能）

CPF検証と同時に、Product Hunt #1獲得可能性をスコアリングします。

### 評価項目（各10点、合計80点以上で#1獲得可能）

| 項目 | 10点 | 5点 | 0点 |
|------|------|-----|-----|
| **Hunter確保** | 影響力あるHunter確保済み | Hunter候補あり | Hunter未確保 |
| **事前コミュニティ** | X/Twitter 1,000+ followers | 100-999 followers | 100未満 |
| **ローンチタイミング** | Tuesday-Thursday PST 0:01確約 | 曜日のみ確定 | 未定 |
| **デモ動画品質** | プロ品質、90秒以内 | 自作、2分以内 | 動画なし |
| **差別化明確性** | 一文で差別化説明可能 | やや説明必要 | 差別化不明確 |
| **WTP実績** | 有料ユーザー10人以上 | 5-9人 | 0-4人 |
| **プロンプト品質** | 失敗率10%以下 | 20-30% | 30%以上 |
| **AI技術スタック** | OpenAI GPT-4o + 独自最適化 | GPT-4o標準 | GPT-3.5 |

**総合判定**:
- **80点以上**: Product Hunt #1獲得可能性が高い
- **60-79点**: #3以内獲得可能性あり、要改善
- **60点未満**: Product Hunt戦略の再検討が必要

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
- **標準エラーレスポンス**: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式

---

## Instructions

### 自動実行フロー

**STEP 1: 成果物読み込み**
- `persona.md` → ペルソナ情報
- `interview_simulation.md` → 仮想インタビュー結果、3U検証スコア
- `problem_research.md` → 課題裏付けスコア
- `demand_discovery_forgenai.md` → AI差別化軸スコア

**STEP 2: インタビュー数の集計（ForGenAI基準：30人以上）**
- 実インタビュー数（もしあれば）
- 仮想インタビューのペルソナ数
- 課題裏付け調査の生ログ件数から推定
- **判定**: 30人以上 = ✅、20-29人 = ⚠️、19人以下 = ❌

**STEP 3: 課題共通率の算出（ForGenAI基準：70%以上）**
- 複数ペルソナ/生ログから共通課題の割合を計算
- 例: 30人中24人が同じ課題 → 80%（✅）
- 例: 30人中20人が同じ課題 → 67%（⚠️）

**STEP 4: 支払い意思（WTP）の評価（ForGenAI基準：65%以上）**
- インタビュー結果から「お金を払う」回答を抽出
- WTP金額の中央値・範囲も記録
- **無料AIツールとの比較**: ChatGPT無料版で十分か？ を確認
- **定量データ抽出**: 月額いくらまで払えるか？（$20以上推奨）

**STEP 5: 緊急性スコアの算出（ForGenAI基準：8.5/10以上）**
- 3U検証の「Urgent」スコア
- 生ログの「今すぐ」「早く」「手遅れになる」表現の頻度
- **AI進化速度考慮**: 「今解決しないと、GPT-5リリースで手遅れ」等の緊迫感
- **判定**: 8.5/10以上 = ✅、7.5-8.4/10 = ⚠️、7.5未満 = ❌

**STEP 6: AI差別化スコアの評価（ForGenAI新機能、8/10以上）**
- 既存AIツール（ChatGPT/Claude/Gemini）では解決できない理由
- 独自プロンプト最適化、ドメイン特化データ、統合価値の明示
- **判定**: 8/10以上 = ✅、6-7.9/10 = ⚠️、6未満 = ❌（AI Wrapper批判リスク）

**STEP 7: 3Uスコアの厳格評価（ForGenAI基準）**
- **Unworkable（切実性）**: 8点以上 = ✅、7点 = ⚠️、6点以下 = ❌
- **Unavoidable（不可避性）**: 8点以上 = ✅、7点 = ⚠️、6点以下 = ❌
- **Urgent（今すぐ性）**: 8.5点以上 = ✅、7.5-8.4点 = ⚠️、7.5点以下 = ❌

**STEP 8: GenAI特化定量データの抽出と評価（ForGenAI新機能）**
- API呼び出し頻度（週/月）
- プロンプト失敗率（%）
- コスト削減額（月額/年額）
- 時間削減率（%）
- 支払い意思額（WTP金額、$20以上推奨）
- Product Hunt Upvote意欲（80%以上推奨）

**STEP 9: Product Hunt準備度評価（ForGenAI新機能）**
- Hunter確保状況
- 事前X/Twitterコミュニティ（followers数）
- ローンチタイミング（Tuesday-Thursday PST 0:01）
- デモ動画品質
- 差別化明確性
- WTP実績（有料ユーザー数）
- プロンプト品質（失敗率）
- AI技術スタック（GPT-4o vs GPT-3.5）
- **総合判定**: 80点以上 = #1獲得可能性あり

**STEP 10: 総合判定**
- 9指標（インタビュー数、課題共通率、WTP、緊急性、AI差別化、3U×3、Product Hunt準備度）の個別判定
- 総合CPF達成判定（AI市場基準）
- 次ステップの提案

**STEP 11: 成果物出力**
- ツール: Write
- パス: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/2_discovery/cpf_judgment_forgenai.md`

---

## 成果物フォーマット

```markdown
# CPF判定レポート（ForGenAI版）

**作成日**: [YYYY-MM-DD]
**対象ソリューション**: [ソリューション名]
**総合判定**: ✅ CPF達成（AI市場基準） / ⚠️ 要改善 / ❌ 見直し

---

## エグゼクティブサマリー

| 指標 | 目標 | 実績 | 判定 | GenAIベンチマーク |
|------|------|------|:----:|-----------------|
| インタビュー数 | 30人以上 | XX人 | ✅/⚠️/❌ | Jasper 50人以上 |
| 課題共通率 | 70%以上 | XX% | ✅/⚠️/❌ | ChatGPT 95%, Perplexity 90% |
| 支払い意思（WTP） | 65%以上 | XX% | ✅/⚠️/❌ | ChatGPT Plus 150M+ subscribers |
| 緊急性スコア | 8.5/10以上 | X.X/10 | ✅/⚠️/❌ | ChatGPT 9/10, Perplexity 9/10 |
| AI差別化スコア | 8/10以上 | X.X/10 | ✅/⚠️/❌ | Perplexity 9/10（Citation） |
| 3Uスコア（Unworkable） | 8点以上 | X/10 | ✅/⚠️/❌ | - |
| 3Uスコア（Unavoidable） | 8点以上 | X/10 | ✅/⚠️/❌ | - |
| 3Uスコア（Urgent） | 8.5点以上 | X/10 | ✅/⚠️/❌ | - |
| Product Hunt準備度 | 80点以上 | XX/80 | ✅/⚠️/❌ | Perplexity #1（3,200 upvotes） |

**総合判定**: [判定とその理由]

---

## 詳細分析

### 1. インタビュー分析

| 種別 | 件数 |
|------|------|
| 実インタビュー | X人 |
| 仮想インタビュー | X人 |
| 課題裏付け生ログ | X件 |
| **合計** | **XX件** |

**評価**: [インタビュー数の評価とコメント]

**AI市場基準との比較**:
- 30人以上 → ✅ AI市場競争に対応可能
- 20-29人 → ⚠️ 追加インタビュー推奨
- 19人以下 → ❌ 統計的有意性不足、競合多数のAI市場で不利

---

### 2. 課題共通率

**特定された共通課題（Top 3）**:

| 順位 | 課題 | 出現率 | 既存AIツールで解決可能か？ |
|:----:|------|:------:|----------------------|
| 1 | [課題1] | XX% | [ChatGPT/Claude/Geminiで解決可or不可] |
| 2 | [課題2] | XX% | [ChatGPT/Claude/Geminiで解決可or不可] |
| 3 | [課題3] | XX% | [ChatGPT/Claude/Geminiで解決可or不可] |

**課題共通率**: XX%（目標70%以上）

**評価**: [課題共通率の評価とコメント]

**GenAIベンチマーク比較**:
- ChatGPT: 95%（情報検索の課題）
- Perplexity: 90%（検索結果の信頼性不足）
- Midjourney: 95%（非デザイナーのビジュアル作成困難）

---

### 3. 支払い意思（WTP）

**WTP分布**:

| 回答 | 人数 | 割合 |
|------|------|------|
| 「絶対払う」 | X人 | XX% |
| 「おそらく払う」 | X人 | XX% |
| 「ChatGPT無料版で十分」 | X人 | XX% |

**WTP金額（中央値）**: 月額$XX
**WTP金額（範囲）**: $XX〜$XX

**評価**: [WTPの評価とコメント]

**無料AIツールとの競合分析**:
- ChatGPT無料版で十分 → ❌ 差別化不足
- ChatGPT Plus $20を上回るWTP → ✅ 有料化可能
- ChatGPT Plus $20未満のWTP → ⚠️ 価格戦略要検討

**GenAIベンチマーク比較**:
- ChatGPT Plus: $20/月、150M+ subscribers
- Perplexity Pro: $20/月
- Jasper AI: $49/月〜$125/月

---

### 4. 緊急性スコア

**3U検証結果**:

| 要素 | スコア | 目標 | 評価 | AI進化速度考慮 |
|------|:------:|:----:|:----:|--------------|
| Unworkable（切実性） | X/10 | 8点以上 | ✅/⚠️/❌ | [AI機能がないと業務停止] |
| Unavoidable（不可避性） | X/10 | 8点以上 | ✅/⚠️/❌ | [ChatGPT/Claude/Geminiで代替不可] |
| Urgent（今すぐ性） | X/10 | 8.5点以上 | ✅/⚠️/❌ | [GPT-5リリース前に解決必須] |

**緊急性平均スコア**: X.X/10

**評価**: [緊急性の評価とコメント]

**GenAIベンチマーク比較**:
- ChatGPT: 9/10（情報アクセスの即時性需要）
- Perplexity: 9/10（情報の信頼性は即座の需要）
- Midjourney: 8/10（クリエイティブ制作の需要）

---

### 5. AI差別化スコア（ForGenAI新機能）

**差別化ポイント**:

| 差別化軸 | スコア | 既存AIツールとの比較 |
|---------|:------:|------------------|
| 独自プロンプト最適化 | X/10 | [ChatGPT標準プロンプトとの差] |
| ドメイン特化データ | X/10 | [汎用LLMにないデータ] |
| 統合価値（複数AI統合） | X/10 | [ChatGPT単体にない価値] |
| UX最適化（非技術者向け） | X/10 | [プロンプト自動補完等] |

**AI差別化総合スコア**: X.X/10（目標8/10以上）

**評価**: [AI差別化の評価とコメント]

**「AI Wrapper」批判への対応**:
- 8/10以上 → ✅ 明確な差別化あり
- 6-7.9/10 → ⚠️ 差別化軸の強化が必要
- 6未満 → ❌ AI Wrapper批判リスク、根本的再検討

---

### 6. GenAI特化定量データ分析（ForGenAI新機能）

#### API呼び出し頻度

| 頻度区分 | 人数 | 割合 |
|---------|------|------|
| 週20回以上 | X人 | XX% |
| 週10-19回 | X人 | XX% |
| 週5-9回 | X人 | XX% |
| 週5回未満 | X人 | XX% |

**平均頻度**: 週X回、月X回

**評価**: [頻度の評価とAI市場での重要性]

---

#### プロンプト失敗率

| 失敗率区分 | 人数 | 割合 |
|-----------|------|------|
| 50%以上 | X人 | XX% |
| 30-49% | X人 | XX% |
| 10-29% | X人 | XX% |
| 10%未満 | X人 | XX% |

**平均失敗率**: XX%

**評価**: [失敗率の評価と改善ニーズ]
- 30%以上 → ✅ 既存AIツールの限界、改善ニーズあり
- 10-29% → ⚠️ 一部改善余地あり
- 10%未満 → ❌ 既存AIツールで十分の可能性

---

#### コスト削減額

| 削減額区分 | 人数 | 割合 |
|-----------|------|------|
| 月10万円以上 | X人 | XX% |
| 月5-10万円 | X人 | XX% |
| 月1-5万円 | X人 | XX% |
| 月1万円未満 | X人 | XX% |

**平均削減額**: 月額X万円、年額X万円

**評価**: [コスト削減の評価とWTPとの相関]

---

#### 時間削減率

| 削減率区分 | 人数 | 割合 |
|-----------|------|------|
| 80%以上 | X人 | XX% |
| 50-79% | X人 | XX% |
| 30-49% | X人 | XX% |
| 30%未満 | X人 | XX% |

**平均削減率**: XX%

**評価**: [時間削減率の評価と生産性インパクト]

---

### 7. Product Hunt準備度評価（ForGenAI新機能）

| 評価項目 | スコア | 詳細 |
|---------|:------:|------|
| Hunter確保 | X/10 | [Hunter名、影響力] |
| 事前コミュニティ | X/10 | [X/Twitter followers数] |
| ローンチタイミング | X/10 | [Tuesday-Thursday PST 0:01確約] |
| デモ動画品質 | X/10 | [品質、長さ] |
| 差別化明確性 | X/10 | [一文説明可能性] |
| WTP実績 | X/10 | [有料ユーザー数] |
| プロンプト品質 | X/10 | [失敗率] |
| AI技術スタック | X/10 | [GPT-4o vs GPT-3.5] |

**Product Hunt準備度総合スコア**: XX/80

**評価**: [Product Hunt #1獲得可能性の評価]
- 80点以上 → ✅ Product Hunt #1獲得可能性が高い
- 60-79点 → ⚠️ #3以内獲得可能性あり、要改善
- 60点未満 → ❌ Product Hunt戦略の再検討が必要

---

## CPF達成判定

### 判定結果: [✅ CPF達成（AI市場基準） / ⚠️ 要改善 / ❌ 見直し]

**判定理由**:
[具体的な理由を記述]

**AI市場での訴求ポイント**:
1. [訴求ポイント1]
2. [訴求ポイント2]
3. [訴求ポイント3]

**既存AIツールとの差別化**:
- ChatGPT無料版との差: [差別化ポイント]
- ChatGPT Plusとの差: [差別化ポイント]
- Claude/Geminiとの差: [差別化ポイント]

---

## 改善提案（要改善/見直しの場合）

### 改善が必要な項目

| 指標 | 現状 | 目標 | 改善案 |
|------|------|------|--------|
| [指標1] | XX | XX | [改善案] |
| [指標2] | XX | XX | [改善案] |

### 具体的アクション

1. [アクション1]
2. [アクション2]
3. [アクション3]

---

## 次のステップ

### CPF達成の場合

| コマンド | 内容 |
|----------|------|
| `/research-competitors` | 競合調査へ（PSF検証開始、ChatGPT/Claude/Gemini分析） |
| `/validate-10x` | 10倍検証へ（3軸以上の優位性証明、AI差別化軸含む） |
| `/create-producthunt-strategy` | Product Hunt #1獲得戦略策定 |
| `/select-ai-tech-stack` | AI技術スタック最終決定（GPT-4o vs Claude vs Gemini） |

### 要改善/見直しの場合

| コマンド | 内容 |
|----------|------|
| `/simulate-interview` | 追加インタビュー実施（30人以上を目指す） |
| `/create-persona` | ペルソナ再定義（AI差別化軸の強化） |
| `/discover-demand` | 別の課題を探索（既存AIツールで解決できない課題） |
| `/build-prompt-library` | プロンプト品質改善（失敗率30%以下を目指す） |

---

## 参照成果物

| ファイル | 作成日 |
|----------|--------|
| persona.md | [日付] |
| interview_simulation.md | [日付] |
| problem_research.md | [日付] |
| demand_discovery_forgenai.md | [日付] |
```

---

## 使用例

```
User: /validate-cpf

Skill:
# CPF判定 自律実行開始（ForGenAI版 - AI市場基準）

入力ファイル読み込み中...
- persona.md ✅
- interview_simulation.md ✅
- problem_research.md ✅
- demand_discovery_forgenai.md ✅

[自動判定中...]
- STEP 1: 成果物読み込み ✅
- STEP 2: インタビュー数集計 ✅ (35件 - AI市場基準達成)
- STEP 3: 課題共通率算出 ✅ (85% - ChatGPT 95%に近い)
- STEP 4: WTP評価 ✅ (72% - AI市場基準達成、ChatGPT Plus $20超え)
- STEP 5: 緊急性スコア算出 ✅ (8.8/10 - Perplexity 9/10に近い)
- STEP 6: AI差別化スコア評価 ✅ (8.5/10 - Citation機能で差別化)
- STEP 7: 3Uスコア厳格評価 ✅ (Unworkable 8.5, Unavoidable 8.2, Urgent 9.0)
- STEP 8: GenAI特化定量データ抽出 ✅ (API頻度週25回、失敗率35%、コスト削減月8万円)
- STEP 9: Product Hunt準備度評価 ✅ (78/80 - #1獲得可能性あり)
- STEP 10: 総合判定 ✅
- STEP 11: 成果物出力 ✅

## 完了

成果物: cpf_judgment_forgenai.md
総合判定: ✅ CPF達成（AI市場基準）

| 指標 | 実績 | 判定 | GenAIベンチマーク |
|------|------|:----:|-----------------|
| インタビュー数 | 35人 | ✅ | Jasper 50人以上 |
| 課題共通率 | 85% | ✅ | ChatGPT 95%, Perplexity 90% |
| WTP | 72% | ✅ | ChatGPT Plus 150M+ subscribers |
| 緊急性 | 8.8/10 | ✅ | ChatGPT 9/10, Perplexity 9/10 |
| AI差別化 | 8.5/10 | ✅ | Perplexity 9/10（Citation） |
| 3Uスコア | すべて8点以上 | ✅ | - |
| Product Hunt準備度 | 78/80 | ✅ | Perplexity #1（3,200 upvotes） |

**AI市場での訴求ポイント**:
1. 課題共通率85%（ChatGPT 95%、Perplexity 90%に匹敵）
2. AI差別化スコア8.5/10（Citation機能で差別化、ChatGPTにない価値）
3. Product Hunt準備度78/80（#1獲得可能性が高い）

**既存AIツールとの差別化**:
- ChatGPT無料版との差: Citation機能、信頼性スコアリング
- ChatGPT Plusとの差: ドメイン特化プロンプト最適化、専門知識統合
- Claude/Geminiとの差: リアルタイム情報取得、複数ソース統合

推奨: `/research-competitors` で競合調査→PSF検証へ
　　　 `/create-producthunt-strategy` でProduct Hunt #1獲得戦略策定
```

---

## 注意事項

1. **実インタビューを推奨**: 仮想インタビューだけでなく実顧客への確認が理想（Jasper 50人以上）
2. **AI差別化を重視**: 「AI Wrapper」批判を避けるため、独自価値を明確化
3. **無料AIツールとの競合分析**: ChatGPT/Claude/Gemini無料版で十分か？ を必ず確認
4. **Product Hunt戦略の統合**: CPF検証とProduct Hunt準備度を同時評価
5. **プロンプト品質の重視**: 失敗率30%以下を目指す
6. **AI進化速度考慮**: 「今解決しないと手遅れ」感が重要

---

## 更新履歴

- 2026-01-02: ForGenAI版として新規作成（AI市場基準70%、AI差別化軸追加、Product Hunt準備度評価追加、GenAI成功事例12社統合）

