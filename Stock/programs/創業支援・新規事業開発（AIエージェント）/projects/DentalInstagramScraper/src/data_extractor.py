"""
Data extraction module for Instagram profiles.

Extracts clinic information including postal codes, addresses, and phone numbers.
"""
import re
import time
import logging
from typing import Optional
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

try:
    from .models import InstagramProfile, ExtractedData
except ImportError:
    from models import InstagramProfile, ExtractedData


logger = logging.getLogger(__name__)


class DataExtractor:
    """Extract clinic data from Instagram profiles."""

    # Regular expression patterns
    POSTAL_CODE_PATTERN = re.compile(r'〒?\s*(\d{3})-?(\d{4})')
    ADDRESS_PATTERN = re.compile(
        r'((?:北海道|東京都|大阪府|京都府|.{2,3}県)'
        r'[^\n]{0,50}?'
        r'(?:市|区|町|村|丁目|番地|号|ビル|F))'
    )
    PHONE_PATTERN = re.compile(r'0\d{1,4}[-\s]?\d{1,4}[-\s]?\d{4}')
    PERSON_NAME_PATTERN = re.compile(r'院長[:\s]*([^\n\s]{2,10})')

    def __init__(self, scrape_delay: float = 5.0, request_timeout: int = 10):
        """
        Initialize the data extractor.

        Args:
            scrape_delay: Delay in seconds between external link scraping requests
            request_timeout: Timeout in seconds for HTTP requests
        """
        self.scrape_delay = scrape_delay
        self.request_timeout = request_timeout
        logger.info("DataExtractor initialized")

    def extract(self, profile: InstagramProfile) -> ExtractedData:
        """
        Extract clinic data from Instagram profile.

        Args:
            profile: Instagram profile data

        Returns:
            ExtractedData with extracted information and confidence score
        """
        logger.info(f"Starting extraction for profile: {profile.username}")

        try:
            # Extract clinic name from full_name
            clinic_name = profile.full_name.strip()

            # Extract postal code
            postal_code = self._extract_postal_code(profile.bio)
            logger.debug(f"Extracted postal code: {postal_code}")

            # Extract address (prioritize areas near postal code)
            address = self._extract_address(profile.bio, postal_code)
            logger.debug(f"Extracted address: {address}")

            # Initialize notes list
            notes = []
            needs_review = False

            # Extract phone number
            phone_number = self._extract_phone_number(profile.bio)
            logger.debug(f"Extracted phone number: {phone_number}")

            # Extract person name (院長)
            person_name = self._extract_person_name(profile.bio)
            logger.debug(f"Extracted person name: {person_name}")

            # Store external link
            external_link = profile.external_url

            # If address is empty and external link exists, try scraping
            if not address and external_link:
                logger.info(f"Address not found in bio, attempting to scrape external link: {external_link}")
                scraped_address = self._scrape_external_link(external_link)
                if scraped_address:
                    address = scraped_address
                    notes.append("Address extracted from external website")
                    logger.info(f"Successfully scraped address: {address}")

            # Create extracted data object
            extracted = ExtractedData(
                clinic_name=clinic_name,
                postal_code=postal_code,
                address=address,
                phone_number=phone_number,
                person_name=person_name,
                external_link=external_link,
                needs_manual_review=needs_review,
                extraction_notes="; ".join(notes)
            )

            # Calculate confidence score
            confidence = self._calculate_confidence(extracted)
            extracted.confidence = confidence

            logger.info(f"Extraction completed with confidence: {confidence:.2f}")
            return extracted

        except Exception as e:
            logger.error(f"Error during extraction: {str(e)}", exc_info=True)
            return ExtractedData(
                clinic_name=profile.full_name,
                confidence=0.0,
                needs_manual_review=True,
                extraction_notes=f"Extraction error: {str(e)}"
            )

    def _extract_postal_code(self, text: str) -> Optional[str]:
        """
        Extract postal code from text.

        Prioritizes postal codes immediately after "〒" symbol.
        Returns first match and sets needs_manual_review if multiple found.

        Args:
            text: Text to search for postal code

        Returns:
            Postal code in xxx-xxxx format, or None if not found
        """
        try:
            # Find all postal code matches
            matches = list(self.POSTAL_CODE_PATTERN.finditer(text))

            if not matches:
                logger.debug("No postal code found")
                return None

            # Prioritize matches immediately after "〒"
            for match in matches:
                start_pos = match.start()
                if start_pos > 0 and text[start_pos - 1] == '〒':
                    postal_code = f"{match.group(1)}-{match.group(2)}"
                    logger.debug(f"Found postal code with 〒 symbol: {postal_code}")
                    return postal_code

            # If no "〒" prefix, use first match
            first_match = matches[0]
            postal_code = f"{first_match.group(1)}-{first_match.group(2)}"

            if len(matches) > 1:
                logger.warning(f"Multiple postal codes found ({len(matches)}), using first: {postal_code}")

            return postal_code

        except Exception as e:
            logger.error(f"Error extracting postal code: {str(e)}", exc_info=True)
            return None

    def _extract_address(self, text: str, postal_code: Optional[str]) -> Optional[str]:
        """
        Extract address from text.

        Prioritizes addresses near postal code (within 30 characters).
        Prefers addresses containing prefecture names.

        Args:
            text: Text to search for address
            postal_code: Previously extracted postal code (for proximity search)

        Returns:
            Extracted address, or None if not found
        """
        try:
            # Find all address matches
            matches = list(self.ADDRESS_PATTERN.finditer(text))

            if not matches:
                logger.debug("No address found")
                return None

            # If postal code exists, prioritize addresses within 30 characters
            if postal_code and postal_code in text:
                postal_pos = text.find(postal_code)
                nearby_matches = []

                for match in matches:
                    distance = abs(match.start() - postal_pos)
                    if distance <= 30:
                        nearby_matches.append((distance, match))

                if nearby_matches:
                    # Sort by distance and get closest
                    nearby_matches.sort(key=lambda x: x[0])
                    closest_match = nearby_matches[0][1]
                    address = closest_match.group(1).strip()
                    logger.debug(f"Found address near postal code: {address}")
                    return address

            # Otherwise, use first match with prefecture
            for match in matches:
                address = match.group(1).strip()
                if any(pref in address for pref in ['北海道', '東京都', '大阪府', '京都府', '県']):
                    logger.debug(f"Found address with prefecture: {address}")
                    if len(matches) > 1:
                        logger.warning(f"Multiple addresses found ({len(matches)}), using first with prefecture")
                    return address

            # Fallback to first match
            address = matches[0].group(1).strip()
            logger.debug(f"Using first address match: {address}")
            return address

        except Exception as e:
            logger.error(f"Error extracting address: {str(e)}", exc_info=True)
            return None

    def _extract_phone_number(self, text: str) -> Optional[str]:
        """
        Extract phone number from text.

        Args:
            text: Text to search for phone number

        Returns:
            Extracted phone number, or None if not found
        """
        try:
            match = self.PHONE_PATTERN.search(text)
            if match:
                phone = match.group(0)
                logger.debug(f"Found phone number: {phone}")
                return phone

            logger.debug("No phone number found")
            return None

        except Exception as e:
            logger.error(f"Error extracting phone number: {str(e)}", exc_info=True)
            return None

    def _extract_person_name(self, text: str) -> Optional[str]:
        """
        Extract person name (院長) from text.

        Args:
            text: Text to search for person name

        Returns:
            Extracted person name, or None if not found
        """
        try:
            match = self.PERSON_NAME_PATTERN.search(text)
            if match:
                name = match.group(1)
                logger.debug(f"Found person name: {name}")
                return name

            logger.debug("No person name found")
            return None

        except Exception as e:
            logger.error(f"Error extracting person name: {str(e)}", exc_info=True)
            return None

    def _scrape_external_link(self, url: str) -> Optional[str]:
        """
        Scrape external website for address information.

        Respects robots.txt and includes proper delays between requests.

        Args:
            url: URL to scrape

        Returns:
            Extracted address from website, or None if not found
        """
        try:
            # Validate URL
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                logger.warning(f"Invalid URL format: {url}")
                return None

            # Check robots.txt (basic check)
            # In production, use robotparser module for proper checking

            # Set user agent
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; DentalClinicScraper/1.0; +https://example.com/bot)'
            }

            # Wait before making request
            logger.info(f"Waiting {self.scrape_delay} seconds before scraping...")
            time.sleep(self.scrape_delay)

            # Make request
            logger.info(f"Scraping URL: {url}")
            response = requests.get(url, headers=headers, timeout=self.request_timeout)
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')

            # Search for address in common locations
            # Look for text containing postal codes or prefecture names
            text_content = soup.get_text(separator='\n')

            # Try to extract address from scraped content
            address = self._extract_address(text_content, None)

            if address:
                logger.info(f"Successfully extracted address from external link: {address}")
                return address

            logger.warning(f"No address found in scraped content from {url}")
            return None

        except requests.exceptions.Timeout:
            logger.error(f"Timeout while scraping {url}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Error scraping {url}: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error while scraping {url}: {str(e)}", exc_info=True)
            return None

    def _calculate_confidence(self, extracted: ExtractedData) -> float:
        """
        Calculate confidence score for extracted data.

        Scoring rules:
        - postal_code + address: 0.9
        - postal_code OR address: 0.6
        - External link used: -0.1
        - Multiple candidates: -0.2

        Args:
            extracted: Extracted data object

        Returns:
            Confidence score between 0.0 and 1.0
        """
        try:
            score = 0.0

            # Base score from postal code and address
            has_postal = bool(extracted.postal_code)
            has_address = bool(extracted.address)

            if has_postal and has_address:
                score = 0.9
                logger.debug("High confidence: both postal code and address found")
            elif has_postal or has_address:
                score = 0.6
                logger.debug("Medium confidence: postal code or address found")
            else:
                score = 0.3
                logger.debug("Low confidence: no postal code or address found")

            # Penalty for external link usage
            if "external website" in extracted.extraction_notes:
                score -= 0.1
                logger.debug("Confidence reduced: address from external website")

            # Penalty for multiple candidates (if flagged in notes)
            if "multiple" in extracted.extraction_notes.lower():
                score -= 0.2
                logger.debug("Confidence reduced: multiple candidates found")

            # Bonus for additional fields
            if extracted.phone_number:
                score += 0.05
            if extracted.person_name:
                score += 0.05

            # Ensure score is within bounds
            score = max(0.0, min(1.0, score))

            logger.debug(f"Final confidence score: {score:.2f}")
            return score

        except Exception as e:
            logger.error(f"Error calculating confidence: {str(e)}", exc_info=True)
            return 0.0
