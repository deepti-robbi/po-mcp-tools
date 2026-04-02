from fastapi import FastAPI
# from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP
mcp = FastMCP("lifestylemcp")

# Add a simple tool to demonstrate the server
@mcp.tool()
def greet(name: str = "World") -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport='http', host="127.0.0.1", port=9002)
# from mcp.server.fastmcp import FastMCP
# from lifestyle_mcp_app.tools.exercise import exercise_tips

# mcp = FastMCP("lifestyle-mcp")

# mcp.tool()(exercise_tips)

# from fastmcp import FastMCP
# import logging
# logger = logging.getLogger(__name__)

# mcp = FastMCP(name="lifestyle-mcp")



# def exercise_tips(patient_id: str, query: str) -> dict:
#     """
#     Lifestyle recommendation logic (CogniAuraFit)
#     """
#     logger.info(f"q={query}")
#     q = query.lower()

#     if "hypertension" in q:
#         return {
#             "condition": "hypertension",
#             "exercise": ["walking", "light jogging", "yoga"],
#             "duration": "30 mins daily",
#             "intensity": "low to moderate",
#             "note": "avoid high intensity workouts"
#         }

#     if "diabetes" in q:
#         return {
#             "condition": "diabetes",
#             "exercise": ["brisk walking", "cycling", "strength training"],
#             "duration": "45 mins daily",
#             "intensity": "moderate"
#         }

#     return {
#         "condition": "general",
#         "exercise": ["walking", "stretching"],
#         "duration": "30 mins daily"
#     }

# if __name__ == "__main__":
#     # mcp.run()
#      mcp.run(transport="http", host="127.0.0.1", port=9002)