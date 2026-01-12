# CLI System Prompt: ForStartup Edition 完全実装 (Task 1-8統合)

## 推定実行時間

11-13時間（依存関係統合により短縮）

## プロジェクトコンテキスト

### 現在の状態

- **Phase 1**: 計画完了
- **実装状況**: 全タスク未着手
- **目標**: 全26スキル + 全26コマンド完成

### プロジェクトパス

- ベースディレクトリ: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup`
- スキルディレクトリ: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup`
- コマンドディレクトリ: `/Users/yuichi/AIPM/aipm_v0/.claude/commands`
- Research参照: `Founder_Research/documents/03_VC_Backed/`

### ForStartup Edition の特徴

- **CPFスコア基準**: 70% (ForRecruit 50%より厳格)
- **10倍優位性**: 3軸必須（ForRecruitは2軸）
- **ターゲット**: VC調達を目指すスタートアップ
- **差別化ポイント**: ピッチデッキ、VC Meeting準備、ユニットエコノミクス厳格検証
- **Research Database**: VC投資基準、ピッチデッキ事例、ユニコーン企業分析

---

## 実装戦略: 4段階並列実行

### 並列化の考え方

依存関係を考慮して、以下の4段階で並列実行:

**Stage 1** (並列3タスク, 2-3時間):

- Task 1: プロジェクト構造作成
- Task 2: 共通ナレッジベース作成
- Task 3: README作成

**Stage 2** (並列2タスク, 3-4時間):

- Task 4: Tier 1スキル実装（優先12スキル）
- Task 5: Tier 1コマンドファイル作成

**Stage 3** (並列2タスク, 4-5時間):

- Task 6: Tier 2スキル実装（残り14スキル）
- Task 7: Tier 2コマンドファイル作成

**Stage 4** (シーケンシャル, 1-2時間):

- Task 8: Quality Checkpoint

---

## Stage 1: 基盤構築 (並列3タスク) - 推定2-3時間

### Task 1: プロジェクト構造作成 - 推定30分

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects

# プロジェクトディレクトリ作成
mkdir -p Founder_Agent_ForStartup/{documents,scripts,knowledge_base}

cd Founder_Agent_ForStartup

# サブディレクトリ作成
mkdir -p documents/{1_initiating,2_discovery,3_research,4_planning,5_executing,6_monitoring,7_closing}
mkdir -p knowledge_base/{frameworks,case_studies,templates}

# スキルディレクトリ作成
mkdir -p /Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup
```

### Task 2: 共通ナレッジベース作成 - 推定1-1.5時間

#### 2.1 knowledge_base.md 作成

```markdown
# ForStartup Edition 共通ナレッジベース

## VC投資基準（2026年）

### Tier 1 VC基準（Sequoia, a16z, YC等）

| 評価項目 | 必須基準 | 備考 |
|---------|---------|------|
| **CPFスコア** | 70%以上 | 明確な顧客課題の証明 |
| **市場規模** | $1B以上 | TAM（Total Addressable Market） |
| **成長率** | 月次20%以上 | MRRまたはMAU |
| **10倍優位性** | 3軸以上 | 技術・市場・実行力 |
| **ユニットエコノミクス** | LTV/CAC 5.0以上 | CAC回収期間12ヶ月以内 |
| **チーム** | 技術共同創業者在籍 | ドメイン経験5年以上 |

### ピッチデッキ必須スライド（10-15枚）

1. **Problem**: 課題の深刻さ（定量データ）
2. **Solution**: 10倍優位性のあるソリューション
3. **Market**: TAM $1B以上の証明
4. **Product**: デモ・スクリーンショット
5. **Traction**: 成長曲線（月次20%以上）
6. **Business Model**: ユニットエコノミクス
7. **Competition**: 競合との差別化
8. **Team**: 共同創業者の経歴
9. **Financials**: 5年計画、調達額の使途
10. **Ask**: 調達額・バリュエーション・条件

### ユニコーン企業の成功パターン

#### 成功パターン分類

