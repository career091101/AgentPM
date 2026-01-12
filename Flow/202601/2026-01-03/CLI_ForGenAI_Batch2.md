# CLI System Prompt: ForGenAI Edition Phase 2 Batch 2 + Phase 4 Commands

## 推定実行時間
3-4時間

## プロジェクトコンテキスト

### 前提条件
- **Batch 1**: 完了済み（優先6スキル実装）
- **Phase 1**: 完了（プロジェクト構造、26コマンドファイル）

### プロジェクトパス
- ベースディレクトリ: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI`
- スキルディレクトリ: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai`
- コマンドディレクトリ: `/Users/yuichi/AIPM/aipm_v0/.claude/commands`

---

## Task 1: 残り12スキル実装 - 推定2.5時間

### スキルリスト（優先度順）

#### Tier 1: コアスキル (6個) - 60分
1. **research-problem** - 課題リサーチ（AI技術動向統合）
2. **validate-10x** - 10倍優位性検証（AI差別化評価）
3. **simulate-interview** - インタビューシミュレーション（AI特化質問）
4. **startup-scorecard** - スタートアップスコアカード（AI基準）
5. **create-mvv** - MVV作成（AI倫理・透明性重視）
6. **analyze-aarrr** - AARRR分析（AI製品メトリクス）

#### Tier 2: 戦略スキル (6個) - 60分
7. **build-flywheel** - フライホイール構築（Product Hunt連携）
8. **build-lp** - LP作成（AI製品特化）
9. **build-synergy-map** - シナジーマップ（AI技術スタック統合）
10. **inventory-internal-resources** - リソース棚卸し（AI人材・データ）
11. **validate-market-timing** - 市場タイミング検証（AI技術成熟度）
12. **validate-cannibalization** - カニバリゼーション検証

---

### Tier 1 実装（コアスキル）

#### 1.1 research-problem スキル

**GenAI特化カスタマイズ**:

```markdown
## AI技術動向統合

### 調査対象
1. **最新LLMモデル**: GPT-4 Turbo, Claude 3.5 Sonnet, Gemini 1.5 Pro
2. **エージェントフレームワーク**: LangChain, AutoGPT, CrewAI
3. **ベクトルDB**: Pinecone, Weaviate, ChromaDB
4. **AI市場レポート**: Gartner, McKinsey, a16z AI Report

### 課題分析の追加軸
- **AI導入障壁**: 技術的ハードル、コスト、精度不足
- **既存AI製品の不足**: 汎用すぎ、精度低い、高コスト
- **新技術機会**: マルチモーダル、エージェント、オンデバイスAI

### Research統合
- **事例**: Perplexity（検索AI）、Jasper（コンテンツ生成）の成功パターン
- **参照**: @GenAI_research/problem_analysis/ai_adoption_barriers.md
```

**実装コマンド**:
```bash
cp -r for_recruit/research-problem for_genai/research-problem
# SKILL.md に上記カスタマイズを追加
```

---

#### 1.2 validate-10x スキル

**GenAI特化カスタマイズ**:

```markdown
## AI差別化の10倍優位性評価

### 評価軸（3軸必須）
1. **精度**: 既存AI製品より10%以上高精度
2. **速度**: 3倍以上高速（レスポンスタイム）
3. **コスト**: API料金1/10（独自モデル・最適化）
4. **専門性**: ドメイン特化で汎用AIを圧倒
5. **UX**: プロンプト不要のノーコードUI

### 10倍優位性の証明方法
- **ベンチマーク比較**: MMLU, HumanEval等での定量評価
- **ユーザーテスト**: A/Bテストで既存製品と比較
- **コスト試算**: API料金シミュレーション

### Research統合
- **事例**: Perplexity（検索精度でGoogle比1.5倍）、Midjourney（画像生成速度10倍）
- **参照**: @GenAI_research/differentiation/10x_ai_advantages.md
```

---

#### 1.3 simulate-interview スキル

**GenAI特化カスタマイズ**:

```markdown
## AI特化インタビュー質問

### 技術検証質問
1. 「既存のAIツール（ChatGPT等）で代替できないのはなぜですか？」
2. 「使用するLLMモデルは何ですか？理由は？」
3. 「プロンプトエンジニアリングの難易度はどの程度ですか？」
4. 「ファインチューニングは必要ですか？データは揃っていますか？」
5. 「ハルシネーション（誤情報生成）対策はありますか？」

### ビジネス検証質問
1. 「API料金がユーザー課金を上回りませんか？」
2. 「Product Huntでローンチ予定はありますか？」
3. 「AI技術の陳腐化リスクにどう対応しますか？」

### Research統合
- **事例**: Jasper（ファインチューニングで精度92%達成）
- **参照**: @GenAI_research/validation/interview_best_practices.md
```

