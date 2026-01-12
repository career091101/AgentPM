const API_BASE_URL = 'http://localhost:5555/api';

export async function getPosts() {
  const response = await fetch(`${API_BASE_URL}/posts`);
  if (!response.ok) throw new Error('Failed to fetch posts');
  const data = await response.json();

  // APIレスポンス（variant_1, variant_2, variant_3）を配列に変換
  const posts = [
    { variant: '案1', ...data.variant_1 },
    { variant: '案2', ...data.variant_2 },
    { variant: '案3', ...data.variant_3 }
  ];

  return { posts, metadata: data.metadata };
}

export async function approvePost(data) {
  const response = await fetch(`${API_BASE_URL}/approve`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      ...data,
      source: 'webui'  // 承認ソースを追加
    })
  });
  if (!response.ok) throw new Error('Failed to approve post');
  return response.json();
}

export async function refinePost(data) {
  const response = await fetch(`${API_BASE_URL}/refine`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  if (!response.ok) throw new Error('Failed to refine post');
  return response.json();
}

export async function schedulePost(data) {
  const response = await fetch(`${API_BASE_URL}/schedule`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  if (!response.ok) throw new Error('Failed to schedule post');
  return response.json();
}

// ============================================================
// Slack統合API（リアルタイム更新）
// ============================================================

/**
 * 承認イベントをポーリングで取得
 * @param {string} since - ISO 8601形式のタイムスタンプ（この時刻以降のイベントを取得）
 * @returns {Promise<{events: Array, last_check: string, total_count: number}>}
 */
export async function getApprovalEvents(since = null) {
  const url = since
    ? `${API_BASE_URL}/approval-events?since=${encodeURIComponent(since)}`
    : `${API_BASE_URL}/approval-events`;

  const response = await fetch(url);
  if (!response.ok) throw new Error('Failed to fetch approval events');
  return response.json();
}

/**
 * Web UIから承認した際にSlackに通知
 * @param {Object} data - 通知データ
 * @param {string} data.variant - 承認された案（例: "案1"）
 * @param {string} data.content - 投稿内容
 * @param {string} data.approval_file - 承認ファイル名
 * @param {string} [data.slack_thread_ts] - Slackスレッドのタイムスタンプ（オプション）
 * @returns {Promise<{success: boolean, slack_response?: Object, error?: string}>}
 */
export async function notifySlack(data) {
  const response = await fetch(`${API_BASE_URL}/notify-slack`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.error || 'Failed to notify Slack');
  }
  return response.json();
}

/**
 * 承認イベントのポーリングを開始
 * @param {Function} onEvent - 新しいイベントが見つかった時のコールバック
 * @param {number} interval - ポーリング間隔（ミリ秒）、デフォルト5秒
 * @returns {Function} - ポーリングを停止する関数
 */
export function startApprovalPolling(onEvent, interval = 5000) {
  let lastCheck = new Date().toISOString();
  let isRunning = true;

  const poll = async () => {
    if (!isRunning) return;

    try {
      const result = await getApprovalEvents(lastCheck);

      if (result.events && result.events.length > 0) {
        // Slack経由の承認イベントのみ通知
        const slackEvents = result.events.filter(e => e.source === 'slack');
        if (slackEvents.length > 0) {
          onEvent(slackEvents);
        }
      }

      lastCheck = result.last_check;
    } catch (error) {
      console.error('Polling error:', error);
    }

    if (isRunning) {
      setTimeout(poll, interval);
    }
  };

  // 初回実行
  poll();

  // 停止関数を返す
  return () => {
    isRunning = false;
  };
}

/**
 * 承認済み投稿の一覧を取得（キューから）
 * @returns {Promise<{approved_posts: Array, count: number}>}
 */
export async function getApprovedPosts() {
  const response = await fetch(`${API_BASE_URL}/queue/approved`);
  if (!response.ok) throw new Error('Failed to fetch approved posts');
  return response.json();
}

/**
 * 未承認投稿の一覧を取得（キューから）
 * @returns {Promise<{pending_posts: Array, count: number}>}
 */
export async function getPendingPosts() {
  const response = await fetch(`${API_BASE_URL}/queue/pending`);
  if (!response.ok) throw new Error('Failed to fetch pending posts');
  return response.json();
}

/**
 * 未承認投稿を削除
 * @param {string} queueId - キューID
 * @returns {Promise<{success: boolean, message: string}>}
 */
export async function deletePendingPost(queueId) {
  const response = await fetch(`${API_BASE_URL}/queue/delete-pending`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ queue_id: queueId })
  });
  if (!response.ok) throw new Error('Failed to delete pending post');
  return response.json();
}
