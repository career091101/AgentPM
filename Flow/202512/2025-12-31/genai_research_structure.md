# T005-3: GenAI_Research フォルダ構造作成レポート

**作成日**: 2025-12-31
**作成者**: Claude Sonnet 4.5
**タスク**: YouTubeトランスクリプト→GenAI_Research統合 Phase 1

---

## エグゼクティブサマリー

GenAI_Researchプロジェクトのフォルダ構造を確認・拡張し、469個のYouTubeトランスクリプト統合の準備を完了しました。既存のLifeisBeautiful/、Ochyai_Note/フォルダを維持しつつ、新規に`sources/Founder_Agent_Videos/`および7つのトピック、7つの技術スタック、6つのユースケースフォルダを整備しました。

---

## プロジェクト位置

**絶対パス**:
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research
```

**注意**: 当初の計画では`/projects/GenAI_research/`と想定していましたが、実際は`Founder_Agent_ForGenAI`プロジェクト配下に存在します。

---

## 最終フォルダ構造

```
GenAI_research/
├── README.md                          # プロジェクト概要
├── LLM/                               # LLM向け要約・構造化資料
│   └── 00_INDEX.md
├── LifeisBeautiful/                   # 既存（53ファイル、週刊Life is beautiful）
├── Ochyai_Note/                       # 既存（17ファイル、落合陽一 note）
│   ├── articles/
│   ├── images/
│   ├── metadata/
│   ├── scripts/
│   └── logs/
├── sources/                           # ソース別管理（NEW）
│   └── Founder_Agent_Videos/         # 469個のトランスクリプト（処理中）
│       ├── *.md（3ファイル、469予定）
│       └── README.md（未作成）
├── topics/                            # トピック別インデックス
│   ├── README.md
│   ├── agents/                        # 420動画予定
│   ├── llm/                           # 373動画予定
│   ├── prompt_engineering/            # 309動画予定
│   ├── rag/                           # 253動画予定
│   ├── genai/                         # 113動画予定（NEW）
│   ├── startup/                       # 112動画予定（NEW）
│   └── fine_tuning/                   # 61動画予定
├── technologies/                      # 技術別インデックス
│   ├── README.md
│   ├── google/                        # 294動画予定（NEW）
│   ├── openai/                        # 191動画予定
│   ├── anthropic/                     # 189動画予定
│   ├── hugging_face/                  # 27動画予定（NEW）
│   ├── langchain/                     # 25動画予定
│   ├── llamaindex/
│   └── chatgpt/
├── use_cases/                         # ユースケース別インデックス
│   ├── README.md
│   ├── startup_support/               # スタートアップ支援
│   ├── customer_support/              # カスタマーサポート自動化
│   ├── automation/                    # 業務自動化
│   ├── code_generation/               # コード生成（NEW）
│   ├── content_creation/              # コンテンツ作成（NEW）
│   └── data_analysis/                 # データ分析（NEW）
├── speakers/                          # 話者別インデックス（動的生成予定）
└── index.yaml                         # 統合インデックス（未作成）
```

---

## 実施内容

### 1. 既存構造の確認

**既存フォルダ**:
- ✅ `LifeisBeautiful/` - 53ファイル（週刊Life is beautiful）
- ✅ `Ochyai_Note/` - 17ファイル（落合陽一 note）
- ✅ `LLM/` - LLM向け要約資料
- ✅ `sources/Founder_Agent_Videos/` - 3ファイル（469予定）
- ✅ `topics/` - 5カテゴリ（agents, llm, prompt_engineering, rag, fine_tuning）
- ✅ `technologies/` - 5カテゴリ（openai, anthropic, langchain, llamaindex, chatgpt）
- ✅ `use_cases/` - 3カテゴリ（startup_support, customer_support, automation）
- ✅ `speakers/` - 空（動的生成予定）

### 2. 不足フォルダの作成（NEW）

**Topics（2フォルダ追加）**:
```bash
mkdir -p topics/genai
mkdir -p topics/startup
```

**Technologies（2フォルダ追加）**:
```bash
mkdir -p technologies/google
mkdir -p technologies/hugging_face
```

**Use Cases（3フォルダ追加）**:
```bash
mkdir -p use_cases/code_generation
mkdir -p use_cases/content_creation
mkdir -p use_cases/data_analysis
```

---

## カテゴリ別予測ファイル数

### Topics（7カテゴリ）

| カテゴリ | 予測動画数 | カバレッジ | 説明 |
|---------|----------|-----------|------|
| agents | 420 | 89.6% | AIエージェント、マルチエージェント |
| llm | 373 | 79.5% | 大規模言語モデル |
| prompt_engineering | 309 | 65.9% | プロンプト設計 |
| rag | 253 | 53.9% | 検索拡張生成 |
| genai | 113 | 24.1% | 生成AI全般 |
| startup | 112 | 23.9% | スタートアップ、起業 |
| fine_tuning | 61 | 13.0% | ファインチューニング |

### Technologies（7カテゴリ）

| カテゴリ | 予測動画数 | カバレッジ | 説明 |
|---------|----------|-----------|------|
| google | 294 | 62.7% | Gemini、PaLM |
| openai | 191 | 40.7% | GPT-4、ChatGPT |
| anthropic | 189 | 40.3% | Claude |
| hugging_face | 27 | 5.8% | Transformers |
| langchain | 25 | 5.3% | LLMフレームワーク |
| llamaindex | 0 | 0% | （未検出） |
| chatgpt | （重複） | - | OpenAIに統合予定 |

### Use Cases（6カテゴリ）

| カテゴリ | 説明 | LLM抽出予定 |
|---------|------|-------------|
| startup_support | スタートアップ支援 | ✅ |
| customer_support | カスタマーサポート自動化 | ✅ |
| automation | 業務自動化 | ✅ |
| code_generation | コード生成 | ✅ |
| content_creation | コンテンツ作成 | ✅ |
| data_analysis | データ分析 | ✅ |

**注**: Use Casesの詳細分類はT005-4 Phase1（LLM解析）で動的に決定されます。

---

## 既存ファイルの統計

### LifeisBeautiful/

```bash
$ find LifeisBeautiful/ -type f | wc -l
53
```

**内容**: 週刊Life is beautiful（AIトレンド、投資・産業観点）

### Ochyai_Note/

```bash
$ find Ochyai_Note/ -type f | wc -l
17（記事数）
```

**内容**: 落合陽一のnote記事（Markdown + JSON + 画像）

### sources/Founder_Agent_Videos/

```bash
$ find sources/Founder_Agent_Videos/ -type f -name "*.md" | wc -l
3（現在）→ 469（目標）
```

**ステータス**: T005-4（メタデータ処理）で469ファイルを追加予定

---

## README.md の現在の内容

```markdown
# GenAI_research

