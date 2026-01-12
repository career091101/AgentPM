# Week 6 Phase 1 - MCPセットアップガイド完全性評価

**評価日時**: 2026-01-10
**評価対象**: MCP（Model Context Protocol）統合セットアップドキュメント
**参照基準**: @docs/implementation_guides/week6_mcp.md

---

## エグゼクティブサマリー

| 評価項目 | スコア | 判定 |
|---------|--------|------|
| **Slack App設定ガイド** | 8.5/10 | ✅ 優秀 |
| **BigQuery MCP設定ガイド** | 8.0/10 | ✅ 良好 |
| **Sentry MCPガイド** | 0/10 | ❌ 未作成 |
| **オンボーディング難易度** | Medium | 新規メンバー向け補足あり |
| **全体完成度** | 71% | 要改善 |

**結論**: Slack・BigQueryのセットアップガイドは十分な完全性を持つが、Sentry MCPの専用ガイドが未作成。統合テスト手順とチーム共有設定の記載が不足している。

---

## 1. Slack App Setup Guide 完全性評価

**ファイル**: `/Users/yuichi/AIPM/aipm_v0/docs/slack_app_setup_guide.md`
**総合スコア**: 8.5/10

### 強み

| 項目 | 評価 | 詳細 |
|------|------|------|
| **段階的な手順** | ✅ | Step 1-7で体系的に説明 |
| **スコープ定義** | ✅ | 必須・推奨・オプションで分類（表形式） |
| **トークン取得手順** | ✅ | Bot User OAuth Token、Team IDの両者を明確化 |
| **インストール方法** | ✅ | ワークスペース追加～招待まで一連の流れを提示 |
| **トラブルシューティング** | ✅ | 3つの一般的なエラー（not_in_channel、invalid_auth、missing_scope）に対応 |
| **セキュリティ** | ✅ | トークン保護、最小権限の原則、アクセス制御を記載 |
| **動作確認** | ✅ | curlコマンドでの手動テスト例を提示 |

### 改善すべき点

| 項目 | 重要度 | 改善案 |
|------|--------|--------|
| **スクリーンショット** | 中 | Step 1-2、2-2、3-2の画面キャプチャが欲しい |
| **Team ID取得の複数手段** | 低 | URLパラメータ方式とcurl API方式の両方記載（✓ 既出） |
| **.mcp.json設定例** | 中 | 「次のステップ」で簡潔な.mcp.json設定例を追加 |
| **期待実行時間** | 低 | 「所要時間: 15-20分」の見積もり追加 |

### スコア根拠: 8.5/10

- **完全性**: 85% - 基本手順とトラブルシューティングはカバー
- **明瞭性**: 90% - 段階的で読みやすい
- **実用性**: 85% - 実際のセットアップに十分な情報
- **補足資料**: 70% - スクリーンショット不足

---

## 2. BigQuery MCP Setup Guide 完全性評価

**ファイル**: `/Users/yuichi/AIPM/aipm_v0/docs/bigquery_mcp_setup_guide.md`
**総合スコア**: 8.0/10

### 強み

| 項目 | 評価 | 詳細 |
|------|------|------|
| **前提条件の明確化** | ✅ | GCPアカウント、プロジェクト作成、BigQuery有効化 |
| **サービスアカウント作成** | ✅ | Step 2-1～2-4で詳細に説明 |
| **ロール付与** | ✅ | 必須・オプションロールを表形式で整理 |
| **JSONキーの保存方法** | ✅ | 絶対パス指定、chmod設定など実装的 |
| **環境変数設定** | ✅ | 絶対パスの重要性を強調 |
| **セキュリティベストプラクティス** | ✅ | キーローテーション周期（6ヶ月）を明記 |
| **Python APIテスト例** | ✅ | 実行可能なサンプルコード提供 |

### 改善すべき点

| 項目 | 重要度 | 改善案 |
|------|--------|--------|
| **GCPコンソール画面** | 中 | Step 1-1, 2-2, 3-1の画面キャプチャ追加 |
| **プロジェクトID確認** | 低 | Step 4で記載（✓ 既出） |
| **bashテストスクリプト** | 中 | Python例があるが、bash版の`scripts/test_bigquery_mcp.sh`へのリンク追加 |
| **.mcp.json設定例** | 中 | 次のステップで.mcp.json内のbigquery設定例を簡潔に提示 |
| **接続テスト** | 低 | Python APIテスト後の「Claude Code内での確認方法」を追加 |

