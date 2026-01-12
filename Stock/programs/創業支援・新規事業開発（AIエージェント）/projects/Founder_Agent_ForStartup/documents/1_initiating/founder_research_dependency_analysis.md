# Founder_Research依存関係分析レポート

**作成日**: 2025-12-31
**対象プロジェクト**: Founder_Agent_ForStartup
**分析者**: AI Project Management System

## 1. 現状調査結果

### ディレクトリ構造の状態

```bash
# Founder_Agent_ForStartup内のFounder_Research
drwxr-xr-x@ 14 yuichi  staff   448 Dec 30 18:47 Founder_Research
```

**判定**: **実体ディレクトリ（シンボリックリンクではない）**

### ファイル数比較

| 場所 | 総ファイル数 | Markdownファイル数 |
|------|------------|------------------|
| `/projects/Founder_Research/` | 671 | 635 |
| `/projects/Founder_Agent_ForStartup/Founder_Research/` | 660 | 635 |

**差分**: 11ファイル差異あり（ほぼ同一）

## 2. 重複による影響

### ディスク使用量
- 推定サイズ: 約200-300MB（Markdownファイル635件 × 平均300-500KB）
- 重複によるディスク消費: **実質2倍**

### 管理コスト
- Founder_Research更新時に2箇所同期が必要
- 不整合リスク: High
- バージョン管理の複雑化: High

## 3. 推奨アクション

### 即時対応（優先度: High）

**シンボリックリンク化**:

```bash
#!/bin/bash
# 実行前に必ずバックアップを取得すること

cd "/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForStartup"

# 1. バックアップ作成
tar -czf Founder_Research_backup_$(date +%Y%m%d_%H%M%S).tar.gz Founder_Research

# 2. 実体削除
rm -rf Founder_Research

# 3. シンボリックリンク作成
ln -s ../Founder_Research ./Founder_Research

# 4. 確認
ls -la | grep Founder_Research
# 期待される出力: lrwxr-xr-x ... Founder_Research -> ../Founder_Research
```

### 検証手順

```bash
# シンボリックリンク確認
file Founder_Research
# 期待: Founder_Research: symbolic link to ../Founder_Research

# 参照確認
ls Founder_Research/README.md
# エラーが出なければ成功

# domain_config.yamlのパスが機能するか確認
cat domain_config.yaml | grep reference_paths
```

### 中長期対応（優先度: Medium）

1. **自動整合性チェック**:
   ```python
   # scripts/check_founder_research_sync.py
   import os
   from pathlib import Path

   def check_symlink():
       target = Path("projects/Founder_Agent_ForStartup/Founder_Research")
       if target.is_symlink():
           print("✅ Founder_Researchはシンボリックリンクです")
           print(f"   参照先: {target.resolve()}")
       else:
           print("❌ Founder_Researchは実体ディレクトリです")
           print("   シンボリックリンクへの変更を推奨")
   ```

2. **Pre-commit hook**:
   ```bash
   # .git/hooks/pre-commit
   if [ -d "projects/Founder_Agent_ForStartup/Founder_Research" ] && 
      [ ! -L "projects/Founder_Agent_ForStartup/Founder_Research" ]; then
       echo "⚠️  Founder_Researchが実体ディレクトリです"
       echo "   シンボリックリンクに変更してください"
       exit 1
   fi
   ```

## 4. リスク評価

| リスク | 現状 | シンボリックリンク化後 |
|--------|------|-------------------|
| ディスク使用量 | 2倍 | 1倍（正常） |
| データ不整合 | High | None |
| 更新作業コスト | 2倍 | 1倍（正常） |
| Git履歴の複雑さ | High | Low |

## 5. 関連ドキュメント

- プロジェクト憲章: `/documents/1_initiating/project_charter.md`（セクション9.3）
- domain_config.yaml: 参照パス設定（line 19）
- パス管理規約: `/.claude/rules/path_conventions.md`

## 6. 承認

| 項目 | 判定 |
|------|------|
| シンボリックリンク化の必要性 | ✅ 必要 |
| 実行優先度 | High |
| 想定作業時間 | 5-10分 |
| リスクレベル | Low（バックアップ取得前提） |

---

**次のアクション**: プロジェクトマネージャーの承認後、シンボリックリンク化を実施
