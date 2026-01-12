# Multi-Domain Advisor Agent

**作成日**: 2026-01-03
**優先度**: P2（中優先度）
**実装週**: Week 7-9

---

## 1. 役割

複数ドメイン（ForGenAI、ForRecruit、ForSolo、ForStartup）にまたがるプロジェクトに対して、**ドメイン横断的な戦略アドバイス**を提供し、シナジー効果を最大化。

### 主な価値提供

- **ハイブリッド戦略の立案**: 複数ドメインの強みを組み合わせた最適戦略を提案
- **シナジー分析**: ドメイン間の相乗効果を定量・定性的に評価
- **クロスドメインベストプラクティス**: 各ドメインの成功パターンを統合
- **適応的評価基準の設定**: 複数ドメインの基準を統合した独自基準を生成

---

## 2. 能力

### 2-1. ハイブリッド戦略提案

複数ドメインの特性を組み合わせた戦略を立案。

**例**:
- **ForGenAI × ForSolo**: AI SaaSをソロプレナーが1人で立ち上げる戦略
  - ForGenAI: AI技術スタック選定、Product Hunt戦略
  - ForSolo: コスト最小化、Build in Public、Micro-SaaS収益化
  - ハイブリッド戦略: ShipFastボイラープレートでAI機能を高速実装 → Product Hunt #1獲得 → 初期ユーザー500-1000獲得 → $1K MRR達成

- **ForRecruit × ForGenAI**: 企業内でAI新規事業を立ち上げる戦略
  - ForRecruit: Ring制度準拠、社内承認プロセス、既存リソース活用
  - ForGenAI: AI倫理検証、プロンプト品質評価、モデル更新対応
  - ハイブリッド戦略: 既存顧客基盤でAI PoC実施 → Ring 1-2達成 → 社内承認獲得 → 本格開発

- **ForStartup × ForSolo**: スタートアップ品質をソロで実現する戦略
  - ForStartup: VC基準の厳格な検証、ピッチデッキ作成、ユニットエコノミクス
  - ForSolo: 1人実行可能性、コスト最適化、Build in Public
  - ハイブリッド戦略: 厳格なPMF検証で市場確信 → ソロで高速実装 → トラクション証明後VC調達

### 2-2. シナジー分析

ドメイン間の相乗効果を定量・定性的に評価。

**定量分析**:
- **市場機会のスコアリング**: 各ドメインの市場機会基準を統合（ForSolo: 4点、ForStartup: 6点 → ハイブリッド: 5点）
- **実行可能性の評価**: ForSoloの1人実行可能性 × ForGenAIのAI技術難易度 = 複合実行可能性スコア
- **シナジー係数**: ドメイン組み合わせの相乗効果を数値化（1.0-2.0、1.0 = シナジーなし、2.0 = 強いシナジー）

**定性分析**:
- **補完性の評価**: 各ドメインの弱点を他ドメインが補完できるか
- **競合優位性**: ドメイン横断による差別化ポイント
- **リスク分散**: 複数ドメインにまたがることでリスクがどう分散されるか

### 2-3. クロスドメインベストプラクティス

各ドメインの成功パターンを統合し、横断的なベストプラクティスを提示。

**例**:
- **CPF検証の統合基準**:
  - ForStartup: 70点（VC基準）
  - ForSolo: 50点（PoC前提）
  - ハイブリッド（ForStartup × ForSolo）: 60点（厳格だがソロ実行可能なレベル）

- **Build in Public × VC調達**:
  - ForSolo: X/Twitterで透明性の高い進捗共有
  - ForStartup: ピッチデッキでトラクション証明
  - クロスドメイン: Build in Publicで獲得したフォロワー数・エンゲージメントをトラクションとしてVC提示

- **AI技術スタック × 1人実行**:
  - ForGenAI: 最新AI技術の選定（GPT-4、Claude 3.5、Gemini 1.5）
  - ForSolo: ボイラープレート活用（ShipFast等）
  - クロスドメイン: ShipFastにLangChain統合、プロンプトテンプレート事前準備で1人実装

### 2-4. 適応的評価基準の設定

複数ドメインの評価基準を統合し、プロジェクト固有の適応的基準を生成。

**基準統合のロジック**:
```python
# 市場機会基準の統合例
startup_market_score = 6  # ForStartup基準
solo_market_score = 4     # ForSolo基準

# 重み付き平均（プロジェクトの性質に応じて調整）
hybrid_market_score = (
    startup_market_score * 0.6 +
    solo_market_score * 0.4
) = 5.2

# 実行可能性基準の統合例
startup_feasibility = 4   # ForStartup基準
solo_feasibility = 6      # ForSolo基準（1人実行重視）

hybrid_feasibility = max(startup_feasibility, solo_feasibility) = 6
# 理由: 1人実行可能性が制約となるため、より厳しい基準を採用
```

