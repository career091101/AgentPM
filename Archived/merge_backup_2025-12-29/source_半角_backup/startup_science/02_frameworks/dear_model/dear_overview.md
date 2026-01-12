---
id: "FRAMEWORK_DEAR_001"
title: "DEAR Model (カスタマーサクセス)"
title_ja: "DEARモデル"
category: "framework"
type: "process"
source_book: "起業の科学"
chapter: "STEP 4"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"

tags:
  stage:
    - pmf
    - scale
  concepts:
    - customer_success
    - b2b_saas
    - churn_prevention
  related_frameworks:
    - aarrr
    - retention
  disciplines:
    - customer_success
    - account_management

framework:
  components_count: 4
  phases:
    - name: "Deployment"
      description: "導入・オンボーディング"
      duration: "0-30日"
    - name: "Engagement"
      description: "利用定着"
      duration: "30-90日"
    - name: "Adoption"
      description: "組織浸透"
      duration: "90-180日"
    - name: "ROI"
      description: "投資対効果実感"
      duration: "180日+"
  target: "各フェーズで定量KPI達成"

dependencies:
  requires:
    - CONCEPT_PMF_001
  enables:
    - CONCEPT_SCALE_001

skills:
  applicable:
    - customer_success_management
    - churn_prevention
  triggers:
    - "カスタマーサクセス"
    - "DEAR分析"

quality:
  fact_check: "pass"
  sources_count: 3
  last_verified: "2025-12-28"

priority: "high"
---

# DEAR Model (カスタマーサクセス)

> **出典**: 田所雅之「起業の科学」STEP 4、Gainsight "Customer Success Methodology"
> **関連**: [[CONCEPT_RETENTION_001]], [[FRAMEWORK_AARRR_001]]

---

## 1. 定義

**DEAR Model** は、B2B SaaSカスタマーサクセスの4段階フレームワーク。**Churn防止・LTV最大化**が目的。

**4つのフェーズ**:
```
D - Deployment（導入）
E - Engagement（エンゲージメント）
A - Adoption（組織浸透）
R - ROI（投資対効果）
```

**重要な原則**:
> 「B2B SaaSの解約は、契約時ではなく導入プロセスで決まる」
> — Lincoln Murphy, Customer Success Consultant

**適用対象**: B2B SaaS（特にACV $5K+）

---

## 2. なぜ重要か

### 2.1 Churn率への影響

**データ**:
```
DEAR完遂率とChurn率の相関:

DEAR 100%達成: Churn率 2%/年
DEAR 50%達成: Churn率 15%/年
DEAR 0%達成: Churn率 40%/年

→ DEAR成功でChurn率 1/20に削減
```

**B2B SaaSの真実**:
- 契約後30日でChurnリスク判明
- 90日以内にROI実感なし → 更新時解約90%
- First Value（初回価値体験）までの速度が生死を分ける

参照: [[CONCEPT_RETENTION_001]]

---

### 2.2 LTVへの影響

**Unit Economicsへのインパクト**:

| 指標 | DEAR成功 | DEAR失敗 | 差分 |
|------|---------|---------|------|
| **Churn率** | 2%/年 | 40%/年 | 20倍 |
| **平均契約期間** | 50ヶ月 | 2.5ヶ月 | 20倍 |
| **LTV** | $50,000 | $2,500 | 20倍 |

参照: [[TACTIC_UNIT_ECONOMICS_001]]

---

## 3. D - Deployment（導入フェーズ）

### 3.1 定義

**Deployment** = 契約からFirst Value（初回価値体験）までのプロセス

**期間**: 0-30日（理想は7日以内）

**ゴール**: ユーザーが「使える状態」になる

---

### 3.2 KPI

**必須KPI**:

| KPI | 目標値 | 測定方法 |
|-----|--------|---------|
| **Time to First Value** | 7日以内 | 契約日〜初回ログイン |
| **Onboarding完了率** | 80%+ | チュートリアル完了率 |
| **キックオフ実施率** | 100%（Enterprise） | MTG実施記録 |
| **Admin設定完了率** | 100% | 管理画面設定状況 |

---

### 3.3 Deployment成功の4ステップ