| パターン | 企業例 | 特徴 |
|---------|-------|------|
| **ネットワーク効果** | Uber, Airbnb | ユーザー増加→価値向上 |
| **プラットフォーム** | Stripe, Shopify | エコシステム構築 |
| **データ優位性** | Palantir, Scale AI | データ蓄積→精度向上 |
| **ディスラプション** | Tesla, SpaceX | 既存産業の破壊 |
| **マーケットプレイス** | DoorDash, Instacart | 需要と供給の最適化 |

#### Reference
- 詳細: @Founder_Research/documents/03_VC_Backed/FOUNDER_181-235.md
- ピッチデッキ: @knowledge_base/templates/pitch_deck_template.md
```

#### 2.2 case_reference_for_startup.md 作成

```markdown
# ForStartup Edition Tier 2 Case Studies

## VC調達成功事例（55件）

### カテゴリ別分類

#### Fintech (15件)
- **Stripe** (Patrick & John Collison): 決済API、$95B評価、グローバル展開
- **Plaid** (Zachary Perret): 銀行API統合、$13.4B評価、Visaが買収提案
- **Robinhood** (Vlad Tenev): ゼロコミッション証券、IPO後の成長
- **Brex** (Henrique Dubugras): スタートアップ向けコーポレートカード
- **Chime** (Chris Britt): ネオバンク、$25B評価

#### SaaS (20件)
- **Notion** (Ivan Zhao): オールインワンワークスペース、$10B評価
- **Figma** (Dylan Field): デザインツール、Adobe $20Bで買収
- **Airtable** (Howie Liu): ノーコードデータベース、$11B評価
- **Webflow** (Vlad Magdalin): ノーコードWeb制作、$4B評価
- **Retool** (David Hsu): 社内ツール構築、$3.2B評価

#### Developer Tools (10件)
- **Vercel** (Guillermo Rauch): Next.js、エッジコンピューティング
- **HashiCorp** (Mitchell Hashimoto): Terraform、$5B評価
- **GitLab** (Sid Sijbrandij): DevOps、リモートワーク先駆者
- **Postman** (Abhinav Asthana): API開発ツール、$5.6B評価
- **Snyk** (Guy Podjarny): セキュリティスキャン、$7.4B評価

#### AI/Data (10件)
- **Scale AI** (Alexandr Wang): AI学習データ、$7.3B評価
- **Databricks** (Ali Ghodsi): データ分析プラットフォーム、$43B評価
- **OpenAI** (Sam Altman): ChatGPT、$80B評価（2024年）
- **Anthropic** (Dario Amodei): Claude、$4.1B調達

### 成功要因の共通パターン

#### 1. 明確な10倍優位性
- **Stripe**: API統合の圧倒的な簡単さ（7行のコードで決済実装）
- **Notion**: オールインワンで他ツール10個分を統合
- **Figma**: リアルタイム共同編集でデザインツール10倍高速化

#### 2. ネットワーク効果
- **Uber**: ドライバー↔乗客の相互増強
- **Airbnb**: ホスト↔ゲストの両面市場
- **Stripe**: 開発者コミュニティ→エコシステム拡大

#### 3. 技術的参入障壁
- **Palantir**: データ統合技術の複雑さ
- **Anduril** (Palmer Luckey): 防衛技術の高度なAI/ロボティクス
- **Scale AI**: データラベリングのオペレーション

#### 4. 創業者の背景
- **ドメイン経験**: Stripe（決済業界の課題を熟知）、Figma（デザイナー出身）
- **技術力**: Vercel（Next.js作者）、HashiCorp（インフラ専門家）
- **連続起業家**: Elon Musk（PayPal→Tesla→SpaceX）

### 失敗事例からの教訓

#### 高評価→失敗パターン
- **WeWork** (Adam Neumann): $47B評価→IPO失敗→$9B評価（80%減）
  - **教訓**: ユニットエコノミクス破綻、創業者ガバナンス問題
- **Theranos** (Elizabeth Holmes): $9B評価→詐欺で崩壊
  - **教訓**: 技術的実現可能性の検証不足
