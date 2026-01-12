---
name: create-fundraising-plan
description: |
  スタートアップの資金調達ロードマップ（Pre-Seed → Seed → Series A → Series B）を
  自動生成する自律実行型スキル（ForStartup版）。

  **VC投資基準に準拠**：
  - 各ラウンドで達成すべきマイルストーン（CPF/PSF/PMF/成長率等）
  - 調達額・評価額の目安（日本市場・グローバル市場）
  - 資金使途の最適配分（人材、マーケティング、開発等）
  - 次のラウンドまでの期間（月数）とランウェイ設計

  **Researchナレッジ統合**：
  - Airbnb: 2009年1月〜2020年12月（11年、$6.4B調達）
  - Freshworks: 2010年10月〜2021年9月（11年、IPO $12-13B評価）
  - Box: 2005年〜2015年1月（10年、IPO $3.5B評価）

  使用タイミング：
  - CPF/PSF達成後、資金調達の戦略を立案したい
  - VCミーティング前の準備として
  - 長期的な成長計画を策定したい
  - 既存投資家への報告資料として

  所要時間：15-30分（自動実行）
  出力：fundraising_roadmap.md
trigger_keywords:
  - "資金調達計画"
  - "資金調達ロードマップ"
  - "シリーズA準備"
  - "VC調達戦略"
  - "ファンドレイジング"
  - "fundraising plan"
stage: planning
dependencies:
  - validate-cpf（CPF達成が望ましい）
  - validate-psf（PSF達成が望ましい）
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/fundraising_roadmap.md
execution_time: 15-30分
framework_reference: Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
priority: P1
framework_compliance: 100%
domain: ForStartup
---

# Create Fundraising Plan Skill (ForStartup Edition)

スタートアップの**Pre-Seed → Seed → Series A → Series B**の資金調達ロードマップを自動生成する自律実行型Skill。

**ForStartup版の特徴**：
- VC投資基準に準拠した現実的な調達額・評価額の目安
- Airbnb/Freshworks/Boxの成功事例から抽出したマイルストーン設計
- 日本市場とグローバル市場の両方に対応
- ガントチャート風の視覚的タイムライン生成

---

## このSkillでできること

