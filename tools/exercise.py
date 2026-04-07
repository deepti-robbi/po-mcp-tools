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
             "exercise": {
      "aerobic": {
        "type": "Brisk walking / jogging / cycling / swimming",
        "duration": "30-45 minutes per day, at least 5 days a week",
        "intensity": "Moderate (50-70% of maximum heart rate, able to talk but not sing)"
      },
      "strength_training": {
        "type": "Light resistance or bodyweight exercises",
        "duration": "20-30 minutes, 2-3 times per week",
        "intensity": "Low to moderate (avoid heavy lifting or straining)"
      },
      "flexibility": {
        "type": "Stretching exercises",
        "duration": "10-15 minutes daily",
        "intensity": "Low (gentle stretching without discomfort)"
      }
    },
    "daily_yoga": [
      {
        "name": "Tadasana (Mountain Pose)",
        "duration": "5 minutes",
        "benefit": "Improves posture and promotes relaxation"
      },
      {
        "name": "Vrikshasana (Tree Pose)",
        "duration": "5 minutes",
        "benefit": "Enhances balance and focus, reduces stress"
      },
      {
        "name": "Bhujangasana (Cobra Pose)",
        "duration": "5 minutes",
        "benefit": "Improves blood circulation and reduces fatigue"
      },
      {
        "name": "Setu Bandhasana (Bridge Pose)",
        "duration": "5 minutes",
        "benefit": "Helps calm the brain and reduce blood pressure"
      },
      {
        "name": "Shavasana (Corpse Pose)",
        "duration": "10-15 minutes",
        "benefit": "Deep relaxation and stress reduction"
      },
      {
        "name": "Pranayama (Anulom Vilom, Bhramari)",
        "duration": "10-15 minutes",
        "benefit": "Regulates breathing and helps lower blood pressure"
      }
    ]
        }

    if "diabetes" in q:
        return {
            "condition": "diabetes",
"exercise": {
      "aerobic": {
        "type": "Brisk walking / cycling / swimming",
        "duration": "30-45 minutes per day",
        "intensity": "Moderate (50-70% of maximum heart rate, able to talk but not sing)"
      },
      "strength_training": {
        "type": "Bodyweight exercises or light weights",
        "duration": "20-30 minutes, 2-3 times per week",
        "intensity": "Moderate (8-12 repetitions per set, 2-3 sets)"
      },
      "flexibility": {
        "type": "Stretching exercises",
        "duration": "10-15 minutes daily",
        "intensity": "Low (gentle stretch without pain)"
      }
    },
    "daily_yoga": [
      {
        "name": "Surya Namaskar (Sun Salutation)",
        "duration": "10-15 minutes",
        "benefit": "Improves overall metabolism and blood circulation"
      },
      {
        "name": "Bhujangasana (Cobra Pose)",
        "duration": "5 minutes",
        "benefit": "Stimulates abdominal organs and pancreas"
      },
      {
        "name": "Dhanurasana (Bow Pose)",
        "duration": "5 minutes",
        "benefit": "Helps regulate blood sugar levels"
      },
      {
        "name": "Ardha Matsyendrasana (Seated Spinal Twist)",
        "duration": "5 minutes",
        "benefit": "Improves digestion and pancreatic function"
      },
      {
        "name": "Pranayama (Anulom Vilom, Kapalbhati)",
        "duration": "10-15 minutes",
        "benefit": "Reduces stress and improves oxygenation"
      }
    ]
        }

    return {
        "condition": "general",
        "exercise": ["walking", "stretching"],
        "duration": "30 mins daily"
    }