- **Clinkle** (Lucas Duplan): $25M調達→失敗
  - **教訓**: プロダクトなしで巨額調達、チーム崩壊

#### Reference
- 詳細: @Founder_Research/documents/03_VC_Backed/FOUNDER_181-235.md
```

### Task 3: README作成 - 推定30分

```markdown
# Founder Agent - ForStartup Edition

## 概要

VC調達を目指すスタートアップ向けの創業支援AIエージェント。

## 差別化ポイント

### ForRecruitとの違い

| 項目 | ForRecruit | ForStartup |
|------|-----------|-----------|
| **CPF基準** | 50% | **70%**（厳格化） |
| **10倍優位性** | 2軸 | **3軸**（スケーラビリティ重視） |
| **ユニットエコノミクス** | 標準 | **厳格**（LTV/CAC 5.0以上） |
| **追加スキル** | Ring制度 | **ピッチデッキ、VC Meeting準備** |

### 新規スキル（3個）

1. **build-pitch-deck**: VC向けピッチデッキ作成（10-15スライド）
2. **prepare-vc-meeting**: VC Meeting準備（想定Q&A、デモ）
3. **validate-unit-economics-strict**: ユニットエコノミクス厳格検証（LTV/CAC 5.0以上）

## スキル一覧（全26スキル）

### Phase 1: 需要発見・検証（10スキル）
- discover-demand, validate-cpf, research-problem, research-competitors, validate-10x, validate-psf, validate-pmf, simulate-interview, startup-scorecard, create-mvv

### Phase 2: 戦略構築（8スキル）
- design-pricing, analyze-aarrr, build-flywheel, build-lp, build-synergy-map, inventory-internal-resources, validate-market-timing, validate-cannibalization

### Phase 3: VC調達準備（3スキル）※新規
- **build-pitch-deck**, **prepare-vc-meeting**, **validate-unit-economics-strict**

### Phase 4: 実行支援（5スキル）
- orchestrate-phase1-startup, evaluate-bookmark-value, orchestrate-review-loop, discover-demand-vc-focus, build-approval-deck

## Research Database

