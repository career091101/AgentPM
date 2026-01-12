---
id: "FOUNDER_012"
title: "Travis Kalanick - Uber"
category: "founder"
tier: "legendary"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: [Ride-sharing, Marketplace, Two-sided Platform, Aggressive Growth, Disruption]

# 基本情報
founder:
  name: "Travis Kalanick"
  birth_year: 1976
  nationality: "American"
  education: "UCLA (Computer Engineering, dropout)"
  prior_experience: "Scour創業者（ファイル共有）、Red Swoosh創業者（P2P）"

company:
  name: "Uber"
  founded_year: 2009
  industry: "Ride-sharing / Transportation"
  current_status: "active (IPO 2019)"
  valuation: "$70B+ (ピーク時)"
  employees: 30000

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 95
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "招待制MVP・ドライバー直接ヒアリング"
  psf:
    ten_x_axes:
      - axis: "利便性"
        multiplier: 10
      - axis: "信頼性"
        multiplier: 5
      - axis: "コスト透明性"
        multiplier: 10
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 10
    competitive_advantage: "両面マーケットプレイス・アプリベース配車・動的価格設定"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "高級ブラックカーから一般配車へ"
    original_idea: "UberBlack（高級車配車）"
    pivoted_to: "UberX（一般車配車）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Garrett Camp", "Ryan Graves", "Dara Khosrowshahi"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia"
    - "Britannica"
    - "Bloomberg"
    - "CNN Money"
    - "Harvard Digital Initiative"
---

# Travis Kalanick - Uber

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Travis Kalanick |
| 生年 | 1976年8月6日 |
| 国籍 | アメリカ人 |
| 学歴 | UCLA（コンピュータエンジニアリング）中退 |
| 創業前経験 | Scour創業（$250B訴訟で破綻）、Red Swoosh創業（$19Mで売却） |
| 企業名 | Uber Technologies, Inc. |
| 創業年 | 2009年 |
| 業界 | ライドシェア / 交通 |
| 現在の状況 | 上場（2019年IPO） |
| 評価額/時価総額 | ピーク時$70B+、2019年IPO時$82B |

## 2. 創業ストーリー

### 2.1 創業前の経験（Red Swoosh経験）

**Scour（1998-2000）**:
- UCLAの同級生と共に創業したファイル共有サービス
- 映画・音楽のオンライン共有で人気を博す
- MPAA、RIAA、NMPAから$250Bの著作権侵害訴訟
- 2000年9月にChapter 11破産申請

**Red Swoosh（2001-2007）**:
- Scour閉鎖の4ヶ月後に創業
- 「復讐のビジネス」と呼ばれた P2Pファイル共有会社
- 2011年のFailConで「最も運の悪い起業家」と自称
- 課題: IRSとの問題、共同創業者との対立、エンジニアのGoogle引き抜き
- 資金節約のため実家に戻り、2006年にはタイに移住
- 2007年にAkamai Technologiesに$19Mで売却

**学び**:
- 投資家とのコントロール争いの重要性を痛感
- 「粘り強さ」と「諦めない精神」の醸成
- 規制との戦い方を学習

### 2.2 課題発見（需要発見）

**着想源**:
- Garrett Camp（StumbleUpon共同創業者）がサンフランシスコでタクシーを拾えないフラストレーション
- 高級ブラックカーサービスは不便で高価
- Taxi Magic、Cabulousなど既存サービスは機能不十分

**問題の明確化**:
- サンフランシスコでタクシーを便利に呼ぶ方法がない
- 価格が不透明、到着時間が不明確
- 支払いプロセスが面倒

**着想の経緯**:
- CampはKalanickの自宅（通称「JamPad」）の常連
- JamPadはCastro Districtにある非公式なテックサロン
- 2009年、スマートフォンアプリで高級車を直接呼べるコンセプトを開発

### 2.3 CPF検証（Customer Problem Fit）

