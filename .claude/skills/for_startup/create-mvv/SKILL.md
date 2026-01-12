---
name: create-mvv-for-startup
description: |
  Edition-specific: MVV（Mission/Vision/Values）を早期定義する自律実行型スキル。VC投資基準（スケーラビリティ、市場機会、チーム力）との整合性チェックを必須化し、グローバル展開戦略とのシナジー評価を追加します。

  Edition-specific features:
  - VC投資視点: 10x成長、グローバル展開を意識したビジョン設定
  - スケーラビリティ重視: TAM $1B+市場を前提とした大胆なビジョン
  - 創業者フィット: Founder-Issue-Fitを反映した本質的なMission
  - 成長ストーリー: Seed → Series A → IPO/M&Aまでの一貫した価値観

  使用タイミング:
  - ビジネスアイデアが固まった段階
  - リーンキャンバス作成前後
  - 組織の理念を明確化したい（Seed調達Seed Stage段階）

  所要時間: 20-40分（自動実行）
  出力: mvv.md
trigger_keywords:
  - "/for-startup-create-mvv"
  - "MVV作成"
  - "ミッション策定"
  - "ビジョン策定"
  - "create MVV"
  - "mission vision values"
stage: "planning"
dependencies:
  - discover-demand（需要発見完了推奨）
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup/documents/1_initiating/mvv.md
---

# Create MVV Skill (ForStartup Edition)

MVV（Mission/Vision/Values）を早期定義する自律実行型Skill。**ForStartup特化版**では、VC投資対象としてのビジョン（10x成長、グローバル展開）を重視し、創業者フィットと成長ストーリーの一貫性を検証します。

---

## このSkillでできること

1. **Mission定義**: 何のために存在するか（存在意義）を明確化
2. **Vision定義**: どこを目指すか（目指す未来）を描画
3. **Values定義**: どう行動するか（行動指針）を策定
4. **VC投資視点チェック**: 10x成長、グローバル展開を意識したビジョンの検証（ForStartup追加）
5. **創業者フィット評価**: Founder-Issue-Fitを反映した本質的なMissionの確認（ForStartup追加）
6. **MVV整合性検証**: MVV 3要素の相互整合性を確認
7. **Lean Canvas整合**: リーンキャンバスとの整合性を検証

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `business_idea.md` (オプション), `lean_canvas.md` (オプション) |
| **出力** | `{IDEA_FOLDER}/documents/1_initiating/mvv.md` |
| **次のSkill** | `/build-flywheel` または `/orchestrate-phase1-startup` |

### 入力ファイル詳細

| ファイル | パス | 必須/オプション | 未存在時の動作 |
|---------|------|----------------|--------------|
| business_idea.md | `{IDEA_FOLDER}/documents/1_initiating/business_idea.md` | オプション | demand_discovery.mdから推論 |
| lean_canvas.md | `{IDEA_FOLDER}/documents/2_discovery/lean_canvas.md` | オプション | business_idea.mdから推論 |

**フォールバック戦略**:
1. lean_canvas.md → business_idea.md → demand_discovery.md → ユーザー入力から推論

---

## Domain-Specific Knowledge (from Founder_Research)

### Success Patterns

#### 1. Infrastructure Startup - スケーラビリティ軸

**MVV構造**:
- **Mission**: 開発者がインフラ構築に費やす時間をゼロに近づけ、プロダクト開発に集中できる世界を実現する
- **Vision**: 全世界のスタートアップがワンクリックで本番級インフラをデプロイできるプラットフォーム
- **Values**:
  1. 開発者ファースト: 複雑さを徹底的に排除し、最小限の設定で動作
  2. スピード重視: セットアップ時間を5分以内に短縮
  3. スケーラビリティ: ユーザー数増加に自動追従、エンジニアリング負荷ゼロ

**VC投資基準との整合性**:
- ✅ **スケーラビリティ**: インフラ自動スケーリング、水平展開可能なアーキテクチャ
- ✅ **10倍優位性**: 競合比50倍高速セットアップ、コスト80%削減
- ✅ **市場機会**: TAM $50B（グローバルクラウド市場）、250万スタートアップがターゲット