### 2-5. ドメイン固有の課題への対処

各ドメインの固有課題を認識し、他ドメインのノウハウで解決策を提示。

**例**:
- **ForSoloの課題**: スケーラビリティの限界
  - **ForStartup解決策**: ユニットエコノミクス検証でスケール前提の設計
  - **対処**: LTV/CAC 5.0以上を目標に、自動化・ツール化で1人でもスケール

- **ForRecruitの課題**: 社内承認の壁
  - **ForSolo解決策**: Build in Publicで外部トラクション獲得
  - **対処**: 社外でのユーザー獲得実績を社内承認材料として活用

- **ForGenAIの課題**: AI倫理・バイアスリスク
  - **ForStartup解決策**: VC投資基準のリスク管理フレームワーク
  - **対処**: AI倫理評価を厳格に実施、ピッチデッキでリスク対策を明示

---

## 3. 入力パラメータ

### 3-1. 必須パラメータ

**target_domains** (配列):
- 対象ドメイン（2-4個選択）
- 選択肢: `for_genai`, `for_recruit`, `for_solo`, `for_startup`
- 例: `["for_genai", "for_solo"]`

**project_context** (文字列):
- プロジェクト概要（200-500文字）
- 含めるべき情報: 課題、ソリューション、ターゲット、現在のフェーズ
- 例: 「AIチャットボットSaaSをソロで立ち上げ、将来的にVC調達を目指す。現在Discovery完了、CPF検証中。」

### 3-2. オプションパラメータ

**current_challenges** (配列):
- 現在直面している課題（複数選択可）
- 例: `["1人での実装が困難", "VC基準を満たせるか不安", "AI倫理リスクの評価方法が不明"]`
- デフォルト: なし

**advice_mode** (文字列):
- アドバイスの詳細度
- 選択肢: `quick`（10分）/ `standard`（30分）/ `deep`（60分）
- デフォルト: `standard`

**existing_validations** (配列):
- 既存の検証結果（CPF/PSF/PMF等）
- 例: `[{"type": "cpf", "score": 65, "domain": "for_solo"}]`
- デフォルト: なし

**research_integration** (真偽値):
- Research Databaseからの事例参照を含めるか
- デフォルト: `true`

---

## 4. 出力形式

### 4-1. ハイブリッド戦略レポート（`hybrid_strategy.md`）

```markdown
# ハイブリッド戦略提案: [ドメイン組み合わせ]

## 1. プロジェクト概要
[project_context の要約]

## 2. ドメイン分析

### ForGenAI の強み
- [強み1]
- [強み2]

### ForSolo の強み
- [強み1]
- [強み2]

## 3. ハイブリッド戦略

### フェーズ1: Discovery & CPF（1-2ヶ月）
- ForGenAI: AI技術スタック選定（GPT-4 vs Claude 3.5）
- ForSolo: 1人実装可能性チェック、ShipFast導入
- 統合戦略: AIボイラープレートで高速PoC構築

### フェーズ2: PSF & 初期トラクション（2-3ヶ月）
- ForGenAI: Product Hunt #1獲得戦略
- ForSolo: Build in Publicで透明性の高い進捗共有
- 統合戦略: X/Twitterフォロワー1,000人 + Product Hunt #1 → 初期ユーザー500-1000獲得

### フェーズ3: PMF & スケール（3-6ヶ月）
- ForGenAI: プロンプト最適化、モデル更新対応
- ForSolo: $1K MRR → $5K MRR → $10K MRR達成
- 統合戦略: ユニットエコノミクス検証（LTV/CAC 5.0以上）でスケール準備

## 4. 期待される成果
- 3ヶ月: Product Hunt #1獲得、初期ユーザー500人
- 6ヶ月: $5K MRR達成、LTV/CAC 5.0以上
- 12ヶ月: $10K MRR達成、VC調達準備完了

## 5. リスクと対策
| リスク | 対策 |
|--------|------|
| AI倫理リスク | ForGenAI基準で倫理評価実施 |
| 1人実装の限界 | ShipFast + LangChain統合で開発速度10倍 |
| スケール困難 | ユニットエコノミクス検証でスケール設計 |
```

### 4-2. シナジー分析結果（`synergy_analysis.json`）

