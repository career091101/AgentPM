# インターネット調査に基づく解決策提案

**調査日**: 2026-01-02
**目的**: Instagram歯科医院データ収集の課題に対する代替ソリューションの特定

---

## 現在の課題まとめ

1. **Instagramハッシュタグ検索がスパムで汚染**（@ysato1101の投稿が支配）
2. **プロフィール抽出率が低い**（3.9%）
3. **1000件目標に対して実績0件**
4. **スケーラビリティの限界**

---

## 調査結果に基づく解決策

### 解決策1: Google Site Search + Instagram URL抽出【最も実用的】

#### 概要
Instagramの検索制限を回避するため、**Googleのサイト内検索**を利用します。

#### 手法
```
site:instagram.com/p/ 歯科医院 東京
site:instagram.com/p/ 歯科 新宿
site:instagram.com/p/ デンタルクリニック 渋谷
```

#### メリット
- ✅ Instagramのスパムフィルタを回避
- ✅ Googleの検索精度を活用（スパム投稿が除外される）
- ✅ 無料（追加コストなし）
- ✅ 実装が簡単（Google Custom Search API使用）

#### 実装ステップ
1. **Google Custom Search API**セットアップ（無料枠: 100リクエスト/日）
2. 地域別クエリ実行:
   ```python
   queries = [
       "site:instagram.com/p/ 歯科医院 東京",
       "site:instagram.com/p/ 歯科 渋谷",
       "site:instagram.com/p/ デンタルクリニック 新宿"
   ]
   ```
3. 投稿URLリストを取得
4. 各URLからプロフィール情報を抽出（既存のbrowser_collector.py使用）

#### 期待成果
- **収集件数**: 500-1000件（地域による）
- **データ品質**: ⭐⭐⭐⭐ (4/5)
- **実装時間**: 2-3時間
- **コスト**: 無料（100リクエスト/日）または月5ドル（10,000リクエスト/日）

