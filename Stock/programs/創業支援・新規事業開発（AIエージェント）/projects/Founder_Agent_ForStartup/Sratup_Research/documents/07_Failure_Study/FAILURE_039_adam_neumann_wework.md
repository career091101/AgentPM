---
id: "FAILURE_039"
title: "Adam Neumann - WeWork (Founder Misconduct & Misalignment)"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["real estate", "sharing economy", "failure", "founder misconduct", "corporate governance", "over-valuation", "IPO collapse"]

# 基本情報
founder:
  name: "Adam Neumann"
  birth_year: 1979
  nationality: "イスラエル/アメリカ"
  education: "Baruch College (中退)"
  prior_experience: "スタートアップ創業者（複数失敗経験あり）"

company:
  name: "WeWork"
  founded_year: 2010
  industry: "Real Estate / Shared Workspace / Commercial"
  current_status: "public（SPAC経由、2023年NYSE回帰）"
  valuation: "$47B（ピーク時）→ $1.4B（2023年）"
  employees: 15,000+（ピーク時）

# VC投資情報
funding:
  total_raised: "$15B+"
  funding_rounds:
    - round: "seed"
      date: "2010"
      amount: "$1M"
      lead_investors: ["Miguel McKelvey（共同創業者）"]
    - round: "series_a"
      date: "2011"
      amount: "$5M"
      lead_investors: ["Benchmark Capital"]
    - round: "series_b"
      date: "2013"
      amount: "$10M"
      lead_investors: ["Khosla Ventures"]
    - round: "series_c"
      date: "2014"
      amount: "$150M"
      lead_investors: ["Benchmark Capital"]
    - round: "series_f"
      date: "2015"
      amount: "$430M"
      lead_investors: ["SoftBank Vision Fund"]
    - round: "series_g"
      date: "2017"
      amount: "$3.6B"
      lead_investors: ["SoftBank Vision Fund"]
    - round: "later_rounds"
      date: "2018-2019"
      amount: "$6B+"
      investors: ["SoftBank", "Benchmark", "Saudi PIF", "Fidelity"]
  top_tier_vcs: ["SoftBank Vision Fund", "Benchmark Capital"]
  notable_investors: ["Benchmark", "Khosla Ventures", "SoftBank Vision Fund", "Saudi Public Investment Fund", "Fidelity Investments"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "founder_misconduct_ipo_collapse"
  failure_pattern: "P22 + P24 + P28"
  failure_details:
    ipo_filing_date: "2019-08"
    ipo_withdrawn: "2019-09"
    peak_valuation: "$47B"
    post_ipo_valuation: "$1.4B（2023年）"
    founder_ousted: "2019-09"
    employees_affected: "6,000+（解雇）"
    shareholder_losses: "$40B+"
  failure_patterns:
    - code: "P22"
      name: "ファウンダー問題・ガバナンス欠陥"
      description: "Adam Neumannの私的利益優先、強引な経営、不透明な関連会社取引"
    - code: "P24"
      name: "過度な時価総額評価"
      description: "$47Bの評価に見合わない実質的価値、黒字化道筋なし"
    - code: "P28"
      name: "過剰調達"
      description: "$15B+調達したが、モデルの根本的欠陥（不動産スケーリング不可）"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0
    problem_commonality: 85
    wtp_confirmed: true
    urgency_score: 4
    validation_method: "市場需要はあったが、ビジネスモデルは破綻"
  psf:
    ten_x_axes:
      - axis: "費用削減"
        multiplier: 0.8  # 不動産費用は若干削減されたが、大きな革新性なし
      - axis: "利便性"
        multiplier: 3  # 柔軟な働き方は実現されたが、差別化不足
      - axis: "持続可能性"
        multiplier: 0  # ビジネスモデルが破綻
    mvp_type: "full_product"
    initial_cvr: null
    uvp_clarity: 9  # 「共有オフィス」は明確だが、10倍優位性なし
    competitive_advantage: "なし（不動産の長期契約縛りにより、スケーリング不可）"
  pivot:
    occurred: false
    pivot_count: 0

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []
  related_cases: ["FAILURE_014 (Theranos - Fraud)", "FAILURE_015 (MoviePass - Unit Economics)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 18
  last_verified: "2025-12-29"
  primary_sources:
    - "Rebranding the Deal (NYT Investigation)"
    - "WeWork IPO S-1 Filing (SEC)"
    - "The We Company Prospectus"
    - "Masayoshi Son Interview (SoftBank)"
    - "Bloomberg Investigation"
    - "Wall Street Journal Analysis"
---

# Adam Neumann - WeWork（Founder Misconduct & Misalignment）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Adam Neumann |
| 生年 | 1979年4月23日 |
| 国籍 | イスラエル（後にアメリカ国籍取得） |
| 学歴 | Baruch College（経営学、中退） |
| 共同創業者 | Miguel McKelvey（CFOから離脱） |
| 企業名 | WeWork（元The We Company） |
| 創業年 | 2010年 |
| 業界 | リアルエステート / シェアードワークスペース / コマーシャル |
| ピーク評価額 | $47B（2019年） |
| 現在の評価額 | $1.4B（2023年） |
| 従業員（ピーク時） | 15,000人以上 |
| 現在の状況 | 公開企業（2023年NYSE上場）、Adam Neumann追放 |

## 2. 創業ストーリーと急速な拡大

### 2.1 初期段階（2010-2013年）

**創業動機**:
- Adam Neumannが離婚後、共同作業スペースの需要を見出す
- フリーランサー向けの柔軟なオフィス環境を提供
- Miguel McKelveyとの協業で規模拡大

**初期モデル**:
- ニューヨークで最初のオフィスを開設（2010年）
- 月額アクセスベースの料金体系
- 企業から個人まで幅広いセグメント対象

**初期資金調達**:
- Seed: $1M（2010年）
- Series A: $5M（2011年）
- Benchmark Capitalが主導投資家

### 2.2 急速なスケーリング（2013-2017年）

**Series C - $150M（2014年）**:
- Benchmark Capitalが継続投資
- 企業評価額: $1B（ユニコーン認定）
- 世界展開の開始（ロンドン、東京等）

**SoftBank Vision Fund参入（2015-2017年）**:
- Series F: $430M（2015年）
- Series G: $3.6B（2017年）
- SoftBankの積極的支援で急速なグローバル拡張

**拡大ペース**:
- 2015年: 世界中で100以上のロケーション
- 2017年: 200以上のロケーション
- 2019年: 850以上のロケーション（ピーク時）

### 2.3 評価額の急騰（2017-2019年）

**$20B（2018年）** → **$47B（2019年）**:
- SoftBankが追加投資で時価総額を倍増
- Vision Fund内の主要ポートフォリオ企業へ
- IPO前のピークバリュエーション：$47B

## 3. ビジネスモデルの本質的欠陥

### 3.1 不動産の長期負債

**コスト構造**:
- 建物オーナーとの**長期リース契約**（15-20年）
- 固定費が極めて高い
- テナント需要が下がっても赤字続行

**テナント単価よりリース契約単価が高い**:
- WeWorkがテナント（オフィス）から得る月額: $500-$1,000/デスク
- 不動産オーナーに支払うリース代: $2,000-$3,000/デスク
- **スケーリングすればするほど赤字拡大**

**計算例**:
- 100デスク施設
- 月額テナント収入: $50,000（@$500/デスク）
- 月額リース代: $200,000（@$2,000/デスク）
- **月額赤字: -$150,000**

### 3.2 オキュパンシーレートの問題

**理想的な採算分岐点**: 80-90%の入居率
- しかしWeWorkは多くの施設で50-70%程度に止まる

**2019年の実績**:
- 平均入居率: 約60%
- 月額損失：数億ドル

### 3.3 競合による市場飽和

**IWG（Regus親会社）等の競合参入**:
- より低価格の提供
- より柔軟な契約条件
- WeWorkの価格プレミアムが正当化困難

## 4. Adam Neumann の私的利益優先行為

### 4.1 関連会社取引の不透明性

**不動産資産の買い漁り**:
- Neumannが個人所有で不動産を購入
- WeWorkに高額でリースバック
- WeWorkが赤字でも、Neumannは収益化

**具体例**:
- 2013-2019年: Neumannが複数の物件を購入
- WeWorkがリース代として高額支払い
- Neumannの個人資産は数十億ドルに増加

### 4.2 給与・特典の過剰支給

**CEO給与**:
- 2018年: $17M
- 2019年: 追加ボーナス数十万ドル

**個人的支出の会社補填**:
- 豪邸の購入（会社が融資を支援）
- プライベートジェットの利用
- ワイン・美術品の購入（会社アカウント）

### 4.3 投票権の不透合な支配

**ダブルクラス株構造の導入**:
- Neumannの個人株: 10票/株
- 他の投資家の株: 1票/株
- 少数株で絶対支配権を維持

**取締役会への支配**:
- 親友を取締役に任免
- 意思決定の透明性欠如
- 投資家への説明責任なし

## 5. IPO計画と急転直下の崩壊

### 5.1 IPO準備と華やかな宣伝（2019年初～中盤）

**IPO計画**:
- 2019年秋のNYSE上場目指す
- 目標調達額: $3-4B
- IPO後の評価額目標: $60-100B

**メディア戦略**:
- 「Steve Jobsの後継者」というポジショニング
- カリスマ経営者のイメージ構築
- WeWorkが「不動産革命」を起こすという物語

**Neumannの露出**:
- Fortune, Forbes, Bloomberg等の雑誌表紙
- TED Talkでの講演
- 「マインドフルネス」「社会的インパクト」を強調

### 5.2 S-1ファイリングと問題の顕在化（2019年8月）

**S-1提出（2019年8月14日）**:
- SEC（米証券取引委員会）に上場申請書を提出
- 初めて詳細な財務情報が公開

**メディア分析による問題指摘**:
- **The New York Times**: Neumannの不動産取引の詳細報道
- **Bloomberg**: 関連会社取引による過度な給与支給
- **The Wall Street Journal**: ガバナンス欠陥の指摘

**主要な懸念項目**:
1. **赤字幅の深刻性**
   - 2018年: -$1.4B損失
   - 2019年1H: -$900M損失
   - 黒字化の見通しなし

2. **関連会社取引**
   - Neumannが所有する不動産をWeWorkがリース
   - 妥当な市場価格を大幅に上回る
   - 2013-2019年: Neumannが個人的に数百万ドル追加収益

3. **ガバナンス問題**
   - ダブルクラス株で一人支配
   - 独立した取締役が少ない
   - 報酬委員会が機能していない

4. **ビジネスモデル懸念**
   - 不動産リース契約が固定費化
   - 経済不況時のリスク極度に高い
   - スケーリングによる黒字化の理論的根拠なし

### 5.3 IPO中止と権力喪失（2019年9月）

**2019年9月24日: IPO延期発表**
- WeWorkが突如IPO延期を発表
- 理由: 「市況判断」という表向きの説明
- 実際: 投資家からの質問攻撃に耐えられず

**投資家離反**:
- SoftBank Vision Fund: 追加投資を停止
- Benchmark等初期投資家: 徹底的な批判
- IPO関連企業（JP Morgan等）: サポート縮小

**Neumannへの圧力**:
- SoftBankのMasayoshi Son: 公開の場でNeumannを批判
- 「Neumannは経営者失格」との評価
- Neumannは自主的な辞任を示唆

**2019年9月26日: CEO辞任声明**
- Neumannが自発的にCEO辞任を表明
- 辞任パッケージ: $1.7B（給与、株式補償、家購入サポート等）

## 6. 辞任後の落ちぶれと返金要求

### 6.1 SoftBankによるバイアウト

**2019年10月: $3B追加投資予定の縮小**
- SoftBankが支援を大幅に削減
- WeWork従業員の20%（6,000人）削減開始
- 施設の大量閉鎖

**2019年11月: SoftBankがWeWork管財人に**
- SoftBankが事実上経営支配
- 新CEO Sandeep Mathrani着任
- Neumannは完全に権力喪失

### 6.2 Neumann辞任金の返還訴訟

**2021年: SoftBankがNeumannを訴訟**
- 辞任時に支払われた$1.7Bの返還要求
- 理由: 「詐欺的な関連会社取引」「ガバナンス違反」
- 和解額: 未公開（推定$500M以上の返金）

### 6.3 Neumann の現在

**2023年以降**:
- WeWorkの新CEO下で経営再建
- Neumannは返金交渉の傍ら、新規プロジェクト検討
- 著名VC投資家からは完全に敬遠

## 7. 失敗パターン分析

### 7.1 P22: ファウンダー問題・ガバナンス欠陥

**支配構造の問題**:
- ダブルクラス株（1:10の投票権差）
- 少数株での絶対支配
- 取締役会の独立性欠如

**私的利益優先**:
- 関連会社取引を通じた個人資産化
- CEO給与の過度な支給
- 企業資産の私物化

**透明性の欠如**:
- 重要な情報を隠蔽
- IPO S-1まで不動産リース取引の詳細が非公開
- 投資家への開示不足

### 7.2 P24: 過度な時価総額評価

**評価額の非合理性**:
- $47B評価額に見合う事業基盤なし
- アクティブユーザーあたりの収益が低い
- Airbnbと比較しても割高

**ユニコーン化による弊害**:
- メディアのヒーロー化
- 批判的検証の欠如
- 実績に基づかない評価

**IPO前評価の詐欺的性質**:
- 赤字ビジネスを「革新的企業」と宣伝
- 「世界中のオフィス」という幻想販売
- 実態：不動産スケーリングの失敗

### 7.3 P28: 過剰調達

**$15B調達の実態**:
- SoftBankのビジョン重視により無批判に投資
- Unit Economicsの検証なし
- 赤字を支援金で補填し続ける

**資金の使途**:
- 施設拡大（しかし黒字化道筋なし）
- 不動産リース契約（長期の負債化）
- Neumann個人への報酬・特典

## 8. なぜWeWorkは失敗したか

### 8.1 ビジネスモデルの根本的欠陥

**スケーリング不可能性**:
- 不動産リース：長期固定費
- テナント収入：変動的で不安定
- 大規模化 = 赤字拡大

**対比：成功した共有経済モデル**:
- **Airbnb**: ホスト中心、資産所有不要
- **Uber**: ドライバー中心、車両所有不要
- **WeWork**: 建物所有＋長期リース = 資本集約的

### 8.2 不動産市場への根本的誤解

**Neumannの仮説**:
- 「不動産市場を民主化する」「共有オフィスが標準化」
- 「WeWorkが全世界の不動産市場を支配」

**実態**:
- 企業は自社ビル又は安定した賃貸を選好
- 一時的な席貸しニーズは限定的
- 不動産オーナーも高額テナント（長期契約）を優先

### 8.3 COVID-19パンデミックの衝撃

**2020年以降の急変**:
- リモートワークの普及
- オフィス需要の激減
- 長期リース契約の足枷化

## 9. 被害者

### 9.1 従業員

**大量解雇**:
- 2019年: 6,000人削減（全体の20%）
- 2020年: 追加削減
- 解雇時点での給与未払い問題も

### 9.2 テナント企業

**サービス品質低下**:
- 施設閉鎖により移転費用負担
- 契約の突然の解除
- 返金なし

### 9.3 投資家

**総損失額: 推定$40B+**
- SoftBank Vision Fund: $7B以上投資、ほぼ全損
- Benchmark Capital: 初期投資家、返金活動実施中
- その他機関投資家: 数十億ドルの損失

### 9.4 不動産オーナー

**未払い・契約違反**:
- リース料金の支払い遅延
- 急な契約解除
- 空きスペースの処理

## 10. 教訓

### 10.1 ガバナンスの重要性

**投資家として**:
- ファウンダーの関連会社取引を詳細に検査
- ダブルクラス株構造の危険性を認識
- 独立取締役の機能を重視

**ファウンダーとして**:
- 透明性と説明責任が長期的信頼を築く
- 私的利益と会社利益の分離
- 倫理的リーダーシップが持続成長を可能にする

### 10.2 ビジネスモデルの検証

**資本集約的モデルの注意**:
- 長期固定費のリスク
- スケーリングの限界を理解
- Unit Economics（LTV/CAC）の計算

**テスト**: 「黒字化の見通しはあるか」
- WeWorkの場合: 不動産リース構造では本質的に黒字不可能
- 赤字ビジネスへの無限投資は警戒

### 10.3 メディア・ヒーロー化への警戒

**カリスマ経営者の危険性**:
- メディアのヒーロー化により批判が減少
- 技術的・財務的検証が軽視される
- タイムズ紙等による調査報道の重要性

**投資判断基準**:
- メディアの評判ではなく、実績ベース
- 専門家による技術的・財務的検証
- 親友取締役ではなく、独立した外部監査

### 10.4 企業文化と社会的インパクト

**「We」というブランドの欺瞞**:
- 「コミュニティ」「ウェルネス」を謳いながら
- ファウンダーによる支配と搾取
- 従業員・テナントへの背信

**本来のカルチャー**:
- 透明性と民主性が必須
- 長期的な関係構築を重視
- 短期利益より信頼を優先

## 11. 日本への示唆

**日本でのWeWork型詐欺リスク**:
- 不動産スタートアップの増加
- ガバナンスの形骸化（特にファミリービジネス）
- メディアのベンチャー企業ヒーロー化

**避けるべき警告サイン**:
- ファウンダーの個人資産が急増
- 関連会社取引が多い
- 透明性の欠如、情報隠蔽
- メディア露出の異常な多さ
- 赤字ビジネスへの無限投資

**チェックリスト**:
- [ ] ガバナンス構造は独立性を確保しているか？
- [ ] 関連会社取引は市場価格で透明化されているか？
- [ ] ビジネスモデルは黒字化の見通しあるか？
- [ ] 資本集約的モデルのリスクを理解しているか？
- [ ] メディア報道に依存していないか、実績をベースにしているか？

## 12. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2010年） | ✅ PASS | Wikipedia、Crunchbase |
| ピーク評価額（$47B） | ✅ PASS | WeWork S-1、Bloomberg、WSJ |
| 総調達額（$15B+） | ✅ PASS | Crunchbase、SoftBank公開情報 |
| IPO中止（2019年9月） | ✅ PASS | SEC、企業プレスリリース、NYT |
| CEO辞任（2019年9月26日） | ✅ PASS | 公式声明、Bloomberg |
| 辞任パッケージ（$1.7B） | ✅ PASS | SEC Filing、Bloomberg |
| 従業員削減（6,000人） | ✅ PASS | 公式発表、Bloomberg |
| Neumann個人資産形成 | ✅ PASS | NYT Investigation |
| ダブルクラス株構造 | ✅ PASS | S-1 Filing（SEC） |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 13. 参照ソース

1. [New York Times - The Man Behind WeWork](https://www.nytimes.com/2019/08/29/magazine/the-corner-office.html)
2. [Bloomberg - The Messy, Beautiful Disaster That is WeWork](https://www.bloomberg.com/features/2019-softbank-wework/)
3. [Wall Street Journal - WeWork's Stumble Shakes SoftBank](https://www.wsj.com/articles/wework-s-stumble-shakes-softbank-11568914202)
4. [SEC - The We Company S-1 Filing](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company_name=wework&type=&dateb=&owner=exclude&count=100)
5. [Wikipedia - WeWork](https://en.wikipedia.org/wiki/WeWork)
6. [Crunchbase - WeWork](https://www.crunchbase.com/organization/wework)
7. [Business Insider - The Rise and Fall of Adam Neumann](https://www.businessinsider.com/adam-neumann-wework-ceo-founder-2019-8)
8. [The Verge - WeWork IPO Collapse Timeline](https://www.theverge.com/2019/9/24/20881143/wework-ipo-delayed-adam-neumann)
9. [Financial Times - SoftBank's $47bn Bet on WeWork](https://www.ft.com/content/fa8f9c4a-84b8-11e9-a028-86cea8523dc2)
10. [CNBC - Adam Neumann Resignation Analysis](https://www.cnbc.com/2019/09/24/wework-ceo-adam-neumann-resigns.html)
11. [Axios - Neumann Severance Details](https://www.axios.com/adam-neumann-wework-severance-details-b0f5c9ac-d47c-46c8-a72f-ae63b0be92b5.html)
12. [TechCrunch - WeWork Restructuring](https://techcrunch.com/2019/09/24/wework-ipo-delayed/)
13. [Forbes - The Implosion of Adam Neumann's Ambitions](https://www.forbes.com/sites/parkehayes/2019/09/24/wework-delays-ipo/)
14. [Reuters - SoftBank Reduces WeWork Funding](https://www.reuters.com/article/us-wework-softbank-idUSKBN1WL3TM)
15. [Mashable - WeWork Corporate Culture Crisis](https://mashable.com/article/wework-culture-crisis)
16. [Quartz - Why WeWork Failed](https://qz.com/1698237/why-wework-failed-unit-economics-and-corporate-governance/)
17. [The Information - WeWork IPO Documents Reveal](https://www.theinformation.com/articles/softbanks-vision-fund-documents-reveal-concerns-about-wework)
18. [Harvard Business Review - The WeWork Debacle](https://hbr.org/2019/10/the-wework-debacle)

