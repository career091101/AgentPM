#!/usr/bin/env python3
"""
X Bookmark Batch Evaluator for Claude Code

823件のブックマークを一括評価し、Claude Codeに評価依頼JSONを生成。

使用方法:
    # 全件評価依頼を生成
    python batch_evaluate_bookmarks.py --input x_bookmarks_data_fulltext.json

    # TOP 10のみ評価依頼を生成
    python batch_evaluate_bookmarks.py --input x_bookmarks_data_fulltext.json --top 10

    # スコア境界線のみ（ルールベース事前フィルタ）
    python batch_evaluate_bookmarks.py --input x_bookmarks_data_fulltext.json --filter-boundary
"""

import json
import argparse
from pathlib import Path
from typing import Dict, Any, List
from bookmark_value_evaluator import BookmarkValueEvaluator


def create_batch_evaluation_request(posts: List[Dict[str, Any]],
                                    batch_size: int = 50) -> List[Dict[str, Any]]:
    """
    Claude Code用のバッチ評価依頼を生成

    Args:
        posts: 評価対象投稿リスト
        batch_size: 1バッチあたりの投稿数（Claude Codeの処理効率を考慮）

    Returns:
        バッチ評価依頼リスト
    """
    batches = []
    total = len(posts)

    for i in range(0, total, batch_size):
        batch_posts = posts[i:i+batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (total + batch_size - 1) // batch_size

        batch = {
            "バッチ番号": f"{batch_num}/{total_batches}",
            "投稿数": len(batch_posts),
            "開始番号": i + 1,
            "終了番号": min(i + batch_size, total),
            "評価依頼": []
        }

        for j, post in enumerate(batch_posts, start=i+1):
            batch["評価依頼"].append({
                "投稿番号": j,
                "投稿データ": {
                    "text": post.get('text', ''),
                    "author_username": post.get('author_username', ''),
                    "engagement": post.get('engagement', {}),
                    "posted_at": post.get('posted_at', ''),
                    "url": post.get('url', '')
                }
            })

        batches.append(batch)

    return batches


def create_instruction_message(total_posts: int, total_batches: int,
                               filter_mode: str = None) -> str:
    """Claude Code実行用の指示メッセージを生成"""

    filter_msg = ""
    if filter_mode == "boundary":
        filter_msg = "（ルールベースで50-70点の境界線投稿のみ）"
    elif filter_mode == "top":
        filter_msg = "（高エンゲージメント投稿のみ）"

    return f"""# X Bookmark 全件評価依頼{filter_msg}

## 概要

{total_posts}件の投稿を7軸評価モデルで評価します。
全{total_batches}バッチに分割されています。

## 評価方法

各投稿について、以下の7軸で評価してください：

1. **実践的価値（20点）**: 概念的理解の深さ、理論・原理、比較分析
2. **最新性（15点）**: 投稿日からの経過日数
3. **データドリブン（15点）**: 数値データ、実験結果、統計情報
4. **引用・参照性（15点）**: 引用文化、参照リンク
5. **集合知評価（15点）**: いいね数・RT数（相関0.89）
6. **発信者専門性（10点）**: 著者の専門性（TOP 20リスト参照）
7. **情報の深さ（10点）**: 洞察、批判的視点、今後の展望

## 出力形式

各投稿の評価結果をJSON配列で出力：

```json
[
  {{
    "投稿番号": 1,
    "総合スコア": 0-100,
    "判定": "VERY HIGH / HIGH / MEDIUM / LOW",
    "評価詳細": {{
      "実践的価値": 0-20,
      "最新性": 0-15,
      "データドリブン": 0-15,
      "引用・参照性": 0-15,
      "集合知評価": 0-15,
      "発信者専門性": 0-10,
      "情報の深さ": 0-10
    }},
    "理由": "評価理由（3-5文）",
    "カテゴリ": "AI・生成AI / ビジネス・起業 / 開発 / デザイン・UX / その他",
    "概念的タイプ": "理論・原理 / 比較・分析 / トレンド・ニュース / まとめ / 事例紹介 / ベストプラクティス / 思考・考察 / その他",
    "推奨アクション": "具体的なアクション",
    "文脈評価": {{
      "深い洞察": "文脈・ニュアンスの評価",
      "ユーザー適合度": "97.1%概念的学習との適合度（高/中/低）",
      "隠れた価値": "ルールベースでは捉えきれない価値"
    }}
  }},
  ...
]
```

## 実行手順

1. `batch_1.json` を開く
2. 各投稿を7軸評価
3. 結果を `evaluation_results_batch_1.json` に保存
4. バッチ2へ進む（全{total_batches}バッチ）

## 参照

- 評価基準詳細: `.claude/commands/evaluate-bookmark-value.md`
- ユーザー学習スタイル: 97.1%概念的学習、70.7%AI・生成AI特化

---

**重要**: 全{total_posts}件の評価完了後、以下のスクリプトで結果を統合してください：

```bash
python scripts/merge_evaluation_results.py --output final_evaluation_results.json
```
"""


def main():
    parser = argparse.ArgumentParser(
        description='X Bookmark バッチ評価依頼生成（Claude Code用）'
    )

    parser.add_argument('--input', required=True,
                       help='入力JSONファイル（x_bookmarks_data_fulltext.json）')
    parser.add_argument('--output-dir', default='Flow/202512/2025-12-31/batch_evaluation',
                       help='出力ディレクトリ')
    parser.add_argument('--batch-size', type=int, default=50,
                       help='1バッチあたりの投稿数（デフォルト: 50）')
    parser.add_argument('--top', type=int,
                       help='TOP N件のみ評価（エンゲージメント順）')
    parser.add_argument('--filter-boundary', action='store_true',
                       help='ルールベースで50-70点の境界線投稿のみ抽出')

    args = parser.parse_args()

    # 入力データ読み込み
    with open(args.input, 'r', encoding='utf-8') as f:
        data = json.load(f)

    posts = data.get('bookmarks', data)

    # フィルタリング
    filter_mode = None

    if args.top:
        # TOP N件に絞る
        posts = sorted(posts,
                      key=lambda x: x.get('engagement', {}).get('likes', 0),
                      reverse=True)[:args.top]
        filter_mode = "top"
        print(f"TOP {args.top}件を抽出しました。")

    if args.filter_boundary:
        # ルールベース評価で境界線のみ抽出
        print("ルールベース評価で境界線投稿を抽出中...")
        evaluator = BookmarkValueEvaluator()
        boundary_posts = []

        for post in posts:
            result = evaluator.evaluate(post)
            score = result['総合スコア']
            if 50 <= score <= 70:
                boundary_posts.append(post)

        posts = boundary_posts
        filter_mode = "boundary"
        print(f"境界線投稿 {len(posts)}件を抽出しました。")

    # 出力ディレクトリ作成
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # バッチ生成
    batches = create_batch_evaluation_request(posts, args.batch_size)

    # バッチファイル保存
    for i, batch in enumerate(batches, 1):
        batch_file = output_dir / f"batch_{i}.json"
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batch, f, ensure_ascii=False, indent=2)
        print(f"✓ {batch_file} 保存（{batch['投稿数']}件）")

    # 指示メッセージ生成
    instruction = create_instruction_message(len(posts), len(batches), filter_mode)
    instruction_file = output_dir / "INSTRUCTION.md"
    with open(instruction_file, 'w', encoding='utf-8') as f:
        f.write(instruction)
    print(f"\n✓ {instruction_file} 保存")

    # サマリー表示
    print("\n" + "="*60)
    print("バッチ評価依頼生成完了")
    print("="*60)
    print(f"総投稿数: {len(posts)}件")
    print(f"総バッチ数: {len(batches)}バッチ")
    print(f"バッチサイズ: {args.batch_size}件/バッチ")
    print(f"出力先: {output_dir}")
    print("\n次のステップ:")
    print(f"1. {instruction_file} を確認")
    print(f"2. Claude Codeで各バッチファイルを評価")
    print(f"3. 全バッチ完了後、結果を統合")


if __name__ == '__main__':
    main()
