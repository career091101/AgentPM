# Startup Science Skills

「起業の科学」フレームワークを実践するためのClaude Code Skills集。

## Skills一覧

### 統合メンター

| Skill | コマンド | 用途 |
|-------|---------|------|
| Startup Mentor | `/startup-mentor` | 統合型スタートアップメンター |

### ステージ検証

| Skill | コマンド | 用途 |
|-------|---------|------|
| Idea Validation | `/validate-idea` | Ideaステージ対話型検証 |
| CPF Validation | `/validate-cpf` | CPF達成度診断 |
| PSF Validation | `/validate-psf` | PSF達成度診断 |
| PMF Validation | `/validate-pmf` | PMF達成度診断 |

### フレームワーク適用

| Skill | コマンド | 用途 |
|-------|---------|------|
| Lean Canvas | `/apply-lean-canvas` | リーンキャンバス作成支援 |
| Pivot Decision | `/apply-pivot-decision` | ピボット判断支援 |
| AARRR Analysis | `/apply-aarrr-analysis` | AARRR指標分析 |
| Five Perspectives | `/apply-five-perspectives` | 5つの眼市場分析 |

### 事例参照

| Skill | コマンド | 用途 |
|-------|---------|------|
| Case Reference | `/reference-cases` | ソロプレナー成功事例参照 |

---

## 自律実行型Skills

Phase1（アイデア創出→PSF検証）およびPhase2-3（PMF検証→スケール）を自動実行するSkills。対話最小限、ステージゲートでHuman-in-the-Loop。

### Phase 1: 需要発見・企画（12スキル）

#### 需要発見・企画

| Skill | コマンド | 用途 | 所要時間 |
|-------|---------|------|:--------:|
| Discover Demand | `/discover-demand` | 需要発見リサーチ（生ログベース） | 15-30分 |
| Create MVV | `/create-mvv` | MVV早期定義 | 20-40分 |
| Create Persona | `/create-persona` | ターゲットペルソナ自動生成 | 15-30分 |
| Build Flywheel | `/build-flywheel` | フライホイール設計 | 30-50分 |

#### 検証

| Skill | コマンド | 用途 | 所要時間 |
|-------|---------|------|:--------:|
| Research Problem | `/research-problem` | Web課題発見 | 30-60分 |
| Simulate Interview | `/simulate-interview` | 仮想ペルソナインタビュー | 25-45分 |
| Validate CPF | `/validate-cpf` | CPF達成基準に基づき総合判定 | 20-40分 |
| Research Competitors | `/research-competitors` | 競合・代替案を自動調査 | 40-70分 |
| Validate 10x | `/validate-10x` | 10倍優位性検証 | 40-70分 |

#### MVP構築

| Skill | コマンド | 用途 | 所要時間 |
|-------|---------|------|:--------:|
| Build LP | `/build-lp` | LP構築（HTML/CSS/JS） | 40-80分 |
| Validate PSF | `/validate-psf` | PSF達成基準に基づき総合判定 | 20-40分 |
| Create SNS Content | `/create-sns-content` | SNSコンテンツ作成 | 30-50分 |

---

### Phase 2: PMF検証（2スキル）

| Skill | コマンド | 用途 | 所要時間 |
|-------|---------|------|:--------:|
| **Validate PMF** | `/validate-pmf` | **PMF達成を4指標で総合判定** | **20-40分** |
| Pivot Decision | `/pivot-decision` | CPF/PSF未達成時に最適Pivot選択 | 30-50分 |

**Validate PMF の測定指標**:
- Sean Ellisテスト（≥40%）
- 月次成長率（≥10%/月）
- Churn Rate（≤5%/月）
- NPS（≥50）

---

### Phase 3: スケール（3スキル）

