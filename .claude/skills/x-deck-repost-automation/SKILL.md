# X Pro Deck 海外AI動向リポスト自動化スキル

## 概要

X Proの16個のキュレーションデッキから海外AI動向の人気投稿を自動抽出し、takano式（高野メソッド）解説文を添えてリポスト投稿を生成・予約投稿する完全自動化スキル。

**バージョン**: 1.0.0
**作成日**: 2026-01-12
**ベーススキル**: `sns-automation v2`（Phase 1-3流用）

---

## 目的

### 主要機能

1. **デッキからの自動収集**: 16個のX Pro Decksから高エンゲージメント投稿を収集
2. **インテリジェントフィルタ**: 10万インプレッション以上 + AI関連のみ抽出
3. **takano式解説生成**: 700-1500字の高品質な解説文を自動生成
4. **最適時間帯配信**: Late API経由で4-6投稿/日を予約投稿

### ターゲットユーザー

- CEO・経営者向けのAI動向キュレーション
- 海外AI企業の最新情報を日本語で解説
- ビジネス戦略・競争優位の観点で分析

---

## データソース

### X Pro Decks（16個）

データソース定義: `deck_search_queries.json`

| カテゴリ | デッキ数 | 例 |
|---------|---------|-----|
| **AI関連** | 10個 | JP AI Leader, AI Companies #1, AI People #1-5, AI Robotics, AI Leaders #1-2 |
| **AR/VR** | 3個 | AR/VR Companies, AR/VR People #1-2 |
| **VC** | 1個 | VC Firms |
| **TechMedia** | 2個 | Tech News, Tech Journalists |

**検索条件**:
- 最低リツイート数: 50（JP AI Leaderのみ10）
- RTフィルター: 多くのデッキで `-filter:retweets` 使用

---

## 実行フロー

### Phase 1: デッキデータ収集（20-30分）

**目的**: X Pro Decksから高インプレッション投稿を収集

**処理内容**:
1. `deck_search_queries.json` から16個のデッキ検索クエリ読み込み
2. Claude in Chrome MCPで各デッキを順次検索
3. 各デッキから上位20-30件取得（合計320-480件）
4. インプレッション数でソート、10万以上フィルタ
5. AI関連判定（LLM判定ワンパス化）
6. 上位10-20件を抽出

**出力ファイル**:
- `deck_timeline_{date}.json` (320-480件)
- `deck_top_tweets_{date}.json` (10-20件、10万インプ以上、AI関連のみ)

**実装ガイド**: `phases/phase1_deck_data_collection.md`

---

### Phase 2: コンテンツ分析（20-30分）

**目的**: リポスト対象の投稿を詳細分析

**処理内容**:
1. 上位10-20件の投稿詳細取得（Claude in Chrome MCP）
   - 「さらに表示」クリックで全文取得
   - スクリーンショットで画像・動画キャプチャ
   - リプライ分析（エンゲージメント理解）
2. Web調査（`research-topic`流用）
   - 投稿トピックの最新情報
   - ファクトチェック
   - 専門家意見収集

**出力ファイル**:
- `tweet_details_full_{date}.json` (全文・画像URL含む)
- `reply_insights_{date}.json` (リプライ分析)
- `research_findings_{date}.json` (Web調査結果)

**実装ガイド**: `phases/phase2_content_analysis.md`

---

### Phase 3: リポスト投稿生成（30-40分）

**目的**: takano式解説文付きリポスト投稿を生成

**投稿フォーマット**:
```
[takano式解説文（700-1500字）]

🔗 元の投稿: https://x.com/username/status/123456789
```

**重要**: Late APIは引用リポスト未対応のため、URL埋め込み方式を採用。Xは自動でリンクカードを生成するため、視覚的には引用リポストに近い表示になる。

**takano式7要素**（70点以上必須）:
1. **Hook**（15点）: 衝撃的数字 × 企業名 × 断定型
2. **Data/Evidence**（20点）: 数値5個以上、企業名3社以上
3. **Empathy**（10点）: CEO向け共感要素
4. **Insight**（15点）: 「つまり」「ポイントは」で洞察
5. **Advice**（10点）: 具体的行動提案
6. **Question ending**（15点）: CEO向け問いかけ
7. **Proper nouns**（15点）: 固有名詞10個以上

