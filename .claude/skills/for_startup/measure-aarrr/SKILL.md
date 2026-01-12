---
name: measure-aarrr-forstartup
description: |
  AARRR（Acquisition/Activation/Retention/Referral/Revenue）フレームワークでVC投資基準の成長ファネルを測定。月次成長率20%、年次3倍の厳格な目標設定、DAU/MAU・NRR・LTV/CAC等のVC判断指標を統合し、成長を阻害するボトルネックを定量分析します。

  使用タイミング：
  - PMF達成後、Series A資金調達準備時
  - 月次/週次の成長レビュー（投資家レポート向け）
  - Phase3（スケール）実行時
  - VC対応Q&A準備時

  所要時間：40-60分（初回設定含む、厳格な検証のため通常版より+10分）
  出力：AARRR分析レポート、VC投資判断用KPIダッシュボード、改善施策優先順位リスト

trigger_keywords:
  - "AARRR"
  - "パイレーツメトリクス"
  - "成長ファネル"
  - "ファネル分析"
  - "グロースハック"
  - "VC KPI"
  - "成長率測定"
stage: executing
dependencies:
  - validate-pmf（PMF達成が前提）
  - validate-unit-economics-strict（ユニットエコノミクス厳格検証完了推奨）
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/aarrr_analysis_forstartup.md
execution_time: 40-60分
framework_reference:
  - Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
  - aipm_v0/.claude/skills/for_startup/_analysis/research_knowledge.md
priority: P1
framework_compliance: 100%
vc_readiness: true
---

# Measure AARRR Skill (ForStartup Edition)

AARRR（Pirate Metrics）5段階ファネルを**VC投資基準**で測定し、成長ボトルネックを特定する自律実行型Skill。

**ForStartup専用の拡張機能**:
- 月次成長率20%、年次3倍を基準とした目標設定
- DAU/MAU、NRR、LTV/CAC等のVC投資判断指標を追加
- Airbnb、Freshworks等の成功事例からAARRRファネル最適化パターンを統合
- 成長を阻害する定量的ボトルネック分析

---

## このSkillでできること

1. **VC投資基準での5段階ファネル測定**: Acquisition → Activation → Retention → Referral → Revenue の転換率をVC投資水準で自動計測
2. **成長率厳格検証**: 月次成長率20%以上、年次3倍以上の達成状況を自動判定
3. **VC判断指標の統合分析**: DAU/MAU、NRR（Net Revenue Retention）、LTV/CAC、Payback期間を一元測定
4. **ボトルネック定量分析**: 各段階の転換率を業界ベンチマーク＋VC基準と比較し、成長阻害要因を特定
5. **業界ベンチマーク取得**: WebSearchで最新の業界標準値を取得（SaaS、Marketplace、E-commerce等）
6. **改善施策の投資対効果評価**: インパクトと実装難易度でQuick Winsを特定し、ROI見積もりを提供
7. **投資家向けKPIダッシュボード作成**: VCミーティングで提示可能なKPI可視化レポートを生成
8. **成功事例ベースの最適化提案**: Airbnb、Freshworks等のAARRRファネル最適化パターンを参照し、具体的な施策を推薦

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `pmf_judgment.md`, アナリティクスデータ, 売上データ, 成長率データ（月次/年次） |
| **出力** | `Flow/{YYYYMM}/{YYYY-MM-DD}/aarrr_analysis_forstartup.md`, VC投資判断用KPIダッシュボード |
| **次のSkill** | `/build-pitch-deck`, `/prepare-vc-meeting`, 個別改善施策の実行 |

---

## Instructions

**実行モード**: 自律実行（ユーザー介入不要）
**推定所要時間**: 40-60分

### 自動実行ステップ

#### STEP 1: PMF判定確認

- PMF判定レポート（`pmf_judgment.md`）を読み込み
- PMF達成判定が「✅ PMF達成」であることを確認
- **ForStartup基準**: NPS 50+、Retention 80%+ の厳格な基準を満たしているか確認
- 未達成の場合は警告を表示し、処理を中断（Series A調達にはPMF達成が必須）

#### STEP 2: AARRR 5段階の定義（VC投資基準版）

AARRRフレームワークの5段階を**VC投資判断で重視される指標**とともに明確化:

| 段階 | 定義 | 主要KPI | VC重視指標 |
|-----|------|---------|----------|
| **Acquisition（獲得）** | 訪問者がサイトに到達 | 訪問者数、流入チャネル別内訳 | CAC（顧客獲得コスト）、CAC Payback期間 |
| **Activation（活性化）** | 初回体験で価値を実感（Aha Moment） | サインアップ率、Aha Moment達成率 | Aha Moment到達時間、オンボーディング完了率 |
| **Retention（継続）** | 継続的に利用 | DAU/MAU、D1/D7/D30継続率、Churn Rate | **DAU/MAU比率**、**NRR（Net Revenue Retention）**、Cohort分析 |
| **Referral（紹介）** | 他の人に紹介 | バイラル係数（K-factor）、紹介率、NPS | **Viral Coefficient > 1.0**、Organic成長率 |
| **Revenue（収益）** | 収益を生む | ARPU、課金転換率、LTV | **LTV/CAC比率 > 5.0**、**Payback期間 < 12ヶ月**、GrossMargin > 70% |

#### STEP 3: 業界ベンチマーク取得

WebSearchで最新の業界ベンチマークを取得（**VC投資基準を優先**）:

```
検索クエリ例:
- "AARRR metrics benchmarks 2026 SaaS VC"
- "SaaS activation rate Series A 2026"
- "B2B retention rate VC benchmark 2026"
- "viral coefficient average 2026"
- "SaaS LTV/CAC ratio Series A 2026"
- "DAU/MAU ratio benchmark SaaS 2026"
- "Net Revenue Retention 120% 2026"
```

**デフォルトベンチマーク（VC投資基準、SaaS業界）**:

| 段階 | KPI | VC投資基準 | 一般基準 | 備考 |
|-----|-----|----------|---------|------|
| Acquisition | 訪問者数 | 月次成長率 **20%以上** | 15%以上 | 絶対値よりも成長率が重要 |
| Acquisition | CAC | $100-500（B2B SaaS） | - | 業界・プラン依存 |
| Activation | サインアップ率 | **3-5%** | 2-5% | 訪問者からのサインアップ |
| Activation | Aha Moment達成率 | **50%+** | 40%+ | オンボーディング完了率 |
| Retention | **DAU/MAU比率** | **30-50%** | 20%+ | VC最重視指標（エンゲージメント） |
| Retention | 月次継続率 | **90-95%** | 85-95% | (MAU - Churn) / MAU |
| Retention | **NRR（Net Revenue Retention）** | **120%+** | 110%+ | 既存顧客の売上成長率 |
| Retention | Churn Rate | **<3%/月（B2B）** | <5%/月（B2B） | 解約率 |
| Referral | バイラル係数 | **>1.0（理想）** | >0.5 | K-factor |
| Referral | 紹介率 | **15-30%** | 10-30% | 紹介ユーザー / 総ユーザー |
| Referral | NPS | **50+** | 40+ | Promoters% - Detractors% |
| Revenue | 有料転換率 | **3-5%** | 2-5% | 無料→有料 |
| Revenue | **LTV/CAC比率** | **> 5.0** | > 3.0 | VC投資判断の最重要指標 |
| Revenue | **Payback期間** | **< 12ヶ月** | < 18ヶ月 | CAC回収期間 |
| Revenue | GrossMargin | **> 70%（SaaS）** | > 60% | 粗利率 |

#### STEP 4: 実績データ入力ガイド（VC投資判断版）

ユーザーに以下のデータ入力を依頼（対話形式）:

**Acquisition（獲得）**:
- 月間訪問者数（Unique Visitors）: XXX人
- 前月比成長率: +XX%（**目標: 20%以上**）
- 年次成長率: +XX%（**目標: 3倍（200%）以上**）
- 主要流入チャネル（例: SEO XX%, SNS XX%, 広告 XX%）
- CAC（顧客獲得コスト）: $XXX/顧客

**Activation（活性化）**:
- サインアップ数: XXX人
- サインアップ率: XX%（= サインアップ数 / 訪問者数）（**目標: 3-5%**）
- Aha Moment達成数（オンボーディング完了者）: XXX人
- Aha Moment達成率: XX%（= Aha Moment達成数 / サインアップ数）（**目標: 50%+**）
- Aha Moment到達時間（中央値）: XX分（**目標: < 5分**）

**Retention（継続）**:
- MAU（月間アクティブユーザー）: XXX人
- DAU（日次アクティブユーザー）: XXX人
- **DAU/MAU比率: XX%**（**目標: 30-50%**、**VCが最重視**）
- D1継続率: XX%（翌日も利用）
- D7継続率: XX%（7日後も利用）
- D30継続率: XX%（30日後も利用）
- 月次継続率: XX%（**目標: 90-95%**）
- Churn Rate: XX%/月（= 月次解約数 / 月初ユーザー数）（**目標: <3%/月**）
- **NRR（Net Revenue Retention）: XXX%**（**目標: 120%+**、**VCが最重視**）
  - 計算式: (前月MRR + アップセル - ダウングレード - 解約) / 前月MRR × 100%

**Referral（紹介）**:
- 紹介経由の新規ユーザー数: XXX人
- 紹介率: XX%（= 紹介ユーザー / 総ユーザー）（**目標: 15-30%**）
- バイラル係数（K-factor）: X.XX（= 1ユーザーが紹介する平均人数 × 紹介された人の登録率）（**目標: >1.0**）
- NPS: XX点（Promoters% - Detractors%）（**目標: 50+**）
- Organic成長率（紹介のみによる成長）: XX%/月

**Revenue（収益）**:
- 有料ユーザー数: XXX人
- 課金転換率: XX%（= 有料ユーザー / 総ユーザー）（**目標: 3-5%**）
- ARPU（月間平均顧客単価）: ¥XXX
- MRR（月次経常収益）: ¥XXX,XXX
- **LTV（顧客生涯価値）: ¥XXX,XXX**
- **LTV/CAC比率: X.XX**（**目標: > 5.0**、**VC投資判断最重要**）
- **Payback期間: XX ヶ月**（**目標: < 12ヶ月**）
- GrossMargin: XX%（**目標: > 70% for SaaS**）

**データソース例**:
- Google Analytics 4（訪問者、サインアップ）
- Mixpanel / Amplitude（ユーザー行動、継続率、DAU/MAU）
- 決済システム（Stripe, Paddle等）（収益、LTV、NRR）
- アンケートツール（NPS）
- Cohort分析ツール（Retention分析）

#### STEP 5: ファネル分析（VC投資判断版）

各段階の転換率を計算し、**VC投資基準との差分を可視化**:

```
総訪問者: A人（月次成長率: +XX%、目標: +20%）
  ↓ サインアップ率: B%（目標: 3-5%）
サインアップ: B人
  ↓ Aha Moment達成率: C%（目標: 50%+）
活性化ユーザー: C人
  ↓ 継続率（D30）: D%（目標: 90-95%）
継続ユーザー: D人
  ↓ 課金転換率: E%（目標: 3-5%）
有料ユーザー: E人
  ↓ ARPU: ¥F
MRR: ¥G（月次成長率: +XX%、目標: +20%）
```

**総合転換率**:
```
訪問者 → 収益転換率 = (E / A) × 100%
```

**VC重視指標の達成状況**:
| 指標 | 実績値 | VC基準 | 達成状況 |
|------|-------|--------|---------|
| 月次成長率（訪問者） | XX% | 20%+ | ✅/❌ |
| 月次成長率（MRR） | XX% | 20%+ | ✅/❌ |
| 年次成長率（MRR） | XX% | 200%+（3倍） | ✅/❌ |
| DAU/MAU比率 | XX% | 30-50% | ✅/❌ |
| NRR | XXX% | 120%+ | ✅/❌ |
| LTV/CAC比率 | X.XX | > 5.0 | ✅/❌ |
| Payback期間 | XX ヶ月 | < 12ヶ月 | ✅/❌ |

#### STEP 6: ボトルネック自動検出（VC投資判断版）

各段階をVC投資基準と比較し、**成長阻害要因を定量的に特定**:

**判定基準（VC投資水準）**:
- ✅ **良好**: VC基準以上（投資判断クリア）
- ⚠️ **ボトルネック**: VC基準 - 10%以内（改善推奨）
- ❌ **重大ボトルネック**: VC基準 - 10%未満（投資判断に深刻な影響）

**ボトルネック特定ロジック**:
1. 各段階の実績値をVC基準と比較
2. VC基準からの差分が最も大きい段階を「最優先ボトルネック」として特定
3. 差分の大きい順にランク付け
4. **成長率指標（月次20%、年次3倍）を最優先で判定**
   - 成長率が基準未達の場合、他のKPIが良好でも「重大ボトルネック」と判定

**VC投資判断への影響評価**:
- **Series A調達への影響**: 重大ボトルネックが1つでもあれば調達成功率が大幅低下
- **評価額への影響**: ボトルネック数と評価額の逆相関を定量化（例: ボトルネック1つで評価額-20%）

#### STEP 7: ボトルネック優先順位付け（VC投資判断版）

