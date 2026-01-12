# Extract Content Skill

ツイート詳細データから記事・YouTube・PDFリンクのコンテンツを抽出するClaude Code Skill。

---

## 概要

**ClaudeCode LLM直接実行型**により、WebFetchツールを使用して記事コンテンツ（タイトル・本文・メタ情報）を自動抽出します。Pythonスクリプト不要で、**91.7%の成功率**を実現。

---

## クイックスタート

### 1. 前提条件

`tweet_details_ai_{YYYYMMDD}.json` が存在すること（`scrape-tweet-details` スキル実行後）

### 2. スキル実行

```bash
# Claude Codeで実行
コンテンツ抽出
```

または

```bash
/extract-content
```

### 3. 出力確認

```bash
# 出力ファイル
Stock/programs/副業/projects/SNS/data/extracted_contents_ai_YYYYMMDD.json

# 内容確認
cat Stock/programs/副業/projects/SNS/data/extracted_contents_ai_20260102.json | jq '.metadata'
```

---

## 実行パラメータ

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| **入力ファイル** | 最新の `tweet_details_ai_*.json` | ツイート詳細データ |
| **model** | haiku | ClaudeCode実行モデル |
| **thinking** | false | 思考モード |

---

## 出力フォーマット

```json
{
  "metadata": {
    "processed_at": "2026-01-02T12:38:00",
    "source_file": "tweet_details_ai_20260102.json",
    "total_links": 12,
    "success_count": 11,
    "error_count": 1,
    "success_rate": 91.7
  },
  "extracted_contents": [
    {
      "url": "https://example.com/article",
      "type": "article",
      "title": "記事タイトル",
      "content": "本文の最初の500ワード...",
      "word_count": 530,
      "status": "success",
      "tweet_id": "2006...",
      "username": "cb_doge",
      "domain": "example.com"
    }
  ]
}
```

---

## パフォーマンス

| 指標 | 実績（2026-01-02） |
|------|------------------|
| **成功率** | 91.7% (11/12) |
| **総抽出ワード数** | 1,322 |
| **平均ワード数/記事** | 120 |
| **実行時間** | 約8分 |

---

## トラブルシューティング

### WebFetchタイムアウト

**症状**: `status: "timeout"` エラー

**対処法**: 正常動作です。次のリンクへ自動進行します。

### 403 Forbidden

**症状**: `status: "forbidden"` エラー

**対処法**: アクセス制限があるサイトです（例: help.x.com）。次のリンクへ自動進行します。

---

## 次のアクション

抽出完了後、以下のアクションを実行できます：

1. **analyze-replies**: リプライから反響ポイント抽出
2. **research-topic**: WebSearchで最新ニュース・ファクトチェック
3. **generate-sns-posts**: 抽出コンテンツを元に投稿文生成

---

## 技術詳細

詳細は [SKILL.md](SKILL.md) を参照してください。

---

## 更新履歴

- 2026-01-02: 初版作成（ClaudeCode LLM直接実行型）
- 実績: 11/12リンク成功（91.7%）、1,322ワード抽出