このフォルダは、生成AI/AIエージェント領域の調査ログ（一次資料のストック）と、そこから抽出した洞察（LLM向けに要約・構造化した二次資料）をまとめます。

## まず読む（LLM向け）
- `LLM/00_INDEX.md`（読み順・要点・入力に適したファイル一覧）

## 収録ソース（一次資料）
- `LifeisBeautiful/`：週刊 *Life is beautiful*（主にAIトレンド/投資・産業観点を含む）
- `Ochyai_Note/`：落合陽一 note 記事アーカイブ（MD + JSON + 画像）

## 運用ルール（最小）
- 一次資料は原則そのまま保持し、加工物は `LLM/` 配下に追加する。
- 参照元の出典は「ファイルパス」を必ず残す（再検証できるようにする）。
```

**更新予定**: T005-4完了後に`sources/Founder_Agent_Videos/`の説明を追加

---

## シンボリックリンク戦略（T005-5で実装予定）

### 設計方針

1. **実ファイル配置**: `sources/Founder_Agent_Videos/*.md`
2. **カテゴリ参照**: `topics/`, `technologies/`, `use_cases/`にはシンボリックリンクを配置
3. **重複回避**: 同一ファイルを複数カテゴリから参照可能

### 実装例

```bash
# 実ファイル
sources/Founder_Agent_Videos/yw3QQxX9FZQ.md

# シンボリックリンク
topics/agents/yw3QQxX9FZQ.md -> ../../sources/Founder_Agent_Videos/yw3QQxX9FZQ.md
topics/llm/yw3QQxX9FZQ.md -> ../../sources/Founder_Agent_Videos/yw3QQxX9FZQ.md
technologies/google/yw3QQxX9FZQ.md -> ../../sources/Founder_Agent_Videos/yw3QQxX9FZQ.md
```

---

## 次のステップ（T005-4）

T005-4では、469個のトランスクリプトに以下のメタデータを付与します：

### Phase 1: パイロット50動画（1.5時間）

1. **WebSearch**: YouTube動画のタイトル・チャンネル名を取得
2. **LLM解析**: トランスクリプトから話者、要約、キーポイント、ユースケースを抽出
3. **YAML frontmatter付与**:
   ```yaml
   ---
   video_url: "https://www.youtube.com/watch?v=XXXXX"
   title: "[動画タイトル]"
   speaker: "[話者名]"
   topic_tags: ["#GenAI", "#Startup"]
   summary: "[200字要約]"
   key_points: ["[ポイント1]", "[ポイント2]"]
   technologies_mentioned: ["OpenAI GPT-4", "LangChain"]
   use_cases: ["スタートアップ支援"]
   ---
   ```
4. **sources/Founder_Agent_Videos/にコピー**

### Phase 2: 残り419動画（3時間）

- パイロット結果を踏まえて全動画を自動処理
- チェックポイント保存（metadata_progress.json）
- エラーハンドリング（部分メタデータ保存）

---

## 技術的考慮事項

### ディスク容量

- **既存コンテンツ**: 約20-30MB（LifeisBeautiful + Ochyai_Note）
- **新規トランスクリプト**: 17MB（469ファイル）
- **シンボリックリンク**: 約1-2MB（メタデータのみ）
- **合計**: 約40-50MB（軽量）

### パス管理

- **全角括弧の遵守**: `創業支援・新規事業開発（AIエージェント）`
- **相対パス使用**: シンボリックリンクは相対パスで作成
- **pathlib推奨**: Pythonスクリプトでは`pathlib.Path`を使用

---

## 成功基準

- ✅ 既存フォルダ構造確認完了（LifeisBeautiful、Ochyai_Note維持）
- ✅ sources/Founder_Agent_Videos/ディレクトリ存在確認
- ✅ 7トピックフォルダ作成完了（genai, startup追加）
- ✅ 7技術スタックフォルダ作成完了（google, hugging_face追加）
- ✅ 6ユースケースフォルダ作成完了（code_generation, content_creation, data_analysis追加）
- ✅ 次ステップ（T005-4）の準備完了

---

## 変更履歴

| 日付 | 作業者 | 変更内容 |
|------|--------|---------|
| 2025-12-30 | （前回） | 基本フォルダ構造作成（topics, technologies, use_cases, sources, speakers） |
| 2025-12-31 | Claude Sonnet 4.5 | 不足フォルダ追加（topics/genai, topics/startup, technologies/google, technologies/hugging_face, use_cases/code_generation, use_cases/content_creation, use_cases/data_analysis） |

---

**作成日**: 2025-12-31
**ステータス**: ✅ 完了
**次のタスク**: T005-4 Phase1 - パイロット50動画メタデータ処理
