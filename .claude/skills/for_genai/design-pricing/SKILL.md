---
name: design-pricing-for-genai
description: |
  ForGenAI特化版: 生成AI市場に最適化されたプライシング戦略を設計する自律実行型スキル。SaaSサブスク、API従量課金、Freemiumモデルを組み合わせ、GenAI成功製品のUnit Economicsベンチマーク（ChatGPT、Jasper、Midjourney等）に基づいた収益モデルを構築します。

  ForGenAI固有の特徴:
  - SaaSサブスク検討（ChatGPT Plus $20/月、Jasper $49/月、Midjourney $10/月）
  - API従量課金による収益化（OpenAI API $0.01/1K tokens、利益率5倍以上）
  - Freemium戦略評価（月間制限付き無料 + 有料プラン、Free→Paid転換率3-5%）
  - GenAI_Research統合（12件の成功事例、収益モデル成功パターン・失敗教訓）

  使用タイミング:
  - PSF検証段階（MVP完成後）
  - 収益モデル検証前
  - Product Hunt準備段階

  所要時間: 60-90分（自動実行）
  出力: pricing_strategy_forgenai.md
domain: for_genai
stage: psf_validation
---

# Design Pricing Skill (ForGenAI Edition)

生成AI市場に最適化されたプライシング戦略を設計する自律実行型Skill。**ForGenAI特化版**では、ChatGPT、Jasper、Midjourney等の成功製品の収益モデルをベンチマークとし、SaaSサブスク・API従量課金・Freemium戦略を組み合わせた持続可能な収益モデルを構築します。

---

## このSkillでできること

1. **収益モデル分類**: SaaS/API/Freemium/ハイブリッドの4類型から最適選択
2. **SaaSサブスク設計**: ChatGPT Plus $20/月パターン、Jasper $49/月パターン
3. **API従量課金設計**: OpenAI API $0.01/1K tokens、利益率5倍以上の設定
4. **Freemium戦略評価**: 月間制限付き無料 + 有料プラン、Free→Paid転換率3-5%
5. **Unit Economics試算**: LTV/CAC比、Churn率、継続期間、損益分岐点の計算
6. **価格設定根拠**: 顧客価値、競合比較、API料金コスト構造に基づく価格決定
7. **GenAI Research事例との比較**: ChatGPT、Jasper、Midjourney、Perplexity等の収益モデルとのベンチマーク

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `lean_canvas.md`, `psf_diagnosis.md`, `competitor_research.md`, `ai_tech_stack_selection.md` |
| **出力** | `{IDEA_FOLDER}/documents/3_planning/pricing_strategy_forgenai.md` |
| **次のSkill** | `/validate-unit-economics` または `/create-producthunt-strategy` |
| **ステージ** | PSF検証〜Product Hunt準備段階 |

---

## ForGenAI固有の評価基準

### 収益モデル調整

| 指標 | Origin | ForGenAI | 理由 |
|------|--------|----------|------|
| **価格戦略** | 標準価格設定 | **Freemium優先検討** | ChatGPT: 無料プランで100M+ MAU獲得、Plus $20/月で収益化 |
| **収益化** | サブスク中心 | **SaaS + API従量のハイブリッド** | OpenAI: API従量 + ChatGPT Plus、Perplexity: Pro $20/月 + API |
| **Free→Paid転換率** | 考慮なし | **3-5%目標** | ChatGPT 4.8%、Cursor 5.1%、Perplexity 3.2% |
| **Unit Economics目標** | LTV/CAC比 3倍以上 | **LTV/CAC比 5倍以上** | GenAI成功製品: 10-20倍、最低基準5倍 |

### API料金シミュレーション（新規項目）

| 指標 | 計算方法 | 目標値 | 根拠 |
|------|---------|--------|------|
| **1ユーザー月間コスト** | リクエスト数 × トークン数 × API料金 | $0.50-$5 | OpenAI API $0.01/1K tokens基準 |
| **推奨価格** | API料金の5倍以上 | $2.99-$50/月 | 利益率80%以上、ChatGPT Plus $20/月参考 |
| **Free Tier制限** | 月間リクエスト数 | 10-100回 | バイラル成長とコスト抑制の両立 |

---

## Domain-Specific Knowledge (from GenAI_Research)

### Success Patterns（収益モデル成功事例）

#### 1. ChatGPT（OpenAI）- Freemium + SaaSサブスクの成功

**収益モデル**:
| 項目 | 内容 | 収益化手段 |
|------|------|----------|
| **無料プラン** | GPT-3.5 Turbo無制限 | 100M+ MAU獲得、バイラル成長 |
| **ChatGPT Plus** | $20/月（GPT-4o無制限） | 150M+ subscribers、$3B ARR |
| **ChatGPT Team** | $25/月/ユーザー | 中小企業向け、管理機能 |
| **ChatGPT Enterprise** | カスタム価格 | 大企業向け、セキュリティ強化 |
| **API従量課金** | $0.01/1K tokens〜 | 開発者向け、B2B収益 |

**成果**:
- Free→Paid転換率: 4.8%（150M+ subscribers / 3.1B MAU推定）
- LTV/CAC比: 15-20倍（推定LTV $240、CAC $12-16）
- Churn率: 推定5-8%（年間）
- 継続期間: 平均12-18ヶ月
- ARR: $3B+（2024年推定）

**Unit Economics詳細**:
```
LTV = ARPU $20/月 × 継続期間12ヶ月 = $240
CAC = バイラル成長（自然流入95%）、有料広告費（$12-16/ユーザー）
LTV/CAC比 = $240 / $12-16 = 15-20倍
Churn率 = 5-8%（年間、業界平均15-20%の1/2〜1/3）
```

