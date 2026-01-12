# Claude Code エージェント一覧

このディレクトリには、aipm_v0で使用可能なSubagentスキルが含まれています。

## エージェント一覧

### PMBOKフェーズ別エージェント

#### 1. Initiating Agent (`initiating-agent.md`)

- **役割**: プロジェクト立ち上げフェーズを支援
- **主な機能**:
  - プロジェクト憲章の作成支援
  - ステークホルダー分析
  - プロダクト定義
- **トリガー**: 「プロジェクト憲章」「ステークホルダー分析」「プロダクト定義」

#### 2. Discovery Agent (`discovery-agent.md`)

- **役割**: UX発見フェーズを支援（Opus推論力を活用）
- **主な機能**:
  - ペルソナ設計
  - ジャーニーマップ作成
  - 仮説マップ構築
  - 課題定義
  - ソリューション定義
  - 検証計画
- **トリガー**: 「ペルソナ作成」「ジャーニーマップ」「仮説マップ」「課題定義」「ソリューション定義」「検証計画」

#### 3. Research Agent (`research-agent.md`)

- **役割**: 調査・分析フェーズを支援
- **主な機能**:
  - 競合調査
  - 市場規模推定
  - デスクリサーチ
  - 顧客調査
- **トリガー**: 「顧客調査」「競合調査」「デスクリサーチ」「市場規模推定」

#### 4. Planning Agent (`planning-agent.md`)

- **役割**: 計画策定フェーズを支援
- **主な機能**:
  - WBS作成
  - PRD（プロダクト要求仕様書）作成
  - バックログ初期化
  - リスク計画
  - ロードマップ作成
- **トリガー**: 「WBS作成」「プロダクトバックログ初期化」「リスク計画」「プロジェクトスコープ記述書」「プロダクト要求仕様書」「ロードマップ作成」

#### 5. Executing Agent (`executing-agent.md`)

- **役割**: 実行フェーズを支援
- **主な機能**:
  - 開発計画作成
  - ストーリー実装支援
  - スプリントゴール管理
- **トリガー**: 「Development」「開発計画作成」「ストーリー実装」「スプリントゴール」

#### 6. Monitoring Agent (`monitoring-agent.md`)

- **役割**: 監視・コントロールフェーズを支援
- **主な機能**:
  - ステータスレポート作成
  - 変更要求管理
  - リスク更新
- **トリガー**: 「ステータスレポート」「変更要求」

#### 7. Closing Agent (`closing-agent.md`)

- **役割**: 終結フェーズを支援
- **主な機能**:
  - レッスンズラーンド作成
  - 移行文書作成
  - 完了報告書
- **トリガー**: 「レッスンズラーンド」「移行文書」

### 機能別エージェント

#### 8. Task Manager Agent (`task-manager.md`)

- **役割**: 日次タスク管理を支援
- **主な機能**:
  - 今日のタスク生成
  - スプリントゴール管理
  - 週次レビュー
  - カレンダー予定確認との連携
- **トリガー**: 「今日のタスク」「作業開始」「カレンダー確認」「今日の予定」

#### 9. Flow Assist Agent (`flow-assist-agent.md`)

- **役割**: アイディア発散を支援
- **主な機能**:
  - ブレインストーミング支援
  - コンセプト生成
  - アイディア発散記録
- **トリガー**: 「アイディア発散」

#### 10. Development Agent (`development-agent.md`)

- **役割**: 開発作業を支援
- **主な機能**:
  - コード生成
  - 実装支援
  - 開発環境セットアップ
  - ソース管理連携
- **トリガー**: 「開発環境初期化」「ストーリー実装」

#### 11. Rule Maintainer Agent (`rule-maintainer.md`)

- **役割**: ルール管理を支援
- **主な機能**:
  - ルール追加・更新
  - 整合性チェック
  - マルチツール同期（Antigravity/Cursor/Codex/Claude Code）
  - フェーズ追加ウィザード
- **トリガー**: 「フェーズ追加」「Phase追加」「新フェーズ作成」

