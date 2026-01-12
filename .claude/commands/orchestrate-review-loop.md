---
name: orchestrate-review-loop
description: |
  Main → SubAgent → Review → Integrationのレビューループを実行するオーケストレータースキル。
  SubAgentが実装して終わりではなく、Mainがdiffとテスト証拠でレビュー、ズレがあれば即リプランして次の指示に反映。
  品質70点以上を自動保証します。
---

このコマンドは `/orchestrate-review-loop` スキルを起動します。
