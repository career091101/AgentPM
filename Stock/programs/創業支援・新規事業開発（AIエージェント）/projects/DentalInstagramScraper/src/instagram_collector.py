"""
Instagram Collector Module

This module handles Instagram data collection using the instaloader library.
Collects profiles from hashtag searches.
"""

import logging
import os
import time
from typing import List
from pathlib import Path

import instaloader

try:
    from .models import InstagramProfile
except ImportError:
    from models import InstagramProfile


class InstagramCollector:
    """Instagram data collector using instaloader."""

    def __init__(self, session_file: str = '.instagram_session', rate_limit_delay: float = 5.0):
        """
        Initialize the Instagram collector.

        Args:
            session_file: Path to the session file for persistent login
            rate_limit_delay: Delay in seconds between requests to avoid rate limits
        """
        self.logger = logging.getLogger(__name__)
        self.session_file = session_file
        self.rate_limit_delay = rate_limit_delay

        # Initialize instaloader
        self.loader = instaloader.Instaloader(
            download_pictures=False,
            download_videos=False,
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            compress_json=False,
            quiet=True
        )

        self.logger.info("InstagramCollector initialized")

    def login(self, username: str, password: str) -> bool:
        """
        Login to Instagram.

        Args:
            username: Instagram username
            password: Instagram password

        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            # Try to load existing session
            if os.path.exists(self.session_file):
                self.logger.info(f"Loading existing session from {self.session_file}")
                self.loader.load_session_from_file(username, self.session_file)
                self.logger.info("Session loaded successfully")
                return True

        except Exception as e:
            self.logger.warning(f"Failed to load session: {e}")

        # Perform new login
        try:
            self.logger.info(f"Logging in as {username}...")
            self.loader.login(username, password)

            # Save session for future use
            self.loader.save_session_to_file(self.session_file)
            self.logger.info("Login successful and session saved")
            return True

        except Exception as e:
            self.logger.error(f"Login failed: {e}")
            return False

    def collect_from_hashtag(self, hashtag: str, max_posts: int = 100) -> List[InstagramProfile]:
        """
        Collect Instagram profiles from a hashtag.

        Args:
            hashtag: Hashtag to search (without # symbol)
            max_posts: Maximum number of posts to process

        Returns:
            List[InstagramProfile]: List of unique profiles
        """
        profiles = []
        seen_usernames = set()

        try:
            self.logger.info(f"Searching hashtag: #{hashtag}")

            # Get posts from hashtag
            posts = self.loader.get_hashtag_posts(hashtag)

            count = 0
            for post in posts:
                if count >= max_posts:
                    break

                try:
                    # Get profile from post owner
                    profile = post.owner_profile

                    # Skip if already seen
                    if profile.username in seen_usernames:
                        continue

                    # Check if profile looks like a dental clinic
                    if self._is_dental_related(profile):
                        instagram_profile = self._convert_to_profile(profile)
                        profiles.append(instagram_profile)
                        seen_usernames.add(profile.username)

                        self.logger.info(
                            f"Collected profile: {profile.username} "
                            f"({len(profiles)} profiles so far)"
                        )

                    count += 1

                    # Rate limiting
                    time.sleep(self.rate_limit_delay)

                except Exception as e:
                    self.logger.warning(f"Error processing post: {e}")
                    continue

            self.logger.info(
                f"Collected {len(profiles)} dental clinic profiles "
                f"from #{hashtag} (processed {count} posts)"
            )

        except Exception as e:
            self.logger.error(f"Error collecting from hashtag #{hashtag}: {e}")

        return profiles

    def _is_dental_related(self, profile) -> bool:
        """
        Check if profile is related to dental clinics.

        Args:
            profile: Instaloader Profile object

        Returns:
            bool: True if profile appears to be dental-related
        """
        # Keywords to look for in bio and username
        dental_keywords = [
            '歯科', '歯医者', 'デンタル', 'dental', 'clinic',
            '矯正', '審美', 'ホワイトニング', 'インプラント',
            '小児歯科', 'クリニック', '医院'
        ]

        bio_lower = profile.biography.lower() if profile.biography else ''
        username_lower = profile.username.lower()
        full_name_lower = profile.full_name.lower() if profile.full_name else ''

        # Check if any keyword is in bio, username, or full name
        for keyword in dental_keywords:
            if (keyword.lower() in bio_lower or
                keyword.lower() in username_lower or
                keyword.lower() in full_name_lower):
                return True

        return False

    def _convert_to_profile(self, insta_profile) -> InstagramProfile:
        """
        Convert instaloader Profile to InstagramProfile.

        Args:
            insta_profile: Instaloader Profile object

        Returns:
            InstagramProfile: Converted profile
        """
        return InstagramProfile(
            username=insta_profile.username,
            full_name=insta_profile.full_name or '',
            bio=insta_profile.biography or '',
            external_url=insta_profile.external_url,
            followers_count=insta_profile.followers,
            following_count=insta_profile.followees,
            posts_count=insta_profile.mediacount
        )

    def get_profile(self, username: str) -> InstagramProfile:
        """
        Get a specific Instagram profile by username.

        Args:
            username: Instagram username

        Returns:
            InstagramProfile: Profile data

        Raises:
            Exception: If profile not found or error occurs
        """
        try:
            self.logger.info(f"Fetching profile: {username}")
            profile = instaloader.Profile.from_username(self.loader.context, username)

            # Rate limiting
            time.sleep(self.rate_limit_delay)

            return self._convert_to_profile(profile)

        except Exception as e:
            self.logger.error(f"Error fetching profile {username}: {e}")
            raise