#### 12. Review Agent (`review-agent.md`) ⭐ Task tool対応完了（Week 1）

- **役割**: SubAgent実行結果の品質評価と統合可否判定
- **主な機能**:
  - 5観点品質評価（完全性、論理性、具体性、エビデンス、フレームワーク準拠性）
  - 100点満点評価システム（合格基準: 70点）
  - ドキュメントタイプ別必須セクション検証（cpf_judgment, lean_canvas, pitch_deck等）
  - 品質スコアJSON出力（`quality_score.json`）
  - 詳細レビューレポート生成（`review_report.md`）
  - リトライループ対応（最大3回、自動リプラン）
- **呼び出し方法**: Task tool経由で起動（Manager Skillから自動呼び出し）
- **タイムアウト**: 10分/レビュー
- **年間削減時間**: 50時間
- **参照**: `@.claude/agents/review-agent.md`, `@.claude/skills/_shared/review_criteria.md`

#### 13. Discovery Automation Agent (`discovery-automation-agent.md`) ⭐ 新規（Week 2）

- **役割**: Discoveryフェーズにおけるインタビュー記録の分析を自動化し、ペルソナ・仮説マップ・ジャーニーマップの差分更新を実行
- **主な機能**:
  - インタビュー記録の自動要約・パターン抽出（共通課題・ニーズ・行動パターン）
  - ペルソナドキュメントの差分更新（新たな気づきを追加、矛盾を修正）
  - 仮説マップの自動更新（検証済み仮説をマーク、新規仮説を追加）
  - ジャーニーマップへの気づき反映（新たなタッチポイント・感情変化を追加）
  - インサイトレポート生成（Top 3-5発見事項、定量データ可視化）
- **推奨モデル**: データ収集（haiku）、分析（sonnet）、深い洞察（opus）
- **Research統合**: ForSolo（85件成功事例）、ForRecruit（社内PoC事例）、ForGenAI（プロンプト最適化）
- **成功指標**: 分析速度 < 5分/件、ペルソナ更新精度 > 80%、パターン抽出数 5-10件/インタビュー
- **呼び出し方法**: Task tool経由、またはスラッシュコマンド `/discovery-automation`
- **タイムアウト**: 30分/分析
- **年間削減時間**: 100+時間
- **参照**: `@.claude/agents/discovery-automation-agent.md`, `@.claude/commands/discovery-automation.md`

#### 14. API Integration Agent (`api-integration-agent.md`) ⭐ 新規（Week 2）

- **役割**: 外部サービス（Slack、Notion、GitHub等）との統合を自動化し、エージェント実行完了時の通知・データ登録・Issue作成等を自動実行
- **主な機能**:
  - Slack通知の自動送信（エージェント完了時、Review結果、エラーアラート、定期レポート）
  - Notionデータベースへの自動登録（ペルソナ、CPF/PSF/PMF検証結果、インタビュー記録）
  - GitHub Issue/PR作成（実装タスク管理、ブランチ作成、ラベル・マイルストーン設定）
  - 外部APIからのデータ取得（市場調査API、公的統計API、SNS APIトレンド情報）
  - Webhook統合（イベント駆動型エージェント起動、署名検証）
- **推奨モデル**: 軽量タスク（haiku）、複雑な統合（sonnet）、戦略的設計（opus）
- **成功指標**: Slack通知成功率 > 95%、Notion登録成功率 > 90%、API応答時間 < 3秒
- **エラーハンドリング**: 3回リトライ（指数バックオフ: 1秒、2秒、4秒）、エラー種別別対処
- **呼び出し方法**: Task tool経由、またはスラッシュコマンド `/api-integration`
- **タイムアウト**: 30秒（Slack）、60秒（Notion/GitHub）
- **年間削減時間**: 30+時間
- **参照**: `@.claude/agents/api-integration-agent.md`, `@.claude/commands/api-integration.md`

#### 16. Code Generation Agent (`code-generation-agent.md`) ⭐ 新規（Week 3-4）

