#!/usr/bin/env python3
"""
ForSolo Tier 2 Case Studies Automated Improvement Script

自動追加要素:
1. YAML Frontmatter（標準フォーマット）
2. Solo Fit評価テンプレート（6軸）
3. Quality Scoreセクション
4. 日本市場適用セクション
5. Actionable Playbook

推定削減: 176.5時間 → 44時間（75%削減）
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Base path
BASE_PATH = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/knowledge_base/tier2_case_studies")
AUDIT_JSON_PATH = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/existing_files_quality_audit_report.json")


def load_audit_data() -> List[Dict]:
    """Load audit results from JSON"""
    with open(AUDIT_JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_yaml_frontmatter(file_path: Path, skill: str, content: str) -> str:
    """Generate YAML frontmatter based on file content"""

    # Extract existing data from content
    founder_match = re.search(r'(?:創業者|Founder)[：:]\s*([^\n]+)', content)
    founder_name = founder_match.group(1).strip() if founder_match else "Unknown"

    product_match = re.search(r'(?:プロダクト|Product)[：:]\s*([^\n]+)', content)
    product_name = product_match.group(1).strip() if product_match else file_path.stem

    # Extract MRR if present
    mrr_match = re.search(r'\$([0-9,]+)\s*(?:MRR|ARR|/mo|/month)', content)
    mrr = mrr_match.group(1) if mrr_match else "Unknown"

    # Determine category
    category = "App"  # Default
    if "newsletter" in content.lower() or "ニュースレター" in content:
        category = "Newsletter"
    elif any(keyword in content.lower() for keyword in ["twitter", "x.com", "sns", "social"]):
        category = "SNS"

    # Generate file ID
    file_id = f"TIER2_SOLO_{file_path.stem.upper()}"

    yaml = f"""---
id: "{file_id}"
title: "{product_name} - {skill.replace('-', ' ').title()}"
founder: "{founder_name}"
product: "{product_name}"
category: "{category}"
skill: "{skill}"
created: "{datetime.now().strftime('%Y-%m-%d')}"
updated: "{datetime.now().strftime('%Y-%m-%d')}"
quality_score: 0  # To be calculated
mrr: "{mrr}"
source: "Solopreneur_Research"
tags:
  - ForSolo
  - {category}
  - {skill}
solo_fit_score:
  total: 0
  tech_feasibility: 0
  skill_coverage: 0
  time_to_market: 0
  cost_efficiency: 0
  marketing_solo: 0
  support_scalability: 0
---

"""
    return yaml


def generate_solo_fit_template() -> str:
    """Generate Solo Fit evaluation template (6 axes)"""
    return """
## Solo Fit評価（ForSolo固有）

### 評価基準（6軸）

| 軸 | スコア | 評価 |
|----|-------|------|
| **技術実行可能性** | ?/10 | [フルスタック開発が1人で可能か] |
| **スキル充足度** | ?/10 | [コーディング、マーケ、CS全て対応可能か] |
| **時間確保可能性** | ?/10 | [週何時間確保できるか] |
| **コスト実現可能性** | ?/10 | [初期投資、月額コストが許容範囲か] |
| **マーケ実行可能性** | ?/10 | [Build in Public、SNS運用が実行可能か] |
| **サポート実行可能性** | ?/10 | [CS対応、コミュニティ管理が可能か] |
| **総合** | **?/60** | [判定: ✅ Solo Fit達成 / ❌ Solo Fit未達] |

### Solo Fit判定基準
- **45点以上/60点**: ✅ Solo Fit達成（1人実行可能性高）
- **30-44点**: ⚠️ Solo Fit条件付き（リソース補完が必要）
- **30点未満**: ❌ Solo Fit未達（チーム必須）

### 必須スキルチェック
- [ ] **コーディング**: フルスタック開発（フロントエンド + バックエンド）
- [ ] **マーケティング**: Build in Public、SNS運用、コンテンツ作成
- [ ] **カスタマーサポート**: 問い合わせ対応、コミュニティ管理

### 時間配分モデル（週30時間想定）
- 開発: 15時間 (50%)
- マーケティング: 9時間 (30%)
- カスタマーサポート: 6時間 (20%)

"""


def generate_quality_score_template() -> str:
    """Generate Quality Score section template"""
    return """
## Quality Score: ?/100

### スコア内訳
| 基準 | スコア | 評価 |
|------|--------|------|
| **定量データ完全性** (30点) | ?/30 | [MRR、開発期間、コスト、ユーザー数の記載率] |
| **ソース信頼性** (25点) | ?/25 | [1次ソースリンク（X/Twitter、公式サイト、Product Hunt）の有無] |
| **1人実行可能性** (30点) | ?/30 | [Solo Fit評価、必須スキル、時間配分の記載] |
| **スキルカバレッジ** (15点) | ?/15 | [対象スキルの検証ポイント網羅性] |