**ForGenAI教訓**:
- **Freemiumでバイラル成長**: 無料プランで100M+ MAU獲得、有料転換4.8%で十分収益化
- **$20/月の価格設定**: ChatGPT Plusが市場標準、これを上回る価値提供が必要
- **API + SaaSのハイブリッド**: 個人向けSaaS + 開発者向けAPI、収益源の多様化
- **LTV/CAC比 15-20倍**: バイラル成長でCAC最小化、高LTVで圧倒的収益性

#### 2. Jasper AI - マーケター特化SaaSサブスクの成功

**収益モデル**:
| 項目 | 内容 | 収益化手段 |
|------|------|----------|
| **Starter** | $49/月（月間10万words） | 個人マーケター向け |
| **Boss Mode** | $125/月（無制限） | プロマーケター向け |
| **Business** | カスタム価格 | チーム・企業向け |
| **API** | 従量課金 | カスタムユースケース |

**成果**:
- ARR: $75M（2022年ピーク）
- 有料ユーザー: 10万人以上
- LTV/CAC比: 10-15倍（推定LTV $600、CAC $40-60）
- Churn率: 10-15%（年間）
- 継続期間: 平均10-12ヶ月

**Unit Economics詳細**:
```
LTV = ARPU $49/月 × 継続期間12ヶ月 = $588
CAC = Product Hunt #2効果、有料広告費（$40-60/ユーザー）
LTV/CAC比 = $588 / $40-60 = 10-15倍
Churn率 = 10-15%（年間）
```

**ForGenAI教訓**:
- **$49/月の高単価設定**: ChatGPT Plus $20/月の2倍以上、特化価値で差別化
- **月間10万words制限**: 使用量制限でコスト管理、無制限プランは$125/月
- **Product Hunt #2効果**: 初期ユーザー獲得、CAC削減
- **LTV/CAC比 10-15倍**: マーケター特化でCAC抑制、高ARPU

#### 3. Midjourney - Discord + サブスクの成功

**収益モデル**:
| 項目 | 内容 | 収益化手段 |
|------|------|----------|
| **Basic** | $10/月（月間200画像） | 初心者向け |
| **Standard** | $30/月（月間無制限） | 一般ユーザー向け |
| **Pro** | $60/月（ステルスモード、無制限） | プロ向け |
| **Mega** | $120/月（商用利用、無制限） | 企業向け |

**成果**:
- 月間売上: $200M（2024年推定）
- 有料ユーザー: 200万人以上（$10-60/月の平均$30計算）
- LTV/CAC比: 20倍以上（推定LTV $360、CAC $15-20）
- Churn率: 推定8-12%（年間）
- 継続期間: 平均12ヶ月

**Unit Economics詳細**:
```
LTV = ARPU $30/月 × 継続期間12ヶ月 = $360
CAC = Discord経由バイラル成長（$15-20/ユーザー）
LTV/CAC比 = $360 / $15-20 = 18-24倍
Churn率 = 8-12%（年間）
```

**ForGenAI教訓**:
- **$10/月の低価格エントリー**: 初心者向け、月間200画像制限でコスト管理
- **Discord経由バイラル成長**: CAC最小化、コミュニティ主導
- **Pro/Mega高額プラン**: $60-120/月、商用利用需要
- **LTV/CAC比 20倍以上**: バイラル成長でCAC最小化、高継続率

#### 4. Perplexity AI - Freemium + Pro $20/月の成功

**収益モデル**:
| 項目 | 内容 | 収益化手段 |
|------|------|----------|
| **Free** | GPT-3.5、月間5回Pro検索 | バイラル成長、Product Hunt #1獲得 |
| **Perplexity Pro** | $20/月（無制限Pro検索、GPT-4o、Claude） | ChatGPT Plus同価格、差別化 |
| **API** | 従量課金 | 開発者向け、B2B収益 |

**成果**:
- Free→Paid転換率: 3.2%（推定）
- ARR: $20M（2024年推定）
- LTV/CAC比: 12-18倍（推定LTV $240、CAC $13-20）
- Churn率: 推定10-12%（年間）
- Product Hunt #1獲得（3,200 upvotes）

**Unit Economics詳細**:
```
LTV = ARPU $20/月 × 継続期間12ヶ月 = $240
CAC = Product Hunt #1効果、自然流入（$13-20/ユーザー）
LTV/CAC比 = $240 / $13-20 = 12-18倍
Churn率 = 10-12%（年間）
Free→Paid転換率 = 3.2%
```

**ForGenAI教訓**:
- **$20/月の市場標準価格**: ChatGPT Plusと同価格、差別化はCitation機能
- **Free Tier戦略**: 月間5回Pro検索無料、有料転換3.2%
- **Product Hunt #1効果**: 初期ユーザー爆発的獲得、CAC削減
- **複数LLM対応**: GPT-4o + Claude、技術スタック差別化

#### 5. Cursor - 開発者特化、$20/月、転換率5.1%の成功

**収益モデル**:
| 項目 | 内容 | 収益化手段 |
|------|------|----------|
| **Free** | 月間2,000 completions | 開発者向けバイラル成長 |
| **Pro** | $20/月（無制限completions） | 開発者生産性10倍、転換率5.1% |

**成果**:
- Free→Paid転換率: 5.1%（GenAI市場最高クラス）
- LTV/CAC比: 15倍以上（推定LTV $240、CAC $15-20）
- Churn率: 推定8%（年間、開発者は高継続率）
- 継続期間: 平均12ヶ月以上

**Unit Economics詳細**:
```
LTV = ARPU $20/月 × 継続期間12ヶ月 = $240
CAC = VS Code拡張でバイラル成長（$15-20/ユーザー）
LTV/CAC比 = $240 / $15-20 = 12-16倍
Churn率 = 8%（年間）
Free→Paid転換率 = 5.1%（業界最高クラス）
```

