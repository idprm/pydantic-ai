from dataclasses import dataclass

import httpx
import asyncio

from pydantic_ai import Agent, RunContext


@dataclass
class MyDeps:
    api_key: str
    http_client: httpx.AsyncClient


agent = Agent(
    'gemini-2.5-flash-lite',
    deps_type=MyDeps,
)


@agent.system_prompt  
async def get_system_prompt(ctx: RunContext[MyDeps]) -> str:  
    response = await ctx.deps.http_client.get(  
        'https://google.com',
        headers={'Authorization': f'Bearer {ctx.deps.api_key}'},  
    )
    response.raise_for_status()
    return f'Prompt: {response.text}'


async def main():
    async with httpx.AsyncClient() as client:
        deps = MyDeps('foobar', client)
        result = await agent.run('Tell me a joke.', deps=deps)
        print(result.output)
        #> Did you hear about the toothpaste scandal? They called it Colgate.

asyncio.run(main())