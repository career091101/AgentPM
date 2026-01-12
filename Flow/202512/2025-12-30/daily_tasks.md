# 日次タスク

**日付**: 2025-12-30
**曜日**: 火曜日

---

## 📋 AI 構想・タスクリスト

### 【Inbox: 今日の悩み・気がかり・やりたいこと】

- **Founder Agent の開発推進**:

  - [ ] **Origin（オリジナル版）の完成**:
    - `Founder_Agent_Phase1` プロジェクトをベースに、Discovery〜MVP までのワークフローを自律的につなぐ
    - 『起業の科学』ナレッジ (`startup_science_knowledge.md`) を確実に組み込む
  - [ ] **4 パターンへの展開**:
    - [ ] **ForStartup**: Origin そのもの
    - [ ] **ForRecruit**: 組織開発・採用特化
    - [ ] **ForSolo**: ソロプレナー調査 (`Solopreneur_Research` データ) を活用
    - [ ] **ForGenAI**: GenAI プロダクト特化 (`GenAI_Research` 新設フォルダ活用)
  - [ ] 実行＆自律改善サイクルの確立

- **Trading Agent の実装と検証**:

  - [ ] **Type 1 (TradingAgents)**: README 定義に基づき、欠落している Skill（データ収集・統合）を実装してテスト実行する
  - [ ] **Type 2 (エリオット波動)**: 既存スクリプト (`extract_report_content.py`等) を自律ワークフロー化する
  - [ ] 実行結果に基づき自律改善させる

- **SNS ノウハウの体系化**:
  - [ ] SNS フォルダ内のナレッジ（X, LinkedIn, FB, Insta 等）を媒体別にまとめる
  - [ ] 不足情報はエージェントが自律的に調査・補完する

### 【Candidates: 候補タスク】

- **A. TradingAgents (Type 1) のスキル実装**: `orchestrate-trading-strategy` などを実装し、初回実行を行う
- **B. Founder Agent (Origin) のオーケストレーション**: `AgentSkills.md` を実ワークフローファイル (`.agent/workflows/*.md`) に変換・統合する
- **C. エリオット波動 (Type 2) のワークフロー化**: レポート要約〜分析の流れを自動化定義する

---

## 🚀 今日の確定タスク (予定)

- [ ] **Trading Agent (Type 1 & 2) の現状整理と実装計画の策定** (完了)
- [ ] **TradingAgents (Type 1) のスキル実装 (最小構成) とテスト実行**
- [ ] **Founder Agent (Origin) のオーケストレーション設計**

---

## 📝 メモ

- **Trading Agent**: `src/agents` が空だったため、README の設計を正として実装を進める必要がある。
- **GenAI Research**: フォルダ作成済み (`/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/GenAI_Research`)。
- **オーケストレーション**: 複数の Agent Skill を並列・自律的に動かす仕組み（Make や n8n を使わず、Antigravity/Claude Code 内で完結させる）。
