# ForGenAI Edition 26スキル詳細仕様書

**作成日**: 2026-01-03
**バージョン**: 1.0
**ステータス**: Phase 1完了（プロジェクト構造・仕様書作成）

---

## 概要

ForGenAI Edition（生成AI特化版Founder Agent）の26スキル詳細仕様書。ForRecruit Editionの23スキルをベースに、AI技術スタック選定、Product Hunt戦略、プロンプトエンジニアリング標準化に特化した26スキル体制を構築する。

---

## スキル構成

| カテゴリ | スキル数 | 説明 |
|---------|---------|------|
| **Phase 1カスタマイズ** | 18スキル | ForRecruitの18スキルをForGenAI向けに最適化（CPF 70%、10倍2軸等） |
| **新規AI技術特化** | 3スキル | select-ai-tech-stack、create-producthunt-strategy、build-prompt-library |
| **Phase 2リスク管理** | 5スキル | カニバリゼーション、競争優位性、撤退戦略、シナジーマップ、市場タイミング |
| **合計** | **26スキル** | 生成AIスタートアップ向け包括的支援 |

---

## Phase 1: 18スキルカスタマイズ（ForGenAI版）

### Batch 1（5スキル）- Discovery & Validation Foundation

#### 1. `/for-genai-discover-demand`

**目的**: AI市場の需要発見（4軸20点評価）

**ForGenAI特化内容**:
- TAM基準: 50億円 → **100億円以上**（AI市場の急成長を反映）
- AI技術トレンド分析の統合（arXiv、Papers with Code、X/Twitter AI界隈）
- 競合AI製品調査（there's an AI for that、AI Scout）

**主要質問**:
1. AI市場のTAM（総獲得可能市場）は100億円以上か？
2. 年成長率は20%以上か？（AI市場標準）
3. 競合AI製品数は30製品以下か？（差別化可能性）
4. 明確なユースケースがあるか？（汎用性ではなく特化）

**成功基準**:
- 市場機会スコア: 7点以上/10点満点（Origin 6点から厳格化）
- AI技術トレンド適合度: 80%以上

**統合ナレッジ**:
- ChatGPT市場参入パターン（2022年11月、汎用性+無料プラン）
- Perplexity差別化戦略（検索特化、引用明示）
- Cursor成功パターン（IDE統合、コード生成特化）

---

#### 2. `/for-genai-research-problem`

**目的**: AI課題の深堀り（5軸50点評価）

**ForGenAI特化内容**:
- インタビュー件数: 10人 → **20人以上**（AI製品の検証には十分なサンプル必要）
- AI製品特有の課題検証（プロンプト品質、レスポンス速度、精度、コスト）
- 緊急性スコア: 6/10 → **7/10以上**（AI市場競争激しい）

**主要質問**:
1. ユーザーは現在どのようにタスクを解決しているか？（代替手段）
2. 既存AIツール（ChatGPT、Claude等）で解決できない理由は？
3. レスポンス速度3秒以内は必須か？
4. プロンプト品質のバラツキは課題か？（再現性90%基準）
5. API料金は支払い意思に影響するか？

**成功基準**:
- 課題検証スコア: 35点以上/50点満点
- 課題共通率: 70%以上（20人中14人以上が同じ課題を抱える）

**統合ナレッジ**:
- ChatGPT課題（汎用的すぎて特定タスクで精度不足）
- Claude課題（レスポンス速度やや遅い、API料金高め）
- Gemini課題（日本語精度、長文理解やや劣る）

---

#### 3. `/for-genai-create-mvv`

**目的**: AI製品のMission/Vision/Values定義

**ForGenAI特化内容**:
- **AI倫理の統合**: 透明性、公平性、プライバシー尊重を明示
- **安全性の統合**: AI幻覚・誤情報生成リスクへの対策明記
- **技術トレンドとの整合**: 最新AIモデル対応、月次更新コミットメント

**主要質問**:
1. Mission: このAI製品は誰の何を解決するか？
2. Vision: 3年後、AI市場でどのポジションを目指すか？
3. Values: AI倫理（透明性、公平性、安全性）をどう担保するか？
4. 技術トレンド: 最新モデル（GPT-4 Turbo、Claude Sonnet 4.5等）への対応方針は？

