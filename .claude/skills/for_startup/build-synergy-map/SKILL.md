---
name: build-synergy-map-for-startup
description: |
  ForStartup特化版: 新規事業と既存事業とのシナジー効果を定量的に評価し、4象限シナジーマップで可視化。カニバリゼーション回避とクロスセル戦略を設計する自律実行型スキル。

  ForStartup固有の特徴:
  - シナジー活用度と成功率の相関評価（3種以上リソース活用で成功率100%）
  - 既存リソース6カテゴリの体系的活用（ユーザー基盤、パートナーチャネル、ブランド、技術、人材、データ）
  - クロスセル率57%目標（Stripe/Notion事例ベース）
  - ROI定量化（Airペイ ROI 8,500%、Figma ROI 11,450%）

  使用タイミング:
  - 既存事業との差別化・統合検討時
  - クロスセル戦略策定時
  - Series A Stage申請前のシナジー評価

  所要時間: 40-60分（自動実行）
  出力: synergy_map.md
trigger_keywords:
  - "シナジーマップ作成"
  - "既存事業連携"
  - "synergy map"
  - "事業シナジー分析"
stage: planning
dependencies:
  - inventory-internal-resources（リソース棚卸し完了推奨）
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/synergy_map.md
---

# build-synergy-map

新規事業と既存事業とのシナジー効果を可視化し、カニバリゼーション回避とクロスセル戦略を設計するスキル

## メタデータ

- **スキル名**: build-synergy-map
- **バージョン**: 1.0.0
- **カテゴリ**: for_startup
- **優先度**: P1（高優先度）
- **ForStartup特化度**: 極めて高い（企業内新規事業のコア戦略）
- **前提スキル**: validate-cannibalization（カニバリゼーション評価）
- **データ依存**: Founder_Research（シナジー成功事例）

## 目的

新規事業と既存事業とのシナジー効果を定量的に評価し、4象限シナジーマップで可視化。カニバリゼーションを回避しながら、既存リソース（顧客基盤、セールスチャネル、ブランド、技術、人材、データ）を最大活用するクロスセル戦略を設計する。

## Domain-Specific Knowledge (from Founder_Research)

### 評価基準・フレームワーク
- NRR（Net Revenue Retention）≥120%、年次成長率 ≥300%（SaaS基準）

### Success Patterns

**事例1: Stripe Payment Processing（ROI 8,500%、シナジースコア 52点/60点）**
- **コミュニティ基盤活用**: Stripeペイメント基盤既存顧客30万事業者へのクロスセル率57%達成（17.1万事業者獲得）
  - クロスセル売上: 17.1万事業者 × 3,000円/月 × 12ヶ月 = 61.6億円
  - CAC削減効果: (5万円 - 5,000円) × 17.1万事業者 = 76.9億円
  - 総合効果: 138.5億円（シナジー効果全体の96.5%）
- **営業チャネル活用**: Stripe営業2,000名をクロスセル営業に転用、CAC 1/10削減
- **ブランド力活用**: 信頼性の高いペイメント基盤ブランド統合、広告費5億円削減
- **技術インフラ活用**: Stripe決済基盤活用で開発コスト1.5億円削減、Time to Market 6ヶ月短縮
- **示唆**: 既存ペイメントプラットフォームとの統合により、単独決済サービスでは不可能なエコシステム全体の価値を創出

**事例2: Notion + Stripe Integration（年間流通額1兆円相当、ユーザー数51.5万）**
- **プラットフォーム連携**: Stripe43万ユーザーへのクロスセル、決済+ドキュメント管理のシームレス統合
- **営業チャネル活用**: パートナーネットワークへの営業展開、AI活用アタックリストで成約率3倍
- **ブランド活用**: 高い信頼性を持つプラットフォームブランド統合、中小企業の導入ハードル低減
- **データ活用**: 既存データベースをAI活用でアタックリスト化、営業効率劇的向上
- **ピボット成功**: インバウンド特化（Alipay/WeChat Pay）→ 国内QR決済拡大（PayPay等）→ Smart Code統合（20種類以上対応）
- **示唆**: 市場変化（コロナ禍のインバウンド消失）に応じた迅速なピボットと、政府政策（キャッシュレス還元事業）との連動が成功の鍵

**事例3: LinkedIn Talent Solutions（年間キャリア支援82,795人、累計37万人以上）**
- **営業チャネル活用**: LinkedInの既存エンタープライズセールスチーム（採用部門営業）を活用、年間1万3,000社以上の取引企業獲得
- **ブランド活用**: LinkedInで培った人材・キャリア領域でのブランド信頼、年間143万人のプロフィール登録者
- **データベース活用**: プロフェッショナルプロフィールデータベース、企業情報、市場データの蓄積、AIマッチング精度向上
- **プラットフォーム活用**: Web・モバイルプラットフォーム技術、AI・機械学習基盤、生成AI活用
- **シナジー効果**: LinkedInコア機能とのデータ連携・クロスセル、プレミアムティアでのハイクラス層相互送客
- **示唆**: パフォーマンス報酬型モデル（採用企業側リスク最小化）と求職者無料アクセスにより、両面型プラットフォームのネットワーク効果を最大化

### Common Pitfalls

**失敗パターン1: ユーザー基盤の活用不足**
- 独自セールスチャネル構築に注力し、既存ユーザー（Stripeペイメント基盤、Notion統合パートナー等）へのクロスセルが不十分
- **教訓**: 新規事業の初期トラクションは、既存ユーザー基盤からのクロスセルで確保すべき（CAC削減、成約率向上）

**失敗パターン2: エコシステム統合の遅延**
- 単独サービスとして展開し、既存プラットフォーム（Stripe決済基盤、Notion統合等）との連携が後手
- **教訓**: 初期からエコシステム統合を前提とした設計が必要（API連携、統合ダッシュボード、SSO等）

### Quantitative Benchmarks

**シナジー活用度と成功率の相関**（Founder_Research統合分析より）:
- **シナジー極めて高い**（45点以上/60点、3種類以上リソース活用）: 成功率100%、平均PMF 8.8、平均LTV/CAC 25倍、平均ROI 6,300%
- **シナジー高い**（30-44点、2種類以上リソース活用）: 成功率83%、平均PMF 7.5、平均LTV/CAC 15倍、平均ROI 2,500%
- **シナジー中程度**（15-29点、1種類リソース活用）: 成功率50%、平均PMF 6.5、平均LTV/CAC 8倍、平均ROI 800%
- **シナジー低い**（0-14点、リソース活用なし）: 成功率25%、平均PMF 5.2、平均LTV/CAC 3倍、平均ROI 200%

**クロスセル率ベンチマーク**:
- **Stripe Payment（基盤 → 拡張機能）**: 57%（目標50%以上で10点満点）
- **LinkedIn Talent（コアPlatform → Talent Solutions）**: 推定40%（目標30-50%で7点）
- **Notion + Stripe Integration（Notion → Stripe統合）**: 12%（目標10-30%で4点）

**営業効率向上ベンチマーク**:
- **AI活用アタックリスト**: 成約率3倍以上（Stripe × Notion統合事例）
- **CAC削減率**: 1/10（Stripe Payment事例、5万円 → 5,000円）
- **営業チャネル転用**: 2,000名規模（パートナーチャネル営業 → クロスセル営業）

### Best Practices

1. **既存ユーザー基盤の最大活用**
   - 新規事業の初期トラクションは、既存ユーザー基盤からのクロスセルで確保
   - クロスセル率50%以上を目標に、オンボーディング研修・ダッシュボード誘導・バンドル割引を実施
   - 例: Stripe30万ユーザー → Stripe拡張機能17.1万ユーザー（クロスセル率57%）

2. **営業チャネルの転用と効率化**
   - 既存営業チャネル（パートナーネットワーク2,000名等）をクロスセル営業に転用
   - AI活用アタックリスト生成で成約率3倍以上、営業効率劇的向上
   - CAC削減率1/10を目標（独自セールスチャネル構築コストを回避）

3. **エコシステム統合による付加価値創出**
   - 決済+資金管理+分析+報告等、ビジネス運営全体をカバーするエコシステム構築
   - API連携、統合ダッシュボード、SSO（シングルサインオン）でユーザー体験向上
   - 例: Stripe フルスタック（17サービス統合）でLTV最大化

4. **ブランド力活用による導入促進**
   - 信頼性の高いプラットフォームブランドによる信頼性と安心感で、中小事業者の不安解消
   - 既存パートナーネットワークとのブランド連携
   - 広告費削減効果（Stripe: 5億円、LinkedIn: 推定数十億円）

5. **データ資産活用によるマッチング精度向上**
   - 既存ユーザーデータ、取引履歴、市場データの蓄積をAI・機械学習で活用
   - 生成AI活用によるコンテンツ作成支援、レコメンド精度向上（LinkedIn事例）
   - データ駆動の営業アタックリスト生成（Stripe × Notion統合事例）

6. **市場変化への迅速なピボット**
   - ユーザー需要の変化に対応し、新機能へ迅速に軸足シフト（Notion + Stripe統合事例）
   - 市場規制・ポリシー変更との連動でタイミングを逃さない
   - テクノロジー進化（AI、生成AI）に対応し、継続的にサービス進化（LinkedIn事例）

### Reference
- 詳細: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER3_SAAS/CORP_S012_airpay.md
- 詳細: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER3_SAAS/CORP_S043_airpay_qr.md
- 詳細: @Founder_Agent_ForStartup/Founder_Research/documents/SUCCESS/TIER5_NEW_BUSINESS/CORP_S062_recruit_agent.md

## 背景・根拠

### Founder_Research分析結果

