from mcp import types as mcp_types

from pydantic_ai.mcp import MCPServerSSE

server = MCPServerSSE(
    'http://localhost:3001/sse',
    client_info=mcp_types.Implementation(
        name='MyApplication',
        version='2.1.0',
    ),
)