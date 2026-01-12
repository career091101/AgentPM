---
name: sns-automation
description: |
  Phase 1-4のSNS自動化全工程を実行するオーケストレータースキル。
  データ収集→分析→投稿生成→Late API予約投稿の全工程を自動化します。

  実行フロー:
  - Phase 1: データ収集（12-22分、5並列最適化版）
  - Phase 2: 分析・調査（35-55分、逐次実行 1→1.5→2→3、フィルタリング追加）
  - Phase 3: 投稿生成（15-20分、高野式7パターン + X/Threads派生）
  - Phase 4: マルチプラットフォーム予約投稿（5-10分、Late API、6投稿自動化）

  所要時間: 67-107分（Phase 2フィルタリング追加により+5-10分）
  出力: 各フェーズの成果物 + final_summary.md

  投稿先（Option C対応）:
  - LinkedIn: 1案/日（8:00 JST）
  - X: 3投稿/日（派生7:30 + スレッド12:00 + スレッド20:00）
  - Threads: 2投稿/日（派生7:30 + 新規20:00）
  - 合計: 6投稿/日

trigger_keywords:
  - "SNS自動化"
  - "SNS全工程実行"
  - "投稿自動化"

stage: Phase 1-4 Orchestration
dependencies:
  - collect-x-timeline
  - extract-top-tweets
  - scrape-tweet-details
  - extract-content
  - filter-extracted-content  # Phase 2.15: AI関連コンテンツフィルタリング
  - analyze-replies
  - research-topic
  - generate-sns-posts-takano  # 高野式7パターン + X/Threads派生（v2.4）
  - approve-and-schedule

output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/sns_automation_summary.md
execution_time: 67-107分
priority: P0
model: claude-sonnet-4-5-20250929  # Sonnet 4.5 (2026年1月時点の最新モデル)
---

# SNS Automation Skill - Phase 1-4統合版

Phase 1-4のSNS自動化全工程を実行するオーケストレータースキル。

**Version**: 2.0（Option C対応版 - X/Threads投稿数増加）

---

## 📖 重要: 最初に読むべきドキュメント

### 全サブスキル共通情報

**必読**: [@sns_automation_shared_context.md](./sns_automation_shared_context.md)

このファイルには以下の共通情報が記載されています（**並列実行時の重複読み込みを防ぐため、最初に1回のみ読み込んでください**）:
- プロジェクト概要・ターゲットオーディエンス
- 実行フロー全体像
- 共通ファイルパス・命名規則
- 品質基準（高野メソッド7要素）
- エラーハンドリング基本方針
- Late API設定
- 出力フォーマット

### ドキュメント構造

このSKILL.mdは以下の構造で記述されています：

- **Core セクション** - 実行に必須の情報（Phase 1-4の概要）
- **Extended セクション** - オプショナル詳細（評価基準、進捗表示等）

詳細情報は外部ファイルに分離されており、必要時のみ参照してください。

---

# 🎯 Core Section - 実行に必須の情報

このセクションには、スキル実行に必要な最小限の情報が記載されています。

---

## このSkillでできること

1. **Phase 1: データ収集**（5並列最適化版、12-22分）
   - Xタイムライン収集（200件）
   - Top 10ツイート抽出
   - ツイート詳細取得（リンク・リプライ、5並列処理）

2. **Phase 2: 分析・調査**（逐次実行 1→1.5→2→3、35-55分）
   - STEP 2.1: コンテンツ抽出（記事・YouTube・PDF、AI関連度スコア付与）
   - STEP 2.15: コンテンツフィルタリング（AI関連のみ抽出、非AI関連除外）
   - STEP 2.2: リプライ分析（インサイト抽出）※データなし時スキップ
   - STEP 2.3: Web調査（ファクトチェック・専門家意見）

3. **Phase 3: 投稿生成**（順次実行、15-20分）
   - 高野式7パターンからAIが最適3パターン自動選択
   - LinkedIn投稿3案生成（厳格チェックリスト検証）
   - X/Threads派生投稿生成（Option C対応）:
     - X派生（Top 1トピック、フック変更）
     - Xスレッド1（Top 2トピック、5-7ツイート深掘り型）
     - Xスレッド2（Top 3トピック、5-7ツイート深掘り型）
     - Threads派生（Top 1トピック、フック変更）
     - Threads新規（Top 2トピック、LinkedIn似表現）

4. **Phase 4: マルチプラットフォーム予約投稿**（順次実行、5-10分）
   - Late API既存予約との競合検出（4時間帯: 7:30, 8:00, 12:00, 20:00）
   - 6投稿を同一日に分散予約（Late API経由）:
     - LinkedIn: 8:00 JST（高野式メイン）
     - X派生: 7:30 JST
     - Xスレッド1: 12:00 JST
     - Xスレッド2: 20:00 JST
     - Threads派生: 7:30 JST
     - Threads新規: 20:00 JST
   - 失敗投稿のフォールバック（Markdown生成）

