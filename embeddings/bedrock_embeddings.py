from pydantic_ai import Embedder

# Using Amazon Titan
embedder = Embedder('bedrock:amazon.titan-embed-text-v2:0')


async def main():
    result = await embedder.embed_query('Hello world')
    print(len(result.embeddings[0]))
    #> 1024