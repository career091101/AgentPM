import { PREFECTURES, Prefecture } from '../constants'

interface MultiPrefectureSelectorProps {
  selectedPrefectures: Prefecture[]
  onChange: (prefectures: Prefecture[]) => void
  disabled?: boolean
}

export default function MultiPrefectureSelector({
  selectedPrefectures,
  onChange,
  disabled = false
}: MultiPrefectureSelectorProps) {
  const handleToggle = (prefecture: Prefecture) => {
    if (selectedPrefectures.includes(prefecture)) {
      onChange(selectedPrefectures.filter(p => p !== prefecture))
    } else {
      onChange([...selectedPrefectures, prefecture])
    }
  }

  const handleSelectAll = () => {
    onChange([...PREFECTURES])
  }

  const handleDeselectAll = () => {
    onChange([])
  }

  return (
    <div className="w-full max-w-4xl">
      <div className="flex justify-between items-center mb-4">
        <label className="block text-lg font-bold text-gray-800 flex items-center gap-2">
          <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          都道府県を選択（複数選択可）
        </label>
        <div className="flex gap-2">
          <button
            type="button"
            onClick={handleSelectAll}
            disabled={disabled}
            className="px-4 py-2 text-sm font-semibold bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg hover:from-blue-600 hover:to-blue-700 shadow-md hover:shadow-lg transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none transition-all duration-200"
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

      <div className="border-2 border-gray-200 rounded-xl p-5 bg-gradient-to-br from-white to-gray-50 shadow-inner max-h-80 overflow-y-auto">
        {selectedPrefectures.length > 0 && (
          <div className="mb-4 pb-4 border-b-2 border-blue-100">
            <p className="text-sm font-semibold text-gray-700 mb-2 flex items-center gap-2">
              <svg className="w-4 h-4 text-green-600" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              選択中: <span className="text-blue-600 font-bold">{selectedPrefectures.length}件</span>
            </p>
            <div className="flex flex-wrap gap-2 mt-3">
              {selectedPrefectures.map(prefecture => (
                <span
                  key={prefecture}
                  className="inline-flex items-center px-3 py-1.5 text-sm bg-gradient-to-r from-blue-100 to-blue-200 text-blue-900 rounded-full font-medium shadow-sm hover:shadow-md transition-all"
                >
                  {prefecture}
                  <button
                    type="button"
                    onClick={() => handleToggle(prefecture)}
                    disabled={disabled}
                    className="ml-2 text-blue-700 hover:text-red-600 font-bold transition-colors"
                  >
                    ×
                  </button>
                </span>
              ))}
            </div>
          </div>
        )}

        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2">
          {PREFECTURES.map((prefecture) => (
            <label
              key={prefecture}
              className={`flex items-center p-2.5 rounded-lg cursor-pointer transition-all duration-200 ${
                selectedPrefectures.includes(prefecture)
                  ? 'bg-gradient-to-r from-blue-100 to-purple-100 shadow-md border-2 border-blue-300'
                  : 'bg-white hover:bg-gray-50 border-2 border-transparent hover:border-gray-200'
              } ${disabled ? 'cursor-not-allowed opacity-50' : 'hover:shadow-lg transform hover:scale-105'}`}
            >
              <input
                type="checkbox"
                checked={selectedPrefectures.includes(prefecture)}
                onChange={() => handleToggle(prefecture)}
                disabled={disabled}
                className="mr-2 h-4 w-4 text-blue-600 focus:ring-2 focus:ring-blue-500 border-gray-300 rounded cursor-pointer"
              />
              <span className={`text-sm ${selectedPrefectures.includes(prefecture) ? 'font-semibold text-blue-900' : 'font-medium text-gray-700'}`}>
                {prefecture}
              </span>
            </label>
          ))}
        </div>
      </div>
    </div>
  )
}
