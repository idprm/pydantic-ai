from pydantic_ai import Embedder
import asyncio

embedder = Embedder('openai:text-embedding-3-small')


async def main():
    # Embed a search query
    result = await embedder.embed_query('What is machine learning?')
    print(f'Embedding dimensions: {len(result.embeddings[0])}')
    #> Embedding dimensions: 1536

    # Embed multiple documents at once
    docs = [
        'Machine learning is a subset of AI.',
        'Deep learning uses neural networks.',
        'Python is a programming language.',
    ]
    result = await embedder.embed_documents(docs)
    print(f'Embedded {len(result.embeddings)} documents')
    #> Embedded 3 documents

asyncio.run(main())