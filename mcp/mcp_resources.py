import asyncio

from pydantic_ai.mcp import MCPServerStdio


async def main():
    server = MCPServerStdio('python', args=['-m', 'mcp_resource_server'])

    async with server:
        # List all available resources
        resources = await server.list_resources()
        for resource in resources:
            print(f' - {resource.name}: {resource.uri} ({resource.mime_type})')
            #>  - user_name_resource: resource://user_name.txt (text/plain)

        # Read a text resource
        user_name = await server.read_resource('resource://user_name.txt')
        print(f'Text content: {user_name}')
        #> Text content: Alice


if __name__ == '__main__':
    asyncio.run(main())