**グローバル展開ロードマップ**:
- Seed期: US西海岸スタートアップ50社での実証（3ヶ月）
- Series A: ヨーロッパ・APAC展開、カスタマー事例100社を営業資料に
- Series B: エンタープライズ向けコンプライアンス対応、ISO/SOC2取得

#### 2. Developer Tools SaaS - プラットフォーム軸

**MVV構造（API Management例）**:
- **Mission**: エンタープライズの複雑なAPI管理と監視を自動化し、開発効率を加速させる
- **Vision**: 全世界のエンタープライズがAPI First戦略を実行でき、新サービス開発を3倍高速化できる世界
- **Values**:
  1. 開発者中心: 複雑さ排除、CLI/SDK/Webhookで最小学習曲線
  2. エコシステム統合: GitHub、AWS、Datadog等150+ツール連携、DevOps効率5倍向上
  3. データドリブン: API パフォーマンス可視化、本番環境の透視

**VC投資基準との整合性**:
- ✅ **10倍優位性**: 競合比3倍高速なデプロイ、統合費用50%削減
- ✅ **市場機会**: TAM $25B（エンタープライズAPI管理市場）、5万以上の潜在カスタマー
- ✅ **スケーラビリティ**: SaaS提供で地理的制限なし、新地域追加コスト逓減

**成長戦略**:
- Seed期: Fortune 500の開発チーム20社でベータテスト、LTV検証
- Series A: Slack、Stripe等デベロッパープラットフォームとのパートナーシップ、チャネル多角化
- Series B: エンタープライズセールス体制確立、年間サポート売上30%達成

#### 3. B2B Marketplace - ネットワーク効果軸

**MVV構造**:
- **Mission**: 製造業企業とサプライヤーをリアルタイムで繋ぎ、サプライチェーン全体の効率化を実現する
- **Vision**: 全製造業がリアルタイム発注・在庫管理を実現でき、サプライチェーンコストが50%削減される世界
- **Values**:
  1. 透明性重視: 価格・在庫・納期をすべて可視化、比較可能な構造
  2. 買い手・売り手WinWin: 手数料体系で双方の経済性を最大化
  3. データエコシステム: サプライチェーン分析によるコスト改善提案

**グローバルスケーリング戦略**:
- Series A: 既存顧客ネットワークからサプライヤー1,000社リクルート
- Series B: アジア太平洋地域展開、GMV $1B達成
- Series C: 北米・ヨーロッパ展開、ユニットエコノミクス確立

### Common Pitfalls

#### 1. スタディサプリ個別指導 - 既存製品カニバリゼーション

**MVV構造の問題**:
- **Mission**: すべての学習者に個別最適化された教育を提供する
- **Vision**: 教育の機会均等、オンライン個別指導の普及
- **Values**: 個別最適化、低価格化、アクセシビリティ向上

**失敗の本質**:
- 市場検証不足（PMFなしで資金調達）で安易にスケーリング開始
- 顧客セグメント混同（大企業向けと中小企業向けの同時展開）
- Missionと実装のギャップ（「顧客ファースト」を謳いながら不透明な価格体系）
- CAC回収期間が25ヶ月 → VC基準12ヶ月に大幅超過
- 結果: $5Mの資金で事業継続不可に

**教訓**:
- MVV策定時にCAC/LTV検証を必須化（LTV/CAC 5.0以上確保）
- ユニットエコノミクス達成まで地理的展開を遅延
- Missionが実装とズレていないか繰り返し検証

#### 2. Crowdsourced Logistics - 規制リスク軽視

**MVV構造の問題**:
- **Mission**: ギグワーカーとして個人が自由に配送業務を受託
- **Vision**: 10分単位で働ける世界、フレキシブルな雇用創出
- **Values**: スピード、個人の自由、低コスト配送

**失敗の本質**:
- **労働法遵守の甘さ**: ワーカーを「独立請負人」と偽り、給与・保険責任を回避
- **VC投資家の審査不足**: ESG規準を無視したビジネスモデルへの投資
- **規制当局との対立**: 複数国で労働法違反で訴追、営業停止
- **Missionと実装の矛盾**: 「個人の自由」を謳きながら実際には時給固定・強制割り当て
- 結果: $100Mの資金調達後、労働訴訟で破産

