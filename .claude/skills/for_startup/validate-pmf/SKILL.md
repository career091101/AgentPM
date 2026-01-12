---
name: validate-pmf
description: |

  ForStartup調整:
  - 外部顧客獲得基準: 100社/人以上（Series B Stage必須要件）
  - DAU/MAU、継続率、NPS: 起業の科学基準を維持
  - 収益化開始: 初期売上発生必須（3年黒字計画必須）

  使用タイミング：
  - Series A Stage突破後、外部顧客獲得段階
  - MVP稼働、初期顧客100社/人以上獲得後
  - Phase2（PMF検証）開始時

  所要時間：30-50分（アンケート設計含む）
  出力：PMF診断レポート、Series B Stage移行判定
trigger_keywords:
  - "PMF検証"
  - "PMF診断"
  - "Sean Ellisテスト"
  - "プロダクトマーケットフィット"
  - "PMF達成確認"
stage: planning
dependencies:
  - validate-psf（PSF達成が前提）
  - validate-ring-criteria（Series A Stage突破が前提）
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/pmf_diagnosis.md
execution_time: 30-50分
framework_reference: Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
priority: P0
framework_compliance: 100%
---

# Validate PMF Skill (ForStartup Edition)

起業の科学のPMF達成基準に基づき、4つの定量指標（Sean Ellisテスト、月次成長率、Churn Rate、NPS）で総合判定を行う自律実行型Skill（ForStartup特化版）。スタートアップのGrowth Stage基準に準拠し、外部顧客獲得100社/人以上を必須要件とする。

---

## このSkillでできること

1. **4指標統合評価**: Sean Ellisテスト、月次成長率、Churn Rate、NPSを一元判定
2. **Series B Stage基準準拠**: 外部顧客獲得100社/人以上、収益化開始、3年黒字計画を検証
3. **自動アンケート設計**: Sean Ellisテスト・NPSのアンケートテンプレート自動生成
4. **ボトルネック特定**: どの指標が不足しているか、改善アクションを提案
5. **Series B Stage移行判断**: 本格事業化へ進むか、改善すべきかを提示

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `psf_validation.md`, `ring_criteria_diagnosis.md`, 顧客データ, 利用ログ |
| **出力** | `Flow/{YYYYMM}/{YYYY-MM-DD}/pmf_diagnosis.md` |
| **次のSkill** | `/measure-aarrr` → `/build-approval-deck`（PMF達成時） |
| **ステージ** | Phase2（PMF検証）、Series B Stage段階 |

---

## Knowledge Base参照

- PMF概念: `startup_science/01_stages/pmf/pmf_overview.md`
- Sean Ellisテスト: `startup_science/01_stages/pmf/sean_ellis_test.md`
- 成長メトリクス: `startup_science/02_metrics/growth_metrics.md`
- Churn Rate: `startup_science/02_metrics/churn_rate.md`
- NPS: `startup_science/02_metrics/nps.md`

---

## Domain-Specific Knowledge (from Founder_Research)

### Success Patterns

**Tier 2 事例（成功事例）**

**1. Airレジ（PMF達成事例）**
- **外部顧客獲得**: 1年で10万店舗、3年で90.4万アカウント
- **DAU/MAU比率**: 推定40%以上（POSレジの日次利用率高い）
- **継続率**: 推定60%以上（1ヶ月）、Churn率10-15%
- **NPS**: 推定60-70（業界トップクラス）
- **収益化**: Airペイ連携で手数料収益、3年黒字達成

**2. Airペイ（PMF達成事例）**
- **外部顧客獲得**: 1年で20万店舗、3年で51.5万加盟店
- **クロスセル率**: Airレジから57%（業界標準5-15%の4-11倍）
- **継続率**: 推定60%以上、Churn率10%
- **NPS**: 推定70-80（決済手数料最安、サポート充実）
- **収益化**: 初年度売上5億円、3年黒字達成

**3. スタディサプリ（PMF達成事例）**
- **外部顧客獲得**: 初年度30万ユーザー、2年で100万人、5年で200万人
- **DAU/MAU比率**: 推定30-40%（月額サブスク、週3-4回学習）
- **継続率**: 推定50%以上（学習継続率）
- **NPS**: 推定60-70（教育効果実証、コストパフォーマンス）
- **収益化**: 初年度から黒字、3年黒字達成

**4. Geppo（PMF達成事例）**
- **外部顧客獲得**: 2年で300社（BtoB SaaS）
- **回答率**: 96%（競合50-70%の2倍）、DAU/MAU換算90%以上
- **継続率**: 98%（業界トップクラス）
- **NPS**: 推定70-80（人事部門評価、離職率改善効果実証）
- **収益化**: 初年度から黒字、3年黒字達成

---

**Tier 3 事例（VC-Backed Unicorn成功事例）**

**5. Notion（PMF達成事例 - Ivan Zhao）**
- **PMF達成プロセス**:
  - クローズドベータ（2015年、500人）→ Product Hunt #1（2016年3月、6,000アップボート）→ CVR 20%で年間プリオーダー獲得
  - 2019年時点で100万ユーザー到達、2024年時点で1億ユーザー突破
- **Sean Ellisテスト**: 推定50-70%（Product Huntコミュニティの熱狂的支持、"非常に残念"回答率が高い）
- **成長率**: 2019年ARR $3M → 2023年ARR $240M（4年で80倍成長、年平均成長率192%）
- **NPS**: 推定60-70（Wall Street Journal "The Only App You Need for Work-Life Productivity" 評価、コミュニティ主導の成長）
- **Unit Economics**:
  - Net Dollar Retention: 130%以上（推定、エンタープライズ拡大）
  - Churn率: 推定5-10%（個人無料版の離脱を除く）
  - LTV/CAC: 極めて高い（PLG戦略でCAC最小化、無料版→有料版転換が自然発生）
- **PMF達成の転機**: Product Hunt 1.0ローンチ（2016年3月）→ #1 Product of the Day/Week/Month獲得、CVR 20%が初期PMF証明
- **収益化**: 2020年5月フリーミアム導入後、個人無料→エンタープライズ有料（$10-20/月）で急成長、2024年ARR $400M達成
- **出典**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/02_Unicorn/FOUNDER_052_ivan_zhao.md

**6. Figma（PMF達成事例 - Dylan Field）**
- **PMF達成プロセス**:
  - クローズドベータ（2015年12月、個別デモセッション）→ パブリックローンチ（2016年）→ Freemiumモデルで急速普及
  - 2018年時点で3,000+顧客、2024年時点でMAU 13M、総ユーザー4M+
- **Sean Ellisテスト**: 推定55-75%（Design Tools Survey 2022でUIデザイン市場シェア77%達成、業界標準化）
- **成長率**: 2020年ARR推定$200M → 2024年ARR $1B（4年で5倍成長、年平均成長率58%）
- **NPS**: 推定70-80（2022年Adobe買収提案$20B、協業スピード60倍改善が高評価）
- **Unit Economics**:
  - Net Dollar Retention: 132%（2024年実績）
  - Gross Margin: 88.3%（2024年実績）
  - $100K+ ARR顧客: 1,031社（前年比47%成長）
  - Average Contract Value (ACV): 推定$18,000-20,000/年
  - Churn率: 推定3-5%（協業ツールとしての高い定着率）
- **PMF達成の転機**: 2016年パブリックローンチ後、リモートチーム・スタートアップでの急速普及、2018年にエンタープライズ顧客獲得開始（Microsoft、Slack、GitHub等）
- **収益化**: Freemiumモデル（無料版で3ファイル制限、有料版$12-75/editor/月）、2024年売上$749M（前年比48%成長）
- **出典**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_190_dylan_field.md

