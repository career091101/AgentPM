# Phase 4: API Integration v2

SNS自動化スキル v2のAPI連携・予約投稿フェーズ。Late APIを使用してLinkedIn/X/Threadsに予約投稿を実行します。

**Version**: 2.0（v2対応版）

---

## 概要

Phase 3で生成した投稿を、Late APIを使用して各プラットフォームに予約投稿します。

**主要機能**:
1. **LinkedIn 3日分散投稿**: 既存予約を検出し、空き日3日に自動分散
2. **X/Threads同時刻投稿**: 同じTop記事を同時刻（7:30, 12:00, 20:00）に投稿

**所要時間**: 5-10分

---

## 実行フロー

### STEP 4.0: 既存予約検出（30秒）

**目的**: LinkedIn 8:00 AM JSTの既存予約を検出し、投稿可能な空き日を特定

**Late API実行**:
```python
import requests
from datetime import datetime, timedelta
import pytz

JST = pytz.timezone('Asia/Tokyo')
LATE_API_BASE = "https://api.late.dev/api/v1"
LATE_API_TOKEN = os.getenv("LATE_API_TOKEN")

def get_scheduled_posts(platform="linkedin"):
    """
    Late APIから既存の予約投稿を取得

    Args:
        platform: プラットフォーム名（"linkedin", "twitter", "threads"）

    Returns:
        list: 予約済み投稿のリスト
    """
    headers = {
        "Authorization": f"Bearer {LATE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        f"{LATE_API_BASE}/posts?status=scheduled",
        headers=headers
    )

    if response.status_code != 200:
        raise Exception(f"Late API error: {response.text}")

    all_posts = response.json()

    # プラットフォームでフィルタリング
    filtered_posts = [
        post for post in all_posts
        if any(p['platform'] == platform for p in post.get('platforms', []))
    ]

    return filtered_posts

# 実行例
existing_linkedin_posts = get_scheduled_posts(platform="linkedin")
print(f"既存LinkedIn予約: {len(existing_linkedin_posts)}件")
```

**出力**:
- 既存予約投稿リスト
- 予約済み日時情報

---

### STEP 4.1: LinkedIn空き日3日検出（30秒）

**目的**: 8:00 AM JSTの空き日を3日間検出

**関数実装**:
```python
def find_available_linkedin_dates(days=7, time="08:00"):
    """
    Late APIから既存予約を取得し、空いている最初の3日を検出

    Args:
        days: 検索期間（デフォルト7日間）
        time: 投稿時刻（デフォルト08:00 JST）

    Returns:
        list: 空いている3つの日付（ISO 8601形式）
    """
    # 1. Late APIから既存予約を取得
    existing_posts = get_scheduled_posts(platform="linkedin")

    # 2. 指定時刻の予約済み日付を抽出
    reserved_dates = set()
    for post in existing_posts:
        scheduled_for = post.get('scheduledFor')
        if scheduled_for:
            dt = datetime.fromisoformat(scheduled_for.replace('Z', '+00:00'))
            dt_jst = dt.astimezone(JST)

            # 時刻が一致する場合は予約済みとしてマーク
            if dt_jst.strftime("%H:%M") == time:
                reserved_dates.add(dt_jst.date())

    # 3. 今後N日間から空き日を検出
    available_dates = []
    current_date = datetime.now(tz=JST)

    for i in range(days):
        check_date = current_date + timedelta(days=i)

        # 土日を除外（オプション）
        # if check_date.weekday() >= 5:  # 5=土曜, 6=日曜
        #     continue

        if check_date.date() not in reserved_dates:
            scheduled_datetime = check_date.replace(
                hour=int(time.split(':')[0]),
                minute=int(time.split(':')[1]),
                second=0,
                microsecond=0
            )
            available_dates.append(scheduled_datetime.isoformat())

        if len(available_dates) == 3:
            break

    if len(available_dates) < 3:
        raise Exception(
            f"空き日が{len(available_dates)}日しか見つかりませんでした。"
            f"検索期間を{days}日より長く設定してください。"
        )

    return available_dates

# 使用例
available_dates = find_available_linkedin_dates(days=7, time="08:00")
print(f"利用可能日付:")
for i, date in enumerate(available_dates, 1):
    print(f"  {i}. {date}")
# → ['2026-01-13T08:00:00+09:00', '2026-01-15T08:00:00+09:00', '2026-01-17T08:00:00+09:00']
```