1. **4ラウンド資金調達計画**: Pre-Seed/Seed/Series A/Series Bの段階的計画
2. **マイルストーン定義**: 各ラウンドで達成すべきCPF/PSF/PMF/成長率等
3. **調達額・評価額の算出**: 業界標準と成功事例に基づく現実的な数値
4. **資金使途の最適配分**: 人材・マーケティング・開発への投資比率
5. **タイムライン表生成**: Markdownテーブルとガントチャート風の視覚化
6. **ラウンド別詳細計画書**: 各ラウンドの詳細な実行計画

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 現在のステージ、ビジネスモデル、目標市場、既存の検証結果 |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/fundraising_roadmap.md` |
| **次のSkill** | `/build-pitch-deck`（各ラウンド準備時） |
| **ステージ** | Phase2-3（PMF検証〜Series A準備） |

---

## KB参照

このスキルは以下のナレッジベースを参照します：

### コア参照
- @.claude/skills/for_startup/_analysis/research_knowledge.md（資金調達パターン）
- /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#fundraising-overview

### 評価基準・フレームワーク
- NRR（Net Revenue Retention）≥120%、年次成長率 ≥300%（SaaS基準）

### Tier 2 ケーススタディ (12件統合 - 2026-01-02)
スキルに統合された12件のケーススタディ（合計13.2KB）:

**段階的マイルストーン型**:
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/FOUNDER_006_brian_chesky.md → `research/case_studies/tier2/create-fundraising-plan/01_airbnb_fundraising_roadmap.md`
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/02_Unicorn/FOUNDER_060_girish_mathrubootham.md → `02_freshworks_fundraising_roadmap.md`
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/FOUNDER_003_reid_hoffman.md → `06_linkedin_fundraising_roadmap.md`
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/02_Unicorn/FOUNDER_061_aaron_levie.md → `07_box_fundraising_roadmap.md`

**バイラル・高速成長型**:
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/FOUNDER_010_kevin_systrom.md → `08_instagram_fundraising_roadmap.md`
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/FOUNDER_011_jack_dorsey.md → `09_twitter_fundraising_roadmap.md`
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/02_Unicorn/FOUNDER_051_melanie_perkins.md → `11_canva_fundraising_roadmap.md`

**ピボット・戦略転換型**:
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/FOUNDER_008_stewart_butterfield.md → `04_slack_fundraising_roadmap.md`

**インフラ・B2B特化型**:
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/FOUNDER_007_patrick_collison.md → `03_stripe_fundraising_roadmap.md`
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/02_Unicorn/FOUNDER_052_ivan_zhao.md → `12_notion_fundraising_roadmap.md`

**デモ・MVP最小化型**:
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/FOUNDER_009_drew_houston.md → `05_dropbox_fundraising_roadmap.md`

**マーケットプレイス型**:
- /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/FOUNDER_012_travis_kalanick.md → `10_uber_fundraising_roadmap.md`

**統合レポート**: `research/case_studies/tier2/create-fundraising-plan/_integration_report.md`

---

## 資金調達ラウンド定義（ForStartup版）

### ラウンド概要

| ラウンド | 調達額（日本） | 調達額（グローバル） | 評価額（日本） | 評価額（グローバル） | 期間 |
|---------|-------------|-------------------|--------------|-------------------|------|
| **Pre-Seed** | ¥5M-30M | $50K-500K | ¥20M-100M | $500K-5M | 6-12ヶ月 |
| **Seed** | ¥30M-150M | $500K-3M | ¥100M-500M | $5M-30M | 12-18ヶ月 |
| **Series A** | ¥200M-1B | $3M-20M | ¥500M-5B | $30M-150M | 18-24ヶ月 |
| **Series B** | ¥500M-3B | $15M-60M | ¥3B-20B | $100M-500M | 24-36ヶ月 |

---

## 各ラウンドの達成マイルストーン

### Pre-Seed（課題検証フェーズ）

| 項目 | 目標値 | 測定方法 |
|------|--------|----------|
| **CPFスコア** | 60%以上 | `/validate-cpf` で測定 |
| **インタビュー数** | 20人以上 | 課題仮説の検証 |
| **MVP** | プロトタイプ完成 | ユーザーテスト可能な状態 |
| **チーム** | 創業者1-2名 | フルタイムコミット |
| **初期ユーザー** | 10-50人 | 無料/招待制で獲得 |

**資金使途（推奨配分）**:
- 人材: 40%（共同創業者の生活費、初期エンジニア）
- 開発: 40%（MVP開発、クラウドインフラ）
- マーケティング: 10%（初期ユーザー獲得）
- その他: 10%（法務、会計、オフィス）

**成功事例参照**:
- **Airbnb Pre-Seed**: $20K（Y Combinator 2009年1月）、シリアル販売で$30K自己資金
- **Box Pre-Seed**: $15K（Dylan Smith共同創業者のポーカー勝ち金）
- **Freshworks Pre-Seed**: 自己資金、Microsoft India Bizspark Challenge $40K

---

### Seed（ソリューション検証フェーズ）

| 項目 | 目標値 | 測定方法 |
|------|--------|----------|
| **PSFスコア** | 70%以上 | `/validate-psf` で測定 |
| **CPFスコア** | 70%以上（ForStartup基準） | `/validate-cpf` で測定 |
| **10倍優位性** | 3軸以上 | `/validate-10x` で測定 |
| **初期ユーザー** | 100-500人 | アクティブユーザー数 |
| **有料ユーザー** | 10-50人 | WTP（支払い意思）の実証 |
| **月次成長率** | 10-15% | ユーザー数またはMRR |
| **チーム** | 3-5名 | 開発・営業の初期チーム |

**資金使途（推奨配分）**:
- 人材: 50%（エンジニア2-3名、初期営業）
- 開発: 25%（プロダクト改善、インフラ拡張）
- マーケティング: 15%（初期トラクション検証、AdWords等）
- その他: 10%（法務、会計、オフィス拡張）

**成功事例参照**:
- **Airbnb Seed**: $600K（Sequoia Capital 2009年4月）、ニューヨーク市場での写真改善
- **Box Seed**: $350K（Mark Cuban、コールドメール成功）
- **Freshworks Seed**: AdWords投資$40K → 初期トラクション検証

---

### Series A（PMF検証フェーズ）

| 項目 | 目標値 | 測定方法 |
|------|--------|----------|
| **PMF達成** | 4指標中4指標✅ | `/validate-pmf` で測定 |
| **Sean Ellisテスト** | 50%以上 | 「非常に残念」回答率 |
| **月次成長率** | 20%以上/月 | MRR/MAU/GMV |
| **Churn Rate** | 3%以下/月 | 月次解約率 |
| **NPS** | 60以上 | Net Promoter Score |
| **LTV/CAC** | 5.0以上 | ユニットエコノミクス |
| **ARR** | ¥50M-500M | 年間経常収益 |
| **チーム** | 10-20名 | 部門長クラス採用 |

**資金使途（推奨配分）**:
- 人材: 60%（エンジニア10名+、営業チーム、カスタマーサクセス）
- マーケティング: 20%（スケール投資、ブランド構築）
- 開発: 15%（プロダクト拡張、新機能開発）
- その他: 5%（オフィス、法務、管理）

**成功事例参照**:
- **Airbnb Series A**: $7.2M（Sequoia Capital 2010年11月）、評価額$70M、写真改善で予約2-3倍
- **Box Series A**: $1.5M（DFJ 2006年）、エンタープライズピボット開始
- **Freshworks Series A-B**: 計数千万ドル調達（推定$10-20M）

---

### Series B（スケールフェーズ）

| 項目 | 目標値 | 測定方法 |
|------|--------|----------|
| **月次成長率** | 15-20%/月 | MRR/MAU/GMV（維持） |
| **ARR** | ¥500M-3B | 年間経常収益 |
| **LTV/CAC** | 5.0以上（維持） | ユニットエコノミクス |
| **NRR** | 120%以上 | Net Revenue Retention |
| **市場シェア** | 5-10% | ターゲットセグメントでのシェア |
| **グローバル展開** | 2-3カ国 | 海外拠点設立 |
| **チーム** | 50-100名 | 経営チーム完成 |

**資金使途（推奨配分）**:
- 人材: 50%（グローバルチーム、経営幹部採用）
- マーケティング: 25%（市場シェア拡大、ブランド確立）
- 開発: 15%（プラットフォーム拡張、M&A準備）
- 海外展開: 10%（海外拠点設立、ローカライズ）

**成功事例参照**:
- **Airbnb Series B**: $112M（Andreessen Horowitz 2011年7月）、評価額$1.3B、グローバル展開
- **Box Series B-D**: 計$100M+調達（2007-2012年）、継続的成長投資
- **Freshworks Series C-E**: $500M以上調達、グローバル展開（Chennai、San Bruno、London、Sydney、Berlin）

---

## Domain-Specific Knowledge (from Research)

### Success Patterns（資金調達成功パターン）

**事例1: Airbnb（$6.4B調達、$100B+ IPO）**

| ラウンド | 時期 | 金額 | 評価額 | キーポイント |
|---------|------|------|--------|-------------|
| YC Seed | 2009年1月 | $20K | 不明 | Paul Grahamメンター支援 |
| Seed | 2009年4月 | $600K | 不明 | YC卒業後即座に獲得 |
| Series A | 2010年11月 | $7.2M | $70M | 写真改善による実績 |
| Series B | 2011年7月 | $112M | $1.3B | グローバル展開資金 |
| Series C | 2012年7月 | $200M | $2.5B | 欧州・アジア進出 |
| Series D | 2014年4月 | $450M | $10B | ユニコーン突入 |
| Series E | 2015年6月 | $1.5B | $25.5B | IPO準備段階 |
| IPO | 2020年12月 | $3.5B | $100B+ | NASDAQ上場 |

**成功要因**:
1. **「Do things that don't scale」の実践**: 創業者自らニューヨークで写真撮影
2. **定量的成果の実証**: 写真品質改善 → 予約2-3倍増
3. **段階的スケール**: 各ラウンドで明確なマイルストーン達成

**事例2: Freshworks（IPO $12-13B評価）**

| ラウンド | 時期 | 金額 | キーポイント |
|---------|------|------|-------------|
| Pre-Seed | 2010年 | 自己資金 | Microsoft India Bizspark $40K |
| Seed | 2011年 | 不明 | AdWords全額投資で検証 |
| Series A-B | 2013-2015年 | $10-20M推定 | 10,000社顧客達成 |
| Series C-E | 2015-2019年 | $500M+ | グローバル展開 |
| IPO | 2021年9月 | - | NASDAQ上場 |

**成功要因**:
1. **市場タイミング**: Zendesk価格改定直後のローンチ
2. **高い資本効率**: AdWords $40K投資 → 高効率トラクション
3. **SMB特化**: エンタープライズではなく中小企業に集中

**事例3: Box（IPO $3.5B評価）**

| ラウンド | 時期 | 金額 | キーポイント |
|---------|------|------|-------------|
| Pre-Seed | 2005年 | $15K | Dylan Smithポーカー勝ち金 |
| Seed | 2005年 | $350K | Mark Cubanコールドメール |
| Series A | 2006年 | $1.5M | DFJ投資 |
| Series B-D | 2007-2012年 | $100M+ | エンタープライズピボット |
| IPO | 2015年1月 | - | NYSE上場 |

**成功要因**:
1. **ピボットの決断**: コンシューマー→エンタープライズへの戦略転換
2. **ボトムアップ採用**: IT部門を通さずに個人利用開始
3. **フリーミアムモデル**: CAC $0で個人ユーザー獲得

### Common Pitfalls（資金調達の失敗パターン）

1. **早期スケールの危険性**: PMF達成前のマーケティング投資は資金の無駄遣い
2. **評価額の過大設定**: 次のラウンドでダウンラウンドのリスク
3. **資金使途の不明確**: 投資家からの信頼低下
4. **ランウェイ不足**: 次のラウンドまでに資金が枯渇
5. **マイルストーン未達成**: 約束した成果を出せない

### Quantitative Benchmarks（定量基準）

| ラウンド | 月次成長率 | LTV/CAC | ARR | 出典 |
|---------|----------|---------|-----|------|
| Pre-Seed | 検証段階 | 未測定 | - | - |
| Seed | 10-15%/月 | 3.0以上 | - | @research_knowledge.md |
| Series A | 20%以上/月 | 5.0以上 | ¥50M-500M | Airbnb/Freshworks事例 |
| Series B | 15-20%/月 | 5.0以上維持 | ¥500M-3B | Airbnb/Box事例 |

### Best Practices

1. **段階的マイルストーン**: 各ラウンドで明確な達成目標を設定
2. **投資家との関係構築**: 調達前から関係を構築（6-12ヶ月前）
3. **データドリブン**: 定量的成果を常に測定・報告
4. **ランウェイ18ヶ月**: 常に18ヶ月以上のランウェイを確保
5. **希薄化管理**: 各ラウンドでの希薄化を20-25%以内に抑制

### Quantitative Benchmarks (Updated 2026-01-02)

| ラウンド | 月次成長率 | LTV/CAC | ARR | Burn Rate | ランウェイ | 出典 |
|---------|----------|---------|-----|-----------|----------|------|
| Pre-Seed | 検証段階 | 未測定 | - | ~$2-5K/月 | 10-12ヶ月 | Airbnb |
| Seed | 10-15%/月 | 3.0以上 | - | ~$30-50K/月 | 18ヶ月 | Airbnb, Freshworks |
| Series A | 20%以上/月 | 5.0以上 | ¥50M-500M | ~$400K/月 | 18ヶ月 | Airbnb, Dropbox |
| Series B | 15-20%/月 | 5.0以上維持 | ¥500M-3B | ~$4-5M/月 | 22-28ヶ月 | Airbnb, Slack |

### ランウェイ24ヶ月ルールの実践

**Airbnbの実例**:
- Pre-Seed: $20K調達、Burn Rate $2K/月 → ランウェイ10ヶ月（ギリギリ）
- Seed: $600K調達、Burn Rate $33K/月 → ランウェイ18ヶ月 ✅
- Series A: $7.2M調達、Burn Rate $400K/月 → ランウェイ18ヶ月 ✅
- Series B: $112M調達、Burn Rate $4-5M/月 → ランウェイ22-28ヶ月 ✅

**重要な教訓**:
1. 常に18ヶ月以上のランウェイを確保
2. ランウェイの半分（9-12ヶ月）時点で次のラウンド準備開始
3. COVID-19等の危機時は即座のBurn Rate削減（Airbnb: 月間$250M損失→25%人員削減）

### YC $20K → Sequoia $600K パターン

Airbnbの成功パターン（YC → トップティアVC）は再現可能：

| 企業 | YC投資 | Seed投資家 | Seed調達額 | 時間差 | 成功要因 |
|------|--------|----------|----------|--------|---------|
| **Airbnb** | $20K (2009年1月) | Sequoia Capital | $600K | 3ヶ月 | シリアル販売の粘り強さ |
| **Dropbox** | $15K (2007年) | Sequoia Capital | $1.2M | 6ヶ月 | バイラル動画、K-factor実証 |
| **Stripe** | 不明 | Peter Thiel, Sequoia | $2M | 不明 | 開発者体験、7行のコード |
| **Reddit** | $12K (2005年) | Sequoia Capital | $0.1M | 即座 | YC初期バッチの信頼 |

**成功パターン**:
1. Demo Dayでの定量的成果明示
2. 創業者の粘り強さ（Airbnbのシリアル販売のような象徴的ストーリー）
3. 少額でも成長率・顧客満足度を実証
4. Paul Grahamの紹介・YCネットワーク活用

### Reference

- 詳細: @.claude/skills/for_startup/_analysis/research_knowledge.md
- **Tier 2ケーススタディ統合レポート**: @research/case_studies/tier2/create-fundraising-plan/_integration_report.md
- Airbnb事例: @Sratup_Research/documents/01_Legendary/FOUNDER_006_brian_chesky.md → `research/case_studies/tier2/create-fundraising-plan/01_airbnb_fundraising_roadmap.md`
- Freshworks事例: @Sratup_Research/documents/02_Unicorn/FOUNDER_060_girish_mathrubootham.md → `research/case_studies/tier2/create-fundraising-plan/02_freshworks_fundraising_roadmap.md`
- Box事例: @Sratup_Research/documents/02_Unicorn/FOUNDER_061_aaron_levie.md → `research/case_studies/tier2/create-fundraising-plan/07_box_fundraising_roadmap.md`

---

## Instructions

### 自動実行フロー

**STEP 1: 現在ステージの確認**
- 現在の検証状況（CPF/PSF/PMF）
- 既存の顧客数・ユーザー数
- 現在のMRR/ARR（もしあれば）
- チーム規模
- 既存の資金調達状況

**STEP 2: ビジネスモデル・市場の確認**
- ビジネスモデル（SaaS、マーケットプレイス、コンシューマー等）
- ターゲット市場（日本、グローバル、両方）
- 競合状況
- 目標評価額・調達額

**STEP 3: 4ラウンドのロードマップ設計**
- 各ラウンドの調達額・評価額の算出
- マイルストーンの定義
- 資金使途の配分決定
- 期間（次のラウンドまでの月数）の設定

**STEP 4: タイムライン表の生成**
- Markdownテーブル形式
- ガントチャート風の視覚化
- マイルストーン達成時期の明記

**STEP 5: ラウンド別詳細計画書の生成**
- Pre-Seed計画
- Seed計画
- Series A計画
- Series B計画

**STEP 6: リスク分析**
- 各ラウンドでの失敗リスク
- ランウェイ管理
- ダウンラウンド回避策

**STEP 7: 成果物出力**
- ツール: Write
- パス: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/3_planning/fundraising_roadmap.md`

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **入力情報不足**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **計算エラー**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
- **標準エラーレスポンス**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式