**ForGenAI教訓**:
- **転換率5.1%の高さ**: GenAI市場最高クラス、開発者特化が鍵
- **$20/月の開発者標準**: GitHub Copilot $10/月を上回る価値提供
- **VS Code統合**: シームレスUX、スイッチングコスト構築
- **月間2,000 completions無料**: 十分な試用機会、転換率向上

#### 6. Notion AI - 既存ユーザー基盤活用、$10/月の成功

**収益モデル**:
| 項目 | 内容 | 収益化手段 |
|------|------|----------|
| **Notion AI** | $10/月（既存Notion Plus上乗せ） | 既存ユーザー基盤活用 |
| **API** | 従量課金 | 開発者向け、B2B収益 |

**成果**:
- 既存Notion Plus転換率: 15-20%（推定）
- ARR: $10B目標（Notion全体、AI寄与度20-30%）
- LTV/CAC比: 25倍以上（推定LTV $120、CAC $3-5）
- Churn率: 推定5%（年間、既存ユーザー基盤）

**Unit Economics詳細**:
```
LTV = ARPU $10/月 × 継続期間12ヶ月 = $120
CAC = 既存Notionユーザーへのアップセル（$3-5/ユーザー）
LTV/CAC比 = $120 / $3-5 = 24-40倍
Churn率 = 5%（年間、既存ユーザー基盤）
既存ユーザー転換率 = 15-20%
```

**ForGenAI教訓**:
- **$10/月の低価格**: ChatGPT Plus $20/月の半額、既存製品への追加オプション
- **既存ユーザー基盤活用**: CAC最小化、転換率15-20%
- **LTV/CAC比 25倍以上**: 既存ユーザーへのアップセルでCAC削減
- **複数ツール統合**: ドキュメント + AI、統合価値

### Common Pitfalls（失敗パターン）

#### 1. 過度な従量課金によるユーザー離脱

**収益モデルの問題点**:
| 項目 | 数値 | 問題点 |
|------|------|--------|
| **API料金転嫁100%** | $0.01/1K tokens | ユーザーが予測不能なコスト不安 |
| **月額上限なし** | 従量無制限 | 高額請求リスク、離脱 |
| **Free Tierなし** | 初回から有料 | バイラル成長の機会損失 |

**失敗要因**:
- **予測不能なコスト不安**: ユーザーが「今月いくらになるか分からない」と離脱
- **高額請求リスク**: 月$100超えの請求で解約、Churn率50%以上
- **Free Tierなし**: バイラル成長の機会損失、CAC高騰

**Lessons Learned**:
- API料金転嫁は50%以下に抑える、残りは月額定額でカバー
- 月額上限設定（例: $50/月で無制限）、コスト不安解消
- Free Tier必須（月間10-100リクエスト無料）、バイラル成長

#### 2. Free Tierなしによるバイラル成長機会損失

**収益モデルの問題点**:
| 項目 | 内容 | 問題点 |
|------|------|--------|
| **初回から有料** | $20/月の初期設定 | バイラル成長の機会損失 |
| **試用期間短期** | 7日間無料 | 十分な試用機会なし |
| **CAC高騰** | $50-100/ユーザー | 有料広告依存、収益性悪化 |

**失敗要因**:
- **バイラル成長の機会損失**: ChatGPT無料版のような爆発的成長不可
- **CAC高騰**: 有料広告依存、$50-100/ユーザー
- **試用機会不足**: 7日間では価値実感できず、転換率1-2%

**Lessons Learned**:
- Free Tier必須（月間10-100リクエスト無料）、バイラル成長
- 試用期間30日以上、十分な価値実感
- Free→Paid転換率3-5%目標、ChatGPT 4.8%参考

#### 3. 高価格設定によるエンタープライズ限定化

**収益モデルの問題点**:
| 項目 | 数値 | 問題点 |
|------|------|--------|
| **月額料金** | $100/月以上 | 個人ユーザー離脱、市場縮小 |
| **エンタープライズ限定** | $1,000/月〜 | バイラル成長不可 |
| **Free Tierなし** | 初回から$100/月 | 試用機会なし、転換率0.1%以下 |

**失敗要因**:
- **市場縮小**: 個人ユーザー離脱、エンタープライズのみ
- **バイラル成長不可**: Free Tierなし、口コミ拡散なし
- **転換率0.1%以下**: 高額すぎて試用すらされない

**Lessons Learned**:
- 個人向け$10-50/月、チーム向け$100-500/月、エンタープライズ$1,000+/月の3層構造
- Free Tier必須、バイラル成長の起点
- 高額プランはエンタープライズ限定、個人向けは低価格

#### 4. API料金シミュレーション不足による赤字

**収益モデルの問題点**:
| 項目 | 数値 | 問題点 |
|------|------|--------|
| **1ユーザー月間コスト** | $10（OpenAI API料金） | 月額$20では赤字リスク |
| **利益率** | 50%（$20/月、コスト$10） | 目標80%に未達 |
| **無制限プラン** | $20/月 | ヘビーユーザーで赤字 |

**失敗要因**:
- **API料金シミュレーション不足**: 1ユーザー月間コストの過小評価
- **無制限プランのリスク**: ヘビーユーザーで月$50コスト、$20/月で赤字
- **利益率50%**: 目標80%に未達、収益性悪化

**Lessons Learned**:
- 1ユーザー月間コスト試算必須（リクエスト数 × トークン数 × API料金）
- 推奨価格: API料金の5倍以上（利益率80%）
- 無制限プランは月額$50以上、または月間リクエスト上限設定

### Quantitative Benchmarks

#### 収益モデル別のUnit Economics