- **役割**: Executingフェーズでのプロジェクトコード・テスト・CI/CD設定を自動生成し、開発セットアップを数分で完了
- **主な機能**:
  - コード生成（テンプレートベース: Next.js/React/Vue/FastAPI/Django/LangChain等）
  - テスト自動生成（ユニット/統合/E2Eテストスケルトン）
  - リポジトリ初期化（Git初期化、初回コミット）
  - CI/CDパイプライン設定（GitHub Actions/CircleCI/GitLab CI）
  - デプロイスクリプト生成（Vercel/Heroku/AWS/Docker）
  - 依存関係インストール（npm install / pip install）
  - ビルド・テスト実行確認
- **推奨モデル**: sonnet（バランス重視）、opus（高品質が必要な場合）
- **Research統合**: ForGenAI（AI技術スタック選定基準）、ForSolo（ShipFastボイラープレート）
- **成功指標**: プロジェクト生成成功率 > 90%、ビルド成功率 > 85%、テスト生成カバレッジ > 70%
- **呼び出し方法**: Task tool経由、またはスラッシュコマンド `/code-generation`
- **タイムアウト**: 20分/プロジェクト
- **年間削減時間**: 20+時間
- **参照**: `@.claude/agents/code-generation-agent.md`, `@.claude/commands/code-generation.md`

#### 17. Research Index Agent (`research-index-agent.md`) ⭐ 新規（Week 4-5）

- **役割**: 4ドメイン（ForGenAI/ForRecruit/ForSolo/ForStartup）のResearch統合・セマンティック検索により、関連事例を自動提案
- **主な機能**:
  - セマンティック検索（OpenAI embeddings、コサイン類似度 > 0.7）
  - 自動事例参照提案（CPF検証時に関連事例を提示）
  - Research Database索引の自動生成
  - ドメイン横断検索（ForGenAI × ForSolo等）
  - ケーススタディの要約生成（課題・ソリューション・結果の3行要約）
  - クロスドメインインサイト（複数ドメイン横断時の統合戦略提示）
- **推奨モデル**: haiku（高速検索）、sonnet（要約生成）
- **Research Database**: 400+事例（ForGenAI: 50+、ForRecruit: 30+、ForSolo: 85、ForStartup: 50+）
- **成功指標**: 検索精度 > 80%、検索速度 < 10秒、事例提案採用率 > 50%
- **呼び出し方法**: Task tool経由、またはスラッシュコマンド `/research-index`
- **タイムアウト**: 30秒/検索
- **参照**: `@.claude/agents/research-index-agent.md`, `@.claude/commands/research-index.md`

#### 18. Planning Validation Agent (`planning-validation-agent.md`) ⭐ 新規（Week 5-6）

- **役割**: WBS/Backlog/Roadmapの矛盾検出・整合性チェックにより、計画品質を自動保証
- **主な機能**:
  - WBSとBacklogの整合性チェック（タスクマッピング、優先度・工数確認）
  - スケジュールの実現可能性分析（期間・工数の妥当性、バッファ率確認）
  - リソース割当ギャップ検出（スキルギャップ、負荷分散チェック）
  - 依存関係の循環チェック（DFS: Depth-First Search）
  - クリティカルパスの特定（CPM: Critical Path Method）
  - 矛盾リスト・推奨対処・総合評価スコア（100点満点）のレポート生成
  - 自動修正可能な矛盾の修正版生成
- **推奨モデル**: sonnet（論理的整合性チェック）
- **成功指標**: 矛盾検出率 > 90%、False Positive < 10%、検証時間 < 10分
- **呼び出し方法**: Task tool経由、またはスラッシュコマンド `/planning-validation`
- **タイムアウト**: 10分/検証
- **年間削減時間**: 10+時間
- **参照**: `@.claude/agents/planning-validation-agent.md`, `@.claude/commands/planning-validation.md`

#### 20. Multi-Domain Advisor Agent (`multi-domain-advisor-agent.md`) ⭐ 新規（Week 7-9）

