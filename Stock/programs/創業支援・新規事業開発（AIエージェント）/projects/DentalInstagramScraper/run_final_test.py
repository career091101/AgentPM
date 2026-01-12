#!/usr/bin/env python3
"""
Final test - Collect 5 dental clinic profiles from #歯科 hashtag
"""
from browser_collector import collect_from_hashtag, save_to_csv

def main():
    print("🦷 Final Test: Instagram Dental Clinic Collector")
    print("="*60)
    print("\nCollecting 5 profiles from #歯科 hashtag...")
    print("Using 2024-2025 optimized methods\n")

    profiles = collect_from_hashtag(
        hashtag="歯科",
        max_posts=5,  # Small test with 5 posts
        headless=False  # Show browser for visibility
    )

    if profiles:
        print(f"\n✅ Success! Found {len(profiles)} dental clinic profiles")

        # Save to CSV
        csv_file = save_to_csv(profiles, "歯科")

        print(f"\n📋 Results:")
        for p in profiles:
            print(f"\n   @{p.get('instagram_handle')}")
            print(f"   Name: {p.get('full_name', 'N/A')}")
            print(f"   Followers: {p.get('followers', 0):,}")
            if p.get('postal_code'):
                print(f"   📮 {p.get('postal_code')}")
            if p.get('address'):
                print(f"   🏠 {p.get('address')[:50]}...")

    else:
        print("\n⚠️  No profiles collected")
        print("This might be due to:")
        print("  - All posts from same account")
        print("  - None match dental keywords")
        print("  - Network/loading issues")

if __name__ == "__main__":
    main()
