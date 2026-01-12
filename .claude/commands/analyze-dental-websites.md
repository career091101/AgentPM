# /analyze-dental-websites

歯科医院CSVファイルからWebサイトを**サブエージェント（Task tool）で複数ページ探索**し、SNS連携、ブログ日付、子ども向けコンテンツ、待合室写真、営業時間、**医院長名**をJSON出力します。医院長名の抽出率を**70-80%**に向上させます。

## 使い方

```bash
# 基本的な使用
/analyze-dental-websites <csv_file_path>

# バッチサイズと出力パス指定
/analyze-dental-websites <csv_file_path> --batch-size <数> --output <output_path>
```

## 例

```bash
# 10件テストCSVで分析
/analyze-dental-websites test_dental_leads_10_20260103_215311.csv

# 本番5,100件CSVで分析（バッチサイズ20）
/analyze-dental-websites dental_leads_phase_a_20260103_220000.csv --batch-size 20

# カスタム出力パス指定
/analyze-dental-websites dental_leads.csv --output custom_analysis.json
```

## 特徴（サブエージェント版）

- **医院長名抽出率70-80%**: 複数ページを探索して医院長名を高精度で抽出
- **並列探索**: 最大3ページまでサブエージェント（Task tool）で並列探索
- **高速処理**: model="haiku"で1医院あたり25-40秒
- **自動統合**: トップページ + サブエージェント結果を自動統合

## 実行時間目安

| 件数 | 実行時間 | 医院長名抽出率 |
|------|---------|--------------|
| 10件 | 3-5分 | 70-80% |
| 100件 | 20-30分 | 70-80% |
| 500件 | 90-120分 | 70-80% |
| 5,100件 | 15-20時間 | 70-80% |

## 詳細

詳細は @.claude/skills/analyze-dental-websites/SKILL.md を参照してください。