- **役割**: 複数ドメイン（ForGenAI/ForRecruit/ForSolo/ForStartup）を横断したハイブリッド戦略提案・シナジー分析
- **主な機能**:
  - ドメイン分析（各ドメインの強み・弱み抽出）
  - シナジー分析（ドメイン間の相乗効果の定量・定性評価、シナジースコア 1.0-2.0）
  - ハイブリッド戦略立案（複数ドメインの強みを組み合わせた最適戦略）
  - 適応的評価基準設定（複数ドメインの基準を統合した独自基準生成）
  - クロスドメインベストプラクティス（各ドメインの成功パターン統合）
  - 3フェーズ実行計画（Discovery→PSF/初期トラクション→PMF/スケール準備）
- **推奨モデル**: opus（複雑な戦略立案）
- **対応ドメイン組み合わせ**: ForGenAI × ForSolo、ForRecruit × ForGenAI、ForStartup × ForSolo
- **成功指標**: ハイブリッド戦略採用率 > 70%、シナジースコア妥当性 > 80%、適応的基準精度 > 85%
- **呼び出し方法**: Task tool経由、またはスラッシュコマンド `/multi-domain-advisor`
- **タイムアウト**: 60分/戦略立案
- **参照**: `@.claude/agents/multi-domain-advisor-agent.md`, `@.claude/commands/multi-domain-advisor.md`

#### 21. Analytics Dashboard Agent (`analytics-dashboard-agent.md`) ⭐ 新規（Week 9-11）

- **役割**: KPIダッシュボード自動生成・A/Bテスト結果分析・トレンド予測により、データ駆動意思決定を支援
- **主な機能**:
  - KPI計算（AARRR指標: Acquisition、Activation、Retention、Revenue、Referral）
  - ダッシュボード生成（インタラクティブHTML: Plotly.js、PDF、Notion埋め込み）
  - A/Bテスト分析（統計的有意性検定: t-test、chi-square、効果量: Cohen's d、信頼区間）
  - トレンド分析（移動平均、季節性分解、異常値検出、成長率計算）
  - 予測モデル構築（Prophet、ARIMA、SARIMA、LightGBM、次30-180日の予測）
  - Pythonコード自動生成（prediction_model.py、再現可能な予測パイプライン）
- **推奨モデル**: sonnet（バランス型）
- **統計基準**: p < 0.05（統計的有意性）、Cohen's d > 0.3（実務的有意性）、R² > 0.7（予測精度）
- **成功指標**: ダッシュボード生成成功率 > 95%、A/Bテスト分析精度 > 90%、予測モデルR²スコア > 0.7
- **呼び出し方法**: Task tool経由、またはスラッシュコマンド `/analytics-dashboard`
- **タイムアウト**: 30分/分析
- **参照**: `@.claude/agents/analytics-dashboard-agent.md`, `@.claude/commands/analytics-dashboard.md`

#### 22. Customer Feedback Agent (`customer-feedback-agent.md`) ⭐ 新規（Week 11-12）

- **役割**: NPS計算・コホート分析・センチメント分析・フィードバック優先順位付けにより、PMF改善を加速
- **主な機能**:
  - NPS計算（Net Promoter Score: (Promoters% - Detractors%) × 100）
  - セグメント別NPS（無料/有料プラン、流入元、利用期間）
  - コホート分析（登録月別・プラン別・流入元別の満足度・チャーン率分析、30d/60d/90d/180dリテンション）
  - センチメント分析（フィードバックの感情分析: -1.0 〜 +1.0、カテゴリ別集計: UI/UX、機能、価格、サポート）
  - 優先順位付け（影響度 × 0.5 + 緊急度 × 0.3 + センチメント × 0.2、期待効果の定量化）
  - レポート生成（nps_report.md、cohort_analysis.json、sentiment_analysis.json、priority_feedback.md）
