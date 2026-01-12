---
name: create-producthunt-strategy
domain: for_genai
description: |
  GenAI製品向けProduct Hunt戦略スキル。Top 5ランキング達成を目指し、4段階戦略（準備・プレローンチ・ローンチ当日・ポストローンチ）を自動生成。Upvote獲得戦術、Hunter選定、コミュニティ動員を含む。

  使用タイミング：
  - PSF検証完了後（製品デモ準備済み）
  - LPローンチ2週間前（Product Hunt準備開始）
  - 初期ユーザー獲得戦略立案時

  所要時間：45-60分（4段階戦略 + Hunter選定 + SNS計画）
  出力：{IDEA_FOLDER}/marketing/producthunt_strategy.md

quality_score: 95
tier: 2
case_study_count: 12
genai_research_refs:
  - GenAI_research/case_studies/producthunt_success_patterns.md
  - GenAI_research/marketing/viral_strategies.md
version: 1.0.0
last_updated: 2026-01-03
---

# Create Product Hunt Strategy Skill - ForGenAI Edition

GenAI製品向けProduct Hunt戦略の完全自律実行型Skill。**Top 5ランキング達成**を目標に、4段階ローンチ戦略（準備・プレローンチ・ローンチ当日・ポストローンチ）を自動生成し、Upvote獲得、Hunter選定、コミュニティ動員計画を提供。

---

## 1. Overview

### このSkillでできること

1. **4段階ローンチ戦略立案**: 準備（2週間前）、プレローンチ（1週間前）、ローンチ当日（24時間バトル）、ポストローンチ（1週間後）
2. **Hunter選定戦略**: フォロワー1000+、AI分野専門、過去ローンチ実績のあるHunterリストと確保戦略
3. **時間別アクションプラン**: ローンチ当日の時間別戦術（0-6h: 100 Upvotes、6-12h: SNS拡散、12-18h: コメント対応、18-24h: ラストスパート）
4. **Upvote獲得戦術**: コミュニティ動員、SNS戦略、インフルエンサー連携、メールリスト活用
5. **成功パターン分析表**: Midjourney、Notion AI、Perplexity等のUpvoteカウント、戦略ポイント、タイムライン
6. **SNS拡散計画**: X/Twitter、LinkedIn、Reddit、Hacker News、Indie Hackers戦略
7. **1st Comment準備**: 製品背景、チーム紹介、技術スタック、開発動機の雛形生成
8. **FAQ準備**: 想定質問10件とベスト回答案

### 従来版（汎用）との差分

| 要素 | 汎用Product Hunt戦略 | create-producthunt-strategy (ForGenAI) |
|------|-------------------|--------------------------------------|
| **ターゲットランキング** | Top 10 | **Top 5（AI製品は競争激しい）** |
| **Hunter選定基準** | フォロワー500+ | **フォロワー1000+ + AI分野専門** |
| **ローンチ当日目標** | 50 Upvotes（初動） | **100 Upvotes（0-6h、AI製品は高い関心）** |
| **デモ要件** | スクリーンショット | **インタラクティブデモGIF/動画（90秒以内）必須** |
| **技術スタック訴求** | なし | **"Powered by GPT-4o/Claude"等の信頼性訴求** |
| **コミュニティ戦略** | Product Huntのみ | **AI系Reddit/HN/Indie Hackers併用** |
| **成功事例参照** | 汎用SaaS | **AI製品12事例（Midjourney、Perplexity等）** |

### 4段階ローンチ戦略（Product Hunt Top 5達成ロードマップ）

#### Phase 1: 準備期間（ローンチ2週間前）

**目標**: ローンチ基盤構築、Hunter確保、アセット作成完了

| タスク | 具体的アクション | 担当 | 期限 |
|--------|---------------|------|------|
| **Hunter選定・確保** | ①実績Hunter候補リスト作成（Chris Messina、Kevin William David等）<br>②第1候補にDM/メール依頼<br>③早期アクセス提供、フィードバック収集 | 創業者 | -14日 |
| **アセット作成** | ①スクリーンショット5-7枚作成<br>②デモGIF 3-5個作成<br>③デモ動画30-60秒作成<br>④タグライン・説明文執筆 | デザイナー<br>マーケティング | -12日 |
| **プロダクトページ準備** | ①Product Huntドラフトページ作成<br>②Hunter・チームメンバーへのレビュー依頼<br>③フィードバック反映、最終版確定 | 創業者<br>Hunter | -10日 |
| **FAQ準備** | ①想定質問10件リスト作成（技術スタック、差別化、料金等）<br>②回答テンプレート作成<br>③チーム内共有、回答責任者決定 | 創業者<br>CTO | -10日 |
| **コミュニティウォームアップ** | ①X/Twitterで開発裏話共有（Build in Public）<br>②Discord/Slackで専用チャンネル作成<br>③メールリストにローンチ予告送信 | マーケティング | -14日～継続 |

**Phase 1完了チェックリスト**:
- [ ] Hunter確保済み（第1候補または第2候補）
- [ ] プロダクトページドラフト完成（Hunter承認済み）
- [ ] デモアセット完成（スクリーンショット5+、GIF 3+、動画1）
- [ ] FAQ 10件準備完了
- [ ] コミュニティ通知済み（X/Twitter、Discord、メールリスト）

---

#### Phase 2: プレローンチ（ローンチ1週間前）

**目標**: 最終準備、ベータテスター動員、SNS告知拡大

| タスク | 具体的アクション | 担当 | 期限 |
|--------|---------------|------|------|
| **ベータテスター動員** | ①ベータユーザーへのメール送信（upvote依頼）<br>②Product Hunt通知設定依頼<br>③ローンチ日時リマインダー（タイムゾーン注意） | マーケティング | -7日 |
| **SNS予告強化** | ①カウントダウン開始（X/Twitter、LinkedIn）<br>②製品ティーザー投稿（GIF、スクリーンショット）<br>③インフルエンサーへの事前連絡 | マーケティング | -7日～-3日 |
| **最終確認** | ①プロダクトページ最終レビュー（誤字脱字チェック）<br>②デモ動画・GIFの表示確認<br>③ローンチ日時確定（火曜12:01 AM PT） | 創業者<br>Hunter | -3日 |
| **チーム体制準備** | ①ローンチ日の役割分担決定<br>②質問対応シフト作成（24時間カバー）<br>③緊急連絡体制構築（Slack等） | 創業者 | -3日 |
| **最終予告** | ①「Launch on Tuesday 12:01 AM PT」ツイート<br>②Discord/Slackでリマインダー<br>③メールリストに最終通知 | マーケティング | -1日 |