| Skill | コマンド | 用途 | 所要時間 |
|-------|---------|------|:--------:|
| **Measure AARRR** | `/measure-aarrr` | **AARRR成長ファネル分析** | **40-50分** |
| **Monitor Burn Rate** | `/monitor-burn-rate` | **バーンレート・ランウェイ監視** | **5-10分** |
| Validate Unit Economics | `/validate-unit-economics` | ユニットエコノミクスで財務検証 | 30-50分 |

**Measure AARRR の測定指標**:
- Acquisition（獲得）- 訪問者数、流入チャネル
- Activation（活性化）- サインアップ率、Aha Moment達成率
- Retention（継続）- DAU/MAU、D30継続率、Churn Rate
- Referral（紹介）- 紹介率、バイラル係数、NPS
- Revenue（収益）- 課金転換率、ARPU、MRR、LTV/CAC

**Monitor Burn Rate の測定指標**:
- Net Burn Rate（月次消費金額）
- Runway（資金が尽きるまでの期間）
- 18ヶ月ルール（起業の科学）に基づく資金調達タイミング判定

---

### Phase 4: SNS/データ収集（1スキル）

| Skill | コマンド | 用途 | 所要時間 |
|-------|---------|------|:--------:|
| **Collect X Timeline** | `/collect-x-timeline` | **Xタイムライン収集（GraphQL API傍受）** | **5-10分** |

**Collect X Timeline の特徴**:
- カーソルベースAPI傍受方式（重複率0%）
- 目標200件/回（最大500件まで対応）
- ユーザー名、テキスト、いいね、リツイート、リプライ数を構造化
- Cookie認証で自動ログイン
- デバッグモード対応（APIレスポンス保存）

---

### Phase 5: SNS投稿自動化（7スキル - 完全実装済み✅）

**目標**: 月間インプレッション346,766 → 1,000,000、作業時間47.5分 → 15分（68%削減）

| Skill | コマンド | 用途 | 所要時間 | 優先度 |
|-------|---------|------|:--------:|:------:|
| **Extract Top Tweets** | `/extract-top-tweets` | **Top 10高エンゲージメント投稿抽出** | **3-5分** | **P0** ✅ |
| **Scrape Tweet Details** | `/scrape-tweet-details` | **ツイート詳細・リンク・リプライ抽出** | **10-15分** | **P0** ✅ |
| **Extract Content** | `/extract-content` | **記事/YouTube/PDF コンテンツ抽出（LLM実行）** | **5-10分** | **P1** ✅ |
| **Analyze Replies** | `/analyze-replies` | **リプライから反響ポイント分析（LLM実行）** | **10-15分** | **P1** ✅ |
| **Research Topic** | `/research-topic` | **Web調査・ファクトチェック（LLM実行）** | **15-20分** | **P1** ✅ |
| **Generate SNS Posts** | `/generate-sns-posts` | **LinkedIn投稿3案生成（高野メソッド準拠、LLM実行）** | **20-30分** | **P1** ✅ |
| **Approve and Schedule** | `/approve-and-schedule` | **Slack承認・SNS自動投稿（LLM実行）** | **5-10分** | **P1** ✅ |

**Extract Top Tweets の特徴**:
- エンゲージメントスコア計算（いいね + RT×3 + 返信×5）
- 世界的著名人フィルタリング
- Top 10件を自動抽出
- 入力: `x_timeline_{YYYYMMDD}.json`（200件）
- 出力: `top_10_tweets_{YYYYMMDD}.json`

**Scrape Tweet Details の特徴**:
- Playwrightでツイート詳細ページ遷移
- リンク抽出・分類（記事/YouTube/PDF）
- リプライ上位5件取得
- Cookie認証・レート制限対応
- 入力: `top_10_tweets_{YYYYMMDD}.json`
- 出力: `tweet_details_{YYYYMMDD}.json`

