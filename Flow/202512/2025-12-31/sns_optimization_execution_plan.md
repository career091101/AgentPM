# SNSフォルダ最適化 並列実行プラン

## エージェント並列実行戦略

### 推奨並列数: **3-4エージェント**

**理由:**
- Claude Code APIのレート制限を考慮
- ファイルシステムI/O競合の回避
- メモリ使用量の最適化
- エラー発生時のトラブルシューティング容易性

### 推奨モデル・設定

| Phase | モデル | Thinking | 理由 |
|-------|--------|----------|------|
| Phase 1 | haiku | Off | 構造作成のみ（定型作業） |
| Phase 2 | sonnet | On | コンテンツ分析・価値判断が必要 |
| Phase 3 | haiku | Off | 改名・削除（定型作業） |
| Phase 4 | haiku | Off | 確認・削除（定型作業） |

### 実行時間目安

| Phase | 予想時間 | タスク |
|-------|----------|--------|
| Phase 1 | 8-12分 | フォルダ構造作成（7プラットフォーム × 2フォルダ + sources/） |
| Phase 2 | 20-30分 | 1.1GBのコンテンツ移動・分析・統合 |
| Phase 3 | 4-6分 | 改名・プラットフォームフォルダ削除 |
| Phase 4 | 2-3分 | 移行確認・SNSノウハウ削除 |
| **合計** | **34-51分** | - |

※ API応答速度やファイルI/Oにより変動

## バッチ実行設計

### バッチ1: Phase 1 - 構造準備（並列3エージェント）

**エージェント1: 基本構造作成**
```
タスク:
- TikTok/, YouTube/フォルダ作成（algorithm.md, best_practices.mdテンプレート）
- sources/フォルダ作成
- sources/affiliateman/, sources/あずさメソッド/準備
```

**エージェント2: 既存拡張グループA**
```
タスク:
- X/にcase_studies/, resources/追加
- Instagram/にcase_studies/, resources/追加
- TikTok/にcase_studies/, resources/追加
```

**エージェント3: 既存拡張グループB**
```
タスク:
- LinkedIn/にcase_studies/, resources/追加
- Note/にcase_studies/, resources/追加
- Facebook/にcase_studies/, resources/追加
- YouTube/にcase_studies/, resources/追加
```

### バッチ2: Phase 2 - コンテンツ移行（並列4エージェント）

**エージェント4: affiliateman移行**
```
タスク:
- affiliatemanフォルダ全体をSNS_Knowledge/sources/に移動
- 移動完了確認
```

**エージェント5: あずさメソッド移行**
```
タスク:
- あずさメソッドフォルダをSNS_Knowledge/sources/に移動
- 移動完了確認
```

**エージェント6: X/Instagram/TikTokコンテンツ統合**
```
タスク:
- affiliateman/blog/twitter → X/resources/に反映
- affiliateman/video_transcripts/twitter_* → X/case_studies/に抽出
- affiliateman/blog/instagram → Instagram/resources/に反映
- affiliateman/video_transcripts/instagram_* → Instagram/case_studies/に抽出
- affiliateman/blog/tiktok → TikTok/resources/に反映
- affiliateman/video_transcripts/tiktok_* → TikTok/case_studies/に抽出
```

**エージェント7: その他プラットフォーム統合**
```
タスク:
- affiliateman/interviews → 各プラットフォームのcase_studies/に分類
- affiliateman/zoom_consult → 各プラットフォームのcase_studies/に分類
- あずさメソッド → Note/case_studies/に反映
```

### バッチ3: Phase 3 - SNSフォルダ整理（並列3エージェント）

**エージェント8: SNS改名とREADME更新**
```
タスク:
- SNS/をSNS_Practice/に改名
- README.mdを更新（新構造の説明）
```

**エージェント9: プラットフォームフォルダ削除**
```
タスク:
- SNS_Practice/X/, Instagram/, TikTok/, LinkedIn/, Note/, Facebook/, YouTube/, General/を削除
- documents/2_discovery/配下のプラットフォームフォルダを整理
```

**エージェント10: experiments/フォルダ新設**
```
タスク:
- SNS_Practice/experiments/フォルダ作成
- experiments/README.mdとテンプレート作成
```

### バッチ4: Phase 4 - 最終確認と削除（1エージェント）

**エージェント11: 移行確認と削除**
```
タスク:
- 移行完了確認（ファイル数・サイズ検証）
- SNSノウハウ/フォルダ削除
- 最終レポート生成
```

## 実行コマンド例

### バッチ1実行
```
Task tool × 3（並列）
- agent_1_phase1_base_structure
- agent_2_phase1_expand_groupA
- agent_3_phase1_expand_groupB
```

### バッチ2実行（バッチ1完了後）
```
Task tool × 4（並列）
- agent_4_phase2_affiliateman_migration
- agent_5_phase2_azusa_migration
- agent_6_phase2_content_integration_main
- agent_7_phase2_content_integration_other
```

### バッチ3実行（バッチ2完了後）
```
Task tool × 3（並列）
- agent_8_phase3_rename
- agent_9_phase3_cleanup
- agent_10_phase3_experiments
```

### バッチ4実行（バッチ3完了後）
```
Task tool × 1
- agent_11_phase4_final_verification
```

## モニタリング戦略

各バッチ実行後、以下を確認：
1. **エラーログチェック**: 各エージェントの実行ログ確認
2. **ファイル整合性**: 移行前後のファイル数・サイズ比較
3. **次バッチ実行可否判断**: エラーがあれば修正後に次バッチ実行

## リスク管理

### リスク1: ファイル移動中のデータロス
- **対策**: 移動前に`du -sh`でサイズ記録、移動後に検証

### リスク2: エージェント間のファイル競合
- **対策**: バッチ設計で同一ファイルへの同時アクセスを回避

### リスク3: API制限によるエージェント失敗
- **対策**: 失敗したエージェントのみ再実行可能な設計

## 実行準備チェックリスト

- [ ] 現在のSNSフォルダ構造をバックアップ
- [ ] `du -sh`で各フォルダサイズを記録
- [ ] git statusで未コミット変更を確認
- [ ] 実行中は他の操作を控える

## 実行開始確認

準備が整いましたら、バッチ1から順次実行します。
実行を開始してよろしいですか？
