---
name: pivot-decision
description: |
  PMF未達成時のピボット判断を体系的に実施。5つのピボット種類（Zoom In/Out、Customer Segment、Problem、Technology）から最適な方向性を選定し、**AI技術スタック変更（OpenAI→Anthropic→Gemini）、垂直特化戦略、API vs UI選択**などGenAI製品特有のピボット要素を統合評価します。

  【ForGenAI版の特徴】
  - AI製品特有のピボット選択肢追加（モデル選択、垂直特化、API/UI戦略）
  - Slack/Instagram/Perplexity/Cursor等の成功ピボット事例統合
  - モデルコモディティ化時代のピボット戦略（差別化ポイントの移動）
  - GenAI_research統合（SaaS置換、Move 37的ブレイクスルー）

  使用タイミング：
  - PMF未達成判明時（`/validate-pmf` で❌判定）
  - 3ヶ月連続で改善が見られない時
  - AI精度95%達成が技術的に困難な時
  - モデルコモディティ化で差別化困難な時
  - ランウェイ6ヶ月以上ある時（ピボット実行余力）

  所要時間：60-90分（ピボット戦略策定含む）
  出力：ピボット判断レポート、実行プラン、リスク分析

trigger_keywords:
  - "ピボット検討"
  - "ピボット判断"
  - "方向転換"
  - "PMF未達成"
  - "戦略変更"
  - "AI技術スタック変更"
  - "垂直特化検討"

stage: Phase2（PMF検証）→ Pivot Phase
dependencies:
  - validate-pmf（PMF未達成判定が前提）
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/pivot_decision_forgenai.md
execution_time: 60-90分
framework_reference: Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
priority: P1
framework_compliance: 100%
domain: ForGenAI
---

# Pivot Decision Skill (ForGenAI版)

起業の科学の5つのピボット種類に加え、**GenAI製品特有のピボット選択肢（AI技術スタック変更、垂直特化戦略、API vs UI戦略、オープンソース vs クローズド）**を統合した自律実行型Skill。

**ForGenAI版の強化点**：
- AI製品特有ピボット選択肢追加（モデル選択、垂直特化、API/UI、B2B/B2C）
- Slack/Instagram/Perplexity/Cursor/Anthropic等の成功ピボット事例統合
- モデルコモディティ化時代のピボット戦略（競争軸の移動: モデル性能→配布・運用）
- GenAI_research統合（SaaS置換トレンド、Move 37的ブレイクスルー期待）

---

## このSkillでできること

1. **5つのピボット種類の体系的評価**: Zoom In/Out、Customer Segment、Problem、Technology Pivot
2. **AI製品特有ピボット選択肢**: モデル選択、垂直特化、API vs UI、B2B vs B2C
3. **成功ピボット事例ベンチマーク**: Slack/Instagram/Perplexity/Cursor/Anthropic等12事例統合
4. **ピボット実行可能性判定**: ランウェイ、チームスキル、市場機会の3軸評価
5. **リスク分析と軽減策**: ピボット失敗パターンと回避策
6. **実行プラン自動生成**: 3ヶ月ピボットロードマップ、マイルストーン設定

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `pmf_diagnosis_forgenai.md`（PMF未達成診断）, 財務データ, チームスキルマップ, 市場分析 |
| **出力** | `Flow/{YYYYMM}/{YYYY-MM-DD}/pivot_decision_forgenai.md` |
| **次のSkill** | `/select-ai-tech-stack`（Technology Pivot時）→ `/discover-demand`（Problem Pivot時） |
| **ステージ** | Pivot Phase → Phase1（再発見） or Phase2（再検証） |

---

## Knowledge Base参照

### 起業の科学ナレッジ
- Pivot概念: `startup_science/01_stages/pivot/pivot_overview.md`
- Zoom In/Out Pivot: `startup_science/01_stages/pivot/zoom_pivots.md`
- Customer Segment Pivot: `startup_science/01_stages/pivot/customer_pivot.md`
- Problem Pivot: `startup_science/01_stages/pivot/problem_pivot.md`
- Technology Pivot: `startup_science/01_stages/pivot/technology_pivot.md`

### ForGenAI専用ナレッジ（GenAI_research統合）

#### GenAI市場トレンド（ピボット判断に影響）
- **モデルコモディティ化**: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`
  - モデル性能から配布・統合・運用へ競争軸が移動
  - 差別化ポイント: UI/ワークフロー/データ/セキュリティ
  - ピボット戦略: モデル性能競争から運用最適化へ
- **SaaS置換トレンド**: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`
  - 従来SaaSのUI/ビジネスロジックが自然言語＋エージェントで置換
  - ピボット機会: SaaS特化AI（会計AI、営業AI、HR AI等）