---

## 成果物フォーマット

```markdown
# 資金調達ロードマップ（ForStartup版）

**作成日**: [YYYY-MM-DD]
**対象プロダクト**: [プロダクト名]
**ビジネスモデル**: [SaaS / マーケットプレイス / コンシューマー等]
**ターゲット市場**: [日本 / グローバル / 両方]
**現在ステージ**: [Pre-Seed準備中 / Seed調達中 / Series A準備中等]

---

## エグゼクティブサマリー

### 資金調達概要

| ラウンド | 目標調達額 | 目標評価額 | 達成マイルストーン | 期間 |
|---------|----------|----------|-----------------|------|
| **Pre-Seed** | ¥XX M | ¥XX M | CPF達成、MVP完成 | XX ヶ月 |
| **Seed** | ¥XX M | ¥XX M | PSF達成、初期ユーザー獲得 | XX ヶ月 |
| **Series A** | ¥XX M | ¥XX B | PMF達成、ARR ¥XX M | XX ヶ月 |
| **Series B** | ¥XX B | ¥XX B | スケール、グローバル展開 | XX ヶ月 |

**総調達目標**: ¥XX B（4ラウンド合計）

---

## タイムライン（ガントチャート風）

```
2026   2027   2028   2029   2030
Q1 Q2 Q3 Q4 | Q1 Q2 Q3 Q4 | Q1 Q2 Q3 Q4 | Q1 Q2 Q3 Q4 | Q1 Q2 Q3 Q4
▓▓▓▓▓▓░░░░░░|░░░░░░░░░░░░|░░░░░░░░░░░░|░░░░░░░░░░░░|░░░░░░░░░░░░  Pre-Seed
    ▓▓▓▓▓▓▓▓|▓▓▓▓▓▓░░░░░░|░░░░░░░░░░░░|░░░░░░░░░░░░|░░░░░░░░░░░░  Seed
            |    ▓▓▓▓▓▓▓▓|▓▓▓▓▓▓▓▓░░░░|░░░░░░░░░░░░|░░░░░░░░░░░░  Series A
            |            |        ▓▓▓▓|▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓░░░░░░░░  Series B