**7. Databricks（PMF達成事例 - Ali Ghodsi, Ion Stoica, Matei Zaharia）**
- **PMF達成プロセス**:
  - オープンソースApache Spark（2009-2015年、コミュニティ構築）→ エンタープライズピボット（2016年Ali Ghodsi CEO就任）→ 初期顧客獲得（Shell, HP, Salesforce）
  - 2015年売上$1.6M → 2016年エンタープライズ営業転換 → 2018年3,000+顧客 → 2023年10,000+顧客
- **Sean Ellisテスト**: 推定60-80%（Fortune 500の60%以上が顧客、エンタープライズ標準化）
- **成長率**: 2019年ARR推定$200M → 2025年Revenue Run-Rate $4.8B（6年で24倍成長、年平均成長率92%）
- **NPS**: 推定70-85（Apache Spark創始者チームによる公式マネージドサービス、Lakehouseアーキテクチャ革新）
- **Unit Economics**:
  - Net Dollar Retention: 140%+（既存顧客が毎年40%以上支出増）
  - Average Contract Value (ACV): $209,000/年
  - $1M+ ARR顧客: 650+社
  - Gross Margin: 推定75-80%（SaaS標準）
  - Churn率: 推定3-5%（エンタープライズ長期契約）
- **PMF達成の転機**: 2016年Ali GhodsiのCEO就任とエンタープライズピボット → Shell, HP, Salesforce等の大型顧客獲得 → 2020年Lakehouseアーキテクチャ発表で市場リーダー化
- **収益化**: マネージドSpark（AWS, Azure, GCP）、エンタープライズ年次契約、2025年Revenue Run-Rate $4.8B（55% YoY成長）
- **出典**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/FOUNDER_193_ali_ghodsi.md

### Common Pitfalls

**失敗パターン1: 外部顧客獲得失敗（社内実証のみ）**
- **エリクラ**: 6年間実証実験レベル継続、外部ユーザー10万人（目標1,000万人未達）→ 撤退

**失敗パターン2: DAU/MAU低迷**
- **エリクラ**: DAU/MAU推定10%未満（競合タイミー30%以上）
- **教訓**: エンゲージメント低迷はPMF未達成の明確なサイン、ユーザー定着施策強化

**失敗パターン3: 収益化失敗**
- **スタディサプリ個別指導**: 月額10,780円では講師人件費を賄えず、1.5年で撤退
- **教訓**: Unit Economics健全性（LTV/CAC 5.0以上）を厳守、収益性犠牲の成長は持続しない

### Quantitative Benchmarks

**外部顧客獲得**:
- Series B Stage基準: **100社/人以上**（業種による）
- Tier 2ベンチマーク: Airレジ1年10万店舗、Airペイ1年20万店舗、スタディサプリ初年度30万人、Geppo 2年300社
- Tier 3ベンチマーク（VC-Backed）: Notion 2019年100万人、Figma 2018年3,000+顧客、Databricks 2018年3,000+顧客

**Sean Ellisテスト**:
- 基準: **40%以上**（起業の科学準拠）
- Tier 2ベンチマーク: 推定40-50%（Airレジ、Airペイ、スタディサプリ、Geppo）
- Tier 3ベンチマーク: Notion 50-70%、Figma 55-75%、Databricks 60-80%

**月次成長率**:
- 基準: **10%/月以上**（起業の科学準拠）
- Tier 2ベンチマーク: 推定10-20%/月
- Tier 3ベンチマーク:
  - Notion: 年平均成長率192%（2019-2023年、ARR $3M→$240M）
  - Figma: 年平均成長率58%（2020-2024年、ARR $200M→$1B）
  - Databricks: 年平均成長率92%（2019-2025年、ARR $200M→$4.8B）

**DAU/MAU比率**:
- 基準: **30%以上**（起業の科学準拠）
- Tier 2ベンチマーク: Airレジ40%、スタディサプリ30-40%、Geppo 90%以上（回答率96%）
- Tier 3ベンチマーク: Figma MAU 13M（2024年、高エンゲージメント）

**継続率（1ヶ月）/ Churn率**:
- 基準: **継続率40%以上 / Churn率5%/月以下**（起業の科学準拠）
- Tier 2ベンチマーク: Airレジ継続率60%（Churn率10-15%）、Airペイ継続率60%（Churn率10%）、Geppo継続率98%（Churn率2%）
- Tier 3ベンチマーク: Notion Churn率5-10%、Figma Churn率3-5%、Databricks Churn率3-5%

**NPS**:
- 基準: **50以上**（起業の科学準拠）
- Tier 2ベンチマーク: Airレジ60-70、Airペイ70-80、スタディサプリ60-70、Geppo 70-80
- Tier 3ベンチマーク: Notion 60-70、Figma 70-80、Databricks 70-85

**Net Dollar Retention (NDR)**:
- VC投資基準: **120%以上**（既存顧客が毎年20%以上支出増）
- Tier 3ベンチマーク:
  - Notion: 130%以上（推定）
  - Figma: 132%（2024年実績）
  - Databricks: 140%+（2025年実績）

**収益化**:
- Series B Stage基準: **初期売上発生**（黒字化不要、3年黒字計画必須）
- Tier 2ベンチマーク: Airレジ・Airペイ・スタディサプリ・Geppo すべて初年度から売上発生、3年黒字達成
- Tier 3ベンチマーク:
  - Notion: 2020年フリーミアム導入後急成長、2024年ARR $400M
  - Figma: Freemiumモデル、2024年売上$749M（前年比48%成長）
  - Databricks: 2015年$1.6M → 2025年Revenue Run-Rate $4.8B（55% YoY成長）

### Best Practices

**Tier 2ベストプラクティス（成功事例）**

1. **外部顧客獲得の加速**: ホットペッパーグルメ2,000名営業網活用 → Airレジ1年10万店舗、CAC 1-2万円（競合の1/5〜1/10）
2. **クロスセル戦略**: Airレジ90.4万 → Airペイ51.5万、クロスセル率57%（業界標準5-15%の4-11倍）
3. **エンゲージメント最大化**: Geppo回答負荷10倍削減（30分→3分）→ 回答率96%、継続率98%
4. **Unit Economics健全性**: LTV/CAC 10-30倍（Airレジ15-30倍、Geppo 20倍）、Churn率10-15%以下

---

**Tier 3ベストプラクティス（VC-Backed Unicorn成功事例）**

**PMF達成プロセスの最適化**:

5. **クローズドベータでの徹底検証**:
   - **Notion**: Reddit型パワーユーザー500人を招待、6週間で厳しいフィードバック収集 → Product Hunt #1獲得、CVR 20%
   - **Figma**: 個別デモセッション実施、ユーザーの使用様子を直接観察 → 課題の本質的理解
   - **Databricks**: Apache Sparkコミュニティからの30社以上POC実施 → エンタープライズ顧客獲得

6. **Product-Led Growth (PLG) 戦略**:
   - **Notion**: 個人無料版で価値体験 → 職場に持ち込み → エンタープライズ有料化（Land and Expand）
   - **Figma**: Freemiumモデル（無料版で3ファイル制限）→ 自然な有料転換 → 2024年MAU 13M、総ユーザー4M+
   - **Databricks**: オープンソースApache Sparkでコミュニティ構築 → マネージドサービスへの需要創出 → エンタープライズ営業

7. **コミュニティ駆動の成長**:
   - **Notion**: 公式コミュニティを作らず、ユーザーが自発的にファンサイト・テンプレート作成 → Ben Lang（月間80,000ヒット）を採用
   - **Figma**: Design Tools Survey 2022でUIデザイン市場シェア77%達成 → 業界標準化
   - **Databricks**: Apache Spark創始者チームという信頼性 → Fortune 500の60%以上が顧客