**評価軸**:
1. **Impact（影響度）**: 改善時の**成長率・VC評価額**への影響（1-10点）
   - 成長率改善（月次20%達成）: 10点
   - NRR改善（120%達成）: 9点
   - LTV/CAC改善（5.0達成）: 9点
   - DAU/MAU改善（30%達成）: 8点
   - ファネル上流改善（Acquisition）: 7点
   - 計算式: `Impact = (VC重視度 + 後続ステップ数) × 転換率差分% × 成長率への寄与度`

2. **Ease（実装容易性）**: 改善施策の実装難易度（1-10点）
   - 簡単: UI改善、コピー変更、A/Bテスト（8-10点）
   - 中程度: 機能追加、フロー変更、マーケティング施策（4-7点）
   - 困難: プロダクト再設計、技術的難題、組織変更（1-3点）

3. **VC Appeal（VC説得力）**: 改善施策がVC評価に与える影響（1-10点）
   - 高: 成長率20%達成、NRR 120%達成、LTV/CAC 5.0達成（8-10点）
   - 中: DAU/MAU改善、Churn率低減（5-7点）
   - 低: UI改善のみ（1-4点）

**優先スコア（VC投資判断版）**:
```
Priority Score = (Impact × Ease × VC Appeal) / 100
```

高スコア順に改善施策を並べ、**Quick Wins（VC Appeal高 × 実装容易）**を最優先。

#### STEP 8: 改善施策提案（成功事例ベース）

各ボトルネック段階ごとに、**Airbnb、Freshworks等の成功事例**を参照し、3-5個の改善施策を提案:

**Acquisition改善施策例（成功事例ベース）**:
- **Airbnb型**: "Do things that don't scale" - 創業者自らのユーザー獲得（例: NY直接訪問、写真撮影サービス）
- **Freshworks型**: 競合の価格改定タイミングを狙ったゲリラマーケティング
- **SEO最適化**: キーワードリサーチ、コンテンツSEO、バックリンク戦略
- **SNS広告最適化**: A/Bテスト、ターゲティング改善、リターゲティング
- **コンテンツマーケティング**: ブログ、YouTube、Podcast
- **リファラルプログラム強化**: 紹介者インセンティブ設計
- **パートナーシップ拡大**: 戦略的提携、OEMチャネル

**Activation改善施策例（成功事例ベース）**:
- **Airbnb型**: Aha Moment（初回予約成功）への最短経路設計
- **Box型**: フリーミアムモデルでの即時利用開始（IT部門を通さない）
- **オンボーディングフロー改善**: ステップ削減、進捗表示、ツールチップ
- **パーソナライズドオンボーディング**: ユーザーセグメント別フロー
- **初回体験デモ・チュートリアル強化**: インタラクティブチュートリアル
- **空白状態（Empty State）の改善**: サンプルデータ、テンプレート提供

**Retention改善施策例（成功事例ベース）**:
- **Airbnb型**: 写真品質改善で予約2-3倍増（定量的な改善実証）
- **Freshworks型**: SMB特化による使いやすさ（複雑さの排除）
- **NRR 120%達成施策**: アップセル・クロスセル戦略、利用量ベース課金
- **DAU/MAU 30%達成施策**: デイリー利用習慣の形成、リマインダー最適化
- **リマインダー・プッシュ通知の最適化**: パーソナライズ、頻度調整
- **習慣形成フック**: 毎日使う理由づくり（Streaks、Daily Goals）
- **エンゲージメントメール**: 週次サマリー、成果レポート、ベストプラクティス
- **新機能の継続的リリース**: 月次リリースサイクル
- **コミュニティ構築**: Slack、Discord、ユーザー会

**Referral改善施策例（成功事例ベース）**:
- **Airbnb型**: ネットワーク効果の最大化（ホスト⇔ゲストの相互成長）
- **リファラルプログラム導入**: 紹介者・被紹介者双方にインセンティブ（$10-50クレジット等）
- **ソーシャルシェア機能の追加**: ワンクリックシェア、成果可視化
- **NPS調査とPromotersへの紹介依頼**: NPS 50+達成後のタイミング
- **成功事例の可視化**: シェア可能なレポート、実績バッジ
- **バイラルループの設計**: 使うほど広がる仕組み（例: チーム招待必須）

**Revenue改善施策例（成功事例ベース）**:
- **LTV/CAC 5.0達成施策**: CAC削減（Organic成長）、LTV向上（Retention強化、アップセル）
- **Payback期間 < 12ヶ月達成施策**: 年間契約割引、前払い割引
- **価格戦略の見直し**: プラン構成、価格帯、バリューベース価格設定
- **アップセル・クロスセル機能**: 利用量ベース課金、追加機能課金
- **無料トライアル期間の最適化**: 14日 vs 30日のA/Bテスト
- **プレミアム機能の追加**: エンタープライズ向け機能（SSO、API等）
- **年間契約割引の導入**: 20-30%割引でPayback期間短縮

#### STEP 9: Quick Wins特定（VC Appeal優先）

**Quick Wins条件（VC投資判断版）**:
- Impact ≥ 7点
- Ease ≥ 7点
- VC Appeal ≥ 7点
- Priority Score ≥ 343点（7×7×7）

**VC Appeal重視のQuick Wins**:
- 成長率20%達成に直結する施策を最優先
- NRR 120%達成施策を次優先
- LTV/CAC 5.0達成施策を第三優先

Quick Winsを最優先実装リストとして表示し、**VCミーティング前に実装すべき施策**として明示。

#### STEP 10: 実装ロードマップ作成（VC調達タイムライン連動）

**1ヶ月計画（短期）** - VCミーティング前の準備:
- Week 1: Quick Wins施策1（成長率20%達成最優先）
- Week 2: Quick Wins施策2（NRR 120%達成）
- Week 3: ボトルネック1の改善施策（LTV/CAC 5.0達成）
- Week 4: 効果測定・分析、VCミーティング用KPIダッシュボード準備

**3ヶ月計画（中期）** - Series A調達準備:
- Month 1: Quick Wins実行 + 成長率20%達成実証
- Month 2: NRR 120%達成 + LTV/CAC 5.0達成 + A/Bテスト
- Month 3: DAU/MAU 30%達成 + 総合評価 + Series Aピッチデッキ作成

**6ヶ月計画（長期）** - Series A調達完了:
- Month 1-3: 上記3ヶ月計画実行
- Month 4: Series Aピッチング開始
- Month 5: デューデリジェンス対応
- Month 6: Series A調達完了、次のスケール施策実行

#### STEP 11: 成果物出力（VC投資判断版）

以下のMarkdown形式でレポートを生成:

---

## 成果物テンプレート（VC投資判断版）

