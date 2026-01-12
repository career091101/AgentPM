# Founder Agent - ForSolo（ソロプレナー特化版）

**バージョン**: 1.2
**最終更新**: 2026-01-03
**ベース**: Founder Agent Origin + ソロプレナー最適化
**ステータス**: ✅ 本番運用可能（Phase 6テスト完了）

---

## 概要

Founder Agent ForSoloは、1人で事業を運営するソロプレナー向けの特化版です。コスト最小化、利益率重視、個人実行可能性を最優先し、$100K+ ARRを目指すインディーハッカーに最適化されています。

---

## 対象ユーザー

- ソロプレナー（1人起業家）
- インディーハッカー
- サイドプロジェクト起業家
- フリーランスからの事業化

---

## Originとの主な違い

### 1. 個人実行可能性重視の基準

| 基準 | Origin | ForSolo | 理由 |
|------|--------|---------|------|
| **MVP選定** | 10類型から選択 | **LP/Boilerplate/No-Code優先** | 技術コスト最小化 |
| **CAC目標** | 制限なし | **$0-10** | 広告費ゼロ前提（SEO、Build in Public） |
| **LTV/CAC比率** | 3.0以上 | **10.0以上** | 利益率最大化 |
| **チーム規模** | 不問 | **1人固定** | 採用・マネジメントコストゼロ |

### 2. 追加フレームワーク

- **ソロプレナーFIT** - 1人で実行可能か、スキル充足度、時間確保可能性
- **Build in Public戦略** - X/Twitter活用、フォロワー獲得、透明性重視
- **BoilerplateビジネスモデL** - テンプレート販売、リカーリング収益
- **Micro-SaaSパターン** - ニッチ市場、月額$10-50、MRR積み上げ

### 3. コスト最小化戦略

- **初期投資**: $0-1,000（ドメイン、ホスティングのみ）
- **月次コスト**: $50以下（Vercel, Supabase無料枠活用）
- **マーケティング**: $0（SEO、Twitter、Product Hunt）
- **開発**: 自分で実装（Boilerplate活用で時間短縮）

---

## 特化機能

### 1. ソロプレナー成功パターン分析

**参照事例**（85件のケーススタディ + 105件のTier 2専門分析）:
- **Marc Lou**: ShipFast（Boilerplate）で$500K+ ARR
- **Tony Dinh**: BlackMagic.so（Twitter分析）で$500K+ ARR
- **Pieter Levels**: Nomad List（SEO）で$3.5M ARR

**Tier 2ケーススタディ**（2026-01-02完成）:
- **総数**: 105件（6スキル別に特化分析）
- **構成**:
  - validate-cpf: 20件
  - create-bip-strategy: 21件
  - discover-demand: 20件
  - validate-pmf: 20件
  - design-micro-saas-model: 13件
  - validate-solo-fit: 11件
- **品質**: 平均70点以上、定量データ完全性100%、プライマリソース引用100%

**共通パターン**:
- Build in Public（X/Twitterで透明性）
- SEO重視（ブログ記事50+本）
- Boilerplate/Template販売
- 複数プロダクト運営（ポートフォリオ戦略）
- AI活用による開発コスト削減（ChatGPT/Claude等）
- 地理的裁定取引（ベトナム、ジョージア等の低コスト国居住）

### 2. 1人実行可能性チェックリスト

**必須スキル**:
- [ ] コーディング（フルスタック or No-Code）
- [ ] デザイン（Figma or Tailwind CSS）
- [ ] マーケティング（SEO or SNS）
- [ ] カスタマーサポート（最低限）

**時間確保**:
- [ ] 週20時間以上確保可能
- [ ] サイドプロジェクトとして6ヶ月継続可能
- [ ] フルタイム転換のマイルストーン明確

### 3. 収益化戦略（Micro-SaaS）

| フェーズ | MRR目標 | 施策 | 期間 |
|---------|---------|------|------|
| **Phase 0** | $0 | MVP構築、LP公開 | 1-2ヶ月 |
| **Phase 1** | $1K | Product Hunt、初期ユーザー | 3-6ヶ月 |
| **Phase 2** | $5K | SEO、コンテンツマーケ | 6-12ヶ月 |
| **Phase 3** | $10K+ | フルタイム転換 | 12ヶ月以降 |

---

## ディレクトリ構造

```
Founder_Agent_ForSolo/
├── documents/
│   ├── 1_initiating/
│   ├── 2_discovery/
│   ├── 3_planning/
│   ├── 4_executing/
│   ├── 5_monitoring/
│   └── solopreneur/         # ソロプレナー関連（追加）
│       ├── skill_gap_analysis.md
│       ├── time_allocation.md
│       ├── build_in_public_plan.md
│       └── revenue_model.md
├── knowledge_base/          # Tier 2ケーススタディ（2026-01-02追加）
│   ├── tier2_case_studies/
│   │   ├── validate-cpf/         # 20件
│   │   ├── create-bip-strategy/  # 21件
│   │   ├── discover-demand/      # 20件
│   │   ├── validate-pmf/         # 20件
│   │   ├── design-micro-saas-model/ # 13件
│   │   └── validate-solo-fit/    # 11件
│   └── tier2_mapping_matrix.csv  # ケースマッピング
├── Solopreneur_Research/    # 元データ85件
│   └── documents/01_App/case_studies/
├── mvp/
├── system_prompts/
├── domain_config.yaml
└── README.md (このファイル)
```