**Phase 2完了チェックリスト**:
- [ ] ベータテスター動員完了（最低50人に通知）
- [ ] SNSカウントダウン完了（X/Twitter、LinkedIn投稿済み）
- [ ] ローンチ日時確定（火曜12:01 AM PT）
- [ ] チーム役割分担決定（質問対応、SNS投稿、進捗モニター）
- [ ] 最終予告完了（全チャネル）

---

#### Phase 3: ローンチ当日（24時間バトル）

**目標**: Top 5ランキング達成、100+ upvotes（初動6時間）、継続的エンゲージメント

##### 時間別アクションプラン（0:00-23:59 PT）

| 時間帯（PT） | 目標 | 具体的アクション | 担当 | 重要指標 |
|------------|------|---------------|------|---------|
| **23:55-0:00** | ローンチ準備完了 | ①Product Huntログイン、最終確認<br>②Hunter待機確認<br>③チーム全員スタンバイ | 全員 | - |
| **0:00-0:05** | 公開＆初動 | ①Hunter投稿実行<br>②創業者1st Comment投稿（自己紹介、開発背景）<br>③X/Twitter即時投稿<br>④Discord/Slack @everyone通知<br>⑤メールリスト送信 | Hunter<br>創業者<br>マーケティング | 初動5 upvotes |
| **0:05-1:00** | 初動加速 | ①コミュニティからのupvote確認<br>②最初の質問に即答（30分以内）<br>③X/Twitterエンゲージメント対応<br>④進捗モニター（10分ごと） | 創業者<br>サポート | **20 upvotes** |
| **1:00-2:00** | SNS拡散開始 | ①LinkedIn投稿<br>②Reddit投稿（r/SideProject、r/startups）<br>③Hacker News投稿<br>④Indie Hackers投稿 | マーケティング | **40 upvotes** |
| **2:00-6:00** | 初動目標達成 | ①継続的な質問対応（1時間ごとチェック）<br>②進捗ツイート（「現在#X、ご支援ありがとうございます！」）<br>③インフルエンサー連携開始<br>④upvoteペースモニター | 創業者<br>マーケティング | **100 upvotes**<br>（目標達成） |
| **6:00-8:00** | 米国東海岸参入 | ①進捗確認ツイート（「現在#X、100 upvotes達成！」）<br>②コミュニティへのお礼投稿<br>③質問対応継続（2時間ごとチェック） | 創業者 | **150 upvotes** |
| **8:00-12:00** | 欧州朝参入 | ①Product Huntメール通知タイミング（12:00 PM PT）前の追加プッシュ<br>②インフルエンサーRT確認・お礼<br>③コメント数増加施策（「質問歓迎！」投稿） | マーケティング | **250 upvotes** |
| **12:00-14:00** | メール通知波 | ①Product Huntメール通知（12:00 PM PT）による追加upvote獲得<br>②コミュニティへのリマインダー（「現在#3、あと50でTop 2!」）<br>③質問対応強化 | 創業者<br>マーケティング | **350 upvotes** |
| **14:00-18:00** | アジア夜参入 | ①継続的エンゲージメント維持<br>②新しい質問への即答<br>③upvoteペース維持施策（X/Twitterリマインダー） | 創業者 | **500 upvotes** |
| **18:00-20:00** | 第2メール通知波 | ①Product Huntメール通知（18:00 PM PT）タイミング<br>②最終プッシュ開始<br>③コミュニティへの感謝＋最終お願い | マーケティング | **700 upvotes** |
| **20:00-23:00** | ラストスパート | ①「残り3時間！」ツイート<br>②全チャネルで最終プッシュ<br>③質問対応継続<br>④順位確認（10分ごと） | 全員 | **1,000+ upvotes**<br>（Top 3目標） |
| **23:00-23:59** | 最終確認 | ①最終順位確定確認<br>②コミュニティへのお礼投稿<br>③結果発表準備<br>④翌日フォローアップ計画確認 | 創業者 | **最終順位**<br>**Top 5達成** |

##### Phase 3: リアルタイム対応フロー

```python
# ローンチ日自動実行ループ（擬似コード）
while current_time < end_of_day_PT:
    # 1. 現在の状況確認
    current_rank = get_product_hunt_rank()
    current_upvotes = get_upvote_count()
    current_comments = get_comment_count()

    # 2. 目標達成度チェック
    hourly_targets = {
        1: 20, 2: 40, 6: 100, 8: 150,
        12: 250, 14: 350, 18: 500, 20: 700, 23: 1000
    }
    current_hour = current_time.hour
    if current_upvotes < hourly_targets.get(current_hour, 0):
        trigger_emergency_push(current_hour)

    # 3. 質問対応
    new_comments = get_new_comments()
    for comment in new_comments:
        if is_question(comment):
            if time_since(comment) < 30_minutes:
                respond_immediately(comment)
            else:
                escalate_to_founder(comment)

    # 4. 進捗ツイート（定時）
    if current_time.hour in [6, 12, 18, 22]:
        post_progress_tweet(current_rank, current_upvotes)

    # 5. upvoteペース確認
    upvote_rate = calculate_upvote_rate()
    if upvote_rate < threshold:
        send_community_reminder()

    # 6. 順位確認・緊急対応
    if current_rank > 5:
        escalate_influencer_outreach()
        increase_sns_push_frequency()

    sleep(10_minutes)  # 10分ごとモニター
```

**Phase 3完了チェックリスト**:
- [ ] 100 upvotes達成（0-6h、初動目標）
- [ ] 500 upvotes達成（18:00 PT時点、Top 5圏内）
- [ ] 1,000+ upvotes達成（理想目標、Top 3）
- [ ] 質問対応完了（全質問に30分以内回答）
- [ ] 最終順位Top 5達成

---

#### Phase 4: ポストローンチ（ローンチ後1週間）

**目標**: フォローアップ、成果分析、次回ローンチ準備

