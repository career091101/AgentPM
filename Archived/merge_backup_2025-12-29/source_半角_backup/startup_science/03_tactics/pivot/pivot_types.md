---
id: "TACTIC_PIVOT_001"
title: "Pivot Decision Framework (ピボット判断)"
title_ja: "ピボット10類型と判断基準"
category: "tactic"
type: "framework"
source_book: "起業の科学"
chapter: "STEP 3"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"

tags:
  stage:
    - psf
    - pmf
  concepts:
    - pivot
    - validation
    - iteration
  related_frameworks:
    - lean_startup
    - psf
  disciplines:
    - product_strategy
    - business_model

tactic:
  pivot_types_count: 10
  decision_criteria:
    - "PSF未達成が6ヶ月以上継続"
    - "コア仮説が否定された"
    - "市場規模が想定の1/10以下"
    - "競合優位性が構築不可能"
  timing: "早ければ早いほど良い"
  principle: "Data-driven decision"

dependencies:
  requires:
    - CONCEPT_PSF_001
    - CONCEPT_CPF_001
  enables:
    - CONCEPT_PMF_001

skills:
  applicable:
    - pivot_decision
    - hypothesis_testing
  triggers:
    - "ピボット判断"
    - "方向転換"

quality:
  fact_check: "pass"
  sources_count: 3
  last_verified: "2025-12-28"

priority: "high"
---

# Pivot Decision Framework (ピボット判断)

> **出典**: 田所雅之「起業の科学」STEP 3、Eric Ries "The Lean Startup"
> **関連**: [[CONCEPT_PSF_001]], [[CONCEPT_PMF_001]]

---

## 1. 定義

**Pivot（ピボット）** は、スタートアップが検証プロセスで学んだことを元に、戦略の一部または全体を変更すること。

**重要な原則**:
> 「Pivot（方向転換）は失敗ではなく、学習の証明である」
> — Eric Ries

**Pivot vs Persevere（忍耐）の判断**:
- データに基づいて判断
- 感情や執着を排除
- 早期判断が生存確率を上げる

---

## 2. なぜ重要か

### 2.1 生存確率向上

**統計データ**:
```
Pivot経験スタートアップ:
- 0回: 成功率 10%
- 1-2回: 成功率 40%
- 3-5回: 成功率 60%

※ただし6回以上は資金枯渇リスク
```

**理由**:
- 初期仮説が100%正しいことはほぼない
- 市場からのフィードバックが最重要
- Pivotは学習速度の証明

---

### 2.2 資源の最適配分

**Pivot判断のタイミング**:

| タイミング | コスト | リスク | 推奨度 |
|-----------|--------|--------|--------|
| **1-3ヶ月** | 低 | 低 | ✅ 最適 |
| **6ヶ月** | 中 | 中 | ⚠️ やや遅い |
| **1年+** | 高 | 高 | ❌ 手遅れリスク |

**コスト比較**:
```
3ヶ月でPivot: $50K消費、チーム士気◎
1年でPivot: $500K消費、チーム疲弊、創業者の機会コスト大
```

---

## 3. Pivot判断の5つのシグナル

### シグナル1: CPF/PSF指標の停滞

**判断基準**:

| 指標 | 警告ライン | Pivot検討ライン |
|------|-----------|----------------|
| **3U平均スコア** | <7.0点 | <5.0点（3ヶ月改善なし） |
| **インタビュー** | 30件で肯定10件未満 | 50件で肯定15件未満 |
| **MVP反応** | CVR <1% | CVR <0.3%（改善なし） |
| **NPS** | <30 | <10（3ヶ月改善なし） |

参照: [[CONCEPT_CPF_001]], [[CONCEPT_PSF_001]]

---

### シグナル2: コア仮説の否定

**例**:
```
仮説: 「飲食店は予約管理に1万円/月払う」
検証結果: 50店舗中、支払意思あり0店舗

→ Value Capture Pivotが必要（後述）
```

**判断フロー**:
1. コア仮説を明文化
2. 検証結果と比較
3. 統計的有意性判断（サンプル数30+）
4. 否定されたらPivot

---

### シグナル3: 市場規模の誤算

**TAM再計算**:
```
当初想定:
- ペルソナ: 中小飲食店（10万店）
- 単価: 1万円/月
- TAM: 120億円/年

再検証:
- 実際の支払意思: 個人経営のみ（2万店）
- 実際の支払額: 3千円/月
- 実TAM: 7.2億円/年

→ Customer Segment Pivotが必要
```

