# プロジェクト憲章チェックリスト

**作成日**: 2025-12-31
**対象**: Stock/programs配下の全アクティブプロジェクト

---

## ✅ 憲章が存在するプロジェクト（17件）

### 副業プログラム（3件）
1. ✅ **Nexus** - `project_charter.md`
2. ✅ **SNS** - `documents/1_initiating/project_charter.md`
3. ✅ **SNSノウハウ** - `documents/1_initiating/project_charter.md`

### 創業支援・新規事業開発（AIエージェント）プログラム（10件）
4. ✅ **Corporate_Product_Research** - `documents/1_initiating/project_charter.md`
5. ✅ **Founder_Agent_ForGenAI** - `documents/1_initiating/project_charter.md`
6. ✅ **Founder_Agent_ForRecruit** - `documents/1_initiating/project_charter.md`
7. ✅ **Founder_Agent_ForSolo** - `documents/1_initiating/project_charter.md`
8. ✅ **Founder_Agent_ForStartup** - `documents/1_initiating/project_charter.md`
9. ✅ **Founder_Agent_Origin** - `documents/1_initiating/project_charter.md`
10. ✅ **Founder_Agent_Phase1** - `documents/1_initiating/project_charter.md`
11. ✅ **Founder_Research** - `documents/1_initiating/project_charter.md`
12. ✅ **corporate-ai-adoption-failure** - `documents/1_initiating/project_charter.md`
13. ✅ **ideal_partner_matching** - `documents/1_initiating/project_charter.md`

### 資産運用プログラム（4件）
14. ✅ **Merriman Financial Astrology Analysis** - `documents/1_initiating/project_charter.md`
15. ✅ **TradingAgents** - `documents/1_initiating/project_charter.md`
16. ✅ **エリオット波動分析** - `documents/1_initiating/project_charter.md`
17. ✅ **統合分析** - `documents/1_initiating/project_charter.md`

---

## ❌ 憲章が未作成のプロジェクト（3件）

### 副業プログラム（1件）
1. ❌ **affiliateman**
   - パス: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman`
   - 優先度: 低
   - 理由: ideasプロジェクト配下のサブプロジェクト的な位置づけ

### 創業支援・新規事業開発（AIエージェント）プログラム（2件）
2. ❌ **ideas**
   - パス: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/ideas`
   - 優先度: 低
   - 理由: アイデア保管庫的な位置づけ、正式プロジェクト化前の段階

3. ❌ **solo_ideas**
   - パス: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/solo_ideas`
   - 優先度: 低
   - 理由: ソロプレナー向けアイデア保管庫

---

## 📊 サマリー

| 項目 | 件数 |
|------|------|
| 総プロジェクト数 | 20 |
| 憲章あり | 17 (85%) |
| 憲章なし | 3 (15%) |

---

## 🎯 次のアクション

### 優先度1: 未作成憲章の作成（3件）

#### 1. affiliateman
- **作成判断**: 要検討
- **理由**: SNSノウハウプロジェクトのサブディレクトリとして存在。独立プロジェクトか確認が必要
- **確認事項**: README.mdや既存ドキュメントの有無

#### 2. ideas
- **作成判断**: 保留推奨
- **理由**: アイデア保管庫として機能。正式プロジェクト化する際に個別に憲章作成すべき
- **代替アプローチ**: ideasプロジェクト全体の管理方針ドキュメント作成

#### 3. solo_ideas
- **作成判断**: 保留推奨
- **理由**: ideasと同様、アイデア保管庫として機能
- **代替アプローチ**: solo_ideasプロジェクト全体の管理方針ドキュメント作成

---

## 💡 推奨事項

### A. 未作成3件への対応方針

**推奨**: ideasとsolo_ideasは「アイデア保管庫」として憲章不要。affiliatemanのみ検証して判断。

1. **affiliateman**: ディレクトリ構造を確認し、独立プロジェクトなら憲章作成
2. **ideas**: 管理方針ドキュメント（ideas_management.md）を作成
3. **solo_ideas**: 管理方針ドキュメント（solo_ideas_management.md）を作成

### B. 憲章の標準化

現在、憲章のパスが3種類存在：
- `documents/1_initiating/project_charter.md`（主流）
- `documents/00_project/project_charter.md`（旧形式）
- `project_charter.md`（ルート直下）

**推奨**: `documents/1_initiating/project_charter.md`に統一

---

## 📝 チェックリスト完了基準

- [x] Stock/programs配下の全プロジェクトをリストアップ
- [x] 各プロジェクトの憲章有無をチェック
- [x] 未作成プロジェクトのリスト化
- [x] 優先度判定と次のアクション提案
- [x] チェックリストレポート作成

**結論**: 実質的には**全主要プロジェクトに憲章が揃っている**状態。残り3件は性質上憲章不要またはディレクトリ構造の見直しが必要。

---

**作成者**: Claude Sonnet 4.5
**保存先**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/project_charter_checklist.md`