#### ステップ1: キックオフミーティング（Day 1）

**参加者**:
- 顧客: 意思決定者、管理者、エンドユーザー代表
- ベンダー: CSM、テクニカルサポート

**アジェンダ（60分）**:
```
1. 自己紹介・役割確認（10分）
2. プロジェクトゴール再確認（15分）
   - 解決したい課題
   - 成功の定義（KPI）
   - タイムライン
3. オンボーディング計画説明（20分）
   - 4週間のロードマップ
   - 各週のマイルストーン
   - サポート体制
4. Q&A（15分）
```

**成果物**: Deployment Planドキュメント

---

#### ステップ2: 技術セットアップ（Day 1-7）

**タスクリスト**:
- [ ] アカウント作成・招待
- [ ] SSO/SAML設定（Enterprise）
- [ ] データ連携（API、CSV import）
- [ ] 初期設定（ワークフロー、権限等）
- [ ] テストユーザーでの動作確認

**リスク管理**:
```
高リスク事項:
- API連携エラー（データ同期失敗）
- SSO設定トラブル（ログイン不可）
- 旧システムからの移行遅延

対策:
- 事前要件確認チェックリスト
- テクニカルサポート常時待機
- 週2回進捗確認MTG
```

---

#### ステップ3: トレーニング（Day 7-14）

**対象別トレーニング**:

| 対象 | 内容 | 時間 | 形式 |
|------|------|------|------|
| **Admin** | 管理画面、設定、レポート | 2時間 | 1on1 |
| **Power User** | 全機能、Tips、ベストプラクティス | 1時間 | グループ |
| **End User** | 基本機能、よくある操作 | 30分 | ビデオ |

**成果物**:
- トレーニング資料（スライド、動画）
- FAQ集
- クイックスタートガイド

---

#### ステップ4: First Value達成（Day 14-30）

**First Value定義例**:

| プロダクト | First Value | 測定指標 |
|-----------|------------|---------|
| **Slack** | チーム初の2,000メッセージ | メッセージ数 |
| **Salesforce** | 初の商談クローズ | 商談レコード |
| **Zoom** | 初の10人以上会議 | 参加者数 |
| **Asana** | 初のプロジェクト完了 | タスク完了数 |

**施策**:
- デイリーメール（進捗状況、次のステップ）
- プッシュ通知（マイルストーン達成）
- CSMからの個別フォローアップ

---

### 3.4 Deployment失敗の兆候

**Red Flags（危険信号）**:
- [ ] Day 7時点でログインなし
- [ ] キックオフMTG延期・キャンセル
- [ ] 管理者が設定完了していない
- [ ] トレーニング参加者ゼロ
- [ ] 質問・サポート依頼ゼロ（無関心）

**対応**: 即座にアカウント救済プラン発動

---

## 4. E - Engagement（エンゲージメントフェーズ）

### 4.1 定義

**Engagement** = 個人レベルでの継続的利用

**期間**: 30-90日

**ゴール**: デイリー/ウィークリーアクティブユーザー化

---

### 4.2 KPI

| KPI | 目標値 | 測定方法 |
|-----|--------|---------|
| **DAU/MAU比率** | 40%+ | アクティブユーザー率 |
| **Feature利用率** | 5+機能/ユーザー | 機能別利用ログ |
| **セッション時間** | 30分+/週 | 滞在時間 |
| **NPS（個人）** | 50+ | アンケート |

---

### 4.3 Engagement向上施策

#### 施策1: Personalized Onboarding

**例（Asana）**:
```
Day 30: "田中さん、先週は10タスク完了しましたね！
        チームメンバーを招待して協働してみませんか？"

Day 45: "プロジェクトテンプレート機能を使うと
        セットアップ時間が50%削減できます"
```

**効果**: エンゲージメント率 +30%

---

#### 施策2: Habit Building（習慣化）

**Nir Eyal "Hooked Model"適用**:

```
1. Trigger（きっかけ）
   - デイリーダイジェストメール（朝9時）
   - @メンション通知

2. Action（行動）
   - アプリ起動
   - タスク確認・完了

3. Reward（報酬）
   - 進捗可視化
   - チームからの承認

4. Investment（投資）
   - データ蓄積
   - チーム招待
```