- **Move 37的ブレイクスルー**: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`
  - 強化学習による「考える力」獲得
  - ピボット戦略: 汎用AI → 垂直特化AI（数学、医学、法律等で創造的発見）

#### Tier 2: 成功ピボット事例（12ケーススタディ）

**Zoom In Pivot（特定機能に特化）**:

- **[Perplexity - 汎用AI → 検索特化AI]**: `@GenAI_research/case_studies/tier2/perplexity_pivot.md`
  - **Before**: 汎用対話AI（ChatGPT競合）
  - **After**: AI検索エンジン（Google競合）
  - **Pivot理由**: ChatGPT との差別化困難、検索市場の巨大性
  - **成果**: Sean Ellis 55%、月次成長率25-35%、AI精度98%（検索特化）
  - **キーアクション**: 引用機能追加、ファクトチェック強化、検索UI最適化
  - **活用**: 汎用AI市場での苦戦 → 垂直特化で差別化

- **[Cursor - 汎用コーディングAI → VSCode統合IDE]**: `@GenAI_research/case_studies/tier2/cursor_pivot.md`
  - **Before**: ブラウザベースAIコーディングツール
  - **After**: VSCode互換IDE with AI（開発者ワークフロー統合）
  - **Pivot理由**: ブラウザツールは採用障壁高い、VSCode移行コスト削減
  - **成果**: Sean Ellis 65%、月次成長率40-50%、Churn Rate 2.5%
  - **キーアクション**: VSCodeフォーク、拡張機能互換、ショートカット継承
  - **活用**: ワークフロー統合の重要性、既存ツール置き換えの摩擦削減

- **[Jasper AI - 汎用ライティング → マーケティングコピー特化]**: `@GenAI_research/case_studies/tier2/jasper_pivot.md`
  - **Before**: 汎用AIライティングツール
  - **After**: マーケティングコピーライター（広告/LP/メール特化）
  - **Pivot理由**: 汎用市場でChatGPTと競合、マーケター高ARPU狙い
  - **成果**: エンタープライズARPU $250/月、月次成長率20-25%
  - **キーアクション**: テンプレート100+追加、ブランドトーン機能、A/Bテスト統合
  - **活用**: 高ARPU顧客セグメント特化、テンプレート戦略

**Zoom Out Pivot（より大きな課題へ拡大）**:

- **[OpenAI - GPT-3 API → ChatGPT（開発者 → 一般消費者）]**: `@GenAI_research/case_studies/tier2/openai_pivot.md`
  - **Before**: GPT-3 API（開発者向けAPI）
  - **After**: ChatGPT（一般消費者向けUI）
  - **Pivot理由**: API市場は成長遅い、一般消費者市場の巨大性
  - **成果**: 2ヶ月で1億ユーザー（史上最速）、月次成長率30-40%
  - **キーアクション**: UI開発（プロンプトベース）、Freemium戦略、ブランディング
  - **活用**: API → UI戦略、B2D（Developer）→ B2C戦略

- **[Character.AI - チャットボット → キャラクターIP Platform]**: `@GenAI_research/case_studies/tier2/characterai_pivot.md`
  - **Before**: 汎用AIチャットボット
  - **After**: キャラクターIP × AIチャット（エンタメ特化）
  - **Pivot理由**: 汎用チャットはChatGPTが独占、エンタメ市場未開拓
  - **成果**: 月次成長率50-60%、DAU/MAU 0.55（最高水準）、平均セッション28分
  - **キーアクション**: キャラクター作成機能、IP連携、若年層マーケティング
  - **活用**: エンタメ特化戦略、高エンゲージメント設計

**Customer Segment Pivot（ターゲット顧客変更）**:

- **[Anthropic - 研究機関 → Claude Pro（企業/個人ユーザー）]**: `@GenAI_research/case_studies/tier2/anthropic_pivot.md`
  - **Before**: AI安全性研究機関（論文発表中心）
  - **After**: Claude Pro（企業/個人向けAI製品）
  - **Pivot理由**: 研究だけでは収益化困難、商用市場の巨大性
  - **成果**: 企業利用率45%（vs ChatGPT 35%）、ハルシネーション率2%（業界最低）
  - **キーアクション**: 安全性訴求、長文処理特化、企業向け機能（SSO、監査ログ）
  - **活用**: 研究 → 商用化戦略、安全性の差別化

- **[GitHub Copilot - 個人開発者 → エンタープライズ]**: `@GenAI_research/case_studies/tier2/copilot_pivot.md`
  - **Before**: 個人開発者向けAIコーディングツール
  - **After**: エンタープライズ向けAI開発プラットフォーム
  - **Pivot理由**: 個人ARPU低い（$10/月）、企業ARPU高い（$19/月/ユーザー）
  - **成果**: 企業導入率60%（Fortune 500）、ROI 平均3.5倍
  - **キーアクション**: セキュリティ強化、IP保護、組織管理機能、コンプライアンス対応
  - **活用**: B2C → B2B戦略、エンタープライズ営業

- **[Runway ML - プロクリエイター → 一般ユーザー]**: `@GenAI_research/case_studies/tier2/runway_pivot.md`
  - **Before**: プロ向け動画生成ツール（高機能・複雑）
  - **After**: 一般ユーザー向けAI動画生成（シンプル化）
  - **Pivot理由**: プロ市場は小さい、一般ユーザー市場の巨大性
  - **成果**: 月次成長率25-30%、ユーザー10倍増加
  - **キーアクション**: UI簡素化、テンプレート追加、プロンプト簡略化
  - **活用**: プロ → 一般化戦略、UIシンプル化

**Problem Pivot（解決する課題変更）**:

- **[Slack - ゲーム → チームコミュニケーション]**: `@GenAI_research/case_studies/tier2/slack_pivot.md`
  - **Before**: Glitch（オンラインゲーム）
  - **After**: Slack（チームコミュニケーション）
  - **Pivot理由**: ゲーム失敗、開発中の内部ツールが好評
  - **成果**: Sean Ellis推定55%+、NPS推定65+、2014年上場
  - **キーアクション**: ゲーム開発中止、内部ツール製品化、ボトムアップ営業
  - **活用**: 失敗から学ぶ（内部ツールを製品化）、Problem Pivot成功例

- **[Instagram - チェックイン → 写真共有]**: `@GenAI_research/case_studies/tier2/instagram_pivot.md`
  - **Before**: Burbn（位置情報チェックインアプリ）
  - **After**: Instagram（写真共有特化）
  - **Pivot理由**: Foursquare等の競合多数、写真機能のみが好評
  - **成果**: 1年で1,000万ユーザー、2012年Facebook $1B買収
  - **キーアクション**: 位置情報機能削除、写真フィルター追加、シンプル化
  - **活用**: Zoom In Pivot（特定機能に特化）、機能削減の勇気

- **[Flickr - ゲーム → 写真共有]**: `@GenAI_research/case_studies/tier2/flickr_pivot.md`
  - **Before**: Game Neverending（オンラインゲーム）
  - **After**: Flickr（写真共有コミュニティ）
  - **Pivot理由**: ゲーム失敗、写真共有機能のみが好評
  - **成果**: 2005年Yahoo買収、初期Web2.0成功事例
  - **キーアクション**: ゲーム開発中止、写真共有特化、コミュニティ機能強化
  - **活用**: Stewart Butterfield（Slack創業者）の1回目Pivot成功例

**Technology Pivot（技術スタック変更）**:

- **[Replicate - 自社モデル → マルチモデルAPI]**: `@GenAI_research/case_studies/tier2/replicate_pivot.md`
  - **Before**: 自社開発AIモデル（特定用途）
  - **After**: マルチモデルAPIプラットフォーム（Stable Diffusion/LLaMA等）
  - **Pivot理由**: 自社モデルは競争力不足、オープンソースモデル急増
  - **成果**: 月次成長率30-35%、API呼び出し成長率45%/月
  - **キーアクション**: 自社モデル開発中止、オープンソースモデル統合、API最適化
  - **活用**: モデルコモディティ化対応、プラットフォーム戦略

- **[Hugging Face - 自社モデル → コミュニティプラットフォーム]**: `@GenAI_research/case_studies/tier2/huggingface_pivot.md`
  - **Before**: チャットボットモデル開発
  - **After**: AIモデル共有コミュニティプラットフォーム
  - **Pivot理由**: 自社モデルは競争力不足、研究者コミュニティ需要大
  - **成果**: コミュニティ500万+ユーザー、モデルダウンロード10億+/月
  - **キーアクション**: 自社モデル開発中止、GitHub for AI Models構築、オープンソース重視
  - **活用**: コミュニティドリブン戦略、プラットフォーム化

- **[Midjourney - Text-to-Image → Discord中心UI]**: `@GenAI_research/case_studies/tier2/midjourney_pivot.md`
  - **Before**: Webブラウザベース画像生成ツール
  - **After**: Discord中心の画像生成コミュニティ
  - **Pivot理由**: WebUIは採用障壁高い、Discordはコミュニティ構築に最適
  - **成果**: Discord MAU 200万+、NPS 65、月次成長率35-45%
  - **キーアクション**: WebUI開発中止、Discord Bot開発、コミュニティ運営注力
  - **活用**: UI戦略の大胆な転換、コミュニティファースト

---

## 5つのピボット種類（ForGenAI版）

### 1. Zoom In Pivot（特定機能に特化）

**定義**: 既存製品の一部機能のみに特化し、他機能を削除

**AI製品での適用**:
- 汎用AI → 垂直特化AI（検索、コーディング、ライティング、画像生成等）
- 全機能AI → 単一タスクAI（Perplexity式の検索特化）

**判断基準**:
- 全機能のうち1つだけが明確に高評価（Sean Ellis 60%+ vs 他30%）
- 特定機能のNPS 70+ vs 他 40
- 特定機能の利用率80%+ vs 他 20%以下

**成功条件**:
- 特化機能で10x優位性達成（Cursor: 開発速度2.5倍、Perplexity: 検索精度98%）
- 競合が特化していない市場（汎用AI市場は既にChatGPTが独占）
- チームに特化領域の深い知見（Perplexity: Google出身）

**リスク**:
- 市場規模縮小（特化しすぎて顧客数激減）
- 特化機能が差別化にならない

**ForGenAI特有の考慮点**:
- モデルコモディティ化時代は「何をするか」より「誰に対して」が重要
- 垂直特化 = 高ARPU（Jasper: $250/月 vs ChatGPT: $20/月）

**ケーススタディ参照**:
- Perplexity: 汎用AI → 検索特化（Sean Ellis 55%、AI精度98%）
- Cursor: 汎用コーディング → VSCode統合IDE（Sean Ellis 65%、Churn 2.5%）
- Jasper: 汎用ライティング → マーケティングコピー（ARPU $250/月）

---

### 2. Zoom Out Pivot（より大きな課題へ拡大）

**定義**: 既存製品の一部だった機能を、より大きな製品・プラットフォームへ拡張

**AI製品での適用**:
- API → UI（OpenAI: GPT-3 API → ChatGPT）
- 単一AI → AIプラットフォーム（Character.AI: チャットボット → キャラクターIP Platform）
- B2D（Developer）→ B2C（一般消費者）

**判断基準**:
- 現在の市場規模が小さすぎ（API市場 < UI市場 10倍）
- より大きな顧客セグメントへの需要確認（開発者 vs 一般消費者）
- チームにUI/UX/マーケティング能力がある

**成功条件**:
- 大きな市場で差別化可能（OpenAI: ChatGPTで一般消費者市場独占）
- UI/UXで10x優位性（プロンプトベースの自然言語UI）
- ブランディング能力（「AI = ChatGPT」のイメージ確立）

**リスク**:
- 大市場での競争激化（既存大手との戦い）
- チームスキル不足（API開発 ≠ UI/UX設計）

**ForGenAI特有の考慮点**:
- API → UI は高リスク・高リターン（OpenAI成功、多数失敗）
- B2D → B2C は顧客獲得コスト10倍（CAC $100 → $10へ改善可能性）

**ケーススタディ参照**:
- OpenAI: GPT-3 API → ChatGPT（2ヶ月で1億ユーザー、史上最速）
- Character.AI: チャットボット → キャラクターIP Platform（DAU/MAU 0.55、セッション28分）

---

### 3. Customer Segment Pivot（ターゲット顧客変更）

**定義**: 同じ製品で、異なる顧客セグメントをターゲット

**AI製品での適用**:
- 研究機関 → 企業/個人（Anthropic: 研究 → Claude Pro）
- 個人 → エンタープライズ（GitHub Copilot: $10/月 → $19/月/ユーザー）
- プロ → 一般ユーザー（Runway ML: プロクリエイター → 一般ユーザー）
- B2C → B2B or 逆

**判断基準**:
- 現在の顧客セグメントでARPU低すぎ（個人 $10/月 vs 企業 $100/月）
- 別セグメントから強い引き合い（企業からの問い合わせ殺到）
- 別セグメントの市場規模が10倍以上

**成功条件**:
- 新セグメントで10x優位性達成（Anthropic: 安全性、GitHub: セキュリティ）
- 新セグメント向け機能追加可能（SSO、監査ログ、IP保護等）
- 営業チャネル構築能力（B2B営業、エンタープライズ対応）

**リスク**:
- 既存顧客離脱（個人ユーザー → 企業特化で個人が離脱）
- 新セグメントの獲得コスト高すぎ（B2B営業の長期化）

**ForGenAI特有の考慮点**:
- B2C → B2B: ARPU 10倍、営業コスト10倍（トレードオフ）
- 企業向け = 安全性・コンプライアンス必須（Anthropic式）

**ケーススタディ参照**:
- Anthropic: 研究機関 → Claude Pro（企業利用率45%、ハルシネーション率2%）
- GitHub Copilot: 個人開発者 → エンタープライズ（企業導入率60%、ROI 3.5倍）
- Runway ML: プロクリエイター → 一般ユーザー（ユーザー10倍増加）

---

### 4. Problem Pivot（解決する課題変更）

**定義**: 全く異なる課題を解決する製品へ転換

**AI製品での適用**:
- ゲーム → コミュニケーション（Slack: Glitch → Slack）
- チェックイン → 写真共有（Instagram: Burbn → Instagram）
- ゲーム → 写真共有（Flickr: Game Neverending → Flickr）

**判断基準**:
- 現在の課題で全く成果なし（PMF未達成、成長率 < 5%、Churn > 10%）
- 別の課題で強い引き合い（内部ツールが好評、特定機能のみ高評価）
- チームに新課題の知見あり

**成功条件**:
- 新課題で明確な需要確認（顧客インタビュー100人以上）
- 新課題でCPFスコア70%+達成
- チームが新課題に情熱を持つ（長期コミットメント）

**リスク**:
- 完全なやり直し（既存顧客・コード・ブランド放棄）
- チームの疲弊（モチベーション低下）
- ランウェイ不足（Pivot後の成長時間確保できず）

**ForGenAI特有の考慮点**:
- AI技術は汎用的（Problem Pivotでも技術資産は活用可能）
- 失敗から学ぶ（Slack/Flickr: 内部ツールを製品化）

**ケーススタディ参照**:
- Slack: ゲーム → チームコミュニケーション（Sean Ellis 55%+、NPS 65+、上場成功）
- Instagram: チェックイン → 写真共有（1年で1,000万ユーザー、$1B買収）
- Flickr: ゲーム → 写真共有（Yahoo買収、Web2.0成功事例）

---

### 5. Technology Pivot（技術スタック変更）

**定義**: 同じ課題を異なる技術で解決

**AI製品での適用**:
- OpenAI → Anthropic → Gemini（モデル変更）
- 自社モデル → オープンソースモデル（Replicate/Hugging Face）
- WebUI → Discord（Midjourney）
- クローズドソース → オープンソース

**判断基準**:
- 現在の技術で競争力不足（自社モデル vs OpenAI/Anthropicモデル）
- 別技術で10x改善可能（AI精度、コスト、速度）
- モデルコモディティ化で差別化困難

**成功条件**:
- 新技術でAI精度95%+達成（現在 < 90%）
- 新技術でコスト1/10削減（API料金削減）
- 新技術で応答速度3秒以下達成（現在 > 5秒）

**リスク**:
- 技術移行コスト高すぎ（全コード書き換え）
- 新技術の学習コスト（チームスキル不足）
- ベンダーロックイン（OpenAI依存 → Anthropic依存）

**ForGenAI特有の考慮点**:
- モデル選択は戦略的意思決定（OpenAI $0.03/1K vs Anthropic $0.015/1K）
- オープンソースモデル急成長（Llama 3, Mistral等）
- プラットフォーム戦略（自社モデル開発 vs マルチモデルAPI）

**ケーススタディ参照**:
- Replicate: 自社モデル → マルチモデルAPI（API呼び出し成長率45%/月）
- Hugging Face: 自社モデル → コミュニティプラットフォーム（500万+ユーザー、10億+ダウンロード）
- Midjourney: WebUI → Discord（Discord MAU 200万+、NPS 65）

---

## ピボット判断フレームワーク

### STEP 1: ピボット必要性判定

**必須条件チェック**:
- [ ] PMF未達成（`/validate-pmf` で❌判定）
- [ ] 3ヶ月連続で改善なし（Sean Ellis < 30%、成長率 < 5%、Churn > 10%）
- [ ] AI精度95%達成が技術的に困難（現在 < 85%、改善見込みなし）
- [ ] モデルコモディティ化で差別化困難（競合と同等性能、価格競争のみ）
- [ ] ランウェイ6ヶ月以上（Pivot実行・検証の時間確保）

**ピボット不要の場合**:
- 改善余地あり（Sean Ellis 30-39%、成長率 5-14%）
- AI精度向上中（月次 +2-3%改善）
- ランウェイ < 6ヶ月（改善施策に集中すべき）

**ピボット必要の場合** → STEP 2へ

---

### STEP 2: 5つのピボット種類の評価

**各ピボット種類のスコアリング（100点満点）**:

| ピボット種類 | 市場機会（40点） | 実行可能性（30点） | チーム適合性（30点） | 合計 |
|------------|----------------|-----------------|-------------------|------|
| Zoom In Pivot | [評価] | [評価] | [評価] | [合計] |
| Zoom Out Pivot | [評価] | [評価] | [評価] | [合計] |
| Customer Segment Pivot | [評価] | [評価] | [評価] | [合計] |
| Problem Pivot | [評価] | [評価] | [評価] | [合計] |
| Technology Pivot | [評価] | [評価] | [評価] | [合計] |

**市場機会（40点）**:
- 市場規模: 20点（$1B+ = 20点、$100M-1B = 15点、< $100M = 5点）
- 競争状況: 10点（競合なし = 10点、競合1-2社 = 7点、レッドオーシャン = 3点）
- 成長率: 10点（年次50%+ = 10点、20-49% = 7点、< 20% = 3点）

**実行可能性（30点）**:
- 技術的実現性: 15点（既存技術活用可 = 15点、一部新技術 = 10点、全面刷新 = 3点）
- ランウェイ: 10点（12ヶ月以上 = 10点、6-11ヶ月 = 7点、< 6ヶ月 = 0点）
- リソース: 5点（十分 = 5点、不足だが調達可 = 3点、不足 = 0点）

**チーム適合性（30点）**:
- スキル適合: 15点（既存スキルで対応可 = 15点、学習必要 = 10点、採用必要 = 5点）
- 情熱: 10点（チーム全員熱狂 = 10点、半数賛成 = 5点、反対多数 = 0点）
- 実績: 5点（類似経験あり = 5点、なし = 0点）

**判定**:
- 80点以上 → ✅ 推奨ピボット（実行すべき）
- 60-79点 → ⚠️ 要検討ピボット（リスク軽減後に実行）
- < 60点 → ❌ 非推奨ピボット（別のピボット種類を検討）

---

### STEP 3: AI製品特有の追加評価

**モデル選択評価**:

| モデル | AI精度 | コスト（/1K tokens） | 応答速度 | ハルシネーション率 | 推奨用途 |
|--------|--------|---------------------|----------|-------------------|---------|
| **OpenAI GPT-4** | 95%+ | $0.03 | 2.8秒 | 3% | 汎用対話、コーディング |
| **Anthropic Claude** | 96% | $0.015 | 2.6秒 | 2%（最低） | 長文処理、企業向け（安全性重視） |
| **Google Gemini** | 94% | $0.0007-0.002 | 3.2秒 | 4% | コスト重視、大量処理 |
| **Llama 3（OSS）** | 90% | 自社運用（GPU代のみ） | 2.0秒（最適化次第） | 5% | オンプレ、カスタマイズ重視 |

**Technology Pivot時の選択基準**:
- AI精度重視 → Anthropic Claude（96%、ハルシネーション2%）
- コスト重視 → Google Gemini（$0.0007/1K、OpenAIの1/40）
- 速度重視 → Llama 3（自社最適化で2秒以下可能）
- 企業向け → Anthropic Claude（安全性、長文処理）
- 汎用対話 → OpenAI GPT-4（ブランド認知、エコシステム）

**垂直特化 vs 汎用化評価**:

| 戦略 | 市場規模 | 差別化 | ARPU | 成功事例 | 推奨条件 |
|------|---------|--------|------|---------|---------|
| **垂直特化** | 小（$100M-1B） | 高（10x優位性） | 高（$100-500/月） | Cursor, Perplexity, Jasper | 汎用市場で苦戦、深い業界知見あり |
| **汎用化** | 大（$10B+） | 低（ChatGPT独占） | 低（$20/月） | ChatGPT, Claude | ブランド力あり、資金潤沢 |

**Zoom In Pivot（垂直特化）推奨条件**:
- 汎用AIでSean Ellis < 30%（差別化困難）
- 特定機能でSean Ellis 60%+（明確な強み）
- チームに業界知見（Perplexity: Google出身、Cursor: IDE開発経験）
- 高ARPU狙い（Jasper: $250/月、Cursor: $20/月 → 将来$100/月想定）

**API vs UI戦略評価**:

| 戦略 | 顧客セグメント | CAC | ARPU | 成長速度 | 成功事例 | 推奨条件 |
|------|--------------|-----|------|---------|---------|---------|
| **API First** | 開発者 | 低（$10-50） | 高（$100-1,000/月） | 遅（10-15%/月） | Replicate, Hugging Face | 技術力高い、開発者コミュニティあり |
| **UI First** | 一般消費者 | 高（$50-200） | 低（$10-50/月） | 速（30-50%/月） | ChatGPT, Midjourney | ブランディング能力、UI/UX強い |

**Zoom Out Pivot（API → UI）推奨条件**:
- API市場で成長鈍化（月次成長率 < 10%）
- UI需要確認（消費者からの問い合わせ多数）
- チームにUI/UX能力（デザイナー、フロントエンド開発者）
- 資金潤沢（UI開発・マーケティング費用確保）

---

### STEP 4: リスク分析と軽減策

**ピボット失敗パターン（回避すべき）**:

| 失敗パターン | 症状 | 原因 | 回避策 |
|------------|------|------|-------|
| **連続ピボット** | 6ヶ月に3回以上Pivot | 戦略不明確、焦り | 1Pivot = 3ヶ月検証期間設定、焦らず |
| **ランウェイ枯渇** | Pivot中に資金枯渇 | 資金計画甘い | Pivot前に6ヶ月以上ランウェイ確保必須 |
| **チーム分裂** | Pivot方向性で対立 | 全員合意なし | Pivot前にチーム全員で議論・合意形成 |
| **顧客ゼロ化** | Pivot後に既存顧客全離脱 | 顧客ヒアリングなし | Pivot前に既存顧客10人以上ヒアリング |
| **技術負債** | Pivot後に技術的実現不可 | 技術検証不足 | Pivot前にPoC実施（1-2週間） |

**リスク軽減策（Pivot前に実施）**:

1. **顧客ヒアリング（100人）**:
   - 既存顧客: 50人（Pivot後も使うか確認）
   - 新ターゲット: 50人（Pivot後の需要確認）
   - CPFスコア70%+達成を確認

2. **PoC（Proof of Concept）実施（1-2週間）**:
   - 技術的実現性確認（AI精度95%達成可能か）
   - コスト試算（API料金、インフラ費用）
   - 応答速度確認（3秒以下達成可能か）

3. **資金計画見直し**:
   - Pivot後6ヶ月のランウェイ確保
   - 必要に応じてSeed追加調達
   - コスト削減（人件費見直し）

4. **チーム合意形成**:
   - Pivot方向性を全員で議論（1週間）
   - 全員が納得する選択肢選定
   - 反対者がいる場合は再検討

5. **競合分析**:
   - Pivot先の市場で競合10社分析
   - 差別化ポイント明確化（10x優位性）
   - 競合のPMF達成状況確認

---

### STEP 5: ピボット実行プラン策定（3ヶ月）

**Month 1: Pivot準備・PoC**

**Week 1-2: PoC実施**
- 技術検証（AI精度、応答速度、コスト）
- UI/UXプロトタイプ作成
- 顧客ヒアリング10人（新ターゲット）

**Week 3-4: MVP開発**
- コア機能実装（最小限）
- AI精度95%達成確認
- 応答速度3秒以下達成確認

**Month 2: MVP検証・改善**

**Week 5-6: 初期ユーザー獲得（30人）**
- ターゲット顧客にMVP提供
- フィードバック収集（毎日）
- CPFスコア70%+達成確認

**Week 7-8: PSF検証**
- `/validate-psf` 実施
- AI精度・応答速度の改善
- UI/UX改善（ユーザーフィードバック反映）

**Month 3: PMF検証・Product Hunt準備**

**Week 9-10: PMF検証**
- `/validate-pmf` 実施（基本4指標 + AI指標）
- Sean Ellis 40%+達成確認
- 月次成長率15%+達成確認

**Week 11-12: Product Hunt準備 or 次のPivot判断**
- PMF達成 → `/create-producthunt-strategy`
- PMF未達成 → Pivot継続 or 次のPivot種類検討

**マイルストーン**:
- Week 2: PoC完了（技術的実現性確認）
- Week 4: MVP完成（コア機能動作）
- Week 6: 初期ユーザー30人獲得
- Week 8: PSF達成（CPF 70%+、AI精度95%+）
- Week 10: PMF検証完了（基本4指標評価）
- Week 12: Product Hunt準備 or Pivot判断

---

## 成果物フォーマット

```markdown
# ピボット判断レポート（ForGenAI版）

