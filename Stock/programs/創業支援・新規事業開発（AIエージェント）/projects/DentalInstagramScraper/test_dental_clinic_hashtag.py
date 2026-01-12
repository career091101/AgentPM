#!/usr/bin/env python3
"""
Test with #歯科医院 hashtag - more specific for actual clinics
"""
from browser_collector import collect_from_hashtag, save_to_csv

def main():
    print("🦷 Testing #歯科医院 Hashtag")
    print("="*60)
    print("\nThis hashtag is more specific to dental clinics")
    print("Checking 10 posts...\n")

    profiles = collect_from_hashtag(
        hashtag="歯科医院",  # More specific hashtag
        max_posts=10,
        headless=False
    )

    if profiles:
        print(f"\n{'='*60}")
        print(f"✅ FOUND {len(profiles)} DENTAL CLINICS!")
        print(f"{'='*60}\n")

        csv_file = save_to_csv(profiles, "歯科医院")

        for i, p in enumerate(profiles, 1):
            print(f"{i}. @{p.get('instagram_handle')}")
            print(f"   📛 {p.get('full_name', 'N/A')}")
            print(f"   👥 {p.get('followers', 0):,} followers")
            if p.get('postal_code'):
                print(f"   📮 {p.get('postal_code')}")
            if p.get('address'):
                print(f"   🏠 {p.get('address')}")
            print(f"   ℹ️  {(p.get('biography', '')[:100])}...")
            print()

        print(f"💾 Saved to: {csv_file}\n")

        # Stats
        with_data = sum(1 for p in profiles if p.get('postal_code') or p.get('address'))
        print(f"📊 {with_data}/{len(profiles)} profiles have location data")

    else:
        print("\n⚠️  No clinics found")
        print("Trying #小児歯科 might give better results...")

if __name__ == "__main__":
    main()