**判断基準**: 実TAMが想定の1/10以下 → Pivot検討

---

### シグナル4: 競合優位性の欠如

**チェック項目**:
- [ ] 10倍の価値提供ができない
- [ ] 差別化が模倣容易
- [ ] ネットワーク効果なし
- [ ] スイッチングコストなし

**3つ以上該当 → Pivot検討**

参照: [[TACTIC_10X_001]]

---

### シグナル5: チーム士気・資金状況

**警告サイン**:
```
チーム士気:
- 創業者の情熱喪失
- メンバーの離脱
- 毎日が苦痛

資金状況:
- Runway 6ヶ月未満
- 次回調達の見込みなし
```

**対策**: 小さくても勝てる領域へPivot

---

## 4. Pivot 10類型

### 4.1 Zoom-in Pivot（機能特化型）

**定義**: プロダクトの1機能に特化

**事例（Instagram）**:
```
Before: Burbn（位置情報SNS、11機能）
データ: 写真シェアのみ使用率80%
After: Instagram（写真シェア特化）
結果: 2ヶ月で100万ユーザー
```

**判断基準**:
- 1機能の使用率が他の10倍以上
- その機能でNPS 50+

**実行手順**:
1. 機能別使用率分析
2. 最も使われる1機能特定
3. 他機能を全削除
4. UI/UX最適化

---

### 4.2 Zoom-out Pivot（機能拡張型）

**定義**: 1機能を包括的プロダクトへ拡張

**事例（Slack）**:
```
Before: ゲーム開発の内部チャットツール
データ: ゲーム失敗、チャットツールの評判◎
After: Slack（ビジネスチャットプラットフォーム）
結果: 評価額$27B
```

**判断基準**:
- 単機能では収益化困難
- 周辺ニーズが大きい

---

### 4.3 Customer Segment Pivot（顧客セグメント変更）

**定義**: ターゲット顧客を変更

**事例（Slack再び）**:
```
Before: ゲーム開発チーム向け
データ: ゲーム会社は小規模市場
After: 全企業向けビジネスチャット
結果: TAM 100倍に拡大
```

**判断基準**:
- 当初セグメントのTAM小さい
- 別セグメントで10倍の反応

**実行手順**:
1. 既存ユーザー分析（意外なセグメント発見）
2. インタビュー30件/新セグメント
3. MVP投入
4. PMF判定

参照: [[TACTIC_PERSONA_001]]

---

### 4.4 Customer Need Pivot（課題変更）

**定義**: 同じ顧客の別の課題を解決

**事例（YouTube）**:
```
Before: 動画デートサイト
データ: デート需要なし、動画共有需要◎
After: 動画共有プラットフォーム
結果: Googleが$1.65Bで買収
```

**判断基準**:
- 当初課題の3Uスコア低い
- インタビューで別の課題が浮上

---

### 4.5 Platform Pivot（プラットフォーム化）

**定義**: アプリ → プラットフォーム、またはその逆

**事例（Twitter）**:
```
Before: Odeo（Podcastプラットフォーム）
データ: iTunes Podcastに敗北
After: Twitter（マイクロブログアプリ）
結果: 時価総額$40B+
```

**判断基準**:
- アプリ単体では競合優位性なし
- API/3rd party需要が高い

---

### 4.6 Business Architecture Pivot（B2C ⇄ B2B）

**定義**: ビジネスモデルの変更

**事例（Yammer）**:
```
Before: B2C SNS
データ: Facebook/Twitterに勝てない
After: B2B社内SNS
結果: Microsoft $1.2Bで買収
```

**判断基準**:

| 指標 | B2C | B2B |
|------|-----|-----|
| **CAC** | 低 | 高 |
| **LTV** | 低 | 高 |
| **Churn** | 高 | 低 |
| **拡販速度** | 速い | 遅い |

参照: [[TACTIC_UNIT_ECONOMICS_001]]

---

### 4.7 Value Capture Pivot（収益化方法変更）

**定義**: マネタイズ方法の変更

**パターン**:

| Before | After | 事例 |
|--------|-------|------|
| 有料 | 広告 | Facebook |
| 広告 | Freemium | Dropbox |
| 買い切り | サブスク | Adobe Creative Cloud |
| 直販 | マーケットプレイス手数料 | Airbnb |

