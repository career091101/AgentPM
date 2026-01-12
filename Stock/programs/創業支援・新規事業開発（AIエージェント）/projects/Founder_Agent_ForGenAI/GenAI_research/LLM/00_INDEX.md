# GenAI_research（LLM向けインデックス）

目的：このフォルダをLLMに食わせる際に、**小さく・正確に・読み順つき**で渡せるようにする。

## 推奨読み順（最短）
1. `LLM/01_LifeisBeautiful_insights.md`（AIトレンド/未来社会/投資の観点）
2. `LLM/02_Ochyai_Note_insights.md`（AI公共財化・インフラ革命の観点）
3. `LLM/03_source_map.md`（どの主張がどの一次資料に対応するか）
4. `LLM/10_prompt_template.md`（このフォルダを材料に議論/分析させるためのプロンプト雛形）

## LLM投入のコツ
- 一次資料を丸ごと入れる前に、まず `LLM/` の3ファイルだけで「仮説と問い」を固める。
- 追加で一次資料が必要なら、`LLM/manifest.yaml` の **優先度A** から順に足す。

## 収録範囲
- `LifeisBeautiful/`：週刊メルマガ（md）
- `Ochyai_Note/articles/`：記事本文（md）を優先。`*.json` はメタ/画像説明。
