# AI Stock Agents - AI Timeline & AMPI Calculation Tools

from langchain_core.tools import tool
from typing import Annotated
import json
import math
from datetime import datetime
from pathlib import Path


@tool
def calculate_ampi(
    ticker: Annotated[str, "ticker symbol of the company"],
    current_date: Annotated[str, "current analysis date in yyyy-mm-dd format"],
) -> str:
    """
    Calculate AI Milestone Proximity Index (AMPI) for a given stock.

    AMPI measures how close we are to major AI technology milestones (GPT-5, AGI, etc.)
    and weights them by the company's relevance to each milestone.

    Formula:
        For each milestone:
            proximity_score = 100 * exp(-days_to_milestone / 180)  # 180-day half-life
            weighted_score = proximity_score * milestone_weight * company_relevance
        AMPI = sum(weighted_scores), capped at 100

    Interpretation:
    - AMPI ≥ 80: Strong buying signal (milestone within ~30 days)
    - AMPI 50-80: Moderate proximity (milestone 60-120 days)
    - AMPI < 50: Low influence (milestone >120 days)

    Args:
        ticker: Stock symbol (e.g., "MSFT", "NVDA", "GOOGL")
        current_date: Analysis date in yyyy-mm-dd format

    Returns:
        str: JSON string with AMPI score, contributing milestones, and interpretation
    """
    # Load AI milestones data
    data_dir = Path(__file__).parent.parent.parent / "data"
    timeline_file = data_dir / "ai_milestones.json"

    try:
        with open(timeline_file, "r") as f:
            timeline_data = json.load(f)
    except FileNotFoundError:
        return json.dumps({
            "error": f"AI milestones file not found at {timeline_file}",
            "ampi_score": 0
        })

    milestones = timeline_data.get("milestones", [])
    company_relevance = timeline_data.get("company_relevance", {}).get(ticker.upper(), {})

    # Parse current date
    current_date_obj = datetime.strptime(current_date, "%Y-%m-%d")

    # Calculate AMPI
    total_score = 0
    milestone_contributions = []
    half_life_days = 180  # 6 months

    for milestone in milestones:
        milestone_name = milestone["name"]
        milestone_date_str = milestone["date"]
        milestone_weight = milestone.get("weight", 1.0)

        # Parse milestone date
        milestone_date = datetime.strptime(milestone_date_str, "%Y-%m-%d")

        # Calculate days to milestone
        days_to_milestone = (milestone_date - current_date_obj).days

        # Skip past milestones
        if days_to_milestone < 0:
            continue

        # Calculate proximity score (exponential decay)
        proximity_score = 100 * math.exp(-days_to_milestone / half_life_days)

        # Get company relevance (default 0.5 if not specified)
        relevance = company_relevance.get(milestone_name, 0.5)

        # Calculate weighted score
        weighted_score = proximity_score * milestone_weight * relevance

        total_score += weighted_score

        milestone_contributions.append({
            "milestone": milestone_name,
            "date": milestone_date_str,
            "days_away": days_to_milestone,
            "proximity_score": round(proximity_score, 2),
            "company_relevance": relevance,
            "weighted_contribution": round(weighted_score, 2)
        })

    # Cap AMPI at 100
    ampi_score = min(total_score, 100)

    # Determine signal
    if ampi_score >= 80:
        signal = "STRONG_BUY"
        interpretation = "Very high milestone proximity. Major AI breakthrough imminent."
    elif ampi_score >= 50:
        signal = "MODERATE"
        interpretation = "Moderate milestone proximity. AI developments approaching."
    else:
        signal = "LOW_IMPACT"
        interpretation = "Low milestone proximity. AI timeline events distant."

    # Sort contributions by weighted_contribution (descending)
    milestone_contributions.sort(key=lambda x: x["weighted_contribution"], reverse=True)

    result = {
        "ticker": ticker.upper(),
        "analysis_date": current_date,
        "ampi_score": round(ampi_score, 2),
        "signal": signal,
        "interpretation": interpretation,
        "top_milestones": milestone_contributions[:3],  # Top 3 contributors
        "all_milestones": milestone_contributions
    }

    return json.dumps(result, indent=2)


@tool
def get_next_milestone(
    current_date: Annotated[str, "current analysis date in yyyy-mm-dd format"],
) -> str:
    """
    Get the next upcoming AI milestone.

    Args:
        current_date: Current date in yyyy-mm-dd format

    Returns:
        str: JSON string with next milestone info
    """
    # Load AI milestones data
    data_dir = Path(__file__).parent.parent.parent / "data"
    timeline_file = data_dir / "ai_milestones.json"

    try:
        with open(timeline_file, "r") as f:
            timeline_data = json.load(f)
    except FileNotFoundError:
        return json.dumps({"error": "AI milestones file not found"})

    milestones = timeline_data.get("milestones", [])

    # Parse current date
    current_date_obj = datetime.strptime(current_date, "%Y-%m-%d")

    # Find next milestone
    upcoming_milestones = []

    for milestone in milestones:
        milestone_date = datetime.strptime(milestone["date"], "%Y-%m-%d")
        days_to_milestone = (milestone_date - current_date_obj).days

        if days_to_milestone >= 0:  # Future milestone
            upcoming_milestones.append({
                "name": milestone["name"],
                "date": milestone["date"],
                "days_away": days_to_milestone,
                "description": milestone.get("description", "")
            })

    # Sort by days_away
    upcoming_milestones.sort(key=lambda x: x["days_away"])

    if upcoming_milestones:
        next_milestone = upcoming_milestones[0]
        return json.dumps({
            "next_milestone": next_milestone["name"],
            "date": next_milestone["date"],
            "days_away": next_milestone["days_away"],
            "description": next_milestone["description"],
            "all_upcoming": upcoming_milestones[:5]  # Next 5 milestones
        }, indent=2)
    else:
        return json.dumps({"message": "No upcoming milestones found"})
