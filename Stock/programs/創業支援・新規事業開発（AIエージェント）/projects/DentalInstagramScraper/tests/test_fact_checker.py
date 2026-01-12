"""
Tests for fact_checker module.
"""
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from models import ExtractedData
from fact_checker import FactChecker


def test_similarity_calculation():
    """Test address similarity calculation."""
    # Note: This test doesn't require API key
    checker = FactChecker(anthropic_api_key="dummy_key_for_testing")

    # Test case 1: Exact match
    verified1 = "東京都渋谷区神宮前1-2-3"
    extracted1 = "東京都渋谷区神宮前1-2-3"
    similarity1 = checker._calculate_similarity(verified1, extracted1)
    assert similarity1 == 1.0, f"Expected 1.0 for exact match, got {similarity1:.2f}"

    # Test case 2: City/ward match
    verified2 = "東京都渋谷区神宮前1-2-3"
    extracted2 = "東京都渋谷区神宮前4-5-6"
    similarity2 = checker._calculate_similarity(verified2, extracted2)
    assert similarity2 >= 0.8, f"Expected >= 0.8 for city match, got {similarity2:.2f}"

    # Test case 3: Prefecture only match
    verified3 = "東京都渋谷区神宮前1-2-3"
    extracted3 = "東京都新宿区西新宿1-1-1"
    similarity3 = checker._calculate_similarity(verified3, extracted3)
    assert 0.5 <= similarity3 < 0.8, f"Expected 0.5-0.8 for prefecture match, got {similarity3:.2f}"

    # Test case 4: No match
    verified4 = "東京都渋谷区神宮前1-2-3"
    extracted4 = "大阪府大阪市中央区難波1-1-1"
    similarity4 = checker._calculate_similarity(verified4, extracted4)
    assert similarity4 < 0.5, f"Expected < 0.5 for no match, got {similarity4:.2f}"

    # Test case 5: Empty addresses
    similarity5 = checker._calculate_similarity("", "東京都渋谷区")
    assert similarity5 == 0.0, f"Expected 0.0 for empty address, got {similarity5:.2f}"

    print("✅ test_similarity_calculation passed")


def test_build_search_queries():
    """Test search query building."""
    checker = FactChecker(anthropic_api_key="dummy_key_for_testing")

    # Test case 1: All data available
    extracted1 = ExtractedData(
        clinic_name="テスト歯科医院",
        postal_code="150-0001",
        address="東京都渋谷区神宮前1-2-3"
    )
    queries1 = checker._build_search_queries(extracted1)
    assert len(queries1) == 3, f"Expected 3 queries, got {len(queries1)}"
    assert "テスト歯科医院 歯科医院 住所" in queries1[0]
    assert "150-0001" in queries1[1]
    assert "東京都渋谷区" in queries1[2]

    # Test case 2: Only clinic name available
    extracted2 = ExtractedData(
        clinic_name="テスト歯科医院"
    )
    queries2 = checker._build_search_queries(extracted2)
    assert len(queries2) == 1, f"Expected 1 query, got {len(queries2)}"
    assert "テスト歯科医院 歯科医院 住所" in queries2[0]

    # Test case 3: No postal code
    extracted3 = ExtractedData(
        clinic_name="テスト歯科医院",
        address="東京都渋谷区神宮前1-2-3"
    )
    queries3 = checker._build_search_queries(extracted3)
    assert len(queries3) == 2, f"Expected 2 queries, got {len(queries3)}"

    print("✅ test_build_search_queries passed")


def test_parse_verification_response():
    """Test parsing of verification response."""
    checker = FactChecker(anthropic_api_key="dummy_key_for_testing")

    # Test case 1: Complete response
    response1 = """
    住所: 東京都渋谷区神宮前1-2-3
    郵便番号: 150-0001
    情報源: https://example.com/clinic
    """
    parsed1 = checker._parse_verification_response(response1)
    assert parsed1['address'] == "東京都渋谷区神宮前1-2-3"
    assert parsed1['postal_code'] == "150-0001"
    assert len(parsed1['sources']) > 0
    assert "example.com" in parsed1['sources'][0]

    # Test case 2: Address only
    response2 = "住所: 大阪府大阪市中央区難波1-1-1"
    parsed2 = checker._parse_verification_response(response2)
    assert parsed2['address'] == "大阪府大阪市中央区難波1-1-1"
    assert parsed2['postal_code'] is None

    # Test case 3: Not found
    response3 = "情報が見つかりませんでした"
    parsed3 = checker._parse_verification_response(response3)
    assert parsed3['address'] is None
    assert parsed3['postal_code'] is None

    print("✅ test_parse_verification_response passed")


if __name__ == "__main__":
    print("Running fact_checker tests...\n")

    try:
        test_similarity_calculation()
        test_build_search_queries()
        test_parse_verification_response()

        print("\n✅ All tests passed!")
        print("\nNote: Full API integration test skipped (requires valid Anthropic API key)")

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