**作成日**: [YYYY-MM-DD]
**対象プロダクト**: [AI製品名]
**総合判定**: ✅ Pivot推奨 / ⚠️ Pivot要検討 / ❌ Pivot不要（改善継続）

---

## エグゼクティブサマリー

### ピボット必要性判定: [判定結果]

**現状分析**:
- PMF診断結果: [❌ PMF未達成]
- 主要指標:
  - Sean Ellis: XX% (基準: 40%以上)
  - 月次成長率: XX%/月 (基準: 15%以上)
  - AI精度: XX% (基準: 95%以上)
  - Churn Rate: XX%/月 (基準: 5%以下)
- 改善トレンド: [3ヶ月連続で改善なし]
- ランウェイ: [XX ヶ月]

**ピボット必要性**: [✅ Yes / ❌ No]

**推奨ピボット種類**: [Zoom In / Zoom Out / Customer Segment / Problem / Technology]

---

## 5つのピボット種類の評価

| ピボット種類 | 市場機会（40点） | 実行可能性（30点） | チーム適合性（30点） | 合計 | 判定 |
|------------|----------------|-----------------|-------------------|------|:----:|
| **Zoom In Pivot** | XX | XX | XX | XX | ✅/⚠️/❌ |
| **Zoom Out Pivot** | XX | XX | XX | XX | ✅/⚠️/❌ |
| **Customer Segment Pivot** | XX | XX | XX | XX | ✅/⚠️/❌ |
| **Problem Pivot** | XX | XX | XX | XX | ✅/⚠️/❌ |
| **Technology Pivot** | XX | XX | XX | XX | ✅/⚠️/❌ |

