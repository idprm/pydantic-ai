from datetime import timezone
import pytest

from dirty_equals import IsNow, IsStr

from pydantic_ai import models, capture_run_messages, RequestUsage
from pydantic_ai.models.test import TestModel
from pydantic_ai import (
    ModelResponse,
    TextPart,
    ToolCallPart,
    ToolReturnPart,
    UserPromptPart,
    ModelRequest,
)

from fake_database import DatabaseConn
from weather_app import run_weather_forecast, weather_agent

pytestmark = pytest.mark.anyio  
models.ALLOW_MODEL_REQUESTS = False  


async def test_forecast():
    conn = DatabaseConn()
    user_id = 1
    with capture_run_messages() as messages:
        with weather_agent.override(model=TestModel()):  
            prompt = 'What will the weather be like in London on 2024-11-28?'
            await run_weather_forecast([(prompt, user_id)], conn)  

    forecast = await conn.get_forecast(user_id)
    assert forecast == '{"weather_forecast":"Sunny with a chance of rain"}'  

    assert messages == [  
        ModelRequest(
            parts=[
                UserPromptPart(
                    content='What will the weather be like in London on 2024-11-28?',
                    timestamp=IsNow(tz=timezone.utc),  
                ),
            ],
            instructions='Providing a weather forecast at the locations the user provides.',
            timestamp=IsNow(tz=timezone.utc),
            run_id=IsStr(),
        ),
        ModelResponse(
            parts=[
                ToolCallPart(
                    tool_name='weather_forecast',
                    args={
                        'location': 'a',
                        'forecast_date': '2024-01-01',  
                    },
                    tool_call_id=IsStr(),
                )
            ],
            usage=RequestUsage(
                input_tokens=60,
                output_tokens=7,
            ),
            model_name='test',
            timestamp=IsNow(tz=timezone.utc),
            run_id=IsStr(),
        ),
        ModelRequest(
            parts=[
                ToolReturnPart(
                    tool_name='weather_forecast',
                    content='Sunny with a chance of rain',
                    tool_call_id=IsStr(),
                    timestamp=IsNow(tz=timezone.utc),
                ),
            ],
            instructions='Providing a weather forecast at the locations the user provides.',
            timestamp=IsNow(tz=timezone.utc),
            run_id=IsStr(),
        ),
        ModelResponse(
            parts=[
                TextPart(
                    content='{"weather_forecast":"Sunny with a chance of rain"}',
                )
            ],
            usage=RequestUsage(
                input_tokens=66,
                output_tokens=16,
            ),
            model_name='test',
            timestamp=IsNow(tz=timezone.utc),
            run_id=IsStr(),
        ),
    ]