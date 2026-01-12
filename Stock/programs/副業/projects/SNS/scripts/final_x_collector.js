// X Timeline Collector - Simplified for MCP Execution
// Copy and paste this ENTIRE script into the browser console

console.log('🚀 Starting X Timeline Collection...');

// Initialize state
window.XCollectionState = {
  tweets: [],
  seenIds: new Set(),
  cycleCount: 0,
  startTime: new Date().toISOString()
};

// Main extraction function
window.extractAndCollect = function() {
  var state = window.XCollectionState;
  state.cycleCount++;

  var articles = document.querySelectorAll('article[data-testid="tweet"]');
  var newCount = 0;

  for (var i = 0; i < articles.length; i++) {
    try {
      var article = articles[i];

      // Get tweet ID
      var tweetId = null;
      var links = article.querySelectorAll('a[href*="/status/"]');
      for (var j = 0; j < links.length; j++) {
        var match = links[j].href.match(/\/status\/(\d+)/);
        if (match) {
          tweetId = match[1];
          break;
        }
      }

      if (!tweetId || state.seenIds.has(tweetId)) continue;

      // Extract engagement metrics with Japanese labels
      var likeBtn = article.querySelector('[data-testid="like"]');
      var likeLabel = likeBtn ? likeBtn.getAttribute('aria-label') : '';
      var likeMatch = likeLabel.match(/([0-9,]+) 件のいいね/);
      var likes = likeMatch ? parseInt(likeMatch[1].replace(/,/g, '')) : 0;

      var retweetBtn = article.querySelector('[data-testid="retweet"]');
      var rtLabel = retweetBtn ? retweetBtn.getAttribute('aria-label') : '';
      var rtMatch = rtLabel.match(/([0-9,]+) 件のリポスト/);
      var retweets = rtMatch ? parseInt(rtMatch[1].replace(/,/g, '')) : 0;

      var replyBtn = article.querySelector('[data-testid="reply"]');
      var replyLabel = replyBtn ? replyBtn.getAttribute('aria-label') : '';
      var replyMatch = replyLabel.match(/([0-9,]+) 件の返信/);
      var replies = replyMatch ? parseInt(replyMatch[1].replace(/,/g, '')) : 0;

      // Extract text and timestamp
      var textElem = article.querySelector('[data-testid="tweetText"]');
      var text = textElem ? textElem.textContent : '';

      var timeElem = article.querySelector('time');
      var timestamp = timeElem ? timeElem.getAttribute('datetime') : '';

      // Store tweet
      state.tweets.push({
        tweet_id: tweetId,
        text: text,
        likes: likes,
        retweets: retweets,
        replies: replies,
        timestamp: timestamp,
        cycle: state.cycleCount,
        collected_at: new Date().toISOString()
      });

      state.seenIds.add(tweetId);
      newCount++;

    } catch (e) {
      console.error('Error extracting tweet:', e);
    }
  }

  return {
    cycle: state.cycleCount,
    newTweets: newCount,
    totalTweets: state.tweets.length,
    lastThree: state.tweets.slice(-3).map(t => ({
      likes: t.likes,
      retweets: t.retweets,
      replies: t.replies
    }))
  };
};

// Run collection cycle
window.runCollectionCycle = async function(cycles) {
  console.log(`Starting ${cycles} collection cycles...`);

  for (var i = 0; i < cycles; i++) {
    var result = window.extractAndCollect();
    console.log(`Cycle ${result.cycle}: +${result.newTweets} tweets (total: ${result.totalTweets})`);
    console.log('Sample engagement:', result.lastThree);

    // Scroll down
    window.scrollBy(0, 800);

    // Wait for new tweets to load
    await new Promise(resolve => setTimeout(resolve, 2000));
  }

  console.log('✅ Collection complete!');
  console.log(`Total tweets: ${window.XCollectionState.tweets.length}`);

  return window.XCollectionState.tweets;
};

// Export function
window.downloadCollectionData = function() {
  var data = JSON.stringify(window.XCollectionState.tweets, null, 2);
  var blob = new Blob([data], {type: 'application/json'});
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url;
  a.download = 'x_timeline_' + new Date().toISOString().split('T')[0] + '.json';
  a.click();
  console.log('✅ Download started');
};

console.log('✅ Functions loaded!');
console.log('Run: await runCollectionCycle(20)');
console.log('Then: downloadCollectionData()');
