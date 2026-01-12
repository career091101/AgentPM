import json
from collections import defaultdict

# JSON結果を読み込む
with open('scoring_results_batch_001_20260104_125755.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

results = data['results']

# スコア統計
score_dimensions = {
    '基礎評価': [],
    '来院患者数': [],
    '子ども対応力': [],
    'Web積極性': [],
    '医院規模': [],
    'ブログ活動': []
}

sns_stats = {
    'sns_instagram': 0,
    'sns_facebook': 0,
    'sns_line': 0,
    'sns_twitter': 0
}

director_count = sum(1 for r in results if r.get('director_name'))

# 次元別スコア集計
for result in results:
    scores = result['scores']
    for dimension, score in scores.items():
        score_dimensions[dimension].append(score)
    
    # SNS連携カウント
    analysis = result['website_analysis']
    for sns_key in sns_stats.keys():
        if analysis.get(sns_key):
            sns_stats[sns_key] += 1

print("📊 スコアリング詳細統計\n")
print("=" * 60)

# 各次元の統計
for dimension, scores in score_dimensions.items():
    avg = sum(scores) / len(scores) if scores else 0
    max_score = max(scores) if scores else 0
    min_score = min(scores) if scores else 0
    print(f"{dimension}:")
    print(f"  平均: {avg:.1f} | 最大: {max_score} | 最小: {min_score}")

print("\n" + "=" * 60)
print("\n🌐 SNS連携率:")
for sns_name, count in sns_stats.items():
    rate = count / len(results) * 100
    label = {
        'sns_instagram': 'Instagram',
        'sns_facebook': 'Facebook',
        'sns_line': 'LINE',
        'sns_twitter': 'Twitter/X'
    }[sns_name]
    print(f"  {label}: {count}件 ({rate:.1f}%)")

print(f"\n👤 医院長名取得:")
print(f"  取得済み: {director_count}件 ({director_count/len(results)*100:.1f}%)")

print(f"\n📋 メタデータ:")
for key, value in data['metadata'].items():
    print(f"  {key}: {value}")

print("\n✅ スコアリング処理完了!")