**出力**:
- 空き日3つの日付（ISO 8601形式）
- 例: `['2026-01-13T08:00:00+09:00', '2026-01-15T08:00:00+09:00', '2026-01-17T08:00:00+09:00']`

**エラーハンドリング**:
- 空き日が3日未満の場合: 検索期間を14日に延長して再試行
- 14日でも3日未満の場合: ユーザーに警告、手動調整を促す

---

### STEP 4.2: 投稿コンテンツ抽出（1分）

**目的**: Phase 3出力ファイルから投稿コンテンツを抽出

**処理**:
```python
import json

def extract_linkedin_posts(file_path):
    """
    Phase 3出力からLinkedIn投稿3案を抽出

    Args:
        file_path: linkedin_posts_v2_{date}.md のパス

    Returns:
        list: LinkedIn投稿3案のリスト
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 正規表現で案1, 案2, 案3を抽出
    import re

    posts = []
    pattern = r'## 案(\d+):.*?\n\n### 投稿本文.*?\n\n(.*?)\n\n\(ソースはコメント欄に記載\)'
    matches = re.findall(pattern, content, re.DOTALL)

    for match in matches:
        post_number, post_content = match
        posts.append({
            'post_number': int(post_number),
            'content': post_content.strip()
        })

    return posts

def extract_x_threads(file_path):
    """
    Phase 3出力からXスレッド3件を抽出

    Args:
        file_path: x_threads_v2_{date}.json のパス

    Returns:
        list: Xスレッド3件のリスト
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data['threads']

def extract_threads_posts(file_path):
    """
    Phase 3出力からThreads投稿3件を抽出

    Args:
        file_path: threads_posts_v2_{date}.json のパス

    Returns:
        list: Threads投稿3件のリスト
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data['posts']

# 使用例
linkedin_posts = extract_linkedin_posts('Flow/202601/2026-01-12/linkedin_posts_v2_20260112.md')
x_threads = extract_x_threads('Flow/202601/2026-01-12/x_threads_v2_20260112.json')
threads_posts = extract_threads_posts('Flow/202601/2026-01-12/threads_posts_v2_20260112.json')

print(f"LinkedIn投稿: {len(linkedin_posts)}案")
print(f"Xスレッド: {len(x_threads)}件")
print(f"Threads投稿: {len(threads_posts)}件")
```

**出力**:
- LinkedIn投稿3案
- Xスレッド3件
- Threads投稿3件

---

### STEP 4.3: Late API予約投稿実行（2-5分）

**目的**: 各プラットフォームに予約投稿を実行

#### 4.3.1: LinkedIn 3日分散投稿（1-2分）

**スケジュール設定**:
```python
# STEP 1: 空き日とLinkedIn投稿を紐付け
linkedin_schedule = [
    {"post": linkedin_posts[0], "date": available_dates[0], "topic": "Top 1"},  # 案1 → 1日目
    {"post": linkedin_posts[1], "date": available_dates[1], "topic": "Top 2"},  # 案2 → 2日目
    {"post": linkedin_posts[2], "date": available_dates[2], "topic": "Top 3"}   # 案3 → 3日目
]

print("LinkedInスケジュール:")
for schedule in linkedin_schedule:
    print(f"  {schedule['topic']}: {schedule['date']}")
```

**Late APIペイロード**:
```python
def schedule_linkedin_post(content, scheduled_for, linkedin_account_id):
    """
    Late APIでLinkedIn予約投稿

    Args:
        content: 投稿本文
        scheduled_for: ISO 8601形式の日時
        linkedin_account_id: LinkedInアカウントID

    Returns:
        dict: Late APIレスポンス
    """
    headers = {
        "Authorization": f"Bearer {LATE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        'content': content,  # 投稿本文（必須）
        'scheduledFor': scheduled_for,  # ISO 8601形式
        'timezone': 'Asia/Tokyo',
        'platforms': [{
            'platform': 'linkedin',
            'accountId': linkedin_account_id
        }],
        'publishNow': False,
        'crosspostingEnabled': False
    }

    response = requests.post(
        f"{LATE_API_BASE}/posts",
        headers=headers,
        json=payload
    )

    if response.status_code not in [200, 201]:
        raise Exception(f"Late API error: {response.text}")

    return response.json()

# LinkedIn アカウントIDを取得（環境変数またはconfigから）
LINKEDIN_ACCOUNT_ID = os.getenv("LATE_API_LINKEDIN_ACCOUNT_ID")

# 各投稿をスケジュール
for schedule in linkedin_schedule:
    try:
        result = schedule_linkedin_post(
            content=schedule['post']['content'],
            scheduled_for=schedule['date'],
            linkedin_account_id=LINKEDIN_ACCOUNT_ID
        )
        print(f"✅ LinkedIn {schedule['topic']} 予約成功: {schedule['date']}")
    except Exception as e:
        print(f"❌ LinkedIn {schedule['topic']} 予約失敗: {e}")
```