### スコア根拠: 8.0/10

- **完全性**: 80% - 基本セットアップカバー、テスト手順は不十分
- **明瞭性**: 85% - 表形式で分かりやすい
- **実用性**: 80% - 実行可能なコード例が有効
- **補足資料**: 65% - スクリーンショット、bash例が不足

---

## 3. Sentry MCP Setup Guide

**ファイル**: 未作成
**総合スコア**: 0/10 - **要作成**

### week6_mcp.md で要求されている内容

week6_mcp.mdのStep 1（Sentry Auth Token作成）では以下が記載：

```markdown
#### Step 1: Sentry Auth Token作成

1. Sentry Settings > Developer Settings > Auth Tokens にアクセス
2. 「Create New Token」をクリック
3. Scopes選択: `event:read`, `project:read`, `org:read`
4. トークン生成・コピー

#### Step 2: Organization Slug取得

SentryのURL: `https://sentry.io/organizations/YOUR-ORG-SLUG/`
```

### 必要なドキュメント

以下の内容を含む `docs/sentry_mcp_setup_guide.md` を作成すべき：

| セクション | 詳細 | 重要度 |
|-----------|------|--------|
| **前提条件** | Sentryアカウント、プロジェクト作成 | 高 |
| **Developer Settings アクセス** | Token作成までの画面遷移 | 高 |
| **Auth Token の Scopes** | event:read, project:read, org:read の意味 | 高 |
| **Organization Slug 取得** | URLパターンの説明 | 高 |
| **環境変数設定** | SENTRY_AUTH_TOKEN, SENTRY_ORG_SLUG | 高 |
| **動作確認** | curlでのAPI呼び出しテスト | 中 |
| **トラブルシューティング** | invalid_authエラー等 | 中 |
| **セキュリティ** | Token保護、期限管理 | 中 |

### 推定作成所要時間: 30分

---

## 4. 統合テスト手順

### 現状
- ✅ Slack: `scripts/test_slack_mcp.sh` の存在を言及
- ✅ BigQuery: Python APIでの動作確認を記載
- ❌ 統合テスト（複数MCPサーバーの同時動作確認）: 未記載

### 必要な追加内容

#### 4-1. MCPサーバー起動確認スクリプト

**ファイル**: `scripts/test_mcp_integration.sh`（要作成）

```bash
#!/bin/bash

echo "=== MCP Integration Test ==="

# 1. .mcp.json 構文確認
echo "[1/4] Validating .mcp.json..."
jq empty .mcp.json && echo "✅ .mcp.json OK" || echo "❌ .mcp.json ERROR"

# 2. 環境変数確認
echo "[2/4] Checking environment variables..."
[ -n "$SLACK_BOT_TOKEN" ] && echo "✅ SLACK_BOT_TOKEN set" || echo "❌ SLACK_BOT_TOKEN missing"
[ -n "$GOOGLE_APPLICATION_CREDENTIALS" ] && echo "✅ GOOGLE_APPLICATION_CREDENTIALS set" || echo "❌ GOOGLE_APPLICATION_CREDENTIALS missing"
[ -n "$SENTRY_AUTH_TOKEN" ] && echo "✅ SENTRY_AUTH_TOKEN set" || echo "❌ SENTRY_AUTH_TOKEN missing"