8. **エンタープライズピボットの成功**:
   - **Databricks**: 2015年売上$1.6Mでトラクション不足 → 2016年Ali GhodsiのCEO就任、エンタープライズ営業へ転換 → 2025年Revenue Run-Rate $4.8B
   - **Figma**: 2016年パブリックローンチ後、個人ユーザー → 2018年エンタープライズ顧客獲得（Microsoft、Slack、GitHub等）→ 2024年ARR $1B

9. **Net Dollar Retention (NDR) 最大化**:
   - **Notion**: 130%以上（エンタープライズ拡大）
   - **Figma**: 132%（2024年実績、$100K+ ARR顧客1,031社）
   - **Databricks**: 140%+（既存顧客が毎年40%以上支出増、$1M+ ARR顧客650+社）
   - **戦略**: 既存顧客へのアップセル・クロスセル重視、新規獲得コスト削減

### Reference

- 個別事例: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/` `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/`

---

## Tier 3B: PMF失敗事例（ForStartup特化）

ForStartupの厳格な検証基準（VC投資水準）に照らして、PMF未達成により撤退・解散した事例を分析。投資家・起業家が見逃したPMF失敗のシグナルを明確化し、validate-pmf実行時の判断精度を向上させる。

### 失敗事例1: Theranos（P16+P23+P28 - 詐欺・規制失敗）

#### 事例概要
- **企業名**: Theranos（Elizabeth Holmes創業、2003年設立）
- **事業内容**: 血液検査デバイス"Edison"（指先採血で200以上の検査項目、従来の1/1000の血液量、1/10のコスト）
- **失敗の経緯**: 技術が存在しないのに$700M+調達 → 2015年Wall Street Journal暴露 → 2018年解散 → 2022年Holmes有罪判決（禁固11年3ヶ月）
- **結果**: ピーク評価額$9B → 清算価値$0、投資家損失$700M+、従業員800名解雇

#### PMF失敗の詳細

**なぜPMFを達成できなかったのか**:

1. **技術が存在しなかった（P23: 品質問題・詐欺）**:
   - Edisonは機能せず、検査の大部分は従来の商用機器（Siemens等）で実施
   - 血液を希釈して検査し、不正確な結果を患者に提供（健康被害）
   - デモは事前に仕込まれ、投資家・メディアに虚偽説明

2. **規制未遵守（P16: 規制・法的問題）**:
   - FDA承認なし、CLIA（臨床検査改善法）違反
   - 患者データ改ざん、検査品質管理不足
   - 2016年CMS査察で患者健康リスク発見 → 検査センター閉鎖命令

3. **過剰調達による虚偽の信頼性（P28: Death by Overfunding）**:
   - $700M+調達、著名投資家（Rupert Murdoch $125M、Larry Ellison、Walgreens $140M）の盲信
   - 技術検証なし、ビジョンのみで調達継続
   - 評価額$9Bは実態なし、メディアのヒーロー化が批判的検証を阻害

#### 定量データ（PMF未達成の証拠）

| 指標 | PMF達成基準（ForStartup） | Theranos実績 | 判定 |
|------|-------------------------|-------------|:----:|
| **技術的実証** | プロトタイプ動作 + 臨床試験データ | Edison機能せず、データ改ざん | ❌ |
| **外部顧客獲得** | 100社/人以上 | Walgreens 40店舗のみ（技術は偽装） | ❌ |
| **Sean Ellisテスト** | 40%以上 | 実施不可能（技術不在） | ❌ |
| **規制承認** | FDA承認必須（医療機器） | 未承認、CLIA違反 | ❌ |
| **継続率** | 40%以上（1ヶ月） | データなし（検査結果不正） | ❌ |
| **NPS** | 50以上 | 測定不可能 | ❌ |
| **収益化** | 初期売上発生 | Walgreens提携（$140M投資）だが技術偽装 | ❌ |

**刑事責任**:
- 2018年6月DOJ起訴（通信詐欺9件、共謀2件）
- 2022年1月有罪判決（投資家詐欺4件）
- 量刑: 禁固11年3ヶ月、2023年5月収監

#### 失敗パターン詳細

**P16（規制・法的問題）**:
- FDA承認なし → 医療機器として使用禁止
- CLIA違反 → 検査品質管理不足、患者データ改ざん
- 刑事責任 → 投資家・患者を欺いた詐欺罪

**P23（品質問題・詐欺）**:
- 技術が存在しない → Edison機能せず、従来機器で代替
- 患者への健康被害 → 不正確な検査結果、誤診の可能性
- 組織的隠蔽 → 従業員NDA、内部告発者への法的脅迫

**P28（過剰調達）**:
- $700M+調達 → 技術検証なし、著名投資家の盲信
- 評価額$9B → 実態なし、メディアヒーロー化
- 調達資金の使途 → 豪華オフィス、弁護士費用（告発者圧力）

#### ForStartupへの教訓

1. **技術的検証の重要性**:
   - ビジョンだけでは不十分、プロトタイプ動作確認必須
   - 独立した専門家による検証、査読論文の有無確認
   - 医療分野では臨床試験データが必須

2. **規制遵守の厳守**:
   - 医療・金融分野では規制ショートカット不可
   - "Move fast and break things"は患者安全では通用しない
   - FDA承認、CLIA遵守が最優先

3. **投資家デューディリジェンスの強化**:
   - 著名投資家の盲信は危険、技術的検証を独自実施
   - 秘密主義（技術非公開、査読論文なし）は警告サイン
   - 内部告発者への圧力は詐欺の兆候

4. **PMF検証の厳格化**:
   - 外部顧客獲得100社/人以上 → Theranosは40店舗のみ（技術偽装）
   - Sean Ellisテスト40%以上 → 実施不可能（技術不在）
   - 収益化開始 → Walgreens提携は虚偽、実質収益ゼロ

**出典**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/07_Failure_Study/FAILURE_014_theranos.md

---

### 失敗事例2: CODE.SCORE（PMF未達 - リクルート撤退事例）

#### 事例概要
- **企業名**: リクルートキャリア（Recruit Career）
- **製品名**: CODE.SCORE（コードスコア）
- **事業内容**: ITエンジニアの実務スキル可視化サービス（コーディングテスト + ピープルアナリティクス）、法人向けB2B SaaS
- **失敗の経緯**: 2015年ローンチ（Yahoo! JAPAN導入）→ 2017年撤退判断（3年単月黒字未達）→ 2018年3月31日サービス終了
- **結果**: サービス期間約3年、推定顧客50-100社、推定売上1.5億円、完全撤退（代替サービスなし）

#### PMF失敗の詳細

**なぜPMFを達成できなかったのか**:

1. **競合優位性の欠如（2-3倍優位性のみ、10倍なし）**:
   - 差別化ポイント: ピープルアナリティクス統合（3倍）、テスト網羅性（2倍）
   - 競合: paiza（無料）、Track/Codility（低価格）が台頭
   - 企業は単発スキル評価で十分と判断、継続的育成プラットフォームまで求めず

2. **3年単月黒字未達成（リクルート撤退基準）**:
   - 2015年ローンチ → 2017年9月撤退判断 → 2018年3月終了
   - 成長鈍化明確化（月次成長率5-10% → 5%未満）
   - LTV/CAC = 1.2（健全基準3.0未達）、月次Churn率20%（基準5%超過）

3. **市場タイミングのミスマッチ**:
   - 2015年当時はエンジニアスキル評価市場の黎明期
   - 無料サービス（paiza）の普及により有料B2Bモデルが成立しづらい市場に変化
   - 企業の価格感度が高く、「あったら便利」レベル（緊急性スコア7/10）では予算削減時に切られる

#### 定量データ（PMF未達成の証拠）

| 指標 | PMF達成基準（ForStartup） | CODE.SCORE実績 | 判定 |
|------|-------------------------|---------------|:----:|
| **外部顧客獲得** | 100社/人以上 | 推定50-100社 | ⚠️/❌ |
| **Sean Ellisテスト** | 40%以上 | データなし | - |
| **月次成長率** | 10%/月以上 | 5-10% → 5%未満（成長鈍化） | ❌ |
| **Churn Rate** | 5%/月以下 | 推定20%/月 | ❌ |
| **NPS** | 50以上 | データなし | - |
| **収益化** | 初期売上発生 | 2015年度3,000万円、2017年度1.5億円 | ⚠️ |
| **3年黒字計画** | 策定済み | 未達成（営業利益率-20%） | ❌ |
| **LTV/CAC** | ≥ 3.0 | 1.2（ARPU 25万円、CAC 100万円、継続4ヶ月） | ❌ |
| **NRR** | ≥ 100% | 80%（既存顧客の支出減） | ❌ |

**撤退判断の根拠**:
- リクルートの厳格な撤退基準「3年単月黒字」を2018年時点で未達成
- 2017年9月26日公式発表、2018年3月31日終了

#### 失敗パターン詳細

**CPF段階の見逃したシグナル**:
- 企業ニーズは存在したが、「絶対必要」ではなく「あったら便利」レベル
- 緊急性スコア7/10では不足、予算削減時に真っ先に切られる
- 無料代替案（paiza）が存在する市場で、支払い意思（WTP）確認が不十分

**PSF/PMF段階の見逃したシグナル**:
- 2-3倍優位性では無料競合に勝てず（10倍優位性が必須）
- ピープルアナリティクス機能も企業の内製化が進み、差別化が薄れた
- 継続率が低い（月次Churn率20%）→ 1回きりのスキル評価では継続的価値なし

**スケール段階の見逃したシグナル**:
- CAC高騰（100万円）、LTV低迷（120万円）→ LTV/CAC = 1.2
- Yahoo! JAPAN（大手）の成功が中小企業に再現できず
- NRR 80%（既存顧客の支出減）→ アップセル・クロスセル失敗

#### ForStartupへの教訓

1. **無料競合市場での10倍優位性必須**:
   - paiza（無料）vs CODE.SCORE（有料）の市場では、2-3倍優位性では不足
   - 有料化するには、コスト10倍削減 or 機能10倍向上 が必要
   - ピープルアナリティクス（3倍）だけでは価格差を正当化できず

2. **B2B SaaSは継続率（NRR 100%以上）が必須**:
   - 1回きりのスキル評価サービスでは継続的価値なし
   - 継続的育成・配置プラットフォームへの進化が必要だった
   - 月次Churn率20%では、新規獲得で穴埋め不可能

3. **リクルート撤退基準の厳格性が損失拡大を防ぐ**:
   - 3年単月黒字基準により早期撤退、5年累損解消まで引きずらず
   - 成長鈍化を2年目で検知 → 3年目で撤退判断 → 適切なタイミング
   - VC投資のスタートアップも同様の基準（1-2年でPMF判断）を持つべき

4. **CPF検証での緊急性（3U検証）の重要性**:
   - Unworkable（解決不可能）: △ 手動評価では限界だが、代替手段あり
   - Unavoidable（避けられない）: △ 重要だが他の方法でも対処可能
   - Urgent（緊急性）: △ Nice-to-haveレベルでは不足
   - 3Uすべて✅でなければ、PMF達成困難

5. **ForStartup Benchmark比較の厳格化**:
   - 外部顧客獲得: Airレジ1年10万店舗 vs CODE.SCORE 3年50-100社（200-2000倍の差）
   - Churn率: Geppo 2% vs CODE.SCORE 20%（10倍の差）
   - NRR: Figma 132% vs CODE.SCORE 80%（健全vs不健全の明確な差）

**出典**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/WITHDRAWN/CODE.SCORE.md

---

### Tier 3B 失敗事例のPMF診断への活用方法

#### validate-pmf実行時のチェックリスト（失敗回避）

**Theranos型失敗の回避**:
- [ ] 技術的実証完了（プロトタイプ動作 + 第三者検証）
- [ ] 規制遵守確認（医療・金融分野ではFDA/金融庁承認必須）
- [ ] 査読論文・臨床試験データ存在
- [ ] 秘密主義でない（技術公開、内部告発者保護）
- [ ] 投資家の技術的デューディリジェンス実施済み

**CODE.SCORE型失敗の回避**:
- [ ] 無料競合市場では10倍優位性必須（2-3倍では不足）
- [ ] 継続率検証（NRR ≥ 100%、月次Churn ≤ 5%）
- [ ] 緊急性確認（3U検証で「Urgent」が✅）
- [ ] LTV/CAC ≥ 3.0達成（健全なUnit Economics）
- [ ] 大手1社の成功が中小企業に再現可能か検証済み

#### 撤退判断の明確化（ForStartup基準）

| 指標 | 撤退判断基準 | Theranos | CODE.SCORE | あなたのプロジェクト |
|------|------------|----------|-----------|-----------------|
| 技術的実証 | プロトタイプ未動作 | ❌（技術不在） | ✅（技術は動作） | - |
| 外部顧客獲得 | < 50社/人 | ❌（40店舗、偽装） | ⚠️（50-100社） | - |
| 月次成長率 | < 5%/月（3ヶ月連続） | - | ❌（5%未満） | - |
| Churn率 | > 10%/月（3ヶ月連続） | - | ❌（20%/月） | - |
| LTV/CAC | < 1.5 | - | ❌（1.2） | - |
| 3年単月黒字 | 未達成 | ❌（詐欺） | ❌（未達成） | - |
| 規制違反 | FDA/CLIA違反 | ❌（未承認） | - | - |

**判定ロジック**:
- 上記6指標のうち2つ以上❌ → 即座に撤退検討（`/pivot-decision`実行）
- Theranos型（技術不在 + 規制違反）→ 即座に撤退（倫理的責任）
- CODE.SCORE型（3年黒字未達）→ Pivot or 撤退（リクルート基準適用）

---

### Reference（Tier 3B失敗事例）

- Theranos詳細: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/07_Failure_Study/FAILURE_014_theranos.md
- CODE.SCORE詳細: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/WITHDRAWN/CODE.SCORE.md
- 失敗パターン体系: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#failure-patterns

---

## PMF達成基準（ForStartup版）

### 4指標の定義と目標値

| 指標 | 目標値 | 測定方法 | 最低サンプル数 | ForStartup調整 |
|------|--------|----------|---------------|---------------|
| **外部顧客獲得** | **100社/人以上** | 社外顧客数（早期顧客除外） | Series B Stage必須 | **新規追加** |
| **Sean Ellisテスト** | 40%以上 | 「もう使えなくなったら非常に残念」回答率 | 40人以上 | 起業の科学準拠 |
| **月次成長率** | 10%/月以上 | MRR/MAU/トランザクション数の3ヶ月移動平均 | 3ヶ月データ | 起業の科学準拠 |
| **Churn Rate** | 5%/月以下 | 解約率（30日非アクティブ定義） | 3ヶ月データ | 起業の科学準拠 |
| **NPS** | 50以上 | Net Promoter Score（Promoter% - Detractor%） | 40人以上 | 起業の科学準拠 |
| **収益化開始** | 初期売上発生 | 初年度売上発生（黒字化不要） | Series B Stage必須 | **新規追加** |
| **3年黒字計画** | 策定済み | 定量的ロードマップ | Series B Stage必須 | **新規追加** |

### 総合判定基準

| 判定 | 条件 | 次のアクション |
|------|------|---------------|
| ✅ **PMF達成（Series B Stage承認可）** | 外部顧客100社/人以上 + 4指標すべて✅ + 収益化開始 + 3年黒字計画 | 本格事業化（役員承認申請） |
| ⚠️ **要改善** | 外部顧客100社/人以上 + 2-3指標✅ | 改善後に再診断（1-2ヶ月以内） |
| ❌ **PMF未達成** | 外部顧客100社/人未満 OR 0-1指標✅ | Pivot検討（`/pivot-decision`） |

---

## Instructions

### 自動実行フロー

#### STEP 1: 前提条件確認

**必須条件チェック**:
- [ ] PSF達成済み（`/validate-psf` 完了）
- [ ] Series A Stage突破済み（`/validate-ring-criteria` Series A Stage承認可）
- [ ] MVP稼働中（実プロダクトが動作している）
- [ ] **外部顧客100社/人以上獲得**（早期顧客除外）
- [ ] 直近3ヶ月の利用データ存在
- [ ] **収益化開始**（初期売上発生）
- [ ] **3年黒字・5年累損解消計画策定済み**

**データソース確認**:
- PSF検証結果: `Flow/{YYYYMM}/{YYYY-MM-DD}/psf_validation.md`
- Series A Stage診断結果: `Flow/{YYYYMM}/{YYYY-MM-DD}/ring_criteria_diagnosis.md`
- 顧客データベース: 外部顧客数、活動状況
- 利用ログ: 継続率、解約率データ
- アンケート結果: 既存のフィードバック
- 収益データ: 初期売上発生状況
- 3年黒字計画: ロードマップ文書

**前提条件未達成時の対応**:
- 外部顧客100社/人未満 → 「Series B Stage基準未達、外部顧客100社/人以上獲得が必須です」と通知
- MVP未稼働 → 「MVPをリリースして外部顧客を獲得してください」と通知
- PSF未達成 → 「先に `/validate-psf` でPSF達成を確認してください」と通知
- Series A Stage未突破 → 「先に `/validate-ring-criteria` でSeries A Stage承認を確認してください」と通知
- 収益化未開始 → 「Series B Stage基準未達、初期売上発生が必須です」と通知
- 3年黒字計画未策定 → 「Series B Stage基準未達、3年黒字・5年累損解消計画策定が必須です」と通知

---

#### STEP 2: 外部顧客獲得数検証

**外部顧客定義**:
- **社外顧客のみカウント**（早期顧客、グループ会社顧客は除外）
- **アクティブ顧客のみカウント**（過去30日間に利用実績あり）
- **有料顧客優先**（無料トライアルのみは除外、または別枠カウント）

**検証方法**:
```markdown
## 外部顧客獲得数検証

