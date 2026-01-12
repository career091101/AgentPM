# Research Index Agent

**役割**: 4ドメインのResearch Database統合・セマンティック検索・自動事例参照提案

**優先度**: P1（Week 4-5実装）

**年間削減時間**: Research参照時間の短縮（定量化困難だが、意思決定品質向上に貢献）

---

## 1. エージェント概要

### 1.1 目的

4つのドメイン別Research Database（ForGenAI, ForRecruit, ForSolo, ForStartup）を統合し、以下を実現：

1. **セマンティック検索**: 課題記述から類似事例を自動検索（自然言語クエリ対応）
2. **自動事例参照提案**: CPF/PSF/PMF検証時に関連事例を提示
3. **Research Database索引の自動生成**: 全Researchファイルをインデックス化
4. **ドメイン横断検索**: ForGenAI × ForSolo等の複数ドメイン横断検索
5. **ケーススタディの要約生成**: 長文ケーススタディを3行要約

### 1.2 Research Database構成

| ドメイン | Research Location | 規模 | 内容 |
|---------|------------------|------|------|
| **ForGenAI** | `GenAI_research/` | 50+事例 | AI技術トレンド、Product Hunt戦略、プロンプトパターン |
| **ForRecruit** | `Recruit_Product_Research/` | 30+事例 | 企業内新規事業、Ring制度、社内承認プロセス |
| **ForSolo** | `Solopreneur_Research/documents/01_App/case_studies/` | 85事例 | ソロプレナー成功事例、Build in Public、Micro-SaaS |
| **ForStartup** | `Recruit_Product_Research/` | 50+事例（共通） | VC投資基準、ピッチデッキ、ユニットエコノミクス |
| **共通** | `Founder_Research/` | 200+事例 | 創業者ケーススタディ、成功/失敗パターン |

**総事例数**: 400+事例

### 1.3 検索アルゴリズム

#### セマンティック検索

**使用技術**:
- **埋め込みモデル**: OpenAI `text-embedding-3-small`（1536次元、$0.02/1M tokens）
- **ベクトルDB**: Pinecone（無料枠: 1GB、100万ベクトル）または Supabase pgvector（自己ホスト）
- **類似度計算**: コサイン類似度（閾値: 0.7以上で関連性あり）

**インデックス化フロー**:
```
STEP 1: Researchファイル読み込み
├─ Markdownファイル検出（*.md）
├─ ファイル内容抽出（タイトル、本文、キーワード）
└─ メタデータ付与（ドメイン、日付、著者）

STEP 2: チャンク分割
├─ 1ファイルを500-1000 token単位に分割
├─ セクション境界を考慮（## 見出し単位）
└─ オーバーラップ設定（隣接チャンクと50 token重複）

STEP 3: 埋め込み生成
├─ OpenAI API呼び出し（バッチ処理、1000チャンク/リクエスト）
├─ 1536次元ベクトル取得
└─ キャッシュ保存（ローカルJSON）

STEP 4: ベクトルDB保存
├─ Pinecone / Supabase pgvectorに保存
├─ メタデータ付与（file_path, domain, chunk_id, title）
└─ インデックス最適化（HNSW, IVF）
```

**検索フロー**:
```
STEP 1: クエリ埋め込み生成
├─ ユーザークエリ（例: 「AIフィットネスアプリの成功事例」）
├─ OpenAI API呼び出し
└─ 1536次元ベクトル取得

STEP 2: ベクトル検索
├─ Pinecone / Supabase pgvectorでコサイン類似度計算
├─ Top 10候補を取得（類似度降順）
└─ 閾値フィルタリング（類似度 > 0.7）

STEP 3: リランキング
├─ ドメイン一致優先（例: CPF検証中ならForSoloを優先）
├─ 日付新しい順（最新事例を優先）
└─ 多様性確保（同じファイルから複数チャンクを避ける）

STEP 4: 結果返却
├─ Top 3-5事例を返却
├─ タイトル、要約、ファイルパス、関連度スコアを含む
└─ ユーザーが詳細確認できるようリンク提示
```

---

## 2. 能力と実行フロー

### 2.1 主要能力

#### 能力1: セマンティック検索

**入力**: 自然言語クエリ
**出力**: 関連事例Top 3-5（タイトル、要約、関連度、ファイルパス）