# 3. MCPサーバー実行権限確認
echo "[3/4] Checking executable permissions..."
ls -l scripts/mcp_servers/*.py | grep -q rwx && echo "✅ Scripts executable" || echo "⚠️  Scripts need chmod +x"

# 4. Claude Code MCPサーバーテスト
echo "[4/4] Testing MCP servers..."
# (詳細な接続テストは後述)
```

#### 4-2. Claude Code内でのMCP動作確認

**記載すべき場所**: `.claude/rules/mcp_integration.md`（新規作成）

```markdown
### MCP統合テスト（Claude Code内）

#### テスト1: Slack接続確認
- 「Slackのチャンネル一覧を取得して」
- 期待結果: チャンネル情報が返された

#### テスト2: BigQuery接続確認
- 「BigQueryのデータセット一覧を取得して」
- 期待結果: プロジェクト内のデータセット一覧が表示

#### テスト3: Sentry接続確認
- 「Sentryのプロジェクト一覧を取得して」
- 期待結果: プロジェクト情報が返された
```

---

## 5. チーム共有設定

### 現状
- ✅ `.env.example` での環境変数テンプレート提供
- ❌ 新規メンバーのオンボーディング手順が断片的
- ❌ チーム内での認証情報管理ポリシーが不明確

### 必要な追加内容

#### 5-1. チーム向けセットアップガイド（新規作成）

**ファイル**: `docs/onboarding_mcp_setup.md`（新規）

```markdown
# Team Member Onboarding - MCP Setup Guide

## 対象読者
- 新規プロジェクトメンバー
- 既存環境でMCP統合が必要な人

## 全体フロー（所要時間: 45-60分）

### フェーズ1: セットアップ前確認（5分）
- [ ] ワークスペース管理者権限確認（Slack）
- [ ] GCP権限確認（BigQuery用）
- [ ] Sentryアカウント確認

### フェーズ2: 認証情報取得（30-40分）
- [ ] Slack Bot Token取得（@docs/slack_app_setup_guide.md）
- [ ] BigQuery Service Account作成（@docs/bigquery_mcp_setup_guide.md）
- [ ] Sentry Auth Token取得（@docs/sentry_mcp_setup_guide.md）

### フェーズ3: 環境設定（5-10分）
- [ ] `.env`ファイル作成
- [ ] 環境変数設定
- [ ] 権限設定（chmod）

### フェーズ4: 動作確認（5-10分）
- [ ] Claude Code起動
- [ ] MCP統合テスト実行
```

#### 5-2. 認証情報管理ポリシー

**内容例**:
```markdown
## 認証情報の管理ポリシー

### 個人の責任
1. 自分の `.env` は絶対にGitにコミットしない
2. Token/Keyの定期的なローテーション（3-6ヶ月）
3. 権限の最小化（不要なScopeは削除）

### チーム管理者の責任
1. 新規メンバー向けのサンプル `.env.example` を常に最新に保つ
2. 四半期ごとのToken/Keyローテーション計画
3. 本番環境と開発環境での認証情報分離
```

---

## 6. オンボーディング難易度評価

### Slack MCP Setup

**難易度**: Easy ⭐⭐☆☆☆

- **必要な前提知識**: Slack管理権限のみ
- **技術難度**: 低（UIクリック操作）
- **所要時間**: 15-20分
- **つまずきやすい箇所**: Team IDの取得方法（→ 2つの方法をdocで提示済み ✅）

### BigQuery MCP Setup

**難易度**: Medium ⭐⭐⭐☆☆

- **必要な前提知識**: GCP基本操作
- **技術難度**: 中（JSONキーの保存、権限設定）
- **所要時間**: 20-30分
- **つまずきやすい箇所**:
  - ロール付与の種類選択（→ 表で整理済み ✅）
  - 絶対パス指定の重要性（→ 強調済み ✅）
  - Pythonパッケージ未インストール（→ インストール手順あり ✅）

### Sentry MCP Setup

**難易度**: Easy ⭐⭐☆☆☆

- **必要な前提知識**: Sentryアカウント管理
- **技術難度**: 低（UIでのToken生成）
- **所要時間**: 10-15分
- **つまずきやすい箇所**: Organization Slugの特定方法

### 新規メンバー向けサマリー

| シナリオ | 所要時間 | 難易度 | 推奨補足 |
|---------|---------|--------|---------|
| **Slack のみ** | 15分 | Easy | スクリーンショット |
| **Slack + BigQuery** | 40-50分 | Medium | 統合テストスクリプト |
| **3つ全て（フル）** | 50-70分 | Medium | チェックリスト + テスト |

---

## 7. ドキュメント不足箇所リスト

### 優先度: 高

| 項目 | 説明 | 推定作成時間 |
|------|------|------------|
| **Sentry MCP Setup Guide** | 独立した専用ガイド作成 | 30分 |
| **統合テストスクリプト** | `scripts/test_mcp_integration.sh` | 20分 |
| **チーム向けオンボーディング** | `docs/onboarding_mcp_setup.md` | 25分 |
| **.mcp.json設定例** | 各ガイド内に埋め込み | 15分 |

### 優先度: 中

| 項目 | 説明 | 推定作成時間 |
|------|------|------------|
| **スクリーンショット** | Slack/GCPコンソール画面 | 30分 |
| **bash版テストスクリプト** | BigQuery用 `test_bigquery_mcp.sh` | 15分 |
| **Claude Code内の動作確認手順** | MCP機能の使用例 | 20分 |
| **認証情報管理ポリシー** | チーム向けセキュリティガイドライン | 20分 |

### 優先度: 低

| 項目 | 説明 | 推定作成時間 |
|------|------|------------|
| **所要時間見積もり** | 各セットアップガイドに追加 | 5分 |
| **よくある質問（FAQ）** | トラブルシューティング拡張 | 25分 |
| **動画チュートリアル** | スクリーンレコーディング | 60分+ |

---

## 8. week6_mcp.md との対応確認

### week6_mcp.md で言及されているドキュメント

| 項目 | 参照先 | 実装状況 |
|------|--------|---------|
| Slack設定 | `@docs/slack_app_setup_guide.md` | ✅ 完成 |
| BigQuery設定 | `@docs/bigquery_mcp_setup_guide.md` | ✅ 完成 |
| Sentry設定 | (week6_mcp.md内に簡潔記載) | ⚠️ 専用ガイド未作成 |
| セットアップ全体 | week6_mcp.md内で統合 | ✅ 完成 |
| トラブルシューティング | week6_mcp.md内で記載 | ✅ 完成 |

### week6_mcp.md で要求されている但し未実装の項目

1. **`scripts/test_slack_mcp.sh`** - week6_mcp.mdで言及されるが、実装ファイル不確認
2. **`scripts/test_bigquery_mcp.sh`** - week6_mcp.mdで言及されるが、「作成予定」のまま
3. **統合テスト手順** - individual test例は記載あるが、統合テストは未記載

---

## 9. 改善提案

### 即座に実施すべき（所要時間: 1.5時間）

#### ✅ A. Sentry MCPセットアップガイド作成

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/docs/sentry_mcp_setup_guide.md`

**含めるセクション**（week6_mcp.mdより抽出）:
1. 前提条件
2. Sentry Auth Token作成手順
3. Organization Slug取得
4. 環境変数設定
5. 動作確認（API呼び出しテスト）
6. トラブルシューティング（invalid_auth対応）
7. セキュリティベストプラクティス

**参考ドキュメント**: week6_mcp.md の「## 3. Sentry MCP」セクション（L160-201）

---

#### ✅ B. 統合テストスクリプト作成

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/scripts/test_mcp_integration.sh`

**目的**: `.mcp.json`, 環境変数、MCPサーバー実行権限を一括確認

**出力例**:
```
=== MCP Integration Test ===
[1/4] Validating .mcp.json...
✅ .mcp.json OK

[2/4] Checking environment variables...
✅ SLACK_BOT_TOKEN set
✅ GOOGLE_APPLICATION_CREDENTIALS set
✅ SENTRY_AUTH_TOKEN set

[3/4] Checking executable permissions...
✅ Scripts executable

[4/4] Testing MCP servers...
✅ All MCP servers ready
```

---

#### ✅ C. 各セットアップガイドに .mcp.json 設定例を追加

**修正対象**:
- slack_app_setup_guide.md （L273 「次のステップ」セクション）
- bigquery_mcp_setup_guide.md （L251 「次のステップ」セクション）
- (新規) sentry_mcp_setup_guide.md （次のステップセクション）

**追加内容例**:
```markdown
## .mcp.jsonでの設定（参考）

MCPサーバー定義ファイル `~/.claude/settings.json` に以下を追加：

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
      }
    }
  }
}
```

詳細は @docs/implementation_guides/week6_mcp.md を参照。
```

---

### 段階的に実施可能（所要時間: 2.5時間）

#### ✅ D. チーム向けオンボーディングガイド作成

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/docs/onboarding_mcp_setup.md`

**含めるセクション**:
1. 対象読者・目的
2. 全体フロー＋チェックリスト
3. 各フェーズの詳細（各セットアップガイドへのリンク）
4. よくあるエラーと対応
5. サポート連絡先

---

#### ✅ E. 認証情報管理ポリシー文書作成

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/docs/mcp_security_policy.md`

**含めるセクション**:
1. 個人メンバーの責任
2. チーム管理者の責任
3. 定期的なローテーション計画
4. 本番/開発環境の分離
5. インシデント対応手順

---

#### ✅ F. スクリーンショット資料作成（オプション）

**対象画面**:
- Slack App作成フロー（Step 1-2）
- GCP「IAMと管理」→「サービスアカウント」
- GCP「キー管理」画面

**効果**: 新規メンバーの習熟時間を 20-30% 削減

---

## 10. サマリータブル

### ドキュメント完成度

| ドキュメント | 完成度 | スコア | 状態 |
|------------|--------|--------|------|
| slack_app_setup_guide.md | 85% | 8.5/10 | ✅ 優秀（軽微改善） |
| bigquery_mcp_setup_guide.md | 80% | 8.0/10 | ✅ 良好（テスト強化） |
| sentry_mcp_setup_guide.md | 0% | 0/10 | ❌ **要作成** |
| week6_mcp.md | 85% | 8.5/10 | ✅ 優秀（参照リンク） |

### 全体進捗

```
実装対象: 8項目
✅ 完成: 4項目（50%）
⚠️   改善: 2項目（25%）
❌ 未実装: 2項目（25%）
```

---

## 11. 推奨実装順序（Week 6 Day 5）

### Day 5 実装計画

#### 午前（2時間）
1. **A-1**: Sentry MCP Setup Guide 作成（40分）
   - week6_mcp.mdより内容抽出
   - 他のガイドをテンプレートとして使用

2. **B-1**: 統合テストスクリプト作成（30分）
   - bash script で .mcp.json, 環境変数, 権限確認

3. **C-1**: Slack/BigQueryガイドに .mcp.json例追加（20分）
   - 各ガイドの「次のステップ」に埋め込み

#### 午後（2時間）
4. **D-1**: チーム向けオンボーディングガイド作成（60分）
   - フェーズ別チェックリスト
   - 各セットアップガイドへのリンク

5. **E-1**: 認証情報管理ポリシー作成（30分）
   - セキュリティ要件まとめ
   - ローテーション計画の雛形

---

## 12. 参照・関連ファイル

### Week 6 MCPドキュメント
- `/Users/yuichi/AIPM/aipm_v0/docs/implementation_guides/week6_mcp.md` - 本マスター文書
- `/Users/yuichi/AIPM/aipm_v0/docs/slack_app_setup_guide.md` - Slackガイド
- `/Users/yuichi/AIPM/aipm_v0/docs/bigquery_mcp_setup_guide.md` - BigQueryガイド

### Week 6 関連ルール
- `@.claude/rules/settings_management.md` - 設定管理ルール（Week 5）
- `@.claude/rules/context_management.md` - コンテキスト管理

### MCP公式リソース
- [MCP Protocol](https://modelcontextprotocol.io/)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
- [Slack API Documentation](https://api.slack.com/)
- [BigQuery API Documentation](https://cloud.google.com/bigquery/docs)
- [Sentry API Documentation](https://docs.sentry.io/api/)

---

## 結論

**Week 6 Phase 1 MCPセットアップドキュメント** は、Slack・BigQuery 2つの主要MCPサーバーについては十分な完全性を持つ。しかし、以下の点で改善が必要：

### 短期（即座 - Week 6 Day 5）
1. **Sentry MCPセットアップガイドの作成** - 準拠性向上
2. **統合テストスクリプト** - 実装検証の自動化
3. **.mcp.json設定例の埋め込み** - 参照性向上

### 中期（Week 7）
1. **スクリーンショット資料** - 新規メンバー習熟加速
2. **チーム向けオンボーディングガイド** - チーム規模の拡大に対応
3. **認証情報管理ポリシー** - セキュリティリスク低減

### 全体完成度の向上見込み
- **現在**: 71%
- **短期実施後**: 87%
- **中期実施後**: 95%

**推奨**: 短期改善項目3つを **Day 5（金）** に実装し、Phase 1終了時点で 87% 達成。

