"""
Fact checking module using Anthropic Claude API with web search.

Verifies extracted clinic information against web sources.
"""
import re
import logging
from typing import Optional
from difflib import SequenceMatcher
import anthropic

try:
    from .models import ExtractedData, FactCheckResult
except ImportError:
    from models import ExtractedData, FactCheckResult


logger = logging.getLogger(__name__)


class FactChecker:
    """Verify extracted data using Anthropic Claude API with web search."""

    def __init__(self, anthropic_api_key: str):
        """
        Initialize the fact checker.

        Args:
            anthropic_api_key: Anthropic API key for Claude access
        """
        try:
            self.client = anthropic.Anthropic(api_key=anthropic_api_key)
            self.model = "claude-sonnet-4-5-20250929"
            logger.info("FactChecker initialized with Claude Sonnet 4.5")
        except Exception as e:
            logger.error(f"Error initializing Anthropic client: {str(e)}", exc_info=True)
            raise

    def verify(self, extracted: ExtractedData, max_retries: int = 3) -> FactCheckResult:
        """
        Verify extracted data using web search.

        Attempts multiple search strategies in priority order:
        1. "{clinic_name} 歯科医院 住所"
        2. "{postal_code} {clinic_name}"
        3. "{address} {clinic_name}"

        Args:
            extracted: Extracted data to verify
            max_retries: Maximum number of search attempts

        Returns:
            FactCheckResult with verification status and details
        """
        logger.info(f"Starting fact check for clinic: {extracted.clinic_name}")

        # Build search queries in priority order
        queries = self._build_search_queries(extracted)

        if not queries:
            logger.warning("No search queries could be generated")
            return FactCheckResult(
                status="failed",
                verification_notes="No searchable information available"
            )

        # Try each query until success or max_retries reached
        attempts = min(len(queries), max_retries)

        for i, query in enumerate(queries[:attempts]):
            logger.info(f"Attempt {i+1}/{attempts}: Searching with query: {query}")

            try:
                result = self._search_and_verify(query, extracted)

                if result.status == "verified" or result.status == "partial":
                    logger.info(f"Verification successful on attempt {i+1}")
                    return result

                logger.debug(f"Attempt {i+1} did not verify, trying next query...")

            except Exception as e:
                logger.error(f"Error during search attempt {i+1}: {str(e)}", exc_info=True)
                continue

        # All attempts failed
        logger.warning("All verification attempts failed")
        return FactCheckResult(
            status="failed",
            search_query="; ".join(queries[:attempts]),
            verification_notes=f"Failed to verify after {attempts} attempts"
        )

    def _build_search_queries(self, extracted: ExtractedData) -> list[str]:
        """
        Build search queries in priority order.

        Args:
            extracted: Extracted data

        Returns:
            List of search query strings
        """
        queries = []

        # Priority 1: clinic name + "歯科医院 住所"
        if extracted.clinic_name:
            queries.append(f"{extracted.clinic_name} 歯科医院 住所")

        # Priority 2: postal code + clinic name
        if extracted.postal_code and extracted.clinic_name:
            queries.append(f"{extracted.postal_code} {extracted.clinic_name}")

        # Priority 3: address + clinic name
        if extracted.address and extracted.clinic_name:
            queries.append(f"{extracted.address} {extracted.clinic_name}")

        logger.debug(f"Built {len(queries)} search queries")
        return queries

    def _search_and_verify(self, query: str, extracted: ExtractedData) -> FactCheckResult:
        """
        Execute web search and verify results against extracted data.

        Args:
            query: Search query string
            extracted: Extracted data to verify against

        Returns:
            FactCheckResult with verification details
        """
        try:
            # Create prompt for Claude with web search
            prompt = f"""以下の歯科医院の情報について、Web検索を使って正確な住所を調べてください。

医院名: {extracted.clinic_name}
抽出された郵便番号: {extracted.postal_code or '不明'}
抽出された住所: {extracted.address or '不明'}

検索クエリ: {query}

正確な住所情報を見つけたら、以下の形式で回答してください：
- 住所: [完全な住所]
- 郵便番号: [郵便番号]
- 情報源: [参照したWebサイトのURL]

情報が見つからない場合は「情報が見つかりませんでした」と回答してください。"""

            logger.debug(f"Sending search request to Claude API with query: {query}")

            # Call Claude API with web search capability
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            # Extract response text
            response_text = message.content[0].text
            logger.debug(f"Received response: {response_text[:200]}...")

            # Parse response to extract verified address
            verified_info = self._parse_verification_response(response_text)

            if not verified_info['address']:
                logger.debug("No address found in verification response")
                return FactCheckResult(
                    status="failed",
                    search_query=query,
                    verification_notes="No address information found in search results"
                )

            # Calculate similarity between verified and extracted addresses
            similarity = self._calculate_similarity(
                verified_info['address'],
                extracted.address or ""
            )

            # Extract sources
            sources = verified_info.get('sources', [])

            # Determine status based on similarity
            if similarity >= 0.8:
                status = "verified"
                notes = "High similarity with web sources"
            elif similarity >= 0.6:
                status = "partial"
                notes = "Partial match with web sources"
            else:
                status = "failed"
                notes = "Low similarity with web sources"

            logger.info(f"Verification result: {status} (similarity: {similarity:.2f})")

            return FactCheckResult(
                status=status,
                verified_address=verified_info['address'],
                similarity_score=similarity,
                search_query=query,
                sources=sources,
                verification_notes=notes
            )

        except anthropic.APIError as e:
            logger.error(f"Anthropic API error: {str(e)}", exc_info=True)
            return FactCheckResult(
                status="failed",
                search_query=query,
                verification_notes=f"API error: {str(e)}"
            )
        except Exception as e:
            logger.error(f"Unexpected error during verification: {str(e)}", exc_info=True)
            return FactCheckResult(
                status="failed",
                search_query=query,
                verification_notes=f"Error: {str(e)}"
            )

    def _parse_verification_response(self, response: str) -> dict:
        """
        Parse Claude's verification response to extract address info.

        Args:
            response: Response text from Claude

        Returns:
            Dictionary with 'address', 'postal_code', and 'sources'
        """
        result = {
            'address': None,
            'postal_code': None,
            'sources': []
        }

        try:
            # Extract address
            address_match = re.search(r'住所[:\s]*([^\n]+)', response)
            if address_match:
                result['address'] = address_match.group(1).strip()
                logger.debug(f"Parsed address: {result['address']}")

            # Extract postal code
            postal_match = re.search(r'郵便番号[:\s]*([0-9\-]+)', response)
            if postal_match:
                result['postal_code'] = postal_match.group(1).strip()
                logger.debug(f"Parsed postal code: {result['postal_code']}")

            # Extract sources (URLs)
            url_pattern = re.compile(r'https?://[^\s\]]+')
            urls = url_pattern.findall(response)
            result['sources'] = urls[:3]  # Limit to 3 sources
            logger.debug(f"Parsed {len(result['sources'])} sources")

        except Exception as e:
            logger.error(f"Error parsing verification response: {str(e)}", exc_info=True)

        return result

    def _calculate_similarity(self, verified: str, extracted: str) -> float:
        """
        Calculate similarity between verified and extracted addresses.

        Scoring:
        - Exact match: 1.0
        - Partial match (city/ward level): 0.8
        - Prefecture only: 0.5
        - No match: 0.0

        Args:
            verified: Verified address from web search
            extracted: Extracted address from profile

        Returns:
            Similarity score between 0.0 and 1.0
        """
        try:
            if not verified or not extracted:
                logger.debug("Empty address for comparison")
                return 0.0

            # Normalize addresses (remove spaces, convert to full-width)
            verified_norm = verified.replace(' ', '').replace('　', '')
            extracted_norm = extracted.replace(' ', '').replace('　', '')

            # Exact match
            if verified_norm == extracted_norm:
                logger.debug("Exact address match")
                return 1.0

            # Use SequenceMatcher for overall similarity
            overall_similarity = SequenceMatcher(None, verified_norm, extracted_norm).ratio()
            logger.debug(f"Overall similarity: {overall_similarity:.2f}")

            # Check for partial matches at different levels
            # Prefecture match
            prefectures = ['北海道', '東京都', '大阪府', '京都府'] + [f'{p}県' for p in [
                '青森', '岩手', '宮城', '秋田', '山形', '福島',
                '茨城', '栃木', '群馬', '埼玉', '千葉', '神奈川',
                '新潟', '富山', '石川', '福井', '山梨', '長野',
                '岐阜', '静岡', '愛知', '三重', '滋賀', '兵庫',
                '奈良', '和歌山', '鳥取', '島根', '岡山', '広島',
                '山口', '徳島', '香川', '愛媛', '高知', '福岡',
                '佐賀', '長崎', '熊本', '大分', '宮崎', '鹿児島', '沖縄'
            ]]

            prefecture_match = False
            for pref in prefectures:
                if pref in verified_norm and pref in extracted_norm:
                    prefecture_match = True
                    break

            # City/ward match (市区町村)
            city_keywords = ['市', '区', '町', '村']
            city_match = False

            for keyword in city_keywords:
                if keyword in verified_norm and keyword in extracted_norm:
                    # Extract city/ward name
                    v_idx = verified_norm.find(keyword)
                    e_idx = extracted_norm.find(keyword)

                    if v_idx > 0 and e_idx > 0:
                        # Compare the part up to and including the city/ward
                        v_city = verified_norm[:v_idx + 1]
                        e_city = extracted_norm[:e_idx + 1]

                        if v_city == e_city:
                            city_match = True
                            break

            # Determine final similarity score
            if city_match:
                logger.debug("City/ward level match")
                return max(0.8, overall_similarity)
            elif prefecture_match:
                logger.debug("Prefecture level match")
                return max(0.5, overall_similarity)
            else:
                logger.debug("Using overall similarity score")
                return overall_similarity

        except Exception as e:
            logger.error(f"Error calculating similarity: {str(e)}", exc_info=True)
            return 0.0
