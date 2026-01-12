# Late API複数投稿問題の修正記録

## 発生した問題（2026-01-05）

### 症状

SNS自動化スキルのPhase 4（Late API投稿）で、3案を個別に投稿するはずが、1つの投稿に3案すべてが結合されて送信された。

**期待**: 3件の個別投稿（案1、案2、案3）
**実際**: 1件の投稿に3案すべてが含まれる

### 根本原因

1. **LLM推論による実行**
   - SNS自動化スキルはPythonスクリプトではなく、LLM推論で実行されている
   - SKILL.mdには正しいパターンが記載されているが、実際の実行時に逸脱した

2. **バリアント結合の発生箇所**
   - 3つの別々のPOSTリクエストではなく、1つのリクエストに全バリアントが結合された

## 解決策の実装

### 1. 確実なPythonスクリプト作成

**ファイル**: `scripts/fix_late_api_multi_post.py` → `scripts/late_api_multi_post_v2.py`

**特徴**:
- 各案を個別に抽出（正規表現で厳密に分離）
- 3回の独立したPOSTリクエスト
- エラーハンドリングとリトライロジック

**実装の鍵**:

```python
# 各案を個別に抽出
for variant_num in [1, 2, 3]:
    variant_data = extract_variant_content(markdown, variant_num)
    variants.append(variant_data)

# 3回の独立したPOSTリクエスト
for plan in posting_plan:
    variant = next(v for v in variants if v["variant_num"] == plan["variant_num"])
    result = post_to_late_api(variant["full_content"], scheduled_datetime)
```

### 2. .envファイルのインラインコメント除去

**問題**: 環境変数の値にインラインコメントが含まれていた

```bash
# 修正前（問題あり）
LATE_LINKEDIN_ACCOUNT_ID="69576d354207e06f4ca837e1"  # 優一 佐藤

# 修正後（正しい）
# LinkedIn: 優一 佐藤
LATE_LINKEDIN_ACCOUNT_ID="69576d354207e06f4ca837e1"
```

**影響**: Late APIがアカウントIDを正しく解析できず、500エラーが発生

### 3. 共通ライブラリの作成

**ファイル**: `scripts/late_api_utils.py`

**提供する機能**:
- `load_env_vars()`: インラインコメント対応の環境変数読み込み
- `get_late_api_config()`: Late API設定の一元管理
- `format_datetime_for_late_api()`: ISO8601形式への変換
- `post_to_late_api()`: 正しいスキーマでの投稿
- `post_multiple_variants_to_late_api()`: 複数バリアントの個別投稿

### 4. 正しいAPIスキーマの確認

#### エンドポイント

```python
# 誤り
base_url = "https://api.getlate.dev/v1"

# 正しい（設定ファイルで確認済み）
base_url = "https://getlate.dev/api/v1"
```

#### リクエストボディ

```python
# 誤り
payload = {
    "post": content,
    "profile_ids": [account_id],
    "schedule_at": scheduled_datetime_str
}

# 正しい（late_api_post.pyで確認済み）
payload = {
    "content": content,
    "platforms": [
        {
            "platform": "linkedin",
            "accountId": account_id
        }
    ],
    "scheduledFor": scheduled_datetime_str,
    "timezone": "Asia/Tokyo"
}
```

## 再発防止策

### 1. SNS自動化スキルの更新

Phase 4の実装を以下のように変更：

```markdown
## Phase 4: スケジュール投稿

**重要**: 複数案を投稿する場合は、必ず `late_api_multi_post_v2.py` を使用すること。

**実行**:
```bash
python3 scripts/late_api_multi_post_v2.py
```

**LLM推論での投稿は禁止**: 必ずPythonスクリプトを使用。
```

### 2. .env管理のベストプラクティス

**ルール**:
- インラインコメントは使用禁止
- コメントは必ず別行に記載
- 値にスペースや特殊文字が含まれる場合はクォートで囲む

```bash
# 正しい例
# Platform: Service Name
VAR_NAME="value"

# 誤った例（禁止）
VAR_NAME="value"  # Service Name
```

### 3. 共通ライブラリの利用

新規スクリプト作成時は、必ず `late_api_utils.py` をインポート：

```python
from late_api_utils import (
    load_env_vars,
    get_late_api_config,
    post_to_late_api,
    post_multiple_variants_to_late_api
)
```

### 4. テストスクリプトの実行

Late API連携の変更時は、必ず以下のテストを実行：

```bash
# 環境変数読み込みテスト
python3 scripts/late_api_utils.py

# 実際の投稿テスト（確認プロンプトあり）
python3 scripts/late_api_multi_post_v2.py
```

## チェックリスト

Late API投稿の実装・修正時は以下を確認：

- [ ] エンドポイントは `https://getlate.dev/api/v1` を使用
- [ ] リクエストボディは `platforms` 配列形式
- [ ] `scheduledFor` はISO8601形式（`+09:00` 付き）
- [ ] .envファイルにインラインコメントがない
- [ ] 環境変数読み込みは `late_api_utils.load_env_vars()` を使用
- [ ] 複数バリアント投稿は `late_api_multi_post_v2.py` またはユーティリティ関数を使用
- [ ] LLM推論ではなく、Pythonスクリプトで実行

## 参考資料

### 関連ファイル

- **修正版スクリプト**: `scripts/late_api_multi_post_v2.py`
- **共通ライブラリ**: `scripts/late_api_utils.py`
- **.env設定**: `Stock/programs/副業/projects/SNS/.env`
- **API設定**: `config/late_api_config.json`

### 過去の成功実装

- `scripts/late_api_post.py`: 正しいスキーマの参照実装
- `config/late_api_config.json`: エンドポイントとアカウントID設定

## 修正履歴

| 日付 | 修正内容 | 実施者 |
|------|---------|--------|
| 2026-01-05 | 問題発生、修正版スクリプト作成、共通ライブラリ作成 | Claude Code |
| 2026-01-05 | .envインラインコメント除去、再発防止ドキュメント作成 | Claude Code |

---

**最終更新**: 2026-01-05
**次回レビュー**: 2026-02-05（1ヶ月後）