5. **最終サマリー生成**
   - 各フェーズの実行時間
   - 成果物一覧
   - 投稿結果（URL、ステータス）

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | なし（完全自動実行） |
| **出力** | 各フェーズの成果物 + final_summary.md |
| **次のアクション** | 投稿結果の確認、パフォーマンス分析 |

---

## Instructions

**実行モード**: 完全自律実行（人間介入なし）
**推定所要時間**: 62-97分
**日次投稿数**: 6投稿（LinkedIn 1 + X 3 + Threads 2）

---

### Phase 1: データ収集（5並列最適化版、12-22分）

**概要**: Xタイムラインから200件を収集し、AI関連度と高野式適合度でTop 10を抽出。詳細リンク・リプライを5並列処理で取得。

**主要ステップ**:
- STEP 1.1: Xタイムライン収集（5-10分）
- STEP 1.2: Top 10抽出・並列評価（5-8分）
- STEP 1.3: ツイート詳細取得・5並列処理（2-4分）

**詳細手順**: [@phases/phase1_detailed.md](./phases/phase1_detailed.md)

**エラーハンドリング**: 即時停止（[@_shared/error_handling_patterns.md](../_shared/error_handling_patterns.md)参照）

---

### Phase 2: 分析・調査（逐次実行、30-45分）

**概要**: Phase 1データから記事・YouTube・PDFコンテンツを抽出し、リプライを分析。トピックのWeb調査でファクトチェック実施。

**主要ステップ**:
- STEP 2.1: コンテンツ抽出（5-10分）
- STEP 2.2: リプライ分析（10-15分、データなし時スキップ）
- STEP 2.3: Web調査（15-20分）

**詳細手順**: [@phases/phase2_detailed.md](./phases/phase2_detailed.md)

**エラーハンドリング**: STEP 2.1, 2.3成功必須（[@_shared/error_handling_patterns.md](../_shared/error_handling_patterns.md)参照）

---

### Phase 3: 投稿生成（順次実行、15-20分）

**概要**: 高野式7パターンからAIが最適3パターン選択。LinkedIn 3案＋X/Threads派生投稿を生成。

**主要ステップ**:
- STEP 3.1: 高野式7パターン投稿3案生成（LinkedIn、10-15分）
- STEP 3.2: X/Threads派生投稿生成（5分、Option C対応）
  - X派生: LinkedIn→フック変更（280文字）
  - Xスレッド1: Top 2トピック深掘り（5-7ツイート）
  - Xスレッド2: Top 3トピック深掘り（5-7ツイート）
  - Threads派生: LinkedIn→フック変更（500文字）
  - Threads新規: Top 2トピック（500文字）

**詳細手順**: [@phases/phase3_detailed.md](./phases/phase3_detailed.md)、[@generate-sns-posts-takano/SKILL.md](./generate-sns-posts-takano/SKILL.md)

**エラーハンドリング**: チェックリスト未達時は自動再生成（[@_shared/error_handling_patterns.md](../_shared/error_handling_patterns.md)参照）

---

### Phase 4: マルチプラットフォーム予約投稿（Late API、競合回避型、5-10分）

**概要**: Late APIから既存予約を検出し、4時間帯（7:30, 8:00, 12:00, 20:00）で競合を回避。6投稿を同一日に時間帯別予約投稿。

**主要ステップ**:
- STEP 4.0: 既存予約の競合検出（全4時間帯、30秒）
- STEP 4.1: 利用可能日付検索（全時間帯で空いている日、30秒）
- STEP 4.2: コンテンツ抽出（6投稿分、1-2分）
- STEP 4.3: Late API予約投稿（6投稿個別POST、2-5分）

**投稿スケジュール（Option C）**:
| 時刻 | プラットフォーム | 投稿タイプ |
|------|----------------|-----------|
| 7:30 | X | 派生（Top 1） |
| 7:30 | Threads | 派生（Top 1） |
| 8:00 | LinkedIn | 高野式メイン（Top 1） |
| 12:00 | X | スレッド深掘り（Top 2） |
| 20:00 | X | スレッド深掘り（Top 3） |
| 20:00 | Threads | 新規（Top 2） |

**投稿スクリプト**: `scripts/late_api_multi_post_v2.py`

**スキル参照**: [@post-multiplatform/SKILL.md](../post-multiplatform/SKILL.md)

**詳細手順**: [@phases/phase4_detailed.md](./phases/phase4_detailed.md)

**エラーハンドリング**: Late API失敗投稿はMarkdownファイル生成（[@_shared/error_handling_patterns.md](../_shared/error_handling_patterns.md)参照）