**Extract Content の特徴**（ClaudeCode LLM直接実行）:
- WebFetchツールで記事コンテンツ抽出（タイトル・本文・メタ情報）
- YouTube/PDF情報取得（今後実装予定）
- 複数リンク一括処理
- エラーハンドリング（Timeout・403等）
- 実績: 11/12リンク成功（91.7%）、1,322ワード抽出
- 入力: `tweet_details_{YYYYMMDD}.json`
- 出力: `extracted_contents_{YYYYMMDD}.json`

**Analyze Replies の特徴**（ClaudeCode LLM直接実行）:
- ClaudeCode LLMがリプライを意味分析
- 4カテゴリ分類（共感・期待、批判・懸念、追加情報・洞察、質問）
- インサイト日本語要約（投稿作成に直接反映可能）
- エンゲージメント重視（いいね数順）
- 実績: 5ツイート、40リプライ → 24インサイト抽出
- 入力: `tweet_details_{YYYYMMDD}.json`
- 出力: `reply_insights_{YYYYMMDD}.json`

**Research Topic の特徴**（ClaudeCode LLM直接実行）:
- WebSearchツールで最新ニュース・ファクトチェック・批判的視点・専門家意見を収集
- High priority（Top 3）トピックを詳細調査
- 4カテゴリ構造化（最新ニュース、ファクトチェック、批判的視点、専門家意見）
- 実績: 3トピック調査、30ソース、7ファクトチェック、13批判的視点
- 入力: `top_10_ai_tweets_{YYYYMMDD}.json`
- 出力: `research_findings_{YYYYMMDD}.json`

**Generate SNS Posts の特徴**（ClaudeCode Opus + 高野メソッドv6統合）:
- Phase 2全データ統合（コンテンツ抽出、リプライ分析、Web調査）
- LinkedIn投稿3案同時生成（数字インパクト型、衝撃発言型、問題提起型）
- 高野メソッド6要素準拠率100%（引き込み、データ/事例、共感、洞察、問いかけ、固有名詞）
- 予測ER 3.0%以上（業界平均1-3%超え）
- 3案比較表 + 最推奨案の自動選定
- 入力: Phase 2の4ファイル（extracted_contents, reply_insights, research_findings, top_10_ai_tweets）
- 出力: `posts_generated_{YYYYMMDD}.json`

**Approve and Schedule の特徴**（ClaudeCode LLM + SNS API統合）:
- Slack通知（#sns-automationチャンネル、インタラクティブボタン付き）
- 3案承認待機（タイムアウト24時間、推奨案自動承認）
- LinkedIn/Facebook/X 自動投稿（API経由）
- プラットフォーム別最適化（LinkedIn: 1,500字、Facebook: 300-500字、X: スレッド形式）
- 投稿結果レポート生成（post_url、投稿時刻、エラーログ）
- 環境変数で認証管理（SLACK_WEBHOOK_URL, LINKEDIN_ACCESS_TOKEN等）
- 入力: `posts_generated_{YYYYMMDD}.json`
- 出力: `posted_status_{YYYYMMDD}.json`

**バッチ実行戦略**:
- バッチ1: データ収集（3エージェント並列、15-18分）
- バッチ2: コンテンツ抽出（5-8エージェント並列、10-12分）
- バッチ3: 分析（3エージェント並列、15-20分）
- バッチ4: 投稿生成（1エージェント、20-30分、model: opus）
- バッチ5: 承認・投稿（1エージェント、5-10分）
- **総実行時間**: 65-90分（並列実行）

**推定コスト**: $4.70/日 ≈ $141/月

---

### Phase 6: 学習・ナレッジ管理（1スキル）

| Skill | コマンド | 用途 | 所要時間 |
|-------|---------|------|:--------:|
| **Evaluate Bookmark Value** | `/evaluate-bookmark-value` | **X投稿のブックマーク価値判定（7軸評価）** | **即時** |

