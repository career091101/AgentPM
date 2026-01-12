#!/usr/bin/env python3
"""
Run extended dental Instagram data collection for multiple hashtags
"""
import sys
from pathlib import Path
from datetime import datetime

# Import the collector
from browser_collector import collect_from_hashtag, save_to_csv

def main():
    print("=" * 70)
    print("Extended Instagram Dental Clinic Data Collection")
    print("=" * 70)
    print()

    # Multiple hashtags to search
    hashtags = ["小児歯科", "歯科医院", "歯科", "dental_clinic_japan"]
    max_posts_per_hashtag = 30  # Reduced to test multiple hashtags

    all_profiles = []
    hashtag_results = {}

    for hashtag in hashtags:
        print(f"\n{'=' * 70}")
        print(f"📍 Searching hashtag: #{hashtag}")
        print(f"{'=' * 70}\n")

        try:
            profiles = collect_from_hashtag(
                hashtag=hashtag,
                max_posts=max_posts_per_hashtag,
                headless=True
            )

            hashtag_results[hashtag] = len(profiles)
            all_profiles.extend(profiles)

            print()

        except Exception as e:
            print(f"\n❌ Error collecting from #{hashtag}: {e}")
            hashtag_results[hashtag] = 0
            continue

    # Summary
    print()
    print("=" * 70)
    print("✅ Collection Complete!")
    print("=" * 70)
    print()

    # Calculate statistics
    if all_profiles:
        addresses_count = sum(1 for p in all_profiles if p.get('address'))
        postal_codes_count = sum(1 for p in all_profiles if p.get('postal_code'))

        print(f"📊 Summary by Hashtag:")
        for hashtag, count in hashtag_results.items():
            print(f"   #{hashtag}: {count} clinics")
        print()
        print(f"📊 Total Results:")
        print(f"   Total unique clinics: {len(all_profiles)}")
        print(f"   With address data: {addresses_count}")
        print(f"   With postal code: {postal_codes_count}")
        print()

        # Save to CSV
        csv_file = save_to_csv(all_profiles, "dental_extended")
        print()
        print(f"💾 Output:")
        print(f"   CSV File: {csv_file}")
        print(f"   Timestamp: {datetime.now().isoformat()}")
        print()

        return 0

    else:
        print(f"⚠️  No clinics found across all hashtags")
        print()
        print(f"📊 Hashtag Results:")
        for hashtag, count in hashtag_results.items():
            print(f"   #{hashtag}: {count} clinics")
        return 1

if __name__ == "__main__":
    sys.exit(main())