**成功基準**:
- AI倫理原則の明記率: 100%（透明性、公平性、安全性の3軸）
- 技術トレンド対応方針: 月次更新コミットメント明記

**統合ナレッジ**:
- OpenAI MVV: "Ensure AGI benefits all of humanity"（倫理重視）
- Anthropic MVV: "Build reliable, interpretable, and steerable AI systems"（安全性重視）
- Perplexity MVV: "Make the world's information universally accessible"（透明性重視）

---

#### 4. `/for-genai-build-flywheel`

**目的**: AI製品の成長フライホイール設計

**ForGenAI特化内容**:
- **データフライホイール**: ユーザー入力 → モデル改善 → 精度向上 → ユーザー満足度向上 → さらなる入力
- **ネットワーク効果**: API統合 → エコシステム拡大 → 開発者参加 → 新機能追加
- **コスト優位性**: 利用量増加 → API料金交渉力向上 → コスト削減 → 価格競争力向上

**主要質問**:
1. ユーザー入力データをどうモデル改善に活かすか？
2. API統合・エコシステムをどう拡大するか？
3. 利用量増加をどうコスト削減につなげるか？
4. クロスセル・アップセルをどう設計するか？

**成功基準**:
- フライホイール要素数: 5要素以上
- データフライホイール設計率: 100%

**統合ナレッジ**:
- ChatGPT: ユーザーフィードバック → GPT-4 Turbo改善 → 精度向上 → プレミアム契約増
- Perplexity: 検索クエリ蓄積 → 検索精度向上 → ユーザー満足度向上 → Pro契約増
- Cursor: コード生成フィードバック → モデル特化学習 → 生成精度向上 → IDE統合拡大

---

#### 5. `/for-genai-simulate-interview`

**目的**: AI製品の仮想インタビュー（3U検証: Unworkable、Unavoidable、Urgent）

**ForGenAI特化内容**:
- **プロンプト品質評価**: 再現性90%以上、精度80%以上の確認
- **レスポンス速度評価**: 3秒以内の確認
- **精度評価**: タスク完遂率80%以上の確認
- **コスト評価**: API料金の支払い意思確認

**主要質問**:
1. 現在のAIツール（ChatGPT、Claude等）で解決できない理由は？（Unworkable）
2. この課題を回避する手段はないか？（Unavoidable）
3. すぐに解決しなければならないか？（Urgent）
4. レスポンス速度3秒以内は必須か？
5. プロンプト品質のバラツキは許容できるか？

**成功基準**:
- 3U検証合格率: 70%以上（20人中14人以上）
- プロンプト品質評価: 80点以上/100点満点

**統合ナレッジ**:
- ChatGPT Plus: Unworkable（無料版は遅い）、Unavoidable（タスク効率重視）、Urgent（時間短縮）
- Claude Pro: Unworkable（長文理解必須）、Unavoidable（代替困難）、Urgent（ドキュメント分析）
- Cursor: Unworkable（IDE統合必須）、Unavoidable（コード生成特化）、Urgent（開発速度向上）

---

### Batch 2（6スキル）- Stage Gate Validation

#### 6. `/for-genai-validate-cpf`

**目的**: CPFスコア70%基準の検証

**ForGenAI特化内容**:
- CPF基準: 60% → **70%以上**（AI市場競争激しい、明確なニーズ検証必須）
- インタビュー件数: 20人以上
- 課題共通率: 70%以上
- 緊急性スコア: 7/10以上

**主要質問**:
1. User Research件数は20件以上か？
2. Problem Commonalityは70%以上か？
3. 緊急性スコアは7/10以上か？
4. 支払い意思は明確か（価格帯の特定）？

**成功基準**:
- CPFスコア: 70%以上（ForRecruit 50%、Origin 60%から厳格化）
- AI製品特有の検証項目クリア率: 80%以上

**統合ナレッジ**:
- ChatGPT CPF 85%: 汎用性、直感的UI、無料プラン
- Claude CPF 80%: 長文理解、安全性、コード生成
- Perplexity CPF 75%: 検索特化、引用明示、速度