**検索例**:
```
クエリ: 「AIフィットネスアプリの成功事例」

検索結果:
1. [関連度: 92%] Marc Lou - ShipFast (Boilerplate SaaS)
   - 要約: 1人開発で初月100 MRR達成、Build in Public戦略で透明性確保
   - ドメイン: ForSolo
   - パス: @Solopreneur_Research/documents/01_App/case_studies/marc_lou_shipfast.md

2. [関連度: 88%] Tony Dinh - Black Magic
   - 要約: Twitterフォロワー活用でローンチ初日$1K売上、Micro-SaaS収益化
   - ドメイン: ForSolo
   - パス: @Solopreneur_Research/documents/01_App/case_studies/tony_dinh_black_magic.md

3. [関連度: 85%] Product Hunt #1獲得戦略
   - 要約: Hunter確保、事前コミュニティ参加、タイミング最適化で#1達成
   - ドメイン: ForGenAI
   - パス: @GenAI_research/growth/product_hunt_strategy.md
```

#### 能力2: 自動事例参照提案

**トリガー**: CPF/PSF/PMF検証エージェント実行時
**出力**: 検証結果に基づく関連事例Top 3

**統合例（CPF検証時）**:
```python
# CPF検証エージェント実行
cpf_result = Task(description="CPF検証", ...)

# CPF結果をクエリとしてResearch Index Agent起動
research_result = Task(
    description="関連事例検索 - CPF検証結果に基づく",
    prompt=f"""
    @.claude/agents/research-index-agent.md の仕様に従い、以下のCPF検証結果に基づいて関連事例を検索してください。

    **CPF検証結果**:
    - 課題: {cpf_result['problem']}
    - ソリューション: {cpf_result['solution']}
    - ターゲット: {cpf_result['persona']}
    - CPFスコア: {cpf_result['score']}/100

    **検索要件**:
    - ドメイン: {domain}（for_solo / for_recruit / for_genai / for_startup）
    - Top 3事例を返却
    - 類似度 > 80%の事例のみ
    """,
    model="haiku",  # 高速検索
    timeout=30000  # 30秒
)

# 検索結果をCPF判定レポートに統合
cpf_report = generate_cpf_report(cpf_result, research_result)
```

#### 能力3: Research Database索引の自動生成

**トリガー**: 定期実行（週次）またはResearchファイル更新時
**出力**: インデックスファイル（`research_index.json`）、ベクトルDB更新

**自動生成される索引例**:
```json
{
  "index_version": "2026-01-03",
  "total_documents": 415,
  "total_chunks": 8540,
  "domains": {
    "for_genai": {
      "documents": 52,
      "chunks": 1050,
      "categories": ["tech_stack", "growth", "prompt_patterns"]
    },
    "for_recruit": {
      "documents": 35,
      "chunks": 780,
      "categories": ["ring_criteria", "approval_process", "internal_resources"]
    },
    "for_solo": {
      "documents": 85,
      "chunks": 2100,
      "categories": ["app", "saas", "boilerplate", "build_in_public"]
    },
    "for_startup": {
      "documents": 53,
      "chunks": 1200,
      "categories": ["vc_criteria", "pitch_deck", "unit_economics"]
    },
    "founder_research": {
      "documents": 190,
      "chunks": 3410,
      "categories": ["case_studies", "success_patterns", "failure_patterns"]
    }
  }
}
```

#### 能力4: ドメイン横断検索

**入力**: クエリ + 複数ドメイン指定
**出力**: ドメイン別Top 2事例（最大4ドメイン × 2 = 8事例）

**検索例**:
```
クエリ: 「1人でAI SaaSを立ち上げる方法」
ドメイン: for_genai, for_solo

検索結果:
【ForGenAI】
1. [92%] AI技術スタック選定基準（OpenAI vs Anthropic）
2. [88%] Product Hunt #1獲得戦略

【ForSolo】
1. [95%] Marc Lou - ShipFast（Boilerplate SaaS）
2. [90%] Pieter Levels - Nomad List（リモートワーカー向けSaaS）

クロスドメインインサイト:
- ForGenAI × ForSolo: AI技術選定後、ShipFastボイラープレートで高速開発
- Build in Public戦略でProduct Hunt #1獲得を狙う
```

#### 能力5: ケーススタディの要約生成

**入力**: ケーススタディファイルパス
**出力**: 3行要約（課題、ソリューション、結果）

