# Task: GUGA 詳細分析ファイル生成

残り633件のGUGA生成AI活用事例について、12セクション形式の詳細分析ファイルを作成してください。

## データソース

**入力ファイル**: `Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/data_all.md`

**構造**: 18業界別に整理された1,252件の事例（Markdownテーブル形式）

**既存ファイル**: `Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/detailed_cases/`ディレクトリに619件の詳細分析済みファイルが存在

**対象**: 既存ファイルに対応しない残り633件

## 出力フォーマット

### ファイル名規則

`{seq:04d}_{company_slug}_{tool_slug}.md`

**例**:
- `0001_heroz_claude_opus.md`
- `0620_new_company_new_tool.md`

**Slug生成ルール**:
1. 小文字変換
2. スペース → アンダースコア
3. 特殊文字削除
4. 最大30文字（企業名）、20文字（ツール名）

### YAMLフロントマター

```yaml
---
id: "GUGA_{seq:04d}"
title: "[企業名] - [AI導入取り組み名]"
category: "[18業界分類]"
type: "case_study"
version: "1.0"
created_at: "{YYYY-MM-DD}"

company:
  name: "[企業名]"
  name_en: "[English Name]"
  industry: "[業界]"
  country: "日本"
  employees: [number or null]
  founded: [year or null]

ai_adoption:
  ai_tool: "[AIツール名]"
  ai_vendor: "[ベンダー名]"
  use_case_primary: "[主要用途]"
  use_case_secondary: "[副次用途]"
  rollout_start: "YYYY-MM or null"
  rollout_scope: "[対象範囲]"

quantitative_impact:
  # data_all.mdの「定量効果」列から抽出
  # または WebSearch で追加リサーチ
  [metric_name]: "[value or 取得不可]"

tags:
  use_case: ["業務プロセス改善", "既存事業の価値向上", etc.]
  tech_stack: ["Claude", "ChatGPT", "Gemini", etc.]
  success_pattern: ["全社導入", "段階的展開", etc.]

quality:
  source_tier: "tier1"
  sources_count: 1
  picker: "[GUGA協議員名 or 不明]"
  published_date: "{YYYY-MM-DD}"
---
```

### 12セクション構造

```markdown
## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 企業名 | [company.name] |
| 業界 | [company.industry] |
| 従業員数 | [company.employees or 不明] |
| 導入AI | [ai_adoption.ai_tool] |
| 主要用途 | [ai_adoption.use_case_primary] |
| 公表日 | [quality.published_date] |

## 2. AI導入サマリー

[3-5文で導入背景・目的・成果を要約]

## 3. 定量的効果

[quantitative_impact の詳細説明]
[WebSearchで追加データを取得した場合はソース明記]

取得不可の場合:
```
定量的データは公開されていませんが、[定性的な成果を記述]
```

## 4. 導入背景・課題

[推測ベースでも可、業界トレンドと照らし合わせて記述]

## 5. ソリューション詳細

[AI tool の具体的な活用方法]

## 6. 導入プロセス（時系列）

[rollout_start から推測、標準的な導入フローを記述]

## 7. 成功要因分析

[3-5項目の箇条書き]

## 8. 課題・対策

[予想される課題と対策を記述]

## 9. 今後の展開

[rollout_scope の拡大予測]

## 10. 他社への示唆

[この事例から学べるポイント 3-5項目]

## 11. ファクトチェック結果

| 検証項目 | 結果 | 備考 |
|---------|------|------|
| データソース | GUGA公式 | data_all.md |
| 定量効果 | [確認済 or 取得不可] | [備考] |
| 公表日 | {date} | data_all.md より |

## 12. 参考リンク

- GUGA公式: https://example.com (存在しない場合は「公式サイト不明」)
- [WebSearch で見つけた関連記事があれば追加]
```

## 実行ルール

### 1. 既存ファイルの重複回避

`Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/detailed_cases/`ディレクトリに既存の619ファイルが存在します。これらと重複しないよう、以下を確認してください：

```bash
# 既存ファイル一覧取得
ls Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/detailed_cases/*.md | head -20

# 最大シーケンス番号確認
ls Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/detailed_cases/*.md | grep -oE '[0-9]{4}' | sort -n | tail -1
```

**開始シーケンス番号**: 既存最大番号 + 1（おそらく0620から開始）

### 2. data_all.md からのデータ抽出

```markdown
## 1. テクノロジー・AI専業

| # | 企業名 | 公表日 | AIツール | 主要用途 | 定量効果 | 活用カテゴリ |
|---|--------|--------|----------|---------|---------|------------|
| 1 | HEROZ | 2025-12-02 | Claude Opus 4.5 | ... | ... | ... |
```

**抽出フロー**:
1. 業界セクション（## 1. ... ## 18.）を順次処理
2. 各テーブル行を解析
3. 既存ファイルと照合（企業名 + AIツールで判定）
4. 未処理の場合のみ新規ファイル生成

### 3. ROIリサーチの実行

**定量効果が不明な場合**:

```bash
WebSearch("{company_name} {ai_tool} 導入効果 定量 2025")
```

**判定基準**:
- 検索結果に具体的な数値（%、時間短縮、コスト削減）がある → YAMLとセクション3に記載
- 定性的な記述のみ → YAML: "取得不可"、セクション3: 定性的説明

**タイムアウト**: 各WebSearch は30秒でタイムアウト

### 4. 品質基準

**各ファイルの最低要件**:
- [ ] YAMLフロントマター完備（50-60行）
- [ ] 12セクションすべて存在
- [ ] 総行数 200行以上
- [ ] ファイル名規則準拠
- [ ] 重複ファイルなし

## 完了条件

以下の条件をすべて満たした時、タスク完了とみなす：

1. `Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/detailed_cases/`ディレクトリに 619 + 633 = **1,252ファイル** 存在
2. 新規生成された633ファイルが品質基準を満たす
3. 既存619ファイルと重複なし

## 完了時の出力

<promise>ALL CASES GENERATED: 633 files created, total 1,252 files</promise>

## エラーハンドリング

### ケース1: WebSearch タイムアウト

**対処**: quantitative_impact を "取得不可" として続行

### ケース2: data_all.md 解析エラー

**対処**: 該当業界セクションをスキップし、次の業界へ

### ケース3: ファイル名重複

**対処**: シーケンス番号に "_v2" サフィックス追加

## イテレーション管理

**推奨バッチサイズ**: 15ファイル/イテレーション

**計算**:
- 633ファイル ÷ 15 = 42.2イテレーション
- **max-iterations**: 45（余裕を持たせる）

**進捗確認**:
```bash
# 各イテレーション終了後
ls Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/detailed_cases/*.md | wc -l
# → 619 + (iteration * 15) の値を確認
```

## 参照ファイル

- **データソース**: `Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/data_all.md`
- **既存ファイル**: `Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/detailed_cases/0001_*.md` ~ `Stock/programs/生成AI活用事例DB/documents/2_research/guga_analysis/detailed_cases/0619_*.md`
- **テンプレート**: 既存ファイルのフォーマットを参考
