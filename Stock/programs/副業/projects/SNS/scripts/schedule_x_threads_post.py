#!/usr/bin/env python3
"""
Late API経由でX/Threads投稿をスケジュール予約（明日20時）
"""

import os
import json
import requests

# 環境変数から直接読み込み
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
with open(env_path, 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            key, value = line.split('=', 1)
            value = value.strip('"').strip("'")
            if '#' in value:
                value = value.split('#')[0].strip()
            os.environ[key] = value

LATE_API_KEY = os.environ.get('LATE_API_KEY')
LATE_X_ACCOUNT_ID = "69576e284207e06f4ca837e4"
LATE_THREADS_ACCOUNT_ID = "69576df34207e06f4ca837e3"

# X用投稿（スレッド形式 - 各280文字以内）
x_thread = [
    """Googleの社員が、Geminiではなく「Claude Code」を使っている。

この事実、衝撃じゃない？

世界最高峰のAI企業で働く人たちが、自社製品ではなく競合のツールを選んでいる。

理由はシンプル。
「仕事が終わるから」

🧵続く""",

    """Dario Amodei（Anthropic CEO）が最近こう言っていた。

「我々のコーディングエージェントは、人間のエンジニアと同等の能力を持ち始めている」

これ、本当だった。

僕自身、Claude Codeを使い始めて6ヶ月。
以前なら1週間かかっていた開発が、1日で終わる。""",

    """正直、怖くなった。

「このツールがなかったら、自分の価値は何なのか」

でも、すぐに気づいた。

AIを使いこなせる人間の価値が、今まさに爆発的に高まっているということを。""",

    """Sam Altmanも言っていた。
「2026年末までに、AIエージェントが本格的に仕事を代替し始める」

これは脅しじゃない。チャンスの告知だ。

今、AIツールを使いこなす側に回るか。
それとも、代替される側に回るか。

その分岐点が、まさに今年。

あなたはどっち側にいる？"""
]

# Threads用投稿（スレッド形式 - X版と同じ内容）
threads_thread = [
    """Googleの社員が、Geminiではなく「Claude Code」を使っている。

この事実、衝撃じゃない？

世界最高峰のAI企業で働く人たちが、自社製品ではなく競合のツールを選んでいる。

理由はシンプル。
「仕事が終わるから」

🧵続く""",

    """Dario Amodei（Anthropic CEO）が最近こう言っていた。

「我々のコーディングエージェントは、人間のエンジニアと同等の能力を持ち始めている」

これ、本当だった。

僕自身、Claude Codeを使い始めて6ヶ月。
以前なら1週間かかっていた開発が、1日で終わる。""",

    """正直、怖くなった。

「このツールがなかったら、自分の価値は何なのか」

でも、すぐに気づいた。

AIを使いこなせる人間の価値が、今まさに爆発的に高まっているということを。""",

    """Sam Altmanも言っていた。
「2026年末までに、AIエージェントが本格的に仕事を代替し始める」

これは脅しじゃない。チャンスの告知だ。

今、AIツールを使いこなす側に回るか。
それとも、代替される側に回るか。

その分岐点が、まさに今年。

あなたはどっち側にいる？"""
]

url = 'https://getlate.dev/api/v1/posts'
headers = {
    'Authorization': f'Bearer {LATE_API_KEY}',
    'Content-Type': 'application/json'
}

results = []

# X投稿（スレッド形式）
print('=' * 50)
print('📤 Scheduling X (Twitter) thread post...')
print(f'   Scheduled for: 2026-01-05 20:00 JST (明日夜8時)')
print(f'   Thread posts: {len(x_thread)} items')

x_payload = {
    'content': x_thread[0],
    'scheduledFor': '2026-01-05T20:00:00+09:00',
    'timezone': 'Asia/Tokyo',
    'platforms': [
        {
            'platform': 'twitter',
            'accountId': LATE_X_ACCOUNT_ID,
            'platformSpecificData': {
                'threadItems': [{'content': post} for post in x_thread[1:]]
            }
        }
    ],
    'publishNow': False,
    'crosspostingEnabled': False
}

response = requests.post(url, headers=headers, json=x_payload)
result = response.json()

if response.status_code in [200, 201]:
    print('✅ X thread scheduled successfully!')
    post_id = result.get('post', {}).get('_id', 'N/A')
    print(f'   Post ID: {post_id}')
    results.append({'platform': 'X', 'post_id': post_id, 'status': 'scheduled'})
else:
    print(f'❌ X Error: {response.status_code}')
    print(f'   Response: {response.text}')
    results.append({'platform': 'X', 'error': response.text})

# Threads投稿（スレッド形式）
print('=' * 50)
print('📤 Scheduling Threads thread post...')
print(f'   Scheduled for: 2026-01-05 20:00 JST (明日夜8時)')
print(f'   Thread posts: {len(threads_thread)} items')

threads_payload = {
    'content': threads_thread[0],
    'scheduledFor': '2026-01-05T20:00:00+09:00',
    'timezone': 'Asia/Tokyo',
    'platforms': [
        {
            'platform': 'threads',
            'accountId': LATE_THREADS_ACCOUNT_ID,
            'platformSpecificData': {
                'threadItems': [{'content': post} for post in threads_thread[1:]]
            }
        }
    ],
    'publishNow': False,
    'crosspostingEnabled': False
}

response = requests.post(url, headers=headers, json=threads_payload)
result = response.json()

if response.status_code in [200, 201]:
    print('✅ Threads thread scheduled successfully!')
    post_id = result.get('post', {}).get('_id', 'N/A')
    print(f'   Post ID: {post_id}')
    results.append({'platform': 'Threads', 'post_id': post_id, 'status': 'scheduled', 'format': 'thread'})
else:
    print(f'❌ Threads Error: {response.status_code}')
    print(f'   Response: {response.text}')
    results.append({'platform': 'Threads', 'error': response.text})

# 結果保存
print('=' * 50)
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
result_file = os.path.join(data_dir, 'post_result_scheduled_20260105200000_x_threads.json')
with open(result_file, 'w', encoding='utf-8') as f:
    json.dump({
        'scheduled_time': '2026-01-05T20:00:00+09:00',
        'results': results
    }, f, ensure_ascii=False, indent=2)
print(f'📁 Results saved to: {result_file}')
print('🎉 All done!')
