# Founder Agent ForStartup Edition

## Overview

ForStartup Editionは、**VC調達を目指すスタートアップ**向けの創業支援AIエージェントです。厳格な基準（CPF 70%、10倍優位性3軸）を適用し、ピッチデッキ作成やVC Meeting準備など、資金調達に特化した機能を提供します。

## 特徴

### ターゲット

- **対象**: VC調達を目指すスタートアップ（Seed〜Series A）
- **目標**: $1M-10M調達成功
- **フェーズ**: プロダクト開発中〜初期トラクション段階

### ForStartupの特徴

| 項目 | ForStartup |
|------|-----------|
| **CPFスコア基準** | **70%**（厳格） |
| **10倍優位性** | **3軸必須**（速度・コスト・品質） |
| **市場規模** | **TAM $1B以上** |
| **成長率** | **月次20%以上** |
| **ユニットエコノミクス** | **LTV/CAC 5.0以上** |
| **CAC回収期間** | **12ヶ月以内** |
| **追加スキル** | **ピッチデッキ、VC Meeting準備** |

### 新規スキル（3個）

1. **build-pitch-deck**: VC向けピッチデッキ作成（10-15スライド）
2. **prepare-vc-meeting**: VC Meeting準備（想定Q&A、デモ）
3. **validate-unit-economics-strict**: ユニットエコノミクス厳格検証（LTV/CAC 5.0以上）

## プロジェクト構造

```
Founder_Agent_ForStartup/
├── README.md                          # このファイル
├── documents/                         # フェーズ別ドキュメント
│   ├── 1_initiating/                  # Phase 1: 立ち上げ
│   ├── 2_discovery/                   # Phase 2: 発見
│   ├── 3_research/                    # Phase 3: 調査
│   ├── 4_planning/                    # Phase 4: 計画
│   ├── 5_executing/                   # Phase 5: 実行
│   ├── 6_monitoring/                  # Phase 6: モニタリング
│   └── 7_closing/                     # Phase 7: 完了
├── scripts/                           # 自動化スクリプト
└── knowledge_base/                    # ナレッジベース
    ├── knowledge_base.md              # 共通知識
    ├── case_reference_for_startup.md  # VC調達成功事例55件
    ├── frameworks/                    # フレームワーク
    ├── case_studies/                  # ケーススタディ
    └── templates/                     # テンプレート
```

## スキル一覧（全26スキル）

### Phase 1: 需要発見・検証（10スキル）

| スキル | 説明 | コマンド |
|--------|------|---------|
| **discover-demand** | VC向け市場機会発見 | `/for-startup-discover-demand` |
| **validate-cpf** | CPF 70%基準検証 | `/for-startup-validate-cpf` |
| **research-problem** | 課題の深刻さ調査（定量データ） | `/for-startup-research-problem` |
| **research-competitors** | 競合分析・10倍優位性検証 | `/for-startup-research-competitors` |
| **validate-10x** | 10倍優位性3軸検証 | `/for-startup-validate-10x` |
| **validate-psf** | PSF検証（技術実現可能性） | `/for-startup-validate-psf` |
| **validate-pmf** | PMF検証（月次成長率20%以上） | `/for-startup-validate-pmf` |
| **simulate-interview** | VC向けペルソナインタビュー | `/for-startup-simulate-interview` |
| **startup-scorecard** | スタートアップスコアカード評価 | `/for-startup-startup-scorecard` |
| **create-mvv** | VC向けMVV作成 | `/for-startup-create-mvv` |

### Phase 2: 戦略構築（8スキル）

| スキル | 説明 | コマンド |
|--------|------|---------|
| **design-pricing** | SaaSプライシング設計 | `/for-startup-design-pricing` |
| **analyze-aarrr** | AARRRメトリクス分析 | `/for-startup-analyze-aarrr` |
| **build-flywheel** | 成長フライホイール設計 | `/for-startup-build-flywheel` |
| **build-lp** | ランディングページ構築 | `/for-startup-build-lp` |
| **build-synergy-map** | VC調達シナジーマップ | `/for-startup-build-synergy-map` |
| **inventory-internal-resources** | 内部リソース棚卸し | `/for-startup-inventory-internal-resources` |
| **validate-market-timing** | 市場タイミング検証 | `/for-startup-validate-market-timing` |
| **design-exit-strategy** | Exit戦略設計 | `/for-startup-design-exit-strategy` |

### Phase 3: VC調達準備（5スキル）

