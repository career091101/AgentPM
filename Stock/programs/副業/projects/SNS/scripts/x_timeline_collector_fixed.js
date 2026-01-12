// X Timeline Collector - Fixed Version (2026-01-01)
// エンゲージメント指標の取得を修正（日本語aria-label対応）

console.log('🔧 X Timeline Collector Fixed版を注入中...');

// ステートをクリア
delete window.XTimelineCollectorState;
try {
  localStorage.removeItem('x_timeline_collection_backup');
} catch(e) {}

// 修正版収集関数
window.extractTweetsAndAccumulateFixed = function() {
  // ステート初期化
  if (!window.XTimelineCollectorState) {
    window.XTimelineCollectorState = {
      allTweets: [],
      seenIds: new Set(),
      cycleCount: 0,
      startTime: new Date().toISOString()
    };
  }

  var state = window.XTimelineCollectorState;
  state.cycleCount++;
  
  var tweets = document.querySelectorAll('article[data-testid="tweet"]');
  var newCount = 0;
  var duplicateCount = 0;

  tweets.forEach(function(tweet) {
    try {
      // ツイートIDの取得
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

      // 著者情報
      var authorElement = tweet.querySelector('[data-testid="User-Name"]');
      var authorName = authorElement ? (authorElement.querySelector('span') ? authorElement.querySelector('span').textContent : 'Unknown') : 'Unknown';
      var authorUsernameLink = tweet.querySelector('a[role="link"][href^="/"]');
      var authorUsername = authorUsernameLink ? authorUsernameLink.textContent : 'Unknown';

      // ツイート本文
      var textElement = tweet.querySelector('[data-testid="tweetText"]');
      var text = textElement ? textElement.textContent : '';

      // タイムスタンプ
      var timeElement = tweet.querySelector('time');
      var createdAt = timeElement ? timeElement.getAttribute('datetime') : new Date().toISOString();

      // 🔥 エンゲージメント指標（修正版 - 日本語aria-label対応）
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

      // エンゲージメントスコア計算
      var engagementScore = likes + retweets * 3 + replies * 5;

      // リツイート判定
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

  // バックアップ保存
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

console.log('✅ 修正版収集関数を注入完了: window.extractTweetsAndAccumulateFixed()');
console.log('📝 使い方: result = extractTweetsAndAccumulateFixed()');
