---
id: "FOUNDER_184"
title: "Henrique Dubugras & Pedro Franceschi - Brex"
category: "founder"
tier: "vc_backed"
type: "case_study"
version: "1.0"
created_at: "2026-01-02"
updated_at: "2026-01-02"
tags: ["fintech", "corporate-credit-card", "B2B", "SaaS", "payments", "Y-Combinator", "Brazil", "serial-entrepreneur"]

# 基本情報
founder:
  name: "Henrique Dubugras & Pedro Franceschi"
  birth_year: 1995  # Dubugras: 1995年、Franceschi: 1997年
  nationality: "ブラジル → アメリカ"
  education: "Stanford大学（1年で中退）"
  prior_experience: "Pagar.me（ブラジルのStripe）創業・売却（15歳で創業、19歳で売却）"

company:
  name: "Brex"
  founded_year: 2017
  industry: "FinTech / 法人クレジットカード / 支出管理"
  current_status: "private"
  valuation: "$12.3B（2021年）、2025年IPO準備中"
  employees: 1100  # 2024年1月に20%削減後の推定値

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 85  # 70-80名のパイロット顧客 + LinkedInスクレイピングから外国人創業者へのアウトリーチで85名
    problem_commonality: 90  # YCバッチメイトほぼ全員が法人カード取得に苦労、スタートアップ3社に1社がBrexを利用（米国VC支援企業）
    wtp_confirmed: true
    urgency_score: 9
    validation_method: "自己体験 + YCバッチメイト観察 + 85名パイロット顧客での共同構築"
  psf:
    ten_x_axes:
      - axis: "与信枠"
        multiplier: 30
      - axis: "審査スピード"
        multiplier: 100
      - axis: "個人保証"
        multiplier: "無限（不要 vs 必須）"
    mvp_type: "concierge"
    initial_cvr: 0  # パイロット顧客は直接スカウト、CVRデータなし
    uvp_clarity: 10
    competitive_advantage: "個人保証不要 + 銀行残高ベース与信 + 10-20倍の与信枠 + 無料"
  pivot:
    occurred: true
    pivot_count: 2
    pivot_trigger: "market_shift"
    original_idea: "VRスタートアップ（YC応募時）"
    pivoted_to: "法人クレジットカード（YC 3週目）→ スタートアップ専用 → エンタープライズ重視（2022年SMB撤退）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2026-01-02"
  primary_sources:
    - "TechCrunch - How the 22-year-old founders of Brex built a billion-dollar business"
    - "Y Combinator - Q&A with Henrique Dubugras and Pedro Franceschi"
    - "Medium - In-Depth Analysis: The 6-Year Journey of Brex"
    - "TechCrunch - Brex co-founder details decisions behind pivots, layoffs"
    - "TechCrunch - Brex abandons co-CEO model, talks IPO"
    - "Wikipedia - Brex"
    - "LinkedIn - An Interview With Brex Co-Founders"
    - "Contrary Research - Brex Business Breakdown"
    - "The Complete Guide to Brex: A Masterclass for High-Growth Companies"
    - "Brex Journal - The turnaround is over"
    - "TechCrunch - Why did Brex really decide to ditch SMBs"
    - "Brex - Global Capabilities Expansion"
---

# Henrique Dubugras & Pedro Franceschi - Brex

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Henrique Dubugras（1995年生）& Pedro Franceschi（1997年生） |
| 生年 | Dubugras: 1995年、Franceschi: 1997年 |
| 国籍 | ブラジル → アメリカ |
| 学歴 | Stanford大学（1年で中退） |
| 創業前経験 | Pagar.me（ブラジルのStripe）を15歳で創業、19歳で売却（$30M調達、$1.5B処理額、150名体制でStoneに売却） |
| 企業名 | Brex |
| 創業年 | 2017年1月3日 |
| 業界 | FinTech / 法人クレジットカード / 支出管理 |
| 現在の状況 | Private（2025年IPO準備中、2025年8月に営業キャッシュフロー黒字化達成） |
| 評価額/時価総額 | $12.3B（2021年10月） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- 2017年、DubugrasとFranceschiはPagar.me売却後にStanford大学に入学したが、1年未満で中退してY Combinatorに応募
- 当初はVRスタートアップを計画していたが、2017年初頭のConsumer Electronic Showで「自分たちは市場を何も知らない」と気づく
- YC参加3週目に、**自分たちを含むYCバッチメイトの誰も法人クレジットカードを取得できない**ことに気づく
- Dubugras自身の証言: 「PedroとわたしはY Combinatorから$120,000の資金を受けたのに、法人クレジットカードを取得できなかった」

