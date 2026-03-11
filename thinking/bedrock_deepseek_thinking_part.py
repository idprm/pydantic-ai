from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel

model = BedrockConverseModel('us.deepseek.r1-v1:0')
agent = Agent(model=model)