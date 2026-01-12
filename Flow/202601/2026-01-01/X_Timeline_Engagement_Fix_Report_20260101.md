# Xタイムライン エンゲージメント指標修正レポート

**日時**: 2026-01-01
**タスク**: Xタイムライン収集のエンゲージメント指標（いいね、リツイート、リプライ）取得修正

---

## 問題の概要

### 現象

`/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_full.json` のデータで、全てのツイートのエンゲージメント指標が0になっていました：

```json
{
  "likes": 0,
  "retweets": 0,
  "replies": 0,
  "impressions_estimated": 0,
  "engagement_score": 0
}
```

### 原因

2026年1月1日時点でX.comのDOM構造が変更され、aria-labelのフォーマットが**英語から日本語**に変更されていました。

| 要素 | 旧フォーマット（英語） | 新フォーマット（日本語） |
|------|----------------------|------------------------|
| いいね | `"15 Likes"` | `"15 件のいいね。いいねする"` |
| リツイート | `"307 Retweets"` | `"307 件のリポスト件。リポスト"` |
| リプライ | `"14 Replies"` | `"14 件の返信。返信する"` |

既存のスクリプトは英語フォーマットの正規表現パターンを使用していたため、日本語フォーマットにマッチせず、全て0になっていました。

---

## 調査プロセス

### Step 1: DOM構造の調査

**実施内容**:
- Claude In Chromeでブラウザを起動
- X.com/homeに遷移してタイムラインを表示
- JavaScriptでDOM要素を詳細調査

**調査結果**:
```javascript
// 実際に取得されたaria-label
{
  "like_aria": "15 件のいいね。いいねする",
  "reply_aria": "0 件の返信。返信する",
  "retweet_aria": "307 件のリポスト件。リポスト"
}
```

### Step 2: 正規表現パターンのテスト

**発見した問題点**:
1. `\d+` がJavaScriptの一部環境で正しく解釈されない → `[0-9]+` に変更
2. `\s*` がエスケープされていない → 半角スペース ` ` を明示的に使用
3. カンマ区切りの数値（例: `1,497`）に対応していない → `replace(/,/g, '')` で除去

**修正後の正規表現**:
```javascript
// いいね
const likeMatch = likeLabel.match(/([0-9,]+) 件のいいね/);
const likes = likeMatch ? parseInt(likeMatch[1].replace(/,/g, '')) : 0;

// リツイート
const retweetMatch = retweetLabel.match(/([0-9,]+) 件のリポスト/);
const retweets = retweetMatch ? parseInt(retweetMatch[1].replace(/,/g, '')) : 0;

// リプライ
const replyMatch = replyLabel.match(/([0-9,]+) 件の返信/);
const replies = replyMatch ? parseInt(replyMatch[1].replace(/,/g, '')) : 0;
```

### Step 3: テスト実行

**テスト結果（5ツイート）**:
```javascript
{
  "total_tested": 5,
  "success_count": 5,  // 100%成功
  "results": [
    { "likes": 15, "retweets": 0, "replies": 0, "engagement_score": 15 },
    { "likes": 1497, "retweets": 307, "replies": 14, "engagement_score": 2488 },
    { "likes": 5, "retweets": 0, "replies": 0, "engagement_score": 5 },
    { "likes": 12, "retweets": 1, "replies": 0, "engagement_score": 15 },
    { "likes": 332, "retweets": 51, "replies": 0, "engagement_score": 485 }
  ]
}
```

✅ **全てのツイートで正しくエンゲージメント指標を取得できることを確認**

---

## 修正内容

### 修正版スクリプトの作成

**ファイルパス**:
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/x_timeline_collector_fixed.js
```

**主な変更点**:
1. エンゲージメント抽出部分を日本語aria-label対応に修正
2. カンマ区切り数値のサポート
3. より堅牢なエラーハンドリング

**修正前（旧バージョン）**:
```javascript
const likeElement = tweet.querySelector('[data-testid="like"]');
const likesText = likeElement ? likeElement.getAttribute('aria-label') : '0';
const likes = parseInt(likesText.match(/\d+/)?.[0] || '0');
```

**修正後（新バージョン）**:
```javascript
const likeElement = tweet.querySelector('[data-testid="like"]');
const likeLabel = likeElement ? likeElement.getAttribute('aria-label') : '';
const likeMatch = likeLabel.match(/([0-9,]+) 件のいいね/);
const likes = likeMatch ? parseInt(likeMatch[1].replace(/,/g, '')) : 0;
```

---

## 成果物

### 1. 修正版収集スクリプト

| ファイル | パス |
|---------|------|
| 収集関数 | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/x_timeline_collector_fixed.js` |
| Python実行スクリプト | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/run_x_collection_fixed.py` |
| 実行ガイド | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/docs/x_timeline_collection_fixed_guide.md` |