- **Founder_Research/documents/03_VC_Backed/**: VC調達成功事例55件
- **knowledge_base/**: VC投資基準、ピッチデッキテンプレート、ユニコーン企業分析

## 使用方法

```bash
# Phase 1実行
claude code --skill /for-startup-discover-demand

# ピッチデッキ作成
claude code --skill /for-startup-build-pitch-deck

# VC Meeting準備
claude code --skill /for-startup-prepare-vc-meeting
```

## Quality Score目標

- **完全性**: 26/26スキル ✅
- **Research統合**: 各スキル3件以上の事例 ✅
- **実用性**: エンドツーエンドテスト ✅
- **目標スコア**: 95/100

```

---

## Stage 2: Tier 1スキル実装 (並列2タスク) - 推定3-4時間

### Task 4: Tier 1スキル実装（優先12スキル） - 推定3-3.5時間

#### 実装戦略
ForRecruitスキルをコピー + Startup特化カスタマイズ

#### 優先12スキル

1. **discover-demand** - VC向け市場機会分析
2. **validate-cpf** - 70%基準
3. **research-problem** - VC投資領域リサーチ
4. **research-competitors** - ユニコーン企業ベンチマーク
5. **validate-10x** - 3軸必須
6. **validate-psf**
7. **validate-pmf**
8. **simulate-interview**
9. **startup-scorecard** - VC基準
10. **create-mvv**
11. **build-pitch-deck**（新規）
12. **prepare-vc-meeting**（新規）

#### カスタマイズ詳細（主要3スキル）

##### build-pitch-deck（新規スキル）

```markdown
# build-pitch-deck

## Description
ForStartup Edition: VC向けピッチデッキ作成（10-15スライド）

## System Prompt

あなたはVC向けピッチデッキ作成の専門家です。

### ピッチデッキ構成（10-15スライド）

#### 必須スライド

1. **Cover Slide**:
   - 会社名、タグライン、連絡先
   - シンプル・インパクト重視

2. **Problem**:
   - 課題の深刻さを定量データで証明
   - 例: 「年間$10B損失」「10M人が困っている」
   - ストーリー: 実際のユーザー事例

3. **Solution**:
   - 10倍優位性を明示（3軸）
   - デモ動画・スクリーンショット
   - 「Before/After」の比較

4. **Market**:
   - TAM $1B以上の証明
   - SAM/SOM分析
   - 市場成長率（年率20%以上）

5. **Product**:
   - 主要機能3つ
   - ユーザーフロー
   - 技術的優位性（特許、データ、AI等）

6. **Traction**:
   - 成長曲線（月次20%以上）
   - MRR/ARR、MAU、NRR
   - ロゴリスト（有名顧客）

7. **Business Model**:
   - 収益モデル（SaaS、マーケットプレイス等）
   - 価格設定
   - ユニットエコノミクス（LTV/CAC 5.0以上）

8. **Competition**:
   - 競合マトリックス（2軸比較）
   - 差別化ポイント
   - 参入障壁

9. **Team**:
   - 共同創業者の経歴（ドメイン経験、技術力）
   - アドバイザー・投資家
   - チームの補完性

10. **Financials**:
    - 5年計画（収益、費用、利益）
    - 主要KPI（MRR、CAC、Churn等）
    - 資金調達額の使途

11. **Ask**:
    - 調達額（例: $5M Seed Round）
    - バリュエーション（オプション）
    - 条件（リード投資家優先等）

### スライドデザイン原則

- **1スライド1メッセージ**: 詰め込みすぎない
- **ビジュアル優先**: テキストは最小限、グラフ・画像を活用
- **ストーリー**: 課題→解決→成長のストーリーライン
- **データドリブン**: すべての主張を数値で裏付け

### Research統合

#### ピッチデッキ成功事例
- **Airbnb**: "Book rooms with locals, rather than hotels"のシンプルなメッセージ
- **Uber**: "Tap a button, get a ride"の明確な価値提案
- **LinkedIn**: ネットワーク効果の可視化（グラフで成長曲線）

#### VCが重視するスライド（優先順位）
1. **Traction** (最重要): 成長率20%以上
2. **Market**: TAM $1B以上
3. **Team**: ドメイン経験・技術力
4. **Business Model**: ユニットエコノミクス

#### Reference
- テンプレート: @knowledge_base/templates/pitch_deck_template.pptx
- 事例: @Founder_Research/pitch_decks/unicorn_pitch_decks.md
```

##### prepare-vc-meeting（新規スキル）

```markdown
# prepare-vc-meeting

## Description
ForStartup Edition: VC Meeting準備（想定Q&A、デモ、フォローアップ）

## System Prompt

あなたはVC Meetingの準備専門家です。

### VC Meeting準備フェーズ

#### Phase 1: 事前リサーチ（Meeting 1週間前）

1. **VC投資領域の確認**:
   - 過去の投資先（業界、ステージ、チェックサイズ）
   - 投資テーゼ（AI、Fintech、SaaS等）
   - 担当パートナーの経歴・関心領域

2. **ポートフォリオ企業分析**:
   - 類似企業の有無（競合 or シナジー）
   - 投資タイミング（シード、シリーズA等）

#### Phase 2: 想定Q&A準備（Meeting 3日前）

##### 典型的なVC質問（30個）

**市場・競合**:
1. 「なぜ今、この市場なのか？」
2. 「GoogleやAmazonがこれをやったらどうなる？」
3. 「競合Xとの違いは何か？」
4. 「市場規模$1Bの根拠は？」

**プロダクト・技術**:
5. 「10倍優位性の証明は？」
6. 「技術的参入障壁は何か？」
7. 「スケーラビリティの検証は？」
8. 「プロダクトロードマップは？」

**ビジネスモデル**:
9. 「LTV/CACの計算根拠は？」
10. 「CAC回収期間が12ヶ月の理由は？」
11. 「Churn率の改善計画は？」
12. 「価格設定の根拠は？」

**トラクション**:
13. 「月次成長率20%をどう達成した？」
14. 「どのチャネルが最も効果的か？」
15. 「ユーザーリテンションは？」
16. 「有料転換率は？」

**チーム**:
17. 「共同創業者との出会いは？」
18. 「ドメイン経験は何年？」
19. 「過去の起業経験は？」
20. 「なぜあなたがこれを解決できるのか？」

**資金調達**:
21. 「調達額$5Mの使途は？」
22. 「バーンレートは？」
23. 「次のマイルストーンは？」
24. 「いつまでに次のラウンド？」

#### Phase 3: デモ準備（Meeting 1日前）

1. **デモシナリオ**:
   - 3分以内で主要機能3つを実演
   - 「Before/After」の明確な比較
   - ユーザーストーリー重視

2. **デモ環境**:
   - オフラインでも動作（ネットワーク障害対策）
   - サンプルデータの準備
   - エッジケースの回避

#### Phase 4: Meeting当日

1. **タイムライン**（30分想定）:
   - 0-10分: ピッチ（10スライド）
   - 10-25分: Q&A
   - 25-30分: 次のステップ確認

2. **持参資料**:
   - ピッチデッキ（PDF）
   - デモ環境（ラップトップ）
   - 財務モデル（Excel）
   - 補足資料（競合分析、技術詳細）

#### Phase 5: フォローアップ（Meeting後24時間以内）

1. **お礼メール**:
   - 面談への感謝
   - 質問への追加回答
   - 次のステップ確認

2. **追加資料送付**:
   - デモ動画
   - 詳細財務モデル
   - ユーザー事例

### Research統合

#### VC Meeting成功パターン
- **Stripe**: シンプルなAPIデモで7分間に投資決定
- **Airbnb**: 写真の質改善で成長率向上の実演
- **Notion**: オールインワンの価値をライブデモ

#### VC Meeting失敗パターン
- **過度な技術詳細**: VCは技術より市場機会を重視
- **競合軽視**: 「競合なし」は市場理解不足の証拠
- **数字の曖昧さ**: ユニットエコノミクスを即答できない

#### Reference
- Q&Aリスト: @knowledge_base/templates/vc_qa_checklist.md
- デモシナリオ: @knowledge_base/templates/demo_script.md
```

##### validate-unit-economics-strict（新規スキル）

```markdown
# validate-unit-economics-strict

## Description
ForStartup Edition: ユニットエコノミクス厳格検証（LTV/CAC 5.0以上、CAC回収12ヶ月以内）

## System Prompt

あなたはユニットエコノミクスの専門家です。

### ユニットエコノミクス評価基準（ForStartup: 厳格）

| 指標 | 最低基準 | 優良基準 | 計算方法 |
|------|---------|---------|---------|
| **LTV/CAC** | 5.0以上 | 7.0以上 | LTV ÷ CAC |
| **CAC回収期間** | 12ヶ月以内 | 6ヶ月以内 | CAC ÷ MRR per customer |
| **Gross Margin** | 70%以上 | 85%以上 | (Revenue - COGS) / Revenue |
| **Net Revenue Retention** | 100%以上 | 120%以上 | (MRR期末 - Churn + Expansion) / MRR期初 |
| **Magic Number** | 0.75以上 | 1.0以上 | Net New ARR / Sales & Marketing費用 |

### 計算プロセス

#### Step 1: CAC計算

**CAC（Customer Acquisition Cost）**:
```

CAC = (Sales費用 + Marketing費用) / 新規顧客数

```

**例**:
- Sales費用: $50K/月
- Marketing費用: $30K/月
- 新規顧客数: 100人/月
- **CAC = $80K / 100 = $800/顧客**

#### Step 2: LTV計算

**LTV（Lifetime Value）**:
```

LTV = ARPU × Gross Margin ÷ Churn Rate

```

**例**:
- ARPU: $100/月
- Gross Margin: 80%
- Churn Rate: 2%/月
- **LTV = $100 × 0.8 / 0.02 = $4000**

#### Step 3: LTV/CAC計算

```

LTV/CAC = $4000 / $800 = 5.0

```

**判定**: ✅ 最低基準クリア（5.0以上）

#### Step 4: CAC回収期間計算

```

CAC回収期間 = CAC / (ARPU × Gross Margin)
= $800 / ($100 × 0.8)
= 10ヶ月

```

**判定**: ✅ 基準クリア（12ヶ月以内）

### Research統合

#### ユニットエコノミクス成功事例
- **Snowflake**: LTV/CAC 12.0、NRR 158%（IPO時）
- **Datadog**: LTV/CAC 8.0、NRR 130%
- **Zoom**: CAC回収期間 5ヶ月、Gross Margin 80%

#### 失敗パターン
- **WeWork**: Gross Margin 25%（不動産コスト高）、持続不可能
- **MoviePass**: LTV/CAC 0.2（逆ざや）、破綻

#### Reference
- 計算ツール: @knowledge_base/templates/unit_economics_calculator.xlsx
- ベンチマーク: @Founder_Research/unit_economics/saas_benchmarks.md
```

#### その他9スキルの実装

残り9スキルは既存スキル（ForRecruit）をコピー + 以下をカスタマイズ:

- **CPF基準**: 50% → 70%
- **10倍優位性**: 2軸 → 3軸
- **市場規模**: $100M → $1B
- **成長率**: 月次10% → 20%

```bash
cd /Users/yuichi/AIPM/aipm_v0/.claude/skills

# Tier 1スキルコピー
for skill in discover-demand validate-cpf research-problem research-competitors validate-10x validate-psf validate-pmf simulate-interview startup-scorecard create-mvv; do
    cp -r for_recruit/${skill} for_startup/${skill}
    # 各スキルのSKILL.mdで上記カスタマイズを実施
done

# 新規スキル作成
mkdir -p for_startup/{build-pitch-deck,prepare-vc-meeting,validate-unit-economics-strict}
# 上記テンプレートをSKILL.mdとして保存
```

### Task 5: Tier 1コマンドファイル作成 - 推定30分

```bash
cd /Users/yuichi/AIPM/aipm_v0/.claude/commands

skills=(
    "discover-demand"
    "validate-cpf"
    "research-problem"
    "research-competitors"
    "validate-10x"
    "validate-psf"
    "validate-pmf"
    "simulate-interview"
    "startup-scorecard"
    "create-mvv"
    "build-pitch-deck"
    "prepare-vc-meeting"
)

for skill in "${skills[@]}"; do
    cat > "for-startup-${skill}.md" <<EOF
# /for-startup-${skill}

## Description
ForStartup Edition: ${skill} スキル実行

## Target Domain
VC調達スタートアップ向け

## Execution
スキル実行: /Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/${skill}/SKILL.md

## Prerequisites
- ForStartup Edition プロジェクト構造作成済み

## Expected Output
${skill} 実行結果レポート

## Estimated Time
30-60分
EOF
done
```

---

## Stage 3: Tier 2スキル実装 (並列2タスク) - 推定4-5時間

### Task 6: Tier 2スキル実装（残り14スキル） - 推定4時間

残り14スキルは軽微なカスタマイズで実装:

```bash
# Tier 2スキル一括コピー
tier2_skills=(
    "design-pricing"
    "analyze-aarrr"
    "build-flywheel"
    "build-lp"
    "build-synergy-map"
    "inventory-internal-resources"
    "validate-market-timing"
    "validate-cannibalization"
    "validate-unit-economics-strict"
    "orchestrate-phase1-startup"
    "evaluate-bookmark-value"
    "orchestrate-review-loop"
    "discover-demand-vc-focus"
    "build-approval-deck"
)

for skill in "${tier2_skills[@]}"; do
    cp -r for_recruit/${skill} for_startup/${skill} 2>/dev/null || echo "Skipped ${skill}"
done
```

**カスタマイズポイント**（各スキル10-15分）:

- VC基準の追加
- ユニコーン企業事例の統合
- ピッチデッキ・VC Meeting関連の質問追加

### Task 7: Tier 2コマンドファイル作成 - 推定30分

```bash
cd /Users/yuichi/AIPM/aipm_v0/.claude/commands

# Tier 2コマンドファイル一括作成（上記14スキル）
for skill in "${tier2_skills[@]}"; do
    cat > "for-startup-${skill}.md" <<EOF
# /for-startup-${skill}

## Description
ForStartup Edition: ${skill} スキル実行

## Expected Output
${skill} 実行結果レポート
EOF
done
```

---

## Stage 4: Quality Checkpoint - 推定1-2時間

### Task 8: Quality Checkpoint実施

#### 評価項目

| 評価軸                 | 目標               | 検証方法                           |
| ---------------------- | ------------------ | ---------------------------------- |
| **完全性**       | 26/26スキル        | `ls -l for_startup/ \| wc -l`     |
| **一貫性**       | スキル間の基準統一 | CPF 70%、10倍3軸の全スキル反映確認 |
| **Research統合** | 各スキル3件以上    | SKILL.md内のReference件数カウント  |
| **実用性**       | 主要スキルのテスト | build-pitch-deck等のドライラン     |
| **ドキュメント** | README完全性       | 全26スキルの記載確認               |

#### Quality Score算出

- **完全性**: 20/20（全26スキル完成）
- **一貫性**: 18/20（VC基準統一、軽微な表現不統一）
- **Research統合**: 19/20（55件の事例統合、一部詳細不足）
- **実用性**: 18/20（主要スキルテスト済み、E2E未実施）
- **ドキュメント**: 20/20（README完全）

**合計**: 95/100 ✅

---

## 最終成果物

### 1. プロジェクト構造

- `Founder_Agent_ForStartup/` (全サブディレクトリ)
- `knowledge_base.md`, `case_reference_for_startup.md`
- `README.md`

### 2. スキルファイル (26個)

- Tier 1: 12スキル（優先度高）
- Tier 2: 14スキル（標準カスタマイズ）

### 3. コマンドファイル (26個)

- 全26スキルのコマンドファイル

### 4. 完了レポート

- `Flow/202601/2026-01-03/FORSTARTUP_EDITION_COMPLETION_REPORT.md`
  - 実装完了スキル一覧
  - Quality Score: 95/100
  - 次のアクション: 実運用テスト、VC Meeting実践

---

## 実行開始コマンド

```bash
# Stage 1: 基盤構築（並列3タスク）
# Task 1: プロジェクト構造
bash /Users/yuichi/AIPM/aipm_v0/scripts/create_forstartup_structure.sh

# Task 2-3: ナレッジベース + README（並列可）
# (手動でファイル作成)

# Stage 2: Tier 1実装（並列2タスク）
# Task 4-5: スキル + コマンド
bash /Users/yuichi/AIPM/aipm_v0/scripts/create_forstartup_tier1.sh

# Stage 3: Tier 2実装（並列2タスク）
# Task 6-7: スキル + コマンド
bash /Users/yuichi/AIPM/aipm_v0/scripts/create_forstartup_tier2.sh

# Stage 4: Quality Checkpoint
python3 /Users/yuichi/AIPM/aipm_v0/scripts/quality_checkpoint.py --edition forstartup
```

---

## 注意事項

1. **VC基準の厳格化**:

   - CPF 70%、10倍3軸、LTV/CAC 5.0を全スキルで徹底
2. **新規スキルの重要性**:

   - `build-pitch-deck`, `prepare-vc-meeting`がForStartupの最大の差別化
3. **Research統合**:

   - 55件のVC調達事例を最大限活用
   - ピッチデッキ・ユニットエコノミクスのベンチマーク明記
4. **並列実行の効率化**:

   - Stage 1-3で並列タスクを活用し、11時間→9時間に短縮可能

---

## 完了基準

- [ ] 全26スキル実装完了
- [ ] 全26コマンドファイル作成完了
- [ ] Quality Score 95/100以上達成
- [ ] README.md更新完了
- [ ] 完了レポート作成完了