**サプライサイド検証**:
- Kalanickが直接リムジンドライバーに電話でコンセプトを説明
- 10人中3人が「参加したい」と回答
- この結果でアイデアの検証完了と判断

**デマンドサイド検証**:
- 当初は招待制のみでアプリを提供
- ユーザーはKalanickに直接メールを送り、承認されればアクセスコードを取得
- このモデルでダウンロード数が増加 → ソリューションが機能することを確認

**価格設定検証**:
- 既存のブラックカーサービスより低価格で提供
- 「すでに電話でリムジンを予約する人がいる」という前提で需要テストを省略
- より安価で便利な代替手段として市場需要を確認

### 2.4 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | タクシー（従来） | Uberソリューション | 倍率 |
|---|------------|-----------------|------|
| 利便性 | 手を挙げる/電話 | ワンタップで呼べる | 10倍 |
| 信頼性 | いつ来るか不明 | リアルタイム追跡 | 5倍 |
| 価格透明性 | メーターのみ | 事前に見積もり表示 | 10倍 |
| 支払い | 現金/旧式カード | アプリ内自動決済 | 10倍 |
| 品質管理 | なし | 相互評価システム | 新規 |

**Uberがタクシー市場を超えた成長**:
- サンフランシスコの従来タクシー市場: 年間$140M
- Uberの同市場売上: 年間$500M（3倍以上）
- さらに年間3倍のペースで成長 → 従来市場の10倍規模へ

**効率性の優位**:
- UberXドライバーは乗客乗車時間の割合がタクシーより大幅に高い
- 要因: 効率的なマッチング技術、規模の経済、柔軟な労働供給、サージプライシング

**MVP（Minimum Viable Product）**:
- 最初のバージョンは「UberCab」として3台のメルセデスでローンチ
- シンプルな機能: 車を呼ぶ、位置追跡、自動支払い
- 反復的に機能追加

**UVP（独自の価値提案）**:
- 「タップ一つで車が来る」
- 「水道水のように簡単に交通手段にアクセス」

## 3. 成長戦略

### 3.1 都市展開プレイブック

**初期展開**:
1. サンフランシスコ
2. ニューヨーク
3. シアトル
4. シカゴ
5. ボストン（この頃からプレイブックを体系化）

**ローンチプロセス**:
1. 本社から「City Launcher」を派遣
2. Craigslistに数百ドルのボーナス付きドライバー募集広告を大量投稿
3. 無料乗車で顧客獲得
4. 需要が立ち上がったらローカルの「City Manager」を採用
5. 事前告知なしに突然ローンチ → 当局が反応する前に定着

**内部競争文化**:
- 複数のLauncherが都市ローンチの速さを競争
- 数週間で新都市を稼働させることが可能に
- 競争がプレイブックの改善を促進

**City Managerの自律性**:
- 成長目標を達成する限り、数百万ドルのインセンティブを本社承認なしで使用可能
- ローカル市場を最も理解している現地マネージャーに権限委譲
- 2015年時点で年間$2Bをドライバー・乗客インセンティブに投資

**規制への対応**:
- 規制を回避し、規制当局と戦う姿勢がDNAに組み込まれていた
- ドライバーが違反切符を切られても路上に残るよう指示
- 罰金・違反切符は「ビジネスコスト」として会社が負担
- Greyballツールで当局に偽のアプリ画面を表示（後に問題化）

### 3.2 フライホイール

```
ドライバー増加 → 待ち時間短縮 → 乗客満足度向上 → 乗客増加 → ドライバー収入増加 → ドライバー増加
                           ↓
                        口コミ拡大
                           ↓
                        新市場展開
```

### 3.3 アセットライトモデル

- 自社で車両を保有しない
- ドライバーは従業員ではなく独立契約者
- 高いスケーラビリティ
- 2010年のローンチ以降、$25B以上のVC資金調達
- 米国ライドシェア市場の68%シェア獲得

## 4. 失敗・課題とCEO退任

