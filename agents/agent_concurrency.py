import asyncio

from pydantic_ai import Agent, ConcurrencyLimit

# Simple limit: allow up to 10 concurrent runs
agent = Agent('gemini-2.5-flash-lite', max_concurrency=10)


# With backpressure: limit concurrent runs and queue depth
agent_with_backpressure = Agent(
    'gemini-2.5-flash-lite',
    max_concurrency=ConcurrencyLimit(max_running=10, max_queued=100),
)


async def main():
    # These will be rate-limited to 10 concurrent runs
    results = await asyncio.gather(
        *[agent.run(f'Question {i}') for i in range(20)]
    )
    print(len(results))
    #> 20