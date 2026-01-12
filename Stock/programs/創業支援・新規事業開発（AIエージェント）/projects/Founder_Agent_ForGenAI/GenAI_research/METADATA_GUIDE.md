# GenAI_research 統一メタデータ適用ガイド

**作成日**: 2025-12-31
**バージョン**: 1.0
**目的**: GenAI_research内の全ファイルに統一メタデータを適用するための標準とガイドライン

---

## 概要

GenAI_research フォルダには1,700以上のファイルが含まれており、効率的な検索・分類・LLM読み込みのためには統一されたメタデータ構造が必要です。本ガイドでは、ファイルタイプ別の標準メタデータフォーマットと適用手順を定義します。

---

## メタデータ標準（3種類）

### 1. Markdown用YAMLフロントマター

**用途**: Markdownファイル（.md）の先頭に記載

**必須フィールド**:
```yaml
---
title: "ドキュメントタイトル"
date: "2025-12-31"
source: "出典（URL、書籍名、著者名など）"
tags: ["AI", "Startup", "Technology"]
---
```

**オプションフィールド**:
```yaml
author: "著者名"
summary: "3-5行の要約"
key_points:
  - "重要ポイント1"
  - "重要ポイント2"
  - "重要ポイント3"
related_topics: ["LLM", "Agents"]
confidence_level: "high"  # high, medium, low
```

**完全サンプル**:
```yaml
---
title: "生成AIスタートアップの資金調達トレンド2025"
date: "2025-01-15"
source: "週刊Life is beautiful 第123号"
author: "中島聡"
tags: ["AI", "Startup", "Funding", "Trends"]
summary: |
  2025年の生成AIスタートアップ資金調達は、エンタープライズ向けSaaSと
  エージェント領域に集中。平均調達額は前年比150%増加。
  ただし、プロダクトマーケットフィット前の調達は困難化。
key_points:
  - "エンタープライズSaaS領域が調達の60%を占める"
  - "平均Seed調達額: $5M（前年$2M）"
  - "PMF前の調達は2023年比で50%減少"
  - "日本市場では依然として資金調達環境が厳しい"
related_topics: ["Venture Capital", "PMF", "SaaS"]
confidence_level: "high"
---

# 生成AIスタートアップの資金調達トレンド2025

（本文がここに続く）
```

---

### 2. YAML単体ファイル用（大規模メタデータ）

**用途**: 複数記事・ドキュメントのメタデータを1ファイルにまとめる場合

**サンプル**: `timeline_data.yaml`（Ochyai_Note）
```yaml
metadata_version: "1.0"
total_articles: 1620
period: "2019-2025"
last_updated: "2025-12-30"

articles:
  - id: "ochyai_001"
    title: "デジタルネイチャーの未来像"
    date: "2019-03-15"
    url: "https://note.com/ochyai/n/xxx"
    author: "落合陽一"
    tags: ["Digital Nature", "Technology", "Future"]
    summary: "物質と情報の融合が進む2030年の社会像"
    themes: ["technology_future", "digital_nature"]
    word_count: 2500

  - id: "ochyai_002"
    title: "AIと芸術表現の新しい関係"
    date: "2019-04-20"
    url: "https://note.com/ochyai/n/yyy"
    author: "落合陽一"
    tags: ["AI", "Art", "Expression"]
    summary: "生成AIが芸術表現に与える影響と可能性"
    themes: ["art_media_expression", "technology_future"]
    word_count: 3200
```

---

### 3. JSON用（API・構造化データ）

**用途**: プログラムで読み込む構造化データ

**サンプル**: `archive_urls.json`
```json
{
  "version": "1.0",
  "total_count": 1620,
  "last_updated": "2025-12-30",
  "articles": [
    {
      "id": "ochyai_001",
      "title": "デジタルネイチャーの未来像",
      "date": "2019-03-15",
      "url": "https://note.com/ochyai/n/xxx",
      "author": "落合陽一",
      "tags": ["Digital Nature", "Technology", "Future"],
      "summary": "物質と情報の融合が進む2030年の社会像"
    }
  ]
}
```

