#!/usr/bin/env python3
"""
Find real dental clinic Instagram handles using web search
"""
import anthropic
import os
from dotenv import load_dotenv
import json
from datetime import datetime
import re

def find_dental_instagram_handles(location="東京", count=50):
    """
    Use Anthropic API with web search to find real dental clinic Instagram handles

    Args:
        location: Location to search (e.g., "東京", "大阪", "神奈川")
        count: Target number of handles to find
    """
    load_dotenv()

    print(f"🔍 Searching for dental clinic Instagram handles in {location}...")
    print(f"   Target: {count} clinics\n")

    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

    # Search query
    search_queries = [
        f"{location} 歯科医院 Instagram アカウント",
        f"{location} デンタルクリニック Instagram",
        f"{location} 歯科 インスタグラム",
        f"dental clinic {location} instagram account site:instagram.com",
    ]

    all_handles = set()

    for query in search_queries:
        print(f"🔎 Query: {query}")

        try:
            response = client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=4096,
                messages=[{
                    "role": "user",
                    "content": f"""以下の検索クエリで、実在する歯科医院のInstagramアカウント名（@で始まるユーザー名）を見つけてください。

検索クエリ: {query}

以下の形式で、見つけたInstagramアカウントをリストアップしてください：
- アカウント名は@を含めて記載（例: @example_dental）
- 医院名も併記
- 最低10件、最大30件

フォーマット:
@username - 医院名 - 簡単な説明

実在するアカウントのみを報告してください。"""
                }]
            )

            response_text = response.content[0].text
            print(f"   ✅ Response received\n")

            # Extract Instagram handles from response
            # Pattern: @username or instagram.com/username
            handle_patterns = [
                r'@([a-zA-Z0-9._]+)',
                r'instagram\.com/([a-zA-Z0-9._]+)',
            ]

            for pattern in handle_patterns:
                matches = re.findall(pattern, response_text)
                all_handles.update(matches)

            print(f"   Found {len(all_handles)} unique handles so far\n")

        except Exception as e:
            print(f"   ❌ Error: {e}\n")

        if len(all_handles) >= count:
            break

    # Save results
    if all_handles:
        handles_list = [
            {
                'username': handle,
                'discovered_at': datetime.now().isoformat(),
                'location': location,
                'status': 'pending_verification'
            }
            for handle in sorted(all_handles)
        ]

        output_file = f"dental_handles_{location}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(handles_list, f, ensure_ascii=False, indent=2)

        print(f"\n✅ Search complete!")
        print(f"   Total handles found: {len(all_handles)}")
        print(f"   Saved to: {output_file}")

        print(f"\n📋 Sample handles:")
        for handle in sorted(all_handles)[:10]:
            print(f"   - @{handle}")

        if len(all_handles) > 10:
            print(f"   ... and {len(all_handles) - 10} more")

        return handles_list

    else:
        print("\n⚠️  No handles found")
        return []

if __name__ == "__main__":
    # Search for Tokyo dental clinics
    handles = find_dental_instagram_handles(location="東京", count=50)

    if handles:
        print(f"\n💡 Next step: Run verify_and_collect.py to verify these handles and collect data")
