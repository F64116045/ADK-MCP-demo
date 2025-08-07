from google.adk.agents import LlmAgent
from multi_tool_agent.files_agent import get_files_tools
from multi_tool_agent.weather_agent import get_weather_tools

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="combined_agent",
    instruction="Help the user with weather information and file management",
    tools=get_files_tools() + get_weather_tools(),
)
