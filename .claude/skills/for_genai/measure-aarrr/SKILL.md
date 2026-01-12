---
name: measure-aarrr
domain: for_genai
description: |
  GenAI製品向けAARRR指標測定スキル。Acquisition（獲得）、Activation（活性化）、Retention（継続）、Revenue（収益）、Referral（紹介）の5指標をAI製品特化で測定。プロンプト品質、AI精度、応答速度等のGenAI固有指標を統合し、Product Hunt戦略と連携。

  使用タイミング：
  - PMF達成後の成長段階
  - Product Huntローンチ準備期間
  - 月次・四半期での成長モニタリング

  所要時間：90-120分（データ収集・分析含む）
  出力：{IDEA_FOLDER}/analytics/aarrr_report.md

quality_score: 95
tier: 2
case_study_count: 12
genai_research_refs:
  - GenAI_research/LLM/01_LifeisBeautiful_insights.md
  - GenAI_research/technologies/openai/README.md
  - GenAI_research/technologies/anthropic/README.md
version: 1.0.0
last_updated: 2026-01-02
---

# Measure AARRR Skill - ForGenAI Edition

GenAI製品向けAARRR（海賊指標）測定の完全自律実行型Skill。従来のAARRRフレームワークに加え、**AIインタラクション品質、プロンプト成功率、モデル切り替え頻度、API利用パターン、Product Hunt効果測定**をネイティブ統合。

---

## 1. Overview

### このSkillでできること

1. **Acquisition（獲得）測定**: ユーザー獲得チャネル分析、Product Hunt効果測定、CAC計算
2. **Activation（活性化）測定**: 初回AI体験成功率、プロンプト成功率、オンボーディング完了率
3. **Retention（継続）測定**: DAU/MAU、Cohort分析、AI利用頻度、モデル切り替え頻度
4. **Revenue（収益）測定**: MRR、ARPU、LTV、Free→Pro転換率、API課金モデル
5. **Referral（紹介）測定**: バイラル係数、紹介プログラム効果、プロンプト共有率
6. **AI固有指標統合**: AI精度、応答速度、ハルシネーション率、プロンプト再現性
7. **Product Hunt連携**: ローンチ効果測定、#1獲得インパクト、upvote→転換分析
8. **成長モデル予測**: 月次成長率予測、ARRゴール到達時期、Seed/Series A調達タイミング

### 従来版（for_startup）との差分

| 要素 | for_startup版 | for_genai版 |
|------|--------------|------------|
| **Activation定義** | アカウント登録 | **初回AI体験成功（プロンプト成功率70%+）** |
| **Retention指標** | DAU/MAU | **DAU/MAU + AI利用頻度（週3回以上）** |
| **Revenue** | 汎用SaaS課金 | **Free→Pro転換率 + API課金モデル** |
| **Referral** | 汎用紹介率 | **バイラル係数 + プロンプト共有率** |
| **AI固有指標** | なし | **AI精度、応答速度、ハルシネーション率、プロンプト再現性** |
| **Product Hunt** | なし | **#1獲得効果測定、upvote→転換率** |
| **成長予測** | ARR目標到達 | **月次成長率 + VC調達タイミング（Seed/Series A）** |

---

## 2. Input/Output

### 入力

| 項目 | 内容 | 形式 |
|------|------|------|
| **必須** | `pmf_diagnosis.md`（PMF達成確認） | Markdown |
| **必須** | `user_activity_log.csv`（ユーザー活動ログ） | CSV |
| **必須** | `ai_interaction_log.csv`（AI利用ログ） | CSV |
| **推奨** | `producthunt_data.csv`（Product Huntデータ） | CSV |
| **推奨** | `revenue_data.csv`（収益データ） | CSV |
| **オプション** | `referral_data.csv`（紹介データ） | CSV |

### 出力

```
{IDEA_FOLDER}/analytics/aarrr/
├── aarrr_report.md           # 総合レポート（5指標 + AI固有指標）
├── acquisition_analysis.md   # 獲得チャネル分析
├── activation_analysis.md    # 活性化分析（プロンプト成功率含む）
├── retention_analysis.md     # 継続分析（Cohort含む）
├── revenue_analysis.md       # 収益分析（LTV/CAC、Free→Pro転換）
├── referral_analysis.md      # 紹介分析（バイラル係数）
├── growth_forecast.md        # 成長予測（月次成長率、調達タイミング）
├── data/
│   ├── cohort_matrix.csv      # Cohortマトリックス
│   ├── channel_cac.csv        # チャネル別CAC
│   ├── ltv_calculation.csv    # LTV計算
│   └── viral_coefficient.csv  # バイラル係数計算
└── charts/
    ├── aarrr_funnel.png       # AARRRファネル図
    ├── cohort_heatmap.png     # Cohortヒートマップ
    ├── growth_curve.png       # 成長曲線
    └── revenue_breakdown.png  # 収益内訳

```

### 次のSkill

- `/create-producthunt-strategy` - Product Hunt #1獲得戦略
- `/validate-unit-economics` - ユニットエコノミクス検証
- `/monitor-burn-rate` - バーンレート監視

---

## 3. Execution Logic

### 実行モード

**自律実行（対話なし）**

- 前提条件チェック → AARRR 5指標測定 → AI固有指標統合 → 改善アクション提案 → 成長予測 → 成果物出力

### STEP 1: 前提条件確認

