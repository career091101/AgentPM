# SNS自動化スキル 共有コンテキスト

このドキュメントは全サブスキル（Phase 1-4）が共通して参照する基本情報を記載しています。

**対象スキル**:
- collect-x-timeline
- extract-content
- analyze-replies
- research-topic
- generate-sns-posts-takano
- approve-and-schedule

---

## プロジェクト概要

### 目的
AI・テクノロジーの最新情報をLinkedInで発信し、CEO/経営者層にリーチする投稿を自動生成・予約投稿する。

### ターゲットオーディエンス
- CEO/経営者
- 事業責任者
- AI/テクノロジー導入検討者

### 投稿プラットフォーム（Option C対応 v2.4）

**日次投稿数**:
- **LinkedIn**: 1案/日（8:00 JST）
- **X**: 3投稿/日（派生7:30 + スレッド12:00 + スレッド20:00）
- **Threads**: 2投稿/日（派生7:30 + 新規20:00）
- **合計**: 6投稿/日

### プラットフォーム別投稿スケジュール（Option C）

| プラットフォーム | 投稿タイプ | 投稿時刻 | トピック | 説明 |
|----------------|-----------|---------|---------|------|
| **LinkedIn** | 高野式7パターン | 8:00 JST | Top 1 | メイン投稿、1,150-1,300文字 |
| **X派生** | フック変更 | 7:30 JST | Top 1 | LinkedIn→X用フック、280文字 |
| **Xスレッド1** | 深掘り型 | 12:00 JST | Top 2 | 5-7ツイートスレッド |
| **Xスレッド2** | 深掘り型 | 20:00 JST | Top 3 | 5-7ツイートスレッド |
| **Threads派生** | フック変更 | 7:30 JST | Top 1 | LinkedIn→Threads用、500文字 |
| **Threads新規** | LinkedIn似 | 20:00 JST | Top 2 | 独自生成、500文字 |

### 投稿タイプ定義

| タイプ | 説明 | 文字数制限 |
|--------|------|-----------|
| **高野式7パターン** | LinkedIn専用、7要素必須 | 1,150-1,300文字 |
| **フック変更（派生）** | LinkedIn投稿のフックのみ変更 | X: 280文字、Threads: 500文字 |
| **深掘り型スレッド** | 5-7ツイートのX専用スレッド | 各ツイート280文字 |
| **LinkedIn似** | Threads用、LinkedIn風の表現 | 500文字 |

### トピック選定ルール

- **Top 1**: LinkedIn、X派生、Threads派生（同一トピック）
- **Top 2**: Xスレッド1、Threads新規
- **Top 3**: Xスレッド2

---

## 実行フロー全体像

| Phase | 機能 | 所要時間 | 実行モード |
|-------|------|---------|----------|
| **Phase 1** | データ収集 | 20-30分 | 順次実行 |
| **Phase 2** | 分析・調査 | 30-45分 | 逐次実行（1→2→3） |
| **Phase 3** | 投稿生成 | 10-15分 | 高野式7パターン |
| **Phase 4** | 予約投稿 | 2-5分 | Late API完全自動化 |

**総所要時間**: 62-95分

---

## 共通ファイルパス

### 基本ディレクトリ
```
BASE_DIR = Stock/programs/副業/projects/SNS
```

### 出力先ディレクトリ
```
data/              # データファイル（CSV、JSON、Markdown）
config/            # 設定ファイル（late_api_config.json等）
scripts/           # 実行スクリプト
```

### 成果物の命名規則
```
{output_type}_{date}.{ext}

例:
- x_timeline_2026-01-05.csv
- content_extracted_2026-01-05.md
- posts_generated_takano_2026-01-05.md
- late_api_scheduled_2026-01-05.json
```

---

## 共通設定

### 日付フォーマット
- **ファイル名**: `YYYY-MM-DD`
- **ログ**: `YYYY-MM-DD HH:MM:SS JST`
- **Late API**: ISO 8601形式（`YYYY-MM-DDTHH:MM:SS+09:00`）

### タイムゾーン
- **基準**: Asia/Tokyo (JST, UTC+9)
- **投稿時刻**:
  - LinkedIn: 8:00 AM JST（ビジネスタイム）
  - X/Threads: 20:00 JST（リラックスタイム）

---

## 品質基準

### 高野メソッド7要素（Phase 3必須）
1. ① 引き込み - 最初の3行でフックを作る
2. ② データ/事例 - 具体的な数値・事実
3. ③ 共感 - 読者の課題・状況への共感
4. ④ 洞察 - 独自の解釈・視点
5. ⑤ アドバイス - 具体的な行動提案
6. ⑥ 問いかけ - 必ず問いかけで終わる
7. ⑦ 固有名詞 - 企業名・人名・サービス名

