import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

def get_weather_tools():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    WEATHER_SERVER_PATH = os.path.join(BASE_DIR, "weather", "weather.py")
    toolset = MCPToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="uv",
                args=[
                    "run",
                    WEATHER_SERVER_PATH,
                ],
            ),
        ),
    )
    return [toolset]
