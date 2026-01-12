import json
from datetime import datetime
import re

# AI関連キーワード
ai_keywords = {
    # AI技術
    'ai', 'artificial intelligence', 'machine learning', 'deep learning',
    'neural network', 'chatgpt', 'claude', 'gemini', 'gpt', 'llm',
    'large language model', 'agi', 'asi', 'artificial general intelligence',
    'generative ai', 'gen-ai', 'transformer', 'attention mechanism',
    'nlp', 'natural language processing',
    
    # AI企業
    'openai', 'anthropic', 'deepmind', 'google ai', 'microsoft ai',
    'meta ai', 'xai', 'perplexity', 'cohere', 'stability ai',
    
    # AI応用
    'prompt', 'prompting', 'prompt engineering', 'rag',
    'retrieval augmented generation', 'fine-tuning', 'finetuning',
    'image generation', 'text-to-image', '画像生成',
    'agent', 'autonomous agent', 'ai agent',
    'multimodal', 'vision', 'embedding', 'vector database',
    
    # AI関連ツール
    'claude code', 'github copilot', 'cursor', 'codeium',
    'tabnine', 'copilot', 'hugging face',
    
    # AI関連概念
    'alignment', 'rlhf', 'reinforcement learning from human feedback',
    'hallucination', 'context window', 'token',
    'inference', 'pre-training', 'training',
    '機械学習', '深層学習', 'ai', '生成ai', 'llm',
    'エージェント', 'プロンプト', 'ニューラル', 'アルゴリズム'
}

# ファイルを読み込む
with open('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/x_timeline_20260104.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ツイートを処理
ai_related_ids = []
total_tweets = 0

if isinstance(data, list):
    tweets = data
elif isinstance(data, dict) and 'tweets' in data:
    tweets = data['tweets']
else:
    tweets = []

print(f"処理開始: 総ツイート数 = {len(tweets)}")

for tweet in tweets:
    total_tweets += 1
    
    # tweet_id とテキストを取得
    tweet_id = tweet.get('tweet_id') or tweet.get('id')
    text = tweet.get('text', '').lower()
    
    # AI関連キーワードをチェック
    is_ai_related = False
    for keyword in ai_keywords:
        if keyword in text:
            is_ai_related = True
            break
    
    if is_ai_related:
        ai_related_ids.append(str(tweet_id))
        print(f"✓ AI関連: {tweet_id}")

# 結果をまとめる
result = {
    "processed_at": datetime.utcnow().isoformat() + "Z",
    "total_tweets": total_tweets,
    "ai_related_count": len(ai_related_ids),
    "ai_related_tweet_ids": ai_related_ids
}

# 結果を保存
output_path = '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/ai_related_tweet_ids_20260104.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n処理完了:")
print(f"  総ツイート数: {total_tweets}")
print(f"  AI関連ツイート数: {len(ai_related_ids)}")
print(f"  抽出率: {len(ai_related_ids)/total_tweets*100:.1f}%")
print(f"  保存先: {output_path}")
