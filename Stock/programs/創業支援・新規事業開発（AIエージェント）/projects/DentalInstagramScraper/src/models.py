"""
Data models for Instagram dental clinic scraper.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class InstagramProfile:
    """Instagram profile data."""
    username: str
    full_name: str
    bio: str
    external_url: Optional[str] = None
    followers_count: int = 0
    following_count: int = 0
    posts_count: int = 0


@dataclass
class ExtractedData:
    """Extracted clinic data."""
    clinic_name: str
    postal_code: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    person_name: Optional[str] = None
    external_link: Optional[str] = None
    confidence: float = 0.0
    needs_manual_review: bool = False
    extraction_notes: str = ""


@dataclass
class FactCheckResult:
    """Fact check verification result."""
    status: str  # "verified", "partial", "failed"
    verified_address: Optional[str] = None
    similarity_score: float = 0.0
    search_query: str = ""
    sources: list[str] = None
    verification_notes: str = ""

    def __post_init__(self):
        if self.sources is None:
            self.sources = []


@dataclass
class FinalOutput:
    """Final merged output data."""
    clinic_name: str
    postal_code: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    person_name: Optional[str] = None
    external_link: Optional[str] = None
    confidence: float = 0.0
    verification_status: str = "unverified"
    needs_manual_review: bool = False
    notes: str = ""


@dataclass
class FinalRecord:
    """Final record for CSV export."""
    instagram_handle: str
    clinic_name: Optional[str] = None
    postal_code: Optional[str] = None
    address: Optional[str] = None
    extracted_person_name: Optional[str] = None
    external_link_url: Optional[str] = None
    phone_number: Optional[str] = None
    follower_count: int = 0
    bio_text: Optional[str] = None
    fact_check_status: Optional[str] = None
    fact_check_confidence: Optional[float] = None
    verified_address: Optional[str] = None
    verification_source: Optional[str] = None
    needs_manual_review: bool = False
    collected_at: Optional[str] = None
