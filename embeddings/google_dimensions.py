from pydantic_ai import Embedder
from pydantic_ai.embeddings import EmbeddingSettings
import asyncio


embedder = Embedder(
    'google-gla:gemini-embedding-001',
    settings=EmbeddingSettings(dimensions=768),
)


async def main():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 768

asyncio.run(main())