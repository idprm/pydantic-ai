import time
from pydantic_ai import Agent
from pydantic_ai import ToolReturn, BinaryContent

agent = Agent('openai:gpt-5-mini')

@agent.tool_plain
def click_and_capture(x: int, y: int) -> ToolReturn:
    """Click at coordinates and show before/after screenshots."""
    # Take screenshot before action
    before_screenshot = capture_screen()

    # Perform click operation
    perform_click(x, y)
    time.sleep(0.5)  # Wait for UI to update

    # Take screenshot after action
    after_screenshot = capture_screen()

    return ToolReturn(
        return_value=f'Successfully clicked at ({x}, {y})',
        content=[
            f'Clicked at coordinates ({x}, {y}). Here\'s the comparison:',
            'Before:',
            BinaryContent(data=before_screenshot, media_type='image/png'),
            'After:',
            BinaryContent(data=after_screenshot, media_type='image/png'),
            'Please analyze the changes and suggest next steps.'
        ],
        metadata={
            'coordinates': {'x': x, 'y': y},
            'action_type': 'click_and_capture',
            'timestamp': time.time()
        }
    )

# The model receives the rich visual content for analysis
# while your application can access the structured return_value and metadata
result = agent.run_sync('Click on the submit button and tell me what happened')
print(result.output)
# The model can analyze the screenshots and provide detailed feedback