**目標**: 21日間連続使用（習慣化の閾値）

---

#### 施策3: Health Score監視

**Health Scoreアルゴリズム**:

| 指標 | 配点 | 基準 |
|------|------|------|
| **ログイン頻度** | 30点 | 週3回以上 |
| **Feature利用** | 25点 | 5機能以上 |
| **データ投入** | 20点 | 100レコード以上 |
| **チーム招待** | 15点 | 3人以上 |
| **NPS** | 10点 | 7点以上 |

**判定**:
```
80点以上: Green（健全）
50-79点: Yellow（要注意）
50点未満: Red（危険）
```

**アクション**:
- Green: 自動化ナーチャリング
- Yellow: CSMメール
- Red: CSM緊急架電

---

## 5. A - Adoption（組織浸透フェーズ）

### 5.1 定義

**Adoption** = 個人利用から組織全体への拡大

**期間**: 90-180日

**ゴール**: 契約ライセンスの80%+が週次アクティブ

---

### 5.2 KPI

| KPI | 目標値 | 測定方法 |
|-----|--------|---------|
| **Seat利用率** | 80%+ | アクティブ/契約数 |
| **部門カバレッジ** | 3部門+ | 利用部門数 |
| **Power User数** | 10%+ | 週10時間+利用 |
| **Data Volume** | 10,000レコード+ | 蓄積データ量 |

---

### 5.3 Adoption加速施策

#### 施策1: Champion育成

**Champion定義**: 社内でプロダクトを布教する人

**育成プログラム**:
```
Week 1: Advanced Training（2時間）
Week 2: Admin権限付与
Week 3: 社内勉強会開催支援
Week 4: Champion認定証授与
```

**インセンティブ**:
- ベータ機能先行アクセス
- 専任サポート
- 年次カンファレンス招待

**効果**: Adoption率 +40%

---

#### 施策2: Executive Buy-in

**役員巻き込み戦略**:

**QBR（Quarterly Business Review）**:
```
参加者: 顧客役員、ベンダーCSM/営業

アジェンダ（60分）:
1. 前四半期レビュー（20分）
   - KPI達成状況
   - ROI計算
2. 課題・改善提案（20分）
   - 未達成KPI原因分析
   - 改善アクションプラン
3. 次四半期計画（20分）
   - 新機能活用
   - 拡大計画（部門・Seat）
```

**成果物**: QBRレポート、改善アクションプラン

---

#### 施策3: Viral Loop設計

**事例（Slack）**:
```
1. ユーザーA、チャンネル作成
2. @メンションで同僚Bを呼ぶ
3. B、Slackに招待される
4. Bもチャンネル作成、Cを招待
5. 指数関数的拡大
```

**設計要素**:
- 招待のハードル最小化（1クリック）
- 招待インセンティブ（機能アンロック）
- バイラル係数1.0以上

参照: [[FRAMEWORK_AARRR_001]]（Referral）

---

## 6. R - ROI（投資対効果フェーズ）

### 6.1 定義

**ROI** = 顧客が投資対効果を実感し、更新・拡大を決定

**期間**: 180日+

**ゴール**: 契約更新率95%+、Upsell/Cross-sell成功

---

### 6.2 KPI

| KPI | 目標値 | 測定方法 |
|-----|--------|---------|
| **NRR（Net Revenue Retention）** | 110%+ | (継続+拡大-解約)/期初ARR |
| **Renewal Rate** | 95%+ | 更新率 |
| **Upsell率** | 30%+ | Seat/機能拡大率 |
| **ROI Realization** | 100%達成 | 顧客KPI達成率 |

---

### 6.3 ROI実感の4要素

#### 要素1: Hard ROI（定量効果）

**計測例**:

| 業種 | Before（手作業） | After（SaaS） | ROI |
|------|----------------|--------------|-----|
| **営業管理** | 週10時間 | 週2時間 | 時間80%削減 |
| **採用** | 応募100件/月 | 応募300件/月 | 応募3倍 |
| **マーケ** | CVR 1% | CVR 3% | CVR 3倍 |

