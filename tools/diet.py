import logging
logger = logging.getLogger(__name__)

async def diet_tips(patient_id: str, query: str) -> dict:
    """
    Lifestyle recommendation logic (CogniAuraFit)
    """
    logger.info(f"q={query}")
    q = query.lower()

    if "hypertension" in q:
        return {
            "condition": "hypertension",
             "diet": {
      "recommended": [
        "Fruits such as bananas, oranges, apples, and berries",
        "Vegetables, especially leafy greens like spinach and kale",
        "Whole grains such as brown rice, oats, and whole wheat",
        "Low-fat dairy products",
        "Lean proteins like fish, chicken, legumes, and nuts",
        "Foods rich in potassium, magnesium, and fiber"
      ],
      "avoid": [
        "High-sodium foods (processed foods, canned soups, packaged snacks)",
        "Pickles and salty condiments",
        "Fried and fatty foods",
        "Red meat in excess",
        "Sugary beverages and excessive caffeine"
      ]
        }
        }

    if "diabetes" in q:
        return {
            "condition": "diabetes",
            "diet": {
      "recommended": [
        "Whole grains such as brown rice, oats, and whole wheat",
        "High-fiber foods like legumes, beans, and vegetables",
        "Leafy greens such as spinach, kale, and methi",
        "Lean proteins like eggs, fish, tofu, and legumes",
        "Healthy fats from nuts, seeds, and olive oil",
        "Low glycemic index fruits like apple, pear, and berries"
      ],
      "avoid": [
        "Refined sugars and sweets (cakes, pastries, sugary drinks)",
        "Highly processed foods",
        "White bread, white rice, and refined flour products",
        "Fried and high-fat foods",
        "Sugary beverages and packaged juices"
      ]}
        }
    
    if "sore throat" in q:
        return {
            "condition": "sore throat",
            "diet": {
      "recommended": [
        "Warm soups such as vegetable or chicken broth",
        "Soft foods like khichdi, oatmeal, and mashed vegetables",
        "Honey (for soothing effect, not for infants)",
        "Ginger and turmeric-based drinks",
        "Herbal teas like chamomile or tulsi"
      ],
      "avoid": [
        "Spicy and fried foods",
        "Cold beverages and ice cream",
        "Citrus fruits if they irritate the throat",
        "Hard or crunchy foods"
      ]
    }
        }

    return {
        "condition": "general",
        "exercise": ["walking", "stretching"],
        "duration": "30 mins daily"
    }