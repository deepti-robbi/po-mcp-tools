import logging
logger = logging.getLogger(__name__)

async def exercise_tips(patient_id: str, query: str) -> dict:
    """
    Lifestyle recommendation logic (CogniAuraFit)
    """
    logger.info(f"q={query}")
    q = query.lower()

    if "hypertension" in q:
        return {
            "condition": "hypertension",
            "exercise": ["walking", "light jogging", "yoga"],
            "duration": "30 mins daily",
            "intensity": "low to moderate",
            "note": "avoid high intensity workouts"
        }

    if "diabetes" in q:
        return {
            "condition": "diabetes",
            "exercise": ["brisk walking", "cycling", "strength training"],
            "duration": "45 mins daily",
            "intensity": "moderate"
        }

    return {
        "condition": "general",
        "exercise": ["walking", "stretching"],
        "duration": "30 mins daily"
    }