### 顧客セグメント分類

| セグメント | 顧客数 | カウント | 備考 |
|----------|-------|---------|------|
| 外部顧客（有料） | XX社/人 | ✅ | Series B Stage基準カウント対象 |
| 外部顧客（無料トライアル） | XX社/人 | ⚠️ | 別枠参考値 |
| 早期顧客 | XX社/人 | ❌ | 除外 |
| グループ会社顧客 | XX社/人 | ❌ | 除外 |
| **外部顧客合計** | **XX社/人** | - | Series B Stage基準: 100社/人以上 |

### 判定

- ≥ 100社/人 → ✅ 合格（Series B Stage基準達成）
- 50-99社/人 → ⚠️ 要加速（あと少しで達成）
- < 50社/人 → ❌ 不合格（外部スケール不足）
```

**ベンチマーク比較**:
- Airレジ: 1年で10万店舗（外部顧客）
- Airペイ: 1年で20万店舗（外部顧客）
- スタディサプリ: 初年度30万人（外部顧客）
- Geppo: 2年で300社（外部顧客、BtoB）

---

#### STEP 3: Sean Ellisテスト実施

（起業の科学準拠、Origin版と同一）

**アンケート設計**:

```markdown
## Sean Ellisテスト（PMF測定）

**質問**: もし[プロダクト名]が使えなくなったら、どう思いますか？

