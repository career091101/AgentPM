import React, { useState } from 'react';
import { usePosts } from '../contexts/PostsContext';
import ManualEditTab from './ManualEditTab';
import AIRefineTab from './AIRefineTab';
import { approvePost, getPosts } from '../utils/api';
import toast from 'react-hot-toast';

export default function EditModal() {
  const { state, dispatch } = usePosts();
  const [activeTab, setActiveTab] = useState('manual');
  const [isSaving, setIsSaving] = useState(false);

  const handleSave = async () => {
    setIsSaving(true);
    try {
      // キューモードかどうかで分岐
      if (state.queueMode.isActive) {
        // キューモード: 新規APIエンドポイントを使用
        const endpoint = state.queueMode.isApproved
          ? `/api/queue/approved/${state.queueMode.queueId}/update`
          : `/api/queue/pending/${state.queueMode.queueId}/update`;

        const requestBody = state.queueMode.isApproved
          ? { new_content: state.editMode.draftContent }
          : {
              variant_index: state.queueMode.variantIndex,
              new_content: state.editMode.draftContent
            };

        const response = await fetch(`http://localhost:5555${endpoint}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || 'キューの更新に失敗しました');
        }

        toast.success('投稿案を更新しました');
        dispatch({ type: 'CLOSE_QUEUE_EDIT' });

        // ApprovalQueueTabを再読み込み
        window.dispatchEvent(new Event('queue-updated'));

      } else {
        // 既存フロー: 投稿ギャラリー用の/api/approveを使用
        await approvePost({
          variant: state.selectedPost.variantNum || '案1',
          content: state.selectedPost.content,
          refined: true,
          refined_content: state.editMode.draftContent
        });

        // 保存後にデータを再読み込み
        const updatedData = await getPosts();
        dispatch({ type: 'LOAD_POSTS', payload: updatedData });

        toast.success('投稿案を保存しました');
        dispatch({ type: 'CLOSE_EDIT_MODAL' });
      }
    } catch (error) {
      console.error('Error saving:', error);
      toast.error(error.message || '保存に失敗しました');
    } finally {
      setIsSaving(false);
    }
  };

  if (!state.editMode.isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-4xl w-full max-h-[90vh] overflow-hidden">
        {/* ヘッダー */}
        <div className="p-6 border-b">
          <h2 className="text-2xl font-bold">投稿内容を編集</h2>
        </div>

        {/* タブナビゲーション */}
        <div className="flex border-b">
          <button
            onClick={() => setActiveTab('manual')}
            className={`flex-1 py-3 px-4 text-sm font-medium ${
              activeTab === 'manual'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-500 hover:text-gray-700'
            }`}
          >
            手動編集
          </button>
          <button
            onClick={() => setActiveTab('ai')}
            className={`flex-1 py-3 px-4 text-sm font-medium ${
              activeTab === 'ai'
                ? 'border-b-2 border-blue-600 text-blue-600'
                : 'text-gray-500 hover:text-gray-700'
            }`}
          >
            AI修正
          </button>
        </div>

        {/* タブコンテンツ */}
        <div className="p-6 overflow-y-auto" style={{ maxHeight: 'calc(90vh - 200px)' }}>
          {activeTab === 'manual' ? <ManualEditTab /> : <AIRefineTab />}
        </div>

        {/* フッター */}
        <div className="p-6 border-t flex justify-end gap-3">
          <button
            onClick={() => dispatch({ type: state.queueMode.isActive ? 'CLOSE_QUEUE_EDIT' : 'CLOSE_EDIT_MODAL' })}
            className="px-4 py-2 border border-gray-300 rounded hover:bg-gray-50"
          >
            キャンセル
          </button>
          <button
            onClick={handleSave}
            disabled={isSaving}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
          >
            {isSaving ? '保存中...' : '保存'}
          </button>
        </div>
      </div>
    </div>
  );
}