| 収益モデル | 製品数 | 平均LTV/CAC比 | 平均Churn率 | 代表製品 |
|----------|-------|------------|----------|---------|
| **Freemium（無料+有料）** | 6 | 15-20倍 | 5-10% | ChatGPT（15-20倍、Churn率5-8%） |
| **SaaSサブスク** | 5 | 10-15倍 | 10-15% | Jasper（10-15倍、Churn率10-15%） |
| **API従量課金** | 3 | 20-30倍 | 15-20% | OpenAI API（高LTV/CAC、高Churn） |
| **ハイブリッド（SaaS+API）** | 4 | 12-18倍 | 8-12% | Perplexity（12-18倍、Churn率10-12%） |

**ForGenAI基準**:
- **目標LTV/CAC比**: 5倍以上（健全）、10倍以上（優秀）、15倍以上（卓越）
- **目標Churn率**: 15%以下（標準）、10%以下（優秀）、5%以下（卓越）
- **目標継続期間**: 12ヶ月以上

#### Free→Paid転換率の定量評価

| 製品 | Free→Paid転換率 | Free Tier制限 | 有料プラン価格 | 代表的差別化 |
|------|---------------|-------------|-------------|------------|
| **ChatGPT** | 4.8% | GPT-3.5無制限 | $20/月（GPT-4o無制限） | GPT-4o性能、無制限 |
| **Cursor** | 5.1% | 月間2,000 completions | $20/月（無制限） | VS Code統合、開発者特化 |
| **Perplexity** | 3.2% | 月間5回Pro検索 | $20/月（無制限Pro検索） | Citation、複数LLM |
| **Notion AI** | 15-20% | Notion Plus必須 | $10/月（既存ユーザー） | 既存ユーザー基盤活用 |

**Free→Paid転換率の効果**:
- **転換率5.1%**: Cursor、GenAI市場最高クラス、開発者特化が鍵
- **転換率4.8%**: ChatGPT、汎用AI市場で圧倒的成功
- **転換率3.2%**: Perplexity、検索エンジン再定義で成功
- **転換率15-20%**: Notion AI、既存ユーザー基盤活用でCAC最小化

#### API料金シミュレーション基準

| 指標 | 計算方法 | 目標値 | 例（ChatGPT想定） |
|------|---------|--------|-----------------|
| **1リクエストトークン数** | 入力 + 出力トークン | 500トークン平均 | GPT-4o: 入力300 + 出力200 |
| **月間リクエスト数** | 1ユーザー平均 | 100回/月 | ChatGPT Plus: 無制限（実質100-500回/月） |
| **1ユーザー月間コスト** | リクエスト数 × トークン数 × API料金 | $0.50-$5 | 100 × 500 / 1000 × $0.01 = $0.50 |
| **推奨月額価格** | API料金の5倍以上 | $2.99-$50/月 | $0.50 × 5 = $2.50（最低）、ChatGPT $20/月 |
| **利益率** | (月額価格 - API料金) / 月額価格 | 80%以上 | ($20 - $0.50) / $20 = 97.5% |

### Best Practices

#### 1. Freemium戦略の採用検討

**実践方法**:
- **ChatGPTパターン**: 無料プランでバイラル成長、Plus $20/月で収益化
- **Free Tier設定**: 月間10-100リクエスト無料、有料転換3-5%目標
- **収益化手段**: SaaSサブスク$10-50/月、API従量課金

**判断基準**:
- ターゲット市場: B2C SaaS、個人ユーザー向け
- バイラル成長可能性: 口コミ拡散、Product Hunt #1獲得
- Free→Paid転換率: 3-5%以上

**効果**:
- バイラル成長でCAC削減1/5〜1/10
- 100M+ MAU獲得、市場シェア圧倒的
- Free→Paid転換率4.8%で十分収益化

#### 2. SaaSサブスク + API従量のハイブリッド

**実践方法**:
- **OpenAIパターン**: ChatGPT Plus $20/月 + API従量課金
- **Perplexityパターン**: Pro $20/月 + API従量課金
- **個人向けSaaS**: $10-50/月、無制限または月間制限
- **開発者向けAPI**: $0.01/1K tokens〜、B2B収益

**判断基準**:
- 収益モデル: 個人向けSaaS + 開発者向けAPI
- 収益源の多様化: サブスク収益 + API収益
- B2B需要: 開発者、企業のカスタムユースケース

**効果**:
- 収益源の多様化、安定収益確保
- 個人向けSaaS + 開発者向けAPI、両市場攻略
- API収益でB2B市場開拓

#### 3. API料金シミュレーションの徹底

**実践方法**:
1. **1リクエストトークン数試算**: 入力 + 出力トークン、平均500トークン
2. **月間リクエスト数試算**: 1ユーザー平均100回/月
3. **1ユーザー月間コスト試算**: 100 × 500 / 1000 × $0.01 = $0.50
4. **推奨月額価格設定**: API料金の5倍以上、$2.99-$50/月
5. **利益率試算**: (月額価格 - API料金) / 月額価格、80%以上目標

**判断基準**:
- 利益率: 80%以上（健全）、90%以上（優秀）
- API料金の倍率: 5倍以上（最低）、10倍以上（推奨）
- 無制限プランのリスク: ヘビーユーザーで赤字回避

**効果**:
- 収益性の見極め、持続可能なビジネスモデル構築
- API料金転嫁100%回避、ユーザー離脱防止
- 無制限プランの赤字回避、月額$50以上または上限設定

#### 4. Free→Paid転換率3-5%の目標設定

**実践方法**:
1. **Free Tier設定**: 月間10-100リクエスト無料
2. **試用期間30日以上**: 十分な価値実感
3. **差別化明確化**: ChatGPT無料版との差、有料化理由明示
4. **Product Hunt #1獲得**: 初期ユーザー爆発的獲得

