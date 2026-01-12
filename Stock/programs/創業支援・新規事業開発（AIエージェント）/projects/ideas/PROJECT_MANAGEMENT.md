# アイデア管理プロジェクト - 運用ガイドライン

**作成日**: 2025-12-31
**プロジェクトタイプ**: アイデアインデックス・検証管理プロジェクト

---

## 📋 プロジェクト概要

### 目的
FounderAgentで検証したビジネスアイデアを一元管理し、CPF/PSF検証プロセスを体系的に追跡する。

### 位置づけ
- **プロジェクト種別**: インデックスプロジェクト（個別アイデアは番号付きサブプロジェクトとして管理）
- **管理対象**: 副業者・スタートアップ向けビジネスアイデア
- **検証フレームワーク**: Lean Startup (CPF → PSF → MVP)

### プロジェクト憲章の必要性
**不要**
理由: このプロジェクトは個別のアイデア（001, 002, ...）を管理するインデックスであり、各アイデアが独自の憲章を持つ。全体を統括する憲章ではなく、本ドキュメント（運用ガイドライン）で管理方針を定義する。

---

## 📁 ディレクトリ構造

```
ideas/
├── index.md                    # アイデア一覧ダッシュボード
├── PROJECT_MANAGEMENT.md       # 本ドキュメント（運用ガイドライン）
├── 001_ai-business-assistant/  # アイデア001
│   ├── documents/
│   │   └── 1_initiating/
│   │       └── project_charter.md  # 個別憲章
│   └── mvp/
├── 002_sme-ai-consulting/      # アイデア002
│   ├── documents/
│   │   └── 1_initiating/
│   │       └── project_charter.md  # 個別憲章
│   └── mvp/
└── 003_xxxxx/                  # アイデア003 (将来)
```

---

## 🔄 アイデアのライフサイクル

### ステータス定義

| ステータス | 説明 | 達成基準 |
|-----------|------|---------|
| 🆕 Discovery | アイデア発見・検証中 | ペルソナ・課題定義完了 |
| 🟡 CPF Complete | Customer Problem Fit達成 | 10人以上の課題ヒアリング完了 |
| ✅ PSF Complete | Problem Solution Fit達成 | プロトタイプで3人以上が価値認識 |
| 🚀 MVP Deployed | MVP公開済み | 本番環境公開 + 初期ユーザー獲得 |
| 🔄 Pivot | ピボット中 | 仮説変更・方向転換中 |
| 📦 Archived | アーカイブ済み | 検証終了・中止 |

### フロー

```
新規アイデア
  ↓
Discovery (ペルソナ・課題定義)
  ↓
CPF検証 (10人ヒアリング)
  ↓
PSF検証 (プロトタイプ検証)
  ↓
MVP開発・公開
  ↓
PMF追求 → 成長 / Pivot / Archive
```

---

## 🚀 新規アイデア追加プロセス

### 1. アイデア番号の採番
- 3桁の連番を採用（001, 002, ...）
- index.mdで最新番号を確認

### 2. ディレクトリ作成
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/ideas

# 新規ディレクトリ作成
mkdir -p 003_[idea-name]/documents/1_initiating
mkdir -p 003_[idea-name]/mvp
```

### 3. 個別憲章作成
- PMBOKトリガー「プロジェクト憲章」を使用
- 憲章パス: `003_[idea-name]/documents/1_initiating/project_charter.md`
- 必須項目:
  - プロジェクト名
  - 背景・目的
  - ターゲットペルソナ
  - 課題仮説
  - ソリューション仮説
  - 成功指標（CPF/PSF/MVP）

### 4. index.md更新
```markdown
| ID  | 名称 | ステータス | CPF | PSF | 10x | 作成日 |
|-----|------|-----------|:---:|:---:|:---:|--------|
| 003 | [アイデア名](./003_[idea-name]/) | 🆕 Discovery | - | - | - | 2025-XX-XX |
```

### 5. FounderAgentで検証開始
- `/orchestrate_phase1` - Discovery & CPF検証
- `/orchestrate_phase2` - PSF検証
- `/orchestrate_phase3` - MVP開発

---

## 📊 管理ルール

### index.mdの更新タイミング
- 新規アイデア追加時
- ステータス変更時
- CPF/PSF達成時
- MVP公開時

### 個別アイデアの責任範囲
- **個別憲章**: 各アイデアディレクトリ配下で管理
- **検証ドキュメント**: documents/配下に格納
- **MVPコード**: mvp/配下に格納

### アーカイブ基準
- CPF検証で課題が深刻でないと判明
- PSF検証でソリューションが機能しない
- 市場規模が小さすぎる（TAM < 10億円）
- リソース不足で継続不可

---

## 🔗 関連プロジェクト

### Founder_Research
- 役割: 起業家事例研究・パターン抽出
- 連携: 成功パターンをアイデア検証に活用

### Founder_Agent_Phase1
- 役割: Discovery & CPF検証自動化
- 連携: 新規アイデアの初期検証を実行

### solo_ideas
- 役割: Solopreneur向けアイデア管理
- 違い: こちらは副業者・スタートアップ向け

---

## 💡 クイックアクション

### 新規アイデア作成
```
/orchestrate_phase1
```

### ピボット判断
```
/decide_pivot
```

### PMF診断
```
/diagnose_pmf
```

---

## 📝 更新履歴

| 日付 | 更新内容 |
|------|---------|
| 2025-12-31 | 運用ガイドライン初版作成 |
| 2025-12-30 | index.md作成、アイデア001追加 |

---

**運用方針**: 個別アイデアに憲章を持たせ、全体はindex.mdとこのガイドラインで管理する。憲章は個別アイデアレベルで必要。