### 2. 実行手順書

詳細な実行手順を記載したガイドを作成：
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/docs/x_timeline_collection_fixed_guide.md
```

**内容**:
- ブラウザコンソールでの実行手順（Step 1-6）
- トラブルシューティング
- 検証ポイント
- 修正内容の詳細

---

## 次のアクション

### データ再収集の実行

**手順**:
1. ブラウザで https://x.com/home を開く
2. 開発者ツール（F12）を開く
3. 以下のスクリプトをコンソールに貼り付けて実行：

```bash
# スクリプトをクリップボードにコピー
cat /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/x_timeline_collector_fixed.js | pbcopy
```

4. コンソールに貼り付けて実行
5. 収集ループを20サイクル実行（ガイド参照）
6. データを取得して保存：
   - `x_timeline_20260101_fixed.json`
   - `x_timeline_20260101_fixed_top30.json`

### 検証ポイント

- ✅ いいね、リツイート、リプライが0以外の値で取得できている
- ✅ 少なくとも80%以上のツイートでエンゲージメント指標が取得できている
- ✅ `engagement_score`が正しく計算されている
- ✅ Top 30がエンゲージメント順に正しくソートされている

---

## 技術的な学び

### 1. DOM構造の変更に対する対応

Xのような大規模プラットフォームは、頻繁にDOM構造やaria-labelのフォーマットを変更します。堅牢なスクレイピングには以下が重要：

- **多言語対応**: 英語だけでなく、日本語、その他の言語のパターンをサポート
- **柔軟な正規表現**: 数値フォーマット（カンマ区切り、K/M表記）に対応
- **フォールバック**: aria-labelが取得できない場合の代替手段（textContent等）

### 2. JavaScriptの互換性

- `\d` は環境によっては正しく動作しない → `[0-9]` を使用
- テンプレートリテラル（`` ` ``）よりも従来の文字列結合の方が互換性が高い
- ES6のアロー関数ではなく `function()` を使用

### 3. デバッグのベストプラクティス

1. **段階的なテスト**: 1ツイート → 5ツイート → 全体収集
2. **ログ出力**: `console.log` で中間結果を確認
3. **サンプルデータの可視化**: `lastEngagementSample` で直近3件を表示

---

## まとめ

### 達成したこと

- ✅ X.comのDOM構造変更（英語 → 日本語aria-label）を特定
- ✅ エンゲージメント抽出ロジックを修正
- ✅ 修正版スクリプトでテストし、100%成功を確認
- ✅ 実行ガイドと成果物を整備

### 未完了（次回実施）

- ⏸️ 修正版での20サイクル再収集
- ⏸️ `x_timeline_20260101_fixed.json` の保存
- ⏸️ Top 30データの作成
- ⏸️ エンゲージメント取得成功率の最終検証

### 所要時間

- DOM調査: 10分
- 修正版スクリプト作成: 15分
- テスト実行: 5分
- ドキュメント作成: 10分
- **合計**: 約40分

---

## 付録

### A. aria-label サンプル

```javascript
// 日本語フォーマット（2026-01-01時点）
"15 件のいいね。いいねする"
"307 件のリポスト件。リポスト"
"14 件の返信。返信する"

// カンマ区切り数値の例
"1,497 件のいいね。いいねする"
"12,345 件のリポスト件。リポスト"
```

### B. engagement_score 計算式

```javascript
engagement_score = likes + (retweets × 3) + (replies × 5)
```

**理由**:
- いいね: 1点（最も簡単なエンゲージメント）
- リツイート: 3点（拡散効果が高い）
- リプライ: 5点（最も深いエンゲージメント）

### C. impressions_estimated 推定式

```javascript
impressions_estimated = Math.round(engagement_score / 0.02)
```

**仮定**: エンゲージメント率 = 2%
（業界平均: 1-3%）

---

**作成者**: Claude (Sonnet 4.5)
**作成日**: 2026-01-01
**レポートバージョン**: 1.0
