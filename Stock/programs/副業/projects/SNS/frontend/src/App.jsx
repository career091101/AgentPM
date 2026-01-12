import React, { useState, useEffect, useCallback } from 'react';
import { Toaster, toast } from 'react-hot-toast';
import { PostsProvider } from './contexts/PostsContext';
import PostsGallery from './components/PostsGallery';
import EditModal from './components/EditModal';
import ScheduleModal from './components/ScheduleModal';
import ApprovalQueueTab from './components/ApprovalQueueTab';
import { startApprovalPolling } from './utils/api';

export default function App() {
  const [activeView, setActiveView] = useState('gallery');
  const [slackEvents, setSlackEvents] = useState([]);

  // Slack承認イベントのポーリング
  useEffect(() => {
    const handleSlackEvents = (events) => {
      // 新しいSlack承認を通知
      events.forEach(event => {
        toast.success(
          `🔔 Slack承認: ${event.variant}\n承認者: ${event.user_name}`,
          {
            duration: 5000,
            icon: '📱',
            style: {
              background: '#4A154B',
              color: '#fff',
            },
          }
        );
      });

      // イベント履歴に追加
      setSlackEvents(prev => [...events, ...prev].slice(0, 20));
    };

    // ポーリング開始（5秒間隔）
    const stopPolling = startApprovalPolling(handleSlackEvents, 5000);

    // クリーンアップ
    return () => {
      stopPolling();
    };
  }, []);

  return (
    <PostsProvider>
      <div className="min-h-screen bg-gray-50">
        {/* ヘッダー */}
        <header className="bg-white shadow-sm">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div className="flex justify-between items-center">
              <h1 className="text-2xl font-bold text-gray-900">SNS投稿管理</h1>

              {/* Slack連携ステータス */}
              <div className="flex items-center gap-2 text-sm">
                <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800">
                  <span className="w-2 h-2 mr-1.5 rounded-full bg-green-400 animate-pulse"></span>
                  Slack連携中
                </span>
                {slackEvents.length > 0 && (
                  <span className="text-gray-500">
                    最新: {slackEvents[0]?.variant} ({slackEvents[0]?.user_name})
                  </span>
                )}
              </div>
            </div>

            {/* タブナビゲーション */}
            <nav className="mt-4 flex gap-4">
              <button
                onClick={() => setActiveView('gallery')}
                className={`px-4 py-2 font-medium rounded-md transition-colors ${
                  activeView === 'gallery'
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                投稿ギャラリー
              </button>
              <button
                onClick={() => setActiveView('queue')}
                className={`px-4 py-2 font-medium rounded-md transition-colors ${
                  activeView === 'queue'
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                承認キュー
              </button>
            </nav>
          </div>
        </header>

        {/* メインコンテンツ */}
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {activeView === 'gallery' ? <PostsGallery /> : <ApprovalQueueTab />}
        </main>

        {/* 編集モーダル */}
        <EditModal />

        {/* スケジューリングモーダル */}
        <ScheduleModal />

        {/* トースト通知 */}
        <Toaster position="top-right" />
      </div>
    </PostsProvider>
  );
}
