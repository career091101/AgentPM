# 田辺玩具 歯科医院リード収集プロジェクト - セットアップ完了

## セットアップ日時
2026-01-04 14:32

## プロジェクト構成

### ディレクトリ構造
```
tanabe_dental_leads/
├── README.md                    # プロジェクト概要・計画
├── PROJECT_STATUS.md            # 本ファイル
├── documents/                   # ドキュメント
│   ├── 1_initiating/
│   ├── 2_discovery/
│   ├── 3_planning/
│   └── 4_executing/
├── scripts/                     # Pythonスクリプト (38ファイル)
│   ├── collect_with_dedup.py              # Layer 1: 収集時重複排除
│   ├── merge_all_batches_with_dedup.py    # Layer 2: マージ時重複排除
│   ├── validate_data_quality.py           # Layer 3: データ品質検証
│   ├── test_collect_100.py                # Phase 0: テスト収集
│   └── ... (34 other scripts)
├── data/                        # データファイル (380ファイル)
│   ├── batch_XXX_leads_llm_*.csv         # 収集済みリード
│   ├── batch_XXX_基本情報.csv            # 基本情報
│   └── ... (377 other files)
└── evidence/                    # 証拠記録
```

### セットアップ済み項目

#### ✅ 完了
1. プロジェクト構造作成 (Stock/programs/副業/projects/tanabe_dental_leads/)
2. Pythonスクリプト配置 (38ファイル)
   - 3層重複排除システム
   - テスト収集スクリプト
   - バッチ処理スクリプト
3. データファイル配置 (380ファイル)
   - 収集済みバッチデータ
   - LLM分析済みリード
4. プロジェクトドキュメント作成 (README.md)

#### ⬜ 未実施 (Phase 1準備)
1. collection_history.json作成
   - 初回実行時に自動生成される
   - collect_with_dedup.py実行時に作成
2. Python仮想環境セットアップ
   - `python3 -m venv venv`
   - `source venv/bin/activate`
   - `pip install googlemaps`
3. Google Maps API Key設定
   - 環境変数 `GOOGLE_MAPS_API_KEY` の設定
4. Phase 1本番収集スクリプト作成
   - `collect_budget_optimized.py` (未作成)

## 次のステップ

### Phase 1: 本番収集準備

1. **環境セットアップ**
   ```bash
   cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/tanabe_dental_leads
   python3 -m venv venv
   source venv/bin/activate
   pip install googlemaps
   ```

2. **API Key設定**
   ```bash
   export GOOGLE_MAPS_API_KEY="AIzaSyASqcmLzyXnzrK6jcKzl7PVZ_3CmSv4rxc"
   ```

3. **Phase 1スクリプト作成**
   - `collect_budget_optimized.py` を作成
   - 目標: 既存1,615件 + 新規2,211件 = 3,826件
   - 予算: ¥25,500 (残予算¥4,500確保)
   - 検索範囲: 主要8都府県 × 2-3エリア × 3キーワード = 67パターン

4. **実行**
   ```bash
   python scripts/collect_budget_optimized.py
   python scripts/validate_data_quality.py data/dental_leads_budget_YYYYMMDD_HHMMSS.csv
   python scripts/merge_all_batches_with_dedup.py
   ```

### 参照
- 詳細計画: README.md
- 技術仕様: scripts/collect_with_dedup.py
- 品質基準: scripts/validate_data_quality.py

## プロジェクトステータス

| フェーズ | ステータス | 完了日 |
|---------|----------|--------|
| **Phase 0: テスト収集** | ✅ 完了 | 2026-01-04 |
| **プロジェクトセットアップ** | ✅ 完了 | 2026-01-04 |
| **Phase 1: 本番収集** | ⬜ 未着手 | - |
| **Phase B: スコアリング** | ⬜ 未着手 | - |
| **納品** | ⬜ 未着手 | - |

---

**最終更新**: 2026-01-04 14:35
**ステータス**: セットアップ完了、Phase 1準備完了
