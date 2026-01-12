# GenAI_Research フォルダ構造構築レポート

**作成日時**: 2025-12-30
**タスク**: T005-3
**対象**: GenAI_Research統合プロジェクト

---

## 📁 構築完了フォルダ構造

### ベースパス
```
/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/
```

### 完全なディレクトリツリー

```
GenAI_research/
├── README.md                          # 全体ガイド（既存）
│
├── LLM/                               # 既存フォルダ（維持）
│
├── LifeisBeautiful/                   # 既存（53ファイル）※移動せず維持
│
├── Ochyai_Note/                       # 既存（16サブフォルダ）※移動せず維持
│   ├── articles/
│   ├── cookies/
│   ├── full_run/
│   ├── images/
│   ├── logs/
│   ├── metadata/
│   ├── scripts/
│   └── test_run/
│
├── sources/ ★NEW                      # ソース別管理
│   ├── README.md
│   └── Founder_Agent_Videos/ ★NEW    # 469個のトランスクリプト配置予定
│
├── topics/ ★NEW                       # トピック別インデックス
│   ├── README.md
│   ├── agents/ ★NEW                  # 420ファイル想定（89.6%）
│   ├── llm/ ★NEW                     # 356ファイル想定（75.9%）
│   ├── rag/ ★NEW                     # 264ファイル想定（56.3%）
│   ├── prompt_engineering/ ★NEW      # 306ファイル想定（65.2%）
│   └── fine_tuning/ ★NEW             # 56ファイル想定（11.9%）
│
├── technologies/ ★NEW                 # 技術スタック別インデックス
│   ├── README.md
│   ├── langchain/ ★NEW
│   ├── llamaindex/ ★NEW
│   ├── openai/ ★NEW
│   ├── anthropic/ ★NEW
│   └── chatgpt/ ★NEW
│
├── use_cases/ ★NEW                    # ユースケース別インデックス
│   ├── README.md
│   ├── startup_support/ ★NEW
│   ├── automation/ ★NEW
│   └── customer_support/ ★NEW
│
└── speakers/ ★NEW                     # 話者別インデックス（動的生成）
    └── README.md
```

---

## 🎯 設計判断

### 1. 既存フォルダの扱い
**判断**: LifeisBeautiful/、Ochyai_Note/、LLM/ は**移動せず現在位置に維持**

**理由**:
- 既存のスクリプト・パス参照が多数存在
- 移動によるリンク切れリスクを回避
- sources/ は新規追加コンテンツ用のサブフォルダとして位置づけ

### 2. トピックフォルダの優先順位
**T005-2の分析結果に基づく優先構築**:

| トピック | 出現率 | 優先度 |
|----------|--------|--------|
| agents/ | 89.6% | 最優先 |
| llm/ | 75.9% | 高 |
| prompt_engineering/ | 65.2% | 高 |
| rag/ | 56.3% | 中 |
| fine_tuning/ | 11.9% | 低 |

### 3. シンボリックリンク戦略
- **実ファイル**: `sources/Founder_Agent_Videos/` に集約
- **カテゴリ参照**: `topics/`, `technologies/`, `use_cases/`, `speakers/` にはシンボリックリンクを配置
- **メリット**: ストレージ効率化、一元管理、柔軟な分類変更

---

## 📝 各カテゴリの詳細

### sources/ - ソース別管理
**目的**: トランスクリプトの実ファイルを格納し、ソース別に整理

**サブフォルダ**:
- `Founder_Agent_Videos/` - 469個のYouTube動画トランスクリプト（YAML frontmatter付き）

**ファイル形式**:
```yaml
---
video_url: "https://www.youtube.com/watch?v=XXXXX"
video_id: "XXXXX"
title: "[動画タイトル]"
speaker: "[話者名]"
topic_tags:
  - "#GenAI"
  - "#Startup"
summary: |
  [要約]
key_points:
  - "[キーポイント1]"
technologies_mentioned:
  - "OpenAI GPT-4"
use_cases:
  - "スタートアップ支援"
source: "Founder_Agent_Videos"
---
```

---

