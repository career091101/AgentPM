# YouTube Transcripts Knowledge Base

**データソース**: Founder Agent Phase1プロジェクト
**総トランスクリプト数**: 469件
**最終更新**: 2025-12-30

---

## 📊 カテゴリ別分類

| カテゴリ | 件数 | 割合 | 索引ファイル |
|----------|------|------|--------------|
| **CPF関連** | 408件 | 87.0% | [cpf/index.yaml](cpf/index.yaml) |
| **PSF関連** | 14件 | 3.0% | [psf/index.yaml](psf/index.yaml) |
| **PMF関連** | 6件 | 1.3% | [pmf/index.yaml](pmf/index.yaml) |
| **マーケティング** | 9件 | 1.9% | [marketing/index.yaml](marketing/index.yaml) |
| **起業全般** | 1件 | 0.2% | [general/index.yaml](general/index.yaml) |
| **未分類** | 31件 | 6.6% | [unclassified/index.yaml](unclassified/index.yaml) |

---

## 🎯 活用方法

### 1. スキル実行時の参照

各スキルから関連トランスクリプトを参照：

```yaml
# 例: /validate-cpf 実行時
参照: @startup_science/02_frameworks/transcripts/cpf/
目的: CPF達成事例から成功パターンを学習
```

### 2. Knowledge Base統合

```markdown
<!-- スキルのSKILL.mdに追加 -->
## Knowledge Base参照

- CPF概念: `@startup_science/01_stages/cpf/cpf_overview.md`
- CPF事例集: `@startup_science/02_frameworks/transcripts/cpf/`  ← 追加
```

### 3. RAG（検索拡張生成）での利用

**将来実装**: ベクトル検索でセマンティック検索

```python
# 例: CPF関連の顧客インタビュー手法を検索
query = "顧客インタビューで避けるべき質問"
results = search_transcripts(query, category='cpf')
```

---

## 📁 フォルダ構造

```
transcripts/
├── README.md              ← 本ファイル
├── index.yaml             ← 総合索引
├── cpf/                   ← CPF関連（408件）
│   └── index.yaml
├── psf/                   ← PSF関連（14件）
│   └── index.yaml
├── pmf/                   ← PMF関連（6件）
│   └── index.yaml
├── marketing/             ← マーケティング（9件）
│   └── index.yaml
├── general/               ← 起業全般（1件）
│   └── index.yaml
└── unclassified/          ← 未分類（31件）
    └── index.yaml
```

---

## 🔍 索引ファイルの使い方

### YAML形式

```yaml
category: cpf
count: 408
files:
  - filename: gaGaPpnexxA.md
    video_id: gaGaPpnexxA
    path: aipm_v0/Stock/programs/.../transcripts/items/gaGaPpnexxA.md
    size: 12345
  - ...
```

### Python での読み込み

```python
import yaml
from pathlib import Path

# CPF関連のトランスクリプト一覧を取得
with open('cpf/index.yaml', 'r') as f:
    cpf_index = yaml.safe_load(f)

print(f"CPF関連: {cpf_index['count']}件")

for file_info in cpf_index['files']:
    print(f"  - {file_info['filename']}")
```

---

## 🎓 カテゴリ別の特徴

### CPF関連（408件、87.0%）

**主なトピック**:
- 顧客インタビュー手法
- ペルソナ作成
- 課題発見・検証
- ニーズの深堀り

**推奨参照スキル**:
- `/research-problem`
- `/simulate-interview`
- `/validate-cpf`
- `/create-persona`

---

### PSF関連（14件、3.0%）

**主なトピック**:
- MVP開発
- ソリューション設計
- 10倍優位性
- UVP定義

**推奨参照スキル**:
- `/validate-10x`
- `/build-lp`
- `/validate-psf`

---

### PMF関連（6件、1.3%）

**主なトピック**:
- グロースハック
- スケーリング
- メトリクス測定
- リテンション改善

**推奨参照スキル**:
- `/validate-pmf`（Phase2で実装予定）
- `/validate-unit-economics`（Phase2で実装予定）

---

### マーケティング（9件、1.9%）

**主なトピック**:
- SNS戦略
- コンテンツマーケティング
- 集客施策
- 広告運用

**推奨参照スキル**:
- `/create-sns-content`
- `/build-lp`

---

## 🔄 更新履歴

| 日付 | 内容 |
|------|------|
| 2025-12-30 | 初回作成（469件を6カテゴリに分類） |

---

## 📝 メンテナンス

### 新規トランスクリプト追加時

1. 元ファイルを `projects/Founder_Agent_Phase1/documents/references/transcripts/items/` に配置
2. 以下のスクリプトを実行して索引を更新

```bash
python3 scripts/update_transcript_index.py
```

### カテゴリの再分類

分類キーワードを変更する場合は、分類スクリプトを編集：

```python
topics_keywords = {
    'cpf': ['顧客', 'ペルソナ', 'インタビュー', ...],
    'psf': ['ソリューション', 'MVP', ...],
    # ...
}
```

---

## 🔗 関連リソース

- **元データ**: `projects/Founder_Agent_Phase1/documents/references/transcripts/items/`（469件）
- **ステータスレポート**: `projects/Founder_Agent_Phase1/documents/references/transcripts/transcript_status_report.json`
- **チャンネルリスト**: `projects/Founder_Agent_Phase1/documents/references/transcripts/channel_list.json`

---

## 参照方法（スキルから）

```markdown
<!-- SKILL.mdのKnowledge Base参照セクションに追加 -->

## Knowledge Base参照

- CPF概念: `@startup_science/01_stages/cpf/cpf_overview.md`
- **CPF事例集**: `@startup_science/02_frameworks/transcripts/cpf/`  ← 追加
- 顧客インタビュー: `@startup_science/01_stages/cpf/customer_interview.md`
```

**パス**: `@startup_science/02_frameworks/transcripts/`
