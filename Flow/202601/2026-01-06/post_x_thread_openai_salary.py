#!/usr/bin/env python3
"""
X投稿（案3: OpenAI平均年収2.2億円）をLate APIで予約投稿

仕様:
- v0.4.5対応（エンゲージメント指標除外、URL配置修正）
- 7ツイートスレッド
- 予約投稿: 2026-01-06 19:40 JST
"""

import sys
import os
import json
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

# プロジェクトルートをパスに追加
sys.path.insert(0, '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts')

from late_api_post import get_account_id, load_config

def main():
    """メイン処理"""

    # ツイート内容（v0.4.5準拠: エンゲージメント指標なし）
    tweets = [
        # 1/7（フック + 導入）
        """けっこう勘違いしている人多いんだけど、OpenAIが社員に平均年収2.2億円払う理由、「いい会社」で片付けたら本質を見誤ります。

売上の半分が人件費に消えてる。この数字には、危険なシグナルが隠れてる。""",

        # 2/7（年収内訳の詳細）
        """年収2.2億円の内訳：
- 基本給: 3,000万円
- RSU（株式報酬）: 1.9億円

ポイントは、現金ではなく「未公開株」で支払ってる点。つまり、社員は「将来の期待値」に賭けてる。IPOが頓挫したら、この報酬は紙切れになる。""",

        # 3/7（財務実態の深堀り）
        """売上37億ドル、人件費18.5億ドル。

普通のSaaS企業なら人件費率は15-25%。OpenAIは50%。しかも営業利益率はマイナス。

これは「健全な成長企業」ではなく、「投資家の資金で人材を買い漁ってる状態」です。持続可能性に疑問符がつく。""",

        # 4/7（シリコンバレー戦略の解説）
        """なぜこんなことが可能なのか？

答え: マイクロソフトを含む投資家が133億ドル（約2兆円）を注入してるから。

これは「人材への投資」ではなく、「市場独占のための人材囲い込み戦略」。競合を潰すために、市場から優秀なAI人材を一掃してる。""",

        # 5/7（人材獲得競争の本質）
        """GoogleもMetaもAnthropicも、同じゲームに参加してる。

AI人材の争奪戦は、もはや「給与の競争」ではなく「資金力の競争」。

普通のスタートアップがこの市場に参入するのは、ほぼ不可能になってる。資金調達できない企業は、人材を確保できない。""",

        # 6/7（投資家視点の警告）
        """投資家の視点で見ると：

- 売上37億ドルに対して評価額1,570億ドル（PSR 42倍）
- 人件費が売上の50%で営業赤字
- IPO時期は未定、流動性ゼロ

「いい会社」どころか、これはバブルの典型的なシグナルです。冷静に見るべき。""",

        # 7/7（まとめ + CTA）
        """OpenAIの2.2億円年収が示してるのは：

1. AI業界の人材バブル
2. 投資家資金依存の危うさ
3. 市場独占のための焦土作戦

「高給=いい会社」じゃない。この数字の裏にあるリスクを見抜けるかどうかで、あなたの投資判断の質が決まります。

冷静ですか？"""
    ]

    # アカウントID取得
    account_id = get_account_id("twitter")

    # 予約投稿時刻: 2026-01-06 19:40 JST
    scheduled_time = datetime(2026, 1, 6, 19, 40, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
    scheduled_time_iso = scheduled_time.isoformat()

    print(f"📅 予約投稿時刻: {scheduled_time_iso}")
    print(f"📱 スレッド数: {len(tweets)}ツイート")
    print(f"🔑 アカウントID: {account_id}")
    print()

    # Late API設定読み込み
    config = load_config()
    api_key = config["api_key"]
    base_url = config["base_url"]

    # リクエストボディ構築
    request_body = {
        "content": tweets[0],  # 1ツイート目
        "scheduledFor": scheduled_time_iso,
        "timezone": "Asia/Tokyo",
        "platforms": [{
            "platform": "twitter",
            "accountId": account_id,
            "platformSpecificData": {
                "threadItems": [{"text": tweet} for tweet in tweets[1:]],  # 2-7ツイート目
                "enableNotifications": True
            }
        }]
    }

    # Late API投稿
    print("🚀 Late APIへ投稿中...")
    print(f"   リクエスト: {json.dumps(request_body, ensure_ascii=False, indent=2)[:500]}...")

    try:
        response = requests.post(
            f"{base_url}/posts",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json=request_body,
            timeout=30
        )

        if response.status_code == 200 or response.status_code == 201:
            result = response.json()
            print("✅ 投稿成功！")
            print(f"   投稿ID: {result.get('id', 'N/A')}")
            print(f"   ステータス: {result.get('status', 'N/A')}")
            print(f"   予約時刻: {scheduled_time_iso}")
        else:
            print("❌ 投稿失敗")
            print(f"   ステータスコード: {response.status_code}")
            print(f"   レスポンス: {response.text}")
            sys.exit(1)

    except Exception as e:
        print(f"❌ エラー発生: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
