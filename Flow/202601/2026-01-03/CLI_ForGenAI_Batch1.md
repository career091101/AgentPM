# CLI System Prompt: ForGenAI Edition Phase 2 Batch 1 (優先6スキル)

## 推定実行時間
2-3時間

## プロジェクトコンテキスト

### 現在の状態
- **Phase 1**: 完了（プロジェクト構造、26コマンドファイル作成）
- **Quality Score**: 94/100
- **Phase 2-5**: 未実装

### プロジェクトパス
- ベースディレクトリ: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI`
- スキルディレクトリ: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai`
- コマンドディレクトリ: `/Users/yuichi/AIPM/aipm_v0/.claude/commands`
- Research参照: `{ベース}/GenAI_research`

### ForGenAI Edition の特徴
- **CPFスコア基準**: 70% (ForRecruit 50%より厳格)
- **ターゲット**: 生成AI特化のスタートアップ・新規事業
- **差別化ポイント**: AI技術スタック選定、Product Hunt戦略、プロンプト品質管理
- **Research Database**: AI技術トレンド、Product Hunt成功パターン、プロンプトライブラリ

---

## Task 1: 優先6スキル実装 - 推定2-3時間

### 優先スキルリスト
1. **discover-demand** - 需要発見（AI市場特化）
2. **validate-cpf** - Customer Problem Fit検証（70%基準）
3. **research-competitors** - 競合調査（AI製品ベンチマーク）
4. **validate-psf** - Problem Solution Fit検証
5. **design-pricing** - 価格設計（API従量課金対応）
6. **validate-pmf** - Product Market Fit検証

---

### 1.1 discover-demand スキル

**目的**: AI市場特化の需要発見

**実装手順**:

1. 既存スキルをコピー:
   ```bash
   cd /Users/yuichi/AIPM/aipm_v0/.claude/skills
   cp -r for_recruit/discover-demand for_genai/discover-demand
   ```

2. `SKILL.md` カスタマイズ:

   **GenAI特化の追加要素**:
   - **AI市場セグメント分析**:
     - B2B SaaS (企業向けAIツール)
     - Developer Tools (AI API/SDK)
     - Consumer Apps (AIチャットボット、画像生成等)
   - **技術トレンド調査**:
     - 最新LLMモデル（GPT-4, Claude 3.5, Gemini）
     - エージェントフレームワーク（LangChain, AutoGPT）
     - ベクトルDB（Pinecone, Weaviate）
   - **Product Hunt分析**:
     - AI製品の週次ランキング
     - 成功パターン（ローンチタイミング、Hunter確保）
   - **プロンプトユースケース特定**:
     - 課題解決型（文書要約、翻訳、コード生成）
     - クリエイティブ型（画像生成、動画編集）

   **質問項目追加**:
   ```markdown
   ### GenAI特化質問
   1. このAI機能は既存SaaSに統合されますか、それともスタンドアロンですか？
   2. 使用予定のLLMモデルは？（GPT-4, Claude, Gemini, オープンソース）
   3. プロンプトエンジニアリングの複雑度は？（シンプル vs Chain-of-Thought）
   4. Product Huntでのローンチを計画していますか？
   ```

   **Research統合**:
   ```markdown
   ## Domain-Specific Knowledge (from GenAI_research)

   ### Success Patterns
   - **Perplexity**: 検索特化AIで$1B評価（2023年）
   - **Jasper**: コンテンツ生成AIで$1.5B調達（2022年）
   - **Notion AI**: 既存プロダクトへのAI統合成功例

   ### AI Market Trends 2026
   - エージェント型AI: 自律実行タスクの需要増加
   - マルチモーダルAI: テキスト+画像+音声統合
   - オンデバイスAI: プライバシー重視の小型モデル

   ### Product Hunt AI Success Criteria
   - ローンチ曜日: 火〜木（月金は避ける）
   - Hunter確保: トップHunter（500+ followers）
   - 事前コミュニティ参加: 3ヶ月前から活動

   ### Reference
   - 詳細: @GenAI_research/market_analysis/ai_trends_2026.md
   ```

3. テスト実行:
   ```bash
   # スキル動作確認（ドライラン）
   claude code --skill for-genai-discover-demand --dry-run
   ```

---

### 1.2 validate-cpf スキル

**目的**: CPF検証（70%基準、AI市場特化）

**実装手順**:

1. 既存スキルをコピー:
   ```bash
   cp -r for_recruit/validate-cpf for_genai/validate-cpf
   ```