▓ = 調達実行期間   ░ = 次のラウンド準備期間
```

**マイルストーン達成時期**:
- [ ] YYYY-MM: CPF達成（Pre-Seed条件）
- [ ] YYYY-MM: PSF達成（Seed条件）
- [ ] YYYY-MM: PMF達成（Series A条件）
- [ ] YYYY-MM: スケール達成（Series B条件）

---

## ラウンド別詳細計画

### Pre-Seed ラウンド

#### 基本情報

| 項目 | 内容 |
|------|------|
| **目標調達額** | ¥XX M |
| **目標評価額（Post）** | ¥XX M |
| **希薄化率** | XX%（目標: 20%以内） |
| **期間** | XX ヶ月（YYYY-MM 〜 YYYY-MM） |
| **ランウェイ** | XX ヶ月 |

#### 達成マイルストーン

| マイルストーン | 目標値 | 測定方法 | 達成期限 |
|--------------|--------|----------|---------|
| CPFスコア | 60%以上 | `/validate-cpf` | YYYY-MM |
| インタビュー数 | 20人以上 | 課題仮説検証 | YYYY-MM |
| MVP完成 | ユーザーテスト可能 | プロトタイプ | YYYY-MM |
| 初期ユーザー | 10-50人 | 無料/招待制 | YYYY-MM |
| チーム | 1-2名 | フルタイムコミット | YYYY-MM |

#### 資金使途

| 用途 | 配分 | 金額 | 詳細 |
|------|------|------|------|
| 人材 | 40% | ¥XX M | 創業者生活費、初期エンジニア |
| 開発 | 40% | ¥XX M | MVP開発、クラウドインフラ |
| マーケティング | 10% | ¥XX M | 初期ユーザー獲得 |
| その他 | 10% | ¥XX M | 法務、会計、オフィス |

#### ベンチマーク比較

| 企業 | Pre-Seed金額 | 達成事項 | 備考 |
|------|------------|---------|------|
| Airbnb | $20K | YC採用、MVP完成 | シリアル販売$30K併用 |
| Box | $15K | MVP完成 | 共同創業者資金 |
| Freshworks | 自己資金 | MVP完成 | Microsoft $40K活用 |
| **本プロジェクト** | ¥XX M | [達成目標] | - |

---

### Seed ラウンド

#### 基本情報

| 項目 | 内容 |
|------|------|
| **目標調達額** | ¥XX M |
| **目標評価額（Post）** | ¥XX M |
| **希薄化率** | XX%（目標: 20-25%以内） |
| **期間** | XX ヶ月（YYYY-MM 〜 YYYY-MM） |
| **ランウェイ** | XX ヶ月 |

#### 達成マイルストーン

| マイルストーン | 目標値 | 測定方法 | 達成期限 |
|--------------|--------|----------|---------|
| PSFスコア | 70%以上 | `/validate-psf` | YYYY-MM |
| CPFスコア | 70%以上 | `/validate-cpf` | YYYY-MM |
| 10倍優位性 | 3軸以上 | `/validate-10x` | YYYY-MM |
| 初期ユーザー | 100-500人 | アクティブユーザー | YYYY-MM |
| 有料ユーザー | 10-50人 | WTP実証 | YYYY-MM |
| 月次成長率 | 10-15%/月 | ユーザー数/MRR | YYYY-MM |
| チーム | 3-5名 | 開発・営業チーム | YYYY-MM |

#### 資金使途

| 用途 | 配分 | 金額 | 詳細 |
|------|------|------|------|
| 人材 | 50% | ¥XX M | エンジニア2-3名、初期営業 |
| 開発 | 25% | ¥XX M | プロダクト改善、インフラ拡張 |
| マーケティング | 15% | ¥XX M | 初期トラクション検証 |
| その他 | 10% | ¥XX M | 法務、会計、オフィス拡張 |

#### ベンチマーク比較

| 企業 | Seed金額 | 達成事項 | 備考 |
|------|----------|---------|------|
| Airbnb | $600K | ニューヨーク市場成功 | 写真品質改善 |
| Box | $350K | Mark Cuban投資 | コールドメール成功 |
| Freshworks | 推定$1-2M | 10,000社顧客 | AdWords全額投資 |
| **本プロジェクト** | ¥XX M | [達成目標] | - |

---

### Series A ラウンド

#### 基本情報

| 項目 | 内容 |
|------|------|
| **目標調達額** | ¥XX M |
| **目標評価額（Post）** | ¥XX B |
| **希薄化率** | XX%（目標: 20-25%以内） |
| **期間** | XX ヶ月（YYYY-MM 〜 YYYY-MM） |
| **ランウェイ** | XX ヶ月 |

#### 達成マイルストーン

| マイルストーン | 目標値 | 測定方法 | 達成期限 |
|--------------|--------|----------|---------|
| PMF達成 | 4指標中4指標✅ | `/validate-pmf` | YYYY-MM |
| Sean Ellisテスト | 50%以上 | アンケート | YYYY-MM |
| 月次成長率 | 20%以上/月 | MRR/MAU | YYYY-MM |
| Churn Rate | 3%以下/月 | 解約率 | YYYY-MM |
| NPS | 60以上 | アンケート | YYYY-MM |
| LTV/CAC | 5.0以上 | ユニットエコノミクス | YYYY-MM |
| ARR | ¥50M-500M | 年間経常収益 | YYYY-MM |
| チーム | 10-20名 | 部門長クラス採用 | YYYY-MM |

#### 資金使途

| 用途 | 配分 | 金額 | 詳細 |
|------|------|------|------|
| 人材 | 60% | ¥XX M | エンジニア10名+、営業、CS |
| マーケティング | 20% | ¥XX M | スケール投資、ブランド構築 |
| 開発 | 15% | ¥XX M | プロダクト拡張、新機能 |
| その他 | 5% | ¥XX M | オフィス、法務、管理 |

#### ベンチマーク比較

| 企業 | Series A金額 | 評価額 | 達成事項 |
|------|------------|--------|---------|
| Airbnb | $7.2M | $70M | 予約2-3倍増 |
| Box | $1.5M | 不明 | エンタープライズピボット |
| Freshworks | $10-20M推定 | 不明 | 継続成長 |
| **本プロジェクト** | ¥XX M | ¥XX B | [達成目標] |

---

### Series B ラウンド

#### 基本情報

| 項目 | 内容 |
|------|------|
| **目標調達額** | ¥XX B |
| **目標評価額（Post）** | ¥XX B |
| **希薄化率** | XX%（目標: 15-20%以内） |
| **期間** | XX ヶ月（YYYY-MM 〜 YYYY-MM） |
| **ランウェイ** | XX ヶ月 |

#### 達成マイルストーン

| マイルストーン | 目標値 | 測定方法 | 達成期限 |
|--------------|--------|----------|---------|
| 月次成長率 | 15-20%/月 | MRR/MAU/GMV | YYYY-MM |
| ARR | ¥500M-3B | 年間経常収益 | YYYY-MM |
| LTV/CAC | 5.0以上維持 | ユニットエコノミクス | YYYY-MM |
| NRR | 120%以上 | Net Revenue Retention | YYYY-MM |
| 市場シェア | 5-10% | ターゲットセグメント | YYYY-MM |
| グローバル展開 | 2-3カ国 | 海外拠点設立 | YYYY-MM |
| チーム | 50-100名 | 経営チーム完成 | YYYY-MM |

#### 資金使途

| 用途 | 配分 | 金額 | 詳細 |
|------|------|------|------|
| 人材 | 50% | ¥XX M | グローバルチーム、経営幹部 |
| マーケティング | 25% | ¥XX M | 市場シェア拡大、ブランド確立 |
| 開発 | 15% | ¥XX M | プラットフォーム拡張、M&A準備 |
| 海外展開 | 10% | ¥XX M | 海外拠点設立、ローカライズ |

#### ベンチマーク比較

| 企業 | Series B金額 | 評価額 | 達成事項 |
|------|------------|--------|---------|
| Airbnb | $112M | $1.3B | グローバル展開 |
| Box | $100M+ | $2.3B | 継続成長投資 |
| Freshworks | $500M+ | 不明 | グローバル5拠点 |
| **本プロジェクト** | ¥XX B | ¥XX B | [達成目標] |

---

## リスク分析

### ラウンド別リスク

| ラウンド | 主要リスク | 発生確率 | 影響度 | 対策 |
|---------|----------|---------|--------|------|
| Pre-Seed | CPF未達成 | 中 | 高 | 追加インタビュー、ピボット検討 |
| Seed | トラクション不足 | 中 | 高 | マーケティング投資強化 |
| Series A | PMF未達成 | 中 | 非常に高 | Pivot検討、ダウンラウンド準備 |
| Series B | 競合参入 | 高 | 高 | 差別化強化、M&A検討 |

### ランウェイ管理

| 状況 | 推奨アクション |
|------|---------------|
| ランウェイ 18ヶ月以上 | 通常運転、積極投資可能 |
| ランウェイ 12-18ヶ月 | 調達準備開始、コスト見直し |
| ランウェイ 6-12ヶ月 | 調達活動加速、コスト削減 |
| ランウェイ 6ヶ月未満 | 緊急調達、ブリッジファイナンス |

---

## 次のアクション

### 現在ステージ: [ステージ名]

| 優先度 | アクション | 期限 | 担当 |
|:------:|----------|------|------|
| 1 | [アクション1] | YYYY-MM-DD | [担当者] |
| 2 | [アクション2] | YYYY-MM-DD | [担当者] |
| 3 | [アクション3] | YYYY-MM-DD | [担当者] |

### 推奨コマンド

| コマンド | 用途 |
|---------|------|
| `/validate-cpf` | CPF達成確認（Pre-Seed準備） |
| `/validate-psf` | PSF達成確認（Seed準備） |
| `/validate-pmf` | PMF達成確認（Series A準備） |
| `/build-pitch-deck` | VC向けピッチデッキ作成 |
| `/validate-unit-economics` | ユニットエコノミクス検証 |

---

## 参照成果物

| ファイル | 作成日 | 内容 |
|----------|--------|------|
| cpf_judgment.md | [日付] | CPF検証結果 |
| psf_validation.md | [日付] | PSF検証結果 |
| pmf_diagnosis_forstartup.md | [日付] | PMF診断結果 |
| unit_economics.md | [日付] | ユニットエコノミクス分析 |

---

## 成功事例参照

### Airbnb 資金調達サマリー

- **総調達額**: $6.4B（11年間）
- **IPO評価額**: $100B+
- **調達回数**: 6ラウンド + IPO
- **キーポイント**: 各ラウンドで明確なマイルストーン達成

### Freshworks 資金調達サマリー

- **総調達額**: $1-2B推定（11年間）
- **IPO評価額**: $12-13B
- **キーポイント**: 資本効率の高い成長

### Box 資金調達サマリー

- **総調達額**: $100M+（10年間）
- **IPO評価額**: $3.5B
- **キーポイント**: エンタープライズピボットで成功

---

## メタデータ

| 項目 | 内容 |
|-----|------|
| 作成日 | [YYYY-MM-DD] |
| 実行Skill | `/create-fundraising-plan` (ForStartup版) |
| フレームワーク | 起業の科学 + VC投資基準 |
| 成功事例参照 | Airbnb, Freshworks, Box |
| 次の更新予定 | [次のマイルストーン達成時] |
```

