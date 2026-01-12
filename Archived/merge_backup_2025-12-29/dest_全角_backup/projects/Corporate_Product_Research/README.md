# Corporate_Product_Research

リクルート製品100件調査プロジェクト

## 目的

1. **CPF/PSF裏付け**: 起業の科学フレームワークの実証データ収集
2. **パターン抽出**: 成功・失敗パターンの体系化
3. **教材化**: orchestrate-phase1スキルへの参照事例追加

## 調査対象（目標100件）

### SUCCESS 60件

| ティア | 対象 | 目標件数 |
|--------|------|---------|
| TIER1_GLOBAL_MA | グローバルM&A | 10件 |
| TIER2_MEGA_HIT | 自社開発メガヒット | 15件 |
| TIER3_SAAS | SaaS製品 | 15件 |
| TIER4_DOMESTIC_MA | 国内M&A | 10件 |
| TIER5_NEW_BUSINESS | 新規事業成功 | 10件 |

### FAILURE 40件

| ティア | 対象 | 目標件数 |
|--------|------|---------|
| TIER6_CLEAR_WITHDRAWAL | 明確な撤退 | 15件 |
| TIER7_MA_FAILURE | M&A統合失敗 | 10件 |
| TIER8_STRATEGIC_EXIT | 戦略的撤退 | 15件 |

## ディレクトリ構造

```
Corporate_Product_Research/
├── README.md（本ファイル）
├── research_progress.md（進捗管理）
├── _templates/
│   ├── corporate_product_template.md
│   └── withdrawal_criteria.md
├── _index/
│   ├── master_index.md（全件索引）
│   ├── success_patterns.md（成功パターン）
│   └── failure_patterns.md（失敗パターン）
├── documents/
│   ├── SUCCESS/
│   │   ├── TIER1_GLOBAL_MA/
│   │   ├── TIER2_MEGA_HIT/
│   │   ├── TIER3_SAAS/
│   │   ├── TIER4_DOMESTIC_MA/
│   │   └── TIER5_NEW_BUSINESS/
│   └── FAILURE/
│       ├── TIER6_CLEAR_WITHDRAWAL/
│       ├── TIER7_MA_FAILURE/
│       └── TIER8_STRATEGIC_EXIT/
└── analysis/
    ├── cpf_patterns/（CPFパターン分析）
    ├── psf_patterns/（PSF 10倍優位性分析）
    └── withdrawal_analysis/（撤退基準分析）
```

## 調査基準

### 情報ソース

**Tier 1（公式情報 - 最優先）**:
- リクルートHD IR資料（決算説明資料、有価証券報告書）
- リクルートHD公式プレスリリース
- M&A発表資料

**Tier 2（信頼できるメディア）**:
- 日本経済新聞
- 東洋経済オンライン
- ダイヤモンド・オンライン
- 日経ビジネス

**Tier 3（二次情報 - 補完的使用）**:
- 書籍（『リクルートのすごい構"創"力』等）

### 品質保証基準

| 項目 | PASS基準 |
|------|----------|
| ソース数 | 3ソース以上 |
| ファクトチェック | 創業年・M&A年・撤退年すべて2ソース確認 |
| CPF検証データ | インタビュー数・課題共通率・WTPの3つ記載 |
| PSF検証データ | 10倍優位性2軸以上・MVP・UVP記載 |

## 実装ロードマップ

### Phase 1: プロジェクト立ち上げ（1-2週間）
- プロジェクト構造作成
- リクルートHD IR資料の全件調査
- 候補リスト作成
- パイロット事例調査（1件）
- 100件リスト確定

### Phase 2: 優先度A調査（25件 - 2-3週間）
- 並列バッチ実行（5件×5バッチ）
- CPF/PSFパターン分析（中間版）

### Phase 3: 優先度B調査（40件 - 4週間）
- 並列バッチ実行（5件×8バッチ）
- パターン分析の完全版

### Phase 4: 優先度C調査 + 最終統合（35件 - 3週間）
- 並列バッチ実行（5件×7バッチ）
- master_index.md、パターン分析、撤退基準体系化

**総所要期間**: 約2-3ヶ月

## 成功基準（KPI）

| 指標 | 目標値 |
|------|--------|
| 調査完了件数 | 100件 |
| PASS基準達成率 | 80%以上 |
| CPF検証データ充足率 | 60%以上 |
| PSF検証データ充足率 | 70%以上 |
| CPF成功パターン抽出 | 5パターン以上 |
| PSF 10倍優位性パターン抽出 | 5パターン以上 |
| 撤退理由分類 | 5カテゴリ以上 |

## 関連プロジェクト

- `Founder_Research/`: 世界的起業家500人調査（起業家個人）
- `Solopreneur_Research/`: ソロプレナー成功事例（517件）
- `startup_science/`: 起業の科学フレームワーク

## 作成日

2025-12-28
