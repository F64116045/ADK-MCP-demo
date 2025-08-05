# ADK-MCP-demo
Practice project for integrating ADK(Agent Development Kit) as an MCP(Model Context Protocol) client connecting to a local MCP server.

# ADK multi tool agent 
## Introduction  
使用 Google 的 Agent Development Kit（**ADK**）開發，結合 **MCP**（Model Context Protocol，包括：

- **File System MCP Server**
- **Weather MCP Server**

可以讓 LLM Agent 去 Access 檔案系統跟打Weather API
(Execution and environment management is done through the **uv** tool.)

## Project Structure
multi-tool-agent/
├── init.py
├── agent.py # ADK 入口
├── files_agent.py # MCP Files System Agent
├── weather_agent.py # MCP Weather Agent
├── files/ # MCP Server 讀取的檔案資料夾
│ └── sample.txt
├── weather/
│ ├── weather.py # Weather MCP Server  (providing weather API tools)
│ └── main.py
└── pycache/ 

## Environment Setup
### Prerequisites  
- 已安裝 [**uv** 工具]
- Python 3.9 以上版本

### Installation Steps

1. 進入 project directory：

```bash
cd /path/to/your/ADK/
```
2. 使用 uv 安裝 google-adk 及 MCP CLI、httpx
```bash
uv pip install google-adk
uv add "mcp[cli]" httpx
```

## Running the Project
確保在 /ADK directory下
```bash
adk web
```
Open the provided URL (usually http://localhost:8000) in your browser and select your agent to start interacting.


## Problem (Solved)
[WIP] _load_from_yaml_config is not ready for use
代表 agent 加載設定錯誤，通常是因為 agent.py 缺失或路徑錯誤，確認在專案根目錄執行且存在 agent.py。
agent.py 是 ADK Agent 入口檔，如果缺少就會 [WIP] _load_from_yaml_config is not ready for use。

## References
Google ADK - MCP tools
https://google.github.io/adk-docs/tools/mcp-tools/

MCP Protocol Documentation
https://modelcontextprotocol.io/quickstart/server