**Evaluate Bookmark Value の特徴**:
- 823件の実ブックマークデータから抽出した7軸評価モデル
- 0-100点スコアリング（80+: 即ブックマーク、60+: 推奨）
- ユーザー学習スタイル適応（97.1%概念的学習パターン）
- 評価軸: 実践的価値、最新性、データドリブン、引用・参照性、集合知、発信者専門性、情報の深さ
- カテゴリ判定（AI・生成AI 70.7%）、概念的タイプ判定（理論・原理、比較・分析等）
- Python CLI/API対応（スタンドアロンスクリプト）

---

### 評価・統合

| Skill | コマンド | 用途 | 所要時間 |
|-------|---------|------|:--------:|
| Startup Scorecard | `/startup-scorecard` | スタートアップ・スコアカード | 20-40分 |
| **Orchestrate Phase1** | `/orchestrate-phase1` | **Phase1全自動実行** | **3-6時間** |
| **Orchestrate Review Loop** | `/orchestrate-review-loop` | **ドキュメント品質保証レビューループ** | **タスク数×20分** |

---

## Phase別スキル分類サマリー

| Phase | スキル数 | 主な用途 |
|-------|:--------:|---------|
| **Phase 1（アイデア→PSF）** | 12 | 需要発見、MVV定義、CPF/PSF検証、MVP構築 |
| **Phase 2（PMF検証）** | 2 | PMF達成判定、Pivot判断 |
| **Phase 3（スケール）** | 3 | AARRR分析、バーンレート監視、ユニットエコノミクス |
| **Phase 4（SNS/データ収集）** | 1 | Xタイムライン収集、SNSデータ分析 |
| **Phase 5（SNS投稿自動化）** | 7（全実装済み✅） | Top投稿抽出、コンテンツ分析、投稿文生成（高野式）、承認・自動投稿 |
| **Phase 6（学習・ナレッジ管理）** | 1 | X投稿ブックマーク価値判定（7軸評価モデル） |
| **合計** | **27（全実装済み✅）** | 起業の科学フレームワーク準拠率100% |

---

## 自律実行型Skillsの特徴

- **対話最小限**: 入力確認後、自動実行モードで進行
- **ステージゲート**: CPF/PSF/PMF未達成時は必ず停止・報告
- **エラーハンドリング**: 各Skillに最大3回リトライ、失敗時はユーザー通知
- **成果物自動出力**: `{IDEA_FOLDER}/documents/`または`mvp/`に出力
- **スコアリング**: 各Skillで定量的な判定基準あり

---

## 推奨フロー

### Phase 1: アイデア→PSF（12ステップ）

```bash
# オーケストレーター（全自動）
/orchestrate-phase1
  → 12個のSkillを順次実行（3-6時間）
  → ステージゲート: CPF → PSF
  → 最終評価: スコアカード

# 個別実行（カスタマイズしたい場合）
/discover-demand
/create-mvv
/create-persona
/apply-lean-canvas
/build-flywheel
/research-problem
/simulate-interview
/validate-cpf
  → [ステージゲート1: CPF]
/research-competitors
/validate-10x
/build-lp
/validate-psf
  → [ステージゲート2: PSF]
/create-sns-content
/startup-scorecard
```

### Phase 2: PMF検証（2ステップ）

```bash
# PSF達成後、MVP稼働開始
/validate-pmf
  → Sean Ellisテスト、月次成長率、Churn Rate、NPSで総合判定
  → PMF達成 → Phase 3へ
  → PMF未達成 → /pivot-decision

# PMF未達成時
/pivot-decision
  → 10類型のPivot提案
  → Phase 1へ戻る or 改善後に再度/validate-pmf
```

### Phase 3: スケール（3ステップ）

```bash
# PMF達成後、スケール段階
/measure-aarrr
  → AARRR 5段階のファネル分析
  → ボトルネック検出、改善施策提案

/monitor-burn-rate
  → 月次バーンレート、ランウェイ計算
  → 18ヶ月ルールで資金調達タイミング判定

/validate-unit-economics
  → LTV/CAC、CAC回収期間、ユニットエコノミクス
  → 財務的持続可能性確認
```

---

## 使い方