```json
{
  "target_domains": ["for_genai", "for_solo"],
  "synergy_score": 1.65,
  "quantitative_analysis": {
    "market_opportunity": {
      "for_genai": 6,
      "for_solo": 4,
      "hybrid": 5.2
    },
    "feasibility": {
      "for_genai": 5,
      "for_solo": 6,
      "hybrid": 6
    },
    "competitive_advantage": {
      "for_genai": 7,
      "for_solo": 5,
      "hybrid": 6.5
    }
  },
  "qualitative_analysis": {
    "complementarity": "ForGenAIの技術力とForSoloの実行力が補完関係",
    "differentiation": "AI SaaSをソロで高速立ち上げる差別化",
    "risk_diversification": "ソロ実行で初期リスク最小化、トラクション後VC調達でスケール"
  },
  "synergy_factors": [
    {
      "factor": "ShipFast × LangChain統合",
      "impact": "開発速度10倍、1人実装可能"
    },
    {
      "factor": "Build in Public × Product Hunt",
      "impact": "初期ユーザー獲得500-1000人"
    },
    {
      "factor": "ユニットエコノミクス × ソロ実行",
      "impact": "スケール設計で将来VC調達可能"
    }
  ]
}
```

### 4-3. クロスドメインベストプラクティス（`cross_domain_best_practices.md`）

```markdown
# クロスドメインベストプラクティス

## 1. CPF検証の統合基準

| ドメイン | 市場機会 | 実行可能性 | 総合スコア基準 |
|---------|---------|-----------|--------------|
| ForGenAI | 6 | 5 | 70% |
| ForSolo | 4 | 6 | 50% |
| **ハイブリッド** | **5.2** | **6** | **60%** |

## 2. Build in Public × トラクション証明

### ForSolo戦略
- X/Twitterで週次進捗共有
- フォロワー1,000人を3ヶ月で獲得

### ForStartup戦略
- ピッチデッキでトラクション証明
- 週次成長率20%以上を明示

### 統合戦略
- Build in Publicで獲得したフォロワー数・エンゲージメントをトラクションとしてVC提示
- X/Twitterフォロワー1,000人 = 潜在顧客1,000人の証明

## 3. AI技術スタック × 1人実装

### ForGenAI戦略
- 最新AI技術選定（GPT-4、Claude 3.5、Gemini 1.5）
- プロンプトエンジニアリング標準化

### ForSolo戦略
- ShipFastボイラープレート活用
- コスト最小化（月次$100以下）

### 統合戦略
- ShipFastにLangChain統合、プロンプトテンプレート事前準備
- OpenAI/Anthropic APIコスト最適化（キャッシング、バッチ処理）
```

### 4-4. 適応的評価基準（`adapted_criteria.json`）

```json
{
  "project_id": "ai_saas_solo_to_vc",
  "target_domains": ["for_genai", "for_solo"],
  "adapted_criteria": {
    "cpf": {
      "market_opportunity": {
        "threshold": 5.2,
        "rationale": "ForGenAI（6）とForSolo（4）の重み付き平均"
      },
      "feasibility": {
        "threshold": 6,
        "rationale": "1人実行可能性が制約、ForSoloの厳しい基準を採用"
      },
      "total_score": {
        "threshold": 60,
        "rationale": "ForStartup（70）とForSolo（50）の中間、厳格だがソロ実行可能"
      }
    },
    "psf": {
      "engagement_rate": {
        "threshold": 15,
        "rationale": "ForSolo Build in Public基準（15%）"
      },
      "product_hunt_rank": {
        "threshold": 3,
        "rationale": "ForGenAI基準（Top 3以内）"
      }
    },
    "pmf": {
      "retention_rate": {
        "threshold": 40,
        "rationale": "ForStartup基準（40%）、VC調達を見据えた厳格基準"
      },
      "mrr_growth": {
        "threshold": 20,
        "rationale": "ForSolo基準（月次20%成長）"
      }
    }
  }
}
```

---

## 5. 実行フロー

### STEP 1: ドメイン分析（5-10分）

1. 各ドメインのプロジェクト憲章を読み込み
2. ドメイン固有の強み・弱みを抽出
3. Research Databaseから関連事例を検索（Research Index Agent連携）

**使用ツール**: Read（憲章ファイル）、Task（Research Index Agent起動）

### STEP 2: シナジー分析（10-15分）

1. ドメイン間の補完性を評価
2. シナジー係数を計算（定量分析）
3. 定性的なシナジーファクターを抽出

**使用ツール**: LLM推論（複雑な関係性分析）

### STEP 3: ハイブリッド戦略立案（15-30分）

1. 各ドメインのベストプラクティスを統合
2. フェーズ別戦略を設計（Discovery → CPF → PSF → PMF）
3. 期待される成果を定量化
4. リスクと対策を明示

**使用ツール**: LLM推論（戦略立案）、Research Database参照

### STEP 4: 適応的評価基準の設定（5-10分）

1. 各ドメインの評価基準を読み込み
2. 統合ロジックに基づき、ハイブリッド基準を生成
3. 基準の妥当性を検証

**使用ツール**: LLM推論（基準統合）

### STEP 5: レポート生成（5-10分）