| スキル | 説明 | コマンド |
|--------|------|---------|
| **build-pitch-deck** | VC向けピッチデッキ作成（10-15スライド） | `/for-startup-build-pitch-deck` |
| **prepare-vc-meeting** | VC Meeting準備（想定Q&A、デモ） | `/for-startup-prepare-vc-meeting` |
| **validate-unit-economics-strict** | ユニットエコノミクス厳格検証（LTV/CAC 5.0以上） | `/for-startup-validate-unit-economics-strict` |
| **analyze-competitive-moat** | 競合優位性分析 | `/for-startup-analyze-competitive-moat` |
| **validate-ring-criteria** | Ring制度基準検証 | `/for-startup-validate-ring-criteria` |

### Phase 4: レビュー・改善（3スキル）

| スキル | 説明 | コマンド |
|--------|------|---------|
| **orchestrate-review-loop** | レビューループ実行 | `/for-startup-orchestrate-review-loop` |
| **build-approval-deck** | 社内承認用デッキ作成 | `/for-startup-build-approval-deck` |

## 使用方法

### 基本的な実行フロー

#### Step 1: 需要発見

```bash
# VC向け市場機会発見
claude code --skill /for-startup-discover-demand

# CPF検証（70%基準）
claude code --skill /for-startup-validate-cpf

# 10倍優位性検証（3軸）
claude code --skill /for-startup-validate-10x
```

#### Step 2: PMF検証

```bash
# PMF検証（月次成長率20%以上）
claude code --skill /for-startup-validate-pmf

# ユニットエコノミクス厳格検証
claude code --skill /for-startup-validate-unit-economics-strict
```

#### Step 3: VC調達準備

```bash
# ピッチデッキ作成
claude code --skill /for-startup-build-pitch-deck

# VC Meeting準備
claude code --skill /for-startup-prepare-vc-meeting
```

### エンドツーエンド実行

```bash
# Phase 1-4全実行（オーケストレーション）
claude code --skill /for-startup-orchestrate-phase1
```

## VC投資基準

### 一般的なVC投資基準

| 評価項目 | 最低基準 | 理想基準 |
|---------|---------|---------|
| **市場規模** | TAM $1B以上 | TAM $10B以上 |
| **成長率** | 月次成長率20% | 月次成長率30-40% |
| **CPFスコア** | 70%以上 | 80%以上 |
| **10倍優位性** | 3軸（速度・コスト・品質） | 明確な技術的参入障壁 |
| **LTV/CAC** | 5.0以上 | 7.0以上 |
| **CAC回収期間** | 12ヶ月以内 | 6ヶ月以内 |
| **Gross Margin** | 70%以上 | 80%以上 |
| **Net Revenue Retention** | 100%以上 | 120%以上 |

### ピッチデッキ必須スライド（10-15枚）

1. **Cover Slide**: 会社名、タグライン
2. **Problem**: 課題の深刻さ（定量データ）
3. **Solution**: 10倍優位性のあるソリューション
4. **Market**: TAM $1B以上の証明
5. **Product**: デモ・スクリーンショット
6. **Traction**: 成長曲線（月次20%以上）
7. **Business Model**: ユニットエコノミクス
8. **Competition**: 競合との差別化
9. **Team**: 共同創業者の経歴
10. **Financials**: 5年計画、調達額の使途
11. **Ask**: 調達額・バリュエーション・条件

## Research Database

ForStartup Editionは、Founder_Researchプロジェクトの**55件のVC調達成功事例**を活用します。

### カテゴリ別事例数

- **Fintech** (15件): Stripe, Plaid, Robinhood, Brex, Chime等
- **SaaS** (20件): Notion, Figma, Airtable, Webflow, Retool等
- **Developer Tools** (10件): Vercel, HashiCorp, GitLab, Postman等
- **Marketplace** (10件): Uber, Airbnb, Instacart, DoorDash等

### 参照方法

各スキル実行時、以下のパスで事例を参照します:

```
@Founder_Research/documents/03_VC_Backed/FOUNDER_{番号}_{企業名}_{founder名}.md
```

**例**:
- Stripe: `@Founder_Research/documents/03_VC_Backed/FOUNDER_181_stripe_patrick_john_collison.md`
- Notion: `@Founder_Research/documents/03_VC_Backed/FOUNDER_188_notion_ivan_zhao.md`
- Figma: `@Founder_Research/documents/03_VC_Backed/FOUNDER_190_figma_dylan_field.md`

## ユニットエコノミクス基準

### 主要指標

| 指標 | 最低基準 | 理想基準 | 計算式 |
|------|---------|---------|-------|
| **LTV/CAC** | 5.0以上 | 7.0以上 | LTV ÷ CAC |
| **CAC回収期間** | 12ヶ月以内 | 6ヶ月以内 | CAC ÷ (ARPU × Gross Margin) |
| **Gross Margin** | 70%以上 | 80%以上 | (Revenue - COGS) / Revenue |
| **Net Revenue Retention** | 100%以上 | 120%以上 | (MRR期末 - Churn + Expansion) / MRR期初 |
| **Magic Number** | 0.75以上 | 1.0以上 | Net New ARR / Sales & Marketing費用 |

