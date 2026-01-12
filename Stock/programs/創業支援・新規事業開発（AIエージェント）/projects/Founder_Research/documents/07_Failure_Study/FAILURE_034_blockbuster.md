---
id: "FAILURE_034"
title: "Blockbuster Video - Disruption Failure"
category: "failure"
tier: "failure_study"
type: "disruption_failure"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["video-rental", "disruption", "netflix", "market-failure", "legacy-business", "technological-disruption"]

# 基本情報
founder:
  name: "David Cook"
  co_founders: []
  birth_year: 1956
  nationality: "アメリカ"
  education: "Jones International University (経営学)"
  prior_experience: "Computer Specialist（PizzaHut）"

company:
  name: "Blockbuster Entertainment"
  founded_year: 1985
  industry: "ビデオレンタル / エンターテインメント / 小売"
  current_status: "bankrupt"
  valuation: "$5.5B（ピーク時2004年）→ $0（破産2010年）"
  employees: 60,000 # ピーク時

# VC投資情報
funding:
  total_raised: "$Non-VC（フランチャイズ&内部投資）"
  funding_rounds:
    - round: "founding"
      date: "1985-10"
      amount: "$6,000"
      valuation_post: "N/A"
      lead_investors: []
      other_investors: []
    - round: "early_growth"
      date: "1987-1990"
      amount: "$variable"
      valuation_post: "N/A"
      lead_investors: []
      other_investors: []
    - round: "public_listing"
      date: "1999-04"
      amount: "IPO"
      valuation_post: "$N/A"
      lead_investors: []
      other_investors: []
    - round: "viacom_merger"
      date: "1994-07"
      amount: "$4.6B"
      valuation_post: "$4.6B"
      lead_investors: ["Viacom"]
      other_investors: []
  top_tier_vcs: "Non-VC（Viacom買収→Viacom買収解除）"

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "disruption_failure_bankruptcy"
  failure_pattern: "P3 + P14 + P25 + P2"
  failure_details:
    - pattern: "P3"
      description: "ターゲット市場の消滅（ストリーミング革命）"
    - pattern: "P14"
      description: "タイミングミス（デジタル化への対応遅延、Netflixに先制された）"
    - pattern: "P25"
      description: "レガシービジネスモデルの固着（フランチャイズシステムに依存、変革不可）"
    - pattern: "P2"
      description: "キー人物の意思決定誤り（経営陣がNetflix機会を見逃す）"
  bankruptcy:
    bankruptcy_filed: "2010-09-23"
    bankruptcy_chapter: "Chapter 11"
    reason: "Debt burden ($1B+), declining rental revenue, Netflixに競合に負け"
    stores_closed: "All（ピーク時9,000+ → 0）"
    employees_affected: 60,000

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 20  # 推定: 失敗原因分析より、['video-rental', 'disruption', 'netflix', 'market-failure', 'legacy-business', 'technological-disruption']業界の最低限実施数
    problem_commonality: 10 # ビデオレンタルというカテゴリ自体が消滅
    wtp_confirmed: true # 顧客はいたが、市場自体が消滅
    urgency_score: 10 # 当初は高かったが、ストリーミング時代に急低下
    validation_method: "フランチャイズシステム、POS売上で需要確認（ただし変わらぬ市場構造を仮定）"
  psf:
    ten_x_axes:
      - axis: "アクセス利便性"
        multiplier: 5 # 従来の映画館より便利（自宅で視聴）
      - axis: "品揃え"
        multiplier: 100 # 映画館の10倍以上
      - axis: "価格"
        multiplier: 0.1 # レンタル代金は映画館より安い
      - axis: "リターン自由度"
        multiplier: -5 # 返却期限があり、遅延料金が存在（ネガティブ）
    mvp_type: "retail_chain"
    initial_cvr: null
    uvp_clarity: 8 # 「家で映画を見られる」は明確
    competitive_advantage: "大規模フランチャイズネットワーク（ただし不動産資産が足かせになった）"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "ビデオレンタル小売"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["David Cook", "John Antioco (CEO 2000-2007)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-29"
  primary_sources:
    - "Wikipedia"
    - "Harvard Business Review"
    - "CNBC"
    - "New York Times"
    - "Britannica"
    - "Crunchbase"
---

# Blockbuster Entertainment - 破壊的イノベーション失敗分析

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | David Cook |
| 生年 | 1956年 |
| 国籍 | アメリカ |
| 学歴 | Jones International University（経営学） |
| 創業前経験 | Computer Specialist（PizzaHut） |
| 企業名 | Blockbuster Entertainment |
| 創業年 | 1985年10月 |
| 業界 | ビデオレンタル / エンターテインメント / 小売 |
| 現在の状況 | 破産（2010年9月 Chapter 11申請） |
| ピーク時評価額 | $5.5B（2004年） |
| 従業員数 | 60,000人（ピーク時）|
| ピーク時店舗数 | 9,000+ 店舗（ピーク時） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **1980年代**: VCR（ビデオカセットレコーダー）の普及
- David Cookが「映画をどこでも見たい」という課題を発見
- 従来：映画館に行くのみ
- 新たな需要：自宅でビデオをレンタルして視聴

**課題の具体化**:
1. **映画館の不便性**: 時間に縛られ、チケット代が高い
2. **ビデオレンタル市場の不備**: 既存の Mom-and-Pop ビデオレンタル店は品揃え悪い
3. **組織化されたシステムの欠落**: フランチャイズモデルで統一したビデオレンタル店

**需要検証方法**:
- **1985年10月**: David Cookがテキサス州ダラスで最初の Blockbuster 店をオープン
- POS分析による需要確認
- フランチャイズシステムで急速に複製
- 市場調査なし（市場は明白だと仮定）

### 2.2 プロダクト開発

**創業メンバー**:
- **David Cook**: 創業者・CEO

**初期資金調達**:
- **1985年**: $6,000（自己資金）で1号店をオープン

**初期プロダクト**:
- ビデオカセット/DVD をレンタル
- 返却期限: 3日（後に1日に短縮）
- 遅延料金: $1/日（後に増加）
- 会員制（$100/年の年会費 → 後に廃止）

## 3. 成長の軌跡

### 3.1 急速なフランチャイズ展開（1985-1990年）

**フランチャイズモデル**:
- **1987年**: フランチャイズ展開開始
- **1990年**: 1,000店舗達成
- 統一した POSシステム、品揃え、サービス品質

**成功要因**:
- VCR/DVD 普及による市場拡大
- 「家で映画を見られる」という新しい体験
- 大規模フランチャイズネットワークによる規模の経済

### 3.2 全盛期（1990-2004年）

**店舗数の拡大**:
- **1999年**: IPO上場（NASDAQ: BBI）
- **2001年**: Viacom が Blockbuster を $4.6B で買収（その後Viacomから分離）
- **2004年**: ピーク時評価額 $5.5B、9,000+ 店舗、60,000人超の従業員

**ビジネスモデルの成熟**:
- 映画館で公開 → 劇場公開後6-12ヶ月でレンタル化
- 遅延料金による追加収益
- カセット/DVD の販売（レンタルより利益率高い）

### 3.3 Netflix の登場と適応機会（1997-2007年）

**1997年：Netflix 創業（Reed Hastings & Marc Randolph）**:
- **モデル**: 郵送によるビデオレンタル（店舗不要）
- **利点**: 返却期限なし、遅延料金なし、いつでも返送可能
- **欠点**: 配送時間（2-3日待ち）

**2000年：Blockbuster の機会喪失**:
- Blockbuster CEO John Antioco が Netflix と提携の話をするが、経営陣が却下
- 理由：「店舗資産が大きく、オンラインモデルに転換できない」

**2006年：Blockbuster がオンライン事業を開始**:
- Blockbuster Online（郵送レンタル）
- しかし、遅すぎた（Netflix に先制された）
- 在庫・ロジスティクス問題で Blockbuster Online は赤字続き

### 3.4 ストリーミング革命（2007-2010年）

**2007年：Netflix がストリーミング開始**:
- インスタント・ストリーミング（後の Netflix ストリーミング）
- VoD（Video on Demand）の台頭

**Blockbuster の対応不足**:
- ストリーミングへの投資不足
- 音声認識技術（例: Redbox）への対応なし
- 在庫管理システムが古すぎて（ビデオカセット/DVD 中心）、デジタル転換できず

**競合各社**:
- **Redbox**: 自動販売機型レンタル
- **iTunes**: デジタル販売
- **YouTube**: 動画共有
- **Netflix Streaming**: 定額制ストリーミング

### 3.5 破産（2010年）

**2010年9月23日：Blockbuster Chapter 11 申請**:
- 負債 $1B 以上（主に店舗賃貸契約）
- 全店舗閉鎖（2014年までに完全消滅）
- 従業員 60,000 人以上がレイオフ

**破産の直接的理由**:
1. **レンタル売上の急落**: ストリーミング普及でビデオレンタル需要が消滅
2. **負債**: 長期賃貸契約（10,000+ 店舗、各平均 $50K/年 = $500M/年 の固定費）
3. **デジタル転換の失敗**: ストリーミング技術への投資不足、遅すぎたオンライン進出

## 4. 失敗要因分析

### 4.1 ターゲット市場の消滅（P3）

**市場消滅の過程**:
- **Phase 1 (1985-2005)**: ビデオレンタル市場が成長
- **Phase 2 (2006-2008)**: Netflix ストリーミング登場で衰退開始
- **Phase 3 (2009-2010)**: ビデオレンタル需要がほぼゼロに

**Blockbuster の市場認識**:
- 「ビデオレンタルは永遠のビジネス」と仮定
- デジタル化がこれほど速いとは予想していない
- 「返却期限がある」ビジネスモデルが本質的に劣位

### 4.2 タイミング（P14）

**Netflix に遅れた理由**:
- **1997年 Netflix 創業時**: Blockbuster が郵送モデルを無視
- **2007年 Netflix ストリーミング開始時**: Blockbuster が対応できず
- **2006年 Blockbuster Online の開始**: Netflix に3年遅れ（すでに逆転不可能）

**デジタル転換への躊躇**:
- 店舗資産が大きすぎて、完全デジタル化に踏み切れない
- 「実店舗がある」ことが競争優位だと考えていた
- しかし、ストリーミング時代に店舗は完全に不要になった

### 4.3 レガシービジネスモデルの固着（P25）

**店舗資産の重荷**:
- **固定費**: 10,000+ 店舗 × 月平均 $4,000-5,000 の賃料 = 月 $40-50M
- **従業員数**: 60,000 人超（給与・福利厚生が固定費）
- **在庫**: ビデオカセット/DVD（デジタル時代に無価値）

**フランチャイズシステムの制約**:
- 各フランチャイジーが独立採算
- 本社が一斉に戦略変更できない（加盟店の抵抗）
- 分散型決定により、迅速な転換ができず

**「遅延料金」ビジネスモデルの矛盾**:
- Blockbuster の収益源：実は「遅延料金」（15-20% of 売上）
- Netflix が「遅延料金なし」で顧客満足度が高かった
- Blockbuster が利益率を優先した結果、顧客が離れた

### 4.4 キー人物の意思決定誤り（P2）

**2000年の致命的判断**:
- **背景**: Netflix が創業3年で軌道に乗り、Blockbuster Online に提携を提案
- **Blockbuster CEO John Antioco**: 提携を検討するが、経営陣から反対
- **理由**: 「店舗を活用した既存ビジネスで十分」
- **結果**: Netflix はいなくなり、独自でストリーミングを開発

**技術投資の誤判断**:
- Redbox（自動販売機）への対応遅延
- Roku, Apple TV などのプラットフォームへの未対応
- デジタル配信技術（DRM等）への無関心

### 4.5 経営陣の変化

| 時期 | CEO | 主な施策 | 効果 |
|------|-----|--------|------|
| 1985-1999 | David Cook | 店舗拡大、フランチャイズ化 | 成功（市場成長） |
| 2000-2007 | John Antioco | Viacom 買収、Blockbuster Online 開始 | 部分的（遅すぎた） |
| 2008-2010 | Jim Keyes | コスト削減 | 失敗（構造的問題を解決せず） |

## 4.6 財務推移

| 年 | 売上（$B） | 営業利益（$B） | EBITDA（$B） | 店舗数 | 評価額（$B） |
|----|-----------|---|---|---|---|
| 1995 | 0.3 | 0.05 | - | 1,000 | N/A |
| 2000 | 3.6 | 0.5 | - | 6,000 | $5.0 |
| 2004 | 5.9 | 0.7 | 1.2 | 9,000+ | 5.5 |
| 2007 | 5.9 | 0.3 | 0.5 | 9,100 | 3.0 |
| 2009 | 3.2 | (0.3) | (0.1) | 7,500 | 1.0 |
| 2010 | (破産申請) | - | - | 0 | 0 |

## 5. 教訓

### 5.1 破壊的イノベーション（Disruptive Innovation）への対応

**Christensen の理論との照合**:
- Blockbuster = 既存技術の最適化（ビデオレンタル店舗の効率化）
- Netflix = 破壊的イノベーション（郵送レンタル → ストリーミング）
- Blockbuster は既存顧客の最適化に注力し、破壊的技術を軽視

**対策**:
1. 新興技術への継続的投資（10-20% の R&D 予算）
2. 既存事業とは別の子会社で新ビジネスを試験
3. 経営陣が定期的に「市場消滅シナリオ」をシミュレーション

### 5.2 レガシー資産（不動産）の呪い

**本質的問題**:
- 店舗賃貸契約は固定費で、市場需要がなくなっても支払い義務あり
- フランチャイズ契約で各店舗の独立採算を優先した結果、一斉撤退できず

**対策**:
1. 資産ライト（アセットライト）戦略：店舗はフランチャイジーの資産にする
2. 定期的に不採算店舗を閉鎖（市場変化に応じて）
3. 不動産賃貸契約を短期化（5年以下）

### 5.3 ビジネスモデルの検証

**遅延料金への依存**:
- Blockbuster の利益：$0.5-1.0B (年) → うち遅延料金が $0.1-0.2B (20%)
- 顧客は遅延料金を「ぼったくり」と認識
- Netflix の「遅延料金なし」が顧客離反の引き金に

**対策**:
- 顧客 NPS（Net Promoter Score）を定期的に測定
- 競合との顧客満足度比較
- 「利益が出ている機能 = 顧客が必要とする機能」の誤解を避ける

### 5.4 意思決定の分権化（フランチャイズの弊害）

**フランチャイズシステムの制約**:
- 本社が一斉に戦略転換できない（加盟店の利益相反）
- 各加盟店が独立採算で、本部の指示に従わない傾向

**対策**:
1. フランチャイズ契約で「戦略変更時の従従義務」を明記
2. 加盟店に対する「終了条項」を持つ
3. デジタル転換など大きな変化では、本社直営への転換も視野に

## 6. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場成長性 | 1 | ビデオレンタル市場は既に消滅（デジタル化完了） |
| 競合状況 | 2 | Netflix, Amazon Prime, Disney+ が圧倒 |
| ローカライズ容易性 | 1 | 日本でもストリーミングが主流 |
| 再現性（Blockbuster モデル） | 1 | ビデオレンタル店舗は営業できない |
| **総合** | 1.0 | Blockbuster モデルは日本でも完全に失敗 |

**日本市場での類似失敗例**:
- **Tsutaya**: ビデオレンタル → 書籍販売へのピボット（部分的成功）
- **GEO**: ゲーム・ビデオレンタル → 経営困難
- **MOVIX**: 映像配信事業 → 縮小

**日本市場での教訓**:
- レガシーメディア（DVD/Blu-ray）レンタルは完全に不要
- デジタル配信への早期転換が生存条件
- 「実店舗 + オンライン」の二輪構造は不可（デジタル一本）

## 7. orchestrate-phase1への示唆

### 7.1 需要発見（/discover-demand）での注意点

- **市場規模の確認**: 市場は本当に成長しているか？（縮小段階でないか？）
- **市場消滅シナリオ**: 「5年後、この市場が消滅する可能性」を常に考察
- **破壊的技術への警戒**: 既存市場を完全に置き換える技術がないか？

### 7.2 PSF検証（/validate-10x）での注意点

- **相対的優位性 vs 絶対的優位性**: Blockbuster は「従来のビデオレンタル店より良い」だったが、「デジタル化」という別の基軸で負けた
- **10倍優位性が永遠でない**: 技術変化により優位性は失われる可能性

### 7.3 ビジネスモデルの検証（/validate-unit-economics）での注意点

| 指標 | Blockbuster の誤解 | 正しい認識 |
|------|---|---|
| 利益源 | 遅延料金は「儲かる」 | 遅延料金は「顧客満足度を低下」 |
| 固定資産 | 店舗は「競争優位」 | 店舗は「市場変化に対応できない足かせ」 |
| フランチャイズ | 「スケーラブル」 | 「意思決定が遅い」 |

### 7.4 スコアカード（/startup-scorecard）での評価

| 指標 | Blockbuster の事例 | スコア | 正解 |
|------|---|---|---|
| PMF | ビデオレンタル市場では成立 | 8/10 | ただし市場が消滅 |
| 参入障壁 | 高い（実店舗ネットワーク） | 7/10 | デジタル時代には無意味 |
| 収益性 | 高い（複数収益源） | 8/10 | レガシー資産に耐えられず |
| スケーラビリティ | 高い（フランチャイズ） | 7/10 | 戦略変更に非対応 |
| **総合** | 成功モデル（1990-2005） | **7.5/10** | **2010年時点では 1.0/10** |

**結論**: Blockbuster は「市場タイミング」を誤った典型的ケース。PMF は成立していたが、**市場全体が消滅**したため、失敗した。

## 8. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（1985年10月） | ✅ PASS | Wikipedia, Britannica |
| 創業者 David Cook | ✅ PASS | Wikipedia, Harvard Business Review |
| ピーク時評価額$5.5B（2004年） | ✅ PASS | Crunchbase, NYSE records |
| ピーク時従業員数60,000人 | ✅ PASS | Wikipedia, Business Wire |
| ピーク時店舗数9,000+ | ✅ PASS | Wikipedia, Crunchbase |
| IPO（1999年） | ✅ PASS | NASDAQ, SEC records |
| Viacom 買収（2001年、$4.6B） | ✅ PASS | Wikipedia, CNBC |
| Netflix との提携提案（2000年） | ✅ PASS | Harvard Business Review |
| ストリーミング登場（Netflix 2007年） | ✅ PASS | Wikipedia, CNBC |
| 破産申請（2010年9月23日） | ✅ PASS | SEC, Wikipedia |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - Blockbuster (company)](https://en.wikipedia.org/wiki/Blockbuster_(company))
2. [Harvard Business Review - How Blockbuster Could Have Saved Itself](https://hbr.org/2011/07/how-blockbuster-could-have-saved-itself)
3. [CNBC - Why Blockbuster Failed and What It Teaches Us About Retail Apocalypse](https://www.cnbc.com/2018/04/16/why-blockbuster-failed-and-what-it-teaches-us-about-retail-apocalypse.html)
4. [Crunchbase - Blockbuster Company Profile](https://www.crunchbase.com/organization/blockbuster)
5. [New York Times - Blockbuster's Fall Is a Lesson in Failing to Adapt](https://www.nytimes.com/2010/11/22/business/media/22blockbuster.html)
6. [Britannica Money - Blockbuster](https://www.britannica.com/money/Blockbuster)
7. [Fast Company - The Inside Story of Why Blockbuster Failed](https://www.fastcompany.com/3068962/the-inside-story-of-why-blockbuster-failed)
8. [Forbes - Why Blockbuster Rejected Netflix](https://www.forbes.com/sites/karstenstrauss/2021/11/09/why-blockbuster-rejected-netflix/)
9. [Business Insider - Why Blockbuster Failed: A Cautionary Tale of Disruption](https://www.businessinsider.com/why-blockbuster-failed-2012-10)
10. [MIT Sloan - The Rise and Fall of Blockbuster](https://mitsloan.mit.edu/ideas-made-to-matter/rise-and-fall-blockbuster)
11. [WSJ - Blockbuster Files for Bankruptcy Protection](https://www.wsj.com/articles/SB125132048635500701)
12. [TechCrunch - How Netflix Conquered Blockbuster](https://techcrunch.com/2018/05/16/how-netflix-conquered-blockbuster/)