```markdown
# AARRR分析レポート（ForStartup Edition）

**作成日**: {YYYY-MM-DD}
**分析対象期間**: {YYYY-MM-DD} ~ {YYYY-MM-DD}
**総合判定**: ✅ VC調達推奨レベル / ⚠️ 改善必要 / ❌ 調達見送り推奨

---

## エグゼクティブサマリー

### ファネルサマリー

| 指標 | 値 |
|-----|------|
| 総訪問者数 | XXX,XXX人 |
| サインアップ数 | XX,XXX人 |
| 活性化ユーザー数 | X,XXX人 |
| 継続ユーザー数（D30） | X,XXX人 |
| 有料ユーザー数 | XXX人 |
| MRR | ¥XXX,XXX |
| **総合転換率（訪問→収益）** | **XX%** |

### VC投資判断指標

| 指標 | 実績値 | VC基準 | 達成状況 | 投資判断への影響 |
|------|-------|--------|---------|---------------|
| **月次成長率（MRR）** | XX% | **20%+** | ✅/❌ | 最重要（未達成で調達困難） |
| **年次成長率（MRR）** | XX% | **200%+（3倍）** | ✅/❌ | 重要（未達成で評価額低下） |
| **DAU/MAU比率** | XX% | **30-50%** | ✅/❌ | 重要（エンゲージメント指標） |
| **NRR** | XXX% | **120%+** | ✅/❌ | 重要（既存顧客成長力） |
| **LTV/CAC比率** | X.XX | **> 5.0** | ✅/❌ | 最重要（経済性指標） |
| **Payback期間** | XX ヶ月 | **< 12ヶ月** | ✅/❌ | 重要（資本効率） |
| GrossMargin | XX% | > 70% (SaaS) | ✅/❌ | 重要（収益性） |

### VC調達可能性評価

**総合スコア**: XX/100点

| スコア範囲 | 判定 | 調達可能性 |
|-----------|------|-----------|
| **80-100点** | ✅ Series A調達推奨 | 高（評価額も高水準） |
| **60-79点** | ⚠️ 改善後に調達検討 | 中（ボトルネック改善必須） |
| **0-59点** | ❌ 調達見送り推奨 | 低（PMF再検証推奨） |

**現在の判定**: {判定内容}

### 最優先ボトルネック（成長阻害要因）

**🚨 {ステージ名}**: {理由}

- 実績値: XX%
- VC基準: XX%
- 差分: -XX%
- **成長率への影響**: MRR成長率 -XX%/月（改善で +XX%/月見込み）
- **評価額への影響**: 現状評価額から -XX%（改善で +XX%見込み）
- 優先度: 🔴 最高

---

## 5段階詳細分析（VC投資判断版）

### 1. Acquisition（獲得）

**KPI**:
- 月間訪問者数: XXX,XXX人
- 前月比成長率: +XX%（**VC基準: 20%+**）
- 年次成長率: +XX%（**VC基準: 200%+**）
- CAC（顧客獲得コスト）: $XXX

**流入チャネル内訳**:
| チャネル | 訪問者数 | 割合 | CAC | 備考 |
|---------|---------|------|-----|------|
| SEO（自然検索） | XX,XXX | XX% | $XX | Organic、CAC低 |
| SNS（ソーシャル） | XX,XXX | XX% | $XX | Build in Public等 |
| 広告（有料） | XX,XXX | XX% | $XXX | Paid、CAC高 |
| ダイレクト | XX,XXX | XX% | $0 | ブランド力 |
| リファラル（紹介） | XX,XXX | XX% | $0 | バイラル効果 |

**VC基準との比較**:
| KPI | 実績値 | VC基準 | 差分 | 判定 |
|-----|-------|--------|------|:----:|
| 月次成長率 | XX% | 20%+ | +/-XX% | ✅/⚠️/❌ |
| 年次成長率 | XX% | 200%+ | +/-XX% | ✅/⚠️/❌ |

**判定**: ✅ 良好 / ⚠️ 改善必要 / ❌ 重大ボトルネック

**コメント**:
[成長率のトレンド、主要チャネルの状況、VC投資判断への影響]

**成功事例ベースの改善提案**:
- **Airbnb型施策**: {具体的な施策}
- **Freshworks型施策**: {具体的な施策}

---

### 2. Activation（活性化）

**KPI**:
- サインアップ率: XX%（訪問者からのサインアップ）
- Aha Moment達成率: XX%（サインアップからの活性化）
- Aha Moment到達時間（中央値）: XX分

**VC基準との比較**:
| KPI | 実績値 | VC基準 | 差分 | 判定 |
|-----|-------|--------|------|:----:|
| サインアップ率 | XX% | 3-5% | +/-XX% | ✅/⚠️/❌ |
| Aha Moment達成率 | XX% | 50%+ | +/-XX% | ✅/⚠️/❌ |
| Aha Moment到達時間 | XX分 | < 5分 | +/-XX分 | ✅/⚠️/❌ |

**判定**: ✅ 良好 / ⚠️ ボトルネック / ❌ 重大ボトルネック

**コメント**:
[オンボーディングの状況、離脱ポイント、VC投資判断への影響]

**成功事例ベースの改善提案**:
- **Airbnb型施策**: {具体的な施策}
- **Box型施策**: {具体的な施策}

---

### 3. Retention（継続）

**KPI**:
- **DAU/MAU比率: XX%**（**VC基準: 30-50%**、**VCが最重視**）
- D1継続率: XX%
- D7継続率: XX%
- D30継続率: XX%
- 月次継続率: XX%
- Churn Rate: XX%/月
- **NRR（Net Revenue Retention）: XXX%**（**VC基準: 120%+**、**VCが最重視**）

**VC基準との比較**:
| KPI | 実績値 | VC基準 | 差分 | 判定 |
|-----|-------|--------|------|:----:|
| **DAU/MAU比率** | XX% | **30-50%** | +/-XX% | ✅/⚠️/❌ |
| 月次継続率 | XX% | 90-95% | +/-XX% | ✅/⚠️/❌ |
| Churn Rate | XX%/月 | <3%/月（B2B） | +/-XX% | ✅/⚠️/❌ |
| **NRR** | XXX% | **120%+** | +/-XX% | ✅/⚠️/❌ |

**判定**: ✅ 良好 / ⚠️ ボトルネック / ❌ 重大ボトルネック

**コメント**:
[継続率のトレンド、解約理由、NRR分析、VC投資判断への影響]

**NRR分析詳細**:
- 前月MRR: ¥XXX,XXX
- 既存顧客アップセル: +¥XX,XXX
- 既存顧客ダウングレード: -¥XX,XXX
- 既存顧客解約: -¥XX,XXX
- 当月既存顧客MRR: ¥XXX,XXX
- **NRR: XXX%**（計算式: 当月既存顧客MRR / 前月MRR × 100%）

**成功事例ベースの改善提案**:
- **Airbnb型施策**: {具体的な施策}
- **Freshworks型施策**: {具体的な施策}

---

### 4. Referral（紹介）

**KPI**:
- 紹介率: XX%（紹介ユーザー / 総ユーザー）
- バイラル係数（K-factor）: X.XX
- NPS: XX点
- Organic成長率（紹介のみによる成長）: XX%/月

**VC基準との比較**:
| KPI | 実績値 | VC基準 | 差分 | 判定 |
|-----|-------|--------|------|:----:|
| 紹介率 | XX% | 15-30% | +/-XX% | ✅/⚠️/❌ |
| バイラル係数 | X.XX | >1.0（理想） | +/-X.XX | ✅/⚠️/❌ |
| NPS | XX | 50+ | +/-XX | ✅/⚠️/❌ |

**判定**: ✅ 良好 / ⚠️ ボトルネック / ❌ 重大ボトルネック

**コメント**:
[紹介の仕組み、NPS結果の解釈、バイラル成長の可能性、VC投資判断への影響]

**成功事例ベースの改善提案**:
- **Airbnb型施策**: {具体的な施策}

---

### 5. Revenue（収益）

**KPI**:
- 課金転換率: XX%（無料→有料）
- ARPU: ¥XXX
- MRR: ¥XXX,XXX
- 月次成長率（MRR）: +XX%（**VC基準: 20%+**）
- 年次成長率（MRR）: +XX%（**VC基準: 200%+**）
- **LTV: ¥XXX,XXX**
- **LTV/CAC比率: X.XX**（**VC基準: > 5.0**）
- **Payback期間: XX ヶ月**（**VC基準: < 12ヶ月**）
- GrossMargin: XX%（**VC基準: > 70% for SaaS**）

**VC基準との比較**:
| KPI | 実績値 | VC基準 | 差分 | 判定 |
|-----|-------|--------|------|:----:|
| 課金転換率 | XX% | 3-5% | +/-XX% | ✅/⚠️/❌ |
| **LTV/CAC比率** | X.XX | **> 5.0** | +/-X.XX | ✅/⚠️/❌ |
| **Payback期間** | XX ヶ月 | **< 12ヶ月** | +/-XX | ✅/⚠️/❌ |
| GrossMargin | XX% | > 70% (SaaS) | +/-XX% | ✅/⚠️/❌ |
| **月次成長率（MRR）** | XX% | **20%+** | +/-XX% | ✅/⚠️/❌ |
| **年次成長率（MRR）** | XX% | **200%+** | +/-XX% | ✅/⚠️/❌ |

**判定**: ✅ 良好 / ⚠️ ボトルネック / ❌ 重大ボトルネック

**コメント**:
[収益化の状況、プラン構成、成長率トレンド、VC投資判断への影響]

**成功事例ベースの改善提案**:
- **LTV/CAC 5.0達成施策**: {具体的な施策}
- **Payback期間 < 12ヶ月達成施策**: {具体的な施策}

---

## ボトルネック特定（VC投資判断版）

### 優先順位付け

| ランク | ステージ | 問題点 | Impact | Ease | VC Appeal | Priority Score | 判定 |
|:-----:|---------|--------|:------:|:----:|:---------:|:--------------:|:----:|
| 1 | {ステージ} | {問題点} | XX | XX | XX | XXX | 🔴 最高 |
| 2 | {ステージ} | {問題点} | XX | XX | XX | XXX | 🟠 高 |
| 3 | {ステージ} | {問題点} | XX | XX | XX | XXX | 🟡 中 |

**成長率への影響分析**:
- ボトルネック1改善による月次成長率改善見込み: +XX%
- ボトルネック2改善による月次成長率改善見込み: +XX%
- **総合改善による月次成長率見込み**: 現状XX% → 改善後XX%（**VC基準20%達成可否: ✅/❌**）

**評価額への影響分析**:
- ボトルネック1改善による評価額改善見込み: +XX%
- ボトルネック2改善による評価額改善見込み: +XX%
- **総合改善による評価額見込み**: 現状¥XXB → 改善後¥XXB

---

## 改善施策（優先順位順、成功事例ベース）

### Quick Wins（即実行推奨、VCミーティング前必須）

1. **{施策名}** - {ステージ}（**成功事例: Airbnb/Freshworks等**）
   - **期待効果**: {転換率XX% → XX%、MRR +¥XXX,XXX、月次成長率 +XX%}
   - **VC投資判断への影響**: {評価額 +XX%、調達成功率 +XX%}
   - **実装難易度**: 低（X週間）
   - **Impact**: XX/10
   - **Ease**: XX/10
   - **VC Appeal**: XX/10
   - **Priority Score**: XXX
   - **具体的アクション**: {実装内容}
   - **成功事例**: {Airbnb/Freshworks等の具体的な事例}
   - **参照**: @research_knowledge.md p.XX-XX

2. **{施策名}** - {ステージ}
   - （同上）

### 中期施策（1-3ヶ月、Series A調達準備）

3. **{施策名}** - {ステージ}
   - **期待効果**: {内容}
   - **VC投資判断への影響**: {内容}
   - **実装難易度**: 中（XX週間）
   - **Impact**: XX/10
   - **Ease**: XX/10
   - **VC Appeal**: XX/10
   - **Priority Score**: XXX
   - **具体的アクション**: {実装内容}
   - **成功事例**: {具体的な事例}

### 長期施策（3ヶ月以上、Series A調達完了後）

5. **{施策名}** - {ステージ}
   - **期待効果**: {内容}
   - **VC投資判断への影響**: {内容}
   - **実装難易度**: 高（XX週間）
   - **Impact**: XX/10
   - **Ease**: XX/10
   - **VC Appeal**: XX/10
   - **Priority Score**: XXX
   - **具体的アクション**: {実装内容}

---

## 実装ロードマップ（VC調達タイムライン連動）

### 1ヶ月計画（短期、VCミーティング前の準備）

| Week | 施策 | ステージ | 目標 | VC投資判断への影響 |
|:----:|------|---------|------|-----------------|
| Week 1 | {Quick Wins施策1} | {ステージ} | {KPI目標} | 月次成長率 XX% → XX% |
| Week 2 | {Quick Wins施策2} | {ステージ} | {KPI目標} | NRR XXX% → XXX% |
| Week 3 | {ボトルネック1改善} | {ステージ} | {KPI目標} | LTV/CAC X.X → X.X |
| Week 4 | 効果測定・分析 | - | AARRRレポート更新、VCミーティング用KPIダッシュボード準備 | - |

### 3ヶ月計画（中期、Series A調達準備）

| Month | 主要施策 | 目標KPI | VC投資判断への影響 |
|:-----:|---------|---------|-----------------|
| Month 1 | Quick Wins実行 + 成長率20%達成実証 | {月次成長率 XX% → 20%+} | 調達成功率 +30% |
| Month 2 | NRR 120%達成 + LTV/CAC 5.0達成 + A/Bテスト | {NRR XXX% → 120%+, LTV/CAC X.X → 5.0+} | 評価額 +20% |
| Month 3 | DAU/MAU 30%達成 + 総合評価 + Series Aピッチデッキ作成 | {DAU/MAU XX% → 30%+} | Series A調達準備完了 |

### 6ヶ月計画（長期、Series A調達完了）

| Month | マイルストーン | 詳細 |
|:-----:|-------------|------|
| Month 1-3 | 上記3ヶ月計画実行 | AARRR最適化、VC基準達成 |
| Month 4 | Series Aピッチング開始 | 10-20社のVC面談、ピッチデッキ提示 |
| Month 5 | デューデリジェンス対応 | 財務・法務・技術DDへの対応 |
| Month 6 | Series A調達完了 | タームシート締結、資金受領、次のスケール施策実行 |

**3ヶ月後の目標ファネル（VC基準達成版）**:
```
訪問者: XXX,XXX人（現状比+XX%、月次成長率 20%+）
  ↓ サインアップ率: XX%（+XX%、VC基準 3-5%達成）
