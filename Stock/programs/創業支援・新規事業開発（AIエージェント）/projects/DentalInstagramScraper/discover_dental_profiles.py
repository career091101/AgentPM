#!/usr/bin/env python3
"""
Discover dental clinic Instagram profiles using seed keywords
Since hashtag search doesn't work, we'll use direct profile access
and Instagram's profile suggestions
"""
import instaloader
import http.cookiejar
from pathlib import Path
import time
import json
from datetime import datetime

def discover_profiles():
    """Discover dental clinic profiles"""
    print("🔍 Discovering dental clinic Instagram profiles...\n")

    loader = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        save_metadata=False
    )

    # Load cookies
    cookie_file = Path("instagram_cookies.txt")
    cj = http.cookiejar.MozillaCookieJar(str(cookie_file))
    cj.load(ignore_discard=True, ignore_expires=True)
    loader.context._session.cookies = cj

    print(f"✅ Loaded {len(cj)} cookies\n")

    # Seed list - common dental clinic naming patterns
    seed_keywords = [
        # Japanese patterns
        "shikaiin_tokyo", "shikaiin_osaka", "shikaiin_yokohama",
        "dental_clinic_tokyo", "dental_clinic_osaka",
        "haisha_tokyo", "haisha_osaka",
        "kyousei_shika",  # 矯正歯科
        "kodomo_shika",   # 小児歯科

        # English patterns
        "dentalclinic_jp", "dentalclinicjp",
        "tokyodental", "osakadental",
        "japan_dental", "dental_japan",

        # Real profiles (for testing)
        "dentaltown",
    ]

    discovered_profiles = []
    dental_keywords = ['歯科', '歯医者', 'デンタル', 'dental', 'clinic', '矯正', '小児歯科', '審美歯科']

    print("📋 Starting profile discovery...\n")

    for keyword in seed_keywords:
        print(f"🔎 Testing: @{keyword}")

        try:
            profile = instaloader.Profile.from_username(loader.context, keyword)

            # Profile exists!
            bio_lower = profile.biography.lower() if profile.biography else ""
            is_dental = any(kw in bio_lower for kw in dental_keywords)
            is_business = profile.is_business_account

            if is_dental or is_business:
                print(f"   ✅ Found dental profile!")
                print(f"      Name: {profile.full_name}")
                print(f"      Followers: {profile.followers:,}")
                print(f"      Bio: {(profile.biography[:80] + '...') if profile.biography else 'No bio'}")

                discovered_profiles.append({
                    'username': profile.username,
                    'full_name': profile.full_name,
                    'followers': profile.followers,
                    'biography': profile.biography,
                    'external_url': profile.external_url,
                    'is_business_account': profile.is_business_account,
                    'posts': profile.mediacount,
                    'discovered_from': keyword,
                    'discovered_at': datetime.now().isoformat()
                })

                print(f"      ✅ Added to collection ({len(discovered_profiles)} total)\n")

                # Rate limiting
                time.sleep(5)

        except Exception as e:
            error_msg = str(e)

            # Check if Instagram suggests similar profiles
            if "The most similar profiles are:" in error_msg or "does not exist" in error_msg:
                print(f"   ⚠️  Profile doesn't exist")

                # Extract suggested profiles from error message
                # Format: "The most similar profiles are: profile1, profile2, profile3."
                if "similar profiles are:" in error_msg:
                    try:
                        suggestions_part = error_msg.split("similar profiles are:")[1].strip()
                        suggestions = [s.strip().rstrip('.') for s in suggestions_part.split(',')]
                        print(f"   💡 Instagram suggests: {', '.join(suggestions[:3])}")

                        # TODO: Could recursively check these suggestions
                        # For now, just log them

                    except Exception:
                        pass

            else:
                print(f"   ❌ Error: {error_msg}")

            print()
            time.sleep(3)

    # Save discovered profiles
    if discovered_profiles:
        output_file = f"discovered_profiles_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(discovered_profiles, f, ensure_ascii=False, indent=2)

        print(f"\n✅ Discovery complete!")
        print(f"   Total profiles found: {len(discovered_profiles)}")
        print(f"   Saved to: {output_file}")

        # Show summary
        print(f"\n📊 Summary:")
        for profile in discovered_profiles:
            print(f"   - @{profile['username']} ({profile['followers']:,} followers)")

    else:
        print("\n⚠️  No dental clinic profiles found")
        print("   Consider using web search to find real dental clinic Instagram handles")

    return discovered_profiles

if __name__ == "__main__":
    discover_profiles()