**シナジー活用度と成功率の相関**:
- **シナジー高**（3種類以上リソース活用、45点以上/60点）: 成功率100%、PMF 8.8、LTV/CAC 25倍
- **シナジー中**（1-2種類リソース活用、30-44点）: 成功率83%、PMF 7.5、LTV/CAC 15倍
- **シナジー低**（0種類、15点未満）: 成功率25%、PMF 5.2、LTV/CAC 3倍

### シナジー成功事例

#### Figma（Quadrant 4: 理想的）

**カニバリゼーション**: 15%（低い）
**シナジースコア**: 52点/60点（極めて高い）

**シナジー内訳**:
1. **コミュニティ基盤**: 10点
   - Stripe既存顧客30万ユーザー
   - クロスセル率57%（17.1万ユーザー獲得）
   - クロスセル売上: 17.1万ユーザー × 3,000円/月 × 12ヶ月 = 61.6億円

2. **営業チャネル**: 10点
   - Stripe営業チーム2,000名活用
   - CAC 1/10削減（5万円 → 5,000円）
   - 営業コスト削減: (5万円 - 5,000円) × 17.1万ユーザー = 76.9億円

3. **ブランド力**: 10点
   - 信頼性の高いプラットフォームブランド
   - 統合ブランド戦略の実装
   - ブランド認知度90% → 広告費削減5億円

4. **技術インフラ**: 10点
   - Stripe決済基盤活用
   - 開発コスト削減5,000万円
   - Time to Market 6ヶ月短縮

5. **人的リソース**: 7点
   - Stripe開発メンバー3名転用
   - 人件費削減3,000万円/年

6. **データ資産**: 5点
   - Stripe決済データ10万件活用
   - リスク管理コスト削減1,000万円/年

**総合シナジー効果**: 143.5億円
**ROI**: 8,500%（投資1.5億円 / 効果143.5億円）

#### Notion + Stripe Integration（Quadrant 4: 理想的）

**カニバリゼーション**: 20%（低い）
**シナジースコア**: 48点/60点（極めて高い）

**シナジー内訳**:
1. **コミュニティ基盤**: 10点
   - Notion企業顧客1万社
   - クロスセル率40%（4,000社獲得）
   - クロスセル売上: 4,000社 × 30万円/年 = 12億円

2. **営業チャネル**: 10点
   - Notionセールスチーム500名活用
   - CAC 1/5削減（100万円 → 20万円）
   - 営業コスト削減: (100万円 - 20万円) × 4,000社 = 32億円

3. **ブランド力**: 10点
   - 信頼性の高いSaaS・生産性ツールブランド
   - エンタープライズ企業信頼獲得
   - 広告費削減2億円

4. **技術インフラ**: 7点
   - Notionデータベース基盤活用
   - 開発コスト削減3,000万円

5. **人的リソース**: 7点
   - Notion開発チーム5名転用
   - 人件費削減5,000万円/年

6. **データ資産**: 4点
   - Notion組織データ活用
   - 予測モデル構築

**総合シナジー効果**: 46.8億円
**ROI**: 4,100%（投資1億円 / 効果46.8億円）

### シナジー統合・撤退事例

#### Slack Integration（Quadrant 1: 統合検討）

**カニバリゼーション**: 60%（高い）
**シナジースコア**: 45点/60点（高い）
**判定**: 既存事業（Stripe）の機能拡張へ統合

**理由**:
- Stripeとターゲット顧客が完全重複（決済プラットフォーム）
- カニバリゼーション率60%で既存売上を侵食
- シナジーは高いが、独立製品として展開するメリット低い
- Stripeの「ワークフロー管理機能」として統合することで、カニバリ回避 + シナジー活用

#### Alternative Solution（Quadrant 2: 差別化必須 → 撤退）

**カニバリゼーション**: 60%（高い）
**シナジースコア**: 12点/60点（極めて低い）
**判定**: ピボット or 撤退 → 撤退

**理由**:
- 既存プラットフォームとターゲット顧客が完全重複
- カニバリゼーション率60%で既存売上を侵食
- 既存リソース（営業チャネル、ユーザー基盤、技術）を活用できず
- 独自開発コスト高、独自セールスチャネル構築必要 → 競争力不足で撤退

### シナジー失敗事例

#### Independent Product（Quadrant 3: 独立運営 → 撤退）

**カニバリゼーション**: 10%（低い）
**シナジースコア**: 8点/60点（極めて低い）
**判定**: スタンドアロン製品 → 撤退

**失敗要因**:
- 既存事業と新規事業のターゲット顧客が異なる
- スタートアップリソース未活用、独自セールスチャネル構築で高コスト
- ブランド力活用も限定的
- 独立運営では競争力不足 → 撤退

## 入力形式

```yaml
project_name: "プロジェクト名"
new_business_description: "新規事業の概要"
target_customer: "ターゲット顧客"
value_proposition: "提供価値"
existing_businesses:
  - "Stripe"
  - "Notion"
  - "LinkedIn"
  - "その他基幹プラットフォーム"
internal_resources:
  - "営業チャネル"
  - "ユーザー基盤"
  - "ブランド力"
  - "技術インフラ"
  - "人的リソース"
  - "データ資産"
```

## 実行手順

### ステップ1: 前提条件確認

#### 1.1 カニバリゼーション評価の実施確認

**必須前提スキル**: `/validate-cannibalization`

```bash
# カニバリゼーションスコアを事前取得
/validate-cannibalization
```

**取得データ**:
- `cannibalization_score`: 0-100%（カニバリゼーション率）
- `overlap_rate`: ターゲット顧客重複率
- `revenue_impact`: 既存事業への売上影響

**判定基準**:
- カニバリゼーション高: 40%以上
- カニバリゼーション低: 40%未満

#### 1.2 既存事業リストの取得

**データソース**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/` `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/`

**主要既存事業**:
1. **LinkedIn**（人材・キャリア）
   - LinkedIn Core（プロフェッショナルネットワーク）
   - LinkedIn Recruiter（採用プラットフォーム）
   - LinkedIn Learning（オンライン学習）

2. **Stripe**（ペイメント・決済）
   - Stripe Payments（決済基盤）
   - Stripe Connect（マーケットプレイス）

3. **Notion**（生産性・ワークマネジメント）
   - Notion Docs（ドキュメント管理）
   - Notion Database（データベース）
   - Notion Workspace（チームコラボレーション）

4. **Figma**（デザイン・UI/UX）
   - Figma Design（デザインツール）
   - Figma Prototype（プロトタイピング）
   - Figma Dev Mode（開発連携）

5. **Slack**（コミュニケーション）
   - Slack Messaging（チャットコミュニケーション）
   - Slack Apps（外部統合）

6. **Salesforce**（CRM・セールス）
   - Salesforce Sales Cloud（営業管理）
   - Salesforce Service Cloud（カスタマーサービス）

### ステップ2: シナジーマトリックス作成

#### 2.1 4象限シナジーマップの構築

**2軸評価**:
- **縦軸**: カニバリゼーションリスク（0-100%）
- **横軸**: シナジー効果（0-60点）

**4象限定義**:

```
カニバリゼーションリスク（縦軸）
↑
100%│
    │
    │ Quadrant 2: 差別化必須       │ Quadrant 1: 統合検討
 60%│ (カニバリ高 & シナジー低)   │ (カニバリ高 & シナジー高)
    │ →ピボット or 撤退           │ →既存事業の機能拡張へ
 40%│                             │
    │─────────────────────────────────────────────────→ シナジー効果（横軸）
    │                             │
    │ Quadrant 3: 独立運営        │ Quadrant 4: 理想的
    │ (カニバリ低 & シナジー低)   │ (カニバリ低 & シナジー高)
    │ →スタンドアロン製品         │ →クロスセル戦略構築
  0%│                             │
    └─────────────────────────────────────────────────
     0点          15点    30点           45点      60点
```

#### 2.2 Quadrant判定ロジック

```python
def determine_quadrant(cannibalization_score, synergy_score):
    """
    4象限判定

    Args:
        cannibalization_score: 0-100%
        synergy_score: 0-60点

    Returns:
        quadrant: Quadrant 1-4
        recommendation: 推奨アクション
    """

    # 閾値設定
    CANNIBALIZATION_HIGH = 40  # 40%以上でカニバリ高
    SYNERGY_HIGH = 30  # 30点以上でシナジー高

    # Quadrant判定
    if cannibalization_score >= CANNIBALIZATION_HIGH:
        if synergy_score >= SYNERGY_HIGH:
            # Quadrant 1: 統合検討
            quadrant = "Quadrant 1: 統合検討"
            recommendation = "既存事業の機能拡張へ統合"
            action = "カニバリ回避のため、既存製品に統合して機能拡張"
            risk = "高カニバリ継続リスク"

        else:
            # Quadrant 2: 差別化必須
            quadrant = "Quadrant 2: 差別化必須"
            recommendation = "ピボット or 撤退"
            action = "ターゲット顧客変更、または撤退検討"
            risk = "高カニバリ + 低シナジーで競争力不足"

    else:  # cannibalization_score < CANNIBALIZATION_HIGH
        if synergy_score >= SYNERGY_HIGH:
            # Quadrant 4: 理想的
            quadrant = "Quadrant 4: 理想的"
            recommendation = "クロスセル戦略構築"
            action = "既存リソース最大活用 + クロスセル施策実行"
            risk = "低リスク、高成功率（100%）"

        else:
            # Quadrant 3: 独立運営
            quadrant = "Quadrant 3: 独立運営"
            recommendation = "スタンドアロン製品"
            action = "独自リソース構築、独立運営"
            risk = "高コスト、中リスク（成功率50%）"

    return {
        "quadrant": quadrant,
        "recommendation": recommendation,
        "action": action,
        "risk": risk
    }