サインアップ: XX,XXX人
  ↓ Aha Moment達成率: XX%（+XX%、VC基準 50%+達成）
活性化: X,XXX人
  ↓ D30継続率: XX%（+XX%、VC基準 90-95%達成）
継続: X,XXX人（DAU/MAU 30%+達成、NRR 120%+達成）
  ↓ 課金転換率: XX%（+XX%、VC基準 3-5%達成）
有料: XXX人
  ↓ ARPU: ¥XXX（+¥XX）
MRR: ¥XXX,XXX（+XX%、年次3倍達成）
LTV/CAC: X.X（VC基準 5.0+達成）
Payback期間: XX ヶ月（VC基準 < 12ヶ月達成）
```

---

## VC投資判断用KPIダッシュボード

### 成長指標

| 指標 | 現状 | 1ヶ月後目標 | 3ヶ月後目標 | VC基準 |
|------|------|----------|----------|--------|
| 月次成長率（MRR） | XX% | XX% | **20%+** | 20%+ |
| 年次成長率（MRR） | XX% | XX% | **200%+** | 200%+ |
| DAU/MAU比率 | XX% | XX% | **30%+** | 30-50% |
| NRR | XXX% | XXX% | **120%+** | 120%+ |

### 経済性指標

| 指標 | 現状 | 1ヶ月後目標 | 3ヶ月後目標 | VC基準 |
|------|------|----------|----------|--------|
| LTV/CAC比率 | X.XX | X.XX | **> 5.0** | > 5.0 |
| Payback期間 | XX ヶ月 | XX ヶ月 | **< 12ヶ月** | < 12ヶ月 |
| GrossMargin | XX% | XX% | **> 70%** | > 70% |
| CAC | $XXX | $XXX | $XXX | 業界依存 |

### エンゲージメント指標

| 指標 | 現状 | 1ヶ月後目標 | 3ヶ月後目標 | VC基準 |
|------|------|----------|----------|--------|
| D1継続率 | XX% | XX% | XX% | 40%+ |
| D7継続率 | XX% | XX% | XX% | 25%+ |
| D30継続率 | XX% | XX% | **90%+** | 90-95% |
| Churn Rate | XX%/月 | XX%/月 | **< 3%/月** | < 3%/月 |

---

## 次のアクション（VCミーティング準備）

### 即時実行（Week 1）
1. **Quick Wins施策の実装開始**: {具体的な施策名}
2. **Week 1の目標設定**: {具体的な目標KPI}
3. **測定環境整備**: アナリティクスダッシュボード更新（DAU/MAU、NRR、LTV/CAC自動計測）
4. **チーム共有**: 本レポートを関係者に展開、週次レビュー会議設定

### VCミーティング準備（Week 2-4）
1. **KPIダッシュボードの完成**: VC提示用の可視化レポート作成
2. **ピッチデッキ更新**: AARRR改善結果を反映（`/build-pitch-deck`スキル使用）
3. **VC対応Q&A準備**: 成長率・ボトルネック改善に関する質問への回答準備（`/prepare-vc-meeting`スキル使用）
4. **Series A調達計画作成**: 資金調達ロードマップの更新（`/create-fundraising-plan`スキル使用）

### Series A調達準備（Month 2-3）
1. **VC基準達成の実証**: 月次成長率20%、NRR 120%、LTV/CAC 5.0の達成を定量的に示す
2. **デューデリジェンス準備**: 財務・法務・技術DDへの対応資料準備
3. **ターゲットVC選定**: 10-20社のVCリストアップ、warm intro確保
4. **ピッチング開始**: 1社目のVCミーティング実施

---

## 参考情報

### 業界ベンチマーク出典

- {WebSearchで取得したソースURL1}
- {WebSearchで取得したソースURL2}
- {WebSearchで取得したソースURL3}

### 成功事例ベースの参照元

- **Airbnb AARRR最適化事例**: @research_knowledge.md p.XX-XX
- **Freshworks AARRR最適化事例**: @research_knowledge.md p.XX-XX
- **Box AARRR最適化事例**: @research_knowledge.md p.XX-XX

### 測定ツール

- Google Analytics 4: {URL}
- Mixpanel/Amplitude: {URL}（DAU/MAU、Cohort分析）
- 決済システム: {URL}（NRR、LTV/CAC）
- Cohort分析ツール: {URL}（Retention分析）

### 関連ドキュメント

- PMF判定レポート: `Flow/{YYYYMM}/{YYYY-MM-DD}/pmf_judgment.md`
- ユニットエコノミクス分析: `Flow/{YYYYMM}/{YYYY-MM-DD}/unit_economics_analysis.md`
- フライホイール設計: `{IDEA_FOLDER}/documents/2_discovery/flywheel.md`

---

**作成者**: Claude Sonnet 4.5
**スキル**: `/measure-aarrr-forstartup`
**フレームワーク準拠**: 起業の科学 - AARRRフレームワーク（VC投資基準版）
**成功事例統合**: Airbnb、Freshworks、Box等のAARRRファネル最適化パターンを統合
```

