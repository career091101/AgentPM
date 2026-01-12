# Founder Agent システムプロンプト一覧

## 概要

Founder Agent を構成する各エージェント用のシステムプロンプトです。Claude Code で各タスクを並列実行する際に使用します。

## ファイル一覧

| #   | ファイル名                                                                    | 役割                  | 説明                               |
| --- | ----------------------------------------------------------------------------- | --------------------- | ---------------------------------- |
| 01  | [orchestrator_prompt.md](./01_orchestrator_prompt.md)                         | オーケストレーター    | 全体制御、並列呼び出し、ループ管理 |
| 02  | [executor_prompt.md](./02_executor_prompt.md)                                 | Executor              | 事業計画初稿の生成                 |
| 03  | [reviewer_peter_thiel_prompt.md](./03_reviewer_peter_thiel_prompt.md)         | Peter Thiel Agent     | Zero to One 評価                   |
| 04  | [reviewer_yc_prompt.md](./04_reviewer_yc_prompt.md)                           | Y Combinator Agent    | PMF・顧客熱狂度評価                |
| 05  | [reviewer_startup_science_prompt.md](./05_reviewer_startup_science_prompt.md) | Startup Science Agent | 起業の科学フェーズ評価             |
| 06  | [gatekeeper_prompt.md](./06_gatekeeper_prompt.md)                             | Gatekeeper            | スコア集計・通過判定               |
| 07  | [updater_prompt.md](./07_updater_prompt.md)                                   | Skill Updater         | AgentSkills 自動更新               |
| 08  | [affiliateman_strategy_prompt.md](./08_affiliateman_strategy_prompt.md)       | Affiliateman 戦略     | アフィリエイト戦略策定             |

## 実行フロー

```
                    ┌─────────────────┐
                    │   Orchestrator  │
                    │       (01)      │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │    Executor     │
                    │      (02)       │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐  ┌─────────▼─────────┐  ┌───────▼───────┐
│  Thiel (03)   │  │    YC (04)        │  │ StartupSci(05)│
└───────┬───────┘  └─────────┬─────────┘  └───────┬───────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────▼────────┐
                    │   Gatekeeper    │
                    │      (06)       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐ ◄─── FAIL時のみ
                    │    Updater      │
                    │      (07)       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  AgentSkills.md │ ◄─── ルール追記
                    └─────────────────┘
```

## 使用方法

### 1. Claude Code での実行

各プロンプトを Claude Code のシステムプロンプトとして設定し、対応するタスクを実行します。

### 2. 並列実行

Reviewer (03-05) は並列で実行可能です。Orchestrator がこれらを統括します。

### 3. AgentSkills の参照

Executor (02) は必ず `AgentSkills.md` を読み込んでから出力を生成します。

## 関連ファイル

- [AgentSkills.md](../AgentSkills.md) - Executor 制約条件
- [README.md](../README.md) - プロジェクト概要
