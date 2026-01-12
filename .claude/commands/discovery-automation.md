# Discovery Automation Command

**コマンド**: `/discovery-automation`

**説明**: インタビュー記録の自動分析、ペルソナ・仮説マップ・ジャーニーマップの差分更新を実行

**エージェント**: Discovery Automation Agent

---

## 使用方法

```
/discovery-automation
```

または

```
インタビュー分析を実行してください
```

---

## 実行内容

1. **インタビュー記録の読み込み**: `Flow/YYYYMM/YYYY-MM-DD/interview_*.md` を自動検出
2. **パターン抽出**: 共通する課題・ニーズ・行動パターンを抽出
3. **ペルソナ更新**: 既存ペルソナに新たな気づきを差分追加
4. **仮説マップ更新**: 検証済み仮説をマーク、新規仮説を追加
5. **ジャーニーマップ更新**: 新たなタッチポイント・感情変化を反映
6. **インサイトレポート生成**: Top 3-5発見事項をサマリー

---

## 入力パラメータ（対話形式で質問）

### 必須パラメータ

1. **インタビューファイルの場所**:
   - 質問: 「インタビューファイルのディレクトリパスを教えてください」
   - 例: `Flow/202601/2026-01-02/`
   - デフォルト: 最新の `Flow/YYYYMM/YYYY-MM-DD/` ディレクトリ

2. **分析モード**:
   - 質問: 「分析モードを選択してください（quick / standard / deep）」
   - quick: 10分速読、主要パターンのみ抽出
   - standard: 30分標準、詳細分析（推奨）
   - deep: 60分精読、深い洞察と相関関係分析
   - デフォルト: `standard`

### オプションパラメータ

3. **既存ペルソナパス**（差分更新時）:
   - 質問: 「既存のペルソナドキュメントのパスを教えてください（スキップ可）」
   - 例: `Stock/programs/.../documents/2_discovery/persona.md`
   - デフォルト: なし（新規作成）

4. **既存仮説マップパス**（差分更新時）:
   - 質問: 「既存の仮説マップのパスを教えてください（スキップ可）」
   - 例: `Stock/programs/.../documents/2_discovery/hypothesis_map.md`
   - デフォルト: なし（新規作成）

5. **既存ジャーニーマップパス**（差分更新時）:
   - 質問: 「既存のジャーニーマップのパスを教えてください（スキップ可）」
   - 例: `Stock/programs/.../documents/2_discovery/user_journey_map.md`
   - デフォルト: なし（新規作成）

6. **Researchドメイン**:
   - 質問: 「Researchドメインを選択してください（for_solo / for_recruit / for_genai / for_startup）」
   - デフォルト: `for_solo`

7. **最小パターン頻度**:
   - 質問: 「パターン抽出の最小頻度を設定してください（デフォルト: 3）」
   - デフォルト: `3`（3名以上が言及したパターンのみ抽出）

8. **検証閾値**:
   - 質問: 「仮説検証の信頼度閾値を設定してください（デフォルト: 0.7）」
   - デフォルト: `0.7`（70%以上の共感率で「検証済み」）

---

## 出力ファイル

```
Flow/YYYYMM/YYYY-MM-DD/discovery_output/
├── persona_updated.md          # 更新されたペルソナ（差分マーク付き）
├── hypothesis_map_updated.md   # 更新された仮説マップ
├── journey_map_updated.md      # 更新されたジャーニーマップ
├── insights_report.md          # インサイトレポート
└── pattern_analysis.json       # 抽出パターン（機械可読形式）
```

---

## 実行例

### 例1: 新規プロジェクトでのインタビュー分析

```
ユーザー: /discovery-automation

エージェント: インタビューファイルのディレクトリパスを教えてください
ユーザー: Flow/202601/2026-01-02/

エージェント: 分析モードを選択してください（quick / standard / deep）
ユーザー: standard

エージェント: 既存のペルソナドキュメントのパスを教えてください（スキップ可）
ユーザー: [Enter]（スキップ）

エージェント: Researchドメインを選択してください（for_solo / for_recruit / for_genai / for_startup）
ユーザー: for_solo

エージェント: 分析を開始します...

[30分後]

エージェント: 分析が完了しました。以下のファイルを生成しました:
- persona_updated.md: 新規ペルソナ「タナカ ケンジ（32歳・会社員）」
- hypothesis_map_updated.md: 仮説8件（うち検証済み3件）
- journey_map_updated.md: ジャーニー5フェーズ
- insights_report.md: Top 3発見事項
- pattern_analysis.json: パターン8件抽出

インサイトレポートを表示しますか？
```

### 例2: 既存ドキュメントの差分更新

```
ユーザー: インタビュー分析を実行してください

エージェント: インタビューファイルのディレクトリパスを教えてください
ユーザー: Flow/202601/2026-01-03/

エージェント: 分析モードを選択してください（quick / standard / deep）
ユーザー: deep

エージェント: 既存のペルソナドキュメントのパスを教えてください（スキップ可）
ユーザー: Stock/programs/.../documents/2_discovery/persona.md

エージェント: 既存の仮説マップのパスを教えてください（スキップ可）
ユーザー: Stock/programs/.../documents/2_discovery/hypothesis_map.md

エージェント: Researchドメインを選択してください
ユーザー: for_genai

エージェント: 分析を開始します...

[60分後]

エージェント: 分析が完了しました。差分更新を実施しました:
- persona_updated.md: 5箇所更新（通勤時間、継続率データ追加等）
- hypothesis_map_updated.md: 新規仮説3件追加、検証済み2件マーク
- insights_report.md: Top 5発見事項（Product Hunt戦略含む）

ForGenAI Researchとの照合結果:
- Product Hunt #1獲得戦略との整合性: ✅ 高
- プロンプトエンジニアリング適用箇所: 3件特定
```

---

## 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| 分析速度 | < 5分/インタビュー | 実行時間 |
| ペルソナ更新精度 | 人間レビュー合格率 > 80% | Review Agentスコア |
| パターン抽出数 | 平均5-10件/インタビュー | pattern_analysis.json |
| 仮説検証率 | > 60% | 検証済み仮説 / 全仮説 |

---

## 参照

- **エージェント仕様**: `@.claude/agents/discovery-automation-agent.md`
- **Research統合**:
  - ForSolo: `@Solopreneur_Research/documents/01_App/case_studies/`
  - ForRecruit: `@Recruit_Product_Research/`
  - ForGenAI: `@GenAI_research/`
- **並列実行**: `@.claude/rules/parallel_execution.md`

---

**作成日**: 2026-01-03
**Week 2実装**: Discovery Automation Agent（P0）
