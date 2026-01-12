#!/usr/bin/env python3
"""
Generate missing Markdown files from JSON metadata
欠損Markdownファイルの自動生成スクリプト
"""

import json
from pathlib import Path
from datetime import datetime

# Base directory
ARTICLES_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/GenAI_research/Ochyai_Note/full_run/articles")

# Missing files (from A5 validation results)
MISSING_FILES = [
    "2025-12-30_#裸性と身体性 七〇回　aさん　前編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 七一回　aさん　後編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 七七回　大瀧冬佳さん　後編｜落合陽一｜落合陽一.json",
    "2025-12-30_#裸性と身体性 七三回　u_ibillyさん　 後編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 七九回　早百合 さん　後編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 七二回　u_ibillyさん　 前編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 七五回　u_i akagawaさん　後編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 七八回　早百合 さん　前編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 七六回　大瀧冬佳さん　前編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 六九回　ともみんさん　後編｜落合陽一.json",
    "2025-12-30_#裸性と身体性 六八回　ともみんさん　前編｜落合陽一.json",
]


def generate_markdown_from_json(json_path: Path) -> bool:
    """
    JSONファイルから最小限のMarkdownファイルを生成

    Args:
        json_path: JSONファイルのパス

    Returns:
        bool: 生成成功の場合True
    """
    try:
        # Load JSON data
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Generate markdown content
        title = data.get('title', 'Untitled')
        url = data.get('url', '')
        published_at = data.get('published_at') or 'Unknown'
        tags = data.get('tags', [])
        is_paid = data.get('is_paid', False)
        scraped_at = data.get('scraped_at', '')

        md_content = f"""# {title}

**URL**: [{url}]({url})
**公開日**: {published_at}
**タグ**: {', '.join(tags) if tags else 'なし'}
**有料記事**: {'はい' if is_paid else 'いいえ'}

---

## お知らせ

この記事は自動スクレイピング時に本文の取得ができませんでした。

以下のいずれかの理由が考えられます:
- 有料記事でログインが必要
- アクセス制限がかかっている
- 一時的なネットワークエラー

元の記事を閲覧するには、上記のURLにアクセスしてください。

---

**スクレイピング日時**: {scraped_at}
**自動生成日時**: {datetime.now().isoformat()}
"""

        # Save markdown file
        md_path = json_path.with_suffix('.md')
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✅ Generated: {md_path.name}")
        return True

    except Exception as e:
        print(f"❌ Error generating markdown for {json_path.name}: {e}")
        return False


def main():
    """Main execution"""
    print("=" * 80)
    print("欠損Markdownファイル自動生成スクリプト")
    print("=" * 80)
    print(f"\n対象ディレクトリ: {ARTICLES_DIR}")
    print(f"処理対象ファイル数: {len(MISSING_FILES)}")
    print()

    success_count = 0
    failed_count = 0

    for filename in MISSING_FILES:
        json_path = ARTICLES_DIR / filename

        if not json_path.exists():
            print(f"⚠️  JSON file not found: {filename}")
            failed_count += 1
            continue

        # Check if markdown already exists
        md_path = json_path.with_suffix('.md')
        if md_path.exists():
            print(f"⏭️  Markdown already exists, skipping: {md_path.name}")
            continue

        # Generate markdown
        if generate_markdown_from_json(json_path):
            success_count += 1
        else:
            failed_count += 1

    # Summary
    print()
    print("=" * 80)
    print("処理完了")
    print("=" * 80)
    print(f"成功: {success_count}")
    print(f"失敗: {failed_count}")
    print(f"スキップ: {len(MISSING_FILES) - success_count - failed_count}")
    print("=" * 80)

    if success_count > 0:
        print("\n次のステップ:")
        print("1. 生成されたMarkdownファイルを確認してください")
        print("2. 必要に応じて元のURLから手動で本文を取得してください")
        print("3. A5検証を再実行して整合性を確認してください:")
        print("   python3 A5_consistency_validation.py")


if __name__ == "__main__":
    main()
