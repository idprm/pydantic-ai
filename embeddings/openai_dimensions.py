from pydantic_ai import Embedder
from pydantic_ai.embeddings import EmbeddingSettings
import asyncio

embedder = Embedder(
    'openai:text-embedding-3-small',
    settings=EmbeddingSettings(dimensions=256),
)


async def main():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 256

asyncio.run(main())