**教訓**:
- MVV策定時に**労働法、規制要件**を必須チェック項目化
- 意図的な法回避ではなく「将来の規制変更への準備」をMissionに反映
- VC投資家とのESGガバナンス基準の整合性確認

#### 3. CODE.SCORE - ターゲット市場とのミスマッチ

**MVV構造の問題**:
- **Mission**: エンジニアスキルを可視化し、教育の質を向上させる
- **Vision**: すべての教育機関でエンジニアスキル評価が標準化される
- **Values**: 技術力重視、客観的評価、教育効果最大化

**失敗の本質**:
- 市場調査なしにProposed Solutionを作成開始
- Missionと実際の市場ニーズが大きくズレ（スキル可視化 vs AI学習支援の要望）
- 競合（atama+等）が既に10倍優れたAI学習システムを提供
- PMFテストなしで早期にスケール投資、CAC $5000に対しLTVは$3000
- 結果: Series Aラウンド資金を失耗、2年で撤退

**教訓**:
- MVV→PMFテスト→Series A投資の順序は絶対
- 「自社が提供したいMission」ではなく「顧客の最大ペイン」を起点に
- 10倍競争優位性がない領域では、スケール前に差別化軸を確立

### Quantitative Benchmarks

#### MVV品質スコア（成功製品 vs 失敗製品）

| 指標 | 成功製品 | 失敗製品 | 差分 |
|------|---------|---------|------|
| **VC投資基準適合性** | 8.5/10点 | 4.2/10点 | **2.0倍** |
| **PMF達成度** | 確立済み（Paypalモーメント明確） | 未検証（カスタマーの困りごと不明） | **決定的差** |
| **10倍優位性** | 3軸以上明確 | 0.5軸以下（競合有利） | **6倍以上** |
| **Lean Canvas整合性** | 9.2/10点 | 5.0/10点 | **1.8倍** |

#### VC投資家が重視するMVV評価基準

| 基準 | 定義 | VC評価が高い企業 |
|------|------|-----------------|
| **スケーラビリティ** | TAM $1B+でエコノミクス逓減 | Stripe（支払い処理自動化による無限スケール） |
| **10倍優位性** | 3軸以上で競合に圧倒的優位 | Figma（UI/UX、リアルタイム協調、クラウド原生） |
| **市場のターニング** | 市場成長率 >30%で成長可能 | OpenAIの登場時期（LLM革命のターニング） |
| **チーム実行力** | 過去成功起業家による実装力 | Y Combinator出身者による実行力 |
| **ユニットエコノミクス** | LTV/CAC ≥5.0、CAC回収≤12ヶ月 | SaaS企業の財務健全性指標 |

### Best Practices

#### 1. VC投資基準との整合性チェック

**チェック方法**:
```markdown
## VC投資基準整合性チェック（5項目×2軸）

| 基準項目 | 重要度 | 達成状況 | 根拠 | VC評価 |
|---------|:------:|:-------:|------|:------:|
| **タム・市場規模** | 必須 | ✅/⚠️/❌ | TAM $1B+か | S/A/B |
| **10倍優位性** | 必須 | ✅/⚠️/❌ | 3軸以上か | S/A/B |
| **ユニットエコノミクス** | 必須 | ✅/⚠️/❌ | LTV/CAC≥5.0か | S/A/B |
| **市場ターニング** | 重要 | ✅/⚠️/❌ | 市場成長>30%か | S/A/B |
| **チーム実行力** | 重要 | ✅/⚠️/❌ | 過去成功事例あるか | S/A/B |

**合格基準**: 5項目中**必須3項目は全てS/A評価、重要2項目は最低1つS/A**が必要
```

#### 2. グローバル展開パイプラインの検証

**評価軸**:
1. **地域別市場機会**: 各地域でのTAM、成長率、競合状況の差分
2. **現地化可能性**: Productの調整コスト、法規制対応の複雑さ
3. **チャネル多角化**: 直販、パートナーシップ、マーケットプレイスの組み合わせ
4. **資本効率**: 各地域のCAC、LTV、回収期間の見通し

