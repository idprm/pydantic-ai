from pydantic_ai import Agent
from pydantic_ai.mcp import load_mcp_servers

import asyncio

# Load all servers from configuration file
servers = load_mcp_servers('mcp_config.json')

# Create agent with all loaded servers
agent = Agent('openai:gpt-5.2', toolsets=servers)

async def main():
    result = await agent.run('What is 7 plus 5?')
    print(result.output)

asyncio.run(main())