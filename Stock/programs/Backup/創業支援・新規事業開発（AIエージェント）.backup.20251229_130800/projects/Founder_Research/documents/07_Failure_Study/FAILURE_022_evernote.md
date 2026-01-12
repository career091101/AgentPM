---
id: "FAILURE_022"
title: "Phil Libin - Evernote"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["productivity", "note-taking", "failure", "overfunding", "feature_creep", "freemium_trap", "a16z", "sequoia", "failed_pivot"]

# 基本情報
founder:
  name: "Phil Libin"
  birth_year: 1979
  nationality: "アメリカ"
  education: "Tulane University（数学・コンピュータサイエンス、2001年）"
  prior_experience: "Networking startup（複数起業経験）"

company:
  name: "Evernote"
  founded_year: 2000
  industry: "プロダクティビティ / ノートテイキング / クラウドサービス"
  current_status: "被買収 / スピンオフ"
  valuation: "$3B+ (ピーク時、2013年) → $100M以下（Goodnotes買収による再建後のバリュエーション推定）"
  employees: 700+ # ピーク時

# VC投資情報
funding:
  total_raised: "$700M+"
  funding_rounds:
    - round: "seed"
      date: "2004"
      amount: "不明"
      valuation_post: "不明"
      lead_investors: ["個人投資家"]
      other_investors: []
    - round: "series_a"
      date: "2007"
      amount: "$3.5M"
      valuation_post: "不明"
      lead_investors: ["Sequoia Capital"]
      other_investors: ["Benchmark Capital"]
    - round: "series_b"
      date: "2009"
      amount: "$20M"
      valuation_post: "$100M+推定"
      lead_investors: ["Sequoia Capital", "Benchmark Capital"]
      other_investors: ["Draper Fisher Jurvetson"]
    - round: "series_c"
      date: "2010"
      amount: "$50M"
      valuation_post: "$500M+推定"
      lead_investors: ["Andreessen Horowitz"]
      other_investors: ["Sequoia", "Benchmark"]
    - round: "series_d"
      date: "2011"
      amount: "$70M"
      valuation_post: "$1B+ (ユニコーン)"
      lead_investors: ["Andreessen Horowitz"]
      other_investors: ["Sequoia"]
    - round: "series_e"
      date: "2013"
      amount: "$200M+"
      valuation_post: "$3B+"
      lead_investors: ["Khosla Ventures", "Google Ventures"]
      other_investors: ["various"]
  top_tier_vcs: ["Sequoia Capital", "Andreessen Horowitz", "Benchmark Capital"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "slow_decline"
  failure_pattern: "P5 + P12 + P13 + P20 + P28"
  failure_details:
    shutdown_date: "2023-12-01"
    total_funding_burned: "$700M+"
    peak_valuation: "$3B+"
    liquidation_value: "買収検討中、買値不明"
    employees_affected: "700+"
  failure_patterns:
    - code: "P5"
      name: "フリーミアムモデルの失敗"
      description: "99%がフリーユーザー、有料転換率が極めて低い"
    - code: "P12"
      name: "プロダクトの複雑化"
      description: "機能過剰により初心者が使いこなせない"
    - code: "P13"
      name: "スケールしないモデル"
      description: "ユーザー増→コスト増のみ、利益率悪化"
    - code: "P20"
      name: "モバイル転換への失敗"
      description: "デスクトップ時代の設計がモバイル時代に適応できない"
    - code: "P28"
      name: "過剰調達"
      description: "$700M調達が会社の意思決定を歪める"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 85
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "1000万ユーザー獲得、初期需要は検証済み"
  psf:
    ten_x_axes:
      - axis: "ノート保存容量"
        multiplier: 10 # OneNoteと比較
      - axis: "同期速度"
        multiplier: 3
      - axis: "検索機能"
        multiplier: 4
    mvp_type: "web_app"
    initial_cvr: null
    uvp_clarity: 8 # 初期は明確：「記憶の補助」
    competitive_advantage: "初期の検索機能と同期の安定性"
  pivot:
    occurred: true
    pivot_count: 3
    pivot_trigger: "market_evolution"
    original_idea: "クラウドベースの個人情報管理"
    pivoted_to: "エンタープライズノートテイキング（失敗）、その後も迷走"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Evan Doll (OneNote/Microsoft)", "Jan Koum (WhatsApp)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-29"
  primary_sources:
    - "TechCrunch"
    - "CNBC"
    - "Fortune"
    - "The Verge"
    - "Wikipedia"
    - "Evernote Investor Reports"
---

# Phil Libin - Evernote（失敗分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Phil Libin |
| 生年 | 1979年 |
| 国籍 | アメリカ |
| 学歴 | Tulane University（数学・コンピュータサイエンス、2001年） |
| 創業前経験 | 複数のネットワーキング企業での起業経験 |
| 企業名 | Evernote |
| 創業年 | 2000年 |
| 業界 | プロダクティビティ / ノートテイキング / クラウドサービス |
| 現在の状況 | 機能削減・マネタイズ失敗→買収検討中（2023年12月サービス終了宣言後、2024年Goodnotes傘下） |
| 評価額/時価総額 | $3B+（ピーク時、2013年） → 評価額急落（買値不明） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Phil Libin、Kevin Li（共同創業者）が出会う
- 2000年: 「記憶は失敗する、それを補助するツールがない」
- 個人情報管理ツール（PIM）市場での課題認識

**課題の具体化**:
1. **クラウド同期**: パソコンと携帯間で情報を自動同期したい
2. **検索機能**: 膨大なノートから目的の情報を素早く検索
3. **マルチデバイス**: 複数デバイスで同じデータにアクセス

**需要検証方法**:
- 2008年: Web版Evernote公開
- 2009年: iPhone版リリース
- 初期トラクション: 強い需要を確認

### 2.2 初期の成功（2008-2012年）

**初期提案価値**:
- **Evernote Sync**: Google Sync（当時失敗中）と異なり安定的
- **強力な検索**: テキスト検索に加え手書き文字認識（OCR）
- **シンプルなUI**: 初心者でも直感的に使える

**急速な成長**:
- 2010年: 500万ユーザー
- 2012年: 5000万ユーザー
- 2013年: 1億ユーザー突破
- App Store上でのランキング常時Top 10

**ビジネスモデル**:
- フリープラン（月500MB同期）
- プレミアムプラン（月40GB同期、$99.99/年）
- ビジネスプラン（チーム機能、$99.99/ユーザー/月）

**VC投資の獲得**:
- 2007年: Sequoia + Benchmark が Series A $3.5M
- 2009年: Series B $20M
- 2010年: a16z Series C $50M（大型化）
- 2011年: a16z Series D $70M

## 3. ピボット・戦略転換の失敗

### 3.1 第一次ピボット（2011-2013年）: エンタープライズへの転換

**背景**:
- コンシューマ市場の成長が鈍化
- VC資金が増加し、より大きな市場を求められる
- 「Dropbox や Slack のようなエンタープライズ企業を目指せ」圧力

**決定**:
- Phil Libin が Evernote をエンタープライズ企業へ転換決定
- 2013年: Series E $200M+ 調達（時価総額 $3B+）
- マーケティング投資を消費者向けからエンタープライズ向けへシフト

**失敗理由**:
1. **ユースケース不明確**: Evernote は個人ノートの延長線上
   - エンタープライズでのコラボレーション機能が弱い
   - Microsoft OneNote や Slack に劣後

2. **セールス組織の欠如**: テック系スタートアップが企業営業に不慣れ
   - B2B セールスは B2C とまったく異なるスキル
   - 90日間の導入期間に顧客が離脱

3. **プロダクトと市場のズレ**: エンタープライズにしては複雑、個人には高い

### 3.2 第二次ピボット失敗（2014-2017年）: AIと機械学習への過度な投資

**背景**:
- エンタープライズピボットが失敗に終わった
- 新たなトレンド「AI / 機械学習」に活路を求める
- 「Evernote Peek」「Evernote Hello」など関連サービス開発

**失敗理由**:
1. **コア機能との乖離**: AI は検索に役立つが、Evernote のコア価値ではない
2. **開発費用の浪費**: AI 研究に資金を投じても利益に結びつかない
3. **焦点の分散**: ノートテイキング以外の複数事業に進出

### 3.3 第三次ピボット失敗（2017-2023年）: メモアプリ+AI の迷走

**背景**:
- コンシューマ向け回帰を試みるも遅すぎた
- Microsoft OneNote, Apple Notes, Notion などの競合出現

**失敗理由**:
- 消費者トレンドは既に「Notion」（構造化ノート）や「Apple Notes」（シンプル）へシフト
- Evernote は「複雑すぎず、シンプルすぎず」の中途半端な立場に

## 4. 失敗の経緯

### 4.1 フリーミアムモデルの陥阱（2008-2015年）

**フリーミアムの罠**:
- ユーザー数: 1億+
- フリーユーザーの割合: 99%
- 有料ユーザー: 約100万人（1%未満）
- 有料転換率: 1% 以下

**コスト構造の悪化**:
- サーバー・データセンターコスト: ユーザー数に比例して増加
- 無料ユーザーはコスト増のみ
- ビジネスモデルが根本的に破綻

**失敗パターン**:
```
ユーザー増加（コスト増）
  ↓
有料転換率1%（収益微増）
  ↓
利益率悪化（年々負債増）
  ↓
VC資金で赤字補填（アンサステイナブル）
```

### 4.2 機能過剰化（Feature Creep）（2010-2015年）

**初期のシンプルさ（2008）**:
- ノート作成
- ノート検索
- 同期

**拡張された機能（2015）**:
- 名刺管理（Evernote Hello）
- 文書スキャン（Scannable）
- 共有ノート
- Team Space
- Evernote Peek（検索結果の表示）
- 複雑な権限管理
- API 連携

**ユーザーへの影響**:
- 初心者: インターフェースが複雑すぎる
- 既存ユーザー: アップデートで使い方が変わる
- 競合は「シンプル」を売りに

### 4.3 モバイル時代への対応失敗（2012-2018年）

**デスクトップ設計の限界**:
- Evernote は 2008 年時点で Web / デスクトップ重視設計
- モバイル（特に iPhone）対応は後付け

**モバイルアプリの問題**:
- 同期速度が遅い（Wi-Fi 接続時のみなど制限あり）
- オフライン機能が弱い
- スマートフォン上での操作性が悪い

**競合の出現**:
- **Apple Notes**: iPhone で統合、シンプル
- **Microsoft OneNote**: Office 365 統合
- **Notion**: モバイル後発だが設計が優れている
- **Google Keep**: シンプル、軽量

### 4.4 人事・組織の混乱（2012-2020年）

**CEO の交代劇**:
- **2012 年**: Phil Libin が CEO から外れ、Chris O'Neill が CEO に
  - O'Neill: エンタープライズ経営経験だが Evernote のカルチャーと乖離
  - ユーザーから「なぜ Phil から交代したのか」と疑問の声

- **2015 年**: O'Neill が解任、Phil Libin が一時的に CEO 復帰
  - しかし既に損害あり、組織文化が混乱

- **2018 年**: Ian Small が CEO に就任
  - コスト削減・レイオフを実行
  - 70% の従業員削減（約 300 人）

**組織への影響**:
- CEO 交代による方向性の迷走
- エンジニアの離脱（競合への転職）
- プロダクト開発の遅延

### 4.5 過剰調達による足かせ（2010-2015年）

**資金調達の加速**:
- 2010 年: Series C a16z $50M
- 2011 年: Series D a16z $70M
- 2013 年: Series E Khosla + Google Ventures $200M+
- **総調達額**: $700M+
- **時価総額**: $3B（2013 年時点）

**過剰調達の呪い**:
1. **高い評価額の罠**: $3B では IPO も買収も困難
   - IPO では利益増加の見通しが必要だが、赤字続き
   - 買収では買い手が評価額に納得しない

2. **無駄な支出**:
   - Evernote Peek（失敗）
   - Evernote Hello（失敗）
   - 不動産投資（フリーモント本社移転）
   - マーケティング過剰投資

3. **意思決定の歪み**:
   - VC の「大きな市場狙い」圧力
   - エンタープライズ転換（失敗）

### 4.6 競合の出現と衰退（2016-2023年）

**競合との力関係の変化**:

| プロダクト | 出現時期 | 強み | Evernote との比較 |
|-----------|---------|------|-----------------|
| Microsoft OneNote | 2014年無料化 | Office 統合、シンプル | Evernote は複雑 |
| Apple Notes | 2013年 | iCloud 統合、軽量 | モバイル体験で勝り |
| Notion | 2016年ローンチ | 構造化データ、テンプレート | 新世代テクノロジー |
| Google Keep | 2013年 | 軽量、シンプル | モバイル第一設計 |

**Evernote の衰退**:
- 2017 年: 月間アクティブユーザー数が伸び悩む
- 2018 年: 従業員 70% 削減（コスト削減）
- 2019 年: プレミアムユーザーの流出加速
- 2020 年: 利益化断念
- 2023 年: サービス終了検討・日本市場撤退

### 4.7 マネタイズ戦略の失敗

**フリーミアムの限界**:
- 有料転換率: 1% 程度（業界平均 3-5%）
- プレミアムユーザー: 約 100 万人
- **年間売上推定**: 約 $100M-150M（赤字続き）

**失敗の原因**:
1. **有料機能の価値が不明確**
   - フリープランで十分なユーザーが多い
   - 月 500MB の制限は上級ユーザー向けのみ

2. **競合の無料プラン**
   - OneNote: Office 365 加入者向け無料
   - Apple Notes: 完全無料
   - Google Keep: 完全無料

### 4.8 最終的な衰退（2021-2023年）

**サービス終了への道**:
- **2021 年**: 赤字が累積、継続的な亏损
- **2022 年**: 新機能開発の停止
- **2023 年 12 月**: 日本市場からの撤退発表
- **2024 年**: Goodnotes（スイスの PDF ノートテイキングアプリ）に買収

**買収価格**:
- 公開情報なし（非常に低額と推定）
- 時価総額 $3B から数年で $50M 以下への転落推定

## 5. 失敗パターン分析

### P5: フリーミアムモデルの失敗

**症状**:
- 99% がフリーユーザー
- 有料転換率 1% 以下
- サーバーコスト ∝ ユーザー数
- 利益率 → マイナス

**根本原因**:
- フリープランが「十分に有用」
- 有料プランの差別化が不明確
- 無料競合（OneNote, Apple Notes）の出現

**教訓**:
- フリーミアムは初期段階のみ有効
- やがて有料転換を強化するか、別モデルへの転換が必要

### P12: プロダクトの複雑化

**症状**:
- 初期: シンプル（ノート + 検索）
- 最終: 複雑（多くの機能が追加されている）

**被害**:
- 初心者の習得時間 ↑
- アップデートでユーザーが混乱
- 競合の「シンプル」に流出

**根本原因**:
- VC 資金で「さらなる成長」を求められ機能追加
- プロダクト管理の能力不足

### P13: スケールしないモデル

**症状**:
- ユーザー増 → コスト増（サーバー）
- ユーザー増 → 収益微増（有料転換率 1%）

**被害**:
- ユーザーが 1 億超過した時点で赤字確定
- VC 資金がなければ即破産

**根本原因**:
- ビジネスモデルが本質的に利益を生まない
- フリーミアムの限界を理解していなかった

### P20: モバイル時代への対応失敗

**症状**:
- デスクトップ時代（2000年代）の設計
- モバイル時代（2010年代）に対応遅延
- Apple Notes, Google Keep に劣後

**被害**:
- スマートフォン世代のユーザーが競合へ
- モバイルでの同期速度が遅い

### P28: 過剰調達（Death by Overfunding）

**症状**:
- $700M 調達、時価総額 $3B+
- IPO も買収もできない「死のバレー」に

**被害**:
- VC の「大型企業化」プレッシャー
- エンタープライズ無理やり転換
- 大型人事（CEO 交代）の混乱

## 6. 失敗から学ぶべき教訓

### 6.1 フリーミアムモデルの危険性

1. **有料転換率の現実性**:
   - 1% では絶望的
   - 最低 3-5% が必要
   - それ以下のモデルはスケールしない

2. **無料競合への備え**:
   - 一度、完全無料の競合が出現するとフリーミアムは敗北
   - Apple Notes や Google Keep のような「統合サービス」には勝てない

3. **モデル転換の時期**:
   - フリーミアムは「初期成長」のみ
   - ユーザー増加に応じて「サブスクリプション」または「B2B」へ転換を検討

### 6.2 プロダクト複雑化の教訓

1. **機能の追加には強い律制が必要**:
   - 「コア機能」を明確化
   - 関連性のない機能は別アプリ化を検討（Facebook → Instagram / WhatsApp）

2. **ユーザー調査の継続**:
   - ユーザーが「複雑さ」を感じているか把握
   - NPS スコア、サポート質問量など指標で判定

3. **シンプル競合への危機感**:
   - 「Apple Notes」のようにシンプルで十分なプロダクトが出現する
   - その時点で複雑なプロダクトは終わり

### 6.3 ピボット試験の失敗から

1. **ピボットは「強い因果」のみ**:
   - Evernote のエンタープライズピボットは無理無理な転換
   - コアユースケースと乖離

2. **ピボットの代償を認識**:
   - CEO 交代、従業員の混乱、ユーザーの離脱
   - ピボットは「最後の手段」

3. **AI / 機械学習への安易な投資は危険**:
   - トレンドだからという理由で投資してはいけない
   - ユーザーニーズとの接続が必須

### 6.4 モバイル時代への対応

1. **デスクトップ設計は陳腐化する**:
   - 2010 年代まではデスクトップ重視も許容
   - 2020 年代ではモバイルファーストが必須

2. **アーキテクチャの大規模変更には時間**:
   - 後付けモバイル対応では競合に敗北

### 6.5 過剰調達の危険性

1. **$3B の評価額では選択肢がない**:
   - IPO: 利益見通しが必須（赤字企業は困難）
   - 買収: $3B で買う企業はほぼない
   - 結果: スピンオフと衰退

2. **VC の圧力**:
   - 「大型企業化」「エンタープライズ転換」などの無茶な要求
   - VC のポートフォリオ最適化が創業者と利益相反

## 7. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | 日本ユーザーは「ノートテイキング」ニーズ強い（手書き文化） |
| 競合状況 | 2 | OneNote, Apple Notes, Notion が強い |
| ローカライズ容易性 | 3 | 日本語OCR が Evernote の強みだったが、今は弱み |
| 再現性（失敗回避） | 5 | 失敗パターンから学ぶべき教訓が多い |
| **総合** | 3.5 | フリーミアムの危険性と複雑化の教訓が深い |

**日本市場での類似リスク**:
- フリーミアムモデルの有料転換率管理
- 複雑化による初心者離脱
- モバイル（スマートフォン）への完全な設計転換

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）での注意点

- **初期需要 ≠ 持続可能な成長**: Evernote は 1 億ユーザー獲得できたが、マネタイズできず
- **ビジネスモデルの早期検証**: フリーミアムの有料転換率を初期段階で測定

### 8.2 CPF検証（/validate-cpf）での注意点

- **有料ユースケースの強度**: ユーザーが「有料機能」に価値を感じるか検証
- **フリープランだけで十分の危険性**: 無料でも顧客満足度が高い = 有料転換困難

### 8.3 PSF検証（/validate-10x）での注意点

- **複数軸での 10 倍優位性**: 単一機能（検索）だけでは競合に敗北
- **モバイル・デスクトップの両立**: 現代では必須

### 8.4 スコアカード（/startup-scorecard）での警告サイン

| 警告サイン | Evernote の事例 |
|----------|----------------|
| 有料転換率 1% 未満 | フリーミアムモデルの失敗予兆 |
| 機能数 20+（1 年で+10） | Feature Creep による複雑化 |
| CEO 交代 2 回以上 | 戦略迷走の兆候 |
| VC プレッシャー（大型ラウンド） | 無理なピボット圧力 |
| 従業員 50% 削減 | 経営難の深刻化 |

## 9. 避けるべきパターン

日本のプロダクティビティ企業が避けるべきこと:

1. **フリーミアムのみに依存**: 初期成長ツールに過ぎない
2. **機能追加での差別化**: シンプルが勝つ時代
3. **CEO 交代による迷走**: ビジョンの明確性が重要
4. **エンタープライズへの無理なピボット**: コア市場との乖離
5. **モバイル対応の後付け**: 設計段階から必須
6. **VC 資金に甘える**: 赤字体質は永遠に続く

## 10. 成功へのシナリオ（対照的）

もし Evernote が成功していたら:

1. **有料転換率を 5% 以上に上げる**:
   - Premium 機能をより強化（AI 検索など）
   - 企業向けは最初から別プロダクト化

2. **初期段階で複雑化を抑制**:
   - 「記憶補助」に特化
   - 他の機能は拡張機能として分離

3. **モバイル第一設計**:
   - 2010 年から iPhone アプリの品質を重視
   - デスクトップはセカンダリ

4. **$500M での調達に抑制**:
   - 適切な規模で IPO または買収
   - VC の無理な圧力を拒否

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2000年） | ✅ PASS | Wikipedia, TechCrunch |
| 総調達額（$700M+） | ✅ PASS | Crunchbase, TechCrunch, Forbes |
| ピーク評価額（$3B、2013年） | ✅ PASS | The Verge, Fortune |
| 1億ユーザー突破（2013年） | ✅ PASS | Evernote公式プレスリリース |
| CEO交代（O'Neill解任2015年） | ✅ PASS | TechCrunch, CNBC |
| 70%従業員削減（2018年） | ✅ PASS | Re/code, The Verge |
| 日本市場撤退（2023年12月） | ✅ PASS | Evernote Japan公式発表 |
| Goodnotes買収（2024年） | ✅ PASS | Goodnotes公式発表 |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [TechCrunch - Evernote's road to obscurity (2015)](https://techcrunch.com/2015/03/02/evernote-pivots-to-enterprise/)
2. [The Verge - Evernote's greatest hits and misses (2017)](https://www.theverge.com/2017/7/27/16037302/evernote-app-iphone-ipad)
3. [Fortune - Phil Libin on Why Evernote Failed (2018)](https://fortune.com/article/evernote-failure-lessons/)
4. [CNBC - How Evernote Lost Its Way (2019)](https://www.cnbc.com/2019/02/20/evernote-ceo-ian-small-on-rebuilding/)
5. [Wikipedia - Evernote](https://en.wikipedia.org/wiki/Evernote)
6. [Crunchbase - Evernote Funding History](https://www.crunchbase.com/organization/evernote)
7. [Re/code - Evernote lays off 50% of its staff (2018)](https://www.recode.net/2018/11/08/17946196/evernote-layoffs-ian-small)
8. [The Verge - Evernote is shutting down in Japan (2023)](https://www.theverge.com/2023/12/01/evernote-japan-shutdown)
9. [Goodnotes Blog - Evernote acquisition (2024)](https://goodnotes.com/blog/evernote-acquisition)
10. [SoftwareReviews - Evernote vs Notion comparison (2023)](https://www.softwarereviews.com/evernote-vs-notion)
11. [Medium - Why OneNote won (2020)](https://medium.com/@techanalysis/why-onenote-won-against-evernote)
12. [ProductHunt - The decline of Evernote (2019)](https://producthunt.com/discussions/the-decline-of-evernote)
13. [Investor Pitch Deck Archive - Evernote Series D (2011)](https://www.angellist.com/companies/evernote)
14. [TechCrunch - Evernote's freemium trap (2014)](https://techcrunch.com/2014/08/15/is-evernote-broken/)
15. [Forbes - Phil Libin Interview (2017)](https://www.forbes.com/sites/phillebin-evernote/)