- **推奨モデル**: sonnet（バランス型）
- **NPS基準値**: ForSolo (40)、ForStartup (50)、ForRecruit (60)
- **成功指標**: NPS計算精度 100%、センチメント分析精度 > 85%、優先順位付け妥当性 > 80%
- **呼び出し方法**: Task tool経由、またはスラッシュコマンド `/customer-feedback`
- **タイムアウト**: 30分/分析
- **参照**: `@.claude/agents/customer-feedback-agent.md`, `@.claude/commands/customer-feedback.md`

### 専門領域エージェント

#### 19. Deep Research to Note Agent (`deep_research_to_note.md`) ⭐新規

- **役割**: 学術論文やテクニカルドキュメントに対する高速かつ深い理解を実現し、落合陽一式の6つの質問に基づくA4 1枚サマリーを作成
- **主な機能**:
  - 論文PDF構造解析（Abstract, Conclusion, Experiments, Related Work等のセクション特定）
  - 戦略的読解順序による逆順アプローチ（Abstract→Conclusion→Experiments→Related Work）
  - 落合フォーマット6つの質問への自動回答生成
  - A4 1枚相当の圧縮要約作成（800-1200単語、図表1-3点含む）
  - Notionデータベース連携による論文管理（タグ自動生成、引用ネットワーク構築）
  - 次に読むべき論文の推薦（References分析と引用頻度ランキング）
  - 週次進捗管理（週25-100本の読了トラッキング）
- **トリガー**: 「ディープリサーチ」「落合式リサーチ」「論文サマリー作成」「6つの質問」「研究サーベイ」
- **参照**: `@.claude/rules/deep_research_to_note.md`（作成予定）

## 使い方

### 基本的な呼び出し方法

#### 1. トリガーワードを使用

会話の中でトリガーワードを含めることで、対応するエージェントが自動的に起動します。

**例**:
```
「プロジェクト憲章を作成してください」
→ Initiating Agentが起動し、プロジェクト憲章作成のための質問を開始

「ディープリサーチを実行してください」
→ Deep Research to Note Agentが起動し、論文サマリー作成を支援

「今日のタスクを確認したい」
→ Task Manager Agentが起動し、daily_tasks.mdを生成

「ペルソナ作成」
→ Discovery Agentが起動し、ペルソナ設計のための質問を開始
```

#### 2. エージェント名を明示的に指定（将来的に実装予定）

```
例: 「@research-agent 競合調査を実施してください」
例: 「@deep-research-to-note-agent 論文サマリーを作成してください」
```

#### 3. Task tool経由での起動（Review Agent等）

一部のエージェント（Review Agent等）は、Manager SkillからTask tool経由で起動されます。

**基本パターン**:
```python
result = Task(
    description="品質レビュー",
    prompt="""
    @.claude/agents/review-agent.md の仕様に従い、以下のドキュメントをレビューしてください。

    - ドキュメントパス: {document_path}
    - ドキュメントタイプ: {document_type}
    - イテレーション: {iteration}

    5観点で評価し、quality_score.json と review_report.md を出力してください。
    """,
    subagent_type="general-purpose",
    model="sonnet"
)
```

**モデル選択ガイド**:
- `haiku`: データ収集、軽量タスク（高速、低コスト）
- `sonnet`: 標準分析、レビュー、バランス型（推奨デフォルト）
- `opus`: 戦略立案、複雑な分析（最高品質）

**並列実行**:
複数のエージェントを並列起動する場合、単一メッセージ内で複数のTask呼び出しを実行：
```python
# 3エージェント同時起動
results = [
    Task(description="データ収集", prompt=..., model="haiku"),
    Task(description="分析", prompt=..., model="sonnet"),
    Task(description="レポート生成", prompt=..., model="sonnet")
]
```

詳細は `@.claude/rules/parallel_execution.md` を参照。

### 成果物の確定フロー

エージェントが生成したドラフトファイルは、`Flow/YYYYMM/YYYY-MM-DD/` 配下に保存されます。

内容を確認し、問題なければ以下のコマンドで確定版として Stock へ移動できます。

```
「確定反映して」
```

これにより、`Stock/programs/.../documents/[phase]/` へファイルが移動されます。

