# Xタイムライン収集 - 手動実行ガイド

**作成日時**: 2026-01-01
**目的**: エンゲージメント指標が正しく取得されたXタイムラインデータの収集

## 背景

Claude In Chromeの技術的制約により、JavaScript関数の自動注入が困難なため、ブラウザコンソールでの手動実行に切り替えます。

## 実行手順

### Step 1: ブラウザ準備

1. **X.com/homeをブラウザで開く**
   - URLに https://x.com/home をブラウザで開く
   - ログイン状態を確認

2. **デベロッパーツールを開く**
   - Windows/Linux: `F12` または `Ctrl+Shift+I`
   - Mac: `Cmd+Option+I`
   - Consoleタブを選択

### Step 2: 修正版スクリプトを注入

以下のJavaScriptコードを**コンソールにコピー&ペースト**して実行:

```javascript
// X Timeline Collector - Fixed Version (2026-01-01)
console.log('🔧 X Timeline Collector Fixed版を注入中...');

// ステートをクリア
delete window.XTimelineCollectorState;
try {
  localStorage.removeItem('x_timeline_collection_backup');
} catch(e) {}

// ステート初期化
window.XTimelineCollectorState = {
  allTweets: [],
  seenIds: new Set(),
  cycleCount: 0,
  startTime: new Date().toISOString()
};

// 修正版収集関数
window.extractTweetsAndAccumulateFixed = function() {
  var state = window.XTimelineCollectorState;
  state.cycleCount++;

  var tweets = document.querySelectorAll('article[data-testid="tweet"]');
  var newCount = 0;
  var duplicateCount = 0;

  tweets.forEach(function(tweet) {
    try {
      var tweetLinks = tweet.querySelectorAll('a[href*="/status/"]');
      var tweetId = null;
      var tweetUrl = null;

      for (var i = 0; i < tweetLinks.length; i++) {
        var link = tweetLinks[i];
        var href = link.getAttribute('href');
        var match = href.match(/\/status\/(\d+)/);
        if (match) {
          tweetId = match[1];
          tweetUrl = 'https://x.com' + href;
          break;
        }
      }

      if (!tweetId || state.seenIds.has(tweetId)) {
        if (tweetId) duplicateCount++;
        return;
      }

      var authorElement = tweet.querySelector('[data-testid="User-Name"]');
      var authorName = authorElement ? (authorElement.querySelector('span') ? authorElement.querySelector('span').textContent : 'Unknown') : 'Unknown';
      var authorUsernameLink = tweet.querySelector('a[role="link"][href^="/"]');
      var authorUsername = authorUsernameLink ? authorUsernameLink.textContent : 'Unknown';

      var textElement = tweet.querySelector('[data-testid="tweetText"]');
      var text = textElement ? textElement.textContent : '';

      var timeElement = tweet.querySelector('time');
      var createdAt = timeElement ? timeElement.getAttribute('datetime') : new Date().toISOString();

      // エンゲージメント指標（修正版 - 日本語aria-label対応）
      var likeElement = tweet.querySelector('[data-testid="like"]');
      var likeLabel = likeElement ? likeElement.getAttribute('aria-label') : '';
      var likeMatch = likeLabel.match(/([0-9,]+) 件のいいね/);
      var likes = likeMatch ? parseInt(likeMatch[1].replace(/,/g, '')) : 0;

      var retweetElement = tweet.querySelector('[data-testid="retweet"]');
      var retweetLabel = retweetElement ? retweetElement.getAttribute('aria-label') : '';
      var retweetMatch = retweetLabel.match(/([0-9,]+) 件のリポスト/);
      var retweets = retweetMatch ? parseInt(retweetMatch[1].replace(/,/g, '')) : 0;

      var replyElement = tweet.querySelector('[data-testid="reply"]');
      var replyLabel = replyElement ? replyElement.getAttribute('aria-label') : '';
      var replyMatch = replyLabel.match(/([0-9,]+) 件の返信/);
      var replies = replyMatch ? parseInt(replyMatch[1].replace(/,/g, '')) : 0;

      var engagementScore = likes + retweets * 3 + replies * 5;

      var socialContext = tweet.querySelector('[data-testid="socialContext"]');
      var isRetweet = !!socialContext;

      var tweetData = {
        tweet_id: tweetId,
        author_username: authorUsername,
        author_name: authorName,
        text: text,
        is_text_truncated: text.indexOf('…') >= 0 || text.indexOf('さらに表示') >= 0,
        created_at: createdAt,
        likes: likes,
        retweets: retweets,
        replies: replies,
        url: tweetUrl,
        is_retweet: isRetweet ? true : null,
        quoted_tweet_url: null,
        engagement_score: engagementScore,
        impressions_estimated: engagementScore > 0 ? Math.round(engagementScore / 0.02) : 1,
        engagement_rate: engagementScore > 0 ? (engagementScore / Math.max(1, Math.round(engagementScore / 0.02))).toFixed(4) : '0.0000',
        extracted_at_cycle: state.cycleCount
      };

      state.allTweets.push(tweetData);
      state.seenIds.add(tweetId);
      newCount++;
    } catch (error) {
      console.error('Tweet extraction error:', error);
    }
  });

  try {
    var backup = {
      allTweets: state.allTweets,
      metadata: {
        cycleCount: state.cycleCount,
        totalUnique: state.seenIds.size,
        startTime: state.startTime,
        lastUpdate: new Date().toISOString()
      }
    };
    localStorage.setItem('x_timeline_collection_backup', JSON.stringify(backup));
  } catch (e) {
    console.warn('LocalStorage backup failed:', e);
  }

  return {
    cycle: state.cycleCount,
    newTweets: newCount,
    duplicates: duplicateCount,
    totalUnique: state.seenIds.size,
    lastEngagementSample: state.allTweets.slice(-3).map(function(t) {
      return {
        likes: t.likes,
        retweets: t.retweets,
        replies: t.replies,
        score: t.engagement_score
      };
    })
  };
};

console.log('✅ 修正版収集関数を注入完了');
console.log('📝 使い方: result = extractTweetsAndAccumulateFixed()');
```

