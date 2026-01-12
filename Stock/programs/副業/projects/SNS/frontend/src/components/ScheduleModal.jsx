import React, { useState } from 'react';
import { usePosts } from '../contexts/PostsContext';
import toast from 'react-hot-toast';

export default function ScheduleModal() {
  const { state, dispatch } = usePosts();
  const [loading, setLoading] = useState(false);

  const handleClose = () => {
    dispatch({ type: state.queueMode.isActive ? 'CLOSE_QUEUE_SCHEDULE' : 'CLOSE_SCHEDULE_MODAL' });
  };

  const handlePlatformToggle = (platform) => {
    const { platforms } = state.scheduleMode;
    const newPlatforms = platforms.includes(platform)
      ? platforms.filter(p => p !== platform)
      : [...platforms, platform];

    dispatch({ type: 'UPDATE_SCHEDULE_PLATFORMS', payload: newPlatforms });
  };

  const handleSchedule = async () => {
    const { scheduledTime, platforms } = state.scheduleMode;

    if (!scheduledTime) {
      toast.error('投稿日時を選択してください');
      return;
    }

    if (platforms.length === 0) {
      toast.error('最低1つのプラットフォームを選択してください');
      return;
    }

    setLoading(true);

    try {
      // キューモードかどうかで分岐
      if (state.queueMode.isActive) {
        // キューモード: 承認済みキュー用のスケジューリングAPI
        const response = await fetch(
          `http://localhost:5555/api/queue/approved/${state.queueMode.queueId}/schedule`,
          {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              scheduled_time: scheduledTime,
              platforms: platforms
            })
          }
        );

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || 'スケジューリングに失敗しました');
        }

        toast.success('投稿をスケジュールしました');
        dispatch({ type: 'CLOSE_QUEUE_SCHEDULE' });

        // ApprovalQueueTabを再読み込み
        window.dispatchEvent(new Event('queue-updated'));

      } else {
        // 既存フロー: 投稿ギャラリー用の/api/scheduleを使用
        const response = await fetch('http://localhost:5555/api/schedule', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            scheduled_time: scheduledTime,
            platforms
          })
        });

        if (!response.ok) {
          const errorData = await response.json();
          console.error('API Error:', errorData);

          // エラーメッセージの詳細を抽出
          let errorMessage = 'スケジューリングに失敗しました';
          if (errorData.error) {
            errorMessage = errorData.error;
            if (errorData.details) {
              errorMessage += `: ${errorData.details}`;
            }
          } else if (errorData.message) {
            errorMessage = errorData.message;
          }

          toast.error(errorMessage, {
            duration: 5000,
            style: {
              maxWidth: '500px'
            }
          });
          setLoading(false);
          return;
        }

        const result = await response.json();
        toast.success(`スケジューリング完了: ${new Date(scheduledTime).toLocaleString('ja-JP')}`);
        handleClose();
      }
    } catch (error) {
      console.error('Schedule error:', error);

      // ネットワークエラーかAPIエラーかを判定
      let errorMessage = 'スケジューリングに失敗しました';
      if (error.message) {
        errorMessage += `: ${error.message}`;
      }
      if (error.name === 'TypeError' && error.message.includes('fetch')) {
        errorMessage = 'サーバーに接続できませんでした。バックエンドが起動しているか確認してください。';
      }

      toast.error(errorMessage, {
        duration: 5000,
        style: {
          maxWidth: '500px'
        }
      });
    } finally {
      setLoading(false);
    }
  };

  if (!state.scheduleMode.isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-md w-full mx-4">
        {/* ヘッダー */}
        <div className="flex items-center justify-between p-6 border-b">
          <h2 className="text-xl font-semibold text-gray-900">投稿スケジューリング</h2>
          <button
            onClick={handleClose}
            className="text-gray-400 hover:text-gray-600"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* コンテンツ */}
        <div className="p-6 space-y-6">
          {/* 日時選択 */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              投稿日時
            </label>
            <input
              type="datetime-local"
              value={state.scheduleMode.scheduledTime || ''}
              onChange={(e) => {
                const value = e.target.value;
                if (value) {
                  dispatch({
                    type: 'UPDATE_SCHEDULE_TIME',
                    payload: new Date(value).toISOString()
                  });
                }
              }}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <p className="mt-1 text-xs text-gray-500">
              日本時間（JST）で指定してください
            </p>
          </div>

          {/* プラットフォーム選択 */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              投稿先プラットフォーム
            </label>
            <div className="space-y-2">
              {['LinkedIn', 'X', 'Facebook', 'Threads'].map((platform) => (
                <label key={platform} className="flex items-center">
                  <input
                    type="checkbox"
                    checked={state.scheduleMode.platforms.includes(platform)}
                    onChange={() => handlePlatformToggle(platform)}
                    className="rounded border-gray-300 text-blue-600 focus:ring-blue-500 h-4 w-4"
                  />
                  <span className="ml-2 text-sm text-gray-700">{platform}</span>
                </label>
              ))}
            </div>
          </div>

          {/* 推奨時刻ヒント */}
          <div className="bg-blue-50 rounded-md p-4">
            <h3 className="text-sm font-medium text-blue-900 mb-2">📅 推奨投稿時刻</h3>
            <ul className="text-xs text-blue-700 space-y-1">
              <li>• LinkedIn: 8:00 JST（平日朝）</li>
              <li>• X / Facebook: 20:00 JST（夜）</li>
              <li>• Threads: 20:00 JST（夜）</li>
            </ul>
          </div>
        </div>

        {/* フッター */}
        <div className="flex justify-end gap-3 p-6 border-t bg-gray-50 rounded-b-lg">
          <button
            onClick={handleClose}
            className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
          >
            キャンセル
          </button>
          <button
            onClick={handleSchedule}
            disabled={loading || !state.scheduleMode.scheduledTime || state.scheduleMode.platforms.length === 0}
            className="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center gap-2"
          >
            {loading && (
              <svg className="animate-spin h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            )}
            {loading ? 'スケジューリング中...' : 'スケジューリング実行'}
          </button>
        </div>
      </div>
    </div>
  );
}
