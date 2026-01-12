# create-viral-x-thread プロジェクト経緯レポート

**プロジェクト名**: 海外バズX投稿からスレッド自動生成＆予約投稿システム
**開始日**: 2026-01-03
**ステータス**: 保留（Phase 3完了、Phase 4-5未実装）
**実装者**: Claude Code Sonnet 4.5

---

## プロジェクト概要

### 目的
海外のバズX投稿を収集し、日本語の技術解説スレッド＆画像を生成してSlack承認経由でLate APIに予約投稿する完全自動化システムの構築。

### ターゲット要件
- **情報ソース**: 海外のバズX投稿（RT 100以上、AI関連）
- **スレッド長**: 自動調整（10-15ツイート）
- **トーン**: 技術解説スタイル（落ち着いた、専門的）
- **自動化レベル**: 完全自動（テーマ指定 → リサーチ → 生成 → 承認 → 予約）
- **承認フロー**: Slack経由
- **画像生成**: Gemini NanoBanana API
- **投稿予約**: Late API（毎日20:00 JST）
- **バズ要素**: エンゲージメント最優先（RT・いいね狙い）

### 技術スタック
- **Claude Code**: メインオーケストレーション
- **Claude in Chrome**: X投稿収集（API不要）
- **Claude Sonnet 4.5**: スレッド生成
- **Gemini Imagen 4.0**: 画像生成（NanoBanana API）
- **Slack**: 承認フロー（既存インフラ再利用）
- **Late API**: 投稿予約

---

## 実装進捗サマリー

| Phase | 機能 | ステータス | 実行時間（実績） | 完了日 |
|-------|------|-----------|----------------|--------|
| Phase 1 | バズ投稿収集 | ✅ **完了** | 5-7分 | 2026-01-03 |
| Phase 2 | スレッド生成 | ✅ **完了** | 10-15分 | 2026-01-03 |
| Phase 3 | 画像生成 | ✅ **完了** | 5-10分 | 2026-01-03 |
| Phase 4 | Slack承認 | 🔜 未実装 | 待機 | - |
| Phase 5 | Late API予約 | 🔜 未実装 | 5分 | - |

**総実行時間（Phase 1-3）**: 約20-30分

---

## Phase 1: バズ投稿収集（完了）

### 実装内容
- **エージェント**: general-purpose (Haiku)
- **ツール**: Claude in Chrome（mcp__claude-in-chrome__*）
- **検索クエリ**: `(Claude OR GPT OR Gemini OR AI) min_retweets:100 lang:en`
- **収集件数**: 12件

### 出力ファイル
**ファイル名**: `viral_posts_20260103.json`
**パス**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/viral_posts_20260103.json`

### 収集結果ハイライト

**トップ3投稿**:
1. **Boris Cherny** (@bcherry) - Claude Code創作者の使い方解説
   - RT: 3,438 | いいね: 2,671 | Views: 225,700
   - トピック: Claude Code Tips
   - スレッド: 2ツイート

2. **Jaana Dogan** (@rakyll) - Claude Codeで分散エージェント開発
   - RT: 1,020 | いいね: 9,058 | Views: 73,700
   - トピック: Claude Code Development

3. **Rohit Ghumare** (@ghumare64) - Claude Codeマスタークラス
   - RT: 1,147 | いいね: 6,997 | Views: 53,700
   - トピック: Claude Code Tutorial

### 検証結果
- ✅ 収集速度: 5-7分（想定15-20分より高速）
- ✅ データ品質: 高品質（RT 100以上、AI関連）
- ✅ JSON構造: 正しくフォーマット済み
- ✅ トピック検出: 自動分類成功

---

## Phase 2: スレッド生成（完了）

### 実装内容
- **エージェント**: general-purpose (Sonnet)
- **入力**: `viral_posts_20260103.json`
- **選択**: エンゲージメント最高投稿（Boris Cherny氏）

### 出力ファイル
**ファイル名**: `thread_generated_20260103.json`
**パス**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/thread_generated_20260103.json`

### 生成スレッド仕様

**統計情報**:
- **総ツイート数**: 14（フック1 + 詳細13）
- **総文字数**: 1,875字
- **平均文字数/ツイート**: 134字（280字制限内）
- **推定読了時間**: 4分

