import logging
logger = logging.getLogger(__name__)

async def general_tips(patient_id: str, query: str) -> dict:
    """
    Lifestyle recommendation logic (CogniAuraFit)
    """
    logger.info(f"q={query}")
    q = query.lower()

    if "hypertension" in q:
        return {
            "condition": "hypertension",
            "general_tips": [
      "Monitor blood pressure regularly and maintain a log",
      "Take prescribed medications consistently as directed",
      "Reduce stress through relaxation techniques such as meditation or deep breathing",
      "Limit salt (sodium) intake in daily meals",
      "Maintain a healthy body weight",
      "Avoid smoking and limit alcohol consumption",
      "Ensure adequate sleep (7-8 hours per night)"
    ],
        }

    if "diabetes" in q:
        return {
            "condition": "diabetes",
            "general_tips": [
      "Monitor blood glucose levels regularly as advised by a healthcare provider",
      "Maintain a consistent daily routine for meals and physical activity",
      "Adhere strictly to prescribed medications or insulin therapy",
      "Manage stress through relaxation techniques like meditation or breathing exercises",
      "Ensure adequate sleep (7-8 hours per night)",
      "Avoid smoking and limit alcohol consumption"
    ]
        }
    
    if "sore throat" in q:
        return {
            "condition": "sore throat",
            "general_tips": [
                "Stay well hydrated with warm fluids like water, herbal teas, and broths",
                "Gargle with warm salt water 2-3 times a day",
                "Take adequate rest to support immune recovery",
                "Use steam inhalation or a humidifier to keep air moist",
                "Avoid smoking and exposure to irritants",
                "Limit talking to reduce throat strain"
                ]
        }

    return {
        "condition": "general",
        "exercise": ["walking", "stretching"],
        "duration": "30 mins daily"
    }