2. `SKILL.md` カスタマイズ:

   **評価基準の厳格化**:
   ```markdown
   ## CPF評価基準（ForGenAI: 70%以上で合格）

   | 評価項目 | 配点 | GenAI特化チェックポイント |
   |---------|------|-------------------------|
   | 問題の深刻度 | 25点 | AI未導入による業務時間の損失が定量化されているか |
   | 顧客規模 | 20点 | AI予算を持つ企業数（中小 vs エンタープライズ） |
   | 課題の頻度 | 20点 | 日次で発生する繰り返しタスクか |
   | 既存解決策の不満 | 20点 | 既存AIツールの精度・速度・コストに不満があるか |
   | AI適合性 | 15点 | LLMで自動化可能なタスクか（ルールベースでは不可） |

   **合格基準**: 70点以上（ForRecruitは50点）
   ```

   **GenAI特化質問**:
   ```markdown
   ### AI適合性チェック
   1. この課題はLLMで解決できますか？（ルールベース vs 推論必要）
   2. プロンプトで精度90%以上を達成できる見込みはありますか？
   3. API料金（$0.01/1Kトークン）で採算が取れますか？
   4. ファインチューニングが必要ですか？
   ```

   **Research統合**:
   ```markdown
   ## Domain-Specific Knowledge (from GenAI_research)

   ### CPF成功パターン (AI Products)
   - **高CPFスコア例**:
     - ChatGPT (95点): 情報検索・文書作成の圧倒的効率化
     - Midjourney (90点): デザイナー不足の解決
     - GitHub Copilot (88点): コーディング速度3倍化

   ### Common Pitfalls
   - **低精度問題**: プロンプトでの精度が80%未満（手動修正コスト大）
   - **API料金高騰**: 従量課金で月$1000超のユーザー離脱
   - **ハルシネーション**: 誤情報生成でクリティカル業務に不適

   ### Quantitative Benchmarks
   - CPFスコア70点以上: VC資金調達の最低ライン
   - AI精度90%以上: エンタープライズ導入の必須条件
   - API料金ROI 5倍以上: 持続可能な収益モデル

   ### Reference
   - 詳細: @GenAI_research/case_studies/high_cpf_ai_products.md
   ```

---

### 1.3 research-competitors スキル

**目的**: AI製品ベンチマーク競合調査

**実装手順**:

1. 既存スキルをコピー:
   ```bash
   cp -r for_recruit/research-competitors for_genai/research-competitors
   ```

2. `SKILL.md` カスタマイズ:

   **GenAI特化の競合分析軸**:
   ```markdown
   ## AI製品ベンチマーク項目

   | 分析項目 | 評価ポイント |
   |---------|------------|
   | **使用モデル** | GPT-4, Claude 3.5, Gemini, オープンソース |
   | **API料金** | 1Kトークンあたりの料金 |
   | **レスポンス速度** | 平均応答時間（秒） |
   | **精度** | ベンチマークスコア（MMLU, HumanEval等） |
   | **プロンプト戦略** | Zero-shot, Few-shot, Chain-of-Thought |
   | **ファインチューニング** | カスタムモデル提供の有無 |
   | **差別化** | 独自データ、特殊アルゴリズム、UI/UX |
   | **Product Hunt** | ランキング、Upvote数、Hunter |
   | **価格戦略** | Free tier, 従量課金, サブスク |
   ```

   **調査対象プラットフォーム**:
   ```markdown
   ### 主要調査先
   1. **Product Hunt**: AI製品の週次ランキング
   2. **There's An AI For That**: AI製品検索エンジン
   3. **AI Tool Directory**: カテゴリ別AI製品リスト
   4. **GitHub Trending**: オープンソースAIツール
   5. **Hacker News**: 技術者コミュニティの反応
   ```

   **Research統合**:
   ```markdown
   ## Domain-Specific Knowledge (from GenAI_research)

   ### Competitive Analysis Best Practices
   - **ベンチマーク比較表**: 5-10製品を横断比較
   - **プロンプト精度テスト**: 同一タスクでの精度比較
   - **API料金シミュレーション**: 月間10万リクエスト時の料金比較

   ### AI Product Positioning Map
   - X軸: 汎用性 ← → 特化性
   - Y軸: 低価格 ← → 高価格
   - プロット例: ChatGPT (汎用・高), Jasper (特化・高), Perplexity (特化・中)

   ### Reference
   - 詳細: @GenAI_research/competitive_analysis/ai_product_benchmarks.md
   ```

---

### 1.4 validate-psf スキル

