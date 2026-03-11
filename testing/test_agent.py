import pytest

from pydantic_ai.models.test import TestModel

from weather_app import weather_agent


@pytest.fixture
def override_weather_agent():
    with weather_agent.override(model=TestModel()):
        yield


async def test_forecast(override_weather_agent: None):
    ...
    # test code here