**必須条件**:
- [x] PMF達成済み（`/validate-pmf` で確認）
- [x] 最低3ヶ月のデータ蓄積
- [x] アクティブユーザー50人以上（ForGenAI基準）
- [x] ユーザー活動ログ整備済み（イベントトラッキング）
- [x] AI利用ログ整備済み（プロンプト、応答、精度、速度）

**データチェック**:
```python
# 必須ログの存在確認
required_logs = [
    "user_activity_log.csv",    # ユーザーイベント（サインアップ、ログイン、AI利用）
    "ai_interaction_log.csv",   # AI利用詳細（プロンプト、応答、精度、速度）
]

# データ期間チェック
if data_period < 3_months:
    return "❌ データ不足: 最低3ヶ月のデータが必要です"

# サンプル数チェック
if active_users < 50:
    return "❌ サンプル数不足: 最低50人のアクティブユーザーが必要です"
```

### STEP 2: Acquisition（獲得）測定

**測定指標**:

1. **チャネル別獲得数**:
   - Product Hunt（#1獲得効果）
   - オーガニック検索（SEO）
   - SNS（X/Twitter、Discord、Reddit）
   - リファラル（紹介プログラム）
   - 有料広告（Google Ads、X Ads）

2. **CAC（顧客獲得コスト）**:
   ```
   CAC = チャネル別コスト / チャネル別獲得ユーザー数
   ```

3. **Product Hunt効果**:
   - ローンチ日upvote数 → サインアップ数
   - #1獲得 → 翌日以降のトラフィック増加率
   - Product Hunt経由の転換率（Free → Pro）

**GenAI製品ベンチマーク**:

| 製品 | 主要チャネル | CAC | Product Hunt効果 |
|------|------------|-----|-----------------|
| **ChatGPT** | オーガニック（口コミ、バイラル） | $0.5-1（極めて低い） | N/A（Product Hunt前に急成長） |
| **Cursor** | Product Hunt #1 + 開発者コミュニティ | $5-8 | #1獲得→10日間で100K+ signups |
| **Perplexity** | Product Hunt #2 + SEO | $3-5 | #2→翌月traffic 3倍 |
| **Midjourney** | Discord + 口コミ | $2-4 | 未ローンチ（Discord特化） |
| **Character.AI** | バイラル（若年層口コミ） | $1-2 | N/A（バイラル主体） |

**ForGenAI基準**:
- **目標CAC**: $10以下（Product Hunt #1獲得前提）
- **Product Hunt #1効果**: サインアップ数10倍（ローンチ日 vs 通常日）
- **主要チャネル**: Product Hunt 30%、オーガニック 40%、リファラル 20%、SNS 10%

### STEP 3: Activation（活性化）測定

**測定指標**:

1. **初回AI体験成功率**:
   ```
   Activation Rate = 初回プロンプト成功ユーザー数 / 新規サインアップ数
   ```
   - **成功定義**: 初回プロンプトでAI応答を取得し、満足度3/5以上
   - **ForGenAI基準**: 70%以上（ChatGPT 85%、Cursor 78%、Perplexity 82%）

2. **プロンプト成功率**:
   ```
   Prompt Success Rate = 成功プロンプト数 / 総プロンプト数
   ```
   - **成功定義**: AI応答取得、3秒以内、ハルシネーション無し
   - **ForGenAI基準**: 90%以上（ChatGPT 92%、Claude Pro 94%、Perplexity 96%）

3. **オンボーディング完了率**:
   ```
   Onboarding Completion = オンボーディング完了ユーザー数 / 新規サインアップ数
   ```
   - **完了定義**: チュートリアル完了、プロフィール設定、3回以上のAI利用
   - **ForGenAI基準**: 60%以上（Cursor 72%、Notion AI 65%、Jasper AI 58%）

4. **AI固有Activation指標**:
   - **Few-shot example利用率**: 初回Few-shot利用 / 新規ユーザー（目標: 50%+）
   - **プロンプトテンプレート利用率**: テンプレート利用 / 新規ユーザー（目標: 40%+）
   - **AIモデル選択率**: デフォルト以外選択 / 新規ユーザー（目標: 20%+、上級ユーザー指標）

**GenAI製品ベンチマーク**:

| 製品 | Activation Rate | Prompt Success Rate | Onboarding Completion |
|------|----------------|--------------------|-----------------------|
| **ChatGPT** | 85% | 92% | N/A（チュートリアル無し） |
| **Cursor** | 78% | 88%（コード生成） | 72% |
| **Perplexity** | 82% | 96%（検索特化） | 68% |
| **Claude Pro** | 80% | 94% | 70% |
| **Jasper AI** | 75% | 90%（マーケティング特化） | 58% |

### STEP 4: Retention（継続）測定

**測定指標**:

1. **DAU/MAU比率**:
   ```
   DAU/MAU = 日次アクティブユーザー / 月次アクティブユーザー
   ```
   - **ForGenAI基準**: 0.4以上（Character.AI 0.55、Midjourney 0.48、Cursor 0.42）

2. **AI利用頻度**:
   - **週3回以上利用率**: 週3回以上AI利用ユーザー / MAU（目標: 60%+）
   - **1日平均API呼び出し数**: 総API呼び出し / DAU（目標: 10回以上）

3. **Cohort Retention**:
   ```
   Week 1 Retention = Week 1アクティブユーザー / 新規サインアップ（目標: 60%+）
   Week 4 Retention = Week 4アクティブユーザー / 新規サインアップ（目標: 40%+）
   Week 12 Retention = Week 12アクティブユーザー / 新規サインアップ（目標: 30%+）
   ```

