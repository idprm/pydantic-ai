from pydantic_ai import Embedder
import asyncio

# Model is downloaded from Hugging Face on first use
embedder = Embedder('sentence-transformers:all-MiniLM-L6-v2')


async def main():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 384

asyncio.run(main()) 