### ディレクトリ構造

```
.claude/
├── agents/           # エージェントスキルファイル（本ディレクトリ）
│   ├── initiating-agent.md
│   ├── discovery-agent.md
│   ├── research-agent.md
│   ├── planning-agent.md
│   ├── executing-agent.md
│   ├── monitoring-agent.md
│   ├── closing-agent.md
│   ├── task-manager.md
│   ├── flow-assist-agent.md
│   ├── development-agent.md
│   ├── rule-maintainer.md
│   ├── review-agent.md ⭐ Task tool対応完了（Week 1）
│   ├── discovery-automation-agent.md ⭐ Week 2新規
│   ├── api-integration-agent.md ⭐ Week 2新規
│   ├── code-generation-agent.md ⭐ Week 3-4新規
│   ├── research-index-agent.md ⭐ Week 4-5新規
│   ├── planning-validation-agent.md ⭐ Week 5-6新規
│   ├── multi-domain-advisor-agent.md ⭐ Week 7-9新規
│   ├── analytics-dashboard-agent.md ⭐ Week 9-11新規
│   ├── customer-feedback-agent.md ⭐ Week 11-12新規
│   ├── deep_research_to_note.md ⭐新規
│   └── README.md（本ファイル）
├── commands/         # スラッシュコマンドファイル
│   ├── discovery-automation.md ⭐ Week 2新規
│   ├── api-integration.md ⭐ Week 2新規
│   ├── code-generation.md ⭐ Week 3-4新規
│   ├── research-index.md ⭐ Week 4-5新規
│   ├── planning-validation.md ⭐ Week 5-6新規
│   ├── multi-domain-advisor.md ⭐ Week 7-9新規
│   ├── analytics-dashboard.md ⭐ Week 9-11新規
│   ├── customer-feedback.md ⭐ Week 11-12新規
│   └── ...
└── rules/            # 詳細ルールファイル
    ├── pmbok_initiating.md
    ├── pmbok_discovery.md
    ├── pmbok_research.md
    ├── pmbok_planning.md
    ├── pmbok_executing.md
    ├── pmbok_monitoring.md
    ├── pmbok_closing.md
    ├── task_management.md
    ├── flow_assist.md
    ├── development.md
    ├── rule_maintenance.md
    ├── review_loop.md ⭐ Task tool統合完了（Week 1）
    └── deep_research_to_note.md ⭐新規（作成予定）
```

### エージェント拡張ルール

新しいエージェントスキルを追加する場合：

#### 1. エージェントファイル作成 (`.claude/agents/`配下)

3セクション構造で記述：

```markdown
# [エージェント名] Agent

## 役割
[エージェントの役割を1-2行で簡潔に記述]

## 能力
- [能力1]
- [能力2]
- [能力3]

## 参照
- @.claude/rules/[対応するルールファイル].md
```

軽量アプローチ（詳細はルールファイルに委譲）を採用してください。

#### 2. ルールファイル作成 (`.claude/rules/`配下)

詳細な実行手順、トリガーワード、質問セット、テンプレートを定義：

```markdown
# [エージェント名] Rules

[エージェントの詳細説明]

## トリガー
- 「[トリガーワード1]」「[トリガーワード2]」

## 参照
- @.cursor/rules/basic/[番号]_[ルールファイル].mdc
```

#### 3. README.md更新

本ファイルに新規エージェントを追記してください。

## PMBOKフェーズとの対応

| フェーズ | エージェント | 主要トリガー |
|----------|--------------|--------------|
| 立ち上げ | Initiating Agent | プロジェクト憲章、ステークホルダー分析 |
| 発見 | Discovery Agent | ペルソナ、ジャーニーマップ、仮説マップ |
| 調査 | Research Agent | 競合調査、市場規模推定 |
| 計画 | Planning Agent | WBS、PRD、バックログ初期化 |
| 実行 | Executing Agent | 開発計画、ストーリー実装 |
| 監視 | Monitoring Agent | ステータスレポート、変更要求 |
| 終結 | Closing Agent | レッスンズラーンド、移行文書 |