---

## 使用例

```
User: /create-fundraising-plan

Skill:
# 資金調達ロードマップ 自律作成開始（ForStartup版）

現在ステージ確認中...
✅ CPF達成済み（70%）
✅ PSF検証中
⏳ PMF未達成

ビジネスモデル: SaaS
ターゲット市場: 日本 + グローバル

[自動生成中...]

STEP 1: 現在ステージ確認 ✅
STEP 2: ビジネスモデル・市場確認 ✅
STEP 3: 4ラウンドロードマップ設計 ✅
STEP 4: タイムライン表生成 ✅
STEP 5: ラウンド別詳細計画書生成 ✅
STEP 6: リスク分析 ✅
STEP 7: 成果物出力 ✅

## 完了

成果物: fundraising_roadmap.md

### 資金調達概要

| ラウンド | 目標調達額 | 目標評価額 | 達成マイルストーン | 期間 |
|---------|----------|----------|-----------------|------|
| **Pre-Seed** | ¥20M | ¥80M | CPF達成、MVP完成 | 9ヶ月 |
| **Seed** | ¥100M | ¥400M | PSF達成、初期ユーザー300人 | 15ヶ月 |
| **Series A** | ¥500M | ¥2.5B | PMF達成、ARR ¥100M | 18ヶ月 |
| **Series B** | ¥1.5B | ¥10B | スケール、グローバル2カ国 | 24ヶ月 |

**ベンチマーク比較**:
- Airbnb: 11年で$6.4B調達 → $100B IPO
- Freshworks: 11年で$1-2B調達 → $12-13B IPO
- Box: 10年で$100M+調達 → $3.5B IPO

推奨: `/build-pitch-deck` でVC向けピッチデッキを作成
```

---

## 成功基準

1. ✅ **4ラウンド計画完成**: Pre-Seed/Seed/Series A/Series Bの全ラウンド計画
2. ✅ **マイルストーン定義の明確性**: 各ラウンドで達成すべき定量目標
3. ✅ **現実的な数値設定**: 業界標準と成功事例に基づく調達額・評価額
4. ✅ **タイムライン視覚化**: ガントチャート風の視覚的表現
5. ✅ **成功事例ベンチマーク統合**: Airbnb/Freshworks/Boxとの比較
6. ✅ **リスク分析の具体性**: ラウンド別リスクと対策

---

## 注意事項

1. **現実的な評価**: 過度に楽観的な数値を避け、保守的な計画を策定
2. **マイルストーンの優先**: 調達額よりもマイルストーン達成を優先
3. **ランウェイ管理**: 常に18ヶ月以上のランウェイを確保
4. **希薄化管理**: 各ラウンドでの希薄化を20-25%以内に抑制
5. **投資家との関係構築**: 調達前から関係を構築（6-12ヶ月前）
6. **ピボットの準備**: マイルストーン未達成時のプランBを用意

---

## 更新履歴

- 2026-01-02: ForStartup版として新規作成（Airbnb/Freshworks/Boxナレッジ統合）
