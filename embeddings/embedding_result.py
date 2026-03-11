from pydantic_ai import Embedder
import asyncio

embedder = Embedder('openai:text-embedding-3-small')


async def main():
    result = await embedder.embed_query('Hello world')

    # Access embeddings - each is a sequence of floats
    embedding = result.embeddings[0]  # By index via .embeddings
    embedding = result[0]  # Or directly via __getitem__
    embedding = result['Hello world']  # Or by original input text
    print(f'Dimensions: {len(embedding)}')
    #> Dimensions: 1536

    # Check usage
    print(f'Tokens used: {result.usage.input_tokens}')
    #> Tokens used: 2

    # Calculate cost (requires `genai-prices` to have pricing data for the model)
    cost = result.cost()
    print(f'Cost: ${cost.total_price:.6f}')
    #> Cost: $0.000000

asyncio.run(main())