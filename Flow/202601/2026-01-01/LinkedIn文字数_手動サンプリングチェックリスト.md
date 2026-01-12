# LinkedIn投稿文字数 - 手動サンプリングチェックリスト

**目的**: visual extraction logの制約（冒頭141字のみ）を解消し、実際の投稿全文の文字数を測定

**作業手順**:
1. 各URLをブラウザで開く
2. 投稿本文全体をコピー（画像のalt text、リンクテキストは除外）
3. Google Docs / Wordに貼り付け、文字数をカウント
4. 下記の表に記入
5. 完了後、平均値を算出

---

## Top 10投稿（高インプレッション）

| # | Imp | URL | 文字数 | メモ |
|---|-----|-----|--------|------|
| 1 | 33,136 | https://www.linkedin.com/feed/update/urn:li:activity:7387261803979829248 | ___ | |
| 2 | 27,697 | https://www.linkedin.com/feed/update/urn:li:activity:7391248047881555968 | ___ | |
| 3 | 20,361 | https://www.linkedin.com/feed/update/urn:li:activity:7382188254583812097 | ___ | |
| 4 | 14,519 | https://www.linkedin.com/feed/update/urn:li:activity:7385087381571428352 | ___ | |
| 5 | 13,683 | https://www.linkedin.com/feed/update/urn:li:activity:7387624577327280128 | ___ | |
| 6 | 13,472 | https://www.linkedin.com/feed/update/urn:li:activity:7387986808111833089 | ___ | |
| 7 | 11,065 | https://www.linkedin.com/feed/update/urn:li:activity:7388348969321525248 | ___ | |
| 8 | 11,008 | https://www.linkedin.com/feed/update/urn:li:activity:7394147030954119168 | ___ | |
| 9 | 10,666 | https://www.linkedin.com/feed/update/urn:li:activity:7386899610977386496 | ___ | |
| 10 | 10,384 | https://www.linkedin.com/feed/update/urn:li:activity:7381826174106296320 | ___ | |

**Top 10平均文字数**: ___ 字

---

## Bottom 10投稿（低インプレッション）

⚠️ 注意: これは「人気の投稿Top 50」内でのBottom 10です。全90投稿の真のBottomではありません。

| # | Imp | URL | 文字数 | メモ |
|---|-----|-----|--------|------|
| 1 | 3,907 | https://www.linkedin.com/feed/update/urn:li:activity:7405015647757230080 | ___ | |
| 2 | 3,890 | https://www.linkedin.com/feed/update/urn:li:activity:7380376311019712512 | ___ | |
| 3 | 3,746 | https://www.linkedin.com/feed/update/urn:li:activity:7402844501893132288 | ___ | |
| 4 | 3,731 | https://www.linkedin.com/feed/update/urn:li:activity:7382550647554048000 | ___ | |
| 5 | 3,455 | https://www.linkedin.com/feed/update/urn:li:activity:7403931698029162496 | ___ | |
| 6 | 3,399 | https://www.linkedin.com/feed/update/urn:li:activity:7403206821307510786 | ___ | |
| 7 | 3,344 | https://www.linkedin.com/feed/update/urn:li:activity:7395958980113707008 | ___ | |
| 8 | 3,182 | https://www.linkedin.com/feed/update/urn:li:activity:7383637814363664384 | ___ | |
| 9 | 3,026 | https://www.linkedin.com/feed/update/urn:li:activity:7384000177151545345 | ___ | |
| 10 | 2,905 | https://www.linkedin.com/feed/update/urn:li:activity:7399220594346602496 | ___ | |

**Bottom 10平均文字数**: ___ 字

---

## 分析結果サマリー

### 高野氏ベンチマークとの比較

| 指標 | ユーザー（Top 10） | ユーザー（Bottom 10） | 高野氏ベンチマーク | 判定 |
|------|------------------|---------------------|------------------|------|
| 平均文字数 | ___ 字 | ___ 字 | 760.1字 | |
| 最適範囲（500-1000字）達成率 | ___% | ___% | 56% | |
| 最適範囲（700-900字）達成率 | ___% | ___% | - | |

### 仮説検証

**仮説1: Top投稿は文字数が多い**
- Top 10平均 ___ 字 vs Bottom 10平均 ___ 字
- 差分: ___ 字 (___%)
- 結論: □ 仮説支持 / □ 仮説棄却

**仮説2: 現状の文字数は高野氏より大幅に短い**
- ユーザー平均 ___ 字 vs 高野氏 760.1字
- 差分: ___ 字 (___%)
- 結論: □ 仮説支持（改善必須） / □ 仮説棄却（問題なし）

**仮説3: visual extraction log（141字）は実際の1/5程度**
- 実測平均 ___ 字 vs visual extraction log 141字
- 倍率: ___ 倍
- 結論: □ 仮説支持 / □ 仮説棄却

---

## 次のアクション

### 仮説1が支持された場合（Top投稿は文字数が多い）
→ 文字数を増やす施策が有効

### 仮説2が支持された場合（高野氏より大幅に短い）
→ 700-900字への増加が急務

### 仮説2が棄却された場合（高野氏と同等）
→ 文字数以外の要因（問いかけ終結率0%、パターン単一化）が主原因

---

**作成日**: 2026-01-01
**所要時間（推定）**: 30-45分（20投稿 × 1.5-2分/投稿）
**次のステップ**: 完了後、プロジェクト憲章を更新