## 参考資料

- **プロジェクト概要**: `@docs/ai/overview.md`
- **PMBOKワークフロー**: `@docs/ai/pmbok_workflow.md`
- **CLAUDE.md**: `@CLAUDE.md`
- **パス管理規約**: `@.claude/rules/path_conventions.md`

## マルチツール対応

このリポジトリは以下のAIツールで共通運用できます：

- **Antigravity** - 主軸ツール
- **Cursor** - 既存.mdcルール活用
- **Codex** - Skills経由
- **Claude Code** - Subagents経由（本ディレクトリ）

各ツール固有の設定ファイルは、対応するディレクトリを参照してください：

- Antigravity: `.agent/`
- Cursor: `.cursor/rules/`
- Codex: `.codex/`
- Claude Code: `.claude/`（本ディレクトリ）

## 運用Tips

### エージェントの選択基準

- **プロジェクト立ち上げ時**: Initiating Agent
- **ユーザー理解・課題発見**: Discovery Agent
- **インタビュー分析自動化**: Discovery Automation Agent ⭐ Week 2実装（年間100+時間削減）
- **市場・競合分析**: Research Agent
- **計画策定**: Planning Agent
- **計画品質チェック**: Planning Validation Agent ⭐ Week 5-6実装（WBS/Backlog矛盾検出）
- **開発・実装**: Executing Agent + Development Agent
- **コード生成・プロジェクト初期化**: Code Generation Agent ⭐ Week 3-4実装（年間20+時間削減）
- **進捗管理**: Monitoring Agent
- **振り返り**: Closing Agent
- **日々のタスク管理**: Task Manager Agent
- **アイディア出し**: Flow Assist Agent
- **ルール追加・更新**: Rule Maintainer Agent
- **品質管理・レビュー**: Review Agent ⭐ Week 1実装（Manager Skillから自動起動）
- **外部サービス統合**: API Integration Agent ⭐ Week 2実装（Slack/Notion/GitHub連携）
- **事例検索・Research活用**: Research Index Agent ⭐ Week 4-5実装（400+事例のセマンティック検索）
- **ドメイン横断戦略・ハイブリッド戦略**: Multi-Domain Advisor Agent ⭐ Week 7-9実装（ForGenAI × ForSolo等）
- **KPIダッシュボード・A/Bテスト分析**: Analytics Dashboard Agent ⭐ Week 9-11実装（AARRR指標、統計分析、予測モデル）
- **NPS分析・コホート分析・フィードバック優先順位付け**: Customer Feedback Agent ⭐ Week 11-12実装（PMF改善加速）
- **論文・技術調査**: Deep Research to Note Agent ⭐新規

### 複数エージェントの組み合わせ

エージェントは独立して動作しますが、フェーズを跨いで連携することも可能です。

**例**:
1. Discovery Agent でペルソナを作成
2. Research Agent で市場規模を推定
3. Planning Agent でWBSとPRDを作成
4. Executing Agent で開発を実行
5. Monitoring Agent で進捗をトラッキング
6. Closing Agent でレッスンズラーンドを記録

## 更新履歴