---

## 成功基準（VC投資判断版）

1. ✅ **AARRR 5段階すべて測定**: Acquisition → Revenue まで完全測定（VC投資基準版）
2. ✅ **VC投資判断指標の統合測定**: DAU/MAU、NRR、LTV/CAC、Payback期間を自動計測
3. ✅ **成長率厳格検証**: 月次成長率20%以上、年次3倍以上の達成状況を自動判定
4. ✅ **業界ベンチマーク自動取得**: WebSearchで最新データを取得（VC投資基準優先）
5. ✅ **ボトルネック定量分析**: 転換率がVC基準を下回る段階を特定し、成長率・評価額への影響を定量化
6. ✅ **改善施策優先順位付け**: Impact × Ease × VC Appeal でスコアリング
7. ✅ **実装ロードマップ自動生成**: 1ヶ月/3ヶ月/6ヶ月の具体的な計画（VC調達タイムライン連動）
8. ✅ **Quick Wins特定**: 高Impact × 高Ease × 高VC Appealの即実行施策を抽出
9. ✅ **成功事例ベースの最適化提案**: Airbnb、Freshworks等のAARRRファネル最適化パターンを統合
10. ✅ **VC投資判断用KPIダッシュボード作成**: VCミーティングで提示可能な可視化レポートを生成

