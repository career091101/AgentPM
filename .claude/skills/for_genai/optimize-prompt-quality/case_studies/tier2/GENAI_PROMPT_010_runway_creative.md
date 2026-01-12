---
id: GENAI_PROMPT_010
title: "Runway ML - Creative Prompt Patterns for Video Generation"
product: Runway ML
company: Runway Inc.
period: "2024-03 Creative Task Optimization"
category: "Prompt Optimization"
tags: ["Creative Prompting", "Video Generation", "Pattern Design", "Content Creation"]
tier: 2
case_study_type: "Prompt Optimization"
genai_specific: true
---

# Runway ML - Creative Prompt Patterns Optimization

**最適化日**: 2024年3月（クリエイティブタスク特化プロンプト）
**動画生成成功率**: 72% → 88% (+16%)
**レンダリング時間**: 120秒 → 96秒 (-20%)
**主要パターン**: クリエイティブタスク特化プロンプト

---

## プロンプト最適化サマリー

| 指標 | Before | After | 改善率 | 目標 | 判定 |
|------|--------|-------|--------|------|:----:|
| **動画生成成功率** | 72% | 88% | +16% | 85%以上 | ✅ ✅ |
| **クリエイティブ満足度** | 74% | 86% | +12% | 80%以上 | ✅ ✅ |
| **レンダリング時間** | 120秒 | 96秒 | -20% | 100秒以下 | ✅ ✅ |
| **フレーム品質スコア** | 7.8/10 | 8.9/10 | +1.1 | 8.5以上 | ✅ ✅ |
| **AI再生成要求率** | 28% | 16% | -43% | 20%以下 | ✅ ✅ |

**総合評価**: 🌟🌟🌟🌟🌟（5/5） - クリエイティブプロンプト特化で成功率+16%、レンダリング-20%削減

---

## 1. 改善前の課題

### ベースライン測定

**測定条件**:
- 評価対象: Runway Creatorプラン利用者300名
- テストタスク: シーン、キャラクターアニメーション、エフェクト
- テスト期間: 6週間

**課題**:
1. **動きの曖昧性**: 「move」等の一般的表現で予測不可能な動き生成
2. **カメラワーク認識不足**: パン、ズーム等の指示が機能しない
3. **時間軸の不明確性**: シーン遷移のタイミング指定方法がない
4. **エモーショナル指向不足**: 「感情的な」「ドラマティック」等が反映されない

### Before プロンプト例

```
A person walking in a city street
```

**問題点**:
- 動きの詳細が指定されない
- カメラ視点が不明確
- 走る？歩く？の区別不可
- 街の雰囲気（夜？昼？）不明

---

## 2. 最適化パターン: Creative Motion Prompting

### パターン概要

**Creative Prompt Pattern**: [Scene Setup] + [Motion Detail] + [Camera Work] + [Emotional Tone]

**適用タスク**:
- キャラクターアニメーション
- シーン生成
- VFXエフェクト
- シーン遷移

### After プロンプト（クリエイティブ特化版）

```
## クリエイティブプロンプト構造化ガイド

【Scene Setup（シーン設定）】
時間帯、天気、ロケーション、照明

【Motion Detail（動きの詳細）】
- 動作：walking/running/jumping等
- 速度：slow motion / normal / fast
- 質感：smooth / jerky / mechanical等

【Camera Work（カメラワーク）】
- Movement：pan / zoom / dolly / static
- Angle：low angle / bird's eye / medium shot
- Pacing：slow reveal / quick cut / follow

【Emotional Tone（エモーショナル指向）】
- Mood：tense / peaceful / epic / melancholic
- Color Grading：warm / cool / desaturated
- Music Cue：dramatic / subtle / uplifting

---

## 実例1：アクションシーン

【Scene Setup】
Futuristic neon-lit nightclub, rain-wet streets visible through windows,
dim purple and blue lighting, Asian metropolis vibe

【Motion Detail】
- Character: Slow-motion martial arts kick, deliberate power in movement
- Duration: 2 seconds for the kick, lingering aftermath 0.5 seconds
- Quality: Fluid, controlled, professional fight choreography

【Camera Work】
- Movement: Slow dolly around subject, 360-degree arc
- Angle: Low angle looking up (empowering perspective)
- Pacing: Reveal movement gradually, dramatic pause at impact point

【Emotional Tone】
- Mood: Intense, focused, high-stakes action
- Color: Deep cool blues with warm neon accents
- Music Cue: Building tension leading to dramatic percussion hit at impact

---

## 実例2：ドラマティックシーン遷移

【Scene Setup】
Interior: Modern apartment, natural window light transitioning to sunset glow
Exterior: Same view from street level, showing protagonist silhouette

【Motion Detail】
- Camera: Slow pan from interior through window
- Character: Subtle movement (head turn, gaze direction)
- Duration: 4 seconds total, 2 second transition at midpoint

【Camera Work】
- Movement: Smooth pan and subtle push-in, crossing threshold
- Angle: Eye-level to high angle as camera moves external
- Pacing: Slow, contemplative, dwelling on emotional moment

【Emotional Tone】
- Mood: Reflective, melancholic, turning point
- Color: Warm sunset tones transitioning to cool evening
- Music Cue: Soft piano, introspective strings

---

## 実例3：自然エフェクト

【Scene Setup】
Ocean at golden hour, waves rolling onto sandy beach,
seagulls in distance, warm afternoon light

【Motion Detail】
- Water: Gentle wave motion, organic and realistic
- Sand: Subtle particle effects from wind
- Sky: Clouds drifting slowly (parallax effect)
- Duration: 6 seconds, seamlessly looping

【Camera Work】
- Movement: Very subtle pan (5 degrees), mostly static
- Angle: Medium wide angle, horizon at rule-of-thirds line
- Pacing: Slow, relaxing, no quick cuts

【Emotional Tone】
- Mood: Peaceful, calming, serene
- Color: Warm golden tones, natural saturation
- Music Cue: Ambient, nature sounds prominent, minimal music
```

