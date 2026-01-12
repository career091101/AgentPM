#!/usr/bin/env python3
"""
Run dental Instagram data collection for #小児歯科 hashtag
"""
import sys
from pathlib import Path
from datetime import datetime

# Import the collector
from browser_collector import collect_from_hashtag, save_to_csv

def main():
    print("=" * 60)
    print("Instagram Dental Clinic Data Collection")
    print("=" * 60)
    print()

    # Configuration
    hashtag = "小児歯科"
    max_posts = 100

    print(f"📋 Configuration:")
    print(f"   Hashtag: #{hashtag}")
    print(f"   Target posts: {max_posts}")
    print(f"   Mode: Headless (automated)")
    print()

    # Run collection
    print("▶️  Starting collection...")
    print()

    try:
        profiles = collect_from_hashtag(
            hashtag=hashtag,
            max_posts=max_posts,
            headless=True  # Run in headless mode
        )

        # Save to CSV
        if profiles:
            csv_file = save_to_csv(profiles, hashtag)

            # Calculate statistics
            addresses_count = sum(1 for p in profiles if p.get('address'))
            postal_codes_count = sum(1 for p in profiles if p.get('postal_code'))

            print()
            print("=" * 60)
            print("✅ Collection Complete!")
            print("=" * 60)
            print()
            print(f"📊 Results:")
            print(f"   Total clinics found: {len(profiles)}")
            print(f"   With address data: {addresses_count}")
            print(f"   With postal code: {postal_codes_count}")
            print()
            print(f"💾 Output:")
            print(f"   CSV File: {csv_file}")
            print(f"   Timestamp: {datetime.now().isoformat()}")
            print()

        else:
            print()
            print("⚠️  No data collected")
            return 1

    except Exception as e:
        print()
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