**出力**:
- 予約成功/失敗のログ
- 予約投稿ID

#### 4.3.2: X/Threads同時刻投稿（2-3分）

**スケジュール設定**:
```python
# STEP 1: 今日の日付を取得
today = datetime.now(tz=JST).date()

# STEP 2: X/Threadsを同時刻に設定
x_threads_schedule = [
    {
        "time": "07:30",
        "x_thread": x_threads[0],        # Top 1スレッド
        "threads_post": threads_posts[0], # Top 1投稿
        "date": today,
        "topic": "Top 1"
    },
    {
        "time": "12:00",
        "x_thread": x_threads[1],        # Top 2スレッド
        "threads_post": threads_posts[1], # Top 2投稿
        "date": today,
        "topic": "Top 2"
    },
    {
        "time": "20:00",
        "x_thread": x_threads[2],        # Top 3スレッド
        "threads_post": threads_posts[2], # Top 3投稿
        "date": today,
        "topic": "Top 3"
    }
]

print("X/Threadsスケジュール:")
for schedule in x_threads_schedule:
    scheduled_datetime = f"{schedule['date']}T{schedule['time']}:00+09:00"
    print(f"  {schedule['topic']}: {scheduled_datetime}")
```

**Late APIペイロード（Xスレッド）**:
```python
def schedule_x_thread(thread_data, scheduled_for, twitter_account_id):
    """
    Late APIでXスレッド予約投稿

    Args:
        thread_data: Xスレッドデータ（tweets配列を含む）
        scheduled_for: ISO 8601形式の日時
        twitter_account_id: TwitterアカウントID

    Returns:
        dict: Late APIレスポンス
    """
    headers = {
        "Authorization": f"Bearer {LATE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    tweets = thread_data['tweets']

    payload = {
        'content': tweets[0]['content'],  # 1ツイート目（必須）
        'scheduledFor': scheduled_for,
        'timezone': 'Asia/Tokyo',
        'platforms': [{
            'platform': 'twitter',
            'accountId': twitter_account_id,
            'platformSpecificData': {
                'threadItems': [
                    {'content': tweet['content']}
                    for tweet in tweets[1:]  # 2ツイート目以降
                ]
            }
        }],
        'publishNow': False,
        'crosspostingEnabled': False
    }

    response = requests.post(
        f"{LATE_API_BASE}/posts",
        headers=headers,
        json=payload
    )

    if response.status_code not in [200, 201]:
        raise Exception(f"Late API error: {response.text}")

    return response.json()

# Twitterアカウント IDを取得
TWITTER_ACCOUNT_ID = os.getenv("LATE_API_TWITTER_ACCOUNT_ID")

# 各スレッドをスケジュール
for schedule in x_threads_schedule:
    scheduled_datetime = f"{schedule['date']}T{schedule['time']}:00+09:00"

    try:
        result = schedule_x_thread(
            thread_data=schedule['x_thread'],
            scheduled_for=scheduled_datetime,
            twitter_account_id=TWITTER_ACCOUNT_ID
        )
        print(f"✅ X {schedule['topic']} 予約成功: {scheduled_datetime}")
    except Exception as e:
        print(f"❌ X {schedule['topic']} 予約失敗: {e}")
```

