from pydantic_ai import Embedder
from pydantic_ai.embeddings.bedrock import BedrockEmbeddingSettings

embedder = Embedder(
    'bedrock:amazon.nova-2-multimodal-embeddings-v1:0',
    settings=BedrockEmbeddingSettings(
        dimensions=1024,
        bedrock_nova_embedding_purpose='TEXT_RETRIEVAL',
        truncate=True,
    ),
)