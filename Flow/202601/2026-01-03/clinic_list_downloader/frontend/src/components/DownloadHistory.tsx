import { useState, useEffect } from 'react'

interface DownloadHistoryItem {
  id: number
  search_history_id: number | null
  prefectures: string[]
  keywords: string[]
  file_name: string
  record_count: number
  created_at: string
}

interface DownloadHistoryProps {
  isVisible: boolean
  onClose: () => void
}

export default function DownloadHistory({ isVisible, onClose }: DownloadHistoryProps) {
  const [history, setHistory] = useState<DownloadHistoryItem[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    if (isVisible) {
      loadHistory()
    }
  }, [isVisible])

  const loadHistory = async () => {
    setLoading(true)
    setError('')

    try {
      const username = localStorage.getItem('auth_username')
      const password = localStorage.getItem('auth_password')

      const response = await fetch('/api/download-history', {
        headers: {
          'Authorization': 'Basic ' + btoa(`${username}:${password}`)
        }
      })

      if (!response.ok) {
        throw new Error('Failed to load download history')
      }

      const data = await response.json()
      setHistory(data.download_history)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load history')
    } finally {
      setLoading(false)
    }
  }

  if (!isVisible) return null

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl max-w-6xl w-full max-h-[90vh] overflow-hidden">
        <div className="bg-gradient-to-r from-green-500 to-teal-500 text-white px-6 py-4 flex justify-between items-center">
          <h2 className="text-2xl font-bold">ダウンロード履歴</h2>
          <button
            onClick={onClose}
            className="text-white hover:bg-white hover:bg-opacity-20 rounded-lg p-2 transition-all"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div className="p-6 overflow-y-auto max-h-[calc(90vh-80px)]">
          {loading && (
            <div className="text-center py-12">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-green-500 mx-auto"></div>
              <p className="mt-4 text-gray-600">読み込み中...</p>
            </div>
          )}

          {error && (
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
              {error}
            </div>
          )}

          {!loading && !error && history.length === 0 && (
            <div className="text-center py-12 text-gray-500">
              <svg className="w-16 h-16 mx-auto mb-4 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10" />
              </svg>
              <p className="text-lg">ダウンロード履歴がありません</p>
            </div>
          )}

          {!loading && !error && history.length > 0 && (
            <div className="space-y-4">
              {history.map((item) => (
                <div
                  key={item.id}
                  className="bg-gradient-to-r from-green-50 to-teal-50 border border-green-200 rounded-xl p-4 hover:shadow-lg transition-all"
                >
                  <div className="flex justify-between items-start mb-3">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <svg className="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                        <span className="font-mono text-sm text-gray-700">{item.file_name}</span>
                        <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-xs font-semibold">
                          {item.record_count.toLocaleString()} 件
                        </span>
                      </div>
                      <div className="flex flex-wrap gap-2 mb-2">
                        <span className="text-sm font-semibold text-gray-700">都道府県:</span>
                        {item.prefectures.map((pref, idx) => (
                          <span key={idx} className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-sm">
                            {pref}
                          </span>
                        ))}
                      </div>
                      <div className="flex flex-wrap gap-2">
                        <span className="text-sm font-semibold text-gray-700">キーワード:</span>
                        {item.keywords.map((keyword, idx) => (
                          <span key={idx} className="bg-purple-100 text-purple-800 px-2 py-1 rounded text-sm">
                            {keyword}
                          </span>
                        ))}
                      </div>
                    </div>
                    <div className="text-right text-sm text-gray-500">
                      {new Date(item.created_at).toLocaleString('ja-JP')}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
