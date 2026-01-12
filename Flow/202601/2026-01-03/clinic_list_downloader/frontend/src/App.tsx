import { useState, useEffect } from 'react'
import LoginForm from './components/LoginForm'
import SearchHistory from './components/SearchHistory'
import DownloadHistory from './components/DownloadHistory'
import MultiPrefectureSelector from './components/MultiPrefectureSelector'
import KeywordSelector from './components/KeywordSelector'
import ProgressCounter from './components/ProgressCounter'
import SearchButton from './components/SearchButton'
import ResultsTable from './components/ResultsTable'
import DownloadButton from './components/DownloadButton'
import { Prefecture } from './constants'
import { SearchResponse, SearchProgress } from './types'

function App() {
  // Authentication state
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [currentUsername, setCurrentUsername] = useState('')

  // History modal states
  const [showSearchHistory, setShowSearchHistory] = useState(false)
  const [showDownloadHistory, setShowDownloadHistory] = useState(false)

  // Search state
  const [selectedPrefectures, setSelectedPrefectures] = useState<Prefecture[]>([])
  const [selectedKeywords, setSelectedKeywords] = useState<string[]>(['歯科クリニック'])
  const [minRating, setMinRating] = useState<number>(0.0)
  const [minReviewCount, setMinReviewCount] = useState<number>(0)
  const [maxResults, setMaxResults] = useState<number>(500)
  const [loading, setLoading] = useState(false)
  const [searchResult, setSearchResult] = useState<SearchResponse | null>(null)
  const [error, setError] = useState<string | null>(null)

  // Real-time progress state
  const [realtimeProgress, setRealtimeProgress] = useState<SearchProgress>({
    total_queries: 0,
    completed_queries: 0,
    total_found: 0,
    unique_count: 0,
    current_prefecture: '',
    current_keyword: ''
  })

  // Check if already authenticated on mount
  useEffect(() => {
    const username = localStorage.getItem('auth_username')
    const password = localStorage.getItem('auth_password')

    if (username && password) {
      setCurrentUsername(username)
      setIsAuthenticated(true)
    }
  }, [])

  const handleLoginSuccess = (username: string) => {
    setCurrentUsername(username)
    setIsAuthenticated(true)
  }

  const handleLogout = () => {
    localStorage.removeItem('auth_username')
    localStorage.removeItem('auth_password')
    setIsAuthenticated(false)
    setCurrentUsername('')
    setSearchResult(null)
  }

  const handleSearch = async () => {
    if (selectedPrefectures.length === 0) {
      setError('都道府県を1つ以上選択してください')
      return
    }

    if (selectedKeywords.length === 0) {
      setError('キーワードを1つ以上選択してください')
      return
    }

    setLoading(true)
    setError(null)
    setSearchResult(null)
    setRealtimeProgress({
      total_queries: 0,
      completed_queries: 0,
      total_found: 0,
      unique_count: 0,
      current_prefecture: '',
      current_keyword: ''
    })

    try {
      const username = localStorage.getItem('auth_username')
      const password = localStorage.getItem('auth_password')

      const response = await fetch('/api/search/stream', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Basic ' + btoa(`${username}:${password}`)
        },
        body: JSON.stringify({
          prefectures: selectedPrefectures,
          keywords: selectedKeywords,
          min_rating: minRating,
          min_review_count: minReviewCount,
          max_results: maxResults,
        }),
      })

      if (!response.ok) {
        throw new Error(`検索に失敗しました: ${response.statusText}`)
      }

      const reader = response.body?.getReader()
      const decoder = new TextDecoder()

      if (!reader) {
        throw new Error('Response body is not readable')
      }

      let buffer = ''

      while (true) {
        const { done, value } = await reader.read()

        if (done) break

        buffer += decoder.decode(value, { stream: true })
        const lines = buffer.split('\n\n')
        buffer = lines.pop() || ''

        for (const line of lines) {
          if (!line.trim()) continue

          const eventMatch = line.match(/^event: (.+)$/)
          const dataMatch = line.match(/^data: (.+)$/m)

          if (!eventMatch || !dataMatch) continue

          const eventType = eventMatch[1]
          const data = JSON.parse(dataMatch[1])

          switch (eventType) {
            case 'start':
              setRealtimeProgress(data.progress)
              break

            case 'progress':
            case 'sub_progress':
              setRealtimeProgress(data.progress)
              break

            case 'keyword_complete':
              setRealtimeProgress(data.progress)
              break

            case 'complete':
              setSearchResult({
                prefectures: data.prefectures,
                keywords: data.keywords,
                total_count: data.total_count,
                clinics: data.clinics,
                progress: data.progress
              })
              setRealtimeProgress(data.progress)
              break

            case 'error':
              throw new Error(data.message)
          }
        }
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : '検索中にエラーが発生しました')
      setSearchResult(null)
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = async () => {
    if (selectedPrefectures.length === 0) return

    try {
      const username = localStorage.getItem('auth_username')
      const password = localStorage.getItem('auth_password')

      const params = new URLSearchParams({
        prefectures: selectedPrefectures.join(','),
        keywords: selectedKeywords.join(','),
        min_rating: minRating.toString(),
        min_review_count: minReviewCount.toString(),
        max_results: maxResults.toString(),
      })

      const response = await fetch(`/api/export?${params}`, {
        headers: {
          'Authorization': 'Basic ' + btoa(`${username}:${password}`)
        }
      })

      if (!response.ok) {
        throw new Error(`ダウンロードに失敗しました: ${response.statusText}`)
      }

      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url

      // Generate appropriate filename
      const filename = selectedPrefectures.length === 1
        ? `dental_clinics_${selectedPrefectures[0]}.csv`
        : `dental_clinics_${selectedPrefectures.length}prefectures.csv`

      a.download = filename
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'ダウンロード中にエラーが発生しました')
    }
  }

  // Show login form if not authenticated
  if (!isAuthenticated) {
    return <LoginForm onLoginSuccess={handleLoginSuccess} />
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 py-12 px-4 sm:px-6 lg:px-8">
      <SearchHistory isVisible={showSearchHistory} onClose={() => setShowSearchHistory(false)} />
      <DownloadHistory isVisible={showDownloadHistory} onClose={() => setShowDownloadHistory(false)} />

      <div className="max-w-7xl mx-auto">
        {/* User header with logout and history buttons */}
        <div className="flex justify-end gap-3 mb-6">
          <div className="flex items-center gap-2 bg-white rounded-xl px-4 py-2 shadow">
            <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
            <span className="text-sm font-medium text-gray-700">{currentUsername}</span>
          </div>

          <button
            onClick={() => setShowSearchHistory(true)}
            className="flex items-center gap-2 bg-blue-500 text-white px-4 py-2 rounded-xl hover:bg-blue-600 transition-all shadow"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <span className="text-sm font-medium">検索履歴</span>
          </button>

          <button
            onClick={() => setShowDownloadHistory(true)}
            className="flex items-center gap-2 bg-green-500 text-white px-4 py-2 rounded-xl hover:bg-green-600 transition-all shadow"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10" />
            </svg>
            <span className="text-sm font-medium">ダウンロード履歴</span>
          </button>

          <button
            onClick={handleLogout}
            className="flex items-center gap-2 bg-gray-500 text-white px-4 py-2 rounded-xl hover:bg-gray-600 transition-all shadow"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
            </svg>
            <span className="text-sm font-medium">ログアウト</span>
          </button>
        </div>

        <div className="text-center mb-12 animate-fade-in">
          <div className="inline-block mb-4">
            <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-4 rounded-2xl shadow-lg">
              <svg className="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
          </div>
          <h1 className="text-5xl font-extrabold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-4">
            歯科クリニックリストダウンローダー
          </h1>
          <p className="text-xl text-gray-700 font-medium">
            都道府県を選択して歯科クリニック情報をCSVでダウンロード
          </p>
        </div>

        <div className="bg-white rounded-2xl shadow-2xl border border-gray-100 p-8 mb-8 backdrop-blur-sm bg-white/90">
          <div className="flex flex-col items-center space-y-8">
            <MultiPrefectureSelector
              selectedPrefectures={selectedPrefectures}
              onChange={setSelectedPrefectures}
              disabled={loading}
            />

            <KeywordSelector
              selectedKeywords={selectedKeywords}
              onChange={setSelectedKeywords}
              disabled={loading}
            />

            <div className="w-full max-w-4xl">
              <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-6 shadow-inner">
                <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
                  <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                  </svg>
                  フィルター設定
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div className="bg-white rounded-lg p-4 shadow">
                    <label htmlFor="min-rating" className="block text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2">
                      <span className="text-yellow-500">⭐</span>
                      最小評価: {minRating.toFixed(1)}
                    </label>
                    <input
                      id="min-rating"
                      type="range"
                      min="0"
                      max="5"
                      step="0.5"
                      value={minRating}
                      onChange={(e) => setMinRating(parseFloat(e.target.value))}
                      disabled={loading}
                      className="w-full h-3 bg-gradient-to-r from-yellow-200 to-yellow-400 rounded-lg appearance-none cursor-pointer slider-thumb"
                    />
                    <div className="flex justify-between text-xs text-gray-500 mt-2 font-medium">
                      <span>0.0</span>
                      <span>5.0</span>
                    </div>
                  </div>

                  <div className="bg-white rounded-lg p-4 shadow">
                    <label htmlFor="min-review-count" className="block text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2">
                      <span className="text-blue-500">💬</span>
                      最小口コミ数: {minReviewCount}件
                    </label>
                    <input
                      id="min-review-count"
                      type="range"
                      min="0"
                      max="100"
                      step="5"
                      value={minReviewCount}
                      onChange={(e) => setMinReviewCount(parseInt(e.target.value))}
                      disabled={loading}
                      className="w-full h-3 bg-gradient-to-r from-blue-200 to-blue-400 rounded-lg appearance-none cursor-pointer slider-thumb"
                    />
                    <div className="flex justify-between text-xs text-gray-500 mt-2 font-medium">
                      <span>0</span>
                      <span>100</span>
                    </div>
                  </div>

                  <div className="bg-white rounded-lg p-4 shadow">
                    <label htmlFor="max-results" className="block text-sm font-semibold text-gray-700 mb-3 flex items-center gap-2">
                      <span className="text-purple-500">📊</span>
                      最大抽出件数: {maxResults}件
                    </label>
                    <input
                      id="max-results"
                      type="range"
                      min="50"
                      max="1000"
                      step="50"
                      value={maxResults}
                      onChange={(e) => setMaxResults(parseInt(e.target.value))}
                      disabled={loading}
                      className="w-full h-3 bg-gradient-to-r from-purple-200 to-purple-400 rounded-lg appearance-none cursor-pointer slider-thumb"
                    />
                    <div className="flex justify-between text-xs text-gray-500 mt-2 font-medium">
                      <span>50</span>
                      <span>1,000</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <SearchButton
              onClick={handleSearch}
              disabled={selectedPrefectures.length === 0 || selectedKeywords.length === 0}
              loading={loading}
            />

            <ProgressCounter
              progress={realtimeProgress}
              visible={loading}
            />

            {error && (
              <div className="w-full max-w-4xl p-4 bg-gradient-to-r from-red-50 to-pink-50 border-2 border-red-300 rounded-xl shadow-lg animate-shake">
                <div className="flex items-center gap-3">
                  <svg className="w-6 h-6 text-red-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <p className="text-sm font-medium text-red-800">{error}</p>
                </div>
              </div>
            )}

            {searchResult && (
              <div className="w-full max-w-4xl text-center">
                <div className="bg-gradient-to-r from-green-50 to-emerald-50 border-2 border-green-300 rounded-2xl p-6 shadow-lg mb-4">
                  <div className="flex items-center justify-center gap-3 mb-3">
                    <svg className="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <p className="text-2xl font-bold text-gray-800">
                      {searchResult.total_count}件のクリニックが見つかりました
                    </p>
                  </div>
                  <p className="text-sm text-gray-600 mb-4">
                    評価スコア順にソートされた高品質なクリニックデータです
                  </p>
                  <DownloadButton
                    onClick={handleDownload}
                    disabled={false}
                    count={searchResult.total_count}
                  />
                </div>
              </div>
            )}
          </div>
        </div>

        {searchResult && (
          <ResultsTable
            clinics={searchResult.clinics}
            prefectures={searchResult.prefectures}
          />
        )}

        <footer className="mt-12 text-center">
          <div className="inline-block bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg px-8 py-4 border border-gray-200">
            <p className="text-sm font-medium text-gray-600 flex items-center justify-center gap-2">
              <svg className="w-4 h-4 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
              </svg>
              Powered by Google Maps Platform API
            </p>
            <p className="mt-2 text-xs text-gray-500">© 2026 AIPM v0 Project</p>
          </div>
        </footer>
      </div>
    </div>
  )
}

export default App
