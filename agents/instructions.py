from datetime import date

from pydantic_ai import Agent, RunContext

agent = Agent(
    'gemini-2.5-flash-lite',
    deps_type=str,  
    instructions="Use the customer's name while replying to them.",  
)


@agent.instructions  
def add_the_users_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}."


@agent.instructions
def add_the_date() -> str:  
    return f'The date is {date.today()}.'


result = agent.run_sync('What is the date?', deps='Frank')
print(result.output)
#> Hello Frank, the date today is 2032-01-02.