#!/usr/bin/env python3
"""
X Timeline 収集スクリプト（修正版）
エンゲージメント指標の取得を修正して再収集
"""

import json
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
DATA_DIR = PROJECT_ROOT / "data"

def main():
    print("🚀 X Timeline 収集開始（修正版）")

    # Chromeオプション設定
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # 既存のChromeプロファイルを使用（ログイン済み）
    chrome_options.add_argument("user-data-dir=/Users/yuichi/Library/Application Support/Google/Chrome")
    chrome_options.add_argument("profile-directory=Default")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # X.comに遷移
        print("📱 X.comに遷移中...")
        driver.get("https://x.com/home")
        time.sleep(5)

        # 修正版スクリプトを注入
        print("🔧 修正版スクリプトを注入中...")
        collector_script = (SCRIPTS_DIR / "x_timeline_collector_fixed.js").read_text()
        driver.execute_script(collector_script)
        time.sleep(1)

        # 収集実行スクリプト
        collection_script = """
        async function runCollectionCycles(totalCycles) {
          console.log(`📊 ${totalCycles}サイクルの収集を開始します...`);

          for (let i = 1; i <= totalCycles; i++) {
            const result = window.extractTweetsAndAccumulateFixed();
            console.log(`Cycle ${result.cycle}/${totalCycles}: 新規${result.newTweets}件, 重複${result.duplicates}件, 累計${result.totalUnique}件`);

            window.scrollBy(0, 1000);
            await new Promise(resolve => setTimeout(resolve, 3000));
          }

          console.log('✅ 収集完了！');
          return JSON.parse(localStorage.getItem('x_timeline_collection_backup'));
        }

        return await runCollectionCycles(20);
        """

        print("📊 20サイクルの収集を開始...")
        result = driver.execute_async_script(collection_script)

        # データを保存
        output_file = DATA_DIR / "x_timeline_20260101_fixed.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"✅ データを保存しました: {output_file}")

        # 統計を表示
        all_tweets = result['allTweets']
        with_engagement = [t for t in all_tweets if t['engagement_score'] > 0]

        print(f"\n📊 収集結果:")
        print(f"  総ツイート数: {len(all_tweets)}件")
        print(f"  エンゲージメント取得成功: {len(with_engagement)}件 ({len(with_engagement)/len(all_tweets)*100:.1f}%)")
        print(f"  サイクル数: {result['metadata']['cycleCount']}")

        # Top 30を作成
        sorted_tweets = sorted(all_tweets, key=lambda t: t['engagement_score'], reverse=True)
        top30 = sorted_tweets[:30]

        top30_file = DATA_DIR / "x_timeline_20260101_fixed_top30.json"
        with open(top30_file, 'w', encoding='utf-8') as f:
            json.dump(top30, f, ensure_ascii=False, indent=2)

        print(f"📌 Top 30を保存しました: {top30_file}")

        # Top 5を表示
        print(f"\n🏆 Top 5 エンゲージメント:")
        for i, tweet in enumerate(top30[:5], 1):
            print(f"  {i}. @{tweet['author_username']}: {tweet['engagement_score']}点 (♥{tweet['likes']} 🔁{tweet['retweets']} 💬{tweet['replies']})")

    finally:
        print("\n⏸️  10秒後にブラウザを閉じます...")
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    main()