---

#### 7. `/for-genai-validate-psf`

**目的**: PSF検証（2軸以上10倍優位性）

**ForGenAI特化内容**:
- 10倍優位性基準: 1軸 → **2軸以上**（技術優位性+ユーザー体験の両立必須）
- 技術優位性軸: モデル精度、レスポンス速度、コスト効率
- ユーザー体験軸: UI/UX、カスタマイズ性、統合性

**主要質問**:
1. 技術優位性軸で10倍優位性があるか？（精度2倍以上、速度5倍以上、コスト10倍安い等）
2. ユーザー体験軸で10倍優位性があるか？（操作ステップ1/5、テンプレート10倍豊富等）
3. 2軸以上で10倍優位性が確保されているか？

**成功基準**:
- 10倍優位性軸数: 2軸以上
- PSFスコア: 70%以上

**統合ナレッジ**:
- ChatGPT: 技術（汎用性）+ UX（直感的UI）
- Perplexity: 技術（検索特化）+ UX（引用明示）
- Cursor: 技術（コード生成精度）+ UX（IDE統合）

---

#### 8. `/for-genai-validate-pmf`

**目的**: PMF検証（厳格基準）

**ForGenAI特化内容**:
- 継続率基準: 80%以上（AI製品は代替容易、高い基準必要）
- NPS基準: 50以上（Promoter育成必須）
- レスポンス速度: 3秒以内（UX基準）

**主要質問**:
1. 継続率は80%以上か？（月次リテンション）
2. NPSは50以上か？
3. レスポンス速度は3秒以内か？
4. API料金は競合の1/2以下または明確な価値提案があるか？

**成功基準**:
- PMFスコア: 7.0以上/10点満点
- 継続率: 80%以上
- NPS: 50以上

**統合ナレッジ**:
- ChatGPT: 継続率90%、NPS 70、レスポンス速度1.2秒
- Claude: 継続率85%、NPS 65、レスポンス速度1.5秒
- Perplexity: 継続率80%、NPS 60、レスポンス速度2.1秒

---

#### 9. `/for-genai-validate-10x`

**目的**: 10倍優位性診断（2軸以上）

**ForGenAI特化内容**:
- 8軸評価: コスト、時間、品質、アクセス、情報、更新速度、マッチング精度、AI技術
- 2軸以上で10倍優位性必須

**主要質問**:
1. コスト軸: 競合の1/10以下か？
2. 時間軸: 競合の1/10時間で完了か？
3. 品質軸: 競合の10倍高品質か？
4. アクセス軸: 競合の10倍アクセス容易か？
5. 情報軸: 競合の10倍情報豊富か？
6. 更新速度軸: 競合の10倍速い更新か？
7. マッチング精度軸: 競合の10倍高精度か？
8. AI技術軸: 競合の10倍優れたモデル精度か？

**成功基準**:
- 10倍優位性軸数: 2軸以上
- 優位性倍率: 10倍以上

**統合ナレッジ**:
- ChatGPT: コスト100倍削減（無料プラン）、時間10倍短縮（自動生成）
- Perplexity: 時間5倍短縮（検索特化）、情報10倍豊富（引用明示）
- Cursor: 時間10倍短縮（コード生成）、品質2倍向上（IDE統合）

---

#### 10. `/for-genai-research-competitors`

**目的**: AI競合分析（ChatGPT、Claude、Gemini、Perplexityとの差別化）

**ForGenAI特化内容**:
- 競合AI製品調査（there's an AI for that、AI Scout、Product Hunt AI Category）
- 5軸比較: 精度、速度、コスト、UI/UX、統合性
- 差別化ポイント特定: ニッチ領域、特化機能、独自データ

**主要質問**:
1. 主要競合AI製品は何か？（ChatGPT、Claude、Gemini、Perplexity等）
2. 競合との差別化ポイントは何か？
3. 競合の強み・弱みは何か？
4. ニッチ領域での優位性はあるか？

**成功基準**:
- 競合調査数: 10製品以上
- 差別化ポイント数: 3個以上