**判断基準**:
- Free→Paid転換率: 3-5%目標（ChatGPT 4.8%、Cursor 5.1%参考）
- Free Tier制限: 月間10-100リクエスト（バイラル成長とコスト抑制）
- 差別化明確性: 一文で説明可能、有料化理由明示

**効果**:
- Free→Paid転換率4.8%達成（ChatGPT参考）
- バイラル成長でCAC削減、転換率向上
- 差別化明確化で有料化理由納得感

#### 5. 価格設定根拠の明確化（GenAI特化）

**実践方法**:
1. **顧客価値ベース**: 顧客の得られる価値（時間削減、コスト削減）から価格設定
2. **競合比較ベース**: ChatGPT Plus $20/月、Jasper $49/月との比較、差別化ポイント明確化
3. **API料金コスト構造ベース**: API料金の5倍以上、利益率80%以上

**判断基準**:
- 顧客価値: 価格の10倍以上の価値提供（時間削減、コスト削減）
- 競合比較: ChatGPT Plus $20/月を上回る差別化ポイント
- API料金コスト: 利益率80%以上、API料金の5倍以上

**効果**:
- 価格設定の納得感、顧客満足度向上
- ChatGPT Plusとの差別化明確化
- API料金シミュレーションで収益性確保

### Reference

- **詳細事例**: @GenAI_research/case_studies/
- **収益モデル詳細**: @GenAI_research/case_studies/tier2/design-pricing/
- **API料金シミュレーション**: @GenAI_research/LLM/01_LifeisBeautiful_insights.md

---

## エラーハンドリング

このスキルは以下の標準パターンを使用します：

- **ファイル未検出**: @.claude/skills/_shared/error_handling_patterns.md#2-ファイル読み込み失敗
- **データ検証失敗**: @.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗スコア計算等
- **Human-in-the-Loop**: @.claude/skills/_shared/error_handling_patterns.md#6-human-in-the-loop-トリガー条件
- **標準エラーレスポンス**: @.claude/skills/_shared/error_handling_patterns.md#5-標準エラーレスポンス形式

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 60-90分

### 自動実行ステップ（ForGenAI調整版）

1. **入力ファイル読み込み**: lean_canvas.md, psf_diagnosis.md, competitor_research.md, ai_tech_stack_selection.md
2. **【NEW】GenAI Researchベンチマーク調査**: ChatGPT、Jasper、Midjourney、Perplexity、Cursor、Notion AI等の収益モデル事例
3. **収益モデル分類**: SaaS/API/Freemium/ハイブリッドの4類型から最適選択
4. **【NEW】Freemium戦略検討**: ChatGPTパターン（無料プラン + Plus $20/月）、Free→Paid転換率3-5%
5. **【NEW】SaaSサブスク設計**: Jasper $49/月パターン、Midjourney $10/月パターン
6. **【NEW】API従量課金設計**: OpenAI API $0.01/1K tokens、利益率5倍以上の設定
7. **【NEW】API料金シミュレーション**: 1ユーザー月間コスト試算、推奨価格設定
8. **Unit Economics試算**: LTV/CAC比、Churn率、継続期間、損益分岐点の計算
9. **価格設定根拠**: 顧客価値、競合比較、API料金コスト構造に基づく価格決定
10. **【NEW】GenAI Research事例との比較**: ChatGPT、Jasper、Midjourney等の収益モデルとのベンチマーク
11. **成果物出力**: pricing_strategy_forgenai.md

### 収益モデル4類型

| 収益モデル | 説明 | 代表製品 | ForGenAI適用度 |
|----------|------|---------|---------------|
| **Freemium（無料+有料）** | 無料プラン + 有料プラン | ChatGPT、Perplexity | 高（Free→Paid転換率3-5%） |
| **SaaSサブスク** | 月額/年額固定料金 | Jasper、Midjourney | 高（$10-60/月） |
| **API従量課金** | リクエスト数×料金 | OpenAI API | 中（B2B向け、$0.01/1K tokens） |
| **ハイブリッド（SaaS+API）** | サブスク + 従量課金 | Perplexity Pro + API | 高（個人SaaS + 開発者API） |

### API料金シミュレーション計算式

```markdown
## API料金シミュレーション

### 1ユーザー月間コスト試算

1リクエストトークン数 = [入力トークン] + [出力トークン] = [合計]トークン
月間リクエスト数 = [回/月]
月間トークン数 = [リクエスト数] × [1リクエストトークン数] = [合計]トークン
API料金 = [月間トークン数] / 1000 × $0.01 = $[コスト]/月

### 推奨月額価格設定

目標利益率 = 80%以上
推奨価格 = [API料金] × 5倍以上 = $[価格]/月

### 実例（ChatGPT想定）

1リクエストトークン数 = 300（入力） + 200（出力） = 500トークン
月間リクエスト数 = 100回/月
月間トークン数 = 100 × 500 = 50,000トークン
API料金 = 50,000 / 1000 × $0.01 = $0.50/月
推奨価格 = $0.50 × 5 = $2.50/月（最低）
実際価格 = $20/月（ChatGPT Plus、利益率97.5%）
```

### Unit Economics試算フォーマット