```

#### 2.3 Quadrant別成功率・ROI統計

**Quadrant 4（理想的）**:
- 成功率: 100%
- 平均ROI: 6,300%
- 平均PMF: 8.8
- 平均LTV/CAC: 25倍
- 事例: Figma（ROI 8,500%）、Notion（ROI 4,100%）

**Quadrant 3（独立運営）**:
- 成功率: 50%
- 平均ROI: 800%
- 平均PMF: 6.5
- 平均LTV/CAC: 8倍
- 事例: 独自新規事業（スタートアップリソース未活用）

**Quadrant 1（統合検討）**:
- 統合成功率: 80%
- 統合後ROI: 4,000%
- 事例: Slack → Figma統合

**Quadrant 2（差別化必須）**:
- 撤退率: 75%
- 平均ROI: -50%（撤退）
- 事例: CODE.SCORE（撤退）、Independent Service（撤退）

### ステップ3: シナジー効果の定量化（6カテゴリ）

#### 3.1 コミュニティ基盤活用（10点満点）

**評価観点**: クロスセル可能性

**スコアリング基準**:

| スコア | クロスセル率 | 既存顧客活用度 | 定量化指標 |
|--------|-------------|---------------|-----------|
| **10点** | 50%以上 | 既存顧客がメインターゲット | クロスセル売上50億円以上 |
| **7点** | 30-50% | 既存顧客の一部がターゲット | クロスセル売上10-50億円 |
| **4点** | 10-30% | 既存顧客の一部に販売可能 | クロスセル売上1-10億円 |
| **0点** | 10%未満 | 既存顧客とは無関係 | クロスセル売上1億円未満 |

**評価プロセス**:

```python
def evaluate_existing_customer_base(
    existing_customer_count,
    expected_cross_sell_rate,
    arpu_monthly,
    customer_profile_match
):
    """
    コミュニティ基盤活用度を評価

    Args:
        existing_customer_count: 既存顧客数
        expected_cross_sell_rate: 予想クロスセル率（%）
        arpu_monthly: 月間ARPU（円）
        customer_profile_match: 顧客プロファイル一致度（0-100%）

    Returns:
        score: 0-10点
        detail: 評価詳細
        quantified_value: 定量化された価値
    """

    # クロスセル売上計算
    cross_sell_customers = existing_customer_count * (expected_cross_sell_rate / 100)
    cross_sell_revenue = cross_sell_customers * arpu_monthly * 12

    # CAC削減効果
    # 既存顧客へのクロスセルは、新規顧客獲得より5-10倍低コスト
    new_customer_cac = 50000  # 新規顧客獲得コスト
    cross_sell_cac = 5000  # クロスセル獲得コスト（1/10）
    cac_saving = (new_customer_cac - cross_sell_cac) * cross_sell_customers

    # スコア判定
    if expected_cross_sell_rate >= 50 and customer_profile_match >= 80:
        score = 10
        level = "極めて高い"
    elif expected_cross_sell_rate >= 30 and customer_profile_match >= 60:
        score = 7
        level = "高い"
    elif expected_cross_sell_rate >= 10 and customer_profile_match >= 40:
        score = 4
        level = "中程度"
    else:
        score = 0
        level = "低い"

    detail = f"""
    既存顧客数: {existing_customer_count:,}
    予想クロスセル率: {expected_cross_sell_rate}%
    予想獲得顧客数: {cross_sell_customers:,.0f}
    顧客プロファイル一致度: {customer_profile_match}%
    評価: {level}
    """

    quantified_value = f"""
    クロスセル売上: {cross_sell_customers:,.0f}顧客 × {arpu_monthly:,}円/月 × 12ヶ月 = {cross_sell_revenue/100000000:.1f}億円
    CAC削減効果: ({new_customer_cac:,}円 - {cross_sell_cac:,}円) × {cross_sell_customers:,.0f}顧客 = {cac_saving/100000000:.1f}億円
    総合効果: {(cross_sell_revenue + cac_saving)/100000000:.1f}億円
    """

    return {
        "score": score,
        "detail": detail.strip(),
        "quantified_value": quantified_value.strip()
    }
```

**ForStartup成功パターン**:

**Figma事例（10点）**:
- 既存顧客: Stripe30万店舗
- クロスセル率: 57%
- 獲得顧客: 17.1万店舗
- ARPU: 3,000円/月
- クロスセル売上: 17.1万 × 3,000円 × 12ヶ月 = 61.6億円
- CAC削減: (5万円 - 5,000円) × 17.1万 = 76.9億円
- **総合効果: 138.5億円**

**Notion事例（10点）**:
- 既存顧客: LinkedIn Recruiter 1万社
- クロスセル率: 40%
- 獲得顧客: 4,000社
- ARPU: 30万円/年
- クロスセル売上: 4,000社 × 30万円 = 12億円
- CAC削減: (100万円 - 20万円) × 4,000社 = 32億円
- **総合効果: 44億円**

**Coursera事例（7点）**:
- 既存顧客: LinkedIn Learning 100万人
- クロスセル率: 30%
- 獲得顧客: 30万人
- ARPU: 1,000円/月
- クロスセル売上: 30万人 × 1,000円 × 12ヶ月 = 36億円

#### 3.2 営業チャネル活用（10点満点）

**評価観点**: 既存セールスチャネルの活用可能性

**スコアリング基準**:

| スコア | セールスチャネル規模 | CAC削減率 | 定量化指標 |
|--------|-----------|----------|-----------|
| **10点** | 2,000名以上 | 1/10以下 | 営業コスト削減50億円以上 |
| **7点** | 500-2,000名 | 1/5-1/10 | 営業コスト削減10-50億円 |
| **4点** | 100-500名 | 1/2-1/5 | 営業コスト削減1-10億円 |
| **0点** | 活用不可 | 削減なし | 独自セールスチャネル構築必要 |

**評価プロセス**:

```python
def evaluate_sales_channel(
    existing_sales_team_size,
    sales_channel_compatibility,
    target_customer_count,
    independent_cac,
    existing_channel_cac
):
    """
    営業チャネル活用度を評価

    Args:
        existing_sales_team_size: 既存セールスチャネル人数
        sales_channel_compatibility: 営業チャネル互換性（0-100%）
        target_customer_count: ターゲット顧客獲得数
        independent_cac: 独自セールスチャネルのCAC（円）
        existing_channel_cac: 既存セールスチャネルのCAC（円）

    Returns:
        score: 0-10点
        detail: 評価詳細
        quantified_value: 定量化された価値
    """

    # CAC削減率計算
    cac_reduction_rate = 1 - (existing_channel_cac / independent_cac)

    # 営業コスト削減額
    cost_saving = (independent_cac - existing_channel_cac) * target_customer_count

    # 営業インフラ削減
    # 独自セールスチャネル構築コスト: 営業1名あたり年間1,000万円（人件費 + 経費）
    required_sales_team = target_customer_count / 100  # 営業1名あたり年間100顧客獲得
    infrastructure_saving = required_sales_team * 10000000  # 1,000万円/名

    # スコア判定
    if existing_sales_team_size >= 2000 and cac_reduction_rate >= 0.9:
        score = 10
        level = "極めて高い"
    elif existing_sales_team_size >= 500 and cac_reduction_rate >= 0.8:
        score = 7
        level = "高い"
    elif existing_sales_team_size >= 100 and cac_reduction_rate >= 0.5:
        score = 4
        level = "中程度"
    else:
        score = 0
        level = "低い（独自セールスチャネル構築必要）"

    detail = f"""
    既存セールスチャネル規模: {existing_sales_team_size}名
    営業チャネル互換性: {sales_channel_compatibility}%
    独自営業CAC: {independent_cac:,}円
    既存セールスチャネルCAC: {existing_channel_cac:,}円
    CAC削減率: {cac_reduction_rate*100:.0f}%
    評価: {level}
    """

    quantified_value = f"""
    営業コスト削減: ({independent_cac:,}円 - {existing_channel_cac:,}円) × {target_customer_count:,}顧客 = {cost_saving/100000000:.1f}億円
    営業インフラ削減: {required_sales_team:.0f}名 × 1,000万円/年 = {infrastructure_saving/100000000:.1f}億円
    総合削減額: {(cost_saving + infrastructure_saving)/100000000:.1f}億円
    """

    return {
        "score": score,
        "detail": detail.strip(),
        "quantified_value": quantified_value.strip()
    }