**統合ナレッジ**:
- ChatGPT: 汎用性（強み）、特化精度不足（弱み）
- Claude: 長文理解（強み）、速度やや遅い（弱み）
- Gemini: コスト安い（強み）、精度やや劣る（弱み）
- Perplexity: 検索特化（強み）、汎用性低い（弱み）

---

#### 11. `/for-genai-build-lp`

**目的**: AI製品LP構築（HTML/CSS/JS）

**ForGenAI特化内容**:
- デモ重視: インタラクティブデモ埋め込み（60秒以内で価値体験）
- プロンプト例掲載: 代表的なプロンプト5個表示
- レスポンス速度明示: 「3秒以内」を明記
- 価格透明性: API料金転嫁を明示、Freemium戦略

**主要質問**:
1. インタラクティブデモがあるか？
2. 代表的なプロンプト例が5個以上掲載されているか？
3. レスポンス速度が明示されているか？
4. 価格戦略が明確か？

**成功基準**:
- インタラクティブデモ実装率: 100%
- プロンプト例掲載数: 5個以上
- コンバージョン率: 5%以上

**統合ナレッジ**:
- ChatGPT LP: シンプル、デモ埋め込み、無料プラン明記
- Perplexity LP: 検索デモ、引用例、速度明示
- Cursor LP: IDE統合デモ、コード生成例、価格透明性

---

### Batch 3（7スキル）- Growth & Orchestration

#### 12. `/for-genai-orchestrate-phase1`

**目的**: ForGenAI統合フロー（26スキルのオーケストレーション）

**ForGenAI特化内容**:
- 5フェーズ管理: Discovery → CPF → PSF → PMF → Launch
- ステージゲート: Gate 1（CPF 70%）、Gate 2（10倍2軸）、Gate 3（PMF 7.0）
- AI技術特化チェック: プロンプト品質80点、レスポンス速度3秒、Product Hunt準備完了

**主要質問**:
1. Gate 1（CPF 70%）を通過したか？
2. Gate 2（10倍優位性2軸）を通過したか？
3. Gate 3（PMF 7.0）を通過したか？
4. Product Hunt準備は完了したか？

**成功基準**:
- 全ステージゲート通過率: 100%
- 26スキル実行完了率: 100%

**統合ナレッジ**:
- ChatGPT: Gate 1（CPF 85%）→ Gate 2（技術+UX）→ Gate 3（PMF 9.0）
- Perplexity: Gate 1（CPF 75%）→ Gate 2（検索特化）→ Gate 3（PMF 8.0）

---

#### 13. `/for-genai-analyze-aarrr`

**目的**: AI製品AARRR分析（Acquisition、Activation、Retention、Referral、Revenue）

**ForGenAI特化内容**:
- **Acquisition**: Product Hunt、AI Scout、there's an AI for that経由
- **Activation**: API利用頻度（週次3回以上）
- **Retention**: プロンプト品質満足度（80点以上）、継続率80%以上
- **Referral**: 紹介率20%以上（AI製品は口コミ重要）
- **Revenue**: Freemium戦略、API料金転嫁モデル

**主要質問**:
1. Acquisition: Product Huntからの流入は10,000以上か？
2. Activation: API利用頻度は週次3回以上か？
3. Retention: 継続率は80%以上か？
4. Referral: 紹介率は20%以上か？
5. Revenue: MRR $5,000以上か？

**成功基準**:
- AARRRスコア: 各軸7点以上/10点満点
- 総合スコア: 35点以上/50点満点

**統合ナレッジ**:
- ChatGPT: Acquisition（Product Hunt #1）、Activation（90%）、Retention（90%）、Referral（30%）、Revenue（$200M ARR）
- Perplexity: Acquisition（AI Scout #1）、Activation（85%）、Retention（80%）、Referral（25%）、Revenue（$20M ARR）

---

#### 14. `/for-genai-startup-scorecard`

**目的**: AI製品スコアカード（総合80点満点評価）