```markdown
## Unit Economics試算

### LTV（Life Time Value）計算

ARPU（月間平均収益/顧客） = [計算式]
継続期間（月） = [推定値]
Churn率（年間） = [推定値]

LTV = ARPU × 継続期間 × (1 - Churn率/12) = [計算結果]

### CAC（Customer Acquisition Cost）計算

営業費 = [推定値]
マーケティング費 = [推定値]
新規顧客数 = [推定値]

CAC = (営業費 + マーケティング費) / 新規顧客数 = [計算結果]

### LTV/CAC比

LTV/CAC比 = LTV / CAC = [計算結果]

**判定**:
- 5倍以上 → ✅ 健全
- 3-5倍 → ⚠️ 要改善
- 3倍未満 → ❌ 撤退検討

### Free→Paid転換率

Free Tierユーザー数 = [推定値]
有料転換ユーザー数 = [推定値]

Free→Paid転換率 = [有料転換ユーザー数] / [Free Tierユーザー数] × 100% = [計算結果]%

**判定**:
- 5%以上 → ✅ 優秀（Cursor 5.1%参考）
- 3-5% → ✅ 健全（ChatGPT 4.8%、Perplexity 3.2%参考）
- 3%未満 → ⚠️ 要改善

### 損益分岐点

固定費（月間） = [推定値]
ARPU = [推定値]
変動費（API料金/顧客） = [推定値]

損益分岐点（顧客数） = 固定費 / (ARPU - 変動費) = [計算結果]
損益分岐点到達時期 = [推定時期]

### GenAI Research事例との比較

| 製品名 | LTV/CAC比 | Churn率 | 継続期間 | 収益モデル | Free→Paid転換率 |
|--------|----------|---------|---------|----------|---------------|
| ChatGPT | 15-20倍 | 5-8% | 12-18ヶ月 | Freemium | 4.8% |
| Jasper | 10-15倍 | 10-15% | 10-12ヶ月 | SaaSサブスク | - |
| Midjourney | 20倍以上 | 8-12% | 12ヶ月 | SaaSサブスク | - |
| Perplexity | 12-18倍 | 10-12% | 12ヶ月 | Freemium | 3.2% |
| Cursor | 15倍以上 | 8% | 12ヶ月以上 | Freemium | 5.1% |
| Notion AI | 25倍以上 | 5% | 12ヶ月 | SaaSサブスク | 15-20% |
| 本製品 | [計算結果] | [推定値] | [推定値] | [収益モデル] | [計算結果] |
```

---

## 成果物フォーマット

### pricing_strategy_forgenai.md（ForGenAI調整版）