**需要検証方法**:
- 自己体験: Pagar.me時代にブラジルからアメリカで事業をしていたときも同じ問題に直面していた
- YCバッチメイト全員への観察: 誰も法人カードを取得できない、または個人保証が必要だった
- 創業者としての大きなネットワーク（Pagar.me時代の人脈 + YCコミュニティ）を活用

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: **85名**（70-80名のパイロット顧客 + LinkedInで外国人創業者をスクレイピングしてメール）
- 手法: 創業者または財務担当者である友人・家族に直接コンタクト → LinkedInで外国人創業者（FICOスコアなしで最も苦労する層）を特定してメール送信
- 発見した課題の共通点: スタートアップは投資を受けても法人カードを取得できない、伝統的銀行はクレジットヒストリーのない初期企業を審査できない

**3U検証**:
- **Unworkable（現状では解決不可能）**: 伝統的銀行はスタートアップを審査できず、個人保証が必須
- **Unavoidable（避けられない）**: 会社運営には経費精算・支払いが不可欠
- **Urgent（緊急性が高）**: 9/10 - カードがないと事業運営が困難、創業者個人のクレジットスコアにリスク

**支払い意思（WTP）**:
- 確認方法: パイロット顧客85名と共同でMVPを構築、製品ローンチ前から待機リスト形成
- 結果: **確認済み** - 2018年ローンチ時にスタートアップは「文字通りカードを取得できなかった」ため、強烈な需要が存在

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 |
|---|------------|-----------------|------|
| 与信枠 | $5,000-20,000（個人クレジット依存） | $100,000-600,000（銀行残高ベース） | **30x** |
| 審査スピード | 数週間〜数ヶ月 | 数分（オンライン完結） | **100x以上** |
| 個人保証 | 必須（創業者個人のリスク） | **不要** | **無限** |
| 年会費 | $95-695 | **$0** | **無限** |

**MVP**:
- タイプ: **Concierge MVP**（70-80名のパイロット顧客と共同構築）
- 初期機能: 高速サインアップ、個人保証不要の高与信枠、自動レシート取り込み
- 初期反応: パイロット顧客からのフィードバックで機能を精緻化
- CVR: パイロット顧客は直接スカウトのためCVRデータなし

**UVP（独自の価値提案）**:
- 個人保証不要で、会社の銀行残高と収益をもとに与信枠を決定
- 伝統的カードの10-20倍、最大40倍の与信枠（Brex銀行口座と組み合わせた場合）
- 年会費無料、グローバル利用可能、リアルタイムレポート

**競合との差別化**:
- **代替的与信モデル**: 個人クレジットスコアではなく、会社のキャッシュポジションと収益を評価
- **スタートアップ特化**: YC、Sequoia、Andreessen Horowitzなど著名VCから資金調達した企業を優先
- **米国VC支援スタートアップの3社に1社が利用**（2024年時点）

## 3. ピボット/失敗経験

### 3.1 YC 3週目のピボット（2017年）

- **元のアイデア**: VRスタートアップ
- **ピボット後**: 法人クレジットカード
- **きっかけ**: Consumer Electronic Showで「市場を何も知らない」と気づき、YCバッチメイトが誰も法人カードを取得できない現実を目の当たりに
- **学び**: 自分たちが深く知っている問題、自分たちが顧客である領域にフォーカス

### 3.2 SMB撤退ピボット（2022年）

- **元のアイデア**: スタートアップ専用カードから中小企業（SMB）へ拡大
- **ピボット後**: 「プロフェッショナルな資金調達」を受けた企業のみに絞り、SMB顧客数万社のアカウントを閉鎖
- **きっかけ**:
  - 「すべてを同時にやるのは本当に難しい」と気づく
  - 顧客から遠ざかり、組織が肥大化（過剰な管理レイヤー）
  - 資金調達額ではなく「組織のフォーカス」が成功の鍵
- **影響**: 2022年10月に従業員11%削減（136名）、2024年1月に20%削減（282名）
- **学び**: ノーと言う勇気、フォーカスの重要性