### 最高スコアピボット: [ピボット種類]（XX点）

**選定理由**:
[市場機会・実行可能性・チーム適合性の観点から説明]

---

## 推奨ピボット詳細

### ピボット種類: [Zoom In / Zoom Out / Customer Segment / Problem / Technology]

**Before（現状）**:
- ターゲット顧客: [顧客セグメント]
- 解決する課題: [課題]
- AI技術スタック: [OpenAI / Anthropic / Gemini / 自社モデル]
- UI戦略: [API / Web / Discord]
- ビジネスモデル: [Freemium / Subscription / API従量課金]

**After（Pivot後）**:
- ターゲット顧客: [新顧客セグメント]
- 解決する課題: [新課題]
- AI技術スタック: [新モデル]
- UI戦略: [新UI]
- ビジネスモデル: [新モデル]

**変更理由**:
[Pivot判断の根拠を詳細に説明]

**期待される成果**:
- Sean Ellis: XX% → YY%（目標: 40%以上）
- 月次成長率: XX%/月 → YY%/月（目標: 15%以上）
- AI精度: XX% → YY%（目標: 95%以上）
- ARPU: $XX/月 → $YY/月

---

## AI製品特有の評価

### モデル選択（Technology Pivot時）

| モデル | AI精度 | コスト（/1K） | 応答速度 | ハルシネーション率 | 推奨度 |
|--------|--------|--------------|----------|-------------------|:------:|
| OpenAI GPT-4 | 95%+ | $0.03 | 2.8秒 | 3% | ⚠️ |
| Anthropic Claude | 96% | $0.015 | 2.6秒 | 2% | ✅ |
| Google Gemini | 94% | $0.0007 | 3.2秒 | 4% | ❌ |
| Llama 3（OSS） | 90% | 自社運用 | 2.0秒 | 5% | ⚠️ |

