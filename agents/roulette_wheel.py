import os
import logfire

from pydantic_ai import Agent, RunContext
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

logfire.configure()  
logfire.instrument_pydantic_ai() 

provider = GoogleProvider(api_key=os.getenv("GOOGLE_API_KEY"))
model = GoogleModel('gemini-2.5-flash-lite', provider=provider)

roulette_agent = Agent(  
    model=model,
    deps_type=int,
    output_type=bool,
    system_prompt=(
        'Use the `roulette_wheel` function to see if the '
        'customer has won based on the number they provide.'
    ),
)


@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:  
    """check if the square is a winner"""
    return 'winner' if square == ctx.deps else 'loser'


# Run the agent
success_number = 18  
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.output)  
#> True

result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.output)
#> False