### 3.3 Co-CEO解消（2024年）

- **元の体制**: Dubugras & Franceschi 共同CEO（創業以来7年間）
- **新体制**: Franceschi が単独CEO、Dubugras は取締役会長
- **きっかけ**: 2025年IPO準備、キャッシュフロー黒字化達成（2025年8月）
- **学び**: 成長ステージに応じた組織体制の最適化

## 4. 成長戦略

### 4.1 初期トラクション獲得

- **2017年4月**: Y Combinator Series A（$7M、Ribbit Capital主導、YC Demo Day前に完了）
- **2018年3月**: Series B（$60M、YC Continuity Fund主導）
- **2018年**: 法人クレジットカード正式ローンチ
- **2018-2020**: Series C（$150M、DST Global主導、評価額$2.6B）
- **2021年4月**: Series D（$425M）
- **2021年10月**: 評価額$12.3Bに到達

### 4.2 フライホイール

```
VC支援スタートアップへの高与信枠カード提供
    ↓
利用額増加 → インターチェンジフィー収益
    ↓
データ蓄積（スタートアップの財務パターン）
    ↓
より正確な与信モデル → さらに高い与信枠提供
    ↓
顧客満足度向上 → 口コミでスタートアップ間に拡散
    ↓
米国VC支援スタートアップの3社に1社が利用
```

### 4.3 スケール戦略

- **ニッチドミナンス**: まずYC卒業生、次にSequoia/a16z投資先など著名VC支援企業に絞る
- **ネットワーク効果**: スタートアップコミュニティ内での口コミ
- **プロダクト拡張**: クレジットカードからSaaS（支出管理ソフトウェア）へ
  - 2022年にソフトウェアサブスクリプション収益を追加（インターチェンジフィーのみから脱却）
- **エンタープライズシフト**: 2022年SMB撤退後、エンタープライズ顧客が91%成長（2024年）、純収益維持率130%超

### 4.4 グローバル展開

- **2023年**: 日本、シンガポール、フィリピンを含む50カ国以上でローカル通貨カード提供
- ただし**米国法人のみ対象**（米国企業のグローバル展開を支援するモデル）

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | 自社開発の与信エンジン、銀行API統合 |
| マーケティング | YCネットワーク、VCネットワーク経由の紹介 |
| 分析 | 自社開発の財務分析プラットフォーム |
| 支払い処理 | Visa提携、自社発行プラットフォーム |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **自己体験からの課題発見**: Pagar.me時代とYC時代の両方で同じ問題に直面
2. **代替的与信モデル**: クレジットスコアではなく銀行残高・収益ベースの与信
3. **10倍優位性**: 与信枠30倍、審査スピード100倍、個人保証不要
4. **フォーカス**: SMB撤退の勇気、エンタープライズへの集中

### 6.2 タイミング要因

- スタートアップブーム（2017-2021年のVC投資急増）
- 伝統的銀行のスタートアップ軽視
- API Bankingの普及（FinTech参入障壁低下）

### 6.3 差別化要因

- シリアルアントレプレナー（Pagar.me売却実績）による信頼性
- ブラジルでの決済事業経験（FinTech知見）
- YCネットワーク活用

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | 日本スタートアップも法人カード取得に苦労するが、米国ほど深刻ではない |
| 競合状況 | 4 | 伝統的銀行が依然強い、FinTech法人カードは少ない |
| ローカライズ容易性 | 2 | 日本の与信審査文化・規制が異なる、個人保証が一般的 |
| 再現性 | 2 | 銀行ライセンス取得の難易度、規制対応コスト |
| **総合** | 2.75 | **低〜中** - 規制・文化的障壁が高いが、ニッチニーズは存在 |

**備考**:
- Brexは米国法人のみ対象のため、日本企業は直接利用不可
- 日本スタートアップの海外展開時には活用可能

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **成功点**: 自分自身が顧客（YCバッチメイト全員が同じ課題）
- **教訓**: 自己体験 + 周囲の観察で課題の共通性を確認（interview_count: 85、problem_commonality: 90%）
- **推奨**: 自分が深く知っている領域、自分が顧客である問題にフォーカス

### 8.2 CPF検証（/validate-cpf）