```markdown
# Pricing Strategy（ForGenAI Edition）

**作成日**: [YYYY-MM-DD]
**プロジェクト**: [プロジェクト名]
**収益モデル**: [収益モデル名]

---

## エグゼクティブサマリー

**収益モデル**: [Freemium/SaaSサブスク/API従量/ハイブリッド]
**目標LTV/CAC比**: [X倍]（ForGenAI基準5倍以上）
**目標Churn率**: [X%]（ForGenAI基準15%以下）
**Freemium採用**: [Yes/No]
**Free→Paid転換率目標**: [X%]（ForGenAI基準3-5%）

**GenAI Research事例との比較**:
- 本製品のLTV/CAC比: [X倍] vs ChatGPT 15-20倍、Jasper 10-15倍
- 本製品のChurn率: [X%] vs ChatGPT 5-8%、Perplexity 10-12%
- 本製品のFree→Paid転換率: [X%] vs ChatGPT 4.8%、Cursor 5.1%

---

## 収益モデル設計

### 主要収益源

**収益モデル**: [Freemium/SaaSサブスク/API従量/ハイブリッド]

**価格設定**:
- **Free Tier**: 月間[X]リクエスト無料
- **個人向けプラン**: $[価格]/月（月間[X]リクエストまたは無制限）
- **チーム向けプラン**: $[価格]/月/ユーザー（管理機能、優先サポート）
- **エンタープライズプラン**: カスタム価格（セキュリティ強化、カスタマイズ）
- **API従量課金**: $[価格]/1K tokens（開発者向け、B2B収益）

**価格設定根拠**:
1. **顧客価値ベース**: 顧客の得られる価値（時間削減、コスト削減）[X倍]円/月
2. **競合比較ベース**: ChatGPT Plus $20/月、Jasper $49/月との比較、差別化ポイント[10倍優位性のある軸]
3. **API料金コスト構造ベース**: API料金$[X]/月、推奨価格$[Y]/月（5倍以上、利益率80%）

### Freemium戦略検討（ForGenAI調整版）

**採用判断**: [Yes/No]

**ChatGPTパターン適用可能性**:
- Free Tier: 月間[X]リクエスト無料（バイラル成長）
- Plus $20/月: GPT-4o無制限（ChatGPT Plus同価格）
- Free→Paid転換率: [X%]目標（ChatGPT 4.8%、Cursor 5.1%参考）

**バイラル成長効果**:
- Free Tier設定: 月間[X]リクエスト無料
- CAC削減効果: 1/5〜1/10削減見込み（ChatGPT参考）
- Product Hunt #1獲得: 初期ユーザー爆発的獲得

### SaaSサブスク設計（ForGenAI調整版）

**サブスクプラン**: [有/無]

**Jasper $49/月パターン適用可能性**:
- 月額$49/月: 月間10万words制限（Jasper参考）
- 月額$125/月: 無制限（Jasper Boss Mode参考）
- 差別化ポイント: マーケター特化、テンプレートライブラリ

**Midjourney $10/月パターン適用可能性**:
- Basic $10/月: 月間200画像（Midjourney参考）
- Standard $30/月: 月間無制限（Midjourney参考）
- Pro $60/月: ステルスモード、商用利用（Midjourney参考）

### API従量課金設計（ForGenAI調整版）

**API従量課金**: [有/無]

**OpenAI API $0.01/1K tokensパターン適用可能性**:
- API料金: $0.01/1K tokens（OpenAI参考）
- 利益率: 5倍以上（推奨価格$0.05/1K tokens以上）
- B2B需要: 開発者、企業のカスタムユースケース

**API料金シミュレーション**:
```
1リクエストトークン数 = [入力] + [出力] = [合計]トークン
月間リクエスト数 = [回/月]
月間トークン数 = [リクエスト数] × [1リクエストトークン数] = [合計]トークン
API料金 = [月間トークン数] / 1000 × $0.01 = $[コスト]/月
推奨価格 = $[コスト] × 5倍以上 = $[価格]/月
利益率 = ([推奨価格] - [API料金]) / [推奨価格] = [X]%
```

### ハイブリッド戦略（SaaS + API）

**ハイブリッド計画**: [有/無]

**Perplexityパターン適用可能性**:
- 個人向けSaaS: Pro $20/月（無制限Pro検索、GPT-4o + Claude）
- 開発者向けAPI: 従量課金（$0.01/1K tokens〜）
- 収益源の多様化: サブスク収益 + API収益

**収益源の多様化効果**:
- 個人向けSaaS: $10-50/月、無制限または月間制限
- 開発者向けAPI: $0.01/1K tokens〜、B2B収益
- 両市場攻略: 個人ユーザー + 開発者、収益源の分散

---

## Unit Economics試算

[上記フォーマット参照]

---

## 価格戦略

### ターゲット別価格設定

**Free Tierユーザー向け**: 月間[X]リクエスト無料
**個人向け**: $[価格]/月
**チーム向け**: $[価格]/月/ユーザー
**エンタープライズ向け**: カスタム価格

### 価格変更戦略

**Product Huntローンチ特別価格**: Early Bird Discount 50% OFF
**Lifetime Deal（Product Hunt限定）**: $[価格]（生涯アクセス）
**Free Tier拡大**: ローンチ後3ヶ月、月間[X]リクエスト→[Y]リクエスト

### 競合比較（GenAI市場）

| ChatGPT Plus | Jasper AI | Perplexity Pro | 本製品 |
|-------------|----------|---------------|--------|
| $20/月 | $49/月 | $20/月 | $[価格]/月 |
| GPT-4o無制限 | 月間10万words | 無制限Pro検索 | [機能] |
| [差別化] | [差別化] | [差別化] | [差別化] |

---

## リスクと対策

**リスク1**: API料金シミュレーション不足で赤字
**対策**: 1ユーザー月間コスト試算、推奨価格API料金の5倍以上

**リスク2**: Free→Paid転換率3%未満
**対策**: Free Tier十分設定、試用期間30日以上、差別化明確化

**リスク3**: ChatGPT Plus $20/月との差別化不足
**対策**: 10倍優位性のある軸で差別化、Citation機能等の独自価値

---

## GenAI Research事例との比較

| 製品名 | 収益モデル | LTV/CAC比 | Churn率 | Free→Paid転換率 | 特徴 |
|--------|----------|----------|---------|---------------|------|
| ChatGPT | Freemium | 15-20倍 | 5-8% | 4.8% | 無料プラン + Plus $20/月、バイラル成長 |
| Jasper | SaaSサブスク | 10-15倍 | 10-15% | - | $49/月、マーケター特化 |
| Midjourney | SaaSサブスク | 20倍以上 | 8-12% | - | $10/月〜、Discord経由成長 |
| Perplexity | Freemium | 12-18倍 | 10-12% | 3.2% | Pro $20/月、Citation差別化 |
| Cursor | Freemium | 15倍以上 | 8% | 5.1% | $20/月、開発者特化 |
| Notion AI | SaaSサブスク | 25倍以上 | 5% | 15-20% | $10/月、既存ユーザー基盤活用 |
| 本製品 | [収益モデル] | [X倍] | [X%] | [X%] | [特徴] |

---

## 次のアクション

1. API料金シミュレーションの精緻化
2. Free Tier設定の顧客ヒアリング
3. ChatGPT Plus $20/月との差別化ポイント明確化
4. Product Hunt Early Bird Discount戦略策定
5. Free→Paid転換率3-5%達成施策検討
```

---

## ForGenAI Knowledge Base Reference

### 評価基準・フレームワーク
- CPF/PSF/PMF基準: @.claude/skills/_shared/knowledge_base.md#forgenai-evaluation
- Product Hunt戦略: @.claude/skills/_shared/knowledge_base.md#product-hunt-strategy
- AI技術スタック選定: @.claude/skills/_shared/knowledge_base.md#ai-tech-stack
- ForGenAI評価基準: @.claude/skills/_shared/knowledge_base.md#forgenai-evaluation

### 事例参照
- 成功パターン（Tier 2）: @GenAI_research/case_studies/tier2/design-pricing/
- ChatGPT収益モデル: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_001_chatgpt.md
- Jasper AI収益モデル: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_002_jasper.md
- Midjourney収益モデル: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_003_midjourney.md
- Perplexity AI収益モデル: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_004_perplexity.md
- Cursor収益モデル: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_005_cursor.md
- Notion AI収益モデル: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_006_notion_ai.md

### Tier 2 ケーススタディ（12件統合）

1. **ChatGPT** - Freemium + SaaSサブスクの成功
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_001_chatgpt.md
   - Free→Paid転換率4.8%、LTV/CAC比15-20倍、ARR $3B+

2. **Jasper AI** - マーケター特化$49/月の成功
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_002_jasper.md
   - ARR $75M、LTV/CAC比10-15倍、Product Hunt #2効果

3. **Midjourney** - Discord + $10/月の成功
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_003_midjourney.md
   - 月間売上$200M、LTV/CAC比20倍以上、バイラル成長

4. **Perplexity AI** - Pro $20/月 + Citation差別化
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_004_perplexity.md
   - Free→Paid転換率3.2%、Product Hunt #1獲得、ARR $20M

5. **Cursor** - 開発者特化、転換率5.1%の成功
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_005_cursor.md
   - Free→Paid転換率5.1%（GenAI最高クラス）、LTV/CAC比15倍以上