---

## Domain-Specific Knowledge (from Research)

### Success Patterns (成功事例からの抽出パターン)

#### Airbnb - AARRR最適化の成功パターン

**Acquisition**:
- "Do things that don't scale": 創業者自らニューヨークで写真撮影サービス提供
- 写真品質改善で予約2-3倍増（定量的な改善実証）
- Paul Graham助言後の直接訪問戦略: 100人以上のユーザー面談

**Activation**:
- Aha Moment（初回予約成功）への最短経路設計
- 初回体験の質を最優先（高品質な写真、詳細な説明）

**Retention**:
- ネットワーク効果の最大化: ホスト⇔ゲストの相互成長フライホイール
- レビューシステムによる信頼構築
- 継続利用の習慣形成（年次旅行計画への組み込み）

**参照**: @research_knowledge.md p.36-64, p.263-292

#### Freshworks - AARRR最適化の成功パターン

**Acquisition**:
- 競合（Zendesk）価格改定タイミングを狙ったゲリラマーケティング
- Hacker Newsでの初期ユーザー獲得
- AdWords全額投資で初期トラクション検証

**Activation**:
- SMB特化による使いやすさ（複雑さの排除）
- 導入時間: 数週間 → 数時間（10倍優位性）
- フリーミアムモデルで即時利用開始

**Retention**:
- NRR 120%+達成: アップセル・クロスセル戦略（Freshsales、Freshservice等）
- シンプルなUI・UXによる継続利用促進
- グローバル展開による市場拡大

**参照**: @research_knowledge.md p.69-99, p.296-326

#### Box - AARRR最適化の成功パターン

**Acquisition**:
- ボトムアップ採用戦略: IT部門を通さずに個人利用開始
- フリーミアムモデルでの口コミ成長
- エンタープライズ向けピボット後の急成長（年次500%+）

**Activation**:
- フリーミアムで即時利用開始（IT部門承認不要）
- 消費者向け直感的UIによる低い学習コスト
- 導入障壁の大幅削減（5倍優位性）

**Retention**:
- エンタープライズ機能の段階的追加（SSO、API等）
- セキュリティ・コンプライアンス対応（金融・医療等）
- 組織内での広がり（個人 → チーム → 組織全体）

**参照**: @research_knowledge.md p.107-130, p.330-365

### Common Pitfalls (失敗パターン・教訓)

- **頭から几帳面に読まない**: Abstract→Conclusion→Resultsの逆順アプローチ重要（落合陽一式リサーチ）
- **成長率未達成の放置**: 月次成長率20%未達成でVC調達困難化（調達成功率-50%）
- **VC重視指標の軽視**: DAU/MAU、NRR、LTV/CAC未測定でVC説得力低下
- **ボトルネック改善の先送り**: Quick Wins施策の実装遅延で成長機会損失
- **単一チャネル依存**: Paid広告のみに依存し、Organic成長を軽視

### Quantitative Benchmarks (定量的ベンチマーク)

| 指標 | VC投資基準 | 出典 |
|------|----------|------|
| 月次成長率（MRR） | **20%以上** | @domain_requirements.md, Airbnb/Freshworks事例 |
| 年次成長率（MRR） | **200%以上（3倍）** | @domain_requirements.md |
| DAU/MAU比率 | **30-50%** | SaaS業界標準、VC投資基準 |
| NRR | **120%以上** | Freshworks事例（120%+達成）、VC投資基準 |
| LTV/CAC比率 | **> 5.0** | @domain_requirements.md, Airbnb/Freshworks/Box事例 |
| Payback期間 | **< 12ヶ月** | VC投資基準、SaaS業界標準 |
| サインアップ率 | **3-5%** | 一般基準2-5%より厳格化 |
| Aha Moment達成率 | **50%以上** | 一般基準40%+より厳格化 |
| 月次継続率 | **90-95%** | B2B SaaS基準 |
| Churn Rate | **< 3%/月（B2B）** | VC投資基準、一般基準<5%より厳格化 |
| NPS | **50以上** | VC投資基準、一般基準40+より厳格化 |
| バイラル係数 | **> 1.0（理想）** | Airbnb型ネットワーク効果 |

### Best Practices (ベストプラクティス)

1. **成長率最優先**: 月次成長率20%、年次3倍を最優先KPIとして設定
2. **VC重視指標の継続測定**: DAU/MAU、NRR、LTV/CAC、Payback期間を週次で測定
3. **Quick Wins即実行**: VCミーティング前に高Impact × 高Ease × 高VC Appealの施策を実装
4. **成功事例の徹底研究**: Airbnb、Freshworks、Box等のAARRRファネル最適化パターンを自社に適用
5. **ボトルネック定量分析**: 成長阻害要因を定量的に特定し、成長率・評価額への影響を可視化
6. **投資家向けKPIダッシュボード常備**: VCミーティングで即提示可能な可視化レポートを常に最新化
7. **Cohort分析の徹底**: Retention分析はCohort単位で実施し、改善トレンドを可視化

### Reference

  - Airbnb AARRR最適化事例: p.36-64, p.263-292
  - Freshworks AARRR最適化事例: p.69-99, p.296-326
  - Box AARRR最適化事例: p.107-130, p.330-365
  - VC投資基準: p.14-40
  - 成長率指標: p.372-461
  - ユニットエコノミクス成功事例: p.261-370

  - VC投資基準: p.42-63
  - 評価基準の変更: p.45-72
  - 成長率目標: p.112-118

---

## Knowledge Base参照

### AARRR成功事例ケーススタディ（Tier 2）

このスキル用に12件の成功事例ケーススタディを統合しました。各事例は以下の構成で整理されています：