### 総合評価
- **95点以上**: Tier 2認定、ベンチマークケース
- **85-94点**: Tier 2合格
- **70-84点**: Tier 3（基準は満たすが改善余地あり）
- **70点未満**: 不合格（再作成）

### 改善推奨ポイント
- [ ] MRR、開発期間、初期投資の定量データ追加
- [ ] X/Twitter、Product Hunt等の1次ソースリンク追加
- [ ] Solo Fit 6軸評価の詳細化
- [ ] スキル固有の検証ポイント強化

"""


def generate_japan_market_template() -> str:
    """Generate Japan Market Adaptation template"""
    return """
## 日本市場適用

### 文化的適応
日本市場で本事例を適用する際の調整ポイント:

1. **言語・ローカライゼーション**
   - UI/UX: 日本語対応必須（機械翻訳ではなくネイティブレビュー）
   - カスタマーサポート: 日本語対応（英語のみは避ける）
   - マーケティング: 日本語コンテンツ作成（X/Twitter、ブログ等）

2. **決済・価格設定**
   - クレジットカード: JCB対応追加
   - 価格表示: 税込表示（消費税10%）
   - 決済手段: 銀行振込、コンビニ決済の検討

3. **マーケティングチャネル**
   - SNS: X/Twitter中心（70%）、LinkedIn補完（20%）、Facebook/Instagram（10%）
   - Build in Public: 日本では慎重（失敗の公開に抵抗あり）
   - コミュニティ: Slack/Discord活用（日本語チャンネル）

4. **タイムライン調整**
   - フォロワー獲得: 米国の1.5倍時間（日本市場は保守的）
   - PMF達成: 米国の1.2-1.5倍時間
   - MRR成長: 米国比80%ペース（市場規模差）

### 推奨アプローチ（日本）

#### Phase 1: 市場参入（0-3ヶ月）
1. **ローカライゼーション**
   - [ ] UI/UX日本語化（ネイティブチェック）
   - [ ] 日本語サポートドキュメント作成
   - [ ] 価格設定（税込表示、円建て）

2. **初期マーケティング**
   - [ ] X/Twitterアカウント作成（日本語）
   - [ ] Product Hunt Japan対応検討
   - [ ] 日本語ランディングページ作成

3. **決済対応**
   - [ ] Stripe日本対応（JCB追加）
   - [ ] 銀行振込オプション検討

#### Phase 2: 成長加速（4-12ヶ月）
1. **コミュニティ構築**
   - [ ] Slack/Discord日本語チャンネル
   - [ ] 定期的な日本語コンテンツ発信（週2-3回）

2. **ローカルパートナーシップ**
   - [ ] 日本のインフルエンサー協業
   - [ ] コミュニティイベント参加

#### Phase 3: スケール（12ヶ月以降）
1. **法人対応**
   - [ ] 請求書発行対応
   - [ ] 法人向け機能追加

2. **マーケット拡大**
   - [ ] 日本特有のニーズ対応
   - [ ] 競合との差別化強化

### 成功事例（日本市場）
- [日本市場で成功した類似事例を追記]

### 注意点
- Build in Publicは日本では慎重に（失敗談は控えめに）
- 価格設定は米国の80-120%が適正（購買力平価考慮）
- サポート品質重視（日本はCS品質要求が高い）

"""


def generate_playbook_template(skill: str) -> str:
    """Generate Actionable Playbook template"""
    return f"""
## 実行可能なPlaybook（{skill}）

### Week 1-2: 準備フェーズ
- [ ] タスク1: [具体的なアクション]
- [ ] タスク2: [具体的なアクション]
- [ ] タスク3: [具体的なアクション]
- [ ] マイルストーン: [Week 1-2終了時の達成目標]

### Week 3-4: 実装フェーズ
- [ ] タスク4: [具体的なアクション]
- [ ] タスク5: [具体的なアクション]
- [ ] タスク6: [具体的なアクション]
- [ ] マイルストーン: [Week 3-4終了時の達成目標]

### Month 2-3: 成長フェーズ
- [ ] タスク7: [具体的なアクション]
- [ ] タスク8: [具体的なアクション]
- [ ] タスク9: [具体的なアクション]
- [ ] マイルストーン: [Month 2-3終了時の達成目標]

### Month 4-6: スケールフェーズ
- [ ] タスク10: [具体的なアクション]
- [ ] タスク11: [具体的なアクション]
- [ ] タスク12: [具体的なアクション]
- [ ] マイルストーン: [Month 4-6終了時の達成目標]

### 成功基準
- [ ] 定量目標1: [具体的な数値目標]
- [ ] 定量目標2: [具体的な数値目標]
- [ ] 定性目標1: [具体的な状態目標]

