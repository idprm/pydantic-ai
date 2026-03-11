from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerSSE

server = MCPServerSSE('http://localhost:3001/sse')  
agent = Agent('openai:gpt-5.2', toolsets=[server])  


async def main():
    result = await agent.run('What is 7 plus 5?')
    print(result.output)
    #> The answer is 12.