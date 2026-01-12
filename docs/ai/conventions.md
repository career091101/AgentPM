# コーディング規約・設計方針

## 基本原則

1. **ルールは正確に実行** - 独自解釈で変更しない
2. **パス構造を尊重** - Flow/年月/日付の階層を必ず守る
3. **失敗時は報告** - 代替手段を取らず、ユーザーに確認

## ファイル命名規則

### ドラフトファイル
```
draft_[document_type].md
```
例: `draft_project_charter.md`, `draft_persona.md`

### 確定版ファイル
```
[document_type].md
```
例: `project_charter.md`, `persona.md`

## ディレクトリ構造

### Flow（作業中）
```
Flow/
└── YYYYMM/
    └── YYYY-MM-DD/
        ├── draft_*.md
        └── backlog/
```

### Stock（確定版）
```
Stock/
└── programs/
    └── [program_id]/
        └── projects/
            └── [project_id]/
                └── documents/
                    ├── 1_initiating/
                    ├── 2_discovery/
                    ├── 2_research/
                    ├── 3_planning/
                    ├── 4_executing/
                    ├── 5_monitoring/
                    └── 6_closing/
```

## パス参照

すべてのパスは `pmbok_paths.mdc` の変数を使用：

- `{{dirs.flow}}` - Flowルート
- `{{dirs.stock}}` - Stockルート
- `{{patterns.flow_date}}` - 今日の日付フォルダ
- `{{patterns.project_dir}}` - プロジェクトディレクトリ

## Markdown形式

- 見出しレベルは適切に使用（H1はタイトルのみ）
- コードブロックには言語指定
- テーブルは整形済みで出力
