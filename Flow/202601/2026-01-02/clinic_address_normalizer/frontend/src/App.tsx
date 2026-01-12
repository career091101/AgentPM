import { useState } from 'react'

// ========== 型定義 ==========

interface NormalizeRequest {
  clinic_query: string
  prefecture: string
  city?: string
  area_hint?: string
  google_maps_url?: string
}

interface NormalizeResponse {
  // 入力データ
  clinic_query: string
  prefecture: string
  city: string
  area_hint: string
  google_maps_url: string

  // 出力データ
  place_id: string
  display_name: string
  formatted_address: string
  postal_code: string
  lat: string
  lng: string
  match_confidence: string  // high/mid/low
  needs_manual_review: string  // true/false
  error_code: string
  error_message: string
}

// ========== メインコンポーネント ==========

function App() {
  // State管理
  const [formData, setFormData] = useState<NormalizeRequest>({
    clinic_query: '',
    prefecture: '',
    city: '',
    area_hint: '',
    google_maps_url: ''
  })
  const [result, setResult] = useState<NormalizeResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // フォーム送信処理
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('/api/normalize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'APIエラーが発生しました')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : '不明なエラーが発生しました')
    } finally {
      setLoading(false)
    }
  }

  // フォームリセット
  const handleReset = () => {
    setFormData({
      clinic_query: '',
      prefecture: '',
      city: '',
      area_hint: '',
      google_maps_url: ''
    })
    setResult(null)
    setError(null)
  }

  // ========== レンダリング ==========

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        {/* ヘッダー */}
        <header className="mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            歯科クリニック住所正規化ツール
          </h1>
          <p className="text-gray-600">
            Google Maps APIを使って医院データを正規化します
          </p>
        </header>

        {/* 入力フォーム */}
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <form onSubmit={handleSubmit} className="space-y-4">
            {/* 医院名（必須） */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                医院名 <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                value={formData.clinic_query}
                onChange={e => setFormData({...formData, clinic_query: e.target.value})}
                placeholder="例: 田中歯科クリニック"
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>

            {/* 都道府県（必須） */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                都道府県 <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                value={formData.prefecture}
                onChange={e => setFormData({...formData, prefecture: e.target.value})}
                placeholder="例: 東京都"
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                required
              />
            </div>

            {/* 市区町村（任意） */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                市区町村（任意）
              </label>
              <input
                type="text"
                value={formData.city}
                onChange={e => setFormData({...formData, city: e.target.value})}
                placeholder="例: 渋谷区"
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>

            {/* 地域ヒント（任意） */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                地域ヒント（任意）
              </label>
              <input
                type="text"
                value={formData.area_hint}
                onChange={e => setFormData({...formData, area_hint: e.target.value})}
                placeholder="例: 恵比寿"
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>

            {/* Google Maps URL（任意） */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Google Maps URL（任意）
              </label>
              <input
                type="url"
                value={formData.google_maps_url}
                onChange={e => setFormData({...formData, google_maps_url: e.target.value})}
                placeholder="https://maps.app.goo.gl/..."
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>

            {/* ボタン */}
            <div className="flex gap-4">
              <button
                type="submit"
                disabled={loading}
                className="flex-1 bg-blue-600 text-white px-6 py-3 rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors font-medium"
              >
                {loading ? (
                  <span className="flex items-center justify-center">
                    <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    処理中...
                  </span>
                ) : '正規化実行'}
              </button>
              <button
                type="button"
                onClick={handleReset}
                className="px-6 py-3 border border-gray-300 rounded-md hover:bg-gray-50 transition-colors font-medium"
              >
                リセット
              </button>
            </div>
          </form>
        </div>

        {/* エラー表示 */}
        {error && (
          <div className="bg-red-50 border border-red-300 text-red-800 px-6 py-4 rounded-lg mb-6">
            <div className="flex items-center">
              <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
              </svg>
              <strong className="font-medium">エラー:</strong>
              <span className="ml-2">{error}</span>
            </div>
          </div>
        )}

        {/* 結果表示 */}
        {result && (
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">正規化結果</h2>

            {/* エラーメッセージ（処理内エラー） */}
            {result.error_message && (
              <div className="bg-yellow-50 border border-yellow-300 text-yellow-800 px-4 py-3 rounded mb-4">
                <p className="font-medium">警告: {result.error_message}</p>
                <p className="text-sm">エラーコード: {result.error_code}</p>
              </div>
            )}

            {/* 基本情報 */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
              <div>
                <h3 className="text-sm font-medium text-gray-500">施設名</h3>
                <p className="text-lg font-semibold text-gray-900">{result.display_name || '未取得'}</p>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-500">信頼度</h3>
                <span className={`inline-block px-3 py-1 rounded-full text-sm font-medium ${
                  result.match_confidence === 'high' ? 'bg-green-100 text-green-800' :
                  result.match_confidence === 'mid' ? 'bg-yellow-100 text-yellow-800' :
                  'bg-red-100 text-red-800'
                }`}>
                  {result.match_confidence === 'high' ? '高' :
                   result.match_confidence === 'mid' ? '中' : '低'}
                </span>
              </div>
            </div>

            {/* 住所情報 */}
            <div className="space-y-3 mb-6">
              <div>
                <h3 className="text-sm font-medium text-gray-500">住所</h3>
                <p className="text-gray-900">{result.formatted_address || '未取得'}</p>
              </div>
              <div>
                <h3 className="text-sm font-medium text-gray-500">郵便番号</h3>
                <p className="text-gray-900">{result.postal_code || '未取得'}</p>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <h3 className="text-sm font-medium text-gray-500">緯度</h3>
                  <p className="text-gray-900">{result.lat || '未取得'}</p>
                </div>
                <div>
                  <h3 className="text-sm font-medium text-gray-500">経度</h3>
                  <p className="text-gray-900">{result.lng || '未取得'}</p>
                </div>
              </div>
            </div>

            {/* Place ID */}
            <div className="bg-gray-50 p-4 rounded-lg mb-4">
              <h3 className="text-sm font-medium text-gray-500 mb-1">Place ID</h3>
              <p className="text-xs font-mono text-gray-700 break-all">{result.place_id || '未取得'}</p>
            </div>

            {/* 要確認フラグ */}
            {result.needs_manual_review === 'true' && (
              <div className="bg-orange-50 border border-orange-300 text-orange-800 px-4 py-3 rounded">
                <div className="flex items-center">
                  <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                  </svg>
                  <strong className="font-medium">要確認:</strong>
                  <span className="ml-2">この結果は手動レビューが推奨されます</span>
                </div>
              </div>
            )}
          </div>
        )}

        {/* フッター */}
        <footer className="mt-8 text-center text-sm text-gray-600">
          <p>Powered by Google Maps Platform APIs</p>
        </footer>
      </div>
    </div>
  )
}

export default App