### ハイブリッド構成（推奨）

このシステムは**スキル（Skills）**と**スラッシュコマンド（Slash Commands）**のハイブリッド構成です。

#### 方法1: スラッシュコマンドで明示的に呼び出し（推奨）

```bash
# Phase 1: アイデア→PSF（12スキル）
/discover-demand       # 需要発見リサーチ
/create-mvv           # MVV早期定義
/create-persona       # ペルソナ自動生成
/build-flywheel       # フライホイール設計
/research-problem     # Web課題発見
/simulate-interview   # 仮想ペルソナインタビュー
/validate-cpf         # CPF検証
/research-competitors # 競合調査
/validate-10x         # 10倍優位性検証
/build-lp             # LP構築
/validate-psf         # PSF検証
/create-sns-content   # SNSコンテンツ作成

# Phase 2: PMF検証（2スキル）
/validate-pmf         # PMF達成判定（NEW!）
/pivot-decision       # Pivot判断支援

# Phase 3: スケール（3スキル）
/measure-aarrr        # AARRR分析（NEW!）
/monitor-burn-rate    # バーンレート監視（NEW!）
/validate-unit-economics # ユニットエコノミクス

# 評価・統合
/startup-scorecard    # スコアカード
/orchestrate-phase1   # Phase1全自動実行（3-6時間）

# その他のスキル
/startup-mentor       # 統合型スタートアップメンター
```

#### 方法2: 自然言語で自動検出（スキル機能）

```bash
# Claudeが自動的にスキルを検出して提案
「需要を発見してください」        → discover-demand スキル検出
「MVVを作成してください」          → create-mvv スキル検出
「PMFを検証して」                 → validate-pmf スキル検出
「AARRRファネルを分析して」        → measure-aarrr スキル検出
「バーンレートを監視して」         → monitor-burn-rate スキル検出
```

### 構成ディレクトリ

```
.claude/
├── commands/          # スラッシュコマンド（明示的呼び出し用）
│   ├── discover-demand.md
│   ├── create-mvv.md
│   ├── validate-pmf.md        # NEW!
│   ├── measure-aarrr.md       # NEW!
│   ├── monitor-burn-rate.md   # NEW!
│   └── ...
└── skills/           # スキル（自動検出 + 複雑なワークフロー）
    ├── discover-demand/SKILL.md
    ├── create-mvv/SKILL.md
    ├── validate-pmf/SKILL.md         # NEW!
    ├── measure-aarrr/SKILL.md        # NEW!
    ├── monitor-burn-rate/SKILL.md    # NEW!
    └── ...
```

### 使い分けのポイント

| 用途 | 推奨方法 | 例 |
|------|---------|---|
| 明示的に実行したい | スラッシュコマンド | `/validate-pmf` |
| Claudeに判断させたい | 自然言語 | 「PMFを検証して」 |
| 全自動実行 | スラッシュコマンド | `/orchestrate-phase1` |

---

## 共通リソース

- `_shared/knowledge_base.md` - 全概念・フレームワークへのパス集
- `_shared/prompts/mentor_persona.md` - メンターペルソナ定義

## Knowledge Base

すべてのSkillsは以下のknowledge baseを参照します:

```
aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/
├── startup_science/          # フレームワーク・概念集
│   ├── 01_stages/            # ステージ別概念
│   ├── 02_frameworks/        # フレームワーク集
│   ├── 03_tactics/           # 戦術・手法
│   ├── 04_organization/      # 組織・経営
│   └── 99_reference/         # SNS戦略等
└── projects/Founder_Agent_ForStartup/
    └── Sratup_Research/      # 594件の創業者ケーススタディ
        ├── INDEX.md          # 【重要】全スキル参照用インデックス
        ├── documents/        # 9カテゴリ別ケーススタディ
        │   ├── 01_Legendary/     # 50件（Airbnb, Amazon等）
        │   ├── 02_Unicorn/       # 76件（Freshworks等）
        │   ├── 03_VC_Backed/     # 61件（Box等）
        │   └── ...               # 他6カテゴリ
        └── _analysis/
            └── research_knowledge.md  # VC投資基準・定量ベンチマーク
```