6. **Notion AI** - 既存ユーザー基盤活用$10/月
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_006_notion_ai.md
   - 既存ユーザー転換率15-20%、LTV/CAC比25倍以上

7. **GitHub Copilot** - 開発者向け$10/月
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_007_copilot.md
   - 10x developer productivity、VS Code統合

8. **Runway ML** - クリエイター特化動画生成
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_008_runway.md
   - $1.5B評価額、Discord/Slackコミュニティ

9. **ElevenLabs** - 音声合成、多言語対応
   - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_009_elevenlabs.md
   - 15言語以上対応、API提供でB2B収益化

10. **Grammarly AI** - 既存製品AI強化
    - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_010_grammarly.md
    - 30M DAU、ライティング支援特化

11. **Character.AI** - エンタメ特化$9.99/月
    - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_011_character_ai.md
    - 100M+ MAU、TikTokバイラル拡散

12. **Otter.ai** - 文字起こし、Zoom統合
    - 参照: @GenAI_research/case_studies/tier2/design-pricing/GENAI_PRICING_012_otter.md
    - リアルタイム処理、Zoom統合でCAC削減

### 全体参照
- ForGenAI全体概要: @.claude/skills/_shared/knowledge_base.md#forgenai-edition
- Product Hunt戦略: @.claude/skills/_shared/knowledge_base.md#product-hunt-strategy
- AI技術スタック選定基準: @.claude/skills/_shared/knowledge_base.md#ai-tech-stack

---
## 使用例

```
User: /design-pricing-for-genai

Skill:
# Pricing Strategy設計 自律実行開始（ForGenAI Edition）

入力ファイル読み込み中...
- lean_canvas.md ✅
- psf_diagnosis.md ✅
- competitor_research.md ✅
- ai_tech_stack_selection.md ✅

[自動生成中...]
- STEP 1: 入力ファイル読み込み ✅
- STEP 2: GenAI Researchベンチマーク調査 ✅（ChatGPT、Jasper、Midjourney、Perplexity、Cursor、Notion AI）
- STEP 3: 収益モデル分類 ✅（Freemium + SaaSサブスク）
- STEP 4: Freemium戦略検討 ✅（月間100リクエスト無料、Plus $20/月）
- STEP 5: SaaSサブスク設計 ✅（個人$20/月、チーム$25/月/ユーザー）
- STEP 6: API従量課金設計 ✅（$0.01/1K tokens、利益率5倍）
- STEP 7: API料金シミュレーション ✅（1ユーザー月間コスト$0.50、推奨価格$20/月）
- STEP 8: Unit Economics試算 ✅（LTV/CAC比18倍、Churn率6%、Free→Paid転換率4.5%）
- STEP 9: 価格設定根拠 ✅（顧客価値・ChatGPT Plus比較・API料金）
- STEP 10: GenAI Research事例との比較 ✅
- STEP 11: 成果物出力 ✅

## 完了

成果物: pricing_strategy_forgenai.md

Unit Economics試算結果:
- LTV/CAC比: 18倍 ✅（ForGenAI基準5倍以上超過、ChatGPT 15-20倍に匹敵）
- Churn率: 6% ✅（ForGenAI基準15%以下クリア、ChatGPT 5-8%に近い）
- 継続期間: 14ヶ月（ChatGPT 12-18ヶ月参考）
- Free→Paid転換率: 4.5% ✅（ChatGPT 4.8%、Cursor 5.1%に匹敵）

収益モデル:
- 主要収益源: Freemium（無料プラン + Plus $20/月）
- Free Tier: 月間100リクエスト無料（バイラル成長）
- SaaSサブスク: Plus $20/月（ChatGPT Plus同価格）
- API従量課金: $0.01/1K tokens（開発者向け、利益率5倍）

API料金シミュレーション:
- 1ユーザー月間コスト: $0.50（100リクエスト × 500トークン × $0.01/1K）
- 推奨価格: $20/月（API料金の40倍、利益率97.5%）
- 無制限プランのリスク: ヘビーユーザーで月$5コスト、$20/月で十分利益確保

GenAI Research事例との比較:
- 本製品のLTV/CAC比: 18倍 vs ChatGPT 15-20倍、Jasper 10-15倍
- 本製品のChurn率: 6% vs ChatGPT 5-8%、Perplexity 10-12%
- 本製品のFree→Paid転換率: 4.5% vs ChatGPT 4.8%、Cursor 5.1%
- Freemium採用: ChatGPTパターンに準拠、バイラル成長戦略

推奨: Unit Economics健全、Product Hunt準備可能
```

---

## 注意事項

1. **Freemium優先検討**: ChatGPTパターン（無料プラン + Plus $20/月、Free→Paid転換率4.8%）
2. **API料金シミュレーション必須**: 1ユーザー月間コスト試算、推奨価格API料金の5倍以上
3. **Free→Paid転換率3-5%目標**: ChatGPT 4.8%、Cursor 5.1%、Perplexity 3.2%参考
4. **Unit Economics厳密計算**: LTV/CAC比5倍以上、Churn率15%以下
5. **ChatGPT Plus $20/月との差別化**: 10倍優位性のある軸で差別化、Citation機能等
6. **Product Hunt Early Bird Discount**: ローンチ時50% OFF、Lifetime Deal検討

---

## 更新履歴

- 2026-01-03: ForGenAI特化版として作成、GenAI Research統合（12事例）

---

**テンプレートバージョン**: v1.0-ForGenAI
**最終更新**: 2026-01-03
**作成者**: Claude Code
**ForGenAI特化要素**: Freemium戦略、API料金シミュレーション、Free→Paid転換率、12事例統合
