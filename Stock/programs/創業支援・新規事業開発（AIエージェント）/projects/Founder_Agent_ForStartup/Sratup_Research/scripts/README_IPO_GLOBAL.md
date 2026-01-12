# IPO_Global Batch Generation System

Task toolベースの並列バッチ実行システム - 25社のIPO成功ケーススタディを自動生成

## 概要

このシステムは、Claude CodeのTask toolを使用して15-20並列で実行し、IPO_Globalカテゴリの起業家ケーススタディ25件を自動生成します。

### 主要機能
- **15-20並列実行**: Wave overlap戦略で常時15-20タスクを維持
- **完全自動化**: エラー時最大2回リトライ、人間介入不要
- **高品質保証**: CPF/PSF完全対応、12+ソース、100% fact-check pass
- **スレッドセーフ**: 原子的ファイル更新による進捗管理

### 進捗目標
- 現在: 400/500 (80%)
- 目標: 425/500 (85%)
- 05_IPO_Global: 21/50 → 46/50 (92%)

---

## アーキテクチャ

### システム構成
```
TaskToolOrchestrator (メインコントローラー)
  │
  ├─ PromptGenerator       - IPO_Global専用プロンプト生成
  ├─ TaskExecutor          - Task tool実行ラッパー
  ├─ ProgressTracker       - スレッドセーフ進捗管理
  ├─ RetryHandler          - リトライロジック
  └─ DocumentValidator     - 品質検証
```

### Wave Overlap戦略
```
Wave 1: [=====100%=====]
Wave 2:      [=====100%=====]
Wave 3:           [=====100%=====]
            ^60%  ^60%  ^60%
```
60%完了時点で次Waveを開始し、ピーク時15-20並列タスクを維持

---

## ファイル構成

### コアモジュール (7ファイル)
```
scripts/
├── task_tool_orchestrator.py      # メインコントローラー
├── prompt_generator.py             # プロンプトテンプレート
├── task_executor.py                # Task tool実行
├── progress_tracker.py             # 進捗管理 (fcntlロック)
├── retry_handler.py                # リトライロジック
├── validation.py                   # 品質検証
└── update_research_progress.py     # 自動更新
```

### 設定ファイル
```
scripts/
├── wave_definitions_ipo_global.json   # 25社5Wave設定
└── progress_ipo_global.json           # 進捗追跡 (自動生成)
```

---

## 対象企業 (25社)

### Wave 1: US Tech Giants
- FOUNDER_357: Snowflake (Frank Slootman)
- FOUNDER_358: Palantir (Peter Thiel & Alex Karp)
- FOUNDER_359: DoorDash (Tony Xu)
- FOUNDER_360: Airbnb (Brian Chesky)
- FOUNDER_361: Pinterest (Ben Silbermann)

### Wave 2: US Mobility & Enterprise
- FOUNDER_362: Uber (Travis Kalanick)
- FOUNDER_363: Lyft (Logan Green)
- FOUNDER_364: Snap (Evan Spiegel)
- FOUNDER_365: Shopify (Tobi Lütke)
- FOUNDER_375: CrowdStrike (George Kurtz)

### Wave 3: European Leaders
- FOUNDER_366: Spotify (Daniel Ek)
- FOUNDER_367: Adyen (Pieter van der Does)
- FOUNDER_368: Deliveroo (Will Shu)
- FOUNDER_369: Revolut (Nikolay Storonsky)
- FOUNDER_379: Wise (Kristo Käärmann)

### Wave 4: Asian Super Apps
- FOUNDER_370: Grab (Anthony Tan)
- FOUNDER_371: Sea Limited (Forrest Li)
- FOUNDER_372: Coupang (Bom Kim)
- FOUNDER_373: Kakao (Brian Kim)
- FOUNDER_374: Line (Takeshi Idezawa)

### Wave 5: Recent IPO Mix
- FOUNDER_376: Datadog (Olivier Pomel)
- FOUNDER_377: Coinbase (Brian Armstrong)
- FOUNDER_378: Rivian (RJ Scaringe)
- FOUNDER_380: Auto1 (Christian Bertermann)
- FOUNDER_381: Zomato (Deepinder Goyal)

---

## 使用方法

### 1. Dry Run（テスト実行）
```bash
cd scripts
python3 task_tool_orchestrator.py --dry-run
```
25ターゲットのリスト、Wave分割を確認

### 2. Wave 1テスト実行
```bash
python3 task_tool_orchestrator.py --wave ipo_wave1 --max-parallel 20
```
5文書生成テスト

### 3. 全Wave実行
```bash
python3 task_tool_orchestrator.py --max-parallel 20
```
全25文書を生成（推定2.5-3時間）