### 投稿文字数
- **標準**: 700-900文字
- **ロング**: 1000-1500文字
- **LinkedIn最適**: 800-1200文字（エンゲージメント最大化）

### チェックリスト合格基準
- **必須**: 7要素すべて達成
- **禁止事項**: 0件（8項目の禁止事項に抵触しない）
- **総合スコア**: 70点以上（100点満点）

---

## エラーハンドリング基本方針

### 全Phase共通
- **即時停止**: Phase 1-4の全フェーズでエラー発生時は即座に停止
- **リトライ**: 外部API失敗時は最大3回リトライ（指数バックオフ）
- **フォールバック**: データ不足時は代替データソースを使用

### Phase別方針
| Phase | エラー時の対応 | 理由 |
|-------|--------------|------|
| **Phase 1** | 即時停止 | 後続処理が全て依存 |
| **Phase 2** | 即時停止 | 品質重視 |
| **Phase 3** | 即時停止 | 投稿生成は最重要 |
| **Phase 4** | 部分成功許容 | 1案でも成功すればOK |

**詳細**: [@_shared/error_handling_patterns.md](../_shared/error_handling_patterns.md)

---

## Late API設定（Phase 4）

### 基本情報
- **API URL**: `https://getlate.dev/api/v1`
- **設定ファイル**: `Stock/programs/副業/projects/SNS/config/late_api_config.json`
- **ダッシュボード**: https://getlate.dev/dashboard

### 必要な環境変数（.env）
```
LATE_API_KEY=sk_...
LATE_LINKEDIN_ACCOUNT_ID=...
LATE_TWITTER_ACCOUNT_ID=...    # Option C対応
LATE_THREADS_ACCOUNT_ID=...    # Option C対応
```

### 投稿パラメータ（Option C対応）
- **プラットフォーム**: linkedin, twitter, threads
- **予約時刻**: 7:30, 8:00, 12:00, 20:00 JST
- **競合検出**: 全4時間帯で自動回避（`target_hours=[7, 8, 12, 20]`）
- **Xスレッド**: `threadItems`パラメータ使用

### 投稿スクリプト
- **LinkedIn専用（旧）**: `scripts/late_api_post.py`
- **マルチプラットフォーム（新）**: `scripts/late_api_multi_post_v2.py`

**詳細**: [@late_api_integration_guide.md](./late_api_integration_guide.md)

---

## 出力フォーマット

### 成功時のステータス
```yaml
status: success
phase: "Phase {N}"
execution_time: "{M}分"
output_file: "{path}"
timestamp: "{YYYY-MM-DD HH:MM:SS JST}"
```

### エラー時のステータス
```yaml
status: error
error_code: PHASE_{N}_FAILURE
message: "Phase {N}の{skill_name}スキルが失敗しました"
timestamp: "{YYYY-MM-DD HH:MM:SS JST}"
details:
  attempted_action: "{action}"
  failure_reason: "{reason}"
  retry_count: N
```

---

## 関連ドキュメント

### メインドキュメント
- **オーケストレーター**: [@SKILL.md](./SKILL.md)
- **高野式投稿生成**: [@generate-sns-posts-takano/SKILL.md](./generate-sns-posts-takano/SKILL.md)

### 詳細ガイド
- **Late API統合**: [@late_api_integration_guide.md](./late_api_integration_guide.md)
- **高野式7パターン**: [@generate-sns-posts-takano/takano_patterns_detailed.md](./generate-sns-posts-takano/takano_patterns_detailed.md)
- **エラーハンドリング**: [@_shared/error_handling_patterns.md](../_shared/error_handling_patterns.md)

### 設定ファイル
- **パターン設定**: [@generate-sns-posts-takano/takano_patterns_config.json](./generate-sns-posts-takano/takano_patterns_config.json)
- **Late API設定**: `Stock/programs/副業/projects/SNS/config/late_api_config.json`

---

## 使用ガイドライン

### サブスキル開発者向け

1. **このファイルを最初に読み込む** - 全サブスキルの冒頭で参照
2. **重複記述を避ける** - 共通情報はこのファイルから参照
3. **パス規約を遵守** - 命名規則に従ってファイルを出力
4. **エラーハンドリングを統一** - 共有パターンを使用

### オーケストレーター開発者向け

1. **Task tool起動時に参照指示** - サブエージェントに読み込みを指示
2. **重複読み込みを最小化** - 共通情報は1回のみ読み込み
3. **コンテキスト効率を最大化** - 詳細情報は必要時のみ読み込み