### ベンチマーク（成功事例）

| 企業 | LTV/CAC | CAC回収期間 | 特徴 |
|------|---------|------------|------|
| **Shopify** | 7.5 | 5ヶ月 | 低CAC、高リテンション |
| **Atlassian** | 9.0 | 3ヶ月 | プロダクト主導成長 |
| **Zoom** | 6.8 | 4ヶ月 | バイラル成長 |
| **Slack** | 8.2 | 6ヶ月 | ネットワーク効果 |

## VC Meeting準備

### VC Meeting前の準備（7-14日前）

#### Phase 1: VC調査（7日前）

1. **投資家プロフィール**:
   - 過去の投資先（類似企業）
   - 投資フェーズ（Seed、Series A等）
   - 投資額レンジ
   - ポートフォリオ企業

2. **パートナー調査**:
   - LinkedIn、Twitter、ブログ
   - 最近の発言・関心領域

#### Phase 2: 想定Q&A準備（Meeting 3日前）

**典型的なVC質問（30個）**:

- **市場・競合**: 「なぜ今、この市場なのか？」「GoogleやAmazonがこれをやったらどうなる？」
- **プロダクト・技術**: 「10倍優位性の証明は？」「技術的参入障壁は何か？」
- **ビジネスモデル**: 「LTV/CACの計算根拠は？」「CAC回収期間が12ヶ月の理由は？」
- **トラクション**: 「月次成長率20%をどう達成した？」「どのチャネルが最も効果的か？」
- **チーム**: 「なぜあなたがこの課題を解決できるのか？」

#### Phase 3: デモ準備（Meeting 2日前）

1. **デモシナリオ作成**: 3-5分のデモストーリー
2. **デモ環境チェック**: 動作確認（3回以上）
3. **バックアップ準備**: スクリーンショット・動画

#### Phase 4: フォローアップ（Meeting後24時間以内）

1. **お礼メール**: 面談への感謝、質問への追加回答
2. **追加資料送付**: デモ動画、詳細財務モデル、ユーザー事例

## Quality Score目標

| 評価軸 | 目標 | 達成基準 |
|--------|------|---------|
| **完全性** | 20/20 | 全26スキル完成 |
| **一貫性** | 18/20 | VC基準統一（CPF 70%、10倍3軸） |
| **Research統合** | 19/20 | 各スキル3件以上の事例参照 |
| **実用性** | 18/20 | 主要スキルのE2Eテスト |
| **ドキュメント** | 20/20 | README完全性 |
| **合計スコア** | **95/100以上** | |

## 開発ロードマップ

### Stage 1: 基盤構築（完了）

- [x] プロジェクト構造作成
- [x] 共通ナレッジベース作成
- [x] README作成

### Stage 2: Tier 1スキル実装（次）

- [ ] Tier 1スキル実装（優先12スキル）
- [ ] Tier 1コマンドファイル作成

### Stage 3: Tier 2スキル実装

- [ ] Tier 2スキル実装（残り14スキル）
- [ ] Tier 2コマンドファイル作成

### Stage 4: Quality Checkpoint

- [ ] Quality Score評価
- [ ] E2Eテスト実施
- [ ] 完了レポート作成

## 参考資料

### ナレッジベース

- **knowledge_base.md**: ForStartup Edition共通知識
- **case_reference_for_startup.md**: VC調達成功事例55件

### テンプレート

- **ピッチデッキテンプレート**: `@knowledge_base/templates/pitch_deck_template.pptx`
- **ユニットエコノミクス計算ツール**: `@knowledge_base/templates/unit_economics_calculator.xlsx`
- **VC Q&Aチェックリスト**: `@knowledge_base/templates/vc_qa_checklist.md`

### フレームワーク

- **CPF Framework**: `@knowledge_base/frameworks/cpf_framework.md`
- **10倍優位性検証**: `@knowledge_base/frameworks/10x_validation.md`
- **ユニットエコノミクス**: `@knowledge_base/frameworks/unit_economics.md`

## ライセンス

このプロジェクトは、内部使用専用です。

## 貢献

ForStartup Editionの改善提案は、以下の手順で行ってください:

1. Issueを作成
2. 改善内容を記述
3. レビュー待ち

## 連絡先

プロジェクトに関する質問は、プロジェクトマネージャーまでお願いします。

---

**Last Updated**: 2026-01-03
**Version**: 1.0.0
**Status**: Stage 1 Complete
