#!/usr/bin/env python3
"""
Google Maps API接続テスト
"""

import os
import requests

API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")

if not API_KEY:
    print("❌ Error: GOOGLE_MAPS_API_KEY environment variable not set")
    exit(1)

print(f"✅ API Key found: {API_KEY[:10]}...")

# Places Text Search (New) テスト
print("\n📍 Testing Places Text Search (New)...")
url = "https://places.googleapis.com/v1/places:searchText"
headers = {
    "X-Goog-Api-Key": API_KEY,
    "Content-Type": "application/json",
    "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress"
}
body = {
    "textQuery": "東京駅 東京都",
    "maxResultCount": 1
}

try:
    response = requests.post(url, headers=headers, json=body, timeout=10)

    if response.status_code == 200:
        data = response.json()
        if data.get("places"):
            place = data["places"][0]
            print(f"✅ Places API (New) is working!")
            print(f"   Found: {place.get('displayName', {}).get('text', 'N/A')}")
            print(f"   Address: {place.get('formattedAddress', 'N/A')}")
        else:
            print("⚠️  API returned no results (but API is working)")
    elif response.status_code == 403:
        print("❌ Error 403: API not enabled or key restrictions too strict")
        print(f"   Response: {response.text}")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"❌ Exception: {e}")

print("\n✅ API test completed")