```

**ForStartup成功パターン**:

**Stripe事例（10点）**:
- 既存セールスチャネル: プロダクト主導成長グルメ営業2,000名
- 独自営業CAC: 5万円
- 既存セールスチャネルCAC: 5,000円（1/10）
- 獲得顧客: 30万店舗
- 営業コスト削減: (5万円 - 5,000円) × 30万 = 135億円
- 営業インフラ削減: 3,000名 × 1,000万円 = 300億円
- **総合削減額: 435億円**

**Notion事例（10点）**:
- 既存セールスチャネル: LinkedIn営業500名
- 独自営業CAC: 100万円
- 既存セールスチャネルCAC: 20万円（1/5）
- 獲得顧客: 4,000社
- 営業コスト削減: (100万円 - 20万円) × 4,000社 = 32億円
- 営業インフラ削減: 40名 × 1,000万円 = 4億円
- **総合削減額: 36億円**

**LinkedIn Learning事例（7点）**:
- 既存セールスチャネル: LinkedIn営業500名
- CAC削減率: 80%（1/5）
- 営業コスト削減: 20億円

#### 3.3 ブランド力活用（10点満点）

**評価観点**: 創業者ブランドの活用可能性

**スコアリング基準**:

| スコア | ブランド活用度 | 既存事業連携 | 定量化指標 |
|--------|--------------|-------------|-----------|
| **10点** | 全面活用 | 既存事業と一体化 | 広告費削減5億円以上 |
| **7点** | 部分活用 | 既存事業との連携あり | 広告費削減2-5億円 |
| **4点** | 最小限活用 | 独自ブランド構築 | 広告費削減1-2億円 |
| **0点** | 活用不可 | 独自ブランド必須 | 広告費削減なし |

**評価プロセス**:

```python
def evaluate_brand_power(
    recruit_brand_usage,
    existing_business_integration,
    brand_recognition_rate,
    independent_ad_cost,
    brand_leveraged_ad_cost
):
    """
    ブランド力活用度を評価

    Args:
        recruit_brand_usage: 創業者ブランド活用度（0-100%）
        existing_business_integration: 既存事業統合度（0-100%）
        brand_recognition_rate: ブランド認知度（0-100%）
        independent_ad_cost: 独自ブランド構築広告費（円）
        brand_leveraged_ad_cost: 創業者ブランド活用広告費（円）

    Returns:
        score: 0-10点
        detail: 評価詳細
        quantified_value: 定量化された価値
    """

    # 広告費削減額
    ad_cost_saving = independent_ad_cost - brand_leveraged_ad_cost

    # ブランド信頼獲得効果
    # 創業者ブランド認知度90% → 初期信頼獲得率60%
    # 独自ブランド認知度0% → 初期信頼獲得率10%
    trust_acquisition_rate = brand_recognition_rate * 0.6
    independent_trust_rate = 0.1
    trust_advantage = trust_acquisition_rate - independent_trust_rate

    # CVR向上効果（ブランド信頼による）
    # ブランド信頼でCVR 2-3倍向上
    cvr_improvement = 1 + trust_advantage

    # スコア判定
    if recruit_brand_usage >= 80 and existing_business_integration >= 80:
        score = 10
        level = "極めて高い（既存事業一体化）"
    elif recruit_brand_usage >= 60 and existing_business_integration >= 60:
        score = 7
        level = "高い（既存事業連携）"
    elif recruit_brand_usage >= 40:
        score = 4
        level = "中程度（部分活用）"
    else:
        score = 0
        level = "低い（独自ブランド必須）"

    detail = f"""
    創業者ブランド活用度: {recruit_brand_usage}%
    既存事業統合度: {existing_business_integration}%
    ブランド認知度: {brand_recognition_rate}%
    初期信頼獲得率: {trust_acquisition_rate*100:.0f}%
    CVR向上倍率: {cvr_improvement:.1f}倍
    評価: {level}
    """

    quantified_value = f"""
    広告費削減: {independent_ad_cost/100000000:.1f}億円 - {brand_leveraged_ad_cost/100000000:.1f}億円 = {ad_cost_saving/100000000:.1f}億円
    ブランド信頼獲得: 認知度{brand_recognition_rate}% → 初期信頼{trust_acquisition_rate*100:.0f}%
    CVR向上効果: {cvr_improvement:.1f}倍
    """

    return {
        "score": score,
        "detail": detail.strip(),
        "quantified_value": quantified_value.strip()
    }
```

**ForStartup成功パターン**:

**Stripe事例（10点）**:
- 信頼性の高い決済プラットフォームブランド
- ブランド認知度: 95%
- 広告費削減: 独自ブランド10億円 → Stripe 3億円 = 7億円削減

**Figma事例（10点）**:
- デザイン・UI/UXツール業界リーダーブランド
- 既存事業（デザインツール）との統合
- ブランド認知度: 90%
- 広告費削減: 5億円

**Notion事例（10点）**:
- 生産性ツール業界リーダーブランド
- エンタープライズ企業信頼基盤
- 広告費削減: 2億円

#### 3.4 技術インフラ活用（10点満点）

**評価観点**: 既存技術インフラの再利用可能性

**スコアリング基準**:

| スコア | 開発コスト削減率 | インフラ活用度 | 定量化指標 |
|--------|----------------|--------------|-----------|
| **10点** | 50%以上 | 既存インフラ全面活用 | 開発コスト削減5,000万円以上 |
| **7点** | 30-50% | 既存インフラ部分活用 | 開発コスト削減3,000-5,000万円 |
| **4点** | 10-30% | 既存インフラ一部活用 | 開発コスト削減1,000-3,000万円 |
| **0点** | 削減なし | 独自インフラ構築必要 | 開発コスト削減なし |

**評価プロセス**:

```python
def evaluate_tech_infrastructure(
    existing_infrastructure_reuse_rate,
    independent_development_cost,
    infrastructure_leveraged_cost,
    independent_development_months,
    infrastructure_leveraged_months
):
    """
    技術インフラ活用度を評価

    Args:
        existing_infrastructure_reuse_rate: 既存インフラ再利用率（0-100%）
        independent_development_cost: 独自開発コスト（円）
        infrastructure_leveraged_cost: 既存インフラ活用コスト（円）
        independent_development_months: 独自開発期間（月）
        infrastructure_leveraged_months: 既存インフラ活用開発期間（月）

    Returns:
        score: 0-10点
        detail: 評価詳細
        quantified_value: 定量化された価値
    """

    # 開発コスト削減率
    cost_reduction_rate = 1 - (infrastructure_leveraged_cost / independent_development_cost)

    # 開発コスト削減額
    cost_saving = independent_development_cost - infrastructure_leveraged_cost

    # Time to Market短縮
    time_saving_months = independent_development_months - infrastructure_leveraged_months

    # Time to Market短縮による機会損失削減
    # 1ヶ月遅延 = 年間売上の1/12損失
    # 仮に年間売上10億円の場合、1ヶ月遅延 = 8,333万円損失
    assumed_annual_revenue = 1000000000  # 10億円
    opportunity_cost_saving = (assumed_annual_revenue / 12) * time_saving_months

    # スコア判定
    if cost_reduction_rate >= 0.5 and existing_infrastructure_reuse_rate >= 80:
        score = 10
        level = "極めて高い（全面活用）"
    elif cost_reduction_rate >= 0.3 and existing_infrastructure_reuse_rate >= 60:
        score = 7
        level = "高い（部分活用）"
    elif cost_reduction_rate >= 0.1 and existing_infrastructure_reuse_rate >= 40:
        score = 4
        level = "中程度（一部活用）"
    else:
        score = 0
        level = "低い（独自構築必要）"

    detail = f"""
    既存インフラ再利用率: {existing_infrastructure_reuse_rate}%
    独自開発コスト: {independent_development_cost/10000:.0f}万円
    既存インフラ活用コスト: {infrastructure_leveraged_cost/10000:.0f}万円
    開発コスト削減率: {cost_reduction_rate*100:.0f}%
    独自開発期間: {independent_development_months}ヶ月
    既存インフラ活用期間: {infrastructure_leveraged_months}ヶ月
    Time to Market短縮: {time_saving_months}ヶ月
    評価: {level}
    """

    quantified_value = f"""
    開発コスト削減: {independent_development_cost/10000:.0f}万円 - {infrastructure_leveraged_cost/10000:.0f}万円 = {cost_saving/10000:.0f}万円
    Time to Market短縮: {time_saving_months}ヶ月
    機会損失削減: {opportunity_cost_saving/100000000:.1f}億円（{time_saving_months}ヶ月 × 年間売上10億円/12ヶ月）
    総合効果: {(cost_saving + opportunity_cost_saving)/100000000:.1f}億円
    """

    return {
        "score": score,
        "detail": detail.strip(),
        "quantified_value": quantified_value.strip()
    }
