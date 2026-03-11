from pydantic_ai import Embedder
from pydantic_ai.embeddings import EmbeddingSettings
import asyncio

# Default settings for all calls
embedder = Embedder(
    'openai:text-embedding-3-small',
    settings=EmbeddingSettings(dimensions=512),
)


async def main():
    # Override for a specific call
    result = await embedder.embed_query(
        'Hello world',
        settings=EmbeddingSettings(dimensions=256),
    )
    print(len(result.embeddings[0]))
    #> 256

asyncio.run(main())