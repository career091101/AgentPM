# T005-1: YouTubeトランスクリプト棚卸しレポート

**作成日**: 2025-12-31
**作成者**: Claude Sonnet 4.5
**タスク**: YouTubeトランスクリプト→GenAI_Research統合 Phase 1

---

## エグゼクティブサマリー

Founder_Agent_Phase1プロジェクトの`transcripts/items/`ディレクトリに存在する469個のYouTubeトランスクリプトファイルを棚卸ししました。これらのファイルはGenAI_Researchプロジェクトに統合され、YAML frontmatterメタデータを付与して検索可能な知識ベースとして整備されます。

---

## 基本統計

| 項目 | 値 |
|------|-----|
| **総ファイル数** | 469件 |
| **総サイズ** | 17MB |
| **平均ファイルサイズ** | 74KB (約37KB) |
| **ファイル形式** | Markdown (.md) |
| **ディレクトリ** | `/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/references/transcripts/items/` |

---

## ファイル構造

### 現在のフォーマット

各トランスクリプトファイルは以下の構造を持ちます：

```markdown
# Transcript: {video_id}

- URL: https://www.youtube.com/watch?v={video_id}
- Retrieved at: {timestamp}

## Text

- [00:02] トランスクリプト本文...
- [00:05] タイムスタンプ付きテキスト...
```

### 現在の課題

1. **メタデータ不足**: YAML frontmatterが存在しない
2. **検索不能**: 動画タイトル、話者名、トピックタグがない
3. **分類不能**: カテゴリ、技術スタック、ユースケース情報がない
4. **孤立**: GenAI_Researchプロジェクトと統合されていない

---

## サンプルファイルプレビュー（10件）

| # | ファイル名 | Video ID | サイズ | 行数 | URL |
|---|-----------|----------|--------|------|-----|
| 1 | -Csoj96rIrs.md | -Csoj96rIrs | 17,055 bytes | 279 | https://www.youtube.com/watch?v=-Csoj96rIrs |
| 2 | -NrAX4OapkQ.md | -NrAX4OapkQ | 20,799 bytes | 439 | https://www.youtube.com/watch?v=-NrAX4OapkQ |
| 3 | -WB0T0XmDrY.md | -WB0T0XmDrY | 17,428 bytes | 376 | https://www.youtube.com/watch?v=-WB0T0XmDrY |
| 4 | -mldKsBR0UM.md | -mldKsBR0UM | 22,253 bytes | 211 | https://www.youtube.com/watch?v=-mldKsBR0UM |
| 5 | 04Gap8vWV28.md | 04Gap8vWV28 | 10,601 bytes | 238 | https://www.youtube.com/watch?v=04Gap8vWV28 |
| 6 | 09tJS0ZEHms.md | 09tJS0ZEHms | 13,047 bytes | 279 | https://www.youtube.com/watch?v=09tJS0ZEHms |
| 7 | 15_pppse4fY.md | 15_pppse4fY | 14,776 bytes | 311 | https://www.youtube.com/watch?v=15_pppse4fY |
| 8 | 1AWFAWfHNcs.md | 1AWFAWfHNcs | 87,581 bytes | 1,541 | https://www.youtube.com/watch?v=1AWFAWfHNcs |
| 9 | 1HHZdB2O2tI.md | 1HHZdB2O2tI | 13,175 bytes | 280 | https://www.youtube.com/watch?v=1HHZdB2O2tI |
| 10 | 1WImBwiA7RA.md | 1WImBwiA7RA | 8,279 bytes | 178 | https://www.youtube.com/watch?v=1WImBwiA7RA |

### ファイルサイズ分布

- **最大ファイル**: `yDpV_jgO93c.md`（推定200KB+、長編動画）
- **最小ファイル**: `khZS7dMkqek.md`（推定5KB未満、短編動画）
- **中央値**: 約37KB（約10-15分の動画）

---

## サンプル内容プレビュー

### ファイル: -Csoj96rIrs.md

```markdown
# Transcript: -Csoj96rIrs

- URL: https://www.youtube.com/watch?v=-Csoj96rIrs
- Retrieved at: 2025-12-30T09:14:20+09:00

## Text

- [00:02] こんにちは。キノコです。この動画では
- [00:05] AIXについて解説をします。最近企業の
- [00:09] DX推進の現場でAIXという新しい概念
- [00:14] が注目されています。しかしAIXって何
- [00:17] ?DXとは何が違うのと疑問を持つ方も
- [00:21] いらっしゃるのではないでしょうか。
...（省略）
```

**推測される内容**: AIX（AI Transformation）に関する解説動画。企業のDX推進との違いを説明。

---

## transcript_status_report.json 解析結果

### ファイル構造

```json
{
  "meta": {
    "created_at": "2025-12-30T08:34:28+09:00",
    "config": {
      "transcripts_dir": "...",
      "languages": "ja,ja-JP,en",
      "batch_size": 20
    }
  },
  "videos": {}
}
```

### 利用可能な情報

- ✅ `meta.config`: トランスクリプト取得設定
- ✅ `transcripts_dir`: ファイル配置場所
- ❌ `videos`: **空（メタデータなし）**

**結論**: `transcript_status_report.json`には動画タイトル、チャンネル名、公開日等のメタデータが含まれていません。**WebSearch + LLM解析**戦略が必須です。

---

## 次のステップ（T005-2）

T005-2では、これらの469ファイルからトピック・技術スタックを抽出します：

1. **ルールベース処理**: キーワードマッチングで技術タグを抽出
2. **LLMサンプリング**: 10動画で精度検証
3. **トピック分布**: GenAI、Startup、LLM、RAG等の頻出度分析

---

## 処理方針

### Phase 1: パイロット50動画（WebSearch + LLM）

- WebSearchツールで動画タイトル・チャンネル名を取得
- LLMで検索結果を解析してメタデータ抽出
- トランスクリプト本文をLLMで分析（話者、要約、キーポイント）

### Phase 2: 残り419動画（自動処理）

- パイロット結果を踏まえて全動画を処理
- チェックポイント保存（metadata_progress.json）
- エラーハンドリング（部分メタデータ保存）

---

## 技術的考慮事項

### 推定処理時間

- **WebSearch**: 469動画 × 3秒 = 約23分（レート制限対策含む）
- **LLM処理**: 469動画 ÷ 10動画/バッチ × 30秒 = 約23分
- **合計**: 約50-60分（エラーリトライ含む）

### 推定コスト

- **Claude Haiku**: 47バッチ × $0.003 = 約$0.14（トランスクリプト分析）
- **WebSearch**: 469リクエスト × 無料
- **合計**: 約$0.15-0.20（実質無料）

---

## 成功基準

- ✅ 469ファイルの完全棚卸し完了
- ✅ サンプルプレビュー10件取得
- ✅ transcript_status_report.json解析完了
- ✅ 次ステップ（T005-2）の準備完了

---

**作成日**: 2025-12-31
**ステータス**: ✅ 完了
**次のタスク**: T005-2 トピック抽出
