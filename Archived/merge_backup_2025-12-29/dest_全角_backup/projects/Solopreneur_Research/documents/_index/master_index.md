---
id: "INDEX_MASTER"
title: "Solopreneur Research Master Index"
type: "index"
version: "1.0"
created_at: "2025-12-27"
updated_at: "2025-12-27"
total_documents: 250
total_persons: 150
---

# Solopreneur Research Master Index

全カテゴリ横断のマスターインデックス。RAG検索の起点として使用。

---

## ドキュメント統計

| カテゴリ | ドキュメント数 | YAML対応済み | 主要内容 |
|---------|---------------|-------------|----------|
| **01_App** | 106 | 1 (参考実装) | アプリ開発者事例 |
| **02_Newsletter** | ~80 | 0 | ニュースレター戦略・事例 |
| **03_SNS** | ~70 | 1 (参考実装) | SNS成長戦略事例 |
| **_templates** | 5 | 3 (v4.0対応) | ドキュメントテンプレート |
| **_index** | 3 | 3 | インデックスファイル |
| **_cross_reference** | 1 | 1 | クロスリファレンス |

---

## カテゴリ別インデックス

| カテゴリ | インデックスファイル | 説明 |
|---------|---------------------|------|
| App | [01_App/index.md](../01_App/index.md) | 106件のアプリ開発者事例 |
| SNS | [03_SNS/index.md](../03_SNS/index.md) | ~70件のSNS成長戦略事例 |
| Newsletter | (作成予定) | ~80件のニュースレター関連文書 |

---

## 収益ティア別クイックリファレンス

### $100K+ MRR

| ID | 人物名 | カテゴリ | プロダクト | MRR | ファイル |
|----|--------|---------|----------|-----|----------|
| APP_003 | Pieter Levels | App | PhotoAI | $237K | [003_pieter_levels.md](../01_App/case_studies/003_pieter_levels.md) |
| APP_018 | Tony Dinh | App | TypingMind | $142K | [018_tony_dinh.md](../01_App/case_studies/018_tony_dinh.md) |
| SNS_001 | Pieter Levels | SNS | - | $360K | [pieter_levels](../03_SNS/case_studies/pieter_levels/sns_analysis.md) |

### $50K-100K MRR

| ID | 人物名 | カテゴリ | プロダクト | MRR | ファイル |
|----|--------|---------|----------|-----|----------|
| APP_001 | Wilson Wilson | App | Senja | $50K | [001_wilson_senja.md](../01_App/case_studies/001_wilson_senja.md) |
| APP_014 | Danny Postma | App | HeadshotPro | $75K | [014_danny_postma.md](../01_App/case_studies/014_danny_postma.md) |

---

## 成長戦略別クイックリファレンス

### Build in Public

| ID | 人物名 | カテゴリ | 結果 | ファイル |
|----|--------|---------|------|----------|
| APP_003 | Pieter Levels | App | $237K MRR | [003_pieter_levels.md](../01_App/case_studies/003_pieter_levels.md) |
| APP_001 | Wilson Wilson | App | $50K MRR | [001_wilson_senja.md](../01_App/case_studies/001_wilson_senja.md) |
| SNS_001 | Pieter Levels | SNS | 785K followers | [pieter_levels](../03_SNS/case_studies/pieter_levels/sns_analysis.md) |

### TikTok Viral

| ID | 人物名 | カテゴリ | 結果 | ファイル |
|----|--------|---------|------|----------|
| APP_005 | Brock Anderson | App | 1.2M followers | [005_brock_anderson.md](../01_App/case_studies/005_brock_anderson.md) |

### SEO First

| ID | 人物名 | カテゴリ | 結果 | ファイル |
|----|--------|---------|------|----------|
| APP_014 | Danny Postma | App | $75K MRR | [014_danny_postma.md](../01_App/case_studies/014_danny_postma.md) |

---

## ニッチ別クイックリファレンス

### AI Tools

| ID | 人物名 | プロダクト | MRR |
|----|--------|----------|-----|
| APP_003 | Pieter Levels | PhotoAI | $118K |
| APP_018 | Tony Dinh | TypingMind | $137K |

### SaaS / Testimonials

| ID | 人物名 | プロダクト | MRR |
|----|--------|----------|-----|
| APP_001 | Wilson Wilson | Senja | $50K |

### Remote Work

| ID | 人物名 | プロダクト | MRR |
|----|--------|----------|-----|
| APP_003 | Pieter Levels | NomadList, RemoteOK | $228K |

---

## クロスリファレンス

| ファイル | 説明 |
|----------|------|
| [person_registry.md](../_cross_reference/person_registry.md) | 同一人物の複数カテゴリ文書リンク |
| (strategy_patterns.md) | 戦略パターン別クロスリファレンス（作成予定） |

---

## 日本市場適用性 TOP 10

| # | ID | 人物名 | スコア | 理由 |
|---|-----|--------|--------|------|
| 1 | APP_018 | Tony Dinh | 3.6 | 開発者ツール、ローカライズ容易 |
| 2 | APP_003 | Pieter Levels | 3.6 | AI活用、グローバル展開 |
| 3 | APP_001 | Wilson Wilson | 3.4 | SaaS、日本市場ニーズあり |

---

## RAGクエリ例

このインデックスを使用したRAG検索の例：

```python
# 例1: $50K以上のBuild in Public事例
filter = {
    "mrr_tier": {"$in": ["50k+", "100k+"]},
    "tags.growth_strategy": {"$contains": "build_in_public"}
}

# 例2: AI Tools x Twitter成長
filter = {
    "tags.niche": {"$contains": "ai_tools"},
    "tags.marketing_channel": {"$contains": "twitter"}
}

# 例3: 日本市場適用性3.5以上
filter = {
    "japan_score.total": {"$gte": 3.5}
}
```

---

## ファイル構造

```
documents/
├── _index/
│   ├── master_index.md          # このファイル
│   └── taxonomy.yaml            # 統制語彙定義
├── _cross_reference/
│   └── person_registry.md       # 人物レジストリ
├── _templates/
│   ├── case_study_template.md   # App用 v4.0
│   ├── sns_analysis_template.md # SNS用 v1.0
│   └── ...
├── 01_App/
│   ├── index.md                 # Appインデックス
│   └── case_studies/
├── 02_Newsletter/
│   └── ...
└── 03_SNS/
    ├── index.md                 # SNSインデックス
    └── case_studies/
```

---

## 更新履歴

| 日付 | 変更内容 |
|------|----------|
| 2025-12-27 | 初版作成、RAG最適化構造導入 |