---

## ファイルタイプ別適用指針

### A. LLM/配下（優先度: 最高）

**対象**: LLM向けに要約・構造化された二次資料

**適用範囲**: 全6ファイル

**サンプル適用**:
- `LLM/00_INDEX.md` → 読み順ガイドなので簡易メタデータのみ
- `LLM/01_LifeisBeautiful_insights.md` → 完全メタデータ適用

**適用手順**:
1. 既存ファイルを読み込む
2. 先頭にYAMLフロントマター挿入
3. title, date, source, tags, summary, key_points を記載

---

### B. LifeisBeautiful/配下（優先度: 高）

**対象**: 週刊Life is beautifulメルマガアーカイブ

**適用範囲**: 全51ファイル

**標準メタデータ**:
```yaml
---
title: "週刊Life is beautiful 第XX号"
date: "YYYY-MM-DD"
source: "Life is beautiful Newsletter"
author: "中島聡"
tags: ["AI", "Technology", "Investment", "Trends"]
summary: "（3-5行の要約）"
key_points:
  - "（重要ポイント1）"
  - "（重要ポイント2）"
newsletter_number: XX
---
```

---

### C. Ochyai_Note/配下（優先度: 中）

**対象**: 落合陽一note記事（1,620記事）

**適用方針**:
- **個別記事**: 手動適用は非現実的 → `timeline_data.yaml`に集約済み
- **分析レポート**: Analysis/配下の7レポート + timeline_analysis.md等に適用

**分析レポート適用サンプル**:
```yaml
---
title: "落合陽一ノート：テーマ別分析 - デジタルネイチャー"
date: "2025-12-30"
source: "Ochyai_Note全1,620記事分析"
author: "Claude Code Agent"
tags: ["Digital Nature", "Technology", "Analysis"]
summary: |
  落合陽一noteの全記事から「デジタルネイチャー」テーマを抽出し、
  時系列変化と主要論点を分析。2019-2025年の思想変遷を追跡。
key_points:
  - "デジタルネイチャーの概念定義が2019→2025で進化"
  - "物質性への着目が2021年以降顕著"
  - "教育・社会実装フェーズへ移行（2023-2025）"
related_topics: ["Technology Future", "Physicality", "Education"]
analysis_period: "2019-2025"
source_articles: 342
confidence_level: "high"
---
```

---

### D. sources/, speakers/, technologies/, topics/, use_cases/（優先度: 低）

**対象**: 分類軸フォルダ（将来拡張用）

**適用方針**: README.md を各フォルダに配置し、フォルダの目的を記載

**サンプル**: `technologies/README.md`
```yaml
---
title: "Technologies フォルダ - 技術別分類"
date: "2025-12-31"
description: "GenAI関連技術スタック別のドキュメント・事例"
tags: ["LlamaIndex", "LangChain", "Anthropic", "OpenAI"]
---

# Technologies フォルダ

## 概要
このフォルダは、生成AI/AIエージェント関連の技術スタック別にドキュメント・事例を分類します。

## サブフォルダ
- `llamaindex/`: LlamaIndex関連
- `langchain/`: LangChain関連
- `anthropic/`: Anthropic Claude関連
- `openai/`: OpenAI関連
```

---

## 適用優先順位マトリクス

