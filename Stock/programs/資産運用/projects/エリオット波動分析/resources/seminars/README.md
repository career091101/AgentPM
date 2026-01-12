# エリオット波動完全攻略セミナー 文字起こし

## フォルダ構成

```
seminars/
├── README.md                    # このファイル
├── transcripts/                 # 文字起こし原本
│   ├── 20XX-XX-XX_タイトル.txt  # 日付_セミナー名.txt
│   └── ...
└── summaries/                   # AI要約済みファイル
    ├── 20XX-XX-XX_タイトル_summary.md
    └── ...
```

## ファイル命名規則

| 種類 | 形式 | 例 |
|------|------|-----|
| 文字起こし原本 | `YYYY-MM-DD_タイトル.txt` | `2025-01-15_波動カウント基礎.txt` |
| AI要約 | `YYYY-MM-DD_タイトル_summary.md` | `2025-01-15_波動カウント基礎_summary.md` |

## 文字起こしの登録手順

1. `transcripts/` フォルダに文字起こしファイルを配置
2. Antigravityに「セミナー要約して」と依頼
3. 自動でknowledgeへの統合まで実施

## AI処理ワークフロー

```
文字起こし(.txt) 
    ↓ AIで要点抽出
要約ファイル(.md)
    ↓ 内容分類
knowledge/への統合
    ├── 該当chapterファイルに追記
    ├── glossary.mdに新用語追加
    └── case_studies/に実例追加
```

## 統合先knowledgeファイル

| セミナー内容 | 統合先 |
|-------------|--------|
| 推進波・インパルス関連 | `ch2_impulse.md` |
| 修正波関連 | `ch3_corrective.md` |
| 複合修正波関連 | `ch4_complex.md` |
| ダイアゴナル関連 | `ch5_diagonal.md` |
| トレード・実践関連 | `ch6_trading.md` |
| 新用語 | `glossary.md` |
| 実践事例 | `case_studies/` |

---

_作成: 2025-12-21_