**ForStartupスキル専用Researchインデックス**:
@Founder_Agent_ForStartup/Sratup_Research/INDEX.md
- 594件のケーススタディ索引
- スキル別参照マップ（18スキル対応）
- 定量基準クイックリファレンス（15+指標）

---

## 起業の科学フレームワーク準拠率

| カテゴリ | 総数 | 実装済み | カバレッジ |
|---------|:----:|:--------:|:---------:|
| アイデア検証 | 3 | 1 | 33.3% |
| CPF | 5 | 5 | **100%** ✅ |
| PSF | 4 | 4 | **100%** ✅ |
| PMF | 7 | 6 | **85.7%** ✅ |
| スケール | 9 | 8 | **88.9%** ✅ |
| MVV | 4 | 4 | **100%** ✅ |
| ファイナンス | 3 | 2 | 66.7% |
| **合計** | **61** | **46** | **75.4%** |

**主な実装フレームワーク（新規追加分）**:
- Sean Ellisテスト（validate-pmf）
- 月次成長率（validate-pmf）
- Churn Rate（validate-pmf）
- AARRRフレームワーク（measure-aarrr）
- バーンレート・ランウェイ（monitor-burn-rate）

---

## ForStartup版スキル（VC調達特化）- 18スキル完成

ForStartup版は、VC資金調達を目指すスタートアップ創業者向けに、厳格化された評価基準とVC投資家視点を統合したスキル群です。

### 主な特徴

- **CPFスコア閾値**: 60% → **70%**（VC投資水準）
- **10倍優位性**: 2軸 → **3軸以上**（スケーラビリティ重視）
- **LTV/CAC基準**: 3.0 → **5.0以上**（Series A基準）
- **Researchナレッジ統合**: 594件のケーススタディ（Airbnb CPF 85%, Freshworks 80%, Box 70%）
- **定量ベンチマーク**: 15+指標（月次成長率20%+、NPS 50+、LTV/CAC 5.0+）
- **新規スキル**: ピッチデッキ自動生成、VC対応Q&A、資金調達ロードマップ、スコアカード

**Researchインデックス**: @Founder_Agent_ForStartup/Sratup_Research/INDEX.md
- 各スキルの適用事例・定量基準を参照可能
- 9カテゴリ別ケーススタディ（Legendary 50件、Unicorn 76件、VC_Backed 61件等）
- スキル別参照マップ（18スキル × 3-5事例）

### ForStartup版スキル一覧（18スキル）

#### Phase 1: 需要発見・企画（8スキル）

| Skill | コマンド | 用途 | 所要時間 | Origin差分 |
|-------|---------|------|:--------:|:-----------|
| Discover Demand | `/discover-demand` | 需要発見（VC基準） | 15-30分 | VC基準適用 |
| Create MVV | `/create-mvv` | MVV定義 | 20-40分 | スケール重視 |
| Create Persona | `/create-persona` | ペルソナ作成 | 15-30分 | 30人推奨 |
| Build Flywheel | `/build-flywheel` | フライホイール設計 | 30-50分 | NW効果強調 |
| Research Problem | `/research-problem` | 課題調査 | 30-60分 | 定量抽出 |
| Simulate Interview | `/simulate-interview` | 仮想インタビュー | 25-45分 | 3U厳格化 |
| Validate CPF | `/validate-cpf` | CPF検証（VC投資基準70%） | 20-40分 | **70%閾値** |
| Research Competitors | `/research-competitors` | 競合調査 | 40-70分 | VC視点 |

#### Phase 2-3: PSF/PMF検証・スケール（6スキル）