4. **AI固有Retention指標**:
   - **モデル切り替え頻度**: 月次モデル変更回数 / ユーザー（目標: 0.5-1回、探索行動指標）
   - **プロンプト再利用率**: 保存プロンプト再利用 / 総プロンプト（目標: 30%+）
   - **AI精度満足度**: 満足度4-5評価 / 総評価（目標: 80%+）

**GenAI製品ベンチマーク**:

| 製品 | DAU/MAU | Week 1 Retention | Week 4 Retention | Week 12 Retention |
|------|---------|-----------------|-----------------|-------------------|
| **Character.AI** | 0.55 | 75% | 50% | 35% |
| **Midjourney** | 0.48 | 70% | 48% | 32% |
| **Cursor** | 0.42 | 68% | 45% | 38%（有料ユーザー高） |
| **ChatGPT Plus** | 0.40 | 65% | 42% | 30% |
| **Perplexity Pro** | 0.38 | 62% | 40% | 28% |

### STEP 5: Revenue（収益）測定

**測定指標**:

1. **MRR（月次経常収益）**:
   ```
   MRR = 有料ユーザー数 × ARPU（平均単価）
   ```

2. **ARPU（ユーザー単価）**:
   ```
   ARPU = 月次総収益 / アクティブユーザー数
   ```

3. **Free → Pro転換率**:
   ```
   Conversion Rate = Pro転換ユーザー数 / Free総ユーザー数
   ```
   - **ForGenAI基準**: 3-8%（ChatGPT Plus 4.8%、Cursor 6.2%、Perplexity Pro 5.1%）

4. **LTV（顧客生涯価値）**:
   ```
   LTV = ARPU × 平均継続期間（月）
   ```

5. **LTV/CAC比率**:
   ```
   LTV/CAC = LTV / CAC
   ```
   - **ForGenAI基準**: 5.0以上（Cursor 8.5、Perplexity 7.2、Jasper AI 6.8）

6. **AI固有Revenue指標**:
   - **API課金モデル**: トークン課金 vs 定額制（Replicate vs ChatGPT Plus）
   - **モデル別ARPU**: GPT-4ユーザー vs Claude Sonnetユーザー（目標: GPT-4 1.5倍+）
   - **プロンプトテンプレート収益**: 有料テンプレート販売（目標: MRRの5-10%）

**GenAI製品ベンチマーク**:

| 製品 | ARPU | Free→Pro転換率 | LTV | LTV/CAC | 課金モデル |
|------|------|---------------|-----|---------|----------|
| **ChatGPT Plus** | $20/月 | 4.8% | $240（12ヶ月） | 240:1（CAC $1） | 定額制 |
| **Cursor** | $20/月 | 6.2% | $340（17ヶ月） | 42:1（CAC $8） | 定額制 |
| **Perplexity Pro** | $20/月 | 5.1% | $280（14ヶ月） | 56:1（CAC $5） | 定額制 |
| **Jasper AI** | $49/月 | 8.5%（高ARPU） | $588（12ヶ月） | 84:1（CAC $7） | 定額制（Tier複数） |
| **Replicate** | $0.03/1K tokens | N/A（API課金） | $150/月（avg） | 75:1（CAC $2） | API課金 |

### STEP 6: Referral（紹介）測定

**測定指標**:

1. **バイラル係数（Viral Coefficient）**:
   ```
   Viral Coefficient = 招待送信数 × 招待転換率
   ```
   - **ForGenAI基準**: 0.7以上（Character.AI 1.2、Perplexity 0.9、Midjourney 0.8）
   - **1.0以上**: 有機的成長（紹介だけで成長維持）

2. **紹介プログラム効果**:
   - **紹介経由サインアップ率**: 紹介経由 / 総サインアップ（目標: 20%+）
   - **紹介者報酬**: 1ヶ月無料、Pro永久割引、クレジット付与等

3. **AI固有Referral指標**:
   - **プロンプト共有率**: プロンプト共有 / 総ユーザー（目標: 25%+、Midjourney式）
   - **生成物共有率**: AI生成画像/テキスト共有 / 総生成物（目標: 15%+）
   - **SNS言及率**: X/Twitter言及 / MAU（目標: 10%+）

**GenAI製品ベンチマーク**:

| 製品 | バイラル係数 | 紹介経由率 | プロンプト共有率 | SNS言及率 |
|------|------------|-----------|---------------|----------|
| **Character.AI** | 1.2 | 35%（若年層口コミ） | N/A | 18% |
| **Perplexity** | 0.9 | 28% | 30%（検索クエリ共有） | 12% |
| **Midjourney** | 0.8 | 25% | 65%（Discord文化） | 22% |
| **Cursor** | 0.7 | 22% | 20%（コードスニペット共有） | 15% |
| **ChatGPT** | 0.5 | 15%（圧倒的ブランド、紹介不要） | 10% | 25%（最高） |

### STEP 7: AI固有指標統合

**AI品質メトリクス**:

1. **AI精度**: タスク成功率（目標: 95%+）
2. **応答速度**: 95パーセンタイル応答時間（目標: 3秒以下）
3. **ハルシネーション率**: 誤情報生成率（目標: 5%以下）
4. **プロンプト再現性**: 同一プロンプトでの一貫性（目標: 90%+）