**判断基準**:
- 現在の収益モデルで支払意思<30%
- 別モデルでWTP（支払意思）高い

---

### 4.8 Engine of Growth Pivot（成長エンジン変更）

**Eric Riesの3つの成長エンジン**:

| 成長エンジン | 特徴 | 事例 |
|------------|------|------|
| **Sticky** | 高Retention、低Churn | Slack, Dropbox |
| **Viral** | 紹介・招待ループ | WhatsApp, Instagram |
| **Paid** | 広告・営業 | Salesforce |

**Pivot例**:
```
Before: Viral成長狙い
データ: バイラル係数0.3（<1.0で失敗）
After: Sticky成長（高Retention重視）
結果: Churn率2%達成、LTV向上
```

参照: [[FRAMEWORK_AARRR_001]]

---

### 4.9 Channel Pivot（販売チャネル変更）

**定義**: 顧客獲得経路の変更

**事例（Amazon）**:
```
Before: オンライン書店
After: マーケットプレイス（3rdパーティ販売者）
結果: GMVの50%が3rdパーティ経由
```

**判断基準**:
- CAC/LTV比率が悪化（>0.33）
- 別チャネルでCAC 1/10

---

### 4.10 Technology Pivot（技術スタック変更）

**定義**: 同じソリューションを別技術で実現

**事例**:
```
Before: デスクトップアプリ
データ: インストール障壁高い
After: Webアプリ
結果: CVR 3倍
```

**判断基準**:
- 技術的負債が成長阻害
- 新技術でコスト1/10、速度10倍

---

## 5. Pivot判断プロセス

### ステップ1: データ収集（1-2週間）

**必須データ**:
- [ ] CPF/PSF指標（3U, NPS, Retention）
- [ ] ユーザーインタビュー30+件
- [ ] MVP/プロトタイプ反応
- [ ] 競合分析
- [ ] 市場規模再計算

---

### ステップ2: Pivot会議（半日）

**参加者**: 全創業者 + コアメンバー

**アジェンダ**:
1. **データレビュー**（60分）
   - 各指標の推移
   - 仮説vs実績
2. **5つのシグナルチェック**（30分）
3. **Pivot vs Persevereディベート**（60分）
   - Pivot派の主張
   - Persevere派の主張
4. **投票**（10分）
   - 全員一致が理想
5. **Next Action決定**（30分）

---

### ステップ3: Pivot実行（1-4週間）

**Small Pivot（軽微な変更）**:
```
例: Customer Segment Pivot
期間: 1-2週間
- 新ペルソナ定義
- LP修正
- インタビュー20件
- MVP投入
```

**Big Pivot（大幅変更）**:
```
例: Business Architecture Pivot（B2C→B2B）
期間: 1-3ヶ月
- 事業計画書き換え
- プロダクト再設計
- GTM戦略変更
- チーム再編
```

---

## 6. よくある間違い

| 間違い | 症状 | 対策 |
|--------|------|------|
| **感情的判断** | 「絶対いける」と執着 | データドリブン判断 |
| **Pivot連発** | 月1回Pivot | 仮説検証期間3ヶ月確保 |
| **Half Pivot** | 中途半端な変更 | 明確なPivot実行 |
| **チーム無視** | 創業者単独判断 | 全員合意形成 |
| **資金枯渇後** | 手元資金$0でPivot | Runway 6ヶ月以上で判断 |

---

## 7. 成功事例

### 7.1 Twitter（Platform Pivot + Customer Need Pivot）

**経緯**:
```
2005: Odeo（Podcastプラットフォーム）創業
2006: iTunes Podcast発表 → 競合優位性喪失
2006/7: 全社ハッカソン → Twttr（140文字投稿）誕生
2006/10: Odeo売却、Twitter社に社名変更
2007: SXSW祭典でバイラル
2013: IPO（時価総額$31B）
```

**Pivotの種類**: Platform → App

**成功要因**:
- 早期判断（競合出現後4ヶ月）
- 社内プロトタイプで検証
- 創業者全員合意

---

### 7.2 Slack（Zoom-out Pivot + Customer Segment Pivot）

**経緯**:
```
2009: Tiny Speck社創業（ゲーム開発）
2012: ゲーム「Glitch」失敗
2012: 内部チャットツールの評判◎
2013: Slack正式ローンチ
2014: $1.1B評価
2019: 上場（時価総額$23B）
```