- **成功例**: LinkedInスクレイピングで外国人創業者（最も課題が深刻な層）をターゲティング
- **注意点**: パイロット顧客と共同構築（Concierge MVP）で課題を深掘り
- **学び**: 友人・家族 → 最も課題が深刻な層へと段階的に拡大

### 8.3 PSF検証（/validate-10x）

- **成功例**: 与信枠30倍、審査スピード100倍、個人保証不要（無限倍）の3軸で圧倒的優位性
- **重要点**: 10倍優位性が複数軸にまたがる（単一軸ではない）
- **推奨**: 最低2軸以上の10倍優位性を確保

### 8.4 スコアカード（/startup-scorecard）

- **高評価項目**: 10倍優位性（3軸）、課題共通性90%、緊急性9/10、WTP確認済み
- **低評価項目**: SMB撤退による顧客数万社のアカウント閉鎖（フォーカスミス）
- **最終結果**: $12.3B評価額、2025年IPO準備中、営業キャッシュフロー黒字化達成

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **日本スタートアップ特化法人カード**: 銀行残高・VC調達額ベースの与信、個人保証不要オプション（規制対応必要）
2. **フリーランス向けビジネスカード**: 銀行口座連携で与信枠自動調整、経費精算自動化
3. **海外展開スタートアップ向けマルチカレンシーカード**: 日本企業のグローバル展開を支援（Brexは米国企業のみのため逆方向ニーズ）

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2017年1月3日） | PASS | Wikipedia, TechCrunch, Y Combinator |
| パイロット顧客数（70-85名） | PASS | Medium, Contrary Research |
| 評価額（$12.3B、2021年） | PASS | TechCrunch, Medium, Tracxn |
| SMB撤退（2022年6月） | PASS | TechCrunch, Wikipedia |
| 従業員削減（2022年11%, 2024年20%） | PASS | TechCrunch, Fast Company |
| 営業キャッシュフロー黒字化（2025年8月） | PASS | Brex Journal, TechCrunch |
| Co-CEO解消（2024年6月） | PASS | TechCrunch, Payments Dive |
| 米国VC支援スタートアップ3社に1社利用 | PASS | Swipesum, Kruze Consulting |

**凡例**: PASS = 2ソース以上確認

## 参照ソース

1. [TechCrunch - How the 22-year-old founders of Brex built a billion-dollar business](https://techcrunch.com/2018/10/05/how-the-22-year-old-founders-of-brex-built-a-billion-dollar-business-in-less-than-2-years/)
2. [Y Combinator - Q&A with Henrique Dubugras and Pedro Franceschi](https://www.ycombinator.com/blog/qa-with-henrique-dubugras-and-pedro-franceschi-cofounders-of-brex)
3. [Medium - In-Depth Analysis: The 6-Year Journey of Brex](https://medium.com/@maxslashwang/in-depth-analysis-the-6-year-journey-of-brex-from-startup-to-12-3-4ad9ff0ae4c0)
4. [TechCrunch - Brex co-founder details decisions behind pivots, layoffs](https://techcrunch.com/2022/11/02/brex-co-founder-henrique-dubugras-details-decisions-behind-pivots-layoffs-going-remote/)
5. [TechCrunch - Brex abandons co-CEO model, talks IPO](https://techcrunch.com/2024/06/12/fintech-brex-abandons-co-ceo-model-talks-ipo-cash-burn-and-plans-for-a-secondary-sale/)
6. [Wikipedia - Brex](https://en.wikipedia.org/wiki/Brex)
7. [LinkedIn - An Interview With Brex Co-Founders](https://www.linkedin.com/pulse/interview-brex-co-founders-pedro-franceschi-henrique-dubugras-li)
8. [Contrary Research - Brex Business Breakdown](https://research.contrary.com/company/brex)
9. [Swipesum - The Complete Guide to Brex](https://www.swipesum.com/insights/the-complete-guide-to-brex-a-masterclass-for-high-growth-companies)
10. [Brex Journal - The turnaround is over](https://www.brex.com/journal/the-turnaround-is-over)
11. [TechCrunch - Why did Brex really decide to ditch SMBs](https://techcrunch.com/2022/06/19/what-was-really-behind-brexs-decision-to-ditch-smbs/)
12. [Brex - Global Capabilities Expansion](https://www.brex.com/journal/press/brex-expands-empower-with-new-markets-and-global-capabilities)