**評価フォーマット**:
```markdown
## グローバル展開パイプライン評価

| 地域 | TAM | 成長率 | 現地化コスト | CAC見通し | Series評価 |
|------|:---:|:-----:|:----------:|:-------:|:--------:|
| 北米 | $5B | 25% | 低（英語） | $2000 | **Seed** |
| APAC | $3B | 35% | 中（言語） | $1500 | **Series A** |
| EU | $2B | 18% | 高（規制） | $3000 | **Series B** |

**総合拡大戦略**: [段階的地域展開パス]
**規制リスク対策**: [各地域の対応内容]
```

#### 3. PMFテスト前提のMVV設計

**Stripeモデル（支払い処理自動化）**:
1. **顧客深掘り**: 初期ターゲット（Y Combinator企業）での密集インタビュー
2. **最小実装版**: 3ヶ月で基本機能MVP、コード行数300以下の最小化
3. **メトリクス検証**: Paypal Momentを明確化（導入直後のCAC回収率70%達成）
4. **スケーリング投資**: PMF確立後のSeries AでSalesエンジニアリング投資

**MVVへの反映**:
- **Mission**: カスタマーペインから逆算（例: 決済処理により開発者の時間を80%削減）
- **Vision**: PMFテストで検証された定量目標（例: 月間トランザクション$X達成）
- **Values**: 初期顧客との共創から抽出（例: 開発者ファースト、シンプリシティ重視）

### Reference

- 成功事例: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/` `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/`
- VC投資基準: a16z, Sequoia、Y Combinatorの投資基準
- SaaS Metrics: Bessemer Venture Partners "State of Cloud"レポート

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-50分

### 自動実行ステップ

1. **ビジネスアイデア・リーンキャンバス読み込み**
2. **成功スタートアップのMVV調査**（Stripe、Figma、Airbnb等）
3. **Mission草案作成**（1-2文、カスタマーペイン起点、市場ターニング意識）
4. **Vision草案作成**（3-5年後のマーケット状態、定量目標+VC資金調達ステージ）
5. **Values草案作成**（3-5個の実装指針、PMFテスト優先度反映）
6. **VC投資基準適合性チェック**（5項目、必須3項目全てクリア必須）（ForStartup必須）
7. **グローバル展開パイプライン評価**（地域別TAM、規制、資本効率）（ForStartup追加）
8. **ユニットエコノミクス検証**（LTV/CAC、CAC回収期間）（ForStartup強化）
9. **Lean Canvas整合性検証**（Problem/UVP/Solution整合）
10. **成果物出力**

### 判定基準（7項目チェック、ForStartup調整版）

| 項目 | 合格条件 |
|------|----------|
| Mission明確性 | 30秒で読め、市場ターニングとの関連が明確 |
| Vision具体性 | イメージ可能、定量目標と資金調達ステージ明記 |
| Values実用性 | 3-5個、PMFテスト時の優先施策につながる |
| MVV整合性 | Mission→Vision→Values整合（3/3） |
| Lean Canvas整合 | Problem/UVP/Solution整合（3/3） |
| **VC投資基準適合** | **TAM、10倍優位性、ユニットエコノミクス合格** |
| **グローバル展開可能性** | **スケーラビリティあり、規制リスク対応済み** |

**総合判定**:
- 7/7: ✅ MVV完了 → Series投資準備へ
- 5-6/7: ⚠️ 要改善 → 不合格項目をリプラン
- 0-4/7: ❌ 再定義 → ビジネスアイデア検証やり直し

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **WebSearch失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#1-外部api失敗websearchwebfetch等
- **データ検証失敗**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件

---

## Knowledge Base参照

- MVV概念: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#mvv-overview`
- リーンキャンバス: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#lean-canvas-overview`
- **Founder Research**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/`

---

## 成果物フォーマット

```markdown
# MVV（Mission/Vision/Values）（VC投資向けEdition）

**作成日**: [YYYY-MM-DD]
**プロジェクト**: [プロジェクト名]
**総合判定**: ✅ Series投資準備完了 / ⚠️ 要改善 / ❌ 再検証必須

---

## Mission（存在意義）

> [1-2文、30秒で読める、社会的意義が明確]

**社会課題**: [何の社会課題を解決するか]
**提供価値**: [誰にどんな価値を提供するか]

---

## Vision（目指す未来）

> [3-5年後の理想状態、イメージ可能、測定可能要素あり]

