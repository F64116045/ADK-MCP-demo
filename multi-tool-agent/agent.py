import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/home/eason/ADK/multi-tool-agent/files")

toolset = MCPToolset(
    connection_params=StdioServerParameters(
        command='npx',
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            os.path.abspath(TARGET_FOLDER_PATH),
        ],
    ),
)

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='filesystem_assistant_agent',
    instruction=(
        "Help the user manage their files. You can list files, read files, etc., "
        "but you must never read or reveal the contents of the file named 'sample.txt'."
    ),
    tools=[toolset],
)


