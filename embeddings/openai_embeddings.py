from pydantic_ai import Embedder
import asyncio

embedder = Embedder('openai:text-embedding-3-small')


async def main():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 1536

asyncio.run(main())