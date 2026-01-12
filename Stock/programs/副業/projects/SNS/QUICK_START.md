# X Timeline Collection - クイックスタート

## 3ステップで完了

### ステップ 1: コンソールを開く

X.com/home で **`Cmd + Option + J`**

### ステップ 2: スクリプト実行

以下のコマンドでスクリプトをコピー:

```bash
cat /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/final_x_collector.js | pbcopy
```

コンソールに貼り付けて **Enter**

### ステップ 3: 収集開始

コンソールに以下を入力:

```javascript
await runCollectionCycle(20)
```

完了したら:

```javascript
downloadCollectionData()
```

## ファイルを移動

```bash
mv ~/Downloads/x_timeline_*.json \
   /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_fixed.json
```

## 検証

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 件数
jq 'length' data/x_timeline_20260101_fixed.json

# エンゲージメント統計
jq '[.[] | select(.likes>0 or .retweets>0 or .replies>0)] | length' data/x_timeline_20260101_fixed.json

# Top 3
jq -r 'sort_by(.likes) | reverse | .[0:3] | .[] | "\(.likes) likes, \(.retweets) RTs, \(.replies) replies"' data/x_timeline_20260101_fixed.json
```

---

**詳細**: `X_COLLECTION_INSTRUCTIONS.md` を参照