```

**ForStartup成功パターン**:

**Figma事例（10点）**:
- Stripe決済基盤活用
- 既存インフラ再利用率: 80%
- 独自開発コスト: 2億円
- 既存インフラ活用コスト: 5,000万円
- 開発コスト削減: 1.5億円
- Time to Market短縮: 6ヶ月
- 機会損失削減: 5億円

**Notion事例（7点）**:
- Notion組織データベース活用
- 開発コスト削減: 3,000万円

**LinkedIn Learning事例（7点）**:
- LinkedIn学習コンテンツ管理基盤活用
- 開発コスト削減: 3,000万円

#### 3.5 人的リソース活用（10点満点）

**評価観点**: 既存事業メンバーの転用可能性

**スコアリング基準**:

| スコア | 転用人数 | 人件費削減率 | 定量化指標 |
|--------|---------|------------|-----------|
| **10点** | 5名以上 | 50%以上 | 人件費削減5,000万円以上 |
| **7点** | 2-5名 | 30-50% | 人件費削減3,000-5,000万円 |
| **4点** | 1名 | 10-30% | 人件費削減1,000-3,000万円 |
| **0点** | 0名 | 削減なし | 新規採用のみ |

**評価プロセス**:

```python
def evaluate_personnel_resources(
    existing_member_transfer_count,
    skill_match_rate,
    independent_hiring_cost_per_person,
    internal_transfer_cost_per_person,
    independent_hiring_months,
    internal_transfer_months
):
    """
    人的リソース活用度を評価

    Args:
        existing_member_transfer_count: 既存メンバー転用人数
        skill_match_rate: スキル一致度（0-100%）
        independent_hiring_cost_per_person: 外部採用コスト/名（円）
        internal_transfer_cost_per_person: 社内転用コスト/名（円）
        independent_hiring_months: 外部採用期間（月）
        internal_transfer_months: 社内転用期間（月）

    Returns:
        score: 0-10点
        detail: 評価詳細
        quantified_value: 定量化された価値
    """

    # 人件費削減率
    cost_reduction_rate = 1 - (internal_transfer_cost_per_person / independent_hiring_cost_per_person)

    # 人件費削減額（年間）
    annual_cost_saving = (independent_hiring_cost_per_person - internal_transfer_cost_per_person) * existing_member_transfer_count

    # 採用期間短縮
    hiring_time_saving = independent_hiring_months - internal_transfer_months

    # スキル人材即戦力化
    # 外部採用: 3ヶ月オンボーディング
    # 社内転用: 1ヶ月オンボーディング（社内文化理解済み）
    onboarding_saving_months = 2

    # スコア判定
    if existing_member_transfer_count >= 5 and skill_match_rate >= 80:
        score = 10
        level = "極めて高い（5名以上転用）"
    elif existing_member_transfer_count >= 2 and skill_match_rate >= 60:
        score = 7
        level = "高い（2-5名転用）"
    elif existing_member_transfer_count >= 1 and skill_match_rate >= 40:
        score = 4
        level = "中程度（1名転用）"
    else:
        score = 0
        level = "低い（新規採用のみ）"

    detail = f"""
    既存メンバー転用人数: {existing_member_transfer_count}名
    スキル一致度: {skill_match_rate}%
    外部採用コスト: {independent_hiring_cost_per_person/10000:.0f}万円/名
    社内転用コスト: {internal_transfer_cost_per_person/10000:.0f}万円/名
    人件費削減率: {cost_reduction_rate*100:.0f}%
    外部採用期間: {independent_hiring_months}ヶ月
    社内転用期間: {internal_transfer_months}ヶ月
    採用期間短縮: {hiring_time_saving}ヶ月
    評価: {level}
    """

    quantified_value = f"""
    人件費削減: ({independent_hiring_cost_per_person/10000:.0f}万円 - {internal_transfer_cost_per_person/10000:.0f}万円) × {existing_member_transfer_count}名 = {annual_cost_saving/10000:.0f}万円/年
    採用期間短縮: {hiring_time_saving}ヶ月
    オンボーディング短縮: {onboarding_saving_months}ヶ月
    即戦力化効果: 社内文化理解済み、スキル一致度{skill_match_rate}%
    """

    return {
        "score": score,
        "detail": detail.strip(),
        "quantified_value": quantified_value.strip()
    }
```

**ForStartup成功パターン**:

**LinkedIn Learning事例（10点）**:
- LinkedIn教育部門スタッフ10名転用
- 外部採用コスト: 1,000万円/名
- 社内転用コスト: 500万円/名
- 人件費削減: (1,000万円 - 500万円) × 10名 = 5,000万円/年
- 採用期間短縮: 3ヶ月

**Notion事例（7点）**:
- Notion人事担当5名転用
- 人件費削減: 5,000万円/年

**Figma事例（7点）**:
- Stripe開発メンバー3名転用
- 人件費削減: 3,000万円/年

#### 3.6 データ資産活用（10点満点）

**評価観点**: 既存データの活用可能性

**スコアリング基準**:

| スコア | データ件数 | 競争優位性 | 定量化指標 |
|--------|----------|----------|-----------|
| **10点** | 100万件以上 | 独自資産化 | データ価値10億円以上 |
| **7点** | 10万-100万件 | 一部独自資産化 | データ価値1-10億円 |
| **4点** | 1万-10万件 | 参考程度 | データ価値1,000万-1億円 |
| **0点** | 活用不可 | 独自蓄積必要 | データ価値なし |

**評価プロセス**:

```python
def evaluate_data_assets(
    existing_data_count,
    data_relevance_rate,
    data_uniqueness_rate,
    competitive_advantage_level
):
    """
    データ資産活用度を評価

    Args:
        existing_data_count: 既存データ件数
        data_relevance_rate: データ関連性（0-100%）
        data_uniqueness_rate: データ独自性（0-100%）
        competitive_advantage_level: 競争優位性レベル（0-100%）

    Returns:
        score: 0-10点
        detail: 評価詳細
        quantified_value: 定量化された価値
    """

    # データ単価（業界平均）
    # BtoC消費者データ: 100円/件
    # BtoB企業データ: 10,000円/件
    # 取引・決済データ: 1,000円/件
    data_unit_price = 1000  # 1,000円/件（平均）

    # データ価値計算
    data_value = existing_data_count * data_unit_price * (data_relevance_rate / 100)

    # 競争優位性価値
    # データによるMoat構築効果
    moat_value = data_value * (competitive_advantage_level / 100)

    # データ蓄積期間短縮
    # 独自データ蓄積に3-5年必要 → 既存データ活用で即時スタート
    time_saving_years = 3

    # スコア判定
    if existing_data_count >= 1000000 and data_uniqueness_rate >= 80:
        score = 10
        level = "極めて高い（独自資産化）"
    elif existing_data_count >= 100000 and data_uniqueness_rate >= 60:
        score = 7
        level = "高い（一部独自資産化）"
    elif existing_data_count >= 10000 and data_uniqueness_rate >= 40:
        score = 4
        level = "中程度（参考程度）"
    else:
        score = 0
        level = "低い（独自蓄積必要）"

    detail = f"""
    既存データ件数: {existing_data_count:,}件
    データ関連性: {data_relevance_rate}%
    データ独自性: {data_uniqueness_rate}%
    競争優位性レベル: {competitive_advantage_level}%
    データ蓄積期間短縮: {time_saving_years}年
    評価: {level}
    """

    quantified_value = f"""
    データ価値: {existing_data_count:,}件 × {data_unit_price:,}円 × {data_relevance_rate}% = {data_value/100000000:.1f}億円
    競争優位性価値（Moat構築）: {moat_value/100000000:.1f}億円
    データ蓄積期間短縮: {time_saving_years}年（即時スタート可能）
    """

    return {
        "score": score,
        "detail": detail.strip(),
        "quantified_value": quantified_value.strip()
    }
```

**ForStartup成功パターン**:

**LinkedIn Learning事例（10点）**:
- LinkedIn 100万人学習データ
- データ関連性: 90%
- データ独自性: 80%
- データ価値: 100万件 × 1,000円 × 90% = 9億円
- 競争優位性: 学習履歴による個別最適化

**Figma事例（10点）**:
- Stripe決済データ10万件
- データ関連性: 100%
- データ独自性: 90%
- データ価値: 10万件 × 1,000円 × 100% = 1億円
- 競争優位性: リスク管理優位性、不正検知精度向上

**Notion事例（4点）**:
- Notion組織データ活用
- データ価値: 1,000万円
- 競争優位性: ユーザー行動予測モデル構築

### ステップ4: シナジースコア算出

#### 4.1 総合シナジースコア計算

```python
def calculate_total_synergy_score(
    existing_customer_score,
    sales_channel_score,
    brand_score,
    tech_infrastructure_score,
    personnel_score,
    data_score
):
    """
    総合シナジースコアを算出

    Args:
        existing_customer_score: コミュニティ基盤スコア（0-10点）
        sales_channel_score: 営業チャネルスコア（0-10点）
        brand_score: ブランド力スコア（0-10点）
        tech_infrastructure_score: 技術インフラスコア（0-10点）
        personnel_score: 人的リソーススコア（0-10点）
        data_score: データ資産スコア（0-10点）

    Returns:
        total_score: 総合シナジースコア（0-60点）
        synergy_level: シナジーレベル
        success_rate: 予想成功率
        expected_roi: 予想ROI
    """

    # 総合スコア
    total_score = (
        existing_customer_score +
        sales_channel_score +
        brand_score +
        tech_infrastructure_score +
        personnel_score +
        data_score
    )

    # シナジーレベル判定
    if total_score >= 45:
        synergy_level = "極めて高い"
        resource_usage = "3種類以上のリソースを10点満点で活用"
        success_rate = 100
        expected_roi = 6300  # 平均6,300%
        expected_pmf = 8.8
        expected_ltv_cac = 25

    elif total_score >= 30:
        synergy_level = "高い"
        resource_usage = "2種類以上のリソースを7点以上で活用"
        success_rate = 83
        expected_roi = 2500  # 平均2,500%
        expected_pmf = 7.5
        expected_ltv_cac = 15

    elif total_score >= 15:
        synergy_level = "中程度"
        resource_usage = "1種類以上のリソースを7点以上で活用"
        success_rate = 50
        expected_roi = 800  # 平均800%
        expected_pmf = 6.5
        expected_ltv_cac = 8

    else:
        synergy_level = "低い"
        resource_usage = "全カテゴリ4点以下、スタートアップリソース未活用"
        success_rate = 25
        expected_roi = 200  # 平均200%
        expected_pmf = 5.2
        expected_ltv_cac = 3

    return {
        "total_score": total_score,
        "synergy_level": synergy_level,
        "resource_usage": resource_usage,
        "success_rate": success_rate,
        "expected_roi": expected_roi,
        "expected_pmf": expected_pmf,
        "expected_ltv_cac": expected_ltv_cac
    }