**要約例**:
```
元ファイル: marc_lou_shipfast.md (850行)

要約:
- **課題**: SaaS開発に毎回2-3週間かかり、アイデア検証が遅い
- **ソリューション**: Next.js + Supabase + Stripeのボイラープレート「ShipFast」を開発し、自分で使いながら販売
- **結果**: 初月100 MRR達成、6ヶ月で$50K売上、1人開発で月$8-10K MRR維持

キーメトリクス: 初月100 MRR → 6ヶ月$50K → 定常$8-10K/月
```

### 2.2 実行フロー

```
STEP 1: 入力受付
├─ 検索クエリ（自然言語）
├─ ドメイン指定（単一 or 複数）
├─ 検索モード（quick / standard / deep）
└─ Top N件（デフォルト: 5）

STEP 2: クエリ解析
├─ キーワード抽出
├─ ドメイン推定（明示されていない場合）
└─ 検索意図分類（成功事例 / 失敗事例 / 技術比較 / 評価基準）

STEP 3: クエリ埋め込み生成
├─ OpenAI text-embedding-3-small呼び出し
├─ 1536次元ベクトル取得
└─ キャッシュ確認（同一クエリは再利用）

STEP 4: ベクトル検索
├─ Pinecone / Supabase pgvectorでコサイン類似度計算
├─ Top 20候補を取得
└─ 類似度閾値フィルタリング（> 0.7）

STEP 5: リランキング
├─ ドメイン一致優先
├─ 日付新しい順
├─ 多様性確保（同じファイルから1件のみ）
└─ Top N件に絞り込み

STEP 6: 要約生成
├─ 各事例の3行要約を生成（未キャッシュの場合）
├─ キーメトリクス抽出（MRR、ユーザー数、成長率等）
└─ 要約をキャッシュ保存

STEP 7: 結果返却
├─ 検索結果リスト（タイトル、要約、関連度、ファイルパス）
├─ クロスドメインインサイト（複数ドメイン検索の場合）
└─ 詳細確認リンク（ファイルパス）

STEP 8: 検索ログ記録
├─ クエリ、検索結果、実行時間を記録
├─ 採用率トラッキング（ユーザーがリンクをクリックしたか）
└─ 検索精度改善のためのデータ蓄積
```

---

## 3. 入力パラメータ

### 3.1 必須パラメータ

#### 1. 検索クエリ

**質問**: 「検索したい内容を自然言語で入力してください」

**例**:
- 「AIフィットネスアプリの成功事例」
- 「Product Hunt #1を獲得する方法」
- 「VC調達成功のピッチデッキ事例」
- 「社内新規事業でRing 2を突破した事例」

**デフォルト**: なし（必須）

### 3.2 オプションパラメータ

#### 2. ドメイン指定

**質問**: 「検索対象のドメインを選択してください（複数選択可）」

**選択肢**:
- `for_genai`: 生成AI特化版
- `for_recruit`: 企業内新規事業特化版
- `for_solo`: ソロプレナー特化版
- `for_startup`: スタートアップ特化版
- `all`: 全ドメイン横断検索

**デフォルト**: `all`

#### 3. 検索モード

**質問**: 「検索モードを選択してください」

**選択肢**:
- `quick`: Top 3のみ、高速検索（< 5秒）
- `standard`: Top 5、バランス型（< 10秒）（推奨デフォルト）
- `deep`: Top 10、詳細検索（< 20秒）

**デフォルト**: `standard`

#### 4. Top N件

**質問**: 「表示する事例数を入力してください」

**範囲**: 1-20

**デフォルト**: 5

#### 5. 類似度閾値

**質問**: 「最低類似度を設定してください（0.0-1.0）」

**範囲**: 0.0-1.0

**デフォルト**: 0.7（70%以上の関連性）

---

## 4. 出力ファイル

### 4.1 出力先

```
Flow/YYYYMM/YYYY-MM-DD/research_search/
├── search_results.md            # 検索結果（人間可読）
├── search_results.json          # 検索結果（機械可読）
└── search_log.json              # 検索ログ
```

### 4.2 検索結果形式

#### search_results.md