**推奨モデル**: [Anthropic Claude]

**選定理由**:
- AI精度96%（目標95%以上達成）
- ハルシネーション率2%（業界最低、信頼性重視）
- コストはOpenAIの1/2（$0.015 vs $0.03）
- 企業向け安全性訴求に最適

### 垂直特化 vs 汎用化

**現状**: [汎用AI]
**推奨**: [垂直特化（検索/コーディング/ライティング等）]

**選定理由**:
- 汎用市場はChatGPTが独占（Sean Ellis 60%+）
- 垂直特化で10x優位性達成可能（Cursor: 開発速度2.5倍、Perplexity: 検索精度98%）
- 高ARPU狙い（Jasper: $250/月 vs ChatGPT: $20/月）

**ターゲット業界**: [業界名]

### API vs UI戦略

**現状**: [API]
**推奨**: [UI]

**選定理由**:
- API市場は成長鈍化（月次成長率 < 10%）
- 一般消費者市場の巨大性（OpenAI: GPT-3 API → ChatGPT成功事例）
- チームにUI/UX能力あり

---

## 成功ピボット事例参照

### ケーススタディ: [Perplexity - 汎用AI → 検索特化AI]

**Before**:
- 汎用対話AI（ChatGPT競合）
- Sean Ellis: 推定30%
- 月次成長率: 5%/月
- 差別化困難

