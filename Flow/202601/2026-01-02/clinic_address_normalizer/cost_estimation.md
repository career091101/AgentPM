# Google Places API コスト試算

## API呼び出し回数（現在の仕様）

### パターンA: 5件候補すべて取得する場合

1医院の検索につき：
- **Places Text Search (New)**: 1回（5件の候補を取得）
- **Place Details (New)**: 5回（各候補の郵便番号を取得）
- **合計**: 6回のAPI呼び出し

### パターンB: 1件のみ取得する場合（元のmain.py）

1医院の検索につき：
- **Places Text Search (New)**: 1回（最大5件取得）
- **Place Details (New)**: 1回（上位1件のみ詳細取得）
- **合計**: 2回のAPI呼び出し

---

## Places API (New) 料金表（2026年1月時点）

### Places Text Search (New)

FieldMaskによって料金が異なります：

| FieldMask | 料金（1,000リクエストあたり） | 1リクエストあたり |
|-----------|---------------------------|-----------------|
| **Basic Data** (id, displayName, formattedAddress, location) | $32 | $0.032 |
| **Contact Data** (websiteUri) | +$3 | +$0.003 |
| **Atmosphere Data** (rating, userRatingCount) | +$5 | +$0.005 |

**今回のFieldMask**:
```
places.id,places.displayName,places.formattedAddress,
places.rating,places.userRatingCount,places.googleMapsUri,places.websiteUri
```

含まれるデータ:
- Basic Data: $0.032
- Contact Data (websiteUri): +$0.003
- Atmosphere Data (rating, userRatingCount): +$0.005

**合計: 約$0.040/リクエスト**

### Place Details (New)

| FieldMask | 料金（1,000リクエストあたり） | 1リクエストあたり |
|-----------|---------------------------|-----------------|
| **Basic Data** (addressComponents) | $17 | $0.017 |

---

## 1医院あたりのコスト

### パターンA: 5件候補すべて取得

```
Places Text Search: 1回 × $0.040 = $0.040
Place Details:      5回 × $0.017 = $0.085
─────────────────────────────────────────
合計:                             $0.125
```

**1医院あたり: 約$0.125（約18円 ※1ドル=145円換算）**

### パターンB: 1件のみ取得（元のmain.py仕様）

```
Places Text Search: 1回 × $0.040 = $0.040
Place Details:      1回 × $0.017 = $0.017
─────────────────────────────────────────
合計:                             $0.057
```

**1医院あたり: 約$0.057（約8円）**

---

## 無料枠で処理できる医院数

Google Cloudは**月$200の無料クレジット**があります（毎月リセット）。

### パターンA: 5件候補取得の場合

```
$200 / $0.125 = 1,600医院/月
```

**月間約1,600医院まで無料**

### パターンB: 1件のみ取得の場合

```
$200 / $0.057 = 3,508医院/月
```

**月間約3,500医院まで無料**

---

## 実例: 大量データ処理の場合

### ケース1: 10,000件の医院データ（5件候補取得）

```
総コスト: 10,000件 × $0.125 = $1,250
無料枠分: $200
実費:     $1,050（約152,000円）
```

### ケース2: 10,000件の医院データ（1件のみ取得）

```
総コスト: 10,000件 × $0.057 = $570
無料枠分: $200
実費:     $370（約53,650円）
```

---

## コスト削減策

### 1. google_maps_url を事前収集（最大50%削減）

`google_maps_url`カラムにGoogle MapsのURLが記載されている場合、
**Places Text Searchをスキップ**できます。

```
1医院あたり: $0.017のみ（Place Details）
10,000件:    $170（約24,650円）
無料枠内:    11,764件まで
```

### 2. 重複データを削除

同じ医院が複数回出現する場合、キャッシュ機能で重複API呼び出しを削減。

### 3. バッチ処理

月初に無料枠$200を使い切る前提で、月1,600〜3,500件を処理。

---

## 推奨運用方法

### 小規模（月500件以内）
- **パターンA（5件候補）**: 完全無料
- 候補を見比べて正確性を担保

### 中規模（月1,000〜3,000件）
- **パターンB（1件のみ）**: ほぼ無料
- 高精度な検索クエリを作成（city, area_hintを活用）

### 大規模（月10,000件以上）
- **事前にgoogle_maps_url収集**: $0.017/件
- または有料プランで処理（$200〜$1,000/月）

---

## 料金アラート設定（推奨）

Google Cloud Consoleで以下を設定：

1. **予算アラート**: $50, $100, $150, $200
2. **使用量モニタリング**: 毎日チェック
3. **自動停止**: $200到達時にAPI無効化

これで予期しない高額請求を防げます。

---

## 参考リンク

- [Places API (New) 料金](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing)
- [Google Maps Platform 料金計算ツール](https://mapsplatformtransition.withgoogle.com/calculator)