#### 参考資料
- [How to Scrape Instagram in 2026 - Scrapfly](https://scrapfly.io/blog/posts/how-to-scrape-instagram)
- [Instagram Scraping Complete Guide 2025 - ScrapeCreators](https://scrapecreators.com/blog/how-to-scrape-instagram-data-the-complete-2025-guide)

---

### 解決策2: 日本の歯科医院データベース活用【最も確実】

#### 概要
既存の**商用/政府データベース**から歯科医院データを取得し、Instagramアカウントをクロスチェックします。

#### 利用可能なデータベース

| サービス | 件数 | 価格 | データ項目 | API |
|---------|------|------|-----------|-----|
| **SCUEL** | 22万件（全医療機関） | 無料API（要申請） | 住所、電話、診療科目、売上 | ✅ |
| **Wellness (WDB)** | 歯科医院全国網羅 | 有料（要問合せ） | 施設属性、診療実績、設備 | ❓ |
| **政府統計 (e-Stat)** | 全国医療施設 | 無料API（要登録） | 基本情報、地域別 | ✅ |
| **Econos** | 約15.7万件 | Excel購入 | 基本情報 | ❌ |

#### 推奨: SCUELデータベース

**理由**:
- ✅ 無料API提供（条件付き）
- ✅ 22万件の医療機関データ（歯科医院含む）
- ✅ 230以上のデータフィールド
- ✅ 月次更新

**実装ステップ**:
1. SCUELに無料API利用申請（https://scueldata.me/）
2. 歯科医院データを地域別に取得
3. 医院名から Instagram handle を推測
   ```python
   clinic_name = "渋谷歯科医院"
   instagram_handle = "shibuya_dental_clinic"
   ```
4. Instagram プロフィール存在確認
5. データ統合（SCUEL住所データ + Instagram情報）

#### 期待成果
- **収集件数**: 1000-5000件
- **住所データ率**: 100%（SCUEL保証）
- **Instagram アカウント確認率**: 30-50%
- **データ品質**: ⭐⭐⭐⭐⭐ (5/5)
- **実装時間**: 3-4時間
- **コスト**: 無料

#### 参考資料
- [SCUEL歯科データベース](https://scueldata.me/dental/)
- [医療・介護データベース - Wellness](https://www.wellness.co.jp/wdb/)
- [政府統計 e-Stat API](https://www.e-stat.go.jp/stat-search/database?toukei=00450021)

---

### 解決策3: Instagram Graph API (Business Discovery)

#### 概要
Instagram公式APIの**Business Discovery**エンドポイントを使用します。

#### 仕様
- **対象**: ビジネス/クリエイターアカウントのみ
- **レート制限**: 200リクエスト/時/アカウント
- **データアクセス**: 公開プロフィール、投稿、フォロワー数等

#### メリット
- ✅ 公式API（利用規約違反リスクなし）
- ✅ 安定したデータ取得
- ✅ レート制限が明確

#### デメリット
- ❌ ビジネスアカウント認証が必要（審査1-2週間）
- ❌ 個人アカウントの歯科医院は取得不可
- ❌ レート制限が厳しい（200リクエスト/時）

#### 実装コスト
- **審査時間**: 1-2週間
- **開発時間**: 4-6時間
- **API コスト**: 無料
- **データ品質**: ⭐⭐⭐⭐ (4/5)

#### 参考資料
- [Instagram Graph API Complete Guide 2025 - Elfsight](https://elfsight.com/blog/instagram-graph-api-complete-developer-guide-for-2025/)
- [Instagram API for Businesses 2025 - Tagembed](https://tagembed.com/blog/instagram-api/)

---

### 解決策4: Google Maps API代替（無料/低コスト）

#### 概要
Google Maps APIの代わりに、**無料/低コストの代替サービス**を使用します。

#### 代替サービス比較

| サービス | 無料枠 | 特徴 | POI検索 |
|---------|-------|------|---------|
| **OpenStreetMap** | 完全無料 | オープンソース、コミュニティ運営 | ✅ |
| **Mapbox** | 100,000リクエスト/月 | 人気の高い代替、優れたUI | ✅ |
| **HERE Maps** | 250リクエスト/日 | 優れたルーティング機能 | ✅ |
| **MapTiler** | 100,000タイル/月 | 詳細な地図データ | ❓ |

#### 推奨: Mapbox Places API

**理由**:
- ✅ 無料枠が大きい（100,000リクエスト/月 = 約3,300リクエスト/日）
- ✅ POI検索に対応（歯科医院検索可能）
- ✅ APIドキュメントが充実
- ✅ クレジットカード登録不要（無料枠内）

**実装例**:
```python
import requests

# Mapbox Places API
url = "https://api.mapbox.com/geocoding/v5/mapbox.places/歯科医院.json"
params = {
    "access_token": "YOUR_MAPBOX_TOKEN",
    "proximity": "139.7,35.7",  # 東京の座標
    "limit": 10
}

response = requests.get(url, params=params)
dental_clinics = response.json()
```

#### 期待成果
- **収集件数**: 500-2000件（地域による）
- **住所データ率**: 100%
- **実装時間**: 2-3時間
- **コスト**: 無料（無料枠内）

#### 参考資料
- [12 Best Google Maps API Alternatives - Radar](https://radar.com/blog/google-maps-api-alternatives-competitors)
- [5 Powerful Alternatives to Google Maps API - Nordic APIs](https://nordicapis.com/5-powerful-alternatives-to-google-maps-api/)
- [7 Free Map APIs Compared to Google Maps - Felt](https://felt.com/blog/7-free-map-apis-compared-to-google-maps)

---

### 解決策5: Instagram ハッシュタグ戦略の改善

#### 背景: 2025年のInstagramハッシュタグ制限

**重要な変更**:
- Instagramは2025年12月に**ハッシュタグを5個に制限**
- スパム対策として実施（Adam Mosseri発表）
- AI駆動の発見機能へ移行（ハッシュタグ依存度低下）

#### 新しいベストプラクティス

**従来のアプローチ**:
```
❌ 20-30個のハッシュタグを乱用
❌ トレンドと無関係なキーワードを追加
```

**2025年の推奨アプローチ**:
```
✅ 3-5個の高関連性ハッシュタグのみ使用
✅ ニッチ特化型タグを選択
✅ キャプションにSEOキーワードを含める
```

#### 歯科医院検索への応用

**改善されたハッシュタグ戦略**:
```python
hashtags = [
    # 地域特化型（効果的）
    "#渋谷歯科医院",
    "#新宿デンタルクリニック",

    # ニッチ特化型
    "#東京審美歯科",
    "#インプラント専門医",

    # 一般的なタグは避ける（スパムが多い）
    # ❌ "#歯科"
    # ❌ "#ホワイトニング"
]
```

#### 実装の改善

**既存コードの最適化**:
```python
# config.yaml の更新
instagram:
  hashtags:
    - "渋谷歯科医院"
    - "新宿デンタルクリニック"
    - "東京審美歯科"
    - "港区小児歯科"
    - "六本木矯正歯科"
  posts_per_hashtag: 50  # 100→50に削減
  scroll_count: 10  # 3→10に増加
```

#### 期待成果
- **データ品質**: ⭐⭐⭐ (3/5)（改善されるが、劇的ではない）
- **実装時間**: 30分
- **コスト**: 無料

#### 参考資料
- [Instagram Hashtag Limit 2025: Why Only 3-5 Hashtags Work - Prominds](https://prominds.digital/instagram-hashtag-limit-2025/)
- [Instagram Introduces New Hashtag Rules to Tackle Spam - Android Headlines](https://www.androidheadlines.com/2025/12/instagram-new-hashtag-rules-tackle-spam.html)
- [Instagram Hashtag Spam Limit: 5-Tag Rule - GSM Rumors](https://gsmrumors.com/instagram-hashtag-spam-limit/)

---

## 推奨実装順序

### フェーズ1: 短期（即日実施可能）

**1位: Google Site Search + Instagram URL抽出**
- **実装時間**: 2-3時間
- **コスト**: 無料（または月5ドル）
- **期待収集件数**: 500-1000件
- **優先度**: ⭐⭐⭐⭐⭐

**手順**:
1. Google Custom Search API セットアップ
2. サイト内検索クエリ実行（地域別）
3. Instagram投稿URL抽出
4. 既存browser_collector.pyでプロフィール取得

---

### フェーズ2: 中期（1-2日で実施）

**2位: SCUELデータベース + Instagram クロス検索**
- **実装時間**: 3-4時間（API申請時間除く）
- **コスト**: 無料
- **期待収集件数**: 1000-5000件
- **優先度**: ⭐⭐⭐⭐⭐

**手順**:
1. SCUEL無料API利用申請
2. 歯科医院データ取得（地域別）
3. Instagram handle 推測ロジック実装
4. プロフィール存在確認 + データ統合

---

### フェーズ3: 長期（1-2週間）

**3位: Instagram Graph API (Business Discovery)**
- **実装時間**: 4-6時間 + 審査1-2週間
- **コスト**: 無料
- **期待収集件数**: 200-500件（レート制限による）
- **優先度**: ⭐⭐⭐

**手順**:
1. Meta Developer アカウント作成
2. Instagram Business Account 認証申請
3. Graph API統合
4. Business Discovery エンドポイント実装

---

## 複合戦略（最も推奨）

### ハイブリッドアプローチ

**ステップ1**: SCUELデータベースで基礎データ取得（住所保証）
**ステップ2**: Google Site Search でInstagram投稿URL発見
**ステップ3**: 既存スクレイピングでプロフィール詳細取得
**ステップ4**: データ統合（SCUEL住所 + Instagram プロフィール）

#### 期待成果
- **収集件数**: 2000-5000件
- **住所データ率**: 100%（SCUEL保証）
- **Instagram プロフィール率**: 40-60%
- **データ品質**: ⭐⭐⭐⭐⭐ (5/5)
- **総実装時間**: 4-6時間
- **総コスト**: 無料-月10ドル

---

## 次のアクション

### 即座に実行すべきこと

1. **Google Site Search アプローチのテスト実装**（2-3時間）
   - Google Custom Search API セットアップ
   - 初期テスト（100件収集）
   - データ品質確認

2. **SCUELデータベース調査**（30分）
   - 無料API利用条件の確認
   - 申請手続きの開始

3. **既存ハッシュタグ戦略の改善**（30分）
   - 地域特化型ハッシュタグへの変更
   - config.yaml更新

### ユーザー承認が必要な事項

- [ ] Google Custom Search API 利用の承認（無料枠: 100リクエスト/日、有料: 月5ドル）
- [ ] SCUEL無料API申請の承認（条件確認後）
- [ ] Mapbox API利用の承認（無料枠: 100,000リクエスト/月）
- [ ] 実装優先度の決定（フェーズ1 → フェーズ2の順推奨）

---

## 参考資料まとめ

### Instagram スクレイピング
- [How to Scrape Instagram in 2026 - Scrapfly](https://scrapfly.io/blog/posts/how-to-scrape-instagram)
- [Instagram Scraping Complete Guide 2025 - ScrapeCreators](https://scrapecreators.com/blog/how-to-scrape-instagram-data-the-complete-2025-guide)
- [Best Instagram Scrapers of 2025 - Proxyway](https://proxyway.com/best/instagram-scrapers)
- [How to Scrape Social Media Data in 2026 - ZenRows](https://www.zenrows.com/blog/social-media-scraping)

### 歯科医院データベース
- [SCUEL歯科データベース](https://scueldata.me/dental/)
- [医療・介護データベース - Wellness](https://www.wellness.co.jp/wdb/)
- [政府統計 e-Stat 医療施設調査](https://www.e-stat.go.jp/stat-search/database?toukei=00450021)
- [知る人ぞ知る、病院リスト・病院データベースの入手方法 - Exemedical](https://exemedical.jp/post-800/)

### Instagram ハッシュタグ問題
- [Instagram Hashtag Limit 2025: Why Only 3-5 Hashtags Work - Prominds](https://prominds.digital/instagram-hashtag-limit-2025/)
- [Instagram Introduces New Hashtag Rules to Tackle Spam - Android Headlines](https://www.androidheadlines.com/2025/12/instagram-new-hashtag-rules-tackle-spam.html)
- [Instagram Shadowban 2025 - Andrew Lee Ventures](https://andrewlee.ventures/blog/instagram-shadowban-what-it-is-and-how-to-remove-it)

### Google Maps API 代替
- [12 Best Google Maps API Alternatives - Radar](https://radar.com/blog/google-maps-api-alternatives-competitors)
- [5 Powerful Alternatives to Google Maps API - Nordic APIs](https://nordicapis.com/5-powerful-alternatives-to-google-maps-api/)
- [7 Free Map APIs Compared to Google Maps - Felt](https://felt.com/blog/7-free-map-apis-compared-to-google-maps)

### Instagram Graph API
- [Instagram Graph API Complete Guide 2025 - Elfsight](https://elfsight.com/blog/instagram-graph-api-complete-developer-guide-for-2025/)
- [Instagram API for Businesses 2025 - Tagembed](https://tagembed.com/blog/instagram-api/)

---

**レポート作成日**: 2026-01-02
**調査実施**: Claude Code Agent (Sonnet 4.5) + WebSearch
**ファイルパス**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/DentalInstagramScraper/RESEARCH_BASED_SOLUTIONS.md`
