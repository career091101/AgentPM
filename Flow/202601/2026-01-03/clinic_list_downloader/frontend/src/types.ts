// API型定義

export interface ClinicData {
  place_id: string
  clinic_name: string
  address: string
  postal_code: string
  phone_number: string
  website_url: string
  rating: number
  user_rating_count: number
}

export interface SearchProgress {
  total_queries: number
  completed_queries: number
  total_found: number
  unique_count: number
  current_prefecture: string
  current_keyword: string
}

export interface SearchResponse {
  prefectures: string[]
  keywords: string[]
  total_count: number
  clinics: ClinicData[]
  progress: SearchProgress
}

export interface SearchRequest {
  prefectures: string[]
  keywords?: string[]
  min_rating?: number
  min_review_count?: number
  max_results?: number
}
