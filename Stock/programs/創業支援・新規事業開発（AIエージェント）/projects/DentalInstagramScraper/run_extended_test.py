#!/usr/bin/env python3
"""
Extended test - Check 20 posts from #歯科 to find real dental clinics
"""
from browser_collector import collect_from_hashtag, save_to_csv

def main():
    print("🦷 Extended Test: Find Real Dental Clinics")
    print("="*60)
    print("\nChecking 20 posts from #歯科 hashtag...")
    print("Looking for actual dental clinic accounts\n")

    profiles = collect_from_hashtag(
        hashtag="歯科",
        max_posts=20,  # Check more posts
        headless=False
    )

    if profiles:
        print(f"\n{'='*60}")
        print(f"✅ SUCCESS! Found {len(profiles)} dental clinics!")
        print(f"{'='*60}\n")

        # Save to CSV
        csv_file = save_to_csv(profiles, "歯科")

        print(f"📋 Dental Clinics Found:\n")
        for i, p in enumerate(profiles, 1):
            print(f"{i}. @{p.get('instagram_handle')}")
            print(f"   Name: {p.get('full_name', 'N/A')}")
            print(f"   Followers: {p.get('followers', 0):,}")
            if p.get('postal_code'):
                print(f"   📮 {p.get('postal_code')}")
            if p.get('address'):
                print(f"   🏠 {p.get('address')[:60]}")
            print(f"   Bio: {(p.get('biography', '')[:80])}...")
            print()

        print(f"💾 CSV saved: {csv_file}")

        # Statistics
        with_postal = sum(1 for p in profiles if p.get('postal_code'))
        with_address = sum(1 for p in profiles if p.get('address'))

        print(f"\n📊 Statistics:")
        print(f"   Total clinics: {len(profiles)}")
        print(f"   With postal code: {with_postal} ({with_postal/len(profiles)*100:.1f}%)")
        print(f"   With address: {with_address} ({with_address/len(profiles)*100:.1f}%)")

    else:
        print("\n⚠️  No dental clinics found in 20 posts")
        print("\nThis could mean:")
        print("  - The top posts are mostly from non-clinic accounts")
        print("  - Try other hashtags: #歯科医院, #小児歯科, #矯正歯科")

if __name__ == "__main__":
    main()
