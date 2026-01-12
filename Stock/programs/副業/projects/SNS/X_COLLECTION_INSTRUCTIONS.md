# X Timeline Collection - 実行手順

## 問題の原因

Claude In Chrome MCP の JavaScript 実行ツールには、複雑な制御構文（if, for, function等）を含むコードに対する制限があり、直接実行ができませんでした。

## 解決策

ブラウザのコンソールに直接スクリプトを貼り付けて実行します。

## 実行手順

### 1. ブラウザコンソールを開く

X.com/home のタブで以下のいずれかを実行:

- **Mac Chrome**: `Cmd + Option + J`
- **Windows/Linux Chrome**: `Ctrl + Shift + J`
- **Firefox**: `Ctrl + Shift + K`

または:
- 右クリック → 「検証」→「Console」タブ

### 2. スクリプトをコピー

以下のファイルの内容を全てコピー:

```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/final_x_collector.js
```

### 3. コンソールに貼り付けて実行

1. コンソールに全文を貼り付け
2. Enter キーを押す
3. 以下のメッセージが表示されることを確認:
   ```
   ✅ Functions loaded!
   Run: await runCollectionCycle(20)
   Then: downloadCollectionData()
   ```

### 4. データ収集を開始

コンソールに以下を入力して実行:

```javascript
await runCollectionCycle(20)
```

実行中の出力例:
```
Starting 20 collection cycles...
Cycle 1: +10 tweets (total: 10)
Sample engagement: [{likes: 27, retweets: 1, replies: 0}, ...]
Cycle 2: +8 tweets (total: 18)
...
Cycle 20: +5 tweets (total: 215)
✅ Collection complete!
Total tweets: 215
```

### 5. データをダウンロード

コンソールに以下を入力して実行:

```javascript
downloadCollectionData()
```

ブラウザのダウンロードフォルダに `x_timeline_2026-01-01.json` が保存されます。

### 6. ファイルを移動

ダウンロードしたファイルを以下の場所に移動:

```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260101_fixed.json
```

## データ検証

以下のコマンドで結果を確認:

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 件数確認
python3 -c "import json; data=json.load(open('data/x_timeline_20260101_fixed.json')); print(f'Total tweets: {len(data)}')"

# エンゲージメント統計
python3 -c "import json; data=json.load(open('data/x_timeline_20260101_fixed.json')); with_eng=[t for t in data if t['likes']>0 or t['retweets']>0 or t['replies']>0]; print(f'With engagement: {len(with_eng)}/{len(data)} ({len(with_eng)/len(data)*100:.1f}%)')"

# Top 3 確認
python3 -c "import json; data=json.load(open('data/x_timeline_20260101_fixed.json')); top3=sorted(data, key=lambda x: x['likes'], reverse=True)[:3]; print('Top 3 by likes:'); [print(f\"  {t['likes']} likes, {t['retweets']} RTs, {t['replies']} replies\") for t in top3]"
```

## 期待される結果

- **収集件数**: 200件以上
- **エンゲージメント有効率**: 80%以上
- **Top 3**: すべて likes > 0

## トラブルシューティング

### スクリプトエラーが出る場合

1. ページを再読み込み
2. スクロールして少しツイートを表示
3. 再度スクリプトを貼り付け

### 途中で止まった場合

現在のデータを確認:

```javascript
console.log(`Collected so far: ${window.XCollectionState.tweets.length}`)
```

続きから再開:

```javascript
await runCollectionCycle(10)  // 残りのサイクル数
```

### データが取れていない場合

手動で1サイクル実行して確認:

```javascript
var result = window.extractAndCollect()
console.log(result)
```

## スクリプトの仕組み

1. **初期化**: `window.XCollectionState` にデータを蓄積
2. **抽出**: 日本語 aria-label から正規表現でエンゲージメント数値を取得
   - `"27 件のいいね。いいねする"` → `27`
   - `"1 件のリポスト。リポストする"` → `1`
   - `"5 件の返信。返信する"` → `5`
3. **重複除外**: `seenIds` Set で同一ツイートを除外
4. **スクロール**: 各サイクルで 800px 下にスクロール
5. **待機**: 2秒待って新しいツイートを読み込み
6. **エクスポート**: JSON形式でダウンロード

## 参考: 前回の問題

前回収集データ (`x_timeline_20260101_full.json`) では、英語フォーマットの正規表現を使用していたため:

```javascript
// ❌ 前回（英語フォーマット）
var likeMatch = likeLabel.match(/([0-9,]+) Likes/);

// ✅ 今回（日本語フォーマット）
var likeMatch = likeLabel.match(/([0-9,]+) 件のいいね/);
```

すべてのエンゲージメント指標が 0 になっていました。

今回の修正版では、日本語 aria-label に正しく対応しています。
