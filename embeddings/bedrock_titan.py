from pydantic_ai import Embedder
from pydantic_ai.embeddings.bedrock import BedrockEmbeddingSettings

embedder = Embedder(
    'bedrock:amazon.titan-embed-text-v2:0',
    settings=BedrockEmbeddingSettings(
        dimensions=512,
        bedrock_titan_normalize=True,
    ),
)