```markdown
# Research Search Results

**クエリ**: 「AIフィットネスアプリの成功事例」
**ドメイン**: for_solo, for_genai
**検索日時**: 2026-01-03 16:45:23
**検索時間**: 4.2秒

---

## 検索結果（5件）

### 1. Marc Lou - ShipFast (Boilerplate SaaS) [関連度: 92%]

**ドメイン**: ForSolo
**ファイル**: @Solopreneur_Research/documents/01_App/case_studies/marc_lou_shipfast.md

**要約**:
- **課題**: SaaS開発に毎回2-3週間かかり、アイデア検証が遅い
- **ソリューション**: Next.js + Supabase + Stripeのボイラープレート「ShipFast」を開発し、自分で使いながら販売
- **結果**: 初月100 MRR達成、6ヶ月で$50K売上、1人開発で月$8-10K MRR維持

**キーメトリクス**:
- 初月MRR: $100
- 6ヶ月売上: $50K
- 定常MRR: $8-10K/月

**詳細**: [ファイルを開く](../../../Solopreneur_Research/documents/01_App/case_studies/marc_lou_shipfast.md)

---

### 2. Tony Dinh - Black Magic [関連度: 88%]

**ドメイン**: ForSolo
**ファイル**: @Solopreneur_Research/documents/01_App/case_studies/tony_dinh_black_magic.md

**要約**:
- **課題**: Twitterフォロワーを収益化したい
- **ソリューション**: Twitter分析ツール「Black Magic」をローンチ、X（旧Twitter）でBuild in Public戦略
- **結果**: ローンチ初日$1K売上、3ヶ月で$10K MRR達成

**キーメトリクス**:
- ローンチ初日売上: $1K
- 3ヶ月MRR: $10K

**詳細**: [ファイルを開く](../../../Solopreneur_Research/documents/01_App/case_studies/tony_dinh_black_magic.md)

---

### 3. Product Hunt #1獲得戦略 [関連度: 85%]

**ドメイン**: ForGenAI
**ファイル**: @GenAI_research/growth/product_hunt_strategy.md

**要約**:
- **課題**: Product Huntで注目を集める方法が不明
- **ソリューション**: Hunter確保、事前コミュニティ参加、タイミング最適化（火-木曜0:00 PST）
- **結果**: #1獲得で初日1000+アップボート、500+ユーザー獲得

**キーメトリクス**:
- #1獲得率: 40%（準備した場合）
- 初日ユーザー獲得: 500-1000

**詳細**: [ファイルを開く](../../../GenAI_research/growth/product_hunt_strategy.md)

---

## クロスドメインインサイト

**ForSolo × ForGenAI統合戦略**:
1. ShipFastボイラープレートでAI機能を高速実装
2. Build in Public戦略でX（旧Twitter）でフォロワー獲得
3. Product Hunt #1を狙い、初期ユーザー500-1000獲得
4. 初月MRR $100を目標に、3ヶ月で$10K MRR達成

**類似成功パターン**:
- 1人開発 + AI統合 + Build in Public → 初月MRR $100-1K
- Product Hunt #1 → 初日500-1000ユーザー → 3ヶ月$10K MRR
```

#### search_results.json

```json
{
  "query": "AIフィットネスアプリの成功事例",
  "domains": ["for_solo", "for_genai"],
  "search_mode": "standard",
  "execution_time_ms": 4200,
  "results": [
    {
      "rank": 1,
      "relevance_score": 0.92,
      "title": "Marc Lou - ShipFast (Boilerplate SaaS)",
      "domain": "for_solo",
      "file_path": "Solopreneur_Research/documents/01_App/case_studies/marc_lou_shipfast.md",
      "summary": {
        "problem": "SaaS開発に毎回2-3週間かかり、アイデア検証が遅い",
        "solution": "Next.js + Supabase + Stripeのボイラープレート「ShipFast」を開発し、自分で使いながら販売",
        "result": "初月100 MRR達成、6ヶ月で$50K売上、1人開発で月$8-10K MRR維持"
      },
      "key_metrics": {
        "initial_mrr": 100,
        "six_month_revenue": 50000,
        "steady_mrr": "8000-10000"
      }
    }
    // ... 他の結果
  ],
  "cross_domain_insights": [
    "ForSolo × ForGenAI統合戦略: ShipFastボイラープレートでAI機能を高速実装",
    "Build in Public戦略でX（旧Twitter）でフォロワー獲得",
    "Product Hunt #1を狙い、初期ユーザー500-1000獲得"
  ]
}
```

---

## 5. Task tool統合

### 5.1 Manager Skillからの呼び出しパターン