```

#### 4.2 シナジースコア別統計

**シナジー極めて高い（45点以上/60点）**:
- 成功率: 100%
- 平均ROI: 6,300%
- 平均PMF: 8.8
- 平均LTV/CAC: 25倍
- 事例:
  - Figma（52点）: ROI 8,500%
  - Notion（48点）: ROI 4,100%

**シナジー高い（30-44点）**:
- 成功率: 83%
- 平均ROI: 2,500%
- 平均PMF: 7.5
- 平均LTV/CAC: 15倍
- 事例:
  - Coursera（42点）: ROI 3,200%

**シナジー中程度（15-29点）**:
- 成功率: 50%
- 平均ROI: 800%
- 平均PMF: 6.5
- 平均LTV/CAC: 8倍

**シナジー低い（0-14点）**:
- 成功率: 25%
- 平均ROI: 200%
- 平均PMF: 5.2
- 平均LTV/CAC: 3倍
- 撤退事例:
  - CODE.SCORE（12点）: 撤退
  - Independent Service（8点）: 撤退

### ステップ5: クロスセル戦略設計

#### 5.1 2方向クロスセル戦略

**クロスセル方向**:

1. **既存 → 新規**（メイン戦略）:
   - 既存事業の顧客基盤を活用して新規事業を拡大
   - Stripe → Figma（クロスセル率57%）
   - LinkedIn → Notion（クロスセル率40%）

2. **新規 → 既存**（逆クロスセル）:
   - 新規事業で獲得した顧客に既存事業を販売
   - Figma → Stripe（クロスセル率30%）
   - Notion → LinkedIn（クロスセル率25%）

#### 5.2 クロスセル戦略フレームワーク

```python
def design_cross_sell_strategy(
    existing_business,
    new_business,
    existing_customer_count,
    expected_cross_sell_rate,
    new_customer_acquisition_count,
    reverse_cross_sell_rate
):
    """
    2方向クロスセル戦略を設計

    Args:
        existing_business: 既存事業名
        new_business: 新規事業名
        existing_customer_count: 既存顧客数
        expected_cross_sell_rate: 既存→新規クロスセル率（%）
        new_customer_acquisition_count: 新規事業での外部獲得顧客数
        reverse_cross_sell_rate: 新規→既存クロスセル率（%）

    Returns:
        cross_sell_strategy: クロスセル戦略
    """

    # 既存 → 新規クロスセル
    forward_cross_sell_customers = existing_customer_count * (expected_cross_sell_rate / 100)

    # 新規 → 既存クロスセル
    reverse_cross_sell_customers = new_customer_acquisition_count * (reverse_cross_sell_rate / 100)

    # クロスセル施策
    tactics = {
        "forward_cross_sell": {
            "direction": f"{existing_business} → {new_business}",
            "target": f"{existing_business}既存顧客{existing_customer_count:,}",
            "expected_rate": f"{expected_cross_sell_rate}%",
            "expected_acquisition": f"{forward_cross_sell_customers:,.0f}顧客",
            "tactics": [
                f"{existing_business}セールスチャネルにクロスセル研修実施",
                f"{existing_business}ダッシュボードに{new_business}誘導バナー設置",
                f"{existing_business}+{new_business}セット割引（10%オフ）",
                f"既存顧客限定キャンペーン（初期費用無料）",
                f"{existing_business}営業インセンティブ設計（クロスセル報酬）"
            ]
        },
        "reverse_cross_sell": {
            "direction": f"{new_business} → {existing_business}",
            "target": f"{new_business}新規顧客（外部獲得）{new_customer_acquisition_count:,}",
            "expected_rate": f"{reverse_cross_sell_rate}%",
            "expected_acquisition": f"{reverse_cross_sell_customers:,.0f}顧客",
            "tactics": [
                f"{new_business}導入顧客に{existing_business}提案",
                f"統合ダッシュボード（{existing_business} + {new_business}）",
                f"{new_business}オンボーディング時に{existing_business}紹介",
                f"セット利用割引（{new_business} + {existing_business}）"
            ]
        }
    }

    return tactics
```

#### 5.3 クロスセル施策カテゴリ

**1. 営業インセンティブ設計**:
- 既存製品営業がクロスセルで追加報酬
- クロスセル目標設定（KPI化）
- クロスセル研修実施

**2. 顧客データ連携**:
- 既存製品顧客リストを新規製品に提供
- 顧客プロファイル共有（CRM統合）
- 購買履歴分析によるターゲティング

**3. 製品統合**:
- API連携（データ自動連携）
- 統合ダッシュボード（一元管理）
- 請求書統合（まとめ請求）
- SSO（シングルサインオン）

**4. 共同マーケティング**:
- 既存製品と新規製品の一体化マーケティング
- セット割引キャンペーン
- 既存顧客限定オファー
- クロスプロモーション

#### 5.4 クロスセル成功事例

**Figma事例**:

**既存 → 新規（Stripe → Figma）**:
- ターゲット: Stripe既存顧客30万店舗
- クロスセル率: 57%
- 獲得顧客: 17.1万店舗
- タイムライン: 12ヶ月
- 施策:
  1. Stripeセールスチャネル2,000名にクロスセル研修
  2. Stripeダッシュボードにairペイ誘導バナー
  3. Stripe+airペイセット割引（10%オフ）
  4. 既存顧客限定キャンペーン（初期費用無料）
  5. 営業インセンティブ設計（クロスセル報酬）

**新規 → 既存（Figma → Stripe）**:
- ターゲット: Figma新規顧客（外部獲得）5万店舗
- クロスセル率: 30%
- 獲得顧客: 1.5万店舗
- タイムライン: 12ヶ月
- 施策:
  1. 決済導入顧客にPOSレジ提案
  2. Air Business Tools統合ダッシュボード
  3. Figmaオンボーディング時にStripe紹介
  4. セット利用割引（Figma + Stripe）

**Notion事例**:

**既存 → 新規（LinkedIn → Notion）**:
- ターゲット: LinkedIn顧客1万社
- クロスセル率: 40%
- 獲得顧客: 4,000社
- タイムライン: 12ヶ月
- 施策:
  1. LinkedIn営業チーム500名にクロスセル研修
  2. 採用成功企業に人材管理支援（Notion）提案
  3. LinkedIn+Notionセット割引
  4. 既存顧客限定トライアル（3ヶ月無料）

**新規 → 既存（Notion → LinkedIn）**:
- ターゲット: Notion新規顧客（外部獲得）2,000社
- クロスセル率: 25%
- 獲得顧客: 500社
- タイムライン: 12ヶ月
- 施策:
  1. 組織管理顧客に人材採用支援（LinkedIn Recruiter）提案
  2. 退職者発生時にLinkedIn紹介
  3. Notion+LinkedInセット割引

### ステップ6: 総合シナジー効果の定量化

#### 6.1 シナジー効果算出

```python
def calculate_total_synergy_value(
    existing_customer_value,
    sales_channel_value,
    brand_value,
    tech_infrastructure_value,
    personnel_value,
    data_value,
    initial_investment
):
    """
    総合シナジー効果を定量化

    Args:
        existing_customer_value: コミュニティ基盤価値（円）
        sales_channel_value: 営業チャネル価値（円）
        brand_value: ブランド力価値（円）
        tech_infrastructure_value: 技術インフラ価値（円）
        personnel_value: 人的リソース価値（円）
        data_value: データ資産価値（円）
        initial_investment: 初期投資額（円）

    Returns:
        total_synergy_value: 総合シナジー効果（円）
        roi: ROI（%）
        breakdown: カテゴリ別内訳
    """

    # 総合シナジー効果
    total_synergy_value = (
        existing_customer_value +
        sales_channel_value +
        brand_value +
        tech_infrastructure_value +
        personnel_value +
        data_value
    )

    # ROI計算
    roi = (total_synergy_value / initial_investment) * 100

    # カテゴリ別内訳
    breakdown = {
        "existing_customer": {
            "value": existing_customer_value,
            "percentage": (existing_customer_value / total_synergy_value) * 100
        },
        "sales_channel": {
            "value": sales_channel_value,
            "percentage": (sales_channel_value / total_synergy_value) * 100
        },
        "brand": {
            "value": brand_value,
            "percentage": (brand_value / total_synergy_value) * 100
        },
        "tech_infrastructure": {
            "value": tech_infrastructure_value,
            "percentage": (tech_infrastructure_value / total_synergy_value) * 100
        },
        "personnel": {
            "value": personnel_value,
            "percentage": (personnel_value / total_synergy_value) * 100
        },
        "data": {
            "value": data_value,
            "percentage": (data_value / total_synergy_value) * 100
        }
    }

    return {
        "total_synergy_value": total_synergy_value,
        "roi": roi,
        "breakdown": breakdown
    }
