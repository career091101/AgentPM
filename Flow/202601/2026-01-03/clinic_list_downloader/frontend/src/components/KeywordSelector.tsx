import { useState } from 'react'

// デフォルトキーワードリスト
const DEFAULT_KEYWORDS = [
  '歯科クリニック',
  'デンタルクリニック',
  'dental clinic',
  '歯医者',
  '歯科医院',
  '矯正歯科',
  '小児歯科',
  '審美歯科',
  'インプラント',
  'ホワイトニング',
]

interface KeywordSelectorProps {
  selectedKeywords: string[]
  onChange: (keywords: string[]) => void
  disabled?: boolean
}

export default function KeywordSelector({
  selectedKeywords,
  onChange,
  disabled = false
}: KeywordSelectorProps) {
  const [customKeyword, setCustomKeyword] = useState('')

  const handleToggle = (keyword: string) => {
    if (selectedKeywords.includes(keyword)) {
      onChange(selectedKeywords.filter(k => k !== keyword))
    } else {
      onChange([...selectedKeywords, keyword])
    }
  }

  const handleAddCustomKeyword = () => {
    const trimmedKeyword = customKeyword.trim()
    if (trimmedKeyword && !selectedKeywords.includes(trimmedKeyword) && !DEFAULT_KEYWORDS.includes(trimmedKeyword)) {
      onChange([...selectedKeywords, trimmedKeyword])
      setCustomKeyword('')
    }
  }

  const handleRemoveCustomKeyword = (keyword: string) => {
    onChange(selectedKeywords.filter(k => k !== keyword))
  }

  const handleSelectAll = () => {
    onChange([...DEFAULT_KEYWORDS])
  }

  const handleDeselectAll = () => {
    onChange([])
  }

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault()
      handleAddCustomKeyword()
    }
  }

  // カスタムキーワード（デフォルトリストにないもの）
  const customKeywords = selectedKeywords.filter(k => !DEFAULT_KEYWORDS.includes(k))

  return (
    <div className="w-full max-w-4xl">
      <div className="flex justify-between items-center mb-4">
        <label className="block text-lg font-bold text-gray-800 flex items-center gap-2">
          <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14" />
          </svg>
          検索キーワードを選択（複数選択可）
        </label>
        <div className="flex gap-2">
          <button
            type="button"
            onClick={handleSelectAll}
            disabled={disabled}
            className="px-4 py-2 text-sm font-semibold bg-gradient-to-r from-purple-500 to-purple-600 text-white rounded-lg hover:from-purple-600 hover:to-purple-700 shadow-md hover:shadow-lg transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none transition-all duration-200"
          >
            ✓ 全選択
          </button>
          <button
            type="button"
            onClick={handleDeselectAll}
            disabled={disabled}
            className="px-4 py-2 text-sm font-semibold bg-gradient-to-r from-gray-500 to-gray-600 text-white rounded-lg hover:from-gray-600 hover:to-gray-700 shadow-md hover:shadow-lg transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none transition-all duration-200"
          >
            × 全解除
          </button>
        </div>
      </div>

      <div className="border-2 border-gray-200 rounded-xl p-5 bg-gradient-to-br from-white to-gray-50 shadow-inner">
        {/* 選択中のキーワード表示 */}
        {selectedKeywords.length > 0 && (
          <div className="mb-4 pb-4 border-b-2 border-purple-100">
            <p className="text-sm font-semibold text-gray-700 mb-2 flex items-center gap-2">
              <svg className="w-4 h-4 text-green-600" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              選択中: <span className="text-purple-600 font-bold">{selectedKeywords.length}件</span>
            </p>
            <div className="flex flex-wrap gap-2 mt-3">
              {selectedKeywords.map(keyword => (
                <span
                  key={keyword}
                  className="inline-flex items-center px-3 py-1.5 text-sm bg-gradient-to-r from-purple-100 to-purple-200 text-purple-900 rounded-full font-medium shadow-sm hover:shadow-md transition-all"
                >
                  {keyword}
                  <button
                    type="button"
                    onClick={() => handleToggle(keyword)}
                    disabled={disabled}
                    className="ml-2 text-purple-700 hover:text-red-600 font-bold transition-colors"
                  >
                    ×
                  </button>
                </span>
              ))}
            </div>
          </div>
        )}

        {/* デフォルトキーワード選択 */}
        <div className="mb-4">
          <h4 className="text-sm font-bold text-gray-700 mb-3">デフォルトキーワード</h4>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2">
            {DEFAULT_KEYWORDS.map((keyword) => (
              <label
                key={keyword}
                className={`flex items-center p-2.5 rounded-lg cursor-pointer transition-all duration-200 ${
                  selectedKeywords.includes(keyword)
                    ? 'bg-gradient-to-r from-purple-100 to-pink-100 shadow-md border-2 border-purple-300'
                    : 'bg-white hover:bg-gray-50 border-2 border-transparent hover:border-gray-200'
                } ${disabled ? 'cursor-not-allowed opacity-50' : 'hover:shadow-lg transform hover:scale-105'}`}
              >
                <input
                  type="checkbox"
                  checked={selectedKeywords.includes(keyword)}
                  onChange={() => handleToggle(keyword)}
                  disabled={disabled}
                  className="mr-2 h-4 w-4 text-purple-600 focus:ring-2 focus:ring-purple-500 border-gray-300 rounded cursor-pointer"
                />
                <span className={`text-sm ${selectedKeywords.includes(keyword) ? 'font-semibold text-purple-900' : 'font-medium text-gray-700'}`}>
                  {keyword}
                </span>
              </label>
            ))}
          </div>
        </div>

        {/* カスタムキーワード追加 */}
        <div className="mt-4 pt-4 border-t-2 border-gray-200">
          <h4 className="text-sm font-bold text-gray-700 mb-3 flex items-center gap-2">
            <svg className="w-4 h-4 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
            カスタムキーワード追加
          </h4>
          <div className="flex gap-2">
            <input
              type="text"
              value={customKeyword}
              onChange={(e) => setCustomKeyword(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="独自のキーワードを入力..."
              disabled={disabled}
              className="flex-1 px-4 py-2 border-2 border-gray-300 rounded-lg focus:border-purple-500 focus:ring-2 focus:ring-purple-200 outline-none transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            />
            <button
              type="button"
              onClick={handleAddCustomKeyword}
              disabled={disabled || !customKeyword.trim()}
              className="px-6 py-2 text-sm font-semibold bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-lg hover:from-purple-600 hover:to-pink-600 shadow-md hover:shadow-lg transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none transition-all duration-200"
            >
              追加
            </button>
          </div>

          {/* 追加されたカスタムキーワード */}
          {customKeywords.length > 0 && (
            <div className="mt-3">
              <p className="text-xs text-gray-600 mb-2">追加したキーワード:</p>
              <div className="flex flex-wrap gap-2">
                {customKeywords.map(keyword => (
                  <span
                    key={keyword}
                    className="inline-flex items-center px-3 py-1.5 text-sm bg-gradient-to-r from-pink-100 to-purple-100 text-purple-900 rounded-full font-medium shadow-sm"
                  >
                    {keyword}
                    <button
                      type="button"
                      onClick={() => handleRemoveCustomKeyword(keyword)}
                      disabled={disabled}
                      className="ml-2 text-purple-700 hover:text-red-600 font-bold transition-colors"
                    >
                      ×
                    </button>
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
