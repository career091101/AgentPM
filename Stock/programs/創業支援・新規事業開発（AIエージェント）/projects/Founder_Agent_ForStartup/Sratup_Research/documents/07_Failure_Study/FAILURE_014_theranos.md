---
id: "FAILURE_014"
title: "Elizabeth Holmes - Theranos (Fraud & Regulatory Failure)"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["healthcare", "fraud", "failure", "regulatory", "criminal", "blood testing"]

# 基本情報
founder:
  name: "Elizabeth Holmes"
  birth_year: 1984
  nationality: "アメリカ"
  education: "Stanford University (Chemical Engineering, 中退)"
  prior_experience: "Stanford研究員（中退して創業）"

company:
  name: "Theranos"
  founded_year: 2003
  industry: "Healthcare / Blood Testing / Medical Devices"
  current_status: "dissolved"
  valuation: "$9B（ピーク時）→ $0（清算）"
  employees: 800（ピーク時）

# VC投資情報
funding:
  total_raised: "$700M+"
  funding_rounds:
    - round: "seed"
      date: "2004"
      amount: "$6M"
      lead_investors: ["Tim Draper"]
    - round: "series_b"
      date: "2005"
      amount: "undisclosed"
      lead_investors: ["Don Lucas"]
    - round: "series_c"
      date: "2006"
      amount: "$28.5M"
      lead_investors: ["ATA Ventures"]
    - round: "multiple_rounds"
      date: "2004-2015"
      amount: "$700M+"
      investors: ["Rupert Murdoch ($125M)", "Walgreens ($140M)", "Larry Ellison", "Betsy DeVos", "Don Lucas", "Draper Fisher Jurvetson"]
  top_tier_vcs: ["Draper Fisher Jurvetson"]
  notable_investors: ["Rupert Murdoch", "Larry Ellison", "Walgreens", "Safeway"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "fraud_regulatory_shutdown"
  failure_pattern: "P16 + P23 + P28"
  failure_details:
    shutdown_date: "2018-09"
    total_funding_burned: "$700M+"
    peak_valuation: "$9B"
    liquidation_value: "$0"
    employees_affected: "800+"
    criminal_charges: "Elizabeth Holmes: 有罪判決（2022年）、禁固11年3ヶ月"
    civil_penalties: "SEC和解、投資家返金不可"
  failure_patterns:
    - code: "P16"
      name: "規制・法的問題"
      description: "FDA承認なし、CLIA違反、患者データ改ざん"
    - code: "P23"
      name: "品質問題・詐欺"
      description: "技術が機能せず、結果を偽装、投資家・患者を欺いた"
    - code: "P28"
      name: "過剰調達"
      description: "$700M+調達したが、技術は実現不可能"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0
    problem_commonality: 80
    wtp_confirmed: false
    urgency_score: 3
    validation_method: "技術的実証なし、虚偽の主張のみ"
  psf:
    ten_x_axes:
      - axis: "血液量"
        multiplier: 0.001  # 主張は1000倍少ない血液量だが、実現せず
      - axis: "検査コスト"
        multiplier: 0  # 主張はコスト削減だが、実現せず
      - axis: "検査速度"
        multiplier: 0  # 主張は迅速だが、実現せず
    mvp_type: "fraud_no_working_product"
    initial_cvr: null
    uvp_clarity: 10  # 主張は明確だが、全て虚偽
    competitive_advantage: "なし（技術が存在しなかった）"
  pivot:
    occurred: false
    pivot_count: 0

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []
  related_cases: ["FAILURE_015 (MoviePass - Unit Economics Failure)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources:
    - "Bad Blood (John Carreyrou book)"
    - "WSJ (John Carreyrou investigation)"
    - "SEC Complaint (2018)"
    - "DOJ Criminal Indictment (2018)"
    - "Trial Verdict (2022)"
---

# Elizabeth Holmes - Theranos（Fraud & Regulatory Failure）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Elizabeth Anne Holmes |
| 生年 | 1984年2月3日 |
| 国籍 | アメリカ |
| 学歴 | Stanford University（化学工学、2003年中退） |
| 創業前経験 | Stanford研究員（Channing Robertson教授の研究室） |
| 企業名 | Theranos（"therapy" + "diagnosis"） |
| 創業年 | 2003年（19歳） |
| 業界 | ヘルスケア / 血液検査 / 医療機器 |
| 現在の状況 | 解散（2018年9月）、創業者有罪判決（2022年） |
| ピーク評価額 | $9B（2014年） |
| 清算価値 | $0 |

## 2. 創業ストーリー（虚偽の物語）

### 2.1 Stanford中退と創業（2003年）

**起業動機（Holmes主張）**:
- 19歳でStanford中退
- 「針嫌いだった自分の経験から、指先採血で検査できる技術を開発したい」
- Channing Robertson教授の支援

**初期ビジョン**:
- 指先から数滴の血液で200以上の検査
- 従来の1/1000の血液量
- 従来の1/10のコスト
- 迅速な結果（数時間以内）

**問題点**:
- この技術は当初から実現不可能だった
- しかしHolmesは投資家・メディアに虚偽の主張を繰り返した

### 2.2 初期資金調達（2004-2006年）

**Seed（2004年）**:
- $6M調達
- リード投資家: Tim Draper（Draper Fisher Jurvetson）
- 技術的実証なし、ビジョンのみで調達

**Series C（2006年）**:
- $28.5M調達
- ATA Venturesがリード
- 依然として動作する製品なし

**投資家への虚偽説明**:
- 「技術は完成している」
- 「FDA承認プロセス進行中」
- 「アフガニスタンで米軍が使用中」（全て虚偽）

## 3. 詐欺の手口

### 3.1 技術的虚偽

**主張された技術: "Edison"**:
- 指先から数滴の血液（指先採血）
- 200以上の検査項目
- 従来の1/1000の血液量
- 従来の1/10のコスト

**実態**:
- Edisonは機能しなかった
- 検査の大部分は従来の商用機器（Siemens等）で実施
- 血液を希釈して検査（結果が不正確）
- 患者に虚偽の結果を提供

### 3.2 デモの偽装

**投資家向けデモ**:
- Edisonのデモは事前に仕込まれていた
- 実際の血液検査ではなく、事前に用意した結果を表示
- 技術者が裏で手動操作

**メディア向けデモ**:
- Walgreens店舗でのデモも偽装
- 実際には従来の機器で検査
- メディアに「革命的技術」として紹介

### 3.3 Walgreensとの提携（2013年）

**提携内容**:
- Walgreens店舗内にTheranos検査センター設置
- $140M投資
- 全米40店舗で展開

**虚偽の説明**:
- Holmesは「Edisonで検査している」と主張
- 実際には従来の機器を使用
- 患者に不正確な結果を提供（健康被害）

## 4. 詐欺の発覚

### 4.1 John Carreyrou調査（2015年）

**Wall Street Journalの調査**:
- 2015年10月、John Carreyrou記者が調査記事を公開
- 元従業員の内部告発
- 技術が機能していないことを暴露

**Holmesの反応**:
- 記事を否定
- 弁護士（David Boies）を使って圧力
- メディアで反論

### 4.2 規制当局の調査（2015-2016年）

**CMS（Centers for Medicare & Medicaid Services）**:
- 2016年、Theranos検査センターを査察
- CLIA（臨床検査改善法）違反を発見
- 患者の健康に直接的リスク

**FDA（Food and Drug Administration）**:
- Edisonは未承認医療機器
- 使用禁止命令

**是正措置命令**:
- 2016年7月、CMSがTheranos検査センター閉鎖命令
- Holmesに2年間の検査業界参入禁止

### 4.3 刑事訴追（2018年）

**SEC民事訴訟（2018年3月）**:
- 投資家に対する詐欺
- Holmesは和解（$500,000罰金、Theranos株放棄、10年間の役員禁止）
- 認否なし（no admission of wrongdoing）

**DOJ刑事起訴（2018年6月）**:
- 通信詐欺（wire fraud）の罪状9件
- 共謀の罪状2件
- 最大20年の禁固刑

**Theranos解散（2018年9月）**:
- 全従業員解雇
- 資産清算
- 投資家への返金ゼロ

## 5. 刑事裁判と判決（2021-2022年）

### 5.1 裁判経緯

**2021年9月**: 刑事裁判開始
- 検察: 投資家・患者を欺いた詐欺
- 弁護側: 事業の失敗であり、詐欺の意図なし

**主要証人**:
- 元CFO、元従業員、患者、投資家
- 技術専門家（技術の不可能性を証言）

**Holmesの証言**:
- 「元恋人Ramesh "Sunny" Balwaniに支配されていた」
- 「騙す意図はなかった」

### 5.2 判決（2022年1月）

**有罪判決**:
- 投資家に対する詐欺4件: 有罪
- 患者に対する詐欺: 無罪
- 共謀: 一部有罪

**量刑（2022年11月）**:
- **禁固11年3ヶ月**
- 罰金なし（支払能力なし）
- 出所後3年間の監視付き釈放

**収監（2023年5月）**:
- テキサス州Bryan連邦刑務所
- 最短出所日: 2032年（刑期短縮の可能性あり）

## 6. 失敗パターン分析

### 6.1 P16: 規制・法的問題

**FDA承認なし**:
- Edisonは未承認医療機器
- 臨床試験データなし
- 安全性・有効性の証明なし

**CLIA違反**:
- 検査の品質管理不足
- 検査結果の改ざん
- 患者データの虚偽報告

**刑事責任**:
- 通信詐欺（wire fraud）
- 投資家・患者を欺いた
- 有罪判決、禁固11年3ヶ月

### 6.2 P23: 品質問題・詐欺

**技術が存在しなかった**:
- Edisonは機能しなかった
- 検査の大部分は従来の機器
- 血液希釈による不正確な結果

**患者への健康被害**:
- 不正確な検査結果
- 誤診の可能性
- 適切な治療を受けられなかった患者

**組織的な隠蔽**:
- 従業員に秘密保持契約（NDA）
- 内部告発者への法的脅迫
- メディア・投資家への虚偽説明

### 6.3 P28: 過剰調達（Death by Overfunding）

**$700M+調達**:
- 技術が存在しないのに調達継続
- 投資家は技術を検証せず、ビジョンのみで投資
- 著名投資家（Murdoch、Ellison等）の盲信

**調達資金の使途**:
- 豪華なオフィス
- 高額な弁護士費用（告発者への圧力）
- 技術開発ではなく、イメージ戦略

**評価額$9B**:
- 実態のない評価額
- メディアのヒーロー化
- 批判的検証の欠如

## 7. なぜ詐欺が長期間継続したか

### 7.1 カリスマと物語

**Elizabeth Holmesのイメージ**:
- 「女性版Steve Jobs」
- 黒のタートルネック（Jobs模倣）
- 深い声（威厳を演出）
- Stanford中退の天才起業家

**メディアのヒーロー化**:
- Fortune、Forbes、Inc.等が特集
- TED Talkでの講演
- 「医療を民主化する」というビジョン

### 7.2 著名投資家・取締役の信頼

**取締役会**:
- George Shultz（元国務長官）
- Henry Kissinger（元国務長官）
- James Mattis（元国防長官）
- William Perry（元国防長官）

**問題点**:
- 医療・科学の専門家がいない
- 技術的検証なし
- ビジョンと人脈のみで信頼

### 7.3 秘密主義

**情報統制**:
- 従業員に厳格なNDA
- 部門間の情報共有禁止
- 内部告発者への法的脅迫

**外部からの検証困難**:
- 技術の公開なし
- 査読論文なし
- 独立した検証なし

## 8. 被害者

### 8.1 患者

**健康被害**:
- 不正確な検査結果
- 誤診の可能性
- 訴訟（集団訴訟）

### 8.2 投資家

**総損失額**: $700M+
- Rupert Murdoch: $125M損失
- Walgreens: $140M損失
- Betsy DeVos: 推定$100M損失
- 返金ゼロ

### 8.3 従業員

**解雇**:
- 800人以上が職を失う
- 履歴書に「Theranos」と書くことの汚名

**内部告発者への報復**:
- Tyler Shultz（George Shultzの孫）
- 法的脅迫、家族との断絶
- $400,000の弁護士費用

## 9. 教訓

### 9.1 技術的検証の重要性

**投資前のデューディリジェンス**:
- 技術の実証を要求
- 独立した専門家による検証
- 査読論文の有無

**ビジョンだけでは不十分**:
- 実現可能性の検証
- プロトタイプの動作確認
- 臨床試験データ

### 9.2 規制遵守

**医療分野の特殊性**:
- FDA承認必須
- CLIA遵守
- 患者の安全が最優先

**規制ショートカットは不可**:
- Move fast and break thingsは医療では通用しない
- 患者の健康に直接影響

### 9.3 組織文化

**透明性と説明責任**:
- 秘密主義は危険
- 内部告発者の保護
- 批判的な声を尊重

**倫理的リーダーシップ**:
- 短期的成功より長期的信頼
- 患者・投資家への誠実さ

### 9.4 メディアリテラシー

**ヒーロー化の危険性**:
- メディアの美談を鵜呑みにしない
- 批判的検証の重要性
- 専門家の意見を聞く

## 10. 日本への示唆

**日本でのTheranos型詐欺リスク**:
- 医療分野のスタートアップは規制が厳格
- しかし、バイオベンチャーでの類似事例あり
- 投資家の技術的検証能力が課題

**避けるべき警告サイン**:
- 秘密主義（技術の非公開）
- 規制当局の承認なし
- 査読論文なし
- 著名人への過度な依存
- 内部告発者への圧力

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2003年） | ✅ PASS | Bad Blood、Wikipedia、WSJ |
| ピーク評価額（$9B） | ✅ PASS | WSJ、Forbes、SEC Complaint |
| 総調達額（$700M+） | ✅ PASS | Crunchbase、WSJ、SEC |
| 有罪判決（2022年1月） | ✅ PASS | DOJ、裁判記録、CNBC |
| 量刑（禁固11年3ヶ月） | ✅ PASS | DOJ、裁判記録、NYT |
| Walgreens投資（$140M） | ✅ PASS | WSJ、Bad Blood |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Bad Blood - John Carreyrou (Book)](https://www.goodreads.com/book/show/37976541-bad-blood)
2. [WSJ - Theranos Investigation Series](https://www.wsj.com/news/author/7696)
3. [SEC Complaint - Elizabeth Holmes (2018)](https://www.sec.gov/litigation/complaints/2018/comp-pr2018-41-theranos-holmes.pdf)
4. [DOJ Press Release - Criminal Indictment](https://www.justice.gov/usao-ndca/pr/theranos-founder-and-former-chief-operating-officer-charged-alleged-wire-fraud-schemes)
5. [Wikipedia - Theranos](https://en.wikipedia.org/wiki/Theranos)
6. [CNBC - Elizabeth Holmes Verdict](https://www.cnbc.com/2022/01/03/theranos-ceo-elizabeth-holmes-found-guilty-of-fraud.html)
7. [NYT - Elizabeth Holmes Sentenced](https://www.nytimes.com/2022/11/18/technology/elizabeth-holmes-sentencing.html)
8. [Forbes - Elizabeth Holmes Net Worth](https://www.forbes.com/profile/elizabeth-holmes/)
9. [Vanity Fair - Theranos Investigation](https://www.vanityfair.com/news/2016/09/elizabeth-holmes-theranos-exclusive)
10. [ABC News - The Dropout (Documentary)](https://www.abc.net.au/news/2019-03-13/the-dropout-podcast-elizabeth-holmes-theranos/10824268)
11. [Crunchbase - Theranos](https://www.crunchbase.com/organization/theranos)
12. [FDA Warning Letter - Theranos (2016)](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/theranos-inc-8/4/16)
13. [CMS - Theranos Sanctions](https://www.cms.gov/newsroom/press-releases/statement-principal-deputy-administrator-andy-slavitt-certificate-revocation-newark-blood-testing)
14. [Bloomberg - Theranos Collapse](https://www.bloomberg.com/news/features/2018-09-05/theranos-employees-detail-the-company-s-final-desperate-days)
15. [NPR - Theranos Timeline](https://www.npr.org/sections/health-shots/2018/09/05/644567995/theranos-to-dissolve-as-investors-fail-to-find-a-buyer)