---

## 使用方法

### ForSolo特化スキル（28スキル + 1オーケストレーター）

#### Phase 1: 需要発見・問題検証
```bash
# 需要発見
/for-solo-discover-demand

# 問題調査
/for-solo-research-problem

# 競合調査
/for-solo-research-competitors

# CPF検証
/for-solo-validate-cpf

# 10倍優位性検証
/for-solo-validate-10x
```

#### Phase 2: ソリューション検証
```bash
# ペルソナ作成
/for-solo-create-persona

# インタビューシミュレーション
/for-solo-simulate-interview

# PSF検証
/for-solo-validate-psf

# PMF検証（⭐ テスト済み、本番運用可能）
/for-solo-validate-pmf
```

#### Phase 3: ビジネスモデル設計
```bash
# MVV作成
/for-solo-create-mvv

# Micro-SaaS収益モデル設計（⭐ テスト済み、本番運用可能）
/for-solo-design-micro-saas-model

# ソロプレナーFIT検証（⭐ テスト済み、本番運用可能）
/for-solo-validate-solo-fit

# Build in Public戦略作成
/for-solo-create-bip-strategy

# ツールスタック最適化
/for-solo-optimize-tool-stack
```

#### Phase 4: 成長戦略
```bash
# フライホイール構築
/for-solo-build-flywheel

# コンテンツフライホイール作成
/for-solo-create-content-flywheel

# AARRR測定
/for-solo-measure-aarrr

# バーンレートモニタリング
/for-solo-monitor-burn-rate
```

#### Phase 5: 戦略深化（Phase 2）
```bash
# カニバリゼーション検証
/for-solo-validate-cannibalization

# 競争優位性（Moat）構築
/for-solo-build-competitive-moat

# Exit戦略設計
/for-solo-design-exit-strategy

# シナジーマップ作成
/for-solo-build-synergy-map

# 市場タイミング検証
/for-solo-validate-market-timing
```

**テスト状況**（2026-01-02完了）:

**Phase 6A（初期2スキル）**:
- ✅ `design-micro-saas-model`: 品質5.0/5.0、Tier 2参照69%、本番運用可能
- ✅ `validate-solo-fit`: 品質5.0/5.0、Tier 2参照100%、本番運用可能

**Phase 6B（追加4スキル）**:
- ✅ `discover-demand`: 高品質、Tier 2参照95%、本番運用可能
- ✅ `validate-cpf`: 品質93/100、Tier 2参照100%、本番運用可能
- ✅ `validate-pmf`: 品質78/80、Tier 2参照100%、本番運用可能
- ✅ `create-bip-strategy`: 品質8.5/10、Tier 2参照100%、本番運用可能

**総合**: ✅ **6/6スキル合格（100%）、平均成熟度90.8%**
- ⏳ 残り17スキル: Phase 6C（オプション）でテスト予定

---

## 評価基準（利益率・実行可能性重視）

| 評価項目 | Origin基準 | ForSolo基準 | 理由 |
|---------|-----------|------------|------|
| ビジネスモデル | 4点以上 | **6点以上** | 利益率・LTV/CAC比率重視 |
| 実行可能性 | 4点以上 | **6点以上** | 1人実行可能性が最重要 |
| 市場機会 | 6点以上 | **4点以上** | ニッチ市場OK |

**追加評価項目**:
- **スキル充足度**: 70%以上（不足スキルは外注可）
- **時間確保**: 週20時間以上確保可能
- **初期投資**: $1,000以下
- **月次コスト**: $50以下

---

## 参考リソース（Originに追加）

### ソロプレナー研究

- **Solopreneur_Research/documents/01_App/case_studies/** - 85件のケーススタディ
- **Build in Public事例** - Marc Lou, Tony Dinh, Pieter Levels等
- **Boilerplate分析** - ShipFast, LaunchFast等のビジネスモデル
- **Indie Hacker Community** - フォーラム、ポッドキャスト

---

## 成功指標

| 指標 | 目標 | 備考 |
|------|------|------|
| **MRR** | $1K（3ヶ月）、$5K（12ヶ月）、$10K（24ヶ月） | 段階的成長 |
| **LTV/CAC** | 10.0以上 | 広告費ゼロ前提 |
| **利益率** | 80%以上 | コスト最小化 |
| **Xフォロワー** | 1K（6ヶ月）、10K（24ヶ月） | Build in Public |

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-03 | 1.2 | **Phase 2（戦略深化）追加**: 5スキル追加（validate-cannibalization、build-competitive-moat、design-exit-strategy、build-synergy-map、validate-market-timing）、orchestrate-phase1-soloオーケストレーター追加、合計28スキル+1オーケストレーター、Solo特化カスタマイズ完了 |
| 2026-01-02 | 1.1 | **Phase 5-6完全完了**: Tier 2ケーススタディ105件完成、スキルテスト6個実施（Phase 6A: design-micro-saas-model、validate-solo-fit / Phase 6B: discover-demand、validate-cpf、validate-pmf、create-bip-strategy）、合格率100%（6/6）、平均成熟度90.8%、本番運用可能レベル達成 |
| 2025-12-30 | 1.0 | 初版作成（ForSolo特化版） |
