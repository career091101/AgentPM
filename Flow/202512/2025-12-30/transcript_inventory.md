# YouTube動画トランスクリプト所在確認レポート

**調査日時**: 2025-12-30
**対象ディレクトリ**: `transcripts/items/`

---

## 📊 サマリー

| 項目 | 値 |
|------|-----|
| **総ファイル数** | 469個 |
| **総サイズ** | 17MB |
| **ファイル形式** | Markdown (.md) |
| **作成日時** | 2025-12-30 18:47 |
| **ベースパス** | `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/references/transcripts/items/` |

---

## 📁 発見ファイル一覧（サンプル20件）

### 1. `-Csoj96rIrs.md`
- **パス**: `items/-Csoj96rIrs.md`
- **サイズ**: 17KB
- **作成日時**: 2025-12-30 18:47
- **内容プレビュー**:
  ```
  # Transcript: -Csoj96rIrs

  - URL: https://www.youtube.com/watch?v=-Csoj96rIrs
  - Retrieved at: 2025-12-30T09:14:20+09:00

  ## Text

  - [00:02] こんにちは。キノコです。この動画では
  - [00:05] AIXについて解説をします。最近企業の
  - [00:09] DX推進の現場でAIXという新しい概念
  ```
- **推定トピック**: AIX、DX推進

### 2. `-NrAX4OapkQ.md`
- **サイズ**: 20KB

### 3. `-WB0T0XmDrY.md`
- **サイズ**: 17KB

### 4. `-mldKsBR0UM.md`
- **サイズ**: 22KB

### 5. `04Gap8vWV28.md`
- **サイズ**: 10KB

### 6. `09tJS0ZEHms.md`
- **サイズ**: 13KB

### 7. `15_pppse4fY.md`
- **サイズ**: 14KB

### 8. `1AWFAWfHNcs.md`
- **サイズ**: 86KB（最大サイズ）
- **内容プレビュー**:
  ```
  # Transcript: 1AWFAWfHNcs

  - URL: https://www.youtube.com/watch?v=1AWFAWfHNcs
  - Retrieved at: 2025-12-30T09:17:55+09:00

  ## Text

  - [00:03] 読み込めてますねこれいやすごくないです
  - [00:04] かただですよ本当にすごいのはここから
  - [00:07] ですこのカスタマイズ性の高さがAIと
  - [00:09] メイクを組み合わせることのすごいところ
  ```
- **推定トピック**: ChatGPT、LINE、個人DX

### 9. `1HHZdB2O2tI.md`
- **サイズ**: 13KB

### 10. `1WImBwiA7RA.md`
- **サイズ**: 8.1KB

### 11. `1choivCbZDg.md`
- **サイズ**: 14KB

### 12. `1eNoNadJfHE.md`
- **サイズ**: 51KB

### 13. `1jenfjT2PW8.md`
- **サイズ**: 11KB

### 14. `1v7HPnyaaPU.md`
- **サイズ**: 2.7KB（最小サイズ）

### 15. `239JDMFuGcQ.md`
- **サイズ**: 9.0KB

### 16. `2D72MYTqUbE.md`
- **サイズ**: 33KB

### 17. `2HVFruvFf08.md`
- **サイズ**: 18KB

### 18. `2VroIM26s84.md`
- **サイズ**: 38KB

### 19. `2YLoX7FSwYQ.md`
- **サイズ**: 17KB

### 20. `... 449個の追加ファイル`

---

## 📝 ファイル構造

全てのトランスクリプトファイルは以下の統一フォーマットを使用：

```markdown
# Transcript: [video_id]

- URL: https://www.youtube.com/watch?v=[video_id]
- Retrieved at: [ISO 8601 timestamp]

## Text

- [HH:MM] [トランスクリプトテキスト]
- [HH:MM] [トランスクリプトテキスト]
...
```

### 特徴
- **メタデータ**: URL、取得時刻のみ（動画タイトル、チャンネル名、公開日なし）
- **タイムスタンプ付きテキスト**: 各行にタイムスタンプ（分:秒）が付与
- **言語**: 主に日本語、一部英語トランスクリプト含む

---

## 🔍 主要トピック（予備調査）

サンプルファイルから確認された頻出キーワード：
- AI、AIX
- DX、個人DX
- ChatGPT
- LLM
- LINE
- カスタマイズ、自動化

**次ステップ**: T005-2でルールベースのトピック抽出を実行し、全469動画の詳細分類を実施

---

## ✅ 完了確認

- [x] 全トランスクリプトファイル数: 469個確認
- [x] 総サイズ: 17MB確認
- [x] ファイル構造: 統一されたMarkdown形式
- [x] サンプルプレビュー: 20ファイル確認

**T005-1タスク完了**

**次のタスク**: T005-2（トランスクリプトから重要トピック抽出）

---

**作成者**: Claude Code
**生成日時**: 2025-12-30