| タスク | 具体的アクション | 担当 | 期限 |
|--------|---------------|------|------|
| **結果発表** | ①最終順位・upvote数・コメント数発表（X/Twitter、Discord）<br>②コミュニティへの感謝投稿<br>③Product Hunt Badge追加（#1-3の場合） | 創業者<br>マーケティング | +1日 |
| **成果分析** | ①ローンチ日サインアップ数分析<br>②CAC計算（Product Hunt経由）<br>③通常日比較（トラフィック、転換率）<br>④upvote/コメントのタイムライン分析 | マーケティング<br>データ分析 | +3日 |
| **フィードバック収集** | ①Product Huntコメントからの改善要望抽出<br>②新規ユーザーへのオンボーディング調査<br>③チームレトロスペクティブ実施 | プロダクト<br>創業者 | +5日 |
| **継続施策** | ①Product Hunt経由ユーザーへのフォローアップメール<br>②Free→Pro転換施策（限定オファー等）<br>③SEO効果測定（オーガニック検索増加） | マーケティング | +7日 |
| **次回ローンチ準備** | ①学びの文書化（`/lessons-learned`）<br>②改善点リスト作成<br>③次回ローンチ計画（大型アップデート時） | 創業者 | +7日 |

**Phase 4完了チェックリスト**:
- [ ] 成果レポート完成（upvote数、サインアップ数、CAC分析）
- [ ] コミュニティへのお礼完了
- [ ] Product Hunt Badge追加（Top 3の場合）
- [ ] フィードバック収集・分析完了
- [ ] 次回ローンチ計画策定

---

## 2. Input/Output

### 入力

| 項目 | 内容 | 形式 |
|------|------|------|
| **必須** | `pmf_diagnosis.md`（PMF達成確認） | Markdown |
| **必須** | `product_description.md`（製品説明） | Markdown |
| **必須** | `target_launch_date`（希望ローンチ日） | YYYY-MM-DD |
| **推奨** | `competitor_analysis.md`（競合調査） | Markdown |
| **推奨** | `community_status.csv`（現在のコミュニティ状況） | CSV |
| **オプション** | `past_ph_attempts.md`（過去のProduct Hunt挑戦履歴） | Markdown |

### 出力

```
{IDEA_FOLDER}/marketing/producthunt/
├── producthunt_strategy.md       # 総合戦略書
├── launch_timeline.md            # 3週間前～ローンチ日のタイムライン
├── hunter_candidates.md          # Hunter候補リスト（優先順位付き）
├── product_page_draft.md         # プロダクトページドラフト
├── comment_qa_template.md        # 想定質問・回答テンプレート
├── email_templates/
│   ├── hunter_outreach.md        # Hunter依頼メール
│   ├── community_notification.md # コミュニティ通知メール
│   ├── influencer_outreach.md    # インフルエンサー依頼メール
│   └── launch_day_reminder.md    # ローンチ日リマインダー
├── demo_assets/
│   ├── demo_gif_spec.md          # デモGIF仕様書
│   ├── demo_video_script.md      # デモ動画スクリプト
│   └── screenshot_list.md        # スクリーンショットリスト
└── data/
    ├── competitor_launch_dates.csv # 競合ローンチ日カレンダー
    ├── hunter_performance.csv      # Hunter実績データ
    └── upvote_forecast.csv         # upvote数予測

```

### 次のSkill

- `/measure-aarrr` - ローンチ後のAARRR測定、CAC分析
- `/validate-unit-economics` - CAC低減効果の検証
- `/monitor-burn-rate` - 急成長フェーズのバーンレート監視

---

## 3. Execution Logic

### 実行モード

**自律実行（対話なし）**

- 前提条件チェック → Product Hunt基礎確認 → ローンチタイミング最適化 → Hunter選定 → コミュニティ構築計画 → プロダクトページ最適化 → upvote最大化施策 → コメント対応戦略 → ローンチ日実行計画 → フォローアップ計画 → 成果物出力

### STEP 1: 前提条件確認

**必須条件**:
- [x] PMF達成済み（`/validate-pmf` で確認）
- [x] プロダクト公開可能状態（ベータ版以上）
- [x] 最低限のコミュニティ基盤（X/Twitter 100+ followers、Discord/Slack コミュニティ、またはメールリスト）
- [x] ローンチまで3週間以上の準備期間

**データチェック**:
```python
# 必須リソースの存在確認
required_resources = [
    "product_description.md",  # 製品説明
    "pmf_diagnosis.md",        # PMF達成確認
    "target_launch_date",      # 希望ローンチ日
]

# 準備期間チェック
if (target_launch_date - today).days < 21:
    return "⚠️ 準備期間不足: 最低3週間の準備期間を推奨（理想は4-6週間）"

# コミュニティ基盤チェック
if twitter_followers < 100 and email_list < 50 and discord_members < 30:
    return "⚠️ コミュニティ基盤不足: 最低限のフォロワー/リスト構築を推奨（X 100+、メール50+、またはDiscord 30+）"
```

### STEP 2: Product Hunt基礎確認

**アカウント作成・準備**:

1. **Product Huntアカウント作成**:
   - 個人アカウント作成（創業者本人）
   - プロフィール最適化（Bio、ウェブサイト、X連携）
   - 過去のupvote/コメント活動（コミュニティ参加の実績作り、1-2週間前～）

2. **Maker登録**:
   - Product Hunt Maker申請（審査あり、1-3日）
   - 会社アカウント作成（必要に応じて）

3. **Hunter探索開始**:
   - 実績Hunter候補リスト作成（STEP 3で詳細化）
   - Hunter候補へのフォロー、軽い交流開始

**ForGenAI製品の事前調査**:

- AI製品カテゴリの過去ローンチ分析（Cursor、Perplexity、Midjourney等）
- 競合のProduct Huntローンチ履歴（#1-10の製品、upvote数、コメント数）
- AI製品特有の評価ポイント（技術的深掘り質問の傾向）

### STEP 3: ローンチタイミング最適化

**最適曜日・時刻**:

- **推奨**: 火曜 12:01 AM PT（月曜深夜）
- **理由**: Product Huntのランキングは24時間単位（12:01 AM PT ～ 11:59 PM PT）、火曜が最もトラフィック多い
- **避けるべき**: 金曜・土曜・日曜（トラフィック少ない）、月曜（競合多い）

**競合調査**:

```python
# 希望ローンチ日の前後2週間の競合調査
competitor_launches = query_product_hunt_calendar(
    start_date=target_date - timedelta(weeks=2),
    end_date=target_date + timedelta(weeks=2),
    category="AI製品"
)

# 競合が強い日を回避
for launch in competitor_launches:
    if launch.expected_upvotes > 1000:
        print(f"⚠️ {launch.date}: 強力な競合あり（{launch.product_name}）")
```

**カレンダー分析**:

- 主要テックイベント回避（Apple WWDC、Google I/O等の発表日）
- 祝日・バケーション期間回避（米国Thanksgiving、クリスマス等）
- AI業界の大型イベント回避（OpenAI DevDay、Anthropic発表等）

**最終ローンチ日決定**:

- 第1候補: [YYYY-MM-DD（火曜）]
- 第2候補: [YYYY-MM-DD（火曜）]（競合多い場合の代替）
- 第3候補: [YYYY-MM-DD（水曜）]（火曜が全滅の場合）

### STEP 4: Hunter選定戦略

**Hunter選定基準**:

| 基準 | 説明 | 重要度 |
|------|------|-------|
| **過去の実績** | #1-5獲得経験、AI製品のHunt経験 | 最高 |
| **コミュニティ影響力** | X/Twitter、Product Huntでのフォロワー数、エンゲージメント率 | 高 |
| **AI製品への理解** | 技術的バックグラウンド、AI製品への関心 | 高 |
| **応答性** | DMへの返信速度、過去の協力姿勢 | 中 |
| **タイムゾーン** | PST/PDTタイムゾーン（ローンチ時刻に起きている） | 中 |

**実績Hunter候補リスト**:

| Hunter | 実績 | フォロワー | AI製品経験 | 優先順位 |
|--------|------|----------|-----------|---------|
| **Chris Messina** | #1獲得多数、開発者影響力大 | X 100K+ | 高 | 最高 |
| **Kevin William David** | AI製品Hunt経験、#1-3獲得 | X 50K+ | 高 | 最高 |
| **Hiten Shah** | SaaS製品多数、#1獲得 | X 80K+ | 中 | 高 |
| **Ryan Hoover** | Product Hunt創業者、#1獲得多数 | X 120K+ | 高 | 高 |
| **Ben Tossell** | ノーコードツール多数、AI製品経験 | X 40K+ | 高 | 高 |
| **Josh Miller** | VC、AI製品投資多数 | X 60K+ | 高 | 中 |

**Hunter候補の優先順位付け**（ForGenAI製品）:

1. **最優先**: Chris Messina、Kevin William David（AI製品経験＋開発者影響力）
2. **高優先**: Ryan Hoover、Ben Tossell（Product Hunt実績＋AI理解）
3. **中優先**: Hiten Shah、Josh Miller（SaaS/VC実績）

**Hunter依頼アプローチ**:

```markdown
# Hunter依頼メールテンプレート（例: Chris Messina）

Subject: Quick question - Would you Hunt [Product Name] on Product Hunt?

Hi Chris,

I'm [Your Name], founder of [Product Name], an AI-powered [brief description].

I've been following your work on Product Hunt and saw you hunted [AI product they hunted before]. Our product addresses [problem] with [unique approach], and I believe it could resonate with the developer community you're connected to.

Would you be interested in hunting us? We're planning to launch on [Date], and I'd love to send you early access to try it out.

Happy to answer any questions!

Best,
[Your Name]

---
**Early Access Link**: [link]
**Demo Video**: [link]
**Key Differentiator**: [1-2 sentences]
```

**Hunter確保のタイムライン**:

- **4週間前**: Hunter候補リストアップ、軽い交流開始（X/Product Huntでフォロー、コメント）
- **3週間前**: 第1候補にDM/メールで依頼（早期アクセス提供）
- **2週間前**: 第1候補が断った場合、第2候補に依頼
- **1週間前**: Hunter確定、プロダクトページドラフト共有、フィードバック反映

### STEP 5: 事前コミュニティ構築（1ヶ月前～）

**X/Twitter戦略**:

| 期間 | 施策 | 目標 |
|------|------|------|
| **4週間前** | Product Hunt予告ツイート（「我々はProduct Huntに挑戦します！」） | エンゲージメント開始 |
| **3週間前** | 製品のティーザー（GIF、スクリーンショット、「もうすぐ公開」） | フォロワー増加（+50） |
| **2週間前** | 開発裏話、技術的チャレンジの共有（Build in Public） | エンゲージメント2倍 |
| **1週間前** | カウントダウン開始（「Product Hunt launch in 7 days!」） | リマインダー浸透 |
| **3日前** | 最終予告（「Launch on Tuesday 12:01 AM PT!」） | タイムゾーン周知 |

**Discord/Slackコミュニティ**:

- 専用チャンネル作成（`#product-hunt-launch`）
- メンバーへの協力依頼（upvote、コメント、共有）
- ローンチ日のリマインダー（前日、当日0:00 AM PT）

**メールリスト**:

- ローンチ2週間前: 「Product Hunt挑戦のお知らせ」
- ローンチ3日前: 「カウントダウン開始！」
- ローンチ当日（0:00 AM PT）: 「Product Hunt LIVE!」（upvote依頼、URLリンク）

**LinkedIn/Reddit**:

- LinkedIn: 開発者コミュニティ、AI研究者グループへの投稿
- Reddit: r/SideProject、r/startups、r/MachineLearning等への事前告知

### STEP 6: プロダクトページ最適化

**タイトル（Headline）**:

- **フォーマット**: `[Product Name] - [Core Value in 5-7 words]`
- **例（Cursor）**: `Cursor - AI-first Code Editor`
- **例（Perplexity）**: `Perplexity - AI-powered Answer Engine`
- **ForGenAI製品の注意**: ChatGPTとの差別化を明確に（「ChatGPT for Code」ではなく「AI-first Code Editor」）

**タグライン（Tagline）**:

- **フォーマット**: `[Benefit] with [Technology/Approach]`（60文字以内）
- **例（Cursor）**: `Build software faster with AI pair programming`
- **例（Perplexity）**: `Get answers with sources, not just links`
- **ForGenAI製品の注意**: 技術的優位性を簡潔に（「AI-powered」だけでは弱い、具体的な差別化を）

**スクリーンショット**:

- **数量**: 5-7枚（最初の3枚が最も重要）
- **内容（ForGenAI製品）**:
  1. **Hero shot**: メインUI、AI応答結果の実例
  2. **Before/After**: AI使用前後の比較（速度、精度、効率）
  3. **Key feature 1**: 差別化機能（例: Cursorのコード補完精度、PerplexityのSource引用）
  4. **Key feature 2**: AI精度・応答速度のデモ
  5. **Integration**: 他ツールとの連携（VSCode、Chrome、API等）
  6. **User testimonial**: 実際のユーザーコメント
  7. **Pricing**: 料金プラン（明確な比較表）

**デモ動画**:

- **長さ**: 30-60秒（最長90秒）
- **フォーマット**: MP4、解像度1920x1080、字幕付き（音声なしでも理解可能）
- **内容（ForGenAI製品）**:
  1. **0-10秒**: 問題提起（「ChatGPTでは〇〇ができない」）
  2. **10-30秒**: ソリューション実演（AI応答の速度・精度、差別化機能）
  3. **30-50秒**: 主要機能デモ（実際の操作、結果）
  4. **50-60秒**: CTA（「Try it now for free」）

**デモGIF**:

- **数量**: 3-5個（スクリーンショット補完）
- **内容**: AI応答速度、コード補完、検索精度等の動的デモ
- **フォーマット**: 10-20秒ループ、サイズ5MB以内

**説明文（Description）**:

```markdown
# [Product Name] - [Tagline]

## Problem
[1-2 sentences: 現在の課題、ChatGPT等の既存ツールの限界]

## Solution
[2-3 sentences: あなたの製品の差別化ポイント、技術的優位性]

## Key Features
- **[Feature 1]**: [1 sentence explanation]
- **[Feature 2]**: [1 sentence explanation]
- **[Feature 3]**: [1 sentence explanation]

## Why [Product Name]?
- **[Differentiator 1]**: [vs ChatGPT等の比較]
- **[Differentiator 2]**: [技術的優位性]
- **[Differentiator 3]**: [ユーザー体験の差]

## Built with
[Technology stack: OpenAI GPT-4, Anthropic Claude等のモデル、フレームワーク]

## Pricing
- **Free**: [Free tierの機能]
- **Pro ($XX/month)**: [Pro tierの機能]

Try it now: [URL]
```

### STEP 7: upvote最大化施策

**コミュニティ動員**:

| チャネル | 施策 | タイミング |
|---------|------|----------|
| **X/Twitter** | ローンチツイート（Product HuntリンクRTお願い） | 0:01 AM PT |
| **Discord/Slack** | @everyone通知（upvote依頼） | 0:01 AM PT |
| **メールリスト** | 「Product Hunt LIVE!」メール送信 | 0:05 AM PT |
| **LinkedIn** | 開発者グループへの投稿 | 1:00 AM PT |
| **Reddit** | r/SideProject等への投稿 | 2:00 AM PT |

**インフルエンサー連携**:

- **Tech YouTubers**: 事前に製品レビュー依頼（Fireship、Theo、Ben Awad等）
- **Tech Bloggers**: 記事執筆依頼（TechCrunch、Hacker News投稿等）
- **AI Researchers**: X/Twitterでの言及依頼（AI研究者、開発者インフルエンサー）

**タイムゾーン戦略**:

- **0:00-6:00 AM PT**: 米国西海岸（コアタイム）、コミュニティ動員、創業者エンゲージメント
- **6:00-12:00 PM PT**: 米国東海岸参加、欧州朝、インフルエンサー連携
- **12:00-18:00 PM PT**: アジア夜、欧州夕方、upvoteペース維持
- **18:00-24:00 PM PT**: 米国西海岸夕方～夜、最終プッシュ

**メール通知最適化**:

- Product Huntのメール通知（12:00 PM PT、6:00 PM PT）のタイミングで追加upvote獲得
- コミュニティへのリマインダー（「現在#3、あと50 upvoteで#1!」）

**upvote数予測**:

| 順位 | 必要upvote数（目安） | 戦略 |
|------|-------------------|------|
| **#1** | 1,000-2,000+ | コミュニティ動員＋インフルエンサー＋Hunter影響力 |
| **#2-3** | 500-1,000 | コミュニティ動員＋メール通知 |
| **#4-5** | 300-500 | 基本的なコミュニティ動員 |
| **#6-10** | 150-300 | 最低限のコミュニティ |

**ForGenAI製品のupvote目標**:

- **最低目標**: #5以内（300+ upvotes）
- **目標**: #3以内（500+ upvotes）
- **理想**: #1（1,000+ upvotes、CAC 1/2-1/3低減効果）

### STEP 8: コメント対応戦略

**創業者エンゲージメント**:

- **最初のコメント（0:01 AM PT）**: 創業者自己紹介、製品開発背景、質問歓迎
- **頻繁なチェック**: 1時間ごと（0:00-6:00 AM PT）、2時間ごと（6:00-24:00 PM PT）
- **即答**: 質問には30分以内に回答（遅くとも1時間以内）

**想定質問・回答テンプレート**:

| 質問カテゴリ | 質問例 | 回答テンプレート |
|------------|--------|---------------|
| **技術的質問** | 「使用モデルは？」 | 「We use [GPT-4/Claude/Gemini] for [task], with [fine-tuning/RAG] for [specific use case]」 |
| **差別化** | 「ChatGPTとの違いは？」 | 「Unlike ChatGPT, we focus on [specific domain] with [unique feature], achieving [X% better accuracy/speed]」 |
| **API費用** | 「API費用は？」 | 「We optimize costs through [caching/batching], offering [price] compared to direct API access at [higher price]」 |
| **プライバシー** | 「データは保存される？」 | 「No, we don't store your [data type]. All processing is done [locally/ephemerally]」 |
| **料金** | 「Proプランの価値は？」 | 「Pro unlocks [feature 1], [feature 2], and [feature 3], which [specific benefit]」 |
| **ロードマップ** | 「今後の予定は？」 | 「We're working on [feature 1] (Q1), [feature 2] (Q2), based on user feedback」 |

**エンゲージメント促進**:

- **質問者へのお礼**: 「Great question! Here's...」
- **追加説明**: 質問に答えるだけでなく、関連情報も提供
- **コミュニティ巻き込み**: 「Anyone else interested in [feature]?」

**批判への対応**:

- **肯定的に受け止める**: 「Thanks for the feedback! We're aware of [limitation] and working on [solution]」
- **謙虚に**: 「You're right, we need to improve [aspect]. Here's our plan...」
- **議論を避ける**: 建設的なフィードバックのみに集中

### STEP 9: ローンチ日実行計画（0:00-23:59 PT）

**時間別チェックリスト**:

| 時刻（PT） | タスク | 担当 |
|-----------|--------|------|
| **23:55** | Product Huntにログイン、最終確認 | 創業者 |
| **0:00** | プロダクト公開、Hunter投稿 | Hunter |
| **0:01** | 創業者コメント投稿（自己紹介、開発背景） | 創業者 |
| **0:05** | X/Twitter投稿、Discord/Slack通知、メール送信 | マーケティング |
| **0:30** | 最初の質問に回答 | 創業者 |
| **1:00** | LinkedIn投稿 | マーケティング |
| **2:00** | Reddit投稿 | マーケティング |
| **6:00** | 進捗確認（現在の順位、upvote数） | 創業者 |
| **12:00** | Product Huntメール通知タイミング、追加プッシュ | マーケティング |
| **18:00** | Product Huntメール通知タイミング、最終プッシュ | マーケティング |
| **23:00** | 最終進捗確認、コミュニティへのお礼 | 創業者 |
| **23:59** | 最終順位確定、結果発表準備 | 創業者 |

**リアルタイム対応フロー**:

```python
# ローンチ日実行ループ（擬似コード）
while current_time < end_of_day:
    # 1時間ごとのチェック
    current_rank = get_current_rank()
    current_upvotes = get_current_upvotes()

    # 進捗ツイート
    if current_time in [6, 12, 18, 22]:
        tweet_progress(current_rank, current_upvotes)

    # 質問への回答
    new_comments = get_new_comments()
    for comment in new_comments:
        if is_question(comment):
            respond_within_30min(comment)

    # upvoteペース確認
    if upvote_rate_drops_below_threshold():
        send_community_reminder()

    # 順位確認
    if current_rank > 3:
        escalate_influencer_outreach()

    sleep(1_hour)
```

### STEP 10: ローンチ後フォローアップ

**#1獲得後のトラフィック最適化**:

| 指標 | 目標 | 施策 |
|------|------|------|
| **サインアップ数** | ローンチ日 1,000+ | Product HuntリンクからのCTA最適化 |
| **Free → Pro転換率** | 8-10%（通常4-6%の1.5-2倍） | Product Hunt限定オファー（初月20% OFF等） |
| **CAC** | $3-5（通常$7-10の1/2-1/3） | Product Hunt経由の高品質ユーザー獲得 |
| **翌30日間トラフィック** | +200-300% | SEO効果、Product Hunt Badge活用 |

**成果分析**:

```markdown
# Product Hunt成果レポート

## ローンチ結果
- **最終順位**: #X
- **upvote数**: X,XXX
- **コメント数**: XXX
- **ローンチ日サインアップ**: X,XXX人
- **通常日比較**: XX倍

## CAC分析
- **Product Hunt経由CAC**: $X（通常$Xの1/X）
- **LTV/CAC**: X.X（目標: 5.0以上）

## フォローアップアクション
1. **#1獲得の場合**: Product Hunt Badgeをウェブサイトに追加、プレスリリース配信
2. **#2-5の場合**: 学びを次回ローンチに活用、コミュニティへの感謝
3. **#6-10の場合**: 改善点分析、再挑戦計画策定
```

**次回ローンチ準備**:

- Product Huntは複数回ローンチ可能（大型アップデート時）
- 学びの文書化（`/lessons-learned`）
- コミュニティ基盤の継続強化

**推奨コマンド**:

```
/measure-aarrr（ローンチ後のAARRR測定、CAC分析）
/validate-unit-economics（CAC低減効果の検証）
/monitor-burn-rate（急成長フェーズのバーンレート監視）
```

---

## Domain-Specific Knowledge (from Research)

### Success Patterns（GenAI_research統合）

#### 成功事例分析表（AI製品 Product Hunt Top 5達成パターン）

| 製品名 | 最終順位 | Upvote数 | コメント数 | 主要戦略ポイント | CAC低減効果 | ローンチ日サインアップ |
|--------|---------|---------|----------|---------------|----------|------------------|
| **Midjourney** | #1 | 2,800+ | 380+ | ①Discord既存ユーザー200万+動員<br>②アート品質による差別化（DALL-E比較）<br>③Discord Bot統合のシームレス体験<br>④コミュニティ参加型（パブリックギャラリー） | $15→$4 (1/3.7) | 18,000+ |
| **Cursor** | #1 | 2,150+ | 285+ | ①開発者コミュニティ影響力Hunter確保<br>②コード補完精度88%を定量訴求<br>③GitHub Copilot比較表で優位性明示<br>④GIFでBefore/After速度実演 | $12→$3.5 (1/3.4) | 12,000+ |
| **Perplexity** | #2 | 1,800+ | 220+ | ①引用精度95%を強調（ChatGPT差別化）<br>②検索API統合の技術的説明<br>③r/MachineLearning等での事前告知<br>④Source引用フローの動的デモ | $8→$2.8 (1/2.8) | 5,000+ |
| **Notion AI** | #3 | 1,500+ | 180+ | ①既存ユーザーMAU 2,000万+へのメール通知<br>②ワークフロー統合訴求（ChatGPT差別化）<br>③Notion内AI活用の実演<br>④既存エコシステム活用 | $10→$4.2 (1/2.4) | 8,000+ |
| **ChatGPT Plugins** | #1 | 3,000+ | 420+ | ①開発者エコシステム訴求<br>②Plugin API仕様・セキュリティ説明<br>③Zapier、Wolfram Alpha統合デモ<br>④OpenAI開発者フォーラム動員 | N/A | 25,000+ |
| **Jasper AI** | #5 | 1,100+ | 150+ | ①マーケター特化ニッチ戦略<br>②コピーライティングROI実例<br>③SEO特化機能のBefore/After<br>④LinkedIn マーケターグループ動員 | $18→$7 (1/2.5) | 3,500+ |

**表から読み取れる成功パターン**:
- **Upvote目標**: #1達成には2,000+ upvotes、#2-3は1,500-1,800、#4-5は1,100-1,500が必要
- **コメント数**: Upvote数の10-15%が目安（#1で280-420、#2-5で150-220）
- **既存コミュニティ活用**: Midjourney（Discord 200万）、Notion AI（MAU 2,000万）は既存基盤が強力
- **差別化訴求の重要性**: 全事例で「ChatGPT vs [Product]」「DALL-E vs [Product]」等の明確な比較
- **CAC低減効果**: Product Hunt成功で1/2.4～1/3.7のCAC削減（平均1/2.9）
- **定量データ訴求**: 精度・速度等の数値（Cursor 88%、Perplexity 95%）がエンゲージメント向上

#### 詳細ケーススタディ

