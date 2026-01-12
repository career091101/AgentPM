# 5CLI並列実行ガイド - 500件完全達成

**作成日**: 2025-12-29
**目標**: 5つのClaude Code CLIで並列実行し、残り321件を完成させる
**推定時間**: 5-7時間

---

## 🚀 クイックスタート

### 0. 完全自動で起動（Human介入なし）

5つのCLI（タスクリスト）を最大5並列で自動実行する場合は、以下を実行:

```bash
cd /Users/yuichi/AIPM
python3 aipm_v0/Flow/202512/2025-12-29/auto_batch_parallel_executor.py --max-concurrent-agents 5
```

### 1. 5つのターミナルを開く

```bash
# Terminal 1 (CLI-1)
cd /Users/yuichi/AIPM/aipm_v0
claude

# Terminal 2 (CLI-2)
cd /Users/yuichi/AIPM/aipm_v0
claude

# Terminal 3 (CLI-3)
cd /Users/yuichi/AIPM/aipm_v0
claude

# Terminal 4 (CLI-4)
cd /Users/yuichi/AIPM/aipm_v0
claude

# Terminal 5 (CLI-5)
cd /Users/yuichi/AIPM/aipm_v0
claude
```

### 2. 監視ダッシュボード起動 (別ターミナル)

```bash
# Terminal 6 (監視専用)
cd /Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-29
watch -n 30 python3 monitor_all_cli.py
```

### 3. 各CLIでタスクを開始

**CLI-1** (Terminal 1):
```
@Flow/202512/2025-12-29/cli1_vc_backed_tasks.md を読み込んで、
このタスクリストの全64件を並列バッチで実行してください。
```

**CLI-2** (Terminal 2):
```
残り4つのCLI用タスクリストを作成してから開始します
(このメッセージの後に作成します)
```

---

## 📋 各CLI担当内訳

| CLI | 担当 | ファイル数 | 難易度 | 推定時間 |
|-----|------|------------|--------|----------|
| CLI-1 | VC_Backed + IPO_Global Part1 | 64件 | 中 | 4-5h |
| CLI-2 | Pivot + IPO_Global Part2 + IPO_Japan Part1 | 64件 | 高 | 5-6h |
| CLI-3 | Failure + IPO_Japan Part2 | 64件 | 高 | 5-6h |
| CLI-4 | Emerging Part1 (1-66) | 66件 | 中-高 | 5-6h |
| CLI-5 | Emerging Part2 (67-150) | 75件 | 中-高 | 6-7h |
| **合計** | | **333件** | | **5-7h** |

---

## ⚙️ 実行設定 (全CLI共通)

### 品質基準

```yaml
quality_standards:
  fact_check_pass_rate: 100%
  min_sources: 12
  target_score: 85+
  null_completion: 100%
```

### 並列実行設定

```yaml
parallel_config:
  concurrent_agents: 10-15
  retry_on_failure: true
  max_retries: 3
  delay_between_tasks: 2秒
```

### Research Guidelines準拠

```yaml
compliance:
  - null補完必須 (推定値+コメント)
  - ソース12件以上
  - Fact Check全件PASS
  - orchestrate-phase1示唆記載
```

---

## 📊 進捗チェックポイント

### 1時間後 (期待: 10-15件/CLI)

```bash
# 各CLIで実行
現在の進捗を報告してください:
- 完了件数
- 平均実行時間
- エラー件数
```

### 3時間後 (期待: 30-40件/CLI)

```bash
# 遅延しているCLIで実行
並列数を15に増やして残りタスクを実行してください
```

### 5時間後 (期待: 50-60件/CLI)

```bash
# 各CLIで実行
残り件数と推定完了時刻を報告してください
```

---

## 🛠️ トラブルシューティング

### 問題: CLIが遅延している

**確認**:
```
現在何件完了していますか？予定より遅れていますか？
```

**対応**:
```
並列数を20に増やして、残りタスクを高速実行してください
```

### 問題: メモリ不足エラー

**対応**:
```
並列数を5に減らして、メモリ使用量を抑えて実行してください
```

### 問題: API Rate Limit

**対応**:
```
各タスク間に5秒の待機時間を入れて、Rate Limitを回避してください
```

### 問題: 情報不足 (Emerging企業)

**ガイドライン**:
```yaml
conservative_estimation:
  interview_count: 0  # データなしは0
  problem_commonality: 20-30%  # 保守的推定
  sources: Twitter, ProductHunt, Crunchbase活用
  wtp_confirmed: false  # 不明はfalse
```

---

## ✅ 完了チェックリスト

### 各CLI完了時

- [ ] 割り当てファイル100%作成
- [ ] 品質チェック実行
- [ ] 平均スコア80+確認
- [ ] Fact Check Pass率95%+確認
- [ ] Git commit実行

### 全CLI完了後

- [ ] 監視ダッシュボードで500件確認
- [ ] 統合品質チェック実行
- [ ] 最終レポート生成
- [ ] Git統合コミット
- [ ] 完了報告作成

---

## 🎯 成功条件

### 必須条件

✅ **総ファイル数500件達成**
✅ **Fact Check Pass率100%**
✅ **平均品質スコア85+**
✅ **Null完全補完率100%**

### 理想条件

🎖️ **実行時間5時間以内**
🎖️ **全CLIエラー0件**
🎖️ **Grade A率50%以上**

---

## 📝 次のステップ

### 1. 残り4つのタスクリスト作成

CLI-2, CLI-3, CLI-4, CLI-5用のタスクリストを作成します。

### 2. 実行開始

全てのCLIで同時にタスクを開始します。

### 3. 監視

監視ダッシュボードで進捗を追跡します。

### 4. 完了

全CLI完了後、統合品質チェックを実行します。

---

## 📞 サポート

### エラー発生時

```
エラーが発生しました。以下を確認してください:
1. エラーメッセージ
2. 発生したタスク (Founder ID)
3. 試行回数
```

### 質問・相談

```
不明な点があれば、いつでも質問してください。
並列実行を中断せずに対応します。
```

---

**準備完了！** 5つのターミナルでClaude Codeを起動し、各CLIでタスクを開始してください。

---

**作成者**: Claude Code (Sonnet 4.5)
**最終更新**: 2025-12-29 12:10
**ステータス**: ✅ 実行準備完了