### 4.1 2017年の危機

**Susan Fowlerの告発（2017年2月）**:
- 元Uberエンジニアがブログで性差別・セクハラを告発
- HR部門が問題を無視していたと主張
- 「Bro Culture」（男性優位文化）の存在が明らかに

**その他のスキャンダル**:
- Lyftからドライバーを引き抜くため、競合の乗車を注文・キャンセル
- Greyballで当局を欺く行為が発覚
- 自動運転車の知的財産訴訟（Waymo vs Uber）
- Kalanick自身がUberドライバーと運賃について口論する動画がリーク

**Eric Holder調査**:
- 元司法長官による内部調査を実施
- 広範なセクハラ・性差別の存在を確認
- 取締役会が行動を起こさざるを得なくなる

### 4.2 CEO退任（2017年6月）

**経緯**:
- 主要投資家Benchmark Capitalからの圧力
- 「私が一歩引いて、Uberが次の章に進む時が来た」と辞任
- 辞任後も取締役として残留（後に2019年に退任）

**Kalanick自身の反省**:
- 「会社が成長するにつれ、生き残りと偉大な会社を築くために役立った多くのことにしがみついていた。しかしそれらはスケールすると負債になっていった」

### 4.3 教訓

1. **文化の重要性**: 有害な職場文化は最終的に財務パフォーマンスに影響
2. **成功への対処法**: 生き残りスキルと成功時のスキルは異なる
3. **倫理的境界**: 業界規範に挑戦することと、法律や基本的な人間の尊厳を無視することは別
4. **コントロールの二面性**: 投資家からのコントロールを守ることに執着しすぎた結果、監督機能が弱体化

## 5. Uber後の活動（CloudKitchens）

### 5.1 概要

- 2018年にCloudKitchensを設立
- ゴーストキッチン（デリバリー専用キッチン）のインフラ提供
- 現在の評価額: $15B
- 30カ国で数百のキッチンユニットを運営

### 5.2 事業構成

| 事業 | 概要 |
|------|------|
| CloudKitchens | ゴーストキッチン不動産・運営 |
| Otter | デリバリー注文統合ソフトウェア（米国取引の18%を処理） |
| Lab37 | ロボティクス部門（「Bowl Builder」で1時間200食） |
| Picnic | 職場向けスマートフードロッカー |
| Future Foods | バーチャルレストランブランドのライセンス |

### 5.3 ビジョン

- 「Internet Food Court」コンセプト（2024年発表）
- 自動化による15分以内配達を目指す
- 「調理のサービス化」（Cooking-as-a-Service）
- 「健康的な食事を富裕層だけでなくすべての人に」

## 6. 使用ツール・サービス

| カテゴリ | ツール/アプローチ |
|---------|-----------------|
| 初期検証 | 招待制アプリ、直接電話ヒアリング |
| 成長 | プレイブック化、City Manager制度 |
| 採用 | Craigslist大量広告 |
| 規制対応 | 法的費用を「ビジネスコスト」として計上 |
| 資金調達 | 議決権10倍構造で創業者コントロール維持 |

## 7. 成功要因分析

### 7.1 主要成功要因

1. **明確な10倍優位性**: タクシーより圧倒的に便利
2. **プレイブック化**: 都市展開を再現可能なプロセスに
3. **積極的な資金調達**: $25B+のVC資金で競合を圧倒
4. **City Manager自律性**: ローカルへの権限委譲

### 7.2 失敗要因

1. **有害な企業文化**: 「勝利至上主義」が行き過ぎ
2. **規制軽視**: 法律・倫理の境界を越えすぎた
3. **監督機能の欠如**: 投資家からのコントロール保護が裏目に
4. **成長優先の限界**: 「Growth at all costs」の副作用

### 7.3 タイミング要因

- スマートフォンの普及（iPhone 2007年、アプリストア2008年）
- GPS技術の成熟
- ギグエコノミーの台頭
- タクシー業界の変革への抵抗（規制による独占状態）

