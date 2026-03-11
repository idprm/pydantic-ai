from pydantic_ai.mcp import MCPServerStdio

server = MCPServerStdio(
    'python',
    args=['generate_svg.py'],
    allow_sampling=False,
)