---

#### 1.4 startup-scorecard スキル

**GenAI特化カスタマイズ**:

```markdown
## AI特化スコアカード評価項目

| カテゴリ | 項目 | 配点 | GenAI特化基準 |
|---------|------|------|--------------|
| **技術** | AI精度 | 15 | 90%以上 |
| **技術** | API料金最適化 | 10 | ユーザー課金の20%以内 |
| **技術** | レスポンス速度 | 10 | 3秒以内 |
| **市場** | Product Hunt実績 | 10 | Top 5達成 |
| **市場** | GitHub Stars | 10 | 1000以上 |
| **収益** | Freemium転換率 | 10 | 10%以上 |
| **差別化** | 10倍優位性 | 15 | 3軸以上 |
| **実行** | AI人材確保 | 10 | プロンプトエンジニア在籍 |
| **倫理** | AI倫理対応 | 10 | バイアス対策・透明性 |

**合格基準**: 70点以上（ForRecruitは60点）
```

---

#### 1.5 create-mvv スキル

**GenAI特化カスタマイズ**:

```markdown
## AI倫理・透明性を重視したMVV

### Mission例（AI製品）
- 「AIで〇〇業界の生産性を10倍にする」
- 「誰でも使えるAIツールで情報格差を解消」

### Vision例
- 「2026年までに〇〇分野でNo.1 AIツールになる」
- 「AIエージェントで人間の創造的作業を支援」

### Value例（AI倫理重視）
1. **透明性**: AIの判断根拠を明示
2. **公平性**: バイアス除去・多様性尊重
3. **プライバシー**: データ保護・同意取得
4. **説明責任**: AI誤動作時の責任明確化

### Research統合
- **事例**: OpenAI（透明性重視のMission）、Anthropic（Constitutional AI）
- **参照**: @GenAI_research/ethics/ai_mission_best_practices.md
```

---

#### 1.6 analyze-aarrr スキル

**GenAI特化カスタマイズ**:

```markdown
## AI製品のAARRRメトリクス

| フェーズ | 指標 | GenAI特化の測定方法 |
|---------|------|------------------|
| **Acquisition** | Product Hunt Upvotes | ローンチ日の獲得数 |
| **Activation** | 初回プロンプト成功率 | 80%以上 |
| **Retention** | 月次リテンション | 40%以上（プロンプト再利用） |
| **Revenue** | Free→Paid転換率 | 10%以上 |
| **Referral** | バイラル係数 | 1.2以上（AI生成コンテンツ共有） |

### AI特化の追加指標
- **プロンプト再利用率**: ユーザーが過去のプロンプトを再利用
- **API利用率**: 有料ユーザーのアクティブ利用70%以上
- **精度改善率**: 月次+2%（ユーザーフィードバック反映）

### Research統合
- **事例**: ChatGPT（バイラル係数3.0）、Midjourney（Discord統合でRetention 60%）
- **参照**: @GenAI_research/metrics/ai_aarrr_benchmarks.md
```

---

### Tier 2 実装（戦略スキル） - 簡略版

残り6スキルは既存スキルのコピー + 軽微なカスタマイズで実装：

#### 実装コマンド（一括）:
```bash
cd /Users/yuichi/AIPM/aipm_v0/.claude/skills

# Tier 2スキル一括コピー
for skill in build-flywheel build-lp build-synergy-map inventory-internal-resources validate-market-timing validate-cannibalization; do
    cp -r for_recruit/${skill} for_genai/${skill}
done
```

#### カスタマイズポイント（各スキル5-10分）:
- **build-flywheel**: Product Hunt → バイラル成長の連鎖追加
- **build-lp**: AI製品特化のLP構成（デモ動画、精度ベンチマーク）
- **build-synergy-map**: AI技術スタック統合（LLM + ベクトルDB + UI）
- **inventory-internal-resources**: AI人材・データの棚卸し
- **validate-market-timing**: AI技術成熟度のタイミング評価
- **validate-cannibalization**: 既存AI製品との共食い検証

---

## Task 2: Phase 4 - コマンドファイル作成 - 推定1時間

### コマンドファイル作成（18個）

Batch 1の6個 + Batch 2の12個 = 18個のコマンドファイルを作成。