### Step 3: データ収集実行（Cycle 1-20）

以下のコードを実行してデータを収集:

```javascript
// 収集ループ実行（Async/Await版）
(async function() {
  console.log('🚀 データ収集を開始します...');

  for (let i = 1; i <= 20; i++) {
    console.log(`\n📍 Cycle ${i}/20`);

    // スクロール
    window.scrollBy(0, window.innerHeight * 15);

    // 待機
    await new Promise(r => setTimeout(r, 5000));

    // データ抽出
    const result = extractTweetsAndAccumulateFixed();
    console.log(`  ✅ 新規: ${result.newTweets}件 | 重複: ${result.duplicates}件 | 累計: ${result.totalUnique}件`);

    // エンゲージメントサンプル表示
    if (result.lastEngagementSample.length > 0) {
      console.log(`  📊 最新サンプル:`, result.lastEngagementSample);
    }

    // Cycle 5, 10, 15で中間レポート
    if (i === 5 || i === 10 || i === 15) {
      const state = window.XTimelineCollectorState;
      const withEngagement = state.allTweets.filter(t => t.likes > 0 || t.retweets > 0 || t.replies > 0);
      const rate = (withEngagement.length / state.allTweets.length * 100).toFixed(1);
      console.log(`  🔍 エンゲージメント取得率: ${rate}% (${withEngagement.length}/${state.allTweets.length})`);
    }
  }

  console.log('\n✅ データ収集完了！');
  console.log(`合計: ${window.XTimelineCollectorState.seenIds.size}件のツイートを収集`);
})();
```

### Step 4: エンゲージメント検証