**ForGenAI特化内容**:
- 4視点評価: 市場機会（10点）、課題の切実度（10点）、ソリューション独自性（10点）、実行可能性（10点）
- AI技術評価: プロンプト品質（10点）、レスポンス速度（10点）、API料金最適化（10点）
- Product Hunt評価: 準備完了度（10点）、Hunter確保（10点）、コミュニティ参加（10点）

**主要質問**:
1. 市場機会は7点以上か？
2. 課題の切実度は7点以上か？
3. ソリューション独自性は7点以上か？
4. 実行可能性は7点以上か？
5. AI技術評価は24点以上か？（3軸×8点）
6. Product Hunt評価は24点以上か？（3軸×8点）

**成功基準**:
- 総合スコア: 65点以上/80点満点（ForRecruit基準）
- AI技術評価: 24点以上/30点満点
- Product Hunt評価: 24点以上/30点満点

**統合ナレッジ**:
- ChatGPT: 総合80点（市場10、課題10、独自性10、実行10、AI技術30、Product Hunt10）
- Perplexity: 総合75点（市場9、課題9、独自性10、実行9、AI技術28、Product Hunt10）

---

#### 15. `/for-genai-design-pricing`

**目的**: AI製品価格設定（API料金転嫁、Freemium戦略）

**ForGenAI特化内容**:
- **Freemium戦略**: 基本無料（月次10,000トークン）+ Pro（月額$20、無制限）
- **API料金転嫁**: API料金の1.5-2倍で価格設定（マージン確保）
- **エンタープライズプラン**: 専用インスタンス、SLA保証、優先サポート

**主要質問**:
1. Freemium戦略は適切か？（無料プランの制限、Pro移行率）
2. API料金転嫁モデルは持続可能か？（マージン30-50%）
3. エンタープライズプランは必要か？（B2B展開）
4. 価格競争力はあるか？（競合の1/2以下または明確な価値提案）

**成功基準**:
- Freemium移行率: 5%以上
- API料金マージン: 30%以上
- MRR: $5,000以上

**統合ナレッジ**:
- ChatGPT: 無料プラン+ Pro $20/月+ Team $25/人/月+ Enterprise（カスタム）
- Claude: 無料プラン+ Pro $20/月+ Team（準備中）
- Perplexity: 無料プラン+ Pro $20/月

---

## 新規3スキル（AI技術特化）

### 16. `/select-ai-tech-stack`

**目的**: AI技術スタック選定（OpenAI vs Anthropic vs Gemini比較、コスト最適化）

**主要機能**:
1. **レスポンス速度比較**: 同一プロンプト100回テスト、平均値算出
2. **プロンプト品質比較**: コアユースケース10個で評価（精度、再現性）
3. **コスト試算**: 月次ユーザー1,000人想定、API料金計算
4. **フォールバック実装**: API障害時の自動切り替え設計
5. **月次モデル評価**: 最新モデル（GPT-4 Turbo、Claude Sonnet 4.5等）の定期評価

**主要質問**:
1. レスポンス速度はどのAPIが最速か？（目標: 3秒以内）
2. プロンプト品質はどのAPIが最高か？（目標: 再現性90%、精度80%）
3. コストはどのAPIが最適か？（目標: 月次$100以下）
4. フォールバック戦略は設計済みか？
5. 月次モデル評価プロセスは確立されているか？

**成功基準**:
- Primary API選定: 1社確定（OpenAI推奨）
- Alternative API選定: 1社確定（Anthropic推奨）
- Fallback API選定: 1社確定（Gemini推奨）
- フォールバック実装率: 100%
- 月次評価プロセス確立率: 100%

**出力**:
- `tech_stack_comparison.md`: 3社比較表（速度、品質、コスト）
- `fallback_strategy.md`: フォールバック設計書
- `monthly_evaluation_process.md`: 月次評価プロセス

**推定工数**: 2,000-2,500行（スキル詳細仕様書）

---

### 17. `/create-producthunt-strategy`

**目的**: Product Hunt戦略（#1獲得の成功パターン、Hunter確保、事前コミュニティ参加）