**計算式**:
```
年間ROI = (年間削減コスト - SaaS年額) / SaaS年額 × 100

例:
削減コスト: $100,000（人件費換算）
SaaS年額: $20,000

ROI = ($100,000 - $20,000) / $20,000 × 100 = 400%
```

---

#### 要素2: Soft ROI（定性効果）

**例**:
- 従業員満足度向上（NPS +20）
- ブランド向上（顧客満足度調査で高評価）
- 意思決定速度向上（データドリブン化）

---

#### 要素3: Success Story作成

**事例インタビュー（30分）**:
```
1. 導入前の課題（5分）
2. 選定理由（5分）
3. 導入プロセス（5分）
4. 達成した成果（10分）←最重要
5. 今後の展望（5分）
```

**活用**:
- Webサイト掲載
- 営業資料
- カンファレンス登壇

---

#### 要素4: Executive Sponsorship

**役員レベルでのROI報告**:

**年次ビジネスレビュー**:
```
参加者: 顧客CXO、ベンダーVP/C-level

アジェンダ（90分）:
1. 年間総括（30分）
   - 定量ROI報告
   - 主要成果
2. 戦略的価値提案（30分）
   - 次年度ロードマップ
   - 新機能による追加価値
3. 拡大計画（30分）
   - 他部門展開
   - Enterprise契約アップグレード
```

---

## 7. DEAR進捗管理

### 7.1 DEARダッシュボード

**顧客セグメント別**:

| セグメント | D完了 | E達成 | A達成 | R達成 | Health |
|----------|------|------|------|------|--------|
| Enterprise A社 | ✅ | ✅ | ✅ | ⏳ | Green |
| SMB B社 | ✅ | ⚠️ | ❌ | ❌ | Yellow |
| Startup C社 | ⏳ | ❌ | ❌ | ❌ | Red |

**アクション優先度**: Red > Yellow > Green

---

### 7.2 フェーズ別Playbook

**Deployment Playbook**:
```
Week 1:
- Day 1: キックオフMTG
- Day 3: 技術セットアップ完了確認
- Day 7: Admin Training

Week 2:
- Day 10: End User Training
- Day 14: First Value達成確認

Week 3-4:
- 継続利用促進
- 課題ヒアリング
```

**Engagement Playbook**:
```
Month 2:
- Week 1: Health Score測定開始
- Week 2: Feature利用促進キャンペーン
- Week 3: 個別フォローアップ（Yellow/Red）
- Week 4: NPS調査

Month 3:
- 同上 + Champion候補特定
```

---

## 8. Churn予兆検知

### 8.1 Early Warning Signals

**Red Flags（30-60日前）**:

| シグナル | 深刻度 | アクション |
|---------|-------|-----------|
| **ログイン激減** | 高 | 即架電 |
| **Champion退職** | 高 | 後任者フォロー |
| **サポート問い合わせ急増** | 中 | 課題ヒアリング |
| **NPS低下** | 中 | 満足度調査 |
| **契約更新MTG延期** | 高 | 役員エスカレーション |

---

### 8.2 Win-back施策

**解約申し出時の対応**:

```
Step 1: 理由ヒアリング（48時間以内）
  - 価格？機能不足？サポート不満？
  - 競合？内製？

Step 2: Retention Offer
  - 価格: 20-30%割引オファー
  - 機能: カスタム開発提案
  - サポート: 専任CSM配置

Step 3: Executive介入
  - VP/C-level架電
  - 特別条件提示

成功率: 30-50%
```

---

## 9. 成功事例

### 9.1 Gainsight（DEAR発案企業）

**顧客（SaaS企業A）のDEAR実施結果**:

```
Before DEAR:
- Churn率: 25%/年
- NRR: 85%
- Deployment期間: 60日

After DEAR:
- Churn率: 5%/年（1/5に削減）
- NRR: 120%（拡大成功）
- Deployment期間: 14日（1/4に短縮）
```

**ROI**: CSチーム投資の10倍のChurn削減効果

---

### 9.2 Slack

**DEAR適用例**:

