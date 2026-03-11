from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

server = MCPServerStdio('python', args=['mcp_server.py'], timeout=10)
agent = Agent('openai:gpt-5.2', toolsets=[server])


async def main():
    result = await agent.run('What is the weather in Paris?')
    print(result.output)
    #> The weather in Paris is sunny and 26 degrees Celsius.