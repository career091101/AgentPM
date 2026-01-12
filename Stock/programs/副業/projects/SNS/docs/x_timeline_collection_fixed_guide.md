# X Timeline 収集ガイド（修正版）

## 問題

2026年1月1日時点で、X.comのDOM構造が変更され、エンゲージメント指標（いいね、リツイート、リプライ）が全て0になっていました。

### 原因

aria-labelのフォーマットが英語から日本語に変更：
- 旧: `"15 Likes"`
- 新: `"15 件のいいね。いいねする"`

### 解決策

日本語aria-labelに対応した正規表現パターンに修正：
```javascript
// 修正前
const likesText = likeElement.getAttribute('aria-label');
const likes = parseInt(likesText.match(/\d+/)?.[0] || '0');

// 修正後
const likeLabel = likeElement.getAttribute('aria-label');
const likeMatch = likeLabel.match(/([0-9,]+) 件のいいね/);
const likes = likeMatch ? parseInt(likeMatch[1].replace(/,/g, '')) : 0;
```

## 実行手順

### Step 1: ブラウザでX.comを開く

1. Chrome/Edgeでhttps://x.com/home にアクセス
2. ログインしてタイムラインを表示

### Step 2: 開発者ツールを開く

- **Mac**: `Cmd + Option + J`
- **Windows**: `F12` または `Ctrl + Shift + J`

### Step 3: 修正版スクリプトを注入

以下のファイルの内容をコピーして、コンソールに貼り付けて実行：

```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/x_timeline_collector_fixed.js
```

または、以下のコマンドでクリップボードにコピー：

```bash
cat /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/x_timeline_collector_fixed.js | pbcopy
```

### Step 4: 収集を実行（20サイクル）

コンソールに以下を貼り付けて実行：

```javascript
async function runCollectionCycles(totalCycles) {
  console.log(`📊 ${totalCycles}サイクルの収集を開始します...`);

  for (let i = 1; i <= totalCycles; i++) {
    const result = window.extractTweetsAndAccumulateFixed();

    console.log(`Cycle ${result.cycle}/${totalCycles}: 新規${result.newTweets}件, 重複${result.duplicates}件, 累計${result.totalUnique}件`);
    console.log('直近3件のエンゲージメント:', result.lastEngagementSample);

    window.scrollBy(0, 1000);
    await new Promise(resolve => setTimeout(resolve, 3000));
  }

  console.log('✅ 収集完了！');
  return JSON.parse(localStorage.getItem('x_timeline_collection_backup'));
}

// 20サイクル実行
await runCollectionCycles(20);
```

### Step 5: データを取得

コンソールに以下を貼り付けて実行：

```javascript
// データを取得
const data = JSON.parse(localStorage.getItem('x_timeline_collection_backup'));

console.log(`📊 総ツイート数: ${data.allTweets.length}件`);
console.log(`🔥 エンゲージメント取得成功: ${data.allTweets.filter(t => t.engagement_score > 0).length}件`);

// Top 5を表示
const sorted = data.allTweets.sort((a, b) => b.engagement_score - a.engagement_score);
console.log('\n🏆 Top 5 エンゲージメント:');
sorted.slice(0, 5).forEach((t, i) => {
  console.log(`${i+1}. @${t.author_username}: ${t.engagement_score}点 (♥${t.likes} 🔁${t.retweets} 💬${t.replies})`);
  console.log(`   ${t.text.substring(0, 80)}...`);
});

// JSONとしてコピー
copy(JSON.stringify(data, null, 2));
console.log('\n✅ クリップボードにコピーしました');
```

### Step 6: データを保存

1. クリップボードの内容を以下のファイルに保存：
   ```
   /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_fixed.json
   ```

2. Top 30を抽出（コンソールで実行）：
   ```javascript
   const top30 = sorted.slice(0, 30);
   copy(JSON.stringify(top30, null, 2));
   console.log('✅ Top 30をクリップボードにコピーしました');
   ```

3. Top 30を保存：
   ```
   /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_fixed_top30.json
   ```

## 検証ポイント

### 成功基準

- ✅ いいね、リツイート、リプライが0以外の値で取得できている
- ✅ 少なくとも80%以上のツイートでエンゲージメント指標が取得できている
- ✅ engagement_scoreが正しく計算されている（0以外）
- ✅ Top 30がエンゲージメント順に正しくソートされている

### 確認方法

```javascript
// エンゲージメント取得率を確認
const data = JSON.parse(localStorage.getItem('x_timeline_collection_backup'));
const withEngagement = data.allTweets.filter(t => t.engagement_score > 0);
const successRate = (withEngagement.length / data.allTweets.length * 100).toFixed(1);

console.log(`エンゲージメント取得成功率: ${successRate}%`);
console.log(`成功: ${withEngagement.length}件 / 全体: ${data.allTweets.length}件`);
```

## トラブルシューティング

### Q: エンゲージメント指標が依然として0になる

A: aria-labelの言語設定を確認：
```javascript
const tweet = document.querySelector('article[data-testid="tweet"]');
const likeBtn = tweet.querySelector('[data-testid="like"]');
console.log('aria-label:', likeBtn.getAttribute('aria-label'));
```

- 日本語の場合: `"15 件のいいね。いいねする"` → 現在の修正版で対応
- 英語の場合: `"15 Likes"` → 旧バージョンで対応
- その他の言語: パターンを追加で修正が必要

### Q: スクリプト注入でエラーが出る

A: ブラウザのコンソールを一度クリアして再実行：
```javascript
console.clear();
// 再度スクリプトを貼り付けて実行
```

### Q: localStorageが保存できない

A: ブラウザのストレージ容量を確認。データが大きすぎる場合は、サイクル数を減らす（20→10）。

## 修正内容の詳細

### DOM調査結果（2026-01-01）

```javascript
// 実際に取得されたaria-label
{
  "like_aria": "15 件のいいね。いいねする",
  "reply_aria": "0 件の返信。返信する",
  "retweet_aria": "307 件のリポスト件。リポスト"
}
```

### 修正版正規表現

```javascript
// いいね
/([0-9,]+) 件のいいね/

// リツイート
/([0-9,]+) 件のリポスト/

// リプライ
/([0-9,]+) 件の返信/
```

### 注意点

- カンマ区切りの数値（例: `1,497`）に対応するため、`replace(/,/g, '')`で除去
- 全角スペースではなく半角スペース（` `）を使用
- `\d`ではなく`[0-9]`を使用（JavaScriptの正規表現エンジンの互換性）

## 参照

- 修正版スクリプト: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/x_timeline_collector_fixed.js`
- 保存先: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/`
- DOM調査ログ: 2026-01-01 調査実施