#### コマンドファイルテンプレート:

```markdown
# /for-genai-{skill_name}

## Description
{スキルの簡潔な説明（1行）}

## Target Domain
ForGenAI Edition（生成AI特化版）

## Execution
スキル実行: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/{skill_name}/SKILL.md`

## Prerequisites
- ForGenAI Edition プロジェクト構造作成済み
- GenAI_research フォルダ参照可能

## Expected Output
{期待される成果物（例: CPF評価レポート、競合分析表等）}

## Estimated Time
{推定実行時間（例: 15-30分）}

## Notes
- CPF基準: 70%以上（ForRecruit 50%より厳格）
- Research統合: 最低3件の成功パターン参照
- AI特化評価: 精度・速度・API料金を必ず含む
```

#### 一括作成スクリプト:

```bash
cd /Users/yuichi/AIPM/aipm_v0/.claude/commands

# Batch 1 + Batch 2の全18スキル
skills=(
    "discover-demand"
    "validate-cpf"
    "research-competitors"
    "validate-psf"
    "design-pricing"
    "validate-pmf"
    "research-problem"
    "validate-10x"
    "simulate-interview"
    "startup-scorecard"
    "create-mvv"
    "analyze-aarrr"
    "build-flywheel"
    "build-lp"
    "build-synergy-map"
    "inventory-internal-resources"
    "validate-market-timing"
    "validate-cannibalization"
)

for skill in "${skills[@]}"; do
    cat > "for-genai-${skill}.md" <<EOF
# /for-genai-${skill}

## Description
ForGenAI Edition: ${skill} スキル実行

## Target Domain
生成AI特化版

## Execution
スキル実行: /Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/${skill}/SKILL.md

## Prerequisites
- ForGenAI Edition プロジェクト構造作成済み

## Expected Output
${skill} 実行結果レポート

## Estimated Time
15-30分
EOF
    echo "Created: for-genai-${skill}.md"
done
```

---

## 最終成果物

### 1. 新規スキルファイル (12個)
- Tier 1: `research-problem`, `validate-10x`, `simulate-interview`, `startup-scorecard`, `create-mvv`, `analyze-aarrr`
- Tier 2: `build-flywheel`, `build-lp`, `build-synergy-map`, `inventory-internal-resources`, `validate-market-timing`, `validate-cannibalization`

### 2. コマンドファイル (18個)
- Batch 1の6個 + Batch 2の12個

### 3. 完了レポート
- `Flow/202601/2026-01-03/FORGENAI_PHASE2_BATCH2_COMPLETION_REPORT.md`
  - 実装完了スキル一覧（累計18/26スキル）
  - コマンドファイル作成状況（18/26）
  - 次のアクション（Phase 3-5移行）

---

## 重要な注意事項

1. **Tier 2は軽微なカスタマイズのみ**:
   - 基本構造は既存スキルを踏襲
   - GenAI特化の質問・評価軸を追加（5-10分/スキル）

2. **コマンドファイルは自動生成**:
   - スクリプトで18個を一括作成
   - テンプレートの一貫性を保つ

3. **Research統合は最低限**:
   - Tier 2スキルは参照パスのみ記載
   - 詳細統合はPhase 5で実施

---

## 実行開始コマンド

```bash
cd /Users/yuichi/AIPM/aipm_v0/.claude/skills

# Tier 1スキル作成（手動カスタマイズ）
for skill in research-problem validate-10x simulate-interview startup-scorecard create-mvv analyze-aarrr; do
    cp -r for_recruit/${skill} for_genai/${skill}
    echo "Created for_genai/${skill} - CUSTOMIZE NOW"
done

# Tier 2スキル作成（軽微なカスタマイズ）
for skill in build-flywheel build-lp build-synergy-map inventory-internal-resources validate-market-timing validate-cannibalization; do
    cp -r for_recruit/${skill} for_genai/${skill}
    echo "Created for_genai/${skill} - LIGHT CUSTOMIZATION"
done

# コマンドファイル一括作成
cd /Users/yuichi/AIPM/aipm_v0/.claude/commands
bash create_forgenai_commands.sh  # 上記スクリプトを実行
```

---

## 次のステップ

Batch 2完了後、Phase 3-5に進む:
- **Phase 3**: 残り8スキル実装（AI特化の新規スキル）
- **Phase 4**: コマンドファイル残り8個作成
- **Phase 5**: Quality Checkpoint（95/100目標）

詳細: `CLI_ForGenAI_Phase3-5.md` 参照