## 8. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | タクシーアプリは普及、ライドシェアは規制 |
| 競合状況 | 3 | JapanTaxi、DiDiなど存在 |
| ローカライズ容易性 | 2 | 規制が厳しく参入障壁高い |
| 再現性 | 3 | プレイブック手法は参考になる |
| **総合** | 2.75 | 規制環境が大きく異なり直接再現困難 |

## 9. orchestrate-phase1への示唆

### 9.1 需要発見（/discover-demand）

- **示唆**: 自分自身が経験した「フラストレーション」から始める
- **適用**: 創業者が毎日感じる不便を探す

### 9.2 CPF検証（/validate-cpf）

- **示唆**: サプライサイドとデマンドサイドを別々に検証
- **適用**: 10人中3人が「やりたい」で十分と判断（サプライ側）
- **適用**: 招待制でデマンドを段階的に検証

### 9.3 PSF検証（/validate-10x）

- **示唆**: 既存市場の10倍の価値を創出できれば新市場を創造
- **適用**: サンフランシスコでタクシー市場の3倍超え → 最終的に10倍

### 9.4 スコアカード（/startup-scorecard）

- **示唆**: 成長と文化のバランスを意識的に設計
- **適用**: 成功時のスキルは生き残り時とは異なることを認識

## 10. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **B2Bデリバリー最適化**: CloudKitchens型のゴーストキッチンインフラ
2. **規制対応型モビリティ**: 日本の法規制に適合したライドシェア代替
3. **City Manager型展開**: 地方都市特化のサービス展開プレイブック

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| Scour $250B訴訟 | 正確 | Wikipedia |
| Red Swoosh $19M売却 | 正確 | Britannica |
| 2009年Uber創業 | 正確 | 複数ソース |
| 2017年6月CEO退任 | 正確 | CNN Money |
| CloudKitchens $15B評価額 | 正確 | TechCrunch (2024) |

## 参照ソース

1. [Travis Kalanick - Wikipedia](https://en.wikipedia.org/wiki/Travis_Kalanick)
2. [Travis Kalanick | Britannica Money](https://www.britannica.com/money/Travis-Kalanick)
3. [Uber vs. Taxi - Harvard Digital Initiative](https://d3.harvard.edu/platform-digit/submission/uber-vs-taxi/)
4. [The rise and fall of Uber CEO Travis Kalanick - CNN Money](https://money.cnn.com/2017/06/21/technology/uber-ceo-travis-kalanick-timeline/index.html)
5. [Uber's International Launch Playbook - Bloomberg](https://www.bloomberg.com/news/articles/2014-11-20/ubers-international-launch-playbook-includes-some-tough-lessons)
6. [Uber MVP - Dittofi](https://www.dittofi.com/learn/uber-mvp)
7. [How Uber Used a Simplified Business Model - Entrepreneur](https://www.entrepreneur.com/growing-a-business/how-uber-used-a-simplified-business-model-to-disrupt-the/286683)
8. [Travis Kalanick CEO Resignation - CEO Today](https://www.ceotodaymagazine.com/2025/04/booted-from-his-own-empire-travis-kalanick-and-the-fall-of-ubers-toxic-titan/)
9. [CloudKitchens - Wikipedia](https://en.wikipedia.org/wiki/CloudKitchens)
10. [Travis Kalanick's Vision for Restaurants - Restaurant Spaces](https://info.restaurantspacesevent.com/blog/travis-kalanicks-vision-for-the-future-of-restaurants)
11. [All-In Summit 2024 - Travis Kalanick Interview](https://podcastnotes.org/all-in-podcast/in-conversation-with-travis-kalanick-cloudkitchens-strategy-at-uber-being-a-war-time-ceo-and-competing-in-china-all-in-summit-2024/)
12. [Learning From Uber's Mistakes - Stanford GSB](https://www.gsb.stanford.edu/insights/learning-ubers-mistakes)