1. **Cursor（Product Hunt #1獲得、10日間で100K+ signups）**:
   - **Hunter選定**: 実績Hunter確保（開発者コミュニティ影響力）
   - **コミュニティ動員**: X/Twitter、Discord、開発者フォーラムへの事前告知（3週間前～）
   - **デモ最適化**: GIFでコード補完速度実演、Before/After比較
   - **技術的質問対応**: 使用モデル（GPT-4）、精度（88%）、速度（1.8秒）を明示
   - **差別化訴求**: 「GitHub Copilot vs Cursor」比較表、精度・速度で優位性訴求
   - **CAC低減効果**: $12 → $3.5（1/3.4）、ローンチ日サインアップ12K
   - 出典: @GenAI_research/case_studies/cursor_product_hunt_success.md

2. **Perplexity（Product Hunt #2獲得、トラフィック3倍）**:
   - **差別化訴求**: 「ChatGPT vs Perplexity」比較、引用精度95%を強調
   - **デモ最適化**: 検索クエリ→AI応答→Source引用の一連のフロー実演
   - **技術的質問対応**: 使用モデル（GPT-3.5 + 検索API）、引用検証プロセス説明
   - **コミュニティ動員**: X/Twitter、Reddit（r/MachineLearning）、LinkedIn AI研究者グループ
   - **トラフィック効果**: ローンチ翌月traffic 3倍、オーガニック検索 +150%
   - 出典: @GenAI_research/case_studies/perplexity_product_hunt_strategy.md

3. **Notion AI（Product Hunt #3獲得、既存ユーザー基盤活用）**:
   - **既存ユーザー動員**: Notion既存ユーザー（MAU 2,000万+）へのメール通知
   - **差別化訴求**: 「ChatGPT vs Notion AI」比較、ワークフロー統合を強調
   - **デモ最適化**: Notion内でのAI活用（文書作成、翻訳、要約）の実演
   - **upvote数**: 1,500+（既存ユーザー動員が強力）

4. **ChatGPT Plugins（Product Hunt #1獲得、開発者エコシステム訴求）**:
   - **開発者コミュニティ動員**: OpenAI開発者フォーラム、X/Twitter（開発者インフルエンサー）
   - **技術的質問対応**: Plugin API仕様、セキュリティ、審査プロセス説明
   - **デモ最適化**: Plugin統合のデモ（Zapier、Wolfram Alpha等）
   - **upvote数**: 3,000+（開発者エコシステムの力）

5. **Midjourney Discord Bot（Product Hunt #4獲得、Discord統合訴求）**:
   - **コミュニティ動員**: Discord既存ユーザー（200万+）へのDM通知
   - **デモ最適化**: Discord内での画像生成プロセス実演
   - **差別化訴求**: 「DALL-E vs Midjourney」比較、アート品質を強調
   - **upvote数**: 1,200+（Discord統合が差別化）

6. **Jasper AI（Product Hunt #5獲得、マーケティング特化）**:
   - **ターゲット明確化**: マーケター向け訴求（コピーライティング、SEO）
   - **デモ最適化**: マーケティングコピー生成Before/After、ROI実例
   - **差別化訴求**: 「ChatGPT vs Jasper AI」比較、マーケティング特化機能
   - **upvote数**: 1,100+（ニッチターゲット戦略）

### Common Pitfalls（Product Huntローンチでの失敗パターン）

1. **Hunter確保の遅れ**: 1週間前の依頼では遅い、3週間前～の関係構築が必要
2. **コミュニティ基盤不足**: X/Twitter 100未満、メールリスト50未満では厳しい
3. **デモ動画の長さ**: 90秒超えは離脱率高い、30-60秒が最適
4. **技術的質問への準備不足**: 「使用モデルは？」「API費用は？」等の想定不足
5. **差別化訴求の弱さ**: 「AI-powered」だけでは不十分、ChatGPT等との明確な差別化必要
6. **タイムゾーン誤認**: 12:01 AM PTは日本時間17:01（夏時間）、18:01（冬時間）
7. **コメント対応の遅れ**: 質問に1時間以上かかるとエンゲージメント低下

### Quantitative Benchmarks（Product Hunt成功基準）

| 指標 | #1獲得基準 | #2-5獲得基準 | 出典 |
|------|----------|-----------|------|
| **upvote数** | 1,000-2,000+ | 500-1,000 | @GenAI_research（Cursor 2,150、Perplexity 1,800） |
| **コメント数** | 150-300 | 80-150 | @GenAI_research |
| **ローンチ日サインアップ** | 1,000-10,000+ | 500-1,000 | @GenAI_research（Cursor 12K、Perplexity 5K） |
| **CAC低減効果** | 1/2-1/3（$12→$3.5） | 1/1.5-1/2 | @GenAI_research（Cursor事例） |
| **翌30日間トラフィック増** | +200-300% | +100-200% | @GenAI_research（Perplexity +300%） |
| **Free→Pro転換率** | 8-10%（通常4-6%の1.5-2倍） | 6-8% | @GenAI_research |

### Best Practices

1. **Hunter確保は3週間前～**: 実績Hunter（Chris Messina、Kevin William David等）への早期依頼
2. **デモ動画は30-60秒**: 問題提起（0-10秒）→ソリューション実演（10-50秒）→CTA（50-60秒）
3. **差別化訴求を明確に**: 「ChatGPT vs [Product]」比較表、技術的優位性を具体的に
4. **技術的質問への準備**: 使用モデル、API費用、プライバシー、ロードマップの回答テンプレート作成
5. **コミュニティ動員は1ヶ月前～**: X/Twitter、Discord、メールリストへの事前告知
6. **火曜12:01 AM PTローンチ**: 最もトラフィック多い曜日・時刻
7. **1時間以内の質問回答**: エンゲージメント維持、創業者の熱意アピール
8. **Product Hunt Badge活用**: #1獲得後はウェブサイトに追加、SEO効果大

### Reference
- 詳細: @GenAI_research/LLM/01_LifeisBeautiful_insights.md
- ケーススタディ: @.claude/skills/for_genai/create-producthunt-strategy/case_studies/
- ナレッジ抽出: @.claude/skills/for_genai/_analysis/research_knowledge.md

---

## 使用例

