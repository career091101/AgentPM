---
id: "FAILURE_009"
title: "Jeffrey Katzenberg & Meg Whitman - Quibi"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["streaming", "mobile", "failure", "overfunding", "PMF", "timing", "COVID-19"]

# 基本情報
founder:
  name: "Jeffrey Katzenberg (Founder), Meg Whitman (CEO)"
  birth_year: 1950 # Katzenberg, Whitman: 1956
  nationality: "アメリカ"
  education: "Katzenberg: NYU (中退), Whitman: Princeton (経済学), Harvard Business School (MBA)"
  prior_experience: "Katzenberg: DreamWorks Animation共同創業者, Disney元幹部; Whitman: HP CEO, eBay CEO"

company:
  name: "Quibi (Quick Bites)"
  founded_year: 2018
  industry: "ストリーミング / モバイル動画 / エンタメ"
  current_status: "shutdown"
  valuation: "$1.75B（調達額）"
  employees: 200+ # シャットダウン時

# VC投資情報
funding:
  total_raised: "$1.75B"
  funding_rounds:
    - round: "seed"
      date: "2018-08"
      amount: "$1B"
      valuation_post: "不明"
      lead_investors: ["Alibaba Group", "Disney"]
      other_investors: ["21st Century Fox", "Entertainment One", "Breyer Capital", "Greenspring Associates", "JPMorgan Chase", "Liberty Global", "Lionsgate", "Madrone Capital Partners", "MGM", "NBCUniversal", "Sony Pictures Entertainment", "Goldman Sachs", "Viacom"]
    - round: "seed_2"
      date: "2020-03"
      amount: "$750M"
      valuation_post: "不明"
      lead_investors: ["Google", "Procter & Gamble"]
      other_investors: []
  top_tier_vcs: ["Goldman Sachs", "JPMorgan Chase", "Alibaba Group", "Disney", "NBCUniversal", "Sony Pictures Entertainment", "WarnerMedia", "Madrone Capital Partners"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "shutdown"
  failure_pattern: "P12 + P14 + P28"
  failure_details:
    shutdown_date: "2020-12"
    total_funding_burned: "$1.75B"
    peak_valuation: "$1.75B"
    liquidation_value: "<$100M（Rokuへコンテンツライブラリ売却）"
    employees_affected: "200+"
    months_to_failure: 6
  failure_patterns:
    - code: "P12"
      name: "PMF未達成のまま調達"
      description: "市場検証なしで$1.75B調達、実際のユーザーニーズとミスマッチ"
    - code: "P14"
      name: "タイミング問題"
      description: "COVID-19パンデミックで「移動中の暇つぶし」というコンセプトが崩壊"
    - code: "P28"
      name: "過剰調達"
      description: "$1.75Bの過剰調達が焦点分散と高コスト体質を生んだ"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0 # 市場検証なし
    problem_commonality: 50  # 推定: ['streaming', 'mobile', 'failure', 'overfunding', 'PMF', 'timing', 'COVID-19']業界標準値、市場調査データ不足
    wtp_confirmed: false
    urgency_score: 2 # 「移動中の暇つぶし」は低緊急度
    validation_method: "創業者の仮説のみ、顧客検証なし"
  psf:
    ten_x_axes:
      - axis: "コンテンツ品質"
        multiplier: 1.5 # ハリウッドレベルだが、競合も同等
      - axis: "モバイル最適化"
        multiplier: 2 # Turnstyle技術は独自だが、ユーザーには不要
      - axis: "ソーシャル機能"
        multiplier: 0.1 # シェア機能なし、TikTokに完敗
    mvp_type: "full_product"
    initial_cvr: null
    uvp_clarity: 3 # コンセプトは明確だが、市場ニーズとミスマッチ
    competitive_advantage: "ハリウッドコンテンツ、Turnstyle技術（縦横切替）"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "モバイル専用短編ストリーミング"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Meg Whitman", "Jeffrey Katzenberg"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources:
    - "Variety"
    - "CNBC"
    - "Wikipedia"
    - "Failory"
    - "Smartware Advisors"
    - "Deadline"
---

# Jeffrey Katzenberg & Meg Whitman - Quibi（失敗分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Jeffrey Katzenberg（創業者）, Meg Whitman（CEO） |
| 生年 | Katzenberg: 1950年, Whitman: 1956年 |
| 国籍 | アメリカ |
| 学歴 | Katzenberg: NYU（中退）, Whitman: Princeton（経済学）, Harvard Business School（MBA） |
| 創業前経験 | Katzenberg: DreamWorks Animation共同創業者, Disney元幹部; Whitman: HP CEO, eBay CEO |
| 企業名 | Quibi（Quick Bites） |
| 創業年 | 2018年（NewTVとして） |
| 業界 | ストリーミング / モバイル動画 / エンタメ |
| 現在の状況 | 閉鎖（2020年12月、ローンチから6ヶ月でシャットダウン） |
| 評価額/時価総額 | $1.75B（調達額）→ <$100M（清算額） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **Jeffrey Katzenberg**の仮説: 「モバイル世代は短編コンテンツを求めている」
- 移動中、待ち時間、通勤時間などの「in-between moments（隙間時間）」を狙う
- ハリウッドクオリティの短編コンテンツ（5-10分）をモバイルで提供

**課題の具体化**:
1. **長編コンテンツの視聴時間不足**: 忙しい現代人に長編は負担
2. **モバイル最適化の欠如**: 既存ストリーミングはTV向け
3. **質の低いSNS動画**: TikTok等はアマチュアコンテンツ

**需要検証方法**:
- **市場検証なし**: 創業者の仮説と経験のみ
- ユーザーインタビューなし、MVP検証なし
- **過去の成功体験に依存**: Katzenberg（DreamWorks）、Whitman（eBay, HP）

### 2.2 プロダクト開発

**コア機能**:
- **短編コンテンツ**: 5-10分のエピソード
- **モバイル専用**: スマートフォンのみで視聴可能
- **Turnstyle技術**: 縦横画面切替で異なるアングル表示

**コンテンツ戦略**:
- **超高額制作費**: 1分あたり$100,000（1時間あたり$6M）
- **ハリウッドスター**: Steven Spielberg, Jennifer Lopez, Idris Elba, Kevin Hart等
- **初年度コンテンツ予算**: $1.1B
- **175以上のオリジナルコンテンツ**: ローンチ時

**価格設定**:
- **広告あり**: $4.99/月
- **広告なし**: $7.99/月

## 3. 失敗の経緯

### 3.1 ローンチ前の異常な期待（2018-2020年）

**過剰な資金調達**:
- **2018年8月**: Seed $1B調達（投資家: Alibaba, Disney, NBCUniversal, Sony Pictures, Goldman Sachs, JPMorgan Chase等）
- **2020年3月**: 追加$750M調達（投資家: Google, Procter & Gamble等）
- **総調達額**: $1.75B（史上最大級のメディアスタートアップ調達）

**ハリウッドの期待**:
- 主要スタジオがこぞって投資
- 「次世代のストリーミングプラットフォーム」として注目
- Katzenberg/Whitmanの実績に基づく信頼

### 3.2 ローンチと即座の失敗（2020年4月）

**COVID-19パンデミックの直撃**:
- **2020年4月6日**: Quibiローンチ
- COVID-19ロックダウンで「移動中の暇つぶし」というコンセプトが崩壊
- ユーザーは在宅でNetflix, YouTube, TikTokに夢中

**初期ダウンロード数の失望**:
- **目標**: 初年度720万人の有料会員
- **実績**: ローンチ初週170万ダウンロード（一見成功）
- しかし、90日間無料トライアル終了後、解約率が急上昇
- **シャットダウン時の有料会員**: 約50万人（目標の7%）

### 3.3 根本的なプロダクト問題

**1. プロダクトマーケットフィット（PMF）の欠如**:
- **解決策を探す問題**: 「移動中の暇つぶし」は本当に問題だったのか?
- TikTok, YouTube, Instagram等の無料短編コンテンツで満足
- 有料で短編コンテンツを見る理由がない

**2. コンテンツ品質の問題**:
- **$1.1B投資したのに、記憶に残るコンテンツなし**
- バイラル化したコンテンツゼロ
- 「まあまあの品質」で話題性なし

**3. ソーシャル機能の欠如**:
- **スクリーンショット禁止**: コンテンツ保護のため
- **シェア機能なし**: SNSで拡散不可
- リアクションGIF、ミーム作成不可 → バズらない
- 現代のコンテンツ消費トレンドを無視

**4. モバイル専用の制約**:
- **TVキャスト不可**: 在宅中でも小さな画面のみ
- ユーザーからの要望を無視し続けた
- 2020年5月にようやくTVキャスト対応（手遅れ）

**5. 高額な価格設定**:
- **$4.99/月（広告あり）**: TikTok, YouTube（無料）と比較して高い
- **$7.99/月（広告なし）**: Netflix, Disney+と同等レベル
- 短編コンテンツに支払う価値なし

### 3.4 TikTokとの比較

| 項目 | Quibi | TikTok |
|------|-------|--------|
| コンテンツ哲学 | スタジオ品質 | UGC（ユーザー生成） |
| 制作費 | $100,000/分 | ほぼゼロ |
| シェア機能 | なし | 完全統合 |
| 価格 | $4.99-7.99/月 | 無料 |
| バイラル性 | ゼロ | 極めて高い |
| コミュニティ | なし | 強固 |

**TikTokの勝因**:
- 数百万のユーザーが参加、リミックス、トレンド拡散
- カルチャーエンジン（文化形成）
- アルゴリズムによるパーソナライゼーション

**Quibiの敗因**:
- 一方通行のコンテンツ配信
- ユーザー参加なし
- 現代の短編動画文化を理解していない

### 3.5 シャットダウン（2020年10月-12月）

**2020年10月21日**: シャットダウン発表
- ローンチから**わずか6ヶ月**
- CEO Meg Whitman: 「我々のアイデアは正しかったが、時期が悪かった」
- しかし、業界アナリストは「COVID-19のせいだけではない」と指摘

**資産処理**:
- **2021年1月**: コンテンツライブラリをRokuに$100M未満で売却
- **投資家への返金**: 約$350M（調達額$1.75Bの20%）
- **従業員**: 200人以上が職を失う

## 4. 失敗パターン分析

### P12: PMF未達成のまま調達

**市場検証の完全な欠如**:
- ユーザーインタビューなし
- MVP検証なし
- 創業者の仮説のみで$1.75B調達

**PMFの誤解**:
- 「移動中の暇つぶし」は本当にペインポイントか?
- TikTok, YouTube等の無料コンテンツで十分
- 有料短編ストリーミングの需要は存在しなかった

**過去の成功体験への過信**:
- Katzenberg: DreamWorks Animationの成功
- Whitman: eBay, HPでのCEO経験
- しかし、メディア市場は2018-2020年に激変していた

### P14: タイミング問題

**COVID-19の直撃**:
- ローンチ時期が最悪（2020年4月）
- 「移動中の暇つぶし」コンセプトが完全崩壊
- 在宅勤務でTikTok, Netflix, YouTubeの利用が急増

**逆説的なタイミング**:
- ストリーミングサービスは好調だった（Netflix, Disney+等）
- しかし、Quibiのコンセプト（移動中）が時代とミスマッチ
- 在宅中に小さな画面で見る理由なし

### P28: 過剰調達（Death by Overfunding）

**$1.75Bの弊害**:
- **高コスト体質**: 1分あたり$100,000の制作費
- **焦点の分散**: 175以上のコンテンツを同時制作
- **柔軟性の欠如**: 資金があるため、市場フィードバックを無視

**非効率な資金使用**:
- 初年度コンテンツ予算$1.1B
- しかし、記憶に残るコンテンツゼロ
- マーケティング費用も莫大だが、効果なし

**投資家の期待プレッシャー**:
- $1.75B調達 → 高い成長期待
- 現実的なIPOや買収の可能性低下
- ピボットやダウンサイジングの柔軟性なし

## 5. 失敗から学ぶべき教訓

### 5.1 PMF検証の重要性

1. **仮説検証なしの大規模調達は危険**:
   - 過去の成功体験は新市場では通用しない
   - 小規模MVP → 検証 → スケールの順序を守る

2. **ユーザーインタビューの必須性**:
   - 「移動中の暇つぶし」は本当に問題か?
   - 有料短編コンテンツに支払う意思はあるか?

3. **競合分析の不足**:
   - TikTok, YouTube, Instagramの無料短編動画
   - Netflix, Disney+の長編ストリーミング
   - Quibiの立ち位置が不明確

### 5.2 プロダクト設計の教訓

1. **ソーシャル機能の必須性**:
   - 現代のコンテンツはシェアされることで価値を持つ
   - スクリーンショット禁止、シェア機能なしは致命的

2. **プラットフォーム制約の危険性**:
   - モバイル専用の制約は不要
   - ユーザーが求めるのは「どこでも見られる」こと

3. **コンテンツ品質 vs バイラル性**:
   - $100,000/分の制作費 → バイラル化ゼロ
   - TikTokのUGCは低コストで極めてバイラル

### 5.3 タイミングとマーケットの教訓

1. **マーケットタイミングの重要性**:
   - COVID-19は不運だが、コンセプトが時代遅れ
   - 2018年時点で短編動画市場はTikTok, Instagramが制覇していた

2. **カルチャーの理解**:
   - 短編動画 = UGC + ソーシャル + バイラル
   - ハリウッドスタジオモデルは短編動画に不適合

### 5.4 過剰調達の危険性

1. **資金調達 != 成功**:
   - $1.75B調達が逆に会社を破壊
   - 高コスト体質、焦点分散、柔軟性欠如

2. **適正な調達額**:
   - PMF検証まで最小限の資金
   - 検証後に本格調達

## 6. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 2 | 日本でも短編動画はTikTok, YouTube Shortsが主流 |
| 競合状況 | 1 | TikTok, YouTube, LINE VOOMが強い |
| ローカライズ容易性 | 2 | コンテンツのローカライズは可能だが、PMF不足 |
| 再現性（失敗回避） | 5 | 失敗パターンから学ぶべき教訓が極めて多い |
| **総合** | 2.5 | PMF検証なしの大規模調達の典型的失敗例 |

**日本市場での類似リスク**:
- 短編動画市場はTikTok, YouTube Shortsが独占
- 有料短編ストリーミングの需要は低い
- ソーシャル機能なしのコンテンツは拡散しない

## 7. orchestrate-phase1への示唆

### 7.1 需要発見（/discover-demand）での注意点

- **創業者の仮説を盲信しない**: Katzenberg/Whitmanの経験でも市場を読み間違えた
- **既存ソリューションの検証**: TikTok, YouTube等で既に満たされている可能性
- **ペインポイントの深さ**: 「移動中の暇つぶし」は低緊急度の問題

### 7.2 CPF検証（/validate-cpf）での注意点

- **有料意思の確認**: 無料代替品（TikTok等）がある中で、本当に支払うか?
- **インタビュー必須**: 最低50-100人のターゲットユーザーに深堀り
- **WTP（支払意思額）**: $4.99/月は短編動画に対して高すぎる

### 7.3 PSF検証（/validate-10x）での注意点

- **10倍の優位性が必要**: Quibiは既存ソリューション（TikTok）に劣っていた
- **ソーシャル機能の重要性**: シェア、コメント、リミックス機能は必須
- **バイラル性**: コンテンツがバズらなければ短命

### 7.4 スコアカード（/startup-scorecard）での警告サイン

| 警告サイン | Quibiの事例 |
|----------|------------|
| PMF検証なし | ユーザーインタビューゼロ |
| 過剰調達 | $1.75B調達、PMF前に |
| 競合優位性不足 | TikTok（無料）に完敗 |
| ソーシャル機能欠如 | シェア、スクショ禁止 |
| 高価格設定 | $4.99/月、無料競合多数 |

## 8. 避けるべきパターン

日本のスタートアップが避けるべきこと:

1. **市場検証なしの大規模調達**: PMF前に$1.75Bは狂気の沙汰
2. **過去の成功体験への過信**: DreamWorks, eBayの成功 ≠ Quibiの成功
3. **ソーシャル機能の軽視**: 現代のコンテンツはシェアされることで価値を持つ
4. **競合分析の不足**: TikTokという無料で優れた競合を無視
5. **ユーザーフィードバックの無視**: TVキャスト要望を長期間無視

## 9. Jeffrey Katzenberg/Meg Whitmanのコメント

**Katzenbergのコメント（2020年10月）**:
> "COVID-19がなければ成功していた可能性がある。しかし、パンデミックは我々のコンセプトを破壊した。"

**Whitmanのコメント（2020年10月）**:
> "我々のアイデアは正しかったが、時期が悪かった。$350M以上を投資家に返金できることは幸いだ。"

**業界の反応**:
- COVID-19のせいだけではない
- PMF不足、ソーシャル機能欠如、高価格設定が主因
- 過去の成功者でも、現代のメディア市場を読み間違えた典型例

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2018年） | ✅ PASS | Wikipedia, Variety |
| 総調達額（$1.75B） | ✅ PASS | Variety, CNBC, Tracxn |
| ローンチ日（2020年4月6日） | ✅ PASS | Wikipedia, CNBC |
| シャットダウン日（2020年10月21日発表） | ✅ PASS | Variety, Deadline, CNBC |
| 有料会員数（約50万人） | ✅ PASS | CNBC, Wikipedia |
| Rokuへの売却額（<$100M） | ✅ PASS | Wikipedia, Variety |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Variety - Quibi Closes Upsized $750 Million Second Round of Funding](https://variety.com/2020/digital/news/quibi-750-million-funding-investment-mobile-video-1203523586/)
2. [Variety - Quibi Confirms Shutdown](https://variety.com/2020/digital/news/quibi-confirms-shutdown-jeffrey-katzenberg-meg-whitman-1234812643/)
3. [CNBC - Quibi founder Katzenberg, CEO Whitman explain what went wrong](https://www.cnbc.com/2020/10/22/quibi-co-founders-katzenberg-whitman-explain-what-went-wrong.html)
4. [CNBC - Quibi officially announces it's shutting down](https://www.cnbc.com/2020/10/21/quibi-to-shut-down-after-just-6-months.html)
5. [Wikipedia - Quibi](https://en.wikipedia.org/wiki/Quibi)
6. [Failory - 7 Reasons Quibi Failed Despite Raising $1.8B](https://www.failory.com/cemetery/quibi)
7. [Smartware Advisors - Case Study: Quibi & the Risks of Ignoring User Behavior](https://www.smartwareadvisors.com/pages/case-study-the-rise-and-fall-of-quibi-and-lessons-learned)
8. [Deadline - Quibi Shutdown: Jeffrey Katzenberg & Meg Whitman Exclusive Q&A](https://deadline.com/2020/10/quibi-shuts-down-jeffrey-katzenberg-meg-whitman-interview-exclusive-1234601254/)
9. [NBC News - A look at why Quibi failed so soon after launching](https://www.nbcnews.com/business/business-news/look-why-quibi-failed-so-soon-after-launching-n1244312)
10. [The Washington Post - Jeffrey Katzenberg's Quibi shutting down](https://www.washingtonpost.com/business/2020/10/21/quibi-shutting-down-katzenberg/)
11. [Humology - Quibi Case Study](https://www.humology.com/quibi-case-study)
12. [Apptunix - Why Quibi Failed in Less Than a Year: 5 Lessons to Learn](https://www.apptunix.com/blog/why-quibi-failed-in-less-than-a-year-5-lessons-to-learn/)
13. [LinkedIn - The Epic Fall of Quibi](https://www.linkedin.com/pulse/epic-fall-quibi-18b-funded-startup-shuts-down-6-months-rakesh-soni)
14. [Babson Thought & Action - The Lessons Learned from a $1.7 Billion Failure](https://entrepreneurship.babson.edu/lessons-from-billion-dollar-failure/)
15. [Tracxn - Quibi Funding Rounds & List of Investors](https://tracxn.com/d/companies/quibi/__gxSm2rJkI4JidtqdR6HPpWETfQxUnkMVquRsmuSmNWo/funding-and-investors)
