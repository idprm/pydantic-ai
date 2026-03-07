import os
import logfire

from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

logfire.configure()  
logfire.instrument_pydantic_ai() 

provider = GoogleProvider(api_key=os.getenv("GOOGLE_API_KEY"))
model = GoogleModel('gemini-2.5-flash-lite', provider=provider)
agent = Agent(model)

result = agent.run_sync('Where does "hello world" come from?')  
print(result.output)
"""
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
"""