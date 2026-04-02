import asyncio
import json
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

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
       

if __name__ == "__main__":
    asyncio.run(mainex())