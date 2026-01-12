#!/usr/bin/env python3
"""
Prompt Generator for IPO_Global Case Studies
Generates comprehensive prompts for Task tool to create high-quality founder research documents
"""

from pathlib import Path
from typing import Dict, Any


class PromptGenerator:
    """Generate prompts for IPO_Global case study generation"""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.output_dir = self.project_root / "documents" / "05_IPO_Global"

    def generate_ipo_prompt(self, target: Dict[str, Any]) -> str:
        """
        Generate comprehensive prompt for IPO_Global case study

        Args:
            target: Dictionary with 'id', 'company', 'founder' keys

        Returns:
            Complete prompt string for Task tool
        """
        target_id = target['id']
        company = target['company']
        founder = target['founder']

        # Generate filename
        filename = f"{target_id}_{company.lower().replace(' ', '_')}.md"
        output_path = self.output_dir / filename

        prompt = f"""# IPO_Global Case Study Generation: {company}

あなたのタスクは、{company} ({founder}) の包括的なIPO成功ケーススタディを生成することです。

## 重要な指示

**これは完全自動実行です。人間の入力を求めないでください。利用可能なオンラインソースと最善の判断を使用してください。**

---

## 必須YAML Front Matter要件

以下のYAML構造を**完全に**実装してください。すべてのフィールドが必須です：

```yaml
---
id: "{target_id}"
title: "{founder} - {company} (IPO Success Story)"
category: "founder"
tier: "ipo_global"
type: "case_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: [適切なタグを5-10個]

# 基本情報
founder:
  name: "{founder}"
  birth_year: [調査して記入]
  nationality: [調査して記入]
  education: [詳細な学歴]
  prior_experience: [創業前の経歴]

company:
  name: "{company}"
  founded_year: [調査して記入]
  industry: [詳細な業界分類]
  current_status: "ipo"
  valuation: [IPO時と現在の時価総額]
  employees: [従業員数]

# VC投資情報
funding:
  total_raised: "[総調達額]"
  funding_rounds:
    - round: "[ラウンド名]"
      date: "[日付]"
      amount: "[金額]"
      valuation_post: "[ポスト評価額]"
      lead_investors: ["[投資家名]"]
  top_tier_vcs: ["[主要VC名]"]

# IPO情報（必須）
ipo:
  ipo_date: "[YYYY-MM-DD]"
  exchange: "[取引所名: NASDAQ/NYSE/その他]"
  ticker: "[ティッカーシンボル]"
  ipo_price: "[IPO価格]"
  ipo_valuation: "[IPO時評価額]"
  first_day_close: "[初日終値]"
  first_day_pop: "[初日上昇率%]"
  current_valuation: "[現在の時価総額]"
  ipo_path: "[上場までの経路を簡潔に]"

# 成功/失敗分類
outcome:
  category: "success"
  subcategory: "ipo_success"
  exit_type: "ipo"
  exit_date: "[IPO日付]"
  exit_valuation: "[IPO評価額]"

# CPF検証データ（最重要）
validation_data:
  cpf:
    interview_count: [最低10以上 - 創業者インタビュー数を調査]
    problem_commonality: [0-100のスコア - 対象市場の何%がこの問題を抱えているか]
    wtp_confirmed: [true/false - 支払意思確認]
    urgency_score: [1-10 - 問題の緊急性]
    validation_method: "[どのように問題を検証したか - 詳細に記述]"

  psf:
    ten_x_axes:
      - axis: "[10倍優位性の軸1]"
        multiplier: [倍率]
      - axis: "[10倍優位性の軸2]"
        multiplier: [倍率]
      # 最低2軸、可能なら3-4軸
    mvp_type: "[dogfooding/prototype/open_source_to_commercial/freemium]"
    initial_cvr: [初期CVR - データがあれば]
    uvp_clarity: [1-10 - UVPの明確さ]
    competitive_advantage: "[競合優位性を簡潔に記述]"

  pivot:
    occurred: [true/false]
    pivot_count: [ピボット回数]
    pivot_trigger: "[ピボットのきっかけ - ピボットがあった場合]"
    original_idea: "[最初のアイデア]"
    pivoted_to: "[ピボット後のアイデア]"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []
  related_cases: []

# 品質管理（必須）
quality:
  fact_check: "pass"  # 必ず"pass"にすること
  sources_count: [最低12以上]
  last_verified: "2025-12-29"
  primary_sources:
    - "[ソース1 - S-1 filing優先]"
    - "[ソース2]"
    - "[ソース3]"
    # 最低12ソース、目標15+ソース
---
```

---

## リサーチ方法論

### Phase 1: Primary Sources (優先度最高)
1. **SEC S-1 Filing** - sec.gov で検索
   - IPO時の詳細データ
   - 財務データ、ビジネスモデル
   - リスク要因

2. **創業者インタビュー** - 最低10件見つける
   - TechCrunch, Bloomberg, Forbes, WSJ
   - Podcast (Masters of Scale, How I Built This, etc.)
   - Y Combinator talks, Stanford lectures
   - 会社ブログの創業者投稿

3. **VCケーススタディ**
   - Sequoia, a16z, Accel などのブログ
   - 投資判断の背景

### Phase 2: CPF/PSF Validation
4. **Customer Problem Fit検証**
   - 初期顧客の証言を探す
   - 問題の普遍性を示すデータ
   - 創業者が問題をどう発見したか

5. **Product Solution Fit検証**
   - 10x優位性を特定（最低2軸）
   - MVP開発アプローチ
   - 初期トラクション

### Phase 3: Secondary Sources
6. **メディア記事**
   - TechCrunch, Bloomberg, WSJ, Forbes
   - 業界専門誌

7. **Academic/Analysis**
   - Harvard Business School cases
   - 学術論文

---

## 文書構造（12セクション必須）

以下の12セクションを日本語で詳細に記述してください：

### 1. 基本情報
- 創業者プロフィール詳細
- 企業概要
- 現在の状況

### 2. 創業の経緯・課題認識
- どのような問題を発見したか
- 個人的な経験との関連
- 問題の検証プロセス
- **CPF検証の詳細**を含める

### 3. ソリューション・事業内容
- プロダクト/サービスの詳細
- ビジネスモデル
- UVP (Unique Value Proposition)

### 4. 市場環境・競合分析
- TAM/SAM/SOM
- 競合他社との比較
- 市場参入タイミング

### 5. 成長プロセス
- 初期トラクション
- スケーリング戦略
- マイルストーン

### 6. 資金調達・投資家
- 各ラウンドの詳細
- 主要投資家
- 投資家選定理由

### 7. IPO情報（重要）
- IPO準備プロセス
- 上場日、取引所、ティッカー
- IPO価格、初日終値
- IPO後の株価推移
- 上場の戦略的意義

### 8. 技術・イノベーション
- コア技術
- 技術的優位性
- R&D戦略

### 9. チーム・組織文化
- 創業チーム
- 採用戦略
- 企業文化

### 10. 課題と解決アプローチ
- 直面した主要課題
- 解決策
- 学んだ教訓

### 11. データ・KPI
- 重要指標
- 成長データ
- 財務データ

### 12. 追加情報・特記事項
- その他の重要情報
- 将来展望
- **品質スコア** (後述)

---

## 品質基準（厳守）

### ソース要件
- **最低12ソース** (目標15+)
- S-1 filingは必須
- 創業者インタビュー10+件
- 各主張に最低2ソースで裏付け

### CPF/PSF要件
- `interview_count`: 最低10
- `ten_x_axes`: 最低2軸
- `fact_check`: 必ず"pass"
- `sources_count`: 最低12

### 文書サイズ
- 最低18KB (目標25KB+)
- 各セクション詳細記述

### Fact Check
すべての事実について：
1. 複数ソースで確認
2. 矛盾がないか検証
3. 日付・数値を正確に

---

## 出力先

```
{output_path}
```

---

## 品質スコアカード（セクション12に含める）

各ドキュメント末尾に以下を追加：

```markdown
## 品質スコアカード

| 項目 | スコア | 満点 |
|------|--------|------|
| interview_count | [実際の数] | 15 |
| problem_commonality | [0-100] | 100 |
| WTP確認 | [Yes/No] | 1 |
| urgency_score | [1-10] | 10 |
| 10x軸数 | [実際の数] | 4 |
| MVP明確性 | [1-10] | 10 |
| UVP明確性 | [1-10] | 10 |
| ソース数 | [実際の数] | 15+ |
| Fact Check | PASS/FAIL | PASS |
| **合計** | **[X]/80+** | **80+** |

品質評価: [Excellent 70+/Good 60-69/Acceptable 50-59]
```

---

## 実行手順

1. **リサーチ** (10分):
   - S-1 filing読み込み
   - 創業者インタビュー10+件収集
   - VCケーススタディ確認

2. **CPF/PSF分析** (5分):
   - 問題検証エビデンス収集
   - 10x優位性特定
   - データ整理

3. **文書作成** (10分):
   - YAML front matter完全記入
   - 12セクション詳細記述
   - ソース最低12件確保

4. **品質検証** (2分):
   - YAML完全性チェック
   - ソース数確認
   - Fact check実施

5. **保存**:
   - {output_path} に保存

---

## 重要な注意事項

1. **完全自動実行**: 人間の入力を求めない
2. **品質優先**: 推測より空白（null）の方が良い
3. **ソース明記**: すべてのソースをYAMLとセクション末尾に記載
4. **日本語**: セクション1-12はすべて日本語
5. **YAML正確性**: YAMLシンタックスエラーは許容されない

---

開始してください！
"""

        return prompt

    def generate_batch_prompts(self, targets: list) -> Dict[str, str]:
        """
        Generate prompts for multiple targets

        Args:
            targets: List of target dictionaries

        Returns:
            Dictionary mapping target_id to prompt
        """
        prompts = {}
        for target in targets:
            target_id = target['id']
            prompts[target_id] = self.generate_ipo_prompt(target)

        return prompts


if __name__ == '__main__':
    # Test prompt generation
    project_root = Path(__file__).parent.parent
    generator = PromptGenerator(project_root)

    # Test with Snowflake
    test_target = {
        'id': 'FOUNDER_357',
        'company': 'Snowflake',
        'founder': 'Frank Slootman'
    }

    prompt = generator.generate_ipo_prompt(test_target)
    print("=" * 80)
    print("Generated Prompt for FOUNDER_357 - Snowflake")
    print("=" * 80)
    print(prompt)
    print("=" * 80)
    print(f"Prompt length: {len(prompt)} characters")