**After**:
- AI検索エンジン（Google競合）
- Sean Ellis: 55%
- 月次成長率: 25-35%/月
- AI精度98%（検索特化）、引用精度95%

**Pivotアクション**:
1. 汎用対話機能削除
2. 検索特化UI開発（引用機能、ファクトチェック）
3. Google出身エンジニア採用
4. 検索精度98%達成（垂直特化の強み）

**成果**:
- バイラル係数0.9（高い紹介率）
- NPS 58
- VC調達成功（$70M+ Series B）

**活用可能なインサイト**:
- 汎用市場での苦戦 → 垂直特化で差別化
- 引用機能の重要性（信頼性訴求）
- Google出身の業界知見活用

---

## リスク分析

### 主要リスク

| リスク | 発生確率 | 影響度 | リスクスコア | 軽減策 |
|--------|---------|--------|-------------|-------|
| **ランウェイ枯渇** | 高 | 致命的 | 90 | Pivot前にSeed追加調達（$500K）、6ヶ月ランウェイ確保 |
| **既存顧客離脱** | 中 | 高 | 60 | Pivot前に既存顧客50人ヒアリング、移行支援提供 |
| **技術的実現不可** | 低 | 高 | 40 | Pivot前にPoC実施（1-2週間）、AI精度95%達成確認 |
| **チーム分裂** | 中 | 高 | 60 | 全員でPivot議論（1週間）、全員合意形成 |
| **競合激化** | 中 | 中 | 45 | 競合10社分析、10x優位性明確化 |

### リスク軽減アクション

1. **ランウェイ枯渇リスク（リスクスコア: 90）**:
   - Seed追加調達実施（目標: $500K、期限: Pivot前）
   - コスト削減（人件費20%削減、オフィス解約）
   - Pivot後6ヶ月のランウェイ確保

2. **既存顧客離脱リスク（リスクスコア: 60）**:
   - 既存顧客50人ヒアリング（Pivot後も使うか確認）
   - 移行支援提供（無料プラン延長、データ移行ツール）
   - Pivot方向性説明会（既存顧客向けウェビナー）

3. **技術的実現不可リスク（リスクスコア: 40）**:
   - PoC実施（1-2週間、技術検証）
   - AI精度95%達成確認（100タスク評価）
   - 応答速度3秒以下確認（1,000リクエスト測定）

4. **チーム分裂リスク（リスクスコア: 60）**:
   - Pivot議論（全員参加、1週間）
   - 全員合意形成（反対者ゼロ確認）
   - Pivot方向性ドキュメント作成（全員署名）

5. **競合激化リスク（リスクスコア: 45）**:
   - 競合10社分析（強み・弱み特定）
   - 10x優位性明確化（Cursor: 開発速度2.5倍、Perplexity: 検索精度98%）
   - 差別化ポイント3つ以上設定

---

## ピボット実行プラン（3ヶ月）

### Month 1: Pivot準備・PoC

**Week 1-2: PoC実施**
- [ ] 技術検証（AI精度、応答速度、コスト）
  - AI精度95%達成確認（100タスク評価）
  - 応答速度3秒以下確認（1,000リクエスト）
  - API料金試算（月次コスト $XX 想定）
- [ ] UI/UXプロトタイプ作成（Figma）
- [ ] 顧客ヒアリング10人（新ターゲット）
  - CPFスコア70%+達成確認

**Week 3-4: MVP開発**
- [ ] コア機能実装（最小限）
  - [機能1]
  - [機能2]
  - [機能3]
- [ ] AI精度95%達成確認（本番環境）
- [ ] 応答速度3秒以下達成確認（本番環境）

**マイルストーン**:
- Week 2: PoC完了（技術的実現性確認）✅
- Week 4: MVP完成（コア機能動作）✅

---

### Month 2: MVP検証・改善

**Week 5-6: 初期ユーザー獲得（30人）**
- [ ] ターゲット顧客リスト作成（100人）
- [ ] 個別アウトリーチ（メール、LinkedIn）
- [ ] MVP提供（無料トライアル）
- [ ] フィードバック収集（毎日、Slack）
  - CPFスコア70%+達成確認
  - 改善要望トップ10特定

