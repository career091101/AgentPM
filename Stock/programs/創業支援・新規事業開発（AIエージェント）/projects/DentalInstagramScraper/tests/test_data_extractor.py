"""
Tests for data_extractor module.
"""
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from models import InstagramProfile
from data_extractor import DataExtractor


def test_postal_code_extraction():
    """Test postal code extraction."""
    extractor = DataExtractor()

    # Test case 1: With 〒 symbol
    bio1 = "〒150-0001 東京都渋谷区神宮前"
    result1 = extractor._extract_postal_code(bio1)
    assert result1 == "150-0001", f"Expected '150-0001', got '{result1}'"

    # Test case 2: Without symbol
    bio2 = "住所: 150-0001 東京都渋谷区神宮前"
    result2 = extractor._extract_postal_code(bio2)
    assert result2 == "150-0001", f"Expected '150-0001', got '{result2}'"

    # Test case 3: No hyphen
    bio3 = "〒1500001 東京都渋谷区神宮前"
    result3 = extractor._extract_postal_code(bio3)
    assert result3 == "150-0001", f"Expected '150-0001', got '{result3}'"

    # Test case 4: Not found
    bio4 = "歯科医院です"
    result4 = extractor._extract_postal_code(bio4)
    assert result4 is None, f"Expected None, got '{result4}'"

    print("✅ test_postal_code_extraction passed")


def test_address_extraction():
    """Test address extraction."""
    extractor = DataExtractor()

    # Test case 1: Full address with postal code
    bio1 = "〒150-0001 東京都渋谷区神宮前1-2-3"
    postal1 = "150-0001"
    result1 = extractor._extract_address(bio1, postal1)
    assert "東京都渋谷区" in result1, f"Expected address with '東京都渋谷区', got '{result1}'"

    # Test case 2: Address without postal code
    bio2 = "大阪府大阪市中央区難波1-2-3 難波ビル"
    result2 = extractor._extract_address(bio2, None)
    assert "大阪府" in result2, f"Expected address with '大阪府', got '{result2}'"

    # Test case 3: Not found
    bio3 = "歯科医院です"
    result3 = extractor._extract_address(bio3, None)
    assert result3 is None, f"Expected None, got '{result3}'"

    print("✅ test_address_extraction passed")


def test_phone_number_extraction():
    """Test phone number extraction."""
    extractor = DataExtractor()

    # Test case 1: Standard format
    bio1 = "電話: 03-1234-5678"
    result1 = extractor._extract_phone_number(bio1)
    assert result1 == "03-1234-5678", f"Expected '03-1234-5678', got '{result1}'"

    # Test case 2: Without hyphens
    bio2 = "電話: 0312345678"
    result2 = extractor._extract_phone_number(bio2)
    assert result2 == "0312345678", f"Expected '0312345678', got '{result2}'"

    # Test case 3: Not found
    bio3 = "歯科医院です"
    result3 = extractor._extract_phone_number(bio3)
    assert result3 is None, f"Expected None, got '{result3}'"

    print("✅ test_phone_number_extraction passed")


def test_full_extraction():
    """Test full extraction pipeline."""
    extractor = DataExtractor()

    profile = InstagramProfile(
        username="test_dental",
        full_name="テスト歯科医院",
        bio="〒150-0001 東京都渋谷区神宮前1-2-3\n電話: 03-1234-5678\n院長: 山田太郎",
        external_url="https://example.com"
    )

    result = extractor.extract(profile)

    assert result.clinic_name == "テスト歯科医院"
    assert result.postal_code == "150-0001"
    assert "東京都渋谷区" in result.address
    assert result.phone_number == "03-1234-5678"
    assert result.person_name == "山田太郎"
    assert result.confidence > 0.5

    print("✅ test_full_extraction passed")
    print(f"   Confidence: {result.confidence:.2f}")


def test_confidence_calculation():
    """Test confidence score calculation."""
    extractor = DataExtractor()

    # Test case 1: High confidence (postal + address)
    profile1 = InstagramProfile(
        username="test1",
        full_name="テスト歯科1",
        bio="〒150-0001 東京都渋谷区神宮前1-2-3"
    )
    result1 = extractor.extract(profile1)
    assert result1.confidence >= 0.9, f"Expected confidence >= 0.9, got {result1.confidence:.2f}"

    # Test case 2: Medium confidence (address only)
    profile2 = InstagramProfile(
        username="test2",
        full_name="テスト歯科2",
        bio="東京都渋谷区神宮前1-2-3"
    )
    result2 = extractor.extract(profile2)
    assert 0.5 <= result2.confidence < 0.9, f"Expected 0.5 <= confidence < 0.9, got {result2.confidence:.2f}"

    # Test case 3: Low confidence (no address info)
    profile3 = InstagramProfile(
        username="test3",
        full_name="テスト歯科3",
        bio="歯科医院です"
    )
    result3 = extractor.extract(profile3)
    assert result3.confidence < 0.5, f"Expected confidence < 0.5, got {result3.confidence:.2f}"

    print("✅ test_confidence_calculation passed")


if __name__ == "__main__":
    print("Running data_extractor tests...\n")

    try:
        test_postal_code_extraction()
        test_address_extraction()
        test_phone_number_extraction()
        test_full_extraction()
        test_confidence_calculation()

        print("\n✅ All tests passed!")

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