**カバーした13トピック**:
1. バニラ設定で十分
2. 5〜15の並列実行
3. CLAUDE.md共有
4. Plan mode活用
5. **検証手段を与える（最重要）**
6. Opus 4.5活用
7. スラッシュコマンド
8. タスク分離の徹底
9. .claudeignore除外
10. バックグラウンド実行
11. Resume機能
12. コスト最適化（40-50%削減）
13. 「正しい使い方」は存在しない

**フックツイート（1ツイート目）**:
```
🚨 Claude Code開発者本人が「自分の使い方」を公開

驚いたのは「特別なカスタマイズなしでも十分使える」ということ

・5〜15のClaude並列実行
・チームでCLAUDE.md共有
・Plan modeで計画→一発実装
・検証手段を与えるのが最重要

公式開発者が共有してくれた13のポイントを解説します👇
```

### 検証結果
- ✅ 各ツイート280字以内（厳守）
- ✅ エンゲージメント要素（フック、数字、具体例）完備
- ✅ 技術的正確性維持（元投稿＋公式ドキュメント確認済み）
- ✅ 【Tip X】形式で構造化

---

## Phase 3: 画像生成（完了）

### 試行錯誤の経緯

#### v1（初回生成）- 失敗
**問題点**:
- ❌ 日本語テキストが文字化け
  - 「アレコンジャナブ Claude Code迭択の13月Tips」（意味不明）
  - 「特制定にこので使かるリガでる」（崩れ）
  - 「毎5~155用削通験」（崩れ）

**原因**: Imagen 4.0は日本語のレンダリングに課題あり

#### v2（NanoBanana Pro最適化）- 成功 ✅

**改善点**:
1. **プロンプトエンジニアリング手法適用**:
   - 構造化プロンプト: `[主題] + [スタイル] + [構図] + [色彩] + [照明] + [品質キーワード] + [技術仕様]`
   - 日本語テキスト削除（意図的にテキストなし版生成）
   - 左40%にテキストオーバーレイ用スペース確保

2. **詳細な視覚要素指定**:
   - 5〜15個のターミナルウィンドウ（カスケード配置）
   - Python/JavaScript/TypeScriptのシンタックスハイライト
   - Claude Codeロゴ（紫〜青グラデーション）
   - 並列処理を示唆する幾何学模様

3. **カラーパレット最適化**:
   - プライマリ: #4A90E2（青）→ #9B51E0（紫）グラデーション
   - セカンダリ: #2D2D2D（ダークチャコール）
   - アクセント: #00D4FF（シアン）、#FF6B35（オレンジ）

### 出力ファイル（v2）