**Pivotの種類**:
1. Zoom-out（チャット機能 → プラットフォーム）
2. Customer Segment（ゲーム開発者 → 全企業）

**成功要因**:
- 自分たちが欲しいものを作った
- プロダクト完成度高い状態でローンチ
- D30 Retention 93%（最初から）

---

### 7.3 Instagram（Zoom-in Pivot）

**経緯**:
```
2010/3: Burbn（位置情報SNS）開発開始
2010/6: 使用データ分析 → 写真シェアのみ使用率80%
2010/8: 写真特化へPivot決定
2010/10: Instagram正式ローンチ
2010/12: 100万ユーザー突破
2012/4: Facebook $1B買収
```

**成功要因**:
- データドリブン判断
- 迅速な実行（2ヶ月）
- UI/UX磨き込み

---

## 8. 失敗事例から学ぶ

### 8.1 某フードデリバリー（Pivot遅延）

**経緯**:
```
Year 1: B2C向けデリバリーアプリ
Year 2: Unit Economics悪化（CAC > LTV）
Year 3: 改善施策も効果なし
Year 4: 資金枯渇でB2B Pivotするも手遅れ
Year 5: サービス終了
```

**失敗要因**:
- Year 2時点でPivot判断すべきだった
- 創業者の執着
- データ無視

---

## 9. Pivot判断チェックリスト

### Pivot検討すべき状況

- [ ] PSF指標が3ヶ月以上改善しない
- [ ] インタビュー50件で肯定<30%
- [ ] MVP CVR <0.3%が継続
- [ ] NPS <10が3ヶ月継続
- [ ] TAMが想定の1/10以下
- [ ] 10倍価値提供が不可能と判明
- [ ] 創業者の情熱喪失
- [ ] Runway 6ヶ月未満

**3つ以上該当 → Pivot会議招集**

---

### Persevere（忍耐）すべき状況

- [ ] 指標は改善傾向（小さくても）
- [ ] コアユーザーが熱狂（NPS 70+）
- [ ] 市場タイミングが合っていない（早すぎる）
- [ ] プロダクト完成度が低い（改善余地大）
- [ ] Runway 18ヶ月以上

**3つ以上該当 → Persevere（継続）**

---

## 10. Pivot後のアクション

### 1週間以内:
- [ ] 新ペルソナ定義
- [ ] 新仮説リスト作成
- [ ] 最小限MVP設計
- [ ] チームへ説明・合意形成

### 1ヶ月以内:
- [ ] インタビュー30件
- [ ] MVP開発・リリース
- [ ] 初期反応収集
- [ ] KPI設定

### 3ヶ月以内:
- [ ] PSF判定
- [ ] Next Pivot or Persevere判断

---

## 11. 関連概念

| 概念 | 関係性 | リンク |
|------|--------|--------|
| PSF | Pivot判断の基準 | [[CONCEPT_PSF_001]] |
| CPF | Pivot前に再検証 | [[CONCEPT_CPF_001]] |
| PMF | Pivot成功でPMF到達 | [[CONCEPT_PMF_001]] |
| 3U検証 | Pivot判断データ | [[TACTIC_3U_001]] |
| Unit Economics | Value Capture Pivot判断 | [[TACTIC_UNIT_ECONOMICS_001]] |

---

## クイックリファレンス

```
定義: 学習に基づく戦略変更
原則: Pivot ≠ 失敗、学習の証明

5つの判断シグナル:
1. CPF/PSF指標停滞（3ヶ月+）
2. コア仮説の否定
3. TAM想定の1/10以下
4. 競合優位性の欠如
5. チーム士気・資金悪化

10類型:
1. Zoom-in（機能特化）
2. Zoom-out（機能拡張）
3. Customer Segment（顧客変更）
4. Customer Need（課題変更）
5. Platform（プラットフォーム化）
6. Business Architecture（B2C⇄B2B）
7. Value Capture（収益化変更）
8. Engine of Growth（成長エンジン変更）
9. Channel（販売チャネル変更）
10. Technology（技術変更）

判断タイミング:
- 1-3ヶ月: ✅ 最適
- 6ヶ月: ⚠️ やや遅い
- 1年+: ❌ 手遅れリスク

成功要因:
- データドリブン判断
- 早期実行
- チーム全員合意
- 十分なRunway確保
```

---

**ファイル情報**
- 作成日: 2025-12-28
- 最終更新: 2025-12-28
- バージョン: 1.0