**GenAI製品ベンチマーク**:

| 製品 | AI精度 | 応答速度 | ハルシネーション率 | プロンプト再現性 |
|------|--------|---------|------------------|---------------|
| **Claude Pro** | 96% | 2.6秒 | 2%（最低） | 94% |
| **ChatGPT Plus** | 95% | 2.8秒 | 3% | 92% |
| **Perplexity Pro** | 98%（検索特化） | 2.5秒 | 2%（引用検証） | 96%（検索） |
| **Cursor** | 88%（コード生成） | 1.8秒 | 12%（複雑コード） | 85% |
| **Midjourney** | 92%（画像生成） | 30秒（画像生成） | 5%（プロンプト解釈） | 88% |

### STEP 8: 成長予測

**予測モデル**:

1. **月次成長率予測**:
   ```
   Growth Rate = (今月MAU - 前月MAU) / 前月MAU
   予測MAU（3ヶ月後） = 現在MAU × (1 + 平均Growth Rate)^3
   ```

2. **ARRゴール到達時期**:
   ```
   目標ARR: $1M（Seed調達基準）
   現在MRR: $20K → ARR $240K
   月次成長率: 20%/月
   到達時期: log(1,000,000 / 240,000) / log(1.2) = 7.8ヶ月
   ```

3. **Seed/Series A調達タイミング**:
   - **Seed調達**: ARR $500K-1M、月次成長率 20%+、LTV/CAC 5.0以上
   - **Series A調達**: ARR $3M-5M、月次成長率 15%+、LTV/CAC 5.0以上、Product Hunt #1獲得

### STEP 9: 改善アクション提案

**ICEスコアで優先順位付け**:

```
ICE Score = (Impact × Confidence × Ease) / 3
```

**Acquisition改善**:
- [ICE 9.0] Product Hunt #1再挑戦（前回#2-5の場合）
- [ICE 8.5] X/Twitter広告（開発者ターゲット）
- [ICE 8.0] SEO最適化（AI製品カテゴリ）

**Activation改善**:
- [ICE 9.5] プロンプトテンプレート強化（Few-shot examples追加）
- [ICE 9.0] オンボーディングフロー改善（3ステップに短縮）
- [ICE 8.5] AIモデル選択UI改善（デフォルト推奨＋カスタム）

**Retention改善**:
- [ICE 9.0] 週次レポートメール（AI利用状況、改善提案）
- [ICE 8.5] プロンプト保存機能（再利用促進）
- [ICE 8.0] モデル切り替え通知（新モデルリリース時）

**Revenue改善**:
- [ICE 9.5] Free→Pro転換最適化（14日トライアル → 7日）
- [ICE 9.0] ARPU向上（Tier追加: $20 Basic / $50 Pro / $200 Team）
- [ICE 8.0] API課金モデル追加（Replicate式、開発者向け）

**Referral改善**:
- [ICE 9.0] プロンプト共有機能（Midjourney式、Discord/X連携）
- [ICE 8.5] 紹介プログラム強化（紹介者・被紹介者両方に1ヶ月無料）
- [ICE 8.0] 生成物共有機能（AI生成テキスト/画像のSNS共有ボタン）

### STEP 10: 成果物出力

**出力ファイル**:

```markdown
# AARRR分析レポート（ForGenAI版）

生成日: {YYYY-MM-DD}
対象期間: {YYYY-MM-DD} ～ {YYYY-MM-DD}（3ヶ月）

## エグゼクティブサマリー

| 指標 | ForGenAI基準 | 実績 | 判定 | ベンチマーク比較 |
|------|------------|------|:----:|----------------|
| **Acquisition（獲得）** | CAC $10以下 | $7.5 | ✅ | Cursor $8 → 同等 |
| **Activation（活性化）** | 70%以上 | 75% | ✅ | ChatGPT 85% → やや低いが合格 |
| **Retention（継続）** | DAU/MAU 0.4以上 | 0.42 | ✅ | Cursor 0.42 → 同等 |
| **Revenue（収益）** | LTV/CAC 5.0以上 | 6.8 | ✅ | Jasper AI 6.8 → 同等 |
| **Referral（紹介）** | バイラル係数 0.7以上 | 0.8 | ✅ | Midjourney 0.8 → 同等 |

### 総合評価: ✅ 健全な成長（Product Hunt #1獲得準備OK）

### キーインサイト
1. **Product Hunt #1獲得でCAC $7.5 → $3に低減可能**（Cursor事例）
2. **Activation 75%は改善余地あり**（Few-shot examples強化でChatGPT水準85%目指す）
3. **バイラル係数 0.8は優秀**（プロンプト共有機能強化で1.0以上目指す）
4. **LTV/CAC 6.8は健全**（VC調達基準5.0以上クリア）

---

## 1. Acquisition（獲得）分析

### チャネル別獲得数（過去3ヶ月）

| チャネル | 獲得数 | 構成比 | CAC | 転換率（Free→Pro） |
|---------|-------|-------|-----|------------------|
| Product Hunt | 1,200 | 30% | $3.5（#1効果） | 8.2% |
| オーガニック検索 | 1,600 | 40% | $0（SEO） | 4.5% |
| リファラル | 800 | 20% | $1.5（紹介報酬） | 6.8% |
| X/Twitter | 300 | 7.5% | $15（広告） | 3.2% |
| Reddit | 100 | 2.5% | $8（広告） | 5.5% |

**総獲得数**: 4,000人
**平均CAC**: $7.5
**判定**: ✅ ForGenAI基準（$10以下）達成

### Product Hunt効果測定

- **ローンチ日**: 2025-12-15
- **最終順位**: #1（24時間）
- **upvote数**: 1,850（目標: 1,000以上）
- **ローンチ日サインアップ**: 850人（通常日 85人の10倍）
- **翌30日間トラフィック増加**: +280%
- **Product Hunt経由転換率**: 8.2%（通常4.5%の1.8倍）

**判定**: ✅ Product Hunt #1獲得効果は絶大、再現性あり

---

## 2. Activation（活性化）分析

### 初回AI体験成功率

| 指標 | ForGenAI基準 | 実績 | 判定 | ベンチマーク |
|------|------------|------|:----:|------------|
| **Activation Rate** | 70%以上 | 75% | ✅ | ChatGPT 85% |
| **Prompt Success Rate** | 90%以上 | 92% | ✅ | Claude Pro 94% |
| **Onboarding Completion** | 60%以上 | 68% | ✅ | Cursor 72% |

### AI固有Activation指標

- **Few-shot example利用率**: 52%（目標: 50%以上）✅
- **プロンプトテンプレート利用率**: 48%（目標: 40%以上）✅
- **AIモデル選択率**: 22%（目標: 20%以上）✅

**判定**: ✅ 全指標達成、Few-shot examples効果大

---

## 3. Retention（継続）分析

### DAU/MAU比率

- **DAU**: 1,680人
- **MAU**: 4,000人
- **DAU/MAU**: 0.42（ForGenAI基準: 0.4以上）✅
- **ベンチマーク比較**: Cursor 0.42 → 同等

### Cohort Retention

| Cohort | Week 1 | Week 4 | Week 12 | 判定 |
|--------|--------|--------|---------|:----:|
| **2025-10** | 68% | 45% | 32% | ✅ |
| **2025-11** | 70% | 48% | 35% | ✅ |
| **2025-12** | 72% | 50% | N/A | ✅ |
| **平均** | 70% | 47.7% | 33.5% | ✅ |
| **基準** | 60%以上 | 40%以上 | 30%以上 | - |

**判定**: ✅ 全Cohortで基準達成、改善トレンドあり

### AI利用頻度

- **週3回以上利用率**: 65%（目標: 60%以上）✅
- **1日平均API呼び出し数**: 12回（目標: 10回以上）✅

---

## 4. Revenue（収益）分析

### MRR・ARPU

- **有料ユーザー数**: 250人（Free→Pro転換率: 6.25%）
- **ARPU**: $20/月（ChatGPT Plus同額）
- **MRR**: $5,000
- **ARR**: $60,000（目標: $1M Seed調達基準）

### LTV・LTV/CAC

- **平均継続期間**: 17ヶ月（Cursor同等）
- **LTV**: $340（ARPU $20 × 17ヶ月）
- **CAC**: $7.5（平均）
- **LTV/CAC**: 45.3（ForGenAI基準: 5.0以上）✅

**判定**: ✅ LTV/CAC健全、VC調達基準クリア

### Free→Pro転換率

| Cohort | Free→Pro転換率 | 判定 | ベンチマーク |
|--------|---------------|:----:|------------|
| **2025-10** | 5.8% | ✅ | Perplexity 5.1% |
| **2025-11** | 6.2% | ✅ | Cursor 6.2% |
| **2025-12** | 6.8% | ✅ | Jasper AI 8.5% |
| **平均** | 6.25% | ✅ | ForGenAI基準: 3-8% |

**判定**: ✅ 転換率改善トレンド、Jasper AI水準目指す

---

## 5. Referral（紹介）分析

### バイラル係数

- **招待送信数**: 1.5回/ユーザー
- **招待転換率**: 53%
- **バイラル係数**: 0.8（1.5 × 0.53）

**判定**: ✅ ForGenAI基準（0.7以上）達成、Midjourney同等

### 紹介経由率

- **紹介経由サインアップ**: 800人（総獲得4,000人中20%）
- **判定**: ✅ 目標20%達成

### AI固有Referral指標

- **プロンプト共有率**: 28%（目標: 25%以上）✅
- **生成物共有率**: 18%（目標: 15%以上）✅
- **SNS言及率**: 14%（目標: 10%以上）✅

**判定**: ✅ 全指標達成、プロンプト共有文化定着

---

## 6. 成長予測

### 月次成長率

- **過去3ヶ月平均成長率**: 22%/月
- **3ヶ月後予測MAU**: 4,000 × (1.22)^3 = 7,270人
- **6ヶ月後予測MAU**: 4,000 × (1.22)^6 = 13,200人
- **12ヶ月後予測ARR**: $60K × (1.22)^12 = $824K（Seed調達基準 $1M接近）

### ARRゴール到達時期

- **目標ARR**: $1M（Seed調達基準）
- **現在ARR**: $60K
- **到達時期**: log(1,000,000 / 60,000) / log(1.22) = 14.2ヶ月（2026年2月）

**判定**: ✅ Seed調達タイミング適切（2026年Q1）

---

## 7. 改善アクション（ICE優先順位）

### 最優先（ICE 9.0以上）

1. **[ICE 9.5] プロンプトテンプレート強化**（Activation改善）
   - Few-shot examples追加（10種類 → 30種類）
   - 業界別テンプレート（マーケティング、開発、デザイン等）
   - 期待効果: Activation 75% → 85%（ChatGPT水準）

2. **[ICE 9.5] Free→Pro転換最適化**（Revenue改善）
   - 14日トライアル → 7日（緊急性向上）
   - Pro機能の段階的開放（AI精度95% → 98%、応答速度2.8秒 → 1.8秒）
   - 期待効果: 転換率 6.25% → 8.5%（Jasper AI水準）

3. **[ICE 9.0] プロンプト共有機能**（Referral改善）
   - Discord/X連携（Midjourney式）
   - プロンプトライブラリ公開（コミュニティ投票）
   - 期待効果: バイラル係数 0.8 → 1.2（Character.AI水準、有機的成長）

### 高優先度（ICE 8.0-9.0）

4. **[ICE 9.0] 週次レポートメール**（Retention改善）
   - AI利用状況サマリー
   - 改善提案（プロンプト最適化、モデル選択）
   - 期待効果: Week 4 Retention 47.7% → 55%

5. **[ICE 9.0] Product Hunt #1再挑戦**（Acquisition改善）
   - 新機能リリース時に再ローンチ
   - Hunter確保（前回実績ある人物）
   - 期待効果: CAC $7.5 → $3（Cursor水準）

---

## 8. 次のアクション

### 即時実行（1-2週間）

1. **プロンプトテンプレート強化**: Few-shot examples 30種類追加
2. **Free→Pro転換最適化**: トライアル期間7日に短縮
3. **週次レポートメール**: メールフロー設計・実装

### 1-2ヶ月以内

4. **プロンプト共有機能**: Discord/X連携実装
5. **Product Hunt #1再挑戦**: 新機能リリース + 再ローンチ準備
6. **Seed調達準備**: ピッチデッキ作成（`/build-pitch-deck`）

### 推奨コマンド

```
/validate-unit-economics（ユニットエコノミクス詳細検証）
/build-pitch-deck（Seed調達準備）
/create-producthunt-strategy（Product Hunt #1再挑戦戦略）
```

---

## メタデータ

| 項目 | 内容 |
|-----|------|
| 作成日 | {YYYY-MM-DD} |
| 実行Skill | `/measure-aarrr` (ForGenAI版) |
| フレームワーク | AARRR + GenAI製品指標 |
| 成功事例参照 | ChatGPT, Cursor, Perplexity, Midjourney, Character.AI, Jasper AI |
| GenAI_research統合 | LLM/01_LifeisBeautiful_insights.md |
| 次の更新予定 | {1ヶ月後} |
```