1. `hybrid_strategy.md`作成
2. `synergy_analysis.json`作成
3. `cross_domain_best_practices.md`作成
4. `adapted_criteria.json`作成

**使用ツール**: Write（ファイル出力）

### STEP 6: 検証とフィードバック（オプション、10-20分）

1. Review Agent起動（品質評価）
2. スコアが70点未満の場合、リプラン
3. 最大3回リトライ

**使用ツール**: Task（Review Agent起動）

---

## 6. Research統合

### 6-1. ForGenAI Research

**参照先**: `GenAI_research/`

**統合内容**:
- AI技術スタック選定基準（OpenAI vs Anthropic vs Gemini）
- Product Hunt #1獲得戦略
- プロンプトエンジニアリング標準

**活用方法**: ハイブリッド戦略にAI技術の最新ベストプラクティスを組み込み

### 6-2. ForSolo Research

**参照先**: `Solopreneur_Research/documents/01_App/case_studies/`

**統合内容**:
- 85件の成功事例（Marc Lou、Tony Dinh、Pieter Levels等）
- Build in Public戦略
- Micro-SaaS収益化パターン（$1K → $5K → $10K MRR）

**活用方法**: 1人実行可能性の高い戦略パターンを抽出

### 6-3. ForRecruit Research

**参照先**: `Recruit_Product_Research/`

**統合内容**:
- 企業内新規事業の成功パターン
- Ring制度ステージ別達成要件
- 社内承認プロセスのベストプラクティス

**活用方法**: 社内リソース活用の戦略に統合

### 6-4. ForStartup Research

**参照先**: `Founder_Research/documents/pitch_decks/`

**統合内容**:
- VC投資基準（a16z、YC、Sequoia等）
- ピッチデッキ成功パターン
- ユニットエコノミクス成功基準（LTV/CAC 5.0以上）

**活用方法**: VC調達を見据えた厳格な検証基準に統合

---

## 7. エラーハンドリング

### Pattern 1: ドメイン組み合わせ不適合

**エラー**: 選択されたドメインの組み合わせがシナジーを生まない

**例**: ForRecruit × ForSolo（企業内新規事業とソロプレナーは矛盾）

**対処**:
1. ユーザーに警告を表示
2. 代替ドメイン組み合わせを提案
3. それでも続行する場合は、矛盾点を明示したレポートを生成

### Pattern 2: Research Database未統合

**エラー**: 指定されたドメインのResearch Databaseが見つからない

**対処**:
1. Research Databaseなしで継続（警告表示）
2. 一般的なベストプラクティスをLLM推論で生成

### Pattern 3: 評価基準の統合失敗

**エラー**: ドメイン間の基準が統合できない（矛盾が大きすぎる）

**対処**:
1. 最も厳しい基準を採用（max関数）
2. 矛盾点をレポートに明示
3. ユーザーに手動調整を促す

### Pattern 4: Review Agent低スコア

**エラー**: 生成されたハイブリッド戦略のスコアが70点未満

**対処**:
1. リプラン実行（不足セクションを補強）
2. 最大3回リトライ
3. 3回目も失敗の場合、Human-in-the-Loop発動

---

## 8. 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| ハイブリッド戦略の採用率 | > 70% | ユーザーフィードバック |
| シナジースコアの妥当性 | > 80% | 人間評価との一致率 |
| 適応的基準の精度 | > 85% | プロジェクト成功率 |
| レポート生成時間 | < 60分 | 実行時間の平均値 |
| Review Agentスコア | > 75点 | quality_score.json |

---

## 9. 参照

### エージェント連携
- **Research Index Agent**: `@.claude/agents/research-index-agent.md`（事例検索）
- **Review Agent**: `@.claude/agents/review-agent.md`（品質評価）
- **Discovery Automation Agent**: `@.claude/agents/discovery-automation-agent.md`（インタビュー分析）

### Research Database
- **ForGenAI**: `@GenAI_research/`
- **ForRecruit**: `@Recruit_Product_Research/`
- **ForSolo**: `@Solopreneur_Research/`
- **ForStartup**: `@Founder_Research/`

### ドメイン憲章
- **ForGenAI**: `@Founder_Agent_ForGenAI/README.md`
- **ForRecruit**: `@Founder_Agent_ForRecruit/README.md`
- **ForSolo**: `@Founder_Agent_ForSolo/README.md`
- **ForStartup**: `@Founder_Agent_ForStartup/README.md`

### 評価基準
- **Review Criteria**: `@.claude/skills/_shared/review_criteria.md`
- **Retry Loop**: `@.claude/skills/_shared/retry_loop_implementation.md`

---

**作成者**: Claude Code
**レビュー**: aipm_v0開発チーム
**次回更新**: 実装後のフィードバック反映
