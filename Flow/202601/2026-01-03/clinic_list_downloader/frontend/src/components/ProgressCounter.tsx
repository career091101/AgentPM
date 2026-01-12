import { SearchProgress } from '../types'

interface ProgressCounterProps {
  progress: SearchProgress
  visible: boolean
}

export default function ProgressCounter({ progress, visible }: ProgressCounterProps) {
  if (!visible) {
    return null
  }

  const progressPercent = progress.total_queries > 0
    ? Math.round((progress.completed_queries / progress.total_queries) * 100)
    : 0

  return (
    <div className="w-full max-w-4xl">
      <div className="bg-gradient-to-r from-blue-50 to-purple-50 border-2 border-blue-300 rounded-2xl p-6 shadow-lg">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-bold text-gray-800 flex items-center gap-2">
            <svg className="w-6 h-6 text-blue-600 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            検索進行中...
          </h3>
          <span className="text-2xl font-bold text-blue-600">
            {progressPercent}%
          </span>
        </div>

        {/* プログレスバー */}
        <div className="w-full bg-gray-200 rounded-full h-6 mb-4 overflow-hidden shadow-inner">
          <div
            className="bg-gradient-to-r from-blue-500 to-purple-500 h-6 rounded-full transition-all duration-500 ease-out flex items-center justify-end pr-3"
            style={{ width: `${progressPercent}%` }}
          >
            {progressPercent > 10 && (
              <span className="text-white text-xs font-bold">
                {progress.completed_queries} / {progress.total_queries}
              </span>
            )}
          </div>
        </div>

        {/* 詳細情報 */}
        <div className="grid grid-cols-2 gap-4 text-sm">
          <div className="bg-white rounded-lg p-3 shadow">
            <div className="flex items-center gap-2 mb-1">
              <svg className="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
              <span className="font-semibold text-gray-700">クエリ進捗</span>
            </div>
            <p className="text-lg font-bold text-blue-600">
              {progress.completed_queries} / {progress.total_queries}
            </p>
          </div>

          <div className="bg-white rounded-lg p-3 shadow">
            <div className="flex items-center gap-2 mb-1">
              <svg className="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
              <span className="font-semibold text-gray-700">発見件数</span>
            </div>
            <p className="text-lg font-bold text-green-600">
              {progress.total_found.toLocaleString()}件
            </p>
          </div>

          <div className="bg-white rounded-lg p-3 shadow">
            <div className="flex items-center gap-2 mb-1">
              <svg className="w-4 h-4 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span className="font-semibold text-gray-700">重複排除後</span>
            </div>
            <p className="text-lg font-bold text-purple-600">
              {progress.unique_count.toLocaleString()}件
            </p>
          </div>

          <div className="bg-white rounded-lg p-3 shadow">
            <div className="flex items-center gap-2 mb-1">
              <svg className="w-4 h-4 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              </svg>
              <span className="font-semibold text-gray-700">処理中</span>
            </div>
            <p className="text-sm font-bold text-orange-600 truncate">
              {progress.current_prefecture} - {progress.current_keyword}
            </p>
          </div>
        </div>

        {/* ステータスメッセージ */}
        <div className="mt-4 p-3 bg-blue-100 border border-blue-300 rounded-lg">
          <p className="text-sm text-blue-800 flex items-center gap-2">
            <svg className="w-4 h-4 animate-pulse" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
            </svg>
            {progress.current_prefecture && progress.current_keyword
              ? `「${progress.current_keyword}」で${progress.current_prefecture}を検索中...`
              : '検索を準備中...'}
          </p>
        </div>
      </div>
    </div>
  )
}