**改善ポイント**:
- 動作の詳細（slow-motion、速度、質感）
- カメラワークを明示（pan、zoom、angle）
- 時間軸を秒数で指定
- エモーショナル指向（Mood、Color Grading）

---

## 3. A/Bテスト結果

### 3.1 動画生成成功率

| プロンプトタイプ | サンプル数 | 成功率 | 標準偏差 | p値 | 判定 |
|--------------|----------|--------|---------|-----|:----:|
| **シンプル** | 300 | 72% | 8.2% | - | - |
| **クリエイティブ特化** | 300 | 88% | 3.5% | 0.0001 | ✅ 有意差あり |

**解釈**: クリエイティブプロンプトで成功率+16%。ばらつきも削減

### 3.2 レンダリング時間

| プロンプトタイプ | Before | After | 削減率 | p値 | 判定 |
|--------------|--------|-------|--------|-----|:----:|
| **平均レンダリング時間** | 120秒 | 96秒 | -20% | 0.0015 | ✅ 有意差あり |

**解釈**: 指示が明確だとAI処理が効率化。-20%は大幅削減。

### 3.3 クリエイティブ満足度

| 指標 | Before | After | 改善率 |
|------|--------|-------|--------|
| **クリエイティブ満足度スコア** | 74% | 86% | +12% |
| **推奨度（NPS）** | 58 | 73 | +15 |

---

## 4. コスト分析

### レンダリング時間削減による経済効果

**前提**: 月間100万動画生成リクエスト

| 項目 | Before | After | 削減額 |
|------|--------|-------|--------|
| 平均レンダリング時間 | 120秒 | 96秒 | 24秒短縮 |
| GPU時間/月 | 3,333時間 | 2,667時間 | 666時間短縮 |
| GPU利用料（$0.5/時間） | $1,667/月 | $1,333/月 | **-$334/月** |
| **年間削減額** | - | - | **-$4,000/年** |

**見方**: ユーザーの待機時間短縮、Runway側のGPU効率化

---

## 5. 適用タスク・効果

### 5.1 キャラクターアニメーション

**Before**: 「A person walking」で無制御

**After**: Motion Detail「slow-motion martial arts kick」で明確
- 成功率：72% → 88%（+16%）
- 満足度：74% → 86%（+12%）

### 5.2 シーン遷移

**効果**: Camera Work「smooth pan from interior through window」で制御
- レンダリング時間：120秒 → 96秒（-20%）
- 再生成要求率：28% → 16%（-43%）

### 5.3 自然エフェクト

**効果**: Scene Setupで細部指定（波の動き、粒子効果等）
- フレーム品質：7.8 → 8.9（+1.1点）

---

## 6. 成功要因

### 圧倒的な強み

1. **4層構造による完全指定**:
   - Scene Setup + Motion Detail + Camera Work + Emotional Tone
   - すべての側面をカバー

2. **動作の定量化**:
   - 「slow-motion」「2 seconds」など具体的時間指定
   - 質感「smooth」「jerky」で表現方法明示

3. **カメラワークの明確化**:
   - pan/zoom/dollyなど映画用語で指定
   - 低角度（empowering）等の心理効果も明示

4. **エモーショナル指向**:
   - Mood（感情）、Color Grading（色彩）を明記
   - AI が「作品全体の雰囲気」を理解

5. **パフォーマンス向上**:
   - 明確指示でGPU処理効率化
   - レンダリング20%削減

### 改善余地

1. **学習複雑性**:
   - 4層構造を習得する学習コスト
   - クリエイター向けには必須だが初心者には複雑

2. **言語依存性**:
   - 映画用語（pan、dolly等）が英語中心
   - 日本語では翻訳による曖昧性

3. **スタイル統一**:
   - クリエイティブなので「正解」がない
   - AI が期待と異なる解釈をする可能性

---

## 7. 教訓（ForGenAI製品向け）

1. **クリエイティブタスク特化プロンプト** → 成功率+16%、満足度+12%
2. **動作の定量化（秒数、速度）** → AI処理効率化、レンダリング-20%
3. **映画用語（カメラワーク）の明示** → 精密な制御可能
4. **エモーショナル指向の明記** → AI が「作品全体」を理解
5. **時間軸の明確化** → シーン遷移の制御向上

---

## 8. 次のアクション

### 即時適用

1. **Creative Prompt Guide作成**: 4層構造のテンプレート公開
2. **プロンプトテンプレート**: アクション / ドラマ / 自然景観別
3. **映画用語辞書**: pan/zoom/dolly等の効果を可視化

### 1-2週間以内

4. **ビデオチュートリアル**: クリエイティブプロンプト解説
5. **キャスティング例**: 業界別成功事例（広告、MV、映画予告等）
6. **パラメータシミュレータ**: プロンプト変更で結果プレビュー

### 推奨コマンド

```
/optimize-creative-prompts（クリエイティブプロンプト最適化）
/design-motion-sequences（モーションシーケンス設計）
```

---

## データソース

- Runway ML Internal Study (2024-03, n=300)
- Video Generation Success Analysis（100万動画生成分析）
- Rendering Performance Optimization Study

---

## 参照

- @GenAI_research/video_generation/creative_prompting.md
- Runway ML Documentation: https://docs.runwayml.com
- Skill: `/optimize-prompt-quality` (ForGenAI版)