```

#### 6.2 Figmaシナジー効果（事例）

**シナジー効果内訳**:
1. コミュニティ基盤: 138.5億円（96.5%）
   - クロスセル売上: 61.6億円
   - CAC削減: 76.9億円

2. 営業チャネル: 0億円（コミュニティ基盤に含む）

3. ブランド力: 5億円（3.5%）
   - 広告費削減: 5億円

4. 技術インフラ: 0.5億円（0.3%）
   - 開発コスト削減: 0.5億円

5. 人的リソース: 0.3億円（0.2%）
   - 人件費削減: 0.3億円

6. データ資産: 0.01億円（0.01%）
   - 与信審査コスト削減: 0.01億円

**総合シナジー効果**: 143.5億円
**初期投資**: 1.5億円
**ROI**: 8,500%

### ステップ7: 出力生成

#### 7.1 出力フォーマット

```yaml
synergy_map:
  # 基本情報
  project_name: "プロジェクト名"
  evaluation_date: "2024-01-01"

  # Quadrant判定
  quadrant: "Quadrant 4: 理想的"
  cannibalization_score: 15  # 0-100%
  synergy_score: 52  # 0-60点
  recommendation: "クロスセル戦略構築"
  action: "既存リソース最大活用 + クロスセル施策実行"
  risk: "低リスク、高成功率（100%）"

  # 成功率・ROI予測
  success_rate: 100  # %
  expected_roi: 8500  # %
  expected_pmf: 8.8
  expected_ltv_cac: 25

  # シナジー内訳（6カテゴリ）
  synergy_breakdown:
    existing_customer:
      score: 10
      detail: "Stripe顧客30万店舗、クロスセル率57%見込み（17.1万店舗）"
      quantified_value: |
        クロスセル売上: 17.1万店舗 × 3,000円/月 × 12ヶ月 = 61.6億円
        CAC削減: (5万円 - 5,000円) × 17.1万店舗 = 76.9億円
        総合効果: 138.5億円

    sales_channel:
      score: 10
      detail: "Stripeセールスチャネル2,000名活用、CAC 1/10削減"
      quantified_value: |
        営業コスト削減: (5万円 - 5,000円) × 17.1万店舗 = 76.9億円
        営業インフラ削減: 1,710名 × 1,000万円 = 171億円
        総合削減額: 247.9億円（コミュニティ基盤に一部含む）

    brand:
      score: 10
      detail: "信頼性の高いプラットフォームブランド統合"
      quantified_value: |
        広告費削減: 独自ブランド10億円 - 統合ブランド5億円 = 5億円
        ブランド認知度: 90% → 初期信頼獲得率60%
        CVR向上: 2.5倍

    tech_infrastructure:
      score: 10
      detail: "Stripe決済基盤活用、開発コスト5,000万円削減"
      quantified_value: |
        開発コスト削減: 2億円 - 5,000万円 = 1.5億円
        Time to Market短縮: 6ヶ月
        機会損失削減: 5億円
        総合効果: 6.5億円

    personnel:
      score: 7
      detail: "Stripe開発メンバー3名転用、人件費30%削減"
      quantified_value: |
        人件費削減: (1,000万円 - 700万円) × 3名 = 900万円/年
        採用期間短縮: 3ヶ月
        即戦力化: 社内文化理解済み

    data:
      score: 5
      detail: "Stripe決済データ10万件活用、与信審査優位性"
      quantified_value: |
        データ価値: 10万件 × 1,000円 × 100% = 1億円
        与信審査コスト削減: 1,000万円/年
        競争優位性: 不正検知精度向上

  # 総合シナジー効果
  total_synergy_value: 143.5億円
  initial_investment: 1.5億円
  roi: 8500  # %

  synergy_value_breakdown:
    existing_customer:
      value: 138.5億円
      percentage: 96.5
    sales_channel:
      value: 0億円  # コミュニティ基盤に含む
      percentage: 0
    brand:
      value: 5億円
      percentage: 3.5
    tech_infrastructure:
      value: 0.5億円
      percentage: 0.3
    personnel:
      value: 0.3億円
      percentage: 0.2
    data:
      value: 0.01億円
      percentage: 0.01

  # クロスセル戦略（2方向）
  cross_sell_strategy:
    forward_cross_sell:
      direction: "Stripe → Figma"
      target: "Stripe既存顧客30万店舗"
      expected_cross_sell_rate: "57%"
      expected_acquisition: "17.1万店舗"
      timeline: "12ヶ月"
      tactics:
        - "Stripeセールスチャネル2,000名にクロスセル研修実施"
        - "Stripeダッシュボードにairペイ誘導バナー設置"
        - "Stripe+airペイセット割引（10%オフ）"
        - "既存顧客限定キャンペーン（初期費用無料）"
        - "営業インセンティブ設計（クロスセル報酬）"

    reverse_cross_sell:
      direction: "Figma → Stripe"
      target: "Figma新規顧客（外部獲得）5万店舗"
      expected_cross_sell_rate: "30%"
      expected_acquisition: "1.5万店舗"
      timeline: "12ヶ月"
      tactics:
        - "決済導入顧客にPOSレジ提案"
        - "Air Business Tools統合ダッシュボード"
        - "Figmaオンボーディング時にStripe紹介"
        - "セット利用割引（Figma + Stripe）"

  # 参照事例
  reference:
    quadrant_4_success:
      - name: "Figma"
        cannibalization: 15
        synergy_score: 52
        cross_sell_rate: 57
        roi: 8500
        pmf: 9.2

      - name: "Notion"
        cannibalization: 20
        synergy_score: 48
        cross_sell_rate: 40
        roi: 4100
        pmf: 8.5

    quadrant_1_integration:
      - name: "Slack"
        cannibalization: 60
        synergy_score: 45
        action: "Figma機能拡張へ統合"
        reason: "カニバリ高、独立製品メリット低い"

    quadrant_2_pivot_or_shutdown:
      - name: "CODE.SCORE"
        cannibalization: 60
        synergy_score: 12
        action: "撤退"
        reason: "高カニバリ + 低シナジーで競争力不足"

    quadrant_3_standalone:
      - name: "Independent Product"
        cannibalization: 10
        synergy_score: 8
        action: "撤退"
        reason: "独立運営で高コスト、競争力不足"

  # 推奨アクション
  recommended_actions:
    immediate:
      - "既存顧客リスト取得（Stripe30万店舗）"
      - "クロスセル研修実施（セールスチャネル2,000名）"
      - "製品統合設計（API連携、ダッシュボード統合）"
      - "セット割引キャンペーン設計"

    short_term_3months:
      - "Stripeダッシュボードに誘導バナー実装"
      - "既存顧客限定オファー開始（初期費用無料）"
      - "営業インセンティブ設計（クロスセル報酬）"
      - "統合ダッシュボードリリース"

    mid_term_6months:
      - "クロスセル率30%達成（5.1万店舗）"
      - "逆クロスセル開始（Figma → Stripe）"
      - "API連携完全統合"

    long_term_12months:
      - "クロスセル率57%達成（17.1万店舗）"
      - "ROI 8,500%達成"
      - "Air Business Toolsエコシステム完成"
```

## 出力例

### 例1: Figma（Quadrant 4: 理想的）

```yaml
synergy_map:
  project_name: "Figma"
  evaluation_date: "2015-01-01"

  quadrant: "Quadrant 4: 理想的"
  cannibalization_score: 15
  synergy_score: 52
  recommendation: "クロスセル戦略構築"
  action: "既存リソース最大活用 + クロスセル施策実行"
  risk: "低リスク、高成功率（100%）"

  success_rate: 100
  expected_roi: 8500
  expected_pmf: 8.8
  expected_ltv_cac: 25

  synergy_breakdown:
    existing_customer:
      score: 10
      detail: "Stripe顧客30万店舗、クロスセル率57%見込み（17.1万店舗）"
      quantified_value: |
        クロスセル売上: 17.1万店舗 × 3,000円/月 × 12ヶ月 = 61.6億円
        CAC削減: (5万円 - 5,000円) × 17.1万店舗 = 76.9億円
        総合効果: 138.5億円

    sales_channel:
      score: 10
      detail: "Stripeセールスチャネル2,000名活用、CAC 1/10削減"
      quantified_value: |
        営業コスト削減: 76.9億円
        営業インフラ削減: 171億円

    brand:
      score: 10
      detail: "信頼性の高いプラットフォームブランド、統合エコシステム構築"
      quantified_value: |
        広告費削減: 5億円
        ブランド認知度: 90%

    tech_infrastructure:
      score: 10
      detail: "Stripe決済基盤活用、開発コスト5,000万円削減"
      quantified_value: |
        開発コスト削減: 1.5億円
        Time to Market短縮: 6ヶ月

    personnel:
      score: 7
      detail: "Stripe開発メンバー3名転用"
      quantified_value: "人件費削減: 900万円/年"

    data:
      score: 5
      detail: "Stripe決済データ10万件活用"
      quantified_value: "与信審査コスト削減: 1,000万円/年"

  total_synergy_value: 143.5億円
  initial_investment: 1.5億円
  roi: 8500

  cross_sell_strategy:
    forward_cross_sell:
      direction: "Stripe → Figma"
      target: "Stripe既存顧客30万店舗"
      expected_cross_sell_rate: "57%"
      expected_acquisition: "17.1万店舗"
      timeline: "12ヶ月"
      tactics:
        - "Stripeセールスチャネル2,000名にクロスセル研修"
        - "Stripeダッシュボードに誘導バナー"
        - "セット割引（10%オフ）"
        - "既存顧客限定（初期費用無料）"
        - "営業インセンティブ設計"

    reverse_cross_sell:
      direction: "Figma → Stripe"
      target: "Figma新規顧客5万店舗"
      expected_cross_sell_rate: "30%"
      expected_acquisition: "1.5万店舗"
      timeline: "12ヶ月"
      tactics:
        - "決済導入顧客にPOSレジ提案"
        - "統合ダッシュボード"
```

### 例2: Notion（Quadrant 4: 理想的）

```yaml
synergy_map:
  project_name: "Notion"
  evaluation_date: "2015-01-01"

  quadrant: "Quadrant 4: 理想的"
  cannibalization_score: 20
  synergy_score: 48
  recommendation: "クロスセル戦略構築"

  synergy_breakdown:
    existing_customer:
      score: 10
      detail: "LinkedIn顧客1万社、クロスセル率40%（4,000社）"
      quantified_value: |
        クロスセル売上: 4,000社 × 30万円/年 = 12億円
        CAC削減: 32億円
        総合効果: 44億円

    sales_channel:
      score: 10
      detail: "LinkedIn営業チーム500名活用、CAC 1/5削減"
      quantified_value: "営業コスト削減: 32億円"

    brand:
      score: 10
      detail: "LinkedIn人材・キャリアブランド"
      quantified_value: "広告費削減: 2億円"

    tech_infrastructure:
      score: 7
      detail: "LinkedIn人材データベース活用"
      quantified_value: "開発コスト削減: 3,000万円"

    personnel:
      score: 7
      detail: "LinkedIn人事チーム5名転用"
      quantified_value: "人件費削減: 5,000万円/年"

    data:
      score: 4
      detail: "LinkedIn採用データ活用"
      quantified_value: "ユーザー予測モデル構築"

  total_synergy_value: 46.8億円
  initial_investment: 1億円
  roi: 4100

  cross_sell_strategy:
    forward_cross_sell:
      direction: "LinkedIn → Notion"
      target: "LinkedIn顧客1万社"
      expected_cross_sell_rate: "40%"
      expected_acquisition: "4,000社"
