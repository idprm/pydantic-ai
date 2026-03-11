from pydantic_ai import Agent
from pydantic_ai.models.xai import XaiModel, XaiModelSettings

model = XaiModel('grok-4-fast-reasoning')
settings = XaiModelSettings(xai_include_encrypted_content=True)
agent = Agent(model, model_settings=settings)