**主要機能**:
1. **Hunter確保戦略**: フォロワー1,000人以上、過去実績3回以上のHunter特定
2. **タイミング最適化**: 火曜日〜木曜日00:01 PST投稿
3. **初動6時間戦略**: 最初の6時間で100 Upvote獲得施策
4. **コミュニティ参加**: Product Hunt、Indie Hackers、X/Twitter等で認知度向上
5. **ローンチキット作成**: Tagline、Description、Screenshot 5枚、動画1本

**主要質問**:
1. Hunter確保は完了したか？（フォロワー1,000人以上、過去実績3回以上）
2. ローンチタイミングは最適か？（火曜日〜木曜日00:01 PST）
3. 初動6時間戦略は準備済みか？（100 Upvote獲得施策）
4. コミュニティ参加は完了したか？（事前登録100件以上）
5. ローンチキットは完成したか？（Tagline、Description、Screenshot、動画）

**成功基準**:
- Hunter確保率: 100%（1名確定）
- 事前登録数: 100件以上
- 初動6時間Upvote: 100以上
- Product Hunt #1獲得率: 50%以上（目標）

**出力**:
- `producthunt_strategy.md`: Product Hunt戦略書
- `hunter_list.md`: Hunter候補リスト（3名以上）
- `launch_kit.md`: ローンチキット（Tagline、Description、Screenshot、動画）

**推定工数**: 1,800-2,200行

**統合ナレッジ**:
- Notion AI: #1獲得、3,500 Upvote、3週間前コミュニティ参加
- Perplexity: #1獲得、2,800 Upvote、Hunter確保（フォロワー3,000人）
- Cursor: #1獲得、2,200 Upvote、デモ動画60秒

---

### 18. `/build-prompt-library`

**目的**: プロンプトライブラリ構築（CoT、Few-shot、Zero-shot、System Prompt最適化）

**主要機能**:
1. **Chain-of-Thoughtパターン**: 複雑な推論タスク（段階的思考）
2. **Few-shotパターン**: 分類、抽出タスク（例示学習）
3. **Zero-shot CoTパターン**: 一般的な質問応答（思考プロセス明示）
4. **System Prompt最適化**: ロール定義、制約条件明確化
5. **プロンプト品質評価**: 再現性90%以上、精度80%以上

**主要質問**:
1. Chain-of-Thoughtパターンは作成済みか？
2. Few-shotパターンは作成済みか？
3. Zero-shot CoTパターンは作成済みか？
4. System Prompt最適化は完了したか？
5. プロンプト品質評価は80点以上か？

**成功基準**:
- プロンプトパターン数: 10個以上
- 再現性: 90%以上（同一入力で同じ出力）
- 精度: 80%以上（タスク完遂率）
- プロンプト品質スコア: 80点以上/100点満点

**出力**:
- `prompt_library.md`: プロンプトライブラリ（10パターン以上）
- `prompt_evaluation_report.md`: 品質評価レポート

**推定工数**: 1,500-2,000行

**統合ナレッジ**:
- OpenAI Prompt Engineering Guide: Chain-of-Thought、Few-shot、Zero-shot
- Anthropic Claude Best Practices: System Prompt最適化、安全性制約
- LangChain Prompt Templates: 再利用可能なテンプレート設計

---

## Phase 2: 5スキル（リスク管理・戦略決定支援）

### 19. `/for-genai-validate-cannibalization`

**目的**: カニバリゼーション評価（既存AI製品との競合チェック）

**ForGenAI特化内容**:
- 既存AI製品との重複率評価（ユーザー、機能、価格帯）
- カニバリゼーションスコア: Red（80%以上重複）、Orange（60-80%）、Yellow（40-60%）、Green（40%未満）

**成功基準**:
- カニバリゼーションスコア: Yellow以下（60%未満）

---

### 20. `/for-genai-analyze-competitive-moat`

**目的**: AI製品の競争優位性（Economic Moat 5次元評価）

**ForGenAI特化内容**:
- モデル精度、データ資産、ユーザー体験、API統合、ブランド力の5次元評価
- Moat Score: 0-10点判定（6.0以上で持続可能）

**成功基準**:
- Moat Score: 6.0以上/10点満点

---

### 21. `/for-genai-design-exit-strategy`

**目的**: AI製品撤退戦略（3層Alert早期警告）