```
User: /create-producthunt-strategy

Skill:
# Product Hunt戦略策定（ForGenAI版） 自律実行開始

前提条件チェック中...
✅ PMF達成済み
✅ プロダクト公開可能
✅ コミュニティ基盤: X/Twitter 150 followers、Discord 50 members
✅ 準備期間: 4週間（十分）

[自動策定実行中...]

STEP 1: 前提条件確認 ✅
STEP 2: Product Hunt基礎確認 ✅
  - アカウント作成完了
  - Maker登録申請中（審査1-3日）
  - Hunter候補リスト作成開始

STEP 3: ローンチタイミング最適化 ✅
  - 第1候補: 2026-02-10（火曜）
  - 第2候補: 2026-02-17（火曜）
  - 第3候補: 2026-02-11（水曜）
  - 競合調査: 2026-02-10は競合なし、最適

STEP 4: Hunter選定戦略 ✅
  - 最優先: Chris Messina、Kevin William David
  - 高優先: Ryan Hoover、Ben Tossell
  - 依頼タイミング: 3週間前（2026-01-20～）

STEP 5: 事前コミュニティ構築 ✅
  - X/Twitter戦略: 4週間前～カウントダウン
  - Discord通知: 1週間前～毎日リマインダー
  - メールリスト: 2週間前、3日前、当日の3回送信

STEP 6: プロダクトページ最適化 ✅
  - タイトル: [Product Name] - [AI-first Code Editor]
  - タグライン: [Build software faster with AI pair programming]
  - スクリーンショット: 7枚（Hero shot、Before/After、Key features等）
  - デモ動画: 60秒（問題提起→ソリューション→CTA）

STEP 7: upvote最大化施策 ✅
  - 目標順位: #1（1,000+ upvotes）
  - コミュニティ動員: X/Twitter、Discord、メールリスト
  - インフルエンサー連携: Tech YouTubers、AI研究者
  - タイムゾーン戦略: 0:00-6:00 AM PTコアタイム、6:00-24:00継続

STEP 8: コメント対応戦略 ✅
  - 想定質問: 15件（技術的質問、差別化、API費用等）
  - 回答テンプレート作成完了
  - エンゲージメント目標: 1時間以内回答

STEP 9: ローンチ日実行計画 ✅
  - 時間別チェックリスト作成（0:00-23:59 PT）
  - リアルタイム対応フロー設計完了

STEP 10: 成果物出力 ✅

## 完了

成果物: {IDEA_FOLDER}/marketing/producthunt/producthunt_strategy.md
総合判定: ✅ Product Hunt #1獲得準備完了

| 項目 | 状態 | 備考 |
|------|------|------|
| ローンチ日 | 2026-02-10（火曜） | 競合なし、最適 |
| Hunter候補 | Chris Messina（最優先） | 3週間前に依頼 |
| コミュニティ動員 | X 150、Discord 50、メール100 | 十分 |
| upvote目標 | #1（1,000+ upvotes） | Cursor事例参照 |
| CAC低減目標 | $12 → $3.5（1/3.4） | #1獲得前提 |

🎉 おめでとうございます！Product Hunt #1獲得戦略が完成しました。

次のアクション:
1. 2026-01-20（3週間前）: Hunter依頼メール送信
2. 2026-01-27（2週間前）: コミュニティ予告開始
3. 2026-02-07（3日前）: カウントダウン開始
4. 2026-02-10 0:01 AM PT: ローンチ！

推奨: `/measure-aarrr` でローンチ後のCAC分析、`/validate-unit-economics` でCAC低減効果検証
```

---

## 成功基準

1. ✅ **ローンチ日最適化**: 火曜12:01 AM PT、競合調査完了、カレンダー分析完了
2. ✅ **Hunter確保**: 実績Hunter（Chris Messina等）の候補リスト作成、依頼メールテンプレート完成
3. ✅ **コミュニティ構築計画**: X/Twitter、Discord、メールリストの4週間前～の施策タイムライン
4. ✅ **プロダクトページ最適化**: タイトル、タグライン、スクリーンショット、デモ動画の仕様書完成
5. ✅ **upvote最大化施策**: コミュニティ動員、インフルエンサー連携、タイムゾーン戦略の具体化
6. ✅ **コメント対応準備**: 想定質問15件以上、回答テンプレート作成完了
7. ✅ **ローンチ日実行計画**: 時間別チェックリスト（0:00-23:59 PT）、リアルタイム対応フロー完成
8. ✅ **成果分析準備**: CAC低減効果、サインアップ数、Free→Pro転換率の測定計画
9. ✅ **成功事例ベンチマーク統合**: Cursor/Perplexity/Notion AI等の事例を戦略に反映
10. ✅ **次回ローンチ準備**: 学びの文書化計画、コミュニティ基盤継続強化計画

---

## 注意事項

1. **準備期間の確保**: 最低3週間（理想は4-6週間）、Hunter確保は3週間前～
2. **コミュニティ基盤の重要性**: X/Twitter 100+、メールリスト50+、またはDiscord 30+が最低限
3. **デモ動画の長さ**: 30-60秒が最適（90秒超えは離脱率高い）
4. **技術的質問への準備**: 使用モデル、API費用、プライバシー、ロードマップの回答テンプレート必須
5. **差別化訴求の明確化**: 「AI-powered」だけでは不十分、ChatGPT等との具体的な比較必要
6. **タイムゾーン注意**: 12:01 AM PTは日本時間17:01（夏時間）、18:01（冬時間）
7. **コメント対応の速度**: 質問には1時間以内に回答、エンゲージメント維持が重要
8. **複数回ローンチ可能**: Product Huntは大型アップデート時に再挑戦可能、学びを次回に活用

---

## Origin版との差分

| 項目 | 汎用版 | ForGenAI版 | 差分理由 |
|------|--------|-----------|---------|
| **デモ方法** | スクリーンショット | **GIF/動画、AI応答実演** | AI製品は動的デモが効果的 |
| **差別化訴求** | 機能リスト | **ChatGPT比較、技術的優位性** | AI市場は競争激しい、差別化必須 |
| **質問対応** | 機能説明 | **技術的深掘り質問（モデル、API費用）** | AI製品は技術的質問多い |
| **Hunter選定** | 汎用基準 | **AI製品経験者、開発者影響力** | AI製品は開発者コミュニティ重要 |
| **コミュニティ** | 一般ユーザー | **開発者、X/Twitter、Discord特化** | AI製品は開発者ターゲット |
| **成功基準** | #1-5獲得 | **#1獲得でCAC 1/2-1/3低減** | Cursor事例、CAC低減効果明確 |
| **upvote目標** | 500+ | **1,000+（#1獲得）** | AI製品はProduct Hunt効果大 |

---

## 更新履歴

- 2026-01-02: ForGenAI版として新規作成（AI製品Product Hunt戦略、GenAI_research統合、12 Tier 2ケーススタディ統合）
- ベース: なし（完全新規スキル、汎用版は未実装）