### 4. ステータス確認
```bash
python3 task_tool_orchestrator.py --status
```
現在の進捗を表示

### 5. 品質検証
```bash
python3 task_tool_orchestrator.py --validate
```
全文書の品質チェック

### 6. 進捗更新
```bash
python3 update_research_progress.py
```
research_progress.mdを自動更新

---

## 品質基準

### YAML要件
- ✓ `interview_count`: 最低10
- ✓ `problem_commonality`: 0-100スコア
- ✓ `wtp_confirmed`: boolean
- ✓ `urgency_score`: 1-10
- ✓ `ten_x_axes`: 最低2軸
- ✓ `mvp_type`: 指定値
- ✓ `uvp_clarity`: 1-10
- ✓ `fact_check`: "pass"
- ✓ `sources_count`: 最低12

### ドキュメント要件
- ✓ 12セクション (日本語)
- ✓ 最低18KB
- ✓ IPO情報セクション必須

### リサーチ要件
- ✓ S-1 filing必須
- ✓ 創業者インタビュー10+件
- ✓ 複数ソースで事実確認

---

## 進捗追跡

### progress_ipo_global.json構造
```json
{
  "batch_id": "ipo_global_batch_20251229",
  "total_targets": 25,
  "completed": [],
  "failed": [],
  "in_progress": [],
  "real_time_stats": {
    "tasks_running": 0,
    "avg_duration_seconds": 0,
    "fact_check_pass_rate": 0
  },
  "retry_queue": []
}
```

### スレッドセーフ更新
fcntlロックによる原子的ファイル更新:
1. Exclusive lock取得
2. Read → Update → Write
3. Atomic rename (.tmp → .json)
4. Lock解放

---

## エラーハンドリング

### リトライポリシー
- **最大リトライ**: 2回
- **リトライ対象**: timeout, fact_check失敗, sources不足, network error
- **タイムアウト延長**: 2x (900s → 1800s)

### エラー分類
- `timeout`: タイムアウトエラー
- `fact_check`: Fact check失敗
- `insufficient_sources`: ソース不足
- `network`: ネットワークエラー
- `other`: その他

---

## 想定タイムライン

| フェーズ | 所要時間 | 累計 |
|---------|----------|------|
| Dry Run | 5分 | 5分 |
| Wave 1テスト | 20分 | 25分 |
| 全Wave実行 | 80分 | 105分 |
| リトライ | 20分 | 125分 |
| 検証 | 10分 | 135分 |
| 進捗更新 | 5分 | **140分 (2時間20分)** |

**楽観的**: 2時間
**現実的**: 2.5-3時間
**悲観的**: 4時間

---

## トラブルシューティング

### PyYAMLインストールエラー
```bash
pip3 install pyyaml
```

### Task tool API不明
現在は既存のsubprocess (`claude code -p`) をフォールバックとして使用。
Task tool API確認後、`task_executor.py`の該当箇所を更新。

### リソース不足
```bash
# 並列数を減らす
python3 task_tool_orchestrator.py --max-parallel 15
```

### 進捗ファイル破損
```bash
# 進捗ファイルを削除して再初期化
rm scripts/progress_ipo_global.json
python3 task_tool_orchestrator.py --dry-run
```

---

## 成功基準

- ✓ 完了率: 25/25 (100%)
- ✓ Fact-check pass: 100%
- ✓ 平均ソース数: >= 12
- ✓ 平均interview_count: >= 10
- ✓ 実行時間: <= 3時間
- ✓ リトライ率: <= 20%

### 最終状態
- 総進捗: 425/500 (85%)
- 05_IPO_Global: 46/50 (92%)
- research_progress.md更新済み
- 全文書検証済み

---

## 拡張性

### 新しいWaveの追加
1. `wave_definitions_ipo_global.json`に追加
2. ターゲット数を調整
3. 実行: `python3 task_tool_orchestrator.py`

### 他カテゴリへの適用
1. 新しいwave定義JSON作成
2. `prompt_generator.py`でプロンプト調整
3. カテゴリ固有の検証ルール追加

---

## 開発履歴

- **2025-12-29**: 初版リリース
  - 7モジュール実装完了
  - Dry run成功
  - 25社5Wave設定完了

---

## 参照

- **計画書**: `/Users/yuichi/.claude/plans/snug-wishing-honey.md`
- **テンプレート**: `documents/05_IPO_Global/FOUNDER_352_eric_yuan_zoom.md`
- **進捗管理**: `research_progress.md`

---

## ライセンス

このシステムは Founder_Research プロジェクトの一部です。
