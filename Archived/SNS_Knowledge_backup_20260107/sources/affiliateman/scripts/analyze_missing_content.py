#!/usr/bin/env python3
"""
未取得URLを分類・分析して、取得すべきコンテンツを特定する
"""

missing_urls = [
    "https://affiliateman.site",
    "https://affiliateman.site/",
    "https://affiliateman.site/1-2/",
    "https://affiliateman.site/conceptmakeguide/",
    "https://affiliateman.site/dm/",
    "https://affiliateman.site/gaibu/",
    "https://affiliateman.site/instagram-book/",
    "https://affiliateman.site/kanagawagurume/",
    "https://affiliateman.site/kei/",
    "https://affiliateman.site/koteipin/",
    "https://affiliateman.site/line/",
    "https://affiliateman.site/main/",
    "https://affiliateman.site/movies/",
    "https://affiliateman.site/note_ryu/",
    "https://affiliateman.site/notelink/",
    "https://affiliateman.site/out_2",
    "https://affiliateman.site/out_3",
    "https://affiliateman.site/out_4",
    "https://affiliateman.site/out_4/",
    "https://affiliateman.site/output/",
    "https://affiliateman.site/output12/",
    "https://affiliateman.site/output_10/",
    "https://affiliateman.site/output_11/",
    "https://affiliateman.site/present/",
    "https://affiliateman.site/qa10/",
    "https://affiliateman.site/qa5/",
    "https://affiliateman.site/qa6/",
    "https://affiliateman.site/qa8/",
    "https://affiliateman.site/qa9/",
    "https://affiliateman.site/qa_1/",
    "https://affiliateman.site/rakutenafii/",
    "https://affiliateman.site/salesblog/",
    "https://affiliateman.site/tiktok_baz/",
    "https://affiliateman.site/tiktok_contentsbaz/",
    "https://affiliateman.site/tiktok_monetize/",
    "https://affiliateman.site/trend/",
    "https://affiliateman.site/twitter-20man/",
    "https://affiliateman.site/twitter_anya/",
    "https://affiliateman.site/wp-content/uploads/2022/11/SNS攻略サロンインタビュー資料.pdf",
    "https://affiliateman.site/wp-content/uploads/2022/11/マイメアリー資料-2.pdf"
]

categories = {
    'qa': [],
    'output': [],
    'tiktok': [],
    'twitter': [],
    'instagram': [],
    'pdf': [],
    'other': []
}

for url in missing_urls:
    if '/qa' in url:
        categories['qa'].append(url)
    elif '/output' in url or '/out_' in url:
        categories['output'].append(url)
    elif '/tiktok' in url:
        categories['tiktok'].append(url)
    elif '/twitter' in url:
        categories['twitter'].append(url)
    elif '/instagram' in url:
        categories['instagram'].append(url)
    elif '.pdf' in url:
        categories['pdf'].append(url)
    else:
        categories['other'].append(url)

print("=" * 60)
print("未取得URLの分類")
print("=" * 60)

for category, urls in categories.items():
    if urls:
        print(f"\n【{category.upper()}】({len(urls)}件)")
        for url in urls:
            slug = url.split('/')[-2] if url.endswith('/') else url.split('/')[-1]
            print(f"  - {slug:30s} {url}")

print("\n" + "=" * 60)
print("推奨アクション")
print("=" * 60)

print("""
1. 質疑応答（QA）ページ: 10件
   → 既に一部取得済みの可能性。重複確認が必要
   → 質疑応答は重要コンテンツなので、すべて取得推奨

2. アウトプット（OUTPUT）ページ: 8件
   → コンテンツの性質を確認後、取得判断

3. TikTok追加ページ: 3件
   → TikTokノウハウの補完として取得推奨

4. Twitter追加ページ: 2件
   → Twitterノウハウの補完として取得推奨

5. Instagram追加ページ: 1件
   → 取得推奨

6. PDFファイル: 2件
   → 資料として重要。ダウンロード推奨

7. その他: 14件
   → 個別に内容確認が必要
   - main, movies, present, line, dm などは重要な可能性
""")
