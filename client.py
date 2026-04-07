import asyncio
import json
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

#python client.py

async def mainex():
   transprt = StreamableHttpTransport("http://127.0.0.1:9002/mcp")
   async with Client(transport=transprt) as client:
       await client.ping()
       print("ping rcvd")

       tool_list  = await client.list_tools()
       print(f"available tools:{tool_list}")
       greeting = await client.call_tool("greet",{"name":"Deepti"})
       result = json.dumps(greeting.structured_content)
       print(f"greeting:{result}")
       print("==================")
       excercisetips = await client.call_tool("exercise_tips",
                                              {"patient_id":"c947658d-b047-4ec0-96f1-2d8ef2f78cc6",
                                               "query":"hypertension"})
       result = json.dumps(excercisetips.structured_content)
       print(f"excercisetips:{result}")
       


async def lifestyle_client():
    transport = StreamableHttpTransport("http://127.0.0.1:9002/mcp")

    async with Client(transport=transport) as client:
        await client.ping()
        print("ping received")

        condition = "hypertension"   # 🔑 single source of truth

        # -------------------------------
        # Call all tools in parallel
        # -------------------------------
        general_task = client.call_tool(
            "general_tips",
            {"patient_id":"c947658d-b047-4ec0-96f1-2d8ef2f78cc6","query": condition}
        )

        diet_task = client.call_tool(
            "diet_tips",
            {"patient_id":"c947658d-b047-4ec0-96f1-2d8ef2f78cc6","query": condition}
        )

        exercise_task = client.call_tool(
            "exercise_tips",
            {
                "patient_id": "c947658d-b047-4ec0-96f1-2d8ef2f78cc6",
                "query": condition
            }
        )

        # Await all
        general_res, diet_res, exercise_res = await asyncio.gather(
            general_task, diet_task, exercise_task
        )

        # -------------------------------
        # Extract structured content safely
        # -------------------------------
        def extract(result):
            if result and result.structured_content:
                return result.structured_content.get("result", result.structured_content)
            return {}

        general_data = extract(general_res)
        diet_data = extract(diet_res)
        exercise_data = extract(exercise_res)

        # -------------------------------
        # Consolidated Response
        # -------------------------------
        consolidated = {
            "condition": condition,
            "recommendations": {
                "general_tips": general_data,
                "diet": diet_data,
                "exercise": exercise_data
            }
        }

        print("\n===== CONSOLIDATED OUTPUT =====")
        print(json.dumps(consolidated, indent=2))

if __name__ == "__main__":
    # asyncio.run(mainex())
    asyncio.run(lifestyle_client())