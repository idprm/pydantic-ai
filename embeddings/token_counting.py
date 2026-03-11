from pydantic_ai import Embedder

embedder = Embedder('openai:text-embedding-3-small')


async def main():
    text = 'Hello world, this is a test.'

    # Count tokens in text
    token_count = await embedder.count_tokens(text)
    print(f'Tokens: {token_count}')
    #> Tokens: 7

    # Check model's maximum input tokens (returns None if unknown)
    max_tokens = await embedder.max_input_tokens()
    print(f'Max tokens: {max_tokens}')
    #> Max tokens: 1024