| フォルダ | ファイル数 | 優先度 | 適用範囲 | 工数見積 |
|---------|----------|--------|---------|---------|
| **LLM/** | 6 | 最高 | 全ファイル | 0.5人日 |
| **LifeisBeautiful/** | 51 | 高 | 全ファイル | 1.5人日 |
| **Ochyai_Note/Analysis/Reports/** | 10 | 高 | レポートのみ | 0.5人日 |
| **sources/** | 4 | 中 | README追加 | 0.2人日 |
| **technologies/等** | 4 | 低 | README追加 | 0.3人日 |
| **Ochyai_Note/articles/** | 1,620 | 保留 | timeline_data.yaml参照 | - |

**総工数**: 3人日（優先度高のみ）

---

## YouTube トランスクリプト用メタデータ

**対象**: `sources/Founder_Agent_Videos/` 配下のトランスクリプトファイル

**標準フォーマット**:
```yaml
---
title: "動画タイトル（例: Founder Agent開発講座 第1回）"
video_url: "https://youtube.com/watch?v=XXXXX"
speaker: "話者名"
date: "2025-01-15"
duration: "01:25:30"
tags: ["Founder Agent", "Startup", "AI"]
summary: |
  Founder Agentの概要と、起業の科学フレームワークとの対応を解説。
  CPF/PSF診断の実装方法と、自律的な市場調査エージェントの設計を紹介。
key_points:
  - "Founder Agent = 起業の科学 × LLM"
  - "CPF診断の自動化手法"
  - "PSF達成までの12ステップ"
  - "自律エージェントの設計パターン"
related_framework: "起業の科学 - CPF/PSF"
transcript_type: "YouTube Auto-generated + Manual Edit"
language: "ja"
---

# 動画トランスクリプト

（以下、トランスクリプト本文）
```

---

## メタデータ検証チェックリスト

新規ファイル作成時、または既存ファイル更新時に以下をチェック：

### 必須項目チェック
- [ ] `title` フィールドが存在し、内容が明確
- [ ] `date` フィールドが YYYY-MM-DD 形式
- [ ] `source` フィールドが出典を明示
- [ ] `tags` が3-5個設定され、関連性が高い

### 推奨項目チェック
- [ ] `summary` が3-5行で要約されている
- [ ] `key_points` が3-10個リストアップ
- [ ] `confidence_level` が設定されている（high/medium/low）

### LLM最適化チェック
- [ ] タイトルが検索しやすい（キーワード含む）
- [ ] 要約が独立して理解可能（コンテキスト不要）
- [ ] タグが一般的な用語（過度な略語を避ける）

---

## 自動化スクリプト（将来実装）

大量ファイルへのメタデータ適用を効率化するため、以下のスクリプトを将来実装予定：

### 1. メタデータ抽出スクリプト
```python
# extract_metadata.py
# 既存ファイルからタイトル、日付、キーワードを自動抽出
```

### 2. メタデータ検証スクリプト
```python
# validate_metadata.py
# YAMLフロントマターの構文チェック、必須フィールド確認
```

### 3. 一括適用スクリプト
```python
# apply_metadata.py
# テンプレートを使用して複数ファイルに一括適用
```

---

## トラブルシューティング

### Q1: 既存の内容を壊さずにメタデータを追加したい
**A**: ファイル先頭に `---` で囲んだYAMLフロントマターを挿入。本文は変更不要。

### Q2: 大量ファイルへの適用が現実的でない
**A**: 優先度の高いフォルダ（LLM, LifeisBeautiful, Analysis/Reports）のみに適用。Ochyai_Note/articles/は`timeline_data.yaml`で代用。

### Q3: メタデータの信頼度（confidence_level）の判断基準は？
**A**:
- **high**: 公式資料、一次情報、検証済み
- **medium**: 二次情報、未検証だが信頼できる出典
- **low**: 推測、仮説、要検証

---

## まとめ

### 実施済み
- [x] 統一メタデータ標準の定義（index.yaml）
- [x] メタデータ適用ガイドの作成（本ドキュメント）
- [x] サンプルフォーマットの提供

### 次のステップ
- [ ] LLM/配下（6ファイル）へのメタデータ適用（0.5人日）
- [ ] LifeisBeautiful/配下（51ファイル）へのメタデータ適用（1.5人日）
- [ ] Ochyai_Note/Analysis/Reports/（10ファイル）へのメタデータ適用（0.5人日）
- [ ] YouTube トランスクリプトへのメタデータ適用（0.5人日）
- [ ] 自動化スクリプトの実装（将来）

---

**作成者**: Claude Code Agent
**最終更新**: 2025-12-31
**関連ドキュメント**: `index.yaml`, `README.md`