**Late APIペイロード（Threads）**:
```python
def schedule_threads_post(threads_data, scheduled_for, threads_account_id):
    """
    Late APIでThreads予約投稿（単一 or スレッド対応）

    Args:
        threads_data: Threads投稿データ
        scheduled_for: ISO 8601形式の日時
        threads_account_id: ThreadsアカウントID

    Returns:
        dict: Late APIレスポンス
    """
    headers = {
        "Authorization": f"Bearer {LATE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    # type判定: "single" or "thread"
    if threads_data['type'] == 'single':
        # 単一投稿
        payload = {
            'content': threads_data['content'],
            'scheduledFor': scheduled_for,
            'timezone': 'Asia/Tokyo',
            'platforms': [{
                'platform': 'threads',
                'accountId': threads_account_id
            }],
            'publishNow': False,
            'crosspostingEnabled': False
        }
    else:
        # スレッド投稿（2-3投稿）
        posts = threads_data['posts']
        payload = {
            'content': posts[0]['content'],  # 1投稿目（必須）
            'scheduledFor': scheduled_for,
            'timezone': 'Asia/Tokyo',
            'platforms': [{
                'platform': 'threads',
                'accountId': threads_account_id,
                'platformSpecificData': {
                    'threadItems': [
                        {'content': post['content']}
                        for post in posts[1:]  # 2投稿目以降
                    ]
                }
            }],
            'publishNow': False,
            'crosspostingEnabled': False
        }

    response = requests.post(
        f"{LATE_API_BASE}/posts",
        headers=headers,
        json=payload
    )

    if response.status_code not in [200, 201]:
        raise Exception(f"Late API error: {response.text}")

    return response.json()

# ThreadsアカウントIDを取得
THREADS_ACCOUNT_ID = os.getenv("LATE_API_THREADS_ACCOUNT_ID")

# 各Threads投稿をスケジュール（Xと同時刻）
for schedule in x_threads_schedule:
    scheduled_datetime = f"{schedule['date']}T{schedule['time']}:00+09:00"

    try:
        result = schedule_threads_post(
            threads_data=schedule['threads_post'],
            scheduled_for=scheduled_datetime,
            threads_account_id=THREADS_ACCOUNT_ID
        )
        print(f"✅ Threads {schedule['topic']} 予約成功: {scheduled_datetime}")
    except Exception as e:
        print(f"❌ Threads {schedule['topic']} 予約失敗: {e}")
```

**出力**:
- X予約成功/失敗のログ（3件）
- Threads予約成功/失敗のログ（3件）
- 予約投稿ID

---

### STEP 4.4: 予約結果サマリー生成（30秒）

**目的**: 予約投稿の結果をサマリーファイルとして出力

**処理**:
```python
def generate_schedule_summary(
    linkedin_schedule,
    x_threads_schedule,
    output_path
):
    """
    予約結果サマリーを生成

    Args:
        linkedin_schedule: LinkedIn予約スケジュール
        x_threads_schedule: X/Threads予約スケジュール
        output_path: 出力ファイルパス
    """
    summary = f"""# SNS予約投稿サマリー v2

**生成日時**: {datetime.now(tz=JST).isoformat()}

---

## LinkedIn（3日分散投稿）

| 案 | トピック | 予約日時 | ステータス |
|----|---------|---------|-----------|
"""

    for schedule in linkedin_schedule:
        summary += f"| 案{schedule['post']['post_number']} | {schedule['topic']} | {schedule['date']} | ✅ 予約完了 |\n"

    summary += "\n---\n\n## X（3スレッド同時刻投稿）\n\n"
    summary += "| トピック | 予約日時 | ツイート数 | ステータス |\n"
    summary += "|---------|---------|-----------|----------|\n"

    for schedule in x_threads_schedule:
        scheduled_datetime = f"{schedule['date']}T{schedule['time']}:00+09:00"
        tweet_count = schedule['x_thread']['total_tweets']
        summary += f"| {schedule['topic']} | {scheduled_datetime} | {tweet_count} | ✅ 予約完了 |\n"

    summary += "\n---\n\n## Threads（3投稿同時刻投稿）\n\n"
    summary += "| トピック | 予約日時 | タイプ | ステータス |\n"
    summary += "|---------|---------|--------|----------|\n"

    for schedule in x_threads_schedule:
        scheduled_datetime = f"{schedule['date']}T{schedule['time']}:00+09:00"
        post_type = schedule['threads_post']['type']
        type_label = "単一" if post_type == "single" else f"スレッド({schedule['threads_post'].get('total_posts', 'N')}投稿)"
        summary += f"| {schedule['topic']} | {scheduled_datetime} | {type_label} | ✅ 予約完了 |\n"

    summary += "\n---\n\n## 投稿総数\n\n"
    summary += f"- **LinkedIn**: 3案（1案/日×3日）\n"
    summary += f"- **X**: 3スレッド（計{sum(s['x_thread']['total_tweets'] for s in x_threads_schedule)}ツイート）\n"

    threads_count = 0
    for s in x_threads_schedule:
        if s['threads_post']['type'] == 'single':
            threads_count += 1
        else:
            threads_count += s['threads_post'].get('total_posts', 1)
    summary += f"- **Threads**: {threads_count}投稿\n"
    summary += f"- **合計**: LinkedIn 3案 + X {sum(s['x_thread']['total_tweets'] for s in x_threads_schedule)}ツイート + Threads {threads_count}投稿\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"✅ サマリー生成完了: {output_path}")

# 実行例
generate_schedule_summary(
    linkedin_schedule,
    x_threads_schedule,
    'Flow/202601/2026-01-12/schedule_summary_v2_20260112.md'
)
```