- [ ] 非常に残念
- [ ] 少し残念
- [ ] 残念ではない（代替品を探す）
- [ ] よくわからない（ほとんど使っていない）

**フォローアップ質問**（オプション）:
- 最も価値を感じている機能は何ですか？
- どんな人に薦めたいですか？
```

**配信方法**:
- メール/アプリ内通知で全アクティブユーザーに配信
- 回答期限: 1週間
- リマインダー: 3日後、6日後

**集計・分析**:
- 「非常に残念」回答数 / 有効回答数 × 100 = XX%
- 有効回答数: 最低40人（理想は50人以上）
- 「よくわからない」は分母から除外

**判定**:
- ≥ 40% → ✅ 合格（PMF達成の兆候）
- 30-39% → ⚠️ 要改善（もう少しで達成）
- < 30% → ❌ 不合格（PMF未達成）

---

#### STEP 4: 月次成長率計算

（起業の科学準拠、Origin版と同一）

**指標選択**（ビジネスモデルに応じて選択）:

| ビジネスモデル | 主要指標 | 計算式 |
|-------------|---------|-------|
| SaaS | MRR（月次経常収益） | (今月MRR - 先月MRR) / 先月MRR × 100 |
| コンシューマー | MAU（月間アクティブユーザー） | (今月MAU - 先月MAU) / 先月MAU × 100 |
| マーケットプレイス | GMV（取引総額） | (今月GMV - 先月GMV) / 先月GMV × 100 |

**データ取得**:
- 直近3ヶ月のデータを取得
- 例: 10月、11月、12月のMRR/MAU/GMV

**3ヶ月移動平均計算**:
```
10月→11月の成長率: (11月 - 10月) / 10月 × 100 = X%
11月→12月の成長率: (12月 - 11月) / 11月 × 100 = Y%
平均成長率: (X + Y) / 2 = Z%
```

**トレンド分析**:
- 加速傾向: X% < Y% → ✅ ポジティブ
- 横ばい: X% ≈ Y% → ⚠️ 注意
- 減速傾向: X% > Y% → ❌ ネガティブ

**判定**:
- ≥ 10%/月 → ✅ 合格（健全な成長）
- 5-9%/月 → ⚠️ 要改善（やや遅い）
- < 5%/月 → ❌ 不合格（成長不足）

---

#### STEP 5: Churn Rate測定

（起業の科学準拠、Origin版と同一）

**解約定義**（プロダクトに応じて選択）:

| プロダクト種類 | 解約定義 | 基準 |
|-------------|---------|------|
| SaaS（有料） | 契約解除 | 明示的なキャンセル |
| Freemium | 30日間非アクティブ | ログイン・利用なし |
| アプリ | アンインストール | アプリ削除 |

**Cohort分析**（推奨手法）:

```markdown
## Cohort別Churn Rate

| 登録月 | 初月残存 | 3ヶ月残存 | 6ヶ月残存 | Churn Rate（月次） |
|-------|---------|-----------|-----------|------------------|
| 10月 | 100人 | 85人 | 75人 | 約5%/月 |
| 11月 | 120人 | 110人 | - | 約4%/月 |
| 12月 | 150人 | - | - | データ不足 |
```

**計算式**:
```
月次Churn Rate = (月初顧客数 - 月末顧客数) / 月初顧客数 × 100
```

**3ヶ月平均Churn Rate**:
- 10月、11月、12月のChurn Rateを平均

**判定**:
- ≤ 5%/月 → ✅ 合格（B2B基準）
- ≤ 7%/月 → ✅ 合格（B2C基準）
- 6-10%/月 → ⚠️ 要改善（やや高い）
- > 10%/月 → ❌ 不合格（離脱が多すぎ）

**ForStartup Benchmark**:
- Airレジ: 推定Churn率10-15%
- Airペイ: 推定Churn率10%
- Geppo: 継続率98%（Churn率2%）

---

#### STEP 6: NPS測定

（起業の科学準拠、Origin版と同一）

**アンケート設計**:

```markdown
## NPS調査

