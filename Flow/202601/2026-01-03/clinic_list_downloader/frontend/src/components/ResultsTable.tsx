import { ClinicData } from '../types'

interface ResultsTableProps {
  clinics: ClinicData[]
  prefectures: string[]
}

export default function ResultsTable({ clinics, prefectures }: ResultsTableProps) {
  if (clinics.length === 0) {
    return null
  }

  const prefectureDisplay = prefectures.length === 1
    ? prefectures[0]
    : `${prefectures.length}都道府県（${prefectures.slice(0, 3).join('、')}${prefectures.length > 3 ? '...' : ''}）`

  return (
    <div className="w-full mt-8">
      <div className="bg-white rounded-lg shadow-md overflow-hidden">
        <div className="px-6 py-4 bg-gray-50 border-b border-gray-200">
          <h2 className="text-xl font-semibold text-gray-800">
            検索結果: {prefectureDisplay} ({clinics.length}件)
          </h2>
          {prefectures.length > 1 && (
            <p className="text-sm text-gray-600 mt-1">
              選択: {prefectures.join('、')}
            </p>
          )}
        </div>

        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  クリニック名
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  住所
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  郵便番号
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  電話番号
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  評価
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  口コミ数
                </th>
                <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  ウェブサイト
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {clinics.slice(0, 20).map((clinic) => (
                <tr key={clinic.place_id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                    {clinic.clinic_name}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-500">
                    {clinic.address}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {clinic.postal_code || '-'}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {clinic.phone_number || '-'}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                    {clinic.rating > 0 ? (
                      <span className="inline-flex items-center">
                        {clinic.rating.toFixed(1)} <span className="text-yellow-500 ml-1">★</span>
                      </span>
                    ) : (
                      '-'
                    )}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {clinic.user_rating_count > 0 ? `${clinic.user_rating_count}件` : '-'}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-blue-600">
                    {clinic.website_url ? (
                      <a
                        href={clinic.website_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="hover:underline"
                      >
                        リンク
                      </a>
                    ) : (
                      '-'
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {clinics.length > 20 && (
          <div className="px-6 py-4 bg-gray-50 border-t border-gray-200 text-sm text-gray-600">
            ※ 最初の20件のみ表示しています。全{clinics.length}件をダウンロードするにはCSVボタンをクリックしてください。
          </div>
        )}
      </div>
    </div>
  )
}