**出力ファイル例**:
```markdown
# SNS予約投稿サマリー v2

**生成日時**: 2026-01-12T10:00:00+09:00

---

## LinkedIn（3日分散投稿）

| 案 | トピック | 予約日時 | ステータス |
|----|---------|---------|-----------|
| 案1 | Top 1 | 2026-01-13T08:00:00+09:00 | ✅ 予約完了 |
| 案2 | Top 2 | 2026-01-15T08:00:00+09:00 | ✅ 予約完了 |
| 案3 | Top 3 | 2026-01-17T08:00:00+09:00 | ✅ 予約完了 |

---

## X（3スレッド同時刻投稿）

| トピック | 予約日時 | ツイート数 | ステータス |
|---------|---------|-----------|----------|
| Top 1 | 2026-01-12T07:30:00+09:00 | 6 | ✅ 予約完了 |
| Top 2 | 2026-01-12T12:00:00+09:00 | 7 | ✅ 予約完了 |
| Top 3 | 2026-01-12T20:00:00+09:00 | 5 | ✅ 予約完了 |

---

## Threads（3投稿同時刻投稿）

| トピック | 予約日時 | タイプ | ステータス |
|---------|---------|--------|----------|
| Top 1 | 2026-01-12T07:30:00+09:00 | 単一 | ✅ 予約完了 |
| Top 2 | 2026-01-12T12:00:00+09:00 | スレッド(2投稿) | ✅ 予約完了 |
| Top 3 | 2026-01-12T20:00:00+09:00 | 単一 | ✅ 予約完了 |

---

## 投稿総数

- **LinkedIn**: 3案（1案/日×3日）
- **X**: 3スレッド（計18ツイート）
- **Threads**: 4投稿
- **合計**: LinkedIn 3案 + X 18ツイート + Threads 4投稿
```

---

## エラーハンドリング

### LinkedIn予約エラー

**ケース1: 空き日不足（3日未満）**
- **対応**: 検索期間を14日に延長して再試行
- **14日でも不足**: ユーザーに警告、手動調整を促す

**ケース2: Late APIエラー（401/403）**
- **対応**: トークン再取得を促す
- **ログ**: エラーメッセージを詳細に記録

**ケース3: ネットワークエラー**
- **対応**: 3回リトライ（5秒間隔）
- **3回失敗**: エラーログを出力、ユーザーに通知

### X/Threads予約エラー

**ケース1: スレッド投稿エラー**
- **対応**: threadItems形式を確認し、再試行
- **最大リトライ**: 2回

**ケース2: 文字数超過エラー**
- **対応**: Phase 3に戻り、280文字以内に再生成
- **自動修正**: 不可（品質低下のため）

**ケース3: 同時刻衝突エラー**
- **対応**: 1分後にずらして再試行（7:31, 12:01, 20:01）
- **最大リトライ**: 1回

---

## 参照

- **Late API公式ドキュメント**: https://late.dev/docs/api
- **Phase 3出力**: LinkedIn/X/Threads投稿データ
- **環境変数**:
  - `LATE_API_TOKEN`: Late APIトークン
  - `LATE_API_LINKEDIN_ACCOUNT_ID`: LinkedInアカウントID
  - `LATE_API_TWITTER_ACCOUNT_ID`: TwitterアカウントID
  - `LATE_API_THREADS_ACCOUNT_ID`: ThreadsアカウントID

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|-----------|---------|
| 2026-01-12 | 2.0 | v2対応版作成。LinkedIn 3日分散投稿、X/Threads同時刻投稿追加 |

---

**実装日**: 2026-01-12
**バージョン**: 2.0（sns-automation-v2対応）