**出力ファイル**:
- `repost_drafts_{date}.json` (4-6件のリポスト投稿案)

**実装ガイド**: `phases/phase3_repost_generation.md`
**テンプレート**: `takano_repost_template.md`

---

### Phase 4: Late API予約投稿（10-15分）

**目的**: 4-6投稿を最適な時間帯に予約投稿

**投稿スケジュール**:
| 時刻 | 投稿 | 対象記事 |
|------|------|--------|
| 7:30 | リポスト1 | Top 1 |
| 8:30 | リポスト2 | Top 2 |
| 12:00 | リポスト3 | Top 3 |
| 12:30 | リポスト4 | Top 4 |
| 20:00 | リポスト5 | Top 5 |
| 21:00 | リポスト6 | Top 6 |

**Late API仕様**（URL埋め込み方式）:
```json
{
  "content": "[takano式解説文]\n\n🔗 元の投稿: https://x.com/username/status/123456789",
  "platforms": [
    {
      "platform": "twitter",
      "accountId": "LATE_TWITTER_ACCOUNT_ID"
    }
  ],
  "scheduledFor": "2026-01-13T07:30:00+09:00",
  "timezone": "Asia/Tokyo"
}
```

**エラーハンドリング**: 指数バックオフリトライ（5秒→15秒→30秒）

**出力ファイル**:
- `late_api_repost_{date}.json` (投稿結果)
- `repost_summary_{date}.md` (サマリーレポート)

**実装ガイド**: `phases/phase4_late_api_scheduling.md`

---

## 設定ファイル

### `repost_config.json`

リポスト自動化の全体設定。

**主要設定項目**:
```json
{
  "filters": {
    "min_impressions": 100000,
    "ai_related_only": true,
    "engagement_threshold": {
      "min_likes": 1000,
      "min_retweets": 100
    }
  },
  "posting": {
    "posts_per_day": {"min": 4, "max": 6},
    "time_slots": [...]
  },
  "takano_style": {
    "min_length": 700,
    "max_length": 1500,
    "quality_threshold": 70
  }
}
```

### `deck_search_queries.json`

16個のX Pro Decks検索クエリ定義。

**データ構造**:
```json
{
  "decks": [
    {
      "deckName": "JP AI Leader",
      "searchQuery": "(from:keitowebai OR ...) min_retweets:10",
      "description": "日本のAIリーダー6名のツイート"
    },
    ...
  ]
}
```

### `takano_repost_template.md`

takano式リポスト投稿生成の詳細テンプレート。

**内容**:
- 7要素の詳細ガイドライン
- Hook 7パターン
- 品質チェック基準
- プロンプトテンプレート

---

## 出力ファイル

### Phase 1出力

| ファイル | 説明 | 保存先 |
|---------|------|--------|
| `deck_timeline_{date}.json` | 全デッキ収集データ（320-480件） | `Flow/{YYYYMM}/{YYYY-MM-DD}/` |
| `deck_top_tweets_{date}.json` | フィルタ後Top投稿（10-20件） | `Flow/{YYYYMM}/{YYYY-MM-DD}/` |

### Phase 2出力

| ファイル | 説明 | 保存先 |
|---------|------|--------|
| `tweet_details_full_{date}.json` | 投稿詳細（全文・画像含む） | `Flow/{YYYYMM}/{YYYY-MM-DD}/` |
| `reply_insights_{date}.json` | リプライ分析結果 | `Flow/{YYYYMM}/{YYYY-MM-DD}/` |
| `research_findings_{date}.json` | Web調査結果 | `Flow/{YYYYMM}/{YYYY-MM-DD}/` |

### Phase 3出力

| ファイル | 説明 | 保存先 |
|---------|------|--------|
| `repost_drafts_{date}.json` | リポスト投稿案（4-6件） | `Flow/{YYYYMM}/{YYYY-MM-DD}/` |

### Phase 4出力