**ファイル名**: `thread_image_20260103_v2.png`
**パス**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/thread_image_20260103_v2.png`

**仕様**:
- **解像度**: 1408 x 768px（16:9、Twitter推奨）
- **ファイルサイズ**: 1.1 MB
- **フォーマット**: PNG（8-bit RGB）
- **生成モデル**: Imagen 4.0（Google）

### 検証結果
- ✅ 視覚的クオリティ: 非常に高品質
- ✅ 構図設計: Twitter最適化（左40%空白、右60%ビジュアル）
- ✅ 技術的完成度: シャープなエッジ、プロフェッショナルグレード
- ✅ テキスト問題解決: テキストなし版で回避

---

## 生成ファイル一覧

### Phase 1出力
1. `viral_posts_20260103.json` (12件のバズ投稿)

### Phase 2出力
2. `thread_generated_20260103.json` (14ツイートのスレッド)

### Phase 3出力
3. `thread_image_20260103.png` (v1 - 日本語文字化けあり)
4. `thread_image_20260103_v2.png` (v2 - 高品質版、推奨)

### スキルドキュメント
5. `.claude/skills/create-viral-x-thread/SKILL.md` (Phase 1-3実装済み)

---

## キーファインディング

### 成功要因
1. **Claude Code並列エージェント活用**
   - Phase 1: Haiku（コスト削減）
   - Phase 2: Sonnet（高品質生成）
   - Phase 3: Sonnet（プロンプトエンジニアリング）

2. **Claude in Chromeの威力**
   - X API不要でバズ投稿収集
   - 5-7分で12件収集（想定より高速）

3. **プロンプトエンジニアリング**
   - 構造化プロンプトでImagen 4の性能を最大化
   - 日本語テキスト問題を回避（テキストなし版）

### 課題・制約
1. **Imagen 4の日本語レンダリング**
   - ❌ 日本語テキストが文字化け
   - ✅ 解決策: 英語プロンプト＋テキストなし版

2. **Late API未検証**
   - Phase 5で実装予定
   - API仕様の事前確認が必要

3. **Slack承認フロー未統合**
   - 既存の`approve_and_schedule.py`は存在
   - スレッド形式への対応が必要

---

## 未実装機能（Phase 4-5）

### Phase 4: Slack承認フロー

**実装タスク**:
1. 既存の`approve_and_schedule.py`を改修
2. スレッド形式（14ツイート）に対応
3. 画像プレビュー表示
4. 承認/却下/修正ボタン実装
5. 修正フィードバックループ（最大3回）

**参照ファイル**:
- `Stock/programs/副業/projects/SNS/scripts/approve_and_schedule.py`
- `Stock/programs/副業/projects/SNS/scripts/slack_approval_server.py`

### Phase 5: Late API予約投稿

**実装タスク**:
1. Late API仕様確認（エンドポイント、認証方法）
2. スレッド投稿API呼び出し実装
3. 画像添付機能実装
4. 投稿時刻設定（毎日20:00 JST）
5. エラーハンドリング

**必要情報**:
- Late API アクセストークン（未取得）
- API仕様ドキュメント

---

## 次のステップ（再開時）

### 短期（Phase 4実装）
1. Slack承認フローの改修
   - スレッド形式対応
   - 画像プレビュー表示
   - Interactive Buttonsテスト

2. 統合テスト
   - Phase 1-4の連続実行
   - エラーハンドリング検証

### 中期（Phase 5実装）
1. Late API調査
   - アクセストークン取得
   - API仕様確認
   - サンプルリクエスト実行

2. Late API統合
   - 投稿予約機能実装
   - 画像添付テスト

### 長期（完全自動化）
1. マスタースキル作成
   - Phase 1-5を1コマンドで実行
   - `/create-viral-x-thread --auto`

2. 毎日自動実行
   - cron/GitHub Actionsで定期実行
   - 完全無人運用

---

## 再開時の参照情報

### スキルファイル
`.claude/skills/create-viral-x-thread/SKILL.md`

### データディレクトリ
`/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/`

### 実行コマンド例（Phase 1-3）

```bash
# Phase 1: バズ投稿収集
「バズ投稿からスレッド作成」Phase 1のみ実行

# Phase 2: スレッド生成
「バズ投稿からスレッド作成」Phase 2のみ実行

# Phase 3: 画像生成（v2推奨）
「バズ投稿からスレッド作成」Phase 3のみ実行、NanoBanana Pro最適化プロンプト使用
```

### API Keys
- **NanoBanana API**: `AIzaSyCg1OWV0kETK3OocmDgtf4J5dU-NpfpzGs`
- **Late API**: 未取得（Phase 5で必要）

### 関連ドキュメント
- @.claude/rules/execution_preference.md - LLM優先アプローチ
- @.claude/rules/parallel_execution.md - 並列エージェント実行
- @Stock/programs/副業/projects/SNS/scripts/approve_and_schedule.py - 既存Slack承認フロー

---

## プロジェクト成果物の評価

### 実装品質
- ✅ Phase 1-3: 高品質実装完了
- ✅ コード品質: サブエージェント活用で効率化
- ✅ ドキュメント品質: SKILL.md詳細記載

### 生成コンテンツ品質
- ✅ スレッド: エンゲージメント最適化済み
- ✅ 画像: プロフェッショナルグレード
- ✅ 技術正確性: 元投稿＋公式ドキュメント確認済み

### 再利用性
- ✅ スキル化: `.claude/skills/`に保存
- ✅ 汎用性: 他のトピックにも応用可能
- ✅ 拡張性: Phase 4-5追加可能

---

## 総評

**Phase 1-3の実装は成功**。Claude Codeのサブエージェント並列実行、Claude in Chrome、Gemini Imagen 4を効果的に組み合わせ、高品質なコンテンツ生成システムを構築できた。

**Phase 4-5の実装により、完全自動化システムが完成する見込み**。Late API仕様確認が次の重要タスク。

---

**プロジェクトステータス**: 保留（Phase 3完了、Phase 4-5未実装）
**再開推奨時期**: Late APIアクセストークン取得後
**レポート作成日**: 2026-01-03
**次回レビュー**: Phase 4実装前
