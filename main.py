from server import mcp

#Mcp server: fastmcp run main.py --transport http --host 127.0.0.1 --port 9002

if __name__ == "__main__":
    mcp.run(transport='http', host="127.0.0.1", port=9002)