**質問**: [プロダクト名]を友人や同僚に薦める可能性はどのくらいですか？（0-10点）

0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10
絶対薦めない           どちらでもない           絶対薦める

**フォローアップ質問**:
- その理由を教えてください（自由記述）
```

**配信方法**:
- Sean Ellisテストと同時配信可能
- 回答期限: 1週間

**分類・計算**:

| スコア | 分類 | 意味 |
|-------|------|------|
| 9-10点 | Promoter（推奨者） | 熱烈なファン |
| 7-8点 | Passive（中立者） | 満足しているが受動的 |
| 0-6点 | Detractor（批判者） | 不満を持っている |

```
NPS = (Promoter数 / 総回答数 × 100) - (Detractor数 / 総回答数 × 100)

例: 100人中、Promoter 60人、Passive 30人、Detractor 10人
NPS = (60/100 × 100) - (10/100 × 100) = 60 - 10 = 50
```

**判定**:
- ≥ 50 → ✅ 合格（優良スコア）
- 30-49 → ⚠️ 要改善（平均的）
- < 30 → ❌ 不合格（改善必須）

**ForStartup Benchmark**:
- Airレジ: 推定NPS 60-70
- Airペイ: 推定NPS 70-80
- スタディサプリ: 推定NPS 60-70
- Geppo: 推定NPS 70-80

---

#### STEP 7: 収益化・3年黒字計画検証

**収益化検証**:

```markdown
## 収益化状況

### 初期売上発生

| 項目 | 状況 | 金額 |
|-----|------|------|
| 初年度売上 | [発生 / 未発生] | [XX億円] |
| 収益化開始月 | [YYYY-MM] | - |
| 主要収益源 | [サブスク / 手数料 / 広告 等] | - |

### 判定

- 初期売上発生 → ✅ 合格（Series B Stage基準達成）
- 初期売上未発生 → ❌ 不合格（収益化必須）
```

**3年黒字計画検証**:

```markdown
## 3年黒字・5年累損解消計画

### 定量的ロードマップ

| 年次 | 売上 | コスト | 営業利益 | 累損 | 判定 |
|-----|------|-------|---------|------|------|
| 1年目 | XX億円 | XX億円 | ▲XX億円 | ▲XX億円 | - |
| 2年目 | XX億円 | XX億円 | ▲XX億円 | ▲XX億円 | - |
| 3年目 | XX億円 | XX億円 | **XX億円** | ▲XX億円 | 単月黒字達成 ✅ |
| 4年目 | XX億円 | XX億円 | XX億円 | ▲XX億円 | - |
| 5年目 | XX億円 | XX億円 | XX億円 | **0円** | 累損解消 ✅ |

### 判定

- 3年黒字・5年累損解消計画策定済み → ✅ 合格（Series B Stage基準達成）
- 計画未策定 → ❌ 不合格（計画策定必須）
- 計画策定済みだが達成困難 → ⚠️ 要改善（計画見直し必要）
```

**ForStartup Benchmark**:
- Airレジ: 初年度売上発生、3年黒字達成
- Airペイ: 初年度売上5億円、3年黒字達成
- スタディサプリ: 初年度から黒字、3年黒字達成
- Geppo: 初年度から黒字、3年黒字達成

---

#### STEP 8: 総合PMF判定

**7指標の統合評価**:

```markdown
## PMF診断結果サマリー

| 指標 | 目標 | 実績 | 判定 |
|------|------|------|:----:|
| 外部顧客獲得 | ≥100社/人 | XX社/人 | ✅/⚠️/❌ |
| Sean Ellisテスト | ≥40% | XX% | ✅/⚠️/❌ |
| 月次成長率 | ≥10%/月 | XX%/月 | ✅/⚠️/❌ |
| Churn Rate | ≤5%/月 | XX%/月 | ✅/⚠️/❌ |
| NPS | ≥50 | XX | ✅/⚠️/❌ |
| 収益化開始 | 発生 | [発生 / 未発生] | ✅/❌ |
| 3年黒字計画 | 策定済み | [策定済み / 未策定] | ✅/❌ |

**総合判定**: [✅ PMF達成（Series B Stage承認可） / ⚠️ 要改善 / ❌ PMF未達成]
```

**判定ロジック（ForStartup版）**:
```python
必須条件 = (外部顧客獲得 ≥ 100社/人) AND 収益化開始 AND 3年黒字計画策定済み
PMF指標合格数 = ✅の数（Sean Ellisテスト、月次成長率、Churn Rate、NPS）

if not 必須条件:
    総合判定 = "❌ PMF未達成（Series B Stage基準未達）"
elif PMF指標合格数 == 4:
    総合判定 = "✅ PMF達成（Series B Stage承認可）"
elif PMF指標合格数 >= 2:
    総合判定 = "⚠️ 要改善"
else:
    総合判定 = "❌ PMF未達成"
```

---

#### STEP 9: 改善アクション提案

（Origin版と同一、ForStartup Benchmarkを追加）

**未達成指標別の改善策**:

| 指標 | 状態 | 改善アクション | ForStartup Benchmark |
|------|------|---------------|---------------------|
| 外部顧客獲得 < 100社/人 | Series B Stage基準未達 | 1. 営業網活用強化（ホットペッパー営業2,000名等）<br>2. クロスセル率向上（Airレジ→Airペイ 57%）<br>3. 既存顧客基盤への先行案内<br>4. 3ヶ月後に再測定 | Airレジ1年10万店舗、Airペイ1年20万店舗 |
| Sean Ellisテスト < 40% | コアバリュー不足 | 1. 「非常に残念」と回答したユーザーにインタビュー<br>2. 最も価値を感じている機能を特定<br>3. その機能を強化、他機能を削減<br>4. 1ヶ月後に再測定 | - |
| 月次成長率 < 10% | 成長鈍化 | 1. チャネル別獲得コストを分析<br>2. 最も効果的なチャネルに集中投資<br>3. リファラルプログラムの導入<br>4. オンボーディング改善で初月継続率向上 | - |
| Churn Rate > 5% | 離脱多い | 1. 解約理由インタビュー（10人以上）<br>2. オンボーディング強化（初月が重要）<br>3. 定期的なチェックイン（週次/月次）<br>4. ヘルススコア導入で早期警告 | Airレジ10-15%、Airペイ10%、Geppo 2% |
| NPS < 50 | 満足度低い | 1. Detractorにインタビュー（不満点特定）<br>2. クリティカルバグの修正<br>3. カスタマーサポート強化<br>4. 新機能ではなく既存機能の改善に注力 | Airレジ60-70、Airペイ70-80、Geppo 70-80 |
| 収益化未開始 | Series B Stage基準未達 | 1. 収益化モデル見直し（サブスク、手数料、広告等）<br>2. 価格設定検証（Unit Economics健全性）<br>3. 初期売上発生を最優先<br>4. 1ヶ月後に再測定 | Airレジ・Airペイ・スタディサプリ・Geppo すべて初年度売上発生 |
| 3年黒字計画未策定 | Series B Stage基準未達 | 1. 定量的ロードマップ作成（売上、コスト、営業利益、累損）<br>2. Unit Economics健全性確認（LTV/CAC 5.0以上）<br>3. 成長シナリオ3パターン（Best/Base/Worst）<br>4. 1週間以内に策定 | Airレジ・Airペイ・スタディサプリ・Geppo すべて3年黒字達成 |

**優先順位付け（ICEスコア）**:
```markdown
| 改善施策 | Impact（1-10） | Confidence（1-10） | Ease（1-10） | ICEスコア | 優先度 |
|---------|--------------|------------------|------------|----------|--------|
| [施策A] | 9 | 8 | 7 | 504 | 1 |
| [施策B] | 7 | 9 | 5 | 315 | 2 |
| [施策C] | 8 | 6 | 3 | 144 | 3 |
```

---

#### STEP 10: Series B Stage移行判断

**PMF達成時（7指標すべて✅）**:

```markdown
## 次のステップ: Series B Stage承認申請（本格事業化）

