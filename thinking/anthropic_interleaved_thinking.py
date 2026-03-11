from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel, AnthropicModelSettings

model = AnthropicModel('claude-sonnet-4-5')
settings = AnthropicModelSettings(
    anthropic_thinking={'type': 'enabled', 'budget_tokens': 10000},
    extra_headers={'anthropic-beta': 'interleaved-thinking-2025-05-14'},
)
agent = Agent(model, model_settings=settings)
