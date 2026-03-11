from pydantic_ai import Embedder
from pydantic_ai.embeddings.bedrock import BedrockEmbeddingSettings

# Increase concurrency for faster throughput
embedder = Embedder(
    'bedrock:amazon.titan-embed-text-v2:0',
    settings=BedrockEmbeddingSettings(bedrock_max_concurrency=10),
)

# Or reduce concurrency to avoid rate limits
embedder = Embedder(
    'bedrock:amazon.nova-2-multimodal-embeddings-v1:0',
    settings=BedrockEmbeddingSettings(bedrock_max_concurrency=2),
)