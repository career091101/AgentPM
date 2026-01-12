# Founder_Research

世界的起業家500人の調査プロジェクト

## 目的

FounderAgentの`orchestrate-phase1`スキルの裏付けとなる実証データを収集する。

1. **判定基準の検証**: CPF60%、10倍2軸等の閾値が実際に有効か検証
2. **事例DBの構築**: スキル実行時にAIが参照できるナレッジベース
3. **説得材料の整備**: ユーザー向けエビデンス
4. **成功＋失敗事例**: スキル精度向上のための両面調査

## 調査対象（500人）

| ティア | 対象 | 目標件数 |
|--------|------|---------|
| 01_Legendary | 世界的レジェンド起業家 | 50人 |
| 02_Unicorn | 評価額$1B+創業者 | 100人 |
| 03_VC_Backed | シリーズA-C調達済み | 150人 |
| 04_IPO_Japan | 日本上場企業創業者 | 50人 |
| 05_IPO_Global | 海外上場企業創業者 | 50人 |
| 06_Pivot_Success | ピボット成功事例 | 30人 |
| 07_Failure_Study | 失敗事例研究 | 30人 |
| 08_Emerging | 新興起業家（2020年以降創業） | 40人 |

## ディレクトリ構造

```
Founder_Research/
├── README.md（本ファイル）
├── research_progress.md（進捗管理）
├── _index/
│   └── master_index.md（全ドキュメント索引）
├── _templates/
│   ├── founder_case_study_template.md
│   ├── pivot_study_template.md
│   └── failure_study_template.md
├── documents/
│   ├── 01_Legendary/
│   ├── 02_Unicorn/
│   ├── 03_VC_Backed/
│   ├── 04_IPO_Japan/
│   ├── 05_IPO_Global/
│   ├── 06_Pivot_Success/
│   ├── 07_Failure_Study/
│   └── 08_Emerging/
├── analysis/
│   ├── cpf_patterns/
│   ├── psf_patterns/
│   ├── pivot_patterns/
│   └── cross_analysis/
└── _cross_reference/
    └── person_registry.md
```

## orchestrate-phase1対応

各ケーススタディは以下の情報を収集:

- **需要発見**: 創業のきっかけ、課題発見方法
- **CPF検証**: インタビュー実施、課題検証プロセス
- **PSF検証**: 10倍優位性、MVP、競合差別化
- **ピボット/失敗**: 転換点、失敗からの学び

## 関連プロジェクト

- `Solopreneur_Research/`: ソロプレナー成功事例研究（517件）
- `startup_science/`: 起業の科学フレームワーク

## 作成日

2025-12-28