| ファイル | 説明 | 保存先 |
|---------|------|--------|
| `late_api_repost_{date}.json` | Late API投稿結果 | `Flow/{YYYYMM}/{YYYY-MM-DD}/` |
| `repost_summary_{date}.md` | 投稿サマリーレポート | `Flow/{YYYYMM}/{YYYY-MM-DD}/` |

---

## 使用方法

### 手動実行（個別Phase）

```bash
# Phase 1: デッキデータ収集
claude-code --skill x-deck-repost-automation --phase 1

# Phase 2: コンテンツ分析
claude-code --skill x-deck-repost-automation --phase 2

# Phase 3: リポスト投稿生成
claude-code --skill x-deck-repost-automation --phase 3

# Phase 4: Late API予約投稿
claude-code --skill x-deck-repost-automation --phase 4
```

### 完全自動実行（Phase 1-4統合）

```bash
# 全フェーズ自動実行
claude-code --skill x-deck-repost-automation --auto

# 所要時間: 90-115分
# 出力: 4-6件の予約投稿完了
```

### 定期実行設定

```bash
# cronで毎日朝6時実行
0 6 * * * cd /Users/yuichi/agentpm && claude-code --skill x-deck-repost-automation --auto
```

---

## 依存関係

### 既存Skillの流用

| Phase | 流用Skill | 用途 |
|-------|----------|------|
| Phase 1 | `collect-x-timeline` | タイムライン収集ロジック（改造） |
| Phase 1 | `extract-top-tweets` | Top投稿抽出 |
| Phase 2 | `extract-content` | AI関連判定（LLM判定ワンパス化） |
| Phase 2 | `analyze-replies` | リプライ分析 |
| Phase 2 | `research-topic` | Web調査 |
| Phase 3 | `generate-sns-posts-takano` | takano式投稿生成（改造） |
| Phase 4 | `late_api_multi_post_v2.py` | Late API投稿（改造） |

### 外部ツール

- **Claude in Chrome MCP**: ブラウザ自動操作・マルチモーダルコンテンツ取得
- **Late API**: 予約投稿サービス（Proプラン、300リクエスト/分）

### 環境変数

```bash
# Late API認証
export LATE_API_KEY="your_api_key"
export LATE_TWITTER_ACCOUNT_ID="your_account_id"

# X Pro認証（Claude in Chrome経由）
# ブラウザで事前ログイン必須
```

---

## 品質基準

### フィルタ基準

| 項目 | 基準 |
|------|------|
| **インプレッション** | 10万以上 |
| **いいね数** | 1000以上 |
| **リツイート数** | 100以上 |
| **AI関連度** | LLM判定で関連性確認 |

### takano式品質基準

| 項目 | 基準 |
|------|------|
| **総合点** | 70点以上（100点満点） |
| **文字数** | 700-1500字 |
| **固有名詞** | 10個以上 |
| **数値データ** | 5個以上 |
| **企業名** | 3社以上 |

### リジェクト基準

以下の場合は再生成:
- 総合点が70点未満
- 文字数が700字未満または1500字超過
- 固有名詞が10個未満
- データ・数値が不足（5個未満）

---

## パフォーマンス

### 実行時間

| Phase | 所要時間 | 並列化 |
|-------|---------|--------|
| Phase 1 | 20-30分 | 可能（デッキ毎） |
| Phase 2 | 20-30分 | 可能（投稿毎） |
| Phase 3 | 30-40分 | 可能（投稿毎） |
| Phase 4 | 10-15分 | 不可（API直列） |
| **合計** | **90-115分** | - |

### コスト見積もり

- **Claude API**: 約$5-10/日（モデル選択で最適化）
- **Late API**: Proプラン月額費用
- **X Pro**: 月額費用

### モデル選択推奨

- **Phase 1（データ収集）**: haiku（コスト効率）
- **Phase 2（分析）**: sonnet（バランス）
- **Phase 3（生成）**: sonnet（品質重視）
- **Phase 4（投稿）**: haiku（シンプル処理）

---

## リスク・制約事項

### Technical Risks

1. **X Pro Decksアクセス**
   - リスク: Claude in Chrome MCPでX Proにアクセスできない可能性
   - 対策: X標準検索でデッキ検索クエリを実行

