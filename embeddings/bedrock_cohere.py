from pydantic_ai import Embedder
from pydantic_ai.embeddings.bedrock import BedrockEmbeddingSettings

embedder = Embedder(
    'bedrock:cohere.embed-v4:0',
    settings=BedrockEmbeddingSettings(
        dimensions=512,
        bedrock_cohere_max_tokens=1000,
        bedrock_cohere_truncate='END',
    ),
)