**定量目標**:
- [目標1]: [定量指標]
- [目標2]: [定量指標]
- [目標3]: [定量指標]

**理想状態**:
[3-5年後にどんな世界になっているか、顧客・社会の変化]

---

## Values（行動指針）

### Value 1: [価値観名]

**定義**: [PMFテスト時の優先施策に直結する定義]
**実装例**: [MVP開発での実践例]
**VC投資家との整合**: [どのVC評価基準と整合するか]

[繰り返し、3-5個...]

---

## VC投資基準適合性チェック

| 基準 | ウェイト | 達成度 | 根拠 |
|------|:-------:|:------:|------|
| スケーラビリティ（TAM） | 30% | ✅/⚠️/❌ | [TAM $1B+根拠] |
| 10倍優位性 | 25% | ✅/⚠️/❌ | [3軸の優位性根拠] |
| ユニットエコノミクス | 20% | ✅/⚠️/❌ | [LTV/CAC≥5.0根拠] |
| 市場ターニング | 15% | ✅/⚠️/❌ | [成長率>30%根拠] |
| チーム実行力 | 10% | ✅/⚠️/❌ | [過去成功事例] |

**総合スコア**: [X/100点]（70点以上でVC投資候補）

---

## グローバル展開パイプライン

| 地域 | Series | TAM | CAC見通し | 規制リスク |
|------|:------:|:---:|:-------:|:-------:|
| 北米 | Seed | [金額] | [見通し] | [リスク] |
| APAC | Series A | [金額] | [見通し] | [リスク] |
| EU | Series B | [金額] | [見通し] | [リスク] |

**規制対応計画**:
- [対応1]: [具体的な対応内容]
- [対応2]: [タイムラインと必要予算]

---

## MVV整合性検証

### Mission → Vision整合性

**整合度**: ✅ 整合 / ⚠️ やや曖昧 / ❌ 不整合

**検証内容**:
[MissionがVisionの実現につながるか]

### Vision → Values整合性

**整合度**: ✅ 整合 / ⚠️ やや曖昧 / ❌ 不整合

**検証内容**:
[ValuesがVision達成の行動指針になっているか]

### Mission → Values整合性

**整合度**: ✅ 整合 / ⚠️ やや曖昧 / ❌ 不整合

**検証内容**:
[ValuesがMission実現の行動指針になっているか]

---

## Lean Canvas整合性検証

### Problem整合性

**整合度**: ✅ 整合 / ⚠️ やや曖昧 / ❌ 不整合

**検証内容**:
[MissionがProblemの解決につながるか]

### UVP整合性

**整合度**: ✅ 整合 / ⚠️ やや曖昧 / ❌ 不整合

**検証内容**:
[VisionがUVPの理想状態を描いているか]

### Solution整合性

**整合度**: ✅ 整合 / ⚠️ やや曖昧 / ❌ 不整合

**検証内容**:
[ValuesがSolution実現の行動指針になっているか]

---

## VC投資対象の実績パターン

**成功事例**:
- Stripe: 支払い処理自動化、開発者ファースト、Paypal Moment明確、TAM $25B
- Figma: デザイン協調編集、リアルタイムコラボ、3軸優位性、2時間で$20M Series C達成
- Airbnb: ホテルの民泊化、ネットワーク効果、規制対応体制、IPOで10倍リターン

**失敗事例**:
- WeWork: スケーラビリティなし（マージン悪化）、単なるアービトラージ、VC基準未達
- Theranos: 技術実装なし、Missionと実装のギャップ、詐欺的表示で訴追
- Quibi: PMF検証なし、大型資金でスケール、市場ニーズ読み誤り

---

## Next Actions

1. [アクション1]
2. [アクション2]
3. [アクション3]
```

---

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


---

## 更新履歴

- 2026-01-02: ForStartup特化版として作成、成功スタートアップケース統合
- 2026-01-03: VC投資基準中心への改定、Recruit固有参照を削除、グローバル展開戦略強化

---

**テンプレートバージョン**: v3.1-ForStartup-VC Focused
**最終更新**: 2026-01-03
**作成者**: Claude Code
**ForStartup強化要素**: VC投資基準適合性（5項目）、グローバル展開パイプライン、ユニットエコノミクス検証、PMF前提MVV設計