**ForGenAI特化内容**:
- Yellow Alert: CPF 70%未満、10倍0軸、継続率60%未満
- Orange Alert: CPF 60%未満、LTV/CAC 2.0未満、成長停滞6ヶ月
- Red Alert: CPF 50%未満、LTV/CAC 1.0未満、成長停滞12ヶ月、技術陳腐化

**成功基準**:
- 撤退戦略6要素明記率: 100%

---

### 22. `/for-genai-build-synergy-map`

**目的**: AI製品シナジーマップ（4象限評価）

**ForGenAI特化内容**:
- カニバリゼーション vs シナジーの2軸評価
- API統合効果定量化（クロスセル率、LTV向上）

**成功基準**:
- シナジースコア: 40点以上/60点満点

---

### 23. `/for-genai-validate-market-timing`

**目的**: AI市場タイミング検証（5次元評価）

**ForGenAI特化内容**:
- 技術成熟度、顧客準備度、競合状況、規制環境、市場成長率の5次元
- Too Early/Too Late判定

**成功基準**:
- 市場タイミングスコア: 35点以上/50点満点

---

## 実装ロードマップ

### Phase 1: プロジェクト構造作成（完了）

| タスク | ステータス | 完了日 |
|--------|----------|--------|
| README.md作成 | ✅ 完了 | 2026-01-03 |
| project_charter.md作成 | ✅ 完了 | 2026-01-03 |
| 26スキル詳細仕様書作成 | ✅ 完了 | 2026-01-03 |

### Phase 2: 優先6スキル実装（推定5-6時間）

| 優先度 | スキル | 推定工数 | 担当 |
|--------|--------|---------|------|
| P0 | `/for-genai-validate-cpf` | 1,500行 | TBD |
| P0 | `/for-genai-validate-10x` | 1,500行 | TBD |
| P0 | `/select-ai-tech-stack` | 2,000-2,500行 | TBD |
| P0 | `/create-producthunt-strategy` | 1,800-2,200行 | TBD |
| P0 | `/build-prompt-library` | 1,500-2,000行 | TBD |
| P0 | `/for-genai-discover-demand` | 1,500行 | TBD |

### Phase 3: 残り20スキル実装（推定8-10時間）

| カテゴリ | スキル数 | 推定工数 | 担当 |
|---------|---------|---------|------|
| Batch 1残り | 2スキル | 3,000行 | TBD |
| Batch 2残り | 4スキル | 6,000行 | TBD |
| Batch 3残り | 4スキル | 6,000行 | TBD |
| Phase 2全て | 5スキル | 7,500行 | TBD |
| Orchestration | 1スキル | 2,000行 | TBD |

### Phase 4: コマンドファイル26個作成（推定1-2時間）

| タスク | 推定工数 | 担当 |
|--------|---------|------|
| 26コマンドファイル作成 | 26×100行=2,600行 | TBD |

### Phase 5: Quality Checkpoint（推定1時間）

| タスク | 推定工数 | 担当 |
|--------|---------|------|
| 5次元品質評価 | 1時間 | TBD |
| 品質スコア95/100達成 | - | TBD |

**総推定実行時間**: 15-19時間（並列実行で10-12時間に短縮可能）

---

## 次のアクション

1. **Phase 2開始**: 優先6スキル実装（推定5-6時間）
2. **Phase 3開始**: 残り20スキル実装（推定8-10時間）
3. **Phase 4開始**: コマンドファイル26個作成（推定1-2時間）
4. **Phase 5開始**: Quality Checkpoint（推定1時間）
5. **完成レポート作成**: ForGenAI Edition完成宣言

---

## 統合統計（推定）

| 項目 | 実績値 |
|------|--------|
| **総スキル数** | **26スキル** |
| **統合事例数** | **約100件**（ChatGPT、Claude、Perplexity、Notion AI、Cursor等） |
| **平均品質スコア目標** | **95/100** |
| **推定実行時間** | **10-12時間**（並列実行） |

---

**作成者**: AI Project Manager
**最終更新**: 2026-01-03
**ステータス**: Phase 1完了、Phase 2-5待機中
