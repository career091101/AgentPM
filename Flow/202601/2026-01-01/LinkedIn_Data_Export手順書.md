# LinkedIn Data Export 手順書

**目的**: 全投稿の完全な本文データを取得し、文字数・パターン分析を正確に実施

**所要時間**:
- リクエスト: 5分
- ダウンロード待機: 1-3日（LinkedIn側の処理時間）
- 分析スクリプト実行: 10分

---

## Step 1: LinkedIn Data Exportのリクエスト

### 1.1 LinkedInにアクセス

1. ブラウザでLinkedInにログイン
2. 右上のプロフィールアイコンをクリック
3. 「Settings & Privacy」を選択

### 1.2 データダウンロードをリクエスト

1. 左メニューから「Data Privacy」を選択
2. 「Get a copy of your data」セクションを探す
3. 「Request archive」ボタンをクリック

### 1.3 データ範囲の選択

**オプション1: 高速（推奨）**
- 「Select the data you want」を選択
- チェック項目:
  - ✅ Posts（投稿データ）
  - ✅ Articles（記事データ、もしあれば）
  - ✅ Shares（シェアデータ）
- 他の項目（Connections、Messages等）は不要
- 所要時間: 数時間～1日

**オプション2: 完全アーカイブ**
- 「Request a full archive」を選択
- 全データを取得（Connections、Messages、Profile等含む）
- 所要時間: 1-3日

### 1.4 リクエストの確認

1. 「Request archive」ボタンをクリック
2. 確認画面で「Request」を再度クリック
3. 登録メールアドレスに確認メールが届く
4. メール内の「Confirm request」リンクをクリック

---

## Step 2: ダウンロード（1-3日後）

### 2.1 準備完了の通知

LinkedInから「Your data is ready」というメールが届く（通常1-3日）

### 2.2 ダウンロード

1. メール内の「Download your data」リンクをクリック
2. LinkedInにログイン（必要に応じて）
3. 「Download archive」ボタンをクリック
4. ZIPファイルがダウンロードされる（通常数MB～数十MB）

### 2.3 ファイルの解凍

```bash
# ダウンロードフォルダに移動
cd ~/Downloads

# ZIPファイルを解凍
unzip Basic_LinkedInDataExport_*.zip -d linkedin_export

# 解凍されたフォルダに移動
cd linkedin_export
```

---

## Step 3: データ構造の確認

### 3.1 ファイル構成

典型的なLinkedIn Data Exportの構造:

```
linkedin_export/
├── Posts/
│   └── Posts.csv            # 投稿データ（本文、日付、可視性等）
├── Articles/
│   └── Articles.csv         # 記事データ
├── Shares/
│   └── Shares.csv           # シェアデータ
└── README.txt               # データ説明
```

### 3.2 Posts.csvの確認

```bash
# ヘッダー行を確認
head -n 5 Posts/Posts.csv
```

予想される列:
- `PublishedAt`: 投稿日時
- `PostContent`: 投稿本文（**重要**）
- `PostUrl`: 投稿URL
- `Visibility`: 公開範囲（Public/Connections等）
- `SharedPostUrl`: シェア元URL（シェア投稿の場合）

---

## Step 4: 分析スクリプトの実行

### 4.1 Pythonスクリプトを作成

