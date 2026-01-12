# 生成AI活用事例DB プロジェクト

**バージョン**: v3.0
**最終更新**: 2026-01-10
**プロジェクトフェーズ**: Discovery → Planning移行中

## プロジェクト概要

生成AI活用事例データベースの構築プロジェクト。国内外の企業導入事例を体系的に収集・分析し、意思決定支援ツールとして提供する。

**データソース**:
- GUGA生成AI活用事例DB（1,252件）
- OpenAI/Google/Anthropic公式Customer Stories
- その他40+のソースデータベース

**主要成果物**:
- 846社の詳細事例レポート（2026-01-10時点）
- 業界別・用途別分類
- 定量的効果分析（27パターン）

---

## ディレクトリ構造

```
├── README.md（本ファイル）
├── documents/
│   ├── 1_initiating/      ← プロジェクト憲章
│   ├── 2_research/        ← 市場調査、事例分析（860+ファイル）
│   ├── 3_discovery/       ← 需要検証、CPF/PSF/PMF検証
│   └── 4_planning/        ← ビジネス戦略、ロードマップ
└── scripts/               ← データ生成スクリプト
```

---

## フェーズ別ドキュメント

### 1_initiating（立ち上げ）
- `project_charter.md` - プロジェクト憲章（v2確定版）

### 2_research（調査）
- `source_database_list.md` - 40+ソースデータベース一覧
- `cases_japan_guga.md` - 日本企業事例（GUGA DBより）
- `cases_vendor_*.md` - ベンダー別事例（OpenAI, Google等）
- `cases_database_1000.md` - 1,000+事例統合DB
- `market_statistics_2025.md` - 市場統計（採用率78%）
- `research_summary.md` - 統合サマリー
- `project_validation.md` - プロジェクト妥当性検証
- `competitor_analysis.md` - 競合分析（5軸評価）
- `phase0_validation_result.md` - Phase 0検証結果
- `guga_analysis/` - GUGA事例DB詳細分析
  - `overview.md` - 全体概要
  - `quantitative_impacts.md` - 定量的効果（27パターン）
  - `data_all.md` - 全データ統合
  - `by_industry/` - 業界別分類
  - `by_category/` - 用途別分類
  - **`detailed_cases/` - 846社の詳細事例**

### 3_discovery（発見）
- `1a_demand_discovery.md` - 需要発見（市場機会スコア7/10）
- `1b_cpf_validation.md` - 顧客問題適合検証
- `1c_psf_validation.md` - ソリューション適合検証
- `1d_pmf_validation.md` - プロダクト市場適合検証
- `1e_launch_preparation.md` - 事業立ち上げ準備
- `orchestration_report.md` - Phase 1統合管理

### 4_planning（計画）
- `bip_strategy.md` - プロダクト戦略（ICEスコア）

---

## データ統計

| カテゴリ | 件数 |
|---------|------|
| 総事例数 | 1,252件（GUGA DB） |
| 詳細分析済み | 846社（2026-01-10時点） |
| 業界分類 | 18業界 |
| 定量効果パターン | 27種類 |
| ソースデータベース | 40+ |

---

## 次のフェーズ

**Phase 2: Executing（実装）**
- データベースシステム開発
- API設計
- フロントエンド実装

**Phase 3: Monitoring（監視）**
- KPI追跡
- ユーザーフィードバック収集

---

## メンテナンス履歴

- **v3.0** (2026-01-10): Flow→Stock確定反映、846詳細事例追加、PMBOK命名規則統一（1_initiating, 2_research, 3_discovery, 4_planning）
- **v2.0** (2026-01-07): Phase 1完了、Discovery/Planning段階移行
- **v1.0** (2026-01-07): プロジェクト立ち上げ、Initiating完了