---

## エラーハンドリング

### 基本方針

| フェーズ | エラー時の対応 | 理由 |
|---------|--------------|------|
| **Phase 1** | **即時停止** | 後続処理が全て依存するため必須 |
| **Phase 2** | **即時停止（全タスク成功必須）** | 品質重視 |
| **Phase 3** | **即時停止** | 投稿生成は最重要 |
| **Phase 4** | **即時停止** | 投稿は最終成果物 |

### 詳細なエラーハンドリング

リトライ戦略、エラーレスポンス形式、パターン別対応は以下を参照：

📖 **[@_shared/error_handling_patterns.md](../_shared/error_handling_patterns.md)**

**スキル固有のエラー処理**:
- **Cookie認証失敗**: ユーザーに再ログイン依頼 + 停止
- **Late APIエラー**: [@phases/phase4_detailed.md#Late API統合詳細](./phases/phase4_detailed.md#late-api統合詳細)参照

---

## 実行フロー全体図

```
┌─────────────────────────────────────────────┐
│ Phase 1: データ収集（5並列処理、12-22分）    │
├─────────────────────────────────────────────┤
│ 1.1 Xタイムライン収集 (5-10分)              │
│   → x_timeline_{date}.json (200件)         │
│        ↓ (並列処理 STEP 1.2)                │
│ 1.2 Top 10抽出 (5-8分)                     │
│   → top_10_tweets_{date}.json (10件)       │
│        ↓ (5並列処理 STEP 1.3)               │
│ 1.3 ツイート詳細取得 (2-4分)                │
│   → tweet_details_{date}.json             │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Phase 2: 分析・調査（逐次実行、30-45分）     │
├─────────────────────────────────────────────┤
│ 2.1 コンテンツ抽出 (5-10分)                 │
│   → extracted_contents_{date}.json        │
│                    ↓                        │
│ 2.2 リプライ分析 (10-15分, スキップ可)     │
│   → reply_insights_{date}.json            │
│                    ↓                        │
│ 2.3 Web調査 (15-20分)                      │
│   → research_findings_{date}.json         │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Phase 3: 投稿生成（順次実行、10-15分）      │
├─────────────────────────────────────────────┤
│ 3.1 高野式7パターン3案生成                   │
│   - AI自動選択: 最適3パターン               │
│   - チェックリスト検証: 全7項目必須         │
│   → posts_generated_takano_{date}.md     │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Phase 4: LinkedIn予約投稿（自動実行、2-5分）│
├─────────────────────────────────────────────┤
│ 4.0 既存予約の競合検出                      │
│ 4.1 利用可能日付検索                        │
│ 4.2 コンテンツ抽出                          │
│ 4.3 Late API予約投稿（3案、異なる日付）    │
│   → late_api_fixed_{date}.json            │
│   → manual_posts/linkedin_*.md (失敗案)   │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Phase 5: 最終サマリー生成（1-2分）          │
├─────────────────────────────────────────────┤
│ final_summary.md生成                        │
└─────────────────────────────────────────────┘
```

---

# 📚 Extended Section - オプショナル詳細情報

このセクションには、出力フォーマット、評価基準、詳細設定などの補足情報が記載されています。

**通常の実行では参照不要**です。カスタマイズや詳細確認が必要な場合のみ参照してください。

---

## Knowledge Base参照

- **Task tool使用例**: `.claude/skills/orchestrate-review-loop/SKILL.md`
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`
- **並列実行ルール**: `.claude/rules/parallel_execution.md`
- **Phase別詳細**: `.claude/skills/sns-automation/phases/phase{N}_detailed.md`
- **Late API統合提案**: `Flow/202601/2026-01-02/late_api_integration_proposals.md`
- **Late API実装**: `Stock/programs/副業/projects/SNS/scripts/late_api_post.py`
- **本番テストレポート**: `Stock/programs/副業/projects/SNS/PRODUCTION_TEST_REPORT_20260102.md`
- **進捗管理**: `Stock/programs/副業/projects/SNS/PROGRESS.md`

---

## 推定コスト

### LLMコスト（ClaudeCode）

- Phase 1: $0.05（haiku 15分）
- Phase 2: $0.30（haiku+sonnet逐次）
- Phase 3: $0.80（opus 25分）
- Phase 4: $0.03（haiku 5分）
- **合計**: 約$1.18/実行

### Late APIコスト（月額）

| プラン | 料金 | レート制限 | 推奨用途 |
|--------|------|----------|---------|
| **Free** | $0 | 60リクエスト/分 | 検証・テスト |
| **Starter** | $19 | 120リクエスト/分 | 個人利用 |
| **Pro** | $49 | 300リクエスト/分 | 週3-5投稿（推奨★★★★★） |
| **Unlimited** | $99 | 1,200リクエスト/分 | 大量投稿 |

**推奨**: Proプラン（$49/月）- 週3投稿×12プラットフォーム対応可能

### 総コスト試算

- LLM: $1.18/実行 × 3回/週 = **$14.16/月**
- Late API: **$49/月**（Proプラン）
- **月額合計**: 約$63.16

---

## 使用例

```
User: /sns-automation

Skill:
# SNS自動化実行開始

推定所要時間: 62-95分
開始時刻: 2026-01-02 10:00:00

## Phase 1: データ収集（15-25分）

✅ 1.1 Xタイムライン収集完了（5分）
   → x_timeline_20260102.json (200件)

✅ 1.2 Top 10抽出完了（3分）
   → top_10_tweets_20260102.json (10件)

✅ 1.3 ツイート詳細取得完了（8分）
   → tweet_details_20260102.json (リンク12件、リプライ40件)

---

## Phase 2: 分析・調査（35-55分、逐次実行 1→1.5→2→3）

✅ 2.1 コンテンツ抽出完了（8分）
   → extracted_contents_20260102.json (成功率91.7%, 1,322ワード, AI関連度スコア付与済み)

✅ 2.15 コンテンツフィルタリング完了（6分）
   → extracted_contents_filtered_20260102.json (AI関連のみ、保持率75%)
   → non_ai_contents_20260102.json (除外コンテンツ3件)

✅ 2.2 リプライ分析スキップ（データなし）

✅ 2.3 Web調査完了（18分）
   → research_findings_20260102.json (30ソース, 7ファクトチェック)

---

## Phase 3: 投稿生成（10-15分）

✅ 入力タイプ判定: Phase 2統合データ
✅ 最適パターン選択:
   - 案1: パターン3（ニュース引用 → 深掘り）
   - 案2: パターン1（断定型主張 → データ展開）
   - 案3: パターン4（リスト型衝撃ファクト）

✅ 3.1 高野式7パターン投稿3案生成完了（12分）
   → posts_generated_takano_20260102.md
   - 使用パターン: 3, 1, 4
   - チェックリスト: 全案7項目達成
   - 最推奨: 案1（予測ER 4.2%）

---

## Phase 4: LinkedIn予約投稿（2-5分）

✅ 4.0 既存予約検出: 8件、8:00 AM予約済み日付5日間
✅ 4.1 利用可能日付検索: 2026-01-11, 01-12, 01-13
✅ 4.2 コンテンツ抽出: 3案完了
✅ 4.3 Late API予約投稿完了（2分）
   - 案1: ✅ 予約完了（post_id: 67abc123...）
   - 案2: ✅ 予約完了（post_id: 67abc456...）
   - 案3: ✅ 予約完了（post_id: 67abc789...）
   - 予約投稿日時: 2026-01-11/12/13 08:00 JST
   → late_api_fixed_20260104.json

---

## SNS自動化完了

総実行時間: 52分

📄 final_summary.md生成完了: Flow/202601/2026-01-02/sns_automation_summary.md

次のアクション:
1. 投稿パフォーマンス監視（24時間後）
2. エンゲージメント率の測定
3. 次回の実行準備（明日7:00）
```

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-02 | 1.0 | 初版作成（Phase 1-4統合版） |
| 2026-01-03 | 1.1 | Late API統合詳細を追加 |
| 2026-01-03 | 1.2 | Null2実践から得た重要な注意点を追加 |
| 2026-01-04 | 1.3 | Phase 3をgenerate-sns-posts-takano（高野式7パターン版）に変更 |
| 2026-01-04 | 1.4 | 並列実行パターンを明示的なTask()コードブロックで記述 |
| 2026-01-04 | 1.5 | STEP 1.2 Top10抽出ロジックを再設計 |
| 2026-01-04 | 1.6 | Phase 4をLate API統合版に更新 |
| 2026-01-05 | 1.7 | Phase 2を逐次実行（1→2→3）に変更 |
| 2026-01-05 | 1.8 | Phase 4競合回避機能追加 |
| 2026-01-06 | 1.9 | **Phase詳細ファイルを外部化**。STEP 1.1-4.3の詳細手順を`phases/`ディレクトリに分離。メインSKILL.mdを400-500行削減し、参照リンクで構成 |
| 2026-01-12 | 2.0 | **STEP 1.3を5並列化**。ツイート詳細取得を2並列→5並列に変更。処理時間50%短縮（5-8分→2-4分）。Phase 1全体で12-22分に短縮、SNS自動化全体で62-97分に改善 |

---

**実装日**: 2026-01-02
**統合スキル数**: 7スキル
**バージョン**: 2.0（5並列最適化版）
**最終更新**: 2026-01-12
