from fastapi import FastAPI
from fastmcp import FastMCP
from tools.exercise import exercise_tips
from tools.greet import greet
from tools.diet import diet_tips
from tools.general import general_tips
mcp = FastMCP("CogniAuraFit")

# Register tool
mcp.tool()(exercise_tips)
mcp.tool()(diet_tips)
mcp.tool()(general_tips)
mcp.tool()(greet)