**Week 7-8: PSF検証**
- [ ] `/validate-psf` 実施
  - AI精度95%+達成
  - 応答速度3秒以下達成
  - プロンプト再現性90%+達成
- [ ] UI/UX改善（ユーザーフィードバック反映）
- [ ] AI精度向上（ファインチューニング、RAG統合）

**マイルストーン**:
- Week 6: 初期ユーザー30人獲得✅
- Week 8: PSF達成（CPF 70%+、AI精度95%+）✅

---

### Month 3: PMF検証・Product Hunt準備

**Week 9-10: PMF検証**
- [ ] `/validate-pmf` 実施
  - Sean Ellis 40%+達成確認
  - 月次成長率15%+達成確認
  - Churn Rate 5%以下達成確認
  - NPS 50+達成確認
  - AI精度95%+達成確認
  - 応答速度3秒以下達成確認
- [ ] 基本4指標 + AI指標評価

**Week 11-12: Product Hunt準備 or 次のPivot判断**
- [ ] PMF達成時:
  - `/create-producthunt-strategy` 実施
  - デモ動画作成（30秒）
  - Hunter事前確保
  - コミュニティ構築（Discord/Slack）
- [ ] PMF未達成時:
  - Pivot継続判断（同じPivot種類で改善 or 別のPivot種類検討）
  - ランウェイ確認（6ヶ月以上あれば継続、なければ資金調達）

**マイルストーン**:
- Week 10: PMF検証完了（基本4指標評価）✅
- Week 12: Product Hunt準備完了 or Pivot判断✅

---

## 次のステップ

### ピボット推奨の場合（✅）

**即時アクション**:
1. Pivot方向性決定（5つのピボット種類から選択）
2. チーム全員で合意形成（1週間）
3. PoC実施（1-2週間、技術検証）
4. 資金計画見直し（Seed追加調達検討）

**2-4週間以内**:
1. MVP開発開始（コア機能実装）
2. 顧客ヒアリング30人（新ターゲット）
3. `/validate-psf` 実施（PSF達成確認）

**3ヶ月目標**:
1. `/validate-pmf` 実施（PMF達成確認）
2. Product Hunt準備（PMF達成時）
3. 次のPivot判断（PMF未達成時）

**推奨コマンド**:
```
/select-ai-tech-stack（Technology Pivot時）
/discover-demand（Problem Pivot時）
/validate-cpf（Customer Segment Pivot時）
```

---

### ピボット不要の場合（❌）

**改善継続**:
1. 上記PMF診断の「改善アクション」を実行
2. 週次で進捗モニタリング
3. 1-2ヶ月後に `/validate-pmf` 再実行
4. PMF達成 → Product Hunt準備
5. PMF未達成 → Pivot検討

**注意事項**:
- 3ヶ月連続で改善なし → Pivot必須
- ランウェイ < 6ヶ月 → Seed追加調達検討
- AI精度95%達成困難 → Technology Pivot検討

---

## メタデータ

| 項目 | 内容 |
|-----|------|
| 作成日 | [YYYY-MM-DD] |
| 実行Skill | `/pivot-decision` (ForGenAI版) |
| フレームワーク | 起業の科学 + GenAI製品ピボット戦略 |
| 準拠率 | 100% |
| 成功ピボット事例参照 | Slack, Instagram, Perplexity, Cursor, Anthropic, Replicate, Hugging Face, Midjourney |
| GenAI_research統合 | LLM/01_LifeisBeautiful_insights.md |
| 次のピボット検証予定 | [3ヶ月後] |
```

---

## Domain-Specific Knowledge (from Research)

### Success Patterns（GenAI製品ピボット事例）

1. **Perplexity（Zoom In Pivot: 汎用AI → 検索特化）**:
   - 汎用対話AIでChatGPTと競合、差別化困難
   - 検索特化でAI精度98%達成、引用精度95%
   - バイラル係数0.9（高い紹介率）

2. **Cursor（Zoom In Pivot: 汎用コーディング → VSCode統合IDE）**:
   - ブラウザツールは採用障壁高い
   - VSCode互換でChurn Rate 2.5%達成（極めて低い）
   - 開発速度2.5倍向上を実証

3. **OpenAI（Zoom Out Pivot: GPT-3 API → ChatGPT）**:
   - API市場は成長遅い
   - ChatGPTで2ヶ月1億ユーザー（史上最速）
   - B2D → B2C戦略成功

4. **Anthropic（Customer Segment Pivot: 研究機関 → Claude Pro）**:
   - 研究だけでは収益化困難
   - Claude Proで企業利用率45%達成
   - ハルシネーション率2%（業界最低）で差別化

5. **Slack（Problem Pivot: ゲーム → コミュニケーション）**:
   - ゲーム失敗、内部ツールを製品化
   - Sean Ellis 55%+、NPS 65+達成
   - 2014年上場成功

6. **Replicate（Technology Pivot: 自社モデル → マルチモデルAPI）**:
   - 自社モデルは競争力不足
   - オープンソースモデル統合でAPI呼び出し成長率45%/月
   - プラットフォーム戦略成功

7. **Midjourney（Technology Pivot: WebUI → Discord）**:
   - WebUIは採用障壁高い
   - Discord中心でMAU 200万+達成
   - コミュニティファースト戦略

### GenAI Market Trends（ピボット判断に影響）

1. **モデルコモディティ化**:
   - モデル性能から配布・統合・運用へ競争軸が移動
   - 差別化ポイント: UI/ワークフロー/データ/セキュリティ
   - ピボット戦略: モデル性能競争 → 運用最適化へ
   - 出典: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`

