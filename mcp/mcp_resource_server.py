from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Pydantic AI MCP Server')
log_level = 'unset'


@mcp.resource('resource://user_name.txt', mime_type='text/plain')
async def user_name_resource() -> str:
    return 'Alice'


if __name__ == '__main__':
    mcp.run()