2. **Late API引用リポスト未対応** [確定]
   - リスク: Late APIが引用リポスト機能未サポート（2026-01-12検証済み）
   - 対策: URL埋め込み方式（Xがリンクカード自動生成）

3. **インプレッション数取得**
   - リスク: X APIやClaude in Chrome MCPでインプレッション数が取得できない可能性
   - 対策: リツイート数・いいね数でエンゲージメントを推定

### Operational Risks

1. **コスト**
   - リスク: Claude in Chrome MCP + LLM判定 + takano式生成で高コスト
   - 対策: モデル選択（haiku/sonnet/opus）の最適化

2. **実行時間**
   - リスク: Phase 1-4で90-115分（既存v2より長い）
   - 対策: 並列実行の最大化

3. **Late APIレート制限**
   - リスク: 300リクエスト/分（Proプラン）
   - 対策: 4-6投稿/日なので問題なし

---

## 成功基準

### Functional Requirements

- [x] 16個のX Pro Decksから投稿を収集できる（検索クエリJSON抽出済み）
- [ ] 10万インプレッション以上の投稿のみをフィルタできる
- [ ] AI関連投稿のみをLLM判定で抽出できる
- [ ] takano式解説文（700-1500字）を生成できる
- [ ] 高野メソッド7要素をすべて満たす（70点以上）
- [ ] URL埋め込み方式でLate API経由で投稿できる（Xリンクカード自動生成）
- [ ] 4-6投稿/日を最適な時間帯（朝7-9時、昼12-13時、夜20-22時）に予約投稿できる

### Non-Functional Requirements

- [ ] 実行時間: 90-115分以内
- [ ] エラー率: 5%以下
- [ ] takano式解説文の品質: 高野メソッド70点以上

---

## トラブルシューティング

### Phase 1: デッキ検索エラー

**エラー**: "Deck not accessible"
```bash
# 解決策
1. X Proにブラウザでログイン確認
2. 検索クエリの構文確認
3. X標準検索で代替実行
```

### Phase 2: 全文取得失敗

**エラー**: "さらに表示" ボタンが見つからない
```bash
# 解決策
1. read_page()でDOM構造確認
2. find(query="さらに表示")で要素検索
3. スクリーンショットで目視確認
```

### Phase 3: takano式品質不足

**エラー**: "Quality score < 70"
```bash
# 解決策
1. research_findings補強（Web調査追加）
2. プロンプト改善（具体例追加）
3. 手動レビュー・修正
```

### Phase 4: Late API投稿失敗

**エラー**: "Post failed with status 500"
```bash
# 解決策
1. 指数バックオフリトライ実行（5秒→15秒→30秒）
2. 投稿内容の文字数・形式確認
3. accountId・scheduledFor形式確認
4. 3回失敗後はフォールバック（手動投稿用MD生成）
```

---

## 参照

### プロジェクト内

- **実装プラン**: `~/.claude/plans/serene-painting-pumpkin.md`
- **Phase 1詳細**: `phases/phase1_deck_data_collection.md`
- **Phase 2詳細**: `phases/phase2_content_analysis.md`
- **Phase 3詳細**: `phases/phase3_repost_generation.md`
- **Phase 4詳細**: `phases/phase4_late_api_scheduling.md`
- **takano式テンプレート**: `takano_repost_template.md`
- **設定ファイル**: `repost_config.json`
- **検索クエリ**: `deck_search_queries.json`

### ベーススキル

- **sns-automation v2**: `.claude/skills/sns-automation/`
- **takano式プロンプト**: `Stock/programs/副業/projects/SNS/投稿文作成用プロンプト_v6_takano_refined`
- **Late API実装**: `Stock/programs/副業/projects/SNS/scripts/late_api_multi_post_v2.py`

### 外部リソース

- **Late API仕様**: `Flow/202601/2026-01-12/late-api-openapi.yaml`
- **Late API公式**: https://late.so/api
- **X Pro**: https://pro.x.com

---

## 更新履歴

| 日付 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-12 | 1.0.0 | 初版作成、Late API URL埋め込み方式確定 |

---

**作成者**: Claude Sonnet 4.5
**最終更新**: 2026-01-12
**ステータス**: Phase 1-4実装待ち