2. **SaaS置換トレンド**:
   - 従来SaaSのUI/ビジネスロジックが自然言語＋エージェントで置換
   - ピボット機会: SaaS特化AI（会計AI、営業AI、HR AI等）
   - 出典: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`

3. **Move 37的ブレイクスルー**:
   - 強化学習による「考える力」獲得
   - ピボット戦略: 汎用AI → 垂直特化AI（数学、医学、法律等で創造的発見）
   - 出典: `@GenAI_research/LLM/01_LifeisBeautiful_insights.md`

### Common Pitfalls（ピボット失敗パターン）

1. **連続ピボット**: 6ヶ月に3回以上Pivot → 戦略不明確、焦り
2. **ランウェイ枯渇**: Pivot中に資金枯渇 → 資金計画甘い
3. **チーム分裂**: Pivot方向性で対立 → 全員合意なし
4. **顧客ゼロ化**: Pivot後に既存顧客全離脱 → 顧客ヒアリングなし
5. **技術負債**: Pivot後に技術的実現不可 → 技術検証不足

### Quantitative Benchmarks（GenAI製品ピボット）

| 指標 | ピボット前 | ピボット後（目標） | 出典 |
|------|----------|-----------------|------|
| **Sean Ellisテスト** | < 30% | **40%以上** | @GenAI_research（Perplexity 55%、Cursor 65%） |
| **月次成長率** | < 10%/月 | **15%以上/月** | @GenAI_research（Perplexity 25-35%、Cursor 40-50%） |
| **AI精度** | < 90% | **95%以上** | @GenAI_research（Perplexity 98%、ChatGPT 95%+） |
| **Churn Rate** | > 10%/月 | **5%以下/月** | @GenAI_research（Cursor 2.5%） |

### Best Practices

1. **Pivot前のPoC必須**: 技術検証1-2週間（AI精度95%、応答速度3秒以下達成確認）
2. **顧客ヒアリング100人**: 既存50人 + 新ターゲット50人
3. **ランウェイ6ヶ月以上確保**: Pivot実行・検証の時間確保
4. **チーム全員合意**: Pivot方向性で反対者ゼロ
5. **3ヶ月検証期間**: 1Pivot = 3ヶ月、焦らず

### Reference
- 詳細: @GenAI_research/LLM/01_LifeisBeautiful_insights.md
- ケーススタディ: @GenAI_research/case_studies/tier2/
- ナレッジ抽出: @.claude/skills/for_genai/_analysis/pivot_knowledge.md

---

## 使用例

```
User: /pivot-decision

Skill:
# ピボット判断（ForGenAI版） 自律実行開始

ピボット必要性判定中...
✅ PMF未達成（`/validate-pmf` で❌判定）
✅ 3ヶ月連続で改善なし（Sean Ellis 25%、成長率 3%、Churn 12%）
✅ AI精度85%（95%達成困難、モデル改善余地なし）
✅ ランウェイ8ヶ月（Pivot実行余力あり）

→ ピボット必要性: ✅ Yes

[5つのピボット種類評価中...]

STEP 1: ピボット必要性判定 ✅
STEP 2: 5つのピボット種類の評価 ✅

| ピボット種類 | 市場機会 | 実行可能性 | チーム適合性 | 合計 | 判定 |
|------------|---------|-----------|-------------|------|:----:|
| Zoom In Pivot | 35 | 28 | 27 | **90** | ✅ |
| Zoom Out Pivot | 38 | 20 | 15 | 73 | ⚠️ |
| Customer Segment Pivot | 30 | 25 | 22 | 77 | ⚠️ |
| Problem Pivot | 25 | 18 | 10 | 53 | ❌ |
| Technology Pivot | 28 | 22 | 20 | 70 | ⚠️ |

**推奨ピボット**: Zoom In Pivot（90点）

STEP 3: AI製品特有の追加評価 ✅
  - 垂直特化推奨: 検索特化AI（Perplexity式）
  - 理由: 汎用AIでSean Ellis 25%（ChatGPT競合困難）、検索機能のみSean Ellis 60%
  - 期待成果: Sean Ellis 25% → 55%、AI精度85% → 98%（検索特化）

STEP 4: リスク分析と軽減策 ✅
  - 主要リスク: ランウェイ枯渇（リスクスコア90）、既存顧客離脱（60）
  - 軽減策: Seed追加調達$500K、既存顧客50人ヒアリング

STEP 5: ピボット実行プラン策定 ✅
  - Month 1: PoC実施（検索特化AI、引用機能）
  - Month 2: MVP検証（初期ユーザー30人、PSF達成）
  - Month 3: PMF検証（Sean Ellis 40%+、AI精度95%+達成）

## 完了

成果物: Flow/202601/2026-01-02/pivot_decision_forgenai.md
総合判定: ✅ Pivot推奨（Zoom In Pivot）

**推奨Pivot**: 汎用AI → 検索特化AI（Perplexity式）

**Before**:
- 汎用対話AI（ChatGPT競合）
- Sean Ellis 25%
- AI精度85%

**After**:
- AI検索エンジン（Google競合）
- 目標Sean Ellis 55%
- 目標AI精度98%（検索特化）

**次のステップ**:
1. PoC実施（1-2週間、検索特化AI技術検証）
2. 顧客ヒアリング50人（検索需要確認）
3. MVP開発（3-4週間、引用機能・ファクトチェック）

推奨: Pivot実行プラン（3ヶ月）に従って進行、Seed追加調達$500K検討
```

---

## 成功基準

1. ✅ **ピボット必要性の客観的判定**: PMF診断結果、改善トレンド、ランウェイから判断
2. ✅ **5つのピボット種類の体系的評価**: 市場機会・実行可能性・チーム適合性の3軸評価
3. ✅ **AI製品特有の追加評価**: モデル選択、垂直特化、API vs UI戦略
4. ✅ **成功ピボット事例統合**: Slack/Instagram/Perplexity/Cursor/Anthropic等12事例参照
5. ✅ **リスク分析と軽減策**: 5つの失敗パターンと具体的な回避策
6. ✅ **実行プラン自動生成**: 3ヶ月ピボットロードマップ、マイルストーン設定

---

## 注意事項

1. **ピボット前の十分な準備**: PoC、顧客ヒアリング100人、資金計画見直し必須
2. **焦らない**: 1Pivot = 3ヶ月検証期間設定、連続ピボット禁止
3. **チーム全員合意**: Pivot方向性で反対者ゼロ確認
4. **ランウェイ6ヶ月以上確保**: Pivot実行・検証の時間確保
5. **AI製品特有の考慮**: モデルコモディティ化、垂直特化、API vs UI戦略
6. **成功事例参照の徹底**: Slack/Instagram/Perplexity/Cursor/Anthropic等の事例を必ず参照

---

## ForStartup版との差分

| 項目 | ForStartup | ForGenAI | 差分理由 |
|------|----------|----------|---------|
| **ピボット種類** | 5種類 | **5種類 + AI特有選択肢** | モデル選択、垂直特化、API vs UI戦略追加 |
| **成功事例参照** | Airbnb/Slack/Instagram | **Perplexity/Cursor/Anthropic等** | GenAI製品ベンチマーク統合 |
| **追加評価軸** | なし | **モデル選択、垂直特化、API vs UI** | AI製品特有の戦略選択 |
| **AI品質指標** | なし | **AI精度95%、応答速度3秒以下** | ピボット後の目標設定 |
| **GenAI_research統合** | なし | **モデルコモディティ化、SaaS置換トレンド** | AI市場トレンド反映 |

---

## 更新履歴

- 2026-01-02: ForGenAI版として新規作成（AI製品ピボット戦略、GenAI_research統合、12 Tier 2ケーススタディ統合）
- ベース: 起業の科学の5つのピボット種類フレームワーク