```
D（Deployment）:
- 目標: 2,000メッセージ
- 施策: チーム招待促進、インテグレーション設定支援
- 達成率: 85%（7日以内）

E（Engagement）:
- 目標: DAU/MAU 60%+
- 施策: デイリーダイジェスト、プッシュ通知
- 達成率: 75%

A（Adoption）:
- 目標: Seat利用率90%+
- 施策: チャンネル文化醸成、Executive Slack導入
- 達成率: 93%

R（ROI）:
- 顧客実感: メール90%削減、意思決定速度3倍
- NRR: 130%+
```

---

## 10. よくある間違い

| 間違い | 症状 | 対策 |
|--------|------|------|
| **Deployment放置** | 契約後フォローなし | キックオフ必須化 |
| **全顧客均一対応** | リソース浪費 | セグメント別Playbook |
| **Churn後対応** | 手遅れ | 予兆検知・早期介入 |
| **ROI未測定** | 更新時交渉力なし | 定量ROI計算 |
| **CSM不在** | 自動化のみ依存 | ハイタッチCS配置 |

---

## 11. セグメント別DEAR戦略

### 11.1 Enterprise（ACV $50K+）

**アプローチ**: High-touch CS

| フェーズ | 施策 | CSM工数 |
|---------|------|---------|
| D | 専任CSM、週次MTG | 40h |
| E | カスタムTraining | 20h |
| A | QBR、Executive介入 | 10h/四半期 |
| R | 年次ビジネスレビュー | 20h/年 |

**CSM:顧客比率**: 1:10

---

### 11.2 SMB（ACV $5K-50K）

**アプローチ**: Tech-touch CS

| フェーズ | 施策 | 自動化率 |
|---------|------|---------|
| D | 自動メール、セルフサービス | 80% |
| E | プロダクト内ガイド | 90% |
| A | Webinarグループ | 70% |
| R | 自動ROIレポート | 100% |

**CSM:顧客比率**: 1:100

---

### 11.3 Self-serve（ACV <$5K）

**アプローチ**: Low-touch/No-touch CS

**完全自動化**:
- プロダクト内オンボーディング
- 自動メールナーチャリング
- セルフサービスサポート

**CSM介入**: Churn予兆時のみ

---

## 12. ツール

| ツール | 用途 | 価格 |
|--------|------|------|
| **Gainsight** | DEAR管理、Health Score | $$$（Enterprise） |
| **ChurnZero** | CS自動化 | $$（SMB向け） |
| **Totango** | Health監視 | $$ |
| **Intercom** | プロダクト内メッセージ | $ |
| **Pendo** | プロダクト分析 | $$ |

---

## 13. 関連概念

| 概念 | 関係性 | リンク |
|------|--------|--------|
| Retention | DEAR成功でRetention向上 | [[CONCEPT_RETENTION_001]] |
| AARRR | Activation/Retention該当 | [[FRAMEWORK_AARRR_001]] |
| NPS | R（ROI）フェーズで測定 | [[CONCEPT_NPS_001]] |
| Unit Economics | Churn削減でLTV向上 | [[TACTIC_UNIT_ECONOMICS_001]] |
| PMF | DEAR前提にPMF必要 | [[CONCEPT_PMF_001]] |

---

## クイックリファレンス

```
定義: B2B SaaSカスタマーサクセス4段階
目的: Churn防止、LTV最大化

4フェーズ:
D - Deployment（0-30日）
  KPI: Time to First Value 7日以内

E - Engagement（30-90日）
  KPI: DAU/MAU 40%+

A - Adoption（90-180日）
  KPI: Seat利用率 80%+

R - ROI（180日+）
  KPI: NRR 110%+

セグメント別戦略:
- Enterprise: High-touch CS（CSM 1:10）
- SMB: Tech-touch CS（CSM 1:100）
- Self-serve: Low/No-touch CS

Churn予兆検知:
- ログイン激減
- Champion退職
- NPS低下
→ 30-60日前に察知、即介入

成功指標:
- Churn率 2-5%/年
- NRR 110%+
- Renewal Rate 95%+

重要な原則:
「B2B SaaSの解約は導入時に決まる」
「First Value到達までの速度が生死を分ける」
```

---

**ファイル情報**
- 作成日: 2025-12-28
- 最終更新: 2025-12-28
- バージョン: 1.0