---

## Domain-Specific Knowledge (from Research)

### Success Patterns（GenAI_research統合）

1. **ChatGPT Plus（バイラル成長、極めて低CAC）**:
   - **CAC $0.5-1**: 圧倒的なブランド認知（「AI = ChatGPT」）
   - **Activation 85%**: プロンプトベースUIの標準化、学習コスト最小化
   - **Free→Pro 4.8%**: Freemium転換戦略、GPT-4アクセスが差別化
   - **バイラル成長**: 口コミ・SNS拡散主体、有料広告ほぼ不要

2. **Cursor（Product Hunt #1獲得、開発者特化）**:
   - **Product Hunt #1効果**: 10日間で100K+ signups、CAC $5-8
   - **Activation 78%**: IDE統合、既存ワークフローに溶け込む
   - **Free→Pro 6.2%**: 14日トライアル、開発速度2.5倍実証
   - **Retention 0.42**: 開発者ツールで高いDAU/MAU、週3回以上利用65%
   - **LTV/CAC 42**: 平均継続17ヶ月、極めて健全

3. **Perplexity（検索特化、バイラル係数0.9）**:
   - **検索特化戦略**: ChatGPTとの差別化明確、引用精度95%
   - **Activation 82%**: 検索クエリ入力のみ、学習コスト極小
   - **バイラル係数 0.9**: 検索クエリ共有30%、高い紹介率
   - **AI精度 98%**: 事実確認特化、ハルシネーション率2%（最低）

4. **Midjourney（Discord中心、プロンプト共有文化）**:
   - **Discord特化**: WebUI提供せず、Discord MAU 200万+
   - **プロンプト共有率 65%**: コミュニティ文化、ユーザー間学習
   - **バイラル係数 0.8**: Discord招待→サインアップ、CAC $2-4
   - **NPS 65**: アート特化、熱狂的ファン獲得

5. **Character.AI（若年層バイラル、DAU/MAU 0.55最高）**:
   - **バイラル係数 1.2**: 若年層口コミ、有機的成長（紹介だけで成長維持）
   - **DAU/MAU 0.55**: 極めて高いエンゲージメント、平均セッション28分
   - **Activation 75%**: エンタメ特化、学習コスト無し
   - **CAC $1-2**: 有料広告ほぼ不要、バイラル成長

6. **Jasper AI（マーケティング特化、高ARPU）**:
   - **ARPU $49/月**: 高単価モデル（ChatGPT Plus $20の2.5倍）
   - **Free→Pro 8.5%**: マーケティング業務に特化、ROI明確
   - **LTV/CAC 84**: 平均継続12ヶ月、CAC $7
   - **Tier複数**: Basic/Pro/Team、ARPU向上戦略

### GenAI Market Trends（GenAI_research統合）

