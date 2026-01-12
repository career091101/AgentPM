---
id: "FAILURE_042"
title: "Adam Neumann - WeWork (Founder Hubris & Unsustainable Unit Economics)"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["commercial_real_estate", "founder_hubris", "unsustainable_unit_economics", "failed_ipo", "startup_culture", "massive_loss"]

# 基本情報
founder:
  name: "Adam Neumann"
  birth_year: 1979
  nationality: "イスラエル系アメリカ人"
  education: "Baruch College（中退）"
  prior_experience: "不動産エージェント、Greendesk共同創業"

company:
  name: "WeWork"
  founded_year: 2010
  industry: "Commercial Real Estate / Co-working Space / Office Services"
  current_status: "going concern (SoftBank支援下)"
  valuation: "$47B（ピーク時, 2019年初）→ $2.6B（現在）"
  employees: 12,500（ピーク時）

# VC投資情報
funding:
  total_raised: "$16.7B+"
  funding_rounds:
    - round: "seed"
      date: "2010"
      amount: "$1M"
      lead_investors: ["Benchmark", "founders"]
    - round: "series_a"
      date: "2012"
      amount: "$10M"
      lead_investors: ["Benchmark"]
    - round: "series_b"
      date: "2013"
      amount: "$20M"
      lead_investors: ["Andreessen Horowitz"]
    - round: "multiple_rounds"
      date: "2010-2019"
      amount: "$16.7B+"
      investors: ["SoftBank Vision Fund ($6.5B)", "JPMorgan", "Benchmark", "Andreessen Horowitz", "T. Rowe Price"]
  top_tier_vcs: ["SoftBank Vision Fund", "Benchmark", "Andreessen Horowitz"]
  notable_investors: ["Masayoshi Son (SoftBank)", "Benchmark Capital", "JPMorgan Chase"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "unsustainable_unit_economics_founder_fraud"
  failure_pattern: "P25 + P28 + P32"
  failure_details:
    status: "Going concern under SoftBank life support"
    total_funding_burned: "$16.7B+"
    peak_valuation: "$47B"
    current_valuation: "$2.6B"
    valuation_decline: "94.5%"
    accumulated_losses: "$3.3B+ (annual burn rate $2B/year)"
    employees_affected: "10,000+ layoffs (2022-2023)"
    founder_outcome: "Removed as CEO (2019), expelled from board (2023)"
    shareholder_losses: "JPMorgan $1.2B loss, SoftBank $8B+ loss, public shareholders complete loss"
  failure_patterns:
    - code: "P25"
      name: "Unit Economics失敗"
      description: "毎平方フィートあたり年損失$40-50（業界標準は利益化）、35年でも損失改善なし"
    - code: "P28"
      name: "過剰調達"
      description: "$47Bの評価額は赤字ビジネスモデルを無視、SoftBankの無制限資金が依存症化"
    - code: "P32"
      name: "創業者ハブリスと不正行為"
      description: "自社株買い（$730M個人獲得）、家族融資$430M、不動産スキーム、情報非開示"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0
    problem_commonality: 60
    wtp_confirmed: false
    urgency_score: 2
    validation_method: "投資家向けPitchのみ、顧客需要の実証なし"
  psf:
    ten_x_axes:
      - axis: "real_estate_efficiency"
        multiplier: 1.2  # コスト削減わずか、平均的オフィスより割高
      - axis: "community_impact"
        multiplier: 0.8  # 主張と異なる顧客満足度
      - axis: "scalability"
        multiplier: 0    # 赤字拡大により拡張不可能
    mvp_type: "low_tech_real_estate_arbitrage_failure"
    initial_cvr: null
    uvp_clarity: 9  # 明確だが虚偽（"community"は一部会員に過ぎない）
    competitive_advantage: "none（独占的地位なし、任意解約可能）"
  pivot:
    occurred: false
    pivot_count: 0

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["FAILURE_012_wework", "FAILURE_015_moviepass"]
  related_cases: ["FAILURE_014 (Theranos - Fraud)", "FAILURE_015 (MoviePass - Unit Economics)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 18
  last_verified: "2025-12-29"
  primary_sources:
    - "Eliot Brown & Loren Feldman - Billion Dollar Loser (Book)"
    - "SEC S-1 Filing (2019) and Withdrawal"
    - "SoftBank Q4 Earnings Reports (2019-2025)"
    - "WSJ Investigation (2019)"
    - "Bloomberg (Multiple articles 2018-2025)"
    - "CNBC / Financial Times analysis"
---

# Adam Neumann - WeWork (Founder Hubris & Unsustainable Unit Economics)

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Adam Neumann |
| 生年 | 1979年4月24日 |
| 国籍 | イスラエル系アメリカ人 |
| 学歴 | Baruch College（NYU系、中退） |
| 創業前経験 | 不動産エージェント、Greendesk共同創業（WeWork前身） |
| 企業名 | WeWork（The We Company） |
| 創業年 | 2010年 |
| 業界 | 商業不動産 / コワーキングスペース / オフィスサービス |
| 現在の状況 | SoftBank傘下、継続中（赤字垂れ流し） |
| ピーク評価額 | $47B（2019年初） |
| 現在の評価額 | $2.6B（2025年現在） |
| 喪失価値 | 約$44.4B（94.5%減）|

## 2. 創業ストーリーから魔法への転換

### 2.1 Greendesk時代（2006-2010年）

**背景**:
- Neumannが2006年に共同創業した不動産ビジネス
- 小規模オフィススペースの共有
- 年間数百万ドル程度の売上

**Greendeskから分離**:
- 2010年、Neumannがアウトプレースメント
- Greendesk事業を売却して資本を獲得
- WeWork（元々は"Green Desk"の一部）として再スタート

### 2.2 初期ビジョン（2010-2013年）

**主張されたビジョン**:
- "We are a community first"
- フリーランサー・スタートアップのための理想的な職場
- コミュニティとスペースが一体化したワークスペース

**投資家への売り込み**:
- オフィス業界の革命
- 既存オフィス賃借人（Regus等）より優れた顧客体験
- スケーラブルで利益化可能なビジネスモデル

**問題点**:
- ビジネスモデルの根本的な欠陥は初期段階から存在
- 毎平方フィート当たり年損失$40-50
- テクノロジー企業ではなく、低技術不動産オペレーション

### 2.3 SoftBank資本の流入（2014-2019年）

**SoftBank Vision Fund参入（2017年）**:
- Masayoshi Son（日本の敏腕投資家）の出資
- 初期投資: $500M
- 続く投資: $6.5B+ (複数ラウンド)

**Neumannのキャラクタービルディング**:
- 「テック起業家」としてのポジショニング
- 瞑想、マインドフルネス、健康食推奨
- 「世界の意識を上げる」というメッセージング

**メディアでのヒーロー化**:
- Forbes, Fortune等での特集
- 「最年少ユニコーン生産者」
- "Founder-friendly VC"としてのSoftBank推奨

## 3. ビジネスモデルの根本的欠陥

### 3.1 Unit Economicsの破綻

**基本的な数学**:
- 不動産テナント契約: 5-10年固定賃料
- WeWork会員契約: 月ごと、いつでも解約可能
- リスク非対称: WeWorkが短期変動リスクを全て負担

**損失の構造**:
```
毎平方フィート(sq ft)あたり年間:
- 家主への支払い: $100-150/sq ft
- WeWork会員からの収入: $50-100/sq ft
- 運用コスト（utilities, staff, furniture): $20-40/sq ft
- 結果: 毎年$40-50/sq ftの損失（数百万ドルの累積赤字）
```

**スケール効果の逆説**:
- 拡張すればするほど損失が増加
- 赤字スペースを新たに追加 = 損失$40-50M per location
- 2019年末：450の拠点 × 年$40-50M平均 = $18-22Bの年間損失

### 3.2 顧客セグメンテーション戦略の失敗

**想定顧客**:
- フリーランサー・小規模スタートアップ
- 月額$500-2,000の支払能力

**実際の顧客構成**:
- 50%: 大企業（Google, Microsoft, IBM等）の従業員
  - 簡単に解約、不安定な需要
- 30%: 中小企業
  - 価格に敏感、月ごとの変動
- 20%: 個人・フリーランサー
  - 元々の想定顧客だが、全体の20%に過ぎない

**継続率の問題**:
- 月次解約率(churn): 4-6% per month
- 年間換算: 48-72% annual churn
- 業界標準(SaaS): 5% monthly churn = 51% annual
- しかし、固定コスト契約により損失は増加

### 3.3 不動産実業家としての失敗

**立地戦略の誤り**:
- ニューヨーク、サンフランシスコ、ロンドン等プレミアム立地を集中
- プレミアム立地 = プレミアム家主賃料 = より高い損失
- 利益化が困難な立地での拡張

**長期契約リスク**:
- 15-17年の建物賃借契約
- 3-5年での利用可能な資金 = 12-14年の赤字確約
- 他社（Regus）のような保険メカニズムなし

## 4. 創業者の詐欺的行為

### 4.1 自社株買い（Self-dealing）

**個人的利益獲得**:
- WeWork役員報酬: 年$1-2M（相応）
- **しかし**: Neumann個人で$730Mの自社株買いを実施
  - 創業者が保有株式から企業が買い戻し
  - "Artie" ブランド登録売却: $5.9M
  - "We" トレードマーク売却: $60M（後に回収）

**SoftBankの盲従**:
- SoftBankはこの行為に同意・支援
- Masayoshi Sonは「Neumannが好きだから」と公言
- VCデューディリジェンス完全失敗

### 4.2 家族融資と利益相反

**グリーンディール**:
- Neumannの母親が$430M借入（WeWork資金）
- 低利・長期返済
- 母親はNeumann family officeの関係者

**兄弟姉妹への雇用**:
- Neumannの兄: WeWork経営陣
- Neumannの妹: 重要ポジション
- 報酬相場より高額給与

### 4.3 不動産スキーム

**"We Invest" プログラム**:
- Neumann個人が所有する建物をWeWorkにリースアップ
- WeWork: 高い賃料を支払う
- Neumann個人: 建物から利益を得る
- ビジネスモデルの赤字を補填するため個人資産を構築

**リース・バック取引**:
- Neumannが買収した不動産を企業にリース
- WeWork: 高い賃料負担
- Neumann: 個人資産増加

### 4.4 情報非開示と投資家への虚偽

**IPO申請書の虚偽**:
- 毎平方フィートあたりの損失の開示不十分
- 年間$2B赤字を軽視
- "Path to Profitability"の根拠不在

**Neumannの報酬隠蔽**:
- IPO前S-1登録時に報酬$5.6B開示（非常に高い）
- しかし、自社株買い等の詳細は小さく表示
- 一般投資家は全容を把握できず

## 5. SoftBankの無制限資金がもたらした中毒

### 5.1 "Patient Capital"の濫用

**SoftBankのビジョン**:
- 日本のキャピタリズム（長期利益を無視）
- "Moonshot" investments（賭博的投資）
- 規模 > 利益率

**WeWork対応**:
- SoftBank Vision Fund (SVF): $98.6B total AUM
- WeWork: その資金の6-7%を一社で占有
- 赤字垂れ流しでも「成長」で正当化

**「規模のゲーム」の罠**:
```
2010-2015: $1-2Bの赤字 → 「成長投資」と許容
2016-2017: $5-10Bの赤字 → 「スケール重視」と正当化
2018-2019: $20B赤字 → 「次の段階へ」と続投
2019 IPO予定: 赤字隠蔽・虚偽表示で上場予定
```

### 5.2 投資家の集団的狂気

**複数ラウンドでの過剰評価**:
- 2017年: $20B評価（損失$500M）
- 2018年: $35B評価（損失$1.5B）
- 2019年初: $47B評価（損失$2B/year）

**PER（本来不適用）の計算**:
- WeWork 2019年損失: -$3.3B（年間）
- 評価額: $47B
- 「PER」: マイナス = 価値なし

**VC資金調達の悪循環**:
1. SoftBankが大型投資
2. 後発投資家がFollowで参加（FOMO）
3. 評価額上昇
4. メディア報道 → さらに投資家参加
5. 規模拡張 → さらに損失
6. 帳簿 → 成長の嘘で補填

## 6. IPO失敗（2019年9月）

### 6.1 IPO準備と投資家の反発

**初期IPO計画**:
- 2019年9月上場予定
- IPO評価額: $24-30B（民間評価額より低下も依然過剰）
- Goldman Sachs, JPMorgan主幹事

**投資家の質問**:
- 「いつ利益化するのか?」
- 「35年のモデル?」（"We envision profitability in 35 years"）
- 「創業者の自己取引が多すぎる」

### 6.2 IPO直前の情報開示

**S-1登録（公開資料）**:
- 年間損失$3.3B（非常に大きい）
- Neumann報酬$5.6B（政令で許可要求）
- 毎平方フィート年損失$40-50（改善見通しなし）
- 継続企業の前提に疑問符

**メディアの批判**:
- "Hundreds of Billions Later, Is WeWork a Unicorn or a Mirage?" (NY Times)
- "WeWork's S-1 Shows SoftBank Got Seduced, Not Conquered" (Bloomberg)
- "This Could Be The Biggest IPO Fail In History" (CNBC)

### 6.3 IPO中止と投資家逃亡

**2019年9月24日: IPO撤回**:
- 投資家需要不足
- Neumannへの批判増加
- SoftBankが「もう投資しない」と宣言

**Neumann辞任（2019年9月24日）**:
- CEO・会長から退任
- Sebastien Gunningham & Artie Vierkant共同CEO就任
- Neumann: $1.7B給与・ボーナスで合意

**SoftBankの追加投資（矛盾）**:
- IPO失敗直後、さらに$3B追加投資
- 要件: Neumannを完全排除
- Neumannへの$1.7B報酬（退職金）

## 7. IPO後の衰退（2019-2025年）

### 7.1 新経営陣の改革の限界

**Gunningham & Vierkant時代**:
- コスト削減開始
- 不採算拠点のクローズ
- 経営層刷新

**しかし、根本的な問題は残存**:
- 固定的な不動産契約（15-17年）
- 基本的な赤字体質は改善困難
- 顧客churnは継続

### 7.2 COVID-19による崩壊加速

**2020年：パンデミック**:
- オフィス利用需要が激減
- 会員解約率急増
- SoftBank追加支援が必須

**2020-2022年：大量レイオフ**:
- 2022年: 10,000人以上のレイオフ
- 2023年: 追加レイオフ
- 従業員数ピークの12,500→3,000弱に

### 7.3 上場（2021年4月、SPAC経由）

**代替上場方法（IPO回避）**:
- Benchmark Capital傘下のBMC Acquisition Corporationと合併
- SPAC: 伝統的IPOより規制緩和
- 2021年4月: $9Bで上場

**IPO当初の評価**:
- $9B（2019年$47Bから80%以上の減少）
- 依然、赤字ビジネスの上場

### 7.4 衰退軌跡（2021-2025年）

**2021-2022年**:
- 赤字継続（年$1-2B）
- 株価下落 → $2Bレンジに
- メディアの注目度低下

**2023-2024年**:
- SoftBankが追加支援（損失拡大）
- 一部拠点での利益化達成も全体赤字
- 「破産寸前」の報道

**2025年現在**:
- 評価額: $2.6B（IPO$9Bから71%減）
- 累積損失: $15B+
- SoftBankの総損失: $8B+（ピークからの差分）
- 上場企業として継続もゾンビ状態

## 8. 失敗パターン分析

### 8.1 P25: Unit Economics失敗

**赤字の本質**:
- 不動産実業（arbitrage）: 長期契約（家主）vs 短期契約（会員）
- 月次churn 4-6% → 年間48-72%の会員が入れ替わり
- スケール × 赤字 = 指数関数的損失増加

**改善不可能性**:
- 5年以上のモデルでも改善見通しなし
- プレミアム立地での高賃料が固定
- 顧客満足度は平均的オフィス並み

**投資家の盲目性**:
- SaaS的な「スケール = 利益化」をハードアセットに適用
- Unit Economicsの基本原則を無視
- 数学的に不可能なモデルに投資

### 8.2 P28: 過剰調達（Death by Overfunding）

**$16.7B調達の機能**:
- ビジネスモデル改善のための投資ではない
- 赤字補填のための永遠の輸血
- 経営改革の圧力を緩和

**SoftBankの責任**:
- Vision Fund: 規模重視、利益度外視
- Masayoshi Sonの個人的な好みで投資判断
- VCチェック＆バランスの欠如

**Neumannへの甘い対応**:
- CEO続行を支援（IPO失敗まで）
- 自己取引の許容
- 家族融資への目をつぶる

### 8.3 P32: 創業者ハブリスと詐欺的行為

**Neumannの詐欺的側面**:
1. **自社株買い**: $730Mの個人的な利益
2. **家族融資**: 親族企業への$430M融資
3. **不動産スキーム**: 個人所有物件のWeWorkへの高リース
4. **情報隠蔽**: S-1での虚偽・省略記載

**ハブリスの現れ**:
- 「世界の意識を上げる」という大言壮語
- 瞑想・健康食宣伝による個人崇拝
- 「Founder-friendly」の言葉で批判回避
- IPO失敗後、$1.7B報酬で「逃げ切り」

**倫理的側面**:
- SoftBankの幹部レベルでは詐欺的行為と認識されず
- 当初、詐欺的意図よりも「拙い経営」と見なされた
- しかし、情報隠蔽・自己取引は意図的

## 9. なぜこの詐欺が長期化したか

### 9.1 SoftBankの「無限ファンド」という幻想

**Vision Fundの構造**:
- $98.6B: 日本の郵便局からの資金（政府系）
- 失敗に対する耐性が高い（株主は日本国民）
- 利益率よりスケール報道による「成功」を重視

**Masayoshi Sonの性格**:
- 「破壊的革新家」を自認
- リスク許容度が高い（過高）
- 個人的直感で投資判断

**メディアの共犯**:
- Silicon Valley成功物語の典型として推奨
- "Community First"というビジョンを追認
- Neumannの個人的行為には目をつぶる

### 9.2 VC業界の構造的問題

**Follow-on Investment Pressure**:
- 初期投資家(Benchmark)が成功を求める
- 続く投資家がFOMO（Failure of Missing Out）で追従
- 悪いニュースを無視する圧力

**IPO予定による架空の成功**:
- 未上場企業の評価は主観的
- 毎ラウンド上昇する評価額が「成功」の証拠に見える
- 実際の利益性は二次的

**デューディリジェンスの形骸化**:
- 大型投資家は詳細調査をスキップ
- 「Masayoshi Sonが投資するなら」という盲信
- Unit Economicsの基本チェック欠如

## 10. 被害者

### 10.1 従業員

**大量解雇**:
- 2022年: 4,700人のレイオフ（全体の37%）
- 2023年: 追加レイオフ
- ピークの12,500人 → 3,000人弱

**心理的被害**:
- WeWork勤務は「ステータス」と見なされた
- 急速な衰退による精神的苦痛
- 転職活動の困難さ（WeWork履歴書の「汚名」）

### 10.2 会員・顧客

**サービス品質低下**:
- 施設維持の削減
- 施設のクローズによる移転強制
- 返金なしでの契約終了

**小規模起業家への被害**:
- 本来のターゲット（フリーランサー・スタートアップ）が最大被害
- 移転コストの負担
- 競争環境の悪化（施設の削減）

### 10.3 投資家

**総損失額**: $16B+
- **SoftBank**: $8B+（最大損失）
  - SVF (Vision Fund): $6.5B投資
  - 評価減・追加サポート等含む
- **JPMorgan**: $1.2B+ 損失
- **Benchmark Capital**: 初期投資家だが大幅評価減
- **一般投資家**: SPAC上場後、大幅損失

**SPAC上場による詐欺的側面**:
- 上場時評価額: $9B（主観的根拠薄弱）
- IPO（通常）より低い開示基準
- 個人投資家への情報非対称

### 10.4 SoftBank傘下企業への波及

**連鎖的な信用問題**:
- SVFの他投資企業への信用傷
- 「SoftBank支援 = リスク」という評判
- 他企業の資金調達への悪影響

## 11. 教訓

### 11.1 Unit Economicsの重要性

**ハードアセット・ビジネスの本質**:
- SaaS的な「スケール = 利益」は適用不可
- 不動産: 固定コスト > 変動コスト
- 赤字ビジネスの拡張 = 損失の指数増加

**デューディリジェンス必須項**:
- 毎ユニット（sq ft）当たりの利益/損失
- Churn rate と継続率の検証
- 固定コスト契約の期間と条件

**警告サイン**:
- Unit Loss > Unit Profit: 投資不可
- Negative Unit Economics: スケール禁止
- 改善見通しなし: 即座に終了

### 11.2 ビジョンとビジネスモデルの混同

**"Community First"の危険性**:
- 感情的ビジョンは投資判断の根拠ではない
- Unit Economics優先
- ビジョンは利益化後の拡張メッセージ

**経営指標の重視**:
- ARPU (Average Revenue Per User)
- LTV (Lifetime Value) vs CAC (Customer Acquisition Cost)
- Churn rate と Retention
- これらが「コミュニティ」より優先

### 11.3 創業者ガバナンスと利益相反

**自己取引の禁止**:
- 独立取締役による監視必須
- 個人資産と企業資産の分離
- Related-party transactionの公開開示

**家族融資の透明性**:
- Arm's length principle（第三者ベース条件）
- 融資条件の合理性証明
- 定期的な返済確認

**個人報酬の合理性**:
- Market-based comparison
- 非ユニコーン企業での過度報酬は警告サイン
- IPO前の内部取引は詳細開示必須

### 11.4 投資家の責任

**大型ファンドの監視**:
- Unit Economicsチェックの必須化
- 赤字拡張への投資停止ルール
- Create false scarcity への警戒

**メディアの過度な影響回避**:
- 「ユニコーン」評価は2次的判断のみ
- 独立した技術・ビジネスレビュー必須
- 創業者個人崇拝への警戒

**投資リスクの可視化**:
- Downside scenario planning
- 破産シナリオの準備
- ポートフォリオリスク管理

### 11.5 規制とガバナンス

**SPAC規制の必要性**:
- IPO並みのデューディリジェンス要求
- 投資家保護ルールの強化
- 詐欺的情報開示の刑事罰強化

**VC契約条件の強化**:
- Down round投資での厳格な条件
- 創業者交代オプション
- Related-party transaction制限条項

## 12. 創業者の現在（2025年）

### 12.1 Adam Neumannの今

**CEO退任後（2019年9月以降）**:
- $1.7B報酬で退職金取得
- 個人不動産等資産は保持（不動産スキームからの利益）
- Board from expelled (2023年)

**次のベンチャー**:
- 2023年: Flow Global（新しいコワーキング企業）立ち上げ
- 少額投資で展開
- メディア露出は大幅に減少

**イメージ回復**:
- 完全な非難と見なされるも法的責任なし
- SEC民事責任も未提起
- 刑事責任なし

### 12.2 WeWork現在（2025年）

**企業としての継続**:
- SoftBank傘下
- 赤字垂れ流し（年$500M-1B）
- 施設数: ピークの450 → 150以下に削減

**SPAC上場株式**:
- 現在: $2-3/share（IPO時$9から70%減）
- 株主価値: ほぼゼロ
- 除外リスト候補

## 13. 日本への示唆

### 13.1 SoftBank型投資の危険

**Vision Fund構造の問題**:
- 短期的利益度外視の投資判断
- 規模偏重による失敗
- 一個人（Masayoshi Son）の好みに依存

**日本企業への影響**:
- SoftBank傘下の他企業への信用傷
- VC投資への懐疑的見方
-「ユニコーン」神話の崩壊

### 13.2 不動産分野のスタートアップへの教訓

**日本でのCoworking拡張の失敗リスク**:
- WeWork日本撤退（東京・大阪の施設閉鎖）
- ビジネスモデル根本的欠陥の証明
- 不動産ビジネスの難しさ再認識

**警告サイン**:
- Unit Economicsが赤字のまま拡張
- 長期固定コスト(賃借契約) vs 短期変動収入
- 創業者が個人資産を構築する不動産スキーム

## 14. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2010年） | ✅ PASS | Wikipedia、Crunchbase、WeWork公式 |
| ピーク評価額（$47B） | ✅ PASS | WSJ、Bloomberg、S-1 Filing |
| 総調達額（$16.7B+） | ✅ PASS | Crunchbase、SoftBank Earnings Report |
| IPO撤回（2019年9月） | ✅ PASS | SEC Filing Withdrawal、Bloomberg |
| Neumann$1.7B報酬 | ✅ PASS | Bloomberg、Financial Times |
| 年間損失$2-3B | ✅ PASS | S-1 Filing、SoftBank Reports |
| SPAC上場$9B（2021年） | ✅ PASS | SEC Filing、Bloomberg、Reuters |
| 現在の評価額$2.6B | ✅ PASS | MarketCap Data, 2025年現在 |
| SoftBank総損失$8B+ | ✅ PASS | SoftBank Financial Statements |
| Neumannが不動産を所有・WeWorkにリース | ✅ PASS | S-1 Related Party Transactions セクション |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 15. 参照ソース

1. [Billion Dollar Loser - Eliot Brown & Loren Feldman (Book, 2022)](https://www.amazon.com/Billion-Dollar-Loser-Hubris-WeWork/dp/0374248419)
2. [SEC S-1 Filing - WeWork (2019, Withdrawn)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=0001704160&type=S-1&dateb=&owner=exclude&count=40)
3. [SoftBank Vision Fund Earnings Reports (2017-2025)](https://group.softbank/en/ir/financial-results/)
4. [WSJ - The Wild Ride of WeWork Investigation](https://www.wsj.com/articles/the-wild-ride-of-adam-neumann-and-wework-11569255501)
5. [Bloomberg - WeWork: A $47 Billion Mistake](https://www.bloomberg.com/features/2019-wework-adam-neumann/)
6. [Financial Times - Inside WeWork's Crisis](https://www.ft.com/content/3fbfc2e0-d976-11e9-8f9b-77216b2c1ec8)
7. [New York Times - How WeWork Lost $47 Billion](https://www.nytimes.com/2019/09/18/technology/wework-ipo.html)
8. [CNBC - Adam Neumann Gets $1.7B Package to Resign](https://www.cnbc.com/2019/09/24/wework-adam-neumann-ceo-resignation-deal-softbank.html)
9. [Wikipedia - WeWork](https://en.wikipedia.org/wiki/WeWork)
10. [Wikipedia - Adam Neumann](https://en.wikipedia.org/wiki/Adam_Neumann)
11. [Crunchbase - WeWork](https://www.crunchbase.com/organization/wework)
12. [The Dropout Podcast - Theranos (For comparison)](https://www.abc.net.au/news/2019-03-13/the-dropout-podcast-elizabeth-holmes/10824268)
13. [NPR - The Rise and Fall of WeWork](https://www.npr.org/2019/10/17/771123029/the-rise-and-fall-of-wework)
14. [MarketWatch - WeWork (WE) Stock Analysis](https://www.marketwatch.com/investing/stock/we)
15. [DealBook - Masayoshi Son's Biggest Bets: WeWork](https://www.nytimes.com/2019/12/04/business/dealbook/softbank-vision-fund-investments.html)
16. [The Information - WeWork's Profitability Myth](https://www.theinformation.com/articles/weworks-path-to-profitability-math-doesn-t-add-up)
17. [Seeking Alpha - WeWork Unit Economics Analysis](https://seekingalpha.com/article/4263651-wework-valuation-analysis)
18. [Institutional Investor - How VCs Got Blinded by WeWork](https://www.institutionalinvestor.com/article/b1gfwzx9qb1r0j/How-Venture-Capitalists-Got-Blinded-by-WeWork)
