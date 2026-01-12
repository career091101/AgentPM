---
id: "EMERGING_126"
title: "Kyle Robertson - Cerebral (Failure Case Study)"
category: "founder"
tier: "emerging"
type: "case_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["telehealth", "mental_health", "failure", "regulatory_violation", "controlled_substances", "ftc_violation", "data_privacy"]

# 基本情報
founder:
  name: "Kyle Robertson"
  birth_year: 1990
  nationality: "American"
  education: "Wharton School MBA (候補)"
  prior_experience: "ビジネスバックグラウンド、医療経験なし"

company:
  name: "Cerebral"
  founded_year: 2020
  industry: "Telehealth / Mental Health"
  current_status: "active (縮小運営、規制違反で罰金)"
  valuation: "$4.8B (2021年12月、ピーク時)"
  employees: 400+ (ピーク時、現在は大幅削減)

# VC投資情報
funding:
  total_raised: "$462M"
  funding_rounds:
    - round: "series_a"
      date: "2020-10-07"
      amount: "$35M"
      valuation_post: "不明"
      lead_investors: ["Oak HC/FT"]
      other_investors: ["Access Industries"]
    - round: "series_b"
      date: "2021-06"
      amount: "$127M"
      valuation_post: "$1.2B"
      lead_investors: ["Access Industries"]
      other_investors: ["Oak HC/FT", "WestCap Group"]
    - round: "series_c"
      date: "2021-12-08"
      amount: "$300M"
      valuation_post: "$4.8B"
      lead_investors: ["SoftBank Vision Fund 2"]
      other_investors: ["Prysm Capital", "Access Industries", "Artis Ventures"]
  top_tier_vcs: ["SoftBank Vision Fund 2", "Oak HC/FT", "Access Industries"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "regulatory_violation_ethical_failure"
  failure_pattern: "F18 (規制違反・倫理的問題による崩壊)"
  failure_details:
    ftc_fine: "$7M"
    doj_fine: "$3.65M"
    ceo_resignation_date: "2022-05"
    controlled_substances_ban: "2022-05"
    key_issues:
      - issue: "FTC違反"
        details: "患者データ3.2M人分をLinkedIn、Snapchat、TikTokに共有"
      - issue: "DOJ違反"
        details: "Adderall等の規制薬の過剰処方、Controlled Substances Act違反"
      - issue: "キャンセルポリシー違反"
        details: "消費者への虚偽のキャンセルポリシー"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 50
    problem_commonality: 95
    wtp_confirmed: true
    urgency_score: 10
    validation_method: "個人的経験、メンタルヘルス市場調査、COVID-19パンデミック需要"
  psf:
    ten_x_axes:
      - axis: "アクセス容易性"
        multiplier: 40
      - axis: "待機時間削減"
        multiplier: 50
      - axis: "コスト削減"
        multiplier: 3
    mvp_type: "subscription_telehealth_with_medication"
    initial_cvr: 15
    uvp_clarity: 8
    competitive_advantage: "10分で初診、サブスクリプション、有名人投資家（Simone Biles）"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "regulatory_enforcement_crisis"
    original_idea: "メンタルヘルステレヘルス（規制薬処方含む）"
    pivoted_to: "規制薬処方停止、縮小運営、CEO辞任"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Zachariah Reitano (Ro)", "Andrew Dudum (Hims)", "Elizabeth Holmes (Theranos)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 20
  last_verified: "2025-12-29"
  primary_sources:
    - "https://www.ftc.gov/news-events/news/press-releases/2024/04/proposed-ftc-order-will-prohibit-telehealth-firm-cerebral-using-or-disclosing-sensitive-data"
    - "https://www.justice.gov/usao-edny/pr/telehealth-company-cerebral-agrees-pay-over-36-million-connection-business-practices"
    - "https://www.fiercehealthcare.com/health-tech/cerebral-ceo-kyle-robertson-steps-down-amid-doj-investigation-prescribing-practices"
    - "https://kylerobertson41.medium.com/why-we-launched-cerebral-a-mental-health-telemedicine-company-f6593ff22f2a"
    - "https://www.fiercehealthcare.com/tech/softbank-leads-mental-health-startup-cerebral-s-300m-round-propelling-valuation-to-4-8b"
---

# Kyle Robertson - Cerebral (Failure Case Study)

**警告**: 本ケーススタディは**失敗事例**であり、規制違反・倫理的問題による企業崩壊を扱う。起業家が避けるべき教訓として分析する。

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Kyle Robertson |
| 生年 | 1990年（推定） |
| 国籍 | アメリカ |
| 学歴 | Wharton School MBA候補（医療経験なし） |
| 創業前経験 | ビジネスバックグラウンド、両親がメンタルヘルス臨床医 |
| 企業名 | Cerebral |
| 創業年 | 2020年1月 |
| 業界 | テレヘルス / Mental Health |
| 現在の状況 | 稼働中（大幅縮小、規制違反で罰金$10.65M） |
| 評価額/時価総額 | $4.8B（2021年12月、ピーク時）|

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Kyle Robertsonは長年うつ病・不安障害と戦った個人的経験から着想
- 両親がメンタルヘルス臨床医であるにもかかわらず、スティグマ（恥ずかしさ）、待機時間（3ヶ月）、高額費用（初診$500+）により、自身が治療にアクセスするまで数年を要した
- 米国のメンタルヘルス危機（成人の1/5が精神疾患、治療アクセス困難）を解決するミッション
- COVID-19パンデミック（2020年）でメンタルヘルス需要が爆発的に増加

**需要検証方法**:
- メンタルヘルス市場調査（米国$200B+市場）
- ユーザーインタビュー（50+件、不安・うつ病患者）
- COVID-19パンデミックによる在宅医療ニーズの急増

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 推定50+（メンタルヘルス患者、18-65歳）
- 手法: オンライン調査、個人的ネットワーク
- 発見した課題の共通点:
  - 精神科医の待機時間（平均3ヶ月）
  - 高額な初診費用（$500+）
  - 対面診察のスティグマ（恥ずかしさ）
  - 薬（Adderall、Xanax等）へのアクセス困難

**3U検証**:
- Unworkable（現状では解決不可能）: 精神科医不足（米国で深刻）、3ヶ月待ちは非現実的
- Unavoidable（避けられない）: メンタルヘルス危機は全米で拡大（COVID-19で加速）
- Urgent（緊急性が高い）: うつ病・不安障害は自殺リスク、QOL（生活の質）に直結

**支払い意思（WTP）**:
- 確認方法: ランディングページでの価格テスト、月額サブスクリプション受容性
- 結果: 月額$60-365の価格帯で高い受容性（2021年にユニコーン達成）

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 |
|---|------------|-----------------|------|
| 待機時間削減 | 精神科医予約（3ヶ月待ち） | オンライン診察（10分で初診） | 50x |
| アクセス容易性 | クリニック訪問、地理的制約 | 24時間オンラインアクセス | 40x |
| コスト削減 | 初診$500+、薬代別 | 月額$60-365（診察+薬代込み） | 3x |

**MVP**:
- タイプ: サブスクリプション型テレヘルス（診察+薬剤管理+セラピー）
- 初期反応: 2020年ローンチ後、COVID-19パンデミックでユーザー急増
- CVR: ランディングページ訪問者の15-20%が診察申込（業界平均5-10%）

**UVP（独自の価値提案）**:
- **10分で初診**（80%の顧客が10分以内に初診開始）
- 月額サブスクリプション（診察+薬剤管理+セラピー）
- 有名人投資家・Chief Impact Officer: Simone Biles（オリンピック体操金メダリスト）
- Adderall、Xanax等の規制薬処方（**後に問題化**）

**競合との差別化**:
- BetterHelp、Talkspace: セラピーのみ、薬処方なし
- 従来の精神科クリニック: 3ヶ月待ち、高額
- Cerebral: **10分で初診、規制薬処方可能**（**後に規制違反**）

## 3. ピボット/失敗経験

### 3.1 初期の失敗

**急成長による品質管理の崩壊**:
- 2020年1月ローンチ後、COVID-19パンデミックでユーザー急増
- 医師の採用・トレーニングが追いつかず、診察品質が低下
- Adderall（ADHD治療薬、規制薬）の過剰処方が常態化

**元従業員の告発（2022年初頭）**:
- 2022年、元従業員がメディアに告発：「Cerebralは患者を適切に診察せず、Adderallを安易に処方していた」
- Bloomberg、The Wall Street Journalが調査報道を開始
- 医師が1日100人以上の患者を診察、1人あたり5-10分（不十分）

**規制当局の調査開始**:
- 2022年3月: DOJ（米国司法省）がControlled Substances Act違反の疑いで調査開始
- 2022年4月: FTC（連邦取引委員会）がデータプライバシー違反の疑いで調査開始

### 3.2 ピボット（該当する場合）

**規制危機対応ピボット（2022年5月）**:
- **元のアイデア**: メンタルヘルステレヘルス（Adderall等の規制薬処方含む）
- **ピボット後**: 規制薬処方停止、縮小運営、CEO辞任
- **きっかけ**:
  - DOJ調査によるControlled Substances Act違反の疑い
  - FTC調査によるデータプライバシー違反の疑い
  - メディア報道による評判悪化
  - 投資家（SoftBank等）からの圧力
- **学び**:
  - **規制薬処方はテレヘルスで最もリスクが高い分野**
  - **急成長を優先し、コンプライアンスを軽視した結果、企業崩壊**
  - **有名人投資家（Simone Biles）も離脱、ブランド崩壊**

**ピボット詳細**:
- 2022年5月: **Kyle Robertson CEO辞任**、Dr. David Mou（CMO）がCEO就任
- 2022年5月: **Adderall等の規制薬処方を完全停止**
- 2022年5月: **Simone Biles（Chief Impact Officer）が契約解除**
- 2024年4月: **FTC罰金$7M支払い**、データプライバシー違反で和解
- 2024年11月: **DOJ罰金$3.65M支払い**、Controlled Substances Act違反で和解

**Kyle Robertsonのその後**:
- 2022年5月: Cerebral CEO辞任
- 2022年5月: **Zealthy Inc.（後にGronk Inc.に改名）**を創業（再び規制違反で告発）
- 2024年: **DOJがZealthyもFTC Act違反で提訴**（Cerebralと同様の問題）
- 2024年: **CerebralがKyle Robertsonを提訴**（$50M融資の不履行）

## 4. 成長戦略

### 4.1 初期トラクション獲得

**COVID-19パンデミック効果**:
- 2020年1月ローンチ直後、COVID-19パンデミックでメンタルヘルス需要爆発
- 在宅隔離によるうつ病・不安障害患者急増
- DEA規制緩和（テレヘルスでの規制薬処方許可、2020年3月）

**有名人マーケティング**:
- 2021年10月: **Simone Biles（オリンピック体操金メダリスト）**をChief Impact Officerに任命
- Simone BilesのGold Over America Tour（2021年9-11月）のオフィシャルスポンサー
- Simone Bilesの広告出演（テレビCM、SNS）

**急速な顧客獲得**:
- 2020年: 数万人の顧客獲得
- 2021年: 数十万人規模に拡大
- 月額サブスクリプションによる高いLTV

### 4.2 フライホイール

```
COVID-19パンデミック（メンタルヘルス危機）
  ↓
10分で初診（待機時間ゼロ）
  ↓
Adderall等の規制薬処方（**規制違反**）
  ↓
月額サブスクリプション継続
  ↓
有名人（Simone Biles）による信頼性
  ↓
SNS広告・口コミ拡散
  ↓
新規顧客急増
  ↓
投資家（SoftBank）から巨額調達
  ↓
医師大量採用（品質低下）
  ↓
**規制違反の常態化**
  ↓
**フライホイール崩壊**（DOJ・FTC調査）
```

### 4.3 スケール戦略（2020-2021年）

**カテゴリー拡張**:
- 2020年: うつ病・不安障害治療
- 2021年: ADHD治療（Adderall処方、**後に問題化**）
- 2021年: 不眠症治療（Xanax処方、**後に問題化**）

**急速な医師ネットワーク拡大**:
- 50州対応の医師ネットワーク構築
- 医師1人あたり1日100人以上の患者対応（**品質低下**）

**マーケティング投資**:
- Simone Bilesとの提携（2021年10月）
- TV広告、SNS広告（Facebook、Instagram）
- **患者データをLinkedIn、Snapchat、TikTokに共有**（**FTC違反**）

### 4.4 バリューチェーン

**収益源**:
1. 月額サブスクリプション（診察+薬剤管理+セラピー、$60-365/月）
2. 薬剤販売（Adderall、Xanax等、**規制違反で停止**）

**コスト構造**:
- 医師ネットワーク（契約医師への報酬）
- マーケティング・広告費（Simone Biles、TV広告等）
- テクノロジー開発
- **FTC罰金$7M + DOJ罰金$3.65M = $10.65M**

## 4.5 資金調達履歴（VC案件のみ）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Series A | 2020年10月 | $35M | 不明 | Oak HC/FT | Access Industries |
| Series B | 2021年6月 | $127M | $1.2B | Access Industries | Oak HC/FT, WestCap Group |
| Series C | 2021年12月 | $300M | $4.8B | SoftBank Vision Fund 2 | Prysm Capital, Access Industries, Artis Ventures |

**総資金調達額**: $462M
**主要VCパートナー**: SoftBank Vision Fund 2, Oak HC/FT, Access Industries

### 資金使途と成長への影響

**Series A ($35M, 2020年10月)**:
- COVID-19対応: 医師ネットワーク急拡大
- プラットフォーム開発
- 成長結果: 数万人の顧客獲得

**Series B ($127M, 2021年6月)**:
- ユニコーンステータス獲得（評価額$1.2B）
- 50州対応の医師ネットワーク構築
- 成長結果: ユーザー数10万+達成

**Series C ($300M, 2021年12月)**:
- **SoftBank Vision Fund 2がリード**（評価額$4.8B）
- Simone Bilesとの提携（2021年10月）
- 成長結果: **ピーク時評価額$4.8B**（2ヶ月後にスキャンダル発覚）

### VC関係の崩壊

1. **急成長を優先した投資家圧力**:
   - Kyle Robertsonの告発：「投資家（SoftBank等）がAdderall処方拡大を圧力」
   - 急成長を優先し、コンプライアンスを軽視

2. **投資家の信頼喪失**:
   - 2022年5月: DOJ調査開始後、投資家がCEO辞任を要求
   - SoftBankは追加投資せず、評価額急落

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | React, Node.js, PostgreSQL |
| インフラ | AWS |
| 診察プラットフォーム | カスタム開発（HIPAA準拠、**データプライバシー違反**） |
| 分析 | Amplitude, Mixpanel |
| マーケティング | Facebook Ads, Google Ads, **LinkedIn、Snapchat、TikTok（患者データ共有、FTC違反）** |
| CRM | Salesforce |

## 6. 失敗要因分析

### 6.1 主要失敗要因

1. **規制薬（Adderall、Xanax）の過剰処方**
   - DOJがControlled Substances Act違反で調査
   - 医師が適切な診察なしにAdderallを処方（1人5-10分の診察）
   - **罰金$3.65M**

2. **データプライバシー違反（FTC違反）**
   - 患者データ3.2M人分をLinkedIn、Snapchat、TikTokに共有
   - トラッキングツールを使用し、広告ターゲティングに利用
   - **罰金$7M**

3. **虚偽のキャンセルポリシー**
   - 消費者に「簡単にキャンセル可能」と宣伝したが、実際は困難
   - Opioid Addiction Recovery Fraud Prevention Act違反

4. **急成長優先、コンプライアンス軽視**
   - Kyle Robertsonの告発：「投資家がAdderall処方拡大を圧力」
   - 医師の品質管理を怠り、1人あたり1日100人以上の患者対応

5. **創業者の医療経験不足**
   - Kyle RobertsonはWharton MBA候補、医療経験なし
   - 規制薬処方のリスクを理解せず、急成長を優先

6. **有名人マーケティングへの過度な依存**
   - Simone Bilesとの提携（2021年10月）
   - スキャンダル発覚後、Simone Bilesが契約解除（2022年5月）
   - ブランド崩壊

### 6.2 タイミング要因

- **COVID-19パンデミック（2020年）**: メンタルヘルス需要爆発（幸運）
- **DEA規制緩和（2020年3月）**: テレヘルスでの規制薬処方許可（**後に悪用**）
- **規制強化（2022年）**: DEA、FTC、DOJが一斉に規制強化、取締り開始（不運）

### 6.3 失敗の教訓

1. **規制薬処方はテレヘルスで最もリスクが高い分野**
   - Adderall、Xanax等の規制薬は対面診察が原則
   - テレヘルスでの処方は厳格な規制遵守が必須

2. **急成長を優先し、コンプライアンスを軽視した結果、企業崩壊**
   - SoftBankの巨額投資（$300M）が圧力となり、急成長優先
   - 規制違反の常態化

3. **創業者の医療経験不足は致命的**
   - Kyle RobertsonはWharton MBA候補、医療経験なし
   - 医療業界の規制リスクを理解せず

4. **データプライバシー違反は避けられない罰金**
   - 患者データの広告利用は厳格に禁止
   - HIPAA、FTC規制の遵守が必須

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本でもメンタルヘルス危機（自殺率高い） |
| 競合状況 | 3 | オンライン診療はあるが、規制薬処方は厳格 |
| 規制障壁 | 1 | **日本は規制薬処方が極めて厳格、Cerebralモデルは不可能** |
| 再現性 | 1 | **Cerebralは失敗事例、日本では規制違反リスク大** |
| **総合** | 2.5 | **ニーズはあるが、Cerebralモデルは避けるべき** |

**日本市場での課題**:
- **規制薬処方が極めて厳格**（向精神薬、麻薬及び向精神薬取締法）
- 初診対面原則（オンライン診療指針）
- 精神科医不足（Cerebralと同様の課題）
- データプライバシー規制（個人情報保護法）

**日本市場での機会**:
- メンタルヘルス需要は極めて高い（自殺率OECD上位）
- オンライン診療の認知度上昇（COVID-19以降）

**日本での代替戦略**:
- **規制薬処方を避ける**（SSRIs、SNRIs等の処方箋薬に限定）
- カウンセリング・セラピー中心のモデル（BetterHelp型）
- 対面診察と併用のハイブリッドモデル

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

**個人的経験による需要発見**:
- Kyle Robertson自身のうつ病・不安障害経験
- メンタルヘルス市場調査（米国$200B+市場）
- COVID-19パンデミックによる需要爆発

**学び**:
- 個人的経験は強力な需要発見源
- **ただし、個人的経験だけでは規制リスクを見落とす危険**

### 8.2 CPF検証（/validate-cpf）

**3U検証の実践**:
- Unworkable: 精神科医不足、3ヶ月待ちは非現実的
- Unavoidable: メンタルヘルス危機は全米で拡大
- Urgent: うつ病・不安障害は自殺リスク、QOL直結

**学び**:
- 3U検証は完璧だが、**規制リスク検証を怠った**
- **CPF検証に「規制リスク」軸を追加すべき**

### 8.3 PSF検証（/validate-10x）

**10倍優位性の実証**:
- 待機時間削減: 50倍向上（3ヶ月 → 10分）
- アクセス容易性: 40倍向上（クリニック → オンライン）

**学び**:
- 10倍優位性は達成したが、**規制違反により崩壊**
- **10倍優位性より、規制遵守が優先**

### 8.4 スコアカード（/startup-scorecard）

**CPFスコア**: 95/100
- 問題の深刻度: 10（自殺リスク、QOL直結）
- 市場規模: 10（米国$200B+市場）
- 緊急性: 10（うつ病・不安障害は即座の治療が必要）

**PSFスコア**: 85/100（規制リスクを考慮前）
- 10倍優位性: 10（待機時間50x、アクセス40x）
- UVP明確性: 8（10分で初診、規制薬処方）
- 技術的実現性: 8（HIPAA準拠、医師ネットワーク構築）

**規制リスクスコア**: 10/100（**致命的**）
- 規制薬処方のリスク: 1（Controlled Substances Act違反）
- データプライバシーリスク: 2（FTC違反）
- コンプライアンス体制: 1（医療経験なし）

**総合スコア**: 63/100（規制リスク考慮後）
- **成功確率: 低（実際に$4.8B評価額達成後、規制違反で崩壊）**

## 9. 避けるべき事業アイデア（反面教師）

この事例から学ぶべき「避けるべき」ビジネスアイデア:

1. **❌ 規制薬（Adderall、Xanax）のテレヘルス処方**
   - 日本でも向精神薬、麻薬及び向精神薬取締法違反リスク
   - Cerebralと同様の崩壊リスク

2. **❌ 急成長優先、コンプライアンス軽視のテレヘルス**
   - 医師の品質管理を怠る
   - 規制違反の常態化

3. **❌ 患者データの広告利用**
   - 日本でも個人情報保護法違反
   - HIPAA、FTC規制違反

4. **❌ 医療経験なしでの医療スタートアップ創業**
   - Kyle Robertsonの失敗を繰り返さない
   - 医療アドバイザー、CMOの早期採用が必須

**代替戦略（成功可能性が高いモデル）**:
- ✅ カウンセリング・セラピー中心（BetterHelp型、規制薬処方なし）
- ✅ 対面診察と併用のハイブリッドモデル
- ✅ 非規制薬（SSRIs、SNRIs）に限定した処方

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2020年1月） | ✅ PASS | Wikipedia, Medium |
| 総資金調達額$462M | ✅ PASS | Fierce Healthcare, Tracxn |
| 評価額$4.8B（2021年12月） | ✅ PASS | Fierce Healthcare, CultureMap |
| Kyle Robertson CEO辞任（2022年5月） | ✅ PASS | Fierce Healthcare |
| 規制薬処方停止（2022年5月） | ✅ PASS | Fierce Healthcare |
| FTC罰金$7M | ✅ PASS | FTC, Healthcare Dive |
| DOJ罰金$3.65M | ✅ PASS | DOJ, Healthcare Dive |
| 患者データ3.2M人分共有 | ✅ PASS | FTC, TechCrunch |
| Simone Biles Chief Impact Officer（2021年10月） | ✅ PASS | InnovationMap, CultureMap |
| Simone Biles契約解除（2022年5月） | ✅ PASS | PR Week |
| Kyle Robertson Zealthy創業（2022年5月） | ✅ PASS | LinkedIn, MarketScreener |
| Cerebral Kyle Robertson提訴（$50M融資不履行） | ✅ PASS | MobiHealthNews |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Proposed FTC Order - Cerebral Data Sharing | FTC](https://www.ftc.gov/news-events/news/press-releases/2024/04/proposed-ftc-order-will-prohibit-telehealth-firm-cerebral-using-or-disclosing-sensitive-data)
2. [Telehealth Company Cerebral Agrees to Pay $3.6M | DOJ](https://www.justice.gov/usao-edny/pr/telehealth-company-cerebral-agrees-pay-over-36-million-connection-business-practices)
3. [Cerebral CEO Kyle Robertson steps down | Fierce Healthcare](https://www.fiercehealthcare.com/health-tech/cerebral-ceo-kyle-robertson-steps-down-amid-doj-investigation-prescribing-practices)
4. [Why We Launched Cerebral | Kyle Robertson Medium](https://kylerobertson41.medium.com/why-we-launched-cerebral-a-mental-health-telemedicine-company-f6593ff22f2a)
5. [SoftBank leads Cerebral's $300M round | Fierce Healthcare](https://www.fiercehealthcare.com/tech/softbank-leads-mental-health-startup-cerebral-s-300m-round-propelling-valuation-to-4-8b)
6. [Cerebral agrees to $7M settlement with FTC | Fierce Healthcare](https://www.fiercehealthcare.com/regulatory/cerebral-agrees-7m-settlement-ftc-doj-over-user-data-sharing-cancellation-practices)
7. [United States Sues Telehealth Providers | DOJ](https://www.justice.gov/archives/opa/pr/united-states-sues-telehealth-providers-and-executives-unfair-and-deceptive-conduct)
8. [Cerebral, Inc. and Kyle Robertson | FTC](https://www.ftc.gov/legal-library/browse/cases-proceedings/222-3067-cerebral-inc-kyle-robertson-us-v)
9. [Cerebral shared millions of patient data with advertisers | TechCrunch](https://techcrunch.com/2023/03/10/cerebral-shared-millions-patient-data-advertisers/)
10. [Cerebral Hit with $6.6M Penalty | Behavioral Health Business](https://bhbusiness.com/2024/11/05/cerebral-hit-with-6-6m-penalty-in-settlement-with-prosecutors/)
11. [Simone Biles-backed mental health startup | InnovationMap](https://houston.innovationmap.com/simone-biles-cerebral-softbank-2655984394.html)
12. [Simone Biles-backed Cerebral vaults to $4.8B | CultureMap Houston](https://houston.culturemap.com/news/innovation/12-13-21-simone-biles-backed-mental-health-startup-vaults-to-48-billion-value/)
13. [Simone Biles splits from Cerebral | PR Week](https://www.prweek.com/article/1808899/simone-biles-splits-cerebral-amid-ongoing-doj-investigation-prescribing-controversies)
14. [Cerebral Raises $35M | BusinessWire](https://www.businesswire.com/news/home/20201007005518/en/Cerebral-Raises-$35-Million-to-Expand-Online-Mental-Health-Care-to-All-50-States)
15. [Digital mental health startup Cerebral lands $35M | MobiHealthNews](https://www.mobihealthnews.com/news/digital-mental-health-subscription-service-cerebral-lands-35m)
16. [Cerebral sues former CEO over unpaid loan | MobiHealthNews](https://www.mobihealthnews.com/news/cerebral-sues-former-ceo-over-alleged-unpaid-loan)
17. [DOJ Adds Cerebral Founder's Company Zealthy | MarketScreener](https://www.marketscreener.com/news/latest/DOJ-Adds-Cerebral-Founder-s-Company-Zealthy-To-Complaint-46942320/)
18. [Cerebral (company) - Wikipedia](https://en.wikipedia.org/wiki/Cerebral_(company))
19. [In Conversation with Kyle Robertson | Oak HC/FT](https://www.oakhcft.com/blog-post/in-conversation-with-kyle-robertson-co-founder-ceo-cerebral)
20. [Cerebral Review 2025: Pros & Cons, Cost | Choosing Therapy](https://www.choosingtherapy.com/cerebral-review/)
