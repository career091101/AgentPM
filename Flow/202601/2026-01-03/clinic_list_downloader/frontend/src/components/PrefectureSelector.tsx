import { PREFECTURES, Prefecture } from '../constants'

interface PrefectureSelectorProps {
  value: Prefecture | ''
  onChange: (prefecture: Prefecture) => void
  disabled?: boolean
}

export default function PrefectureSelector({ value, onChange, disabled = false }: PrefectureSelectorProps) {
  return (
    <div className="w-full max-w-md">
      <label htmlFor="prefecture" className="block text-sm font-medium text-gray-700 mb-2">
        都道府県を選択
      </label>
      <select
        id="prefecture"
        value={value}
        onChange={(e) => onChange(e.target.value as Prefecture)}
        disabled={disabled}
        className="block w-full px-4 py-3 text-base border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:cursor-not-allowed"
      >
        <option value="">都道府県を選択してください</option>
        {PREFECTURES.map((prefecture) => (
          <option key={prefecture} value={prefecture}>
            {prefecture}
          </option>
        ))}
      </select>
    </div>
  )
}
