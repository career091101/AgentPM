"""
Example usage of data_extractor and fact_checker modules.

This script demonstrates how to use the extraction and verification pipeline.
"""
import os
import logging
from src.models import InstagramProfile
from src.data_extractor import DataExtractor
from src.fact_checker import FactChecker


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def example_data_extraction():
    """Example: Extract clinic data from Instagram profile."""
    print("\n" + "="*80)
    print("Example 1: Data Extraction")
    print("="*80 + "\n")

    # Create sample Instagram profile
    profile = InstagramProfile(
        username="sample_dental_clinic",
        full_name="サンプル歯科医院",
        bio="""
        〒150-0001 東京都渋谷区神宮前1-2-3 渋谷ビル2F
        電話: 03-1234-5678
        院長: 山田太郎

        一般歯科、矯正歯科、インプラント
        平日 9:00-18:00
        土曜 9:00-13:00
        """,
        external_url="https://example.com/clinic",
        followers_count=1500,
        following_count=200,
        posts_count=120
    )

    # Initialize extractor
    extractor = DataExtractor(scrape_delay=5.0, request_timeout=10)

    # Extract data
    logger.info("Starting data extraction...")
    extracted = extractor.extract(profile)

    # Display results
    print(f"Clinic Name: {extracted.clinic_name}")
    print(f"Postal Code: {extracted.postal_code}")
    print(f"Address: {extracted.address}")
    print(f"Phone Number: {extracted.phone_number}")
    print(f"Person Name: {extracted.person_name}")
    print(f"External Link: {extracted.external_link}")
    print(f"Confidence Score: {extracted.confidence:.2f}")
    print(f"Needs Manual Review: {extracted.needs_manual_review}")
    print(f"Notes: {extracted.extraction_notes}")

    return extracted


def example_fact_checking(extracted_data):
    """Example: Verify extracted data using Anthropic API."""
    print("\n" + "="*80)
    print("Example 2: Fact Checking")
    print("="*80 + "\n")

    # Get API key from environment
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("⚠️  ANTHROPIC_API_KEY not found in environment variables.")
        print("   Skipping fact checking example.")
        print("   To enable, set: export ANTHROPIC_API_KEY='your-api-key'")
        return None

    # Initialize fact checker
    checker = FactChecker(anthropic_api_key=api_key)

    # Verify data
    logger.info("Starting fact check...")
    try:
        result = checker.verify(extracted_data, max_retries=3)

        # Display results
        print(f"Verification Status: {result.status}")
        print(f"Verified Address: {result.verified_address}")
        print(f"Similarity Score: {result.similarity_score:.2f}")
        print(f"Search Query: {result.search_query}")
        print(f"Sources: {', '.join(result.sources[:3])}")
        print(f"Notes: {result.verification_notes}")

        return result

    except Exception as e:
        logger.error(f"Fact checking failed: {str(e)}")
        print(f"❌ Error: {str(e)}")
        return None


def example_complete_pipeline():
    """Example: Complete extraction and verification pipeline."""
    print("\n" + "="*80)
    print("Example 3: Complete Pipeline")
    print("="*80 + "\n")

    # Sample profiles
    profiles = [
        InstagramProfile(
            username="clinic_a",
            full_name="A歯科医院",
            bio="〒100-0001 東京都千代田区千代田1-1-1",
            external_url="https://example.com/clinic-a"
        ),
        InstagramProfile(
            username="clinic_b",
            full_name="B歯科クリニック",
            bio="大阪府大阪市中央区難波2-2-2\nTEL: 06-1234-5678",
            external_url=None
        ),
        InstagramProfile(
            username="clinic_c",
            full_name="C歯科",
            bio="院長: 佐藤花子\n一般歯科・小児歯科",
            external_url="https://example.com/clinic-c"
        ),
    ]

    extractor = DataExtractor()
    results = []

    for profile in profiles:
        print(f"\nProcessing: {profile.username}")
        print("-" * 40)

        # Extract
        extracted = extractor.extract(profile)
        print(f"  Extracted - Confidence: {extracted.confidence:.2f}")

        results.append({
            'username': profile.username,
            'extracted': extracted
        })

    print(f"\n✅ Processed {len(results)} profiles")
    return results


if __name__ == "__main__":
    print("\n" + "="*80)
    print("Instagram Dental Clinic Scraper - Usage Examples")
    print("="*80)

    # Example 1: Data Extraction
    extracted = example_data_extraction()

    # Example 2: Fact Checking (requires API key)
    if extracted:
        example_fact_checking(extracted)

    # Example 3: Complete Pipeline
    example_complete_pipeline()

    print("\n" + "="*80)
    print("Examples completed!")
    print("="*80 + "\n")
