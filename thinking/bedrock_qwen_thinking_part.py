from pydantic_ai import Agent
from pydantic_ai.models.bedrock import BedrockConverseModel, BedrockModelSettings

model = BedrockConverseModel('qwen.qwen3-32b-v1:0')
model_settings = BedrockModelSettings(
    bedrock_additional_model_requests_fields={'reasoning_config': 'high'}
)
agent = Agent(model=model, model_settings=model_settings)