### topics/ - トピック別インデックス
**目的**: AI/GenAI技術のトピック別にトランスクリプトを分類

**サブフォルダ**:
1. **agents/** - AIエージェント関連（420ファイル想定）
   - マルチエージェントシステム、自律型AI

2. **llm/** - 大規模言語モデル（356ファイル想定）
   - GPT-4、Claude、LLM基礎

3. **rag/** - Retrieval-Augmented Generation（264ファイル想定）
   - ベクトルDB、Embedding、検索拡張

4. **prompt_engineering/** - プロンプトエンジニアリング（306ファイル想定）
   - Few-shot、Chain-of-Thought、プロンプト最適化

5. **fine_tuning/** - モデルファインチューニング（56ファイル想定）
   - PEFT、LoRA、ドメイン特化モデル

---

### technologies/ - 技術スタック別インデックス
**目的**: 具体的な技術・フレームワーク・プロダクト別に分類

**サブフォルダ**:
1. **langchain/** - LangChainフレームワーク
2. **llamaindex/** - LlamaIndexによるRAG実装
3. **openai/** - OpenAI API、GPT-4
4. **anthropic/** - Anthropic Claude API
5. **chatgpt/** - ChatGPT活用事例

---

### use_cases/ - ユースケース別インデックス
**目的**: AI/GenAIの活用シーン別に分類

**サブフォルダ**:
1. **startup_support/** - スタートアップ支援
   - アイデア検証、プロダクト開発、ピッチ資料

2. **automation/** - 業務自動化
   - タスク自動化、ワークフロー最適化

3. **customer_support/** - カスタマーサポート
   - チャットボット、FAQ自動応答

---

### speakers/ - 話者別インデックス
**目的**: 話者別にトランスクリプトを検索可能にする

**特徴**:
- サブフォルダは動的生成（T005-5で自動作成）
- 話者名はLLMによるトランスクリプト分析で抽出
- メタデータのspeakerフィールドに基づく分類

---

## ✅ 完了確認

### フォルダ作成
- [x] sources/Founder_Agent_Videos/ 作成
- [x] topics/ + 5サブフォルダ作成
- [x] technologies/ + 5サブフォルダ作成
- [x] use_cases/ + 3サブフォルダ作成
- [x] speakers/ 作成

### ドキュメント作成
- [x] sources/README.md 作成
- [x] topics/README.md 作成
- [x] technologies/README.md 作成
- [x] use_cases/README.md 作成
- [x] speakers/README.md 作成

### 既存フォルダ保護
- [x] LifeisBeautiful/ - 移動なし（53ファイル維持）
- [x] Ochyai_Note/ - 移動なし（16サブフォルダ維持）
- [x] LLM/ - 移動なし（既存構造維持）

---

## 📊 統計情報

| 項目 | 値 |
|------|-----|
| **新規作成フォルダ数** | 17個 |
| **新規作成README数** | 5個 |
| **既存フォルダ保護数** | 3個 |
| **想定トランスクリプト数** | 469個（sources/Founder_Agent_Videos/） |
| **既存コンテンツ数** | 53+16=69ファイル/フォルダ（LifeisBeautiful + Ochyai_Note） |

---

## 🔄 次のステップ

### T005-4 Phase1: パイロット50動画にメタデータ付与
1. トランスクリプトファイルを`sources/Founder_Agent_Videos/`に配置
2. WebSearch + LLM解析でメタデータ抽出
3. YAML frontmatterを付与
4. 品質検証（サンプリング10動画）

### T005-4 Phase2: 残り419動画にメタデータ付与
1. パイロット結果を踏まえて全動画処理
2. エラーハンドリング・レジューム機能
3. 進捗管理（metadata_progress.json）

### T005-5: カテゴリ分類
1. メタデータに基づいてシンボリックリンク作成
2. topics/, technologies/, use_cases/, speakers/ に配置
3. 各カテゴリのREADMEに動画一覧を追記

### T005-6: 統合インデックス作成
1. index.yaml生成
2. 全トランスクリプトのメタデータ統合
3. カテゴリ別統計情報

---

**作成者**: Claude Code
**生成日時**: 2025-12-30
**T005-3タスク完了**
