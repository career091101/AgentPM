import React from 'react';

export default function PostCard({ post, index, onSelect, onEdit, onSchedule, onDelete }) {
  const ratingColor = {
    'S級': 'bg-purple-100 text-purple-800',
    'A級': 'bg-blue-100 text-blue-800',
    'B級': 'bg-green-100 text-green-800'
  }[post.rating] || 'bg-gray-100 text-gray-800';

  const handleDelete = () => {
    if (window.confirm('この投稿案を削除しますか？')) {
      onDelete();
    }
  };

  return (
    <div className="border rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow">
      {/* ヘッダー */}
      <div className="flex justify-between items-start mb-3">
        <div>
          <span className="text-sm font-medium text-gray-600">{post.variant}</span>
          <span className={`ml-2 px-2 py-1 rounded text-xs font-semibold ${ratingColor}`}>
            {post.rating}
          </span>
        </div>
        <div className="flex items-center gap-2">
          {post.recommended && (
            <span className="bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded">
              推奨
            </span>
          )}
          {onDelete && (
            <button
              onClick={handleDelete}
              className="text-gray-400 hover:text-red-500 transition-colors"
              title="削除"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          )}
        </div>
      </div>

      {/* 本文（3行まで表示、オーバーフローは省略）*/}
      <div className="mb-3 text-sm text-gray-800 line-clamp-3">
        {post.content}
      </div>

      {/* 統計情報 */}
      <div className="flex gap-4 text-xs text-gray-500 mb-3">
        <span>{post.character_count}字</span>
        <span>予測ER: {post.predicted_er}</span>
      </div>

      {/* ボタン */}
      <div className="flex flex-col gap-2">
        <div className="flex gap-2">
          <button
            onClick={onSelect}
            className="flex-1 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors text-sm font-medium"
          >
            承認
          </button>
          <button
            onClick={onEdit}
            className="px-4 py-2 border border-gray-300 rounded hover:bg-gray-50 transition-colors text-sm font-medium"
          >
            編集
          </button>
        </div>
        {onSchedule && (
          <button
            onClick={onSchedule}
            className="w-full bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition-colors text-sm font-medium"
          >
            スケジューリング
          </button>
        )}
      </div>
    </div>
  );
}
