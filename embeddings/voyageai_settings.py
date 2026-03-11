from pydantic_ai import Embedder
from pydantic_ai.embeddings.voyageai import VoyageAIEmbeddingSettings

embedder = Embedder(
    'voyageai:voyage-3.5',
    settings=VoyageAIEmbeddingSettings(
        dimensions=512,  # Reduce output dimensions
        voyageai_input_type='document',  # Override input type for all requests
    ),
)