| Skill | コマンド | 用途 | 所要時間 | Origin差分 |
|-------|---------|------|:--------:|:-----------|
| Validate 10x | `/validate-10x` | 10倍優位性検証（3軸以上） | 40-70分 | **3軸必須** |
| Validate PSF | `/validate-psf` | PSF検証（厳格版） | 20-40分 | MVP必須 |
| Validate PMF | `/validate-pmf` | PMF検証（厳格版） | 20-40分 | 厳格版 |
| Measure AARRR | `/measure-aarrr` | AARRR分析 | 40-50分 | 20%/月 |
| Validate Unit Economics | `/validate-unit-economics` | ユニットエコノミクス（LTV/CAC 5.0+） | 30-50分 | **5.0+基準** |
| Monitor Burn Rate | `/monitor-burn-rate` | バーンレート監視 | 5-10分 | 18ヶ月 |

#### 資金調達特化（4スキル）- **ForStartup新規**

| Skill | コマンド | 用途 | 所要時間 | 備考 |
|-------|---------|------|:--------:|:-----|
| **Build Pitch Deck** | `/build-pitch-deck` | VCピッチデッキ自動生成（10-15スライド） | 30-45分 | Airbnb/Freshworks/Boxパターン |
| **Prepare VC Meeting** | `/prepare-vc-meeting` | VC対応Q&A準備（50質問・8カテゴリ） | 60-90分 | 準備度スコア付き |
| **Create Fundraising Plan** | `/create-fundraising-plan` | 資金調達ロードマップ（Pre-Seed→Series B） | 15-30分 | 4ラウンド計画 |
| **Startup Scorecard** | `/startup-scorecard` | VC投資基準でのスコアカード評価 | 30-60分 | 35点以上でVC推奨 |

### Build Pitch Deck スキルの特徴

**VCピッチデッキ自動生成**（10-15スライド構成）:

| スライド | 内容 | 配点 |
|---------|------|:----:|
| Problem | 課題・3Uスコア・定量データ | 10点 |
| Solution | UVP・Before/After・MVP | 10点 |
| Market Size | TAM/SAM/SOM・市場成長率 | 10点 |
| Product | プロダクト詳細・ロードマップ | 10点 |
| Traction | KPI・成長率・NPS | **15点** |
| Business Model | 収益モデル・LTV/CAC | **15点** |
| Competition | 10倍優位性・参入障壁 | 10点 |
| Go-to-Market | GTM戦略・フライホイール | 10点 |
| Team | 創業チーム・FIF | 10点 |
| Financials | 3年予測・損益分岐点 | 10点 |
| Ask | 調達額・資金使途 | 10点 |

**投資家説得力スコア**:
- 110-130点: 優秀（即Series A調達推奨）
- 90-109点: 良好（弱点改善後に調達）
- 70-89点: 要改善（3ヶ月改善後に再提出）
- 70点未満: 再構築（CPF/PSF再検証）

**参照ナレッジ**:
- Airbnb: $100B+ IPO、Paul Graham評価ポイント
- Freshworks: $12-13B IPO、競合比較・価格戦略
- Box: $3.5B IPO、ボトムアップ採用モデル

### ForStartup版の使い方

```bash
# VC調達準備フロー（推奨順序）
/validate-cpf              # CPF検証（70%以上必須）
/validate-10x              # 10倍優位性検証（3軸以上）
/validate-unit-economics   # ユニットエコノミクス（LTV/CAC 5.0+）
/build-pitch-deck          # ピッチデッキ自動生成（NEW!）

# 次のステップ（今後実装予定）
/prepare-vc-meeting        # VC対応Q&A準備
/create-fundraising-plan   # 資金調達ロードマップ
```

---

## 開発ガイドライン

新しいSkillを追加する際は:

1. 適切なカテゴリディレクトリ配下に配置
2. 対話型プロンプト設計（質問→回答→提案）
3. knowledge_baseへの参照を含める
4. 具体的アクションアイテム提示

---

## ライセンス

内部利用のみ。