```python
result = Task(
    description="Research検索 - AIフィットネスアプリ成功事例",
    prompt="""
    @.claude/agents/research-index-agent.md の仕様に従い、以下の検索を実行してください。

    **検索クエリ**: 「AIフィットネスアプリの成功事例」
    **ドメイン**: for_solo, for_genai
    **検索モード**: standard
    **Top N件**: 5
    **類似度閾値**: 0.7

    以下を生成してください:
    1. search_results.md（人間可読形式）
    2. search_results.json（機械可読形式）
    3. クロスドメインインサイト
    """,
    subagent_type="general-purpose",
    model="haiku",  # 高速検索
    timeout=30000  # 30秒
)
```

### 5.2 CPF検証エージェントとの連携

```python
# CPF検証エージェント実行
cpf_result = Task(description="CPF検証", ...)

# CPF結果に基づいてResearch検索
research_result = Task(
    description="関連事例検索 - CPF検証結果に基づく",
    prompt=f"""
    @.claude/agents/research-index-agent.md の仕様に従い、以下のCPF検証結果に基づいて関連事例を検索してください。

    **課題**: {cpf_result['problem']}
    **ソリューション**: {cpf_result['solution']}
    **ターゲット**: {cpf_result['persona']}
    **ドメイン**: {domain}
    **Top 3事例**

    CPF判定レポートに統合できる形式で返却してください。
    """,
    model="haiku"
)

# 検索結果をCPF判定レポートに統合
cpf_report = merge(cpf_result, research_result)
```

### 5.3 モデル選択ガイド

| モデル | 用途 | 検索速度 | 要約品質 | コスト |
|--------|------|---------|---------|--------|
| **haiku** | 高速検索のみ（要約生成なし） | 最速（< 3秒） | - | 低 |
| **sonnet** | 標準検索 + 要約生成（推奨デフォルト） | 中速（< 10秒） | 高 | 中 |
| **opus** | Deep検索 + 高品質要約 + クロスドメインインサイト | 低速（< 30秒） | 最高 | 高 |

---

## 6. エラーハンドリング

### Pattern 1: インデックス未構築

**エラー**: ベクトルDBにインデックスが存在しない

**対処**:
1. 自動インデックス構築を提案
2. ユーザーに構築許可を確認
3. 許可された場合、STEP 1-4の索引生成フローを実行（10-20分）
4. 完了後に検索を再実行

### Pattern 2: 類似事例が見つからない

**エラー**: 類似度 > 0.7の事例が0件

**対処**:
1. 類似度閾値を0.5に下げて再検索
2. それでも0件の場合、クエリを拡張（関連キーワード追加）
3. 最終的に見つからない場合、「該当事例なし」と明示
4. 代替提案: ドメインを拡張（for_solo → all）

### Pattern 3: OpenAI API制限

**エラー**: Rate Limit Exceeded

**対処**:
1. キャッシュされた埋め込みを優先使用
2. バッチサイズを縮小（1000 → 100チャンク/リクエスト）
3. リトライ（指数バックオフ: 1秒、2秒、4秒）
4. 最終的に失敗した場合、キーワードベース検索にフォールバック

### Pattern 4: ベクトルDB接続エラー

**エラー**: Pinecone / Supabase pgvectorに接続できない

**対処**:
1. ローカルキャッシュ（JSON）で検索を試行
2. キャッシュミスの場合、キーワードベース検索にフォールバック
3. エラーログを記録し、後で手動修復を促す

---

## 7. 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| 検索精度（関連度 > 0.8） | > 80% | 人間評価でTop 5に関連事例が含まれる率 |
| 検索速度（standard モード） | < 10秒 | 実行時間の平均値 |
| 事例提案の採用率 | > 50% | ユーザーがリンクをクリックした率 |
| クエリカバレッジ | > 90% | 類似度 > 0.7の事例が見つかる率 |
| クロスドメインインサイト品質 | > 75% | 人間評価で有用と判断される率 |

---

## 8. 参照

- **エージェント仕様**: `@.claude/agents/research-index-agent.md`（本ファイル）
- **並列実行**: `@.claude/rules/parallel_execution.md`
- **Discovery Automation Agent**: `@.claude/agents/discovery-automation-agent.md`
- **Research統合**:
  - ForGenAI: `@GenAI_research/`
  - ForRecruit: `@Recruit_Product_Research/`
  - ForSolo: `@Solopreneur_Research/`
  - ForStartup: `@Recruit_Product_Research/`（共通）
  - 共通: `@Founder_Research/`

---

**作成日**: 2026-01-03
**Week 4-5実装**: Research Index Agent（P1）