**目的**: Problem Solution Fit検証（AIソリューション適合性）

**実装手順**:

1. 既存スキルをコピー:
   ```bash
   cp -r for_recruit/validate-psf for_genai/validate-psf
   ```

2. `SKILL.md` カスタマイズ:

   **GenAI特化のソリューション検証**:
   ```markdown
   ## PSF評価項目（GenAI特化）

   | 評価項目 | 配点 | GenAI特化チェック |
   |---------|------|-----------------|
   | AI精度 | 25点 | プロンプトでの精度90%以上達成見込み |
   | API料金 | 20点 | 月間$100以下で1000ユーザー対応可能 |
   | レスポンス速度 | 15点 | 3秒以内の応答（ストリーミング対応） |
   | プロンプト複雑度 | 15点 | ユーザーがプロンプトを理解・修正可能 |
   | スケーラビリティ | 15点 | 10万リクエスト/日に対応可能 |
   | 差別化 | 10点 | 既存AI製品と明確に異なる価値提供 |

   **合格基準**: 70点以上
   ```

   **GenAI特化質問**:
   ```markdown
   ### AIソリューション検証
   1. プロトタイプでの精度は？（実測値）
   2. 使用LLMモデルは？（コスト最適化済みか）
   3. プロンプトテンプレートは標準化されていますか？
   4. ハルシネーション対策はありますか？
   5. APIレート制限対策は？
   ```

   **Research統合**:
   ```markdown
   ## Domain-Specific Knowledge (from GenAI_research)

   ### PSF Success Patterns
   - **Jasper**: コンテンツ生成で精度92%達成（ファインチューニング）
   - **Grammarly AI**: 文法チェックで精度95%（独自モデル）
   - **Perplexity**: 検索精度88%（RAG活用）

   ### Common Pitfalls
   - **低精度**: プロンプトのみで精度80%未満
   - **高コスト**: API料金がユーザー課金を上回る
   - **遅延**: 10秒以上の応答でユーザー離脱

   ### Reference
   - 詳細: @GenAI_research/solution_validation/psf_benchmarks.md
   ```

---

### 1.5 design-pricing スキル

**目的**: AI製品の価格設計（API従量課金対応）

**実装手順**:

1. 既存スキルをコピー:
   ```bash
   cp -r for_recruit/design-pricing for_genai/design-pricing
   ```

2. `SKILL.md` カスタマイズ:

   **GenAI特化の価格モデル**:
   ```markdown
   ## AI製品の価格設計パターン

   | 価格モデル | 適用ケース | 例 |
   |----------|-----------|-----|
   | **完全無料** | バイラル成長優先 | ChatGPT Free |
   | **Freemium** | 月間制限付き無料 + 有料プラン | Claude (Free 100msgs/day) |
   | **従量課金** | API使用量ベース | OpenAI API ($0.01/1K tokens) |
   | **サブスク** | 月額固定 + 使用制限 | Jasper ($49/月) |
   | **ハイブリッド** | サブスク + 従量課金 | Anthropic Pro ($20/月 + API) |

   ### AI特有のコスト構造
   - **API料金**: OpenAI/Anthropic/Google APIの料金
   - **インフラ**: ベクトルDB、キャッシュサーバー
   - **ファインチューニング**: カスタムモデル学習コスト
   - **モニタリング**: ログ保存、精度測定
   ```

   **価格設計ステップ**:
   ```markdown
   ### Step 1: API料金シミュレーション
   - 1ユーザーあたり月間リクエスト数: 100回
   - 1リクエストあたりトークン数: 500トークン
   - API料金: $0.01/1K tokens
   - **月間コスト**: 100 × 500 / 1000 × $0.01 = $0.50/ユーザー

   ### Step 2: 価格設定
   - API料金の5倍以上で設定（利益率80%確保）
   - **推奨価格**: $2.99/月〜$9.99/月

   ### Step 3: Free Tier設定
   - 月間10リクエストまで無料（バイラル促進）
   - Free → Paid転換率10%目標
   ```

   **Research統合**:
   ```markdown
   ## Domain-Specific Knowledge (from GenAI_research)

   ### Pricing Success Patterns
   - **ChatGPT**: $20/月（無制限）で2M+ 有料ユーザー
   - **Jasper**: $49/月（月間10万words）でARR $75M
   - **Midjourney**: $10/月（月間200画像）で黒字化

   ### Pricing Pitfalls
   - **過度な従量課金**: ユーザー離脱（予測不能なコスト）
   - **Free Tierなし**: バイラル成長の機会損失
   - **高価格**: $50/月以上はエンタープライズのみ

   ### Reference
   - 詳細: @GenAI_research/pricing_strategies/ai_saas_pricing.md
   ```

