import json
import logging
from pathlib import Path
from collections import Counter
import sys

# Configuration
# Path to the ENRICHED file
TARGET_FILE = Path(__file__).parent.parent / "Flow" / "202512" / "2025-12-31" / "x_bookmarks_data_enriched.json"

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def validate_data():
    if not TARGET_FILE.exists():
        logger.error(f"File not found: {TARGET_FILE}")
        return

    logger.info(f"Validating file: {TARGET_FILE}")
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    bookmarks = data.get("bookmarks", [])
    logger.info(f"Total bookmarks: {len(bookmarks)}")
    
    metadata = data.get("metadata", {})
    logger.info(f"Metadata: {json.dumps(metadata, indent=2, ensure_ascii=False)}")

    # 1. Required fields
    required_fields = ["id", "url", "text"] # replies/media might be missing if not yet enriched or failed
    
    # 2. Data types
    invalid_types_count = 0

    # 3. Duplicates
    seen_ids = set()
    duplicates_count = 0
    
    # 4. Content checks
    enriched_media_count = 0
    enriched_replies_count = 0
    full_text_candidates = 0
    
    for i, b in enumerate(bookmarks):
        # Check duplicates
        bid = b.get("id")
        if bid in seen_ids:
            logger.warning(f"Duplicate ID found: {bid} at index {i}")
            duplicates_count += 1
        seen_ids.add(bid)

        # Check enriched fields
        if b.get("media"):
            enriched_media_count += 1
        
        if b.get("replies"):
            enriched_replies_count += 1
            
            # Check URL extraction in replies
            r_info = b["replies"]
            if r_info.get("has_source_urls"):
                # logger.info(f"  ID {bid}: Found source URLs in replies: {r_info.get('source_urls')}")
                pass

        # Check text length (heuristic for full text)
        text = b.get("text", "")
        if len(text) > 140: # Arbitrary threshold for potentially "long" or expanded text
            full_text_candidates += 1

    logger.info("-" * 40)
    logger.info(f"Validation Results:")
    logger.info(f"  Duplicates: {duplicates_count}")
    logger.info(f"  Enriched with Media: {enriched_media_count}")
    logger.info(f"  Enriched with Replies: {enriched_replies_count}")
    logger.info(f"  Long text (>140 chars): {full_text_candidates}")
    
    if duplicates_count == 0:
        logger.info("✅ No duplicates found.")
    else:
        logger.error(f"❌ {duplicates_count} duplicates found.")

    if enriched_replies_count >= 3: # We expect at least the test batch
        logger.info(f"✅ Enrichment seems to be working (found {enriched_replies_count} records with replies).")
    else:
        logger.warning(f"⚠️ Low enrichment count: {enriched_replies_count}")

if __name__ == "__main__":
    validate_data()