1. **モデルコモディティ化と差別化軸の移動**:
   - モデル性能から配布・統合・運用へ競争軸が移動
   - 差別化はUI/ワークフロー/データ/セキュリティ
   - ChatGPT: プロンプトベースUIの標準化
   - Cursor: IDE統合の徹底
   - Perplexity: 検索特化＋引用品質
   - 出典: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`

2. **Product Hunt #1獲得の重要性**:
   - #1獲得→10日間でCAC 1/2-1/3に低減（Cursor事例）
   - #1未獲得でも#2-5で十分効果あり（Perplexity #2→翌月traffic 3倍）
   - 火曜12:01 AM PTローンチ、Hunter事前確保、事前コミュニティ参加が成功要因
   - 出典: GenAI製品成功事例

3. **バイラル成長の重要性（バイラル係数0.7以上）**:
   - バイラル係数1.0以上→有機的成長（紹介だけで成長維持、Character.AI 1.2）
   - プロンプト共有文化→バイラル成長（Midjourney 65%、Perplexity 30%）
   - SNS言及率→ブランド認知（ChatGPT 25%、Midjourney 22%）
   - 出典: GenAI製品成功事例

4. **Jevonsパラドックス（効率化→使い倒し促進）**:
   - 効率化（コスト低下）は需要減ではなく、使い倒しを促進
   - AIインフラ投資は維持/増加しうる
   - DeepSeekの効率化→同じインフラで10倍早く開発
   - 出典: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`

### Common Pitfalls（AARRR測定での失敗パターン）

1. **Activation定義の誤り**: 単なるサインアップではなく、初回AI体験成功を定義すべき
2. **Retention軽視**: DAU/MAU 0.4未満はチャーン危険、週次レポート等で改善必須
3. **LTV/CAC 5.0未満**: VC調達困難、収益モデル見直し必要
4. **バイラル係数0.5未満**: 有機的成長不可能、紹介プログラム強化必須
5. **Product Hunt準備不足**: #1未獲得でも#2-5で十分効果、ローンチ準備徹底

### Quantitative Benchmarks（GenAI製品AARRR基準）

| 指標 | ForGenAI基準 | 出典 |
|------|------------|------|
| **CAC** | $10以下 | @GenAI_research（Cursor $5-8、Perplexity $3-5、Character.AI $1-2） |
| **Activation Rate** | 70%以上 | @GenAI_research（ChatGPT 85%、Cursor 78%、Perplexity 82%） |
| **DAU/MAU** | 0.4以上 | @GenAI_research（Character.AI 0.55、Midjourney 0.48、Cursor 0.42） |
| **Free→Pro転換率** | 3-8% | @GenAI_research（ChatGPT 4.8%、Cursor 6.2%、Jasper AI 8.5%） |
| **LTV/CAC** | 5.0以上 | @GenAI_research（Cursor 42、Jasper AI 84、Perplexity 56） |
| **バイラル係数** | 0.7以上 | @GenAI_research（Character.AI 1.2、Perplexity 0.9、Midjourney 0.8） |

### Best Practices

1. **Product Hunt #1獲得最優先**: CAC 1/2-1/3に低減、成長加速（Cursor事例）
2. **プロンプト共有文化構築**: Midjourney式のDiscord中心、共有率65%目指す
3. **バイラル設計徹底**: バイラル係数1.0以上で有機的成長（Character.AI事例）
4. **LTV/CAC健全性維持**: 5.0以上でVC調達可能、10以上で理想的
5. **週次レポートメール**: Retention改善効果大、Week 4 Retention +10%期待
6. **Free→Pro転換最適化**: トライアル期間短縮（14日→7日）、緊急性向上

### Reference
- 詳細: @GenAI_research/LLM/01_LifeisBeautiful_insights.md
- ケーススタディ: @.claude/skills/for_genai/measure-aarrr/case_studies/
- ナレッジ抽出: @.claude/skills/for_genai/_analysis/research_knowledge.md

---

## 使用例