---

### 1.6 validate-pmf スキル

**目的**: Product Market Fit検証（AI製品特化）

**実装手順**:

1. 既存スキルをコピー:
   ```bash
   cp -r for_recruit/validate-pmf for_genai/validate-pmf
   ```

2. `SKILL.md` カスタマイズ:

   **GenAI特化のPMF指標**:
   ```markdown
   ## PMF評価指標（GenAI特化）

   | 指標 | 目標値 | GenAI特化の測定方法 |
   |------|-------|------------------|
   | **NPS** | 50以上 | AI精度・速度の満足度 |
   | **Retention** | 40%以上（月次） | プロンプト再利用率 |
   | **Product Hunt** | Top 5 | ローンチ日のランキング |
   | **GitHub Stars** | 1000+ | オープンソース版の人気 |
   | **API利用率** | 70%以上 | 有料ユーザーのアクティブ利用 |
   | **精度改善** | 月次+2% | ユーザーフィードバック反映 |

   **PMF達成の目安**: 上記6項目中4項目を達成
   ```

   **GenAI特化質問**:
   ```markdown
   ### PMF検証質問
   1. ユーザーは週3回以上使用していますか？
   2. 「このAIツールなしでは困る」と答えるユーザーは40%以上いますか？
   3. Product Huntでトップ5に入りましたか？
   4. GitHub Starsが月次100以上増加していますか？
   5. ユーザーが自発的にプロンプトを改善していますか？
   ```

   **Research統合**:
   ```markdown
   ## Domain-Specific Knowledge (from GenAI_research)

   ### PMF Success Patterns
   - **ChatGPT**: ローンチ2ヶ月で100M MAU（史上最速PMF）
   - **Midjourney**: Discord統合でバイラル成長
   - **Perplexity**: 検索特化で明確な差別化

   ### PMF失敗パターン
   - **精度不足**: 80%未満の精度で継続利用なし
   - **汎用すぎ**: ChatGPTと差別化できず埋もれる
   - **高価格**: $50/月以上で個人ユーザー離脱

   ### Reference
   - 詳細: @GenAI_research/pmf_validation/ai_product_pmf.md
   ```

---

## 最終成果物

### 1. 新規スキルファイル (6個)
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/discover-demand/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/validate-cpf/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/research-competitors/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/validate-psf/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/design-pricing/SKILL.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/validate-pmf/SKILL.md`

### 2. コマンドファイル (6個)
- `/Users/yuichi/AIPM/aipm_v0/.claude/commands/for-genai-discover-demand.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/commands/for-genai-validate-cpf.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/commands/for-genai-research-competitors.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/commands/for-genai-validate-psf.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/commands/for-genai-design-pricing.md`
- `/Users/yuichi/AIPM/aipm_v0/.claude/commands/for-genai-validate-pmf.md`

### 3. 完了レポート
- `Flow/202601/2026-01-03/FORGENAI_PHASE2_BATCH1_COMPLETION_REPORT.md`
  - 実装完了スキル一覧
  - Research統合状況
  - 次のアクション（Batch 2移行）

---

## 重要な注意事項

1. **Research統合の徹底**:
   - 各スキルに最低3件の成功パターン・事例を統合
   - 定量的ベンチマークを明記
   - 詳細ドキュメントへの参照パスを記載

2. **CPF基準の厳格化**:
   - ForRecruit (50%) → ForGenAI (70%)
   - AI市場の競争激化を反映

3. **AI特化の評価軸**:
   - API料金、精度、速度、プロンプト複雑度を必ず含める

4. **Product Hunt戦略**:
   - ローンチタイミング、Hunter確保、事前コミュニティ参加を明記

---

## 実行開始コマンド

```bash
cd /Users/yuichi/AIPM/aipm_v0/.claude/skills

# スキル作成
for skill in discover-demand validate-cpf research-competitors validate-psf design-pricing validate-pmf; do
    cp -r for_recruit/${skill} for_genai/${skill}
    echo "Created for_genai/${skill}"
done

# コマンドファイル作成（次のBatch 2で実装）
```

---

## 次のステップ

Batch 1完了後、以下のタスクに進む:
- **Batch 2**: 残り12スキル実装（CLI_ForGenAI_Batch2.md参照）
- **Phase 3-5**: コマンドファイル作成、Quality Checkpoint（CLI_ForGenAI_Phase3-5.md参照）