### リスクと緩和策
| リスク | 確率 | 影響 | 緩和策 |
|--------|------|------|--------|
| [リスク1] | [高/中/低] | [高/中/低] | [対策] |
| [リスク2] | [高/中/低] | [高/中/低] | [対策] |

"""


def improve_file(file_path: Path, audit_result: Dict) -> bool:
    """Improve a single file by adding missing elements"""

    try:
        # Read current content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        skill = audit_result["skill"]
        elements = audit_result["elements"]

        # Build improved content
        improved_content = ""

        # 1. Add YAML Frontmatter if missing
        if not elements["yaml_frontmatter"]["present"]:
            improved_content = generate_yaml_frontmatter(file_path, skill, content)
            # Remove old content's YAML if exists
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
        else:
            # Extract existing YAML
            yaml_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
            if yaml_match:
                improved_content = yaml_match.group(1)
                content = content[len(improved_content):]

        # Add main content
        improved_content += content

        # 2. Add Solo Fit evaluation if missing
        if not elements["solo_fit_evaluation"]["present"]:
            # Insert before References or at the end
            if "## References" in improved_content or "## 参照" in improved_content:
                improved_content = re.sub(
                    r'(## References|## 参照)',
                    generate_solo_fit_template() + r'\n\1',
                    improved_content
                )
            else:
                improved_content += "\n" + generate_solo_fit_template()

        # 3. Add Quality Score section if missing
        if not elements["quality_score_section"]["present"]:
            if "## References" in improved_content or "## 参照" in improved_content:
                improved_content = re.sub(
                    r'(## References|## 参照)',
                    generate_quality_score_template() + r'\n\1',
                    improved_content
                )
            else:
                improved_content += "\n" + generate_quality_score_template()

        # 4. Add Japan Market Adaptation if missing
        if not elements["japan_market_adaptation"]["present"]:
            if "## References" in improved_content or "## 参照" in improved_content:
                improved_content = re.sub(
                    r'(## References|## 参照)',
                    generate_japan_market_template() + r'\n\1',
                    improved_content
                )
            else:
                improved_content += "\n" + generate_japan_market_template()

        # 5. Add Playbook if missing
        if not elements["playbook"]["present"]:
            if "## References" in improved_content or "## 参照" in improved_content:
                improved_content = re.sub(
                    r'(## References|## 参照)',
                    generate_playbook_template(skill) + r'\n\1',
                    improved_content
                )
            else:
                improved_content += "\n" + generate_playbook_template(skill)

        # 6. Ensure References section exists
        if "## References" not in improved_content and "## 参照" not in improved_content:
            improved_content += "\n\n## References\n\n- Source: `@Solopreneur_Research/documents/[元データパス]`\n- [1次ソースリンクをここに追加]\n"

        # Write improved content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(improved_content)

        return True

    except Exception as e:
        print(f"❌ Error improving {file_path}: {e}")
        return False


def main():
    """Main improvement execution"""
    print("ForSolo Tier 2 自動改善スクリプト開始...")

    # Load audit data
    audit_data = load_audit_data()
    print(f"監査データ読み込み: {len(audit_data)}件")

    # Filter files that need improvement (score < 95)
    files_to_improve = [item for item in audit_data if item["total_score"] < 95]
    print(f"改善対象ファイル: {len(files_to_improve)}件")

    # Improve files by priority
    improved_count = 0
    failed_count = 0

    # Sort by priority (high -> medium -> low)
    priority_order = {"高": 0, "中": 1, "低": 2}
    files_to_improve.sort(key=lambda x: priority_order.get(x["priority"], 3))

    for i, item in enumerate(files_to_improve, 1):
        file_path = BASE_PATH / item["file"]
        priority = item["priority"]
        score = item["total_score"]

        print(f"\n改善中 ({i}/{len(files_to_improve)}): {item['file']}")
        print(f"  優先度: {priority} | 現在スコア: {score}")

        if improve_file(file_path, item):
            improved_count += 1
            print(f"  ✅ 改善完了")
        else:
            failed_count += 1
            print(f"  ❌ 改善失敗")

    # Summary
    print(f"\n{'='*60}")
    print(f"自動改善完了")
    print(f"{'='*60}")
    print(f"✅ 成功: {improved_count}件")
    print(f"❌ 失敗: {failed_count}件")
    print(f"\n次のステップ:")
    print(f"1. 改善ファイルの手動レビュー（定量データ、1次ソースリンク追加）")
    print(f"2. Solo Fit評価の具体的スコア入力")
    print(f"3. Quality Scoreの再計算")
    print(f"4. 再監査スクリプト実行")


if __name__ == "__main__":
    main()