### 推奨アクション
1. `/build-approval-deck` で役員承認用資料作成
2. Unit Economics健全性確認（LTV/CAC ≥ 5.0、Churn率≤15%）
3. `/measure-aarrr` でAARRRファネルを測定
4. スケール戦略策定（営業網活用、クロスセル強化）

### 移行タイミング
- 即時移行可能
- 目安: 2-4週間で役員承認申請

### ForStartup成功事例
- Airレジ: 1年10万店舗、3年黒字達成
- Airペイ: 1年20万店舗、初年度売上5億円、3年黒字達成
- Geppo: 2年300社、継続率98%、3年黒字達成
```

**要改善時（必須条件✅ + PMF指標2-3個✅）**:

```markdown
## 次のステップ: 改善後に再診断

### 改善計画（1-2ヶ月）
1. 未達成指標の改善アクション実行
2. 週次で進捗モニタリング
3. 1-2ヶ月後に `/validate-pmf` を再実行
4. 再診断で7指標達成→Series B Stageへ

### 注意事項
- スケール施策は控える（PMF達成前のスケールは危険）
- 新規機能開発より既存機能の改善に注力
- 外部顧客獲得を最優先
```

**PMF未達成時（必須条件❌ OR PMF指標0-1個✅）**:

```markdown
## 次のステップ: Pivot検討

### 警告
7指標のうち0-1個のみ達成、または外部顧客100社/人未達は、PMF未達成の明確なサインです。

### 推奨アクション
1. `/pivot-decision` でPivot判断を実施
2. 以下の5つのPivot種類を検討:
   - ズームイン: 特定機能に特化
   - ズームアウト: より大きな課題へ拡大
   - 顧客セグメント変更: 別のターゲットへ
   - 課題Pivot: 別の課題を解決
   - チャネルPivot: 販売経路を変更

### Pivot判断基準
- 3ヶ月連続で改善が見られない
- チーム全員がPivot必要性を認識
- ランウェイが6ヶ月以上ある

### ForStartup撤退事例
- エリクラ: 6年実証実験レベル継続、外部スケールせず → 撤退
- スタディサプリ個別指導: 1.5年でUnit Economics不健全と判断 → 撤退
- 教訓: 1-2年でPMF判断、達成できなければ速やかに撤退
```

---

#### STEP 11: 成果物出力

**ツール**: Write
**パス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/pmf_diagnosis.md`

**成果物構造**: 下記テンプレート参照

---

## 成果物フォーマット

```markdown
# PMF診断レポート（ForStartup Edition）

**作成日**: [YYYY-MM-DD]
**対象プロダクト**: [プロダクト名]
**総合判定**: ✅ PMF達成（Series B Stage承認可） / ⚠️ 要改善 / ❌ PMF未達成
**Series B Stage承認**: [承認可 / 要改善 / 承認不可]

---

## エグゼクティブサマリー

### 総合判定: [判定結果]

| 指標 | 目標 | 実績 | 判定 |
|------|------|------|:----:|
| **外部顧客獲得** | ≥100社/人 | XX社/人 | ✅/⚠️/❌ |
| Sean Ellisテスト | ≥40% | XX% | ✅/⚠️/❌ |
| 月次成長率 | ≥10%/月 | XX%/月 | ✅/⚠️/❌ |
| Churn Rate | ≤5%/月 | XX%/月 | ✅/⚠️/❌ |
| NPS | ≥50 | XX | ✅/⚠️/❌ |
| **収益化開始** | 発生 | [発生 / 未発生] | ✅/❌ |
| **3年黒字計画** | 策定済み | [策定済み / 未策定] | ✅/❌ |

**判定理由**:
[7指標の状況から総合判定の根拠を記載]

**ForStartup Benchmark比較**:
- Airレジ: 1年10万店舗、Sean Ellis推定45%、NPS 60-70、3年黒字
- Airペイ: 1年20万店舗、クロスセル率57%、NPS 70-80、初年度売上5億円
- あなたのプロジェクト: [Benchmark比較コメント]

---

## 詳細分析

### 1. 外部顧客獲得

**顧客セグメント分類**:

| セグメント | 顧客数 | カウント | 備考 |
|----------|-------|---------|------|
| 外部顧客（有料） | XX社/人 | ✅ | Series B Stage基準カウント対象 |
| 外部顧客（無料トライアル） | XX社/人 | ⚠️ | 別枠参考値 |
| 早期顧客 | XX社/人 | ❌ | 除外 |
| グループ会社顧客 | XX社/人 | ❌ | 除外 |
| **外部顧客合計** | **XX社/人** | - | Series B Stage基準: 100社/人以上 |

**判定**: ✅ 合格 / ⚠️ 要改善 / ❌ 不合格

**インサイト**:
- 外部顧客獲得ペース: [月間XX社/人]
- 主要獲得チャネル: [営業網 / 既存顧客クロスセル / 広告 等]
- 改善提案: [具体的なアクション]

**ForStartup Benchmark比較**:
- Airレジ: 1年で10万店舗（月間約8,333店舗ペース）
- Airペイ: 1年で20万店舗（月間約16,667店舗ペース）
- あなたのプロジェクト: 月間XX社/人ペース → [評価]

---

### 2. Sean Ellisテスト

[Origin版と同一]

---

### 3. 月次成長率

[Origin版と同一]

---

### 4. Churn Rate

[Origin版と同一、ForStartup Benchmarkを追加]

**ForStartup Benchmark比較**:
- Airレジ: 推定Churn率10-15%
- Airペイ: 推定Churn率10%
- Geppo: 継続率98%（Churn率2%）
- あなたのプロジェクト: Churn率XX% → [評価]

---

### 5. NPS（Net Promoter Score）

[Origin版と同一、ForStartup Benchmarkを追加]

**ForStartup Benchmark比較**:
- Airレジ: 推定NPS 60-70
- Airペイ: 推定NPS 70-80
- スタディサプリ: 推定NPS 60-70
- Geppo: 推定NPS 70-80
- あなたのプロジェクト: NPS XX → [評価]

---

### 6. 収益化状況

**初期売上発生**:

| 項目 | 状況 | 金額 |
|-----|------|------|
| 初年度売上 | [発生 / 未発生] | [XX億円] |
| 収益化開始月 | [YYYY-MM] | - |
| 主要収益源 | [サブスク / 手数料 / 広告 等] | - |

**判定**: ✅ 合格 / ❌ 不合格

**インサイト**:
- 収益化モデル: [詳細]
- Unit Economics: LTV/CAC比 [XX倍]
- 改善提案: [具体的なアクション]

**ForStartup Benchmark比較**:
- Airレジ: 初年度売上発生、3年黒字達成
- Airペイ: 初年度売上5億円、3年黒字達成
- あなたのプロジェクト: 初年度売上XX億円 → [評価]

---

### 7. 3年黒字・5年累損解消計画

**定量的ロードマップ**:

| 年次 | 売上 | コスト | 営業利益 | 累損 | 判定 |
|-----|------|-------|---------|------|------|
| 1年目 | XX億円 | XX億円 | ▲XX億円 | ▲XX億円 | - |
| 2年目 | XX億円 | XX億円 | ▲XX億円 | ▲XX億円 | - |
| 3年目 | XX億円 | XX億円 | **XX億円** | ▲XX億円 | 単月黒字達成 ✅ |
| 4年目 | XX億円 | XX億円 | XX億円 | ▲XX億円 | - |
| 5年目 | XX億円 | XX億円 | XX億円 | **0円** | 累損解消 ✅ |

**判定**: ✅ 合格 / ⚠️ 要改善 / ❌ 不合格

**インサイト**:
- 成長シナリオ: [Best/Base/Worst]
- リスク要因: [主要リスク3つ]
- 改善提案: [具体的なアクション]

**ForStartup Benchmark比較**:
- Airレジ: 3年黒字達成
- Airペイ: 3年黒字達成
- スタディサプリ: 初年度から黒字、3年黒字達成
- Geppo: 初年度から黒字、3年黒字達成
- あなたのプロジェクト: 3年黒字[達成見込み / 困難] → [評価]

---

## 改善アクション

### 未達成指標の改善計画

[STEP 9の改善アクション表を出力]

### 優先順位付け（ICEスコア）

[ICEスコア表を出力]

---

## 次のステップ

[STEP 10のSeries B Stage移行判断を出力]

---

## 参照成果物

| ファイル | 作成日 | 内容 |
|----------|--------|------|
| psf_validation.md | [日付] | PSF検証結果 |
| ring_criteria_diagnosis.md | [日付] | Series A Stage診断結果 |
| sean_ellis_survey.csv | [日付] | Sean Ellisテスト生データ |
| nps_survey.csv | [日付] | NPS調査生データ |
| growth_data.csv | [日付] | 月次成長率データ |
| churn_data.csv | [日付] | Churn Rateデータ |
| revenue_data.csv | [日付] | 収益データ |
| 3year_plan.md | [日付] | 3年黒字・5年累損解消計画 |

---

## メタデータ

| 項目 | 内容 |
|-----|------|
| 作成日 | [YYYY-MM-DD] |
| 実行Skill | `/validate-pmf` (ForStartup Edition) |
| フレームワーク | 起業の科学（PMF達成基準） + Series B Stage基準 |
| 準拠率 | 100% |
| 次の更新予定 | [1-2ヶ月後] |
| Research統合 | Founder_Research 31製品分析 |
| Benchmark製品 | Airレジ、Airペイ、スタディサプリ、Geppo |
```