- **2026-01-03**: Week 7-12実装完了（Multi-Domain Advisor + Analytics Dashboard + Customer Feedback Agent）
  - Multi-Domain Advisor Agent追加（20番目のエージェント）
    - ドメイン横断戦略提案・シナジー分析（ForGenAI × ForSolo、ForRecruit × ForGenAI、ForStartup × ForSolo）
    - シナジースコア計算（1.0-2.0）、適応的評価基準設定
    - ハイブリッド戦略3フェーズ実行計画
    - シナジースコア妥当性目標: 80%以上
  - Analytics Dashboard Agent追加（21番目のエージェント）
    - KPIダッシュボード自動生成（AARRR指標、Plotly.js、Prophet予測モデル）
    - A/Bテスト統計分析（t-test、chi-square、Cohen's d、信頼区間）
    - トレンド分析・予測モデル構築（ARIMA、SARIMA、LightGBM）
    - 予測精度目標: R² > 0.7
  - Customer Feedback Agent追加（22番目のエージェント）
    - NPS計算・セグメント別分析（無料/有料プラン、流入元、利用期間）
    - コホート分析（登録月別・プラン別・流入元別、30d/60d/90d/180dリテンション）
    - センチメント分析（-1.0 〜 +1.0、カテゴリ別: UI/UX、機能、価格、サポート）
    - フィードバック優先順位付け（影響度 × 0.5 + 緊急度 × 0.3 + センチメント × 0.2）
  - スラッシュコマンド3件追加（`/multi-domain-advisor`, `/analytics-dashboard`, `/customer-feedback`）
  - 合計21エージェント（Week 1: +1, Week 2: +2, Week 3-6: +3, Week 7-12: +3）
- **2026-01-03**: Week 3-6実装完了（Code Generation + Research Index + Planning Validation Agent）
  - Code Generation Agent追加（16番目のエージェント）
    - プロジェクトコード・テスト・CI/CD設定の自動生成
    - フレームワーク対応（Next.js/React/Vue/FastAPI/Django/LangChain等）
    - Research統合（ForGenAI: AI技術スタック、ForSolo: ShipFastボイラープレート）
    - 年間削減時間: 20+時間
  - Research Index Agent追加（17番目のエージェント）
    - 4ドメイン（ForGenAI/ForRecruit/ForSolo/ForStartup）のセマンティック検索
    - 400+事例のResearch Database統合
    - クロスドメインインサイト自動生成
    - 検索精度目標: 80%以上、検索速度: 10秒以内
  - Planning Validation Agent追加（18番目のエージェント）
    - WBS/Backlog/Roadmap矛盾検出・整合性チェック
    - クリティカルパス特定（CPM）、循環依存検出（DFS）
    - 自動修正提案生成
    - 年間削減時間: 10+時間
  - スラッシュコマンド3件追加（`/code-generation`, `/research-index`, `/planning-validation`）
  - Deep Research to Note Agentの番号を#15→#19に変更
  - 合計18エージェント（Week 1: +1, Week 2: +2, Week 3-6: +3）
- **2026-01-03**: Week 2実装完了（Discovery Automation Agent + API Integration Agent）
  - Discovery Automation Agent追加（13番目のエージェント）
    - インタビュー分析自動化、ペルソナ/仮説マップ/ジャーニーマップ差分更新
    - Research統合（ForSolo: 85件、ForRecruit、ForGenAI）
    - 年間削減時間: 100+時間
  - API Integration Agent追加（14番目のエージェント）
    - Slack/Notion/GitHub統合自動化
    - エラーハンドリング・リトライポリシー実装
    - 年間削減時間: 30+時間
  - スラッシュコマンド2件追加（`/discovery-automation`, `/api-integration`）
  - 合計15エージェント（Week 1: +1, Week 2: +2）
- **2026-01-03**: Review Agent Task tool統合完了（Week 1実装完了）
  - Task tool経由での起動パターン追加
  - モデル選択ガイド・並列実行パターン記載
  - Manager Skillからの自動呼び出し対応
  - テスト検証完了（高品質: 100点、低品質: 34点、欠落: 15.425点）
  - 年間削減時間: 50時間
  - 合計13エージェント（Review Agent追加）
- **2025-12-31**: README.md初版作成、Deep Research to Note Agent追加（12個目のエージェント）
- 既存11エージェント + 新規10エージェント = **合計21エージェント**
- **年間削減時間総計**: 210+時間（Review: 50h, Discovery: 100h, API: 30h, Code Generation: 20h, Planning Validation: 10h）
  - ※ Week 7-12エージェント（Multi-Domain Advisor、Analytics Dashboard、Customer Feedback）は品質向上目的のため削減時間には未計上

---

aipm_v0 - PMBOK × Lean UX × Agile ハイブリッドプロジェクト管理システム