`/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts/analyze_linkedin_export.py` を作成:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn Data Export分析スクリプト
"""

import pandas as pd
import json
from pathlib import Path
import re

def analyze_linkedin_export(csv_path: str) -> dict:
    """LinkedIn Data ExportのPosts.csvから文字数分析"""

    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    # 列名を確認（LinkedIn側の命名に依存）
    content_col = None
    for col in df.columns:
        if 'content' in col.lower() or 'text' in col.lower() or 'post' in col.lower():
            content_col = col
            break

    if not content_col:
        return {'error': f'投稿本文の列が見つかりませんでした。利用可能な列: {df.columns.tolist()}'}

    # 文字数分析
    char_counts = []
    for idx, row in df.iterrows():
        text = str(row[content_col])
        if pd.notna(text) and text != 'nan':
            char_counts.append(len(text))

    # パターン分類（既存のロジックを流用）
    def classify_pattern(text: str) -> str:
        if re.search(r'(氏は|氏が|によると|報道によると|発表|述べた)', text[:100]):
            return 'Pattern 3: ニュース引用型'
        if '【告知】' in text or 'イベント' in text[:50]:
            return 'Pattern 5: イベント型'
        if re.search(r'(である|だ|でした)。', text[:200]):
            return 'Pattern 1: 断定型'
        num_count = len(re.findall(r'\d+,?\d*', text))
        if num_count >= 5:
            return 'Pattern 4: リスト型・衝撃ファクト'
        return 'その他'

    # 問いかけ終結チェック
    def check_question_ending(text: str) -> bool:
        ending = text[-50:]
        question_patterns = [
            r'か？', r'でしょうか', r'ますか', r'ませんか',
            r'のでは', r'だろうか', r'はいかが', r'どう思いますか', r'いかがでしょうか'
        ]
        return any(re.search(pattern, ending) for pattern in question_patterns)

    patterns = {}
    question_endings = 0

    for idx, row in df.iterrows():
        text = str(row[content_col])
        if pd.notna(text) and text != 'nan':
            pattern = classify_pattern(text)
            patterns[pattern] = patterns.get(pattern, 0) + 1

            if check_question_ending(text):
                question_endings += 1

    return {
        'total_posts': len(char_counts),
        'char_count_analysis': {
            'count': len(char_counts),
            'average': sum(char_counts) / len(char_counts) if char_counts else 0,
            'median': sorted(char_counts)[len(char_counts) // 2] if char_counts else 0,
            'min': min(char_counts) if char_counts else 0,
            'max': max(char_counts) if char_counts else 0,
            'optimal_range_500_1000': sum(1 for c in char_counts if 500 <= c <= 1000),
            'optimal_range_700_900': sum(1 for c in char_counts if 700 <= c <= 900),
            'distribution': {
                'under_500': sum(1 for c in char_counts if c < 500),
                '500_700': sum(1 for c in char_counts if 500 <= c < 700),
                '700_900': sum(1 for c in char_counts if 700 <= c < 900),
                '900_1000': sum(1 for c in char_counts if 900 <= c < 1000),
                'over_1000': sum(1 for c in char_counts if c >= 1000)
            }
        },
        'pattern_classification': patterns,
        'question_ending': {
            'count': question_endings,
            'rate': question_endings / len(char_counts) * 100 if char_counts else 0,
            'benchmark_takano': '問いかけ終結 ほぼ必須（推定80%以上）'
        }
    }

if __name__ == '__main__':
    # ダウンロードフォルダのパスを指定
    export_path = Path.home() / 'Downloads' / 'linkedin_export' / 'Posts' / 'Posts.csv'

    if not export_path.exists():
        print(f"エラー: {export_path} が見つかりません")
        print("LinkedIn Data Exportをダウンロードして解凍してください")
        exit(1)

    result = analyze_linkedin_export(str(export_path))

    # 結果を表示
    print("=" * 80)
    print("LinkedIn Data Export 完全分析レポート")
    print("=" * 80)
    print()

    if 'error' in result:
        print(f"エラー: {result['error']}")
    else:
        print(f"分析対象投稿数: {result['total_posts']}投稿")
        print()

        print("【文字数分析】")
        ca = result['char_count_analysis']
        print(f"平均文字数: {ca['average']:.1f}字")
        print(f"中央値: {ca['median']}字")
        print(f"最小: {ca['min']}字")
        print(f"最大: {ca['max']}字")
        print(f"最適範囲(500-1000字): {ca['optimal_range_500_1000']}投稿 ({ca['optimal_range_500_1000']/ca['count']*100:.1f}%)")
        print(f"高野氏推奨範囲(700-900字): {ca['optimal_range_700_900']}投稿 ({ca['optimal_range_700_900']/ca['count']*100:.1f}%)")
        print()

        print("文字数分布:")
        for range_name, count in ca['distribution'].items():
            print(f"  {range_name}: {count}投稿 ({count/ca['count']*100:.1f}%)")
        print()

        print(f"高野氏ベンチマーク: 平均760.1字、500-1000字が56%")
        print()

        print("【パターン分類】")
        for pattern, count in sorted(result['pattern_classification'].items(), key=lambda x: x[1], reverse=True):
            print(f"{pattern}: {count}投稿 ({count/result['total_posts']*100:.1f}%)")
        print()

        print("【問いかけ終結率】")
        qe = result['question_ending']
        print(f"問いかけで終わる投稿: {qe['count']}投稿 ({qe['rate']:.1f}%)")
        print(f"高野氏ベンチマーク: {qe['benchmark_takano']}")
        print()

        # JSON出力
        output_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/LinkedIn/linkedin_export_complete_analysis.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"詳細結果をJSONで保存: {output_path}")
```

### 4.2 スクリプトの実行

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
python3 scripts/analyze_linkedin_export.py
```

---

## Step 5: 結果の解釈と次のアクション

### 5.1 文字数が高野氏より短い場合（平均 < 500字）

**結論**: 文字数不足が確定
**アクション**:
1. 700-900字を目標に設定
2. 高野氏7パターンのテンプレート作成
3. 1投稿あたりの作成時間を10分→40分に増加

### 5.2 文字数が高野氏と同等の場合（平均 500-800字）

**結論**: 文字数は問題なし、他の要因が主原因
**アクション**:
1. 問いかけ終結率0% → 80%+への改善を最優先
2. パターン分類の体系化（7パターン適用）
3. 投稿頻度の最適化（毎日30投稿 → 週3回12投稿）

### 5.3 プロジェクト憲章の更新

分析結果を反映:
- Section 1.2 LinkedInベンチマーク比較表の「文字数」行を更新
- ⚠️ データ制約の注記を削除
- Section 3.1.1 または 3.3.3 に根本原因を追記

---

## トラブルシューティング

### Q1: LinkedIn Data Exportが24時間経っても届かない

**A**: 最大72時間かかる場合があります。以下を確認:
1. 迷惑メールフォルダをチェック
2. LinkedIn Settings → Data Privacy → 「Download your data」で進捗確認
3. 3日経過後も届かない場合は再リクエスト

### Q2: Posts.csvに本文列がない / 空白が多い

**A**: 以下の可能性:
1. LinkedIn側のエクスポート形式変更 → 他の列名（Commentary、Text等）を確認
2. 投稿がシェアのみで本文なし → ShareUrl列から判別
3. プライバシー設定で一部投稿が除外 → 投稿数を確認

### Q3: 文字数が異常に少ない（平均100字未満等）

**A**: 以下を確認:
1. HTMLタグがエスケープされている → 正規表現で除去
2. リンクURLが含まれている → URLを除外して再カウント
3. シェア投稿のみで本文なし → オリジナル投稿のみフィルタリング

---

**作成日**: 2026-01-01
**次回更新予定**: LinkedIn Data Export完了後（2026-01-02～04頃）
**関連ドキュメント**: `LinkedIn文字数_手動サンプリングチェックリスト.md`