---

## ForStartup Knowledge Base Reference

### 評価基準・フレームワーク
- VC投資基準総合: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - CPF/PSF/PMF ≥70%、TAM ≥$1B、月次成長率 ≥20%、10倍優位性 3軸以上
  - NRR（Net Revenue Retention）≥120%、年次成長率 ≥300%（SaaS基準）
- VC調達ロードマップ: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - Pre-Seed → Seed → Series A基準
- ユニットエコノミクス: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - LTV/CAC ≥5.0、CAC回収期間 ≤12ヶ月、Gross Margin ≥70%

### ケーススタディ
- 成功事例（Legendary）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/
  - Brian Chesky（Airbnb）、Patrick Collison（Stripe）、Brian Armstrong（Coinbase）
- 成功事例（Unicorn）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/02_Unicorn/
  - Girish Mathrubootham（Freshworks）、Henrique Dubugras（Brex）
- 成功事例（VC-Backed）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/
  - Dylan Field（Figma）、Vlad Tenev（Robinhood）、Melanie Perkins（Canva）
- 失敗事例: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/
  - Elizabeth Holmes（Theranos）、Adam Neumann（WeWork）

### 事例参照
- 成功パターン（Tier 1-4）: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#success-patterns
- 失敗パターン: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#failure-patterns
- スキル別推奨事例: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/case_reference_for_startup.md#skill-mapping-validate-pmf
- Airレジ PMF 9.2事例: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/

### 全体参照
- ForStartup全体概要: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#forrecruit-edition
- Seed調達ステージゲート: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#ring-stage-gates
- 撤退基準: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---
## 使用例

```
User: /validate-pmf

Skill:
# PMF診断 自律実行開始（ForStartup Edition）

前提条件チェック中...
✅ PSF達成済み
✅ Series A Stage突破済み
✅ MVP稼働中
✅ 外部顧客獲得: 150社（Series B Stage基準達成）
✅ 3ヶ月データ存在
✅ 収益化開始（初年度売上3,000万円）
✅ 3年黒字計画策定済み

[自動診断実行中...]

STEP 1: 前提条件確認 ✅
STEP 2: 外部顧客獲得数検証 ✅
  - 外部顧客（有料）: 150社
  - 判定: ✅ 合格（Series B Stage基準達成）

STEP 3: Sean Ellisテスト実施 ✅
  - 有効回答数: 55社
  - 「非常に残念」: 48%
  - 判定: ✅ 合格

STEP 4: 月次成長率計算 ✅
  - 指標: MRR
  - 3ヶ月平均: 15.2%/月
  - 判定: ✅ 合格

STEP 5: Churn Rate測定 ✅
  - 3ヶ月平均: 4.5%/月
  - 判定: ✅ 合格

STEP 6: NPS測定 ✅
  - NPS: 62
  - 判定: ✅ 合格

STEP 7: 収益化・3年黒字計画検証 ✅
  - 初年度売上: 3,000万円 ✅
  - 3年黒字計画: 策定済み ✅
  - 判定: ✅ 合格

STEP 8: 総合PMF判定 ✅
STEP 9: 改善アクション提案（スキップ: 全指標合格）
STEP 10: Series B Stage移行判断 ✅
STEP 11: 成果物出力 ✅

## 完了

成果物: Flow/202601/2026-01-02/pmf_diagnosis.md
総合判定: ✅ PMF達成（Series B Stage承認可）

| 指標 | 実績 | 判定 |
|------|------|:----:|
| 外部顧客獲得 | 150社 | ✅ |
| Sean Ellisテスト | 48% | ✅ |
| 月次成長率 | 15.2%/月 | ✅ |
| Churn Rate | 4.5%/月 | ✅ |
| NPS | 62 | ✅ |
| 収益化開始 | 発生（3,000万円） | ✅ |
| 3年黒字計画 | 策定済み | ✅ |

おめでとうございます！PMF達成、Series B Stage承認申請が可能です。

推奨: `/build-approval-deck` で役員承認用資料作成、本格事業化へ
```

---

## 成功基準

1. ✅ **7指標すべて測定完了**: データ欠損なし、最低サンプル数達成
2. ✅ **総合判定の妥当性**: 起業の科学 + Series B Stage基準で客観的に判定
3. ✅ **自動アンケート設計**: Sean Ellisテスト・NPSのテンプレート自動生成
4. ✅ **改善アクションの具体性**: 実行可能な提案、ICEスコアで優先順位付け、ForStartup Benchmark統合
5. ✅ **Series B Stage移行判断の明確性**: 本格事業化 or Pivot or 改善の判断根拠明示

---

## 注意事項

1. **ForStartup特化調整**:
   - 外部顧客獲得100社/人以上が必須（社内実証のみは不可）
   - 収益化開始が必須（初期売上発生）
   - 3年黒字・5年累損解消計画策定が必須
   - リクルート撤退事例（エリクラ6年、スタディサプリ個別1.5年等）を参照

2. **最低サンプル数の遵守**: Sean Ellisテスト・NPSは最低40人、成長率・Churn Rateは3ヶ月データ必須
3. **早期判定の危険性**: データ不足での判定は誤判断につながる
4. **PMF達成前のスケール禁止**: PMF未達成でのマーケティング投資は資金の無駄遣い
5. **定期的な再測定**: PMF達成後も四半期ごとに再測定し、維持を確認
6. **1-2年でPMF判断**: エリクラ失敗の教訓（6年実証実験は異常）、達成できなければ速やかに撤退

---

## 更新履歴

- 2026-01-02: ForStartup特化版として新規作成、Founder_Research 31製品分析統合
- Series B Stage基準追加（外部顧客獲得、収益化、3年黒字計画）
- ForStartup Benchmark追加（Airレジ、Airペイ、スタディサプリ、Geppo）
- Domain-Specific Knowledgeセクション追加（15事例統合）