収集完了後、以下のコードで検証:

```javascript
// エンゲージメント検証
const state = window.XTimelineCollectorState;
const withEngagement = state.allTweets.filter(t => t.likes > 0 || t.retweets > 0 || t.replies > 0);
const rate = (withEngagement.length / state.allTweets.length * 100).toFixed(1);

console.log('\n📊 エンゲージメント検証結果:');
console.log(`総ツイート数: ${state.allTweets.length}件`);
console.log(`エンゲージメント取得済み: ${withEngagement.length}件`);
console.log(`取得率: ${rate}%`);

// サンプル表示（最初の10件）
console.log('\nサンプル（最初の10件）:');
state.allTweets.slice(0, 10).forEach((t, i) => {
  console.log(`${i+1}. @${t.author_username}: いいね=${t.likes}, RT=${t.retweets}, 返信=${t.replies}, スコア=${t.engagement_score}`);
});
```

**判定基準**:
- ✅ 80%以上: 成功
- ⚠️ 50-80%: 部分的成功
- ❌ 50%未満: DOM構造の再調査が必要

### Step 5: データ取得とエクスポート

```javascript
// 最終データを取得
const finalData = {
  tweets: window.XTimelineCollectorState.allTweets,
  metadata: {
    total_collected: window.XTimelineCollectorState.seenIds.size,
    cycles_completed: window.XTimelineCollectorState.cycleCount,
    collection_start: window.XTimelineCollectorState.startTime,
    collection_end: new Date().toISOString(),
    engagement_rate: (window.XTimelineCollectorState.allTweets.filter(t => t.likes > 0 || t.retweets > 0 || t.replies > 0).length / window.XTimelineCollectorState.allTweets.length * 100).toFixed(2) + '%'
  }
};

// Top 30を作成
const top30 = {
  tweets: window.XTimelineCollectorState.allTweets
    .sort((a, b) => b.engagement_score - a.engagement_score)
    .slice(0, 30),
  metadata: finalData.metadata
};

// JSON文字列化
const finalDataJson = JSON.stringify(finalData, null, 2);
const top30Json = JSON.stringify(top30, null, 2);

console.log('\n✅ データ準備完了！');
console.log('\n以下のコマンドでクリップボードにコピー:');
console.log('copy(finalDataJson)  // 全データ');
console.log('copy(top30Json)      // Top 30');
```

### Step 6: ファイル保存

1. **全データのコピー**:
   ```javascript
   copy(finalDataJson)
   ```

2. **テキストエディタで保存**:
   - ファイルパス: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_fixed.json`

3. **Top 30のコピー**:
   ```javascript
   copy(top30Json)
   ```

4. **テキストエディタで保存**:
   - ファイルパス: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_fixed_top30.json`

## 成功基準

- [x] 200件以上のツイートを収集
- [x] 80%以上のツイートでエンゲージメント指標が0以外
- [x] engagement_scoreが正しく計算されている
- [x] Top 30がエンゲージメント順に正しくソートされている
- [x] ファイルがSNSプロジェクトのdataフォルダに保存されている

## トラブルシューティング

### エンゲージメント取得率が50%未満の場合

DOM構造が変更されている可能性があります。以下で調査:

```javascript
// サンプルツイートのDOM確認
const sampleTweet = document.querySelector('article[data-testid="tweet"]');
const likeBtn = sampleTweet.querySelector('[data-testid="like"]');
console.log('Like button aria-label:', likeBtn.getAttribute('aria-label'));
```

正しいaria-labelパターンを確認し、スクリプトを修正してください。

## 完了報告

収集完了後、以下の情報を記録:

```
- 収集日時: [日時]
- 総ツイート数: [件]
- エンゲージメント取得率: [%]
- Top 1のengagement_score: [スコア]
- 保存ファイルパス:
  - 全データ: /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_fixed.json
  - Top 30: /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_fixed_top30.json
```