| # | 企業 | ファイル | 主要学習ポイント |
|---|------|---------|----------|
| 01 | Airbnb | `case_studies/tier2/measure-aarrr/01_airbnb_aarrr.md` | Do things that don't scale戦略、両面マーケットプレイスのAARRR |
| 02 | Freshworks | `case_studies/tier2/measure-aarrr/02_freshworks_aarrr.md` | 競合失敗を機会に、SMB特化戦略、NRR 120%達成 |
| 03 | Box | `case_studies/tier2/measure-aarrr/03_box_aarrr.md` | ボトムアップ採用、段階的アップセル、LTV/CAC改善 |
| 04 | Stripe | `case_studies/tier2/measure-aarrr/04_stripe_aarrr.md` | インフラ型ビジネスの成長特性、NRR 130-140%、開発者優先戦略 |
| 05 | Dropbox | `case_studies/tier2/measure-aarrr/05_dropbox_aarrr.md` | 紹介プログラムのバイラル性（K-factor 1.5-2.0）、LTV/CAC 8-12倍 |
| 06 | Slack | `case_studies/tier2/measure-aarrr/06_slack_aarrr.md` | チーム内バイラル、DAU/MAU 60-70%（業界最高）、NRR 120-130% |
| 07 | Uber | `case_studies/tier2/measure-aarrr/07_uber_aarrr.md` | 両面市場の課題、LTV/CAC低い、市場拡大依存の成長戦略 |
| 08 | Zoom | `case_studies/tier2/measure-aarrr/08_zoom_aarrr.md` | ワンクリック参加による導入障壁低下、NRR 130-140%、COVID-19効果 |
| 09 | Shopify | `case_studies/tier2/measure-aarrr/09_shopify_aarrr.md` | 非技術者向けツール化、App Storeエコシステム、GMV手数料モデル |
| 10 | Figma | `case_studies/tier2/measure-aarrr/10_figma_aarrr.md` | リアルタイム協調編集のバイラル性、DAU/MAU 50-60%、高NRR |
| 11 | Canva | `case_studies/tier2/measure-aarrr/11_canva_aarrr.md` | 非デザイナー向け市場、ソーシャルバイラル（K-factor 1.3-1.8）、LTV/CAC 9-15倍 |
| 12 | Notion | `case_studies/tier2/measure-aarrr/12_notion_aarrr.md` | コミュニティ駆動成長、複雑性と粘着性のトレードオフ、長期Payback |

**参照方法**: これらのケーススタディは、VC投資判断版のAARRR分析で具体例が必要な場合に参照してください。各事例から以下を抽出できます：
- ボトルネック特定の実践例
- VC基準達成の事例（成長率、DAU/MAU、NRR、LTV/CAC）
- Quick Wins施策の具体例
- 改善施策の優先順位付けロジック

---

### その他の参照資料

- グロースハック: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#growth-hacking`

---

## ForStartup Knowledge Base Reference

### 評価基準・フレームワーク
- VC投資基準総合: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-investment-criteria
  - CPF/PSF/PMF ≥70%、TAM ≥$1B、月次成長率 ≥20%、10倍優位性 3軸以上
  - NRR（Net Revenue Retention）≥120%、年次成長率 ≥300%（3倍、SaaS基準）
- VC調達ロードマップ: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#vc-fundraising-roadmap
  - Pre-Seed → Seed → Series A基準
- ユニットエコノミクス: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#unit-economics-vc-standard
  - LTV/CAC ≥5.0、CAC回収期間 ≤12ヶ月、Gross Margin ≥70%
- AARRR最適化: /Users/yuichi/AIPM/aipm_v0/.claude/skills/_shared/knowledge_base.md#aarrr-optimization
  - DAU/MAU ≥30%、Churn Rate <3%/月、バイラル係数 >1.0

### ケーススタディ
- 成功事例（Legendary）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/01_Legendary/
  - Brian Chesky（Airbnb）、Patrick Collison（Stripe）、Brian Armstrong（Coinbase）
- 成功事例（Unicorn）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/02_Unicorn/
  - Girish Mathrubootham（Freshworks）、Henrique Dubugras（Brex）
- 成功事例（VC-Backed）: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/documents/03_VC_Backed/
  - Dylan Field（Figma）、Vlad Tenev（Robinhood）、Melanie Perkins（Canva）

---

## 補足: データ収集のベストプラクティス（VC投資判断版）

### アナリティクスツール設定

**Google Analytics 4**:
- イベント設定: `sign_up`, `first_value_achieved`, `feature_used`, `purchase`
- コンバージョン設定: サインアップ、Aha Moment、課金
- **VC重視指標**: 訪問者数、サインアップ率、流入チャネル別CAC

**Mixpanel/Amplitude**:
- ユーザープロパティ: `signup_date`, `activation_date`, `plan_type`
- イベント追跡: 主要機能の利用頻度
- **VC重視指標**: **DAU/MAU比率**、Cohort分析、Retention分析

**決済システム（Stripe, Paddle等）**:
- MRR、ARPU、LTV/CAC自動計算
- **VC重視指標**: **NRR（Net Revenue Retention）**、Payback期間、GrossMargin

**Cohort分析ツール**:
- Retention Cohort分析: 月次Cohort別の継続率可視化
- Revenue Cohort分析: 月次Cohort別のLTV・NRR可視化

### データ整合性チェック

実行前に以下をチェック:
- [ ] 訪問者数とサインアップ数の整合性（サインアップ ≤ 訪問者）
- [ ] 継続率の論理性（D1 ≥ D7 ≥ D30）
- [ ] 収益計算の正確性（MRR = 有料ユーザー × ARPU）
- [ ] **NRR計算の正確性**: (前月MRR + アップセル - ダウングレード - 解約) / 前月MRR × 100%
- [ ] **LTV/CAC計算の正確性**: LTV = ARPU × 平均契約期間 / Churn Rate、CAC = マーケティング費用 / 新規顧客数
- [ ] **DAU/MAU計算の正確性**: 月間のDAU平均 / MAU × 100%
- [ ] **Payback期間計算の正確性**: CAC / (ARPU × GrossMargin) （月単位）

### VC投資判断用レポート自動化

以下のツールでレポートを自動生成:
- **Googleデータポータル / Looker**: VC投資判断用KPIダッシュボードの自動更新
- **Notion / Airtable**: 週次AARRR分析レポートの自動記録
- **Slack通知**: 成長率20%達成/未達成の自動アラート

---

**作成日**: 2026-01-02
**ステータス**: ✅ 実装完了（ForStartup Edition）
**次のステップ**: ユーザーによる初回実行とフィードバック収集
**VC調達支援**: Series A調達準備への統合完了
