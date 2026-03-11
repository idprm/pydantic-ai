from pydantic_ai import Embedder
import asyncio

embedder = Embedder('cohere:embed-v4.0')


async def main():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 1024

asyncio.run(main())