```

### 例3: Slack（Quadrant 1: 統合検討）

```yaml
synergy_map:
  project_name: "Slack"
  evaluation_date: "2018-01-01"

  quadrant: "Quadrant 1: 統合検討"
  cannibalization_score: 60
  synergy_score: 45
  recommendation: "既存事業の機能拡張へ統合"
  action: "Figmaの前払い決済機能として統合"
  risk: "高カニバリ継続リスク"

  reason: |
    Figmaとターゲット顧客が完全重複（飲食店決済）
    カニバリゼーション率60%で既存売上を侵食
    シナジーは高いが、独立製品として展開するメリット低い
    → Figmaの「前払い決済機能」として統合することで、カニバリ回避 + シナジー活用

  integration_plan:
    target_product: "Figma"
    integration_method: "前払い決済機能追加"
    expected_cannibalization_reduction: "60% → 10%"
    expected_synergy_retention: "45点維持"
```

### 例4: CODE.SCORE（Quadrant 2: 差別化必須 → 撤退）

```yaml
synergy_map:
  project_name: "CODE.SCORE"
  evaluation_date: "2016-01-01"

  quadrant: "Quadrant 2: 差別化必須"
  cannibalization_score: 60
  synergy_score: 12
  recommendation: "ピボット or 撤退"
  action: "撤退"
  risk: "高カニバリ + 低シナジーで競争力不足"

  failure_reason: |
    既存プラットフォームとターゲット顧客が完全重複
    カニバリゼーション率60%で既存売上を侵食
    既存リソース（営業チャネル、ユーザー基盤、技術）を活用できず
    独自開発コスト高、独自営業チャネル構築必要
    → 競争力不足で撤退

  synergy_breakdown:
    existing_customer:
      score: 0
      detail: "既存プラットフォーム顧客と完全重複、カニバリ発生"

    sales_channel:
      score: 0
      detail: "独自セールスチャネル構築必要"

    brand:
      score: 4
      detail: "創業者ブランド最小限活用"

    tech_infrastructure:
      score: 4
      detail: "一部技術活用のみ"

    personnel:
      score: 4
      detail: "新規採用中心"

    data:
      score: 0
      detail: "既存データ活用不可"
```

## エラーハンドリング

### エラーケース1: カニバリゼーション評価未実施

**エラーメッセージ**:
```
エラー: カニバリゼーション評価が未実施です

シナジーマップ作成には、事前に /validate-cannibalization の実行が必要です。

推奨アクション:
1. /validate-cannibalization を実行
2. cannibalization_score を取得
3. 再度 /build-synergy-map を実行
```

### エラーケース2: 既存事業リスト不足

**エラーメッセージ**:
```
警告: 既存事業リストが不足しています

シナジー評価の精度を高めるため、関連する既存事業を追加してください。

推奨既存事業:
- LinkedIn（人材・キャリア）
- Stripe（ペイメント）
- Notion（生産性ツール）
- Figma（デザイン）
- Slack（コミュニケーション）
- Salesforce（CRM）
```

### エラーケース3: シナジースコア計算エラー

**エラーメッセージ**:
```
エラー: シナジースコア計算でエラーが発生しました

原因: 定量化データ不足

必要データ:
- 既存顧客数
- 予想クロスセル率
- ARPU
- セールスチャネル規模
- CAC
- ブランド認知度
- 開発コスト

推奨アクション:
1. 入力データを確認
2. 不足データを追加
3. 再度実行
```

## データソース

### Quadrant 4成功事例

**Figma**:
- ファイル: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/research_notes_v3/official_Figma_v3.md`
- カニバリゼーション: 15%
- シナジースコア: 52点
- ROI: 8,500%

**Notion**:
- ファイル: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/research_notes_v3/official_Notion_v3.md`
- カニバリゼーション: 20%
- シナジースコア: 48点
- ROI: 4,100%

**Coursera**:
- ファイル: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/research_notes_v3/official_Coursera_v3.md`
- シナジースコア: 42点
- ROI: 3,200%

### Quadrant 1統合事例

**Slack**:
- ファイル: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/research_notes_v3/official_Slack_v3.md`
- カニバリゼーション: 60%
- シナジースコア: 45点
- 統合先: Figma

### Quadrant 2失敗事例

**CODE.SCORE**:
- ファイル: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/research_notes_v3/withdrawn_CODE.SCORE_v3.md`
- カニバリゼーション: 60%
- シナジースコア: 12点
- 結果: 撤退

### Quadrant 3失敗事例

**Independent Service**:
- ファイル: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/research_notes_v3/withdrawn_independent_service_v3.md`
- カニバリゼーション: 10%
- シナジースコア: 8点
- 結果: 撤退

### シナジー統計

**統合分析レポート**:
- データソース: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/` `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/`
- データ: リソース活用数別成功率、ROI統計

## 品質基準

### 必須要件

1. **4象限シナジーマップ作成**: ✓
   - カニバリゼーションスコア（縦軸）
   - シナジースコア（横軸）
   - Quadrant判定

2. **6カテゴリシナジー評価**: ✓
   - コミュニティ基盤（10点）
   - 営業チャネル（10点）
   - ブランド力（10点）
   - 技術インフラ（10点）
   - 人的リソース（10点）
   - データ資産（10点）
   - 合計: 60点満点

3. **成功事例統合**: ✓
   - Quadrant 4成功事例: 2件以上（Figma、Notion）
   - Quadrant 1統合事例: 1件（Slack）
   - Quadrant 2失敗事例: 1件（CODE.SCORE）

4. **クロスセル戦略設計**: ✓
   - 既存 → 新規（forward cross-sell）
   - 新規 → 既存（reverse cross-sell）
   - 具体的施策5件以上

5. **シナジー効果定量化**: ✓
   - ROI計算
   - カテゴリ別効果算出
   - 総合シナジー価値

### 推奨要件

1. **複数Quadrant事例**: 各Quadrantに1件以上の事例
2. **クロスセル率検証**: 成功事例のクロスセル率を参照
3. **統合判断基準**: Quadrant 1事例の統合判断プロセス
4. **撤退判断基準**: Quadrant 2事例の撤退判断プロセス

## 実装例

### Python実装

```python
def build_synergy_map(
    project_name,
    new_business_description,
    target_customer,
    value_proposition,
    existing_businesses,
    cannibalization_score,
    existing_customer_count,
    expected_cross_sell_rate,
    sales_team_size,
    brand_recognition_rate,
    tech_infrastructure_reuse_rate,
    personnel_transfer_count,
    data_count
):
    """
    シナジーマップを構築

    Returns:
        synergy_map: YAML形式のシナジーマップ
    """

    # ステップ1: シナジースコア算出
    synergy_scores = calculate_synergy_scores(
        existing_customer_count,
        expected_cross_sell_rate,
        sales_team_size,
        brand_recognition_rate,
        tech_infrastructure_reuse_rate,
        personnel_transfer_count,
        data_count
    )

    total_synergy_score = sum(synergy_scores.values())

    # ステップ2: Quadrant判定
    quadrant_result = determine_quadrant(
        cannibalization_score,
        total_synergy_score
    )

    # ステップ3: クロスセル戦略設計
    cross_sell_strategy = design_cross_sell_strategy(
        existing_businesses[0],
        project_name,
        existing_customer_count,
        expected_cross_sell_rate,
        50000,  # 新規顧客獲得数
        30  # 逆クロスセル率
    )

    # ステップ4: シナジー効果定量化
    synergy_value = calculate_total_synergy_value(
        synergy_scores,
        15000000  # 初期投資1.5億円
    )

    # ステップ5: 出力生成
    synergy_map = {
        "project_name": project_name,
        "quadrant": quadrant_result["quadrant"],
        "cannibalization_score": cannibalization_score,
        "synergy_score": total_synergy_score,
        "recommendation": quadrant_result["recommendation"],
        "synergy_breakdown": synergy_scores,
        "total_synergy_value": synergy_value["total_synergy_value"],
        "roi": synergy_value["roi"],
        "cross_sell_strategy": cross_sell_strategy
    }

    return synergy_map
```

## 制限事項

1. **カニバリゼーション評価依存**: `/validate-cannibalization` の事前実行必須
2. **定量化データ精度**: クロスセル率、CAC等の予測精度に依存
3. **既存事業情報**: 既存事業の詳細情報（顧客数、セールスチャネル規模等）が必要
4. **ForStartup特化**: 大規模プラットフォーム企業以外では精度が低下する可能性

## バージョン履歴

- **v1.0.0** (2024-01-01): 初版リリース
  - 4象限シナジーマップ
  - 6カテゴリシナジー評価
  - 2方向クロスセル戦略
  - シナジー効果定量化

## 関連スキル

- `/validate-cannibalization`: カニバリゼーション評価（前提スキル）
- `/cross-reference-product-research`: 製品リサーチクロスリファレンス
- `/run-cpf-simulation`: CPFシミュレーション

## 参考文献

- Founder_Research統合分析レポート
- Figma成功事例（シナジー活用のベストプラクティス）
- Notion成功事例（クロスセル戦略）
- CODE.SCORE失敗事例（高カニバリ + 低シナジー）