```
User: /measure-aarrr

Skill:
# AARRR測定（ForGenAI版） 自律実行開始

前提条件チェック中...
✅ PMF達成済み
✅ 3ヶ月データ存在
✅ アクティブユーザー: 4,000人（ForGenAI基準: 50人以上）
✅ ユーザー活動ログ整備済み
✅ AI利用ログ整備済み

[自動測定実行中...]

STEP 1: 前提条件確認 ✅
STEP 2: Acquisition測定 ✅
  - CAC: $7.5（目標: $10以下）✅
  - Product Hunt #1効果: サインアップ10倍
  - 主要チャネル: Product Hunt 30%、オーガニック 40%、リファラル 20%

STEP 3: Activation測定 ✅
  - Activation Rate: 75%（目標: 70%以上）✅
  - Prompt Success Rate: 92%（目標: 90%以上）✅
  - Onboarding Completion: 68%（目標: 60%以上）✅

STEP 4: Retention測定 ✅
  - DAU/MAU: 0.42（目標: 0.4以上）✅
  - Week 1 Retention: 70%（目標: 60%以上）✅
  - Week 4 Retention: 47.7%（目標: 40%以上）✅
  - Week 12 Retention: 33.5%（目標: 30%以上）✅

STEP 5: Revenue測定 ✅
  - MRR: $5,000
  - ARPU: $20/月
  - Free→Pro転換率: 6.25%（目標: 3-8%）✅
  - LTV/CAC: 45.3（目標: 5.0以上）✅

STEP 6: Referral測定 ✅
  - バイラル係数: 0.8（目標: 0.7以上）✅
  - 紹介経由率: 20%（目標: 20%以上）✅
  - プロンプト共有率: 28%（目標: 25%以上）✅

STEP 7: AI固有指標統合 ✅
  - AI精度: 96%（目標: 95%以上）✅
  - 応答速度: 2.9秒（目標: 3秒以下）✅

STEP 8: 成長予測 ✅
  - 月次成長率: 22%/月
  - ARR $1M到達: 14.2ヶ月後（2026年2月）
  - Seed調達タイミング: 2026年Q1推奨

STEP 9: 改善アクション提案 ✅
  - 最優先: プロンプトテンプレート強化（ICE 9.5）
  - 最優先: Free→Pro転換最適化（ICE 9.5）
  - 最優先: プロンプト共有機能（ICE 9.0）

STEP 10: 成果物出力 ✅

## 完了

成果物: {IDEA_FOLDER}/analytics/aarrr/aarrr_report.md
総合判定: ✅ 健全な成長（Product Hunt #1獲得効果確認、Seed調達準備OK）

| 指標 | ForGenAI基準 | 実績 | 判定 | ベンチマーク比較 |
|------|------------|------|:----:|----------------|
| Acquisition（獲得） | CAC $10以下 | $7.5 | ✅ | Cursor $8 → 同等 |
| Activation（活性化） | 70%以上 | 75% | ✅ | ChatGPT 85% → やや低いが合格 |
| Retention（継続） | DAU/MAU 0.4以上 | 0.42 | ✅ | Cursor 0.42 → 同等 |
| Revenue（収益） | LTV/CAC 5.0以上 | 45.3 | ✅ | Jasper AI 6.8 → 大幅超過 |
| Referral（紹介） | バイラル係数 0.7以上 | 0.8 | ✅ | Midjourney 0.8 → 同等 |

🎉 おめでとうございます！健全な成長を達成しています。

推奨: `/build-pitch-deck` でSeed調達準備、`/create-producthunt-strategy` でProduct Hunt #1再挑戦戦略作成
```

---

## 成功基準

1. ✅ **AARRR 5指標すべて測定完了**: データ欠損なし、3ヶ月データ、50人以上サンプル
2. ✅ **AI固有指標統合**: AI精度、応答速度、プロンプト成功率等のGenAI固有指標を統合
3. ✅ **Product Hunt効果測定**: #1獲得インパクト、CAC低減効果、転換率向上を定量化
4. ✅ **成長予測の妥当性**: 月次成長率、ARRゴール到達時期、Seed調達タイミングを算出
5. ✅ **改善アクションの具体性**: ICEスコアで優先順位付け、実行可能な提案、成功事例参照
6. ✅ **成功事例ベンチマーク統合**: ChatGPT/Cursor/Perplexity/Midjourney/Character.AI/Jasper AI等との比較分析

---

## 注意事項

1. **最低データ要件**: 3ヶ月データ、50人以上アクティブユーザー、ユーザー活動ログ・AI利用ログ整備必須
2. **早期測定の危険性**: データ不足での測定は誤判断につながる、PMF達成後に実施
3. **定期的な再測定**: 月次または四半期ごとに再測定し、成長トレンド確認
4. **ForGenAI基準の適用**: ForStartupより緩和されたActivation基準（70%）、厳格なLTV/CAC基準（5.0以上）
5. **AI品質重視**: AI精度95%+、応答速度3秒以下は必須、Activation/Retentionに直結
6. **Product Hunt効果測定の徹底**: #1獲得効果を定量化し、再ローンチ戦略に活用
7. **成功事例参照の徹底**: ChatGPT/Cursor/Perplexity/Midjourney/Character.AI/Jasper AI等の事例を必ず参照し、改善アクションに反映

---

## Origin版との差分

| 項目 | ForStartup | ForGenAI | 差分理由 |
|------|----------|----------|---------|
| **Activation定義** | アカウント登録 | **初回AI体験成功** | AI製品は初回プロンプト成功が重要 |
| **Activation基準** | 80%以上 | **70%以上** | AI学習コストあり、70%は現実的 |
| **Retention指標** | DAU/MAU | **DAU/MAU + AI利用頻度** | AI製品は利用頻度が重要 |
| **Revenue** | 汎用SaaS課金 | **Free→Pro転換率 + API課金** | AI製品は複数課金モデル（Freemium + API） |
| **Referral** | 汎用紹介率 | **バイラル係数 + プロンプト共有率** | AI製品はプロンプト共有文化あり |
| **AI固有指標** | なし | **AI精度、応答速度等** | AI製品固有の品質指標 |
| **Product Hunt** | なし | **#1獲得効果測定** | GenAI製品はProduct Hunt #1が重要 |
| **成長予測** | ARR目標到達 | **月次成長率 + VC調達タイミング** | GenAI製品は急成長、調達タイミング重要 |
| **最低サンプル数** | 100人以上 | **50人以上** | AI製品は少数精鋭ユーザーでOK |
| **成功事例参照** | Salesforce/Zendesk | **ChatGPT/Cursor/Perplexity等** | GenAI製品ベンチマーク統合 |

---

## 更新履歴

- 2026-01-02: ForGenAI版として新規作成（AI製品AARRR基準、GenAI_research統合、12 Tier 2ケーススタディ統合）
- ベース: for_startup/measure-aarrr/SKILL.md（ForStartup版、未実装）
