import React, { useState, useEffect } from 'react';
import toast from 'react-hot-toast';
import { usePosts } from '../contexts/PostsContext';

export default function ApprovalQueueTab() {
  const { dispatch } = usePosts();
  const [pendingPosts, setPendingPosts] = useState([]);
  const [approvedPosts, setApprovedPosts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('pending');

  // 未承認投稿案を取得
  const fetchPendingPosts = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5555/api/queue/pending');
      if (!response.ok) {
        throw new Error('Failed to fetch pending posts');
      }
      const data = await response.json();
      setPendingPosts(data.pending_posts || []);
    } catch (error) {
      console.error('Error fetching pending posts:', error);
      toast.error('未承認投稿案の取得に失敗しました');
    } finally {
      setLoading(false);
    }
  };

  // 承認済み投稿案を取得
  const fetchApprovedPosts = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5555/api/queue/approved');
      if (!response.ok) {
        throw new Error('Failed to fetch approved posts');
      }
      const data = await response.json();
      setApprovedPosts(data.approved_posts || []);
    } catch (error) {
      console.error('Error fetching approved posts:', error);
      toast.error('承認済み投稿案の取得に失敗しました');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (activeTab === 'pending') {
      fetchPendingPosts();
    } else {
      fetchApprovedPosts();
    }

    // キュー更新イベントリスナー
    const handleQueueUpdate = () => {
      if (activeTab === 'pending') {
        fetchPendingPosts();
      } else {
        fetchApprovedPosts();
      }
    };

    window.addEventListener('queue-updated', handleQueueUpdate);
    return () => {
      window.removeEventListener('queue-updated', handleQueueUpdate);
    };
  }, [activeTab]);

  // 承認＋自動スケジューリング処理
  const handleApprove = async (queueId, variantIndex) => {
    const confirmApprove = window.confirm(
      'この投稿案を承認し、自動スケジューリングしますか？\n\n' +
      'LinkedIn: 明日 8:00 JST\n' +
      'X / Threads: 明日 20:00 JST\n\n' +
      '※既存の予約と時間が重複する場合は自動的に1時間ずつずらされます。'
    );

    if (!confirmApprove) return;

    setLoading(true);
    try {
      const response = await fetch('http://localhost:5555/api/queue/approve-and-schedule', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          queue_id: queueId,
          variant_index: variantIndex,
          platforms: ['LinkedIn', 'X', 'Threads']
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Approval and scheduling failed');
      }

      const result = await response.json();

      // 成功メッセージ（スケジュール時刻を表示）
      let scheduleMsg = '承認完了！自動スケジューリング済み:\n';
      if (result.scheduled_info) {
        Object.entries(result.scheduled_info).forEach(([platform, info]) => {
          const scheduledTime = new Date(info.scheduled_time);
          scheduleMsg += `${platform}: ${scheduledTime.toLocaleString('ja-JP')}\n`;
        });
      }

      toast.success(scheduleMsg, { duration: 5000 });
      fetchPendingPosts(); // リロード
    } catch (error) {
      console.error('Error approving and scheduling post:', error);
      toast.error(error.message || '承認・スケジューリングに失敗しました');
    } finally {
      setLoading(false);
    }
  };

  // 却下処理
  const handleReject = async (queueId) => {
    const reason = prompt('却下理由を入力してください（任意）:');

    try {
      const response = await fetch('http://localhost:5555/api/queue/reject', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          queue_id: queueId,
          reason: reason || 'User rejected'
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Rejection failed');
      }

      toast.success('投稿案を却下しました');
      fetchPendingPosts(); // リロード
    } catch (error) {
      console.error('Error rejecting post:', error);
      toast.error(error.message || '却下に失敗しました');
    }
  };

  // 未承認投稿の削除
  const handleDeletePending = async (queueId) => {
    const confirmDelete = window.confirm(
      'この投稿案を削除しますか？\n\n' +
      '※この操作は取り消せません。'
    );

    if (!confirmDelete) return;

    try {
      const response = await fetch('http://localhost:5555/api/queue/delete-pending', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          queue_id: queueId
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || '削除に失敗しました');
      }

      toast.success('投稿案を削除しました');
      fetchPendingPosts(); // リロード
    } catch (error) {
      console.error('Error deleting pending post:', error);
      toast.error(error.message || '削除に失敗しました');
    }
  };

  // 未承認キューの編集
  const handleEdit = (queueId, variantIndex, content) => {
    dispatch({
      type: 'OPEN_QUEUE_EDIT',
      payload: {
        queueId,
        variantIndex,
        content,
        isApproved: false
      }
    });
  };

  // 承認済みキューの編集
  const handleEditApproved = (queueId, content) => {
    dispatch({
      type: 'OPEN_QUEUE_EDIT',
      payload: {
        queueId,
        content,
        isApproved: true,
        variantIndex: null
      }
    });
  };

  // 承認済みキューのスケジューリング
  const handleScheduleApproved = (queueId, content) => {
    dispatch({
      type: 'OPEN_QUEUE_SCHEDULE',
      payload: {
        queueId,
        content
      }
    });
  };

  // 承認済み投稿の削除
  const handleDeleteApproved = async (queueId) => {
    const confirmDelete = window.confirm(
      'この承認済み投稿を削除しますか？\n\n' +
      '※この操作は取り消せません。'
    );

    if (!confirmDelete) return;

    try {
      const response = await fetch('http://localhost:5555/api/queue/delete-approved', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          queue_id: queueId
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || '削除に失敗しました');
      }

      toast.success('承認済み投稿を削除しました');
      fetchApprovedPosts(); // リロード
    } catch (error) {
      console.error('Error deleting approved post:', error);
      toast.error(error.message || '削除に失敗しました');
    }
  };

  return (
    <div className="max-w-6xl mx-auto p-6">
      {/* タブ切り替え */}
      <div className="flex gap-4 mb-6 border-b">
        <button
          onClick={() => setActiveTab('pending')}
          className={`px-4 py-2 font-medium border-b-2 transition-colors ${
            activeTab === 'pending'
              ? 'border-blue-600 text-blue-600'
              : 'border-transparent text-gray-600 hover:text-gray-900'
          }`}
        >
          未承認 ({pendingPosts.length})
        </button>
        <button
          onClick={() => setActiveTab('approved')}
          className={`px-4 py-2 font-medium border-b-2 transition-colors ${
            activeTab === 'approved'
              ? 'border-green-600 text-green-600'
              : 'border-transparent text-gray-600 hover:text-gray-900'
          }`}
        >
          承認済み ({approvedPosts.length})
        </button>
      </div>

      {loading ? (
        <div className="text-center py-12">
          <div className="inline-block animate-spin rounded-full h-12 w-12 border-4 border-gray-300 border-t-blue-600"></div>
          <p className="mt-4 text-gray-600">読み込み中...</p>
        </div>
      ) : (
        <>
          {/* 未承認タブ */}
          {activeTab === 'pending' && (
            <div className="space-y-6">
              {pendingPosts.length === 0 ? (
                <div className="text-center py-12 bg-gray-50 rounded-lg">
                  <p className="text-gray-600">未承認の投稿案はありません</p>
                </div>
              ) : (
                pendingPosts.map((item) => (
                  <div key={item.queue_id} className="bg-white border rounded-lg shadow-sm p-6">
                    {/* ヘッダー */}
                    <div className="flex justify-between items-start mb-4">
                      <div>
                        <h3 className="text-lg font-semibold text-gray-900">
                          {item.topic?.title || '投稿案'}
                        </h3>
                        <p className="text-sm text-gray-500 mt-1">
                          作成日時: {new Date(item.created_at).toLocaleString('ja-JP')}
                        </p>
                        <p className="text-sm text-gray-500">
                          Queue ID: {item.queue_id}
                        </p>
                      </div>
                      <div className="flex gap-2">
                        <button
                          onClick={() => handleReject(item.queue_id)}
                          className="px-4 py-2 text-sm font-medium text-red-700 bg-red-50 border border-red-300 rounded-md hover:bg-red-100"
                        >
                          全て却下
                        </button>
                        <button
                          onClick={() => handleDeletePending(item.queue_id)}
                          className="p-2 text-gray-400 hover:text-red-500 transition-colors"
                          title="削除"
                        >
                          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                          </svg>
                        </button>
                      </div>
                    </div>

                    {/* トピック概要 */}
                    {item.topic?.summary && (
                      <div className="mb-4 p-4 bg-blue-50 rounded-md">
                        <p className="text-sm text-gray-700">{item.topic.summary}</p>
                      </div>
                    )}

                    {/* 投稿案一覧 - 3列グリッド表示 */}
                    <div className="grid grid-cols-3 gap-4">
                      {item.posts
                        ?.sort((a, b) => b.predicted_er - a.predicted_er)
                        .map((post, index) => {
                          const isRecommended = index === 0;

                          return (
                            <div
                              key={index}
                              className={`rounded-md p-4 relative ${
                                isRecommended
                                  ? 'border-2 border-blue-500 bg-blue-50'
                                  : 'border bg-gray-50'
                              }`}
                            >
                              {/* 推奨バッジ */}
                              {isRecommended && (
                                <span className="absolute top-2 right-2 bg-blue-600 text-white text-xs px-2 py-1 rounded-full">
                                  推奨
                                </span>
                              )}

                              {/* バリエーション情報 */}
                              <h4 className="font-medium text-gray-900 mb-2">
                                {post.variant}
                              </h4>
                              <div className="text-xs text-gray-600 mb-3">
                                <div>ER: {post.predicted_er}%</div>
                                <div>評価: {post.rating}/10</div>
                                <div>{post.character_count}文字</div>
                              </div>

                              {/* 投稿内容プレビュー */}
                              <p className="text-sm text-gray-700 mt-2 line-clamp-4 whitespace-pre-wrap">
                                {post.content}
                              </p>

                              {/* アクションボタン */}
                              <div className="mt-4 flex gap-2">
                                <button
                                  onClick={() => handleEdit(item.queue_id, index, post.content)}
                                  className={`flex-1 px-3 py-1 text-sm font-medium text-white rounded-md ${
                                    isRecommended
                                      ? 'bg-blue-600 hover:bg-blue-700'
                                      : 'bg-gray-600 hover:bg-gray-700'
                                  }`}
                                >
                                  編集
                                </button>
                                <button
                                  onClick={() => handleApprove(item.queue_id, index)}
                                  className="flex-1 px-3 py-1 text-sm font-medium text-white bg-green-600 rounded-md hover:bg-green-700"
                                >
                                  承認
                                </button>
                              </div>
                            </div>
                          );
                        })}
                    </div>
                  </div>
                ))
              )}
            </div>
          )}

          {/* 承認済みタブ */}
          {activeTab === 'approved' && (
            <div className="space-y-6">
              {approvedPosts.length === 0 ? (
                <div className="text-center py-12 bg-gray-50 rounded-lg">
                  <p className="text-gray-600">承認済みの投稿案はありません</p>
                </div>
              ) : (
                approvedPosts.map((item) => (
                  <div key={item.queue_id} className="bg-white border rounded-lg shadow-sm p-6">
                    {/* ヘッダー */}
                    <div className="mb-4">
                      <h3 className="text-lg font-semibold text-gray-900">
                        {item.topic?.title || '投稿案'}
                      </h3>
                      <p className="text-sm text-gray-500 mt-1">
                        承認日時: {new Date(item.approved_at).toLocaleString('ja-JP')}
                      </p>
                      <p className="text-sm text-gray-500">
                        Queue ID: {item.queue_id}
                      </p>
                      {item.status === 'scheduled' && (
                        <div className="mt-2 inline-block px-3 py-1 bg-blue-100 text-blue-800 text-sm font-medium rounded-full">
                          スケジュール済み
                        </div>
                      )}
                    </div>

                    {/* 承認された投稿案 */}
                    {item.approved_post && (
                      <div className="border rounded-md p-4 bg-green-50">
                        <h4 className="font-medium text-gray-900 mb-2">
                          {item.approved_post.variant} (ER: {item.approved_post.predicted_er}%)
                        </h4>
                        <p className="text-sm text-gray-700 whitespace-pre-wrap mb-4">
                          {item.approved_post.content}
                        </p>

                        {/* スケジュール情報（scheduled_infoがある場合） */}
                        {item.scheduled_info && (
                          <div className="mt-4 bg-purple-50 rounded-md p-4 border border-purple-200">
                            <h5 className="text-sm font-medium text-purple-900 mb-2 flex items-center">
                              <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                              </svg>
                              📅 投稿予定時刻
                            </h5>
                            <ul className="text-xs text-purple-700 space-y-1">
                              {Object.entries(item.scheduled_info).map(([platform, info]) => (
                                <li key={platform} className="flex items-center">
                                  <span className="font-medium w-20">{platform}:</span>
                                  <span>{new Date(info.scheduled_time).toLocaleString('ja-JP', {
                                    year: 'numeric',
                                    month: '2-digit',
                                    day: '2-digit',
                                    hour: '2-digit',
                                    minute: '2-digit',
                                    timeZoneName: 'short'
                                  })}</span>
                                  {info.late_post_id && (
                                    <span className="ml-2 text-purple-500 text-xs">
                                      (ID: {info.late_post_id})
                                    </span>
                                  )}
                                </li>
                              ))}
                            </ul>
                          </div>
                        )}

                        {/* アクションボタン */}
                        <div className="mt-4 flex gap-3">
                          <button
                            onClick={() => handleEditApproved(item.queue_id, item.approved_post.content)}
                            className="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700"
                          >
                            編集
                          </button>
                          {item.status !== 'scheduled' && (
                            <button
                              onClick={() => handleScheduleApproved(item.queue_id, item.approved_post.content)}
                              className="px-4 py-2 text-sm font-medium text-white bg-purple-600 rounded-md hover:bg-purple-700"
                            >
                              スケジュール
                            </button>
                          )}
                          <button
                            onClick={() => handleDeleteApproved(item.queue_id)}
                            className="px-4 py-2 text-sm font-medium text-white bg-red-600 rounded-md hover:bg-red-700"
                          >
                            削除
                          </button>
                        </div>
                      </div>
                    )}
                  </div>
                ))
              )}
            </div>
          )}
        </>
      )}
    </div>
  );
}
