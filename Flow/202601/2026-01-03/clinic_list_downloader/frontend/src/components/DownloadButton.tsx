interface DownloadButtonProps {
  onClick: () => void
  disabled: boolean
  count: number
}

export default function DownloadButton({ onClick, disabled, count }: DownloadButtonProps) {
  if (count === 0) {
    return null
  }

  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className="relative px-8 py-4 text-white text-lg font-bold bg-gradient-to-r from-green-500 to-emerald-600 rounded-2xl shadow-xl hover:shadow-2xl transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-green-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none transition-all duration-300 overflow-hidden group"
    >
      <div className="absolute inset-0 bg-gradient-to-r from-green-600 to-emerald-700 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
      <span className="relative z-10 flex items-center justify-center gap-3">
        <svg className="w-6 h-6 animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
        </svg>
        CSVダウンロード ({count.toLocaleString()}件)
      </span>
    </button>
  )
}
